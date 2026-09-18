"""Проверки справочника по исходникам; игровые документы и БД не исполняются."""
import collections
import hashlib
import json
import re
import unittest
from pathlib import Path
from test_query import BASE, ROOT, query, run_cli

class SkillDevelopmentExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l)for l in(BASE/f'data/{k}/expansion-030.jsonl').read_text().splitlines()]for k in ['entities','relations','processes']}
    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]]if r['kind']==kind]
    def test_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-030-queries.json').read_text())['cases']
        self.assertEqual(len(cases),36)
        self.assertEqual({c['question']for c in cases},{f'IQ-{n:02}'for n in range(1,9)})
        for c in cases:
            with self.subTest(case=c['id']):
                out=self.data.query(query.parser().parse_args([*c['command'],'--no-verify']));rows=out['items'];first=rows[0]if rows else{}
                actual=dict(ids=[r['id']for r in rows if'id'in r],from_ids=sorted({r['from']for r in rows if'from'in r}),to_ids=sorted({r['to']for r in rows if'to'in r}),next_steps=[v['step']for v in first.get('next',[])if'step'in v],next_exits=[v['exit']for v in first.get('next',[])if'exit'in v],depth_limited=out.get('traversal',{}).get('depth_limited'),resolution=first.get('boundary',{}).get('kind'),refs=[v['path']for v in rows if'path'in v])
                for key,value in c['expected'].items():
                    if key.startswith('includes_'):self.assertTrue(set(value)<=set(actual[key[9:]]),(key,actual))
                    else:self.assertEqual(actual[key],value,key)
                self.assertEqual(out['coverage']['state'],'partial') # Freshness checked once by the stage verifier.

    def body(self,s,a=1,b=None):return '\n'.join(self.source(s)[a-1:b])
    def targets(self,q,kind):return {r['to']for r in self.edges(q,kind)}
    def test_schema_and_separate_level_stores(self):
        for s,patterns in [(54,['improvementPoints:','magicImprovementPoints:','logs: new fields.EmbeddedDataField(Log)']), (69,['label:','ip:','isMagic:']), (72,['name:','value:']), (86,['value:','get modifiedValue()']), (124,['value:']), (148,['level:'])]:
            for text in patterns:self.assertIn(text,self.body(s))
        self.assertEqual(self.body(54).count('new fields.SchemaField(skillTraining())'),4)
        for s in [69,72]:
            for text in ['min:','max:','integer:']:self.assertNotIn(text,self.body(s))
        level='parameterAdvancement.purchaseParameter'
        self.assertIn(self.q['Skill.value'],self.targets(level,'writes'))
        self.assertNotIn(self.q['SkillItemData.value'],self.targets(level,'writes'))
        self.assertNotIn(self.q['professionSkill().level'],self.targets(level,'writes'))
    def test_level_price_and_single_awaited_purchase(self):
        text=(ROOT/'module/actor/parameterAdvancement.js').read_text()
        self.assertIn('await actor.update(patch)',text)
        self.assertNotIn('logs.addIpReward(',text)
        self.assertIn('parameterAdvancement.purchaseParameter',self.q)
        self.assertIn(self.q['parameterAdvancement.purchaseParameter'],self.targets('actor.skillMixin.levelUpSkill','calls'))
        self.assertNotIn(self.q['Log.addIpReward'],self.targets('actor.skillMixin.levelUpSkill','calls'))
        p=self.data.processes['proc-000417']
        self.assertEqual(p['steps'][-1]['next'][0]['flow'],'await')
        self.assertEqual(p['steps'][-1]['entity'],self.q['parameterAdvancement.purchaseParameter'])
    def test_log_push_absolute_updates_and_no_returned_promise(self):
        s=self.body(70,14,29)
        for text in ['this.ipLog.push({ label: label, ip: ip, isMagic: isMagic })','if (!isMagic)','if (isMagic)','this.parent.improvementPoints + ip','this.parent.magic.magicImprovementPoints + ip']:self.assertIn(text,s)
        self.assertEqual(s.count('this.parent.parent.update('),2)
        for text in ['async ','await ','return ','this.parent.improvementPoints =']:self.assertNotIn(text,s)
        writes=self.targets('Log.addIpReward','writes')
        self.assertTrue({self.q[q]for q in ['Log.ipLog','ipLog().label','ipLog().ip','ipLog().isMagic','CharacterData.improvementPoints','CharacterData.magic.magicImprovementPoints']}<=writes)
        p=self.data.processes['proc-000418'];self.assertEqual([x['step']for x in p['steps'][1]['next']],['ordinary','magic'])
    def test_manual_controls_training_dom_and_builtin_button_are_distinct(self):
        h=self.body(527);magic=self.body(525);spend=self.body(29,452,458)
        self.assertIn('name="system.improvementPoints"',h);self.assertIn('name="system.magic.magicImprovementPoints"',magic)
        for n in range(1,5):
            for f in ['name','value']:self.assertIn(f'name="system.skillTraining{n}.{f}"',h)
        self.assertEqual(h.count('saveIpSpending'),4)
        for text in ['event.currentTarget.parentElement.children','siblings.item(0).value','siblings.item(1).value < 0 ? siblings.item(1).value : siblings.item(1).value * -1','this.actor.system.logs.addIpReward(label, value)']:self.assertIn(text,spend)
        for text in ['await ','skillTraining','levelUpSkill','this.actor.update']:self.assertNotIn(text,spend)
        self.assertNotIn('data-action="level-up"',h);self.assertIn('data-action="level-up"',self.body(542))
        self.assertIn("thisActor.levelUpSkill(skill.dataset.skill)",self.body(45))
        self.assertNotIn(self.q['Log.addIpReward'],self.targets('WitcherCharacterSheet/IP-training-form-submit','calls'))
    def test_api_and_recipient_selection_do_not_use_common_actor_helper(self):
        for s,text in [(4,'ip: Rewards.handoutIpRewards'),(21,'game.api.rewards.ip([this])'),(49,'game.actors.filter(actor => actor.hasPlayerOwner)'),(49,'if (!actors)'),(49,'if (!game.user.isGM) return')]:self.assertIn(text,self.body(s))
        r=self.body(49,1,88)
        for text in ['getInteractActor','getActorOwner','actor.type','user.active']:self.assertNotIn(text,r)
        self.assertIn('await Rewards.ipRewardDialog(actors)',r)
        self.assertNotIn('await ',self.body(21,2,4));self.assertNotIn('return ',self.body(21,2,4))
        self.assertIn(self.q['game.api.rewards.ip'],self.targets('actor.rewardsMixin.addIpReward','calls'))
    def test_dialog_types_cancellation_and_handout_guards(self):
        dialog=self.body(49,10,55);hand=self.body(49,57,88);helper=self.body(48,1,11)
        for text in ["type: 'checkboxes'","name: 'actors'","'text', 'label'","'number', 'ip'","'checkbox', 'isMagic'",'await DialogV2.input','return values']:self.assertIn(text,dialog)
        for text in ['rejectClose','isGM','min =','max =','required =']:self.assertNotIn(text,dialog+helper)
        for text in ['!values || !values.actors || values.actors.length === 0','values.actors.map(actor => fromUuidSync(actor))','actor.system.logs.addIpReward(label, ip, values.isMagic)','await foundry.applications.handlebars.renderTemplate','ChatMessage.create(chatData)']:self.assertIn(text,hand)
        self.assertEqual(hand.count('if (ip)'),2)
        self.assertNotIn('await ChatMessage.create',hand);self.assertNotIn('await actor.system.logs',hand)
        self.assertNotIn('isMagic',self.body(49,72,79));self.assertNotIn('isMagic',self.body(505))
        p=self.data.processes['proc-000423'];self.assertEqual([x['exit']for x in p['steps'][2]['next']if'exit'in x],['cancelled','failed'])
        p=self.data.processes['proc-000424'];self.assertEqual([x['step']for x in p['steps'][1]['next']if'step'in x],['grant','render'])
    def test_rewards_sheet_only_reads_ip_history(self):
        h=self.body(575)
        for text in ['system.logs.ipLog','ipLog.label','ipLog.ip','ipLog.isMagic']:self.assertIn(text,h)
        for text in ['<input','<button','data-action']:self.assertNotIn(text,h)
        self.assertIn('new RewardsSheet({ document: this.actor })',self.body(29))
        self.assertIn('context.system = this.document.system',self.body(26))
        self.assertIn('submitOnChange: true',self.body(26))
        self.assertFalse(self.edges('templates/sheets/actor/rewards/ip.hbs','writes'))
        self.assertTrue({self.q[q]for q in ['Log.ipLog','ipLog().label','ipLog().ip','ipLog().isMagic']}<=self.targets('templates/sheets/actor/rewards/ip.hbs','reads'))
    def test_core_issue_evidence_and_partial_limits(self):
        for e in json.loads((BASE/'examples/expansion-030-queries.json').read_text())['core_evidence']:self.assertEqual(hashlib.sha256(Path(e['path']).read_bytes()).hexdigest(),e['sha256'])
        for q,n in [('Log.addIpReward/pending-absolute-updates',28),('WitcherCharacterSheet._saveIpSpending/negative-string',200),('Rewards.handoutIpRewards/recipient-contract',233)]:
            e=self.data.entities[self.q[q]];self.assertEqual(e['boundary']['kind'],'dynamic');self.assertIn(f'docs/issues/potential/issue-{n:05}.md',{r['path']for r in e['refs']})
        for s in [22,45,29,69,70,72,26,49,21,527,525,575,574,54]:self.assertEqual(self.data.sources[f'src-{s:06}']['coverage']['definitions']['state'],'partial')
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
        # TASK-0010.006 retires obsolete local variables/guards, not their IDs.
        self.assertTrue({'ent-004949','ent-004950','ent-004951','ent-004952','ent-004995'}.isdisjoint(d.entities))

if __name__=='__main__':unittest.main()
