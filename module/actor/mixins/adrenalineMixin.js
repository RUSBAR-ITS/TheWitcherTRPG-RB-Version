export let adrenalineMixin = {
    async addAdrenaline() {
        if (game.settings.get('TheWitcherTRPG-RB-Version', 'useOptionalAdrenaline')) {
            this.update({ 'system.adrenaline.value': this.system.adrenaline.value + 1 });
        }
    }
};
