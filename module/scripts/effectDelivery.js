import { getActorOwner } from './helper.js';
import { serializeEffect, validateEffectDuration } from '../activeEffect/effectApplication.js';
import { withParameterChanges } from '../actor/parameterPersistence.js';
import { applyLocalActiveEffects, applyLocalStatus } from './effectDeliveryLocal.js';

export const DELIVERY_QUERY = 'TheWitcherTRPG-RB-Version.effectDelivery';
export const SOURCE_QUERY = 'TheWitcherTRPG-RB-Version.effectSource';
const triggers = new Set(['applySelf', 'applyOnTarget', 'applyOnHit', 'applyOnDamage']);
const failure = (reason, state = 'refused') => ({ state, reason });
const deliveryScope = 'TheWitcherTRPG-RB-Version';
const activeSends = new Set();
const boundButtons = new WeakSet();

async function resolveDocument(uuid, type) {
    if (typeof uuid !== 'string' || !uuid) return null;
    try {
        const document = await fromUuid(uuid);
        return document?.documentName === type ? document : null;
    } catch {
        return null;
    }
}

/** Source query receiver: read only, JSON data, no forwarding or Actor writes. */
export async function readEffectSource({ itemUuid, applyWhen } = {}) {
    if (!triggers.has(applyWhen)) return failure('invalidSource');
    const item = await resolveDocument(itemUuid, 'Item');
    if (!item || item.visible === false) return failure('sourceUnavailable');
    try {
        const effects = [...item.effects].filter(effect => effect.system?.[applyWhen]).map(serializeEffect);
        return { state: 'complete', reason: effects.length ? 'source' : 'empty',
            source: { uuid: item.uuid, name: item.name }, effects };
    } catch {
        return failure('invalidSource');
    }
}

export async function resolveEffectSource(itemUuid, applyWhen) {
    const request = { itemUuid, applyWhen };
    const local = await readEffectSource(request);
    if (local.state === 'complete' || local.reason === 'invalidSource') return local;
    const gm = game.users.activeGM;
    if (!gm?.active || gm.id === game.user.id) return local;
    try {
        const result = await gm.query(SOURCE_QUERY, request);
        if (result?.state === 'complete' && Array.isArray(result.effects)) return serializeEffect(result);
        if (result?.state === 'refused') return serializeEffect(result);
    } catch (error) {
        console.error('Witcher effect source query failed', error);
    }
    return failure('sourceUnavailable');
}

/** Local permission takes precedence; otherwise retain the existing owner → GM order. */
export async function getEffectExecutor(actorUuid) {
    const actor = await resolveDocument(actorUuid, 'Actor');
    if (!actor) return { ...failure('actorUnavailable'), actor: null, user: null };
    if (actor.canUserModify(game.user, 'update')) return { state: 'ready', actor, user: game.user };
    const user = getActorOwner(actor);
    if (!user?.active || user.id === game.user.id) return { ...failure('noExecutor'), actor, user: null };
    return { state: 'ready', actor, user };
}

function prepareEntries(entries) {
    if (!Array.isArray(entries)) throw new Error('Expected an effect batch');
    return entries.map(entry => {
        validateEffectDuration(entry.duration);
        const duration = entry.duration == null ? {} : { duration: entry.duration };
        if (entry.kind === 'activeEffects' && Array.isArray(entry.effects)) {
            const effects = entry.effects.map(serializeEffect);
            if (effects.some(effect => !effect || typeof effect !== 'object' || Array.isArray(effect))) {
                throw new Error('Invalid effect data');
            }
            return { kind: entry.kind, effects, ...duration };
        }
        if (entry.kind === 'status' && typeof entry.statusId === 'string'
            && (!entry.statusId || Object.hasOwn(CONFIG.statusEffects, entry.statusId))) {
            return { kind: entry.kind, statusId: entry.statusId, ...duration };
        }
        throw new Error('Invalid effect batch entry');
    });
}

/** Actor query receiver: validate, check this client's permission, write once, never forward. */
export async function receiveEffectDelivery({ actorUuid, entries } = {}) {
    let prepared;
    try { prepared = prepareEntries(entries); }
    catch { return failure('invalidRequest'); }
    const actor = await resolveDocument(actorUuid, 'Actor');
    if (!actor) return failure('actorUnavailable');
    if (!actor.canUserModify(game.user, 'update')) return failure('permission');
    const results = [];
    try {
        await withParameterChanges(actor, async () => {
            for (const entry of prepared) {
                results.push(entry.kind === 'status'
                    ? await applyLocalStatus(actor, entry.statusId, entry.duration)
                    : await applyLocalActiveEffects(actor, entry.effects, entry.duration));
            }
        });
        return { state: 'complete', reason: prepared.length ? 'finished' : 'empty', results };
    } catch (error) {
        console.error('Witcher effect delivery was not confirmed', error);
        // Earlier entries, or part of the failing entry, may already have been saved.
        return { ...failure('writeUnconfirmed', 'unknown'), results };
    }
}

