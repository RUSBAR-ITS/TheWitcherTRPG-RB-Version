import { formatRollContributions } from '../../scripts/rolls/rollModifiers.js';

const format = parts => formatRollContributions(parts, {
    details: game.settings.get('TheWitcherTRPG-RB-Version', 'displayRollsDetails')
});

/** Legacy formula boundary, also used by the overriding defense mixin. */
export function combatModifierFormula(actor, kind) {
    return format(Object.entries(actor.system.combatEffects?.[kind] ?? {}).map(([key, mod]) => ({
        value: Number(mod.value) + (actor.parameterModifiers?.get(`system.combatEffects.${kind}.${key}`)?.rollExtra ?? 0),
        label: mod.name ? game.i18n.localize(mod.name) : ''
    })));
}

export let modifierMixin = {
    addActiveEffects(skillName) {
        const skill = CONFIG.WITCHER.skillMap[skillName];
        if (!skill) return '';
        const path = `system.skills.${skill.attribute.name}.${skill.name}`;
        const value = this.system.skills[skill.attribute.name][skill.name].activeEffectModifiers;
        const prepared = this.parameterModifiers?.get(path);
        const labels = prepared?.input.changes.map(row => row.sourceName).filter(Boolean) ??
            (this.appliedEffects ?? []).filter(effect => effect.system.changes.some(row =>
                row.key === `${path}.activeEffectModifiers`)).map(effect => effect.name).filter(Boolean);
        const parts = [{ value, label: [...new Set(labels)].join(' & ') }];
        for (const [key, modifier] of Object.entries(this.system.skillGroupModifiers ?? {})) {
            if (modifier.group === 'allSkills' || CONFIG.WITCHER[modifier.group]?.includes?.(skill.name)) {
                parts.push({ value: Number(modifier.value) +
                    (this.parameterModifiers?.get(`system.skillGroupModifiers.${key}`)?.rollExtra ?? 0),
                    label: modifier.name ? game.i18n.localize(modifier.name) : '' });
            }
        }
        return format(parts);
    },

    addAttackModifiers() {
        return combatModifierFormula(this, 'attackModifier');
    },

    addDefenseModifiers() {
        return combatModifierFormula(this, 'defenseModifier');
    }
};
