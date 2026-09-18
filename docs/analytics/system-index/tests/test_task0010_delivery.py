"""Адресная навигация .009; поведение проверено в изолированных JS-тестах."""
import unittest
from test_query import query

class DeliveryIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = query.Dataset()
        cls.q = {e['qualified_name']: e['id'] for e in cls.data.entities.values()}

    def calls(self, name):
        return {r['to'] for r in self.data.outgoing[self.q[name]] if r['kind'] == 'calls'}

    def test_delivery_shares_copy_and_outer_parameter_operation(self):
        self.assertIn(self.q['effectApplication.appliedEffectData'], self.calls('applyActiveEffectToActor'))
        self.assertIn(self.q['effectApplication.appliedEffectData'], self.calls('actor.temporaryEffectMixin.applyTemporaryItemImprovements'))
        self.assertIn(self.q['parameterPersistence.withParameterChanges'], self.calls('applyActiveEffectToActor'))

    def test_native_creation_and_nested_items_reach_family_and_clock(self):
        self.assertIn(self.q['effectFamilies.createEffectDocuments'], self.calls('WitcherActiveEffect.createDocuments'))
        self.assertIn(self.q['effectFamilies.assignedItemData'], self.calls('WitcherItem.createDocuments'))
        self.assertIn(self.q['effectApplication.initializeEffectStart'], self.calls('WitcherActiveEffect._preCreate'))
        self.assertIn(self.q['effectApplication.initializeEffectStart'], self.calls('effectFamilies.assignedItemData'))

    def test_prepared_duration_mutation_and_private_forwarder_retired(self):
        self.assertNotIn('applyTemporaryItemImprovements', self.q)
        self.assertNotIn('applyActiveEffectToActor/effect.duration.rounds', self.q)
        self.assertIn('chat.damageData().duration', self.q)
        self.assertIn('WitcherActiveEffect.isExpiryTrackable', self.q)

    def test_delivery_processes_state_awaited_writes_and_pending_live_boundary(self):
        for id in ['proc-000036', 'proc-000037', 'proc-000038', 'proc-000045', 'proc-000046']:
            p = self.data.processes[id]
            self.assertTrue(any(n['flow'] == 'await' for s in p['steps'] for n in s['next']))
            self.assertIn('partial', p['coverage'])
            self.assertTrue(any(r['path'] == 'docs/analytics/task-0010-009-checks.md' for r in p['refs']))

    def test_expiry_init_and_whole_batch_share_parameter_boundary(self):
        self.assertIn(self.q['effectExpiry.registerEffectExpiry'], self.calls('init callback'))
        self.assertIn(self.q['effectExpiry.apply'], self.calls('effectExpiry.refresh'))
        self.assertIn(self.q['parameterPersistence.withParameterChanges'], self.calls('effectExpiry.apply'))

    def test_expiry_process_separates_authority_and_final_normalization(self):
        p = next(p for p in self.data.processes.values() if p['entry']['entity'] == self.q['effectExpiry.refresh'])
        steps = {s['id']: s for s in p['steps']}
        self.assertEqual({n.get('step') or n.get('exit') for n in steps['authority']['next']}, {'actors', 'native'})
        self.assertEqual({n['exit'] for n in steps['batch']['next']}, {'done', 'failed'})
        self.assertTrue(all(n['flow'] == 'await' for n in steps['batch']['next']))
