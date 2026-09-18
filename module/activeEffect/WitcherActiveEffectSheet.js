import { baseMixin } from './mixins/baseMixin.js';
import { temporaryItemImprovementMixin } from './mixins/temporaryItemImprovementMixin.js';
import { MODIFIER_DEFAULTS, derivedModifierChoices, getEffectTargetType, modifierSettings, supportsModifierChange, switchModifierChannel } from './modifierContext.js';

const DialogV2 = foundry.applications.api.DialogV2;

export class WitcherActiveEffectConfig extends foundry.applications.sheets.ActiveEffectConfig {
    #attributeKeyListId = `witcher-attribute-key-list-${foundry.utils.randomID()}`;

    static DEFAULT_OPTIONS = {
        actions: {
            wizard: WitcherActiveEffectConfig.wizardAction,
            addChange: WitcherActiveEffectConfig.addChangeAction
        }
    };

    /** @override */
    static PARTS = {
        header: { template: 'templates/sheets/active-effect/header.hbs' },
        tabs: { template: 'templates/generic/tab-navigation.hbs' },
        details: { template: 'templates/sheets/active-effect/details.hbs', scrollable: [''] },
        duration: { template: 'templates/sheets/active-effect/duration.hbs' },
        changes: {
            template: 'templates/sheets/active-effect/changes.hbs',
            templates: ['templates/sheets/active-effect/change.hbs',
                'systems/TheWitcherTRPG-RB-Version/templates/sheets/activeEffect/change.hbs',
                'systems/TheWitcherTRPG-RB-Version/templates/sheets/activeEffect/modifier-settings.hbs'],
            scrollable: ['ol[data-changes]']
        },
        systemSpecific: {
            template: 'systems/TheWitcherTRPG-RB-Version/templates/sheets/activeEffect/system-specific.hbs',
            scrollable: ['']
        },
        footer: { template: 'templates/generic/form-footer.hbs' }
    };

    static TABS = {
        sheet: {
            ...super.TABS.sheet,
            tabs: [...super.TABS.sheet.tabs, { id: 'systemSpecific' }]
        }
    };

    /** @override */
    async _prepareContext(options) {
        const context = await super._prepareContext(options);
        context.systemFields = this.document.system.schema.fields;
        return context;
    }

    _readFormData() {
        return this._processFormData(null, this.form, new foundry.applications.ux.FormDataExtended(this.form));
    }

    _modifierEditorContext(change, prefix) {
        const settings = modifierSettings(change);
        return {
            settings,
            modifierPrefix: prefix,
            derivedChoices: derivedModifierChoices(),
            modifierInputs: Object.keys(MODIFIER_DEFAULTS).map(key => ({
                key, name: `${prefix}.${key}`, value: settings[key], label: `WITCHER.Effect.Modifier.${key}`,
                hint: `WITCHER.Effect.Modifier.${key}Hint`,
                disabled: key === 'fullEffect' ? !settings.affectsParameter
                    : ['shiftsCap', 'affectsAdvancement'].includes(key) ? settings.affectsRoll
                    : key === 'optionalOnRoll' ? !settings.affectsRoll : false
            }))
        };
    }

    async _renderChange(context) {
        const change = foundry.utils.deepClone(context.change);
        const changeType = ActiveEffect.CHANGE_TYPES[change.type];
        const targetType = context.targetType ?? getEffectTargetType(this.document);
        // Preserve registered custom renderers and native non-numeric/Item/Token rows.
        if (targetType !== 'Actor' || !supportsModifierChange(change) || changeType?.render) {
            return super._renderChange({ ...context, change });
        }
        if (typeof change.value !== 'string') change.value = JSON.stringify(change.value);
        for (const key of ['key', 'type', 'value', 'phase', 'priority']) {
            change[`${key}Path`] = `system.changes.${context.index}.${key}`;
        }
        return foundry.applications.handlebars.renderTemplate(
            'systems/TheWitcherTRPG-RB-Version/templates/sheets/activeEffect/change.hbs', {
                ...context, change, changeType,
                ...this._modifierEditorContext(change, `system.changes.${context.index}`)
            }
        );
    }

