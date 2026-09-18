"""Адресные связи производных TASK-0010.005; игровые числа проверены отдельно."""
import unittest
from test_query import ROOT, query

class DerivedCalculationIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = query.Dataset()
        cls.q = {e['qualified_name']: e['id'] for e in cls.data.entities.values()}

    def targets(self, name, kind='calls'):
        return {r['to'] for r in self.data.outgoing[self.q[name]] if r['kind'] == kind}

    def test_all_derived_consumers_share_helper(self):
        for owner in ['calculateStats', 'calculateWeigthEncumbrance', 'calculateFixedDerivedStats', 'calculateDerivedStat']:
            self.assertIn(self.q['derivedPreparation.calculateDerivedParameter'], self.targets('WitcherActor.' + owner))

    def test_chain_and_row_recalculation(self):
        targets = self.targets('derivedPreparation.calculateDerivedParameter')
        for name in ['derivedPreparation.derivedStatInput', 'derivedPreparation.calculateDerivedParameter', 'derivedStatData.derivedStatBase', 'parameterCalculation.calculateParameter']:
            self.assertIn(self.q[name], targets)
        self.assertIn(self.q['parameterCalculation.calculateParameter'], self.targets('derivedPreparation.derivedStatInput'))

    def test_manual_base_contract_has_three_consumers(self):
        for name in ['CommonActorData.prepareBaseData', 'WitcherModifiersConfiguration._prepareContext', 'derivedPreparation.calculateDerivedParameter']:
            self.assertIn(self.q['derivedStatData.isManualDerivedStat'], self.targets(name))

    def test_body_damage_uses_filtered_input(self):
        self.assertIn(self.q['derivedPreparation.derivedStatInput'], self.targets('WitcherActor.calculateAttackStats'))
        self.assertIn('bodyDamage', self.data.processes['proc-000177']['steps'][0]['summary'])

    def test_resource_routing_and_no_persistence(self):
        self.assertIn(self.q['derivedStatData.RESOURCE_STATS'], self.targets('parameterPreparation.parameterTarget', 'reads'))
        self.assertIn(self.q['parameterPreparation.actor.parameterModifiers'], self.targets('derivedPreparation.calculateDerivedParameter', 'writes'))
        for name in ['derivedPreparation.calculateDerivedParameter', 'derivedPreparation.derivedStatInput']:
            self.assertFalse(any('update' in self.data.entities[e]['qualified_name'].lower() for e in self.targets(name)))

    def test_definition_locations_and_retired_relations(self):
        for name in ['derivedStatData.isManualDerivedStat', 'derivedStatData.derivedStatBase', 'derivedPreparation.derivedStatInput', 'derivedPreparation.calculateDerivedParameter']:
            e = self.data.entities[self.q[name]]; loc = e['location']
            line = (ROOT / self.data.sources[loc['source']]['path']).read_text().splitlines()[loc['line_start'] - 1]
            self.assertIn('function ' + name.split('.')[-1] + '(', line)
        for p in self.data.processes.values():
            for s in p['steps']:
                self.assertTrue(all(r in self.data.relations for r in s['relations']))

    def test_navigation_has_process_and_current_report(self):
        eid = self.q['derivedPreparation.calculateDerivedParameter']
        self.assertTrue(any(p['entry']['entity'] == eid for p in self.data.processes.values()))
        result = self.data.query(query.parser().parse_args(['details', eid, '--no-verify']))
        self.assertTrue(any(r.get('path') == 'docs/analytics/task-0010-005-checks.md' for r in result['items']))
