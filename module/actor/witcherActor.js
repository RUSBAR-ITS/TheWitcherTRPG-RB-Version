import { PARAMETER_INTERNAL, inParameterOperation, prepareParameterUpdate } from './parameterPersistence.js';
import { calculateDerivedParameter, derivedStatInput } from './derivedPreparation.js';
import { calculateActorParameter, prepareParameterInputs, prepareSkillParameters, resetParameterPreparation } from './parameterPreparation.js';
import { installWound } from '../item/criticalWoundOperations.js';
import { getRandomInt } from '../scripts/helper.js';
import { WITCHER } from '../setup/config.js';
import { modifierMixin } from './mixins/modifierMixin.js';
import { damageUtilMixin } from './mixins/damageUtilMixin.js';
import { castSpellMixin } from './mixins/castSpellMixin.js';
import { locationMixin } from './mixins/locationMixin.js';
import { weaponAttackMixin } from './mixins/weaponAttackMixin.js';
import { verbalCombatMixin } from './mixins/verbalCombatMixin.js';
import { defenseMixin } from './mixins/defenseMixin.js';
import { damageMixin } from './mixins/damageMixin.js';
import { temporaryEffectMixin } from './mixins/temporaryEffectMixin.js';
import { professionMixin } from './mixins/professionMixin.js';
import { armorMixin } from './mixins/armorMixin.js';
import { healMixin } from './mixins/healMixin.js';
import { rewardsMixin } from './mixins/rewardsMixin.js';
import { craftingMixin } from './mixins/craftingMixin.js';
import { currencyConverterMixin } from './mixins/currencyConverterMixin.js';
import { adrenalineMixin } from './mixins/adrenalineMixin.js';
import { skillMixin } from './mixins/skillMixin.js';

export default class WitcherActor extends Actor {
    _initialize(options = {}) {
        this._parameterPreview = options.parameterPreview === true;
        super._initialize(options);
    }

    static async updateDocuments(updates = [], operation = {}) {
        if (operation[PARAMETER_INTERNAL] || operation.pack) return super.updateDocuments(updates, operation);
        const changes = updates.map(patch => {
            const actor = operation.parent?.actor ?? game.actors?.get(patch._id);
            return actor && !inParameterOperation(actor) ? prepareParameterUpdate(actor, patch) : patch;
        });
        return super.updateDocuments(changes, operation);
    }

    /**
     * An array of ActiveEffect instances which are present on the Actor or Items which have a limited duration.
     * @type {ActiveEffect[]}
     */
    get temporaryEffects() {
        let temporaryEffects = super.temporaryEffects;

        let temporaryItemImprovements = this.items
            .map(item => item.effects.filter(effect => effect.isAppliedTemporaryItemImprovement))
            .flat();
        return temporaryEffects.concat(temporaryItemImprovements);
    }

    prepareBaseData() {
        super.prepareBaseData();
        resetParameterPreparation(this);
    }

    prepareDerivedData() {
        super.prepareDerivedData();

        if (this.type === 'loot') return;
        if (this.type === 'mystery') return;

        let armorEffects = this.getList('armor')
            .filter(armor => armor.system.equipped)
            .map(armor => armor.system.effects)
            .flat()
            .filter(effect => effect.statusEffect)
            .map(effect => WITCHER.armorEffects.find(armorEffect => armorEffect.id == effect.statusEffect));
        if (!this._parameterPreview) this.applyStatus(armorEffects);

        prepareParameterInputs(this);
        this.calculateStats();
        prepareSkillParameters(this);
        this.calculateFixedDerivedStats();
        this.calculateDerivedStats();
        this.calculateAttackStats();
    }

    calculateStats() {
        // Prepare all uninjured maxima first: BODY/WILL also provide the existing
        // encumbrance/wound-threshold inputs. Do not run native phases twice.
        for (const [key, stat] of Object.entries(this.system.stats)) {
            stat.max = calculateActorParameter(this, `system.stats.${key}`).value;
        }
        const threshold = calculateDerivedParameter(this, 'woundTreshold', { store: false }).value;
        const { deathState, woundThreshold } = this.system.healthState;
        deathState.applied = !deathState.ignored && this.system.derivedStats.hp.value <= 0;
        woundThreshold.applied = !deathState.applied && !woundThreshold.ignored &&
            this.system.derivedStats.hp.value < threshold;
        const encumbrance = this.calculateWeigthEncumbrance();
        const armor = this.getArmorEcumbrance();
        for (const key of ['int', 'ref', 'dex', 'body', 'spd', 'emp', 'cra', 'will']) {
            this.calculateStat(key, { encumbrance, armor });
        }
        this.system.reputation.value = this.system.reputation.max;
    }

