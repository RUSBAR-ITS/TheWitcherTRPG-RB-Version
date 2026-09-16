"""Индекс локализаций: исходные JSON/код и поиск. Foundry/браузер не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
from test_query import BASE, ROOT, query, run_cli

class LocalizationExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.leaves={}
        def unique(pairs):
            out={}
            for k,v in pairs:
                if k in out:raise AssertionError('Duplicate raw member: '+k)
                out[k]=v
            return out
        for lang in ['en','ru']:
            raw=json.loads((ROOT/f'lang/{lang}.json').read_text(),object_pairs_hook=unique)
            result={}
            def walk(obj,path):
                for k,v in obj.items():
                    seg=path+[k]
                    if isinstance(v,dict):walk(v,seg)
                    else:
                        if not isinstance(v,str):raise AssertionError('Not a string leaf')
                        key='.'.join(seg)
                        if key in result:raise AssertionError('Expanded collision: '+key)
                        result[key]=(v,seg)
            walk(raw,[]);cls.leaves[lang]=result
        cls.translations={lang:{e['name']:e for e in cls.data.entities.values()
            if e['kind']=='field' and (e.get('location') or {}).get('source')==sid}
            for lang,sid in [('en','src-000002'),('ru','src-000003')]}

    def test_24_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-011-queries.json').read_text())['cases']
        self.assertEqual(len(cases),24)
        for case in cases:
            with self.subTest(case=case['id']):
                run=run_cli([*case['command'],'--format','json'],cwd='/tmp')
                self.assertEqual(run.returncode,0,run.stderr)
                out=json.loads(run.stdout);items=out['items'];first=items[0] if items else {}
                actual=dict(ids=[x['id'] for x in items if 'id' in x],
                    from_ids=sorted({x['from'] for x in items if 'from' in x}),
                    to_ids=sorted({x['to'] for x in items if 'to' in x}),
                    next_steps=[x['step'] for x in first.get('next',[]) if 'step' in x],
                    next_exits=[x['exit'] for x in first.get('next',[]) if 'exit' in x],
                    resolution=first.get('boundary',{}).get('kind'),
                    refs=[x['path'] for x in items if 'path' in x])
                for k,v in case['expected'].items():
                    if k.startswith('includes_'):self.assertTrue(set(v)<=set(actual[k[9:]]),(k,actual))
                    else:self.assertEqual(actual[k],v,k)
                self.assertEqual(out['freshness']['state'],'current')

    def test_all_raw_leaves_exact_addresses_and_language_identity(self):
        self.assertEqual([len(self.leaves[l]) for l in ['en','ru']],[1163,1162])
        for lang,sid in [('en','src-000002'),('ru','src-000003')]:
            self.assertEqual(set(self.translations[lang]),set(self.leaves[lang]))
            source=(ROOT/f'lang/{lang}.json').read_text().splitlines()
            for key,(value,segments) in self.leaves[lang].items():
                e=self.translations[lang][key];loc=e['location']
                pointer='/'+'/'.join(x.replace('~','~0').replace('/','~1') for x in segments)
                self.assertEqual(loc['symbol'],pointer)
                self.assertEqual(e['qualified_name'],lang+'::'+key)
                self.assertEqual(e['owner'],sid)
                self.assertIn(json.dumps(segments[-1],ensure_ascii=False),source[loc['line_start']-1])
                self.assertIn(json.dumps(value,ensure_ascii=False),e['summary'])
                self.assertNotIn(key,e['aliases'])  # aliases normalize case; exact keys must not
                self.assertEqual(loc['line_end'],loc['line_start'])
            self.assertEqual(self.data.sources[sid]['coverage']['definitions']['state'],'complete')
            self.assertFalse(self.data.sources[sid]['coverage']['definitions']['remaining'])
        # A raw dotted property remains an intact pointer segment.
        r=self.translations['ru']['WITCHER.Actor.Skill.Intelligence']
        self.assertEqual(r['location']['symbol'],'/WITCHER/Actor/Skill.Intelligence')

    def test_pairing_placeholders_empty_strings_and_unmatched_keys(self):
        en=self.leaves['en'];ru=self.leaves['ru'];common=en.keys()&ru.keys()
        self.assertEqual((len(common),len(en.keys()-ru.keys()),len(ru.keys()-en.keys())),(1160,3,2))
        self.assertEqual(ru.keys()-en.keys(),{'WITCHER.Damage.silver','WITCHER.Dialog.attackCustom'})
        expected={
            'WITCHER.currencyConverter.errors.insufficient':{'currency'},
            'WITCHER.Combat.healed':{'target','heal'}}
        for lang,leaves in self.leaves.items():
            ph={k:set(re.findall(r'{([^}]+)}',v)) for k,(v,_) in leaves.items() if re.search(r'{[^}]+}',v)}
            self.assertEqual(ph,expected)
            self.assertEqual(sum(v=='' for v,_ in leaves.values()),4)
            dotted={tuple(seg[:i+1]) for _,seg in leaves.values() for i,k in enumerate(seg) if '.' in k}
            self.assertEqual(len(dotted),63)
        pairs=[r for r in self.data.relations.values() if r['kind']=='refers' and
               r['from'] in {e['id'] for e in self.translations['en'].values()} and
               r['to'] in {e['id'] for e in self.translations['ru'].values()}]
        self.assertEqual(len(pairs),1160)
        self.assertEqual({(r['from'],r['to']) for r in pairs},
            {(self.translations['en'][k]['id'],self.translations['ru'][k]['id']) for k in common})

    def test_literals_and_missing_paths_have_source_evidence(self):
        part=[json.loads(l) for l in (BASE/'data/relations/expansion-011.jsonl').read_text().splitlines()]
        literals=[r for r in part if r['kind']=='refers' and r['from'].startswith('src-') and
                  r.get('payload','').startswith(('WITCHER.','TYPES.','EFFECT.'))]
        places=set()
        for r in literals:
            loc=r['location'];line=(ROOT/self.data.sources[loc['source']]['path']).read_text().splitlines()[loc['line_start']-1]
            self.assertIn(r['payload'],line);places.add((loc['source'],loc['line_start'],r['payload']))
            target=self.data.nodes[r['to']]
            if target['kind']=='field':self.assertEqual(target['name'],r['payload'])
            else:self.assertEqual(target['kind'],'boundary')
        self.assertEqual(len(places),533)  # Existing sites plus changed/new label references in issue-00330.
        missing=self.data.entities['ent-003318']
        self.assertEqual(missing['boundary']['expression'],'WITCHER.Item.Availability')
        for lang in ['en','ru']:self.assertIn(missing['boundary']['expression'],self.leaves[lang])
        # Prefix expressions are not recorded as missing leaf definitions.
        self.assertFalse(any(e['kind']=='field' and e['name'] in ['WITCHER.St','WITCHER.Actor.settings'] for e in self.data.entities.values()))

    def test_precise_producers_payloads_and_existing_ids(self):
        d=self.data
        form=[r for r in d.relations.values() if r['from']=='ent-000729' and r['kind']=='reads']
        self.assertIn(self.translations['en']['WITCHER.Effect.applyAfterCalculations']['id'],[r['to'] for r in form])
        self.assertIn('WITCHER.Effect.applyAfterCalculations',self.translations['ru'])
        calls=[r for r in d.relations.values() if r['to']=='ent-003297' and r['kind']=='calls']
        self.assertEqual({(r['from'],r['location']['line_start'],r['payload']) for r in calls},{
            ('ent-003319',69,'{currency: game.i18n.localize(CONFIG.WITCHER.currency[from])}'),
            ('ent-003320',41,'{heal: heal, target: target.name}')})
        expected=[('ent-003309','ent-000010'),('ent-003310','ent-000928'),('ent-003311','ent-000010')]
        for src,to in expected:
            self.assertIn(to,[r['to'] for r in d.relations.values() if r['from']==src and r['kind']=='reads'])
        self.assertEqual(d.entities['ent-000725']['qualified_name'],'game.i18n.localize')
        self.assertEqual(d.entities['ent-000807']['qualified_name'],'ChatMessage.create')
        for lang,line,name in [('en',94,'English'),('ru',124,'Russian')]:
            manifest=(ROOT/'system.json').read_text().splitlines()
            self.assertIn('"lang": "'+lang+'"',manifest[line-1])
            self.assertIn('"name": "'+name+'"',manifest[line])

    def test_accumulated_reverse_edges_and_process_participation(self):
        d=self.data
        historical={kind:[json.loads(l) for part in d.manifest['parts'][kind]
            if not re.search(r'expansion-(\d+)',part) or int(re.search(r'expansion-(\d+)',part).group(1))<=11
            for l in (BASE/part).read_text().splitlines()] for kind in ['entities','relations','processes']}
        self.assertEqual([len(d.sources),*[len(historical[k]) for k in ['entities','relations','processes']]],[615,3361,7570,97])
        represented={e['location']['source'] for e in historical['entities'] if e.get('location') and e['kind']!='boundary'}
        self.assertEqual(len(represented),154)
        for r in d.relations.values():
            self.assertIn(r,d.outgoing[r['from']])
            self.assertIn(r,d.incoming[r['to']])
        for p in d.processes.values():
            ss={x['id']:x for x in p['steps']};todo=[p['steps'][0]['id']];seen=set();exits=set()
            while todo:
                sid=todo.pop()
                if sid in seen:continue
                seen.add(sid)
                for n in ss[sid]['next']:
                    if 'step' in n:todo.append(n['step'])
                    else:exits.add(n['exit'])
            self.assertEqual(seen,set(ss),p['id'])
            self.assertEqual(exits,{e['id'] for e in p['exits']},p['id'])
        for p in [d.processes[f'proc-{n:06}'] for n in range(92,98)]:
            for step in p['steps']:
                for rid in step['relations']:
                    r=d.relations[rid]
                    self.assertEqual(r['from'],step['entity'])
                    self.assertEqual(r['location']['source'],step['location']['source'])
                    self.assertTrue(step['location']['line_start']<=r['location']['line_start']<=step['location']['line_end'])
            out=d.query(query.parser().parse_args(['processes',p['entry']['entity'],'--limit','100','--no-verify']))
            self.assertIn(p['id'],[x['id'] for x in out['items']])
        # Every prior ID still belongs to its prior part; no renumbering to accommodate translations.
        for kind,last in [('entities',1008),('relations',2671),('processes',91)]:
            old=[json.loads(l) for part in d.manifest['parts'][kind] if not re.search(r'expansion-(\d+)',part) or int(re.search(r'expansion-(\d+)',part).group(1))<=10
                 for l in (BASE/part).read_text().splitlines()]
            self.assertEqual(len(old),last)
            self.assertEqual({int(r['id'].split('-')[1]) for r in old},set(range(1,last+1)))

    def test_external_contract_hashes_and_fallback_field_distinction(self):
        text=(BASE/'coverage-011.md').read_text()
        rows=re.findall(r'^\| (/opt/foundryvtt/[^|]+) \| [^|]+ \| ([0-9a-f]{64}) \|$',text,re.M)
        self.assertEqual(len(rows),7)
        for path,digest in rows:self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),digest)
        core=Path('/opt/foundryvtt')
        loc=(core/'client/helpers/localization.mjs').read_text().splitlines()
        for line,literal in [(235,'this.translations = await'),(236,'lang !== "en"'),(368,'expandObject(json)'),
                             (435,'localize(stringId, data)'),(437,'typeof translation !== "string"'),
                             (444,'translation.replace'),(481,'value: Localization.prototype.localize')]:
            self.assertIn(literal,loc[line-1])
        h=(core/'client/applications/handlebars.mjs').read_text().splitlines()
        self.assertIn('if ( !field )',h[534])
        fields=(core/'common/data/fields.mjs').read_text().splitlines()
        self.assertIn('this.label ?? this.fieldPath',fields[663])
        fg=(core/'client/applications/forms/fields.mjs').read_text().splitlines()
        self.assertIn('lbl.innerText = localize ? _loc(label) : label',fg[53])
        # Existing failure marker remains a distinct boundary, not a made-up translation definition.
        self.assertEqual(self.data.entities['ent-000731']['kind'],'boundary')

if __name__=='__main__':
    unittest.main()
