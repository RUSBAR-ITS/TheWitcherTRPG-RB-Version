import { identifiedSkills, PROFESSION_SKILL_PATHS } from '../../skillIdentity.js';
import WitcherConfigurationSheet from './WitcherConfigurationSheet.js';

export default class WitcherProfessionConfigurationSheet extends WitcherConfigurationSheet {
    /** @override */
    static DEFAULT_OPTIONS = {
        actions: {
            insertTemporaryHpParameter: WitcherProfessionConfigurationSheet._onInsertTemporaryHpParameter,
            generateSkillId: WitcherProfessionConfigurationSheet._onGenerateSkillId,
            addEffectDamageProperties: WitcherProfessionConfigurationSheet._onAddEffectDamageProperties,
            removeEffectDamageProperties: WitcherProfessionConfigurationSheet._oRemoveEffectDamageProperties,
            addThreshold: WitcherProfessionConfigurationSheet._onAddThreshold,
            removeThreshold: WitcherProfessionConfigurationSheet._oRemoveThreshold
        }
    };

    static PARTS = {
        ...super.PARTS,
        skillPath1: {
            template:
                'systems/TheWitcherTRPG-RB-Version/templates/sheets/item/configuration/partials/profession/skillPathPart.hbs',
            scrollable: ['']
        },
        skillPath2: {
            template:
                'systems/TheWitcherTRPG-RB-Version/templates/sheets/item/configuration/partials/profession/skillPathPart.hbs',
            scrollable: ['']
        },
        skillPath3: {
            template:
                'systems/TheWitcherTRPG-RB-Version/templates/sheets/item/configuration/partials/profession/skillPathPart.hbs',
            scrollable: ['']
        }
    };

    static TABS = {
        primary: {
            tabs: [
                { id: 'general' },
                { id: 'skillPath1' },
                { id: 'skillPath2' },
                { id: 'skillPath3' },
                { id: 'activeEffects' }
            ],
            initial: 'general',
            labelPrefix: 'WITCHER.Item.Settings'
        }
    };

    /** @inheritdoc */
    _prepareTabs(group) {
        const tabs = super._prepareTabs(group);
        if (group === 'primary') {
            const system = this.item.system;
            tabs.skillPath1.label = this.item.system.skillPath1.pathName;
            tabs.skillPath2.label = this.item.system.skillPath2.pathName;
            tabs.skillPath3.label = this.item.system.skillPath3.pathName;
        }

        return tabs;
    }

    temporaryHpParameters() {
        const localize = key => game.i18n.localize(`WITCHER.TemporaryHP.${key}`);
        const entries = [{ target: { kind: 'ability' }, label: localize('ability'), sourceOnly: true }];
        for (const [key, stat] of Object.entries(CONFIG.WITCHER.statMap)) {
            if (stat.origin === 'stats') entries.push({ target: { kind: 'stat', key }, label: game.i18n.localize(stat.label) });
        }
        for (const [key, skill] of Object.entries(CONFIG.WITCHER.skillMap)) {
            entries.push({ target: { kind: 'builtin', key }, label: game.i18n.localize(skill.rollLabel ?? skill.label) });
        }
        const items = new Map([...[this.item], ...(this.item.actor?.items ?? []), ...(game.items ?? [])].map(item => [item.uuid, item]));
        const seen = new Set();
        for (const skill of identifiedSkills(items.values())) {
            const id = `${skill.kind}:${skill.skillId}`;
            if (seen.has(id)) continue;
            seen.add(id);
            entries.push({ target: { kind: skill.kind, skillId: skill.skillId }, label: `${skill.label} [${skill.skillId}]` });
        }
        return entries;
    }

    async _prepareContext(options) {
        const context = await super._prepareContext(options);
        const entries = this.temporaryHpParameters();
        context.temporaryHpViews = {};
        for (const path of PROFESSION_SKILL_PATHS) {
            const config = foundry.utils.getProperty(this.item.system, `${path}.skillUsage.temporaryHealth`);
            context.temporaryHpViews[path] = Object.entries(config?.references ?? {}).map(([alias, ref]) => {
                const entry = entries.find(entry => entry.target.kind === ref.target.kind &&
                    entry.target.key === (ref.target.key || undefined) && entry.target.skillId === (ref.target.skillId || undefined));
                return { alias, label: entry?.label ?? ref.target.skillId ?? ref.target.key,
                    role: game.i18n.localize(`WITCHER.TemporaryHP.${ref.role}`),
                    value: game.i18n.localize(`WITCHER.TemporaryHP.${ref.value}`) };
            });
        }
        return context;
    }

    static async _onGenerateSkillId(event, element) {
        event.preventDefault();
        const { path } = this.findSkillByPath(element.dataset.skillPath);
        return this.item.update({ [`system.${path}.skillId`]: foundry.utils.randomID() });
    }

