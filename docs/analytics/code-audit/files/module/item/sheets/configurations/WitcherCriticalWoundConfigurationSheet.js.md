# module/item/sheets/configurations/WitcherCriticalWoundConfigurationSheet.js

## Актуализация 2026-09-17 — 14.3.1.00048, TASK-0009.002

**Назначение:** Редактор настроек и адресных переходов травмы.

**Методы, сущности, действия:** Наследует общую конфигурацию, заменяет только PARTS.general. _onRender подключает две зоны Drop. _onDropWound берёт поле по currentTarget, ожидает fromDropData, проверку и update. _processSubmitData нормализует пустоту в null, разрешает UUID и проверяет семью/место перед inherited submit. Штатная вкладка ActiveEffect сохранена. Пустые ссылки допустимы как настройки; их игровая семантика завершается в .003.

**Зависимости и потребители:** [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js), [module/item/criticalWoundOperations.js](../../../../../../../../module/item/criticalWoundOperations.js), [templates/sheets/item/configuration/tabs/criticalWoundGeneral.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/criticalWoundGeneral.hbs), [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js).

Проверки: настоящий TypeDataModel/поля/Roll Foundry 14.367, компиляция Handlebars; лист/DOM/UUID lookup/запись представлены фасадами. Браузер/сохранение после reload не проверялись. [Протокол](../../../../../../task-0009-002-checks.md).

