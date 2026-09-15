"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class CriticalWoundExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-021.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_32_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-021-queries.json').read_text())['cases']
        self.assertEqual(len(cases),32)
        self.assertEqual({c['question'] for c in cases},{f'IQ-{n:02}' for n in range(1,9)})
        for c in cases:
            with self.subTest(case=c['id']):
                run=run_cli([*c['command'],'--format','json'],cwd='/tmp')
                self.assertEqual(run.returncode,0,run.stderr)
                out=json.loads(run.stdout);rows=out['items'];first=rows[0] if rows else {}
                actual=dict(ids=[x['id'] for x in rows if 'id' in x],
                    from_ids=sorted({x['from'] for x in rows if 'from' in x}),
                    to_ids=sorted({x['to'] for x in rows if 'to' in x}),
                    next_steps=[x['step'] for x in first.get('next',[]) if 'step' in x],
                    next_exits=[x['exit'] for x in first.get('next',[]) if 'exit' in x],
                    resolution=first.get('boundary',{}).get('kind'),refs=[x['path'] for x in rows if 'path' in x])
                for key,value in c['expected'].items():
                    if key.startswith('includes_'):self.assertTrue(set(value)<=set(actual[key[9:]]),(key,actual))
                    elif key.startswith('excludes_'):self.assertFalse(set(value)&set(actual[key[9:]]),(key,actual))
                    else:self.assertEqual(actual[key],value,key)
                self.assertEqual(out['freshness']['state'],'current')
                self.assertEqual(out['coverage']['state'],'partial')


    def test_schema_owner_and_prepared_time_are_distinct(self):
        s=self.source(112);a=self.source(14)
        for at,t in [(26,'daysHealed: new fields.NumberField({ initial: 0 })'),(27,'healingTime: new fields.NumberField({ initial: 0 })'),(30,'followUp: new fields.DocumentUUIDField'),(31,"type: 'Item'"),(43,'this.calculateHealingTime(actor)')]:self.assertIn(t,s[at-1])
        self.assertNotRegex('\n'.join(s[9:36]),r'\b(quantity|choices|integer|min|htmlFields)\s*:')
        for at,n in [(50,8),(53,12),(56,15)]:self.assertIn(f'this.healingTime = Math.max({n} - actor.system.stats.body.max, 1)',s[at-1])
        for at,n in [(349,8),(351,12),(353,15)]:self.assertIn(f'return Math.max({n} - this.system.stats.body.max, 1)',a[at-1])
        self.assertNotIn('default:', '\n'.join(s[46:59]+a[345:355]))
        x=self.data.entities[self.q['CriticalWoundData.calculateHealingTime']];y=self.data.entities[self.q['actor.damageMixin.calculateHealingTime']]
        self.assertNotEqual(x['owner'],y['owner']);self.assertFalse([r for r in self.data.incoming[y['id']]if r['kind']=='calls'])
        self.assertEqual({r['to']for r in self.edges('CriticalWoundData.calculateHealingTime','computes')},{self.q['CriticalWoundData.healingTime']})

    def test_pick_and_repeat_keep_real_failure_boundaries(self):
        s=self.source(14);a=self.source(47);schema=self.source(97)
        for at,t in [(316,"game.settings.get('TheWitcherTRPG', 'criticalWoundsPack')"),(317,"criticalWound.system.treatment == 'none'"),(318,'location.name'),(319,'crit.criticalLevel'),(323,'possibleWounds.length == 1'),(326,'crit.location.critEffect ?? getRandomInt(6) + crit.critEffectModifier'),(328,'criticalWound.system.lesserEffect === false'),(330,'criticalWound.system.lesserEffect === true'),(335,'await fromUuid(wound.uuid)'),(336,'this.addItem(wound)'),(343,'ChatMessage.create(chatData)')]:self.assertIn(t,s[at-1])
        self.assertNotIn('await',s[335]);self.assertNotIn('critEffectModifier','\n'.join(schema))
        self.assertIn('foundItem', '\n'.join(a[259:273]));self.assertIn('Number',a[261]);self.assertNotIn('treatment','\n'.join(a[258:273]))
        count=self.steps(316)['count'];self.assertEqual([e['step']for e in count['next']if'step'in e],['resolve','roll'])
        self.assertEqual(self.steps(316)['resolve']['next'][0]['flow'],'await');self.assertEqual(self.steps(316)['add']['next'][0]['flow'],'scheduled')

    def test_heal_threshold_is_outside_treated_and_writes_conditional(self):
        s=self.source(112)
        for at,t in [(69,"this.treatment == 'treated'"),(70,'this.daysHealed += 1'),(71,'sterilized && !this.sterilized'),(72,'this.daysHealed += 2'),(75,"'system.sterilized': true"),(80,"'system.daysHealed': this.daysHealed"),(84,"this.daysHealed >= this.healingTime && this.criticalLevel != 'deadly'"),(86,'this.treat()'),(88,'if (Object.keys(updates))'),(89,'this.parent.update(updates)')]:self.assertIn(t,s[at-1])
        self.assertNotIn('await','\n'.join(s[66:92]));self.assertNotRegex('\n'.join(s[66:92]),r'this\.sterilized\s*=')
        steps=self.steps(322);self.assertEqual([e['step']for e in steps['state']['next']if'step'in e],['day','threshold'])
        for n in ['transition','persist']:self.assertEqual(steps[n]['next'][0]['flow'],'scheduled')
        self.assertEqual({r['to']for r in self.edges('CriticalWoundData.heal','writes')},{self.q['CriticalWoundData.'+n]for n in ['daysHealed','sterilized']})
        self.assertFalse(self.edges('CriticalWoundData.treat','writes'))

    def test_followup_wait_and_effect_lifecycle_are_not_atomic(self):
        s=self.source(112)
        for at,t in [(95,'if (this.followUp)'),(97,'await fromUuid(this.followUp)'),(98,"actor.createEmbeddedDocuments('Item', [followUpItem])"),(101,'this.parent.delete()')]:self.assertIn(t,s[at-1])
        self.assertEqual(sum('await'in l for l in s[93:102]),1)
        self.assertNotIn('effects','\n'.join(s[93:102]));self.assertNotIn('criticalLevel','\n'.join(s[93:102]))
        steps=self.steps(323);self.assertEqual(steps['load']['next'][0]['flow'],'await')
        for n in ['create','delete']:self.assertEqual(steps[n]['next'][0]['flow'],'scheduled')
        self.assertEqual({r['to']for r in self.edges('CriticalWoundData.treat','calls')},{self.q[x]for x in ['fromUuid','Document.createEmbeddedDocuments','Document.delete/Item']})
        self.assertTrue(any(r['to']==self.q['Actor.allApplicableEffects']for r in self.edges('criticalWound/effect-lifecycle','refers')))
        self.assertIn('canHaveTemporaryItemImprovement',self.source(531)[6])

    def test_ui_identifiers_drop_and_two_views(self):
        m=self.source(38);h=self.source(530);f=self.source(599);tab=self.source(562);drop=self.source(167)
        self.assertIn('event.target.dataset.id',m[14]);self.assertIn('_onCriticalWoundRemove',m[23])
        self.assertFalse([e for e in self.data.entities.values()if e['qualified_name'].endswith('._onCriticalWoundRemove')])
        self.assertIn('data-item-id="{{critWound.id}}"',h[3]);self.assertIn('data-id="{{critWound.uuid}}"',h[34]);self.assertIn('data-field="system.daysHealed"',h[24]);self.assertIn('disabled',h[27])
        self.assertNotIn('delete-crit','\n'.join(h+tab));self.assertIn('crit-wounds-table.hbs',tab[7]);self.assertIn('criticalWound',tab[10])
        self.assertNotIn('sterilized','\n'.join(f));self.assertIn('formGroup systemFields.followUp',f[33]);self.assertIn("'system.followUp': item.uuid",drop[18]);self.assertNotIn('await','\n'.join(drop[16:21]))
        self.assertTrue(any(r['from']==self.q['sheet.itemMixin._onItemInlineEdit']and r['kind']=='writes'for r in self.data.incoming[self.q['CriticalWoundData.daysHealed']]))
        self.assertIn('crit.system.heal({ sterilized: isSterilized })',self.source(42)[87])

    def test_three_export_documents_are_evidence_not_runtime_pack(self):
        paths=['Sprained_Leg__Left__XPoH413WkKQUgrnw','Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5','Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3']
        docs=[json.loads((ROOT/'packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l'/f'{p}.json').read_text())for p in paths]
        self.assertEqual([d['system']['treatment']for d in docs],['none','stabilized','treated'])
        self.assertEqual([d['system']['location']for d in docs],['leftLeg','leftLeg','leftArm'])
        for i,d in enumerate(docs):
            self.assertEqual(d['type'],'criticalWound');self.assertEqual(len(d['effects']),1);self.assertTrue(d['effects'][0]['transfer']);self.assertFalse(d['effects'][0]['disabled'])
            self.assertEqual(d['system']['followUp'],f"Compendium.TheWitcherTRPG.criticalWounds.Item.{docs[i+1]['_id']}"if i<2 else None)
        refs=[r['to']for r in self.edges('criticalWound/export-not-pack','refers')if r['to'].startswith('src-')];self.assertEqual(len(refs),3)
        for sid in refs:self.assertFalse(self.data.sources[sid]['coverage']['definitions']['included'])

    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[55, 212, 21])
        self.assertEqual([len(d.sources),len(d.entities),len(d.relations),len(d.processes)],[615, 4528, 11605, 334])
        self.assertEqual(len(d.manifest['scope']['selected_sources']),142)
        self.assertEqual(collections.Counter(s['coverage']['definitions']['state'] for s in d.sources.values()),{'complete':2,'partial':244,'not_indexed':369})
        actor_processes=d.query(query.parser().parse_args(['processes','src-000047','--limit','100','--no-verify']))
        added={p['id'] for p in actor_processes['items'] if 135<=int(p['id'].split('-')[1])<=155}
        self.assertEqual(added,{'proc-000135','proc-000136','proc-000137','proc-000138','proc-000139','proc-000150'})
        for e in self.new['entities']:
            if e['location']:
                l=e['location'];self.assertLessEqual(l['line_end'],len(self.source(int(l['source'][4:]))))
            if e['kind']=='boundary':continue
            defs=[r for r in d.incoming[e['id']] if r['kind']=='defines'];self.assertEqual(len(defs),1,e['id']);self.assertEqual(defs[0]['from'],e['owner'])
        for r in d.relations.values():self.assertIn(r,d.outgoing[r['from']]);self.assertIn(r,d.incoming[r['to']])
        for p in self.new['processes']:
            ss={s['id']:s for s in p['steps']};todo=[p['steps'][0]['id']];seen=set();exits=set()
            while todo:
                name=todo.pop()
                if name in seen:continue
                seen.add(name)
                for n in ss[name]['next']:
                    if 'step' in n:todo.append(n['step'])
                    else:exits.add(n['exit'])
            self.assertEqual(seen,set(ss));self.assertEqual(exits,{e['id'] for e in p['exits']},p['id'])
            for st in ss.values():
                for rid in st['relations']:
                    r=d.relations[rid];self.assertEqual(r['from'],st['entity']);self.assertEqual(r['location']['source'],st['location']['source']);self.assertTrue(st['location']['line_start']<=r['location']['line_start']<=st['location']['line_end'])
            out=d.query(query.parser().parse_args(['processes',p['entry']['entity'],'--limit','100','--no-verify']));self.assertIn(p['id'],{r['id'] for r in out['items']})
        for sid,s in d.sources.items():
            expected={'definitions':{e['id'] for e in d.entities.values() if e['kind']!='boundary' and (e.get('location')or{}).get('source')==sid},'relations':{r['id'] for r in d.relations.values() if (r.get('location')or{}).get('source')==sid},'processes':{p['id'] for p in d.processes.values() if any(st['location']['source']==sid for st in p['steps'])}}
            for facet,ids in expected.items():self.assertEqual(set(s['coverage'][facet]['included']),ids,(sid,facet))

