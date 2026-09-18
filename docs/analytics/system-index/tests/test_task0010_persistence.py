"""Сохраняемые операции .006; численные/Document-контракты проверены отдельно."""
import unittest
from test_query import ROOT, query
class PersistenceIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=query.Dataset();cls.q={e['qualified_name']:e['id']for e in cls.data.entities.values()}
    def targets(self,name,kind='calls'):
        return {r['to']for r in self.data.outgoing[self.q[name]]if r['kind']==kind}
    def test_both_purchases_share_one_writer(self):
        for name in ['actor.skillMixin.levelUpSkill','actor.skillMixin.levelUpStat']:
            self.assertIn(self.q['parameterAdvancement.purchaseParameter'],self.targets(name))
            self.assertNotIn(self.q['Log.addIpReward'],self.targets(name))
        self.assertIn(self.q['Actor.update'],self.targets('parameterAdvancement.purchaseParameter'))
    def test_native_item_and_ae_operations_have_outer_boundary(self):
        for cls in ['WitcherItem','WitcherActiveEffect']:
            for method in ['createDocuments','updateDocuments','deleteDocuments']:
                self.assertIn(self.q['parameterPersistence.withParameterChanges'],self.targets(cls+'.'+method))
    def test_actor_write_previews_without_prepare_writes(self):
        self.assertIn(self.q['parameterPersistence.prepareParameterUpdate'],self.targets('WitcherActor.updateDocuments'))
        self.assertIn(self.q['Document.clone'],self.targets('parameterPersistence.prepareParameterUpdate'))
        self.assertNotIn(self.q['Actor.update'],self.targets('WitcherActor.prepareDerivedData'))
    def test_form_and_button_backend_connections(self):
        self.assertIn(self.q['derivedStatData.isManualDerivedStat'],self.targets('WitcherModifiersConfiguration._processFormData'))
        self.assertIn(self.q['actor.skillMixin.levelUpStat'],self.targets('sheet.statMixin.statListener'))
    def test_partial_failure_crosses_finally(self):
        p=next(p for p in self.data.processes.values()if p['entry']['entity']==self.q['parameterPersistence.withParameterChanges']);s={s['id']:s for s in p['steps']}
        self.assertEqual([n.get('step')for n in s['action']['next']],['normalize'])
        self.assertEqual([n.get('step')for n in s['save']['next']],['release'])
        self.assertEqual({n.get('exit')for n in s['release']['next']},{'done','failed'})
    def test_new_definitions_are_located_in_code(self):
        for name in ['parameterAdvancement.advancementQuote','parameterAdvancement.purchaseParameter','parameterPersistence.parameterCorrections','parameterPersistence.prepareParameterUpdate','parameterPersistence.withParameterChanges']:
            e=self.data.entities[self.q[name]];l=e['location'];line=(ROOT/self.data.sources[l['source']]['path']).read_text().splitlines()[l['line_start']-1];self.assertIn(name.split('.')[-1]+'(',line)
    def test_removed_bug_nodes_are_retired_and_report_navigable(self):
        self.assertNotIn('actor.skillMixin.levelUpSkill.magicalCost.inner',self.q)
        e=self.data.entities[self.q['parameterAdvancement.purchaseParameter']];self.assertTrue(any(r['path']=='docs/analytics/task-0010-006-checks.md'for r in e['refs']))
