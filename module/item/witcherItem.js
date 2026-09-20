import { assignedSkillIds } from './skillIdentity.js';
import { assignedItemData } from '../activeEffect/effectFamilies.js';
import { parameterActor, withParameterChanges } from '../actor/parameterPersistence.js';
import { WOUND_INTERNAL, createWoundDocuments, validateWoundUpdates, withWoundQueue } from './criticalWoundOperations.js';
import { CONTAINER_INTERNAL, serializeContainer, contentOf } from './containerTemplates.js';
import { createContainerDocuments, deleteContainerDocuments } from './containerOperations.js';
import { extendedRoll } from '../scripts/rolls/extendedRoll.js';
import { RollConfig } from '../scripts/rollConfig.js';
import { WITCHER } from '../setup/config.js';
import { damageUtilMixin } from './mixins/damageUtilMixin.js';
import { consumeMixin } from './mixins/consumeMixin.js';
import { repairMixin } from './mixins/repairMixin.js';
import { dismantlingMixin } from './mixins/dismantlingMixin.js';
import { defenseOptionMixin } from './mixins/defenseOptionMixin.js';

export default class WitcherItem extends Item {
    /** Native entry points also cover directory imports and Actor embedded creation. */
    static async createDocuments(data = [], operation = {}) {
        return withParameterChanges(parameterActor(operation.parent), async () => {
            data = assignedItemData(assignedSkillIds(data), operation.parent);
            const create = (rows, options) => options[CONTAINER_INTERNAL]
                ? super.createDocuments(rows, options)
                : createContainerDocuments(rows, options,
                    (documents, context) => super.createDocuments(documents, context),
                    (ids, context) => super.deleteDocuments(ids, context));
            if (!operation[WOUND_INTERNAL] && operation.parent?.documentName === 'Actor' &&
                data.some(item => item.type === 'criticalWound')) {
                return createWoundDocuments(data, operation, create);
            }
            return create(data, operation);
        });
    }

    static async updateDocuments(changes = [], operation = {}) {
        return withParameterChanges(parameterActor(operation.parent), async () => {
            const actor = operation.parent;
            changes = assignedItemData(changes, actor, { update: true });
            if (!operation[WOUND_INTERNAL] && actor?.documentName === 'Actor' &&
                changes.some(row => row.type === 'criticalWound' || actor.items.get(row._id)?.type === 'criticalWound')) {
                return withWoundQueue(actor, () => {
                    validateWoundUpdates(actor, changes);
                    return super.updateDocuments(changes, operation);
                });
            }
            return super.updateDocuments(changes, operation);
        });
    }

    static async deleteDocuments(ids = [], operation = {}) {
        return withParameterChanges(parameterActor(operation.parent), async () => {
            if (operation[CONTAINER_INTERNAL]) return super.deleteDocuments(ids, operation);
            return deleteContainerDocuments(ids, operation, (targets, options) => super.deleteDocuments(targets, options));
        });
    }

    toCompendium(pack, options = {}) {
        const data = super.toCompendium(pack, options);
        if (this.type === 'container') {
            data.system.templateContent = serializeContainer(this);
            data.system.content = [];
            data.system.isStored = false;
            data.system.storedWeight = 0;
        }
        return data;
    }

    clone(data = {}, context = {}) {
        // The existing directory Duplicate command must also copy the contents, not their UUIDs.
        if (this.type === 'container' && context.save) {
            data = foundry.utils.deepClone(data);
            data.system = {
                ...data.system,
                content: [],
                templateContent: serializeContainer(this),
                isStored: false
            };
        }
        return super.clone(data, context);
    }

    async deleteDialog(options = {}, operation = {}) {
        // The cascade asks once, explicitly including the contents. Preserve core dialog for empty Items.
        if (this.type === 'container' && (contentOf(this).length || this.system.templateContent?.items?.length)) {
            return this.delete(operation);
        }
        return super.deleteDialog(options, operation);
    }

    /** @inheritdoc */
    static migrateData(source) {
        this.migrateSpells(source);

        return super.migrateData(source);
    }

    static migrateSpells(source) {
        if (source.system?.class === 'Hexes') {
            source.type = 'hex';
        }

        if (source.system?.class === 'Rituals') {
            source.type = 'ritual';
        }
    }

