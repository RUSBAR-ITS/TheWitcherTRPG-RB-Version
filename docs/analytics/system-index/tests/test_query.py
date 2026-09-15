"""Проверки CLI и отдельного временного набора; игровой код не исполняется."""

from copy import deepcopy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


# Loading the tool must not leave bytecode in the repository.
sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parents[2]
spec = importlib.util.spec_from_file_location("system_index_query", BASE / "query.py")
query = importlib.util.module_from_spec(spec)
spec.loader.exec_module(query)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run_cli(arguments, cwd=ROOT):
    return subprocess.run([sys.executable, "-B", str(BASE / "query.py"), *arguments],
                          cwd=cwd, text=True, capture_output=True, timeout=20)


def source_hash(root, rows):
    h = hashlib.sha256()
    for row in sorted(rows, key=lambda x: x["path"]):
        h.update(row["path"].encode() + b"\0" + (root / row["path"]).read_bytes())
    return h.hexdigest()


def seed_view():
    """Reconstruct the .001 seed without duplicating the full source catalogue."""
    manifest = json.loads((BASE / "manifest.json").read_text())
    rows = {kind: [json.loads(s) for s in (BASE / "examples" / (kind + ".jsonl")).read_text().splitlines()]
            for kind in ("entities", "relations", "processes")}
    rows["sources"] = [json.loads(s) for s in (BASE / "sources.jsonl").read_text().splitlines()]
    selected = ["src-000090", "src-000086", "src-000084"]
    for src in rows["sources"]:
        for aspect, kind in (("definitions", "entities"), ("relations", "relations"), ("processes", "processes")):
            if aspect == "processes":
                included = [r["id"] for r in rows[kind]
                            if any(step["location"]["source"] == src["id"] for step in r["steps"])]
            else:
                included = [r["id"] for r in rows[kind]
                            if r.get("location") and r["location"]["source"] == src["id"]
                            and (aspect != "definitions" or r["kind"] != "boundary")]
            src["coverage"][aspect] = {
                "state": "partial" if src["id"] in selected else "not_indexed",
                "included": included,
                "remaining": ["Охват исторического начального набора .001; расширение пилота здесь не подключено."]
            }
    manifest["scope"]["selected_sources"] = selected
    manifest["scope"]["semantic_scope"] = "Исторический начальный набор из трёх исходников."
    manifest["purpose"] = "seed_examples"
    manifest.pop("query_examples", None)  # Cases are loaded from the original examples explicitly.
    manifest["dataset_id"] = "task-0006.001-seed-view"
    manifest["parts"] = {kind: [kind + ".jsonl"] for kind in rows}
    manifest["reference_hashes"] = {p: digest for p, digest in manifest["reference_hashes"].items()
                                   if p in ("docs/analytics/code-audit/cross-check-0002.md",
                                            "docs/issues/potential/issue-00004.md",
                                            "docs/issues/potential/issue-00015.md")}
    manifest["next_ids"] = {"source": 616, "entity": 36, "relation": 54, "process": 3}
    return manifest, rows


def save_seed_view(directory):
    manifest, rows = seed_view()
    for kind, records in rows.items():
        (directory / (kind + ".jsonl")).write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
    path = directory / "manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False))
    return path


def save_pilot_view(directory):
    """Historical .004/.005 parts for fixed pilot counts; no expansion records."""
    manifest = json.loads((BASE / "manifest.json").read_text())
    rows = {}
    for kind in ("entities", "relations", "processes"):
        rows[kind] = [json.loads(line)
                      for part in (f"examples/{kind}.jsonl", f"data/{kind}/pilot.jsonl")
                      for line in (BASE / part).read_text().splitlines()]
    rows["sources"] = [json.loads(line) for line in (BASE / "sources.jsonl").read_text().splitlines()]
    selected = [4, 8, 19, 22, 45, 47, 52, 55, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 202, 209, 214]
    manifest["scope"]["selected_sources"] = [f"src-{n:06}" for n in selected]
    manifest["scope"]["semantic_scope"] = "Исторические части пилота .004/.005 без расширений."
    manifest["dataset_id"] = "task-0006.005-pilot-view"
    manifest.pop("query_examples", None)
    manifest["parts"] = {kind: [kind + ".jsonl"] for kind in rows}
    manifest["next_ids"] = dict(source=616, entity=401, relation=978, process=15)
    for src in rows["sources"]:
        for aspect, kind in (("definitions", "entities"), ("relations", "relations"), ("processes", "processes")):
            included = [row["id"] for row in rows[kind]
                        if (any(step["location"]["source"] == src["id"] for step in row["steps"])
                            if aspect == "processes" else
                            (row.get("location") or {}).get("source") == src["id"]
                            and (aspect != "definitions" or row["kind"] != "boundary"))]
            src["coverage"][aspect] = dict(state="partial" if included else "not_indexed",
                included=included, remaining=["Исторический охват пилота; расширение .006 исключено из этого среза."])
    for kind, data in rows.items():
        (directory / (kind + ".jsonl")).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in data))
    path = directory / "manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False))
    return path


