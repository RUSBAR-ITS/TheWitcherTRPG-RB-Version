"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class ArmorExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-018.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_32_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-018-queries.json').read_text())['cases']
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


    def test_schemas_and_instance_owners(self):
        a=self.source(108);sp=self.source(127);res=self.source(126)
        declarations=re.findall(r'^\s+(\w+): new fields\.(\w+)','\n'.join(a),re.M)
        self.assertEqual([x for x in declarations if x[0]=='location'],[('location','ArrayField'),('location','StringField')])
        self.assertEqual([n for n,t in declarations if t=='EmbeddedDataField'],['resistance','head','torso','leftArm','rightArm','leftLeg','rightLeg','defenseProperties'])
        self.assertEqual(re.findall(r'^\s+(\w+): new fields\.', '\n'.join(sp),re.M),['stoppingPower','modifiedStoppingPower','maxStoppingPower','modifiedMaxStoppingPower'])
        self.assertEqual('\n'.join(sp).count('persisted: false'),2)
        self.assertNotRegex('\n'.join(sp),r'\b(?:min|max|integer)\s*:')
        self.assertEqual(re.findall(r'^\s+(\w+): new fields\.', '\n'.join(res),re.M),['bludgeoning','slashing','piercing'])
        self.assertIn('prepareBaseData() {}',res[11])
        owner=self.q['SpData'];target=self.q['ResistanceData']
        self.assertEqual({r['from'] for r in self.data.incoming[owner] if r['kind']=='embeds'},{self.q['ArmorData.'+z] for z in ['head','torso','leftArm','rightArm','leftLeg','rightLeg']})
        self.assertEqual({r['from'] for r in self.data.incoming[target] if r['kind']=='embeds'},{self.q['ArmorData.resistance']})

    def test_preparation_order_references_and_distinct_writers(self):
        a=self.source(108);s=self.source(127);r=self.source(126)
        for at,text in [(110,'this.resistance.prepareBaseData()'),(111,'this.head.prepareBaseData()'),(116,'this.rightLeg.prepareBaseData()'),(122,'this.enhancementItemIds'),(124,'this.enhancementItems = []'),(126,'this.parent.actor.items'),(131,'items.get(itemId)'),(136,'system: item.system'),(143,'new Array(this.enhancements - (this.enhancementItemIds?.length ?? 0)).fill({})'),(145,'this.resistance.prepareDerivedData()'),(147,'this.head.prepareDerivedData()'),(152,'this.rightLeg.prepareDerivedData()'),(154,'unwrapAssociatedDiagram(this)')]:self.assertIn(text,a[at-1])
        self.assertIn('this.modifiedStoppingPower = this.stoppingPower',s[26]);self.assertIn('this.modifiedMaxStoppingPower = this.maxStoppingPower',s[27]);self.assertIn('this.maxStoppingPower == 0',s[31]);self.assertIn('this.parent.enhancementItems',s[33]);self.assertIn('+= enhancement.system.stopping',s[36]);self.assertIn('+= enhancement.system.stopping',s[37])
        self.assertIn('Object.keys(this)',r[17]);self.assertIn('this[resistance] || !!enhancement.system[resistance]',r[18])
        reads={edge['to'] for edge in self.edges('SpData.prepareDerivedData','reads')};self.assertIn(self.q['ArmorData.enhancementItems'],reads);self.assertIn(self.q['EnhancementData.stopping'],reads)
        stages={p['name']:p for p in self.new['processes']};p=stages['ArmorData: подготовка улучшений и SP'];self.assertEqual([s['id'] for s in p['steps']],['base','items','slots','models','diagram'])

    def test_migrations_keep_source_and_prepared_separate(self):
        a=self.source(108)
        self.assertIn('source.enhancementItemIds.push(enhancement._id)',a[162]);self.assertIn('this.effects?.forEach',a[167]);self.assertIn('source.effects = Object.fromEntries',a[178]);self.assertIn('delete source.effects',a[183])
        zones=['head','torso','leftArm','rightArm','leftLeg','rightLeg']
        for i,z in enumerate(zones):
            self.assertIn('if (source.'+z+'MaxStopping)',a[188+i*10]);self.assertIn('source.'+z+'.stoppingPower = source.'+z+'Stopping',a[192+i*10]);self.assertIn('source.'+z+'.maxStoppingPower = source.'+z+'MaxStopping',a[193+i*10]);self.assertIn('delete source.'+z+'MaxStopping',a[195+i*10])
        for n,start in [('bludgeoning',254),('slashing',258),('piercing',262)]:self.assertIn('if (source.'+n+')',a[start-1]);self.assertIn('source.resistance.'+n+' = source.'+n,a[start]);self.assertIn('delete source.'+n,a[start+1])
        writes=self.edges('ArmorData.migrateSpFields','writes');self.assertEqual({r['location']['line_start'] for r in writes},{193,194,203,204,213,214,223,224,233,234,243,244})
        self.assertTrue(all('Сырой' in r.get('context','') for r in writes))

    def test_selection_and_layer_branches(self):
        a=self.source(10)
        for at,t in [(3,'-this.system.lifepathModifiers.ignoredArmorEncumbrance'),(4,"this.items.filter(item => item.type == 'armor' && item.system.equipped)"),(9,'Math.max(encumbranceModifier, 0)'),(13,"this.getList('armor').filter(a => a.system.equipped)"),(59,'this.getArmors([])'),(66,'properties.bypassesNaturalArmor'),(73,'this.getArmorSp(armorSet, location.name, properties).displaySP'),(74,'this.getArmorSp(armorSet, location.name, properties).totalSP'),(110,'lightCount > 1 || mediumCount > 1 || heavyCount > 1'),(112,'return;'),(125,"armorSet['lightArmor']?.system[location].modifiedStoppingPower"),(137,'!properties.bypassesWornArmor'),(138,'if (heavyArmorSP)'),(145,'this.getArmorDiffBonus(heavyArmorSP, mediumArmorSP)'),(156,'this.getArmorDiffBonus(mediumArmorSP, lightArmorSP)'),(160,'this.getArmorDiffBonus(heavyArmorSP, lightArmorSP)'),(170,'naturalArmorSP && !properties.bypassesNaturalArmor'),(184,'underArmor <= 0 || overArmor <= 0')]:self.assertIn(t,a[at-1])
        self.assertNotIn('system.location','\n'.join(a[11:85]));self.assertEqual('\n'.join(a[14:20]).count('modifiedMaxStoppingPower > 0'),6)
        self.assertNotIn('armorPiercing','\n'.join(a[11:204]));self.assertIn('diff > 20',a[191]);self.assertIn('diff > 15',a[193]);self.assertIn('diff > 9',a[195]);self.assertIn('diff > 5',a[197]);self.assertIn('diff >= 0',a[199])
        actor=self.source(47);self.assertIn('!i.system.isStored',actor[255]);self.assertIn('this.getArmorEcumbrance()',actor[76])
        source={e['id'] for e in self.data.entities.values() if e['qualified_name'].startswith('actor.armorMixin.getLocationArmor/result.')};self.assertEqual(len(source),3)

    def test_resistances_wear_and_wait_boundaries(self):
        a=self.source(10);model=self.source(108)
        for at,t in [(208,'properties.armorPiercing || properties.improvedArmorPiercing'),(209,'return damageInstance'),(212,'this.getMultiDamageMod(damage)'),(216,'resistance[damageInstance.type]'),(223,'resistance[damage.type]'),(220,'Math.floor(0.5 * damageInstance.damage * damageMulti)'),(224,'Math.floor(0.5 * damageInstance.damage * damageMulti)'),(231,'properties.bypassesWornArmor'),(233,'return 0'),(236,"await new Roll('1d6/2+1').evaluate()"),(239,'spDamage *= 2'),(249,'properties.spDamage ?? 0'),(264,'properties.bypassesNaturalArmor'),(265,"this.type != 'monster'")]:self.assertIn(t,a[at-1])
        self.assertNotIn('naturalArmor','\n'.join(a[256:261]));self.assertNotIn('await','\n'.join(a[240:284]));self.assertNotIn('bypassesWornArmor','\n'.join(a[247:255]));self.assertNotIn('crushingForce','\n'.join(a[247:255]))
        for at,n in [(269,'armorHead'),(274,'armorUpper'),(278,'armorLower'),(281,'armorTailWing')]:self.assertIn('Math.max(this.system.'+n+' - spDamage, 0)',a[at-1])
        self.assertIn('this[location.name].modifiedStoppingPower - spDamage >= 0',model[75]);self.assertIn('this[location.name].stoppingPower - spDamage',model[77]);self.assertNotIn('await','\n'.join(model[74:81]));self.assertNotIn('Math.max','\n'.join(model[74:81]))
        helper=self.source(15);self.assertIn('damageObject.damageProperties.armorPiercing',helper[10]);self.assertIn('damageMod?.multiplication ?? 1',helper[14])
        p=next(p for p in self.new['processes'] if p['name']=='Броня: обычный износ SP');steps={x['id']:x for x in p['steps']};self.assertEqual(steps['dispatch']['next'][0]['flow'],'scheduled')
        p=next(p for p in self.new['processes'] if p['name']=='ArmorData: запрос изменения базового SP');self.assertEqual(p['steps'][1]['next'][0]['flow'],'scheduled')

    def test_forms_maps_and_inventory_use_the_right_stages(self):
        main='\n'.join(self.source(583));general='\n'.join(self.source(590));sp='\n'.join(self.source(127))
        zones=['head','torso','leftArm','rightArm','leftLeg','rightLeg']
        for z in zones:
            for n in ['stoppingPower','maxStoppingPower']:
                self.assertIn('name="system.'+z+'.'+n+'"',main);self.assertIn('systemFields.'+z+'.fields.'+n,general);self.assertIn('value=document.system.'+z+'.'+n,general)
        self.assertEqual(general.count('{{formGroup '),12);self.assertNotIn('Shield',general);self.assertNotIn('encumb',general);self.assertNotIn('modifiedStoppingPower',main)
        self.assertIn('checked item.system.resistance.slashing',main);self.assertIn('name="system.reliability"',main);self.assertIn('data-action=\'editEffect\'',main);self.assertIn('item.system.enhancementsEffects',main)
        w=self.source(164);self.assertIn('context.config.Availability.WITCHER',w[18]);self.assertIn('this.getArmorLocations()',w[20]);self.assertIn("Shield: 'WITCHER.Armor.LocationShield'",w[40]);self.assertIn('armorGeneral.hbs',self.source(182)[6])
        h=self.source(211);self.assertIn("key: 'leftLeg'",h[173]);self.assertIn('WITCHER.Location.rightLeg',h[174]);self.assertIn('modifiedMaxStoppingPower ?? armor.reliabilityMax',h[190]);self.assertIn('modifiedStoppingPower ?? armor.reliability',h[192]);self.assertIn('percentage > 66',h[197]);self.assertIn('percentage > 33',h[198])
        self.assertIn('armorPartsInfo armor.system',self.source(553)[18]);self.assertIn('armor.system.resistance.slashing',self.source(553)[53]);self.assertIn('.location-table',self.source(446)[17])
        for lang in ['en','ru']:
            raw=json.loads((ROOT/'lang'/f'{lang}.json').read_text());flat={}
            def walk(o,p=''):
                for key,v in o.items():
                    n=(p+'.' if p else '')+key
                    if isinstance(v,dict):walk(v,n)
                    else:flat[n]=v
            walk(raw)
            for suffix in ['LeftArm','RightArm','LeftLeg','RightLeg']:self.assertEqual('WITCHER.Armor.location'+suffix in flat,lang=='en')

    def test_selected_damage_consumer_and_status_payload(self):
        s=self.source(14)
        for at,t in [(153,'this.getLocationArmor(location, properties)'),(154,'locationArmor.armorSet'),(155,'locationArmor.totalSP'),(156,'locationArmor.displaySP'),(159,'Math.max(Math.ceil(totalSP / 2), 0)'),(160,'Math.ceil(displaySP / 2)'),(179,'instance.damage -= totalSP'),(185,'instance.afterSp = instance.damage'),(188,'await this.applyAlwaysSpDamage'),(190,'!damageInstances.some(instance => instance.damage > 0)'),(214,'this.calculateArmorResistances'),(233,'instance.afterResistance = instance.damage'),(236,'await this.applySpDamage')]:self.assertIn(t,s[at-1])
        statuses=self.source(74);self.assertIn('spDamage: new fields.NumberField({ initial: 0 })',statuses[30]);self.assertNotIn('spDamage:','\n'.join(self.source(130)))
        entity=self.data.entities[self.q['applyCombatEffect/damage.properties.spDamage']];ss=self.source(int(entity['location']['source'][4:]));self.assertIn('spDamage: status.damage.spDamage',ss[63]);self.assertIn('status.damage.amount > 0',ss[60]);self.assertIn('properties: {',ss[62])
        self.assertFalse(any(p['entry']['entity']==self.q['actor.damageMixin.calculateDamageWithLocation'] for p in self.new['processes']))


    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[139,821,38])
        # Historical .018 totals; the retired duplicate ID3706 remains absent.
        historical={k:[r for r in getattr(d,k).values() if int(r['id'].split('-')[1])<=cap]
                    for k,cap in [('entities',4331),('relations',10834),('processes',268)]}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,4330,10834,268])
        represented={e['location']['source'] for e in historical['entities'] if e['kind']!='boundary' and e.get('location')}
        self.assertEqual(len(represented),235)
        self.assertEqual(615-len(represented),380)
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

