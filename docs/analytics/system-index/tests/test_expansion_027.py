"""Проверки справочника по исходникам; игровые документы и БД не исполняются."""
import collections
import hashlib
import json
import re
import unittest
from pathlib import Path
from test_query import BASE, ROOT, query, run_cli

class RaceBiographyExpansion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset()
        cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
        cls.new={k:[json.loads(l)for l in(BASE/f'data/{k}/expansion-027.jsonl').read_text().splitlines()]for k in ['entities','relations','processes']}
    def source(self,n):return (ROOT/self.data.sources[f'src-{n:06}']['path']).read_text().splitlines()
    def edges(self,q,kind):return [r for r in self.data.outgoing[self.q[q]]if r['kind']==kind]
    def test_31_source_grounded_cli_cases(self):
        cases=json.loads((BASE/'examples/expansion-027-queries.json').read_text())['cases']
        self.assertEqual(len(cases),31)
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

    def test_homeland_and_social_owners_and_schema_slots(self):
        for q,owner in [('HomelandData.value','HomelandData'),('homeland().value','homeland()'),('general().homeland','general()'),('socialStanding().north','socialStanding()'),('general().socialStanding','general()'),('lifeEvent().isOpened','lifeEvent()'),('lifepathData.attacks.*.value','lifepathData.attacks')]:
            self.assertEqual(self.data.entities[self.q[q]]['owner'],self.q[owner])
        self.assertNotIn('CommonItemData','\n'.join(self.source(116)))
        slots='\n'.join(self.source(67));found=re.findall(r"['\"]?(\d+)['\"]?:\s+new fields.SchemaField\(lifeEvent\((\d+)\)\)",slots)
        self.assertEqual(found,[(str(n*10),str(n))for n in range(1,21)])
        for n in range(1,21):self.assertEqual(self.data.entities[self.q[f'lifeEvents().{n*10}']]['owner'],self.q['lifeEvents()'])
        self.assertNotIn('key:', '\n'.join(self.source(66)))
        self.assertNotIn('choices:', '\n'.join(self.source(152)))

    def test_selection_uses_first_sorted_unstored_item_without_field_transfer(self):
        s='\n'.join(self.source(29)[150:171]);lst='\n'.join(self.source(47)[249:257]);drop='\n'.join(self.source(43)[:55])
        for name in ['race','homeland']:self.assertIn(f"context.{name} = actor.getList('{name}')[0]",s)
        self.assertIn('!i.system.isStored',lst);self.assertIn('.sort((a, b) => a.sort - b.sort)',lst)
        self.assertIn('await this.actor.removeItemsOfType(item.type)',drop);self.assertIn('this.actor.addItem(item)',drop)
        self.assertNotIn('general.homeland',s+drop);self.assertNotIn('general.race',s+drop)
        writes={r['to']for r in self.edges('WitcherCharacterSheet._prepareCharacterData','writes')}
        self.assertTrue({self.q['WitcherCharacterSheet.context.race'],self.q['WitcherCharacterSheet.context.homeland']}<=writes)
        self.assertNotIn(self.q['homeland().value'],writes)
        callers={r['to']for r in self.edges('WitcherCharacterSheet._prepareCharacterData','calls')}
        self.assertTrue({self.q['WitcherActor.getList'],self.q['RaceData.enrichedText']}<=callers)

    def test_raw_and_enriched_are_not_conflated_with_editor_persistence(self):
        race='\n'.join(self.source(122));form='\n'.join(self.source(608));actor='\n'.join(self.source(526)[262:337])
        self.assertEqual(race.count('await createEnrichedText'),4)
        self.assertEqual(form.count('formGroup enrichedText.perk'),4)
        self.assertEqual(actor.count('{{editor race.system.perk'),4);self.assertNotIn('enrichedText',actor)
        for n in range(1,5):self.assertIn(f'target="race.system.perk{n}.description"',actor)
        rb=self.q['WitcherCharacterSheet/race-perk-editor-target']
        self.assertEqual(self.data.entities[rb]['boundary']['kind'],'dynamic')
        self.assertFalse(any(r['kind']=='writes'for r in self.data.outgoing[rb]))
        self.assertIn(self.q['perk().description'],{r['to']for r in self.edges('WitcherRaceSheet/named-form-submit','writes')})
        self.assertIn(self.q['createEnrichedText.result.enriched'],{r['to']for r in self.edges('templates/sheets/item/race-sheet.hbs','reads')})

    def test_regions_inline_and_actor_social_choice_have_different_writers(self):
        actor='\n'.join(self.source(526)[301:326]);inline='\n'.join(self.source(43)[127:145]);background='\n'.join(self.source(524))
        regions=['north','nilfgaard','skellige','dolBlathanna','mahakam']
        for n in regions:
            self.assertIn(f'data-field="system.socialStanding.{n}"',actor)
            self.assertIn(self.q[f'socialStanding().{n}'],{r['to']for r in self.edges('sheet.itemMixin._onItemInlineEdit','writes')})
        self.assertNotIn('name=',actor)
        self.assertIn("element.closest('.item').dataset.itemId",inline);self.assertIn('return item.update({ [field]: value })',inline)
        self.assertRegex(background,r"name=['\"]system\.general\.socialStanding['\"]")
        self.assertNotIn(self.q['general().socialStanding'],{r['to']for r in self.edges('sheet.itemMixin._onItemInlineEdit','writes')})
        listeners={r['to']for r in self.edges('WitcherActorSheet.activateListeners/.life-event-display/click','calls')}
        self.assertEqual(listeners,{self.q['WitcherActorSheet._onLifeEventDisplay']})

    def test_actual_social_and_lifepath_readers_are_preserved(self):
        s='\n'.join(self.source(22)[84:132]);self.assertIn("this.type == 'character'",s)
        for v in ["['tolerated', 'toleratedFeared']","['feared', 'toleratedFeared', 'hatedFeared']","['hated', 'hatedFeared']"]:self.assertIn(v,s)
        self.assertEqual(s.count('this.system.general.socialStanding'),4);self.assertNotIn('race',s);self.assertNotIn('homeland',s)
        self.assertIn(self.q['general().socialStanding'],{r['to']for r in self.edges('actor.skillMixin.addSocialStanding','reads')})
        for q,field in [('actor.armorMixin.getArmorEcumbrance','lifepathData.ignoredArmorEncumbrance'),('actor.defenseMixin.handleLifepathModifier','lifepathData.shieldParryBonus'),('actor.castSpellMixin.castSpell','lifepathData.ignoredEvWhenCasting'),('actor.weaponAttackMixin.handleStrikeType','lifepathData.attacks')]:
            self.assertIn(self.q[field],{r['to']for r in self.edges(q,'reads')})
        body='\n'.join(self.source(25)[374:378]);self.assertIn('attacks[strike]',body);self.assertNotIn('.value',body)
        self.assertNotIn(self.q['lifepathData.attacks.*.value'],{r['to']for r in self.edges('actor.weaponAttackMixin.handleStrikeType','reads')})

    def test_life_event_prepared_mutation_is_distinct_from_source_writes(self):
        s='\n'.join(self.source(29)[132:142]);base='\n'.join(self.source(27)[68:72]);toggle='\n'.join(self.source(27)[298:307]);v1='\n'.join(self.source(28)[279:287])
        self.assertIn('context.system = context.actor.system',base)
        for literal in ['Object.entries(context.system.general.lifeEvents)', 'key,', '...value','context.system.lifeEventCounter || context.system.general.lifeEvents.length']:self.assertIn(literal,s)
        self.assertNotIn('.update(',s);self.assertIn('lifeEvents.find(',toggle);self.assertIn('event.key === section.dataset.event',toggle)
        self.assertNotIn('await ',toggle);self.assertIn('lifeEvents[section.dataset.event].isOpened',v1)
        rels=self.edges('WitcherCharacterSheet._prepareContext','writes');r=next(r for r in rels if r['to']==self.q['general().lifeEvents'])
        self.assertIn('PREPARED',r['context']);self.assertIn('_source',r['context'])
        for q in ['WitcherActorSheet._onLifeEventDisplay','WitcherActorSheetV1._onLifeEventDisplay']:
            self.assertIn(self.q['lifeEvent().isOpened'],{r['to']for r in self.edges(q,'writes')})

    def test_counter_loop_and_form_paths_have_explicit_failure_branch(self):
        helper='\n'.join(self.source(211)[129:145]);hbs='\n'.join(self.source(524)[60:95]);schema='\n'.join(self.source(54)[17:18])
        self.assertIn('i < limit',helper);self.assertNotIn('Math.min',helper);self.assertNotIn('keys.length',helper)
        self.assertIn('min="1" max="20"',hbs);self.assertNotIn('min:',schema);self.assertNotIn('max:',schema)
        self.assertIn('data-event="{{this.lifeEvent.key}}"',hbs)
        for n in ['value','details']:self.assertIn('system.general.lifeEvents.{{this.lifeEvent.key}}.'+n,hbs)
        p=next(p for p in self.new['processes']if p['entry']['entity']==self.q['WitcherActorSheet._onLifeEventDisplay'])
        st={s['id']:s for s in p['steps']};self.assertTrue(any(e.get('exit')=='failed'for e in st['lookup']['next']))
        self.assertEqual(st['write']['next'][0]['flow'],'scheduled')
        loop=next(p for p in self.new['processes']if p['entry']['entity']==self.q['handlebars.eachLimit']);st={s['id']:s for s in loop['steps']}
        self.assertEqual(st['card']['next'][0]['step'],'loop')

    def test_external_core_contracts_and_original_issue_dates_are_not_runtime_tests(self):
        evidence=json.loads((BASE/'examples/expansion-027-queries.json').read_text())['core_evidence']
        for e in evidence:self.assertEqual(hashlib.sha256(Path(e['path']).read_bytes()).hexdigest(),e['sha256'])
        for q,n in [('WitcherCharacterSheet/lifeEvents-source-prepared',24),('WitcherCharacterSheet/race-perk-editor-target',109),('handlebars.eachLimit',213),('lifepathData.attacks.*.value',19)]:
            paths={r['path']for r in self.data.entities[self.q[q]]['refs']};self.assertIn(f'docs/issues/potential/issue-{n:05}.md',paths)
        for q,doc in [('WitcherRaceSheet/named-form-submit','Item'),('WitcherHomelandSheet/named-form-submit','Item'),('WitcherCharacterSheet/background-form-submit','Actor')]:
            self.assertIn(self.q['Document.update/'+doc],{r['to']for r in self.edges(q,'calls')})
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
        self.assertEqual({k:len(v)for k,v in self.new.items()},{'entities':95,'relations':334,'processes':11})

if __name__=='__main__':unittest.main()
