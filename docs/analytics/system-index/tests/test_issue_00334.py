"""Адресная сверка UI-маршрутов с кодом; Foundry/браузер не запускаются."""
import unittest
from test_query import ROOT, query


class InterfaceRefactoring(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = query.Dataset()

    def source(self, sid):
        return (ROOT / self.data.sources[sid]['path']).read_text()

    def edges(self, eid, kind):
        return [r for r in self.data.relations.values()
                if r['from'] == eid and r['kind'] == kind]

    def test_removed_routes_are_retired_and_not_callable(self):
        for rid in ['ent-000843', 'ent-003553', 'rel-007830', 'rel-007582']:
            self.assertIn(rid, self.data.manifest['retired_ids'])
            self.assertNotIn(rid, self.data.all)
        sheet = self.source('src-000027')
        self.assertNotIn('this.currencyConverterListeners(', sheet)
        self.assertNotIn('Object.assign(WitcherActorSheet.prototype, currencyConverterMixin)', sheet)
        self.assertIn('openCurrencyConverter: currencyConverterMixin.onOpenCurrencyConverter', sheet)
        self.assertIn('data-action="openCurrencyConverter"', self.source('src-000576'))
        self.assertEqual([r['to'] for r in self.edges('ent-005394', 'registers')], ['ent-005392'])
        self.assertEqual([r['to'] for r in self.edges('ent-005392', 'calls')], ['ent-005393'])

    def test_actor_and_item_description_owners_remain_separate(self):
        self.assertIn("context.effectDescriptionAction = 'displayEffectDescription'", self.source('src-000183'))
        self.assertNotIn('effectDescriptionAction', self.source('src-000027'))
        self.assertIn('{{#if @root.effectDescriptionAction}}', self.source('src-000531'))
        self.assertIn('.effect-display', self.source('src-000036'))
        registrations = self.edges('ent-000826', 'registers')
        self.assertEqual([r['to'] for r in registrations].count('ent-005390'), 1)
        self.assertEqual([r['to'] for r in registrations].count('ent-000828'), 4)

    def test_new_definition_addresses_and_receivers(self):
        expected = {
            'ent-005388': '_ensureWizardButton() {',
            'ent-005389': '#attributeKeyListId =',
            'ent-005390': 'static onDisplayEffectDescription(event, element)',
            'ent-005391': 'context.effectDescriptionAction =',
            'ent-005392': 'onOpenCurrencyConverter(event)',
            'ent-005394': 'actions: {',
            'ent-005395': 'lookup (lookup ../criticalWounds critWound.uuid)',
        }
        for eid, literal in expected.items():
            with self.subTest(eid=eid):
                loc = self.data.entities[eid]['location']
                self.assertIn(literal, self.source(loc['source']).splitlines()[loc['line_start'] - 1])
        handler = self.source('src-000039')
        self.assertIn('return this.actor.handleCurrencyConverter(event)', handler)
        self.assertNotIn('addEventListener', handler)

    def test_editor_refresh_does_not_replace_form_or_write_document(self):
        for eid in ['ent-000696', 'ent-000698', 'ent-005388']:
            loc = self.data.entities[eid]['location']
            body = '\n'.join(self.source(loc['source']).splitlines()[loc['line_start']-1:loc['line_end']])
            for forbidden in ['document.update(', '.innerHTML =', '.value =', 'replaceWith(']:
                # New option.value is allowed; editing form input values is not.
                if forbidden == '.value =' and eid == 'ent-000698':
                    self.assertNotIn('inputField.value', body)
                    continue
                self.assertNotIn(forbidden, body)
        render = self.edges('ent-000696', 'calls')
        self.assertIn('ent-005388', [r['to'] for r in render])
        self.assertIn('ent-000698', [r['to'] for r in render])
        source = self.source('src-000005')
        self.assertNotIn('async autocomplete()', source)
        self.assertIn('datalist.replaceChildren(options)', source)

    def test_changed_processes_reachable_and_relations_at_actual_step(self):
        for number in [25, 28, 32, 33, 47, 48, 53, 119, 134, 332, 466, 467, 468]:
            p = self.data.processes[f'proc-{number:06}']
            steps = {s['id']: s for s in p['steps']}
            pending = [p['steps'][0]['id']]
            seen, exits = set(), set()
            while pending:
                key = pending.pop()
                if key in seen:
                    continue
                seen.add(key)
                for nxt in steps[key]['next']:
                    if 'step' in nxt:
                        pending.append(nxt['step'])
                    else:
                        exits.add(nxt['exit'])
            self.assertEqual(seen, set(steps), p['id'])
            self.assertEqual(exits, {e['id'] for e in p['exits']}, p['id'])
            for step in steps.values():
                loc = step['location']
                self.assertLessEqual(loc['line_end'], len(self.source(loc['source']).splitlines()))
                for rid in step['relations']:
                    where = self.data.relations[rid]['location']
                    with self.subTest(process=p['id'], step=step['id'], relation=rid):
                        self.assertEqual(where['source'], loc['source'])
                        self.assertLessEqual(loc['line_start'], where['line_start'])
                        self.assertLessEqual(where['line_end'], loc['line_end'])


if __name__ == '__main__':
    unittest.main()
