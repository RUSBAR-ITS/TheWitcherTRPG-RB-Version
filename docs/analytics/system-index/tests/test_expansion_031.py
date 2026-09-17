"""Проверки справочника по исходникам; игровые документы и БД не исполняются."""
import collections
import hashlib
import json
import re
import unittest
from pathlib import Path
from test_query import BASE, ROOT, query, run_cli

class MagicItemEditorExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l)for l in(BASE/f'data/{k}/expansion-031.jsonl').read_text().splitlines()]for k in ['entities','relations','processes']}
    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]]if r['kind']==kind]
    def test_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-031-queries.json').read_text())['cases']
        self.assertEqual(len(cases),43)
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

    def body(self,s,a=1,b=None):return '\n'.join(self.source(s)[a-1:b])
    def targets(self,q,kind):return {r['to']for r in self.edges(q,kind)}
    def test_models_inheritance_defense_and_distinct_capabilities(self):
        expected={'HexData':{'danger','stamina','effect','liftRequirement'},'RitualData':{'level','stamina','staminaIsVar','effect','range','duration','defence','components','ritualComponentUuids','alternateRitualComponentUuids','preparationTime','difficultyCheck','templateProperties','regionProperties'},'SpellData':{'class','level','source','domain','sideEffect','stamina','staminaIsVar','effect','range','duration','defence','templateProperties','regionProperties','causeDamages','damage','damageType','damageProperties','createsShield','shield','doesHeal','heal','selfEffects','onCastEffects','defenseProperties'}}
        for c,s,first,last in [('HexData',115,7,20),('RitualData',123,11,37),('SpellData',125,16,60)]:
            own={e['name']for e in self.data.entities.values()if e.get('owner')==self.q[c]and e['kind']=='field'and first<=e['location']['line_start']<=last};self.assertEqual(own,expected[c])
            self.assertIn(self.q['CommonItemData'],self.targets(c,'extends'));self.assertIn('...defenseOptions()',self.body(s,first,last))
        self.assertNotIn('attackOptions()',self.body(115));self.assertNotIn('attackOptions()',self.body(123))
        self.assertIn('...attackOptions()',self.body(125));self.assertIn('Object.assign(SpellData.prototype, spellRegionMixin)',self.body(125));self.assertIn('Object.assign(RitualData.prototype, spellRegionMixin)',self.body(123));self.assertNotIn('spellRegionMixin',self.body(115))
        self.assertIn(self.q['DefenseProperties.createDefenseOption'],self.targets('SpellData.createDefenseOption','calls'))
        self.assertIn('return true',self.body(125,81,83));self.assertIn('return false',self.body(109,22,24))
    def test_skill_priority_matches_type_and_class_fallback(self):
        for s,a,c in [(115,22,'HexData'),(123,39,'RitualData'),(125,62,'SpellData')]:
            b=self.body(s,a,a+6);self.assertIn('CONFIG.WITCHER.skillMap[this.spellAttackSkill] ??',b);self.assertIn('CONFIG.WITCHER.magic[this.parent.type]?.skill ??',b);self.assertIn('CONFIG.WITCHER.magic[this.class].skill',b)
            self.assertIn(self.q[c+'.getUsedSkill'],self.targets('actor.castSpellMixin.castSpell','calls'))
        self.assertIn("initial: 'spellcasting'",self.body(129,28,32));self.assertIn('skill: WITCHER.skillMap.spellcast',self.body(209,712,731))
        self.assertIn('skill: WITCHER.skillMap.ritcraft',self.body(209,712,731));self.assertIn('skill: WITCHER.skillMap.hexweave',self.body(209,712,731))
        self.assertNotIn('spellAttackSkill:',self.body(115,7,20));self.assertNotIn('class:',self.body(123,11,37))
        p=self.data.processes['proc-000426'];self.assertEqual([n['step']for n in p['steps'][0]['next']if'step'in n],['type']);self.assertEqual([n['step']for n in p['steps'][1]['next']if'step'in n],['class'])
    def test_migrations_change_source_without_document_update(self):
        for s,a,b in [(125,117,134),(123,75,88)]:
            t=self.body(s,a,b);self.assertIn('if (source.templateSize)',t);self.assertIn('source.templateProperties = {}',t)
            for k in ['createTemplate','templateSize','templateType','visualEffectDuration']:
                self.assertIn(f'source.templateProperties.{k} = source.{k}',t);self.assertIn(f'delete source.{k}',t)
            self.assertNotIn('.update(',t)
        self.assertIn('parseInt(source.templateSize) || 0',self.body(125,117,134));self.assertNotIn('parseInt',self.body(123,75,88))
        t=self.body(125,86,115)
        self.assertLess(t.index('migrateDamageProperties(source)'),t.index('this.migrateEffectsToTypedField(source)'));self.assertLess(t.index('this.migrateEffectsToTypedField(source)'),t.index('this.migrateTemplate(source)'))
        self.assertIn('this.effects?.forEach',t);self.assertNotIn('source.effects?.forEach',t)
        for k in ['selfEffects','onCastEffects']:self.assertIn(f'Array.isArray(source.{k}) && source.{k}.length > 0',t)
        self.assertEqual(t.count('foundry.utils.randomID()'),2)
        self.assertIn("source.system?.class === 'Hexes'",self.body(192));self.assertIn("source.type = 'ritual'",self.body(192))
    def test_forms_current_nested_paths_legacy_requests_and_inheritance(self):
        h=self.body(611);r=self.body(609);header=self.body(540)
        for f in ['createTemplate','templateSize','templateType','visualEffectDuration']:
            self.assertIn(f'name="system.templateProperties.{f}"',h);self.assertIn(f'name="system.{f}"',r)
            self.assertNotIn(f'name="system.templateProperties.{f}"',r)
        self.assertIn(self.q['TemplateProperties.templateSize'],self.targets('SpellData/named-item-form-submit','writes'));self.assertNotIn(self.q['TemplateProperties.templateSize'],self.targets('RitualData/named-item-form-submit','writes'))
        self.assertIn(self.q['RitualData/legacy-template-form-paths'],self.targets('RitualData/named-item-form-submit','writes'))
        self.assertIn('data-action="editImage"',header);self.assertNotIn('data-action="editImage"',r);self.assertNotIn('data-action="editImage"',self.body(602))
        self.assertIn("configuration = new WitcherSpellConfigurationSheet({ document: this.item })",self.body(179))
        for s in [170,177]:self.assertNotIn('configuration =',self.body(s))
        self.assertIn('...super.PARTS',self.body(187));self.assertIn("if (!system.createTemplate) delete parts.regionProperties",self.body(186))
        self.assertIn('1d6+0',h);self.assertIn('initial: null',self.body(125,39,39))
    def test_component_schema_resolution_and_prepared_identity(self):
        c=self.body(135);p=self.body(123);h=self.body(609,121,160)
        self.assertIn('new fields.DocumentUUIDField()',c);self.assertIn('quantity: new fields.NumberField({ initial: 0 })',c)
        for f in ['img:','name:','id:']:self.assertNotIn('        '+f,c)
        self.assertEqual(p.count('fromUuidSync(component.uuid) ?? { name: component.uuid }'),2)
        self.assertEqual(p.count('uuid: component.uuid'),2);self.assertEqual(p.count('img: component.img'),2);self.assertNotIn('.update(',p);self.assertNotIn('await ',p)
        self.assertEqual(h.count('data-uuid="{{component.uuid}}"'),2);self.assertEqual(h.count('class="edit-component"'),2)
        self.assertNotIn('name=',h);self.assertEqual(h.count('data-field="quantity"'),2)
        self.assertIn('RitualData.ritualComponents',self.q);self.assertIn('RitualData.alternateRitualComponents',self.q)
        cast=self.body(11)
        for f in ['ritualComponentUuids','alternateRitualComponentUuids','ritualComponents','alternateRitualComponents']:self.assertNotIn(f,cast)
        self.assertIn('{{spellItem.system.alternateRitualComponents}}',self.body(487));self.assertNotIn('{{#each spellItem.system.alternateRitualComponents',self.body(487))
    def test_component_crud_selection_first_edit_all_remove_and_async_boundary(self):
        text=self.body(177);drop=text[text.index('async _onDropItem'):text.index('_onEditComponent(event)')]
        edit=text[text.index('    _onEditComponent(event)'):text.index('    _onRemoveComponent(event)')]
        remove=text[text.index('    _onRemoveComponent(event)'):]
        self.assertIn("event.target.closest('.alternateComponents')",drop)
        self.assertEqual(drop.count('push({ uuid: item.uuid, quantity: 1 })'),2)
        self.assertIn('components.findIndex(obj => obj.uuid == itemId)',edit)
        self.assertIn('if (objIndex < 0) return',edit);self.assertIn('Number.isFinite(quantity)',edit)
        self.assertIn('components[objIndex][field] = quantity',edit)
        self.assertIn('.filter(item => item.uuid !== itemId)',remove)
        for t in [edit,remove]:self.assertIn('return this.item.update',t)
        self.assertIn('return (await this._onDropItem(event, document)) ?? null',self.body(172))
        for pid in ['proc-000436','proc-000437']:
            self.assertEqual(self.data.processes[pid]['steps'][-1]['next'][0]['flow'],'await')
        for q in ['RitualData.ritualComponentUuids','RitualData.alternateRitualComponentUuids']:
            for meth in ['_onDropItem','_onEditComponent','_onRemoveComponent']:self.assertIn(self.q[q],self.targets('WitcherRitualSheet.'+meth,'writes'))
    def test_keyed_statuses_text_and_active_effects_are_separate(self):
        s=self.body(125);h=self.body(597)
        for n in ['selfEffects','onCastEffects']:
            self.assertIn(f'{n}: new fields.TypedObjectField(new fields.SchemaField(itemEffect()))',s);self.assertIn('data-target=\'system.'+n+'\'',h)
        self.assertEqual(h.count('data-field="statusEffect"'),2)
        for f in ['name','percentage','varEffect']:self.assertNotIn('data-field="'+f+'"',h)
        self.assertIn('{ percentage: 0 }',self.body(186,87,92));self.assertIn('`${target}.-=${id}`',self.body(186,108,115))
        self.assertIn('spellItem.system.selfEffects?.length > 0',self.body(11));self.assertIn('Object.values(spellItem.system.selfEffects ?? {})',self.body(11))
        self.assertIn('spellItem.effects?.filter(effect => effect.system.applySelf)',self.body(11))
        self.assertFalse(self.edges('templates/chat/item/partials/item-description/spell-description.hbs','writes'))
        self.assertIn('{{item.system.effect}}',self.body(502));self.assertNotIn('{{{item.system.effect}}}',self.body(502))
    def test_focus_and_template_fields_have_concrete_next_stage_readers(self):
        for n in range(1,5):
            self.assertIn(f'focus{n}: new fields.SchemaField(focus())',self.body(55))
            for f in ['name','value']:self.assertIn(f'name="system.focus{n}.{f}"',self.body(525))
            self.assertIn(f'if (this.system.focus{n}.value > 0)',self.body(11))
        self.assertIn(self.q['focus().value'],self.targets('actor.castSpellMixin.castSpell','reads'));self.assertNotIn(self.q['focus().value'],self.targets('actor.castSpellMixin.castSpell','writes'))
        for f in ['createTemplate','templateType','templateSize']:self.assertIn(self.q['TemplateProperties.'+f],self.targets('spellRegionMixin.createSpellRegion','reads'))
        self.assertIn(self.q['TemplateProperties.visualEffectDuration'],self.targets('spellRegionMixin.deleteSpellVisualEffect','reads'))
        self.assertIn('spellItem.system.createSpellRegion?.(roll, damage, { stamina: origStaCost })',self.body(11))
    def test_core_issue_evidence_and_partial_limits(self):
        for e in json.loads((BASE/'examples/expansion-031-queries.json').read_text())['core_evidence']:self.assertEqual(hashlib.sha256(Path(e['path']).read_bytes()).hexdigest(),e['sha256'])
        for q,n in [('magic/getUsedSkill-fallback',64),('magic/template-source-migration',128),('RitualData/component-uuid-resolution',130),('RitualSheet/component-identity-and-persistence',132),('SpellConfiguration/inherited-region-guard',74),('magic/text-status-active-effect-separation',133)]:
            e=self.data.entities[self.q[q]];self.assertEqual(e['boundary']['kind'],'dynamic');self.assertIn(f'docs/issues/potential/issue-{n:05}.md',{r['path']for r in e['refs']})
        for s in [115,123,125,170,177,179,187,540,602,609,611,597,502,151,76,135,117,11]:self.assertEqual(self.data.sources[f'src-{s:06}']['coverage']['definitions']['state'],'partial')
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
        self.assertEqual({k:len(v)for k,v in self.new.items()},{'entities':170,'relations':602,'processes':15})

if __name__=='__main__':unittest.main()
