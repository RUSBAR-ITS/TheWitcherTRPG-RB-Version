import { effectIdentityFields, validateEffectIdentity } from './witcherActiveEffectData.js';

const fields = foundry.data.fields;

export default class WitcherTemporaryItemImprovementData extends foundry.data.ActiveEffectTypeDataModel {
    static metadata = Object.freeze({
        type: 'temporaryItemImprovement'
    });

    static defineSchema() {
        return {
            ...super.defineSchema(),
            ...effectIdentityFields(),
            applySelf: new fields.BooleanField({
                initial: false,
                label: 'WITCHER.Effect.applySelf'
            }),
            applyOnTarget: new fields.BooleanField({
                initial: false,
                label: 'WITCHER.Effect.applyOnTarget'
            }),
            isTransferred: new fields.BooleanField({ initial: false })
        };
    }

    static validateJoint(data) {
        validateEffectIdentity(data);
    }
}
