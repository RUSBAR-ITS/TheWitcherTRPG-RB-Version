export let currencyConverterMixin = {
    onOpenCurrencyConverter(event) {
        return this.actor.handleCurrencyConverter(event);
    }
};
