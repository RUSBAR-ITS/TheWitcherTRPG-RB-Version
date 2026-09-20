import { initialTemporaryHpClock, temporaryHpDuration } from './temporaryHpDuration.js';
import { createEffectDocuments, updateEffectDocuments, isFamilySuppressed } from './effectFamilies.js';
import { initializeEffectStart } from './effectApplication.js';
import { parameterActor, withParameterChanges } from '../actor/parameterPersistence.js';
import { routesParameterChange } from '../actor/parameterPreparation.js';

const DialogV2 = foundry.applications.api.DialogV2;

export default class WitcherActiveEffect extends ActiveEffect {
    static async createDocuments(data = [], operation = {}) {
        return withParameterChanges(parameterActor(operation.parent), () =>
            createEffectDocuments(data, operation, (rows, context) => super.createDocuments(rows, context)));
    }

    static async updateDocuments(changes = [], operation = {}) {
        return withParameterChanges(parameterActor(operation.parent), () =>
            updateEffectDocuments(changes, operation, (rows, context) => super.updateDocuments(rows, context)));
    }

    static async deleteDocuments(ids = [], operation = {}) {
        return withParameterChanges(parameterActor(operation.parent), () => super.deleteDocuments(ids, operation));
    }

    /** Numeric rows are consumed by the system calculator, not a second time by core. */
    shouldApplyChange(change, options) {
        if (!super.shouldApplyChange(change, options)) return false;
        if (options?.witcherNumeric) return true;
        return !(this.type === 'base' && routesParameterChange(this.actor, change));
    }

    get isSuppressed() {
        return this.isSourceSuppressed || isFamilySuppressed(this);
    }

    get isSourceSuppressed() {
        if (
            this.parent?.system?.isActive === false ||
            this.parent?.system?.equipped === false ||
            this.system.applySelf === true ||
            this.system.applyOnTarget === true ||
            this.system.applyOnHit === true ||
            this.system.applyOnDamage === true
        )
            return true;

        return super.isSuppressed;
    }

    // A superseded source keeps aging; suppression must not pause its clock.
    get isTemporary() {
        return !!this.system?.temporaryHpDuration || super.isTemporary;
    }

    _prepareDuration(duration, context) {
        return temporaryHpDuration(this, duration) ?? super._prepareDuration(duration, context);
    }

    get isExpiryTrackable() {
        if (this.system?.temporaryHpDuration) return false;
        return this.persisted && !this.inCompendium && this.isEmbedded &&
            !this.disabled && !this.isSourceSuppressed && !!this.start && this.isTemporary;
    }

    get isDisabled() {
        return this.disabled || !(this.parent?.system?.equipped ?? true);
    }

    /**
     * Is this effect an temporary Item Improvement on an item
     * @type {boolean}
     */
    get isAppliedTemporaryItemImprovement() {
        return this.system.isTransferred;
    }

    get isTemporaryItemImprovement() {
        return this.type === 'temporaryItemImprovement';
    }

    /* -------------------------------------------- */
    /*  Event Handlers                              */
    /* -------------------------------------------- */

    /** @inheritDoc */
    async _preCreate(data, options, user) {
        const actor = parameterActor(this.parent);
        if (this.system.temporaryHpDuration) {
            const clock = initialTemporaryHpClock(this.system.temporaryHpDuration, actor);
            this.updateSource({ 'system.temporaryHpDuration': clock });
            foundry.utils.setProperty(data, 'system.temporaryHpDuration', clock);
        }
        if (actor && data.start == null) {
            const source = this.toObject();
            source.start = null;
            initializeEffectStart(source, actor);
            const clock = { start: source.start, duration: source.duration };
            this.updateSource(clock);
            // Core respects explicit start fields. Queue correction runs only here.
            Object.assign(data, clock);
        }
        const allowed = await super._preCreate(data, options, user);
        if (allowed === false) return false;

        for await (let change of this._source.system.changes) {
            if (change.key.includes('@skill')) {
                await this.chooseSkill(change);
            }
        }
    }

    async chooseSkill(change) {
        let allSkills = Object.keys(CONFIG.WITCHER.skillMap)
            .map(key => {
                let skill = CONFIG.WITCHER.skillMap[key];
                return {
                    label: skill.label,
                    value: 'system.skills.' + skill.attribute.name + '.' + key + '.activeEffectModifiers',
                    group: game.i18n.localize('WITCHER.skills.name')
                };
            })
            .reduce((skills, skill) => {
                skills[skill.label] = skill;
                return skills;
            }, {});

        const dialogTemplate = await foundry.applications.handlebars.renderTemplate(
            'systems/TheWitcherTRPG-RB-Version/templates/dialog/activeEffects/wizard.hbs',
            {
                selects: allSkills
            }
        );

        let skill = await DialogV2.prompt({
            content: dialogTemplate,
            modal: true,
            ok: {
                callback: (event, button, dialog) => {
                    return button.form.elements.path.value;
                }
            },
            rejectClose: true
        });

        change.key = skill;
    }

    /** @inheritDoc */
    async _preUpdate(data, options, user) {
        const allowed = await super._preUpdate(data, options, user);
        if (allowed === false) return false;

        const hasFlag = Object.hasOwn(data.system ?? {}, 'applyAfterCalculations') ||
            Object.hasOwn(data, 'system.applyAfterCalculations');
        const current = this._source?.system?.applyAfterCalculations ?? this.system.applyAfterCalculations;
        const next = hasFlag ? (data.system?.applyAfterCalculations ?? data['system.applyAfterCalculations']) : current;
        const phase = next ? 'final' : 'initial';
        const changes = data.system?.changes ?? data['system.changes'];
        const phaseChanged = hasFlag && next !== current;
        if (!changes && !phaseChanged) return;

        // Explicitly switching the effect's phase moves all rows. Otherwise retain
        // submitted per-row phases and use the effect setting only for missing ones.
        const source = changes ?? this._source?.system?.changes ?? this.system.changes;
        const updated = foundry.utils.deepClone(Object.values(source ?? {})).map(change => ({
            ...change,
            phase: phaseChanged ? phase : (change.phase ?? phase)
        }));
        data.system ??= {};
        data.system.changes = updated;
        delete data['system.changes'];
    }
}
