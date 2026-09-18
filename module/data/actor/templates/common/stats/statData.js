const fields = foundry.data.fields;

export default function stat(label, unmodifiedMax = 0, capped = false) {
    return {
        ...(capped ? { baseCap: new fields.NumberField({ initial: 10, required: true, nullable: false, label: 'WITCHER.Effect.Modifier.baseCap' }) } : {}),
        max: new fields.NumberField({ initial: 0, integer: true }),
        unmodifiedMax: new fields.NumberField({ initial: unmodifiedMax, integer: true, label }),
        value: new fields.NumberField({ initial: 0 }),
        label: new fields.StringField({ initial: label }),
        totalModifiers: new fields.NumberField({ initial: 0, integer: true })
    };
}
