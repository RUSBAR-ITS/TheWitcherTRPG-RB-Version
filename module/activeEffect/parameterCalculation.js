/** Numeric contract only: no Documents, writes, dice, or intermediate rounding. */
function finite(value, name) {
    if (typeof value !== 'number' || !Number.isFinite(value)) throw new TypeError(`Invalid ${name}: ${value}`);
    return value;
}

function limit(value, min, cap) {
    if (min !== null) value = Math.max(min, value);
    if (cap !== null) value = Math.min(cap, value);
    return value;
}

/** Input order breaks equal-priority override ties, just as the stable native sort does. */
export function calculateOperations(base, changes) {
    let value = finite(base, 'base');
    const rows = changes.map((change, order) => {
        if (!['add', 'multiply', 'override'].includes(change.type)) {
            throw new TypeError(`Unsupported numeric operation: ${change.type}`);
        }
        return { ...change, value: finite(change.value, 'modifier'), order };
    });
    for (const change of rows) if (change.type === 'add') value += change.value;
    for (const change of rows) if (change.type === 'multiply') value *= change.value;
    const overrides = rows.filter(change => change.type === 'override')
        .sort((a, b) => (a.priority ?? 50) - (b.priority ?? 50) || a.order - b.order);
    if (overrides.length) value = overrides.at(-1).value;
    return finite(value, 'result');
}

/** Separate parameter, cap, advancement and roll contributions without changing input. */
export function calculateParameter({ base, cap = null, min = null, changes = [], advancementBase = base }) {
    if (cap !== null) finite(cap, 'cap');
    if (min !== null) finite(min, 'minimum');
    const numeric = changes.filter(change => !change.disabled);
    const capValue = cap === null ? null : limit(
        Math.floor(calculateOperations(cap, numeric.filter(change => change.shiftsCap))), min, null
    );
    const parameter = numeric.filter(change => change.affectsParameter !== false && !change.affectsRoll);
    const ordinary = parameter.filter(change => !change.fullEffect);
    const raw = Math.floor(calculateOperations(base, parameter));
    const ordinaryRaw = Math.floor(calculateOperations(base, ordinary));
    const value = limit(raw, min, capValue);
    const ordinaryValue = limit(ordinaryRaw, min, capValue);
    // Compare against the ordinary-only contribution. Clipped ordinary bonuses
    // cannot become full bonuses merely because another row has fullEffect.
    const fullExtra = ordinaryValue + (raw - ordinaryRaw) - value;
    const rollChanges = numeric.filter(change => change.affectsRoll && !change.optionalOnRoll);
    const rollModifier = Math.floor(calculateOperations(0, rollChanges));
    const advancement = limit(Math.floor(calculateOperations(
        advancementBase, numeric.filter(change => change.affectsAdvancement)
    )), min, capValue);
    return {
        value, cap: capValue, advancement, raw, ordinaryValue, fullExtra,
        rollModifier, rollExtra: fullExtra + rollModifier,
        optionalChanges: numeric.filter(change => change.affectsRoll && change.optionalOnRoll).map(change => ({ ...change }))
    };
}
