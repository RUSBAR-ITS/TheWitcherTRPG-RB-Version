# module/item/criticalWoundOperations.js

## Актуализация 2026-09-17 — 14.3.1.00049

**Назначение:** Общий жизненный цикл criticalWound.

**Методы и действия:** woundKey/requireOwner/prepareWoundStage; installWound и installWoundLocked; transitionWound; healWound/removeWound; writeStage/stageMatches; native createWoundDocuments/validateWoundUpdates; selectInitialWound; очередь withWoundQueue и reportWoundResult. Полная замена через ForcedReplacement.create; результаты applied/unchanged/rejected/failed. Формула/таргет-валидаторы из .002 сохранены.

**Непосредственные зависимости/потребители:** [module/data/item/criticalWoundData.js](../../../../../../module/data/item/criticalWoundData.js), [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js), [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js), [module/actor/mixins/damageMixin.js](../../../../../../module/actor/mixins/damageMixin.js), [module/actor/sheets/mixins/healMixin.js](../../../../../../module/actor/sheets/mixins/healMixin.js), [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js). Foundry Document/Roll/Collection/UI — внешние API.

[Проверки и пределы](../../../../task-0009-lifecycle-checks.md). Ниже сохранены датированные срезы; для изменённых операций действует описание .00049.

## Актуализация 2026-09-17 — 14.3.1.00048, TASK-0009.002

**Назначение:** Общие проверки травм — первая часть сервиса.

**Методы, сущности, действия:** validateHealingDuration разбирает ограниченную грамматику: числа, @body, арифметика и шесть функций. evaluateHealingDuration использует Foundry Roll с strict=true и конечным положительным итогом, возвращает value/error без записи. validateWoundTarget проверяет подтип, доступность, отсутствие self-link, ручной ID и часть тела. Foundry Roll и Item/Actor — внешние API/данные; очередь, payload и операции установки ещё не реализованы.

**Зависимости и потребители:** [module/data/item/criticalWoundData.js](../../../../../../module/data/item/criticalWoundData.js), [module/item/sheets/configurations/WitcherCriticalWoundConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherCriticalWoundConfigurationSheet.js).

Проверки: настоящий TypeDataModel/поля/Roll Foundry 14.367, компиляция Handlebars; лист/DOM/UUID lookup/запись представлены фасадами. Браузер/сохранение после reload не проверялись. [Протокол](../../../../task-0009-002-checks.md).

