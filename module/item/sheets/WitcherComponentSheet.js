import WitcherItemSheet from './WitcherItemSheet.js';

export default class WitcherComponentSheet extends WitcherItemSheet {
    static DEFAULT_OPTIONS = {
        position: {
            width: 600
        }
    };
    static PARTS = {
        main: {
            template: `systems/TheWitcherTRPG-RB-Version/templates/sheets/item/component-sheet.hbs`,
            scrollable: ['']
        }
    };
}
