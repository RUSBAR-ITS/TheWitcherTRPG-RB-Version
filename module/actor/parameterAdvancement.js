import { calculateOperations, calculateParameter } from '../activeEffect/parameterCalculation.js';
import { prepareParameterInputs } from './parameterPreparation.js';

/** Largest retained acquired base. Bonuses never confiscate levels below the cap. */
export function retainedBaseLimit(input) {
    const { cap } = calculateParameter(input);
    if (cap === null) return Infinity;
    const rows = input.changes.filter(row => !row.disabled && row.affectsAdvancement);
    const intercept = calculateOperations(0, rows);
    const slope = calculateOperations(1, rows) - intercept;
    if (slope <= 0) return Math.floor(calculateOperations(input.advancementBase ?? input.base, rows)) <= cap ? Infinity : cap;
    return Math.max(cap, Math.ceil((cap + 1 - intercept) / slope) - 1);
}

export function advancementQuote(actor, target, multiplier = 1) {
    if (actor.type !== 'character') return { allowed: false, reason: 'characterOnly' };
    const input = prepareParameterInputs(actor).inputs.get(target);
    if (!input || !Number.isFinite(multiplier) || multiplier <= 0) return { allowed: false, reason: 'invalidTarget' };
    const primary = /^system\.stats\.(int|ref|dex|body|spd|emp|cra|will|luck)$/.test(target);
    if (!primary && !/^system\.skills\.[^.]+\.[^.]+$/.test(target)) return { allowed: false, reason: 'invalidTarget' };
    const sourcePath = target + (primary ? '.unmodifiedMax' : '.value');
    const base = foundry.utils.getProperty(actor._source, sourcePath);
    if (!Number.isFinite(base)) return { allowed: false, reason: 'invalidTarget' };
    const result = calculateParameter({ ...input, advancementBase: base });
    const allowed = result.cap === null || (result.value < result.cap && result.advancement < result.cap);
    return { allowed, reason: allowed ? null : 'atCap', sourcePath, base,
        cost: Math.max(result.advancement, 1) * multiplier };
}

/** One purchase = one awaited Actor update; never call the reward writer here. */
export async function purchaseParameter(actor, target, { multiplier = 1, magical = false, label = target } = {}) {
    const quote = advancementQuote(actor, target, multiplier);
    const refuse = reason => {
        ui.notifications.warn(game.i18n.localize(`WITCHER.ParameterAdvancement.${reason}`));
        return false;
    };
    if (!quote.allowed) return refuse(quote.reason);
    const source = actor._source.system;
    const ordinary = source.improvementPoints;
    const magic = magical ? source.magic?.magicImprovementPoints : 0;
    if (!Number.isFinite(ordinary) || !Number.isFinite(magic) || !Array.isArray(source.logs?.ipLog)) return refuse('invalidTarget');
    const magicCost = magical ? Math.min(Math.max(magic, 0), quote.cost) : 0;
    const ordinaryCost = quote.cost - magicCost;
    if (ordinaryCost > Math.max(ordinary, 0)) return refuse('notEnoughIP');
    const logLabel = `${game.i18n.localize(label)} ${quote.base} -> ${quote.base + 1}`;
    const log = foundry.utils.deepClone(source.logs.ipLog);
    if (magicCost) log.push({ label: logLabel, ip: -magicCost, isMagic: true });
    if (ordinaryCost) log.push({ label: logLabel, ip: -ordinaryCost, isMagic: false });
    const patch = {
        [quote.sourcePath]: quote.base + 1,
        'system.improvementPoints': ordinary - ordinaryCost,
        'system.logs.ipLog': log
    };
    if (magical) patch['system.magic.magicImprovementPoints'] = magic - magicCost;
    const saved = await actor.update(patch);
    if (!saved) return refuse('writeCancelled');
    return saved;
}
