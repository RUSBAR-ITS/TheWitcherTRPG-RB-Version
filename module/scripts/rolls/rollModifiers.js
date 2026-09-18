/** Numeric contributions and labels are kept separate until the Roll boundary. */
export function formatRollModifier(value, label = '', { details = false, hideZero = true } = {}) {
    const number = Number(value);
    if (!Number.isFinite(number)) throw new TypeError('A roll modifier must be finite');
    if (hideZero && number === 0) return '';
    const annotation = details && label ? String(label).replace(/[\[\]]/g, '').trim() : '';
    return `${number < 0 ? '-' : '+'}${Math.abs(number)}${annotation ? `[${annotation}]` : ''}`;
}

export function formatRollContributions(contributions, options = {}) {
    return contributions.map(({ value, label }) => formatRollModifier(value, label, options)).join('');
}
