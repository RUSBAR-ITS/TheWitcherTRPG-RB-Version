import { collectRollModifiers, resolveRollModifiers } from '../../actor/rollContext.js';

/** Called only after the action/skill is known; call again after a context change. */
export async function chooseRollModifiers(actor, context, { title = '', manual = 0 } = {}) {
    const collection = collectRollModifiers(actor, context);
    if (!collection.optional.length) return resolveRollModifiers(collection, [], manual);
    const content = await foundry.applications.handlebars.renderTemplate(
        'systems/TheWitcherTRPG-RB-Version/templates/dialog/conditional-modifiers.hbs', {
            candidates: collection.optional.map((row, index) => ({ ...row, index,
                operation: game.i18n.localize(`EFFECT.CHANGES.TYPES.${row.type}`) }))
        });
    const selected = await foundry.applications.api.DialogV2.prompt({
        window: { title: title || game.i18n.localize('WITCHER.Effect.Modifier.optionalOnRoll') },
        content, rejectClose: false,
        ok: {
            label: game.i18n.localize('WITCHER.Button.Continue'),
            callback: (_event, button) => collection.optional.filter((_row, index) =>
                button.form.elements.namedItem(`modifier-${index}`)?.checked).map(row => row.id)
        }
    });
    if (selected === null || selected === undefined) return null;
    return resolveRollModifiers(collection, selected, manual);
}
