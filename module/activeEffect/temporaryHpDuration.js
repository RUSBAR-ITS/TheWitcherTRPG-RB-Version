import { withParameterChanges } from '../actor/parameterPersistence.js';

const operations = new Map();
const clockOf = effect => effect.system?.temporaryHpDuration;

export function temporaryHpCombat(actor) {
    const combats = [...(game.combats ?? [])];
    const active = game.combat;
    if (active) combats.sort((a, b) => Number(b === active) - Number(a === active));
    return combats.find(combat => combat.started && combat.getCombatantsByActor(actor).length) ?? null;
}

/** Each created instance gets its own combat start; templates never keep an old binding. */
export function initialTemporaryHpClock(clock, actor) {
    const result = { ...clock, combatId: null, combatantId: null, startRound: null };
    const combat = clock.unit === 'rounds' && actor ? temporaryHpCombat(actor) : null;
    if (combat) Object.assign(result, { combatId: combat.id,
        combatantId: combat.getCombatantsByActor(actor)[0].id, startRound: combat.round });
    return result;
}

/** Local label only: native world-time expiration does not own these effects. */
export function temporaryHpDuration(effect, duration) {
    const clock = clockOf(effect);
    if (!clock) return null;
    let value = clock.value;
    let state = 'manual';
    if (clock.unit === 'rounds') {
        const combat = clock.combatId ? game.combats.get(clock.combatId) : null;
        state = combat?.started ? 'combat' : 'waitingCombat';
        if (combat?.started && Number.isFinite(clock.startRound)) value -= Math.max(0, combat.round - clock.startRound);
    }
    const label = game.i18n.format('WITCHER.TemporaryHP.durationLabel', {
        value, unit: game.i18n.localize(`WITCHER.TemporaryHP.${clock.unit}`),
        state: game.i18n.localize(`WITCHER.TemporaryHP.${state}`)
    });
    return { ...duration, value: null, expiry: null, expired: false,
        seconds: Infinity, secondsRemaining: Infinity, remaining: Infinity, label };
}

export async function reconcileTemporaryHp(actor, { endedCombatId = null } = {}) {
    if (!game.users.activeGM?.isSelf || !actor) return;
    return withParameterChanges(actor, async () => {
        for (const effect of actor.allApplicableEffects()) {
            let clock = clockOf(effect);
            if (!clock || clock.unit !== 'rounds') continue;
            let remove = clock.combatId && (clock.combatId === endedCombatId || !game.combats.get(clock.combatId)?.started);
            if (!remove && !effect.disabled && !effect.isSourceSuppressed) {
                if (!clock.combatId) {
                    const initial = initialTemporaryHpClock(clock, actor);
                    if (initial.combatId) {
                        if (!await effect.update({ 'system.temporaryHpDuration': initial })) {
                            throw new Error(game.i18n.localize('WITCHER.EffectApplication.writeFailed'));
                        }
                        clock = initial;
                    }
                }
                const combat = clock.combatId ? game.combats.get(clock.combatId) : null;
                remove = combat?.started && Number.isFinite(clock.startRound) &&
                    Math.max(0, combat.round - clock.startRound) >= clock.value;
            }
            if (remove && !await effect.delete()) throw new Error(game.i18n.localize('WITCHER.EffectApplication.writeFailed'));
        }
    });
}

function actorsForTemporaryHp(combat) {
    const actors = new Map();
    const include = actor => { if (actor) actors.set(actor.uuid, actor); };
    for (const actor of game.actors ?? []) include(actor);
    for (const scene of game.scenes ?? []) for (const token of scene.tokens) include(token.actor);
    for (const combatant of combat?.combatants ?? []) include(combatant.actor);
    return [...actors.values()].filter(actor => [...actor.allApplicableEffects()].some(effect => clockOf(effect)));
}

function refreshActor(actor, options) {
    if (!actor) return;
    for (const effect of actor.allApplicableEffects()) if (clockOf(effect)) effect.updateDuration();
    actor.render(false);
    if (!game.users.activeGM?.isSelf) return;
    const previous = operations.get(actor.uuid) ?? Promise.resolve();
    const next = previous.catch(() => {}).then(() => reconcileTemporaryHp(actor, options)).catch(error => {
        console.error('Witcher temporary HP duration', error);
        ui.notifications.error(game.i18n.localize('WITCHER.TemporaryHP.errors.clock'));
    });
    operations.set(actor.uuid, next);
    void next.finally(() => { if (operations.get(actor.uuid) === next) operations.delete(actor.uuid); });
}

export function registerTemporaryHpHooks() {
    const refreshAll = (combat, options) => actorsForTemporaryHp(combat).forEach(actor => refreshActor(actor, options));
    Hooks.on('updateCombat', (combat, change) => {
        if (Object.hasOwn(change, 'round') || Object.hasOwn(change, 'turn')) refreshAll(combat);
    });
    Hooks.on('createCombatant', combatant => refreshActor(combatant.actor));
    Hooks.on('deleteCombat', combat => refreshAll(combat, { endedCombatId: combat.id }));
    Hooks.on('createActiveEffect', effect => { if (clockOf(effect)) refreshActor(effect.actor); });
    Hooks.on('updateActiveEffect', (effect, change) => {
        if (clockOf(effect) && Object.hasOwn(change, 'disabled')) refreshActor(effect.actor);
    });
    Hooks.once('ready', () => refreshAll());
    Hooks.on('userConnected', () => refreshAll());
}
