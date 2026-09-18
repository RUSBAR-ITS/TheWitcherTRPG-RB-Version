import { isManualDerivedStat } from '../../../data/actor/derivedStatData.js';
const { HandlebarsApplicationMixin } = foundry.applications.api;
const { ActorSheetV2 } = foundry.applications.sheets;
import { skillMixin } from '../mixins/skillMixin.js';
import { statMixin } from '../mixins/statMixin.js';

export default class WitcherModifiersConfiguration extends HandlebarsApplicationMixin(ActorSheetV2) {
    statMap = CONFIG.WITCHER.statMap;
    skillMap = CONFIG.WITCHER.skillMap;

    constructor(options = {}) {
        super(options);

        this.type = options.type;
        this.skillKey = options.skillKey;
    }

    /** @override */
    static DEFAULT_OPTIONS = {
        window: {
            resizable: true
        },
        position: {
            width: 520
        },
        classes: ['witcher', 'sheet', 'actor', 'modifier-configuration'],
        form: {
            submitOnChange: true,
            closeOnSubmit: false
        },
        actions: {}
    };

    static PARTS = {
        stats: {
            template: 'systems/TheWitcherTRPG-RB-Version/templates/sheets/actor/configuration/app/edit-stats.hbs'
        },
        skills: {
            template: 'systems/TheWitcherTRPG-RB-Version/templates/sheets/actor/configuration/app/edit-skills.hbs'
        }
    };

    async _onRender(context, options) {
        await super._onRender(context, options);

        this.activateListeners(this.element);
    }

    activateListeners(html) {
        //mixins
        this.statListener(html);
        this.skillListener(html);
    }

    _processFormData(event, form, formData) {
        const data = super._processFormData(event, form, formData);
        const flat = foundry.utils.flattenObject(data);
        const allowed = {};
        for (const [path, value] of Object.entries(flat)) {
            let match = /^system\.derivedStats\.([^.]+)\.unmodifiedMax$/.exec(path);
            if (match && isManualDerivedStat(match[1], this.document.system.customStat)) allowed[path] = value;
            match = /^system\.stats\.([^.]+)\.(unmodifiedMax|baseCap)$/.exec(path);
            if (match && this.document.system.stats[match[1]] &&
                (match[2] !== 'baseCap' || Object.hasOwn(this.document.system.stats[match[1]], 'baseCap'))) allowed[path] = value;
            match = /^system\.skills\.([^.]+)\.([^.]+)\.(value|baseCap|isProfession|isPickup|isLearned)$/.exec(path);
            if (match && this.document.system.skills[match[1]]?.[match[2]]) allowed[path] = value;
            if (path === 'system.reputation.unmodifiedMax') allowed[path] = value;
        }
        return foundry.utils.expandObject(allowed);
    }

    async _prepareContext(options) {
        const context = await super._prepareContext(options);
        context.config = CONFIG.WITCHER;
        context.config.statLabels = Object.keys(CONFIG.WITCHER.statMap).reduce((obj, stat) => {
            obj[stat] = CONFIG.WITCHER.statMap[stat].label ?? CONFIG.WITCHER.statMap[stat].labelShort;
            return obj;
        }, {});

        const prepared = this.document.system;
        const source = this.document.toObject().system;
        const statRows = group => Object.fromEntries(Object.entries(prepared[group]).map(([key, value]) => {
            const raw = source[group]?.[key] ?? {};
            const resource = ['hp', 'sta', 'resolve', 'focus', 'vigor', 'shield'].includes(key);
            const canEditBase = group === 'stats' || isManualDerivedStat(key, prepared.customStat);
            return [key, {
                ...value,
                unmodifiedMax: raw.unmodifiedMax,
                baseCap: raw.baseCap,
                hasBaseCap: Number.isFinite(raw.baseCap),
                currentValue: resource || key === 'luck' ? value.max : value.value,
                canEditBase
            }];
        }));
        const skills = Object.fromEntries(Object.entries(prepared.skills).map(([attribute, group]) => [attribute,
            Object.fromEntries(Object.entries(group).map(([key, skill]) => [key, {
                ...skill,
                value: source.skills[attribute][key].value,
                baseCap: source.skills[attribute][key].baseCap,
                currentValue: skill.modifiedValue ?? skill.value + (skill.activeEffectModifiers ?? 0)
            }]))
        ]));
        context.system = {
            ...prepared, stats: statRows('stats'), derivedStats: statRows('derivedStats'), skills,
            reputation: { ...prepared.reputation, unmodifiedMax: source.reputation?.unmodifiedMax }
        };
        context.canPurchase = this.document.type === 'character';
        context.skillKey = this.skillKey;
        context.type = this.type;

        return context;
    }
}

Object.assign(WitcherModifiersConfiguration.prototype, statMixin);
Object.assign(WitcherModifiersConfiguration.prototype, skillMixin);
