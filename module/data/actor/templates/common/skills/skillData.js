const fields = foundry.data.fields;

export default class Skill extends foundry.abstract.DataModel {
    static defineSchema() {
        return {
            value: new fields.NumberField({ initial: 0 }),
            baseCap: new fields.NumberField({ initial: 10, required: true, nullable: false, label: 'WITCHER.Effect.Modifier.baseCap' }),
            label: new fields.StringField({ initial: '' }),
            isVisible: new fields.BooleanField({ initial: false }),
            activeEffectModifiers: new fields.NumberField({ initial: 0 }),
            isProfession: new fields.BooleanField({ initial: false }),
            isPickup: new fields.BooleanField({ initial: false }),
            isLearned: new fields.BooleanField({ initial: false })
        };
    }

    /** The embedding field owns the skill's label, including aliases such as commonsp. */
    _initialize(options = {}) {
        super._initialize(options);
        if (this.schema.label) this.label = this.schema.label;
    }

    get modifiedValue() {
        return this.value + this.activeEffectModifiers;
    }
}
