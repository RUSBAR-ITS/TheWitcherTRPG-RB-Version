/** Resolve full Item data for presentation without changing the saved reference. */
export async function linkedItemContext(uuid, fallback = {}) {
    let item;
    if (uuid) {
        try {
            item = await fromUuid(uuid);
        } catch (error) {
            console.warn('TheWitcherTRPG | Linked Item', uuid, error);
        }
    }
    const available = item?.documentName === 'Item' && !!item.system && item.visible !== false;
    const view = {
        ...fallback,
        uuid,
        available,
        missing: !!uuid && !available,
        name: available ? item.name : fallback.name || uuid || '',
        img: available ? item.img : 'icons/svg/item-bag.svg',
        description: ''
    };
    if (available) {
        view.description = await foundry.applications.ux.TextEditor.implementation.enrichHTML(
            item.system.description ?? '',
            { secrets: item.isOwner, relativeTo: item }
        );
    }
    return view;
}
