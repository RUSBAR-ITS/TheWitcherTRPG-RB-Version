import CommonItemData from './commonItemData.js';
import { describeContainer, validateTemplate } from '../../item/containerTemplates.js';

const fields = foundry.data.fields;

export default class ContainerData extends CommonItemData {
    static defineSchema() {
        return {
            ...super.defineSchema(),
            carry: new fields.NumberField({ initial: 0 }),
            storedWeight: new fields.NumberField({ initial: 0 }),
            content: new fields.ArrayField(new fields.StringField()),
            templateContent: new fields.ObjectField({
                initial: null,
                nullable: true,
                validate: value => {
                    if (value === null) return true;
                    try {
                        validateTemplate(value);
                        return true;
                    } catch {
                        return false;
                    }
                }
            })
        };
    }

    calcWeight() {
        const contents = describeContainer(this.parent);
        return this.isCarried && !this.isStored ? this.quantity * this.weight + contents.weight : 0;
    }

    prepareDerivedData() {
        super.prepareDerivedData();
        const contents = describeContainer(this.parent);
        this.storedWeight = contents.weight;
        this.itemContent = contents.rows;
        this.contentIncomplete = contents.incomplete;
    }
}
