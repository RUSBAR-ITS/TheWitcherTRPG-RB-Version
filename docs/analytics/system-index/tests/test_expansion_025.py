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
        model='\n'.join(self.source(111));common='\n'.join(self.source(109))
        self.assertIn('content: new fields.ArrayField(new fields.StringField())',model)
        self.assertIn("quantity: new fields.StringField({ initial: '1' })",common)
        for q,owner in [('ContainerData.content','ContainerData'),('ContainerData.itemContent','ContainerData'),('ContainerData.itemContent[].uuid','ContainerData.itemContent'),('CommonItemData.isStored','CommonItemData'),('ValuableData.type','ValuableData')]:
            self.assertEqual(self.data.entities[self.q[q]]['owner'],self.q[owner])
        self.assertNotIn('itemContent:',model[:model.index('calcWeight()')])
        self.assertIn('uuid: itemId',model)

    def test_drop_guard_and_two_independent_requests(self):
        text='\n'.join(self.source(166));guard=text[text.index('async _onDropItem'):text.index('_onRemoveItem(event)')]
        types=re.findall(r"'([a-z]+)'",text[text.index('storableItems'):text.index('static PARTS')])
        self.assertEqual(types,['weapon','armor','enhancement','valuable','alchemical','component','diagrams','mutagen','container'])
        for absent in ['await ','return ','isOwner','carry','createEmbeddedDocuments','parent']:
            self.assertNotIn(absent,guard)
        self.assertNotIn('isStored',guard.split('this.item.system.content.push')[0])
        self.assertIn('!this.item.system.content.includes(item.uuid)',guard)
        self.assertLess(guard.index('content.push'),guard.index('this.item.update'))
        self.assertLess(guard.index('this.item.update'),guard.index('item.update({ \'system.isStored\''))
        edges=self.edges('WitcherContainerSheet._onDropItem','calls')
        self.assertEqual([(e['location']['line_start'],e['to'])for e in edges],[(35,self.q['Document.update/Item']),(36,self.q['Document.update/Item'])])
        dispatcher='\n'.join(self.source(172)[122:135]);self.assertIn('(await this._onDropItem(event, document)) ?? null',dispatcher)

    def test_remove_nonmember_and_failure_order(self):
        text='\n'.join(self.source(166)[39:53])
        for literal in ['index > -1','splice(index, 1)','fromUuidSync(uuid)',"'system.isStored': false"]:self.assertIn(literal,text)
        self.assertNotIn('await ',text);self.assertNotIn('return',text)
        self.assertLess(text.index('splice'),text.index('fromUuidSync'))
        self.assertLess(text.index('fromUuidSync'),text.index('this.item.update'))
        self.assertLess(text.index('this.item.update'),text.index("item.update({ 'system.isStored'"))
        writes={e['to']for e in self.edges('WitcherContainerSheet._onRemoveItem','writes')}
        self.assertEqual(writes,{self.q['ContainerData.content'],self.q['CommonItemData.isStored']})

    def test_weight_is_direct_prepared_and_capacity_separate(self):
        model='\n'.join(self.source(111));body=model[model.index('prepareDerivedData()'):]
        self.assertIn('this.storedWeight = 0',body);self.assertIn('this.storedWeight += item.system.quantity * item.system.weight',body)
        for absent in ['item.system.storedWeight','item.system.calcWeight','item.system.isStored','item.system.isCarried','this.carry']:self.assertNotIn(absent,body)
        self.assertIn('this.quantity * this.weight + this.storedWeight',model)
        actor='\n'.join(self.source(47));self.assertIn('item.system.calcWeight?.() ?? 0',actor);self.assertIn('Math.ceil(total + this.system.calcCurrencyWeight())',actor)
        enc='\n'.join(self.source(47)[108:121]);self.assertIn('(this.system.stats.body.max + bodyTotalModifiers) * 10 + this.system.derivedStats.enc.totalModifiers',enc)
        self.assertIn('Math.ceil((totalWeights - currentEncumbrance) / 5)',enc)
        readers=[r for r in self.data.incoming[self.q['ContainerData.storedWeight']]if r['kind']=='reads'and r['location']['source']=='src-000111']
        self.assertEqual({r['from']for r in readers},{self.q['ContainerData.calcWeight']})

    def test_visibility_category_templates_and_context_menu_target(self):
        for n,a in [(27,72),(28,37)]:self.assertIn('filter(i => !i.system.isStored).sort',self.source(n)[a-1])
        getlist='\n'.join(self.source(47)[249:257]);self.assertNotIn('isStored',getlist.split('return this.items.filter')[0]);self.assertIn('!i.system.isStored',getlist)
        self.assertIn("i.system.type == 'clothing' || i.system.type == 'containers'",self.source(29)[244])
        self.assertIn('this._prepareValuables(context)',self.source(29)[129])
        self.assertIn(self.q['WitcherCharacterSheet._prepareValuables'],{r['to']for r in self.edges('WitcherCharacterSheet._prepareContext','calls')})
        inv='\n'.join(self.source(576));self.assertIn('valuables=clothingAndContainers',inv);self.assertIn('valuables=containers',inv)
        rows='\n'.join(self.source(558));self.assertIn("(eq valuable.type 'container')",rows)
        self.assertIn('<details class="stored-item" data-item-id="{{storedItem.uuid}}">',rows)
        self.assertNotIn('remove-item',rows)
        current='\n'.join(self.source(571));self.assertIn('valuables=loots',current);self.assertNotIn('containers',current)
        self.assertIn('partials/monster/tabs/tab-inventory.hbs',self.source(31)[44])
        self.assertIn('partials/monster/monster-inventory-tab.hbs',self.source(550)[295])

    def test_loot_inline_additem_and_delete_boundaries(self):
        loot='\n'.join(self.source(30)[42:66]);self.assertIn("getList('container')",loot);self.assertIn("getList('mutagen')",loot)
        row='\n'.join(self.source(563));self.assertIn('data-item-id="{{item._id}}"',row);self.assertIn('data-field="system.weight"',row)
        add='\n'.join(self.source(47)[258:273]);self.assertIn('!foundItem.system.isStored',add);self.assertNotIn('isStored =',add)
        deleted='\n'.join(self.source(43)[174:180]);self.assertNotIn('await ',deleted);self.assertNotIn('isStored',deleted)
        for n in [111,109,192]:self.assertNotRegex('\n'.join(self.source(n)),r'\b_onDelete\s*\(')
        gift='\n'.join(self.source(34)[98:115]);self.assertNotIn("'container'",gift)
        self.assertIn('callback: this.giftItem.bind(this)', '\n'.join(self.source(34)))

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
        self.assertEqual({k:len(v)for k,v in self.new.items()},{'entities':36,'relations':134,'processes':10})

if __name__=='__main__':unittest.main()
