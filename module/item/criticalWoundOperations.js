/** Validate the small, deterministic language used by wound healing durations. */
export function validateHealingDuration(expression) {
    if (typeof expression !== 'string' || !expression.trim()) throw new Error('invalidFormula');
    const tokens = expression.match(/\s+|@body\b|\d+(?:\.\d+)?|[A-Za-z_]+|[()+*/,\-]/g) ?? [];
    if (tokens.join('') !== expression) throw new Error('invalidFormula');
    const input = tokens.filter(token => !/^\s+$/.test(token));
    let index = 0;
    const take = token => input[index] === token && ++index;
    const require = token => {
        if (!take(token)) throw new Error('invalidFormula');
    };
    const primary = () => {
        if (take('+') || take('-')) return primary();
        if (take('(')) {
            sum();
            return require(')');
        }
        const token = input[index++];
        if (token === '@body' || /^\d+(?:\.\d+)?$/.test(token ?? '')) return;
        if (!['min', 'max', 'floor', 'ceil', 'round', 'abs'].includes(token)) throw new Error('invalidFormula');
        require('(');
        sum();
        let count = 1;
        while (take(',')) {
            sum();
            count++;
        }
        require(')');
        if (!['min', 'max'].includes(token) && count !== 1) throw new Error('invalidFormula');
    };
    const product = () => {
        primary();
        while (take('*') || take('/')) primary();
    };
    const sum = () => {
        product();
        while (take('+') || take('-')) product();
    };
    sum();
    if (index !== input.length) throw new Error('invalidFormula');
    return { needsBody: input.includes('@body') };
}

/** No persistence, dice, notifications or fallback to BODY.max. */
export function evaluateHealingDuration(expression, actor) {
    try {
        const { needsBody } = validateHealingDuration(expression);
        const body = actor?.system?.stats?.body?.value;
        if (needsBody && !Number.isFinite(body)) return { value: null, error: 'missingBody' };
        const roll = new foundry.dice.Roll(expression, needsBody ? { body } : {});
        if (!roll.isDeterministic) return { value: null, error: 'invalidFormula' };
        roll.evaluateSync({ strict: true });
        if (!Number.isFinite(roll.total) || roll.total <= 0) return { value: null, error: 'invalidDuration' };
        return { value: roll.total, error: null };
    } catch {
        return { value: null, error: 'invalidFormula' };
    }
}

/** A transition target must be another readable stage of the same wound and side. */
export function validateWoundTarget(source, target, system = source.system) {
    if (!target || target.documentName !== 'Item' || target.type !== 'criticalWound') return 'invalidTarget';
    if (target.visible === false) return 'unavailableTarget';
    if (source.uuid === target.uuid) return 'selfTarget';
    const id = system.woundTypeId?.trim();
    if (!id || id !== target.system.woundTypeId?.trim() || system.location !== target.system.location) {
        return 'differentWound';
    }
    return null;
}

export const WOUND_INTERNAL = Symbol('witcherWoundOperation');
const woundQueues = new Map();
const clone = value => foundry.utils.deepClone(value);
const outcome = (status, item, reason = null, removed = false) => ({
    status, itemUuid: item?.uuid ?? null, removed, reason
});

export function woundError(reason) {
    const error = new Error(game.i18n.localize(`WITCHER.criticalWound.errors.${reason}`));
    error.reason = reason;
    return error;
}

/** This queue serializes one client's operations, not transactions between clients. */
export async function withWoundQueue(actor, action) {
    if (!actor?.uuid || actor.documentName !== 'Actor') throw woundError('invalidOwner');
    const key = actor.uuid;
    const previous = woundQueues.get(key) ?? Promise.resolve();
    const task = previous.catch(() => {}).then(action);
    woundQueues.set(key, task);
    try {
        return await task;
    } finally {
        if (woundQueues.get(key) === task) woundQueues.delete(key);
    }
}

export function woundKey(system) {
    const id = system?.woundTypeId?.trim();
    const location = system?.location;
    if (!id) throw woundError('missingId');
    if (!location || !Object.hasOwn(CONFIG.WITCHER.location, location)) throw woundError('invalidLocation');
    return JSON.stringify([id, location]);
}

