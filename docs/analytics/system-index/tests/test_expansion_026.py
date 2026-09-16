"""Проверки справочника по исходникам; игровые документы и БД не исполняются."""
import collections
import hashlib
import json
import re
import unittest
from pathlib import Path
from test_query import BASE, ROOT, query, run_cli

class EnhancementMutagenExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l)for l in(BASE/f'data/{k}/expansion-026.jsonl').read_text().splitlines()]for k in ['entities','relations','processes']}
    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]]if r['kind']==kind]
    def test_26_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-026-queries.json').read_text())['cases']
        self.assertEqual(len(cases),26)
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

    def test_schema_types_keep_item_effects_and_text_separate(self):
        enh='\n'.join(self.source(114));mut='\n'.join(self.source(119))
        self.assertIn('TypedObjectField(new fields.SchemaField(itemEffect()))',enh)
        self.assertIn('...consumable()',mut)
        for q,owner in [('EnhancementData.applied','EnhancementData'),('EnhancementData.effects','EnhancementData'),('MutagenData.effect','MutagenData'),('MutagenData.minorMutation','MutagenData'),('WeaponData.enhancementItemIds','WeaponData'),('ArmorData.enhancementItemIds','ArmorData')]:
            self.assertEqual(self.data.entities[self.q[q]]['owner'],self.q[owner])
        self.assertIn("effect: new fields.StringField({ initial: '' })",mut)
        self.assertNotIn('canHaveTemporaryItemImprovement',mut)
        self.assertIn('return false', '\n'.join(self.source(109)[21:24]))
        self.assertNotEqual(self.q['EnhancementData.effects'],self.q['ConsumablePropertiesData.effects'])

    def test_header_provides_mutagen_type_and_substances_are_separate(self):
        h=(ROOT/'templates/partials/item-header.hbs').read_text();m='\n'.join(self.source(605));inv='\n'.join(self.source(576));sub='\n'.join(self.source(523))
        for literal in ['item-header.hbs','name="system.effect"','name="system.minorMutation"']:self.assertIn(literal,m)
        self.assertIn('name="system.alchemyDC"',m);self.assertNotIn('data-dtype',m)
        self.assertIn('(eq item.type "mutagen")',h);self.assertIn('selectOptions config.type selected=item.system.type',h)
        self.assertIn('alchemicals=mutagens',inv);self.assertIn('templates/partials/character/substances.hbs',inv)
        self.assertNotIn('mutagen',sub.lower());self.assertEqual(sub.count('tab-inventory-components.hbs'),9)
        reads={r['to']for r in self.edges('templates/partials/item-header.hbs','reads')}
        self.assertIn(self.q['MutagenData.type'],reads)
        renders={r['to']for r in self.edges('templates/sheets/actor/tabs/tab-inventory.hbs','renders')}
        self.assertTrue({self.q['templates/partials/character/substances.hbs'],self.q['templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs']}<=renders)

    def test_choose_has_no_capacity_or_stock_guard_and_empty_ok(self):
        s='\n'.join(self.source(43)[181:237]);choose=s[:s.index('DialogV2.prompt')]
        self.assertIn("getList('enhancement')",choose);self.assertIn("if (type == 'weapon')",choose)
        self.assertIn('e.system.applied == false',choose)
        self.assertNotIn('await ',s);self.assertNotIn('return ',s)
        self.assertNotIn('quantity >',choose);self.assertNotIn('enhancements >',choose)
        self.assertIn('enhancements.length == 0',choose)
        self.assertIn('ok:',s);self.assertIn('button.form.elements.enhancement.value',s)
        self.assertNotIn('rejectClose',s)
        w='\n'.join(self.source(559));a='\n'.join(self.source(553))
        self.assertIn('data-type="weapon"',w);self.assertNotIn('data-type=',a)
        self.assertIn('enhancement-weapon-slot',a)
        self.assertNotIn('enhancement-armor-slot',a)

    def test_install_orders_prepared_push_independent_updates_and_source_copy(self):
        s='\n'.join(self.source(43)[213:234]);add='\n'.join(self.source(47)[258:273])
        literals=['newEnhancementList.push(enhancementId)',"item.update({ 'system.enhancementItemIds'",'this.actor.items.get(enhancementId)','choosenEnhancement.update','this.actor.addItem(choosenEnhancement, newQuantity, true)']
        self.assertEqual([s.index(x)for x in literals],sorted(s.index(x)for x in literals))
        self.assertIn("'system.applied': true",s);self.assertIn("'system.quantity': 1",s);self.assertIn('newQuantity > 1',s)
        self.assertIn('addItem.toObject ? addItem.toObject() : addItem',add)
        self.assertIn("await this.createEmbeddedDocuments('Item', [newItem])",add)
        writes={r['to']for r in self.edges('sheet.itemMixin._chooseEnhancement/ok.callback','writes')}
        self.assertEqual(writes,{self.q[q]for q in ['WeaponData.enhancementItemIds','ArmorData.enhancementItemIds','EnhancementData.applied','CommonItemData.quantity']})
        p=next(p for p in self.new['processes']if p['entry']['entity']==self.q['sheet.itemMixin._chooseEnhancement/ok.callback'])
        steps={s['id']:s for s in p['steps']}
        self.assertEqual(steps['parent']['next'][0]['flow'],'scheduled')
        self.assertEqual(steps['applied']['next'][0]['flow'],'scheduled')
        self.assertEqual(steps['copy']['next'][0]['flow'],'await')

    def test_prepared_consumers_and_v1_v2_writers_are_distinct(self):
        for n in [155,108]:
            s='\n'.join(self.source(n));self.assertIn('this.parent.actor.items',s);self.assertIn('system: item.system',s);self.assertIn('id: itemId',s)
        s='\n'.join(self.source(27)[174:211]);v1='\n'.join(self.source(28)[169:194])
        self.assertIn('item.system.enhancementItems = newEnhancementList',s)
        self.assertNotIn('enhancementItems =',s[s.index('async _prepareArmor'):])
        self.assertIn('item.system.enhancementItems = newEnhancementList',v1)
        attack='\n'.join(self.source(25)[169:175]);self.assertIn('this.items.get(element.id)',attack);self.assertIn('addEffects(enhancement.system.effects)',attack)
        self.assertIn(self.q['EnhancementData.effects'],{r['to']for r in self.edges('actor.weaponAttackMixin.weaponAttack','reads')})
        self.assertIn('new Array(this.enhancements - (this.enhancementItemIds?.length ?? 0))','\n'.join(self.source(108)))

    def test_remove_contract_and_editor_do_not_claim_finished_writes(self):
        s='\n'.join(self.source(34)[58:88]);body=s[s.index('removeEnhancement(pointerEvent, target)'):]
        self.assertIn('callback: this.removeEnhancement.bind(this)',s)
        self.assertIn('target.parentElement.closest',body);self.assertIn('filter(id => id != choosenEnhancement.id)',body)
        self.assertNotIn('await ',body);self.assertNotIn('quantity',body)
        editor='\n'.join(self.source(172)[144:157]);self.assertIn("if (value == 'on')",editor)
        for q in ['WitcherItemSheet._onAddEffect','WitcherItemSheet._onEditEffect','WitcherItemSheet._oRemoveEffect']:
            self.assertIn(self.q['EnhancementData.effects'],{r['to']for r in self.edges(q,'writes')})
        self.assertNotIn('varEffect','\n'.join(self.source(601)))
        self.assertIn(self.q['sheet.itemContextMenu.removableEnhancement/callback'],self.data.entities)

    def test_mutagen_consume_uses_properties_and_embedded_effects(self):
        sheet='\n'.join(self.source(174));base='\n'.join(self.source(172));consume='\n'.join(self.source(157));via='\n'.join(self.source(206)[13:30])
        self.assertIn('context.config = CONFIG.WITCHER',base)
        self.assertIn('context.config.type = this.getTypes()',sheet)
        self.assertNotIn('configuration =',sheet)
        self.assertIn('new WitcherConfigurationSheet',base)
        for absent in ['minorMutation','this.system.effect;','this.system.effect)']:self.assertNotIn(absent,consume)
        self.assertIn("applyActiveEffectToActorViaId(this.actor.uuid, this.uuid, 'applySelf')",consume)
        self.assertIn('item.effects.filter(effect => effect.system[applyWhen])',via)
        self.assertIn(self.q['item.consumeMixin.consume'],{r['to']for r in self.edges('MutagenData','passes')})

    def test_core_evidence_hashes_and_migration_contract(self):
        evidence=json.loads((BASE/'examples/expansion-026-queries.json').read_text())['core_evidence']
        for x in evidence:self.assertEqual(hashlib.sha256(Path(x['path']).read_bytes()).hexdigest(),x['sha256'])
        model=Path('/opt/foundryvtt/common/abstract/data.mjs').read_text();self.assertIn('toObject(source=true)',model);self.assertIn('if ( source ) return deepClone(this._source)',model)
        menu=Path('/opt/foundryvtt/client/applications/ux/context-menu.mjs').read_text();self.assertIn('item.callback(this.#jQuery ? $(this.#target) : this.#target, event)',menu)
        s='\n'.join(self.source(114));self.assertIn('this.effects?.forEach',s);self.assertIn('Array.isArray(source.effects) && source.effects.length > 0',s);self.assertIn('return [foundry.utils.randomID(), o]',s)
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
        self.assertEqual({k:len(v)for k,v in self.new.items()},{'entities':30,'relations':165,'processes':9})

if __name__=='__main__':unittest.main()
