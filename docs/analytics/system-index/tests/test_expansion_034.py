"""Накопленная сверка справочника. Игровые сценарии и записи мира не исполняются."""
import collections
import json
import unittest
from test_query import BASE, ROOT, query, run_cli

class ThirdWaveCumulativeExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}
        cls.examples=json.loads((BASE/'examples/expansion-034-queries.json').read_text())
    def body(self,n,a=1,b=None):
        return '\n'.join((ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()[a-1:b])
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}
    def test_source_grounded_cli_cases(self):
        cases=self.examples['cases'];self.assertEqual(len(cases),44)
        self.assertEqual({c['question'] for c in cases},{f'IQ-{n:02}' for n in range(1,9)})
        for c in cases:
            with self.subTest(case=c['id']):
                run=run_cli([*c['command'],'--format','json'],cwd='/tmp');self.assertEqual(run.returncode,0,run.stderr)
                out=json.loads(run.stdout);rows=out['items'];first=rows[0]if rows else{}
                actual=dict(ids=[r['id']for r in rows if'id'in r],from_ids=sorted({r['from']for r in rows if'from'in r}),to_ids=sorted({r['to']for r in rows if'to'in r}),next_steps=[v['step']for v in first.get('next',[])if'step'in v],next_exits=[v['exit']for v in first.get('next',[])if'exit'in v],depth_limited=out.get('traversal',{}).get('depth_limited'),resolution=first.get('boundary',{}).get('kind'),refs=[v['path']for v in rows if'path'in v])
                for key,value in c['expected'].items():
                    if key.startswith('includes_'):self.assertTrue(set(value)<=set(actual[key[9:]]),(key,actual))
                    else:self.assertEqual(actual[key],value,key)
                self.assertEqual(out['freshness']['state'],'current');self.assertEqual(out['coverage']['state'],'partial')
    def test_all_ten_handoffs_have_source_witnesses_and_reverse_edges(self):
        groups=self.examples['handoffs'];self.assertEqual([g['id']for g in groups],[f'H{n:02}'for n in range(1,11)])
        self.assertEqual(sum(len(g['edges'])for g in groups),74)
        for g in groups:
            for w in g['edges']:
                with self.subTest(handoff=g['id'],witness=w):
                    self.assertIn(w['literal'],self.body(int(w['source'][4:]),w['line'],w['line']))
                    a,z=self.q[w['from_name']],self.q[w['to_name']]
                    edges=[r for r in self.data.outgoing[a]if r['to']==z and r['kind']==w['kind'] and r.get('location')and r['location']['source']==w['source']and r['location']['line_start']<=w['line']<=r['location']['line_end']]
                    self.assertTrue(edges)
                    for r in edges:self.assertIn(r,self.data.incoming[z])
                    for node in [a,z]:
                        e=self.data.entities[node]
                        if e['owner']is None:self.assertEqual(e['kind'],'boundary')
                        else:self.assertTrue(e['owner']in self.data.entities or e['owner']in self.data.sources)
    def test_independent_updates_do_not_become_transactions(self):
        b=self.body(166,32,53)
        for marker in ["this.item.update({ 'system.content': this.item.system.content })","item.update({ 'system.isStored': true })","item.update({ 'system.isStored': false })"]:self.assertIn(marker,b)
        self.assertNotIn('await ',b)
        for step in ['container','source']:self.assertEqual(self.steps(364)[step]['next'][0]['flow'],'scheduled')
        b=self.body(43,214,234);self.assertNotIn('await ',b)
        self.assertIn('this.actor.addItem',b)
        self.assertEqual(self.steps(379)['parent']['next'][0]['flow'],'scheduled')
        self.assertEqual(self.steps(379)['applied']['next'][0]['flow'],'scheduled')
        self.assertNotIn('await ',self.body(70,14,29));self.assertNotIn('await ',self.body(22,28,40))
        self.assertEqual(self.steps(452)['sta']['next'][0]['flow'],'scheduled')
        self.assertEqual(self.steps(452)['roll']['next'][0]['flow'],'await')
        self.assertIn('this.update({',self.body(11,131,133));self.assertNotIn('await ',self.body(11,131,133))
    def test_race_profession_and_builtin_skill_owners_remain_distinct(self):
        self.assertIn("actor.getList('race')[0]",self.body(29,151,166))
        self.assertIn('this.system.general.socialStanding',self.body(22,85,132))
        self.assertNotIn('race.system.socialStanding',self.body(22,85,132))
        self.assertIn('profession.system.definingSkill.skillName',self.body(20,381,399))
        self.assertNotIn('definingSkill',self.body(185,182,211))
        self.assertIn('system.skills.',self.body(22,35,39))
        self.assertNotEqual(self.q['professionSkill().level'],self.q['Skill.value'])
        outer=self.q['actor.skillMixin.levelUpSkill.magicalCost.outer'];inner=self.q['actor.skillMixin.levelUpSkill.magicalCost.inner'];self.assertNotEqual(outer,inner)
        self.assertIn('let magicalCost =',self.body(22,15,15));self.assertIn('let magicalCost =',self.body(22,21,21))
    def test_prepared_component_views_do_not_imply_cast_consumption(self):
        self.assertIn('this.ritualComponents = []',self.body(123,47,67))
        self.assertIn('fromUuidSync(component.uuid)',self.body(123,47,67))
        self.assertIn("this.item.update({ 'system.ritualComponentUuids': newComponentList })",self.body(177,45,57))
        cast=self.body(11,13,270)
        for key in ['ritualComponentUuids','alternateRitualComponentUuids','removeItem','deleteEmbeddedDocuments']:self.assertNotIn(key,cast)
        self.assertIn('spellItem.system.getUsedSkill()',cast)
        for field in ['RitualData.ritualComponentUuids','professionSkill().level']:
            scope='src-000011'if field.startswith('Ritual')else'src-000022'
            result=self.data.query(query.parser().parse_args(['field',self.q[field],'--access','writes','--scope',scope,'--no-verify']))
            self.assertEqual(result['items'],[]);self.assertEqual(result['coverage']['state'],'partial')
    def test_profession_payload_cast_and_region_have_separate_continuations(self):
        b=self.body(20,300,318);self.assertIn('new ActiveEffect',b);self.assertIn("function: 'applyActiveEffectToActor'",b);self.assertNotIn('await ',b)
        cast=self.body(11,247,269);self.assertLess(cast.index('createSpellRegion'),cast.index('if (!roll.options.fumble)'))
        self.assertIn('await roll.toMessage',cast)
        for step in ['region','status-self','ae-self','status-target','ae-target']:self.assertEqual(self.steps(451)[step]['next'][0]['flow'],'scheduled')
        launch=self.steps(456)['launch']['next'];self.assertEqual(launch[0]['exit'],'done');self.assertEqual(launch[1]['flow'],'scheduled')
        q=self.body(213,15,46);self.assertIn('entity.system[queryData.function]',q);self.assertNotIn('entity.system.regionProperties',q)
        timer=self.body(117,168,175);self.assertIn('canvas.scene.deleteEmbeddedDocuments',timer);self.assertNotIn('await ',timer)
        combat=self.body(200);self.assertIn('game.scenes.active',combat);self.assertNotIn('update.turn',combat);self.assertNotIn('update.round',combat)
        self.assertEqual(self.data.entities['ent-005301']['boundary']['kind'],'external')
    def test_all_source_facets_roles_and_counts_are_recounted(self):
        d=self.data;self.assertEqual([len(d.sources),len(d.entities),len(d.relations),len(d.processes)],[615,5328,14954,465])
        expected={'definitions':{'complete':2,'partial':303,'not_indexed':310},'relations':{'partial':309,'not_indexed':306},'processes':{'partial':160,'not_indexed':455}}
        for key,value in expected.items():self.assertEqual(collections.Counter(s['coverage'][key]['state']for s in d.sources.values()),value)
        inv=json.loads((BASE/'expansion-inventory.json').read_text());files=[f for b in inv['blocks']for f in b['files']]
        self.assertEqual(len(files),615);self.assertEqual(collections.Counter(f['current_role']for f in files),{'primary':232,'neighbor':73,'catalog_only':310})
        for s in d.sources.values():
            for v in s['coverage'].values():
                if v['included']:self.assertFalse(any('ещё не индексированы.'in x for x in v['remaining']),(s['id'],v))
        self.assertEqual(sum(len(p['steps'])for p in d.processes.values()),1537)
        self.assertEqual(sum(len(s['next'])for p in d.processes.values()for s in p['steps']),2918)
    def test_item_header_partial_scope_matches_existing_bindings(self):
        s=self.data.sources['src-000532'];self.assertEqual(s['coverage']['definitions']['included'],['ent-004695'])
        self.assertEqual(len(s['coverage']['relations']['included']),5)
        self.assertEqual(s['coverage']['processes']['state'],'not_indexed')
        h=self.body(532)
        for key in ['system.quantity','system.weight','system.cost','system.sourcebook','system.clickableImage']:self.assertIn('name="'+key+'"',h)
        self.assertTrue(all(s['coverage'][k]['state']=='partial'for k in ['definitions','relations']))
        self.assertFalse(any('expansion-034.jsonl'in p for ps in self.data.manifest['parts'].values()for p in ps))

if __name__=='__main__':unittest.main()
