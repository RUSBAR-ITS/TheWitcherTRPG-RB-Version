/** Source data only: prepared duration/changes must never be copied back to a template. */
export function serializeEffect(effect) {
    return foundry.utils.deepClone(effect.toObject?.() ?? effect);
}

export function validateEffectDuration(duration) {
    if (duration == null) return;
    if (!Number.isSafeInteger(duration) || duration < 0) {
        throw new Error(game.i18n.localize('WITCHER.EffectApplication.invalidDuration'));
    }
}

export function appliedEffectData(effect, duration) {
    validateEffectDuration(duration);
    const data = serializeEffect(effect);
    delete data._id;
    delete data._stats;
    delete data.start;
    data.system ??= {};
    for (const flag of ['applySelf', 'applyOnTarget', 'applyOnHit', 'applyOnDamage']) {
        if (flag in data.system) data.system[flag] = false;
    }
    data.duration ??= {};
    data.duration.expired = false;
    if (duration != null) {
        data.duration.value = duration;
        data.duration.units = 'rounds';
        data.duration.expiry ??= 'turnStart';
    }
    return data;
}

/** Native core initializes Actor effects, but not effects embedded in an Item. */
export function initializeEffectStart(data, actor) {
    if (!actor || data.start != null) return data;
    data.start = foundry.documents.ActiveEffect.implementation.getEffectStart();
    const combat = game.combat?.started ? game.combat : null;
    const combatant = combat?.getCombatantsByActor(actor)[0];
    if (!combatant || combatant.turnNumber == null) return data;
    data.start.combatant = combatant.id;
    data.start.initiative = combatant.initiative;
    const { units, value, expiry } = data.duration ?? {};
    if (units === 'rounds' && Number.isFinite(value) && ['turnStart', 'turnEnd'].includes(expiry)) {
        if (combatant.turnNumber > combat.turn || (expiry === 'turnEnd' && combatant.turnNumber === combat.turn)) {
            data.duration.value = Math.max(0, value - 1);
        }
    }
    return data;
}

export function requireEffectWrite(documents, count) {
    if (documents?.length === count) return documents;
    const message = game.i18n.localize('WITCHER.EffectApplication.writeFailed');
    ui.notifications.error(message);
    throw new Error(message);
}
