"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class DamageExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-017.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_28_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-017-queries.json').read_text())['cases']
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


    def test_models_dto_and_payload_have_distinct_owners(self):
        s=self.source(96);t='\n'.join(s)
        for a,v in [(16,'super.defineSchema()'),(20,'damage: new fields.SchemaField'),(21,'...damageData()'),(22,'properties: new fields.SchemaField'),(23,'...DamageProperties.defineSchema()'),(24,'effects: new fields.ArrayField'),(28,'min: 0, max: 100'),(30,'applied: new fields.BooleanField({ initial: false })')]:self.assertIn(v,s[a-1])
        names=re.findall(r'^\s+(\w+): new fields\.', '\n'.join(self.source(100)), re.M)
        self.assertEqual(names,['itemUuid','formula','crit','strike','type','originalLocation','location','properties'])
        self.assertNotIn('duration',t);self.assertNotIn('getPreprocessedEffects',t)
        self.assertIn('extends foundry.abstract.DataModel',self.source(95)[2]);self.assertEqual(re.findall(r'^\s+(\w+): new fields\.', '\n'.join(self.source(95)), re.M),['rollTotal'])
        self.assertEqual(''.join(self.source(51)).strip(),'export default class WitcherChatMessage extends ChatMessage {}')
        dto='\n'.join(self.source(50));self.assertIn('this.system = system',dto);self.assertIn('this.flags = flags',dto);self.assertNotIn('ChatMessage.create',dto);self.assertNotIn('this.type', '\n'.join(self.source(50)[9:]))
        calls={r['to'] for r in self.edges('DamageMessageData.defineSchema','calls')};self.assertEqual(calls,{self.q[n] for n in ['BaseMessageData.defineSchema','chat.damageData()','DamageProperties.defineSchema']})
        self.assertNotEqual(self.q['DamageMessageData.damage.properties.effects.name'],self.q['itemEffect().name'])

    def test_roll_formula_effect_copies_and_wait_order(self):
        s=self.source(159);t='\n'.join(s)
        for a,v in [(10,'properties: this.system.damageProperties'),(14,'this.parent.system.attackStats.critLocationModifier'),(17,'defenseOptions: this.system.defenseOptions'),(24,"'' + damage.formula"),(26,'damage.properties.variableDamage'),(27,'await this.createVariableDamageDialog'),(30,"damageFormula == ''"),(31,"damageFormula = '0'"),(36,'(${damageFormula})'),(40,'damage.location = WitcherActor.getLocationObject(damage.location.name)'),(47,'damage.properties.getPreprocessedEffects()'),(57,'CONFIG.WITCHER.statusEffects.find'),(60,'if (effect.percentage)'),(61,'getRandomInt(100)'),(63,'rollPercentage > effect.percentage'),(65,'effect.applied = false'),(68,'effect.applied = true'),(77,'new ChatMessageData(this.parent'),(80,'effects: preprocessedEffects'),(83,'await (await new Roll(damageFormula).evaluate()).toMessage(messageData)'),(84,"message.setFlag('TheWitcherTRPG', 'damage'")]:self.assertIn(v,s[a-1])
        self.assertNotIn('extendedRoll',t);self.assertNotIn('system.rollTotal',t);self.assertNotIn('await',s[83]);self.assertNotRegex('\n'.join(s[82:88]),r'return\s')
        self.assertIn('effectsArray.push({ ...effect })',self.source(130)[92]);self.assertIn('existingStatus.percentage += effect.percentage',self.source(130)[90])
        steps=self.steps(219);self.assertEqual(steps['message']['next'][0]['flow'],'await');self.assertEqual(steps['flag']['next'][0]['flow'],'scheduled')
        self.assertFalse(any(p['entry']['entity'] in {self.q['extendedRoll'],self.q['item.damageUtilMixin.createBaseDamageObject'],self.q['DamageProperties.getPreprocessedEffects']} for p in self.new['processes']))
        e=self.q['item.damageUtilMixin.rollDamage/effect.callback'];edges=self.data.outgoing[e];self.assertEqual({r['location']['line_start'] for r in edges if r['kind']=='computes' and r['to']==self.q['DamageMessageData.damage.properties.effects.applied']},{65,68})

    def test_variable_input_markup_and_exact_localization(self):
        s=self.source(159);h=self.source(509)
        self.assertIn('currentDamage: damageFormula',s[93]);self.assertIn('button.form.elements.newDamage.value',s[99]);self.assertIn('rejectClose: true',s[103]);self.assertNotIn('cssClass','\n'.join(s[89:]));self.assertIn('{{cssClass}}',h[0])
        self.assertIn('type=\'text\' value="{{currentDamage}}" name=\'newDamage\'',h[3]);self.assertIn('WITCHER.Item.DamageProperties.variableDamage',h[1]);self.assertIn('WITCHER.Item.properties.variableDamage',s[101])
        self.assertIn('<div class="damage-message" <h1>',s[21]);self.assertNotIn('data-duration',s[57]);self.assertIn("data-status='${effect.statusEffect}'",s[57]);self.assertNotIn('applied','\n'.join(s[51:59]))
        self.assertIn('.percentageFailed',self.source(451)[0]);self.assertIn('.percentageSuccess',self.source(451)[5]);self.assertIn('.apply-status',self.source(451)[9])
        for lang in ['en','ru']:
            payload=json.loads((ROOT/'lang'/f'{lang}.json').read_text());out={}
            def flat(obj,prefix=''):
                for k,v in obj.items():
                    n=prefix+'.'+k if prefix else k
                    if isinstance(v,dict):flat(v,n)
                    else:out[n]=v
            flat(payload);self.assertIn('WITCHER.Item.DamageProperties.variableDamage',out);self.assertNotIn('WITCHER.Item.properties.variableDamage',out)

    def test_damage_instance_fields_setters_and_selected_writers(self):
        s=self.source(197);t='\n'.join(s)
        self.assertNotIn('import ',t);self.assertNotIn('DataModel',t);self.assertNotIn('game.',t)
        initial=re.findall(r'this\.(\w+) = ([^;]+);','\n'.join(s[1:12]));self.assertEqual(initial,[('initialDamage','damage'),('damage','damage'),('type','null'),('shielded','null'),('blocked','null'),('afterSp','null'),('afterLocation','null'),('afterResistance','null'),('source','null')])
        self.assertEqual(t.count('return this;'),3);self.assertEqual(t.count("(this.source ? '[' + this.source + ']' : '')"),5)
        for name,field,a in [('setType','type',19),('setShielded','shielded',24),('setSource','source',29)]:self.assertIn('this.'+field+' = '+field,s[a-1])
        d=self.source(14);self.assertIn("damageInstances[0].setType = 'silver'",d[164]);self.assertNotIn('.setType(',d[164]);self.assertIn('instance.afterSp = instance.damage',d[184]);self.assertIn('instance.afterLocation = instance.damage',d[207]);self.assertIn('instance.afterResistance = instance.damage',d[232])
        calls=[r for r in self.data.incoming[self.q['DamageInstance.setShielded']] if r['kind']=='calls'];self.assertEqual(calls,[])
        ty=self.q['DamageInstance.setType'];self.assertNotIn(165,{r['location']['line_start'] for r in self.data.incoming[ty] if r['kind']=='calls' and r['location']['source']=='src-000014'})
        blocked=[r['from'] for r in self.data.incoming[self.q['DamageInstance.blocked']] if r['kind']=='computes'];self.assertEqual(blocked,[self.q['DamageInstance.constructor']])
        for a,n in [(272,'initialDamageText'),(273,'afterSpText'),(274,'afterLocationText'),(275,'afterResistanceText'),(276,'damageText')]:self.assertIn('instance.'+n+'()',d[a-1])

    def test_consumers_read_system_and_dom_and_mutate_prepared_data(self):
        s=self.source(194)
        for a,v in [(7,"li.querySelector('.damage-message')"),(16,"parseInt(li.querySelector('.dice-total').innerText)"),(17,'li.dataset.messageId'),(28,"parseInt(li.querySelector('.dice-total').innerText)"),(39,"message.system.damage.properties.isNonLethal ? 'sta' : 'hp'"),(104,'game.messages.get(messageId).system.damage'),(106,'await createApplyDamageDialog'),(109,'damageProperties.location = actor.getLocationObject'),(113,'damageProperties.properties.oilEffect = actor.system.category'),(118,'DamageInstance.create(totalDamage).setType(damageProperties.type)')]:self.assertIn(v,s[a-1])
        self.assertNotIn('getFlag','\n'.join(s));self.assertNotIn('rollTotal','\n'.join(s));self.assertNotIn('.update(','\n'.join(s));self.assertNotIn('await',s[115])
        d=self.source(14);self.assertIn('.filter(effect => effect.applied)',d[27]);self.assertIn('damageObject.duration',d[28]);self.assertIn('damageObject.duration',d[31]);self.assertNotIn('applied','\n'.join(self.source(205)[14:28]))
        self.assertEqual({r['from'] for r in self.data.incoming[self.q['DamageMessageData.damage']] if r['kind']=='reads' and r['location']['source']=='src-000194'},{self.q['applyDamageFromMessage']})

    def test_external_cleaning_and_roll_contract_addresses(self):
        r=Path('/opt/foundryvtt/client/dice/roll.mjs').read_text().splitlines();f=Path('/opt/foundryvtt/common/data/fields.mjs').read_text().splitlines()
        body='\n'.join(r[925:953]);self.assertIn('content: String(this.total)',body);self.assertIn('messageData.rolls = [this]',body);self.assertIn('return cls.create(msg)',body);self.assertNotIn('rollTotal',body)
        self.assertIn('this.#cleanKeys(data, options.prune, options.persisted)',f[1078]);self.assertIn('!field && prune',f[1138]);self.assertIn('delete data[k]',f[1139])
        self.assertIn('Number.isInteger(i) && (i >= 0)',f[2374]);self.assertIn('Math.max(value, this.min)',f[1519]);self.assertIn('Math.min(value, this.max)',f[1520])
        rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',(BASE/'coverage-017.md').read_text(),re.M);self.assertEqual(len(rows),2)
        for path,digest in rows:self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)


    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[71,247,19])
        # Historical .017 range; omitted duplicate3706 remains absent.
        historical={k:[r for r in getattr(d,k).values() if int(r['id'].split('-')[1])<=cap]
                    for k,cap in [('entities',4192),('relations',10013),('processes',230)]}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,4191,10013,230])
        represented={e['location']['source'] for e in historical['entities'] if e['kind']!='boundary' and e.get('location')}
        self.assertEqual(len(represented),227)
        self.assertEqual(615-len(represented),388)
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

