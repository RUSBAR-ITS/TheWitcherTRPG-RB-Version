/** Container trees share an owner; portable nodes contain data, never live child references. */
export const STORABLE_TYPES = new Set([
    'weapon',
    'armor',
    'enhancement',
    'valuable',
    'alchemical',
    'component',
    'diagrams',
    'mutagen',
    'container'
]);
export const CONTAINER_INTERNAL = Symbol('witcherContainerOperation');
export const cloneData = value => foundry.utils.deepClone(value);
export const contentOf = item => item._source?.system?.content ?? item.system?.content ?? [];
export const ownerItems = item => item.parent?.items ?? (item.pack ? game.packs.get(item.pack) : game.items);
export const sameOwner = (a, b) =>
    (a.parent?.uuid ?? null) === (b.parent?.uuid ?? null) && (a.pack ?? null) === (b.pack ?? null);

export function containerError(key, data = {}) {
    return new Error(game.i18n.format(`WITCHER.Container.${key}`, data));
}

export function parentsOf(item) {
    return [...ownerItems(item)].filter(parent => parent.type === 'container' && contentOf(parent).includes(item.uuid));
}

/** Synchronous because all physical children must be in the same loaded world/Actor collection. */
export function liveTree(root) {
    const collection = ownerItems(root);
    const lookup = new Map([...collection].map(item => [item.uuid, item]));
    const seen = new Set();
    const result = [];
    const queue = [{ item: root, parent: null }];
    while (queue.length) {
        const { item, parent } = queue.pop();
        if (!item?.system || !sameOwner(root, item) || item.visible === false || seen.has(item.uuid)) {
            throw containerError('invalidTree', { name: root.name });
        }
        seen.add(item.uuid);
        const parents = parentsOf(item);
        if (parents.length > 1 || (parent && parents[0]?.uuid !== parent.uuid)) {
            throw containerError('invalidTree', { name: root.name });
        }
        result.push({ item, parent });
        if (item.type !== 'container') continue;
        if (item.system.templateContent) {
            if (!item.pack || contentOf(item).length) throw containerError('invalidTree', { name: item.name });
            validateTemplate(item.system.templateContent);
            continue;
        }
        for (const uuid of [...contentOf(item)].reverse()) {
            const child = lookup.get(uuid);
            if (!child || !STORABLE_TYPES.has(child.type)) throw containerError('unavailableItem', { uuid });
            queue.push({ item: child, parent: item });
        }
    }
    return result;
}

/** Reject malformed portable data before any writes. Returns all descendant nodes. */
export function validateTemplate(template) {
    if (
        !template ||
        template.version !== 1 ||
        typeof template.sourceUuid !== 'string' ||
        !template.sourceUuid ||
        !Array.isArray(template.items)
    ) {
        throw containerError('invalidTemplate');
    }
    const nodes = [],
        objects = new Set(),
        uuids = new Set([template.sourceUuid]);
    const queue = [...template.items];
    while (queue.length) {
        const node = queue.pop();
        if (
            !node ||
            objects.has(node) ||
            typeof node.sourceUuid !== 'string' ||
            !node.sourceUuid ||
            uuids.has(node.sourceUuid) ||
            !node.data ||
            !STORABLE_TYPES.has(node.data.type) ||
            !node.data.system ||
            !Array.isArray(node.items) ||
            (node.data.type !== 'container' && node.items.length) ||
            node.data.system.content?.length ||
            node.data.system.templateContent
        ) {
            throw containerError('invalidTemplate');
        }
        objects.add(node);
        uuids.add(node.sourceUuid);
        nodes.push(node);
        queue.push(...node.items);
    }
    return nodes;
}

function cleanItemData(item) {
    const data = item.toObject();
    for (const key of ['_id', 'folder', 'sort', 'ownership', '_stats']) delete data[key];
    // Embedded effect ids can stay: their parent UUID changes with the new Item.
    for (const effect of data.effects ?? []) {
        delete effect._stats;
        delete effect.ownership;
        delete effect.author;
    }
    if (data.type === 'container') {
        data.system.content = [];
        data.system.templateContent = null;
        data.system.storedWeight = 0;
    }
    return data;
}

export function serializeContainer(root) {
    if (root.system.templateContent) {
        validateTemplate(root.system.templateContent);
        return cloneData(root.system.templateContent);
    }
    const tree = liveTree(root);
    const nodes = new Map(
        tree.map(({ item }) => [
            item.uuid,
            {
                sourceUuid: item.uuid,
                data: cleanItemData(item),
                items: []
            }
        ])
    );
    for (const { item, parent } of tree) if (parent) nodes.get(parent.uuid).items.push(nodes.get(item.uuid));
    return { version: 1, sourceUuid: root.uuid, items: nodes.get(root.uuid).items };
}

