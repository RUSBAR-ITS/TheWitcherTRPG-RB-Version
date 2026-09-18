import WitcherConfigurationSheet from './WitcherConfigurationSheet.js';

export default class WitcherProfessionConfigurationSheet extends WitcherConfigurationSheet {
    /** @override */
    static DEFAULT_OPTIONS = {
        actions: {
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

    async _preparePartContext(partId, context, options) {
        let partContext = {
            item: context.item,
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
