import { calculateParameter } from '../activeEffect/parameterCalculation.js';

const localize = value => value ? game.i18n.localize(value) : '';
const number = value => {
    const result = Number(value ?? 0);
    if (!Number.isFinite(result)) throw new TypeError('A roll contribution must be finite');
    return result;
};

/** Names are labels only. Item and profession addresses always resolve on this Actor. */
export function resolveRollTarget(actor, target) {
    if (!target) return null;
    if (target.kind === 'builtin') {
        const entry = CONFIG.WITCHER.skillMap[target.key];
        const model = entry && actor.system.skills[entry.attribute.name]?.[target.key];
        if (model) return { id: `system.skills.${entry.attribute.name}.${target.key}`, model,
            stat: entry.attribute.name, skill: target.key, value: model.modifiedValue ??
                number(model.value) + number(model.activeEffectModifiers), label: localize(entry.rollLabel ?? entry.label) };
    } else if (target.kind === 'item' || target.kind === 'profession') {
        const item = actor.items.get(target.itemId);
        if (target.kind === 'item' && item?.type === 'skill') return {
            id: `Item.${item.id}`, model: item.system, stat: item.system.attribute,
            value: item.system.modifiedValue ?? Math.min(item.system.baseCap ?? 10,
                number(item.system.value) + number(item.system.activeEffectModifiers)), label: item.name
        };
        if (target.kind === 'profession' && item?.type === 'profession' &&
            /^(definingSkill|skillPath[1-3]\.skill[1-3])$/.test(target.path)) {
            const model = foundry.utils.getProperty(item.system, target.path);
            if (model) return { id: `Item.${item.id}.${target.path}`, model, stat: model.stat,
                value: Math.min(model.baseCap ?? 10, number(model.level) + number(model.activeEffectModifiers)), label: model.skillName };
        }
    } else if (target.kind === 'stat' || target.kind === 'derived') {
        const group = target.kind === 'stat' ? 'stats' : 'derivedStats';
        const model = Object.hasOwn(actor.system[group], target.key) && actor.system[group][target.key];
        if (model) return { id: `system.${group}.${target.key}`, model,
            value: number(model.max), label: localize(model.label ?? CONFIG.WITCHER.statMap[target.key]?.label) };
    }
    throw new TypeError('Unknown roll target address');
}