export function copyData(root) {
    const data = cleanItemData(root);
    if (root.type === 'container') data.system.templateContent = serializeContainer(root);
    data.system.isStored = false;
    return data;
}

/** Only containment and explicit ActiveEffect origin references are rebased, not arbitrary strings. */
function rebaseOrigins(data, mapping) {
    const entries = [...mapping].sort((a, b) => b[0].length - a[0].length);
    for (const effect of data.effects ?? []) {
        if (typeof effect.origin !== 'string') continue;
        const match = entries.find(([old]) => effect.origin === old || effect.origin.startsWith(`${old}.`));
        if (match) effect.origin = match[1] + effect.origin.slice(match[0].length);
    }
}

/** Expand multiple roots for one native create call. Every template import gets fresh ids. */
export function expandTemplates(inputs, operation) {
    const flat = [],
        rootIds = [];
    const uuidFor = id => (operation.parent ? `${operation.parent.uuid}.Item.${id}` : `Item.${id}`);
    for (const input of inputs) {
        const root = cloneData(input.toObject ? input.toObject() : input);
        const template = root.type === 'container' ? root.system?.templateContent : null;
        root._id = !template && operation.keepId && root._id ? root._id : foundry.utils.randomID();
        rootIds.push(root._id);
        if (!template) {
            flat.push(root);
            continue;
        }
        validateTemplate(template);
        const mapping = new Map([[template.sourceUuid, uuidFor(root._id)]]);
        const pairs = [{ data: root, items: template.items }];
        for (let index = 0; index < pairs.length; index++) {
            const pair = pairs[index];
            const childIds = [];
            for (const node of pair.items) {
                const data = cloneData(node.data);
                data._id = foundry.utils.randomID();
                // Imported children follow the destination root's folder/ownership, not the source world.
                if (!operation.parent) {
                    if (root.folder) data.folder = root.folder;
                    if (root.ownership) data.ownership = cloneData(root.ownership);
                }
                data.system.isStored = true;
                mapping.set(node.sourceUuid, uuidFor(data._id));
                pairs.push({ data, items: node.items });
                childIds.push(uuidFor(data._id));
            }
            if (pair.data.type === 'container') {
                pair.data.system.content = childIds;
                pair.data.system.templateContent = null;
                pair.data.system.storedWeight = 0;
            }
        }
        root.system.isStored = false;
        for (const { data } of pairs) {
            rebaseOrigins(data, mapping);
            flat.push(data);
        }
    }
    return { flat, rootIds };
}

/** Weight uses prepared scalar values, but membership is the saved physical tree. */
export function describeContainer(root) {
    const result = { rows: [], weight: 0, incomplete: false, portable: !!root.system.templateContent };
    const addWeight = data => {
        const value = Number(data.system?.quantity) * Number(data.system?.weight);
        if (!Number.isFinite(value)) result.incomplete = true;
        else result.weight += value;
    };
    if (result.portable) {
        try {
            validateTemplate(root.system.templateContent);
            const queue = root.system.templateContent.items.map(node => ({ node, depth: 0 }));
            while (queue.length) {
                const { node, depth } = queue.shift();
                addWeight(node.data);
                result.rows.push({
                    ...node.data.system,
                    name: `${'— '.repeat(depth)}${node.data.name}`,
                    img: node.data.img,
                    portable: true
                });
                queue.unshift(...node.items.map(child => ({ node: child, depth: depth + 1 })));
            }
        } catch {
            result.incomplete = true;
        }
        return result;
    }
    const lookup = new Map([...(ownerItems(root) ?? [])].map(item => [item.uuid, item]));
    const seen = new Set([root.uuid]);
    const queue = contentOf(root).map(uuid => ({ uuid, direct: true }));
    while (queue.length) {
        const { uuid, direct } = queue.shift();
        const item = lookup.get(uuid);
        const missing = !item?.system || !sameOwner(root, item) || item.visible === false || seen.has(uuid);
        if (direct)
            result.rows.push(
                missing
                    ? { uuid, name: uuid, missing: true, img: 'icons/svg/item-bag.svg' }
                    : {
                          uuid,
                          name: item.name,
                          img: item.img,
                          quantity: item.system.quantity,
                          weight: item.system.weight,
                          description: item.system.description,
                          missing: false
                      }
            );
        if (missing) {
            result.incomplete = true;
            continue;
        }
        seen.add(uuid);
        addWeight(item);
        if (item.type === 'container') queue.push(...contentOf(item).map(child => ({ uuid: child, direct: false })));
    }
    return result;
}