    getItemAttack(
        options = {
            alt: false,
            ctrl: false,
            shift: false
        }
    ) {
        if (!this.system.attackOptions) {
            return {
                attackOption: 'none',
                itemUuid: this.uuid
            };
        }

        let mapKeyToNumber;
        if (Object.values(options).every(key => !key) || this.system.attackOptions.size < 2) {
            mapKeyToNumber = 0;
        } else {
            switch (true) {
                case options.ctrl:
                    mapKeyToNumber = 3;
                    break;
                case options.alt:
                    mapKeyToNumber = 2;
                    break;
                case options.shift:
                    mapKeyToNumber = 1;
                    break;
            }

            mapKeyToNumber = Math.min(mapKeyToNumber, this.system.attackOptions.size - 1);
        }

        let attackOption = [...this.system.attackOptions][mapKeyToNumber];

        let attackSkill = this.system[attackOption + 'AttackSkill'];
        return {
            attackOption,
            skill: attackSkill,
            alias: WITCHER.skillMap[attackSkill]?.label,
            itemUuid: this.uuid
        };
    }

    get isConsumable() {
        return this.system.isConsumable ?? false;
    }

    isAlchemicalCraft() {
        return this.system.alchemyDC && this.system.alchemyDC > 0;
    }

    get alchemyCraftComponentsList() {
        class AlchemyComponent {
            name = '';
            alias = '';
            content = '';
            quantity = 0;

            constructor(name, alias, content, quantity) {
                this.name = name;
                this.alias = alias;
                this.content = content;
                this.quantity = quantity;
            }
        }

        let alchemyCraftComponents = [];
        alchemyCraftComponents.push(
            new AlchemyComponent(
                'vitriol',
                game.i18n.localize('WITCHER.Inventory.Vitriol'),
                `<img src="systems/TheWitcherTRPG-RB-Version/assets/images/vitriol.png" class="substance-img" /> <b>${this.system.alchemyComponents.vitriol}</b>`,
                this.system.alchemyComponents.vitriol > 0 ? this.system.alchemyComponents.vitriol : 0
            )
        );
        alchemyCraftComponents.push(
            new AlchemyComponent(
                'rebis',
                game.i18n.localize('WITCHER.Inventory.Rebis'),
                `<img src="systems/TheWitcherTRPG-RB-Version/assets/images/rebis.png" class="substance-img" /> <b>${this.system.alchemyComponents.rebis}</b>`,
                this.system.alchemyComponents.rebis > 0 ? this.system.alchemyComponents.rebis : 0
            )
        );
        alchemyCraftComponents.push(
            new AlchemyComponent(
                'aether',
                game.i18n.localize('WITCHER.Inventory.Aether'),
                `<img src="systems/TheWitcherTRPG-RB-Version/assets/images/aether.png" class="substance-img" /> <b>${this.system.alchemyComponents.aether}</b>`,
                this.system.alchemyComponents.aether > 0 ? this.system.alchemyComponents.aether : 0
            )
        );
        alchemyCraftComponents.push(
            new AlchemyComponent(
                'quebrith',
                game.i18n.localize('WITCHER.Inventory.Quebrith'),
                `<img src="systems/TheWitcherTRPG-RB-Version/assets/images/quebrith.png" class="substance-img" /> <b>${this.system.alchemyComponents.quebrith}</b>`,
                this.system.alchemyComponents.quebrith > 0 ? this.system.alchemyComponents.quebrith : 0
            )
        );
        alchemyCraftComponents.push(
            new AlchemyComponent(
                'hydragenum',
                game.i18n.localize('WITCHER.Inventory.Hydragenum'),
                `<img src="systems/TheWitcherTRPG-RB-Version/assets/images/hydragenum.png" class="substance-img" /> <b>${this.system.alchemyComponents.hydragenum}</b>`,
                this.system.alchemyComponents.hydragenum > 0 ? this.system.alchemyComponents.hydragenum : 0
            )
        );
        alchemyCraftComponents.push(
            new AlchemyComponent(
                'vermilion',
                game.i18n.localize('WITCHER.Inventory.Vermilion'),
                `<img src="systems/TheWitcherTRPG-RB-Version/assets/images/vermilion.png" class="substance-img" /> <b>${this.system.alchemyComponents.vermilion}</b>`,
                this.system.alchemyComponents.vermilion > 0 ? this.system.alchemyComponents.vermilion : 0
            )
        );
        alchemyCraftComponents.push(
            new AlchemyComponent(
                'sol',
                game.i18n.localize('WITCHER.Inventory.Sol'),
                `<img src="systems/TheWitcherTRPG-RB-Version/assets/images/sol.png" class="substance-img" /> <b>${this.system.alchemyComponents.sol}</b>`,
                this.system.alchemyComponents.sol > 0 ? this.system.alchemyComponents.sol : 0
            )
        );
        alchemyCraftComponents.push(
            new AlchemyComponent(
                'caelum',
                game.i18n.localize('WITCHER.Inventory.Caelum'),
                `<img src="systems/TheWitcherTRPG-RB-Version/assets/images/caelum.png" class="substance-img" /> <b>${this.system.alchemyComponents.caelum}</b>`,
                this.system.alchemyComponents.caelum > 0 ? this.system.alchemyComponents.caelum : 0
            )
        );
        alchemyCraftComponents.push(
            new AlchemyComponent(
                'fulgur',
                game.i18n.localize('WITCHER.Inventory.Fulgur'),
                `<img src="systems/TheWitcherTRPG-RB-Version/assets/images/fulgur.png" class="substance-img" /> <b>${this.system.alchemyComponents.fulgur}</b>`,
                this.system.alchemyComponents.fulgur > 0 ? this.system.alchemyComponents.fulgur : 0
            )
        );

        return alchemyCraftComponents;
    }

