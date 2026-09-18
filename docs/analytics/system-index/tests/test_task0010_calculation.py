"""Адресная навигация TASK-0010.004; численные результаты проверяются игровым кодом отдельно."""
import unittest
from test_query import ROOT, query

class ParameterCalculationIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}

    def edges(self, name, kind):
        return [r for r in self.data.outgoing[self.q[name]]if r['kind']==kind]

    def test_one_stats_pass_and_no_old_weight_duplication(self):
        calls=self.edges('WitcherActor.prepareDerivedData','calls')
        self.assertEqual(sum(r['to']==self.q['WitcherActor.calculateStats']for r in calls),1)
        self.assertIn(self.q['parameterPreparation.prepareSkillParameters'],{r['to']for r in calls})
        calls=self.edges('WitcherActor.calculateStats','calls')
        self.assertEqual(sum(r['to']==self.q['WitcherActor.calculateStat']for r in calls),1)
        proc=self.data.processes['proc-000004']
        self.assertNotIn('stats-second',{s['id']for s in proc['steps']})

    def test_numeric_route_reaches_shared_contract(self):
        for owner,target in [('WitcherActiveEffect.shouldApplyChange','parameterPreparation.routesParameterChange'),
                             ('parameterPreparation.parameterTarget','modifierContext.supportsModifierChange'),
                             ('parameterPreparation.prepareParameterInputs','WitcherActiveEffect.shouldApplyChange'),
                             ('parameterPreparation.calculateActorParameter','parameterCalculation.calculateParameter'),
                             ('parameterCalculation.calculateParameter','parameterCalculation.calculateOperations')]:
            self.assertIn(self.q[target],{r['to']for r in self.edges(owner,'calls')})

    def test_transient_state_has_reset_and_writer_but_not_document_update(self):
        self.assertIn(self.q['parameterPreparation.resetParameterPreparation'],{r['to']for r in self.edges('WitcherActor.prepareBaseData','calls')})
        self.assertIn(self.q['parameterPreparation.actor.parameterModifiers'],{r['to']for r in self.edges('parameterPreparation.calculateActorParameter','writes')})
        for owner in ['parameterPreparation.prepareParameterInputs','parameterPreparation.calculateActorParameter']:
            self.assertFalse(any('update' in self.data.entities[r['to']]['qualified_name'].lower() for r in self.edges(owner,'calls')))

    def test_addresses_point_to_actual_definitions(self):
        names=['calculateOperations','calculateParameter','parameterTarget','routesParameterChange','resetParameterPreparation','prepareParameterInputs','calculateActorParameter','prepareSkillParameters']
        for name in names:
            prefix='parameterCalculation'if name in names[:2]else'parameterPreparation'
            entity=self.data.entities[self.q[prefix+'.'+name]];loc=entity['location']
            line=(ROOT/self.data.sources[loc['source']]['path']).read_text().splitlines()[loc['line_start']-1]
            self.assertIn('function '+name+'(',line)

    def test_query_can_reach_report_and_preparation_process(self):
        for name in ['WitcherActor.calculateStats','WitcherActiveEffect.shouldApplyChange','parameterCalculation.calculateParameter']:
            out=self.data.query(query.parser().parse_args(['details',self.q[name],'--no-verify']))
            self.assertTrue(any(x.get('path')=='docs/analytics/task-0010-004-checks.md'for x in out['items']))
        out=self.data.query(query.parser().parse_args(['processes',self.q['parameterPreparation.prepareParameterInputs'],'--no-verify']))
        self.assertIn('proc-000477', {x['id'] for x in out['items']})
