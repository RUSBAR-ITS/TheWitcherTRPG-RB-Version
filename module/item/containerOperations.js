import {
    CONTAINER_INTERNAL,
    STORABLE_TYPES,
    cloneData,
    contentOf,
    ownerItems,
    sameOwner,
    parentsOf,
    liveTree,
    copyData,
    expandTemplates,
    validateTemplate,
    containerError
} from './containerTemplates.js';

const busyOwners = new Set();
const itemClass = () => CONFIG.Item.documentClass;
const operationFor = owner => (owner ? { parent: owner } : {});
const collectionFor = owner => owner?.items ?? game.items;
const ownerKey = owner => owner?.uuid ?? 'World.Items';
const sourceData = doc => doc.toObject();
const equal = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const escape = text =>
    String(text).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);

async function withOwners(owners, action) {
    const keys = [...new Set(owners.map(ownerKey))];
    if (keys.some(key => busyOwners.has(key))) throw containerError('busy');
    keys.forEach(key => busyOwners.add(key));
    try {
        return await action();
    } finally {
        keys.forEach(key => busyOwners.delete(key));
    }
}

function requireModify(doc, action = 'update') {
    if (!doc.canUserModify(game.user, action)) throw containerError('permission', { name: doc.name });
}

function requireDestination(owner) {
    if (owner) requireModify(owner);
    else if (!itemClass().canUserCreate(game.user)) throw containerError('permission', { name: 'Items' });
}

function snapshot(documents) {
    return [...new Set(documents)].map(doc => ({ doc, data: sourceData(doc) }));
}

function assertUnchanged(snapshots) {
    for (const { doc, data } of snapshots) {
        if (ownerItems(doc).get(doc.id) !== doc || !equal(sourceData(doc), data)) throw containerError('conflict');
    }
}

function previousPatches(owner, patches) {
    const collection = collectionFor(owner);
    return patches.map(patch => {
        const doc = collection.get(patch._id);
        requireModify(doc);
        return Object.fromEntries(
            Object.keys(patch).map(key => [
                key,
                key === '_id' ? patch._id : cloneData(foundry.utils.getProperty(doc._source, key))
            ])
        );
    });
}

async function writePatches(owner, patches) {
    if (!patches.length) return;
    await itemClass().updateDocuments(patches, operationFor(owner));
    for (const patch of patches) {
        const doc = collectionFor(owner).get(patch._id);
        if (
            !doc ||
            Object.entries(patch).some(
                ([key, value]) => key !== '_id' && !equal(foundry.utils.getProperty(doc._source, key), value)
            )
        )
            throw containerError('writeFailed');
    }
}

async function restorePatches(owner, before, attempted) {
    const restore = [];
    for (let i = 0; i < before.length; i++) {
        const old = before[i],
            current = collectionFor(owner).get(old._id);
        if (!current) throw containerError('writeFailed');
        const patch = { _id: old._id };
        for (const [key, value] of Object.entries(old)) {
            if (key === '_id') continue;
            const actual = foundry.utils.getProperty(current._source, key);
            if (equal(actual, value)) continue;
            if (!equal(actual, attempted[i][key])) throw containerError('conflict');
            patch[key] = value;
        }
        if (Object.keys(patch).length > 1) restore.push(patch);
    }
    await writePatches(owner, restore);
}