class RealExamples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="witcher-index-seed-")
        cls.addClassCleanup(cls.tmp.cleanup)
        cls.manifest = save_seed_view(Path(cls.tmp.name))
        cls.data = query.Dataset(cls.manifest)

    @classmethod
    def run_cli(cls, arguments, cwd=ROOT):
        return run_cli(["--dataset", str(cls.manifest), *arguments], cwd=cwd)

    def test_16_approved_cli_examples(self):
        cases = json.loads((BASE / "examples/queries.json").read_text())["cases"]
        for case in cases:
            with self.subTest(case=case["id"]):
                run = self.run_cli(case["command"] + ["--format", "json"])
                self.assertEqual(run.returncode, 0, run.stderr)
                out = json.loads(run.stdout)
                expected = case["expected"]
                projection = {
                    "ids": [x["id"] for x in out["items"] if "id" in x],
                    "relation_ids": [x["id"] for x in out["items"] if "from" in x],
                    "from_ids": sorted({x["from"] for x in out["items"] if "from" in x}),
                    "to_ids": sorted({x["to"] for x in out["items"] if "to" in x}),
                    "reader_ids": sorted({x["from"] for x in out["items"] if x.get("kind") == "reads"}),
                    "process_ids": [out["process"]["id"]] if "process" in out else [
                        x["id"] for x in out["items"] if x.get("id", "").startswith("proc-")],
                    "step_ids": [s for x in out["items"] for s in x.get("step_ids", [])],
                    "ref_paths": [x["path"] for x in out["items"] if "sha256" in x and "relation" in x],
                    "coverage": out["coverage"]["state"],
                    "empty_reason": out["empty_reason"],
                    "gaps": out["gaps"],
                    **out["page"],
                }
                if out["items"]:
                    projection["location"] = out["items"][0].get("location")
                    projection["resolution"] = out["items"][0].get("boundary", {}).get("kind")
                if "process" in out:
                    projection["process_coverage"] = out["process"]["coverage"]
                    projection["exit_kind"] = out["process"]["exits"][0]["kind"]
                for key, value in expected.items():
                    if key != "note":
                        self.assertEqual(projection[key], value, key)
                self.assertEqual(out["freshness"]["state"], "current")

    def test_actual_source_definitions(self):
        # Literal expectations from the three source files, not from search results.
        stat = (ROOT / "module/data/actor/templates/common/stats/statData.js").read_text()
        skill = (ROOT / "module/data/actor/templates/common/skills/skillData.js").read_text()
        intel = (ROOT / "module/data/actor/templates/common/skills/intData.js").read_text()
        self.assertNotIn("activeEffectModifiers", stat)
        self.assertIn("return this.value + this.activeEffectModifiers;", skill)
        self.assertEqual(intel.count("new fields.EmbeddedDataField(Skill,"), 13)
        self.assertEqual(self.data.entities["ent-000004"]["owner"], "ent-000001")
        self.assertEqual(self.data.entities["ent-000009"]["owner"], "ent-000007")

    def test_full_check_and_cwd_independence(self):
        run = self.run_cli(["check", "--freshness", "--format", "json"], cwd="/tmp")
        self.assertEqual(run.returncode, 0, run.stderr)
        out = json.loads(run.stdout)
        self.assertTrue(out["valid"])
        self.assertEqual(out["counts"], {"sources": 615, "entities": 35, "relations": 53, "processes": 2})
        self.assertEqual(out["freshness"]["checked"]["documents"], 618)

    def test_case_and_exact_path(self):
        for command, expected in [
            (["find", "НАВЫК", "--match", "exact"], ["ent-000007"]),
            (["find", "Value", "--match", "exact"], []),
            (["find", "module/data/actor/templates/common/skills/skillData.js", "--match", "exact"], ["src-000086"]),
            (["find", "Skill.value", "--match", "exact"], ["ent-000009"]),
            (["find", "ent-000009", "--match", "exact"], ["ent-000009"]),
        ]:
            with self.subTest(command=command):
                out = self.data.query(query.parser().parse_args(command + ["--no-verify"]))
                self.assertEqual([x["id"] for x in out["items"]], expected)
                self.assertEqual(out["freshness"]["state"], "unchecked")

    def test_pagination_and_process_boundary(self):
        out = self.data.query(query.parser().parse_args(
            ["find", "value", "--match", "exact", "--kind", "field", "--offset", "1", "--limit", "1", "--no-verify"]))
        self.assertEqual([x["id"] for x in out["items"]], ["ent-000009"])
        self.assertFalse(out["page"]["truncated"])
        out = self.data.query(query.parser().parse_args(["process", "proc-000002", "--limit", "1", "--no-verify"]))
        self.assertEqual(out["items"][0]["address"], "proc-000002/schema")
        self.assertTrue(out["items"][0]["next"][0]["outside_page"])
        self.assertEqual(out["process"]["exits"][0]["kind"], "scope_boundary")
        self.assertEqual(out["page"]["next_offset"], 1)
        out = self.data.query(query.parser().parse_args(
            ["find", "value", "--match", "exact", "--kind", "field", "--offset", "20", "--no-verify"]))
        self.assertEqual(out["items"], [])
        self.assertIsNone(out["empty_reason"])  # exhausted page, not an absent definition

    def test_invalid_arguments_and_ids(self):
        for args in [
            ["show", "ent-999999"], ["find", "value", "--limit", "0"],
            ["find", "value", "--offset", "-1"], ["neighbors", "ent-000007", "--direction", "out", "--depth", "0"],
            ["field", "ent-000007"], ["show", "ent-000004", "--scope", "src-999999"]
        ]:
            run = self.run_cli(args)
            self.assertEqual(run.returncode, 2, run.stderr)
            self.assertNotIn("Traceback", run.stderr)

    def test_text_output_is_navigable(self):
        out = self.run_cli(["neighbors", "ent-000018", "--direction", "in", "--relation", "calls"])
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("module/data/actor/templates/common/skills/intData.js:26", out.stdout)
        self.assertIn("this = Intelligence", out.stdout)
        self.assertIn("docs/analytics/code-audit/files/", out.stdout)
        self.assertIn("partial", out.stdout)


