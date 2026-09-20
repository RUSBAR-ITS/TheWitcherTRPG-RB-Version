/** Stable skill identity belongs to the skill, not its Actor/Item instance. */
export const PROFESSION_SKILL_PATHS = Object.freeze(['definingSkill', ...[1, 2, 3].flatMap(path =>
    [1, 2, 3].map(skill => `skillPath${path}.skill${skill}`))]);

export function assignedSkillIds(documents) {
    return documents.map(document => {
        if (!['skill', 'profession'].includes(document.type)) return document;
        const data = foundry.utils.deepClone(document);
        data.system ??= {};
        if (data.type === 'skill') data.system.skillId ||= foundry.utils.randomID();
        else for (const path of PROFESSION_SKILL_PATHS) {
            if (!foundry.utils.getProperty(data.system, `${path}.skillId`)) {
                foundry.utils.setProperty(data.system, `${path}.skillId`, foundry.utils.randomID());
            }
        }
        return data;
    });
}

export function identifiedSkills(items) {
    const entries = [];
    for (const item of items) {
        if (item.type === 'skill' && item.system.skillId) entries.push({
            kind: 'item', skillId: item.system.skillId, itemId: item.id,
            label: item.name, item
        });
        if (item.type === 'profession') for (const path of PROFESSION_SKILL_PATHS) {
            const skill = foundry.utils.getProperty(item.system, path);
            if (skill?.skillId && skill.skillName) entries.push({
                kind: 'profession', skillId: skill.skillId, itemId: item.id, path,
                label: `${item.name}: ${skill.skillName}`, item
            });
        }
    }
    return entries;
}

export function resolveSkillIdentity(actor, target) {
    const matches = identifiedSkills(actor.items).filter(entry =>
        entry.kind === target.kind && entry.skillId === target.skillId);
    if (matches.length !== 1) throw new Error(game.i18n.format('WITCHER.TemporaryHP.errors.skillIdentity', {
        actor: actor.name, id: target.skillId, count: matches.length
    }));
    const { kind, itemId, path } = matches[0];
    return { kind, itemId, ...(path ? { path } : {}) };
}
