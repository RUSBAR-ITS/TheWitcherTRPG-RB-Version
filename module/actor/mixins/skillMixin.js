import { purchaseParameter } from '../parameterAdvancement.js';
import ChatMessageData from "../../chatMessage/chatMessageData.js";
import { prepareCheck } from "../../scripts/rolls/prepareCheck.js";
import { RollConfig } from "../../scripts/rollConfig.js";
import { extendedRoll } from "../../scripts/rolls/extendedRoll.js";

export let skillMixin = {
    async levelUpSkill(skillName) {
        if (this.type !== 'character') return purchaseParameter(this, '');
        const skill = CONFIG.WITCHER.skillMap[skillName];
        if (!skill) return false;
        return purchaseParameter(this, `system.skills.${skill.attribute.name}.${skillName}`, {
            multiplier: skill.costMultiplier ?? 1,
            magical: CONFIG.WITCHER.magicSkills.includes(skillName), label: skill.label
        });
    },

    async levelUpStat(statName) {
        if (!['int', 'ref', 'dex', 'body', 'spd', 'emp', 'cra', 'will', 'luck'].includes(statName)) return false;
        return purchaseParameter(this, `system.stats.${statName}`, {
            multiplier: 10, label: this.system.stats[statName].label
        });
    },

    async rollSkill(skillName, threshold = null, context = {}) {
        return this.rollSkillCheck(CONFIG.WITCHER.skillMap[skillName], threshold, context);
    },

    async rollSkillCheck(skillMapEntry, threshold = null, { action = 'skill' } = {}) {
        let attribute = skillMapEntry.attribute;
        let attributeLabel = game.i18n.localize(attribute.label);

        let skillName = skillMapEntry.name;
        let skillLabel = game.i18n.localize(skillMapEntry.rollLabel ?? skillMapEntry.label);

        let displayRollDetails = game.settings.get('TheWitcherTRPG-RB-Version', 'displayRollsDetails');

        let messageData = new ChatMessageData(this, `${attributeLabel}: ${skillLabel} Check`);

        const check = await prepareCheck(this, { target: { kind: 'builtin', key: skillName },
            action, comparison: '>', threshold }, { promptManual: true,
            title: `${game.i18n.localize('WITCHER.Dialog.Skill')}: ${skillLabel}` });
        if (!check) return null;
        let rollFormula = check.formula;

        rollFormula += this.addSocialStanding(attribute, skillName);

        let armorEnc = this.getArmorEcumbrance();
        if (armorEnc > 0 && (skillName == 'hexweave' || skillName == 'ritcraft' || skillName == 'spellcast')) {
            rollFormula += !displayRollDetails
                ? `-${armorEnc}`
                : `-${armorEnc}[${game.i18n.localize('WITCHER.Armor.EncumbranceValue')}]`;
        }


        let config = new RollConfig();
        config.showCrit = true;
        config.showSuccess = true;
        config.threshold = threshold;
        return extendedRoll(rollFormula, messageData, config);
    },

    addSocialStanding(attribute, skillName) {
        let displayRollDetails = game.settings.get('TheWitcherTRPG-RB-Version', 'displayRollsDetails');

        const tolerated = ['tolerated', 'toleratedFeared'];
        const feared = ['feared', 'toleratedFeared', 'hatedFeared'];
        const hated = ['hated', 'hatedFeared'];

        let socialModifiers = '';
        if (this.type == 'character') {
            // core rulebook page 21
            if (attribute.name == 'emp') {
                if (
                    skillName == 'charisma' ||
                    skillName == 'leadership' ||
                    skillName == 'persuasion' ||
                    skillName == 'seduction'
                ) {
                    if (tolerated.includes(this.system.general.socialStanding)) {
                        socialModifiers += !displayRollDetails
                            ? `-1`
                            : `-1[${game.i18n.localize('WITCHER.socialStanding.tolerated')}]`;
                    } else if (hated.includes(this.system.general.socialStanding)) {
                        socialModifiers += !displayRollDetails
                            ? `-2`
                            : `-2[${game.i18n.localize('WITCHER.socialStanding.hated')}]`;
                    }
                }

                if (skillName == 'charisma' && feared.includes(this.system.general.socialStanding)) {
                    socialModifiers += !displayRollDetails
                        ? `-1`
                        : `-1[${game.i18n.localize('WITCHER.socialStanding.feared')}]`;
                }
            }

            if (
                attribute.name == 'will' &&
                skillName == 'intimidation' &&
                feared.includes(this.system.general.socialStanding)
            ) {
                socialModifiers += !displayRollDetails
                    ? `+1`
                    : `+1[${game.i18n.localize('WITCHER.socialStanding.feared')}]`;
            }
        }

        return socialModifiers;
    },

    async rollCustomSkillCheck(event) {
        const itemId = event.currentTarget.dataset.itemId ?? event.currentTarget.closest('.item')?.dataset.itemId;
        const customSkill = this.items.get(itemId);
        if (customSkill?.type !== 'skill') return null;

        let attribute = CONFIG.WITCHER.statMap[customSkill.system.attribute];
        let attributeLabel = game.i18n.localize(attribute.label);

        let skillLabel = customSkill.name;


        let messageData = new ChatMessageData(this, `${attributeLabel}: ${skillLabel} Check`);

        const check = await prepareCheck(this, { target: { kind: 'item', itemId: customSkill.id } }, {
            promptManual: true, title: `${game.i18n.localize('WITCHER.Dialog.Skill')}: ${skillLabel}`
        });
        if (!check) return null;
        const rollFormula = check.formula;

        let config = new RollConfig();
        config.showCrit = true;
        config.showSuccess = true;
        return extendedRoll(rollFormula, messageData, config);
    }
};
