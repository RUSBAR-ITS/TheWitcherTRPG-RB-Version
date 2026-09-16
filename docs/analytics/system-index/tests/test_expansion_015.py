"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class WeaponAttackExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-015.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_28_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-015-queries.json').read_text())['cases']
        self.assertEqual(len(cases),28)
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


    def test_schema_factories_payload_owners_and_prepared_statistics(self):
        for name,n,a,token in [('actor.attack(label)',58,4,'function attack(label)'),('chat.attackData()',98,3,'function attackData()'),('attackStats',59,5,'function attackStats()'),('AttackMessageData.attackRoll',94,28,'get attackRoll()')]:
            e=self.data.entities[self.q[name]];self.assertEqual((e['location']['source'],e['location']['line_start']),(f'src-{n:06}',a));self.assertIn(token,self.source(n)[a-1])
        for owner in ['actor.attack(label)','chat.attackData()','chat.damageData()','chat.critData()','chat.locationData()']:
            for e in self.data.entities.values():
                if e['kind']!='field' or e['owner']!=self.q[owner]:continue
                l=e['location'];self.assertRegex(self.source(int(l['source'][4:]))[l['line_start']-1],r'\b'+re.escape(e['name'])+r'\s*:',e['qualified_name'])
        self.assertEqual(self.q['WitcherActor.calculateAttackStats'],'ent-000287')
        s=self.source(47)
        for a,t in [(192,'Math.ceil((this.system.stats.body.value - 6) / 2) * 2'),(193,'meleeBonus += meleeBonus'),(194,'`1d6+${meleeBonus}`'),(195,'`1d6+${4 + meleeBonus}`')]:self.assertIn(t,s[a-1])
        self.assertNotIn('update','\n'.join(s[190:196]));self.assertIn('new fields.EmbeddedDataField(DamageProperties)',self.source(100)[15])
        for n in ['item','ammunition','duration']:self.assertNotRegex('\n'.join(self.source(100)),r'\b'+n+r'\s*:')
        self.assertIn('rollTotal',self.source(94)[28]);self.assertIn('messageData.system.rollTotal = evaluatedRoll.total',self.source(202)[61])

    def test_dialog_context_controls_actual_readers_and_css(self):
        h='\n'.join(self.source(510));s=self.source(25);callback='\n'.join(s[103:129])
        controls=set(re.findall(r'name="([^"]+)"',h));reads=set(re.findall(r'form\.elements\.(\w+)',callback))
        self.assertEqual(controls,reads);self.assertEqual(len(controls),20)
        self.assertEqual(callback.count('.checked'),12);self.assertEqual(len(re.findall(r'\??\.value',callback)),8)
        self.assertIn('ammunition?.value',callback);self.assertIn('weapon.system.range ?',callback)
        indexed={e['name'].split('.')[-1] for e in self.new['entities'] if e['qualified_name'].startswith('weapon-attack.form.')};self.assertEqual(indexed,controls)
        for e in self.new['entities']:
            if not e['qualified_name'].startswith('weapon-attack.form.'):continue
            self.assertIn('name="'+e['name']+'"',self.source(510)[e['location']['line_start']-1])
        ctx=[e for e in self.new['entities'] if e['qualified_name'].startswith('actor.weaponAttackMixin.weaponAttack/context.')];self.assertEqual(len(ctx),9)
        for e in ctx:self.assertRegex(s[e['location']['line_start']-1],r'\b'+re.escape(e['name'])+r'\s*[:,]')
        self.assertIn('{{{ammunitionOption}}}',h);self.assertNotRegex(h,r'\b(disabled|required|min)=')
        self.assertIn('(eq false item.system.type.piercing)',h);self.assertIn('item.system.type.piercing',h)
        self.assertIn('weapon_roll_sheet',h);self.assertIn('attack-sheet',h)
        for n,selector in [(479,'.weapon_roll_sheet input'),(447,'div.attack-sheet select')]:self.assertIn(selector,'\n'.join(self.source(n)))

    def test_resource_order_early_returns_and_output_await_boundaries(self):
        s=self.source(25)
        for a,t in [(36,'!attack.skill'),(135,'weapon.createBaseDamageObject()'),(144,'sta.value - 3'),(146,'newSta < 0'),(149,'this.update('),(156,'quantity - 1'),(157,'item.update('),(164,'newQuantity < 0'),(167,'weapon.update('),(177,'damage.properties.toObject(false)'),(179,'for ('),(301,'weapon.rollDamage(damage)'),(310,'await extendedRoll(attFormula, messageData)')]:self.assertIn(t,s[a-1])
        for a in [149,157,167,301]:self.assertNotIn('await',s[a-1])
        self.assertNotRegex('\n'.join(s[153:159]),r'if\s*\(.*[<>]')
        st=self.steps(180);self.assertIn('done',{e.get('exit') for e in st['throwable']['next']});self.assertIn('failed',{e.get('exit') for e in st['loop']['next']})
        self.assertEqual([x['flow'] for x in st['direct']['next']],['scheduled']);self.assertEqual(st['message']['next'][0]['flow'],'await')
        self.assertEqual({x.get('step') for x in st['output']['next']},{'direct','message'})
        writes=self.edges('actor.weaponAttackMixin.weaponAttack','writes')
        self.assertEqual({r['location']['line_start'] for r in writes if r['to']==self.q['CommonItemData.quantity']},{157,167})
        self.assertEqual({r['location']['line_start'] for r in writes if r['to']==self.q['DerivedStats.sta']},{150})
        self.assertIn('damage.properties.getPreprocessedEffects()',self.source(159)[46])
        self.assertEqual(self.data.entities[self.q['weaponAttack/rollOnlyDmg-properties']]['boundary']['kind'],'dynamic')

    def test_formula_signs_replacement_accumulation_and_selected_helpers(self):
        s=self.source(25)
        for a,t in [(11,'damageFormula'),(31,'options.skillReplacement'),(32,'attack.skill = options.skillReplacement.skillName'),(180,"'1d10+'"),(184,'options.skillReplacement.level ?? 0'),(187,'this.constructBaseAttackFormula(skill)'),(250,'customAim > 0'),(256,"customAtt != '0'"),(285,"customDmg != '0'"),(286,"damageFormula += !displayRollDetails"),(290,'damageFormula + damageModifcation'),(369,'CONFIG.WITCHER.weapon.attacks[strike]'),(370,'attackPenality'),(376,"this.system.lifepathModifiers.attacks[strike]")]:self.assertIn(t,s[a-1])
        replacement='\n'.join(s[181:185]);self.assertNotIn('addActiveEffects',replacement);self.assertNotIn('addAttackModifiers',replacement)
        self.assertEqual({r['to'] for r in self.edges('actor.weaponAttackMixin.constructBaseAttackFormula','calls')},{self.q['actor.modifierMixin.'+n] for n in ['addActiveEffects','addAttackModifiers']})
        self.assertIn('damage.location = touchedLocation',s[358]);self.assertIn('damage.originalLocation = location',s[359])
        self.assertNotIn('dmgMulti','\n'.join(s));self.assertIn('attackNumber: 2',self.source(209)[693])
        self.assertIn('formula',self.source(47)[431]);self.assertNotIn('roll',self.source(58)[6].lower())
        self.assertEqual(self.q['actor.weaponAttackMixin.mergeDamageProperties'],'ent-003886')
        for name in ['WitcherItem.getItemAttack','actor.weaponAttackMixin.mergeDamageProperties','extendedRoll']:
            self.assertFalse(any(p['entry']['entity']==self.q[name] for p in self.new['processes']))

    def test_fumble_separate_menu_localization_and_message_consumers(self):
        s=self.source(203)
        for a,t in [(5,'rolls[0]?.options.fumble'),(11,'applyFumble('),(18,'message.system.constructor'),(22,'case AttackMessageData'),(31,'message.system.attacker'),(52,'fumbleAmount < 7'),(54,'fumbleAmount < 9'),(62,"attack.attackOption === 'spell'"),(99,'fumbleAmount >= 6 && fumbleAmount < 9'),(101,'fumbleAmount > 9'),(109,"'WITCHER.fumbleResults.' + result"),(114,'ChatMessage.getSpeaker({ actor: actor })'),(118,'ChatMessage.create(chatData)')]:self.assertIn(t,s[a-1])
        self.assertNotIn('RollTable','\n'.join(s));self.assertNotIn('fromUuid','\n'.join(s));self.assertNotIn('await','\n'.join(s))
        for n in [25,202]:self.assertNotIn('applyFumble','\n'.join(self.source(n)))
        refs=[self.data.entities[r['to']] for r in self.edges('fumble/localization-result-key','refers')]
        self.assertTrue(refs);self.assertEqual({e['qualified_name'].split('::')[0] for e in refs},{'en','ru'})
        self.assertTrue(all('::WITCHER.fumbleResults.' in e['qualified_name'] for e in refs))
        c=self.source(195)
        for a,t in [(20,'fromUuidSync(message.system.attack.itemUuid)'),(23,'item.rollDamage(damage)'),(58,'actor.prepareAndExecuteDefense('),(62,'message.system.attackRoll')]:self.assertIn(t,c[a-1])
        self.assertNotIn('await',c[22]);self.assertNotIn('await',c[57])
        self.assertEqual({r['to'] for r in self.edges('onDamage','calls')},{self.q['fromUuidSync'],self.q['item.damageUtilMixin.rollDamage']})

    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[129,432,13])
        # Historical .015 range; omitted duplicate3706 remains absent.
        historical={k:[r for r in getattr(d,k).values() if int(r['id'].split('-')[1])<=cap]
                    for k,cap in [('entities',4023),('relations',9427),('processes',189)]}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,4022,9427,189])
        represented={e['location']['source'] for e in historical['entities'] if e['kind']!='boundary' and e.get('location')}
        self.assertEqual(len(represented),221)
        self.assertEqual(615-len(represented),394)
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

