import { prepareCheck } from '../../scripts/rolls/prepareCheck.js';
import { resolveRollTarget } from '../rollContext.js';
import { extendedRoll } from '../../scripts/rolls/extendedRoll.js';
import { RollConfig } from '../../scripts/rollConfig.js';
import ChatMessageData from '../../chatMessage/chatMessageData.js';
import { getActorOwner } from '../../scripts/helper.js';

const DialogV2 = foundry.applications.api.DialogV2;

export let professionMixin = {
    calc_total_skills_profession() {
        let totalSkills = 0;
        let profession = this.getList('profession')[0];
        if (profession) {
            totalSkills += Number(profession.system.definingSkill.level);
            totalSkills +=
                Number(profession.system.skillPath1.skill1.level) +
                Number(profession.system.skillPath1.skill2.level) +
                Number(profession.system.skillPath1.skill3.level);
            totalSkills +=
                Number(profession.system.skillPath2.skill1.level) +
                Number(profession.system.skillPath2.skill2.level) +
                Number(profession.system.skillPath2.skill3.level);
            totalSkills +=
                Number(profession.system.skillPath3.skill1.level) +
                Number(profession.system.skillPath3.skill2.level) +
                Number(profession.system.skillPath3.skill3.level);
        }
        return totalSkills;
    },

    async _onProfessionRoll(event) {
        const element = event.currentTarget.closest('.profession-display');
        const skillTarget = { kind: 'profession', itemId: element.closest('.item').dataset.itemId,
            path: element.dataset.skillPath };
        const skill = resolveRollTarget(this, skillTarget).model;

        if (skill.skillAttack.isAttack) {
            return this.doProfessionAttackRoll(skillTarget);
        } else if (skill.skillUsage.hasCustomEffect) {
            return this.doProfessionSkillUsage(skillTarget);
        } else if (skill.thresholds.hasThresholds) {
            return this.doProfessionThreshold(skillTarget);
        } else {
            return this.doProfessionSkillRoll(skillTarget);
        }
    },

    async doProfessionAttackRoll(skillTarget) {
        const skill = resolveRollTarget(this, skillTarget).model;
        let skillAttack = skill.skillAttack;

        if (skillAttack.usesWeapon) {
            return this.doProfessionWeaponAttackRoll(skillTarget);
        }

        let displayRollDetails = game.settings.get('TheWitcherTRPG-RB-Version', 'displayRollsDetails');

        let displayDmgFormula = `${skillAttack.damageFormulaOverride}`;
        let damageFormula = !displayRollDetails
            ? `${skillAttack.damageFormulaOverride}`
            : `${skillAttack.damageFormulaOverride}[${skill.skillName}]`;

        if (skillAttack.applyMeleeBonus && (this.type == 'character' || this.system.addMeleeBonus)) {
            if (this.system.attackStats.meleeBonus < 0) {
                displayDmgFormula += `${this.system.attackStats.meleeBonus}`;
                damageFormula += !displayRollDetails
                    ? `${this.system.attackStats.meleeBonus}`
                    : `${this.system.attackStats.meleeBonus}[${game.i18n.localize('WITCHER.Dialog.attackMeleeBonus')}]`;
            }
            if (this.system.attackStats.meleeBonus > 0) {
                displayDmgFormula += `+${this.system.attackStats.meleeBonus}`;
                damageFormula += !displayRollDetails
                    ? `+${this.system.attackStats.meleeBonus}`
                    : `+${this.system.attackStats.meleeBonus}[${game.i18n.localize('WITCHER.Dialog.attackMeleeBonus')}]`;
            }
        }

        let attack = {
            attackOption: [...skillAttack.attackOptions][0],
            skill: skill.skillName,
            alias: skill.skillName
        };
        let messageDataFlavor = `<h1> ${game.i18n.localize('WITCHER.Dialog.attack')}: ${skill.skillName}</h1>`;

        let meleeBonus = skillAttack.applyMeleeBonus ? this.system.attackStats.meleeBonus : 0;
        let data = {
            attackSkill: attack,
            displayDmgFormula,
            meleeBonus: meleeBonus,
            config: CONFIG.WITCHER
        };

        const dialogTemplate = await foundry.applications.handlebars.renderTemplate(
            'systems/TheWitcherTRPG-RB-Version/templates/dialog/combat/profession-attack.hbs',
            data
        );

        let {
            isExtraAttack,
            location,
            targetOutsideLOS,
            outsideLOS,
            isProne,
            isPinned,
            isActivelyDodging,
            isMoving,
            isAmbush,
            isBlinded,
            isSilhouetted,
            customAtt,
            damageType,
            customDmg
        } = await DialogV2.prompt({
            window: {
                title: `${game.i18n.localize('WITCHER.Dialog.attackWith')}: ${skill.skillName}`,
                contentClasses: ['scrollable']
            },
            position: { width: 600 },
            content: dialogTemplate,
            modal: true,
            ok: {
                callback: (event, button, dialog) => {
                    return {
                        isExtraAttack: button.form.elements.isExtraAttack.checked,
                        location: button.form.elements.location.value,

                        targetOutsideLOS: button.form.elements.targetOutsideLOS.checked,
                        outsideLOS: button.form.elements.outsideLOS.checked,
                        isProne: button.form.elements.isProne.checked,
                        isPinned: button.form.elements.isPinned.checked,
                        isActivelyDodging: button.form.elements.isActivelyDodging.checked,
                        isMoving: button.form.elements.isMoving.checked,
                        isAmbush: button.form.elements.isAmbush.checked,
                        isBlinded: button.form.elements.isBlinded.checked,
                        isSilhouetted: button.form.elements.isSilhouetted.checked,

                        customAtt: button.form.elements.customAtt.value,
                        damageType: button.form.elements.damageType.value,
                        customDmg: button.form.elements.customDmg.value
                    };
                }
            },
            rejectClose: true
        });

        let damage = {
            properties: foundry.utils.deepClone(skillAttack.damageProperties),
            item: { name: skill.skillName },
            crit: {
                critLocationModifier: this.system.attackStats.critLocationModifier,
                critEffectModifier: this.system.attackStats.critEffectModifier
            },
            defenseOptions: foundry.utils.deepClone(skillAttack.defenseOptions)
        };
        damage.type = damageType;

        const check = await prepareCheck(this, { target: skillTarget, action: 'attack' }, { manual: customAtt });
        if (!check) return null;
        let attFormula = check.formula;

        if (targetOutsideLOS) {
            attFormula += !displayRollDetails
                ? `-3`
                : `-3[${game.i18n.localize('WITCHER.Dialog.attackTargetOutsideLOS')}]`;
        }
        if (outsideLOS) {
            attFormula += !displayRollDetails ? `+3` : `+3[${game.i18n.localize('WITCHER.Dialog.attackOutsideLOS')}]`;
        }
        if (isExtraAttack) {
            attFormula += !displayRollDetails ? `-3` : `-3[${game.i18n.localize('WITCHER.Dialog.attackExtra')}]`;
        }
        if (isProne) {
            attFormula += !displayRollDetails ? `-2` : `-2[${game.i18n.localize('WITCHER.Dialog.attackIsProne')}]`;
        }
        if (isPinned) {
            attFormula += !displayRollDetails ? `+4` : `+4[${game.i18n.localize('WITCHER.Dialog.attackIsPinned')}]`;
        }
        if (isActivelyDodging) {
            attFormula += !displayRollDetails
                ? `-2`
                : `-2[${game.i18n.localize('WITCHER.Dialog.attackIsActivelyDodging')}]`;
        }
        if (isMoving) {
            attFormula += !displayRollDetails ? `-3` : `-3[${game.i18n.localize('WITCHER.Dialog.attackIsMoving')}]`;
        }
        if (isAmbush) {
            attFormula += !displayRollDetails ? `+5` : `+5[${game.i18n.localize('WITCHER.Dialog.attackIsAmbush')}]`;
        }
        if (isBlinded) {
            attFormula += !displayRollDetails ? `-3` : `-3[${game.i18n.localize('WITCHER.Dialog.attackIsBlinded')}]`;
        }
        if (isSilhouetted) {
            attFormula += !displayRollDetails
                ? `+2`
                : `+2[${game.i18n.localize('WITCHER.Dialog.attackIsSilhouetted')}]`;
        }

        if (customDmg != '0') {
            damageFormula += !displayRollDetails
                ? `+${customDmg}`
                : `+${customDmg}[${game.i18n.localize('WITCHER.Settings.Custom')}]`;
        }
        damage.formula = damageFormula;

        let touchedLocation = this.getLocationObject(location);
        attFormula += !displayRollDetails
            ? `${touchedLocation.modifier}`
            : `${touchedLocation.modifier}[${touchedLocation.alias}]`;
        damage.location = touchedLocation;
        damage.originalLocation = location;

        messageDataFlavor = `<div class="attack-message"><h1>${game.i18n.localize('WITCHER.Attack.name')}: ${skill.skillName}</h1>`;
        messageDataFlavor += `<span>  ${game.i18n.localize('WITCHER.Armor.Location')}: ${touchedLocation.alias} </span>`;

        messageDataFlavor += `<button class="damage">${game.i18n.localize('WITCHER.table.Damage')}</button>`;

        let messageData = new ChatMessageData(this, messageDataFlavor, 'attack', {
            attacker: this.uuid,
            attack: attack,
            damage: damage,
            defenseOptions: skillAttack.defenseOptions
        });

        await extendedRoll(attFormula, messageData);
    },

    async doProfessionWeaponAttackRoll(skillTarget) {
        const skill = resolveRollTarget(this, skillTarget).model;
        let weapons = this.items
            .filter(item => item.type === 'weapon')
            .filter(weapon => weapon.system.attackOptions.has([...skill.skillAttack.attackOptions][0]));

        let options = '';
        weapons.forEach(
            weapon =>
                (options += `<option value="${weapon.id}" data-itemId="${weapon.itemId}"> ${weapon.name}</option>`)
        );

        let chooserContent = `<select name="choosen">${options}</select>`;
        let itemId = await DialogV2.prompt({
            window: { title: `` },
            content: chooserContent,
            ok: {
                callback: (event, button, dialog) => {
                    return button.form.elements.choosen.value;
                }
            },
            rejectClose: true
        });

        let weapon = this.items.get(itemId);
        return this.weaponAttack(weapon, {
            skillReplacement: skillTarget,
            additionalDamageProperties: skill.skillAttack.damageProperties
        });
    },

    async doProfessionSkillUsage(skillTarget) {
        const skill = resolveRollTarget(this, skillTarget).model;
        let target;
        if (skill.skillUsage.applyOnTarget) {
            target = game.user.targets.first()?.actor;
            if (!target) {
                ui.notifications.error(game.i18n.localize('WITCHER.profession.error.noTarget'));
                return;
            }
        } else {
            target = this;
        }

        if (skill.skillUsage.temporaryHealth.addTemporaryHealth) {
            let temporaryHealth = skill.skillUsage.temporaryHealth;
            let targetStat = target.system.stats[temporaryHealth.difficultyCheck.stat];
            let threshold = targetStat.max * temporaryHealth.difficultyCheck.multiplier;
            let roll = await this.doProfessionSkillRoll(skillTarget, {
                threshold,
                showResult: false
            });
            if (!roll) return null;
            await roll.toMessage(roll.messageData);

            if (roll.options.rollOver > 0) {
                let queryData = {};
                queryData.actorUuid = target.uuid;
                queryData.itemUuid = this.items.get(skillTarget.itemId).uuid;

                let duration = eval(
                    temporaryHealth.temporaryHp.duration.replace('@level', skill.level).match(/\d+\*?\d+/g)[0]
                );
                let value =
                    '' +
                    Math.min(roll.options.rollOver, temporaryHealth.difficultyCheck.maxRollOver) +
                    temporaryHealth.temporaryHp.value;
                if (value.includes('d')) {
                    value = (await new Roll(value).evaluate()).total;
                }

                let newEffect = new ActiveEffect({
                    name: skill.skillName,
                    icon: this.getList('profession')[0].img,
                    description: skill.definition,
                    origin: this.uuid,
                    changes: [
                        {
                            key: `system.combatEffects.temporaryEffects.temporaryHp.${skill.skillName}`,
                            mode: foundry.CONST.ACTIVE_EFFECT_MODES.ADD,
                            value: `{"name": "${skill.skillName}", "value": ${value}}`
                        }
                    ],
                    duration: { rounds: duration }
                });

                getActorOwner(target).query('TheWitcherTRPG-RB-Version.query', {
                    function: 'applyActiveEffectToActor',
                    data: [target.uuid, [newEffect]]
                });
            }
        }
    },

    async doProfessionThreshold(skillTarget) {
        const skill = resolveRollTarget(this, skillTarget).model;
        let thresholds = Object.entries(skill.thresholds.thresholds);

        let choosenThreshold;
        if (thresholds.length == 1) {
            choosenThreshold = thresholds[0][0];
        } else {
            let content = '<select id="threshold">';
            thresholds.forEach(([id, threshold]) => (content += `<option value="${id}" > ${threshold.name}</option>`));
            content += '</select>';
            choosenThreshold = await DialogV2.prompt({
                content: content,
                modal: true,
                ok: {
                    callback: (event, button, dialog) => {
                        return button.form.elements.threshold.value;
                    }
                },
                rejectClose: true
            });
        }

        return this.doProfessionSkillRoll(skillTarget, {
            threshold: skill.thresholds.thresholds[choosenThreshold].value,
            thresholdDesc: skill.thresholds.thresholds[choosenThreshold].name
        });
    },

    async doProfessionSkillRoll(skillTarget, { threshold = null, thresholdDesc = '', showResult = true } = {}) {
        const skill = resolveRollTarget(this, skillTarget).model;
        const check = await prepareCheck(this, { target: skillTarget, threshold, comparison: '>' }, {
            promptManual: true,
            title: `${game.i18n.localize('WITCHER.Dialog.profession.skill')}: ${skill.skillName}`
        });
        if (!check) return null;
        const messageData = new ChatMessageData(this, `<h2>${skill.skillName}</h2>${skill.definition}`);
        const config = new RollConfig({ showResult });
        config.threshold = check.threshold;
        config.thresholdDesc = thresholdDesc;
        return extendedRoll(check.formula, messageData, config);
    }
};