    async enrichedText() {
        return await this.system.enrichedText?.();
    }

    /**
     * @param {string} rollFormula
     * @param {*} messageData
     * @param {RollConfig} config
     */
    async realCraft(rollFormula, messageData, config) {
        //we want to show message to the chat only after removal of items from inventory
        config.showResult = false;

        //added crit rolls for craft & alchemy
        let roll = await extendedRoll(rollFormula, messageData, config);

        messageData.flavor += `<label><b> ${this.actor.name}</b></label><br/>`;

        let result = roll.total > config.threshold;
        let craftedItemName;
        if (this.system.associatedItem?.name) {
            let craftingComponents = this.isAlchemicalCraft()
                ? this.alchemyCraftComponentsList.filter(c => Number(c.quantity) > 0)
                : this.system.craftingComponents.filter(c => Number(c.quantity) > 0);

            let itemsToDelete = [];

            craftingComponents.forEach(component => {
                let componentsToDelete = this.isAlchemicalCraft()
                    ? this.actor.getSubstance(component.name)
                    : this.actor.findNeededComponent(component.name);

                let componentsCountToDelete = Number(component.quantity);
                let componentsLeftToDelete = componentsCountToDelete;
                let componentsCountDeleted = 0;

                componentsToDelete.forEach(toDelete => {
                    let toDeleteCount = Math.min(
                        Number(toDelete.system.quantity),
                        componentsCountToDelete,
                        componentsLeftToDelete
                    );
                    if (toDeleteCount <= 0) {
                        return ui.notifications.info(
                            `${game.i18n.localize('WITCHER.craft.SkipRemovalOfComponent')}: ${toDelete.name}`
                        );
                    }

                    if (componentsCountDeleted < componentsCountToDelete) {
                        itemsToDelete.push({ id: toDelete.id, name: toDelete.name, count: toDeleteCount });
                        componentsCountDeleted += toDeleteCount;
                        componentsLeftToDelete -= toDeleteCount;
                    }
                });

                if (componentsLeftToDelete != 0) {
                    result = false;
                    return ui.notifications.error(game.i18n.localize('WITCHER.err.craftItemAvailable'));
                }
            });

            craftedItemName = this.system.associatedItem?.name;
            if (result) {
                itemsToDelete.forEach(item => {
                    this.actor.removeItem(item.id, item.count);
                    ui.notifications.info(
                        `${item.count} ${item.name} ${game.i18n.localize('WITCHER.craft.ItemsSuccessfullyDeleted')} ${this.actor.name}`
                    );
                });
                let craftedItem = await fromUuid(this.system.associatedItemUuid);
                this.actor.addItem(craftedItem, this.system.resultQuantity);
            }
        } else {
            craftedItemName = game.i18n.localize('WITCHER.craft.SuccessfulCraftForNothing');
        }

        messageData.flavor += `<b>${craftedItemName}</b>`;
        roll.toMessage(messageData);
    }

    /** Find every matching table, including duplicate names within the same pack. */
    getLootRollTables() {
        return game.packs
            .filter(pack => pack.documentName === 'RollTable')
            .flatMap(pack =>
                pack.index.filter(table => table.name === this.name).map(table => ({ pack, id: table._id }))
            );
    }

