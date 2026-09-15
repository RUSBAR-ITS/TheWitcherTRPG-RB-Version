"""Проверка справочника .008 по исходникам; игровой JavaScript не исполняется."""
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class EffectLifecycleExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()

    def source(self,sid):
        return (ROOT/self.data.sources[sid]['path']).read_text().splitlines()

    def edges(self,eid,kind):
        return [r for r in self.data.relations.values() if r['from']==eid and r['kind']==kind]

    def steps(self,pid):
        return {s['id']:s for s in self.data.processes[pid]['steps']}

    def test_24_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-008-queries.json').read_text())['cases']
        self.assertEqual(len(cases),24)
        for case in cases:
            with self.subTest(case=case['id']):
                run=run_cli([*case['command'],'--format','json'],cwd='/tmp')
                self.assertEqual(run.returncode,0,run.stderr)
                out=json.loads(run.stdout);items=out['items'];first=items[0] if items else {}
                actual=dict(ids=[x['id'] for x in items if 'id' in x],
                    locations=sorted([[x['location']['source'],x['location']['line_start']]
                                      for x in items if x.get('location')]),
                    from_ids=sorted({x['from'] for x in items if 'from' in x}),
                    to_ids=sorted({x['to'] for x in items if 'to' in x}),
                    next_steps=[x['step'] for x in first.get('next',[]) if 'step' in x],
                    next_exits=[x['exit'] for x in first.get('next',[]) if 'exit' in x],
                    resolution=first.get('boundary',{}).get('kind'),
                    includes_anchors=[x.get('anchor') for x in items],
                    includes_refs=[x['path'] for x in items if 'path' in x])
                for k,v in case['expected'].items():
                    if k.startswith('includes_'):self.assertTrue(set(v)<=set(actual[k]),(k,actual[k]))
                    else:self.assertEqual(actual[k],v,k)
                self.assertEqual(out['freshness']['state'],'current')
                self.assertEqual(out['coverage']['state'],'partial')


    def test_definitions_and_all_new_defines_addresses(self):
        for n,sid,line,name in [
            (771,36,7,'prepareActiveEffectCategories'),(772,36,49,'onManageActiveEffect'),
            (773,36,81,'_onActiveEffectDisplayInfo'),(774,36,91,'activeEffectListener'),
            (775,23,4,'applyTemporaryItemImprovements'),(776,23,21,'callback:'),
            (777,205,3,'addStatusEffectChatListeners'),(778,205,23,'onApplyStatus'),
            (779,205,30,'applyStatusEffectToTargets'),(780,205,43,'applyStatusEffectToActor'),
            (781,205,74,'handleStatusCounterIntegration'),(782,206,3,'applyActiveEffectToTargets'),
            (783,206,32,'applyActiveEffectToActor'),(784,206,70,'applyTemporaryItemImprovements'),
            (785,198,61,'getActorOwner'),(786,198,3,'getCurrentCharacter'),
            (787,213,15,'async function query'),(788,213,9,'applyTemporaryItemImprovementsToActor'),
            (791,192,321,'prepareEmbeddedDocuments'),(792,192,331,'*allApplicableEffects'),
            (793,192,342,'applyActiveEffects'),(816,92,3,'class TemporaryEffects'),
            (823,27,58,'_prepareContext'),(824,28,24,'getData'),(825,183,4,'class WitcherConfigurationSheet'),
            (827,183,74,'prepareActiveEffectCategories'),(828,183,116,'onManageActiveEffect')]:
            sid=f'src-{sid:06}';e=self.data.entities[f'ent-{n:06}']
            self.assertEqual((e['location']['source'],e['location']['line_start']),(sid,line))
            self.assertIn(name,self.source(sid)[line-1])
        for r in self.data.relations.values():
            if r['kind']=='defines' and int(r['id'][4:])>=1906:
                entity=self.data.entities[r['to']]
                self.assertEqual(entity['owner'],r['from'])
                self.assertEqual(entity['location']['source'],r['location']['source'])
                self.assertEqual(entity['location']['line_start'],r['location']['line_start'])

    def test_category_suppression_transfer_and_visibility_are_distinct(self):
        sm=self.source('src-000036');ae=self.source('src-000008');it=self.source('src-000183')
        self.assertIn('if (e.isDisabled)',sm[33]);self.assertIn('if (e.disabled)',it[100])
        for literal,line in [('isTemporaryItemImprovement && !e.isAppliedTemporaryItemImprovement',35),
                             ('else if (e.isTemporary)',37),('else categories.passive',38)]:
            self.assertIn(literal,sm[line-1])
        self.assertIn('this.disabled || !(this.parent?.system?.equipped ?? true)',ae[18])
        self.assertIn('this.system.isTransferred',ae[26]);self.assertNotIn('type',ae[26])
        self.assertIn("this.type === 'temporaryItemImprovement'",ae[30])
        hbs=self.source('src-000531')
        self.assertIn('effect.isSuppressed @root.actor',hbs[17])
        self.assertIn('document.system.canHaveTemporaryItemImprovement',hbs[6])
        self.assertIn('effect.disabled',hbs[32])
        self.assertEqual(self.data.entities['ent-000797']['boundary']['kind'],'external')
        for n in (771,827):
            self.assertFalse(any(r['to']=='ent-000795' for r in self.edges(f'ent-{n:06}','reads')))

    def test_crud_resolves_owner_and_item_config_is_separate(self):
        s=self.source('src-000036');i=self.source('src-000183');h=self.source('src-000531')
        self.assertIn('parentUuid',s[52]);self.assertIn('fromUuidSync(parentUuid).effects.get(li.dataset.effectId)',s[53])
        self.assertIn('parentUuid == caller.uuid',s[72]);self.assertIn('effect.delete()',s[73])
        self.assertIn('effect.update({ disabled: !effect.disabled })',s[76])
        self.assertNotRegex('\n'.join(s[56:69]), r'(?m)^ {24}type:')
        self.assertIn('type: game.i18n.localize',s[59])  # i18n argument, not effect.type
        self.assertNotIn('transfer:','\n'.join(s[56:69]))
        self.assertIn("li.dataset.effectType === 'temporaryItemImprovement'",i[124])
        self.assertIn('this.document.effects.get(li.dataset.effectId)',i[118])
        self.assertEqual([r['location']['line_start'] for r in self.edges('ent-000826','registers')],[20,21,22,23])
        self.assertIn('data-effect-id="{{effect.id}}"',h[18])
        self.assertEqual(h[19].count('{{effect.parent.uuid}}'),2)
        self.assertIn('html().trim()',s[85]);self.assertIn("toggleClass('invisible')",s[86])
        self.assertNotIn('_onActiveEffectDisplayInfo','\n'.join(i))
        self.assertEqual([x['step'] for x in self.steps('proc-000034')['owner']['next']],['delete','foreign'])

    def test_temporary_copy_replaces_system_and_does_not_await_storage(self):
        s=self.source('src-000023');body='\n'.join(s)
        for line,literal in [(5,"effect.type === 'temporaryItemImprovement'"),(6,'temps.length == 0'),
            (8,"item.type === 'weapon'"),(17,'await DialogV2.prompt'),(22,'button.form.elements.choosen.value'),
            (25,'rejectClose: true'),(28,'weapons.find'),(32,'temp.toObject?.() ?? temp'),
            (34,'origin: this.uuid'),(35,'system: {'),(36,'isTransferred: true'),
            (37,'applySelf: false'),(38,'applyOnTarget: false'),(41,'...temp.duration'),
            (46,"weapon.createEmbeddedDocuments('ActiveEffect', temps)"),
            (50,'await foundry.applications.handlebars.renderTemplate'),(56,'actor: this.actor'),
            (60,'ChatMessage.create(chatData)')]:
            self.assertIn(literal,s[line-1])
        for absent in ['changes','start:','canHaveTemporaryItemImprovement','isStored','equipped']:
            self.assertNotIn(absent,body)
        self.assertNotIn('await',s[45]);self.assertNotIn('await',s[59])
        steps=self.steps('proc-000036')
        self.assertEqual([n['flow'] for n in steps['prompt']['next']],['scheduled','await'])
        self.assertEqual([n['flow'] for n in steps['create']['next']],['sync'])
        for rid in steps['prompt']['relations']:
            self.assertEqual(self.data.relations[rid]['from'],'ent-000775')

    def test_ordinary_effect_mutation_clone_and_query_payload(self):
        s=self.source('src-000206')
        for line,literal in [(15,'fromUuidSync(itemUuid)'),(18,'game.users.activeGM.query'),(27,'effect.system[applyWhen]'),
            (33,'fromUuidSync(actorUuid)'),(37,'effect.duration.rounds = duration ?? effect.duration.rounds'),
            (38,'applyTemporaryItemImprovements(actor, activeEffects)'),(40,'!actor.isOwner'),
            (43,'data: [actorUuid, activeEffects.filter'),(52,'new ActiveEffect(effect)'),(55,'effect.clone('),
            (58,"'system.applySelf': false"),(59,"'system.applyOnTarget': false"),
            (60,"'system.applyOnHit': false"),(61,"'system.applyOnDamage': false"),
            (63,'parent: actor'),(67,'await actor.createEmbeddedDocuments'),(74,'effects: activeEffects')]:
            self.assertIn(literal,s[line-1])
        self.assertNotIn('duration',s[42]);self.assertNotIn('await',s[37])
        self.assertNotIn('isTransferred','\n'.join(s[47:65]))
        steps=self.steps('proc-000037')
        self.assertEqual([n['step'] for n in steps['duration']['next'] if 'step' in n],['temporary'])
        self.assertEqual([n['flow'] for n in steps['create']['next']],['await','await'])
        self.assertFalse(any(r['to']=='ent-000319' for r in self.edges('ent-000783','calls')))
        self.assertEqual([r['to'] for r in self.edges('ent-000783','refers')],['ent-000317'])

    def test_status_target_counter_timer_and_query_return_boundaries(self):
        s=self.source('src-000205');q=self.source('src-000213');hp=self.source('src-000198')
        for line,literal in [(5,"querySelector('.chat-message').each"),(16,"querySelector('a.apply-status')"),
            (25,'getCurrentCharacter()'),(27,'target.uuid'),(31,'game.user.targets'),
            (59,'actor.appliedEffects.find'),(61,'await actor.toggleStatusEffect(statusEffectId)'),
            (63,'handleStatusCounterIntegration'),(65,'statusEffectImmunities?.find'),
            (67,'setTimeout'),(68,'actor.toggleStatusEffect(statusEffectId)'),(69,'1000'),
            (75,"game.modules.get('statuscounter')?.active"),(77,'!duration || duration == 0'),
            (79,'CONFIG.WITCHER.statusEffects.querySelector'),(81,'EffectCounter.getAllCounters(target).querySelector')]:
            self.assertIn(literal,s[line-1])
        self.assertIn('canvas.tokens.controlled[0]?.actor',hp[3]);self.assertIn('game.user.character',hp[3])
        self.assertNotIn('active:',s[60]);self.assertNotIn('active:',s[67])
        self.assertIn('if (queryData.function in callableFunctions)',q[32])
        self.assertIn('callableFunctions[queryData.function](...queryData.data)',q[33])
        self.assertIn('return true',q[34]);self.assertNotIn('await','\n'.join(q[8:46]))
        self.assertIn('entity.system[queryData.function]?.',q[40])
        self.assertTrue(any(r['to']=='ent-000879' for r in self.edges('ent-000787','refers')))
        self.assertEqual([n.get('step') for n in self.steps('proc-000040')['counter']['next'] if 'step' in n],['immune'])
        self.assertEqual(self.steps('proc-000040')['timer']['relations'],
                         [r['id'] for r in self.edges('ent-000780','registers')])
        self.assertEqual(self.data.processes['proc-000041']['entry']['entity'],'ent-000789')

    def test_item_phase_priority_and_actor_collections(self):
        item=self.source('src-000192');sh=self.source('src-000027');act=self.source('src-000047')
        for line,literal in [(322,'super.prepareEmbeddedDocuments()'),(323,'this.applyActiveEffects()'),
            (333,'effect.isAppliedTemporaryItemImprovement'),(348,'!effect.active'),(350,'effect.system.changes.map'),
            (351,'deepClone(change)'),(353,'c.priority ??= c.mode * 10'),(358,'a.priority - b.priority'),
            (362,'!change.key'),(363,'change.effect.apply(this, change)'),(368,'this.overrides =')]:
            self.assertIn(literal,item[line-1])
        self.assertNotIn('shouldApplyChange','\n'.join(item[341:369]))
        self.assertNotIn('phase','\n'.join(item[341:369]))
        self.assertIn('!i.system.isStored',sh[71]);self.assertIn('this.actor.allApplicableEffects()',sh[90])
        self.assertIn('super.temporaryEffects',act[26]);self.assertIn('this.items',act[28])
        self.assertNotIn('active','\n'.join(act[28:32]))
        self.assertEqual([n['step'] for n in self.steps('proc-000044')['active']['next']],['effects','map'])

    def test_pool_data_templates_and_actual_chat_producers(self):
        pool=self.source('src-000092');hbs=self.source('src-000562')
        self.assertIn('TypedObjectField',pool[5]);self.assertIn('name: new fields.StringField',pool[7])
        self.assertIn('value: new fields.NumberField({ initial: 0 })',pool[8])
        self.assertNotIn('temporaryHpSum','\n'.join(pool))
        self.assertIn('temporaryHpSum',self.source('src-000027')[73])
        self.assertIn('crit-wounds-table.hbs',hbs[7]);self.assertIn('documentsByType.criticalWound',hbs[10])
        self.assertIn('effect-part.hbs',hbs[57])
        self.assertEqual([(r['to'],r['location']['line_start']) for r in self.edges('ent-000842','renders')],
                         [('src-000531',58),('src-000530',8)])
        producer=self.data.entities['ent-000871'];s=self.source(producer['location']['source'])
        self.assertIn('apply-status',s[57]);self.assertNotIn('data-duration',s[57])
        spell=(ROOT/'templates/chat/combat/spellItem.hbs').read_text().splitlines()
        self.assertIn('apply-status',spell[62]);self.assertIn('data-duration',spell[63])
        notification=(ROOT/'templates/chat/combat/statusEffect.hbs').read_text()
        self.assertNotIn('apply-status',notification)

    def test_process_reachability_local_relations_and_participation(self):
        procs=[json.loads(l) for l in (BASE/'data/processes/expansion-008.jsonl').read_text().splitlines()]
        self.assertEqual(len(procs),17);self.assertEqual(sum(len(p['steps']) for p in procs),83)
        for p in procs:
            steps={s['id']:s for s in p['steps']};seen=set();pending=[p['steps'][0]['id']];exits=set()
            while pending:
                key=pending.pop()
                if key in seen:continue
                seen.add(key)
                for n in steps[key]['next']:
                    if 'step' in n:pending.append(n['step'])
                    else:exits.add(n['exit'])
            self.assertEqual(seen,set(steps));self.assertEqual(exits,{e['id'] for e in p['exits']})
            for s in steps.values():
                for rid in s['relations']:
                    r=self.data.relations[rid]
                    self.assertEqual(r['from'],s['entity'])
                    self.assertEqual(r['location']['source'],s['location']['source'])
                    self.assertTrue(s['location']['line_start']<=r['location']['line_start']<=s['location']['line_end'])
            out=self.data.query(query.parser().parse_args(['processes',p['entry']['entity'],'--limit','50','--no-verify']))
            self.assertIn(p['id'],[x['id'] for x in out['items']])
        historical={}
        for kind in ['entities','relations','processes']:
            parts=[f'examples/{kind}.jsonl',f'data/{kind}/pilot.jsonl',
                   *[f'data/{kind}/expansion-{n:03}.jsonl' for n in [6,7,8]]]
            historical[kind]=[json.loads(l) for p in parts for l in (BASE/p).read_text().splitlines()]
        self.assertEqual([len(historical[k]) for k in ['entities','relations','processes']],[879,2211,49])
        for kind,rows in historical.items():
            self.assertTrue({r['id'] for r in rows}<=set(getattr(self.data,kind)))
        out=self.data.query(query.parser().parse_args(['processes','src-000047','--no-verify']))
        self.assertEqual([p['id'] for p in out['items']],['proc-000004','proc-000005','proc-000049'])
        out=self.data.query(query.parser().parse_args(['find','value','--match','exact','--kind','field','--limit','1','--no-verify']))
        self.assertEqual(out['page']['total'],5)
        self.assertTrue(out['page']['truncated'])

    def test_external_contract_hashes_and_core_source_distinctions(self):
        text=(BASE/'coverage-008.md').read_text()
        rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',text,re.M)
        self.assertEqual(len(rows),5)
        for path,digest in rows:self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)
        core=Path('/opt/foundryvtt')
        ae=(core/'client/documents/active-effect.mjs').read_text().splitlines()
        self.assertIn('!this.disabled && !this.isSuppressed',ae[209])
        self.assertIn('Number.isFinite(this.duration.value)',ae[225])
        self.assertIn('this.persisted && !this.inCompendium',ae[232])
        actor=(core/'client/documents/actor.mjs').read_text().splitlines()
        self.assertIn('effect.shouldApplyChange',actor[244])
        self.assertIn('for ( const effect of this.effects )',actor[559])
        self.assertIn('await this.deleteEmbeddedDocuments',actor[568])
        clone=(core/'common/abstract/document.mjs').read_text().splitlines()
        self.assertIn('this.toObject()',clone[474])
        self.assertNotIn('toObject(false)','\n'.join(clone[471:484]))

if __name__=='__main__':
    unittest.main()
