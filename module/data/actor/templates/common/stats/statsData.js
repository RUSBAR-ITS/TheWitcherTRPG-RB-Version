import stat from './statData.js';

const fields = foundry.data.fields;

export default class Stats extends foundry.abstract.DataModel {
    static defineSchema() {
        return {
            int: new fields.SchemaField(stat('WITCHER.Actor.Stat.Int', 0, true)),
            ref: new fields.SchemaField(stat('WITCHER.Actor.Stat.Ref', 0, true)),
            dex: new fields.SchemaField(stat('WITCHER.Actor.Stat.Dex', 0, true)),
            body: new fields.SchemaField(stat('WITCHER.Actor.Stat.Body', 0, true)),
            spd: new fields.SchemaField(stat('WITCHER.Actor.Stat.Spd', 0, true)),
            emp: new fields.SchemaField(stat('WITCHER.Actor.Stat.Emp', 0, true)),
            cra: new fields.SchemaField(stat('WITCHER.Actor.Stat.Cra', 0, true)),
            will: new fields.SchemaField(stat('WITCHER.Actor.Stat.Will', 0, true)),
            luck: new fields.SchemaField(stat('WITCHER.Actor.Stat.Luck', 0, true)),
            toxicity: new fields.SchemaField(stat('WITCHER.Actor.Stat.Toxicity', 100))
        };
    }

    prepareBaseData() {
        this.int.max = this.int.unmodifiedMax;
        this.ref.max = this.ref.unmodifiedMax;
        this.dex.max = this.dex.unmodifiedMax;
        this.body.max = this.body.unmodifiedMax;
        this.spd.max = this.spd.unmodifiedMax;
        this.emp.max = this.emp.unmodifiedMax;
        this.cra.max = this.cra.unmodifiedMax;
        this.will.max = this.will.unmodifiedMax;

        this.toxicity.max = this.toxicity.unmodifiedMax;
        this.luck.max = this.luck.unmodifiedMax;
    }

    /** @inheritdoc */
    static migrateData(source) {
        if (source.int?.unmodifiedMax == 0) {
            source.int.unmodifiedMax = source.int.max;
        }
        if (source.ref?.unmodifiedMax == 0) {
            source.ref.unmodifiedMax = source.ref.max;
        }
        if (source.dex?.unmodifiedMax == 0) {
            source.dex.unmodifiedMax = source.dex.max;
        }
        if (source.body?.unmodifiedMax == 0) {
            source.body.unmodifiedMax = source.body.max;
        }
        if (source.spd?.unmodifiedMax == 0) {
            source.spd.unmodifiedMax = source.spd.max;
        }
        if (source.emp?.unmodifiedMax == 0) {
            source.emp.unmodifiedMax = source.emp.max;
        }
        if (source.cra?.unmodifiedMax == 0) {
            source.cra.unmodifiedMax = source.cra.max;
        }
        if (source.will?.unmodifiedMax == 0) {
            source.will.unmodifiedMax = source.will.max;
        }
        if (source.luck?.unmodifiedMax == 0) {
            source.luck.unmodifiedMax = source.luck.max;
        }
        if (source.toxicity?.unmodifiedMax == 0) {
            source.toxicity.unmodifiedMax = source.toxicity.max;
        }

        return super.migrateData(source);
    }
}
