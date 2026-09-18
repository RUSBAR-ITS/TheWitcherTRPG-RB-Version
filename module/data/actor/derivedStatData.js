/** Shared formula/manual-base contract for preparation and the stat editor. */
export const RESOURCE_STATS = Object.freeze(['hp', 'sta', 'resolve', 'focus', 'vigor', 'shield']);

export function isManualDerivedStat(key, customStat) {
    return ['vigor', 'shield'].includes(key) ||
        (!!customStat && ['hp', 'sta', 'resolve', 'focus'].includes(key));
}

/** Do not round a formula before its own modifiers have been applied. */
export function derivedStatBase(key, stat, derived) {
    switch (key) {
        case 'hp': case 'sta': return (stat('body') + stat('will')) / 2 * 5;
        case 'rec': case 'stun': case 'woundTreshold': return (stat('body') + stat('will')) / 2;
        case 'enc': return stat('body') * 10;
        case 'run': return stat('spd') * 3;
        case 'leap': return derived('run') / 5;
        case 'resolve': return (stat('will') + stat('int')) / 2 * 5;
        case 'focus': return (stat('will') + stat('int')) / 2 * 3;
        default: throw new Error(`Unknown automatic derived stat: ${key}`);
    }
}
