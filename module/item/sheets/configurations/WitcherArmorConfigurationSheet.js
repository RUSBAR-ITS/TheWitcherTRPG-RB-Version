import WitcherPropertiesConfigurationSheet from './WitcherPropertiesConfigurationSheet.js';

export default class WitcherArmorConfigurationSheet extends WitcherPropertiesConfigurationSheet {
    static PARTS = {
        ...super.PARTS,
        general: {
            template: 'systems/TheWitcherTRPG-RB-Version/templates/sheets/item/configuration/tabs/armorGeneral.hbs',
            scrollable: ['']
        }
    };
}
