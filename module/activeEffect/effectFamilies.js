import { serializeEffect, initializeEffectStart, requireEffectWrite } from './effectApplication.js';

const SYSTEM = 'TheWitcherTRPG-RB-Version';

export function effectFamily(effect) {
    return effect.system?.nonStacking ? effect.system.effectTypeId?.trim() : null;
}

function scopeOf(effect) {
    const parent = effect.parent;
    if (parent?.documentName === 'Actor') return parent;
    if (effect.system?.isTransferred) return parent;
    return effect.transfer ? parent?.actor : null;
}

function sources(scope) {
    if (!scope) return [];
    const effects = [...(scope.effects ?? [])];
    if (scope.documentName === 'Actor') {
        for (const item of scope.items ?? []) effects.push(...item.effects);
    }
    return effects;
}

function order(effect) {
    return Number(effect.flags?.[SYSTEM]?.applicationOrder) || 0;
}

/** No writes and no recursive use of active/isSuppressed while choosing the winner. */
export function isFamilySuppressed(effect) {
    const family = effectFamily(effect);
    const scope = scopeOf(effect);
    if (!family || !scope) return false;
    const rank = order(effect);
    return sources(scope).some(other => other !== effect && scopeOf(other) === scope &&
        effectFamily(other) === family && !other.disabled && !other.isSourceSuppressed &&
        (order(other) > rank || (order(other) === rank && String(other.id) > String(effect.id))));
}

function assignmentCounter(parent) {
    const owner = parent?.actor ?? parent;
    let next = Math.max(0, ...sources(owner).map(order));
    return () => ++next;
}

function assign(data, next) {
    if (!effectFamily(data)) return;
    data.flags ??= {};
    data.flags[SYSTEM] ??= {};
    data.flags[SYSTEM].applicationOrder = next();
}

function coalesce(data, parent) {
    const families = new Set();
    return data.toReversed().filter(row => {
        const family = effectFamily(row);
        if (!family || (parent.documentName !== 'Actor' && !row.system?.isTransferred)) return true;
        if (families.has(family)) return false;
        families.add(family);
        return true;
    }).reverse();
}

async function removeReplaced(documents, parent) {
    // Transfer sources stay on their Items. Only repeated applied instances with
    // the same parent are deleted; a different Item can become active again.
    const families = new Set(documents.filter(e =>
        (parent.documentName === 'Actor' || e.system?.isTransferred) && !e.disabled && !e.isSourceSuppressed).map(effectFamily).filter(Boolean));
    const keep = new Set(documents.map(e => e.id));
    const old = [...(parent?.effects ?? [])].filter(e => !keep.has(e.id) &&
        (parent.documentName === 'Actor' || e.system?.isTransferred) && families.has(effectFamily(e)));
    if (!old.length) return;
    const removed = await parent.deleteEmbeddedDocuments('ActiveEffect', old.map(e => e.id));
    requireEffectWrite(removed, old.length);
}

export async function createEffectDocuments(data, operation, create) {
    const parent = operation.parent;
    if (!parent || operation.pack || parent.inCompendium || (parent.documentName === 'Item' && !parent.actor)) return create(data, operation);
    const next = assignmentCounter(parent);
    const rows = coalesce(data.map(serializeEffect), parent);
    for (const row of rows) {
        assign(row, next);
        // A newly assigned family starts afresh even when imported from an active copy.
        if (effectFamily(row)) {
            row.start = null;
            if (row.duration) row.duration.expired = false;
        }
    }
    const result = await create(rows, operation);
    if (operation.dryRun) return result;
    const created = requireEffectWrite(result, rows.length);
    await removeReplaced(created, parent);
    return created;
}

export async function updateEffectDocuments(changes, operation, update) {
    const parent = operation.parent;
    if (!parent || operation.pack || parent.inCompendium || (parent.documentName === 'Item' && !parent.actor)) return update(changes, operation);
    const next = assignmentCounter(parent);
    const assigned = [];
    const rows = changes.map(change => {
        const row = foundry.utils.expandObject(serializeEffect(change));
        const previous = parent.effects.get(row._id);
        if (!previous) return row;
        const merged = foundry.utils.mergeObject(previous.toObject(), row, { inplace: false });
        const activated = previous.disabled && merged.disabled === false;
        const newFamily = effectFamily(merged) !== effectFamily(previous);
        const released = ['applySelf', 'applyOnTarget', 'applyOnHit', 'applyOnDamage']
            .some(key => previous.system[key] && merged.system[key] === false);
        if (effectFamily(merged) && (activated || newFamily || released || (!previous.transfer && merged.transfer))) {
            assign(merged, next);
            row.flags = merged.flags;
            assigned.push(row._id);
        }
        return row;
    });
    const updated = await update(rows, operation);
    if (operation.dryRun) return updated;
    await removeReplaced(updated.filter(e => assigned.includes(e.id)), parent);
    return updated;
}

/** Nested effects do not get their own _preCreate when an Item is imported. */
export function assignedItemData(data, actor, { update = false, preserveEffectStart = false } = {}) {
    if (actor?.documentName !== 'Actor') return data;
    const next = assignmentCounter(actor);
    return data.map(original => {
        const row = foundry.utils.expandObject(serializeEffect(original));
        const previous = update ? actor.items.get(row._id) : null;
        const reactivated = previous && (
            (previous.system.equipped === false && row.system?.equipped === true) ||
            (previous.system.isActive === false && row.system?.isActive === true));
        if (update && !reactivated && !row.effects) return row;
        row.effects ??= previous?.effects.map(e => e.toObject()) ?? [];
        for (const effect of row.effects) {
            assign(effect, next);
            // The wound service already initialized these clocks before checking the write.
            if (!update && !(preserveEffectStart && effect.start != null)) {
                effect.start = null;
                if (effect.duration) effect.duration.expired = false;
                initializeEffectStart(effect, actor);
            }
        }
        return row;
    });
}