/** Internal materialization still uses Foundry create and its normal permission/hooks/validation. */
export async function createContainerDocuments(inputs, operation, rawCreate, rawDelete) {
    const pack = operation.pack ?? operation.parent?.pack;
    if (pack || !inputs.some(data => data.type === 'container' && data.system?.templateContent)) {
        for (const data of inputs) if (data.system?.templateContent) validateTemplate(data.system.templateContent);
        return rawCreate(inputs, operation);
    }
    const { flat, rootIds } = expandTemplates(inputs, operation);
    const collection = collectionFor(operation.parent);
    if (flat.some(data => collection.has(data._id))) throw containerError('conflict');
    try {
        const created = await rawCreate(flat, { ...operation, keepId: true });
        const byId = new Map(created.map(doc => [doc.id, doc]));
        for (const data of flat) {
            const doc = byId.get(data._id);
            if (
                !doc ||
                !collection.has(data._id) ||
                doc.type !== data.type ||
                (data.type === 'container' && !equal(contentOf(doc), data.system.content)) ||
                (data.system?.isStored !== undefined && doc.system.isStored !== data.system.isStored) ||
                (data.system?.quantity !== undefined && String(doc.system.quantity) !== String(data.system.quantity))
            ) {
                throw containerError('writeFailed');
            }
        }
        return rootIds.map(id => byId.get(id));
    } catch (error) {
        // Only ids proven absent before this attempt are eligible for cleanup.
        const ids = flat.map(data => data._id).filter(id => collection.has(id));
        try {
            if (ids.length) await rawDelete(ids, { ...operation, deleteAll: false });
            if (ids.some(id => collection.has(id))) throw containerError('writeFailed');
        } catch (cleanupError) {
            console.error(
                'TheWitcherTRPG | Incomplete template creation',
                { ids, parent: operation.parent?.uuid },
                error,
                cleanupError
            );
            throw new AggregateError([error, cleanupError], containerError('incomplete').message);
        }
        throw error;
    }
}

function locationPatches(item, target) {
    const parents = parentsOf(item);
    if (parents.length > 1) throw containerError('invalidTree', { name: item.name });
    const patches = [];
    for (const parent of parents) {
        if (parent.uuid !== target?.uuid)
            patches.push({ '_id': parent.id, 'system.content': contentOf(parent).filter(uuid => uuid !== item.uuid) });
    }
    if (target && !contentOf(target).includes(item.uuid))
        patches.push({ '_id': target.id, 'system.content': [...contentOf(target), item.uuid] });
    const itemPatch = { _id: item.id };
    if (item.system.isStored !== !!target) itemPatch['system.isStored'] = !!target;
    if ((target || item.system.isStored) && item.system.equipped !== undefined && item.system.equipped !== false)
        itemPatch['system.equipped'] = false;
    if (Object.keys(itemPatch).length > 1) patches.push(itemPatch);
    return patches;
}

async function relocate(item, target) {
    const owner = item.parent ?? null;
    const patches = locationPatches(item, target);
    const before = previousPatches(owner, patches);
    try {
        await writePatches(owner, patches);
    } catch (error) {
        try {
            await restorePatches(owner, before, patches);
        } catch (restoreError) {
            console.error('TheWitcherTRPG | Container relocation incomplete', { patches, before }, error, restoreError);
            throw new AggregateError([error, restoreError], containerError('incomplete').message);
        }
        throw error;
    }
    return item;
}

async function createCopy(source, owner, { equipped, stored = false } = {}) {
    requireDestination(owner);
    const data = copyData(source);
    data._id = foundry.utils.randomID();
    if (equipped !== undefined) data.system.equipped = equipped;
    data.system.isStored = stored;
    if (stored && data.system.equipped !== undefined) data.system.equipped = false;
    if (source.type !== 'container') {
        const uuid = owner ? `${owner.uuid}.Item.${data._id}` : `Item.${data._id}`;
        for (const effect of data.effects ?? []) {
            if (effect.origin === source.uuid || effect.origin?.startsWith(`${source.uuid}.`)) {
                effect.origin = uuid + effect.origin.slice(source.uuid.length);
            }
        }
    }
    try {
        const [created] = await itemClass().createDocuments([data], { ...operationFor(owner), keepId: true });
        if (!created) throw containerError('writeFailed');
        return created;
    } catch (error) {
        // Portable containers have their own verified batch cleanup. Ordinary copies use this known id.
        if (source.type !== 'container' && collectionFor(owner).has(data._id)) {
            try {
                await itemClass().deleteDocuments([data._id], { ...operationFor(owner), [CONTAINER_INTERNAL]: true });
                if (collectionFor(owner).has(data._id)) throw containerError('writeFailed');
            } catch (cleanupError) {
                console.error(
                    'TheWitcherTRPG | Copy cleanup incomplete',
                    { id: data._id, parent: owner?.uuid },
                    error,
                    cleanupError
                );
                throw new AggregateError([error, cleanupError], containerError('incomplete').message);
            }
        }
        throw error;
    }
}

