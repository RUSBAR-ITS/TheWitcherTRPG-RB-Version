"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class DocumentsExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l) for l in (BASE/f'data/{k}/expansion-012.jsonl').read_text().splitlines()]
                 for k in ['entities','relations','processes']}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_24_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-012-queries.json').read_text())['cases']
        self.assertEqual(len(cases),24)
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

    def test_models_declarations_ownership_and_weight_inputs(self):
        for q,n,line,literal in [
            ('CommonActorData.defineSchema',55,18,'defineSchema'),('CommonActorData.prepareBaseData',55,63,'prepareBaseData'),
            ('LootData.defineSchema',56,6,'defineSchema'),('LootData.calcCurrencyWeight',56,14,'calcCurrencyWeight'),
            ('CommonItemData.quantity',109,7,'new fields.StringField'),('CommonItemData.calcWeight',109,18,'calcWeight'),
            ('CommonItemData.canBeRepaired',109,26,'canBeRepaired'),('createEnrichedText',102,1,'createEnrichedText')]:
            e=self.data.entities[self.q[q]];self.assertEqual((e['location']['source'],e['location']['line_start']),(f'src-{n:06}',line))
            self.assertIn(literal,self.source(n)[line-1])
        self.assertIn("quantity: new fields.StringField",self.source(109)[6])
        self.assertIn('this.isCarried && !this.isStored ? this.quantity * this.weight : 0',self.source(109)[18])
        self.assertEqual({r['to'] for r in self.edges('CommonItemData.calcWeight','reads')},
                         {self.q['CommonItemData.'+n] for n in ['quantity','weight','isStored','isCarried']})
        self.assertEqual([r['to'] for r in self.edges('LootData','extends')],[self.q['foundry.abstract.TypeDataModel']])
        for q in ['CharacterData','MonsterData']:
            self.assertEqual([r['to'] for r in self.edges(q,'extends')],[self.q['CommonActorData']])
        for n in [55,56]:
            body='\n'.join(self.source(n));self.assertEqual(body.count('Number(this.currency.'),7)
            self.assertIn('return Number(totalPieces * 0.001)',body)
        fields=[e for e in self.new['entities'] if e['kind']=='field' and e['owner']==self.q['CommonItemData']]
        self.assertEqual({e['name'] for e in fields},{'description','quantity','weight','cost','sourcebook','isHidden','isStored','isCarried'})

    def test_preparation_migrations_and_prototype_order(self):
        s=self.source(55)
        for n,literal in [(64,'this.stats'),(77,'Math.floor'),(79,'Math.clamp'),(108,'source.derivedStats.vigor.value'),
                          (111,'this.migrateCalculatedStats(source)'),(112,'this.migrateAdrenaline(source)'),(114,'super.migrateData(source)')]:
            self.assertIn(literal,s[n-1])
        self.assertNotIn('toxicity','\n'.join(s[116:129]))
        a=self.source(47)
        self.assertIn("this.type === 'loot'",a[37]);self.assertIn("this.type === 'mystery'",a[38])
        self.assertIn('applyStatus',a[46]);self.assertNotIn('await',a[46])
        # Actor method is reused from the pilot; no duplicate calculation process introduced.
        self.assertFalse(any(p['entry']['entity']==self.q['WitcherActor.prepareDerivedData'] for p in self.new['processes']))
        mixes=sorted(self.edges('WitcherActor','mixes'),key=lambda r:r['location']['line_start'])
        target=[self.data.entities[r['to']]['qualified_name'] for r in mixes]
        self.assertLess(target.index('actor.modifierMixin'),target.index('actor.defenseMixin'))
        for r in mixes:self.assertIn('Object.assign',a[r['location']['line_start']-1])
        item=self.source(192)
        self.assertIn("'Hexes'",item[18]);self.assertIn("'Rituals'",item[22])
        self.assertNotIn('else','\n'.join(item[17:26]))
        self.assertEqual(list(self.steps(110)),['hex','ritual'])

    def test_enrichment_values_await_and_model_dispatch(self):
        h=self.source(102);self.assertIn('await',h[2]);self.assertIn('field',h[2]);self.assertIn('getField(fieldPath)',h[4])
        m=self.source(57)
        for n,name in [(69,'common'),(70,'academicKnowledge'),(71,'monsterLore')]:
            self.assertIn('await createEnrichedText',m[n-1]);self.assertIn("'"+name+"'",m[n-1])
        self.assertEqual([r['location']['line_start'] for r in self.edges('MonsterData.enrichedText','calls')],[69,70,71])
        for step in self.steps(113).values():self.assertTrue(all(n['flow']=='await' for n in step['next']))
        self.assertEqual(self.steps(111)['html']['next'][0]['step'],'result')
        calls={r['to'] for r in self.edges('WitcherItemSheet._prepareContext','calls')}
        self.assertIn(self.q['WitcherItemSheet/document.system.enrichedText'],calls)
        self.assertNotIn(self.q['WitcherItem.enrichedText'],calls)
        self.assertIn('await this.document.system.enrichedText?.()',self.source(172)[51])
        self.assertIn('await this.system.enrichedText?.()',self.source(192)[172])

    def test_live_context_copy_and_selected_mutations(self):
        v2=self.source(27);v1=self.source(28);char=self.source(29)
        for n,literal in [(66,'CONFIG.WITCHER'),(67,'initiative'),(69,'context.actor = this.actor'),
            (70,'context.system = context.actor.system'),(74,'context.system.combatEffects.temporaryEffects.temporaryHpSum'),(163,'cost()'),(199,'enhancementItems')]:
            self.assertIn(literal,v2[n-1])
        self.assertIn('toObject(false)',v1[34]);self.assertIn('actorData.system',v1[35])
        for n in range(78,84):self.assertIn('await this._prepare',v2[n-1])
        self.assertNotIn('update(','\n'.join(v2[57:96]));self.assertNotIn('update(','\n'.join(v2[174:212]))
        self.assertIn('Object.entries(context.system.general.lifeEvents).map',char[132]);self.assertIn('...value',char[134])
        self.assertEqual(self.steps(132)['character']['next'][0]['flow'],'await')
        self.assertEqual(self.steps(132)['helpers']['next'][0]['flow'],'sync')
        self.assertNotIn('await','\n'.join(char[125:131]))
        self.assertIn('Number(this[i].system.quantity ?? 0)',v2[28])
        self.assertIn('Math.ceil(total)',v2[30])
        self.assertNotIn('enhancementItems','\n'.join(v2[203:212]))

    def test_item_forms_properties_drop_and_external_boundaries(self):
        s=self.source(172)
        self.assertIn('super._onChangeForm',s[78]);self.assertNotIn('await',s[78])
        self.assertIn("value == 'on'",s[151]);self.assertIn('checked',s[152])
        for n in [142,156,163]:self.assertIn('this.item.update',s[n-1]);self.assertNotIn('await',s[n-1])
        self.assertEqual([r['to'] for r in self.edges('WitcherItemSheet._onAddEffect','calls')],[self.q['Document.update/Item']])
        self.assertEqual({x['step'] for x in self.steps(127)['checkbox']['next']},{'checked','write'})
        for step in self.steps(127).values():self.assertTrue(all(n['flow']=='sync' for n in step['next']))
        for n,literal in [(101,'this.isEditable'),(107,'await documentClass.fromDropData'),(108,'return this._onDropDocument'),(111,'return data')]:self.assertIn(literal,s[n-1])
        self.assertNotIn('dropItemSheetData','\n'.join(s))
        p=self.steps(130);self.assertEqual([x['step'] for x in p['type']['next'] if 'step' in x],['ae','actor','item','folder','other'])
        for k in ['ae','actor','item','folder']:self.assertTrue(all(n['flow']=='await' for n in p[k]['next']))
        for q in ['WitcherItemSheet/_onDropActor','WitcherItemSheet/_onDropFolder']:
            self.assertEqual(self.data.entities[self.q[q]]['boundary']['kind'],'dynamic')

    def test_addresses_reverse_links_coverage_and_process_participation(self):
        d=self.data
        self.assertEqual([len(self.new[k]) for k in ['entities','relations','processes']],[231,512,37])
        # The .012 numerical result is historical; .013 tests check current totals.
        historical={kind:[json.loads(line) for part in d.manifest['parts'][kind]
                          if not (re.search(r'expansion-(\d+)',part) and int(re.search(r'expansion-(\d+)',part)[1])>12)
                          for line in (BASE/part).read_text().splitlines()]
                    for kind in ['entities','relations','processes']}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,3554,7907,134])
        represented={e['location']['source'] for e in historical['entities'] if e['kind']!='boundary' and e['location']}
        self.assertEqual(len(represented),179)
        self.assertEqual((len(represented)-2,615-len(represented)),(177,436))
        previous_primary=['src-000002', 'src-000003', 'src-000004', 'src-000005', 'src-000006', 'src-000007', 'src-000008', 'src-000019', 'src-000022', 'src-000023', 'src-000027', 'src-000028', 'src-000029', 'src-000031', 'src-000032', 'src-000036', 'src-000040', 'src-000045', 'src-000046', 'src-000047', 'src-000052', 'src-000054', 'src-000055', 'src-000056', 'src-000057', 'src-000080', 'src-000081', 'src-000082', 'src-000083', 'src-000084', 'src-000085', 'src-000086', 'src-000087', 'src-000088', 'src-000089', 'src-000090', 'src-000091', 'src-000092', 'src-000109', 'src-000172', 'src-000178', 'src-000192', 'src-000202', 'src-000205', 'src-000206', 'src-000209', 'src-000212', 'src-000214', 'src-000215', 'src-000216', 'src-000445', 'src-000453', 'src-000481', 'src-000506', 'src-000521', 'src-000522', 'src-000527', 'src-000531', 'src-000541', 'src-000542', 'src-000543', 'src-000544', 'src-000547', 'src-000562', 'src-000610']
        self.assertEqual(len(previous_primary),65)
        self.assertTrue(set(previous_primary)<=set(d.manifest['scope']['selected_sources']))
        for e in self.new['entities']:
            if e['location']:
                loc=e['location'];self.assertLessEqual(loc['line_end'],len((ROOT/d.sources[loc['source']]['path']).read_text().splitlines()))
            if e['kind']=='boundary':continue
            defs=[r for r in d.incoming[e['id']] if r['kind']=='defines']
            self.assertEqual(len(defs),1,e['id']);self.assertEqual(defs[0]['from'],e['owner'])
        for r in d.relations.values():
            self.assertIn(r,d.outgoing[r['from']]);self.assertIn(r,d.incoming[r['to']])
        for p in self.new['processes']:
            ss={s['id']:s for s in p['steps']};todo=[p['steps'][0]['id']];seen=set();exits=set()
            while todo:
                name=todo.pop()
                if name in seen:continue
                seen.add(name)
                for n in ss[name]['next']:
                    if 'step' in n:todo.append(n['step'])
                    else:exits.add(n['exit'])
            self.assertEqual(seen,set(ss),p['id']);self.assertEqual(exits,{x['id'] for x in p['exits']},p['id'])
            for s in p['steps']:
                for rid in s['relations']:
                    r=d.relations[rid];self.assertEqual(r['from'],s['entity']);self.assertEqual(r['location']['source'],s['location']['source'])
                    self.assertTrue(s['location']['line_start']<=r['location']['line_start']<=s['location']['line_end'])
            out=d.query(query.parser().parse_args(['processes',p['entry']['entity'],'--limit','100','--no-verify']))
            self.assertIn(p['id'],[x['id'] for x in out['items']])
        for sid,s in d.sources.items():
            expected={
                'definitions':{e['id'] for e in d.entities.values() if e['kind']!='boundary' and (e.get('location')or{}).get('source')==sid},
                'relations':{r['id'] for r in d.relations.values() if (r.get('location')or{}).get('source')==sid},
                'processes':{p['id'] for p in d.processes.values() if any(st['location']['source']==sid for st in p['steps'])}}
            for facet,ids in expected.items():self.assertEqual(set(s['coverage'][facet]['included']),ids,(sid,facet))

    def test_core_contract_hashes_and_preparation_boundaries(self):
        text=(BASE/'coverage-012.md').read_text()
        rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',text,re.M)
        self.assertEqual(len(rows),5)
        for path,digest in rows:self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)
        core=Path('/opt/foundryvtt')
        p=(core/'client/documents/abstract/client-document.mjs').read_text().splitlines()
        for n,literal in [(315,'this.system.prepareBaseData()'),(316,'this.prepareBaseData()'),(317,'this.prepareEmbeddedDocuments()'),
                          (318,'this.system.prepareDerivedData()'),(319,'this.prepareDerivedData()')]:self.assertIn(literal,p[n-1])
        self.assertIn('this.constructor.schema.toObject(this)',(core/'common/abstract/data.mjs').read_text().splitlines()[825])
        external=[e for e in self.new['entities'] if e.get('boundary',{}).get('kind')=='external']
        self.assertTrue(external)
        self.assertTrue(all(e['location'] is None and e['boundary']['dependency']=='foundry' for e in external))

if __name__=='__main__':unittest.main()
