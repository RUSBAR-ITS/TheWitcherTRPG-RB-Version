import WitcherItemSheet from './WitcherItemSheet.js';

export default class WitcherCriticalWoundSheet extends WitcherItemSheet {
    static DEFAULT_OPTIONS = {
        position: {
            width: 600,
            height: 620
        }
    };
    static PARTS = {
        main: {
            template: `systems/TheWitcherTRPG-RB-Version/templates/sheets/item/criticalWound-sheet.hbs`,
            scrollable: ['']
        }
    };

    async _onDropItem(event, item) {
        return this.document.update({
            'system.followUp': item.uuid
        });
    }
}
