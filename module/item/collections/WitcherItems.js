import { serializeContainer } from '../containerTemplates.js';

/** Container imports into Items are templates with independent child documents. */
export default class WitcherItems extends foundry.documents.collections.Items {
    _prepareImportDocument(document, options) {
        if (document.type === 'container') options.keepId = false;
        return super._prepareImportDocument(document, options);
    }

    fromCompendium(document, options = {}) {
        if (document.type !== 'container') return super.fromCompendium(document, options);
        const data = super.fromCompendium(document, { ...options, keepId: false });
        if (document.toObject) data.system.templateContent = serializeContainer(document);
        data.system.content = [];
        data.system.isStored = false;
        return data;
    }
}