    /**
     * Resolve all table results before writing loot. The generator stays until
     * item writes complete; a later chat failure reports generatorRemoved=true.
     * Callers must not automatically retry or use normal loot on failure.
     * @returns {Promise<{status: string, records: object[], reason?: string}>}
     */
    async checkIfItemHasRollTable(newQuantity, tables = this.getLootRollTables()) {
        if (!tables.length) return { status: 'not-found', records: [] };
        const records = [];
        let generatorRemoved = false;
        try {
            if (tables.length !== 1) {
                throw new Error(game.i18n.localize('WITCHER.Monster.lootAmbiguousTable'));
            }
            if (!Number.isInteger(newQuantity) || newQuantity < 0) {
                throw new Error(game.i18n.localize('WITCHER.Monster.lootInvalidQuantity'));
            }
            const table = await tables[0].pack.getDocument(tables[0].id);
            const resolved = [];
            for (let i = 0; i < newQuantity; i++) {
                const { results } = await table.roll();
                if (!results.length) throw new Error(game.i18n.localize('WITCHER.Monster.lootEmptyTable'));
                for (const result of results) {
                    const item =
                        result.type === 'document' && result.documentUuid
                            ? await foundry.utils.fromUuid(result.documentUuid)
                            : null;
                    if (item?.documentName !== 'Item') {
                        throw new Error(game.i18n.localize('WITCHER.Monster.lootInvalidResult'));
                    }
                    // Prepare display data before any writes, too.
                    resolved.push({ item, html: await result.getHTML() });
                }
            }

            for (const { item } of resolved) {
                // Never use the generator itself as the destination stack.
                const existing = this.actor.items.find(
                    other => other.id !== this.id && other.name === item.name && other.type === item.type
                );
                let saved;
                if (existing) {
                    saved = await existing.update({ 'system.quantity': Number(existing.system.quantity) + 1 });
                } else {
                    const data = item.toObject();
                    if (item.system.schema.fields.lootQuantityFormula) data.system.lootQuantityFormula = '';
                    saved = await Item.create(data, { parent: this.actor });
                }
                if (!saved) throw new Error(game.i18n.localize('WITCHER.Monster.lootWriteCancelled'));
                records.push({ uuid: saved.uuid, name: saved.name, action: existing ? 'updated' : 'created' });
            }

            const deleted = await this.delete();
            if (!deleted) throw new Error(game.i18n.localize('WITCHER.Monster.lootWriteCancelled'));
            generatorRemoved = true;
            // Confirmation follows all item writes and generator removal.
            for (const { item, html } of resolved) {
                const successMessage = game.i18n.format('WITCHER.Monster.lootGeneratedItem', { item: item.name });
                await ChatMessage.create({
                    user: game.user.id,
                    content: `${foundry.utils.escapeHTML(successMessage)} ${html}`,
                    whisper: game.users.filter(user => user.isGM).map(user => user.id)
                });
                ui.notifications.info(successMessage);
            }
            return { status: 'generated', records, generatorRemoved };
        } catch (error) {
            console.error('TheWitcherTRPG | Loot generation', this.uuid, error);
            const reason = error.message ?? String(error);
            ui.notifications.error(
                game.i18n.format('WITCHER.Monster.lootGenerationFailed', {
                    item: this.name,
                    count: records.length,
                    reason,
                    generator: game.i18n.localize(
                        generatorRemoved
                            ? 'WITCHER.Monster.lootGeneratorRemoved'
                            : 'WITCHER.Monster.lootGeneratorRetained'
                    )
                })
            );
            return {
                status: records.length || generatorRemoved ? 'partial' : 'failed',
                records,
                reason,
                generatorRemoved
            };
        }
    }

    /* -------------------------------------------- */
    /*  Active Effects                              */
    /* -------------------------------------------- */

    prepareEmbeddedDocuments() {
        super.prepareEmbeddedDocuments();
        this.applyActiveEffects();
    }

    /**
     * Get all ActiveEffects that may apply to this Item.
     * @yields {ActiveEffect}
     * @returns {Generator<ActiveEffect, void, void>}
     */
    *allApplicableEffects() {
        for (const effect of this.effects) {
            if (effect.isAppliedTemporaryItemImprovement) yield effect;
        }
    }

    /* -------------------------------------------- */

    /**
     * Apply any transformation to the Item data which are caused by Effects.
     */
    applyActiveEffects() {
        const overrides = {};

        // Organize non-disabled effects by their application priority
        const changes = [];
        for (const effect of this.allApplicableEffects()) {
            if (!effect.active) continue;
            changes.push(
                ...effect.system.changes.map(change => {
                    const c = foundry.utils.deepClone(change);
                    c.effect = effect;
                    c.priority ??= c.mode * 10;
                    return c;
                })
            );
        }
        changes.sort((a, b) => a.priority - b.priority);

        // Apply all changes
        for (const change of changes) {
            if (!change.key) continue;
            const changes = change.effect.apply(this, change);
            Object.assign(overrides, changes);
        }

        // Expand the set of final overrides
        this.overrides = foundry.utils.expandObject(overrides);
    }
}

Object.assign(WitcherItem.prototype, consumeMixin);
Object.assign(WitcherItem.prototype, repairMixin);
Object.assign(WitcherItem.prototype, dismantlingMixin);
Object.assign(WitcherItem.prototype, damageUtilMixin);
Object.assign(WitcherItem.prototype, defenseOptionMixin);
