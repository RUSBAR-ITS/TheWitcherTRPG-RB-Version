"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class DamageApplicationExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-019.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_32_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-019-queries.json').read_text())['cases']
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


    def test_owners_schemas_and_damage_modifiers(self):
        d=self.data;a=self.source(14);u=self.source(15);schema=self.source(62);types=self.source(63)
        for name,line in [('applyDamage',7),('updateDerivedStat',121)]:
            e=d.entities[self.q['actor.damageMixin.'+name]]
            self.assertEqual(e['owner'],self.q['actor.damageMixin']);self.assertEqual(e['kind'],'method');self.assertIn('async '+name,a[line-1])
            defs=[r for r in d.incoming[e['id']]if r['kind']=='defines'];self.assertEqual(len(defs),1);self.assertEqual(defs[0]['from'],e['owner'])
        self.assertEqual(re.findall(r'^\s+(\w+): new fields\.', '\n'.join(schema),re.M),['flat','multiplication','applyAP'])
        self.assertEqual(re.findall(r'^\s+(\w+): new fields\.SchemaField', '\n'.join(types),re.M),['slashing','piercing','bludgeoning','elemental','electricity','fire','ice'])
        self.assertNotRegex('\n'.join(schema),r'\b(?:min|max|integer)\s*:')
        self.assertIn('this.system.damageTypeModification[damage.type]?.flat ?? 0',u[3])
        self.assertIn('damageObject.damageProperties.armorPiercing',u[10])
        calls=self.edges('damageTypeModification','calls');self.assertEqual({r['location']['line_start']for r in calls if r['to']==self.q['damageModification']},set(range(7,14)))
        target=self.q['actor.damageUtilMixin.getFlatDamageMod'];self.assertEqual({r['from']for r in d.incoming[target]if r['kind']=='calls'},{self.q['actor.damageMixin.calculateDamageWithLocation']})

    def test_menu_and_dialog_bind_actual_inputs(self):
        s=self.source(194)
        for at,text in [(7,"li.querySelector('.damage-message')"),(15,'await getInteractActor()'),(16,"parseInt(li.querySelector('.dice-total').innerText)"),(17,'li.dataset.messageId'),(27,'await getInteractActor()'),(39,"message.system.damage.properties.isNonLethal ? 'sta' : 'hp'"),(43,"messageId, 'sta'"),(64,"actor.type == 'monster'"),(65,'actor.system.resistantNonSilver'),(66,'actor.system.resistantNonMeteorite'),(72,'await DialogV2.prompt'),(87,'rejectClose: true')]:self.assertIn(text,s[at-1])
        self.assertEqual(re.findall(r'<option value="([^"]+)"','\n'.join(s[46:56])),['Empty','head','torso','leftArm','rightArm','leftLeg','rightLeg','tailWing'])
        self.assertNotIn('checked','\n'.join(s[68:70]))
        for at,control in [(79,'changeLocation?.value'),(80,'resistNonSilver?.checked'),(81,'resistNonMeteorite?.checked'),(82,'vulnerable?.checked'),(83,'oilDmg?.checked')]:self.assertIn('button.form.elements.'+control,s[at-1])
        cb=self.q['createApplyDamageDialog/ok.callback'];self.assertEqual({r['location']['line_start']for r in self.data.incoming[cb]if r['kind']=='registers'},{77})
        reads=self.edges('createApplyDamageDialog/ok.callback','reads');self.assertEqual({self.data.entities[r['to']]['qualified_name']for r in reads},{'damage-dialog.input.'+n for n in ['changeLocation','resistNonSilver','resistNonMeteorite','vulnerable','oilDmg']})

    def test_message_alias_and_status_input_are_distinct(self):
        s=self.source(194);status=self.source(196);model=self.source(100)
        for at,t in [(104,'game.messages.get(messageId).system.damage'),(106,'await createApplyDamageDialog(actor, damageProperties)'),(108,"dialogData.newLocation != 'Empty'"),(109,'damageProperties.location = actor.getLocationObject(dialogData.newLocation)'),(112,'dialogData.addOilDmg'),(113,'damageProperties.properties.oilEffect = actor.system.category'),(116,'actor.applyDamage('),(118,'DamageInstance.create(totalDamage).setType(damageProperties.type)')]:self.assertIn(t,s[at-1])
        self.assertNotRegex('\n'.join(s[102:122]),r'(?:clone|deepClone|\.update\(|\.setFlag\()')
        self.assertNotIn('await','\n'.join(s[115:121]));self.assertNotIn('await','\n'.join(s[98:101]));self.assertIn('actor.applyDamage(null, [DamageInstance.create(totalDamage).setType(damageObject.type)]',s[99])
        self.assertNotRegex('\n'.join(status[61:72]),r'\btype\s*:');self.assertIn("damage, 'sta'",status[73]);self.assertIn("damage, 'hp'",status[75]);self.assertIn('status.damage.amount > 0',status[60]);self.assertIn('status.damage.amount + (status.damage.modifier ?? 0)',status[73])
        self.assertNotRegex('\n'.join(model),r'\bduration\s*:')
        call=self.q['actor.damageMixin.applyDamage'];incoming={self.data.entities[r['from']]['qualified_name']for r in self.data.incoming[call]if r['kind']=='calls'};self.assertEqual(incoming,{'applyDamageFromMessage','applyDamageFromStatus','actor.damageMixin.applyCritDamage','actor.damageMixin.applyBonusCritDamage'})

    def test_shield_order_and_wait_boundaries(self):
        a=self.source(14)
        for at,t in [(8,'await this.handleShield(damageInstances)'),(10,'!damageObject.properties.bypassesShield'),(11,'!damageInstances.some(instance => instance.damage > 0)'),(17,"DamageInstance.create(5).setType('oil')"),(37,'this.system.derivedStats.shield.value'),(39,'damageInstance.damage < shield'),(40,'damageInstance.shielded = damageInstance.damage'),(41,'damageInstance.damage = 0'),(44,'damageInstance.damage -= shield'),(46,'Math.max(shield - damageInstance.shielded, 0)'),(49,"this.update({ 'system.derivedStats.shield.value': shield })"),(51,'if (shield > 0)'),(56,'shield: this.system.derivedStats.shield.value'),(64,'ChatMessage.create(chatData)'),(67,'return damageInstances')]:self.assertIn(t,a[at-1])
        self.assertNotIn('await',a[48]);self.assertNotIn('await',a[63])
        processes={p['name']:p for p in self.new['processes']};p=processes['Урон: щит, локации и последующие эффекты'];self.assertEqual(p['steps'][0]['id'],'shield')
        guard=p['steps'][1];self.assertEqual([x['exit']for x in guard['next']if'exit'in x],['shield-blocked','failed'])
        self.assertEqual(p['steps'][-2]['next'][0]['flow'],'scheduled')
        shield=processes['Урон: поглощение щитом'];self.assertEqual(shield['steps'][2]['next'][0]['flow'],'scheduled')
        for q in ['DerivedStats.shield','stat().value']:
            writes=[r for r in self.data.incoming[self.q[q]]if r['kind']=='writes'and r['from']==self.q['actor.damageMixin.handleShield']];self.assertEqual({r['location']['line_start']for r in writes},{49})

    def test_location_pipeline_and_post_sp_effects(self):
        a=self.source(14);config=self.source(209)
        for at,t in [(159,'Math.max(Math.ceil(totalSP / 2), 0)'),(160,'Math.ceil(displaySP / 2)'),(165,"damageInstances[0].setType = 'silver'"),(169,"damageProperties.strike === 'strong' ? '*2' : ''"),(170,'new Roll(damageProperties.properties.silverDamage + multi)'),(188,'await this.applyAlwaysSpDamage'),(190,'!damageInstances.some(instance => instance.damage > 0)'),(200,'this.getFlatDamageMod(damageProperties)'),(202,'flatDamageMod > 0'),(203,"DamageInstance.create(flatDamageMod).setSource('WITCHER.Damage.activeEffect')"),(207,'Math.max(Math.floor(location.formula * instance.damage), 0)'),(212,'CONFIG.WITCHER.damageTypes.find'),(214,'this.calculateArmorResistances'),(218,'!damageTypeConfig.likeSilver'),(219,'!damageTypeConfig.likeMeteorite'),(229,'enemyData?.isVulnerable'),(230,'instance.damage *= 2'),(233,'instance.afterResistance = instance.damage'),(236,'await this.applySpDamage')]:self.assertIn(t,a[at-1])
        self.assertNotIn('setType',a[202]);self.assertNotIn("value: 'oil'",'\n'.join(config[732:769]));self.assertIn("value: 'silver'",'\n'.join(config[732:769]))
        self.assertIn('this.createDamageBlockedBySp(',a[73]);self.assertIn('return;',a[74]);self.assertIn('?.filter(effect => effect.statusEffect)',a[26]);self.assertIn('.filter(effect => effect.applied)',a[27]);self.assertNotIn('await','\n'.join(a[25:33]))
        p=next(p for p in self.new['processes']if p['name']=='Урон: расчёт выбранной локации');self.assertEqual([s['id']for s in p['steps']],['armor','silver-select','silver-roll','sp','always-wear','positive','flat','location','resistance','ordinary-wear','return'])
        self.assertEqual([x['exit']for x in p['steps'][5]['next']if'exit'in x],['blocked','failed'])
        self.assertEqual({r['to']for r in self.edges('actor.damageMixin.applyDamage','calls')if r['location']['line_start']>=26},{self.q['applyStatusEffectToActor'],self.q['applyActiveEffectToActorViaId']})

    def test_all_locations_share_objects_and_await_report(self):
        a=self.source(14)
        for at,t in [(86,'this.getAllLocations().map(location => this.getLocationObject(location))'),(90,'damage.location = location'),(92,'this.calculateDamageWithLocation(dialogData, damage, damageInstances)'),(95,'await Promise.all(resultPromises)'),(99,'Math.floor(result.damageInstances.reduce'),(116,'await ChatMessage.create(chatData)'),(118,'await this.updateDerivedStat(totalAppliedDamage, derivedStat)')]:self.assertIn(t,a[at-1])
        self.assertNotRegex('\n'.join(a[84:119]),r'\b(?:clone|deepClone|structuredClone)\b');self.assertNotIn('speaker','\n'.join(a[109:113]));self.assertNotIn('blockedBySp','\n'.join(a[96:101]))
        self.assertIn('damageInstances,',a[192]);self.assertIn('damageInstances,',a[238]);self.assertIn('let location = damageProperties.location',a[150])
        p=next(p for p in self.new['processes']if p['name']=='Урон: применение ко всем локациям');self.assertEqual([s['id']for s in p['steps']],['locations','dispatch','collect','report','resource']);self.assertEqual(p['steps'][1]['next'][0]['flow'],'scheduled');self.assertEqual(p['steps'][3]['next'][0]['flow'],'await')

    def test_temporary_hp_container_and_actual_resource_writers(self):
        a=self.source(14)
        for at,t in [(122,'Math.floor(damage)'),(124,"derivedStat == 'hp'"),(125,'this.temporaryEffects.filter'),(126,"change.key.includes('temporaryHp')"),(129,'for (let change of tempHp.system.changes)'),(130,'JSON.parse(change.value)'),(131,'changeContent.value < damage'),(133,'changeContent.value = 0'),(135,'changeContent.value -= damage'),(138,'change.value = JSON.stringify(changeContent)'),(140,'await tempHp.update({ changes: tempHp.system.changes })'),(144,'await this.update({'),(145,'this.system.derivedStats[derivedStat].value - damage')]:self.assertIn(t,a[at-1])
        body='\n'.join(a[120:147]);self.assertNotIn('Math.max',body);self.assertNotIn('Math.min',body);self.assertNotIn('.delete(',body);self.assertNotIn('break',body);self.assertEqual(body.count('change.key'),1)
        self.assertNotIn('this.system.combatEffects.temporaryEffects.temporaryHp',body)
        writes={r['to']for r in self.edges('actor.damageMixin.updateDerivedStat','writes')};self.assertEqual(writes,{self.q['DerivedStats.hp'],self.q['DerivedStats.sta'],self.q['stat().value']})
        p=next(p for p in self.new['processes']if p['name']=='Урон: временные HP и конечный ресурс');last=p['steps'][-1];self.assertEqual(last['id'],'actor-update');self.assertEqual(last['next'][0]['flow'],'await')
        b=self.data.entities[self.q['updateDerivedStat/change-value-json']];self.assertEqual({r['path']for r in b['refs']if r['relation']=='related_issue'},{'docs/issues/potential/issue-00117.md','docs/issues/potential/issue-00294.md'})

    def test_report_contexts_and_partial_have_different_shapes(self):
        a=self.source(14);single='\n'.join(self.source(491));allview=self.source(490)
        self.assertIn('properties,',a[240]);self.assertNotIn('damageProperties','\n'.join(a[237:244]));self.assertIn('damageProperties: damageResult.damageProperties',a[268]);self.assertIn('" result}}',allview[10])
        for name,line in [('initialDamage',272),('afterSPReduction',273),('afterLocation',274),('afterResistance',275),('finalDamage',276)]:self.assertIn(name+': damageInstances.map',a[line-1]);self.assertIn('{{{'+name+'}}}',single)
        self.assertNotIn('initialDamage','\n'.join(a[103:107]));self.assertNotIn('createDamageResultMessage','\n'.join(a[84:119]))
        self.assertIn('{{shield}}','\n'.join(self.source(492)));self.assertIn('{{damageInstances}}','\n'.join(self.source(492)));self.assertIn('{{initialDamage}}','\n'.join(self.source(493)))
        render_edges=self.edges('damageToAllLocations.hbs','renders');self.assertEqual([(r['to'],r['location']['line_start'])for r in render_edges],[(self.q['damageToLocation.hbs'],11)])
        for q in ['damageToAllLocations.hbs','damageToLocation.hbs','shieldAbsorbs.hbs','spAbsorbs.hbs']:self.assertFalse(self.edges(q,'writes'))


    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[73, 347, 23])
        # Historical .019 totals; new portions extend the current dataset.
        historical={k:[r for r in getattr(d,k).values() if int(r['id'].split('-')[1])<=cap]
                    for k,cap in [('entities',4404),('relations',11181),('processes',291)]}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,4403,11181,291])
        represented={e['location']['source'] for e in historical['entities'] if e['kind']!='boundary' and e.get('location')}
        self.assertEqual(len(represented),239)
        self.assertEqual(615-len(represented),376)
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

