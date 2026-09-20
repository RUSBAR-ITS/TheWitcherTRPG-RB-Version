import { registerTemporaryHpHooks } from '../activeEffect/temporaryHpDuration.js';
import { applyGeneralCombatHooks } from '../scripts/combat/generalCombatHook.js';
import { countdownDurationOfRegions } from '../scripts/regions/regionHooks.js';

export function registerHooks() {
    registerTemporaryHpHooks();
    Hooks.on('updateCombat', (combat, update, options, userId) => {
        combatHooks(combat, update, options, userId);
    });
}

// Only a real forward turn transition triggers periodic work. Initiative edits,
// flags, rewinds and resets are not turns; skipped turns are not replayed.
export function isForwardCombatTurn(combat, update, options = {}) {
    if (!game.user.isActiveGM || !combat.started || options.turnEvents === false || options.direction === -1) {
        return false;
    }
    if (!Object.hasOwn(update, 'round') && !Object.hasOwn(update, 'turn')) return false;
    if (Object.hasOwn(update, 'combatants')) return false;
    const { previous, current } = combat;
    if (!previous || !current || current.turn === null) return false;
    if (!combat.combatants.get(current.combatantId)?.actor) return false;
    return current.round > previous.round ||
        (current.round === previous.round && current.turn > (previous.turn ?? -1));
}

function combatHooks(combat, update, options, userId) {
    if (!isForwardCombatTurn(combat, update, options)) return;
    applyGeneralCombatHooks(combat);
    countdownDurationOfRegions(combat, update, options, userId);
}
