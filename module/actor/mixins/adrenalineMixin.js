export let adrenalineMixin = {
    async addAdrenaline() {
        if (game.settings.get('TheWitcherTRPG-RB-Version', 'useOptionalAdrenaline')) {
            const updated = await this.update({ 'system.adrenaline.value': this.system.adrenaline.value + 1 });
            if (!updated) throw new Error('Adrenaline update was not confirmed');
            return updated;
        }
    }
};