function requireOwner(actor, item, action = 'update') {
    if (actor?.documentName !== 'Actor' || !actor.canUserModify(game.user, 'update')) throw woundError('permission');
    if (item && (actor.items.get(item.id) !== item || item.type !== 'criticalWound')) throw woundError('missingWound');
    if (item && !item.canUserModify(game.user, action)) throw woundError('permission');
}

function matchingWounds(actor, key) {
    return actor.items.filter(item => item.type === 'criticalWound' &&
        item.system.woundTypeId?.trim() && woundKey(item.system) === key);
}

/** A new stage owns its effects; only self-origins are remapped to the instance. */
export function prepareWoundStage(source, actor, existing = null) {
    if (source?.type !== 'criticalWound' || source.visible === false) throw woundError('invalidTarget');
    const data = clone(source.toObject ? source.toObject() : source);
    woundKey(data.system);
    const id = existing?.id ?? foundry.utils.randomID();
    const uuid = existing?.uuid ?? `${actor.uuid}.Item.${id}`;
    const system = clone(data.system);
    system.woundTypeId = system.woundTypeId.trim();
    system.daysHealed = 0;
    system.sterilized = false;
    delete system.quantity;
    delete system.followUp;
    delete system.healingTime;
    const effects = (data.effects ?? []).map(effect => {
        const copy = clone(effect);
        copy._id = foundry.utils.randomID();
        delete copy._stats;
        const sourceUuid = source.uuid ?? data._stats?.compendiumSource;
        if (sourceUuid && copy.origin === sourceUuid) copy.origin = uuid;
        return copy;
    });
    const stage = { name: data.name, img: data.img, type: 'criticalWound', system, flags: data.flags ?? {}, effects };
    // Validate and normalize with the real Item model, without adding it to the collection.
    const preview = new CONFIG.Item.documentClass({ ...(existing?.toObject() ?? {}), ...stage, _id: id }, { parent: actor });
    preview.validate({ strict: true });
    return preview.toObject();
}

function stageMatches(item, expected) {
    if (!item) return false;
    const comparable = data => ({
        name: data.name, img: data.img, type: data.type, system: data.system, flags: data.flags,
        effects: (data.effects ?? []).map(effect => {
            const clean = clone(effect);
            delete clean._stats;
            return clean;
        }).sort((a, b) => a._id.localeCompare(b._id))
    });
    try {
        return foundry.utils.equals(comparable(item.toObject()), comparable(expected));
    } catch {
        return false;
    }
}

async function writeStage(actor, source, existing, create) {
    requireOwner(actor, existing);
    const expected = prepareWoundStage(source, actor, existing);
    if (existing) {
        const replace = foundry.data.operators.ForcedReplacement;
        const patch = { name: expected.name, img: expected.img,
            system: replace.create(expected.system), flags: replace.create(expected.flags), effects: replace.create(expected.effects) };
        existing.updateSource(patch, { dryRun: true });
        let saved;
        try {
            saved = await existing.update(patch, { [WOUND_INTERNAL]: true });
        } catch (error) {
            console.error('TheWitcherTRPG | Wound update', error);
            return outcome('failed', actor.items.get(existing.id), 'uncertainWrite');
        }
        const current = actor.items.get(existing.id);
        if (!saved) return outcome('failed', current, 'writeCancelled');
        return stageMatches(current, expected) ? outcome('applied', current) : outcome('failed', current, 'uncertainWrite');
    }
    delete expected.ownership;
    delete expected._stats;
    let created;
    try {
        created = await create([expected], { parent: actor, keepId: true, [WOUND_INTERNAL]: true });
    } catch (error) {
        console.error('TheWitcherTRPG | Wound create', error);
        return outcome('failed', actor.items.get(expected._id), 'uncertainWrite');
    }
    const current = actor.items.get(expected._id);
    if (created?.length !== 1) return outcome('failed', current, 'writeCancelled');
    try {
        const matches = matchingWounds(actor, woundKey(expected.system));
        return matches.length === 1 && stageMatches(current, expected)
            ? outcome('applied', current) : outcome('failed', current, 'uncertainWrite');
    } catch {
        return outcome('failed', current, 'uncertainWrite');
    }
}

