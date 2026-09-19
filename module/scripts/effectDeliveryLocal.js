import { appliedEffectData, serializeEffect } from '../activeEffect/effectApplication.js';

/** These primitives write locally and never select another client. */
export async function applyLocalActiveEffects(actor, effects, duration) {
    const sources = effects.map(serializeEffect);
    const improvements = await actor.applyTemporaryItemImprovements(sources, duration);
    const data = sources.filter(effect => effect.type !== 'temporaryItemImprovement')
        .map(effect => appliedEffectData(effect, duration));
    const created = data.length ? await actor.createEmbeddedDocuments('ActiveEffect', data) : [];
    // Family coalescing can reduce the count; the registered document class checks the actual writes.
    if ((data.length && !created?.length)
        || (sources.some(effect => effect.type === 'temporaryItemImprovement') && !improvements?.length)) {
        throw new Error('Effect creation did not return documents');
    }
    return {
        state: 'complete', reason: sources.length ? 'applied' : 'empty',
        effectUuids: [...(improvements ?? []), ...created].map(effect => effect.uuid)
    };
}

function hasStatus(actor, statusId) {
    return actor.appliedEffects.some(effect => effect.statuses.has(statusId));
}

export async function applyLocalStatus(actor, statusId, duration) {
    if (!statusId) return { state: 'complete', reason: 'empty' };
    if (hasStatus(actor, statusId)) return { state: 'complete', reason: 'present' };

    await actor.toggleStatusEffect(statusId, { active: true });
    if (!hasStatus(actor, statusId)) throw new Error('Status activation was not confirmed');
    await handleStatusCounterIntegration(actor, statusId, duration);

    if (actor.system.statusEffectImmunities?.includes(statusId)) {
        // Keep the existing visible attempt, but await its removal as part of this operation.
        await new Promise(resolve => setTimeout(resolve, 1000));
        await actor.toggleStatusEffect(statusId, { active: false });
        if (hasStatus(actor, statusId)) throw new Error('Immune status removal was not confirmed');
        return { state: 'complete', reason: 'immune' };
    }
    return { state: 'complete', reason: 'applied' };
}

async function handleStatusCounterIntegration(target, statusId, duration) {
    if (!game.modules.get('statuscounter')?.active) return;
    if (!duration || duration == 0) return;

    // The legacy counter lookup (issue-00003) is outside this delivery refactoring.
    let statusEffect = CONFIG.WITCHER.statusEffects.querySelector(statusEffect => statusEffect.id == statusId);
    let effectCounter = EffectCounter.getAllCounters(target).querySelector(effects => effects.path == statusEffect.img);
    await effectCounter.setValue(parseInt(duration));
    await effectCounter.changeType('statuscounter.countdown_round', target);
}
