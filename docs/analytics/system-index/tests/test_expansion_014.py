"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class WeaponPropertiesExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-014.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_26_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-014-queries.json').read_text())['cases']
        self.assertEqual(len(cases),26)
        self.assertEqual({c['question'] for c in cases},{f'IQ-{n:02}' for n in range(1,9)})
        for c in cases:
            with self.subTest(case=c['id']):
                run=run_cli([*c['command'],'--format','json'],cwd='/tmp')
                self.assertEqual(run.returncode,0,run.stderr)
                out=json.loads(run.stdout);rows=out['items']
                if c['id']=='WPN-07':
                    # Preserve the original case on its historical relation slice;
                    # .031 adds the source-verified Spell model to this delegation.
                    self.assertEqual({r['from'] for r in rows},
                                     {self.q[q] for q in ['WeaponData.defineSchema', 'skillAttack()', 'SpellData.defineSchema']})
                    rows=[r for r in rows if int(r['id'].split('-')[1])<=8995]
                first=rows[0] if rows else {}
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


    def test_schema_owners_actual_names_and_defaults(self):
        for q,n,a,token in [('attackOptions()',129,3,'function attackOptions'),('DefenseProperties',132,3,'class DefenseProperties'),('skillAttack()',133,7,'function skillAttack'),('skillDefense()',134,5,'function skillDefense'),('DamageProperties.effects',130,49,'TypedObjectField'),('attackOptions().attackOptions',129,5,'SetField')]:
            e=self.data.entities[self.q[q]];self.assertEqual((e['location']['source'],e['location']['line_start']),(f'src-{n:06}',a));self.assertIn(token,self.source(n)[a-1])
        for owner in ['WeaponData','DamageProperties','DefenseProperties','attackOptions()','defenseOptions()','skillAttack()','skillDefense()','weaponType()']:
            for e in self.data.entities.values():
                if e['kind']!='field' or e['owner']!=self.q[owner] or e['name']=='enhancementItems':continue
                l=e['location'];src=self.source(int(l['source'][4:]));self.assertRegex(src[l['line_start']-1],r'\b'+re.escape(e['name'])+r'\s*:',e['qualified_name'])
        s='\n'.join(self.source(129));self.assertIn("initial: 'spellcasting'",s);self.assertNotIn('choices:',s);self.assertNotIn('prepare',s)
        self.assertIn('source.applyMeleeBonus ?? false',s);self.assertNotRegex('\n'.join(self.source(155)),r'^\s*attackSkill\s*:',re.M)
        self.assertIn('new fields.ArrayField',self.source(137)[10]);self.assertNotRegex('\n'.join(self.source(142)),r'\bid\s*:')
        self.assertNotIn('defenseProperties','\n'.join(self.source(133)))

    def test_migrations_prepared_state_and_effect_merge(self):
        s=self.source(155)
        self.assertIn('this.parent.actor.items',s[75]);self.assertIn('id: itemId',s[84]);self.assertIn('enhancement._id',s[103]);self.assertIn('this.effects?.forEach',s[108])
        self.assertIn('migrateDamageProperties(source)',s[110]);self.assertIn('super.migrateData(source)',s[112])
        self.assertIn('...this.effects, ...effects',self.source(130)[65]);self.assertIn('source.effects.length > 0',self.source(130)[107]);self.assertIn('randomID()',self.source(130)[110])
        pre='\n'.join(self.source(130)[78:98]);self.assertIn('effect.statusEffect &&',pre);self.assertIn('existingStatus.percentage += effect.percentage',pre);self.assertIn('{ ...effect }',pre);self.assertNotIn('Math.min',pre)
        merge='\n'.join(self.source(25)[327:355]);self.assertIn('Array.isArray(properties[key])',merge);self.assertNotIn('addEffects',merge);self.assertNotIn('typeof properties[key] === \'object\'',merge)
        self.assertEqual({r['from'] for r in self.data.incoming[self.q['DamageProperties.addEffects']] if r['kind']=='calls' and r['location']['source']=='src-000025'},{self.q['actor.weaponAttackMixin.weaponAttack']})
        p=self.data.processes['proc-000158'];st={x['id']:x for x in p['steps']};self.assertIn('lookup',{x.get('step') for x in st['append']['next']});self.assertNotIn('reset',{x.get('step') for x in st['append']['next']})

    def test_configuration_controls_writers_and_template_paths(self):
        s=self.source(186)
        for a,t in [(91,'{ percentage: 0 }'),(96,"closest('.list-item').dataset.id"),(105,'${target}.${id}.${field}'),(112,'${target}.-=${id}')]:self.assertIn(t,s[a-1])
        for a in [81,83,91,105,112]:self.assertNotIn('await',s[a-1])
        self.assertIn("value == 'on'",s[100]);self.assertIn('checked',s[101]);self.assertNotIn('findIndex','\n'.join(s))
        for a,t in [(59,'!system.damageProperties'),(73,'!system.damageProperties && !system.causeDamages'),(75,'!system.createTemplate')]:self.assertIn(t,s[a-1])
        h='\n'.join(self.source(592));self.assertIn('data-id="{{id}}"',h);self.assertIn('system.damageProperties.effects',h);self.assertIn('disabled',h)
        self.assertNotIn('name=','\n'.join(self.source(592)[32:60]));self.assertIn('settings.silverTrait',h);self.assertIn('staminaIsVar',h)
        for n in [585,594]:self.assertNotIn('itemUseAttackSkill','\n'.join(self.source(n)))
        self.assertNotIn('attackOptionsPart','\n'.join(self.source(594)))
        for c in self.new['entities']:
            if '.form.system.' not in c['qualified_name']:continue
            l=c['location'];line=self.source(int(l['source'][4:]))[l['line_start']-1];field=c['qualified_name'].rsplit('.',1)[-1];self.assertIn(field,line,c['qualified_name']);self.assertEqual(c['aliases'],[c['qualified_name'].split('.form.',1)[1]])
        self.assertEqual({r['from'] for r in self.data.incoming[self.q['DamageProperties.effects']] if r['kind']=='writes' and r['location']['source']=='src-000186'}, {self.q['WitcherPropertiesConfigurationSheet.'+n] for n in ['_onAddEffect','_onEditEffect','_oRemoveEffect']})

    def test_attack_and_defense_payload_boundaries(self):
        self.assertEqual(self.q['DocumentSheetV2.#onSubmitDocumentForm'],'ent-000910')
        self.assertNotIn('ItemSheetV2/automatic-form-submit',self.q)
        s=self.source(192)
        for a,t in [(35,'!this.system.attackOptions'),(43,'Object.values(options).every'),(48,'= 3'),(51,'= 2'),(54,'= 1'),(58,'Math.min'),(61,'[...this.system.attackOptions]'),(63,"attackOption + 'AttackSkill'"),(67,'WITCHER.skillMap')]:self.assertIn(t,s[a-1])
        self.assertNotIn('applyRangedMeleeBonus','\n'.join(self.source(25)))
        self.assertIn('meleeAttackSkill ?? this.rangedAttackSkill ?? this.spellAttackSkill ?? this.itemUseAttackSkill',self.source(155)[55])
        self.assertIn('this.defendsAgainst.has(attack)',self.source(132)[15]);self.assertNotIn('isDefense','\n'.join(self.source(132)))
        self.assertIn('isApplicableDefense?.(attack.attackOption)',self.source(16)[18]);self.assertIn('createDefenseOption(attack)',self.source(16)[19])
        self.assertNotRegex('\n'.join(self.source(108)),r'\bisApplicableDefense\s*\(')
        for name,a,token in [('WitcherItem.getItemAttack',30,'weapon.getItemAttack'),('actor.weaponAttackMixin.mergeDamageProperties',138,'this.mergeDamageProperties')]:
            self.assertIn(token,self.source(25)[a-1]);self.assertTrue(any(r['to']==self.q[name] and r['location']['line_start']==a for r in self.edges('actor.weaponAttackMixin.weaponAttack','calls')))

    def test_type_custom_handler_and_external_core(self):
        s=self.source(181);self.assertIn(".find('.damage-type').on('change'",s[32]);self.assertIn('newval[element.id] = !newval[element.id]',s[41]);self.assertNotIn('checked','\n'.join(s[37:50]));self.assertNotIn('await',s[48]);self.assertIn("types.join(', ')",s[47])
        h='\n'.join(self.source(613));self.assertIn('class="damage-type"',h)
        core=Path('/opt/foundryvtt/common/data/fields.mjs');t=core.read_text();self.assertLess(t.index('this.#cleanKeys(data, options.prune, options.persisted)'),t.index('for ( const [name, field] of this.entries() )',t.index('_cleanType(data, options, _state)')))
        self.assertIn('data[k2] = new ForcedDeletion()',t)
        rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',(BASE/'coverage-014.md').read_text(),re.M)
        self.assertEqual(len(rows),1)
        for path,digest in rows:self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)

    def test_graph_addresses_reverse_links_facets_and_processes(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[197,536,21])
        # Historical .014 allocated through entity3894, with unpublished duplicate3706 omitted.
        historical={k:[r for r in getattr(d,k).values() if int(r['id'].split('-')[1])<=cap]
                    for k,cap in [('entities',3894),('relations',8995),('processes',176)]}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,3893,8995,176])
        represented={e['location']['source'] for e in historical['entities'] if e['kind']!='boundary' and e.get('location')}
        self.assertEqual(len(represented),213)
        self.assertEqual(615-len(represented),402)
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

