/**
 * Foundry VTT 14.367: client/documents/roll-table.mjs, RollTable#roll.
 * Intentional behavioral delta: maximum recursion depth 10 instead of 5.
 * Core-local imports/localization use their public client equivalents here.
 * Compare this copy with core when upgrading Foundry (DEC-0003).
 */
export default class WitcherRollTable extends foundry.documents.RollTable {
  async roll({roll, recursive=true, normalize=true, _depth=0}={}) {
    if ( _depth > 10 ) {
      throw new Error(`Maximum recursion depth exceeded when attempting to draw from RollTable ${this.id}`);
    }

    // Normalize the result distribution, rolling a clone of this table if necessary
    if ( !this._source.formula && normalize ) {
      const save = this.canUserModify(game.user, "update") && !this.compendium?.locked;
      const table = await this.normalize({save});
      if ( !save ) return table.roll({_depth, roll, recursive, normalize: false});
    }

    roll ??= foundry.dice.Roll.defaultImplementation.create(this.formula);
    let results = [];

    // Ensure that at least one non-drawn result remains
    const available = this.results.filter(r => !r.drawn);
    if ( !available.length ) {
      ui.notifications.warn(game.i18n.localize("TABLE.NoAvailableResults"));
      return {roll, results};
    }

    // Ensure that results are available within the minimum/maximum range
    const minRoll = (await roll.reroll({minimize: true})).total;
    const maxRoll = (await roll.reroll({maximize: true})).total;
    const availableRange = available.reduce((range, result) => {
      const r = result.range;
      if ( !range[0] || (r[0] < range[0]) ) range[0] = r[0];
      if ( !range[1] || (r[1] > range[1]) ) range[1] = r[1];
      return range;
    }, [null, null]);
    if ( (availableRange[0] > maxRoll) || (availableRange[1] < minRoll) ) {
      ui.notifications.warn(game.i18n.localize("TABLE.NoPossibleResults"));
      return {roll, results};
    }

    // Continue rolling until one or more results are recovered
    let iter = 0;
    while ( !results.length ) {
      if ( iter >= 10000 ) {
        ui.notifications.error("TABLE.DrawMaximumIterations", {format: {name: this.name}});
        break;
      }
      roll = await roll.reroll();
      results = this.getResultsForRoll(roll.total);
      iter++;
    }

    // Draw results recursively from any inner Roll Tables
    if ( recursive ) {
      const inner = [];
      for ( const result of results ) {
        const {type, documentUuid} = result;
        const documentName = foundry.utils.parseUuid(documentUuid)?.type;
        if ( (type === "document") && (documentName === "RollTable") ) {
          const innerTable = await foundry.utils.fromUuid(documentUuid);
          if ( innerTable ) {
            const innerRoll = await innerTable.roll({_depth: _depth + 1});
            inner.push(...innerRoll.results);
          }
        }
        else inner.push(result);
      }
      results = inner;
    }

    // Return the Roll and the results
    return {roll, results};
  }
}
