const fields = foundry.data.fields;

export default class TemporaryHealth extends foundry.abstract.DataModel {
    static defineSchema() {
        return {
            addTemporaryHealth: new fields.BooleanField({
                initial: false,
                label: 'WITCHER.profession.skillPath.skill.skillUsage.temporaryHealth.addTemporaryHealth'
            }),
            mode: new fields.StringField({ initial: 'perPoint', choices: {
                fixed: 'WITCHER.TemporaryHP.fixed', perPoint: 'WITCHER.TemporaryHP.perPoint'
            }, label: 'WITCHER.TemporaryHP.mode' }),
            requiresCheck: new fields.BooleanField({ initial: true, label: 'WITCHER.TemporaryHP.requiresCheck' }),
            rounding: new fields.StringField({ initial: 'up', choices: {
                up: 'WITCHER.TemporaryHP.up', down: 'WITCHER.TemporaryHP.down'
            }, label: 'WITCHER.TemporaryHP.rounding' }),
            durationUnit: new fields.StringField({ initial: 'rounds', choices: {
                rounds: 'WITCHER.TemporaryHP.rounds', minutes: 'WITCHER.TemporaryHP.minutes',
                hours: 'WITCHER.TemporaryHP.hours', days: 'WITCHER.TemporaryHP.days'
            }, label: 'WITCHER.TemporaryHP.durationUnit' }),
            references: new fields.TypedObjectField(new fields.SchemaField({
                role: new fields.StringField({ choices: ['source', 'target'], initial: 'source' }),
                target: new fields.SchemaField({
                    kind: new fields.StringField({ choices: ['ability', 'stat', 'builtin', 'item', 'profession'], initial: 'ability' }),
                    key: new fields.StringField({ initial: '' }), skillId: new fields.StringField({ initial: '' })
                }),
                value: new fields.StringField({ choices: ['base', 'effective'], initial: 'base' })
            }), { initial: () => ({ p1: { role: 'source', target: { kind: 'ability' }, value: 'base' } }) }),
            difficultyCheck: new fields.SchemaField({
                multiplier: new fields.NumberField({
                    initial: 3,
                    label: 'WITCHER.profession.skillPath.skill.skillUsage.temporaryHealth.difficultyCheck.multiplier'
                }),
                stat: new fields.StringField({
                    initial: 'int',
                    label: 'WITCHER.profession.skillPath.skill.skillUsage.temporaryHealth.difficultyCheck.stat',
                    blank: false
                }),
                maxRollOver: new fields.NumberField({
                    initial: 5,
                    label: 'WITCHER.profession.skillPath.skill.skillUsage.temporaryHealth.difficultyCheck.maxRollOver'
                })
            }),
            temporaryHp: new fields.SchemaField({
                value: new fields.StringField({
                    initial: '1d6',
                    label: 'WITCHER.profession.skillPath.skill.skillUsage.temporaryHealth.temporaryHp.value'
                }),
                duration: new fields.StringField({
                    initial: '2*@p1',
                    label: 'WITCHER.profession.skillPath.skill.skillUsage.temporaryHealth.temporaryHp.duration'
                })
            })
        };
    }
}
