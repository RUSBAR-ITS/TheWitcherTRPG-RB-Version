import { prepareCheck } from '../../scripts/rolls/prepareCheck.js';
import { extendedRoll } from '../../scripts/rolls/extendedRoll.js';
import { RollConfig } from '../../scripts/rollConfig.js';
import { costEditMixin } from '../mixins/costEditMixin.js';

const DialogV2 = foundry.applications.api.DialogV2;

const repairModifier = -5;
const perEnchantModifier = 2;

class Repair {
    async process(actor, item) {
        const data = await this.prepareData(actor, item);
        if (data) {
            await this.renderDialog(data);
        }
    }

    async prepareData(actor, item, artisan = null) {
        const diagramId = item.system?.associatedDiagramUuid;
        let diagram = diagramId ? await fromUuid(diagramId) : null;
        if (!diagram) {
            ui.notifications.error(game.i18n.localize(`WITCHER.Repair.alerts.noDiagram`));
            return;
        }

        let ownedComponents = [];
        let missingComponents = [];
        let unknownComponents = [];
        const executor = artisan ?? actor;

        for (const craftingComponent of diagram.system.craftingComponents) {
            const uuid = craftingComponent.uuid;

            let component = executor.findNeededComponent(craftingComponent.name)[0];

            //component is in inventory, might have 0 quantity => checked later
            if (component) {
                ownedComponents.push(component);
            }
            //component is not in inventory
            else {
                //linked in diagram, so we can query data
                if (uuid) {
                    let component;
                    try {
                        component = await fromUuid(uuid);
                    } catch (error) {
                        console.error('TheWitcherTRPG | Repair component', uuid, error);
                    }
                    if (
                        component?.documentName !== 'Item' ||
                        !component.system ||
                        !Number.isFinite(component.system.cost) ||
                        component.visible === false
                    ) {
                        ui.notifications.error(
                            game.i18n.format('WITCHER.Repair.alerts.unavailableComponent', {
                                name: craftingComponent.name || uuid,
                                uuid
                            })
                        );
                        return;
                    }
                    missingComponents.push(component);
                } else {
                    //not linked, so user input is required later
                    unknownComponents.push(craftingComponent);
                }
            }
        }

        return new RepairData(actor, item, diagram, ownedComponents, missingComponents, unknownComponents, artisan);
    }

    async processRequest(owner, item, artisan) {
        const data = await this.prepareData(owner, item, artisan);
        if (data) {
            data.artisan = artisan;
            await this.renderDialog(data);
        }
    }

    async renderDialog(data) {
        const template = await this.prepareDialogTemplate(data);
        const buttons = [
            {
                action: 'repair',
                label: game.i18n.localize(`WITCHER.Repair.buttons.repair`),
                icon: `fas fa-hammer`,
                callback: _ =>
                    this.repairItem(data, {
                        simulate: false,
                        gmRepair: false
                    })
            },
            {
                action: 'sim-repair',
                label: game.i18n.localize(`WITCHER.Repair.buttons.simulate`),
                icon: `fas fa-scale-balanced`,
                callback: _ =>
                    this.repairItem(data, {
                        simulate: true,
                        gmRepair: false
                    })
            }
        ];
        if (!data.artisan) {
            buttons.push({
                action: 'request-repair',
                label: game.i18n.localize(`WITCHER.Repair.buttons.request`),
                icon: `fas fa-coins`,
                callback: _ => this.sendRepairInfoToChat(data, true)
            });
        } else if (game.user.isGM) {
            buttons.push({
                action: 'gm-repair',
                label: game.i18n.localize(`WITCHER.Repair.buttons.gmRepair`),
                icon: `fas fa-crown`,
                callback: _ =>
                    this.repairItem(data, {
                        simulate: true,
                        gmRepair: true
                    })
            });
        }

        await DialogV2.wait({
            modal: true,
            window: { title: `${game.i18n.localize('WITCHER.Repair.action')} ${data.item.name}` },
            content: template,
            buttons: buttons,
            render: _ => this.attachHtmlListeners((cost, data) => (data.additionalCost = cost), data)
        });
    }

