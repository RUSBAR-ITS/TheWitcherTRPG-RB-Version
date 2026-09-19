"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class ChatDeliveryExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-020.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_32_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-020-queries.json').read_text())['cases']
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


    def test_chat_registration_is_separate_from_execution(self):
        entry='\n'.join(self.source(4));combat='\n'.join(self.source(195));chat='\n'.join(self.source(193))
        self.assertIn("Hooks.on('renderChatMessageHTML'",entry)
        for name in ['attackChatMessageListeners','defenseChatMessageListeners','chatMessageListeners']:
            self.assertIn(name+'(message, html)',entry)
        self.assertIn("html.querySelector('button.damage')?.addEventListener('click', _ => onDamage(message))",combat)
        for selector in ['button.stun','button.crit-stun']:
            self.assertIn("querySelectorAll('"+selector+"')",combat)
        for button in ['shield','heal','request-repair']:
            self.assertIn("querySelector('button."+button+"')",chat)
        self.assertIn('bindEffectDelivery(message, html)',chat)
        regs=[r for r in self.data.outgoing['ent-000629']if r['kind']=='registers']
        self.assertEqual({r['to']for r in regs},{self.q[x]for x in ['onShield','onHeal','onRepairRequest']})
        self.assertEqual(self.data.entities[self.q['onHeal']]['location']['line_start'],28)
        self.assertIn(self.q['effectDelivery.bindEffectDelivery'],{r['to']for r in self.data.outgoing['ent-000629']if r['kind']=='calls'})
        self.assertIn('element = $(element)',combat);self.assertIn('await attackChatMessageListeners(message, element)',combat)
        self.assertFalse([r for r in self.data.incoming[self.q['addAttackChatListeners']]if r['kind']=='calls'])

    def test_selected_documents_and_shield_writer(self):
        combat=self.source(195);chat=self.source(193);helper=self.source(198)
        for at,t in [(20,'fromUuidSync(message.system.attack.itemUuid)'),(21,'message.system.damage'),(23,'item.rollDamage(damage)'),(41,'li.dataset.messageId'),(47,'await getInteractActor(), target.dataset.messageId'),(54,'if (!actor) return')]:self.assertIn(t,combat[at-1])
        self.assertNotIn('await',combat[22]);self.assertNotIn('await','\n'.join(combat[57:64]))
        for at,m in [(75,'applyCritDamage'),(83,'applyBonusCritDamage'),(91,'applyCritWound')]:
            self.assertIn('(await getInteractActor()).'+m,combat[at-1]);self.assertIn('game.messages.get(target.dataset.messageId).system.crit',combat[at-1])
        self.assertNotIn('defenderUUID','\n'.join(combat[66:96]))
        for at,t in [(11,"event.currentTarget.getAttribute('data-shield')"),(12,"event.currentTarget.getAttribute('data-actor')"),(14,'fromUuidSync(actorUuid)'),(15,"actor?.update({ 'system.derivedStats.shield.value': shield })"),(17,'actor.name'),(23,'ChatMessage.create(messageData)')]:self.assertIn(t,chat[at-1])
        self.assertNotIn('await','\n'.join(chat[9:24]));self.assertNotIn('applyMode','\n'.join(chat[9:24]))
        for field in ['DerivedStats.shield','stat().value']:
            self.assertTrue(any(r['from']==self.q['onShield'] and r['kind']=='writes' and r['location']['line_start']==15 for r in self.data.incoming[self.q[field]]))
        self.assertIn('getCurrentCharacter()', '\n'.join(helper[10:22]))
        self.assertIn('controlled', '\n'.join(helper[:6]))
        self.assertIn('e.hasPlayerOwner','\n'.join(helper[30:59]))

    def test_repair_input_and_delivery_use_distinct_identifiers(self):
        s=self.source(193);h=self.source(504);socket=self.source(217);repair=self.source(191)
        location=self.data.entities[self.q['onRepairRequest']]['location']
        handler='\n'.join(s[location['line_start']-1:location['line_end']])
        for text in ['await getInteractActor()', 'event.target.dataset.owner', 'game.actors?.get(ownerId)',
                     'event.target.dataset.item', 'owner.items?.get(itemId)', 'if (actor && owner && item)',
                     'await RepairSystem.processRequest(owner, item, actor)']:
            self.assertIn(text,handler)
        self.assertIn('data-owner="{{data.actor.id}}"',h[69]);self.assertIn('data-item="{{data.item.id}}"',h[69])
        self.assertIn("await gm.query('TheWitcherTRPG-RB-Version.query'", '\n'.join(repair))
        self.assertIn("function: 'restoreReliability', uuid: item.uuid, data: []", '\n'.join(repair))
        self.assertNotIn('emitForGM', '\n'.join(repair))
        self.assertTrue(any(r['to']==self.q['Repair.processRequest'] for r in self.edges('onRepairRequest','calls')))
        self.assertTrue(any(r['to']==self.q['Repair.restoreReliability'] for r in self.edges('item.repairMixin.restoreReliability','calls')))
        self.assertTrue(any(r['to']==self.q['Repair._restoreItem'] for r in self.edges('Repair._doRepair','calls')))
        self.assertTrue(any(r['to']==self.q['query'] for r in self.edges('Repair._restoreItem','calls')))
        self.assertTrue(any(r['to']==self.q['Repair.restoreReliability'] for r in self.edges('Repair._restoreItem','calls')))
        for model in ['WeaponData.repair','ArmorData.repair']:
            self.assertTrue(any(r['to']==self.q[model] for r in self.edges('Repair.restoreReliability','calls')))

    def test_queries_whitelists_and_return_boundaries(self):
        s='\n'.join(self.source(213))
        self.assertIn('await callableFunctions[queryData.function](...queryData.data)',s)
        self.assertIn('await entity.system[queryData.function]?.(...queryData.data)',s)
        self.assertIn('CONFIG.queries[DELIVERY_QUERY] = receiveEffectDelivery',s)
        self.assertIn('CONFIG.queries[SOURCE_QUERY] = readEffectSource',s)
        methods={r['to']for r in self.edges('query','calls')}
        self.assertTrue({self.q[x]for x in ['WitcherActor.addItem','actor.temporaryEffectMixin.applyTemporaryItemImprovements','actor.adrenalineMixin.addAdrenaline','item.repairMixin.restoreReliability']}<=methods)
        self.assertNotIn(self.q['RegionProperties.addBehaviorsToRegionUuids'],methods)
        registrations={r['to']for r in self.edges('registerQueries','registers')}
        self.assertTrue({self.q[x]for x in ['effectDelivery.readEffectSource','effectDelivery.receiveEffectDelivery']}<=registrations)

    def test_socket_envelope_guard_and_unawaited_receiver(self):
        s=self.source(204);r=self.source(217)
        for at,t in [(10,'return { type, data }'),(14,'!game.socket || !game.user || !game.users'),(15,'game.user.isGM'),(17,'!game.users.activeGM'),(19,'_createMessage(type, data)'),(20,"await game.socket.emit('system.TheWitcherTRPG-RB-Version', message)")]:self.assertIn(t,s[at-1])
        for at,t in [(5,"'restoreReliability': 'uuid'"),(6,"'addItem': 'uuid'"),(9,'!game.socket || !game.user'),(12,'game.user !== game.users.activeGM'),(17,'fromUuidSync(message.data.shift())'),(18,'fromUuid[message.type](...message.data)'),(22,'callableFunctions[message.type](...message.data)')]:self.assertIn(t,r[at-1])
        self.assertNotIn('await','\n'.join(r));self.assertNotIn('hasOwn','\n'.join(r))
        self.assertEqual([x.get('step')for x in self.steps(308)['lookup']['next']if'step'in x],['uuid','generic'])
        self.assertEqual(self.steps(308)['uuid']['next'][0]['flow'],'scheduled')
        self.assertEqual(self.steps(306)['emit']['next'][0]['flow'],'await')
        self.assertTrue(any(r['from']=='ent-003652'and r['kind']=='writes'for r in self.data.incoming[self.q['_createMessage/result.data']]))

    def test_combat_argument_periodic_map_and_waiting(self):
        hooks=self.source(212);s=self.source(196)
        self.assertIn('applyGeneralCombatHooks(combat)',hooks[10])
        for at,t in [(4,'if (!game.user.isActiveGM) return'),(6,'combat.combatants.get(combat.current.combatantId).actor'),(7,'applyMonsterRegeneration(actor)'),(8,'applyCombatEffects(actor)'),(41,'Object.values(actor.system.combatEffects.turnStartEffects)'),(42,'await applyCombatEffect(actor, status)')]:self.assertIn(t,s[at-1])
        self.assertNotIn('await','\n'.join(s[2:9]));self.assertNotIn('actor.statuses','\n'.join(s[39:44]))
        self.assertEqual(self.steps(309)['regeneration']['next'][0]['flow'],'scheduled');self.assertEqual(self.steps(309)['periodic']['next'][0]['flow'],'scheduled')
        self.assertEqual(self.steps(310)['effect']['next'][0]['step'],'effect');self.assertEqual(self.steps(310)['effect']['next'][0]['flow'],'await')
        e=self.data.entities[self.q['applyMonsterRegeneration']];self.assertEqual(e['location']['line_start'],11)

    def test_periodic_payload_and_view_are_separate(self):
        s=self.source(196);schema=self.source(74);h=self.source(488)
        for at,t in [(47,'!status.heal?.amount && !status.damage?.amount'),(50,'status'),(59,'ChatMessage.create(chatData)'),(61,'status.damage.amount > 0'),(64,'spDamage: status.damage.spDamage'),(65,'damageToAllLocations: status.damage.allLocations'),(66,'effects: []'),(67,'bypassesNaturalArmor: status.damage.ignoreArmor'),(68,'bypassesWornArmor: status.damage.ignoreArmor'),(69,'bypassesShield: status.damage.bypassesShield'),(71,"actor.getLocationObject('torso')"),(74,"status.damage.amount + (status.damage.modifier ?? 0), damage, 'sta'"),(76,"status.damage.amount + (status.damage.modifier ?? 0), damage, 'hp'"),(80,'status.heal.amount > 0'),(81,'calculateHealValue(status.heal.amount)')]:self.assertIn(t,s[at-1])
        self.assertNotIn('await',s[58]);self.assertNotRegex('\n'.join(s[61:72]),r'\btype\s*:')
        for name in ['type','heal.modifier']:
            q='combatEffects.turnStartEffects.'+('damage.'+name if name=='type' else name)
            self.assertFalse([r for r in self.data.incoming[self.q[q]]if r['kind']=='reads'and r['location']['source']=='src-000196'])
        self.assertIn('type: new fields.StringField()',schema[26]);self.assertIn('modifier: new fields.NumberField({ initial: 0 })',schema[34])
        self.assertEqual(len(h),3);self.assertIn('{{img}}',h[1]);self.assertIn('{{localize name}}',h[1]);self.assertNotIn('<button','\n'.join(h))
        self.assertEqual({r['to']for r in self.edges('statusEffect.hbs','reads') if self.data.entities[r['to']]['qualified_name'].startswith('combatEffects.')},{self.q['combatEffects.turnStartEffects.'+n]for n in ['img','name']})
        self.assertEqual(self.steps(311)['message']['next'][0]['flow'],'scheduled');self.assertEqual(self.steps(311)['damage']['next'][0]['flow'],'await')
        self.assertEqual({x['step']for x in self.steps(311)['damage-guard']['next']if'step'in x},{'payload','heal-handoff'})

    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[70, 212, 22])
        # Historical .020 totals; later portions extend the current dataset.
        historical={k:[r for r in getattr(d,k).values() if int(r['id'].split('-')[1])<=cap]
                    for k,cap in [('entities',4474),('relations',11393),('processes',313)]}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,4473,11393,313])
        represented={e['location']['source'] for e in historical['entities'] if e['kind']!='boundary' and e.get('location')}
        self.assertEqual(len(represented),243)
        self.assertEqual(615-len(represented),372)
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

