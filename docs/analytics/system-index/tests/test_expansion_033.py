"""Проверки справочника по исходникам; игровые документы и БД не исполняются."""
import collections
import hashlib
import json
import re
import unittest
from pathlib import Path
from test_query import BASE, ROOT, query, run_cli

class MagicRegionExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l)for l in(BASE/f'data/{k}/expansion-033.jsonl').read_text().splitlines()]for k in ['entities','relations','processes']}
    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]]if r['kind']==kind]
    def test_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-033-queries.json').read_text())['cases']
        self.assertEqual(len(cases),42)
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
    def test_schema_fields_form_and_migration(self):
        h=self.body(596);s=self.body(149)
        self.assertEqual(h.count('{{formGroup'),5)
        for key in ['tokenEnter','tokenTurnStart','tokenMoveWithin','tokenExit']:
            self.assertIn(key+': new fields.DocumentUUIDField',s);self.assertIn('value=item.system.regionProperties.behaviours.'+key,h)
        self.assertIn("label: 'WITCHER.Item.RegionProperties.tokenPreMove'",s)
        self.assertIn('createRegionFromTemplate',h);self.assertNotIn('createRegionFromTemplate',self.body(150))
        self.assertIn('if (!system.createTemplate) delete parts.regionProperties',self.body(186,68,78))
        b=self.body(150,51,55);self.assertIn('source.behaviours.tokenMoveWithin = source.behaviours.tokenPreMove',b);self.assertNotIn('if (',b)
        self.assertIn(self.q['regionBehaviours().tokenMoveWithin'],self.targets('RegionProperties.migrateData','writes'))
    def test_geometry_and_raw_payload_options(self):
        b=self.body(117,23,115)
        for k in ['circle','cone','rect','ray','emanation']:self.assertIn("case '"+k+"'",b)
        self.assertIn('templateSize * grid.size) / grid.distance',b)
        for key in ['roll','item','itemUuid','duration','actorUuid','options']:self.assertIn(key+':',b)
        self.assertIn('flagOptions = {}',b);self.assertIn('options: flagOptions',b);self.assertIn('duration: damage?.duration',b)
        self.assertIn('{ roll, damage, options }',self.body(117,8,8));self.assertIn('{ stamina: origStaCost }',self.body(11,250,250))
        self.assertIn(self.q['actor.castSpellMixin.castSpell/rawDamage.duration'],self.targets('spellRegionMixin.fromItem','reads'))
        self.assertEqual(self.data.entities[self.q['magic-cast/region-options-handoff']]['id'],'ent-005244')
    def test_manual_and_emanation_return_contracts(self):
        b=self.body(117,117,140)
        self.assertIn('Promise.all(this.drawPreview(regionData))',b);self.assertIn('token.scene !== game.user.viewedScene',b)
        self.assertIn('item.system.templateProperties.templateSize / 2 / grid.distance',b);self.assertIn('region.item = item',b)
        self.assertNotIn('.filter(Boolean)',b)
        self.assertIn('canvas.regions.placeRegion(regionData, { create: true })',self.body(117,142,157))
        st={s['id']:s for s in self.process('fromItem: ручное размещение или эманации')['steps']}
        self.assertEqual([n['step']for n in st['branch']['next']],['tokens','manual'])
        self.assertEqual(st['manual']['next'][0]['exit'],'failed');self.assertFalse(any('step'in n for n in st['manual']['next']))
    def test_async_boundaries_are_not_document_completion(self):
        b=self.body(117,2,17);self.assertNotIn('return this.fromItem',b);self.assertNotIn('await this.fromItem',b);self.assertIn('.catch(() => {})',b)
        self.assertIn('await this.regionProperties.addBehaviorsToRegions(regions)',b)
        for a,z in [(12,14),(16,37)]:self.assertNotIn('await ',self.body(150,a,z))
        self.assertIn('region.update({',self.body(150,26,37));self.assertNotIn('await ',self.body(200))
        p=self.process('createSpellRegion: раннее завершение и независимая цепочка');st={s['id']:s for s in p['steps']}
        self.assertEqual(st['launch']['next'][0]['exit'],'done');self.assertEqual(st['launch']['next'][1]['flow'],'scheduled')
        self.assertIn(self.q['RegionProperties.addBehaviorsToRegions'],self.targets('spellRegionMixin.createSpellRegion/behaviors-continuation','calls'))
    def test_behavior_payload_and_uuid_route_depth(self):
        b=self.body(150,39,48)
        for marker in ["type: 'executeMacro'",'events: [event]','uuid: uuid']:self.assertIn(marker,b)
        self.assertNotIn('execute(',b);self.assertNotIn('everyone',b);self.assertNotIn('_id',b)
        self.assertIn('fromUuidSync(uuid)',self.body(150,12,14))
        q=self.body(213);self.assertIn("'addBehaviorsToRegionUuids'",q);self.assertNotIn("'deleteSpellVisualEffect'",q)
        for marker in ['entity[queryData.function]?.(...queryData.data)','entity.system[queryData.function]?.(...queryData.data)']:self.assertIn(marker,q)
        self.assertNotIn('entity.system.regionProperties',q)
        self.assertNotIn(self.q['RegionProperties.addBehaviorsToRegionUuids'],self.targets('query','calls'))
        self.assertIn(self.q['query/nested-region-target'],self.targets('query','refers'))
        self.assertEqual(self.data.entities[self.q['query/nested-region-target']]['id'],'ent-004468')
    def test_visual_timer_scene_and_remote_failure(self):
        b=self.body(117,159,175)
        self.assertIn('uuid: item.uuid',b);self.assertNotRegex(b,r'\b(?:const|let|var)\s+item\b')
        self.assertIn('this.templateProperties.visualEffectDuration * 1000',b)
        self.assertIn("canvas.scene.deleteEmbeddedDocuments('Region', [region.id])",b)
        self.assertNotIn('region.parent',b);self.assertNotIn('await ',b);self.assertNotIn('return',b)
        self.assertNotIn("flags['TheWitcherTRPG-RB-Version'].duration",b)
        self.assertIn(self.q['Scene.deleteEmbeddedDocuments/Region'],self.targets('spellRegionMixin.deleteSpellVisualEffect/timeout','calls'))
    def test_countdown_uses_active_scene_and_arbitrary_update(self):
        b=self.body(200)
        for marker in ['if (!game.user.isActiveGM) return','combat.combatants.get(combat.current.combatantId).actor.uuid','game.scenes.active.regions',"region.flags['TheWitcherTRPG-RB-Version']?.actorUuid === actorUuid","region.flags['TheWitcherTRPG-RB-Version'].duration - 1 > 0","game.scenes.active.deleteEmbeddedDocuments('Region', toDelete)"]:self.assertIn(marker,b)
        for marker in ['update.turn','update.round','combat.scene','Number.isFinite','visualEffectDuration','await ']:self.assertNotIn(marker,b)
        self.assertEqual(b.count('update'),1)
        h=self.body(212);self.assertIn("Hooks.on('updateCombat'",h);self.assertNotIn('await ',h)
        self.assertIn(self.q['spellRegionMixin.fromItem.regionData.flags.TheWitcherTRPG-RB-Version.duration'],self.targets('countdownDurationOfRegions','writes'))
        self.assertIn(self.q['countdownDurationOfRegions'],self.targets('combatHooks','calls'))
    def test_external_evidence_and_primary_partial_scope(self):
        ex=json.loads((BASE/'examples/expansion-033-queries.json').read_text());self.assertEqual(len(ex['core_evidence']),10)
        for v in ex['core_evidence']:self.assertEqual(hashlib.sha256(Path(v['path']).read_bytes()).hexdigest(),v['sha256'])
        for n in [117,149,150,151,200,596,213,212]:self.assertEqual(self.data.sources[f'src-{n:06}']['coverage']['definitions']['state'],'partial')
        e=self.data.entities[self.q['Foundry.executeMacroRegionBehavior']];self.assertEqual(e['boundary']['kind'],'external');self.assertIsNone(e['location'])
        self.assertEqual(self.data.entities[self.q['RegionProperties']]['id'],'ent-004457')
        self.assertEqual(self.data.entities[self.q['spellRegionMixin.fromItem']]['location']['line_end'],140)
    def process(self,name):return next(p for p in self.new['processes']if p['name']==name)
    def test_graph_addresses_facets_and_reachable_processes(self):
        d=self.data
        for e in self.new['entities']:
            if e['kind']=='boundary':continue
            defs=[r for r in d.incoming[e['id']]if r['kind']=='defines'];self.assertEqual(len(defs),1);self.assertEqual(defs[0]['from'],e['owner'])
            l=e['location'];self.assertLessEqual(l['line_end'],len(self.source(int(l['source'][4:]))));self.assertIn(e['id'],d.sources[l['source']]['coverage']['definitions']['included'])
        for r in self.new['relations']:
            self.assertIn(r,d.outgoing[r['from']]);self.assertIn(r,d.incoming[r['to']]);l=r['location'];self.assertLessEqual(l['line_end'],len(self.source(int(l['source'][4:]))));self.assertIn(r['id'],d.sources[l['source']]['coverage']['relations']['included'])
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
        self.assertEqual({k:len(v)for k,v in self.new.items()},{'entities':84,'relations':195,'processes':12})

if __name__=='__main__':unittest.main()