export async function deliverActorEffects(actorUuid, entries) {
    let prepared;
    try { prepared = prepareEntries(entries); }
    catch { return failure('invalidRequest'); }
    const executor = await getEffectExecutor(actorUuid);
    if (executor.state !== 'ready') return failure(executor.reason);
    const request = { actorUuid, entries: prepared };
    if (executor.user.id === game.user.id) return receiveEffectDelivery(request);
    try {
        const result = await executor.user.query(DELIVERY_QUERY, request);
        if (['complete', 'refused', 'unknown'].includes(result?.state)) return serializeEffect(result);
    } catch (error) {
        console.error('Witcher effect delivery query failed', error);
    }
    // A lost response does not prove that no write occurred. Never retry automatically.
    return failure('responseUnconfirmed', 'unknown');
}

export function notifyEffectDelivery(result) {
    if (result.state !== 'complete') {
        const key = result.state === 'unknown' ? 'unconfirmed' : 'refused';
        ui.notifications.warn(game.i18n.localize(`WITCHER.EffectDelivery.${key}`));
    }
    return result;
}

/** Freeze the already calculated action. Repeated tokens do not duplicate the same entry. */
export function createDeliverySnapshot({ actor, item, message, targets }) {
    const recipients = new Map();
    for (const target of targets) {
        const entries = prepareEntries(target.entries).filter(entry => entry.kind === 'status'
            ? entry.statusId : entry.effects.length);
        if (!entries.length) continue;
        const recipient = recipients.get(target.actorUuid)
            ?? { actorUuid: target.actorUuid, name: target.name, entries: [], result: null };
        for (const entry of entries) {
            const signature = JSON.stringify(entry);
            if (recipient.entries.some(row => JSON.stringify(row.entry) === signature)) continue;
            recipient.entries.push({ entry, result: null });
        }
        recipients.set(target.actorUuid, recipient);
    }
    return {
        version: 1, authorId: game.user.id, state: 'waiting',
        action: { actorUuid: actor.uuid, itemUuid: item?.uuid ?? null, name: item?.name ?? actor.name,
            messageUuid: message?.uuid ?? null },
        targets: [...recipients.values()]
    };
}

/** Keep self and all selected targets in one preflight; no dice or writes here. */
export function collectSpellEffects(actor, item, duration, targets = game.user.targets) {
    const entries = (statuses, trigger) => {
        const rows = Object.values(statuses ?? {}).filter(effect => effect.statusEffect)
            .map(effect => ({ kind: 'status', statusId: effect.statusEffect, duration }));
        const effects = (item.effects ?? []).filter(effect => effect.system[trigger]).map(serializeEffect);
        if (effects.length) rows.push({ kind: 'activeEffects', effects, duration });
        return rows;
    };
    const recipients = [{ actorUuid: actor.uuid, name: actor.name,
        entries: entries(item.system.selfEffects, 'applySelf') }];
    const targetEntries = entries(item.system.onCastEffects, 'applyOnTarget');
    for (const target of targets) {
        if (!target.actor) continue;
        recipients.push({ actorUuid: target.actor.uuid, name: target.actor.name, entries: targetEntries });
    }
    return recipients;
}

function deliverySnapshot(message) {
    const data = message.getFlag(deliveryScope, 'effectDelivery');
    return data?.version === 1 ? serializeEffect(data) : null;
}

function canSendDelivery(message, snapshot) {
    return snapshot.authorId === game.user.id && message.canUserModify(game.user, 'update');
}

async function renderDelivery(snapshot) {
    const localize = key => game.i18n.localize(`WITCHER.EffectDelivery.${key}`);
    const resultLabel = result => localize(`results.${result?.reason ?? 'pending'}`);
    return foundry.applications.handlebars.renderTemplate(
        'systems/TheWitcherTRPG-RB-Version/templates/chat/effect-delivery.hbs', {
            action: snapshot.action, stateLabel: localize(`states.${snapshot.state}`),
            waiting: snapshot.state === 'waiting', needsReview: snapshot.state === 'needsReview',
            targets: snapshot.targets.map(target => ({
                name: target.name, resultLabel: target.result ? resultLabel(target.result) : null,
                entries: target.entries.map(row => ({
                    name: row.entry.kind === 'status'
                        ? game.i18n.localize(CONFIG.statusEffects[row.entry.statusId]?.name ?? row.entry.statusId)
                        : row.entry.effects.map(effect => effect.name).join(', '),
                    hasDuration: row.entry.duration != null, duration: row.entry.duration,
                    resultLabel: resultLabel(row.result)
                }))
            }))
        }
    );
}

