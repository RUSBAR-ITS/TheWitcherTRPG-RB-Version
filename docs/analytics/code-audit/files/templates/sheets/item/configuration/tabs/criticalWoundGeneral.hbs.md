# templates/sheets/item/configuration/tabs/criticalWoundGeneral.hbs

## Актуализация 2026-09-17 — 14.3.1.00048, TASK-0009.002

**Назначение:** Вкладка настроек травмы.

**Методы, сущности, действия:** formGroup для ручного ID, запретов, canHeal и формулы. Два текстовых UUID inputs в отдельных data-wound-target зонах. Вывод computed срока и пояснения; текстовый submit и Drop проверяются в классе листа, native DocumentUUID Drop не подключён.

**Зависимости и потребители:** [module/item/sheets/configurations/WitcherCriticalWoundConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherCriticalWoundConfigurationSheet.js), [module/data/item/criticalWoundData.js](../../../../../../../../../module/data/item/criticalWoundData.js), [lang/ru.json](../../../../../../../../../lang/ru.json), [lang/en.json](../../../../../../../../../lang/en.json).

Проверки: настоящий TypeDataModel/поля/Roll Foundry 14.367, компиляция Handlebars; лист/DOM/UUID lookup/запись представлены фасадами. Браузер/сохранение после reload не проверялись. [Протокол](../../../../../../../task-0009-002-checks.md).