/** Snapshot one check; includeStat=false preserves checks explicitly omitting the attribute. */
export function collectRollModifiers(actor, { target = null, stat, includeStat = true, groups = [],
    action = 'skill', strike = null, comparison = '>', threshold = null } = {}) {
    if (!['>', '>=', '<', '<='].includes(comparison)) throw new TypeError('Unknown roll comparison');
    if (threshold !== null && !Number.isFinite(threshold)) throw new TypeError('A threshold is null or a finite number');
    const resolved = resolveRollTarget(actor, target);
    const actualStat = includeStat ? stat ?? resolved?.stat : null;
    const matchingGroups = new Set(groups);
    if (resolved?.skill) {
        for (const [key, members] of Object.entries(CONFIG.WITCHER)) {
            if (Array.isArray(members) && members.includes(resolved.skill)) matchingGroups.add(key);
        }
    }
    const isSkill = ['builtin', 'item', 'profession'].includes(target?.kind);
    if (isSkill) matchingGroups.add('allSkills');
    const context = { target: target ? { ...target } : null, stat: actualStat, groups: [...matchingGroups],
        action, strike, comparison, threshold };
    const sources = new Map();
    const add = (id, value, label, role) => {
        if (sources.has(id)) return;
        const prepared = actor.parameterModifiers?.get(id);
        const input = prepared ? { ...prepared.input,
            base: prepared.base === undefined ? prepared.input.base : prepared.base + (prepared.input.nativeOffset ?? 0),
            changes: [...prepared.input.changes, ...(prepared.contextualChanges ?? [])].map(row => ({ ...row })) }
            : { base: number(value), changes: [] };
        sources.set(id, { id, label: label ?? '', role, input });
    };
    if (actualStat) {
        if (!Object.hasOwn(actor.system.stats, actualStat)) throw new TypeError('Unknown roll attribute');
        const model = actor.system.stats[actualStat];
        add(`system.stats.${actualStat}`, model.value, localize(model.label), 'base');
    }
    if (resolved) {
        add(resolved.id, resolved.value, resolved.label, 'base');
        for (const [index, modifier] of Object.entries(resolved.model.modifiers ?? {})) {
            add(`${resolved.id}.manual.${index}`, modifier.value, localize(modifier.name), 'modifier');
        }
    }
    if (isSkill) {
        for (const [key, modifier] of Object.entries(actor.system.skillGroupModifiers ?? {})) {
            if (matchingGroups.has(modifier.group)) add(`system.skillGroupModifiers.${key}`,
                modifier.value, localize(modifier.name), 'modifier');
        }
    }
    const combatKind = action === 'attack' ? 'attackModifier' : action === 'defense' ? 'defenseModifier' : null;
    if (combatKind) {
        for (const [key, modifier] of Object.entries(actor.system.combatEffects?.[combatKind] ?? {})) {
            add(`system.combatEffects.${combatKind}.${key}`, modifier.value, localize(modifier.name), 'modifier');
        }
    }
    if (action === 'attack' && ['strong', 'joint'].includes(strike)) {
        const path = `system.lifepathModifiers.attacks.${strike}`;
        const modifier = foundry.utils.getProperty(actor, path);
        if (modifier) add(path, modifier.value, localize(modifier.name), 'modifier');
    }
    const optional = new Map();
    for (const source of sources.values()) {
        for (const [index, row] of source.input.changes.entries()) {
            if (row.disabled || !row.affectsRoll || !row.optionalOnRoll) continue;
            row.selectionId = row.source ? `${row.source}:${row.index}` : `${source.id}:${index}`;
            optional.set(row.selectionId, { id: row.selectionId, label: row.sourceName || source.label || source.id,
                target: source.label || source.id, type: row.type, value: row.value });
        }
    }
    const collection = { context, sources: [...sources.values()], optional: [...optional.values()] };
    return { ...collection, automatic: resolveRollModifiers(collection) };
}

/** Recompute selected operations together; a checkbox never changes the saved effect. */
export function resolveRollModifiers(collection, selected = [], manual = 0) {
    const choices = new Set(selected);
    const contributions = [];
    for (const source of collection.sources) {
        const changes = source.input.changes.filter(row => !row.optionalOnRoll || choices.has(row.selectionId))
            .map(row => ({ ...row, optionalOnRoll: false }));
        const result = calculateParameter({ ...source.input, changes });
        const names = [...new Set(changes.filter(row => !row.disabled && row.affectsRoll)
            .map(row => row.sourceName).filter(Boolean))].join(' & ');
        contributions.push({ source: source.id, role: source.role, value: result.value, label: source.label });
        if (result.fullExtra) contributions.push({ source: source.id, role: 'modifier',
            value: result.fullExtra, label: source.label });
        if (result.rollModifier) contributions.push({ source: source.id, role: 'modifier',
            value: result.rollModifier, label: names || source.label });
    }
    const custom = number(manual);
    if (custom) contributions.push({ source: 'manual', role: 'modifier', value: custom,
        label: localize('WITCHER.Settings.Custom') });
    const baseTotal = contributions.filter(row => row.role === 'base').reduce((sum, row) => sum + row.value, 0);
    const modifierTotal = contributions.filter(row => row.role === 'modifier').reduce((sum, row) => sum + row.value, 0);
    const { threshold, comparison } = collection.context;
    return { contributions, baseTotal, modifierTotal, total: baseTotal + modifierTotal,
        threshold: threshold !== null && ['<', '<='].includes(comparison) ? threshold + modifierTotal : threshold };
}