/** Delete a complete owned tree, or restore snapshots if the underlying write fails. */
async function deleteTrees(roots, operation, { confirm = true } = {}) {
    if (!roots.length) return [];
    const pack = operation.pack ?? operation.parent?.pack;
    const owner = operation.parent ?? null;
    const collection = pack ? game.packs.get(pack) : collectionFor(owner);
    const docs = new Map();
    let contentsCount = 0;
    const nested = new Set();
    for (const root of roots) {
        const tree = liveTree(root);
        for (const { item } of tree) {
            requireModify(item, 'delete');
            docs.set(item.id, item);
            if (item !== root) nested.add(item.uuid);
        }
        if (root.system.templateContent) contentsCount += validateTemplate(root.system.templateContent).length;

    }
    contentsCount += nested.size;
    const changes = [];
    if (!pack)
        for (const item of collection) {
            if (item.type !== 'container' || docs.has(item.id)) continue;
            const content = contentOf(item).filter(uuid => ![...docs.values()].some(doc => doc.uuid === uuid));
            if (content.length !== contentOf(item).length) changes.push({ '_id': item.id, 'system.content': content });
        }
    const before = previousPatches(owner, changes);
    const originals = snapshot([...docs.values(), ...changes.map(patch => collection.get(patch._id))]);
    if (confirm && contentsCount) {
        const yes = await foundry.applications.api.DialogV2.confirm({
            window: { title: game.i18n.localize('WITCHER.Container.deleteTitle') },
            content: `<p>${escape(
                game.i18n.format('WITCHER.Container.deleteContents', {
                    name: roots.map(root => root.name).join(', '),
                    count: contentsCount
                })
            )}</p>`,
            no: { default: true },
            rejectClose: false
        });
        if (!yes) return [];
    }
    assertUnchanged(originals);
    const ids = [...docs.keys()];
    let deleted;
    try {
        await writePatches(owner, changes);
        deleted = await itemClass().deleteDocuments(ids, {
            ...operation,
            deleteAll: false,
            [CONTAINER_INTERNAL]: true
        });
        if (ids.some(id => collection.has(id)) || ids.some(id => !deleted.some(doc => doc.id === id))) {
            throw containerError('writeFailed');
        }
        return roots;
    } catch (error) {
        const missing = originals.filter(({ doc }) => docs.has(doc.id) && !collection.has(doc.id));
        try {
            // An absent id not deleted by this request may have moved in another client.
            if (deleted && missing.some(entry => !deleted.some(doc => doc.id === entry.doc.id))) {
                throw containerError('conflict');
            }
            if (missing.length)
                await itemClass().createDocuments(
                    missing.map(entry => entry.data),
                    {
                        ...operation,
                        keepId: true,
                        [CONTAINER_INTERNAL]: true
                    }
                );
            if (ids.some(id => !collection.has(id))) throw containerError('writeFailed');
            await restorePatches(owner, before, changes);
        } catch (restoreError) {
            console.error(
                'TheWitcherTRPG | Container deletion incomplete',
                {
                    ids,
                    parent: owner?.uuid,
                    pack,
                    originals: originals.map(entry => entry.data)
                },
                error,
                restoreError
            );
            throw new AggregateError([error, restoreError], containerError('incomplete').message);
        }
        throw error;
    }
}

export async function deleteContainerDocuments(ids, operation, rawDelete) {
    const pack = operation.pack ?? operation.parent?.pack;
    const collection = pack ? game.packs.get(pack) : collectionFor(operation.parent);
    let roots;
    if (pack)
        roots = operation.deleteAll
            ? await collection.getDocuments()
            : await Promise.all(ids.map(id => collection.getDocument(id)));
    else roots = operation.deleteAll ? [...collection] : ids.map(id => collection.get(id));
    roots = roots.filter(Boolean);
    if (!roots.some(item => item.type === 'container' || parentsOf(item).length)) return rawDelete(ids, operation);
    return withOwners([operation.parent ?? (pack ? { uuid: pack } : null)], () => deleteTrees(roots, operation));
}

