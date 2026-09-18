import skillDefense from './combat/skillDefenseData.js';
import skillAttack from './combat/skillAttackData.js';
import SkillUsage from './profession/skillUsageData.js';
import Threshold from './profession/thresholdData.js';

const fields = foundry.data.fields;

export default function professionSkill() {
    return {
        skillName: new fields.StringField({ initial: '' }),
        stat: new fields.StringField({ initial: '' }),
        definition: new fields.HTMLField({ initial: '' }),
        level: new fields.NumberField({ initial: 0 }),
        activeEffectModifiers: new fields.NumberField({ initial: 0 }),
        baseCap: new fields.NumberField({ initial: 10, required: true, nullable: false, label: 'WITCHER.Effect.Modifier.baseCap' }),

        skillAttack: new fields.SchemaField(skillAttack()),
        skillDefense: new fields.SchemaField(skillDefense()),

        skillUsage: new fields.EmbeddedDataField(SkillUsage),
        thresholds: new fields.EmbeddedDataField(Threshold)
    };
}