async function installWoundLocked(actor, source, reason, create) {
    requireOwner(actor);
    const data = source.toObject ? source.toObject() : source;
    if (reason === 'game' && data.system?.treatment !== 'none') throw woundError('invalidInitialStage');
    const matches = matchingWounds(actor, woundKey(data.system));
    if (matches.length > 1) throw woundError('duplicateWound');
    return writeStage(actor, source, matches[0], create);
}

/** Explicit manual/game inputs share the same family-and-location uniqueness rule. */
export async function installWound(actor, source, { reason = 'manual' } = {}) {
    try {
        return await withWoundQueue(actor, () => installWoundLocked(actor, source, reason,
            (data, options) => actor.createEmbeddedDocuments('Item', data, options)));
    } catch (error) {
        return outcome('rejected', null, error.reason ?? 'invalidData');
    }
}

async function removeWound(actor, item) {
    requireOwner(actor, item, 'delete');
    try {
        const deleted = await item.delete();
        if (!deleted || actor.items.has(item.id)) return outcome('failed', item, 'writeCancelled');
        return outcome('applied', item, null, true);
    } catch (error) {
        console.error('TheWitcherTRPG | Wound delete', error);
        return outcome('failed', item, 'uncertainWrite', !actor.items.has(item.id));
    }
}

/** Actions read the live Item again after asynchronous UUID resolution. */
export async function transitionWound(item, action) {
    const actor = item.parent;
    try {
        return await withWoundQueue(actor, async () => {
            requireOwner(actor, item);
            woundKey(item.system);
            const config = action === 'stabilize' ? ['cannotStabilize', 'stabilizedWound']
                : action === 'treat' ? ['cannotTreat', 'treatedWound'] : null;
            if (!config) throw woundError('invalidAction');
            const [forbidden, field] = config;
            if (item.system[forbidden]) throw woundError('actionForbidden');
            const uuid = item.system[field];
            if (!uuid) {
                if (action === 'stabilize') throw woundError('missingStabilized');
                return removeWound(actor, item);
            }
            const before = item.toObject();
            const target = await fromUuid(uuid);
            requireOwner(actor, item);
            if (!foundry.utils.equals(before, item.toObject())) throw woundError('conflict');
            if (item.system[forbidden] || item.system[field] !== uuid) throw woundError('conflict');
            const invalid = validateWoundTarget(item, target);
            if (invalid) throw woundError(invalid);
            if (matchingWounds(actor, woundKey(item.system)).length !== 1) throw woundError('duplicateWound');
            return writeStage(actor, target, item);
        });
    } catch (error) {
        return outcome('rejected', item, error.reason ?? 'invalidData');
    }
}

export async function healWound(item, { sterilized = false } = {}) {
    const actor = item.parent;
    try {
        return await withWoundQueue(actor, async () => {
            requireOwner(actor, item);
            if (!item.system.canHeal) return outcome('unchanged', item);
            const duration = evaluateHealingDuration(item.system.healingDuration, actor);
            if (duration.error) throw woundError(duration.error);
            const days = item.system.daysHealed;
            if (!Number.isFinite(days) || days < 0) throw woundError('invalidProgress');
            const next = days + 1 + (sterilized && !item.system.sterilized ? 2 : 0);
            if (next >= duration.value) return removeWound(actor, item);
            const patch = { 'system.daysHealed': next };
            if (sterilized && !item.system.sterilized) patch['system.sterilized'] = true;
            try {
                const saved = await item.update(patch, { [WOUND_INTERNAL]: true });
                if (!saved) return outcome('failed', item, 'writeCancelled');
                const current = actor.items.get(item.id);
                if (current?.system.daysHealed !== next || (sterilized && !current.system.sterilized)) {
                    return outcome('failed', current, 'uncertainWrite');
                }
                return outcome('applied', current);
            } catch (error) {
                console.error('TheWitcherTRPG | Wound heal', error);
                return outcome('failed', item, 'uncertainWrite');
            }
        });
    } catch (error) {
        return outcome('rejected', item, error.reason ?? 'invalidData');
    }
}

