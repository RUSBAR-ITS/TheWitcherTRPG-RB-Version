"""Проверки справочника по исходникам; игровые документы и БД не исполняются."""
import collections
import hashlib
import json
import re
import unittest
from pathlib import Path
from test_query import BASE, ROOT, query, run_cli

class MagicCastExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l)for l in(BASE/f'data/{k}/expansion-032.jsonl').read_text().splitlines()]for k in ['entities','relations','processes']}
    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]]if r['kind']==kind]
    def test_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-032-queries.json').read_text())['cases']
        self.assertEqual(len(cases),43)
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
    def test_active_and_legacy_routes_are_distinguished(self):
        h=self.body(525);self.assertEqual(h.count('spell-type-list.hbs'),12)
        for s in [29,31]:self.assertIn("templates/partials/character/tab-magic.hbs",self.body(s));self.assertNotIn('monster-spell-tab.hbs',self.body(s))
        self.assertIn('partials/monster/monster-spell-tab.hbs',self.body(550,302,302));self.assertIn('partials/monster/monster-spell-tab.hbs',self.body(211))
        b=self.body(27,125,149)
        for group in ['noviceSpells','journeymanSpells','masterSpells','hexes','rituals','magicalgift']:self.assertIn('context.'+group,b)
        self.assertNotIn('learned',b);self.assertNotIn('hidden',b)
        self.assertIn('!i.system.isStored',self.body(47,250,257))
        # A caller depends on filtering but does not itself read the field.
        stored=self.q['CommonItemData.isStored']
        self.assertIn(stored,self.targets('WitcherActor.getList','reads'))
        self.assertNotIn(stored,self.targets('WitcherActorSheet._prepareSpells','reads'))
        self.assertIn(stored,self.targets('WitcherActorSheet._prepareSpells','refers'))
        # Legacy context has matching names; V2 is not its demonstrated producer.
        legacy='templates/partials/monster/monster-spell-tab.hbs'
        groups={self.q['WitcherActorSheet._prepareSpells.context.'+n]for n in ['noviceSpells','journeymanSpells','masterSpells','rituals','hexes','magicalgift']}
        self.assertFalse(groups & self.targets(legacy,'reads'))
        self.assertTrue(groups <= self.targets(legacy,'refers'))
        ui=self.body(561);self.assertIn('data-item-id="{{spell.id}}"',ui);self.assertIn('class="spell-roll"',ui)
        dispatch=self.body(47,225,243);self.assertIn('return this.castSpell(item)',dispatch);self.assertNotIn('castSpell(item,',dispatch)
        self.assertIn(self.q['WitcherActor.useItem'],{r['from']for r in self.data.incoming[self.q['actor.castSpellMixin.castSpell']]if r['kind']=='calls'})
    def test_prompt_and_focus_controls_preserve_raw_dom(self):
        h=self.body(508);cb=self.body(11,99,108)
        for name in ['location','isExtraAttack','staCost','focus','secondFocus','customMod']:self.assertIn('name="'+name+'"',h)
        self.assertNotIn('type="number"',h);self.assertNotIn('min=',h);self.assertNotIn('max=',h)
        self.assertIn("{{selectOptions focusOptions blank='' }}",h)
        self.assertIn('staCost?.value ?? spellItem.system.stamina',cb);self.assertIn('isExtraAttack.checked',cb);self.assertNotIn('FormDataExtended',cb)
        self.assertIn('rejectClose: true',self.body(11,93,111));self.assertNotIn('catch',self.body(11,13,270))
        focus=self.body(11,50,79)
        for n in range(1,5):self.assertIn(f'this.system.focus{n}.value > 0',focus)
        writes=[r for r in self.data.incoming[self.q['focus().value']]if r['kind']=='writes'and r['location']['source']=='src-000011'];self.assertEqual(writes,[])
    def test_will_formula_compensation_and_metadata_are_separate(self):
        b='\n'.join(self.source(11))
        self.assertIn('Math.min(armorEnc, Math.max(0, this.system.lifepathModifiers.ignoredEvWhenCasting))',b)
        self.assertIn('armorEnc > 0',b)
        self.assertIn('const check = await prepareCheck',b)
        self.assertIn("action: 'attack' }, { manual: customModifier }",b)
        self.assertIn('rollFormula = check.formula + rollFormula',b)
        self.assertIn('attack: spellItem.getItemAttack()',b)
        self.assertIn(self.q['actor.armorMixin.getArmorEcumbrance'],self.targets('actor.castSpellMixin.castSpell','calls'))
        refs=self.data.entities[self.q['magic-cast/ev-compensation']]['refs'];self.assertIn('docs/issues/potential/issue-00254.md',{r['path']for r in refs})
    def test_cost_guard_and_awaited_update(self):
        b=self.body(11)
        self.assertLess(b.index('let origStaCost = staCostTotal'),b.index('staCostTotal -= Number(focusValue)'))
        for token in ['staCostTotal += 3', 'staCostTotal < 1', 'staCostTotal = 1', 'if (newSta < 0)', "'system.derivedStats.sta.value': newSta", 'const paid = await this.update', 'if (!paid) return']:
            self.assertIn(token,b)
        self.assertLess(b.index('if (!paid) return'),b.index('await extendedRoll'))
        writes=[r for r in self.edges('actor.castSpellMixin.castSpell','writes')if r['to']==self.q['DerivedStats.sta']]
        self.assertTrue(any("'system.derivedStats.sta.value': newSta" in self.source(11)[r['location']['line_start']-1] for r in writes))
        p=self.process('Исходная сила и фактическая оплата STA');st={s['id']:s for s in p['steps']}
        self.assertEqual(st['write']['next'][0]['flow'],'await')
        self.assertIn('skipped',{e.get('exit')for e in st['write']['next']})
    def test_limited_multiplier_and_prepared_percentage_alias(self):
        b=self.body(11,272,286);self.assertIn('parseInt(origStaCost)',b);self.assertIn("value.replace('/STA', '')",b);self.assertIn("value.split('d')[0]",b);self.assertIn('return staminaMulti * value',b);self.assertNotIn('new Roll',b)
        self.assertIn('properties: this.system.damageProperties',self.body(159,8,19))
        b=self.body(11,179,198);self.assertIn('if (spellItem.system.staminaIsVar)',b);self.assertIn('effect.percentage = this.calcStaminaMulti(origStaCost, effect.percentage)',b)
        self.assertLess(self.body(11).index('effect.percentage ='),self.body(11).index('damage.properties = damage.properties?.toObject(false)'))
        self.assertIn(self.q['itemEffect().percentage'],self.targets('actor.castSpellMixin.castSpell','writes'))
        p=self.process('Подготовка damage и процентов эффектов');st={s['id']:s for s in p['steps']};self.assertEqual([x['step']for x in st['scale']['next']if'step'in x],['effects','location'])
    def test_duration_channels_and_typed_schema(self):
        b=self.body(11,164,177);self.assertIn(r"durationText.replace(/\D/g, '')",b);self.assertIn("spellItem.system.duration.split(' ')",b);self.assertIn('new Roll(durationSubstrings.shift()).evaluate()',b)
        self.assertIn('damage.duration = roll.total',b)
        schema=self.body(100)
        for key in ['duration','heal','shield']:self.assertNotIn(key+':',schema)
        for key in ['formula','location','originalLocation','properties']:self.assertIn(key+':',schema)
        self.assertIn("data-duration='{{../damage.duration}}'",self.body(487));self.assertIn('damage.duration',self.body(11,250,266))
        self.assertIn(self.q['actor.castSpellMixin.castSpell/rawDamage.duration'],self.targets('actor.castSpellMixin.castSpell','writes'))
        self.assertIn('docs/issues/potential/issue-00257.md',{r['path']for r in self.data.entities[self.q['magic-cast/raw-duration-and-typed-cleaning']]['refs']})
    def test_variable_heal_and_component_absence(self):
        b=self.body(11,208,213);self.assertIn('this.calcStaminaMulti(origStaCost, heal)',b);self.assertNotRegex(self.body(11),r'\b(?:let|const|var)\s+heal\b')
        for k in ['ritualComponentUuids','alternateRitualComponentUuids','ritualComponents','alternateRitualComponents']:self.assertNotIn(k,self.body(11))
        self.assertIn('{{spellItem.system.alternateRitualComponents}}',self.body(487));self.assertNotIn('#each spellItem.system.alternateRitualComponents',self.body(487))
        self.assertIn('#each spell.system.alternateRitualComponents',self.body(561));self.assertNotIn('spell.system.ritualComponents',self.body(561))
    def test_roll_threshold_order_and_effect_waits(self):
        b=self.body(11)
        markers=['const chatMessage = await','damage.properties =','let messageData =','new RollConfig({ showResult: false })','await extendedRoll','await roll.toMessage','createSpellRegion?.','if (!roll.options.fumble)','await createEffectDelivery','return roll']
        self.assertEqual([b.index(x)for x in markers],sorted(b.index(x)for x in markers))
        self.assertNotIn('difficultyCheck',b);self.assertIn('difficultyCheck',self.body(487))
        calls=self.targets('actor.castSpellMixin.castSpell','calls')
        for name in ['effectDelivery.collectSpellEffects','effectDelivery.createEffectDelivery']:
            self.assertIn(self.q[name],calls)
        for name in ['applyStatusEffectToActor','applyStatusEffectToTargets','applyActiveEffectToActor','applyActiveEffectToTargets']:
            self.assertNotIn(self.q[name],calls)
        self.assertIn('collectSpellEffects(this, spellItem, damage.duration)',b)
        p=self.process('После сообщения: region, fumble, статусы и AE');st={s['id']:s for s in p['steps']}
        self.assertEqual(st['region']['next'][0]['flow'],'scheduled')
        self.assertEqual([x['step']for x in st['fumble']['next']],['delivery','return'])
        self.assertEqual(st['delivery']['next'][0]['flow'],'await')
    def test_chat_action_consumers_and_region_handoff(self):
        h=self.body(487);self.assertIn('data-heal="{{damage.heal}}"',h);self.assertIn('data-shield="{{damage.shield}}"',h);self.assertNotIn('fumble',h)
        heal=self.body(193,26,48);self.assertIn('parseInt(',heal);self.assertIn('game.user.targets.first()?.actor',heal);self.assertIn('canvas.tokens.controlled[0]?.actor',heal);self.assertIn('game.user.character',heal)
        self.assertNotIn('new Roll',self.body(193,10,48));self.assertNotIn('await ',self.body(193,10,48))
        self.assertIn('message.system.attack.itemUuid',self.body(195,19,24));self.assertIn('message.system.damage',self.body(195,19,24))
        self.assertIn('{ stamina: origStaCost }',self.body(11,250,250));self.assertIn('{ roll, damage, options }',self.body(117,8,8));self.assertIn('flagOptions = {}',self.body(117,23,23));self.assertIn('options: flagOptions',self.body(117,49,49))
    def test_core_evidence_and_partial_scope(self):
        ex=json.loads((BASE/'examples/expansion-032-queries.json').read_text())
        self.assertEqual(len(ex['core_evidence']),4)
        for v in ex['core_evidence']:self.assertEqual(hashlib.sha256(Path(v['path']).read_bytes()).hexdigest(),v['sha256'])
        for s in [11,508,487,525,561,539,27]:self.assertEqual(self.data.sources[f'src-{s:06}']['coverage']['definitions']['state'],'partial')
        self.assertEqual(self.data.entities[self.q['actor.castSpellMixin.castSpell']]['id'],'ent-000868');self.assertEqual(self.data.entities[self.q['templates/chat/combat/spellItem.hbs']]['id'],'ent-005170')
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
        self.assertEqual({k:len(v)for k,v in self.new.items()},{'entities':75,'relations':340,'processes':13})

if __name__=='__main__':unittest.main()
