/** Metadata shared by the modifier schema and both effect editor entry points. */
export const MODIFIER_DEFAULTS = Object.freeze({
    affectsParameter: true,
    affectsRoll: false,
    fullEffect: false,
    shiftsCap: false,
    affectsAdvancement: false,
    optionalOnRoll: false
});

export const DERIVED_MODIFIER_TARGETS = Object.freeze([
    'hp', 'sta', 'rec', 'stun', 'enc', 'run', 'leap', 'woundTreshold', 'resolve', 'focus', 'bodyDamage'
]);

/** Item-hosted effects may still target the Actor, including unowned templates. */
export function getEffectTargetType(effect, source = effect) {
    if ((source.type ?? effect.type) === 'temporaryItemImprovement') return 'Item';
    if (effect.parent?.documentName === 'Actor') return 'Actor';
    const system = source.system ?? effect.system;
    if ((source.transfer ?? effect.transfer) ||
        ['applySelf', 'applyOnTarget', 'applyOnHit', 'applyOnDamage'].some(key => system?.[key])) return 'Actor';
    return effect.parent?.documentName === 'Item' ? 'Item' : 'Actor';
}

/** Only known numeric Actor targets use the new contract. Other changes stay native. */
export function supportsModifierChange(change) {
    if (!['add', 'multiply', 'override'].includes(change.type ?? 'add')) return false;
    const key = change.key ?? '';
    return /^system\.stats\.(int|ref|dex|body|spd|emp|cra|will|luck|toxicity)\.(max|value|totalModifiers)$/.test(key) ||
        /^system\.derivedStats\.(hp|sta|rec|stun|enc|run|leap|woundTreshold|resolve|focus|vigor|shield)\.(max|value|totalModifiers)$/.test(key) ||
        /^system\.skills\.[a-z]+\.[a-z]+\.(value|activeEffectModifiers)$/i.test(key) ||
        /^system\.combatEffects\.(attackModifier|defenseModifier)\.[^.]+\.value$/.test(key) ||
        /^system\.skillGroupModifiers\.[^.]+\.value$/.test(key) ||
        /^system\.lifepathModifiers\.attacks\.(strong|joint)\.value$/.test(key);
}

export function modifierSettings(change = {}) {
    return {
        ...Object.fromEntries(Object.entries(MODIFIER_DEFAULTS).map(([key, value]) => [key, change[key] ?? value])),
        excludedDerived: [...(change.excludedDerived ?? [])]
    };
}

/** Apply an explicit UI channel switch; imports are validated, never silently repaired. */
export function switchModifierChannel(change, field) {
    const settings = modifierSettings(change);
    if (field === 'affectsRoll' && settings.affectsRoll) settings.affectsParameter = false;
    if (field === 'affectsParameter' && settings.affectsParameter) settings.affectsRoll = false;
    if (settings.affectsRoll) {
        settings.shiftsCap = false;
        settings.affectsAdvancement = false;
    } else settings.optionalOnRoll = false;
    if (!settings.affectsParameter) {
        settings.fullEffect = false;
        settings.excludedDerived = [];
    }
    return {...change, ...settings};
}

export function derivedModifierChoices() {
    return Object.fromEntries(DERIVED_MODIFIER_TARGETS.map(key => [key,
        game.i18n.localize(key === 'bodyDamage' ? 'WITCHER.Dialog.attackMeleeBonus'
            : CONFIG.WITCHER.statMap[key]?.label ?? CONFIG.WITCHER.statMap[key]?.labelShort ?? key)
    ]));
}
