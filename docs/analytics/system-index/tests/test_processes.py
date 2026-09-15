"""Проверки поиска участия и процессов .004; игровой код не исполняется."""

import json
from pathlib import Path
import tempfile
import unittest

from test_query import BASE, ROOT, query, run_cli, save_seed_view, save_pilot_view


class ProcessParticipation(unittest.TestCase):
    def test_field_participates_through_explicit_step_relation(self):
        with tempfile.TemporaryDirectory(prefix="witcher-index-process-seed-") as tmp:
            data = query.Dataset(save_seed_view(Path(tmp)))
            out = data.query(query.parser().parse_args(
                ["processes", "ent-000012", "--no-verify"]))
            self.assertEqual([(p["id"], p["step_ids"]) for p in out["items"]],
                             [("proc-000001", ["proc-000001/read"])])

    @classmethod
    def setUpClass(cls):
        cls.data = query.Dataset()
        cls.pilot = tempfile.TemporaryDirectory(prefix="witcher-index-process-pilot-")
        cls.addClassCleanup(cls.pilot.cleanup)
        cls.pilot_manifest = save_pilot_view(Path(cls.pilot.name))

    def ask(self, *args):
        return self.data.query(query.parser().parse_args([*args, "--no-verify"]))

    def test_twelve_real_process_cli_cases(self):
        cases = json.loads((BASE / "examples/process-queries.json").read_text())["cases"]
        for case in cases:
            with self.subTest(case=case["id"]):
                run = run_cli(["--dataset", str(self.pilot_manifest), *case["command"], "--format", "json"])
                self.assertEqual(run.returncode, 0, run.stderr)
                out = json.loads(run.stdout)
                first = out["items"][0] if out["items"] else {}
                projection = {
                    "ids": [r["id"] for r in out["items"] if "id" in r],
                    "step_ids": [sid for p in out["items"] for sid in p.get("step_ids", [])],
                    "empty_reason": out["empty_reason"],
                    "coverage": out["coverage"]["state"],
                    "next_steps": [n.get("step") for n in first.get("next", [])],
                    "outside_page": [n.get("outside_page") for n in first.get("next", [])],
                    "ref_anchors": [r["anchor"] for r in out["items"] if "anchor" in r],
                    **out["page"]
                }
                for key, expected in case["expected"].items():
                    if key == "ref_anchors":
                        self.assertTrue(set(expected) <= set(projection[key]))
                    else:
                        self.assertEqual(projection[key], expected, key)
                self.assertEqual(out["freshness"]["state"], "current")
                self.assertEqual(out["coverage"]["state"], case["expected"].get("coverage", "partial"))

    def test_steps_are_reachable_and_relations_have_local_evidence(self):
        # Checks the authored graph, not a simulation of JavaScript or core Foundry.
        processes = [json.loads(line) for line in (BASE / "data/processes/pilot.jsonl").read_text().splitlines()]
        self.assertEqual(len(processes), 12)
        self.assertEqual(sum(len(p["steps"]) for p in processes), 96)
        for p in processes:
            with self.subTest(process=p["id"]):
                steps = {s["id"]: s for s in p["steps"]}
                seen, exits, pending = set(), set(), [p["steps"][0]["id"]]
                while pending:
                    key = pending.pop()
                    if key in seen:
                        continue
                    seen.add(key)
                    for nxt in steps[key]["next"]:
                        if "step" in nxt:
                            pending.append(nxt["step"])
                        else:
                            exits.add(nxt["exit"])
                self.assertEqual(seen, set(steps))
                self.assertEqual(exits, {e["id"] for e in p["exits"]})
                for s in p["steps"]:
                    for rid in s["relations"]:
                        loc = self.data.relations[rid]["location"]
                        self.assertEqual(loc["source"], s["location"]["source"], (s["id"], rid))
                        self.assertTrue(s["location"]["line_start"] <= loc["line_start"] <= s["location"]["line_end"])
                self.assertEqual(p["coverage"], "partial")

    def test_actor_order_and_death_branch_match_source(self):
        actor = (ROOT / "module/actor/witcherActor.js").read_text().splitlines()
        self.assertEqual([actor[n - 1].strip() for n in [49, 50, 51, 52, 53]], [
            "this.calculateStats();", "this.calculateFixedDerivedStats();",
            "this.calculateStats();", "this.calculateDerivedStats();", "this.calculateAttackStats();"])
        steps = self.data.processes["proc-000004"]["steps"]
        self.assertEqual([s["id"] for s in steps[-5:]],
                         ["stats-first", "fixed", "stats-second", "derived", "attacks"])
        calc = {s["id"]: s for s in self.data.processes["proc-000005"]["steps"]}
        self.assertEqual(calc["death"]["next"], [{"step": "value",
                                                "when": "Продолжить после завершения шага", "flow": "sync"}])
        self.assertIn("divider += 2", actor[92])
        self.assertEqual(calc["wound-check"]["location"]["line_start"], 95)
        self.assertIn("woundThreshold.applied = false", actor[94])

    def test_awaits_and_output_branches_are_not_conflated(self):
        steps = {s["id"]: s for s in self.data.processes["proc-000012"]["steps"]}
        for key in ["evaluate", "extra", "rebuild", "publish"]:
            self.assertTrue(all(n["flow"] == "await" for n in steps[key]["next"]))
        for key in ["array-flags", "one-flag"]:
            self.assertEqual(steps[key]["next"][0]["step"], "return")
            self.assertEqual(steps[key]["next"][0]["flow"], "sync")
        self.assertEqual([n["step"] for n in steps["output"]["next"]], ["publish", "defer"])
        self.assertEqual(steps["defer"]["next"][0]["step"], "return")
        source = (ROOT / "module/scripts/rolls/extendedRoll.js").read_text()
        self.assertIn("await evaluatedRoll.toMessage(messageData)", source)
        self.assertNotIn("await message.setFlag", source)
        self.assertNotIn("config.showSuccess", source)
        self.assertIn("evaluatedRoll.total >= config.threshold", source)
        self.assertIn("evaluatedRoll.total < config.threshold", source)

    def test_partial_payload_core_boundary_and_no_transitive_inference(self):
        update = {s["id"]: s for s in self.data.processes["proc-000007"]["steps"]}
        self.assertEqual({n.get("exit") for n in update["allowed"]["next"]}, {"blocked", None})
        self.assertEqual({n.get("exit") for n in update["changes"]["next"]}, {"finished", "failed", None})
        phase = self.ask("processes", "ent-000176")
        self.assertEqual(phase["items"][0]["step_ids"], ["proc-000007/phase"])
        # Its helper reads activeEffectModifiers, but no such read is attached to rollSkillCheck's own step.
        out = self.ask("processes", "ent-000012", "--scope", "src-000022")
        self.assertEqual(out["items"], [])
        core = self.data.processes["proc-000006"]
        self.assertEqual(core["entry"]["entity"], "ent-000313")
        self.assertEqual(next(x for x in core["exits"] if x["id"] == "application")["kind"], "external_boundary")
        self.assertTrue(all(s["location"]["source"] == "src-000008" for s in core["steps"]))


if __name__ == "__main__":
    unittest.main()
