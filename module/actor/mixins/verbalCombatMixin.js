import ChatMessageData from '../../chatMessage/chatMessageData.js';
import { prepareCheck } from '../../scripts/rolls/prepareCheck.js';
import { RollConfig } from '../../scripts/rollConfig.js';
import { extendedRoll } from '../../scripts/rolls/extendedRoll.js';

const DialogV2 = foundry.applications.api.DialogV2;

export let verbalCombatMixin = {
    async verbalCombat() {
        const dialogTemplate = await foundry.applications.handlebars.renderTemplate(
            'systems/TheWitcherTRPG-RB-Version/templates/dialog/verbal-combat.hbs',
            {
                verbalCombat: CONFIG.WITCHER.verbalCombat
            }
        );
        const selection = await DialogV2.prompt({
            window: { title: game.i18n.localize('WITCHER.verbalCombat.DialogTitle') },
            content: dialogTemplate,
            ok: {
                callback: (event, button, dialog) => {
                    const checkedBox = button.form.querySelector('input[name="verbalCombat"]:checked');
                    if (!checkedBox) {
                        ui.notifications.warn(game.i18n.localize('WITCHER.verbalCombat.InvalidAction'));
                        return null;
                    }
                    let group = checkedBox.dataset.group;
                    let verbal = checkedBox.value;

                    let customModifier = button.form.elements.customModifiers.value;

                    return {
                        group,
                        verbal,
                        customModifier
                    };
                }
            },
            rejectClose: true
        });

        if (!selection) return null;
        const { group, verbal, customModifier } = selection;
        const groups = CONFIG.WITCHER.verbalCombat;
        const actions = groups[group];
        if (!Object.hasOwn(groups, group) || !Object.hasOwn(actions ?? {}, verbal)) {
            ui.notifications.warn(game.i18n.localize('WITCHER.verbalCombat.InvalidAction'));
            return null;
        }
        let verbalCombat = actions[verbal];
        let vcName = verbalCombat.name;

        let vcDmg = verbalCombat.baseDmg
            ? `${verbalCombat.baseDmg}+${this.system.stats[verbalCombat.dmgStat.name].value}[${game.i18n.localize(verbalCombat.dmgStat?.label)}]`
            : game.i18n.localize('WITCHER.verbalCombat.None');
        if (verbal == 'Counterargue') {
            vcDmg = `${game.i18n.localize('WITCHER.verbalCombat.CounterargueDmg')}`;
        }

        let effect = verbalCombat.effect;

        const check = await prepareCheck(this, {
            target: verbalCombat.skill ? { kind: 'builtin', key: verbalCombat.skill.name } : null,
            action: 'verbalAttack'
        }, { manual: customModifier });
        if (!check) return null;
        const rollFormula = check.formula;

        let flavor = `
                            <div class="verbal-combat-attack-message">
                              <h2>${game.i18n.localize('WITCHER.verbalCombat.Title')}: ${game.i18n.localize(vcName)}</h2>
                              <b>${game.i18n.localize('WITCHER.Weapon.Damage')}</b>: ${vcDmg} <br />
                              ${game.i18n.localize(effect)}
                              <hr />
                              </div>`;
        flavor += vcDmg.includes('d')
            ? `<button class="vcDamage" > ${game.i18n.localize('WITCHER.table.Damage')}</button>`
            : '';

        let messageData = new ChatMessageData(this, flavor, 'damage', { vcDamage: vcDmg });

        let config = new RollConfig();
        config.showCrit = true;
        return extendedRoll(rollFormula, messageData, config, this.createVerbalCombatFlags(verbalCombat, vcDmg));
    },

    createVerbalCombatFlags(verbalCombat, vcDamage) {
        return [
            {
                key: 'verbalCombat',
                value: verbalCombat
            },
            {
                key: 'damage',
                value: {
                    formula: vcDamage
                }
            }
        ];
    }
};
