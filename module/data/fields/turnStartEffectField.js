/** Object ADD is supported only for individual turn-start effect records. */
export default class TurnStartEffectField extends foundry.data.fields.SchemaField {
    /** Parse JSON without filling absent fields: they must not erase existing modifiers. */
    _castChangeDelta(raw, replacementData = {}) {
        const delta = typeof raw === 'string' ? JSON.parse(this._replaceDataRefs(raw, replacementData)) : raw;
        if (!foundry.utils.isPlainObject(delta)) throw new Error('Expected a turn-start effect object');
        return delta;
    }

    /** Native applyChange subsequently cleans, validates and initializes the merged record. */
    _applyChangeAdd(value, delta, model, change) {
        return foundry.utils.mergeObject(value ?? {}, delta, { inplace: false });
    }
}

/** A lone damage modifier is an inert record until a source supplies damage.amount. */
export class TurnStartDamageModifierField extends foundry.data.fields.NumberField {
    _applyChangeAdd(value, delta, model, change) {
        return (value ?? 0) + delta;
    }
}
