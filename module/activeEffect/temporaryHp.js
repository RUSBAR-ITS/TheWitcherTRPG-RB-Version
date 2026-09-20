const HP_KEY = /^system\.combatEffects\.temporaryEffects\.temporaryHp\.[^.]+$/;

/** Only source rows are editable; prepared rows may contain cyclic effect references. */
export function temporaryHpSources(actor) {
    return [...actor.allApplicableEffects()].filter(effect => effect.active).map(effect => {
        const source = effect.toObject();
        const rows = (source.system?.changes ?? []).map((change, index) => ({ change, index }))
            .filter(({ change }) => HP_KEY.test(change.key) && typeof change.value === 'object' &&
                change.value !== null && Number.isFinite(change.value.value) && change.value.value > 0);
        return { effect, source, rows, time: source._stats?.createdTime ?? 0 };
    }).filter(entry => entry.rows.length).sort((a, b) => a.time - b.time || a.effect.uuid.localeCompare(b.effect.uuid));
}

export function temporaryHpTotal(actor) {
    return temporaryHpSources(actor).reduce((total, source) =>
        total + source.rows.reduce((value, row) => value + row.change.value.value, 0), 0);
}

/** Caller owns the ordinary-resource write and the enclosing parameter operation. */
export async function spendTemporaryHp(actor, damage) {
    if (damage <= 0) return damage;
    const operations = [];
    for (const entry of temporaryHpSources(actor)) {
        if (damage <= 0) break;
        for (const { change } of entry.rows) {
            const absorbed = Math.min(change.value.value, damage);
            change.value.value -= absorbed;
            damage -= absorbed;
            if (damage <= 0) break;
        }
        operations.push({ ...entry, exhausted: entry.rows.every(row => row.change.value.value <= 0) });
    }
    for (const { effect, source, exhausted } of operations) {
        if (exhausted) {
            if (!await effect.delete()) throw new Error(game.i18n.localize('WITCHER.EffectApplication.writeFailed'));
        }
        else {
            const saved = await effect.update({ 'system.changes': source.system.changes });
            if (!saved) throw new Error(game.i18n.localize('WITCHER.EffectApplication.writeFailed'));
        }
    }
    return damage;
}

export function temporaryHpEffectData({ item, name, description, value, duration, unit }) {
    return {
        name, img: item.img, description, origin: item.uuid, type: 'base', transfer: false,
        duration: { value: null, expiry: null, expired: false },
        system: {
            changes: [{ key: `system.combatEffects.temporaryEffects.temporaryHp.${foundry.utils.randomID()}`,
                type: 'add', phase: 'initial', value: { name, value } }],
            temporaryHpDuration: { value: duration, unit, combatId: null, combatantId: null, startRound: null }
        }
    };
}
