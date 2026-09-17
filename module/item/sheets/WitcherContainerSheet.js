import WitcherItemSheet from './WitcherItemSheet.js';
import { describeContainer, ownerItems } from '../containerTemplates.js';
import { storeItem, extractItem, runContainerAction } from '../containerOperations.js';

export default class WitcherContainerSheet extends WitcherItemSheet {
    static PARTS = {
        main: {
            template: 'systems/TheWitcherTRPG-RB-Version/templates/sheets/item/container-sheet.hbs',
            scrollable: ['']
        }
    };

    async _prepareContext(options) {
        const context = await super._prepareContext(options);
        const contents = describeContainer(this.item);
        context.data = {
            ...context.data,
            storedWeight: contents.weight,
            itemContent: contents.rows,
            contentIncomplete: contents.incomplete
        };
        context.portableTemplate = contents.portable;
        return context;
    }

    async _onRender(context, options) {
        await super._onRender(context, options);
        this.element
            .querySelectorAll('.remove-item')
            .forEach(element => element.addEventListener('click', this._onRemoveItem.bind(this)));
        this.element.querySelectorAll('.container-item[data-uuid]').forEach(element => {
            element.draggable = this.isEditable && !this.item.pack && element.dataset.missing !== 'true';
            element.addEventListener('dragstart', event => {
                if (!element.draggable) return event.preventDefault();
                const item = [...ownerItems(this.item)].find(doc => doc.uuid === element.dataset.uuid);
                if (!item) return event.preventDefault();
                event.stopPropagation();
                event.dataTransfer.setData(
                    'text/plain',
                    JSON.stringify({
                        ...item.toDragData(),
                        witcherContainer: this.item.uuid
                    })
                );
            });
        });
        this.element.querySelectorAll('.open-contained-item').forEach(element =>
            element.addEventListener('click', event => {
                event.preventDefault();
                const item = [...ownerItems(this.item)].find(doc => doc.uuid === element.dataset.uuid);
                item?.sheet.render(true);
            })
        );
    }

    async _onDropItem(event, item) {
        const payload = event.dataTransfer
            ? foundry.applications.ux.TextEditor.implementation.getDragEventData(event)
            : {};
        return runContainerAction(() => storeItem(this.item, item, { sourceContainer: payload.witcherContainer }));
    }

    async _onRemoveItem(event) {
        event.preventDefault();
        if (!this.isEditable) return null;
        return runContainerAction(() => extractItem(this.item, event.currentTarget.dataset.uuid));
    }
}
