import { deliverActorEffects, notifyEffectDelivery, resolveEffectSource } from '../effectDelivery.js';

export async function applyActiveEffectToTargets(activeEffects, duration) {
    const results = [];
    for (const target of game.user.targets) {
        results.push(await applyActiveEffectToActor(target.actor.uuid, activeEffects, duration));
    }
    return results;
}

export async function applyActiveEffectToActorViaId(actorUuid, itemUuid, applyWhen, duration) {
    const source = await resolveEffectSource(itemUuid, applyWhen);
    if (source.state !== 'complete') return notifyEffectDelivery(source);
    return applyActiveEffectToActor(actorUuid, source.effects, duration);
}

export async function applyActiveEffectToActor(actorUuid, activeEffects = [], duration) {
    return notifyEffectDelivery(await deliverActorEffects(actorUuid, [
        { kind: 'activeEffects', effects: activeEffects, duration }
    ]));
}
