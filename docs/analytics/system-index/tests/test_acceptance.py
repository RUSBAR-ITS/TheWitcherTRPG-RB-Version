"""Приёмка реального пилота и неизменяющие исходники входы проверки версии."""
from collections import defaultdict
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from test_query import BASE, ROOT, query, run_cli, save_pilot_view


class PilotAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = query.Dataset()
        cls.pilot = tempfile.TemporaryDirectory(prefix="witcher-index-historical-case-")
        cls.addClassCleanup(cls.pilot.cleanup)
        cls.pilot_manifest = save_pilot_view(Path(cls.pilot.name))

    def test_26_independently_located_cases(self):
        cases = json.loads((BASE / "examples/acceptance-queries.json").read_text())["cases"]
        for case in cases:
            with self.subTest(case=case["id"]):
                prefix = ["--dataset", str(self.pilot_manifest)] if case["id"] in {"A01","A13","A15","A23","A25"} else []
                run = run_cli(prefix + case["command"] + ["--format", "json"], cwd="/tmp")
                self.assertEqual(run.returncode, 0, run.stderr)
                out = json.loads(run.stdout)
                items = out["items"]
                first = items[0] if items else {}
                projection = {
                    "ids": [x["id"] for x in items if "id" in x],
                    "owner": first.get("owner"),
                    "location": [(first.get("location") or {}).get(k) for k in ("source", "line_start")],
                    "locations": sorted([[x["location"]["source"], x["location"]["line_start"]]
                                         for x in items if x.get("location")]),
                    "from_ids": sorted({x["from"] for x in items if "from" in x}),
                    "to_ids": sorted({x["to"] for x in items if "to" in x}),
                    "step_ids": [sid for x in items for sid in x.get("step_ids", [])],
                    "includes_ref_paths": [x["path"] for x in items if "sha256" in x and "relation" in x],
                    "includes_anchors": [x.get("anchor") for x in items],
                    "boundary_kind": first.get("boundary", {}).get("kind"),
                    "expression": first.get("boundary", {}).get("expression"),
                    "includes_gaps": out["gaps"],
                    "empty_reason": out["empty_reason"],
                    "coverage": out["coverage"]["state"],
                    "next_steps": [e["step"] for e in first.get("next", []) if "step" in e],
                    "outside_page": all(e.get("outside_page") for e in first.get("next", []) if "step" in e),
                    "depth_limited": out.get("traversal", {}).get("depth_limited"),
                    **out["page"],
                }
                for key, expected in case["expected"].items():
                    if key.startswith("includes_"):
                        self.assertTrue(set(expected) <= set(projection[key]), (key, projection[key]))
                    elif key == "context_contains":
                        self.assertTrue(items)
                        self.assertTrue(all(expected in x.get("context", "") for x in items))
                    elif key == "locations":
                        self.assertEqual(projection[key], sorted(expected))
                    else:
                        self.assertEqual(projection[key], expected, key)
                self.assertEqual(out["freshness"]["state"], "current")

    def test_source_orientations_before_graph_interpretation(self):
        # Literal addresses established by reading actual source, not generated from graph edges.
        samples = [
            ("module/data/actor/templates/common/skills/skillData.js", 9, "activeEffectModifiers: new fields.NumberField"),
            ("module/data/item/skillItemData.js", 10, "activeEffectModifiers: new fields.NumberField"),
            ("module/data/actor/templates/common/stats/statData.js", 7, "value: new fields.NumberField"),
            ("module/TheWitcherTRPG.js", 33, "CONFIG.Actor.documentClass = WitcherActor"),
            ("module/actor/sheets/mixins/skillMixin.js", 35, "skill.addEventListener('click', event => thisActor.rollSkillCheck"),
            ("module/actor/mixins/skillMixin.js", 43, "return this.rollSkillCheck("),
            ("module/actor/mixins/skillMixin.js", 53, "this.system.skills[attribute.name][skillName].value"),
            ("module/actor/mixins/skillMixin.js", 65, "this.addActiveEffects(skillMapEntry.name)"),
            ("module/actor/witcherActor.js", 49, "this.calculateStats()"),
            ("module/actor/witcherActor.js", 51, "this.calculateStats()"),
            ("module/actor/witcherActor.js", 106, "this.system.stats[stat].value = Math.floor("),
            ("module/activeEffect/witcherActiveEffect.js", 117, "change.phase = phase"),
            ("module/scripts/rolls/extendedRoll.js", 86, "await evaluatedRoll.toMessage(messageData)"),
            ("module/scripts/rolls/extendedRoll.js", 95, "evaluatedRoll.messageData = messageData"),
        ]
        for path, line, literal in samples:
            with self.subTest(path=path, line=line):
                self.assertIn(literal, (ROOT / path).read_text().splitlines()[line - 1])
        skill = (ROOT / "module/actor/mixins/skillMixin.js").read_text()
        self.assertNotIn("modifiedValue", skill)
        self.assertNotIn("activeEffectModifiers", skill[skill.index("async rollCustomSkillCheck"):])
        issue = (ROOT / "docs/issues/potential/issue-00190.md").read_text()
        self.assertIn("potential", issue)
        self.assertIn("AE transfer и сохранение в мире не исследованы", issue)
        audit = (ROOT / "docs/analytics/code-audit/cross-check-0002.md").read_text()
        self.assertIn('<a id="r004-07"></a>', audit)

    def test_every_relation_is_retrievable_in_both_directions(self):
        # This is structural reciprocity, not proof of every edge's game semantics.
        expected = {"out": defaultdict(dict), "in": defaultdict(dict)}
        for rid, rel in self.data.relations.items():
            expected["out"][rel["from"]][rid] = rel
            expected["in"][rel["to"]][rid] = rel
        for direction, subjects in expected.items():
            for sid, edges in subjects.items():
                with self.subTest(direction=direction, subject=sid):
                    args = query.parser().parse_args([
                        "neighbors", sid, "--direction", direction, "--depth", "1", "--limit", "5000", "--no-verify"])
                    out = self.data.query(args)
                    self.assertFalse(out["page"]["truncated"])
                    actual = {r["id"]: {k:v for k,v in r.items() if k != "path"} for r in out["items"]}
                    self.assertEqual(actual, edges)

    def test_stale_metadata_against_unchanged_real_source(self):
        # Only a temporary metadata copy changes; current source bytes remain untouched.
        original = (ROOT / "module/data/actor/templates/common/skills/skillData.js").read_bytes()
        manifest = deepcopy(self.data.manifest)
        with tempfile.TemporaryDirectory(prefix="witcher-index-acceptance-") as temp:
            base = Path(temp)
            for kind, paths in manifest["parts"].items():
                for name in paths:
                    dest = base / name
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes((BASE / name).read_bytes())
            records = [json.loads(x) for x in (base / "sources.jsonl").read_text().splitlines()]
            next(x for x in records if x["id"] == "src-000086")["sha256"] = "0" * 64
            (base / "sources.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in records))
            path = base / "manifest.json"
            path.write_text(json.dumps(manifest))
            run = run_cli(["--dataset", str(path), "show", "ent-000012", "--format", "json"])
            self.assertEqual(run.returncode, 0, run.stderr)
            out = json.loads(run.stdout)
            self.assertEqual(out["freshness"]["state"], "stale")
            self.assertEqual(out["items"][0]["location"]["line_start"], 9)
            self.assertEqual([d["path"] for d in out["freshness"]["differences"]],
                             ["module/data/actor/templates/common/skills/skillData.js"])
            run = run_cli(["--dataset", str(path), "check", "--freshness", "--format", "json"])
            self.assertEqual(run.returncode, 1, run.stderr)
            self.assertFalse(json.loads(run.stdout)["valid"])
        self.assertEqual((ROOT / "module/data/actor/templates/common/skills/skillData.js").read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
