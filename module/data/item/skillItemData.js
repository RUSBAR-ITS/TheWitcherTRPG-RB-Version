const fields = foundry.data.fields;

export default class SkillItemData extends foundry.abstract.TypeDataModel {
    get modifiedValue() {
        return Math.min(this.baseCap, this.value + this.activeEffectModifiers);
    }

    static defineSchema() {
        return {
            attribute: new fields.StringField({ initial: '' }),
            value: new fields.NumberField({ initial: 0 }),
            baseCap: new fields.NumberField({ initial: 10, required: true, nullable: false, label: 'WITCHER.Effect.Modifier.baseCap' }),
            label: new fields.StringField({ initial: '' }),
            isOpened: new fields.BooleanField({ initial: false }),
            modifiers: new fields.ArrayField(new fields.SchemaField({
                id: new fields.StringField(), name: new fields.StringField(),
                value: new fields.NumberField({ initial: 0 })
            })),
            activeEffectModifiers: new fields.NumberField({ initial: 0 }),
            isProfession: new fields.BooleanField({ initial: false }),
            isPickup: new fields.BooleanField({ initial: false }),
            isLearned: new fields.BooleanField({ initial: false })
        };
    }
}
