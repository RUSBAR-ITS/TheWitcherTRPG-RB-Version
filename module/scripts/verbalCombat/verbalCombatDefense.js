import { prepareCheck } from '../rolls/prepareCheck.js';
import { extendedRoll } from '../rolls/extendedRoll.js';
import { getInteractActor } from '../helper.js';
import { RollConfig } from '../rollConfig.js';
import ChatMessageData from '../../chatMessage/chatMessageData.js';

export function addVerbalCombatDefenseMessageContextOptions(html, options) {
    let canDefend = li => li.querySelector('.verbal-combat-attack-message')?.length;
    options.push({
        label: `${game.i18n.localize('WITCHER.Context.Defense')}`,
        icon: '<i class="fas fa-shield-alt"></i>',
        visible: canDefend,
        callback: async li => {
            executeDefense(await getInteractActor(), li.dataset.messageId, li.find('.dice-total')[0].innerText);
        }
    });
    return options;
}

async function executeDefense(actor, messageId, totalAttack) {
    if (!actor) return;

    const dialogTemplate = await foundry.applications.handlebars.renderTemplate(
        'systems/TheWitcherTRPG-RB-Version/templates/dialog/verbal-combat-defense.hbs',
        {
            defenses: CONFIG.WITCHER.verbalCombat.Defenses
        }
    );

    new Dialog({
        title: `${game.i18n.localize('WITCHER.Dialog.DefenseTitle')}`,
        content: dialogTemplate,
        buttons: {
            t1: {
                label: `${game.i18n.localize('WITCHER.Dialog.ButtonRoll')}`,
                callback: executeDefenseCallback.bind(this, actor, totalAttack)
            },
            t2: {
                label: `${game.i18n.localize('WITCHER.Button.Cancel')}`
            }
        }
    }).render(true);
}

async function executeDefenseCallback(actor, totalAttack, html) {

    let checkedBox = document.querySelector('input[name="verbalCombat"]:checked');
    if (!checkedBox) return;
    let verbal = checkedBox.value;

    if (verbal == 'Counterargue') {
        actor.verbalCombat();
        return;
    }

    let verbalCombat = CONFIG.WITCHER.verbalCombat.Defenses[verbal];
    let vcName = verbalCombat.name;

    let vcDmg = verbalCombat.baseDmg
        ? `${verbalCombat.baseDmg}+${actor.system.stats[verbalCombat.dmgStat.name].value}[${game.i18n.localize(verbalCombat.dmgStat?.label)}]`
        : game.i18n.localize('WITCHER.verbalCombat.None');

    let effect = verbalCombat.effect;

    const check = await prepareCheck(actor, {
        target: verbalCombat.skill ? { kind: 'builtin', key: verbalCombat.skill.name } : null,
        action: 'verbalDefense', comparison: '>=', threshold: Number(totalAttack)
    }, { manual: html.find('[name=customModifiers]')[0].value });
    if (!check) return null;
    const rollFormula = check.formula;

    let messageData = new ChatMessageData(actor);
    messageData.flavor = `
            <div class="verbal-combat-attack-message">
              <h2>${game.i18n.localize('WITCHER.verbalCombat.Title')}: ${game.i18n.localize(vcName)}</h2>
              <b>${game.i18n.localize('WITCHER.Weapon.Damage')}</b>: ${vcDmg} <br />
              ${game.i18n.localize(effect)}
              <hr />
              </div>`;
    messageData.flavor += vcDmg.includes('d')
        ? `<button class="vcDamage" > ${game.i18n.localize('WITCHER.table.Damage')}</button>`
        : '';

    let config = createRollConfig(verbalCombat.skill, check.threshold);
    config.showCrit = true;
    await extendedRoll(rollFormula, messageData, config, actor.createVerbalCombatFlags(verbalCombat, vcDmg));
}

function createRollConfig(skill, totalAttack) {
    let config = new RollConfig();
    config.showResult = true;
    config.defense = true;
    config.threshold = Number(totalAttack);
    config.thresholdDesc = skill?.label ?? '';
    return config;
}
