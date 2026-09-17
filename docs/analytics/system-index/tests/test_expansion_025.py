"""Проверки справочника по исходникам; игровые документы и БД не исполняются."""
import collections
import hashlib
import json
import re
import unittest
from pathlib import Path
from test_query import BASE, ROOT, query, run_cli

class ContainerExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l)for l in(BASE/f'data/{k}/expansion-025.jsonl').read_text().splitlines()]for k in ['entities','relations','processes']}
    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]]if r['kind']==kind]
    def test_27_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-025-queries.json').read_text())['cases']
        self.assertEqual(len(cases),27)
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

    def test_schema_projection_and_uuid_have_distinct_owners(self):
        model='\n'.join(self.source(111)); helper='\n'.join(self.source(619))
        self.assertIn('content: new fields.ArrayField(new fields.StringField())',model)
        self.assertIn('templateContent: new fields.ObjectField',model)
        self.assertIn('validateTemplate(value)',model)
        for q,owner in [('ContainerData.content','ContainerData'),('ContainerData.itemContent','ContainerData'),('ContainerData.itemContent[].uuid','ContainerData.itemContent')]:
            self.assertEqual(self.data.entities[self.q[q]]['owner'],self.q[owner])
        self.assertIn('missing: false',helper);self.assertIn('sourceUuid: item.uuid',helper)
        self.assertNotIn('fromUuidSync',model)

    def test_drop_uses_verified_service_and_preserves_native_dispatch(self):
        sheet='\n'.join(self.source(166));ops='\n'.join(self.source(618));helper='\n'.join(self.source(619))
        self.assertIn('return runContainerAction(() => storeItem',sheet)
        self.assertIn('witcherContainer: this.item.uuid',sheet)
        self.assertIn('const actorMove = !!source.parent && !source.pack && !!owner',ops)
        self.assertIn('if (move && (source.parent ?? null) === owner) return relocate(source, target)',ops)
        self.assertIn('await deleteTrees([source]',ops)
        self.assertNotIn('this.item.system.content.push',sheet)
        self.assertEqual({e['to'] for e in self.edges('WitcherContainerSheet._onDropItem','calls')}, {self.q['containerOperations.storeItem'],self.q['containerOperations.runContainerAction']})
        self.assertIn('return (await this._onDropItem(event, document)) ?? null','\n'.join(self.source(172)))
        self.assertIn('STORABLE_TYPES = new Set',helper)

    def test_remove_nonmember_and_external_link_do_not_update_other_item(self):
        ops='\n'.join(self.source(618));body=ops[ops.index('export async function extractItem'):]
        self.assertIn('if (!contentOf(container).includes(uuid)) return null',body)
        self.assertIn('if (!item || !sameOwner(item, container) || item.visible === false)',body)
        self.assertNotIn('fromUuid',body)
        self.assertIn('await writePatches',body);self.assertIn('return relocate(item, null)',body)
        self.assertFalse(self.edges('WitcherContainerSheet._onRemoveItem','writes'))
        self.assertIn(self.q['ContainerData.content'],{r['to'] for r in self.edges('containerOperations.extractItem','writes')})

    def test_weight_traverses_tree_and_capacity_stays_separate(self):
        model='\n'.join(self.source(111));helper='\n'.join(self.source(619))
        self.assertIn('this.quantity * this.weight + contents.weight',model)
        self.assertIn('this.isCarried && !this.isStored',model)
        self.assertNotIn('this.carry',model)
        self.assertIn('queue.push(...contentOf(item)',helper)
        self.assertIn('seen.has(uuid)',helper)
        self.assertIn('item.system.calcWeight?.() ?? 0','\n'.join(self.source(47)))
        self.assertEqual({r['to'] for r in self.edges('ContainerData.calcWeight','calls')},{self.q['containerTemplates.describeContainer']})
        self.assertFalse([r for r in self.data.incoming[self.q['ContainerData.storedWeight']] if r['kind']=='reads' and r['location']['source']=='src-000111'])

    def test_visibility_category_templates_and_context_menu_target(self):
        for n,a in [(27,72),(28,37)]:self.assertIn('filter(i => !i.system.isStored).sort','\n'.join(self.source(n)))
        getlist='\n'.join(self.source(47)[249:257]);self.assertNotIn('isStored',getlist.split('return this.items.filter')[0]);self.assertIn('!i.system.isStored',getlist)
        self.assertIn("i.system.type == 'clothing' || i.system.type == 'containers'",'\n'.join(self.source(29)))
        self.assertIn('this._prepareValuables(context)','\n'.join(self.source(29)))
        self.assertIn(self.q['WitcherCharacterSheet._prepareValuables'],{r['to']for r in self.edges('WitcherCharacterSheet._prepareContext','calls')})
        inv='\n'.join(self.source(576));self.assertIn('valuables=clothingAndContainers',inv);self.assertIn('valuables=containers',inv)
        rows='\n'.join(self.source(558));self.assertIn("(eq valuable.type 'container')",rows)
        self.assertIn('<details class="stored-item" data-item-id="{{storedItem.uuid}}">',rows)
        self.assertNotIn('remove-item',rows)
        current='\n'.join(self.source(571));self.assertIn('valuables=loots',current);self.assertNotIn('containers',current)
        self.assertIn('partials/monster/tabs/tab-inventory.hbs','\n'.join(self.source(31)))
        self.assertIn('partials/monster/monster-inventory-tab.hbs','\n'.join(self.source(550)))

    def test_loot_additem_unchanged_and_delete_intercepts_document_entry(self):
        actor='\n'.join(self.source(47));item='\n'.join(self.source(192));mixin='\n'.join(self.source(43))
        self.assertIn('!foundItem.system.isStored',actor)
        self.assertIn('static async deleteDocuments',item);self.assertIn('return deleteContainerDocuments',item)
        self.assertIn('return runContainerAction',mixin)
        ops='\n'.join(self.source(618));self.assertIn('DialogV2.confirm',ops)
        self.assertIn('if (!yes) return []',ops);self.assertIn('missing.map(entry => entry.data)',ops)
        self.assertIn('sourceIntact',ops)
        self.assertIn('clone(data = {}, context = {})',item)

    def test_core_evidence_hashes_and_specific_contracts(self):
        evidence=json.loads((BASE/'examples/expansion-025-queries.json').read_text())['core_evidence']
        for x in evidence:self.assertEqual(hashlib.sha256(Path(x['path']).read_bytes()).hexdigest(),x['sha256'])
        helpers=Path('/opt/foundryvtt/client/utils/helpers.mjs').read_text();start=helpers.index('export function fromUuidSync');body=helpers[start:helpers.index('/* -------------------------------------------- */',start)]
        self.assertIn('collection.index.get(baseId)',body);self.assertIn('strict=true',body);self.assertIn('return doc || null',body)
        self.assertIn('_onDelete(options, userId) {}',Path('/opt/foundryvtt/common/abstract/type-data.mjs').read_text())
        self.assertIn('item.callback(this.#jQuery ? $(this.#target) : this.#target, event)',Path('/opt/foundryvtt/client/applications/ux/context-menu.mjs').read_text())

    def test_graph_addresses_reverse_edges_facets_and_processes(self):
        d=self.data
        for e in self.new['entities']:
            if e['kind']=='boundary':continue
            defs=[r for r in d.incoming[e['id']]if r['kind']=='defines'];self.assertEqual(len(defs),1);self.assertEqual(defs[0]['from'],e['owner'])
            l=e['location'];self.assertLessEqual(l['line_end'],len(self.source(int(l['source'][4:]))))
            self.assertIn(e['id'],d.sources[l['source']]['coverage']['definitions']['included'])
        for r in self.new['relations']:
            self.assertIn(r,d.outgoing[r['from']]);self.assertIn(r,d.incoming[r['to']]);l=r['location'];self.assertLessEqual(l['line_end'],len(self.source(int(l['source'][4:]))))
            self.assertIn(r['id'],d.sources[l['source']]['coverage']['relations']['included'])
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
        # Historical portion counts, not a cap on later extensions.
        self.assertEqual(len(self.new['processes']),10)
        self.assertEqual(len(self.new['entities']),36)
        self.assertTrue(set(r['id'] for r in self.new['relations']).isdisjoint(d.manifest['retired_ids']))

if __name__=='__main__':unittest.main()