    calculateStat(stat, { encumbrance = this.calculateWeigthEncumbrance(), armor = this.getArmorEcumbrance() } = {}) {
        const changes = [];
        if (['ref', 'dex', 'spd'].includes(stat)) {
            changes.push({ type: 'add', value: -encumbrance, affectsParameter: true });
        }
        if (['ref', 'dex'].includes(stat)) {
            changes.push({ type: 'add', value: -armor, affectsParameter: true });
        }
        const { deathState, woundThreshold } = this.system.healthState;
        const divider = deathState.applied ? 3
            : woundThreshold.applied && ['ref', 'dex', 'int', 'will'].includes(stat) ? 2 : 1;
        if (divider !== 1) changes.push({ type: 'multiply', value: 1 / divider, affectsParameter: true });
        this.system.stats[stat].value = calculateActorParameter(this, `system.stats.${stat}`, changes).value;
    }

    calculateWeigthEncumbrance() {
        let currentEncumbrance =
            calculateDerivedParameter(this, 'enc', { uninjured: true, store: false }).value;
        var totalWeights = this.getTotalWeight();

        let encDiff = 0;
        if (currentEncumbrance < totalWeights) {
            encDiff = Math.ceil((totalWeights - currentEncumbrance) / 5);
        }

        return encDiff;
    }

    calculateFixedDerivedStats() {
        for (const key of ['stun', 'run', 'leap', 'enc', 'rec', 'woundTreshold']) {
            const stat = this.system.derivedStats[key];
            const result = calculateDerivedParameter(this, key);
            stat.unmodifiedMax = Math.floor(result.base);
            stat.value = result.value;
            stat.max = ['stun', 'leap', 'rec', 'woundTreshold'].includes(key)
                ? calculateDerivedParameter(this, key, { uninjured: true, store: false }).value : result.value;
        }
    }

    calculateDerivedStats() {
        for (const key of ['hp', 'sta', 'resolve', 'focus', 'vigor', 'shield']) this.calculateDerivedStat(key);
    }

    calculateDerivedStat(stat) {
        const result = calculateDerivedParameter(this, stat);
        this.system.derivedStats[stat].unmodifiedMax = Math.floor(result.base);
        this.system.derivedStats[stat].max = result.value;
    }

    calculateAttackStats() {
        const body = derivedStatInput(this, 'body', ['bodyDamage']);
        const meleeBonus = Math.ceil((body - 6) / 2) * 2;
        this.system.attackStats.meleeBonus += meleeBonus;
        this.system.attackStats.punch.value = `1d6+${meleeBonus}`;
        this.system.attackStats.kick.value = `1d6+${4 + meleeBonus}`;
    }

    async applyStatus(effects) {
        effects
            ?.filter(effect => !!effect.statusEffect)
            .forEach(effect => {
                if (!this.statuses.find(status => status == effect.statusEffect)) {
                    this.toggleStatusEffect(effect.statusEffect);
                }

                if (this.system.statusEffectImmunities?.find(immunity => immunity == statusEffectId)) {
                    //untoggle it so people see it was tried to be applied but failed
                    setTimeout(() => {
                        this.toggleStatusEffect(statusEffectId);
                    }, 1000);
                }
            });
    }

    async removeStatus(effects) {
        effects
            .filter(effect => !!effect.statusEffect)
            .forEach(effect => {
                if (this.statuses.find(status => status == effect.statusEffect)) {
                    this.toggleStatusEffect(effect.statusEffect);
                }
            });
    }

    async useItem(itemId, options) {
        let item = this.items.get(itemId);

        if (!item) return;

        if (item.type === 'weapon') {
            return this.weaponAttack(item, options);
        }

        if (item.type === 'spell' || item.type === 'hex' || item.type === 'ritual') {
            return this.castSpell(item);
        }

        if (item.isConsumable) {
            item.consume();
            this.removeItem(item.id, 1);
            return;
        }
    }

    getTotalWeight() {
        let total = this.items.reduce((total, item) => (total += item.system.calcWeight?.() ?? 0), 0);
        return Math.ceil(total + this.system.calcCurrencyWeight());
    }

    getList(name) {
        if (name === 'shield') {
            return this.items
                .filter(item => item.type == 'armor' && item.system.location == 'Shield')
                .sort((a, b) => a.sort - b.sort);
        }
        return this.items.filter(i => i.type == name && !i.system.isStored).sort((a, b) => a.sort - b.sort);
    }

    async addItem(addItem, numberOfItem = 1, forcecreate = false) {
        if (addItem.type === 'criticalWound') return installWound(this, addItem);
        let foundItem = this.items.find(item => item.name == addItem.name && item.type == addItem.type);
        if (foundItem && !forcecreate && !foundItem.system.isStored) {
            await foundItem.update({ 'system.quantity': Number(foundItem.system.quantity) + Number(numberOfItem) });
        } else {
            //if toObject cannot be called, we dont have a source => we dont need to call toObject
            let newItem = addItem.toObject ? addItem.toObject() : addItem;

            if (numberOfItem) {
                newItem.system.quantity = Number(numberOfItem);
            }

            await this.createEmbeddedDocuments('Item', [newItem]);
        }
    }

    async removeItem(itemId, quantityToRemove) {
        let foundItem = this.items.get(itemId);
        let newQuantity = foundItem.system.quantity - quantityToRemove;
        if (newQuantity <= 0) {
            await this.items.get(itemId).delete();
        } else {
            await foundItem.update({ 'system.quantity': newQuantity });
        }
    }