    _processChangeSubmission(change, index) {
        super._processChangeSubmission(change, index);
        if (!supportsModifierChange(change)) {
            for (const key of [...Object.keys(MODIFIER_DEFAULTS), 'excludedDerived']) delete change[key];
            return;
        }
        const prior = this.document._source.system.changes[index];
        const sameTarget = prior?.key === change.key && prior?.type === change.type;
        Object.assign(change, modifierSettings({ ...(sameTarget ? prior : {}), ...change }));
        // FormDataExtended omits disabled inputs. Read the row's explicit UI state
        // so switching channels cannot revive a previously saved incompatible flag.
        for (const key of Object.keys(MODIFIER_DEFAULTS)) {
            const input = this.form?.querySelector(`[name="system.changes.${index}.${key}"]`);
            if (input) change[key] = input.checked;
        }
        // An empty multiple select has no submitted value; it means clearing the list.
        if (this.form?.querySelector(`[name="system.changes.${index}.excludedDerived"]`)) {
            const select = this.form.querySelector(`[name="system.changes.${index}.excludedDerived"]`);
            change.excludedDerived = select.disabled ? [] : Array.from(select.selectedOptions, option => option.value);
        }
    }

    _syncModifierControls(container, changedField) {
        const inputs = Array.from(container.querySelectorAll('[data-modifier-flag]'));
        if (!inputs.length) return;
        const settings = switchModifierChannel(Object.fromEntries(inputs.map(input => [input.dataset.modifierFlag, input.checked])), changedField);
        for (const input of inputs) {
            const key = input.dataset.modifierFlag;
            input.checked = settings[key];
            input.disabled = key === 'fullEffect' ? !settings.affectsParameter
                : ['shiftsCap', 'affectsAdvancement'].includes(key) ? settings.affectsRoll
                : key === 'optionalOnRoll' ? !settings.affectsRoll : false;
        }
        const select = container.querySelector('[data-modifier-exclusions]');
        if (select) {
            select.disabled = !settings.affectsParameter;
            if (select.disabled) for (const option of select.options) option.selected = false;
        }
    }

    async _onChangeForm(formConfig, event) {
        const field = event.target.dataset.modifierFlag;
        if (field) this._syncModifierControls(event.target.closest('[data-modifier-settings]'), field);
        await super._onChangeForm(formConfig, event);
        const row = event.target.closest('li[data-index]');
        const changesTarget = event.target.name === 'transfer' ||
            /^system\.(applySelf|applyOnTarget|applyOnHit|applyOnDamage)$/.test(event.target.name);
        if (!changesTarget && !(row && /\.(key|type)$/.test(event.target.name))) return;

        const submitted = this._readFormData();
        const changes = Object.values(submitted.system?.changes ?? {});
        const targetType = getEffectTargetType(this.document, submitted);
        const rows = changesTarget ? this.element.querySelectorAll('li[data-index]') : [row];
        for (const current of rows) {
            const index = Number(current.dataset.index);
            const change = changes[index];
            if (!change) continue;
            const changeTypes = Object.fromEntries(Object.entries(ActiveEffect.CHANGE_TYPES)
                .map(([type, config]) => [type, game.i18n.localize(config.label)]));
            const rendered = await this._renderChange({ change, index, targetType,
                fields: this.document.system.schema.fields.changes.element.fields,
                changeTypes, defaultPriority: ActiveEffect.CHANGE_TYPES[change.type]?.defaultPriority ?? 0 });
            current.outerHTML = rendered;
        }
        this.autocomplete(targetType);
    }

    async _onRender(context, options) {
        await super._onRender(context, options);

        this._ensureWizardButton();
        this.autocomplete();
    }

    _ensureWizardButton() {
        const section = this.element.querySelector("section[data-tab='changes']");
        const addButton = section?.querySelector('button[data-action="addChange"]');
        if (!addButton) return;

        let wizard = section.querySelector('[data-witcher-effect-control="wizard"]');
        if (!wizard) {
            wizard = document.createElement('a');
            wizard.dataset.witcherEffectControl = 'wizard';
            wizard.setAttribute('data-action', 'wizard');
            const icon = document.createElement('i');
            icon.className = 'fa-solid fa-wand-magic-sparkles';
            wizard.appendChild(icon);
        }
        addButton.after(wizard);
    }

