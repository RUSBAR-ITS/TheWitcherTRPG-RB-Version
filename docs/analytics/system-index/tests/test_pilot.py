"""Проверки пилота .003 по ориентирам исходников; игровой код не исполняется."""

import json
from pathlib import Path
import unittest

from test_query import BASE, ROOT, query, run_cli


class PilotQueries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = query.Dataset()

    def test_13_source_grounded_cli_cases(self):
        cases = json.loads((BASE / "examples/pilot-queries.json").read_text())["cases"]
        for case in cases:
            with self.subTest(case=case["id"]):
                run = run_cli(case["command"] + ["--format", "json"])
                self.assertEqual(run.returncode, 0, run.stderr)
                out = json.loads(run.stdout)
                first = out["items"][0] if out["items"] else {}
                projection = {
                    "ids": [r["id"] for r in out["items"] if "id" in r],
                    "from_ids": sorted({r["from"] for r in out["items"] if "from" in r}),
                    "to_ids": sorted({r["to"] for r in out["items"] if "to" in r}),
                    "locations": [[r["location"]["source"], r["location"]["line_start"]]
                                  for r in out["items"] if r.get("location")],
                    "owner": first.get("owner"),
                    "source": (first.get("location") or {}).get("source"),
                    "line_start": (first.get("location") or {}).get("line_start"),
                    "resolution": first.get("boundary", {}).get("kind"),
                    "includes_ref_paths": [r["path"] for r in out["items"] if "path" in r],
                    "gaps": out["gaps"],
                    "empty_reason": out["empty_reason"],
                    "coverage": out["coverage"]["state"],
                }
                for key, expected in case["expected"].items():
                    if key == "includes_ref_paths":
                        self.assertTrue(set(expected) <= set(projection[key]), projection[key])
                    elif key == "locations":
                        self.assertCountEqual(projection[key], expected)
                    else:
                        self.assertEqual(projection[key], expected, key)
                self.assertEqual(out["freshness"]["state"], "current")
                self.assertEqual(out["coverage"]["state"], "partial")

    def test_catalogue_and_pilot_are_distinct(self):
        run = run_cli(["check", "--freshness", "--format", "json"], cwd="/tmp")
        self.assertEqual(run.returncode, 0, run.stderr)
        out = json.loads(run.stdout)
        self.assertEqual(out["counts"], {"sources": 615, "entities": 400, "relations": 977, "processes": 14})
        self.assertEqual(len(self.data.manifest["scope"]["selected_sources"]), 23)
        represented = [s for s in self.data.sources.values() if s["coverage"]["definitions"]["included"]]
        self.assertEqual(len(represented), 36)
        self.assertTrue(all(s["coverage"]["definitions"]["state"] == "partial" for s in represented))
        self.assertEqual(self.data.sources["src-000047"]["coverage"]["processes"]["state"], "partial")

    def test_value_paths_and_double_calculation_sites(self):
        # Independent literal source checks guard the interpretation, not game behaviour.
        skill = (ROOT / "module/actor/mixins/skillMixin.js").read_text()
        self.assertIn("let skillValue = this.system.skills[attribute.name][skillName].value;", skill)
        self.assertNotIn("modifiedValue", skill)
        custom = skill[skill.index("async rollCustomSkillCheck"):]
        self.assertIn("let skillValue = customSkill.system.value;", custom)
        self.assertNotIn("activeEffectModifiers", custom)
        actor = (ROOT / "module/actor/witcherActor.js").read_text()
        fragment = actor[actor.index("prepareDerivedData()"):actor.index("    calculateStats()")]
        self.assertEqual(fragment.count("this.calculateStats()"), 2)
        edges = [r for r in self.data.relations.values()
                 if r["kind"] == "calls" and r["from"] == "ent-000280" and r["to"] == "ent-000281"]
        self.assertEqual(sorted(r["location"]["line_start"] for r in edges), [49, 51])

    def test_raw_payload_phase_and_same_name_owners(self):
        ae = (ROOT / "module/activeEffect/witcherActiveEffect.js").read_text()
        self.assertIn("data.system?.applyAfterCalculations ? 'final' : 'initial'", ae)
        self.assertIn("data.system?.changes.forEach", ae)
        self.assertIn("change.phase = phase;", ae)
        self.assertNotEqual(self.data.entities["ent-000012"]["owner"], self.data.entities["ent-000188"]["owner"])
        self.assertEqual(self.data.entities["ent-000188"]["qualified_name"], "SkillItemData.activeEffectModifiers")
        er = (ROOT / "module/scripts/rolls/extendedRoll.js").read_text()
        self.assertNotIn("config.showSuccess", er)
        self.assertIn("await evaluatedRoll.toMessage(messageData)", er)
        self.assertNotIn("await message.setFlag", er)


if __name__ == "__main__":
    unittest.main()
