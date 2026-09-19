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
        self.assertIn(self.q['effectDelivery.deliverActorEffects'], self.calls('applyActiveEffectToActor'))
        self.assertIn(self.q['effectDeliveryLocal.applyLocalActiveEffects'], self.calls('effectDelivery.receiveEffectDelivery'))
        self.assertIn(self.q['effectApplication.appliedEffectData'], self.calls('effectDeliveryLocal.applyLocalActiveEffects'))
        self.assertIn(self.q['effectApplication.appliedEffectData'], self.calls('actor.temporaryEffectMixin.applyTemporaryItemImprovements'))
        self.assertIn(self.q['parameterPersistence.withParameterChanges'], self.calls('effectDelivery.receiveEffectDelivery'))

    def test_grouped_delivery_and_chat_are_connected(self):
        for caller,callee in [
            ('actor.castSpellMixin.castSpell','effectDelivery.collectSpellEffects'),
            ('actor.castSpellMixin.castSpell','effectDelivery.createEffectDelivery'),
            ('chatMessageListeners','effectDelivery.bindEffectDelivery'),
            ('effectDelivery.createEffectDelivery','effectDelivery.sendEffectDelivery'),
            ('effectDelivery.sendEffectDelivery','effectDelivery.getEffectExecutor'),
            ('effectDelivery.sendEffectDelivery','effectDelivery.deliverActorEffects'),
            ('effectDelivery.bindEffectDelivery','effectDelivery.sendEffectDelivery')]:
            self.assertIn(self.q[callee],self.calls(caller))
        service=self.q['effectDelivery.renderDelivery'];template=self.q['templates/chat/effect-delivery.hbs']
        self.assertIn(template,{r['to']for r in self.data.outgoing[service]if r['kind']=='renders'})
        p=self.data.processes['proc-000493'];steps={s['id']:s for s in p['steps']}
        self.assertIn('waiting',{n.get('exit')for n in steps['preflight']['next']})
        self.assertEqual(steps['persist']['next'][0]['step'],'deliver')
        self.assertEqual(steps['persist']['next'][0]['flow'],'await')
        self.assertEqual({n['exit']for n in steps['deliver']['next']if 'exit'in n},{'complete','review'})

    def test_consequence_consumers_and_boundaries(self):
        for caller,callee in [
            ('actor.professionMixin.doProfessionSkillUsage','effectDelivery.createEffectDelivery'),
            ('actor.defenseMixin.handleDefenseResults','effectDelivery.createItemEffectDelivery'),
            ('actor.defenseMixin.handleDefenseResults','effectDelivery.applyParryStagger'),
            ('actor.defenseMixin.skillDefense','effectDelivery.applyCriticalAdrenaline'),
            ('actor.damageMixin.applyDamage','effectDelivery.createItemEffectDelivery'),
            ('item.consumeMixin.consume','effectDelivery.createItemEffectDelivery'),
            ('effectDelivery.createItemEffectDelivery','effectDelivery.resolveEffectSource'),
            ('effectDelivery.createItemEffectDelivery','effectDelivery.createEffectDelivery'),
            ('effectDelivery.applyCriticalAdrenaline','effectDelivery.getEffectExecutor'),
            ('effectDelivery.applyCriticalAdrenaline','actor.adrenalineMixin.addAdrenaline'),
            ('onApplyStatus','fromUuid')]:
            self.assertIn(self.q[callee],self.calls(caller))
        self.assertNotIn(self.q['getActorOwner'],self.calls('actor.professionMixin.doProfessionSkillUsage'))
        steps={s['id']:s for s in self.data.processes['proc-000198']['steps']}
        self.assertEqual(steps['crit-location']['next'][0]['step'],'crit-html')
        self.assertEqual(steps['message']['next'][0]['step'],'adrenaline')
        self.assertEqual(steps['adrenaline']['next'][0]['flow'],'await')
        steps={s['id']:s for s in self.data.processes['proc-000149']['steps']}
        self.assertEqual(steps['message']['next'][0]['step'],'active')
        self.assertEqual(steps['message']['next'][0]['flow'],'await')
        self.assertEqual(self.data.processes['proc-000077']['steps'][-1]['next'][0]['flow'],'await')

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
