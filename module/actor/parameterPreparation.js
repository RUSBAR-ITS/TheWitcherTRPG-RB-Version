import { RESOURCE_STATS } from '../data/actor/derivedStatData.js';
import { calculateParameter } from '../activeEffect/parameterCalculation.js';
import { modifierSettings, supportsModifierChange } from '../activeEffect/modifierContext.js';

const states = new WeakMap();
const numericField = new foundry.data.fields.NumberField({ nullable: true });

/** Numeric parameters use one calculation; current resource pools stay native. */
export function parameterTarget(change) {
    if (!supportsModifierChange(change) || !['initial', 'final'].includes(change.phase)) return null;
    const stat = /^system\.stats\.(int|ref|dex|body|spd|emp|cra|will|luck|toxicity)\.(max|value|totalModifiers)$/.exec(change.key);
    if (stat) {
        if (['luck', 'toxicity'].includes(stat[1]) && stat[2] === 'value') return null;
        return `system.stats.${stat[1]}`;
    }
    const derived = /^(system\.derivedStats\.([^.]+))\.(max|value|totalModifiers)$/.exec(change.key);
    if (derived) return RESOURCE_STATS.includes(derived[2]) && derived[3] === 'value' ? null : derived[1];
    const rollTarget = /^(system\.(?:skillGroupModifiers\.[^.]+|combatEffects\.(?:attackModifier|defenseModifier)\.[^.]+|lifepathModifiers\.attacks\.(?:strong|joint)))\.value$/.exec(change.key);
    if (rollTarget) return rollTarget[1];
    return /^(system\.skills\.[^.]+\.[^.]+)\.(value|activeEffectModifiers)$/.exec(change.key)?.[1] ?? null;
}

export function routesParameterChange(actor, change) {
    return actor && !['loot', 'mystery'].includes(actor.type) && typeof actor.calculateStats === 'function' &&
        !!parameterTarget(change) && !ActiveEffect.CHANGE_TYPES[change.type]?.handler &&
        !!foundry.utils.getProperty(actor, parameterTarget(change));
}

/** Reset only transient calculations. The saved Actor/Item/AE source is untouched. */
export function resetParameterPreparation(actor) {
    states.delete(actor);
    actor.parameterModifiers = new Map();
}

/** Collect both phases once, before numerical consumers, retaining each row's origin. */
export function prepareParameterInputs(actor) {
    if (states.has(actor)) return states.get(actor);
    const inputs = new Map();
    for (const [key, stat] of Object.entries(actor.system.stats)) {
        inputs.set(`system.stats.${key}`, {
            base: stat.max, advancementBase: stat.unmodifiedMax,
            min: key === 'toxicity' ? null : 1,
            cap: key === 'toxicity' ? null : stat.baseCap ?? 10,
            changes: stat.totalModifiers ? [{ type: 'add', value: stat.totalModifiers, affectsParameter: true }] : []
        });
    }
    for (const [attribute, group] of Object.entries(actor.system.skills)) {
        for (const [key, skill] of Object.entries(group)) {
            inputs.set(`system.skills.${attribute}.${key}`, {
                base: skill.value, advancementBase: skill.value, min: null, cap: skill.baseCap ?? 10,
                changes: skill.activeEffectModifiers ? [
                    { type: 'add', value: skill.activeEffectModifiers, affectsParameter: true }
                ] : []
            });
        }
    }
    for (const [key, stat] of Object.entries(actor.system.derivedStats)) {
        inputs.set(`system.derivedStats.${key}`, {
            base: stat.unmodifiedMax, nativeOffset: stat.max - stat.unmodifiedMax,
            min: key === 'stun' ? 1 : null, cap: key === 'stun' ? 10 : null,
            changes: stat.totalModifiers ? [{ type: 'add', value: stat.totalModifiers, affectsParameter: true }] : []
        });
    }
    for (const path of ['system.skillGroupModifiers', 'system.combatEffects.attackModifier',
        'system.combatEffects.defenseModifier', 'system.lifepathModifiers.attacks']) {
        for (const [key, modifier] of Object.entries(foundry.utils.getProperty(actor, path) ?? {})) {
            inputs.set(`${path}.${key}`, { base: modifier.value, min: null, cap: null, changes: [] });
        }
    }
    const rollData = actor.getRollData();
    for (const effect of actor.allApplicableEffects()) {
        if (!effect.active || effect.type !== 'base') continue;
        const replacementData = effect.getReplacementData(rollData);
        for (const [index, change] of effect.system.changes.entries()) {
            if (!routesParameterChange(actor, change) || !effect.shouldApplyChange(change, {
                phase: change.phase, replacementData, witcherNumeric: true
            })) continue;
            const input = inputs.get(parameterTarget(change));
            if (!input) continue;
            // Native formula substitution/evaluation, with a fractional NumberField.
            // Null is the failure sentinel: an invalid multiplier never becomes zero.
            const value = numericField.applyChange(null, actor, { ...change, type: 'override', effect }, { replacementData });
            if (!Number.isFinite(value)) continue;
            input.changes.push({ ...change, ...modifierSettings(change), value,
                source: effect.uuid, sourceName: effect.name, index });
        }
    }
    const state = { inputs, contexts: new Map() };
    states.set(actor, state);
    actor.parameterModifiers = new Map();
    return state;
}

/** Stored result is reusable by derived/roll/progression stages, not an Actor update. */
export function calculateActorParameter(actor, target, contextualChanges = []) {
    const state = prepareParameterInputs(actor);
    const input = state.inputs.get(target);
    if (!input) return null;
    const result = calculateParameter({ ...input, changes: [...input.changes, ...contextualChanges] });
    state.contexts.set(target, contextualChanges);
    actor.parameterModifiers.set(target, { ...result, input, contextualChanges });
    return result;
}

export function prepareSkillParameters(actor) {
    const { inputs } = prepareParameterInputs(actor);
    for (const [path, input] of inputs) {
        if (/^system\.(skillGroupModifiers|combatEffects|lifepathModifiers)\./.test(path)) {
            foundry.utils.getProperty(actor, path).value = calculateActorParameter(actor, path).value;
            continue;
        }
        if (!path.startsWith('system.skills.')) continue;
        const result = calculateActorParameter(actor, path);
        const skill = foundry.utils.getProperty(actor, path);
        skill.value = input.base;
        skill.activeEffectModifiers = result.value - input.base;
    }
}
