"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class InventoryExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-013.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_26_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-013-queries.json').read_text())['cases']
        self.assertEqual(len(cases),26)
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


    def test_definitions_and_schema_ownership(self):
        for name,n,line,literal in [
            ('WitcherActor.addItem',47,259,'async addItem'),('WitcherActor.removeItem',47,275,'async removeItem'),
            ('WitcherActor.useItem',47,225,'async useItem'),('item.consumeMixin.consume',157,4,'async consume'),
            ('consumable().isConsumable',136,7,'BooleanField'),('ConsumablePropertiesData.effects',137,11,'ArrayField'),
            ('itemEffect().percentage',142,7,'min: 0'),('WitcherConsumableConfigurationSheet._onEditEffect',184,49,'_onEditEffect')]:
            e=self.data.entities[self.q[name]];self.assertEqual((e['location']['source'],e['location']['line_start']),(f'src-{n:06}',line));self.assertIn(literal,self.source(n)[line-1])
        self.assertEqual(self.q['item.consumeMixin.consume'],'ent-000867')
        self.assertEqual(self.data.entities[self.q['CommonItemData.quantity']]['owner'],self.q['CommonItemData'])
        self.assertIn('StringField',self.source(109)[6])
        self.assertEqual({e['name'] for e in self.new['entities'] if e['owner']==self.q['ConsumablePropertiesData'] and e['kind']=='field'},{'doesHeal','heal','effects','removesEffects'})
        self.assertNotRegex('\n'.join(self.source(142)),r'\bid\s*:')
        self.assertNotIn('addsTempHp','\n'.join(self.source(137)))

    def test_stack_mutations_and_wait_boundaries(self):
        a=self.source(47)
        for n,t in [(260,'item.name == addItem.name && item.type == addItem.type'),(261,'!forcecreate && !foundItem.system.isStored'),
                    (265,'addItem.toObject()'),(267,'if (numberOfItem)'),(278,'newQuantity <= 0')]:self.assertIn(t,a[n-1])
        for n in [262,271,279,281]:self.assertIn('await',a[n-1])
        for n in [239,240,286]:self.assertNotIn('await',a[n-1])
        self.assertNotIn('await','\n'.join(a[285:290]));self.assertNotIn('if (!item)','\n'.join(a[274:283]))
        writers={r['from'] for r in self.data.incoming[self.q['CommonItemData.quantity']] if r['kind']=='writes' and r['location']['source']=='src-000047'}
        self.assertEqual(writers,{self.q['WitcherActor.addItem'],self.q['WitcherActor.removeItem']})
        self.assertNotIn('isStored','\n'.join(a[251:254]));self.assertIn('!i.system.isStored',a[255])
        self.assertFalse(any(r['kind']=='writes' and r['to']==self.q['CommonItemData.quantity'] and r['location']['source']=='src-000157' for r in self.data.relations.values()))

    def test_inventory_listener_and_current_rows(self):
        s=self.source(43)
        self.assertIn('this.actor.isOwner',s[7]);self.assertIn('await this.actor.removeItemsOfType',s[19]);self.assertIn('item.system.equipped = true',s[23])
        self.assertIn('await this.actor.update(allSkills)',s[37]);self.assertNotIn('await',s[51]);self.assertNotIn('await',s[53])
        self.assertIn("value == 'false'",s[136]);self.assertIn("value == 'true'",s[139]);self.assertNotIn('dtype','\n'.join(s[127:145]))
        self.assertIn("element.dataset.itemtype == 'diagram'",s[96])
        events=[e for e in self.new['entities'] if e['kind']=='event' and e['owner']==self.q['sheet.itemMixin.itemListener']]
        self.assertEqual(len(events),23)
        for e in events:
            self.assertTrue(any(r['kind']=='handles' for r in self.data.incoming[e['id']]),e['qualified_name'])
        summ='\n'.join(self.source(551));self.assertIn('{{#if hasQuantity}}',summ);self.assertNotIn('<input',summ);self.assertNotIn('data-subtype',summ)
        self.assertIn('data-itemType=',summ);self.assertIn('data-spellType=',summ)
        templates=[r for r in self.data.incoming[self.q['CommonItemData.quantity']] if r['kind']=='reads' and r['location']['source'] in {f'src-{n:06}' for n in range(552,560)}]
        self.assertEqual(len(templates),8)
        for r in templates:self.assertIn('data-field="system.quantity"',self.source(int(r['location']['source'][4:]))[r['location']['line_start']-1])

    def test_consume_delegation_hp_and_message(self):
        s=self.source(157);self.assertIn('await this.actor.calculateHealValue',s[7])
        for n in [9,13,14,15,16]:self.assertNotIn('await',s[n-1])
        self.assertIn("this.actor.uuid, this.uuid, 'applySelf'",s[14]);self.assertNotIn('duration',s[14])
        self.assertNotIn('quantity','\n'.join(s));self.assertNotIn('percentage','\n'.join(s))
        self.assertEqual({r['to'] for r in self.edges('item.consumeMixin.consume','calls')},{self.q[x] for x in ['actor.healMixin.calculateHealValue','Document.update/Actor','WitcherActor.applyStatus','WitcherActor.removeStatus','applyActiveEffectToActorViaId','item.consumeMixin.createConsumeMessage']})
        self.assertIn('hp.max',self.source(17)[6]);self.assertIn('parseInt',s[7]);self.assertIn('await',s[28]);self.assertNotIn('await',s[39])
        self.assertNotIn('removesEffects','\n'.join(self.source(496)))

    def test_menu_socket_query_and_actor_identity(self):
        s=self.source(34)
        self.assertIn('onClick: this.consumeItem',s[36]);self.assertIn('callback: this.giftItem',s[93]);self.assertIn('pointerEvent, target',s[116])
        self.assertNotIn('quantity','\n'.join(s[41:57]));self.assertIn('rejectClose: true',s[138]);self.assertIn('hasPlayerOwner',s[121])
        for n in [144,146,149]:self.assertNotIn('await',s[n-1])
        self.assertIn("emitForGM('addItem', [receiver, item, 1])",s[145])
        self.assertIn("'addItem': 'uuid'",self.source(217)[5]);self.assertIn('message.data.shift()',self.source(217)[16]);self.assertNotIn('await',self.source(217)[17])
        incoming=[r for r in self.data.incoming[self.q['WitcherActor.addItem']] if r['kind']=='calls']
        self.assertIn(self.q['registerSocketListeners/message'],{r['from'] for r in incoming});self.assertIn(self.q['query'],{r['from'] for r in incoming})
        self.assertNotIn(self.q['query'],{r['to'] for r in self.edges('sheet.itemContextMenu.giftItem','calls')})

    def test_consumable_configuration_failure_boundaries(self):
        s=self.source(184);h=self.source(591)
        self.assertIn('push({ percentage: 100 })',s[44]);self.assertIn('obj.id == itemId',s[63]);self.assertIn('effects[objIndex][field] = value',s[64]);self.assertIn('item.id !== itemId',s[75])
        for n in [46,67,77]:self.assertIn('this.item.update',s[n-1]);self.assertNotIn('await',s[n-1])
        self.assertIn("value == 'on'",s[58]);self.assertIn('checked',s[59]);self.assertIn('addsTempHp',h[8]);self.assertIn('data-id="{{effect.id}}"',h[19])
        for q in ['ConsumablePropertiesData/itemEffect.id','ConsumablePropertiesData/addsTempHp']:
            self.assertEqual(self.data.entities[self.q[q]]['kind'],'boundary');self.assertEqual(self.data.entities[self.q[q]]['boundary']['kind'],'dynamic')
        writes=self.edges('WitcherConsumableConfigurationSheet._onEditEffect','writes');self.assertTrue(any('objIndex' in r.get('condition','') for r in writes))

    def test_external_core_contracts(self):
        text=(BASE/'coverage-013.md').read_text();rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',text,re.M)
        self.assertEqual(len(rows),3)
        for path,digest in rows:self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)
        core=Path('/opt/foundryvtt');menu=(core/'client/applications/ux/context-menu.mjs').read_text()
        self.assertIn('item.onClick(event, this.#target)',menu);self.assertIn('this.#target, event)',menu)
        self.assertIn('toObject(source=true)',(core/'common/abstract/data.mjs').read_text())
        h=(core/'client/applications/handlebars.mjs').read_text();self.assertIn('Non-existent data field provided',h);self.assertIn('return Handlebars.SafeString("")',h)

    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[142,552,21])
        # Historical .013 totals remain assertions over its immutable ID allocation.
        historical={k:[r for r in getattr(d,k).values() if int(r['id'].split('-')[1])<=cap]
                    for k,cap in [('entities',3696),('relations',8459),('processes',155)]}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,3696,8459,155])
        represented={e['location']['source'] for e in historical['entities'] if e['kind']!='boundary' and e.get('location')}
        self.assertEqual(len(represented),197)
        self.assertEqual(615-len(represented),418)
        self.assertTrue(represented <= {s for s,v in d.sources.items() if v['coverage']['definitions']['included']})
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

if __name__=='__main__':unittest.main()