async function saveDelivery(message, snapshot) {
    const content = message.schema.fields.content.clean(await renderDelivery(snapshot));
    const source = message.toObject(true);
    if (content === source.content && foundry.utils.equals(source.flags?.[deliveryScope]?.effectDelivery, snapshot)) return;
    const saved = await message.update({ content, [`flags.${deliveryScope}.effectDelivery`]: snapshot });
    if (!saved) throw new Error('Effect delivery message update was not confirmed');
}

function interruptedDelivery(snapshot) {
    snapshot.state = 'needsReview';
    for (const target of snapshot.targets) {
        if (target.result?.state === 'complete') continue;
        target.result = failure('responseUnconfirmed', 'unknown');
        for (const row of target.entries) {
            if (!row.result) row.result = failure('responseUnconfirmed', 'unknown');
        }
    }
}

/** Persist before sending; a lost acknowledgement never enables ordinary retry. */
export async function sendEffectDelivery(message) {
    message = game.messages.get(message.id) ?? message;
    const snapshot = deliverySnapshot(message);
    if (!snapshot || !canSendDelivery(message, snapshot)) return failure('permission');
    if (activeSends.has(message.uuid) || ['complete', 'needsReview'].includes(snapshot.state)) return snapshot;
    activeSends.add(message.uuid);
    try {
        if (snapshot.state === 'sending') {
            interruptedDelivery(snapshot);
            await saveDelivery(message, snapshot);
            return snapshot;
        }
        let ready = true;
        for (const target of snapshot.targets) {
            const executor = await getEffectExecutor(target.actorUuid);
            target.result = executor.state === 'ready' ? null : failure(executor.reason);
            if (target.result) ready = false;
        }
        if (!ready) {
            await saveDelivery(message, snapshot);
            return snapshot;
        }

        snapshot.state = 'sending';
        await saveDelivery(message, snapshot);
        for (const target of snapshot.targets) {
            const result = await deliverActorEffects(target.actorUuid, target.entries.map(row => row.entry));
            target.result = result;
            // A complete Actor response must confirm every entry. Bare true is not a receipt.
            if (result.state === 'complete' && (result.results?.length !== target.entries.length
                || result.results.some(row => row.state !== 'complete'))) {
                target.result = failure('responseUnconfirmed', 'unknown');
            }
            for (const [index, row] of target.entries.entries()) {
                const notAttempted = result.reason === 'writeUnconfirmed' && Array.isArray(result.results)
                    && index > result.results.length;
                row.result = result.results?.[index] ?? (target.result.state === 'unknown' && !notAttempted
                    ? failure('responseUnconfirmed', 'unknown') : failure('notSent'));
            }
            if (target.result.state !== 'complete') {
                snapshot.state = 'needsReview';
                await saveDelivery(message, snapshot);
                return snapshot;
            }
            await saveDelivery(message, snapshot);
        }
        snapshot.state = 'complete';
        await saveDelivery(message, snapshot);
        return snapshot;
    } catch (error) {
        console.error('Witcher effect delivery message failed', error);
        // If even this save fails, persisted sending is treated as needsReview after reload.
        if (snapshot.state !== 'waiting') {
            interruptedDelivery(snapshot);
            try { await saveDelivery(message, snapshot); }
            catch (saveError) { console.error('Witcher effect delivery recovery failed', saveError); }
        }
        return notifyEffectDelivery(failure('responseUnconfirmed', 'unknown'));
    } finally {
        activeSends.delete(message.uuid);
    }
}

export async function createEffectDelivery({ actor, item, message, targets }) {
    const snapshot = createDeliverySnapshot({ actor, item, message, targets });
    if (!snapshot.targets.length) return null;
    const card = await ChatMessage.create({
        author: game.user.id, type: 'base', speaker: ChatMessage.getSpeaker({ actor }),
        ...deliveryVisibility(message),
        content: await renderDelivery(snapshot),
        flags: { [deliveryScope]: { effectDelivery: snapshot } }
    });
    if (!card) throw new Error('Effect delivery message was not created');
    await sendEffectDelivery(card);
    return card;
}

function deliveryVisibility(message) {
    if (message) return { whisper: [...message.whisper], blind: message.blind };
    const visibility = {};
    ChatMessage.applyMode(visibility, game.settings.get('core', 'messageMode'));
    return visibility;
}

