import { DERIVED_MODIFIER_TARGETS, MODIFIER_DEFAULTS, modifierSettings, supportsModifierChange } from '../../activeEffect/modifierContext.js';

const fields = foundry.data.fields;

/** Keep the core change schema, adding defaults only to supported numeric rows. */
class ModifierChangeField extends fields.SchemaField {
    _cleanType(data, options, state) {
        if (!options.partial && supportsModifierChange(data)) {
            for (const [key, value] of Object.entries(modifierSettings(data))) data[key] ??= value;
        }
        return super._cleanType(data, options, state);
    }
}

/** Propagate a rejected row through the native partial-update validation tree. */
class ModifierChangesField extends fields.ArrayField {
    _updateDiff(key, value, options, state) {
        super._updateDiff(key, value, options, state);
        if (state.failure.fields[key]?.unresolved) state.failure.unresolved = true;
    }
}

export function effectIdentityFields() {
    return {
        effectTypeId: new fields.StringField({ initial: '', label: 'WITCHER.Effect.Modifier.effectTypeId', hint: 'WITCHER.Effect.Modifier.effectTypeIdHint' }),
        nonStacking: new fields.BooleanField({ initial: false, label: 'WITCHER.Effect.Modifier.nonStacking', hint: 'WITCHER.Effect.Modifier.nonStackingHint' })
    };
}

export function validateEffectIdentity(data) {
    if (data.nonStacking && !data.effectTypeId?.trim()) {
        throw new Error(game.i18n.localize('WITCHER.Effect.Modifier.errors.typeIdRequired'));
    }
}

function validateModifierChange(change) {
    const fail = key => { throw new Error(game.i18n.localize(`WITCHER.Effect.Modifier.errors.${key}`)); };
    if (!supportsModifierChange(change)) {
        // Native/special rows have no numeric settings unless explicitly configured.
        if (Object.keys(MODIFIER_DEFAULTS).some(key => change[key] !== undefined) || change.excludedDerived?.length) fail('unsupported');
        return;
    }
    const s = modifierSettings(change);
    if (s.affectsParameter && s.affectsRoll) fail('channels');
    if (s.affectsRoll && (s.fullEffect || s.shiftsCap || s.affectsAdvancement || s.excludedDerived.length)) fail('rollOnly');
    if (!s.affectsParameter && (s.fullEffect || s.excludedDerived.length)) fail('parameterOnly');
    if (s.optionalOnRoll && !s.affectsRoll) fail('optionalOnly');
}

export default class WitcherActiveEffectData extends foundry.data.ActiveEffectTypeDataModel {
    static defineSchema() {
        const schema = super.defineSchema();
        const booleanFields = Object.fromEntries(Object.keys(MODIFIER_DEFAULTS).map(key => [key,
            new fields.BooleanField({ required: false, initial: undefined, label: `WITCHER.Effect.Modifier.${key}` })
        ]));
        return {
            ...schema,
            changes: new ModifierChangesField(new ModifierChangeField({
                ...Object.fromEntries(Object.entries(schema.changes.element.fields).map(([key, field]) =>
                    [key, new field.constructor({ ...field.options })])),
                ...booleanFields,
                excludedDerived: new fields.ArrayField(new fields.StringField({ choices: DERIVED_MODIFIER_TARGETS }), {
                    required: false, initial: undefined
                })
            }, { validate: validateModifierChange })),
            ...effectIdentityFields(),
            temporaryHpDuration: new fields.SchemaField({
                value: new fields.NumberField({ required: true, nullable: false }),
                unit: new fields.StringField({ choices: ['rounds', 'minutes', 'hours', 'days'], initial: 'rounds' }),
                combatId: new fields.StringField({ nullable: true, initial: null }),
                combatantId: new fields.StringField({ nullable: true, initial: null }),
                startRound: new fields.NumberField({ nullable: true, initial: null })
            }, { nullable: true, initial: null }),
            applySelf: new fields.BooleanField({
                initial: false,
                label: 'WITCHER.Effect.applySelf'
            }),
            applyOnTarget: new fields.BooleanField({
                initial: false,
                label: 'WITCHER.Effect.applyOnTarget'
            }),
            applyOnHit: new fields.BooleanField({
                initial: false,
                label: 'WITCHER.Effect.applyOnHit'
            }),
            applyOnDamage: new fields.BooleanField({
                initial: false,
                label: 'WITCHER.Effect.applyOnDamage'
            }),
            applyAfterCalculations: new fields.BooleanField({
                initial: false,
                label: 'WITCHER.Effect.applyAfterCalculations'
            })
        };
    }

    static validateJoint(data) {
        validateEffectIdentity(data);
    }
}
