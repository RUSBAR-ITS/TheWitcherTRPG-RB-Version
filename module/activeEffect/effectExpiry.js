import { withParameterChanges } from '../actor/parameterPersistence.js';

const installed = new WeakSet();

/** Keep core duration/expiry decisions and batch writes, then normalize each Actor once. */
export function registerEffectExpiry() {
    const registry = foundry.documents.ActiveEffect.registry;
    if (installed.has(registry)) return;
    const refresh = registry.refresh;
    registry.refresh = function (...args) {
        // Core only writes expiry on the active GM; other clients merely refresh clocks.
        if (!game.users.activeGM?.isSelf) return refresh.apply(this, args);
        const context = args[1];
        const actors = [...new Set([...this].map(effect => effect.actor).filter(actor =>
            actor && (!context?.actors || context.actors.has(actor))))];
        const apply = index => index === actors.length
            ? refresh.apply(this, args)
            : withParameterChanges(actors[index], () => apply(index + 1));
        // Includes core's dry-run preparation and every response in its batch.
        // Nested document wrappers cannot clip resources between those responses.
        return apply(0);
    };
    installed.add(registry);
}
