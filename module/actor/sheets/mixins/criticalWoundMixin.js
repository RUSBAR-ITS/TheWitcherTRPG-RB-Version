import { reportWoundResult, woundError } from '../../../item/criticalWoundOperations.js';

export let criticalWoundMixin = {
    async _onCriticalWoundAdd(event) {
        event.preventDefault();
        if (!this.actor.isOwner) return;
        const escape = foundry.utils.escapeHTML;
        const options = Object.entries(CONFIG.WITCHER.location)
            .map(([value, label]) => `<option value="${escape(value)}">${escape(game.i18n.localize(label))}</option>`).join('');
        const data = await foundry.applications.api.DialogV2.prompt({
            window: { title: game.i18n.localize('TYPES.Item.criticalWound') },
            content: `<div class="standard-form"><label>${escape(game.i18n.localize('WITCHER.criticalWound.woundTypeId.label'))}
                <input name="woundTypeId" type="text" required /></label>
                <label>${escape(game.i18n.localize('WITCHER.criticalWound.location.label'))}
                <select name="location">${options}</select></label></div>`,
            ok: { callback: (event, button) => ({ woundTypeId: button.form.elements.woundTypeId.value.trim(),
                location: button.form.elements.location.value }) },
            rejectClose: false
        });
        if (!data) return;
        try {
            const created = await this.actor.createEmbeddedDocuments('Item', [{
                name: game.i18n.localize('TYPES.Item.criticalWound'), type: 'criticalWound', system: data
            }]);
            if (!created.length) throw woundError('writeCancelled');
            created[0].sheet.render(true);
            return created;
        } catch (error) {
            ui.notifications.error(error.message);
        }
    },

    async _onTreat(event) {
        event.preventDefault();
        const element = event.currentTarget;
        const uuid = element?.dataset.id;
        const crit = this.actor.items.find(item => item.uuid === uuid);
        if (!this.actor.isOwner || crit?.type !== 'criticalWound') {
            return reportWoundResult({ status: 'rejected', itemUuid: uuid ?? null,
                removed: false, reason: 'missingWound' });
        }
        const result = element.dataset.action === 'stabilizeCriticalWound'
            ? await crit.system.stabilize() : await crit.system.treat();
        return reportWoundResult(result);
    },

    criticalWoundListener(html) {
        html.querySelectorAll('.add-crit').forEach(el =>
            el.addEventListener('click', event => this._onCriticalWoundAdd(event))
        );
        html.querySelectorAll('[data-action=treatCriticalWound], [data-action=stabilizeCriticalWound]').forEach(button =>
            button.addEventListener('click', event => this._onTreat(event))
        );
    }
};
