"""Навигация изменённых цепочек TASK-0010.003; игровая модель проверяется отдельно."""
import json
import unittest
from test_query import ROOT, BASE, query

class ModifierEditorIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = query.Dataset()
        cls.q = {e['qualified_name']: e['id'] for e in cls.data.entities.values()}

    def edges(self, name, kind):
        return {r['to'] for r in self.data.outgoing[self.q[name]] if r['kind'] == kind}

    def test_model_and_sheet_share_metadata(self):
        for owner, target in [('ModifierChangeField._cleanType', 'modifierContext.supportsModifierChange'),
                              ('validateModifierChange', 'modifierContext.supportsModifierChange'),
                              ('WitcherActiveEffectConfig._renderChange', 'modifierContext.supportsModifierChange'),
                              ('WitcherActiveEffectConfig.wizardAction', 'modifierContext.getEffectTargetType'),
                              ('WitcherActiveEffectConfig.autocomplete', 'modifierContext.getEffectTargetType')]:
            self.assertIn(self.q[target], self.edges(owner, 'calls'))

    def test_wizard_and_plus_reach_submit_not_direct_update(self):
        for owner in ['WitcherActiveEffectConfig.wizardAction/ok.callback', 'WitcherActiveEffectConfig.addChangeAction']:
            calls = self.edges(owner, 'calls')
            self.assertIn(self.q['ActiveEffectConfig.submit/modifierEditor'], calls)
            self.assertNotIn(self.q['Document.update/ActiveEffect'], calls)
        self.assertIn('копия', self.data.entities[self.q['wizardAction/formChangesCopy']]['summary'].lower())

    def test_native_template_fallback_and_new_partial_are_distinct(self):
        paths = {s['path']: s['id'] for s in self.data.sources.values()}
        self.assertIn(paths['templates/sheets/activeEffect/change.hbs'], self.edges('WitcherActiveEffectConfig._renderChange', 'renders'))
        partial = paths['templates/sheets/activeEffect/modifier-settings.hbs']
        for path in ['templates/sheets/activeEffect/change.hbs', 'templates/dialog/activeEffects/wizard.hbs']:
            self.assertTrue(any(r['kind'] == 'renders' and r['to'] == partial for r in self.data.outgoing[paths[path]]))

    def test_phase_process_has_partial_update_early_exits(self):
        proc = self.data.processes['proc-000007']
        self.assertEqual(proc['entry']['entity'], self.q['WitcherActiveEffect._preUpdate'])
        steps = {s['id']: s for s in proc['steps']}
        self.assertTrue(any(n.get('exit') == 'done' and 'false' in n['when'] for n in steps['parent']['next']))
        self.assertTrue(any(n.get('exit') == 'done' for n in steps['changes']['next']))
        self.assertIn('сохран', steps['phase']['summary'])

    def test_current_base_descriptions_and_field_locations(self):
        for name in ['stats-block.input.unmodifiedMax', 'stats-block.input.reputationBase', 'edit-skills.input.skillValue']:
            self.assertIn('source', self.data.entities[self.q[name]]['summary'])
        for name in ['stat.baseCap', 'Skill.baseCap', 'SkillItemData.baseCap', 'professionSkill().baseCap']:
            loc = self.data.entities[self.q[name]]['location']
            source = ROOT / self.data.sources[loc['source']]['path']
            self.assertIn('baseCap: new', source.read_text().splitlines()[loc['line_start'] - 1])

    def test_all_new_localizations_keep_exact_values_and_addresses(self):
        for lang in ['en', 'ru']:
            path = 'lang/' + lang + '.json'
            data = json.loads((ROOT / path).read_text())['WITCHER']['Effect']['Modifier']
            leaves = {k + '.' + a: b for k, v in data.items() if isinstance(v, dict) for a, b in v.items()}
            leaves.update({k: v for k, v in data.items() if isinstance(v, str)})
            self.assertEqual(len(leaves), 31)
            lines = (ROOT / path).read_text().splitlines()
            for key, value in leaves.items():
                entity = self.data.entities[self.q[lang + '::WITCHER.Effect.Modifier.' + key]]
                self.assertIn(value, entity['summary'])
                self.assertIn(json.dumps(value, ensure_ascii=False), lines[entity['location']['line_start'] - 1])

    def test_query_routes_to_implementation_and_process(self):
        for name in ['WitcherActiveEffectConfig.wizardAction', 'WitcherActiveEffect._preUpdate',
                     'modifierContext.getEffectTargetType', 'WitcherModifiersConfiguration._prepareContext']:
            out = self.data.query(query.parser().parse_args(['details', self.q[name], '--no-verify']))
            self.assertTrue(any(r.get('path') == 'docs/analytics/task-0010-003-checks.md' for r in out['items']))
        for name, pid in [('WitcherActiveEffectConfig.wizardAction', 'proc-000026'),
                          ('WitcherActiveEffectConfig.wizardAction/ok.callback', 'proc-000027')]:
            out = self.data.query(query.parser().parse_args(['processes', self.q[name], '--limit', '100', '--no-verify']))
            self.assertIn(pid, {r['id'] for r in out['items']})
