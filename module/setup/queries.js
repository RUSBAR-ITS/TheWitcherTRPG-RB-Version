import {
    applyActiveEffectToActor,
    applyActiveEffectToActorViaId
} from '../scripts/temporaryEffects/applyActiveEffect.js';
import { applyStatusEffectToActor } from '../scripts/statusEffects/applyStatusEffect.js';

const system = 'TheWitcherTRPG-RB-Version';

async function applyTemporaryItemImprovementsToActor(queryData, { timeout }) {
    let actor = fromUuidSync(queryData.actorUuid);
    await actor.applyTemporaryItemImprovements(queryData.effects, queryData.duration);
    return true;
}

async function query(queryData, { timeout }) {
    let callableFunctions = {
        applyStatusEffectToActor,
        applyActiveEffectToActor,
        applyActiveEffectToActorViaId
    };

    let callableEntityFunctions = [
        //Actor
        'addItem',
        'applyTemporaryItemImprovements',
        'addAdrenaline',
        //Item
        'restoreReliability',
        //Region
        'addBehaviorsToRegionUuids'
    ];

    if (queryData.function in callableFunctions) {
        await callableFunctions[queryData.function](...queryData.data);
        return true;
    }

    if (callableEntityFunctions.includes(queryData.function)) {
        let entity = fromUuidSync(queryData.uuid);
        await entity[queryData.function]?.(...queryData.data);
        await entity.system[queryData.function]?.(...queryData.data);
        return true;
    }

    return false;
}

export function registerQueries() {
    CONFIG.queries[`${system}.applyTemporaryItemImprovements`] = applyTemporaryItemImprovementsToActor;
    CONFIG.queries[`${system}.query`] = query;
}