/** World/pack sources are templates; Actor -> world also copies. Actor -> Actor transfers. */
async function place(source, owner, target, { sourceContainer, equipped } = {}) {
    if (source?.documentName !== 'Item' || !STORABLE_TYPES.has(source.type) || source.visible === false)
        throw containerError('invalidItem');
    if (target && (target.type !== 'container' || target.pack || target.system.templateContent))
        throw containerError('templateReadOnly');
    if (target) requireModify(target);
    if (source.pack && !source.system.templateContent && source.type === 'container' && contentOf(source).length) {
        throw containerError('invalidTemplate');
    }
    return withOwners([source.parent ?? null, owner], async () => {
        const tree = liveTree(source);
        if (target) liveTree(target);
        if (target && tree.some(({ item }) => item.uuid === target.uuid)) throw containerError('cycle');
        const parent = parentsOf(source)[0];
        if (sourceContainer && parent?.uuid !== sourceContainer) throw containerError('conflict');
        const worldMove = !source.parent && !source.pack && !owner && !!sourceContainer && !!parent;
        const actorMove = !!source.parent && !source.pack && !!owner;
        const move = worldMove || actorMove;
        if (move) {
            requireModify(source);
            if (parent) requireModify(parent);
            if (source.parent !== owner) for (const { item } of tree) requireModify(item, 'delete');
        }
        if (move && (source.parent ?? null) === owner) return relocate(source, target);
        const originals = snapshot([
            ...tree.map(entry => entry.item),
            ...(target ? [target] : []),
            ...(parent ? [parent] : [])
        ]);
        const created = await createCopy(source, owner, {
            equipped: sourceContainer && source.system.equipped !== undefined ? false : equipped,
            stored: !!target
        });
        try {
            assertUnchanged(originals);
            if (target) await relocate(created, target);
            if (move) {
                assertUnchanged(originals.filter(entry => entry.doc !== target));
                await deleteTrees([source], operationFor(source.parent), { confirm: false });
            }
            return created;
        } catch (error) {
            // Never erase the last remaining copy if source deletion/restoration was incomplete.
            const sourceIntact = tree.every(({ item }) => ownerItems(item).has(item.id));
            if (sourceIntact) {
                try {
                    await deleteTrees([created], operationFor(owner), { confirm: false });
                } catch (cleanupError) {
                    console.error(
                        'TheWitcherTRPG | Transfer cleanup incomplete',
                        { source: source.uuid, created: created.uuid },
                        error,
                        cleanupError
                    );
                    throw new AggregateError([error, cleanupError], containerError('incomplete').message);
                }
            } else
                console.error(
                    'TheWitcherTRPG | Transfer retained destination',
                    { source: source.uuid, created: created.uuid },
                    error
                );
            throw error;
        }
    });
}

export function storeItem(target, source, options = {}) {
    return place(source, target.parent ?? null, target, options);
}

export function importToActor(actor, source, options = {}) {
    return place(source, actor, null, options);
}

export async function extractItem(container, uuid) {
    if (container.pack) throw containerError('templateReadOnly');
    return withOwners([container.parent ?? null], async () => {
        requireModify(container);
        if (!contentOf(container).includes(uuid)) return null;
        const item = [...ownerItems(container)].find(doc => doc.uuid === uuid);
        if (!item || !sameOwner(item, container) || item.visible === false) {
            // Explicitly remove only the broken link, never update an external or missing Item.
            const patches = [
                { '_id': container.id, 'system.content': contentOf(container).filter(value => value !== uuid) }
            ];
            await writePatches(container.parent ?? null, patches);
            return null;
        }
        requireModify(item);
        liveTree(item);
        return relocate(item, null);
    });
}

export async function runContainerAction(action) {
    try {
        return await action();
    } catch (error) {
        console.error('TheWitcherTRPG | Container operation', error);
        ui.notifications.error(error.message);
        return null;
    }
}