    static async addChangeAction() {
        const submitted = this._readFormData();
        const changes = foundry.utils.deepClone(Object.values(submitted.system?.changes ?? {}));
        changes.push({
            ...this.document.system.schema.fields.changes.element.getInitialValue(),
            phase: submitted.system?.applyAfterCalculations ? 'final' : 'initial'
        });
        return this.submit({ updateData: { system: { changes } } });
    }

    static async wizardAction() {
        let selects;
        const initial = this._readFormData();
        const targetType = getEffectTargetType(this.document, initial);

        switch (this.document.type) {
            case 'base':
                selects = targetType === 'Actor' ? this.getActiveEffectsBasePaths() : this.getActiveEffectsItemImprovementPaths();
                break;
            case 'temporaryItemImprovement':
                selects = this.getActiveEffectsItemImprovementPaths();
                break;
        }

        const dialogTemplate = await foundry.applications.handlebars.renderTemplate(
            'systems/TheWitcherTRPG-RB-Version/templates/dialog/activeEffects/wizard.hbs',
            {
                selects,
                modifierWizard: this.document.type === 'base' && targetType === 'Actor',
                ...this._modifierEditorContext({}, 'modifier')
            }
        );

        return DialogV2.prompt({
            classes: ['witcher-effect-wizard'],
            position: { width: 720 },
            content: dialogTemplate,
            modal: true,
            render: (_event, dialog) => {
                dialog.element.addEventListener('change', event => {
                    if (event.target.dataset.modifierFlag) {
                        this._syncModifierControls(event.target.closest('[data-modifier-settings]'), event.target.dataset.modifierFlag);
                    }
                });
            },
            ok: {
                callback: async (event, button) => {
                    const wizard = foundry.utils.expandObject(new foundry.applications.ux.FormDataExtended(button.form).object);
                    const paths = button.form.elements.path.value.split(',').filter(Boolean);
                    const submitted = this._readFormData();
                    const newChanges = foundry.utils.deepClone(Object.values(submitted.system?.changes ?? {}));
                    const schema = this.document.system.schema.fields.changes.element;
                    for (const key of paths) {
                        const change = { ...schema.getInitialValue(), key,
                            phase: submitted.system?.applyAfterCalculations ? 'final' : 'initial' };
                        if (this.document.type === 'base' && targetType === 'Actor' && supportsModifierChange(change)) {
                            Object.assign(change, modifierSettings(wizard.modifier));
                        }
                        newChanges.push(change);
                    }
                    return this.submit({ updateData: { system: { changes: newChanges } } });
                }
            }
        });
    }

    autocomplete(targetType = getEffectTargetType(this.document)) {
        let html = this.element;
        const effectsSection = html.querySelector("section[data-tab='changes']");
        if (!effectsSection) return;

        const inputFields = effectsSection.querySelectorAll('.key input');
        let datalist = effectsSection.querySelector('datalist[data-witcher-effect-control="attribute-key-list"]');
        if (!datalist) {
            datalist = document.createElement('datalist');
            datalist.dataset.witcherEffectControl = 'attribute-key-list';
        }
        const attributeKeyOptions = {};

        datalist.id = this.#attributeKeyListId;
        inputFields.forEach(inputField => {
            inputField.setAttribute('list', this.#attributeKeyListId);
        });

        const config = CONFIG[targetType];

        for (const datamodel in config.dataModels) {
            config.dataModels[datamodel].schema.apply(function () {
                if (!(this instanceof foundry.data.fields.SchemaField)) {
                    attributeKeyOptions[this.fieldPath] = game.i18n.localize(this.label);
                }
            });
        }

        const sortedKeys = Object.keys(attributeKeyOptions).sort();
        const options = document.createDocumentFragment();
        sortedKeys.forEach(key => {
            const attributeKeyOption = document.createElement('option');
            attributeKeyOption.value = key;
            if (!!attributeKeyOptions[key]) attributeKeyOption.label = attributeKeyOptions[key];
            options.appendChild(attributeKeyOption);
        });

        datalist.replaceChildren(options);
        effectsSection.append(datalist);
    }
}

Object.assign(WitcherActiveEffectConfig.prototype, baseMixin);
Object.assign(WitcherActiveEffectConfig.prototype, temporaryItemImprovementMixin);
