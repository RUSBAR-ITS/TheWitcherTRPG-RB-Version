import { chooseRollModifiers } from './conditionalModifiers.js';
import { formatRollContributions } from './rollModifiers.js';
import { getCustomModifierValue } from '../helper.js';

/** All choices finish before the caller spends resources or executes the action. */
export async function prepareCheck(actor, context, { manual = 0, promptManual = false, title = '' } = {}) {
    if (promptManual) {
        manual = await getCustomModifierValue(title);
        if (manual === null) return null;
    }
    const result = await chooseRollModifiers(actor, {
        includeStat: !actor.system.dontAddAttr, ...context
    }, { manual, title });
    if (!result) return null;
    const reverse = ['<', '<='].includes(context.comparison);
    return { ...result, formula: '1d10' + (reverse ? '' : formatRollContributions(result.contributions, {
        details: game.settings.get('TheWitcherTRPG-RB-Version', 'displayRollsDetails')
    })) };
}
