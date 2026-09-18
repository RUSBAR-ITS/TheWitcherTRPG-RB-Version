"""Адресные маршруты .008; арифметика/расходы проверяются настоящим JS отдельно."""
import unittest
from test_query import ROOT, query

class ConsumerIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset();cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
    def calls(self,name):
        return {r['to']for r in self.data.outgoing[self.q[name]]if r['kind']=='calls'}
    def test_shared_check_reaches_numeric_prompt_and_conditional_calculation(self):
        for callee in ['getCustomModifierValue','conditionalModifiers.chooseRollModifiers','rollModifiers.formatRollContributions']:
            self.assertIn(self.q[callee],self.calls('prepareCheck'))
    def test_consumers_reach_shared_check(self):
        for caller in ['actor.skillMixin.rollSkillCheck','actor.skillMixin.rollCustomSkillCheck','actor.professionMixin.doProfessionSkillRoll','actor.professionMixin.doProfessionAttackRoll','actor.weaponAttackMixin.constructBaseAttackFormula','actor.defenseMixin.skillDefense','actor.defenseMixin.stunSave','actor.castSpellMixin.castSpell','actor.verbalCombatMixin.verbalCombat','verbalCombatDefense.prepareCheck','WitcherCharacterSheet._alchemyCraft','WitcherCharacterSheet._craftingCraft','Repair.prepareRollFormula','sheet.statMixin._onStatSaveRoll','sheet.deathsaveMixin._onDeathSaveRoll']:
            self.assertIn(self.q['prepareCheck'],self.calls(caller),caller)
    def test_profession_editors_use_slot_and_name_lookup_is_retired(self):
        self.assertFalse(any('findSkillWithName'in name for name in self.q))
        for method in ['_onAddEffectDamageProperties','_onEditEffectDamageProperties','_oRemoveEffectDamageProperties','_onAddThreshold','_onEditThreshold','_oRemoveThreshold']:
            self.assertIn(self.q['WitcherProfessionConfigurationSheet.findSkillByPath'],self.calls('WitcherProfessionConfigurationSheet.'+method))
    def test_explicit_replacement_and_repair_calls_are_present(self):
        for a,b in [('actor.professionMixin.doProfessionWeaponAttackRoll','actor.weaponAttackMixin.weaponAttack'),('actor.weaponAttackMixin.weaponAttack','actor.weaponAttackMixin.constructBaseAttackFormula'),('Repair.commonRepair','Repair.prepareRollFormula'),('rollClue','actor.skillMixin.rollSkill')]:
            self.assertIn(self.q[b],self.calls(a))
    def test_resource_processes_place_choice_before_expense(self):
        for pid,cost in [('proc-000180','sta'),('proc-000452','cost')]:
            p=self.data.processes[pid];keys=[s['id']for s in p['steps']];self.assertLess(keys.index('check-modifiers'),keys.index(cost))
            st=next(s for s in p['steps']if s['id']=='check-modifiers');self.assertIn('modifier-cancel',{n.get('exit')for n in st['next']})
        keys=[s['id']for s in self.data.processes['proc-000198']['steps']];self.assertLess(keys.index('formula'),keys.index('extra'))
    def test_current_definitions_and_partial_boundaries(self):
        for name in ['prepareCheck','getCustomModifierValue','WitcherProfessionConfigurationSheet.findSkillByPath','Repair.prepareRollFormula']:
            e=self.data.entities[self.q[name]];loc=e['location'];src=self.data.sources[loc['source']];line=(ROOT/src['path']).read_text().splitlines()[loc['line_start']-1]
            self.assertIn(name.split('.')[-1]+'(',line);self.assertEqual(src['coverage']['definitions']['state'],'partial')
        self.assertIn('issue-00111',self.data.entities['ent-004874']['summary'])