    async removeItemsOfType(type) {
        this.deleteEmbeddedDocuments(
            'Item',
            this.items.filter(item => item.type === type).map(item => item.id)
        );
    }

    static getAllLocations() {
        let locations = ['head', 'torso', 'rightArm', 'leftArm', 'rightLeg', 'leftLeg'];

        if (this.type == 'monster' && this.system.hasTailWing) {
            locations.push('tailWing');
        }

        return locations;
    }

    static getLocationObject(location) {
        let alias = '';
        let modifier = `+0`;
        let formula;
        switch (location) {
            case 'randomHuman':
                let randomHumanLocation = getRandomInt(10);
                switch (randomHumanLocation) {
                    case 1:
                        location = 'head';
                        formula = 3;
                        break;
                    case 2:
                    case 3:
                    case 4:
                        location = 'torso';
                        formula = 1;
                        break;
                    case 5:
                        location = 'rightArm';
                        formula = 0.5;
                        break;
                    case 6:
                        location = 'leftArm';
                        formula = 0.5;
                        break;
                    case 7:
                    case 8:
                        location = 'rightLeg';
                        formula = 0.5;
                        break;
                    case 9:
                    case 10:
                        location = 'leftLeg';
                        formula = 0.5;
                        break;
                    default:
                        location = 'torso';
                        formula = 1;
                        break;
                }
                alias = `${game.i18n.localize('WITCHER.Location.Random')}`;
                break;
            case 'randomMonster':
                let randomMonsterLocation = getRandomInt(10);
                switch (randomMonsterLocation) {
                    case 1:
                        location = 'head';
                        formula = 3;
                        break;
                    case 2:
                    case 3:
                    case 4:
                    case 5:
                        location = 'torso';
                        formula = 1;
                        break;
                    case 6:
                    case 7:
                        location = 'rightLeg';
                        formula = 0.5;
                        break;
                    case 8:
                    case 9:
                        location = 'leftLeg';
                        formula = 0.5;
                        break;
                    case 10:
                        location = 'tailWing';
                        formula = 0.5;
                        break;
                    default:
                        location = 'torso';
                        formula = 1;
                        break;
                }
                alias = `${game.i18n.localize('WITCHER.Location.Random')}`;
                break;
            case 'head':
                alias = `${game.i18n.localize('WITCHER.Armor.LocationHead')}`;
                formula = 3;
                modifier = `-6`;
                break;
            case 'torso':
                alias = `${game.i18n.localize('WITCHER.Armor.LocationTorso')}`;
                formula = 1;
                modifier = `-1`;
                break;
            case 'rightArm':
                alias = `${game.i18n.localize('WITCHER.Armor.LocationRight')} ${game.i18n.localize(
                    'WITCHER.Armor.LocationArm'
                )}`;
                formula = 0.5;
                modifier = `-3`;
                break;
            case 'leftArm':
                alias = `${game.i18n.localize('WITCHER.Armor.LocationLeft')} ${game.i18n.localize(
                    'WITCHER.Armor.LocationArm'
                )}`;
                formula = 0.5;
                modifier = `-3`;
                break;
            case 'rightLeg':
                alias = `${game.i18n.localize('WITCHER.Armor.LocationRight')} ${game.i18n.localize(
                    'WITCHER.Armor.LocationLeg'
                )}`;
                formula = 0.5;
                modifier = `-2`;
                break;
            case 'leftLeg':
                alias = `${game.i18n.localize('WITCHER.Armor.LocationLeft')} ${game.i18n.localize(
                    'WITCHER.Armor.LocationLeg'
                )}`;
                formula = 0.5;
                modifier = `-2`;
                break;
            case 'tailWing':
                alias = `${game.i18n.localize('WITCHER.Dialog.attackTail')}`;
                formula = 0.5;
                break;
            default:
                alias = `${game.i18n.localize('WITCHER.Armor.LocationTorso')}`;
                formula = 1;
                modifier = `-1`;
                break;
        }

        return {
            name: location,
            alias: alias,
            formula: formula,
            modifier: modifier
        };
    }
}

Object.assign(WitcherActor.prototype, professionMixin);
Object.assign(WitcherActor.prototype, modifierMixin);
Object.assign(WitcherActor.prototype, damageMixin);
Object.assign(WitcherActor.prototype, damageUtilMixin);
Object.assign(WitcherActor.prototype, weaponAttackMixin);
Object.assign(WitcherActor.prototype, defenseMixin);
Object.assign(WitcherActor.prototype, healMixin);
Object.assign(WitcherActor.prototype, castSpellMixin);
Object.assign(WitcherActor.prototype, verbalCombatMixin);
Object.assign(WitcherActor.prototype, locationMixin);
Object.assign(WitcherActor.prototype, temporaryEffectMixin);
Object.assign(WitcherActor.prototype, armorMixin);
Object.assign(WitcherActor.prototype, rewardsMixin);
Object.assign(WitcherActor.prototype, craftingMixin);
Object.assign(WitcherActor.prototype, currencyConverterMixin);
Object.assign(WitcherActor.prototype, adrenalineMixin);
Object.assign(WitcherActor.prototype, skillMixin);
