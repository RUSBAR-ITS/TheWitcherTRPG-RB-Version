import { retainedBaseLimit } from './parameterAdvancement.js';
import { prepareParameterInputs } from './parameterPreparation.js';
import { RESOURCE_STATS } from '../data/actor/derivedStatData.js';

export const PARAMETER_INTERNAL = Symbol('witcherParameterPersistence');
const operations = new WeakMap();

export function parameterActor(document) {
    if (document?.documentName === 'Actor') return document;
    return document?.actor ?? (document?.parent ? parameterActor(document.parent) : null);
}

export function parameterSnapshot(actor) {
    if (!actor || actor._parameterPreview || !['character', 'monster'].includes(actor.type)) return null;
    const limits = new Map();
    for (const [target, input] of prepareParameterInputs(actor).inputs) {
        if (target.startsWith('system.skills.') || (target.startsWith('system.stats.') && !target.endsWith('.toxicity'))) {
            limits.set(target, retainedBaseLimit(input));
        }
    }
    const maxima = new Map([...RESOURCE_STATS.map(key => `system.derivedStats.${key}`),
        'system.stats.luck', 'system.stats.toxicity'].map(path => [path, foundry.utils.getProperty(actor, path).max]));
    return { limits, maxima };
}

/** Compare completed inputs, never a render or an intermediate remove in a replacement. */
export function parameterCorrections(before, actor) {
    if (!before) return {};
    const patch = {};
    for (const [target, input] of prepareParameterInputs(actor).inputs) {
        if (!before.limits.has(target)) continue;
        const limit = retainedBaseLimit(input);
        const sourcePath = target + (target.startsWith('system.stats.') ? '.unmodifiedMax' : '.value');
        const base = foundry.utils.getProperty(actor._source, sourcePath);
        if (limit < before.limits.get(target) && base > limit) patch[sourcePath] = limit;
    }
    for (const [path, previous] of before.maxima) {
        const maximum = foundry.utils.getProperty(actor, path).max;
        const current = foundry.utils.getProperty(actor._source, `${path}.value`);
        if (Number.isFinite(maximum) && maximum < previous && current > maximum) patch[`${path}.value`] = maximum;
    }
    return patch;
}

/** Preview runs ordinary preparation, but must never apply armor statuses or write Documents. */
export function prepareParameterUpdate(actor, patch = {}, before = parameterSnapshot(actor)) {
    if (!before) return patch;
    let update = foundry.utils.deepClone(patch);
    const seen = new Set();
    for (;;) {
        const preview = actor.clone(update, { keepId: true, parameterPreview: true });
        preview.validate({ strict: true });
        const correction = parameterCorrections(before, preview);
        if (!Object.keys(correction).length) return update;
        const signature = JSON.stringify(correction);
        if (seen.has(signature)) throw new Error('Parameter normalization did not converge');
        seen.add(signature);
        update = foundry.utils.mergeObject(update, correction, { inplace: false });
    }
}

export function inParameterOperation(actor) {
    return operations.has(actor);
}

/** A local nesting boundary, not a lock across users. Outer callers own the final correction. */
export async function withParameterChanges(actor, action) {
    if (!actor || inParameterOperation(actor)) return action();
    const before = parameterSnapshot(actor);
    if (!before) return action();
    operations.set(actor, before);
    try {
        return await action();
    } finally {
        try {
            const patch = prepareParameterUpdate(actor, {}, before);
            if (Object.keys(patch).length) {
                const saved = await actor.update(patch, { [PARAMETER_INTERNAL]: true });
                if (!saved) throw new Error('Parameter correction was cancelled');
            }
        } catch (error) {
            ui.notifications.error(game.i18n.localize('WITCHER.ParameterAdvancement.correctionFailed'));
            throw error;
        } finally {
            operations.delete(actor);
        }
    }
}