export function reportWoundResult(result) {
    if (result.status === 'rejected' || result.status === 'failed') ui.notifications.error(woundError(result.reason).message);
    return result;
}

/** Called by the native Item factory, including Actor imports and duplication. */
export async function createWoundDocuments(data, operation, nativeCreate) {
    return withWoundQueue(operation.parent, async () => {
        const actor = operation.parent;
        requireOwner(actor);
        const keys = new Set();
        for (const source of data) {
            if (source.type !== 'criticalWound') continue;
            const key = woundKey(source.system);
            if (keys.has(key) || matchingWounds(actor, key).length > 1) throw woundError('duplicateWound');
            keys.add(key);
            prepareWoundStage(source, actor);
        }
        const result = [];
        for (const source of data) {
            if (source.type !== 'criticalWound') {
                result.push(...await nativeCreate([source], operation));
                continue;
            }
            const applied = await installWoundLocked(actor, source, 'manual',
                (rows, options) => nativeCreate(rows, { ...operation, ...options }));
            if (applied.status !== 'applied') throw woundError(applied.reason);
            const key = woundKey(source.system);
            result.push(matchingWounds(actor, key)[0]);
        }
        return result;
    });
}

/** Validate all prospective keys together, including multi-Item edits. */
export function validateWoundUpdates(actor, changes) {
    const documents = new Map(actor.items.map(item => [item.id, item.toObject()]));
    for (const change of changes) {
        const item = actor.items.get(change._id);
        if (!item) continue;
        const preview = new CONFIG.Item.documentClass(item.toObject(), { parent: actor });
        preview.updateSource(change);
        documents.set(item.id, preview.toObject());
    }
    const keys = new Set();
    for (const data of documents.values()) {
        if (data.type !== 'criticalWound') continue;
        // Unrelated old drafts must not prevent editing a correctly configured Item.
        if (!data.system.woundTypeId?.trim() && !changes.some(row => row._id === data._id)) continue;
        const key = woundKey(data.system);
        if (keys.has(key)) throw woundError('duplicateWound');
        keys.add(key);
    }
}

/** Read the configured pack on each acquisition, including after a setting change. */
export async function selectInitialWound(crit, rollAlternative) {
    const pack = game.packs.get(game.settings.get('TheWitcherTRPG-RB-Version', 'criticalWoundsPack'));
    if (!pack || pack.documentName !== 'Item') throw woundError('invalidPack');
    const index = await pack.getIndex({
        fields: ['system.woundTypeId', 'system.location', 'system.treatment', 'system.criticalLevel', 'system.lesserEffect']
    });
    const wounds = [...index].filter(row => row.type === 'criticalWound');
    const variants = new Set();
    for (const wound of wounds) {
        const variant = JSON.stringify([woundKey(wound.system), wound.system.treatment]);
        if (variants.has(variant)) throw woundError('ambiguousPack');
        variants.add(variant);
    }
    const candidates = wounds.filter(row => row.system.treatment === 'none' &&
        row.system.location === crit.location?.name && row.system.criticalLevel === crit.criticalLevel);
    if (!candidates.length) throw woundError('missingCandidate');
    let selected = candidates;
    if (candidates.length > 1) {
        const roll = crit.location.critEffect ?? rollAlternative() + (crit.critEffectModifier ?? 0);
        selected = candidates.filter(row => row.system.lesserEffect === (roll <= 4));
    }
    if (selected.length !== 1) throw woundError('ambiguousPack');
    const entry = selected[0];
    const item = await pack.getDocument(entry._id);
    if (!item || item.type !== 'criticalWound' || item.visible === false) throw woundError('invalidTarget');
    for (const field of ['woundTypeId', 'location', 'treatment', 'criticalLevel', 'lesserEffect']) {
        if (item.system[field] !== entry.system[field]) throw woundError('conflict');
    }
    return item;
}
