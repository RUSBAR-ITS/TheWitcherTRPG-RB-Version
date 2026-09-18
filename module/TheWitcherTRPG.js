import { registerEffectExpiry } from './activeEffect/effectExpiry.js';
import { WITCHER } from './setup/config.js';
import * as Chat from './scripts/chat.js';
import * as VerbalCombat from './scripts/verbalCombat/verbalCombat.js';
import * as VerbalCombatDefense from './scripts/verbalCombat/verbalCombatDefense.js';
import * as Combat from './scripts/combat/combat.js';
import * as ApplyDamage from './scripts/combat/applyDamage.js';
import * as ApplyStatusEffects from './scripts/statusEffects/applyStatusEffect.js';
import * as Fumble from './scripts/rolls/fumble.js';
import { registerSettings } from './setup/settings.js';

import WitcherItem from './item/witcherItem.js';
import WitcherItems from './item/collections/WitcherItems.js';
import WitcherActor from './actor/witcherActor.js';
import WitcherRollTable from './rollTable/witcherRollTable.js';

import { registerDataModels } from './setup/registerDataModels.js';
import { registerSheets } from './setup/registerSheets.js';
import { registerSocketListeners } from './setup/socketHook.js';
import WitcherActiveEffect from './activeEffect/witcherActiveEffect.js';
import { registerHooks } from './setup/hooks.js';
import { deprecationWarnings } from './setup/deprecations.js';
import { applyActiveEffectToActorViaId } from './scripts/temporaryEffects/applyActiveEffect.js';
import { preloadHandlebarsTemplates, registerHandelbarHelpers } from './setup/handlebars.js';
import Rewards from './app/reward/reward.js';
import { registerQueries } from './setup/queries.js';

registerHooks();

Hooks.once('init', function () {
    console.log('TheWitcherTRPG | init system');

    CONFIG.WITCHER = WITCHER;
    CONFIG.statusEffects = CONFIG.WITCHER.statusEffects;
    CONFIG.Item.documentClass = WitcherItem;
    CONFIG.Item.collection = WitcherItems;
    CONFIG.Actor.documentClass = WitcherActor;
    CONFIG.RollTable.documentClass = WitcherRollTable;
    CONFIG.ActiveEffect.documentClass = WitcherActiveEffect;
    CONFIG.ActiveEffect.expiryAction = 'delete';
    registerEffectExpiry();

    game.api = {
        applyActiveEffectToActorViaId,
        rewards: {
            ip: Rewards.handoutIpRewards,
            currency: Rewards.handoutCurrencyRewards
        }
    };

    registerDataModels();
    registerSheets();
    preloadHandlebarsTemplates();
    registerSettings();
    registerQueries();
});

Hooks.on('renderChatMessageHTML', (message, html, data) => {
    Combat.attackChatMessageListeners(message, html);
    Combat.defenseChatMessageListeners(message, html);
    VerbalCombat.chatMessageListeners(message, html);
    ApplyStatusEffects.chatMessageListeners(message, html);
    Chat.chatMessageListeners(message, html);
});

Hooks.on('renderActiveEffectConfig', async (activeEffectConfig, html, data) => {});

Hooks.once('ready', async function () {
    // Indexing an optional configured pack must not interrupt independent startup work.
    const packId = game.settings.get('TheWitcherTRPG-RB-Version', 'criticalWoundsPack');
    const criticalWounds = game.packs.get(packId);
    try {
        if (!criticalWounds) throw new Error(game.i18n.localize('WITCHER.Compendium.missingPack'));
        if (criticalWounds.documentName !== 'Item') {
            throw new Error(game.i18n.localize('WITCHER.Compendium.expectedItemPack'));
        }
        await criticalWounds.getIndex({
            fields: ['system.criticalLevel', 'system.location', 'system.lesserEffect', 'system.treatment', 'system.woundTypeId']
        });
    } catch (error) {
        console.error('TheWitcherTRPG | Critical wounds index', packId, error);
        ui.notifications.error(
            game.i18n.format('WITCHER.Compendium.criticalWoundsIndexFailed', {
                pack: criticalWounds?.metadata.label ?? packId,
                reason: error.message ?? String(error)
            })
        );
    }

    // Wait to register hotbar drop hook on ready so that modules could register earlier if they want to
    Hooks.on('hotbarDrop', (bar, data, slot) => {
        if (data.type === 'Item') {
            createMacro(data, slot);
            return false;
        }
    });

    if (game.settings.get('TheWitcherTRPG-RB-Version', 'useWitcherFont')) {
        let els = document.getElementsByClassName('game');
        Array.prototype.forEach.call(els, function (el) {
            if (el) {
                el.classList.add('witcher-style');
            }
        });
        let chat = document.getElementById('chat-log');
        if (chat) {
            chat.classList.add('witcher-style');
        }
    }

    registerSocketListeners();
    deprecationWarnings();
});

