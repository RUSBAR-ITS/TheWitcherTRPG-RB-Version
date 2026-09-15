"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class DefenseExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-016.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_28_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-016-queries.json').read_text())['cases']
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


    def test_choice_delegation_inline_controls_and_professional_override(self):
        s=self.source(16);t='\n'.join(s)
        for a,token in [(19,'item.system.isApplicableDefense?.(attack.attackOption)'),(20,'item.createDefenseOption(attack)'),(23,'CONFIG.WITCHER.defenseOptions.find'),(28,"option.value != 'parry'"),(35,'action: option.value'),(39,'isExtraDefense.checked'),(40,'customDef.value'),(47,'await DialogV2.wait'),(67,"item.system.meleeAttackSkill ?? 'melee'"),(78,'chooser.length == 1'),(81,'chooser.length > 1'),(85,'data-itemId="${option.itemId}"'),(89,'await DialogV2.prompt'),(95,'choosenDefense.value'),(96,'dataset.itemid'),(104,'return this.skillDefense'),(119,'defenseAction.skillOverride')]:self.assertIn(token,s[a-1])
        self.assertNotIn('isStored','\n'.join(s[17:20]));self.assertNotIn('equipped','\n'.join(s[17:20]))
        self.assertEqual(t.count('rejectClose: true'),2);self.assertNotIn('chooser.length == 0',t)
        w=self.source(160);self.assertIn('label: this.name',w[3]);self.assertIn('value: this.name',w[4]);self.assertIn('...this.system.createDefenseOption?.(attack.attackOption)',w[5])
        prof='\n'.join(self.source(121)[48:114]);self.assertNotIn('isDefense',prof);self.assertNotIn('definingSkill',prof);self.assertIn('skillOverride:',prof);self.assertIn('value: this[path][skill].level',prof)
        for name in ['WeaponData.createDefenseOption','item.defenseOptionMixin.createDefenseOption','actor.defenseMixin.prepareAndExecuteDefense']:
            self.assertLess(int(self.q[name].split('-')[1]),4024)
        target=self.q['actor.defenseMixin.prepareAndExecuteDefense']
        self.assertEqual({r['to'] for r in self.data.outgoing[target] if r['kind']=='calls' and r['location']['line_start']==19},{self.q['WeaponData.isApplicableDefense'],self.q['ProfessionData.isApplicableDefense']})

    def test_defense_formula_cost_and_independent_roll_configuration(self):
        s=self.source(16);formula='\n'.join(s[130:185])
        self.assertLess(formula.index('this.handleExtraDefense'),formula.index('let skillMapEntry'))
        for a,token in [(138,'this.system.stats[skillMapEntry.attribute.name].value'),(139,'skillOverride?.skill ??'),(156,'weapon?.system.defenseProperties?.parrying'),(158,'Math.abs(modifier)'),(169,"customDef != '0'"),(180,'this.addActiveEffects(skillName)'),(181,'this.addDefenseModifiers()'),(183,"skillName != 'resistmagic'"),(184,"rollFormula = '10[Stun]'"),(259,'sta.value - 1'),(260,'newSta < 0'),(265,"'system.derivedStats.sta.value': newSta"),(281,"action === 'parrythrown'")]:self.assertIn(token,s[a-1])
        self.assertNotIn('await','\n'.join(s[256:270]));self.assertIn("value: 'parryThrown'",self.source(209)[252])
        own='\n'.join(s[248:255]);self.assertIn('Object.values(this.system.combatEffects.defenseModifier)',own);self.assertIn('` ${mod.value}',own)
        self.assertIn('TypedObjectField',self.source(74)[12])
        q='actor.defenseMixin.skillDefense';out={r['to'] for r in self.edges(q,'calls')};self.assertIn(self.q['actor.defenseMixin.addDefenseModifiers'],out);self.assertNotIn(self.q['actor.modifierMixin.addDefenseModifiers'],out)
        self.assertIn('config.showResult = false',s[293]);self.assertIn('config.defense = true',s[294]);self.assertIn('config.threshold = totalAttack',s[295])
        self.assertIn('evaluatedRoll.total >= config.threshold',self.source(202)[67]);self.assertIn('evaluatedRoll.total < config.threshold',self.source(202)[70])
        self.assertFalse(any(p['entry']['entity']==self.q['extendedRoll'] for p in self.new['processes']))

    def test_crit_thresholds_raw_model_distinction_and_locations(self):
        s=self.source(16);crit='\n'.join(s[309:353]);triples=re.findall(r"criticalLevel: '(\w+)',\s+critdamage: (\d+),\s+bonusdamage: (\d+)",crit)
        self.assertEqual(triples,[('deadly','10','20'),('difficult','8','15'),('complex','5','10'),('simple','3','5')])
        for a,n in [(315,7),(316,10),(317,13),(318,15)]:self.assertIn(f'totalAttack - {n}',s[a-1])
        for a,t in [(207,'await this.handleCritLocation(attackDamageObject)'),(208,'attackDamageObject.location = crit.location'),(209,'crit.critEffectModifier = attackDamageObject.crit.critEffectModifier'),(356,"originalLocation.includes('random')"),(357,"new Roll('2d6+' + attackDamageObject.crit.critLocationModifier)"),(393,'return attackDamageObject.location')]:self.assertIn(t,s[a-1])
        self.assertNotIn('RollTable','\n'.join(s));self.assertEqual(sum('getRandomInt(2)' in line for line in s[355:395]),2)
        d=self.source(97);self.assertNotIn('critEffectModifier','\n'.join(d));self.assertIn('modifier: new fields.NumberField()',d[29]);self.assertIn('modifier: new fields.StringField',self.source(101)[7])
        self.assertIn('critLocationModifier: new fields.NumberField()',self.source(99)[4]);self.assertIn('critEffectModifier: new fields.NumberField()',self.source(99)[5])
        for e in self.new['entities']:
            if e['kind']!='field' or e['owner']!=self.q['DefenseMessageData'] or e['name']=='metadata':continue
            l=e['location'];self.assertRegex(d[l['line_start']-1],r'\b'+re.escape(e['name'])+r'\s*:',e['qualified_name'])
        self.assertEqual({r['to'] for r in self.edges('DefenseMessageData.defineSchema','calls')},{self.q['BaseMessageData.defineSchema']})
        self.assertEqual({r['location']['line_start'] for r in self.edges('actor.defenseMixin.checkForCrit','computes') if r['to']==self.q['DefenseMessageData.crit.critdamage']},{323,331,339,347})

    def test_message_order_hit_block_and_stun_are_distinct(self):
        s=self.source(16)
        for a,t in [(194,'new ChatMessageData'),(195,'attackWeaponProperties: attackDamageObject.properties'),(196,'defender: this.uuid'),(197,'defense: skillName'),(200,'await extendedRoll('),(213,"getActorOwner(attackerActor).query('TheWitcherTRPG.query'"),(228,'messageData.append('),(230,'this.checkForStun(attackDamageObject)'),(239,'messageData.append('),(241,'await roll.toMessage(messageData)'),(243,'this.handleDefenseResults('),(398,'roll.total < totalAttack'),(402,"'applyOnHit'"),(403,'attackDamageObject.duration'),(406,"this.removeStatus([{ statusEffect: 'stun' }])"),(409,"applyStatusEffectToActor(attacker, 'staggered', 1)"),(419,"'system.reliability'"),(424,"'system.reliable'")]:self.assertIn(t,s[a-1])
        for a in [213,243,264,399,406,409,419,424,454]:self.assertNotIn('await',s[a-1])
        self.assertNotIn('roll','\n'.join(s[300:308]));self.assertNotIn('Math.max','\n'.join(s[396:431]))
        self.assertNotRegex('\n'.join(s[416:419]),r'if\s*\(!item')
        self.assertIn('this.applyStatus',s[453]);self.assertNotIn('removeStatus','\n'.join(s[432:456]))
        steps=self.steps(198);self.assertEqual(steps['message']['next'][0]['flow'],'await');self.assertEqual(steps['adrenaline']['next'][0]['flow'],'scheduled');self.assertEqual(steps['message']['next'][0]['step'],'results')
        self.assertEqual({r['to'] for r in self.edges('actor.defenseMixin.handleDefenseResults','writes')},{self.q['ArmorData.reliability'],self.q['WeaponData.reliable']})

    def test_static_context_random_maps_and_selected_consumers(self):
        s=self.source(47);w=self.source(18)
        self.assertEqual(w[4].strip(),'return WitcherActor.getAllLocations();');self.assertNotIn('.call(','\n'.join(w));self.assertIn("this.type == 'monster' && this.system.hasTailWing",s[294])
        self.assertEqual(s[345].strip(),'let randomMonsterLocation = getRandomInt(10);');self.assertIn("location = 'leftLeg'",s[365]);self.assertIn("location = 'tailWing'",s[369])
        self.assertNotIn('hasTailWing','\n'.join(s[301:435]));self.assertNotIn('location =','\n'.join(s[421:426]))
        self.assertIn('modifier = `+0`',s[303]);self.assertIn('formula = 0.5',s[419]);self.assertNotIn('modifier =','\n'.join(s[417:421]))
        self.assertIn('Math.floor(Math.random() * max) + 1',self.source(198)[73]);self.assertIn('this.getAllLocations().map',self.source(14)[85])
        self.assertEqual(self.q['WitcherActor.getLocationObject'],'ent-003946');self.assertEqual(self.q['actor.locationMixin.getLocationObject'],'ent-003945')
        self.assertEqual({r['to'] for r in self.edges('actor.locationMixin.getAllLocations','calls')},{self.q['WitcherActor.getAllLocations']})

    def test_chat_controls_fumble_and_external_dialog_contract(self):
        s=self.source(195)
        self.assertIn('stunSave(message.system.attackWeaponProperties.stun)',s[28]);self.assertIn('stunSave()',s[34]);self.assertIn('getInteractActor()',s[28]);self.assertNotIn('defender','\n'.join(s[25:38]))
        for a,n in [(75,'applyCritDamage'),(83,'applyBonusCritDamage'),(91,'applyCritWound')]:self.assertIn(n+'(game.messages.get(target.dataset.messageId).system.crit)',s[a-1])
        for n in [482,483,484]:self.assertNotIn('data-','\n'.join(self.source(n)))
        self.assertIn('displayFormula',self.source(482)[1]);self.assertIn('crit.criticalLevel',self.source(483)[2]);self.assertIn('stun.modifier',self.source(484)[1])
        f='\n'.join(self.source(203)[74:93]);self.assertIn('message.system.defender',f);self.assertIn('fumbleAmount < 9',f);self.assertIn('unarmedAttackDefense(fumbleAmount)',f);self.assertNotIn('await',f)
        self.assertTrue(any(r['to']==self.q['defenseFumble'] for r in self.edges('applyFumble/defenseFumble','refers')))
        core=Path('/opt/foundryvtt/client/applications/api/dialog.mjs').read_text().splitlines();self.assertIn('!options.buttons?.length',core[192]);self.assertIn('options.buttons.reduce',core[193]);self.assertIn('obj[button.action] = button',core[195])
        rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',(BASE/'coverage-016.md').read_text(),re.M);self.assertEqual(len(rows),1)
        for path,digest in rows:self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)

    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[98,339,22])
        # Historical .016 range; omitted duplicate3706 remains absent.
        historical={k:[r for r in getattr(d,k).values() if int(r['id'].split('-')[1])<=cap]
                    for k,cap in [('entities',4121),('relations',9766),('processes',211)]}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,4120,9766,211])
        represented={e['location']['source'] for e in historical['entities'] if e['kind']!='boundary' and e.get('location')}
        self.assertEqual(len(represented),224)
        self.assertEqual(615-len(represented),391)
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

