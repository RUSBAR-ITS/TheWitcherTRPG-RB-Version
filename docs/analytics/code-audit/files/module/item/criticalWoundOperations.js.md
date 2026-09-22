# module/item/criticalWoundOperations.js

**Приёмка .00144, отчёт .00145:** однократные часы травмы подтверждены в12 боевых сочетаниях; проверены обычный импорт предметов, свежий drop травм, строгий отказ записи, семейства/истечение и reload. [Протокол и границы](../../../../task-0012-checks.md#browser-00144). Явный start при установке травмы сохраняется по принятому контракту; источник свежего timed drop имеет null start. В этом отчёте исходник не менялся.

## Актуальное уточнение — 14.3.1.00144

writeStage перед первым create готовит часы ожидаемой стадии через initializeEffectStart. WOUND_INTERNAL сохраняет их в WitcherItem.createDocuments → assignedItemData. Вложенный AE._preCreate при создании Item не вызывается. stageMatches и ветка обновления ForcedReplacement прежние; в этом файле уточнён только комментарий.

[Проверки и границы](../../../../task-0012-checks.md#clock-fix-00144): 38/38 локально, игровой повтор впереди. Более ранние датированные записи ниже — история.

**Проверка .00142, отчёт .00143:** реальная цепочка создания травмы проходит `writeStage → WitcherItem.createDocuments → assignedItemData`. Предварительная коррекция раундового срока в writeStage повторяется после безусловного сброса start в assignedItemData. При сроке3 получено1 вместо2;00336/.010 не завершены. Вложенный AE._preCreate в этом пути не вызывается. [Доказательства и границы](../../../../task-0012-checks.md#browser-00142). Код здесь не изменён.

## Актуальное изменение — 14.3.1.00142

writeStage перед первым create вызывает импортированный initializeEffectStart для каждой подготовленной копии AE. Ожидаемый и отправляемый start/duration совпадают; штатный _preCreate не корректирует их повторно. stageMatches остаётся строгим; ветка замены через ForcedReplacement и настоящий отказ записи сохранены.

[Исходник](../../../../../../module/item/criticalWoundOperations.js) · [Проверки и границы](../../../../task-0012-checks.md#fixes-00142). Локальная приёмка выполнена; игровой повтор впереди. Более ранние датированные описания ниже — история.

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

