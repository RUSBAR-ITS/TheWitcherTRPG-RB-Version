import { getCurrentCharacter } from '../helper.js';
import { deliverActorEffects, notifyEffectDelivery } from '../effectDelivery.js';

const boundStatusLinks = new WeakSet();
const pendingStatuses = new Set();

export function addStatusEffectChatListeners(html) {
    // setup chat listener messages for each message as some need the message context instead of chatlog context.
    html.querySelector('.chat-message').each(async (index, element) => {
        element = $(element);
        const id = element.data('messageId');
        const message = game.messages?.get(id);
        if (!message) return;

        await chatMessageListeners(message, element);
    });
}

export const chatMessageListeners = async (message, html) => {
    if (!html.querySelector('a.apply-status')) return;

    html.querySelectorAll('a.apply-status').forEach(status => {
        if (boundStatusLinks.has(status)) return;
        boundStatusLinks.add(status);
        status.addEventListener('click', event => onApplyStatus(event));
    });
};

export async function onApplyStatus(event) {
    event.preventDefault();
    const { status: statusId, actorUuid, duration } = event.currentTarget.dataset;
    let key;
    try {
        const target = actorUuid ? await fromUuid(actorUuid) : getCurrentCharacter();
        if (!target || (actorUuid && !target.canUserModify(game.user, 'update'))) {
            return notifyEffectDelivery({ state: 'refused', reason: 'permission' });
        }
        const pendingKey = `${target.uuid}:${statusId}`;
        if (pendingStatuses.has(pendingKey)) return;
        key = pendingKey;
        pendingStatuses.add(key);
        return await applyStatusEffectToActor(target.uuid, statusId, duration);
    } catch (error) {
        console.error('Witcher manual status failed', error);
        return notifyEffectDelivery({ state: 'unknown', reason: 'responseUnconfirmed' });
    } finally {
        if (key) pendingStatuses.delete(key);
    }
}

export async function applyStatusEffectToTargets(statusEffects, duration) {
    const results = [];
    for (const target of game.user.targets) {
        for (const effect of Object.values(statusEffects)) {
            results.push(await applyStatusEffectToActor(target.actor.uuid, effect.statusEffect, duration));
        }
    }
    return results;
}

export async function applyStatusEffectToActor(actorUuid, statusEffectId, duration) {
    // HTML dataset values are strings; zero remains an explicit duration.
    if (typeof duration === 'string') duration = duration.trim() ? Number(duration) : undefined;
    return notifyEffectDelivery(await deliverActorEffects(actorUuid, [
        { kind: 'status', statusId: statusEffectId ?? '', duration }
    ]));
}
