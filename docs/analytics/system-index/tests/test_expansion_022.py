"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class HealingExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-022.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_32_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-022-queries.json').read_text())['cases']
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


    def test_formula_and_three_callers_are_separate(self):
        s=self.source(17);chat=self.source(193);c=self.source(157)
        for at,t in [(4,"value.includes && value.includes('d')"),(5,'await new Roll(value).evaluate()'),(7,'parseInt(this.system.derivedStats.hp.value) + parseInt(heal)'),(8,'parseInt(this.system.derivedStats.hp.max) - parseInt(this.system.derivedStats.hp.value)'),(9,': heal')]:self.assertIn(t,s[at-1])
        self.assertNotIn('.update(', '\n'.join(s));self.assertIn('parseInt(await this.actor.calculateHealValue',c[7]);self.assertIn('parseInt(',chat[26]);self.assertNotIn('calculateHealValue','\n'.join(chat));self.assertNotIn('new Roll','\n'.join(chat))
        incoming={r['from']for r in self.data.incoming[self.q['actor.healMixin.calculateHealValue']]if r['kind']=='calls'}
        self.assertEqual(incoming,{self.q[n]for n in ['item.consumeMixin.consume','applyCombatEffect']})

    def test_dialog_flags_and_source_scoped_controls(self):
        s=self.source(42);h='\n'.join(self.source(513))
        for at,t in [(7,'Math.floor(rec.max / 2)'),(12,'isResting: false'),(13,'isSterilized: false'),(43,').render({ force: true })'),(45,'restDialogListener(document'),(54,'Math.floor(rec.max / 2)'),(57,'totalRec = rec.max'),(58,'dialogData.isResting = true'),(62,'totalRec += 2'),(63,'dialogData.isSterilized = true'),(66,'totalRec += 3'),(68,'totalRec += 2'),(74,"isSterilized ? '' : 'invisible'")]:self.assertIn(t,s[at-1])
        body='\n'.join(s[47:76]);self.assertNotIn('isResting = false',body);self.assertNotIn('isSterilized = false',body);self.assertNotIn('dialogData.isHealingHand',body);self.assertNotIn('dialogData.isHealingTent',body)
        for key in ['resting','sterilized','healing-hand','healing-tent']:self.assertIn('id="'+key+'"',h)
        self.assertNotIn('checked',h)
        regs=self.edges('sheet.healMixin.restDialogListener','registers');self.assertEqual(len(regs),4)
        for r in regs:self.assertTrue(self.data.entities[r['to']]['qualified_name'].endswith('.change'))

    def test_rest_resources_and_trauma_wait_boundaries(self):
        s=self.source(42);h='\n'.join(self.source(494));body='\n'.join(s[77:102])
        self.assertIn('await this.actor.update',s[78]);self.assertIn('Math.min(',s[79]);self.assertIn("'system.derivedStats.sta.value': this.actor.system.derivedStats.sta.max",s[83]);self.assertIn("'system.derivedStats.vigor.value': this.actor.system.derivedStats.vigor.max",s[84]);self.assertNotIn('if (isResting)',body)
        self.assertIn('forEach(crit => crit.system.heal',s[87]);self.assertNotIn('await',s[87]);self.assertIn('ChatMessage.create',s[89]);self.assertNotIn('await',s[89]);self.assertIn('content: await',s[90])
        self.assertNotIn('actualWoundList','\n'.join(s));self.assertIn('actualWoundList',h);self.assertNotIn('vigor',h);self.assertIn('{{totalRec}}',h)
        p=next(p for p in self.new['processes']if p['entry']['entity']==self.q['sheet.healMixin.recoverActor']);ss={x['id']:x for x in p['steps']}
        self.assertEqual(ss['resources']['next'][0]['flow'],'await');self.assertEqual(ss['wounds']['next'][0]['flow'],'scheduled');self.assertEqual(self.steps(331)['heal']['next'][0]['flow'],'scheduled')

    def test_chat_target_report_and_actual_button(self):
        s=self.source(193);h='\n'.join(self.source(485));spell=self.source(487)
        for at,t in [(27,'parseInt(event.currentTarget.getAttribute'),(30,'fromUuidSync(actorUuid)'),(32,'game.user.targets.first()?.actor ?? canvas.tokens.controlled[0]?.actor ?? game.user.character'),(33,'if (!target) return'),(39,'target?.update'),(41,'actor.name'),(45,'getSpeaker({ actor: actor })')]:self.assertIn(t,s[at-1])
        self.assertNotIn('await','\n'.join(s[25:48]));self.assertNotIn('button',h);self.assertIn('data-heal="{{damage.heal}}"',spell[51]);self.assertIn('data-actor="{{templateInfo.actor.uuid}}"',spell[52])
        self.assertEqual({r['to']for r in self.edges('onHeal','reads')if self.data.entities[r['to']]['qualified_name'].startswith('spellItem.hbs/button.heal/')},{self.q[n]for n in ['spellItem.hbs/button.heal/data-heal','spellItem.hbs/button.heal/data-actor']})

    def test_regeneration_and_periodic_heal_do_not_share_guards(self):
        s=self.source(196);a='\n'.join(s[10:38]);b='\n'.join(s[79:87])
        for at,t in [(12,"actor.type != 'monster'"),(13,'actor.system.regeneration === 0'),(14,"actor.statuses.has('dead')"),(16,'await foundry.applications.handlebars.renderTemplate'),(30,'ChatMessage.create'),(32,'actor.update'),(80,'status.heal && status.heal.amount > 0'),(81,'await actor.calculateHealValue(status.heal.amount)'),(82,'if (healedFor > 0)'),(83,'await actor.update'),(84,'await actor.createHealMessage')]:self.assertIn(t,s[at-1])
        self.assertNotIn('await',s[29]);self.assertNotIn('await',s[31]);self.assertNotIn('modifier',b);self.assertNotIn("'dead'",b);self.assertNotIn('regeneration <=',a)
        self.assertIn('actor.system.derivedStats.hp.value',self.source(486)[3]);self.assertIn('actor.system.regeneration',self.source(486)[4]);self.assertIn('{ actor: this.actor }',self.source(17)[17])
        self.assertEqual({r['from']for r in self.data.incoming[self.q['actor.healMixin.createHealMessage']]if r['kind']=='calls'},{self.q['applyCombatEffect']})

    def test_death_threshold_counter_and_no_death_writer(self):
        s=self.source(41);x=self.source(202)
        for at,t in [(8,"'system.deathSaves': 0"),(13,'this.actor.system.deathSaves + 1'),(18,'this.actor.system.derivedStats.hp.value > 0'),(19,'this.actor.system.derivedStats.stun.value'),(20,'Math.floor((this.actor.system.stats.body.max + this.actor.system.stats.will.max) / 2)'),(22,'Math.min(stunBase, 10)'),(24,'stunBase -= this.actor.system.deathSaves'),(37,'config.reversal = true'),(38,'config.showSuccess = true'),(39,'config.showCrit = false'),(42,'await extendedRoll(`1d10`, messageData, config)')]:self.assertIn(t,s[at-1])
        self.assertIn('config.threshold >= 0',x[64]);self.assertIn('evaluatedRoll.total < config.threshold',x[70]);self.assertNotIn('showSuccess','\n'.join(x));self.assertNotIn('.update','\n'.join(s[15:43]));self.assertNotIn('dead','\n'.join(s[15:43]).lower().replace('deathsaves',''))
        writes=self.edges('sheet.deathsaveMixin._onDeathSaveRoll','writes');self.assertEqual({r['to']for r in writes},{self.q['RollConfig.'+n]for n in ['reversal','showSuccess','showCrit','threshold']})
        self.assertNotIn('heal-button','\n'.join(self.source(564)));self.assertIn('heal-button','\n'.join(self.source(520)))

    def test_old_processes_and_identity_preserved(self):
        self.assertEqual(self.data.entities[self.q['onHeal']]['id'],'ent-004410');self.assertEqual(self.data.entities[self.q['applyMonsterRegeneration']]['id'],'ent-004414');self.assertEqual(self.data.entities[self.q['sheet.healMixin.recoverActor']]['id'],'ent-004501')
        self.assertEqual([s['id']for s in self.data.processes['proc-000311']['steps']],['guard','render','message','damage-guard','payload','damage','heal-handoff'])
        self.assertEqual(self.steps(149)['heal']['next'][0]['flow'],'await');self.assertEqual(self.steps(149)['hp']['next'][0]['flow'],'scheduled')
        self.assertEqual({r['to']for r in self.edges('sheet.healMixin.recoverActor/criticalWound.forEach','calls')},{self.q['CriticalWoundData.heal']})

    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[51, 203, 19])
        self.assertEqual([len(d.sources),len(d.entities),len(d.relations),len(d.processes)],[615, 4579, 11808, 353])
        self.assertEqual(len(d.manifest['scope']['selected_sources']),149)
        self.assertEqual(collections.Counter(s['coverage']['definitions']['state'] for s in d.sources.values()),{'complete':2,'partial':250,'not_indexed':363})
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

