import { createItemEffectDelivery } from '../../scripts/effectDelivery.js';

export let consumeMixin = {
    async consume() {
        let properties = this.system.consumeProperties;
        let messageInfos = {};
        if (properties.doesHeal) {
            let heal = parseInt(await this.actor.calculateHealValue(properties.heal));
            this.actor?.update({ 'system.derivedStats.hp.value': this.actor.system.derivedStats.hp.value + heal });
            messageInfos.heal = heal;
        }

        this.actor.applyStatus(properties.effects);
        this.actor.removeStatus(this.system.consumeProperties.removesEffects);
        const message = await this.createConsumeMessage(messageInfos);
        await createItemEffectDelivery({ actor: this.actor, itemUuid: this.uuid, applyWhen: 'applySelf', message });
    },

    async createConsumeMessage(messageInfos) {
        const messageTemplate = 'systems/TheWitcherTRPG-RB-Version/templates/chat/item/consume.hbs';

        let statusEffects = this.system.consumeProperties.effects.map(effect => {
            return {
                name: effect.name,
                statusEffect: CONFIG.WITCHER.statusEffects.find(configEffect => configEffect.id == effect.statusEffect)
            };
        });

        const content = await foundry.applications.handlebars.renderTemplate(messageTemplate, {
            item: this,
            messageInfos,
            statusEffects
        });
        const chatData = {
            content: content,
            speaker: ChatMessage.getSpeaker({ actor: this.actor }),
            style: CONST.CHAT_MESSAGE_STYLES.OTHER
        };

        return ChatMessage.create(chatData);
    }
};
