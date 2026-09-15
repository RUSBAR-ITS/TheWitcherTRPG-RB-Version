"""Проверка индекса UI навыков по исходникам; игровой JS/браузер не исполняются."""
import hashlib
import json
import re
from pathlib import Path
import unittest
import tempfile
from test_query import BASE, ROOT, query, run_cli

class SkillUIExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.historical=tempfile.TemporaryDirectory(prefix='witcher-index-009-case-')
        cls.addClassCleanup(cls.historical.cleanup)
        directory=Path(cls.historical.name)
        manifest=json.loads((BASE/'manifest.json').read_text())
        rows={kind:[json.loads(l) for part in manifest['parts'][kind] if not re.search(r'expansion-(\d+)',part) or int(re.search(r'expansion-(\d+)',part).group(1))<=9
                    for l in (BASE/part).read_text().splitlines()] for kind in ('entities','relations','processes')}
        allowed_relations={r['id'] for r in rows['relations']}
        for process in rows['processes']:
            for step in process['steps']:
                step['relations']=[rid for rid in step['relations'] if rid in allowed_relations]
        rows['sources']=[json.loads(l) for l in (BASE/'sources.jsonl').read_text().splitlines()]
        manifest['parts']={kind:[kind+'.jsonl'] for kind in rows}
        manifest.pop('query_examples',None)
        manifest['dataset_id']='task-0006.009-historical-case'
        manifest['next_ids']=dict(source=616,entity=936,relation=2400,process=64)
        excluded={f'src-{n:06}' for n in [2,3,32,46,40,542,543,544,547,453]}
        manifest['scope']['selected_sources']=[s for s in manifest['scope']['selected_sources'] if s not in excluded]
        manifest['scope']['semantic_scope']='Исторические части до .009; используется для SUI-11.'
        for src in rows['sources']:
            for aspect,kind in [('definitions','entities'),('relations','relations'),('processes','processes')]:
                included=[r['id'] for r in rows[kind] if (
                    any(st['location']['source']==src['id'] for st in r['steps']) if kind=='processes' else
                    (r.get('location') or {}).get('source')==src['id'] and (aspect!='definitions' or r['kind']!='boundary'))]
                src['coverage'][aspect]=dict(state='partial' if included else 'not_indexed',included=included,remaining=['Историческая область .009.'])
        for kind,data in rows.items():
            (directory/(kind+'.jsonl')).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in data))
        cls.historical_manifest=directory/'manifest.json'
        cls.historical_manifest.write_text(json.dumps(manifest,ensure_ascii=False))

    def source(self,sid):
        return (ROOT/self.data.sources[sid]['path']).read_text().splitlines()

    def edges(self,eid,kind):
        return [r for r in self.data.relations.values() if r['from']==eid and r['kind']==kind]

    def steps(self,pid):
        return {s['id']:s for s in self.data.processes[pid]['steps']}

    def test_22_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-009-queries.json').read_text())['cases']
        self.assertEqual(len(cases),22)
        for case in cases:
            with self.subTest(case=case['id']):
                prefix=['--dataset',str(self.historical_manifest)] if case['id']=='SUI-11' else []
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



    def test_source_definitions_and_template_locations(self):
        cases=[(882,27,102,'_prepareCustomSkills'),(886,28,77,'_prepareCustomSkills'),
               (889,27,213,'_onRender'),(891,29,110,'activateListeners'),
               (892,29,122,'_prepareContext'),(893,31,111,'_prepareContext'),
               (898,178,25,'_prepareContext'),(904,40,2,'customSkillListener'),
               (921,550,289,'monster-skill-tab.hbs')]
        for n,sid,line,literal in cases:
            sid=f'src-{sid:06}';entity=self.data.entities[f'ent-{n:06}']
            self.assertEqual((entity['location']['source'],entity['location']['line_start']),(sid,line))
            self.assertIn(literal,self.source(sid)[line-1])
        entities=[json.loads(l) for l in (BASE/'data/entities/expansion-009.jsonl').read_text().splitlines()]
        self.assertEqual(len(entities),56)
        for e in entities:
            if e['location']:
                self.assertLessEqual(e['location']['line_end'],len(self.source(e['location']['source'])))
            if e['kind']=='boundary':continue
            definitions=[r for r in self.data.relations.values() if r['kind']=='defines' and r['to']==e['id']]
            self.assertEqual(len(definitions),1)
            self.assertEqual(definitions[0]['location']['line_start'],e['location']['line_start'])

    def test_registered_classes_shared_parts_and_unselected_legacy_resource(self):
        reg=self.source('src-000215');char=self.source('src-000029');mon=self.source('src-000031')
        for n,literal in [(105,'WitcherCharacterSheet'),(109,'WitcherMonsterSheet'),(131,'WitcherSkillItemSheet')]:
            self.assertIn(literal,reg[n-1])
        self.assertIn('character/tab-skills.hbs',char[43]);self.assertIn('character/tab-skills.hbs',mon[36])
        for eid,line,sid in [('ent-000496',44,'src-000029'),('ent-000498',37,'src-000031')]:
            links=[r for r in self.edges(eid,'refers') if r['to']=='src-000527']
            self.assertEqual([(r['location']['source'],r['location']['line_start']) for r in links],[(sid,line)])
            self.assertFalse(any(r['to']=='src-000527' for r in self.edges(eid,'renders')))
        v1='\n'.join(self.source('src-000028'))
        self.assertNotIn('static PARTS',v1);self.assertNotIn('get template',v1)
        self.assertNotIn('WitcherActorSheetV1','\n'.join(reg))
        imported=[p for p in (ROOT/'module').rglob('*.js') if 'import' in p.read_text() and
                  re.search(r'import[^\n]*WitcherActorSheetV1',p.read_text())]
        self.assertEqual(imported,[])
        pre=(ROOT/'module/setup/handlebars.js').read_text().splitlines()
        self.assertIn('monster-sheet.hbs',pre[2]);self.assertIn('monster-skill-tab.hbs',pre[30])
        self.assertEqual([r['to'] for r in self.edges('ent-000921','renders')],['src-000538'])
        self.assertFalse(any(r['to']=='ent-000921' for r in self.edges('ent-000390','refers')))

    def test_grouping_nine_names_and_seven_visible_groups(self):
        a=self.source('src-000027');v=self.source('src-000028');item=self.source('src-000178')
        for line,literal in [(70,'context.actor.system'),(72,'!i.system.isStored'),
            (79,'await this._prepareCustomSkills'),(103,"this.actor.items.filter(item => item.type === 'skill')"),
            (106,"origin === 'stats'"),(107,'statMap[index].name'),(114,'skill.system.attribute === stat')]:
            self.assertIn(literal,a[line-1])
        self.assertNotIn('context.items','\n'.join(a[101:116]))
        self.assertIn('this.actor.toObject(false)',v[34]);self.assertIn('this._prepareCustomSkills(context)',v[43])
        self.assertIn("origin === 'stats'",item[31]);self.assertIn('r[index] = CONFIG.WITCHER.statMap[index]',item[32])
        cfg=(ROOT/'module/setup/config.js').read_text().splitlines()
        names=re.findall(r"^    (\w+): \{\n        origin: 'stats',\n        name: '(\w+)'",'\n'.join(cfg[16:132]),re.M)
        self.assertEqual(names,[(s,s) for s in ['int','ref','dex','body','spd','emp','cra','will','luck']])
        groups=re.findall(r'^        (\w+): new fields.EmbeddedDataField','\n'.join(self.source('src-000087')),re.M)
        self.assertEqual(groups,['int','ref','dex','body','emp','cra','will'])
        hbs=self.source('src-000527')
        self.assertEqual([n+1 for n,l in enumerate(hbs) if '{{#each system.skills as' in l],[10,33])
        self.assertEqual([n+1 for n,l in enumerate(hbs) if 'lookup ../customSkills skillKey' in l],[24,48])

    def test_partial_hash_dataset_and_model_fields_do_not_merge(self):
        tab=self.source('src-000527');builtin=self.source('src-000522');custom=self.source('src-000521')
        for n in [21,45]:self.assertIn('skill=skill name=name stat=skillKey',tab[n-1])
        for n in [25,49]:
            self.assertIn('custom-skill-display.hbs',tab[n-1]);self.assertNotIn('skill=',tab[n-1])
        self.assertIn('data-skill="{{name}}"',builtin[1]);self.assertIn('data-stat={{stat}}',builtin[1])
        self.assertIn('skill.modifiedValue',builtin[4]);self.assertNotIn('isVisible','\n'.join(builtin))
        self.assertIn('data-action="rollSkill"',custom[0]);self.assertIn('skill.value',custom[3])
        for token in ['data-item-id','#custom-rollable','system.value','skill.modifiedValue','<input']:
            self.assertNotIn(token,'\n'.join(custom))
        for token in ['<input','readonly','disabled']:self.assertNotIn(token,'\n'.join(builtin))
        self.assertEqual(self.data.entities['ent-000928']['kind'],'boundary')
        self.assertEqual([r['to'] for r in self.edges('ent-000916','reads')],['ent-000912','ent-000928','ent-003310'])
        self.assertEqual({r['to'] for r in self.edges('ent-000915','reads')},
                         {'ent-000010','ent-000013','ent-000014','ent-000015','ent-000016','ent-000922','ent-003309'})

    def test_render_listener_dispatch_and_old_dom_contract(self):
        a=self.source('src-000027');c=self.source('src-000029');v=self.source('src-000028')
        self.assertIn('await super._onRender',a[213]);self.assertIn('this.activateListeners(this.element)',a[215])
        self.assertIn('super.activateListeners(html)',c[110])
        self.assertIn('this.skillListener(html)',a[233]);self.assertIn('this.customSkillListener(html)',a[234])
        self.assertIn('this.skillListener(html[0])',v[211]);self.assertIn('this.customSkillListener(html[0])',v[212])
        sm=self.source('src-000045');cm=self.source('src-000040')
        self.assertIn('jQuery = $(html)',sm[26]);self.assertIn('html = $(html)',cm[2])
        self.assertIn('thisActor.rollSkillCheck(skillMap[skill.dataset.skill])',sm[34])
        self.assertNotIn('dataset.stat',sm[34]);self.assertNotIn('await',sm[34])
        self.assertIn("html.find('#custom-rollable').on('click', thisActor.rollCustomSkillCheck.bind(thisActor))",cm[5])
        old=self.source('src-000534');self.assertIn('class="skill item" data-item-id="{{id}}"',old[0])
        self.assertEqual([n+1 for n,l in enumerate(old) if 'id="custom-rollable"' in l],[4,8,12])
        self.assertIn('system.activeEffectModifiers',old[36]);self.assertIn('disabled',old[37])
        self.assertEqual([n['flow'] for n in self.steps('proc-000053')['super']['next']],['await','await'])
        self.assertEqual([r['to'] for r in self.edges('ent-000889','calls')],['ent-000907'])

    def test_item_form_field_names_and_core_boundary(self):
        hbs='\n'.join(self.source('src-000610'));s=self.source('src-000178')
        self.assertEqual(re.findall(r'name="([^"]+)"',hbs),['name','system.attribute'])
        self.assertIn('submitOnChange: true',s[12]);self.assertIn('closeOnSubmit: false',s[13])
        self.assertNotIn('document.update','\n'.join(s));self.assertNotIn('handler:','\n'.join(s))
        model=self.source('src-000124')
        fields=re.findall(r'^            (\w+): new fields.(\w+)','\n'.join(model),re.M)
        self.assertEqual(fields,[('attribute','StringField'),('value','NumberField'),('label','StringField'),
            ('isOpened','BooleanField'),('activeEffectModifiers','NumberField'),
            ('isProfession','BooleanField'),('isPickup','BooleanField'),('isLearned','BooleanField')])
        for token in ['min:','max:','integer:','choices:','modifiers:','modifiedValue','isVisible']:
            self.assertNotIn(token,'\n'.join(model))
        self.assertEqual([r['to'] for r in self.edges('ent-000931','refers')],['ent-000912','ent-000910'])
        self.assertEqual([r['to'] for r in self.edges('ent-000932','refers')],['ent-000184','ent-000910'])
        self.assertEqual([r['to'] for r in self.edges('ent-000918','calls')],['ent-000714'])

    def test_roll_processes_are_reused_and_name_is_not_item_id(self):
        actor=self.source('src-000022')
        for line,literal in [(47,'skillMapEntry.attribute'),(53,'this.system.skills[attribute.name][skillName].value'),
             (135,"event.currentTarget.closest('.item').dataset.itemId"),(137,'customSkill.system.attribute'),
             (141,'customSkill.name'),(142,'customSkill.system.value'),(157,'this.addActiveEffects(customSkill.name)')]:
            self.assertIn(literal,actor[line-1])
        self.assertNotIn('activeEffectModifiers','\n'.join(actor[133:173]))
        added=[json.loads(l) for l in (BASE/'data/processes/expansion-009.jsonl').read_text().splitlines()]
        self.assertTrue(all(p['entry']['entity'] not in ['ent-000382','ent-000302','ent-000304'] for p in added))
        self.assertEqual(self.data.processes['proc-000009']['entry']['entity'],'ent-000382')
        self.assertEqual(self.data.processes['proc-000011']['entry']['entity'],'ent-000302')
        self.assertEqual(self.data.processes['proc-000013']['entry']['entity'],'ent-000304')
        self.assertTrue(any(r['path'].endswith('issue-00187.md') for r in self.data.entities['ent-000382']['refs']))

    def test_process_reachability_local_evidence_and_current_counts(self):
        procs=[json.loads(l) for l in (BASE/'data/processes/expansion-009.jsonl').read_text().splitlines()]
        self.assertEqual(len(procs),14);self.assertEqual(sum(len(p['steps']) for p in procs),46)
        for p in procs:
            steps={s['id']:s for s in p['steps']};pending=[p['steps'][0]['id']];seen=set();exits=set()
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
                   *[f'data/{kind}/expansion-{n:03}.jsonl' for n in [6,7,8,9]]]
            historical[kind]=[json.loads(l) for p in parts for l in (BASE/p).read_text().splitlines()]
        self.assertEqual([len(historical[k]) for k in ['entities','relations','processes']],[935,2399,63])
        for kind,rows in historical.items():
            self.assertTrue({r['id'] for r in rows}<=set(getattr(self.data,kind)))

    def test_external_contract_versions_and_submission_order(self):
        text=(BASE/'coverage-009.md').read_text()
        rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',text,re.M)
        self.assertEqual(len(rows),6)
        for path,digest in rows:self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)
        core=Path('/opt/foundryvtt')
        doc=(core/'client/applications/api/document-sheet.mjs').read_text().splitlines()
        for line,literal in [(466,'if ( !this.isEditable ) return'),(468,'this._prepareSubmitData'),
            (469,'await this._processSubmitData'),(492,'this.document.validate'),
            (508,'expandObject(formData.object)'),(528,'await document.update')]:
            self.assertIn(literal,doc[line-1])
        app=(core/'client/applications/api/application.mjs').read_text().splitlines()
        self.assertIn('await handler.call',app[2140]);self.assertIn('open && formConfig.submitOnChange',app[2160])
        helper=(core/'client/applications/handlebars.mjs').read_text().splitlines()
        self.assertIn('valueAttr ? v[valueAttr] : k',helper[480])

if __name__=='__main__':
    unittest.main()