    async prepareDialogTemplate(data) {
        let templateData = {
            components: [],
            data: data,
            isRequest: data.artisan !== null,
            canEditCost: game.user.isGM
        };

        data.unknownComponents.forEach(oc => {
            templateData.components.push({
                img: 'icons/svg/item-bag.svg',
                name: oc.name,
                quantity: 0,
                missingQuantity: 1,
                required: 1,
                cost: 0
            });
        });

        data.missingComponents.forEach(oc => {
            templateData.components.push({
                img: oc.img,
                name: oc.name,
                quantity: 0,
                missingQuantity: 1,
                required: 1,
                cost: oc.system?.cost ?? 0
            });
        });

        data.ownedComponents.forEach(oc => {
            const missingQuanitity = oc.system.quantity < 1 ? 1 : 0;

            templateData.components.push({
                img: oc.img,
                name: oc.name,
                quantity: oc.system.quantity,
                missingQuantity: missingQuanitity,
                required: 1,
                cost: oc.system.cost
            });
        });

        return await foundry.applications.handlebars.renderTemplate(
            'systems/TheWitcherTRPG-RB-Version/templates/dialog/repair-dialog.hbs',
            templateData
        );
    }

    async repairItem(data, options) {
        if ((!options.simulate || options.gmRepair) && !this._canRepair(data, !options.gmRepair)) return null;

        if (options.gmRepair) {
            return this.gmRepair(data);
        } else {
            return this.commonRepair(data, options.simulate);
        }
    }

    async commonRepair(data, simulate) {
        const rollFormula = await this.prepareRollFormula(data);
        if (rollFormula === null) return null;

        let config = this.prepareRollConfig(data);
        let messageData = await this.initMessageData(data);

        let roll = await extendedRoll(rollFormula, messageData, config);
        const success = roll.total > config.threshold;

        if (!simulate) {
            if (!await this._doRepair(data, success)) return null;
        }

        await roll.toMessage(messageData);
    }

    async gmRepair(data) {
        const content = await this.renderChatTemplate(data, false);
        if (!await this._restoreItem(data.item)) return null;
        await this.sendRepairInfoToChat(data, false, content);
    }

    async prepareRollFormula(data) {
        const check = await prepareCheck(data.executor, { target: { kind: 'builtin', key: 'crafting' },
            action: 'repair' });
        return check?.formula ?? null;
    }

    prepareRollConfig(data, reliabilityToRestore) {
        let config = new RollConfig();

        config.showCrit = true;
        config.showSuccess = true;
        config.showResult = false;
        config.threshold = data.repairDC;
        config.thresholdDesc = data.skillName;
        config.messageOnSuccess = game.i18n.localize('WITCHER.Repair.result.success');
        config.messageOnFailure = game.i18n.localize('WITCHER.Repair.result.failure');

        return config;
    }

    async initMessageData(data) {
        const template = await this.renderChatTemplate(data, false);

        return {
            speaker: ChatMessage.getSpeaker({ actor: data.executor }),
            flavor: template,
            system: {}
        };
    }

    async renderChatTemplate(data, isRequest) {
        return await foundry.applications.handlebars.renderTemplate(
            'systems/TheWitcherTRPG-RB-Version/templates/chat/item/repair.hbs',
            {
                data: data,
                isRequest: isRequest,
                isOrder: data.artisan !== null,
                showComponents: data.ownedComponents.length || data.missingComponents.length
            }
        );
    }