/** A warning is a record of the failed consequence, never a replay of the action. */
export async function reportDeliveryConsequence({ actor, actorUuid = actor?.uuid, message, itemUuid,
    applyWhen, statusId, duration, adrenaline = false, result }) {
    try {
        const target = actor ?? await resolveDocument(actorUuid, 'Actor');
        const content = await foundry.applications.handlebars.renderTemplate(
            'systems/TheWitcherTRPG-RB-Version/templates/chat/effect-delivery-warning.hbs', {
                actorUuid, actorName: target?.name ?? actorUuid, itemUuid, messageUuid: message?.uuid,
                actionLabel: game.i18n.localize(`WITCHER.EffectDelivery.actions.${applyWhen ?? (adrenaline ? 'adrenaline' : 'status')}`),
                reasonLabel: game.i18n.localize(`WITCHER.EffectDelivery.results.${result.reason}`),
                unknown: result.state === 'unknown', adrenaline, statusId, duration,
                statusName: statusId ? game.i18n.localize(CONFIG.statusEffects[statusId]?.name ?? statusId) : null
            }
        );
        const warning = await ChatMessage.create({ author: game.user.id, type: 'base',
            speaker: target ? ChatMessage.getSpeaker({ actor: target }) : {},
            ...deliveryVisibility(message), content });
        if (!warning) notifyEffectDelivery(result);
    } catch (error) {
        console.error('Witcher consequence warning failed', error);
        notifyEffectDelivery(result);
    }
    return result;
}

/** Resolve once and freeze only this Item consequence; damage/consume are not retried. */
export async function createItemEffectDelivery({ actor, itemUuid, applyWhen, duration, message }) {
    try {
        const source = await resolveEffectSource(itemUuid, applyWhen);
        if (source.state !== 'complete') {
            return await reportDeliveryConsequence({ actor, itemUuid, applyWhen, message, result: source });
        }
        return await createEffectDelivery({ actor, item: source.source, message,
            targets: [{ actorUuid: actor.uuid, name: actor.name,
                entries: [{ kind: 'activeEffects', effects: source.effects, duration }] }] });
    } catch (error) {
        console.error('Witcher Item consequence failed', error);
        return reportDeliveryConsequence({ actor, itemUuid, applyWhen, message,
            result: failure('responseUnconfirmed', 'unknown') });
    }
}

export async function applyParryStagger(actorUuid, message) {
    let result;
    try { result = await deliverActorEffects(actorUuid, [{ kind: 'status', statusId: 'staggered', duration: 1 }]); }
    catch { result = failure('responseUnconfirmed', 'unknown'); }
    if (result.state === 'complete') return result;
    return reportDeliveryConsequence({ actorUuid, message, statusId: 'staggered', duration: 1, result });
}

export async function applyCriticalAdrenaline(actorUuid, message) {
    if (!game.settings.get(deliveryScope, 'useOptionalAdrenaline')) return { state: 'complete', reason: 'disabled' };
    let result;
    try {
        const executor = await getEffectExecutor(actorUuid);
        if (executor.state !== 'ready') result = failure(executor.reason);
        else if (executor.user.id === game.user.id) {
            await executor.actor.addAdrenaline();
            return { state: 'complete', reason: 'applied' };
        } else {
            const confirmed = await executor.user.query(`${deliveryScope}.query`, {
                uuid: actorUuid, function: 'addAdrenaline', data: []
            });
            if (confirmed === true) return { state: 'complete', reason: 'applied' };
            result = failure('responseUnconfirmed', 'unknown');
        }
    } catch { result = failure('responseUnconfirmed', 'unknown'); }
    return reportDeliveryConsequence({ actorUuid, message, adrenaline: true, result });
}

/** Called from the existing chat hook; no background retry and no cross-client lock. */
export async function bindEffectDelivery(message, html) {
    const snapshot = deliverySnapshot(message);
    if (!snapshot) return;
    const allowed = canSendDelivery(message, snapshot);
    if (snapshot.state === 'sending' && allowed && !activeSends.has(message.uuid)) {
        await sendEffectDelivery(message);
        return;
    }
    // Native blind messages hide the content even from their author. Expose only
    // neutral delivery controls to that author, never the targets or effects.
    if (message.isContentVisible === false && allowed && !html.querySelector('.effect-delivery-controls')) {
        const controls = document.createElement('div');
        controls.className = 'effect-delivery-controls';
        const state = document.createElement('p');
        state.textContent = game.i18n.localize(`WITCHER.EffectDelivery.states.${snapshot.state}`);
        controls.append(state);
        if (snapshot.state === 'waiting') {
            const send = document.createElement('button');
            send.type = 'button';
            send.className = 'send-effect-delivery';
            send.textContent = game.i18n.localize('WITCHER.EffectDelivery.send');
            controls.append(send);
        }
        html.querySelector('.message-content')?.append(controls);
    }
    const button = html.querySelector('button.send-effect-delivery');
    if (!button) return;
    button.hidden = !allowed || snapshot.state !== 'waiting';
    button.disabled = activeSends.has(message.uuid);
    if (boundButtons.has(button)) return;
    boundButtons.add(button);
    button.addEventListener('click', async event => {
        event.preventDefault();
        button.disabled = true;
        try { await sendEffectDelivery(message); }
        finally { button.disabled = false; }
    });
}