Hooks.once('polyglot.init', LanguageProvider => {
    class FictionalGameSystemLanguageProvider extends LanguageProvider {
        languages = {
            common: { label: 'Common', font: 'Thorass' },
            dwarven: { label: 'Dwarven', font: 'Dethek' },
            elder: { label: 'Elder Speech', font: 'Espruar' }
        };

        async i18nInit() {
            this.languages.common.label = game.i18n.localize('WITCHER.languages.common');
            this.languages.dwarven.label = game.i18n.localize('WITCHER.languages.dwarven');
            this.languages.elder.label = game.i18n.localize('WITCHER.languages.elder');
            return super.i18nInit();
        }

        getUserLanguages(actor) {
            let known_languages = new Set();
            let literate_languages = new Set();
            known_languages.add('common');
            if (
                actor.system.skills.int.eldersp.isProfession ||
                actor.system.skills.int.eldersp.isPickup ||
                actor.system.skills.int.eldersp.isLearned ||
                actor.system.skills.int.eldersp.modifiedValue > 0
            ) {
                known_languages.add('elder');
            }
            if (
                actor.system.skills.int.dwarven.isProfession ||
                actor.system.skills.int.dwarven.isPickup ||
                actor.system.skills.int.dwarven.isLearned ||
                actor.system.skills.int.dwarven.modifiedValue > 0
            ) {
                known_languages.add('dwarven');
            }
            if (
                actor.system.skills.int.commonsp.isProfession ||
                actor.system.skills.int.commonsp.isPickup ||
                actor.system.skills.int.commonsp.isLearned ||
                actor.system.skills.int.commonsp.modifiedValue > 0
            ) {
                known_languages.add('common');
            }
            return [known_languages, literate_languages];
        }
    }
    game.polyglot.api.registerSystem(FictionalGameSystemLanguageProvider);
});

Hooks.on('getChatMessageContextOptions', ApplyDamage.addDamageMessageContextOptions);
Hooks.on('getChatMessageContextOptions', VerbalCombat.addVerbalCombatMessageContextOptions);
Hooks.on('getChatMessageContextOptions', VerbalCombatDefense.addVerbalCombatDefenseMessageContextOptions);
Hooks.on('getChatMessageContextOptions', Combat.addDefenseOptionsContextMenu);
Hooks.on('getChatMessageContextOptions', Combat.addCritMessageContextOptions);
Hooks.on('getChatMessageContextOptions', Fumble.addFumbleContextOptions);

/**
 * Create a Macro from an Item drop.
 * Get an existing item macro if one exists, otherwise create a new one.
 * @param {Object} data     The dropped data
 * @param {number} slot     The hotbar slot to use
 * @returns {Promise}
 */
async function createMacro(data, slot) {
    if (!data.uuid.includes('Actor.') && !data.uuid.includes('Token.')) {
        return ui.notifications.warn(game.i18n.localize('WITCHER.Macro.ownedItemsOnly'));
    }

    let item = fromUuidSync(data.uuid);

    let command = `actor = fromUuidSync('${item.parent.uuid}'); actor.useItem("${item.id}")`;

    let macro = game.macros.find(m => m.name === item.name && m.command === command);

    if (!macro) {
        macro = await Macro.create({
            name: item.name,
            type: 'script',
            img: item.img,
            command: command
        });
    }
    game.user.assignHotbarMacro(macro, slot);
}

registerHandelbarHelpers();