class Fixture:
    """Three real source texts, synthetic evidence docs; isolated temporary root."""
    def __init__(self, root):
        self.root = root
        self.base = root / "index"
        self.base.mkdir()
        self.m, self.rows = seed_view()
        self.m["purpose"] = "test_fixture"
        self.rows["sources"] = [s for s in self.rows["sources"] if s["id"] in self.m["scope"]["selected_sources"]]
        self.m["scope"]["source_count"] = 3
        for src in self.rows["sources"]:
            self.write(src["path"], (ROOT / src["path"]).read_bytes())
        # Clearly synthetic documents; tests never alter the actual audit corpus.
        evidence = "# Test fixture\n\n## Основные функции и методы\n\n<a id=\"r003-04\"></a>\n"
        doc_paths = {s["card"] for s in self.rows["sources"]} | set(self.m["reference_hashes"])
        for path in doc_paths:
            self.write(path, evidence.encode())
        for src in self.rows["sources"]:
            src["card_sha256"] = sha(evidence.encode())
        self.m["reference_hashes"] = {path: sha(evidence.encode()) for path in self.m["reference_hashes"]}
        registry = "".join(f"| [{s['path']}](../../../{s['path']}) | fixture |\n" for s in self.rows["sources"])
        self.write(self.m["scope"]["registry"], registry.encode())
        self.m["scope"]["registry_sha256"] = sha(registry.encode())
        self.m["snapshot"]["source_hash"] = source_hash(root, self.rows["sources"])
        package = b'{"version":"14.367.0"}\n'
        self.write("core-package.json", package)
        self.m["dependencies"]["foundry"].update(
            observed_package_path=str(root / "core-package.json"), package_sha256=sha(package))
        self.m["parts"] = {k: [k + ".jsonl"] for k in self.rows}

    def write(self, path, data):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)

    def save(self):
        for kind, rows in self.rows.items():
            (self.base / (kind + ".jsonl")).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        (self.base / "manifest.json").write_text(json.dumps(self.m))

    def load(self):
        return query.Dataset(self.base / "manifest.json", root=self.root)

    def row(self, rid):
        return next(r for rows in self.rows.values() for r in rows if r["id"] == rid)


