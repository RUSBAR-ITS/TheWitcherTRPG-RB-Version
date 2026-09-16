"""Справочник документов: проверки по JS/ядру; JS и сохранение мира не исполняются."""
import collections
import hashlib
import json
import re
from pathlib import Path
import unittest
import tempfile
from test_query import BASE, ROOT, query, run_cli, save_pre_resource_forms_view

class CumulativeExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.history_dir=tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.history_dir.cleanup)
        cls.history_manifest=save_pre_resource_forms_view(Path(cls.history_dir.name))
        cls.historical=query.Dataset(cls.history_manifest)
        cls.q={e['qualified_name']:e['id'] for e in cls.data.entities.values()}

    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]] if r['kind']==kind]
    def steps(self,n):return {s['id']:s for s in self.data.processes[f'proc-{n:06}']['steps']}

    def test_35_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-023-queries.json').read_text())['cases']
        self.assertEqual(len(cases),35)
        self.assertEqual({c['question'] for c in cases},{f'IQ-{n:02}' for n in range(1,9)})
        for c in cases:
            with self.subTest(case=c['id']):
                # JOIN-16 repeats INV-06; .026 adds the stack writer. Its current
                # answer is checked in .013 and the .026 callback source proof.
                prefix=['--dataset',str(self.history_manifest)] if c['id'] in {'JOIN-16','JOIN-21'} else []
                run=run_cli([*prefix,*c['command'],'--format','json'],cwd='/tmp')
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


    def test_twelve_handoffs_have_source_witnesses_in_both_directions(self):
        groups=json.loads((BASE/'examples/expansion-023-queries.json').read_text())['handoffs']
        self.assertEqual([g['id']for g in groups],[f'H{n:02}'for n in range(1,13)])
        for g in groups:
            for e in g['edges']:
                with self.subTest(handoff=g['id'],edge=e):
                    self.assertIn(e['literal'],self.source(int(e['source'][4:]))[e['line']-1])
                    a,b=self.q[e['from_name']],self.q[e['to_name']]
                    edges=[r for r in self.data.outgoing[a]if r['to']==b and r['kind']==e['kind'] and r.get('location',{}).get('source')==e['source'] and r['location']['line_start']==e['line']]
                    self.assertTrue(edges)
                    for r in edges:self.assertIn(r,self.data.incoming[b])
                    for node in [a,b]:
                        entity=self.data.entities[node]
                        if entity['owner'] is None:self.assertEqual(entity['kind'],'boundary')
                        else:self.assertTrue(entity['owner'] in self.data.sources or entity['owner'] in self.data.entities)

    def test_prepared_payload_and_typed_chat_are_distinct(self):
        weapon=self.source(25);self.assertIn('damage.properties.toObject(false)',weapon[176])
        # Source addresses are resolved from the catalogue, not inferred from CLI results.
        src={s['path']:s['id']for s in self.data.sources.values()}
        def body(path):return '\n'.join(self.source(int(src[path][4:])))
        damage=body('module/data/chatMessage/damageMessageData.js')
        container=body('module/data/chatMessage/templates/damageData.js')
        self.assertIn('new fields.SchemaField',damage);self.assertIn('effects: new fields.ArrayField',damage)
        self.assertIn('new fields.EmbeddedDataField(DamageProperties)',container)
        self.assertNotIn('duration:',container)
        util=body('module/item/mixins/damageUtilMixin.js')
        self.assertIn('damage.properties.getPreprocessedEffects()',util)
        boundary=self.data.entities[self.q['weaponAttack/rollOnlyDmg-properties']]
        self.assertEqual(boundary['boundary']['kind'],'dynamic')
        self.assertTrue(any(r['path'].endswith('issue-00297.md')for r in boundary['refs']))

    def test_async_consume_and_rest_do_not_claim_persistence(self):
        a=self.source(47);c=self.source(157);h=self.source(42)
        for at in [239,240]:self.assertNotIn('await',a[at-1])
        self.assertIn('consume()',a[238]);self.assertIn('removeItem',a[239])
        self.assertIn('await this.actor.calculateHealValue',c[7]);self.assertNotIn('await',c[8])
        self.assertIn('await this.actor.update',h[78]);self.assertIn('forEach',h[87]);self.assertNotIn('await',h[87])
        self.assertEqual(self.steps(149)['hp']['next'][0]['flow'],'scheduled')
        self.assertEqual(self.steps(340)['resources']['next'][0]['flow'],'await')
        self.assertEqual(self.steps(340)['wounds']['next'][0]['flow'],'scheduled')

    def test_armor_resources_source_and_display_have_different_roles(self):
        a=self.source(14);armor=self.source(108)
        self.assertIn('locationArmor.totalSP',a[154]);self.assertIn('locationArmor.displaySP',a[155])
        self.assertIn('applyAlwaysSpDamage',a[187]);self.assertIn('applySpDamage',a[235])
        self.assertIn('this.parent.update',armor[76]);self.assertNotIn('await',armor[76])
        self.assertIn('stoppingPower',armor[77]);self.assertNotIn('modifiedStoppingPower',armor[77])
        self.assertIn('JSON.parse(change.value)',a[129]);self.assertIn('await tempHp.update',a[139])
        # Resource update is later than effect handling; the graph does not guarantee it runs past an earlier throw.
        self.assertIn('await this.update',a[143])

    def test_trauma_form_empty_writer_and_followup_boundary(self):
        a=self.source(112);form='\n'.join(self.source(599))
        self.assertIn('name="system.treatment"',form)
        self.assertFalse([r for r in self.data.incoming[self.q['CriticalWoundData.treatment']]if r['kind']=='writes' and r['location']['source']=='src-000112'])
        self.assertIn('await fromUuid',a[96]);self.assertNotIn('await',a[97]);self.assertNotIn('await',a[100])
        self.assertEqual([n['step']for n in self.steps(323)['link']['next']if 'step'in n],['load','delete'])
        self.assertEqual(self.data.entities[self.q['criticalWound/form-submit']]['boundary']['kind'],'dynamic')

    def test_combat_damage_heal_and_chat_are_separate_entries(self):
        s=self.source(196);hooks=self.source(212)
        self.assertIn('game.user.isActiveGM',s[3]);self.assertNotIn('await',s[6]);self.assertNotIn('await',s[7])
        self.assertIn("Hooks.on('updateCombat'",hooks[4]);self.assertNotIn('changed','\n'.join(hooks))
        self.assertNotIn('type:', '\n'.join(s[61:72]))
        output=self.steps(180)['output'];self.assertEqual([n['step']for n in output['next']if 'step'in n],['direct','message'])
        self.assertEqual([s['id']for s in self.data.processes['proc-000309']['steps']],['gm','actor','regeneration','periodic'])
        # Death roll does not write HP or dead automatically; only the user-facing result is rolled.
        death='\n'.join(self.source(41)[15:43]);self.assertNotIn('.update(',death);self.assertIn('extendedRoll',death)

    def test_catalogue_facets_roles_and_useful_empty_results(self):
        d=self.historical
        self.assertEqual([len(d.sources),len(d.entities),len(d.relations),len(d.processes)],[615,4579,11808,353])
        expected={'definitions':{'complete':2,'partial':250,'not_indexed':363},'relations':{'partial':257,'not_indexed':358},'processes':{'partial':112,'not_indexed':503}}
        for facet,counts in expected.items():self.assertEqual(collections.Counter(s['coverage'][facet]['state']for s in d.sources.values()),counts)
        stat=d.sources['src-000090']['coverage']['processes'];self.assertEqual(stat['state'],'not_indexed');self.assertEqual(stat['included'],[])
        self.assertTrue(d.query(query.parser().parse_args(['processes',self.q['stat().value'],'--no-verify']))['items'])
        sidebar='\n'.join(self.source(560));self.assertIn("name='system.derivedStats.hp.value'",sidebar)
        empty=d.query(query.parser().parse_args(['field',self.q['DerivedStats.hp'],'--access','writes','--scope','src-000560','--no-verify']))
        self.assertEqual(empty['items'],[]);self.assertEqual(empty['coverage']['state'],'partial')
        for s in d.sources.values():
            for v in s['coverage'].values():
                if v['included']:self.assertFalse(any('ещё не индексированы.'in x for x in v['remaining']))

    def test_cumulative_owners_locations_facets_and_process_links(self):
        d=self.data;lengths={sid:len((ROOT/s['path']).read_text().splitlines())for sid,s in d.sources.items()}
        facets={sid:{k:set()for k in ['definitions','relations','processes']}for sid in d.sources}
        for e in d.entities.values():
            if e['location']:
                loc=e['location'];self.assertLessEqual(loc['line_end'],lengths[loc['source']])
                if e['kind']!='boundary':facets[loc['source']]['definitions'].add(e['id'])
            if e['kind']!='boundary':
                defs=[r for r in d.incoming[e['id']]if r['kind']=='defines'];self.assertEqual(len(defs),1,e['id'])
                definer=defs[0]['from']
                if definer!=e['owner']:
                    # Structural owner is the model/container; defineSchema can be the declaring method.
                    declaration=d.entities[definer];self.assertIn(declaration['name'],['defineSchema','constructor'])
                    chain=[];owner=e['owner']
                    while owner in d.entities:
                        self.assertNotIn(owner,chain);chain.append(owner);owner=d.entities[owner]['owner']
                    self.assertIn(declaration['owner'],chain)
                    self.assertEqual(declaration['location']['source'],e['location']['source'])
        for r in d.relations.values():
            self.assertIn(r,d.incoming[r['to']]);self.assertIn(r,d.outgoing[r['from']])
            if r.get('location'):facets[r['location']['source']]['relations'].add(r['id'])
        for p in d.processes.values():
            steps={s['id']:s for s in p['steps']};todo=[p['steps'][0]['id']];seen=set();exits=set()
            while todo:
                n=todo.pop()
                if n in seen:continue
                seen.add(n)
                for nxt in steps[n]['next']:
                    if 'step'in nxt:todo.append(nxt['step'])
                    else:exits.add(nxt['exit'])
            self.assertEqual(seen,set(steps),p['id']);self.assertEqual(exits,{e['id']for e in p['exits']},p['id'])
            for s in steps.values():
                facets[s['location']['source']]['processes'].add(p['id'])
                for rid in s['relations']:
                    # format v1 permits a step to name the callee or aggregate local actions.
                    r=d.relations[rid];self.assertEqual(r['location']['source'],s['location']['source']);self.assertTrue(s['location']['line_start']<=r['location']['line_start']<=s['location']['line_end'])
        for sid,v in facets.items():
            for k,ids in v.items():self.assertEqual(ids,set(d.sources[sid]['coverage'][k]['included']),(sid,k))

if __name__=='__main__':unittest.main()
