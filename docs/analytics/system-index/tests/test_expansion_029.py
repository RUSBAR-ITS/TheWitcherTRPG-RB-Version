"""Проверки справочника по исходникам; игровые документы и БД не исполняются."""
import collections
import hashlib
import json
import re
import unittest
from pathlib import Path
from test_query import BASE, ROOT, query, run_cli

class ProfessionExecutionExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l)for l in(BASE/f'data/{k}/expansion-029.jsonl').read_text().splitlines()]for k in ['entities','relations','processes']}
    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]]if r['kind']==kind]
    def test_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-029-queries.json').read_text())['cases']
        self.assertEqual(len(cases),35)
        self.assertEqual({c['question']for c in cases},{f'IQ-{n:02}'for n in range(1,9)})
        for c in cases:
            with self.subTest(case=c['id']):
                run=run_cli([*c['command'],'--format','json'],cwd='/tmp');self.assertEqual(run.returncode,0,run.stderr)
                out=json.loads(run.stdout);rows=out['items'];first=rows[0]if rows else{}
                actual=dict(ids=[r['id']for r in rows if'id'in r],from_ids=sorted({r['from']for r in rows if'from'in r}),to_ids=sorted({r['to']for r in rows if'to'in r}),next_steps=[v['step']for v in first.get('next',[])if'step'in v],next_exits=[v['exit']for v in first.get('next',[])if'exit'in v],depth_limited=out.get('traversal',{}).get('depth_limited'),resolution=first.get('boundary',{}).get('kind'),refs=[v['path']for v in rows if'path'in v])
                for key,value in c['expected'].items():
                    if key.startswith('includes_'):self.assertTrue(set(value)<=set(actual[key[9:]]),(key,actual))
                    else:self.assertEqual(actual[key],value,key)
                self.assertEqual(out['freshness']['state'],'current');self.assertEqual(out['coverage']['state'],'partial')

    def body(self,a,b):return '\n'.join(self.source(20)[a-1:b])
    def targets(self,q,kind):return {r['to']for r in self.edges(q,kind)}
    def test_address_correction_and_method_owners(self):
        event=self.data.entities['ent-004885'];s=self.data.sources[event['location']['source']]
        self.assertEqual(s['path'],'module/actor/sheets/mixins/skillMixin.js')
        self.assertIn("jQuery.find('.profession-roll').on('click', event => thisActor._onProfessionRoll(event))",self.source(45)[30])
        for i in ['rel-013327','rel-013328','rel-013329']:self.assertEqual(self.data.relations[i]['location']['source'],'src-000045')
        for name,a,b in [('doProfessionAttackRoll',45,230),('doProfessionWeaponAttackRoll',232,260),('doProfessionSkillUsage',262,321),('doProfessionThreshold',323,349),('doProfessionSkillRoll',351,379)]:
            e=self.data.entities[self.q['actor.professionMixin.'+name]];self.assertEqual(e['location']['line_start'],a);self.assertEqual(e['location']['line_end'],b)
            self.assertIn('async '+name+'(',self.body(a,b))
        old=self.data.entities['ent-000875'];self.assertEqual((old['kind'],old['owner']),('function','src-000020'))
        for q in ['calc_total_skills_profession','findSkillWithName','findSkillWithNameInSkillPath','_onProfessionRoll']:self.assertIn('actor.professionMixin.'+q,self.q)
    def test_dispatch_and_regular_roll_await_boundaries(self):
        c='actor.professionMixin';s=self.body(30,43);self.assertNotIn('await ',s);self.assertNotIn('return ',s)
        self.assertLess(s.index('isAttack'),s.index('hasCustomEffect'));self.assertLess(s.index('hasCustomEffect'),s.index('hasThresholds'))
        self.assertIn("this.findSkillWithName(name).skill",s)
        self.assertTrue({self.q[c+'.'+n]for n in ['doProfessionAttackRoll','doProfessionWeaponAttackRoll','doProfessionSkillRoll','doProfessionSkillUsage','doProfessionThreshold']} <= set(self.q.values()))
        r=self.body(351,379)
        for snippet in ['skill.level || 0','this.system.stats[stat].value','CONFIG.WITCHER.statMap[stat].label','await getCustomModifier','new ChatMessageData(this.actor','return extendedRoll(rollFormula, messageData, config)']:self.assertIn(snippet,r)
        self.assertNotIn('addActiveEffects',r);self.assertNotIn('addAttackModifiers',r)
        ext='\n'.join(self.source(202));self.assertIn('evaluatedRoll.total > config.threshold',ext)
        d=self.data.processes['proc-000409'];self.assertTrue(all(s['next'][0]['flow']=='scheduled'for s in d['steps'][2:]))
        self.assertEqual(self.data.processes['proc-000410']['steps'][-1]['next'][0]['flow'],'await')
    def test_attack_controls_and_payload_are_separate_from_documents(self):
        c='actor.professionMixin.doProfessionAttackRoll';h='\n'.join(self.source(507));cb=self.body(118,137)
        names=['isExtraAttack','location','targetOutsideLOS','outsideLOS','isProne','isPinned','isActivelyDodging','isMoving','isAmbush','isBlinded','isSilhouetted','customAtt','damageType','customDmg']
        self.assertEqual(len(re.findall(r'form\.elements\.\w+\.checked',cb)),10)
        self.assertEqual(len(re.findall(r'form\.elements\.\w+\.value',cb)),4)
        for name in names:
            self.assertRegex(h,r'name=["\']'+name+r'["\']');self.assertIn('form.elements.'+name+'.',cb)
            self.assertIn(self.q['profession-attack.hbs.input['+name+']'],self.targets(c+'/prompt.ok.callback','reads'))
        s=self.body(45,230)
        self.assertIn('this.addActiveEffects(attack.name)',s);self.assertNotIn('itemUuid',s);self.assertNotIn('this.update(',s)
        self.assertIn("new ChatMessageData(this, messageDataFlavor, 'attack'",s);self.assertIn('await extendedRoll(attFormula, messageData)',s)
        schema='\n'.join(self.source(100));self.assertIn('itemUuid:',schema);self.assertNotIn('item:',schema);self.assertNotIn('defenseOptions:',schema)
        self.assertIn(self.q['AttackMessageData'],self.targets(c+'.messageData','passes'))
    def test_weapon_chooser_delegates_existing_attack_without_await(self):
        s=self.body(232,260)
        for snippet in ["item.type === 'weapon'",'weapon.system.attackOptions.has([...skill.skillAttack.attackOptions][0])','button.form.elements.choosen.value','this.items.get(itemId)','skillReplacement: skill','additionalDamageProperties: skill.skillAttack.damageProperties']:self.assertIn(snippet,s)
        self.assertNotIn('isStored',s);self.assertNotIn('equipped',s);self.assertNotIn('await this.weaponAttack',s);self.assertNotIn('return this.weaponAttack',s)
        w='\n'.join(self.source(25));self.assertIn('if (options.skillReplacement)',w);self.assertIn('this.constructBaseAttackFormula',w)
        e=self.targets('actor.weaponAttackMixin.weaponAttack','reads');self.assertTrue({self.q['professionSkill().stat'],self.q['professionSkill().level']}<=e)
        p=self.data.processes['proc-000413'];self.assertEqual(p['steps'][-1]['next'][0]['flow'],'scheduled')
    def test_threshold_choice_occurs_before_roll_including_empty_prompt(self):
        s=self.body(323,349)
        for snippet in ['Object.entries(skill.thresholds.thresholds)','thresholds.length == 1','<select id="threshold">','button.form.elements.threshold.value','threshold: skill.thresholds.thresholds[choosenThreshold].value']:self.assertIn(snippet,s)
        self.assertNotIn('.sort(',s);self.assertNotIn('await this.doProfessionSkillRoll',s)
        p=self.data.processes['proc-000411'];self.assertEqual([n['step']for n in p['steps'][0]['next']if 'step'in n],['launch','prompt'])
        self.assertEqual(p['steps'][-1]['next'][0]['flow'],'scheduled')
    def test_temporary_health_target_dc_payload_and_delivery(self):
        source='\n'.join(self.source(20));s=source[source.index('async doProfessionSkillUsage'):source.index('async doProfessionThreshold')];c='actor.professionMixin.doProfessionSkillUsage'
        for snippet in ['game.user.targets.first()?.actor','target = this','targetStat.max * temporaryHealth.difficultyCheck.multiplier','await this.doProfessionSkillRoll','showResult: false','await roll.toMessage(roll.messageData)','roll.options.rollOver > 0',"value.includes('d')",'new ActiveEffect','duration: { rounds: duration }','await createEffectDelivery','actorUuid: target.uuid','effects: [newEffect]']:
            self.assertIn(snippet,s)
        self.assertNotIn('getActorOwner',s);self.assertNotIn('queryData',s);self.assertNotIn('this.update(',s)
        self.assertIn('value: `{"name": "${skill.skillName}", "value": ${value}}`',s)
        self.assertIn('icon:',s)
        self.assertIn(self.q['TemporaryEffects.temporaryHp'],self.targets(c+'.newEffect','passes'))
        self.assertNotIn(self.q['TemporaryEffects.temporaryHp'],self.targets(c,'writes'))
        self.assertIn(self.q['effectDelivery.createEffectDelivery'],self.targets(c+'.deliveryPayload','passes'))
        self.assertIn(self.q['effectDelivery.reportDeliveryConsequence'],self.targets(c,'calls'))

    def test_core_and_issue_evidence_are_not_runtime_confirmation(self):
        for e in json.loads((BASE/'examples/expansion-029-queries.json').read_text())['core_evidence']:self.assertEqual(hashlib.sha256(Path(e['path']).read_bytes()).hexdigest(),e['sha256'])
        for q,n in [('attack-without-item-uuid',239),('temporary-health-payload',294),('regular-speaker',236),('weapon-selection',242),('threshold-selection',115)]:
            e=self.data.entities[self.q['actor.professionMixin/'+q]];self.assertEqual(e['boundary']['kind'],'dynamic');self.assertIn(f'docs/issues/potential/issue-{n:05}.md',{r['path']for r in e['refs']})
        self.assertEqual(self.data.processes['proc-000416']['steps'][1]['next'][0]['flow'],'unknown')
        for s in [20,507,121,29,526,572,144,145,146]:self.assertEqual(self.data.sources[f'src-{s:06}']['coverage']['definitions']['state'],'partial')
    def test_graph_addresses_reverse_edges_facets_and_processes(self):
        d=self.data
        for e in self.new['entities']:
            if e['kind']=='boundary':continue
            defs=[r for r in d.incoming[e['id']]if r['kind']=='defines'];self.assertEqual(len(defs),1);self.assertEqual(defs[0]['from'],e['owner'])
            l=e['location'];self.assertLessEqual(l['line_end'],len(self.source(int(l['source'][4:]))))
            self.assertIn(e['id'],d.sources[l['source']]['coverage']['definitions']['included'])
        for r in self.new['relations']:
            self.assertIn(r,d.outgoing[r['from']]);self.assertIn(r,d.incoming[r['to']]);l=r['location'];self.assertLessEqual(l['line_end'],len(self.source(int(l['source'][4:]))))
            self.assertIn(r['id'],d.sources[l['source']]['coverage']['relations']['included'])
        for p in self.new['processes']:
            steps={s['id']:s for s in p['steps']};todo=[p['steps'][0]['id']];seen=set();exits=set()
            while todo:
                n=todo.pop()
                if n in seen:continue
                seen.add(n)
                for edge in steps[n]['next']:
                    if'step'in edge:todo.append(edge['step'])
                    else:exits.add(edge['exit'])
            self.assertEqual(seen,set(steps));self.assertEqual(exits,{e['id']for e in p['exits']})
            for s in p['steps']:
                for rid in s['relations']:self.assertEqual(d.relations[rid]['from'],s['entity'])
                self.assertIn(p['id'],d.sources[s['location']['source']]['coverage']['processes']['included'])
        # Historical portion counts, not a cap on later extensions.
        self.assertEqual({k:len(v)for k,v in self.new.items()},{'entities':51,'relations':253,'processes':8})

if __name__=='__main__':unittest.main()