class IsolatedCases(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="witcher-index-test-")
        self.addCleanup(self.tmp.cleanup)
        self.fixture = Fixture(Path(self.tmp.name))
        self.fixture.save()

    def test_declared_malformed_inputs(self):
        cases = json.loads((BASE / "tests/fixtures/invalid-records.json").read_text())["cases"]
        for case in cases:
            with self.subTest(case=case["name"]), tempfile.TemporaryDirectory(prefix="witcher-index-invalid-") as temp:
                f = Fixture(Path(temp))
                action = case.get("action")
                if action == "duplicate_entity":
                    f.rows["entities"].append(deepcopy(f.rows["entities"][0]))
                elif not action:
                    target = f.m if case["target"] == "manifest" else f.row(case["target"])
                    for key in case["path"][:-1]:
                        target = target[key]
                    target[case["path"][-1]] = case["value"]
                f.save()
                entity_path = f.base / "entities.jsonl"
                if action == "duplicate_key":
                    entity_path.write_text(entity_path.read_text().replace('{"id":', '{"id": "ent-999999", "id":', 1))
                elif action == "invalid_json":
                    entity_path.write_text("{broken\n")
                elif action == "missing_part":
                    entity_path.unlink()
                with self.assertRaises(query.IndexErrorDetail) as raised:
                    data = f.load()
                    if case.get("freshness"):
                        data.verify(all_docs=True)
                self.assertEqual(raised.exception.detail["code"], case["code"])

    def test_stale_missing_and_unchecked_sources(self):
        f = self.fixture
        path = f.root / f.row("src-000086")["path"]
        path.write_text("// Changed source\n")
        data = f.load()
        args = query.parser().parse_args(["show", "ent-000016"])
        out = data.query(args)
        self.assertEqual(out["freshness"]["state"], "stale")
        self.assertEqual(out["items"][0]["location"]["line_start"], 16)  # historical hint
        path.unlink()
        self.assertEqual(data.query(args)["freshness"]["state"], "missing")
        args.no_verify = True
        self.assertEqual(data.query(args)["freshness"]["state"], "unchecked")

    def test_evidence_and_external_boundary_freshness(self):
        f = self.fixture
        (f.root / f.row("src-000086")["card"]).write_text("changed")
        data = f.load()
        out = data.query(query.parser().parse_args(["show", "ent-000009"]))
        self.assertEqual(out["freshness"]["state"], "stale")
        (f.root / f.row("src-000086")["card"]).unlink()
        self.assertEqual(data.verify(all_docs=True)["state"], "missing")
        (f.root / "core-package.json").unlink()
        out = data.query(query.parser().parse_args(["show", "ent-000034"]))
        self.assertEqual(out["freshness"]["state"], "current")
        self.assertEqual(out["gaps"], ["external_boundary", "external_dependency_unverified"])

    def test_registry_membership_and_bad_symlink(self):
        f = self.fixture
        path = f.root / f.m["scope"]["registry"]
        path.write_text("| [extra](../../../extra) | fixture |\n")
        f.m["scope"]["registry_sha256"] = sha(path.read_bytes())
        f.save()
        with self.assertRaises(query.IndexErrorDetail) as error:
            f.load().verify()
        self.assertEqual(error.exception.detail["code"], "registry_mismatch")
        (f.base / "escaped.jsonl").symlink_to(BASE / "examples/entities.jsonl")
        f.m["parts"]["entities"] = ["escaped.jsonl"]
        f.save()
        with self.assertRaises(query.IndexErrorDetail) as error:
            f.load()
        self.assertEqual(error.exception.detail["code"], "path_escape")

    def test_cli_load_failure_and_freshness_exit_status(self):
        f = self.fixture
        manifest = str(f.base / "manifest.json")
        # This CLI intentionally uses the real repository root: fixture evidence
        # hashes differ from the actual documents, and check must report failure.
        run = run_cli(["--dataset", manifest, "check", "--freshness", "--format", "json"])
        self.assertEqual(run.returncode, 1, run.stderr)
        self.assertFalse(json.loads(run.stdout)["valid"])
        (f.base / "entities.jsonl").write_text("{invalid\n")
        run = run_cli(["--dataset", manifest, "find", "value", "--format", "json"])
        self.assertEqual(run.returncode, 1, run.stderr)
        self.assertEqual(json.loads(run.stderr)["error"]["code"], "invalid_json")
        self.assertNotIn("Traceback", run.stderr)

    def test_access_modes_and_usage_site_scope(self):
        f = self.fixture
        # Artificial writes/computes isolate the access filter from game semantics.
        for number, kind in [(54, "writes"), (55, "computes")]:
            rel = deepcopy(f.row("rel-000050"))
            rel.update(id=f"rel-{number:06d}", kind=kind, context="test_fixture")
            f.rows["relations"].append(rel)
            f.row("src-000086")["coverage"]["relations"]["included"].append(rel["id"])
        f.m["next_ids"]["relation"] = 56
        f.save()
        data = f.load()
        for access, expected in [("reads", ["rel-000050"]), ("writes", ["rel-000054"]),
                                 ("computes", ["rel-000055"]),
                                 ("all", ["rel-000050", "rel-000054", "rel-000055"])]:
            args = query.parser().parse_args(["field", "ent-000012", "--access", access,
                                             "--scope", "src-000086", "--no-verify"])
            self.assertEqual([r["id"] for r in data.query(args)["items"]], expected)
            args.scope = ["src-000084"]
            self.assertEqual(data.query(args)["items"], [])

    def test_graph_cycle_distinct_sites_and_depth(self):
        f = self.fixture
        # Synthetic calls to exercise traversal, not assertions about the real system.
        for number, source, target in [(54, "ent-000018", "ent-000032"), (55, "ent-000032", "ent-000018")]:
            rel = deepcopy(f.row("rel-000051"))
            rel.update(id=f"rel-{number:06d}", **{"from": source, "to": target, "condition": "test_fixture"})
            f.rows["relations"].append(rel)
            f.row("src-000084")["coverage"]["relations"]["included"].append(rel["id"])
        f.m["next_ids"]["relation"] = 56
        f.save()
        data = f.load()
        args = query.parser().parse_args(["neighbors", "ent-000032", "--direction", "out", "--relation", "calls",
                                          "--depth", "1000", "--no-verify"])
        out = data.query(args)
        self.assertEqual([r["id"] for r in out["items"]], ["rel-000051", "rel-000053", "rel-000054", "rel-000055"])
        cycle = next(r for r in out["items"] if r["id"] == "rel-000054")
        self.assertEqual(cycle["path"], ["rel-000051", "rel-000054"])
        args.depth = 1
        self.assertTrue(data.query(args)["traversal"]["depth_limited"])

    def test_retired_id_and_complete_empty_coverage(self):
        f = self.fixture
        f.m["retired_ids"] = ["ent-000100"]
        f.m["next_ids"]["entity"] = 101
        # This test marks only a synthetic fixture's definition aspect complete.
        cov = f.row("src-000086")["coverage"]["definitions"]
        cov.update(state="complete", remaining=[])
        f.save()
        data = f.load()
        with self.assertRaises(query.IndexErrorDetail) as error:
            data.query(query.parser().parse_args(["show", "ent-000100", "--no-verify"]))
        self.assertEqual(error.exception.detail["code"], "retired_id")
        out = data.query(query.parser().parse_args(["find", "absent", "--scope", "src-000086", "--no-verify"]))
        self.assertEqual((out["empty_reason"], out["coverage"]["state"]), ("none_in_scope", "complete"))

    def test_queries_are_read_only(self):
        f = self.fixture
        def snapshot():
            return {str(p.relative_to(f.root)): (p.read_bytes(), p.stat().st_mode, p.stat().st_uid,
                                               p.stat().st_gid, p.stat().st_ino)
                    for p in f.root.rglob("*") if p.is_file()}
        before = snapshot()
        data = f.load()
        for args in [["show", "ent-000004"], ["process", "proc-000002"], ["details", "ent-000010"],
                     ["field", "ent-000012", "--access", "reads"]]:
            data.query(query.parser().parse_args(args))
        data.verify(all_docs=True)
        self.assertEqual(snapshot(), before)


if __name__ == "__main__":
    unittest.main()
