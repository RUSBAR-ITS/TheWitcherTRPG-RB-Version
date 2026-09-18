import { calculateParameter } from '../activeEffect/parameterCalculation.js';
import { prepareParameterInputs } from './parameterPreparation.js';
import { derivedStatBase, isManualDerivedStat } from '../data/actor/derivedStatData.js';

/** Re-evaluate source rows for an edge, retaining exclusions from every later edge. */
export function derivedStatInput(actor, key, excluded, uninjured = false) {
    const target = `system.stats.${key}`;
    const { inputs, contexts } = prepareParameterInputs(actor);
    const input = inputs.get(target);
    const changes = [...input.changes, ...(uninjured ? [] : contexts.get(target) ?? [])]
        .filter(change => !change.excludedDerived?.some(key => excluded.includes(key)));
    return calculateParameter({ ...input, changes }).value;
}

/** No source writes and no recalculation of native effect phases. */
export function calculateDerivedParameter(actor, key, { excluded = [], uninjured = false, store = true } = {}) {
    const target = `system.derivedStats.${key}`;
    const { inputs } = prepareParameterInputs(actor);
    const input = inputs.get(target);
    // Wound state must not lower its own activation threshold through WILL penalties.
    if (key === 'woundTreshold') uninjured = true;
    const path = [...excluded, key];
    const base = isManualDerivedStat(key, actor.system.customStat) ? input.base : derivedStatBase(key,
        stat => derivedStatInput(actor, stat, path, uninjured),
        derived => calculateDerivedParameter(actor, derived, { excluded: path, uninjured, store: false }).value);
    // A row on this node is excluded only by its consumers, not by the node itself.
    const changes = input.changes.filter(change => !change.excludedDerived?.some(key => excluded.includes(key)));
    const result = calculateParameter({ ...input, base: base + input.nativeOffset, changes });
    if (store) actor.parameterModifiers.set(target, { ...result, input, base });
    return { ...result, base };
}
