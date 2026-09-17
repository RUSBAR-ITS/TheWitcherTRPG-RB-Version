import WitcherConfigurationSheet from './WitcherConfigurationSheet.js';
import { validateWoundTarget } from '../../criticalWoundOperations.js';

export default class WitcherCriticalWoundConfigurationSheet extends WitcherConfigurationSheet {
    static DEFAULT_OPTIONS = { position: { width: 640, height: 760 } };

    static PARTS = {
        ...super.PARTS,
        general: {
            template: 'systems/TheWitcherTRPG-RB-Version/templates/sheets/item/configuration/tabs/criticalWoundGeneral.hbs',
            scrollable: ['']
        }
    };

    async _onRender(context, options) {
        await super._onRender(context, options);
        for (const zone of this.element.querySelectorAll('[data-wound-target]')) {
            zone.addEventListener('dragover', event => {
                if (this.isEditable) event.preventDefault();
            });
            zone.addEventListener('drop', event => this._onDropWound(event));
        }
    }

    async _onDropWound(event) {
        event.preventDefault();
        event.stopPropagation();
        if (!this.isEditable) return;
        const field = event.currentTarget?.dataset.woundTarget;
        if (!['stabilizedWound', 'treatedWound'].includes(field)) return;
        try {
            const data = foundry.applications.ux.TextEditor.implementation.getDragEventData(event);
            if (data.type !== 'Item') throw new Error(game.i18n.localize('WITCHER.criticalWound.errors.invalidTarget'));
            const target = await Item.implementation.fromDropData(data);
            const error = validateWoundTarget(this.document, target);
            if (error) throw new Error(game.i18n.localize(`WITCHER.criticalWound.errors.${error}`));
            return await this.document.update({ [`system.${field}`]: target.uuid });
        } catch (error) {
            ui.notifications.error(error.message);
        }
    }

    async _processSubmitData(event, form, submitData, options) {
        if (!this.isEditable) return {};
        const system = { ...this.document.system.toObject(), ...submitData.system };
        for (const field of ['stabilizedWound', 'treatedWound']) {
            const uuid = system[field]?.trim();
            if (submitData.system && field in submitData.system) submitData.system[field] = uuid || null;
            if (!uuid) continue;
            const target = await fromUuid(uuid);
            const error = validateWoundTarget(this.document, target, system);
            if (error) throw new Error(game.i18n.localize(`WITCHER.criticalWound.errors.${error}`));
        }
        return super._processSubmitData(event, form, submitData, options);
    }
}
