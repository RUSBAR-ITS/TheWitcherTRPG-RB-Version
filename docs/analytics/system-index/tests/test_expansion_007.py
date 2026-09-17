"""Ориентиры .007 по прочитанным исходникам; JavaScript/Foundry не исполняются."""
import hashlib
import re
from pathlib import Path
import json
import unittest
from test_query import BASE, ROOT, query, run_cli


class EffectEditorExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = query.Dataset()

    def source(self, sid):
        return (ROOT / self.data.sources[sid]['path']).read_text().splitlines()

    def edges(self, source, kind=None):
        return [r for r in self.data.relations.values()
                if r['from']==source and (kind is None or r['kind']==kind)]

    def steps(self, pid):
        return {s['id']:s for s in self.data.processes[pid]['steps']}

    def test_20_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-007-queries.json').read_text())['cases']
        self.assertEqual(len(cases),20)
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

    def test_class_actions_providers_and_call_sites(self):
        source=self.source('src-000005')
        for line,literal in [(6,'class WitcherActiveEffectConfig'),(9,'wizard: WitcherActiveEffectConfig.wizardAction'),
                             (40,'await super._prepareContext(options)'),(48,'this.autocomplete();'),
                             (52,"wizard.setAttribute('data-action', 'wizard')"),(140,'prototype, baseMixin'),
                             (141,'prototype, temporaryItemImprovementMixin')]:
            self.assertIn(literal,source[line-1])
        self.assertEqual(self.data.entities['ent-000446']['location']['line_start'],6)
        self.assertEqual(self.data.entities['ent-000510']['location']['line_start'],14)
        providers=[(639,'getActiveEffectsBasePaths',2),(640,'getStatSuggestions',14),
                   (641,'getToxSuggestions',32),(642,'getSkillGroupSuggestions',42),
                   (643,'getSkillSuggestions',71),(644,'getLifepathSuggestions',87),
                   (645,'getOtherSuggestions',125),(646,'getDamageModifcators',145),
                   (647,'getActiveEffectsItemImprovementPaths',2),(648,'getItemDamageSuggestions',8)]
        for n,name,line in providers:
            e=self.data.entities[f'ent-{n:06}'];sid='src-000006' if n<647 else 'src-000007'
            self.assertEqual(e['location']['source'],sid)
            self.assertEqual(e['location']['line_start'],line)
            self.assertIn(name+'()',self.source(sid)[line-1])
        self.assertEqual([(r['to'],r['location']['line_start']) for r in self.edges('ent-000639','calls')],
                         [(f'ent-{n:06}',line) for n,line in [(640,4),(641,5),(642,6),(643,7),(644,8),(645,9),(646,10)]])
        self.assertEqual([(r['to'],r['location']['line_start']) for r in self.edges('ent-000647','calls')],
                         [('ent-000648',4)])

    def test_suggestions_resolve_to_real_types_or_explicit_boundaries(self):
        fields={655:(5,'NumberField'),656:(6,'NumberField'),657:(7,'NumberField'),658:(8,'NumberField'),
                659:(9,'TypedObjectField'),660:(7,'NumberField'),661:(10,'NumberField'),662:(11,'NumberField'),
                663:(5,'NumberField'),664:(6,'NumberField'),665:(7,'BooleanField'),666:(29,'StringField'),
                667:(40,'EmbeddedDataField'),668:(51,'StringField'),669:(56,'StringField')}
        for n,(line,typ) in fields.items():
            e=self.data.entities[f'ent-{n:06}'];self.assertEqual(e['location']['line_start'],line)
            self.assertIn(typ,self.source(e['location']['source'])[line-1])
        temporary=self.source('src-000007')
        for n,line,target,path in [(686,12,666,'system.damage'),(687,17,668,'system.damageProperties.oilEffect'),
                                   (688,22,669,'system.damageProperties.silverDamage')]:
            self.assertIn(path,temporary[line-1])
            self.assertEqual([r['to'] for r in self.edges(f'ent-{n:06}','refers')],[f'ent-{target:06}'])
        base=self.source('src-000006')
        self.assertIn('activeEffectModifiers',base[76]);self.assertIn("+ key +",base[76])
        self.assertNotIn('skill.name',base[76])
        for n in [670,671,672,673,676,678,689,690,691,692]:
            self.assertEqual(self.data.entities[f'ent-{n:06}']['boundary']['kind'],'dynamic')
        self.assertIn('commonsp:', '\n'.join(self.source('src-000084')))
        self.assertNotIn('commonspeech:', '\n'.join(self.source('src-000084')))
        self.assertIn('attacks.strong',base[94]);self.assertNotIn('.value',base[94])
        self.assertIn('attacks.joint',base[99]);self.assertNotIn('.value',base[99])
        self.assertIn('new fields.SchemaField',self.source('src-000077')[9])
        self.assertIn('value: new fields.NumberField',self.source('src-000077')[10])
        self.assertIn('parent?.system.damageTypeModification',base[146])
        self.assertIn('parent.parent?.system.damageTypeModification',base[147])
        self.assertEqual([r['to'] for r in self.edges('ent-000692','refers')],['ent-000665'])

    def test_form_prepared_source_and_payload_remain_distinct(self):
        source=self.source('src-000005');callback='\n'.join(source[81:94])
        for line,literal in [(83,"button.form.elements.path.value.split(',')"),
                             (84,'this.document.system.changes'),(86,'newChanges.push({'),
                             (87,'key: path'),(91,'this.document.update({'),(92,'changes: newChanges')]:
            self.assertIn(literal,source[line-1])
        for absent in ['FormData','this.form','await','_source','applyAfterCalculations']:
            self.assertNotIn(absent,callback)
        self.assertEqual([r['to'] for r in self.edges('ent-000699','writes')],['ent-000715','ent-000718'])
        self.assertEqual([r['to'] for r in self.edges('ent-000699','calls')],['ent-000719'])
        continuation=self.edges('ent-000699','refers')
        self.assertEqual([r['to'] for r in continuation],['ent-000319'])
        self.assertIn('не прямой вызов',continuation[0]['context'])
        ae=self.source('src-000008')
        self.assertIn('this._source.system.changes',ae[65]);self.assertIn('change.key = skill',ae[105])
        self.assertIn('data.system?.applyAfterCalculations',ae[113])
        self.assertIn('data.system?.changes.forEach',ae[115])
        self.assertTrue(any(r.get('anchor')=='уточнение-task-0003010'
                            for r in self.data.entities['ent-000319']['refs']))
        self.assertEqual(self.data.processes['proc-000007']['entry']['entity'],'ent-000319')

    def test_promises_cancel_and_nested_callbacks(self):
        source=self.source('src-000005')
        self.assertIn('await foundry.applications.handlebars.renderTemplate',source[70])
        self.assertIn('DialogV2.prompt({',source[77]);self.assertNotIn('await',source[77])
        self.assertNotIn('rejectClose','\n'.join(source[58:97]))
        self.assertNotIn('await','\n'.join(source[98:137]))
        ae=self.source('src-000008')
        for n,literal in [(68,'await this.chooseSkill(change)'),(88,'await foundry.applications.handlebars.renderTemplate'),
                          (95,'await DialogV2.prompt'),(103,'rejectClose: true')]:self.assertIn(literal,ae[n-1])
        self.assertEqual([x.get('step') for x in self.steps('proc-000026')['type']['next']],['base','temporary','render'])
        for pid,owner in [('proc-000026','ent-000697'),('proc-000029','ent-000318')]:
            for rid in self.steps(pid)['prompt']['relations']:
                self.assertEqual(self.data.relations[rid]['from'],owner)
        self.assertTrue(all(x['flow']=='sync' for x in self.steps('proc-000027')['update']['next']))
        self.assertEqual([(x.get('step'),x.get('exit'),x['flow']) for x in self.steps('proc-000029')['prompt']['next']],
                         [('ok',None,'scheduled'),(None,'cancelled','await')])

    def test_autocomplete_and_system_tab_conditions(self):
        loc=self.data.entities['ent-000698']['location']
        source='\n'.join(self.source('src-000005')[loc['line_start']-1:loc['line_end']])
        for literal in ["parent.documentName === 'Actor'","parent.documentName === 'Item'",
                        'for (const datamodel in config.dataModels)','schema.apply(function ()',
                        '!(this instanceof foundry.data.fields.SchemaField)',
                        'attributeKeyOptions[this.fieldPath]',"datalist.id = this.#attributeKeyListId"]:
            self.assertIn(literal,source)
        for absent in ['.transfer','parent.type','document.update','await']:self.assertNotIn(absent,source)
        self.assertEqual([r['to'] for r in self.edges('ent-000720','refers')],[f'ent-{n:06}' for n in range(459,485)])
        wizard='\n'.join(self.source('src-000506'))
        self.assertIn('<select id="path">',wizard);self.assertNotIn('name=',wizard)
        hbs=self.source('src-000541')
        self.assertEqual([i+1 for i,l in enumerate(hbs) if '{{formGroup' in l],[3,6,7,9,10])
        self.assertIn('{{#if systemFields.applyAfterCalculations}}',hbs[1])
        self.assertIn('{{#if isItemEffect}}',hbs[4])
        self.assertIn('{{#unless document.isTemporaryItemImprovement}}',hbs[7])
        # .011 adds the concrete English label; the Temporary missing-field stays distinct.
        self.assertEqual([r['to'] for r in self.edges('ent-000729','reads')],['ent-000176','ent-000731','ent-002011','ent-005361'])
        temporary=(ROOT/'module/data/activeEffects/witcherTemporaryItemImprovementData.js').read_text()
        self.assertNotIn('applyAfterCalculations',temporary)
        self.assertIn('applySelf',temporary);self.assertIn('applyOnTarget',temporary)

    def test_css_uses_actual_common_list_markup(self):
        css=self.source('src-000445');markup='\n'.join(self.source('src-000531'))
        specs=[(751,1,'.effects-list'),(752,7,'.effects-header'),(753,12,'.effects-header'),
               (754,18,'h3'),(755,24,'.effects-header:nth-child(n + 2)'),(756,30,'.effect-first-row'),
               (757,36,'.effect-display'),(758,42,'.effect-list'),(759,47,'.effect-row'),
               (760,54,'.effect-row:hover'),(761,59,'.effect-row:last-child'),(762,63,'.effect-name'),
               (763,69,'.effect-name > img'),(764,74,'.effect-name > h4'),(765,78,'.effect-name'),
               (766,85,'.effect-source'),(767,92,'.effect-description')]
        for n,line,selector in specs:
            self.assertIn(selector,css[line-1])
            e=self.data.entities[f'ent-{n:06}'];self.assertEqual(e['location']['line_start'],line)
            targets=[self.data.entities[r['to']]['location']['source'] for r in self.edges(e['id'],'refers')]
            self.assertEqual(set(targets),set() if n==764 else {'src-000531'})
        self.assertIn('<p>{{effect.name}}</p>',markup);self.assertNotIn('<h4',markup)
        self.assertIn('effect-description invisible',markup)
        self.assertIn('display: none',self.source('src-000474')[206])
        self.assertTrue(any(r['kind']=='imports' and r['to']=='src-000445'
                            and r['location']['line_start']==21 for r in self.data.relations.values()))

    def test_processes_have_local_reachable_steps_and_participation(self):
        procs=[json.loads(l) for l in (BASE/'data/processes/expansion-007.jsonl').read_text().splitlines()]
        self.assertEqual(len(procs),9);self.assertEqual(sum(len(p['steps']) for p in procs),41)
        for p in procs:
            steps={s['id']:s for s in p['steps']};pending=[p['steps'][0]['id']];seen=set();exits=set()
            while pending:
                key=pending.pop()
                if key in seen:continue
                seen.add(key)
                for nxt in steps[key]['next']:
                    if 'step' in nxt:pending.append(nxt['step'])
                    else:exits.add(nxt['exit'])
            self.assertEqual(seen,set(steps));self.assertEqual(exits,{e['id'] for e in p['exits']})
            for s in steps.values():
                for rid in s['relations']:
                    loc=self.data.relations[rid]['location']
                    self.assertEqual(loc['source'],s['location']['source'])
                    self.assertTrue(s['location']['line_start']<=loc['line_start']<=s['location']['line_end'])
            result=self.data.query(query.parser().parse_args(['processes',p['entry']['entity'],'--limit','50','--no-verify']))
            self.assertIn(p['id'],[x['id'] for x in result['items']])

    def test_historical_counts_and_ids(self):
        historical={}
        for kind in ['entities','relations','processes']:
            names=[f'examples/{kind}.jsonl',f'data/{kind}/pilot.jsonl',
                   f'data/{kind}/expansion-006.jsonl',f'data/{kind}/expansion-007.jsonl']
            historical[kind]=[json.loads(l) for name in names for l in (BASE/name).read_text().splitlines()]
        self.assertEqual([len(historical[k]) for k in ['entities','relations','processes']],[768,1905,32])
        for kind,records in historical.items():
            self.assertTrue({r['id'] for r in records}<=set(getattr(self.data,kind)))
        represented={e['location']['source'] for e in historical['entities'] if e['location'] and e['kind']!='boundary'}
        self.assertEqual(len(represented),120)
        self.assertEqual(sum(e['kind']=='boundary' for e in historical['entities']),129)
        self.assertTrue(all(self.data.sources[s]['coverage']['definitions']['state']=='partial' for s in represented))

    def test_external_core_contract_hashes_and_critical_order(self):
        # External implementation remains outside the 615-source catalogue.
        text=(BASE/'coverage-007.md').read_text()
        rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',text,re.M)
        self.assertEqual(len(rows),11)
        for path,digest in rows:
            with self.subTest(path=path):
                self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)
        core=Path('/opt/foundryvtt')
        sheet=(core/'client/applications/sheets/active-effect-config.mjs').read_text().splitlines()
        for line,literal in [(247,'new FormDataExtended(this.form)'),(248,'submitData.system?.changes'),
                             (249,'changes.element.getInitialValue()'),(250,'return this.submit')]:
            self.assertIn(literal,sheet[line-1])
        backend=(core/'client/data/client-backend.mjs').read_text().splitlines()
        self.assertIn('documentClass.cleanData(update',backend[230])
        self.assertIn('await doc._preUpdate(changes',backend[237])
        self.assertIn('"changes", "system.changes"',(core/'common/documents/active-effect.mjs').read_text())
        helper=(core/'client/applications/handlebars.mjs').read_text().splitlines()
        self.assertIn('if ( !field )',helper[534]);self.assertIn('SafeString("")',helper[536])
        dialog=(core/'client/applications/api/dialog.mjs').read_text()
        self.assertIn('rejectClose=false',dialog);self.assertIn('else resolve(result ?? null)',dialog)

if __name__=='__main__':
    unittest.main()
