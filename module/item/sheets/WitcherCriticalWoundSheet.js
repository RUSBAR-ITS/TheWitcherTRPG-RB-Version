import WitcherItemSheet from './WitcherItemSheet.js';
import WitcherCriticalWoundConfigurationSheet from './configurations/WitcherCriticalWoundConfigurationSheet.js';

export default class WitcherCriticalWoundSheet extends WitcherItemSheet {
    configuration = new WitcherCriticalWoundConfigurationSheet({ document: this.document });

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
        // A whole-sheet drop cannot choose between the two transition destinations.
        if (this.isEditable) ui.notifications.info(game.i18n.localize('WITCHER.criticalWound.dropInConfiguration'));
    }
}
