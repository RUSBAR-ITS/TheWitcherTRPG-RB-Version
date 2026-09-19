"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class ResourceFormExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-024.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_29_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-024-queries.json').read_text())['cases']
        self.assertEqual(len(cases),29)
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
                    depth_limited=out.get('traversal',{}).get('depth_limited'),resolution=first.get('boundary',{}).get('kind'),refs=[x['path'] for x in rows if 'path' in x])
                for key,value in c['expected'].items():
                    if key.startswith('includes_'):self.assertTrue(set(value)<=set(actual[key[9:]]),(key,actual))
                    elif key.startswith('excludes_'):self.assertFalse(set(value)&set(actual[key[9:]]),(key,actual))
                    else:self.assertEqual(actual[key],value,key)
                self.assertEqual(out['freshness']['state'],'current')
                self.assertEqual(out['coverage']['state'],'partial')



    def test_sidebar_control_contracts_and_reverse_writers(self):
        common={'system.derivedStats.'+s+'.value'for s in ['hp','sta','focus','resolve','shield']}|{'system.stats.toxicity.value','system.healthState.woundThreshold.ignored','system.healthState.deathState.ignored'}
        expected={560:common|{'system.stats.luck.value','system.adrenaline.value'},565:common|{'system.'+s for s in ['armorHead','armorUpper','armorLower','armorTailWing']}}
        writer=self.q['WitcherActorSheet/resource-form-submit']
        for src,paths in expected.items():
            text='\n'.join(self.source(src));typ='character'if src==560 else'monster'
            raw={re.search(r'\bname=[\'\"]([^\'\"]+)',m[0])[1]:m[0]for m in re.finditer(r'<input\b[^>]*>',text,re.S)if re.search(r'\bname=[\'\"]([^\'\"]+)',m[0])}
            self.assertEqual(set(raw),paths)
            for path,control in raw.items():
                with self.subTest(src=src,path=path):
                    e=self.data.entities[self.q[typ+'/sidebar.hbs.input['+path+']']]
                    loc=e['location'];excerpt='\n'.join(self.source(src)[loc['line_start']-1:loc['line_end']])
                    self.assertIn(path,excerpt)
                    self.assertEqual(e['owner'],self.q[typ+'/sidebar.hbs'])
                    passes=[r for r in self.data.outgoing[e['id']]if r['kind']=='passes'and r['to']==writer]
                    self.assertEqual(len(passes),1)
                    writes=[r for r in self.data.outgoing[writer]if r['kind']=='writes'and r['payload']==path and r['location']['source']==f'src-{src:06}']
                    self.assertTrue(writes)
                    for r in writes:self.assertIn(r,self.data.incoming[r['to']]);self.assertIn('validation',r['condition'])
                    self.assertFalse([r for r in self.data.outgoing[e['id']]if r['kind']=='writes'])
                    self.assertNotIn('unmodifiedMax',path)
            self.assertNotIn('system.derivedStats.vigor.value',raw)
            self.assertFalse([r for r in self.data.incoming[self.q['DerivedStats.vigor']]if r['kind']=='writes'and r['location']['source']==f'src-{src:06}'])

    def test_source_prepared_maximum_and_display_remain_distinct(self):
        stat='\n'.join(self.source(90));self.assertIn('value: new fields.NumberField({ initial: 0 })',stat)
        for src,typ in [(560,'character'),(565,'monster')]:
            txt='\n'.join(self.source(src));self.assertIn("max='99'",txt)
            for role,literal in [('wound-state','hp.max'),('temporaryHpSum','temporaryHpSum'),('vigor-display','vigor.max')]:
                e=self.data.entities[self.q[typ+'/sidebar.hbs.'+role]];loc=e['location']
                self.assertIn(literal,'\n'.join(self.source(src)[loc['line_start']-1:loc['line_end']]))
            self.assertIn('woundTreshold.value',txt)
            self.assertNotIn('temporaryHpSum',re.search(r'<input[^>]+name=.[^\n]*hp.value.*?>',txt,re.S)[0])
        for typ in ['character','monster']:
            eid=self.q[typ+'/sidebar.hbs.wound-state']
            reads={r['to'] for r in self.data.outgoing[eid] if r['kind']=='reads'}
            self.assertIn(self.q['stat().max'],reads)
            self.assertNotIn(self.q['stat().unmodifiedMax'],reads)

    def test_recovery_guards_cap_and_awaited_update(self):
        for src,cls,base in [(27,'WitcherActorSheet',259),(28,'WitcherActorSheetV1',236)]:
            loc=self.data.entities[self.q[cls+'._onRecoverSta']]['location']
            text='\n'.join(self.source(src)[loc['line_start']-1:loc['line_end']])
            self.assertEqual(text.count('this.actor.system.derivedStats.sta.value >= this.actor.system.derivedStats.sta.max'),2)
            self.assertIn('this.actor.system.derivedStats.sta.value + this.actor.system.derivedStats.rec.value',text)
            self.assertIn("'system.derivedStats.sta.value': this.actor.system.derivedStats.sta.max",text)
            self.assertIn('Math.min',text);self.assertEqual(text.count('await this.actor.update'),2)
            self.assertNotIn('ChatMessage',text)
            for act in ['recovery','full']:
                cb=self.q[cls+'._onRecoverSta/'+act+'.callback']
                p=next(p for p in self.new['processes']if p['entry']['entity']==cb)
                st={s['id']:s for s in p['steps']};self.assertEqual([e['step']for e in st['guard']['next']if 'step'in e],['notify','write'])
                self.assertEqual(st['write']['next'][0]['flow'],'await')
                self.assertEqual({r['to']for r in self.data.outgoing[cb]if r['kind']=='writes'},{self.q['DerivedStats.sta'],self.q['stat().value']})
        self.assertIn('recover-sta','\n'.join(self.source(520)));self.assertNotIn('recover-sta','\n'.join(self.source(564)))
        self.assertIn('await this.actor.update','\n'.join(self.source(42)[77:86]));self.assertIn('Math.min','\n'.join(self.source(42)[77:86]))

    def test_core_form_evidence_types_guards_and_full_form(self):
        evidence=json.loads((BASE/'examples/expansion-024-queries.json').read_text())['core_evidence'];self.assertEqual(len(evidence),9)
        for f in evidence:self.assertEqual(hashlib.sha256(Path(f['path']).read_bytes()).hexdigest(),f['sha256'],f['path'])
        app=Path('/opt/foundryvtt/client/applications/api/application.mjs').read_text().splitlines()
        submit='\n'.join(app[2133:2150]);change='\n'.join(app[2157:2162])
        self.assertIn('new FormDataExtended(form)',submit);self.assertIn('await handler.call',submit);self.assertIn('formConfig.submitOnChange',change);self.assertNotIn('await',change)
        self.assertNotIn('checkValidity',submit);self.assertNotIn('reportValidity',submit)
        doc=Path('/opt/foundryvtt/client/applications/api/document-sheet.mjs').read_text().splitlines()
        self.assertIn('if ( !this.isEditable ) return','\n'.join(doc[464:470]));self.assertIn('fallback: false','\n'.join(doc[485:495]));self.assertIn('await document.update','\n'.join(doc[524:532]))
        f=Path('/opt/foundryvtt/client/applications/ux/form-data-extended.mjs').read_text().splitlines()
        self.assertIn('for ( const element of form.elements )','\n'.join(f[104:126]));self.assertIn('element.matches(":disabled")','\n'.join(f[104:126]))
        t='\n'.join(f[170:243]);self.assertIn('field.checked',t);self.assertIn('if ( field.value === "" ) return null',t);self.assertIn('return Number(value)',t);self.assertNotIn('field.max',t)

    def test_core_preparation_evidence_not_a_local_save_claim(self):
        data=Path('/opt/foundryvtt/common/abstract/data.mjs').read_text().splitlines()
        self.assertIn('isEmpty(diff) || options.dryRun','\n'.join(data[668:702]));self.assertIn('this._initialize()','\n'.join(data[783:788]))
        client=Path('/opt/foundryvtt/client/documents/abstract/client-document.mjs').read_text().splitlines()
        self.assertIn('if ( !game._documentsReady ) return','\n'.join(client[59:67]))
        body='\n'.join(client[312:320]);expected=['this.system.prepareBaseData()','this.prepareBaseData()','this.prepareEmbeddedDocuments()','this.system.prepareDerivedData()','this.prepareDerivedData()']
        self.assertEqual(sorted(expected,key=body.index),expected)
        actor=Path('/opt/foundryvtt/client/documents/actor.mjs').read_text().splitlines();self.assertIn('this.applyActiveEffects("final")','\n'.join(actor[427:438]));self.assertIn('this.applyActiveEffects("initial")','\n'.join(actor[470:475]))
        self.assertEqual(self.data.entities[self.q['Actor.update/resource-preparation']]['boundary']['kind'],'external')

    def test_current_registration_context_and_v1_scope(self):
        self.assertIn('submitOnChange: true','\n'.join(self.source(27)[50:55]))
        self.assertIn('context.system = context.actor.system',self.source(27)[69]);self.assertIn('this.actor.toObject(false)',self.source(28)[34])
        regs='\n'.join(self.source(215));self.assertIn('WitcherCharacterSheet',regs);self.assertIn('WitcherMonsterSheet',regs);self.assertNotIn('WitcherActorSheetV1',regs)
        self.assertIn('this.activateListeners(this.element)',self.source(27)[215])
        self.assertIn("jquery.find('.recover-sta')",self.source(27)[224]);self.assertIn("html.find('.recover-sta')",self.source(28)[202])

    def test_shared_fields_link_manual_and_existing_programmatic_writers(self):
        hp={r['from']for r in self.data.incoming[self.q['DerivedStats.hp']]if r['kind']=='writes'}
        expected=['WitcherActorSheet/resource-form-submit','actor.damageMixin.updateDerivedStat','sheet.healMixin.recoverActor','onHeal','applyMonsterRegeneration','applyCombatEffect','item.consumeMixin.consume']
        self.assertTrue({self.q[n]for n in expected}<=hp)
        self.assertEqual(self.q['WitcherActorSheet._onRecoverSta'],'ent-003546');self.assertEqual(self.q['stat().value'],'ent-000004')
        ignored=self.q['CommonActorData.healthState.deathState.ignored']
        self.assertIn(self.q['WitcherActor.calculateStat'],{r['from']for r in self.data.incoming[ignored]if r['kind']=='reads'})

    def test_graph_definitions_facets_and_process_relations(self):
        d=self.data
        historical={kind:[json.loads(line)for part in d.manifest['parts'][kind]
            if '/expansion-'not in part or int(part.rsplit('expansion-',1)[1].split('.')[0])<=24
            for line in(BASE/part).read_text().splitlines()]
            for kind in ['entities','relations','processes']}
        self.assertEqual([len(d.sources),*[len(historical[k])for k in ['entities','relations','processes']]],[615,4634,12075,363])
        self.assertEqual([len(self.new[k])for k in ['entities','relations','processes']],[55,267,10])
        primary_at_024=['src-000002', 'src-000003', 'src-000004', 'src-000005', 'src-000006', 'src-000007', 'src-000008', 'src-000010', 'src-000014', 'src-000015', 'src-000016', 'src-000017', 'src-000018', 'src-000019', 'src-000022', 'src-000023', 'src-000025', 'src-000027', 'src-000028', 'src-000029', 'src-000031', 'src-000032', 'src-000034', 'src-000036', 'src-000038', 'src-000040', 'src-000041', 'src-000042', 'src-000043', 'src-000045', 'src-000046', 'src-000047', 'src-000050', 'src-000051', 'src-000052', 'src-000054', 'src-000055', 'src-000056', 'src-000057', 'src-000058', 'src-000059', 'src-000062', 'src-000063', 'src-000074', 'src-000080', 'src-000081', 'src-000082', 'src-000083', 'src-000084', 'src-000085', 'src-000086', 'src-000087', 'src-000088', 'src-000089', 'src-000090', 'src-000091', 'src-000092', 'src-000094', 'src-000095', 'src-000096', 'src-000097', 'src-000098', 'src-000099', 'src-000100', 'src-000101', 'src-000108', 'src-000109', 'src-000112', 'src-000126', 'src-000127', 'src-000129', 'src-000130', 'src-000131', 'src-000132', 'src-000133', 'src-000134', 'src-000136', 'src-000137', 'src-000155', 'src-000157', 'src-000159', 'src-000160', 'src-000164', 'src-000167', 'src-000172', 'src-000178', 'src-000181', 'src-000182', 'src-000183', 'src-000184', 'src-000186', 'src-000192', 'src-000193', 'src-000194', 'src-000195', 'src-000196', 'src-000197', 'src-000202', 'src-000204', 'src-000205', 'src-000206', 'src-000209', 'src-000212', 'src-000213', 'src-000214', 'src-000215', 'src-000216', 'src-000217', 'src-000445', 'src-000453', 'src-000455', 'src-000481', 'src-000482', 'src-000483', 'src-000484', 'src-000485', 'src-000486', 'src-000488', 'src-000490', 'src-000491', 'src-000492', 'src-000493', 'src-000494', 'src-000496', 'src-000506', 'src-000509', 'src-000510', 'src-000513', 'src-000521', 'src-000522', 'src-000527', 'src-000530', 'src-000531', 'src-000541', 'src-000542', 'src-000543', 'src-000544', 'src-000547', 'src-000551', 'src-000560', 'src-000562', 'src-000565', 'src-000583', 'src-000585', 'src-000590', 'src-000591', 'src-000592', 'src-000593', 'src-000599', 'src-000610', 'src-000613']
        self.assertEqual(len(primary_at_024),151)
        self.assertTrue(set(primary_at_024)<=set(d.manifest['scope']['selected_sources']))
        historical_entities=historical['entities']
        represented={e['location']['source']for e in historical_entities if e['kind']!='boundary'and e.get('location')}
        historical_states=collections.Counter('complete'if s['coverage']['definitions']['state']=='complete'else 'partial'if sid in represented else 'not_indexed'for sid,s in d.sources.items())
        self.assertEqual(historical_states,{'complete':2,'partial':252,'not_indexed':361})
        for e in self.new['entities']:
            if e['kind']=='boundary':continue
            defs=[r for r in d.incoming[e['id']]if r['kind']=='defines'];self.assertEqual(len(defs),1);self.assertEqual(defs[0]['from'],e['owner'])
        for p in self.new['processes']:
            for st in p['steps']:
                l=st['location'];self.assertLessEqual(l['line_end'],len(self.source(int(l['source'][4:]))))
                for rid in st['relations']:self.assertEqual(d.relations[rid]['from'],st['entity'])
        for s in [560,565]:
            row=d.sources[f'src-{s:06}'];self.assertEqual(row['coverage']['definitions']['state'],'partial');self.assertTrue(row['coverage']['processes']['included'])

