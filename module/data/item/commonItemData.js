const fields = foundry.data.fields;

/** Keep invalid numbers for validation instead of rounding/clamping during cleaning. */
class ItemQuantityField extends fields.NumberField {
    _cleanType(value) {
        return value;
    }
}

export function parseItemQuantity(value) {
    const quantity = typeof value === 'number' || (typeof value === 'string' && value.trim())
        ? Number(value) : NaN;
    if (!Number.isInteger(quantity) || quantity < 0) {
        throw new Error(game.i18n.localize('WITCHER.Item.InvalidQuantity'));
    }
    return quantity;
}

export function parseLootQuantityFormula(value) {
    const formula = String(value ?? '').trim();
    if (formula && !Roll.validate(formula)) {
        throw new Error(game.i18n.localize('WITCHER.Monster.lootInvalidFormula'));
    }
    return formula;
}

export default class CommonItemData extends foundry.abstract.TypeDataModel {
    static defineSchema() {
        return {
            description: new fields.StringField({ initial: '' }),
            quantity: new ItemQuantityField({ initial: 1, required: true, nullable: false, integer: true, min: 0 }),
            lootQuantityFormula: new fields.StringField({ initial: '', trim: true }),
            weight: new fields.NumberField({ initial: 0 }),
            cost: new fields.NumberField({ initial: 0 }),
            sourcebook: new fields.StringField({ initial: '' }),

            isHidden: new fields.BooleanField({ initial: false }),
            isStored: new fields.BooleanField({ initial: false }),
            isCarried: new fields.BooleanField({ initial: true })
        };
    }

    calcWeight() {
        return this.isCarried && !this.isStored ? this.quantity * this.weight : 0;
    }

    get canHaveTemporaryItemImprovement() {
        return false;
    }

    get canBeRepaired() {
        return false;
    }
}
