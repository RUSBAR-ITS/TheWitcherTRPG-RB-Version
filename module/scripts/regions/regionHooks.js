export async function countdownDurationOfRegions(combat, update, options, userId) {
    if (!game.user.isActiveGM) return;

    const actorUuid = combat.combatants.get(combat.current.combatantId)?.actor?.uuid;
    if (!actorUuid || !game.scenes.active) return;

    let toDelete = [];
    game.scenes.active.regions
        .filter(region => region.flags['TheWitcherTRPG-RB-Version']?.actorUuid === actorUuid)
        .forEach(region => {
            if (region.flags['TheWitcherTRPG-RB-Version'].duration - 1 > 0) {
                region.setFlag('TheWitcherTRPG-RB-Version', 'duration', region.flags['TheWitcherTRPG-RB-Version'].duration - 1);
            } else {
                toDelete.push(region.id);
            }
        });

    game.scenes.active.deleteEmbeddedDocuments('Region', toDelete);
}
