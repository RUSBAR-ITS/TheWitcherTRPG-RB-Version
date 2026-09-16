"""Проверка индекса UI навыков по исходникам; игровой JS/браузер не исполняются."""
import hashlib
import json
import re
from pathlib import Path
import unittest
import tempfile
from test_query import BASE, ROOT, query, run_cli, save_pre_resource_forms_view

class EditingExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.history_dir=tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.history_dir.cleanup)
        cls.history_manifest=save_pre_resource_forms_view(Path(cls.history_dir.name))
        cls.historical=query.Dataset(cls.history_manifest)

    def source(self,sid):
        return (ROOT/self.data.sources[sid]['path']).read_text().splitlines()

    def edges(self,eid,kind):
        return [r for r in self.data.relations.values() if r['from']==eid and r['kind']==kind]

    def steps(self,pid):
        return {s['id']:s for s in self.data.processes[pid]['steps']}

    def test_24_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-010-queries.json').read_text())['cases']
        self.assertEqual(len(cases),24)
        for case in cases:
            with self.subTest(case=case['id']):
                prefix=['--dataset',str(self.history_manifest)] if case['id']=='ED-10' else []
                run=run_cli([*prefix,*case['command'],'--format','json'],cwd='/tmp')
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



    def test_definitions_and_local_source_addresses(self):
        for n,sid,line,literal in [(936,32,10,'constructor'),(943,32,42,'_onRender'),(944,32,54,'_prepareContext'),
            (950,29,468,'#openModifiers'),(951,31,213,'#openModifiers'),(953,46,8,'_onStatSaveRoll'),
            (955,46,88,'calc_total_stats'),(956,46,98,'_onLuckMinus'),(957,46,105,'_onLuckReset'),
            (958,46,110,'_onAdrenalineMinus'),(959,46,117,'_onAdrenalinePlus'),(960,46,122,'statListener'),
            (964,9,2,'addAdrenaline'),(967,40,15,'removeCustomSkill'),(968,40,19,'customSkillModifierDisplay'),
            (969,40,27,'_onAddCustomSkillModifier'),(970,40,36,'_onRemoveCustomSkillModifier'),
            (971,40,47,'_onEditCustomSkillModifier'),(993,33,65,'_getSkills'),
            (998,27,98,'_renderConfigureDialog'),(1008,29,151,'_prepareCharacterData')]:
            e=self.data.entities[f'ent-{n:06}'];sid=f'src-{sid:06}'
            self.assertEqual((e['location']['source'],e['location']['line_start']),(sid,line))
            self.assertIn(literal,self.source(sid)[line-1])
        for e in map(json.loads,(BASE/'data/entities/expansion-010.jsonl').read_text().splitlines()):
            if e['location']:self.assertLessEqual(e['location']['line_end'],len(self.source(e['location']['source'])))
            if e['kind']=='boundary':continue
            defs=[r for r in self.data.relations.values() if r['kind']=='defines' and r['to']==e['id']]
            self.assertEqual(len(defs),1);self.assertEqual(defs[0]['from'],e['owner'])

    def test_two_parts_constructor_and_shared_config(self):
        c=self.source('src-000032')
        for n,literal in [(11,'super(options)'),(13,'this.type = options.type'),(14,'this.skillKey = options.skillKey'),
                          (27,'submitOnChange: true'),(28,'closeOnSubmit: false'),(56,'context.config = CONFIG.WITCHER'),
                          (57,'context.config.statLabels ='),(58,'.label ??'),(62,'this.document.system')]:
            self.assertIn(literal,c[n-1])
        self.assertEqual([r['to'] for r in self.edges('ent-000942','refers')],['src-000543','src-000542'])
        self.assertNotIn('_configureRenderParts','\n'.join(c));self.assertNotIn('handler:','\n'.join(c))
        for sid,n in [('src-000029',473),('src-000031',218)]:
            lines=self.source(sid);self.assertIn('new WitcherModifiersConfiguration',lines[n-1])
            self.assertIn('document: this.document',lines[n]);self.assertIn('render(true)',lines[n+3])
        self.assertEqual({r['to'] for r in self.edges('ent-000993','reads')},{'ent-000194','ent-000196','ent-000011'})
        self.assertEqual(self.data.entities['ent-000196']['qualified_name'],'WITCHER.skillMap')

    def test_form_names_values_and_disabled_have_no_writer(self):
        hs='\n'.join(self.source('src-000543'));hb='\n'.join(self.source('src-000544'));hk='\n'.join(self.source('src-000542'))
        for literal in ["eq type 'stats'","eq type 'derivedStats'",'reputation=../system.reputation']:self.assertIn(literal,hs)
        for literal in ["name='system.{{@root.type}}.{{stat}}.unmodifiedMax'","value='{{details.max}}'","value='{{reputation.max}}'"]:self.assertIn(literal,hb)
        self.assertNotIn('disabled',hb);self.assertNotIn('readonly',hb)
        self.assertIn("(eq (localize details.label) (localize 'WITCHER.Actor.Stat.Toxicity'))",hb)
        self.assertIn('lookup system.skills skillKey',hk);self.assertEqual(hk.count('type="checkbox"'),3)
        disabled=[s for s in re.findall(r'<input\b[^>]*>',hk,re.S) if 'disabled' in s]
        self.assertEqual(len(disabled),2);self.assertTrue(all('name=' not in x for x in disabled))
        self.assertEqual(self.edges('ent-000987','writes'),[])
        self.assertEqual([r['to'] for r in self.edges('ent-000981','refers')],['ent-000003','ent-000910'])
        newreads=[r for r in self.data.relations.values() if r['to']=='ent-000012' and r['kind']=='reads']
        self.assertEqual({r['from'] for r in newreads},{'ent-000016','ent-000296','ent-000978','ent-000987'})
        out=self.data.query(query.parser().parse_args(['processes','ent-000012','--scope','src-000542','--no-verify']))
        self.assertEqual(out['items'][0]['step_ids'],['proc-000072/ae','proc-000072/disabled'])

    def test_manual_resource_payload_and_await_distinctions(self):
        s=self.source('src-000046');adr=self.source('src-000009')
        for n,literal in [(100,'luck.value > 0'),(101,'await this.actor.update'),(107,'luck.max'),
                          (112,'adrenaline.value > 0'),(113,'await this.actor.update'),(119,'this.actor.addAdrenaline()')]:self.assertIn(literal,s[n-1])
        self.assertNotIn('await',s[118]);self.assertNotIn('return',s[118])
        self.assertIn("useOptionalAdrenaline",adr[2]);self.assertIn('this.update',adr[3]);self.assertNotIn('await',adr[3])
        for line in ['min:', 'max:']:self.assertNotIn(line,'\n'.join(self.source('src-000073')))
        p=self.steps('proc-000073')
        self.assertEqual([x.get('step') or x.get('exit') for x in p['guard']['next']],['write','returned'])
        self.assertTrue(all(x['flow']=='await' for x in p['write']['next']))
        self.assertEqual(self.steps('proc-000076')['call']['next'][0]['exit'],'outside')
        self.assertTrue(any(r['kind']=='mixes' and r['from']=='ent-000277' and r['to']=='ent-000963' and r['location']['line_start']==453 for r in self.data.relations.values()))

    def test_old_modifiers_schema_id_value_and_unawaited_requests(self):
        c=self.source('src-000040');self.assertNotIn('modifiers:','\n'.join(self.source('src-000124')))
        for n,literal in [(16,'.delete()'),(23,"'system.isOpened': !customSkill.system.isOpened"),
            (29,'customSkill.system.modifiers ?? []'),(30,"{ name: 'Modifier', value: 0 }"),
            (40,'Object.values(prevModList)'),(41,'v.id === event.target.dataset.id'),(42,'splice(idxToRm, 1)'),
            (51,"closest('.list-modifiers').dataset.id"),(54,'element.value'),(57,'obj.id == itemId'),(58,'[field] = value')]:self.assertIn(literal,c[n-1])
        for n in [16,22,31,44,60]:
            self.assertNotIn('await',c[n-1]);self.assertNotIn('return',c[n-1])
        self.assertNotIn('Number(','\n'.join(c));self.assertNotIn('parseInt(','\n'.join(c))
        templates=[p.read_text() for p in (ROOT/'templates').rglob('*.hbs')]
        for token in ['add-custom-skill-modifier','edit-custom-skill-modifier','delete-custom-skill-modifier']:self.assertFalse(any(token in text for text in templates))
        old_id_readers=[r for r in self.data.relations.values() if r['kind']=='reads' and r['to']=='ent-000929']
        self.assertEqual({r['from'] for r in old_id_readers},
                         {'ent-000304','ent-000967','ent-000968','ent-000969','ent-000970','ent-000971'})
        self.assertEqual(self.data.entities['ent-000972']['kind'],'boundary')
        self.assertEqual([r['to'] for r in self.edges('ent-000970','calls')],['ent-001003'])

    def test_visibility_has_real_caller_and_schema_path_boundary(self):
        m=self.source('src-000033');h=self.source('src-000547')
        self.assertIn('skillConfiguration.hbs',m[30]);self.assertIn('context.skillConfig = this._getSkills()',m[55])
        self.assertIn("schema.getField(['skills', attribute, skill, 'isVisible'])",m[75])
        self.assertIn('system.skills.'+chr(36)+'{attribute}.'+chr(36)+'{skill}.isVisible',m[78])
        self.assertIn('length === 0 && delete skills[skill]',m[86])
        self.assertIn('formGroup skillProperties.isVisible value=skillProperties.isVisibleValue',h[8]);self.assertNotIn('name=','\n'.join(h))
        self.assertIn('new WitcherMonsterConfigurationSheet',self.source('src-000031')[108])
        self.assertIn('this.configuration?.render(true)',self.source('src-000027')[98])
        self.assertTrue(any(r['path'].endswith('issue-00004.md') for r in self.data.entities['ent-000993']['refs']))

    def test_stat_rolls_and_total_use_existing_targets(self):
        s=self.source('src-000046')
        self.assertIn("stat != 'luck'",s[9]);self.assertIn('threshold = statValue',s[32])
        self.assertIn('await getCustomModifier',s[23]);self.assertIn('await extendedRoll',s[34])
        self.assertIn('reputation.value',s[48]);self.assertIn('Number(repValue)',s[72]);self.assertIn('stats.will.value',s[72])
        self.assertIn("element !== 'toxicity'",s[90]);self.assertIn('context.system.stats[element].max',s[91])
        self.assertNotIn('Number(','\n'.join(s[87:96]))
        callers=[r for r in self.data.relations.values() if r['kind']=='calls' and r['to']=='ent-000955']
        self.assertEqual([(r['from'],r['location']['line_start']) for r in callers],[('ent-001008',168)])
        processes=[json.loads(l) for l in (BASE/'data/processes/expansion-010.jsonl').read_text().splitlines()]
        self.assertTrue(all(p['entry']['entity'] not in ['ent-000369','ent-000300','ent-000280'] for p in processes))
        self.assertEqual([r['to'] for r in self.edges('ent-000383','calls')],['ent-000300'])

    def test_css_declaration_and_class_sources(self):
        css=self.source('src-000453')
        self.assertIn('.application.sheet.witcher.actor.modifier-configuration:not(.extended-sheet)',css[0])
        self.assertIn('.window-content',css[1]);self.assertEqual(css[2].strip(),'display: inherit;')
        self.assertIn("'modifier-configuration'",self.source('src-000032')[24])
        imports=(ROOT/'styles/witcher-styles.css').read_text().splitlines();self.assertIn('modifier-configuration.css',imports[37])
        self.assertLess(next(i for i,l in enumerate(imports) if "'./character/sheet.css'" in l),37)
        self.assertEqual([r['to'] for r in self.edges('ent-001000','writes')],['ent-001001'])

    def test_processes_current_counts_reachability_and_local_evidence(self):
        ps=[json.loads(l) for l in (BASE/'data/processes/expansion-010.jsonl').read_text().splitlines()]
        self.assertEqual(len(ps),28);self.assertEqual(sum(len(p['steps']) for p in ps),74)
        for p in ps:
            ss={s['id']:s for s in p['steps']};todo=[p['steps'][0]['id']];seen=set();exits=set()
            while todo:
                sid=todo.pop()
                if sid in seen:continue
                seen.add(sid)
                for n in ss[sid]['next']:
                    if 'step' in n:todo.append(n['step'])
                    else:exits.add(n['exit'])
            self.assertEqual(seen,set(ss));self.assertEqual(exits,{e['id'] for e in p['exits']})
            for s in ss.values():
                for rid in s['relations']:
                    r=self.data.relations[rid];self.assertEqual(r['from'],s['entity'])
                    self.assertEqual(r['location']['source'],s['location']['source'])
                    self.assertTrue(s['location']['line_start']<=r['location']['line_start']<=s['location']['line_end'])
            out=self.data.query(query.parser().parse_args(['processes',p['entry']['entity'],'--limit','100','--no-verify']))
            self.assertIn(p['id'],[x['id'] for x in out['items']])
        historical={kind:[json.loads(l) for part in self.data.manifest['parts'][kind] if not re.search(r'expansion-(\d+)',part) or int(re.search(r'expansion-(\d+)',part).group(1))<=10
                          for l in (BASE/part).read_text().splitlines()] for kind in ['entities','relations','processes']}
        self.assertEqual([len(self.data.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,1008,2671,91])
        represented={e['location']['source'] for e in historical['entities'] if e['location'] and e['kind']!='boundary'}
        self.assertEqual(len(represented),151)

    def test_external_contract_hashes_and_submission_fields(self):
        text=(BASE/'coverage-010.md').read_text();rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',text,re.M)
        self.assertEqual(len(rows),6)
        for path,digest in rows:self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)
        core=Path('/opt/foundryvtt');f=(core/'client/applications/ux/form-data-extended.mjs').read_text().splitlines()
        for n,literal in [(23,'disabled=false, readonly=true'),(108,'form.elements'),(112,'!name'),(118,'!disabled'),(119,'!readonly'),(199,'["number", "range"]'),(201,'dataType || "Number"')]:self.assertIn(literal,f[n-1])
        fields=(core/'common/data/fields.mjs').read_text().splitlines()
        self.assertIn('name: this.fieldPath',fields[632]);self.assertIn('this.toInput(inputConfig)',fields[665])
        doc=(core/'client/applications/api/document-sheet.mjs').read_text().splitlines()
        self.assertIn('this.document.validate',doc[491]);self.assertIn('expandObject(formData.object)',doc[507]);self.assertIn('await document.update',doc[527])
        h=(core/'client/applications/handlebars.mjs').read_text().splitlines()
        self.assertIn('if ( !field )',h[534]);self.assertIn('field.toFormGroup',h[539])

if __name__=='__main__':
    unittest.main()