    static async _onInsertTemporaryHpParameter(event, element) {
        event.preventDefault();
        const { path } = this.findSkillByPath(element.dataset.skillPath);
        const field = element.dataset.formulaField;
        if (!['value', 'duration'].includes(field)) return;
        const name = `system.${path}.skillUsage.temporaryHealth.temporaryHp.${field}`;
        const input = this.element.querySelector(`[name="${name}"]`);
        const formula = input.value;
        const start = input.selectionStart ?? formula.length, end = input.selectionEnd ?? start;
        const entries = this.temporaryHpParameters();
        const groups = ['ability', 'stat', 'builtin', 'item', 'profession'].map(kind => ({
            label: game.i18n.localize(`WITCHER.TemporaryHP.${kind}`),
            entries: entries.map((entry, index) => ({ ...entry, index })).filter(entry => entry.target.kind === kind)
        })).filter(group => group.entries.length);
        const content = await foundry.applications.handlebars.renderTemplate(
            'systems/TheWitcherTRPG-RB-Version/templates/dialog/temporary-hp-parameter.hbs', { groups });
        const selected = await foundry.applications.api.DialogV2.prompt({
            window: { title: game.i18n.localize('WITCHER.TemporaryHP.insertParameter') },
            position: { width: 600 }, content, modal: true,
            render: (_event, dialog) => {
                const form = dialog.element.querySelector('form');
                const refresh = () => {
                    for (const option of form.elements.parameter.options) {
                        option.disabled = !!option.dataset.sourceOnly && form.elements.role.value === 'target';
                    }
                    if (form.elements.parameter.selectedOptions[0]?.disabled) {
                        form.elements.parameter.value = [...form.elements.parameter.options].find(option => !option.disabled)?.value ?? '';
                    }
                };
                form.elements.role.addEventListener('change', refresh);
                refresh();
            },
            ok: { label: game.i18n.localize('WITCHER.TemporaryHP.insert'), callback: (_event, button) => {
                const form = button.form;
                return { role: form.elements.role.value, target: entries[Number(form.elements.parameter.value)]?.target,
                    value: form.elements.valueKind.value };
            } }
        });
        if (!selected?.target || (selected.target.kind === 'ability' && selected.role !== 'source')) return;
        const config = foundry.utils.getProperty(this.item.system, `${path}.skillUsage.temporaryHealth`);
        let index = 1;
        while (Object.hasOwn(config.references, `p${index}`) || new RegExp(`@p${index}(?![0-9])`).test(formula)) index++;
        const alias = `p${index}`;
        return this.item.update({
            [name]: formula.slice(0, start) + `@${alias}` + formula.slice(end),
            [`system.${path}.skillUsage.temporaryHealth.references.${alias}`]: selected
        });
    }

    async _preparePartContext(partId, context, options) {
        let partContext = {
            item: context.item,
            temporaryHpViews: context.temporaryHpViews,
            config: CONFIG.WITCHER,
            tab: context.tabs[partId],
            partId: partId
        };

        if (partId === 'skillPath1') {
            return {
                ...partContext,
                skillPathFields: context.systemFields.skillPath1,
                skillPath: context.item.system.skillPath1
            };
        }
        if (partId === 'skillPath2') {
            return {
                ...partContext,
                skillPathFields: context.systemFields.skillPath2,
                skillPath: context.item.system.skillPath2
            };
        }
        if (partId === 'skillPath3') {
            return {
                ...partContext,
                skillPathFields: context.systemFields.skillPath3,
                skillPath: context.item.system.skillPath3
            };
        }

        return context;
    }

    _onChangeForm(formConfig, event) {
        super._onChangeForm(formConfig, event);
        if (event.target.dataset.action === 'editEffectDamageProperties') {
            this._onEditEffectDamageProperties(event, event.target);
        }
        if (event.target.dataset.action === 'editThreshold') {
            this._onEditThreshold(event, event.target);
        }
    }

    static async _onAddEffectDamageProperties(event, element) {
        event.preventDefault();
        let path = element.dataset.target;

        let skillObject = this.findSkillByPath(path);

        let id = foundry.utils.randomID();
        return this.item.update({
            [`system.${skillObject.path}.skillAttack.damageProperties.effects.${id}`]: { percentage: 0 }
        });
    }

    async _onEditEffectDamageProperties(event, element) {
        event.preventDefault();
        let effectId = element.closest('.list-item').dataset.id;

        let field = element.dataset.field;
        let value = element.value;

        if (value == 'on') {
            value = element.checked;
        }

        let path = element.closest('.list-item').dataset.target;
        let skillObject = this.findSkillByPath(path);

        return this.item.update({
            [`system.${skillObject.path}.skillAttack.damageProperties.effects.${effectId}.${field}`]: value
        });
    }

    static async _oRemoveEffectDamageProperties(event, element) {
        event.preventDefault();
        let effectId = element.closest('.list-item').dataset.id;

        let path = element.closest('.list-item').dataset.target;
        let skillObject = this.findSkillByPath(path);

        return this.item.update({ [`system.${skillObject.path}.skillAttack.damageProperties.effects.-=${effectId}`]: null });
    }

    static async _onAddThreshold(event, element) {
        event.preventDefault();
        let path = element.dataset.target;
        let skillObject = this.findSkillByPath(path);

        let id = foundry.utils.randomID();
        return this.item.update({
            [`system.${skillObject.path}.thresholds.thresholds.${id}`]: { value: 0 }
        });
    }

    async _onEditThreshold(event, element) {
        event.preventDefault();
        let id = element.closest('.list-item').dataset.id;

        let field = element.dataset.field;
        let value = element.value;

        let path = element.closest('.list-item').dataset.target;
        let skillObject = this.findSkillByPath(path);

        return this.item.update({
            [`system.${skillObject.path}.thresholds.thresholds.${id}.${field}`]: value
        });
    }

    static async _oRemoveThreshold(event, element) {
        event.preventDefault();
        let id = element.closest('.list-item').dataset.id;

        let path = element.closest('.list-item').dataset.target;
        let skillObject = this.findSkillByPath(path);

        return this.item.update({ [`system.${skillObject.path}.thresholds.thresholds.-=${id}`]: null });
        //v14
        // this.item.update({ [`${target}.${id}`]: _del });
    }

    findSkillByPath(path) {
        if (!/^(definingSkill|skillPath[1-3]\.skill[1-3])$/.test(path)) throw new TypeError('Invalid profession slot');
        const skill = foundry.utils.getProperty(this.item.system, path);
        if (!skill) throw new TypeError('Unknown profession slot');
        return { skill, path };
    }
}
