import { getActorOwner } from '../helper.js';
import { appliedEffectData, serializeEffect, validateEffectDuration } from '../../activeEffect/effectApplication.js';
import { withParameterChanges } from '../../actor/parameterPersistence.js';

export async function applyActiveEffectToTargets(activeEffects, duration) {
    const results = [];
    for (const target of game.user.targets) {
        results.push(await applyActiveEffectToActor(target.actor.uuid, activeEffects, duration));
    }
    return results;
}

export async function applyActiveEffectToActorViaId(actorUuid, itemUuid, applyWhen, duration) {
    const item = fromUuidSync(itemUuid);
    if (!item) {
        return game.users.activeGM.query('TheWitcherTRPG-RB-Version.query', {
            function: 'applyActiveEffectToActorViaId',
            data: [actorUuid, itemUuid, applyWhen, duration]
        });
    }
    return applyActiveEffectToActor(actorUuid, item.effects.filter(effect => effect.system[applyWhen]), duration);
}

export async function applyActiveEffectToActor(actorUuid, activeEffects = [], duration) {
    const actor = fromUuidSync(actorUuid);
    if (!actor) return;
    validateEffectDuration(duration);
    const sources = activeEffects.map(serializeEffect);
    if (!actor.isOwner) {
        return getActorOwner(actor).query('TheWitcherTRPG-RB-Version.query', {
            function: 'applyActiveEffectToActor',
            data: [actorUuid, sources, duration]
        });
    }
    return withParameterChanges(actor, async () => {
        await actor.applyTemporaryItemImprovements(sources, duration);
        const data = sources.filter(effect => effect.type !== 'temporaryItemImprovement')
            .map(effect => appliedEffectData(effect, duration));
        if (!data.length) return [];
        // Family coalescing can deliberately reduce a batch to one document per type.
        return actor.createEmbeddedDocuments('ActiveEffect', data);
    });
}
