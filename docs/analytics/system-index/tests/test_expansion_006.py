"""Расширение .006: независимые ориентиры регистраций и локальных процессов.

Проверяется справочник текущего кода; JavaScript, Foundry, браузер и БД не запускаются.
"""
from collections import Counter
import json
import re
import unittest

from test_query import BASE, ROOT, query, run_cli


class RegistrationExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = query.Dataset()

    def test_16_source_grounded_cli_cases(self):
        cases = json.loads((BASE / 'examples/expansion-006-queries.json').read_text())['cases']
        self.assertEqual(len(cases), 16)
        for case in cases:
            with self.subTest(case=case['id']):
                run = run_cli(case['command'] + ['--format', 'json'], cwd='/tmp')
                self.assertEqual(run.returncode, 0, run.stderr)
                out = json.loads(run.stdout); items = out['items']; first = items[0] if items else {}
                projection = dict(ids=[x['id'] for x in items if 'id' in x],
                    locations=sorted([[x['location']['source'], x['location']['line_start']]
                                      for x in items if x.get('location')]),
                    owner=first.get('owner'), from_ids=sorted({x['from'] for x in items if 'from' in x}),
                    empty_reason=out['empty_reason'], includes_refs=[x['path'] for x in items if 'path' in x],
                    includes_anchors=[x.get('anchor') for x in items],
                    next_steps=[e['step'] for e in first.get('next', []) if 'step' in e],
                    next_exits=[e['exit'] for e in first.get('next', []) if 'exit' in e])
                for k,v in case['expected'].items():
                    if k.startswith('includes_'): self.assertTrue(set(v) <= set(projection[k]), (k, projection[k]))
                    else: self.assertEqual(projection[k], sorted(v) if k=='locations' else v, k)
                self.assertEqual(out['freshness']['state'], 'current')
                self.assertEqual(out['coverage']['state'], 'partial')

    def test_manifest_and_all_model_assignments_are_separate(self):
        # Expectations taken from the declarations, including Item.base and implicit AE/Chat base.
        manifest = json.loads((ROOT / 'system.json').read_text())
        self.assertEqual(set(manifest['documentTypes']['Actor']), {'character','monster','loot'})
        self.assertEqual(set(manifest['documentTypes']['Item']), set('alchemical armor component container criticalWound diagrams enhancement hex homeland mount mutagen note profession race ritual spell valuable weapon'.split()))
        specs = {
            'Actor': 'character:CharacterData monster:MonsterData loot:LootData mystery:MysteryActorData',
            'Item': 'base:CommonItemData alchemical:AlchemicalData armor:ArmorData container:ContainerData component:ComponentData criticalWound:CriticalWoundData diagrams:DiagramData enhancement:EnhancementData mount:MountData mutagen:MutagenData note:NoteData profession:ProfessionData homeland:HomelandData race:RaceData spell:SpellData hex:HexData ritual:RitualData valuable:ValuableData weapon:WeaponData clue:ClueData obstacle:ObstacleData skill:SkillItemData',
            'ActiveEffect': 'base:WitcherActiveEffectData temporaryItemImprovement:WitcherTemporaryItemImprovementData',
            'ChatMessage': 'base:BaseMessageData attack:AttackMessageData defense:DefenseMessageData damage:DamageMessageData'}
        expected = {f'CONFIG.{family}.dataModels.{key}': target
                    for family, pairs in specs.items() for key,target in (s.split(':') for s in pairs.split())}
        expected['CONFIG.ChatMessage.documentClass'] = 'WitcherChatMessage'
        edges = [r for r in self.data.relations.values() if r['from']=='ent-000328' and r['kind']=='registers']
        actual = {r['payload']: self.data.entities[r['to']]['qualified_name'] for r in edges}
        self.assertEqual(actual, expected); self.assertEqual(len(edges), 33)
        for r in edges:
            c=self.data.entities[r['to']]; loc=c['location']; path=self.data.sources[loc['source']]['path']
            line=(ROOT/path).read_text().splitlines()[loc['line_start']-1]
            self.assertIn('class '+c['qualified_name'],line)
            self.assertTrue(any(e['kind']=='imports' and e['from']=='src-000214' and e['to']==loc['source'] for e in self.data.relations.values()))
        declarations = {e['qualified_name'].removeprefix('manifest.documentTypes.') for e in self.data.entities.values()
                        if e['qualified_name'].startswith('manifest.documentTypes.')}
        self.assertEqual(declarations, {f'{f}.{t}' for f, ts in manifest['documentTypes'].items() for t in ts})

    def test_sheets_types_defaults_alias_and_resource_addresses(self):
        registrations=[r for r in self.data.relations.values() if r['from']=='ent-000401' and r['kind']=='registers']
        expected_lines=[34,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,105,109,113,118,122,126,131,142]
        self.assertEqual(sorted(r['location']['line_start'] for r in registrations),expected_lines)
        for r in registrations:
            self.assertIn('makeDefault=true',r['payload']);self.assertIn('namespace=witcher',r['payload'])
            c=self.data.entities[r['to']];self.assertEqual(c['kind'],'class')
            self.assertTrue(any(e['kind']=='extends' and e['from']==c['id'] for e in self.data.relations.values()))
        self.assertEqual(self.data.entities['ent-000448']['qualified_name'],'WitcheProfessionSheet')
        self.assertIn('WitcherProfessionSheet',self.data.entities['ent-000448']['aliases'])
        historical_ids={json.loads(l)['id'] for l in (BASE/'data/relations/expansion-006.jsonl').read_text().splitlines()}
        declarations=[r for r in self.data.relations.values() if r['id'] in historical_ids and r['kind']=='refers'
                      and (self.data.entities.get(r['from'],{}).get('qualified_name','').endswith(('.PARTS','.template')))]
        self.assertEqual(len(declarations),50)  # 49 template/return + one templates preload entry.
        self.assertEqual(sum(r['to'].startswith('src-') for r in declarations),41)
        self.assertEqual(len({r['payload'] for r in declarations}),44)
        for r in declarations:
            loc=r['location']; line=(ROOT/self.data.sources[loc['source']]['path']).read_text().splitlines()[loc['line_start']-1]
            self.assertIn(r['payload'],line)
        self.assertEqual((ROOT/'module/item/sheets/WitcherItemSheet.js').read_text().splitlines()[29].strip(),'static PARTS = {};')
        self.assertFalse(any(r['from']=='ent-000524' and r['kind']=='refers' for r in declarations))

    def test_settings_and_deferred_choices_match_source(self):
        expected = {'criticalWoundsPack': (2, "default: 'TheWitcherTRPG-RB-Version.criticalWounds'", 'type: new foundry.data.fields.StringField'),
                    'useOptionalAdrenaline':(17,'default: false','type: Boolean'),
                    'useOptionalVerbalCombat':(25,'default: false','type: Boolean'),
                    'silverTrait':(37,'default: false','type: Boolean'),
                    'displayRollsDetails':(46,'default: false','type: Boolean'),
                    'useWitcherFont':(54,'default: false','type: Boolean'),
                    'displayRep':(61,'default: false','type: Boolean'),
                    'clickableImageItemTypes':(69,"default: 'valuable'",'type: String'),
                    'clickableImageCheckboxForGMOnly':(77,'default: true','type: Boolean')}
        settings={e['name']:e for e in self.data.entities.values() if e['kind']=='setting'}
        self.assertEqual(set(settings),set(expected))
        source=(ROOT/'module/setup/settings.js').read_text().splitlines()
        for key,(line,default,typ) in expected.items():
            e=settings[key];self.assertEqual(e['location']['line_start'],line)
            body='\n'.join(source[line-1:e['location']['line_end']])
            for text in [default,typ,"scope: 'world'",'config: true']:
                self.assertIn(text,body);self.assertIn(text,e['summary'])
        to_choices=[r for r in self.data.relations.values() if r['from']=='ent-000568' and r['to']=='ent-000569']
        self.assertEqual([r['kind'] for r in to_choices],['passes'])
        self.assertEqual(to_choices[0]['location']['line_start'],11)
        self.assertIn("game.packs.filter(p => p.documentName === 'Item')",source[86])
        self.assertIn('record[p.collection] = p.title',source[90])

    def test_ready_and_nonawaited_calls_follow_actual_code(self):
        source=(ROOT/'module/TheWitcherTRPG.js').read_text().splitlines()
        for n,text in [(25,'registerHooks();'),(47,'preloadHandlebarsTemplates();'),(64,'criticalWoundsPack'),(65,'await criticalWounds.getIndex'),(70,"Hooks.on('hotbarDrop'"),(72,'createMacro(data, slot);'),(73,'return false;'),(90,'registerSocketListeners();'),(91,'deprecationWarnings();'),(172,'registerHandelbarHelpers();')]:self.assertIn(text,source[n-1])
        ready=self.data.processes['proc-000021']; steps={s['id']:s for s in ready['steps']}
        self.assertEqual(set(steps),{'lookup','index','hotbar','font-choice','font','socket','deprecations'})
        index=steps['index']['next'];self.assertEqual([(x.get('step'),x.get('exit'),x['flow']) for x in index],[(None,'missing','sync'),(None,'rejected','await'),('index',None,'await'),('hotbar',None,'await')])
        self.assertIn('пустым индексом',index[-1]['when'])
        self.assertEqual([x['step'] for x in steps['font-choice']['next']],['font','socket'])
        init=self.data.processes['proc-000016'];preload=next(s for s in init['steps'] if s['id']=='preload')
        self.assertEqual(preload['next'][0]['flow'],'sync')
        hooks=(ROOT/'module/setup/hooks.js').read_text();self.assertNotIn('await',hooks)
        self.assertIn('applyGeneralCombatHooks(combat);',hooks)
        self.assertIn('countdownDurationOfRegions(combat, update, options, userId);',hooks)
        self.assertTrue(all(e['flow']=='sync' for s in self.data.processes['proc-000022']['steps'] for e in s['next']))

    def test_all_new_processes_have_reachable_local_evidence(self):
        procs=[json.loads(l) for l in (BASE/'data/processes/expansion-006.jsonl').read_text().splitlines()]
        self.assertEqual(len(procs),9)
        for p in procs:
            steps={s['id']:s for s in p['steps']}; pending=[p['steps'][0]['id']];seen=set();exits=set()
            while pending:
                key=pending.pop()
                if key in seen:continue
                seen.add(key)
                for e in steps[key]['next']:
                    if 'step' in e:pending.append(e['step'])
                    else:exits.add(e['exit'])
            self.assertEqual(seen,set(steps));self.assertEqual(exits,{e['id'] for e in p['exits']})
            for s in steps.values():
                for rid in s['relations']:
                    r=self.data.relations[rid];self.assertEqual(r['location']['source'],s['location']['source'],(p['id'],s['id'],rid))
                    self.assertTrue(s['location']['line_start']<=r['location']['line_start']<=s['location']['line_end'],(p['id'],s['id'],rid))

    def test_coverage_counts_and_old_ids_are_preserved(self):
        # Fixed .006 counts describe its parts, not a ceiling for later expansions.
        historical = {kind: [json.loads(line)
                             for part in (f'examples/{kind}.jsonl', f'data/{kind}/pilot.jsonl',
                                          f'data/{kind}/expansion-006.jsonl')
                             for line in (BASE/part).read_text().splitlines()]
                      for kind in ('entities','relations','processes')}
        self.assertEqual([len(self.data.sources), *map(len, historical.values())], [615,636,1601,23])
        selected = [4,8,19,22,45,47,52,55,80,81,82,83,84,85,86,87,88,89,90,91,202,209,212,214,215,216,481]
        self.assertTrue({f'src-{n:06}' for n in selected} <= set(self.data.manifest['scope']['selected_sources']))
        represented = {e['location']['source'] for e in historical['entities']
                       if e['kind']!='boundary' and e.get('location')}
        self.assertEqual(len(represented),108)
        self.assertTrue(all(self.data.sources[s]['coverage']['definitions']['state']=='partial' for s in represented))
        self.assertEqual(self.data.sources['src-000209']['coverage']['definitions']['state'],'partial')
        self.assertTrue(all(f'ent-{n:06}' in self.data.entities for n in range(1,401)))
        self.assertTrue(all(f'rel-{n:06}' in self.data.relations for n in range(1,978)))
        self.assertTrue(all(f'proc-{n:06}' in self.data.processes for n in range(1,15)))
        # Distinct call sites may share endpoints; exact duplicate evidence is prohibited.
        keys=[(r['kind'],r['from'],r['to'],r['location']['source'],r['location']['line_start'], r.get('payload'), r.get('condition'), r.get('context')) for r in self.data.relations.values()]
        self.assertEqual(len(keys),len(set(keys)))

    def test_current_audit_refs_keep_late_corrections(self):
        requirements={'ent-000529':('r002-01','issue-00001.md'),
                      'ent-000328':('r002-02','issue-00005.md'),
                      'ent-000401':('r002-03','issue-00057.md'),
                      'ent-000586':('r002-05','issue-00002.md'),
                      'ent-000589':('r002-09','issue-00006.md')}
        for eid,(anchor,issue) in requirements.items():
            refs=self.data.entities[eid]['refs']
            self.assertTrue(any(r.get('anchor')==anchor for r in refs))
            self.assertTrue(any(r['path'].endswith(issue) for r in refs))
        prior=self.data.entities['ent-000319']['refs']
        self.assertTrue(any(r.get('anchor')=='уточнение-task-0003010' for r in prior))
        self.assertTrue(any(r.get('anchor')=='r005-03' for r in prior))
        issue2=(ROOT/'docs/issues/potential/issue-00002.md').read_text()
        self.assertIn('Пустой индекс сам по себе не вызывает отказа ready',issue2)
        self.assertIn('Статус potential сохранён',issue2)
