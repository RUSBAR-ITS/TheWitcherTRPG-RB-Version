import { resolveRollTarget } from '../actor/rollContext.js';
import { resolveSkillIdentity } from '../item/skillIdentity.js';

const fail = (key, data = {}) => { throw new Error(game.i18n.format(`WITCHER.TemporaryHP.errors.${key}`, data)); };

/** Read a parameter, never the complete check contribution or a current resource. */
export function resolveTemporaryHpReference(reference, { source, target, ability }) {
    const actor = reference.role === 'source' ? source : reference.role === 'target' ? target : null;
    if (!actor || !['base', 'effective'].includes(reference.value)) return fail('reference');
    let address = reference.target;
    if (address?.kind === 'ability') {
        if (reference.role !== 'source') return fail('reference');
        address = ability;
    } else if (['item', 'profession'].includes(address?.kind)) address = resolveSkillIdentity(actor, address);
    if (!['stat', 'builtin', 'item', 'profession'].includes(address?.kind)) return fail('reference');
    let resolved;
    try { resolved = resolveRollTarget(actor, address); } catch { return fail('reference'); }
    let value;
    if (reference.value === 'effective') value = actor.parameterModifiers?.get(resolved.id)?.value ?? resolved.value;
    else if (address.kind === 'stat') value = foundry.utils.getProperty(actor._source, `${resolved.id}.unmodifiedMax`);
    else if (address.kind === 'builtin') value = foundry.utils.getProperty(actor._source, `${resolved.id}.value`);
    else {
        const item = actor.items.get(address.itemId);
        value = foundry.utils.getProperty(item._source ?? item, address.kind === 'item' ? 'system.value' : `system.${address.path}.level`);
    }
    if (!Number.isFinite(value)) return fail('reference');
    return value;
}

/** Only used aliases are resolved; unused configuration does not constrain the target. */
export function temporaryHpFormulaData(config, context) {
    const data = {};
    for (const formula of [config.temporaryHp.value, config.temporaryHp.duration]) {
        for (const match of String(formula).matchAll(/@([A-Za-z0-9_.]+)/g)) {
            const alias = match[1];
            if (!/^p[1-9][0-9]*$/.test(alias) || !Object.hasOwn(config.references ?? {}, alias)) return fail('unknownReference', { alias });
            if (!Object.hasOwn(data, alias)) data[alias] = resolveTemporaryHpReference(config.references[alias], context);
        }
    }
    return data;
}

export function validateTemporaryHpFormulas(config) {
    for (const [field, formula] of Object.entries(config.temporaryHp)) {
        if (!['value', 'duration'].includes(field)) continue;
        if (!String(formula).trim() || !Roll.validate(String(formula))) return fail('formula', { field: game.i18n.localize(`WITCHER.TemporaryHP.${field === 'value' ? 'amount' : 'duration'}`), formula });
    }
}

/** Inject the evaluator in isolated tests; production always uses native Foundry Roll. */
export async function calculateTemporaryHp(config, data, rollOver = 0, evaluate = async (formula, values) => {
    const roll = await new Roll(formula, values).evaluate();
    return { total: roll.total, roll };
}) {
    if (!['fixed', 'perPoint'].includes(config.mode) || !['up', 'down'].includes(config.rounding)) return fail('configuration');
    if (!['rounds', 'minutes', 'hours', 'days'].includes(config.durationUnit)) return fail('configuration');
    const points = config.mode === 'fixed' ? 1 : Math.max(0, Math.floor(Math.min(rollOver, config.difficultyCheck.maxRollOver)));
    if (!Number.isFinite(points)) return fail('configuration');
    const rolls = [];
    const evaluateField = async field => {
        let result;
        try { result = await evaluate(config.temporaryHp[field], data); }
        catch { return fail('formula', { field: game.i18n.localize(`WITCHER.TemporaryHP.${field === 'value' ? 'amount' : 'duration'}`), formula: config.temporaryHp[field] }); }
        if (!Number.isFinite(result.total)) return fail('formula', { field: game.i18n.localize(`WITCHER.TemporaryHP.${field === 'value' ? 'amount' : 'duration'}`), formula: config.temporaryHp[field] });
        if (result.roll) rolls.push(result.roll);
        return result.total;
    };
    let total = 0;
    for (let point = 0; point < points; point++) total += await evaluateField('value');
    const value = config.rounding === 'up' ? Math.ceil(total) : Math.floor(total);
    if (!Number.isFinite(value)) return fail('formula', { field: game.i18n.localize('WITCHER.TemporaryHP.amount'), formula: config.temporaryHp.value });
    const duration = await evaluateField('duration');
    return { value, duration, unit: config.durationUnit, points, rolls };
}
