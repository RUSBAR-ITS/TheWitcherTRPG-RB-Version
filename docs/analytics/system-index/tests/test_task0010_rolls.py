"""Навигация контекста броска .007; арифметика проверяется настоящим JS отдельно."""
import unittest
from test_query import ROOT, query

class RollContextIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset();cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
    def targets(self,name,kind='calls'):
        return {r['to']for r in self.data.outgoing[self.q[name]]if r['kind']==kind}
    def test_all_combat_entry_points_share_formatting(self):
        for name in ['actor.modifierMixin.addAttackModifiers','actor.modifierMixin.addDefenseModifiers','actor.defenseMixin.addDefenseModifiers']:
            self.assertIn(self.q['combatModifierFormula'],self.targets(name))
        self.assertIn(self.q['rollModifiers.formatRollModifier'],self.targets('addPart'))
    def test_collector_and_dialog_are_connected_without_global_roll_injection(self):
        self.assertIn(self.q['rollContext.collectRollModifiers'],self.targets('conditionalModifiers.chooseRollModifiers'))
        self.assertIn(self.q['rollContext.resolveRollModifiers'],self.targets('conditionalModifiers.chooseRollModifiers'))
        self.assertIn(self.q['parameterCalculation.calculateParameter'],self.targets('rollContext.resolveRollModifiers'))
        self.assertNotIn(self.q['rollContext.collectRollModifiers'],self.targets('extendedRoll'))
    def test_new_locations_point_to_real_definitions(self):
        for name in ['rollContext.resolveRollTarget','rollContext.collectRollModifiers','rollContext.resolveRollModifiers','conditionalModifiers.chooseRollModifiers','rollModifiers.formatRollModifier','combatModifierFormula']:
            e=self.data.entities[self.q[name]];loc=e['location'];line=(ROOT/self.data.sources[loc['source']]['path']).read_text().splitlines()[loc['line_start']-1]
            self.assertIn('function '+name.split('.')[-1]+'(',line)
    def test_dialog_has_explicit_skip_and_cancel_exits(self):
        p=next(p for p in self.data.processes.values()if p['entry']['entity']==self.q['conditionalModifiers.chooseRollModifiers']);steps={s['id']:s for s in p['steps']}
        for name in ['empty','cancel']:self.assertIn('done',{n.get('exit')for n in steps[name]['next']})
        self.assertTrue(all(n['flow']=='await'for n in steps['prompt']['next']))
    def test_threshold_and_unchecked_template_document_current_contract(self):
        self.assertIn('null',self.data.entities[self.q['RollConfig.threshold']]['summary'])
        steps={s['id']:s for s in self.data.processes['proc-000012']['steps']};self.assertIn('Number.isFinite',steps['threshold']['summary']);self.assertIn('T<=1',steps['reversed']['summary'])
        renders=self.targets('conditionalModifiers.chooseRollModifiers','renders');self.assertEqual({self.data.sources[s]['path']for s in renders},{'templates/dialog/conditional-modifiers.hbs'})
    def test_scope_remains_partial_and_report_is_reachable(self):
        e=self.data.entities[self.q['rollContext.collectRollModifiers']];self.assertTrue(any(r['path']=='docs/analytics/task-0010-007-checks.md'for r in e['refs']))
        s=self.data.sources[e['location']['source']];self.assertEqual(s['coverage']['definitions']['state'],'partial')
