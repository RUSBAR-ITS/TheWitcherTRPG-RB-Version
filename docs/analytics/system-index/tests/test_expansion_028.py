"""Проверки справочника по исходникам; игровые документы и БД не исполняются."""
import collections
import hashlib
import json
import re
import unittest
from pathlib import Path
from test_query import BASE, ROOT, query, run_cli

class ProfessionEditorExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l)for l in(BASE/f'data/{k}/expansion-028.jsonl').read_text().splitlines()]for k in ['entities','relations','processes']}
    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]]if r['kind']==kind]
    def test_33_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-028-queries.json').read_text())['cases']
        self.assertEqual(len(cases),33)
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

    def test_model_tree_has_ten_slots_distinct_from_base_skill_set(self):
        model='\n'.join(self.source(121));path='\n'.join(self.source(147));skill='\n'.join(self.source(148))
        self.assertIn('definingSkill: new fields.SchemaField(professionSkill())',model)
        for n in range(1,4):
            self.assertIn(f'skillPath{n}: new fields.SchemaField(professionPath())',model)
            self.assertIn(f'skill{n}: new fields.SchemaField(professionSkill())',path)
        self.assertIn('professionSkills: new fields.SetField(',model)
        self.assertIn('level: new fields.NumberField({ initial: 0 })',skill)
        self.assertNotIn('min:',skill);self.assertNotIn('max:',skill);self.assertNotIn('choices:',skill)
        for q,owner in [('ProfessionData.professionSkills','ProfessionData'),('professionPath().skill1','professionPath()'),('professionSkill().level','professionSkill()'),('SkillUsage.temporaryHealth','SkillUsage'),('TemporaryHealth.temporaryHp.duration','TemporaryHealth'),('Threshold.thresholds.*.value','Threshold')]:
            self.assertEqual(self.data.entities[self.q[q]]['owner'],self.q[owner])
        self.assertNotEqual(self.q['ProfessionData.professionSkills'],self.q['WitcheProfessionSheet.context.professionSkills'])

    def test_main_form_enrichment_and_actor_raw_consumers_are_separate(self):
        model='\n'.join(self.source(121));form='\n'.join(self.source(607));char='\n'.join(self.source(526)[:261]);mon='\n'.join(self.source(572))
        self.assertEqual(model.count('await createEnrichedText'),11)
        self.assertEqual(form.count('formInput enrichedText.'),11)
        self.assertEqual(char.count('{{editor profession.system.'),11)
        self.assertEqual(len(re.findall(r'{{editor\s+profession\.system\.',mon)),2)
        self.assertNotIn('enrichedText',char+mon);self.assertNotIn('skillPath',mon)
        prep='\n'.join(self.source(29)[150:171]);m='\n'.join(self.source(31)[110:134])
        self.assertIn('await context.profession?.system.enrichedText()',prep)
        self.assertNotIn('profession.system.enrichedText',m)
        b=self.q['ProfessionData/Actor-raw-editor'];self.assertFalse(any(r['kind']=='writes'for r in self.data.outgoing[b]))
        self.assertEqual(self.data.entities[self.q['templates/partials/character/tab-profession.hbs']]['location']['line_start'],1)
        # The previously indexed race block remains at the same address.
        self.assertIn(self.q['perk().description'],{r['to']for r in self.edges('templates/partials/character/tab-profession.hbs','reads')})

    def test_parts_pass_concrete_schema_and_values_without_defining_configuration(self):
        cf='WitcherProfessionConfigurationSheet';js='\n'.join(self.source(185)[:90]);partial='\n'.join(self.source(587));hbs='\n'.join(self.source(588));sh='\n'.join(self.source(175))
        self.assertNotIn('definingSkill',js)
        self.assertIn('class WitcheProfessionSheet',sh);self.assertIn(".filter(key => key != 'none')",sh)
        self.assertIn('context.config = CONFIG.WITCHER','\n'.join(self.source(172)))
        for n in range(1,4):
            self.assertIn(f'skillFields=skillPathFields.fields.skill{n} skill=skillPath.skill{n}',partial)
            self.assertIn(f'context.item.system.skillPath{n}',js)
        self.assertIn('systemFields=skillFields.fields.skillAttack.fields system=skill.skillAttack',hbs)
        self.assertIn('options=config.statOptions',hbs)
        self.assertIn(self.q['WITCHER.statOptions'],{r['to']for r in self.edges('WitcheProfessionSheet._prepareContext','writes')})
        self.assertIn(self.q['TemporaryHealth.temporaryHp.duration'],{r['to']for r in self.edges(cf+'/schema-form-submit','writes')})

    def test_lookup_owners_and_first_match_order_are_not_row_ids(self):
        cf='WitcherProfessionConfigurationSheet';s='\n'.join(self.source(185)[181:211]);a='\n'.join(self.source(20)[380:414]);h='\n'.join(self.source(588))
        self.assertNotIn('definingSkill',s);self.assertIn('definingSkill',a)
        self.assertLess(a.index('definingSkill'),a.index('skillPath1'))
        for body in [s,a]:
            self.assertLess(body.index('skillPath1'),body.index('skillPath2'));self.assertLess(body.index('skillPath2'),body.index('skillPath3'))
            self.assertIn('skillPath.skill1.skillName === skillName',body);self.assertIn('return null',body)
        for owner in [cf,'actor.professionMixin']:
            self.assertEqual(self.data.entities[self.q[owner+'.findSkillWithName']]['owner'],self.q[owner])
        self.assertIn('data-id="{{id}}" data-target="{{../skill.skillName}}"',h)
        self.assertIn('data-target="{{skill.skillName}}"',h)
        self.assertNotIn('randomID',s+a)

    def test_crud_writes_correct_item_paths_without_await_or_return(self):
        cf='WitcherProfessionConfigurationSheet';ls=self.source(185)
        specs=[('_onAddEffectDamageProperties',102,112,'DamageProperties.effects'),('_onEditEffectDamageProperties',114,131,'DamageProperties.effects'),('_oRemoveEffectDamageProperties',133,142,'DamageProperties.effects'),('_onAddThreshold',144,153,'Threshold.thresholds'),('_onEditThreshold',155,168,'Threshold.thresholds'),('_oRemoveThreshold',170,180,'Threshold.thresholds')]
        for method,a,b,target in specs:
            text='\n'.join(ls[a-1:b]);self.assertIn('this.item.update(',text);self.assertNotIn('await this.item.update',text);self.assertNotIn('return this.item.update',text)
            self.assertIn('this.findSkillWithName(skillName)',text)
            self.assertIn('skillAttack.damageProperties.effects'if'Effect'in method else'thresholds.thresholds',text)
            self.assertIn(self.q[target],{r['to']for r in self.edges(cf+'.'+method,'writes')})
            p=next(p for p in self.new['processes']if p['entry']['entity']==self.q[cf+'.'+method]);self.assertEqual(p['steps'][-1]['next'][0]['flow'],'scheduled')
        self.assertIn("value == 'on'",'\n'.join(ls[113:131]));self.assertNotIn('checked','\n'.join(ls[154:168]))
        for block in [ls[101:112],ls[143:153]]:self.assertIn('foundry.utils.randomID()','\n'.join(block))
        self.assertIn('effects.-=${effectId}','\n'.join(ls[132:142]))
        self.assertIn('thresholds.thresholds.-=${id}','\n'.join(ls[169:180]))

    def test_broken_remove_action_is_not_a_successful_ui_call(self):
        cf='WitcherProfessionConfigurationSheet';js='\n'.join(self.source(185));h='\n'.join(self.source(588))
        self.assertIn('removeEffect: WitcherProfessionConfigurationSheet._oRemoveEffectDamageProperties',js)
        self.assertIn('data-action="removeEffectDamageProperties"',h)
        self.assertNotIn('removeEffectDamageProperties:',js)
        self.assertIn('let element = event.currentTarget','\n'.join(self.source(185)[132:142]))
        t='templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs'
        self.assertNotIn(self.q[cf+'._oRemoveEffectDamageProperties'],{r['to']for r in self.edges(t,'calls')})
        self.assertIn(self.q[cf+'/removeEffectDamageProperties-action'],{r['to']for r in self.edges(t,'passes')})
        for e in ['addEffectDamageProperties','addThreshold','removeThreshold']:
            self.assertIn(self.q[cf+'.actions.'+e],{r['to']for r in self.edges(t,'passes')})

    def test_inline_level_total_and_dispatch_do_not_change_profession_semantics(self):
        inline='\n'.join(self.source(43)[127:145]);total='\n'.join(self.source(20)[8:28]);roll='\n'.join(self.source(20)[29:43])
        self.assertIn("element.closest('.item').dataset.itemId",inline);self.assertIn('return item.update({ [field]: value })',inline)
        self.assertEqual(total.count('Number('),10);self.assertNotIn('.update(',total)
        for fld in ['skillName','stat','level']:self.assertIn(self.q['professionSkill().'+fld],{r['to']for r in self.edges('sheet.itemMixin._onItemInlineEdit','writes')})
        self.assertIn("closest('.profession-display').dataset.name",roll)
        self.assertLess(roll.index('isAttack'),roll.index('hasCustomEffect'));self.assertLess(roll.index('hasCustomEffect'),roll.index('hasThresholds'))
        self.assertIn(self.q['actor.professionMixin/dispatch-execution-029'],{r['to']for r in self.edges('actor.professionMixin._onProfessionRoll','passes')})
        defense='\n'.join(self.source(121)[48:77]);self.assertNotIn('isDefense',defense);self.assertNotIn('definingSkill',defense)
        self.assertIn(self.q['professionSkill().level'],{r['to']for r in self.edges('ProfessionData.findDefenseSkillData','reads')})

    def test_core_hashes_and_old_issue_refs_are_not_new_runtime_evidence(self):
        evidence=json.loads((BASE/'examples/expansion-028-queries.json').read_text())['core_evidence']
        for e in evidence:self.assertEqual(hashlib.sha256(Path(e['path']).read_bytes()).hexdigest(),e['sha256'])
        cf='WitcherProfessionConfigurationSheet'
        for q,n in [(cf+'/removeEffectDamageProperties-action',111),(cf+'/skill-name-lookup',110),('ProfessionData/Actor-raw-editor',109),('Threshold.hasThresholds',119)]:
            self.assertIn(f'docs/issues/potential/issue-{n:05}.md',{r['path']for r in self.data.entities[self.q[q]]['refs']})
        for q in ['WitcheProfessionSheet/named-form-submit',cf+'/schema-form-submit']:
            self.assertIn(self.q['Document.update/Item'],{r['to']for r in self.edges(q,'calls')})
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
        self.assertEqual({k:len(v)for k,v in self.new.items()},{'entities':90,'relations':642,'processes':15})

if __name__=='__main__':unittest.main()
