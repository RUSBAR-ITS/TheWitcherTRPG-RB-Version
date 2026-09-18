import { appliedEffectData } from '../../activeEffect/effectApplication.js';

const DialogV2 = foundry.applications.api.DialogV2;

export let temporaryEffectMixin = {
    async applyTemporaryItemImprovements(effects, duration) {
        let temps = effects.filter(effect => effect.type === 'temporaryItemImprovement');
        if (!temps || temps.length == 0) return;

        let weapons = this.items.filter(item => item.type === 'weapon');

        let options = '';
        weapons.forEach(
            weapon =>
                (options += `<option value="${weapon.id}" data-itemId="${weapon.itemId}"> ${weapon.name}</option>`)
        );

        let chooserContent = `<select name="choosen">${options}</select>`;
        let itemId = await DialogV2.prompt({
            window: { title: `` },
            content: chooserContent,
            ok: {
                callback: (event, button, dialog) => {
                    return button.form.elements.choosen.value;
                }
            },
            rejectClose: true
        });

        let weapon = weapons.find(weapon => weapon.id === itemId);
        temps = temps.map(temp => {
            const data = appliedEffectData(temp, duration);
            data.name = weapon.name + ' - ' + temp.name;
            data.origin = this.uuid;
            data.system.isTransferred = true;
            data.transfer = false;
            return data;
        });
        const applied = await weapon.createEmbeddedDocuments('ActiveEffect', temps);

        const messageTemplate = 'systems/TheWitcherTRPG-RB-Version/templates/chat/item/appliedTemporaryItemImprovements.hbs';

        const content = await foundry.applications.handlebars.renderTemplate(messageTemplate, {
            item: weapon,
            temporaryItemImprovements: applied
        });
        const chatData = {
            content: content,
            speaker: ChatMessage.getSpeaker({ actor: this }),
            style: CONST.CHAT_MESSAGE_STYLES.OTHER
        };

        await ChatMessage.create(chatData);
        return applied;
    }
};
