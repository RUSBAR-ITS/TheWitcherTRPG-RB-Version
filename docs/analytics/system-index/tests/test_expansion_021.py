"""Адресная навигация травм .00049; сервер и браузер не исполняются."""
import json
import unittest
from test_query import BASE, ROOT, query

class CriticalWoundExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}

    def edges(self,name,kind):
        return [r for r in self.data.outgoing[self.q[name]] if r['kind']==kind]

    def test_32_source_grounded_routes(self):
        cases=json.loads((BASE/'examples/expansion-021-queries.json').read_text())['cases']
        self.assertEqual(len(cases),32)
        self.assertEqual({c['question']for c in cases},{f'IQ-{i:02}'for i in range(1,9)})
        for c in cases:
            with self.subTest(case=c['id']):
                out=self.data.query(query.parser().parse_args([*c['command'],'--no-verify']))
                rows=out['items']
                actual=dict(ids=[r['id']for r in rows if 'id'in r],from_ids=sorted({r['from']for r in rows if 'from'in r}),to_ids=sorted({r['to']for r in rows if 'to'in r}),refs=[r['path']for r in rows if 'path'in r])
                for k,v in c['expected'].items():
                    if k.startswith('includes_'):self.assertTrue(set(v)<=set(actual[k[9:]]),(k,actual))
                    elif k.startswith('excludes_'):self.assertFalse(set(v)&set(actual[k[9:]]),(k,actual))
                    else:self.assertEqual(actual[k],v)

    def test_model_delegates_and_old_effect_path_is_gone(self):
        model=(ROOT/'module/data/item/criticalWoundData.js').read_text()
        for n in ['followUp: new fields.', 'healingTime: new fields.', 'calculateHealingTime(']:self.assertNotIn(n,model)
        for method,op in [('heal','healWound'),('treat','transitionWound'),('stabilize','transitionWound')]:
            self.assertIn(self.q['criticalWoundOperations.'+op],{r['to']for r in self.edges('CriticalWoundData.'+method,'calls')})
        self.assertNotIn(self.q['CriticalWoundData.treat'],{r['to']for r in self.edges('CriticalWoundData.heal','calls')})
        self.assertFalse(self.edges('criticalWoundOperations.evaluateHealingDuration','writes'))

    def test_manual_game_and_native_guards_are_navigable(self):
        for name,callee in [('actor.damageMixin.applyCritWound','selectInitialWound'),('actor.damageMixin.applyCritWound','installWound'),('WitcherActor.addItem','installWound'),('WitcherItem.createDocuments','createWoundDocuments'),('WitcherItem.updateDocuments','validateWoundUpdates')]:
            self.assertIn(self.q['criticalWoundOperations.'+callee],{r['to']for r in self.edges(name,'calls')})
        service=(ROOT/'module/item/criticalWoundOperations.js').read_text()
        self.assertIn('replace.create(expected.effects)',service)
        self.assertIn('getIndex({',service)
        self.assertNotIn('this.parent.createEmbeddedDocuments', (ROOT/'module/data/item/criticalWoundData.js').read_text())

    def test_ui_flags_and_single_list(self):
        table=(ROOT/'templates/partials/crit-wounds-table.hbs').read_text()
        for flag in ['cannotStabilize','cannotTreat']:self.assertIn('unless critWound.system.'+flag,table)
        sheet=(ROOT/'module/actor/sheets/mixins/criticalWoundMixin.js').read_text()
        self.assertIn('event.currentTarget',sheet);self.assertNotIn('_onCriticalWoundRemove',sheet)
        self.assertIn(self.q['CriticalWoundData.stabilize'],{r['to']for r in self.edges('sheet.criticalWoundMixin._onTreat','calls')})

    def test_content_has_new_fields_and_safe_final_stages(self):
        docs=[json.loads(p.read_text()) for p in (ROOT/'packsJson/criticalWounds').rglob('*.json')]
        wounds=[d for d in docs if d.get('type')=='criticalWound'];self.assertEqual(len(wounds),94);self.assertEqual(len(docs),98)
        keys=set()
        for d in wounds:
            s=d['system'];key=(s['woundTypeId'],s['location'],s['treatment']);self.assertNotIn(key,keys);keys.add(key)
            self.assertNotIn('followUp',s);self.assertNotIn('healingTime',s)
            if s['treatment']=='treated':self.assertTrue(s['cannotTreat']);self.assertEqual(s['canHeal'],s['criticalLevel']!='deadly')

    def test_changed_graph_locations_and_process_links(self):
        d=self.data
        changed={'proc-000316','proc-000322','proc-000323','proc-000324','proc-000328','proc-000329'}
        changed.update(json.loads(line)['id']for line in (BASE/'data/processes/task-0009-lifecycle.jsonl').read_text().splitlines())
        for p in d.processes.values():
            if p['id'] not in changed:continue
            for st in p['steps']:
                loc=st['location'];source=ROOT/d.sources[loc['source']]['path']
                self.assertLessEqual(loc['line_end'],len(source.read_text().splitlines()))
                for rid in st['relations']:
                    r=d.relations[rid];self.assertEqual(r['from'],st['entity']);self.assertEqual(r['location']['source'],loc['source']);self.assertTrue(loc['line_start']<=r['location']['line_start']<=loc['line_end'])