    _canRepair(data, consumeComponents) {
        if (!data.item.system.canBeRepaired || !data.damagedLocations.length) {
            ui.notifications.warn(game.i18n.localize('WITCHER.Repair.alerts.itemIsAlreadyRepaired'));
            return false;
        }
        if (consumeComponents) {
            const quantities = new Map();
            for (const component of data.ownedComponents) {
                quantities.set(component.id, (quantities.get(component.id) ?? 0) + 1);
            }
            const insufficient = [...quantities].some(([id, required]) => {
                const quantity = data.executor.items.get(id)?.system.quantity;
                return !Number.isFinite(quantity) || quantity < required;
            });
            if (data.missingComponents.length || data.unknownComponents.length || insufficient) {
                ui.notifications.error(game.i18n.localize('WITCHER.Repair.alerts.notEnoughComponents'));
                return false;
            }
        }
        if (!data.item.canUserModify(game.user, 'update') && !game.users.activeGM) {
            ui.notifications.error(game.i18n.localize('WITCHER.Repair.alerts.noActiveGM'));
            return false;
        }
        return true;
    }

    async _doRepair(data, success) {
        if (!this._canRepair(data, true)) return false;
        for (const component of data.ownedComponents) {
            await data.executor.removeItem(component.id, 1);
        }
        return success ? this._restoreItem(data.item) : true;
    }

    async _restoreItem(item) {
        if (item.canUserModify(game.user, 'update')) {
            await this.restoreReliability(item);
            return true;
        }
        const gm = game.users.activeGM;
        if (!gm) {
            ui.notifications.error(game.i18n.localize('WITCHER.Repair.alerts.noActiveGM'));
            return false;
        }
        try {
            const result = await gm.query('TheWitcherTRPG-RB-Version.query', {
                function: 'restoreReliability', uuid: item.uuid, data: []
            });
            if (result === true) return true;
        } catch (error) {
            console.error('TheWitcherTRPG | Repair result could not be confirmed', item.uuid, error);
        }
        ui.notifications.warn(game.i18n.localize('WITCHER.Repair.alerts.unconfirmedRepair'));
        return false;
    }

    async sendRepairInfoToChat(data, isRequest, content = null) {
        content ??= await this.renderChatTemplate(data, isRequest);

        const chatData = {
            content: content,
            speaker: ChatMessage.getSpeaker({ actor: data.executor }),
            style: CONST.CHAT_MESSAGE_STYLES.OTHER
        };

        await ChatMessage.create(chatData);
    }

    restoreReliability(item) {
        return item.system.repair();
    }
}

class RepairData {
    constructor(actor, item, diagram, ownedComponents, missingComponents, unknownComponents, artisan = null) {
        this.actor = actor;
        this.item = item;
        this.diagram = diagram;
        this.ownedComponents = ownedComponents;
        this.missingComponents = missingComponents;
        this.unknownComponents = unknownComponents;
        this.artisan = artisan;
        this.additionalCost = 0;
    }

    get damagedLocations() {
        return this.item.system.damagedLocations ?? [];
    }

    get enchantsCount() {
        return this.item.system?.enhancementItemIds.filter(e => e).length;
    }

    get executor() {
        return this.artisan ?? this.actor;
    }

    get repairDC() {
        return this.diagram.system.craftingDC + repairModifier + this.enchantsDC;
    }

    get repairDCFormula() {
        let formula = `${this.diagram.system.craftingDC}[${game.i18n.localize('WITCHER.Repair.params.craftingDC')}] - ${Math.abs(repairModifier)}[${game.i18n.localize('WITCHER.Repair.params.repairMod')}]`;
        const enchantsCount = this.enchantsCount;
        if (enchantsCount) {
            formula += ` + ${enchantsCount} * ${perEnchantModifier}[${game.i18n.localize('WITCHER.Repair.params.enchants')}]`;
        }

        return formula;
    }

    get enchantsDC() {
        return this.enchantsCount * perEnchantModifier;
    }

    get skillName() {
        return game.i18n.localize(CONFIG.WITCHER.skillMap.crafting.rollLabel);
    }

    get repairPrice() {
        const ownedPrice = this.ownedComponents.reduce((sum, comp) => sum + comp.system.cost, this.additionalCost);

        return this.missingComponents.reduce((sum, comp) => sum + comp.system?.cost, ownedPrice);
    }
}

Object.assign(Repair.prototype, costEditMixin);

let RepairSystem = Object.freeze(new Repair());

export default RepairSystem;
