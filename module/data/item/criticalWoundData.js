import { createEnrichedText } from '../dataUtils.js';
import { evaluateHealingDuration, transitionWound, healWound } from '../../item/criticalWoundOperations.js';

const fields = foundry.data.fields;

export default class CriticalWoundData extends foundry.abstract.TypeDataModel {
    static metadata = Object.freeze({
        type: 'criticalWound'
    });

    static defineSchema() {
        return {
            description: new fields.HTMLField({ initial: '' }),

            criticalLevel: new fields.StringField({
                initial: 'simple',
                label: 'WITCHER.criticalWound.criticalLevel.label'
            }),
            treatment: new fields.StringField({ initial: 'none', label: 'WITCHER.criticalWound.treatment.label' }),
            location: new fields.StringField({ initial: 'torso' }),
            woundTypeId: new fields.StringField({
                initial: '',
                label: 'WITCHER.criticalWound.woundTypeId.label',
                hint: 'WITCHER.criticalWound.woundTypeId.hint'
            }),
            cannotStabilize: new fields.BooleanField({
                initial: true,
                label: 'WITCHER.criticalWound.cannotStabilize'
            }),
            cannotTreat: new fields.BooleanField({ initial: true, label: 'WITCHER.criticalWound.cannotTreat' }),
            canHeal: new fields.BooleanField({ initial: false, label: 'WITCHER.criticalWound.canHeal' }),
            healingDuration: new fields.StringField({
                initial: '',
                label: 'WITCHER.criticalWound.healingDuration.label',
                hint: 'WITCHER.criticalWound.healingDuration.hint'
            }),
            lesserEffect: new fields.BooleanField({
                initial: false,
                label: 'WITCHER.criticalWound.lesserEffect.label',
                hint: 'WITCHER.criticalWound.lesserEffect.hint'
            }),

            daysHealed: new fields.NumberField({ initial: 0 }),
            sterilized: new fields.BooleanField({ initial: false }),

            stabilizedWound: new fields.DocumentUUIDField({
                type: 'Item',
                initial: null,
                nullable: true,
                label: 'WITCHER.criticalWound.stabilizedWound.label',
                hint: 'WITCHER.criticalWound.stabilizedWound.hint'
            }),
            treatedWound: new fields.DocumentUUIDField({
                type: 'Item',
                initial: null,
                nullable: true,
                label: 'WITCHER.criticalWound.treatedWound.label',
                hint: 'WITCHER.criticalWound.treatedWound.hint'
            })
        };
    }

    static validateJoint(data) {
        if (!data.canHeal) return;
        const result = evaluateHealingDuration(data.healingDuration);
        if (result.error && result.error !== 'missingBody') {
            throw new Error(game.i18n.localize(`WITCHER.criticalWound.errors.${result.error}`));
        }
    }

    get healingStatus() {
        if (!this.canHeal) return { value: null, error: 'healingDisabled' };
        return evaluateHealingDuration(this.healingDuration, this.parent?.parent);
    }

    get healingTime() {
        return this.healingStatus.value;
    }

    get healingTimeDisplay() {
        return this.healingTime ?? '—';
    }

    get healingTimeHint() {
        const { error } = this.healingStatus;
        return error ? game.i18n.localize(`WITCHER.criticalWound.errors.${error}`) : this.healingDuration;
    }

    async enrichedText() {
        return {
            description: await createEnrichedText(this, this.description, 'description')
        };
    }

    heal(options) {
        return healWound(this.parent, options);
    }

    treat() {
        return transitionWound(this.parent, 'treat');
    }

    stabilize() {
        return transitionWound(this.parent, 'stabilize');
    }

    get canHaveTemporaryItemImprovement() {
        return false;
    }
}
