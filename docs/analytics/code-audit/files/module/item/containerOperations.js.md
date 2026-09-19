# module/item/containerOperations.js

## Актуализация 2026-09-19 — 14.3.1.00115

createContainerDocuments после expandTemplates и до rawCreate получает ожидаемые quantity/lootQuantityFormula из входных узлов через CONFIG.Item.dataModels[type].schema.fields: clean и validate(strict=true,fallback=false). После записи сравнивает _source.system обоих полей с этим ожиданием. Проверка принимает штатное приведение "6"→6 и trim формулы, но не подмену количества/формулы результатом записи. У моделей без поля оно не проверяется. Новых UUID/правил владения/хранения не вводится; containerTemplates переносит поля без бросков и изменения веса от формулы.

[Результаты107 статических проверок и границы](../../../../task-0011-static-checks.md#quantity-installed-00115). Ниже сохранён исходный пофайловый аудит на его дату; при расхождении текущий контракт описан выше.

## Текущее состояние — 14.3.1.00105

2026-09-19, TASK-0011.005. locationPatches записывает isStored и equipped=false вместе, если предмет экипируемый и помещается/извлекается из хранения. Предыдущий механизм восстановления патчей включает оба поля. createCopy принимает stored, выставляет isStored/equipped до createDocuments; place передаёт назначение и сохраняет снятие при drag с sourceContainer даже на Actor-монстра. Обычный импорт оружия монстру сохраняет прежнее автоэкипирование. UUID, перемещение/копирование, права и вес прежние; обновление Item использует существующие эффекты/parameterPersistence.

[Проверки и границы](../../../../task-0011-static-checks.md#task-0011005): 72 локальных сценария, B05 впереди. Ниже — датированные прежние срезы; утверждения о сохранении equipped при хранении и неограниченной компенсации EV заменены этим разделом.

[Исходный файл](../../../../../../module/item/containerOperations.js)

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../issues/closed/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Ожидаемые операции с содержимым и компенсация частичных записей.

**Основные методы, сущности и действия:** storeItem/importToActor ведут в place: шаблон копируется, свой экземпляр перемещается, между Actor копия создаётся прежде удаления источника. extractItem возвращает вещь в инвентарь; повреждённая внешняя ссылка очищается явно без изменения чужого Item. createContainerDocuments разворачивает шаблоны одной native create пачкой, проверяет результат и чистит только новые ID при отказе. deleteContainerDocuments/deleteTrees подтверждают удаление полного дерева, снимают внешнее членство, проверяют удалённые ID, при отказе пытаются восстановить снимок. withOwners блокирует повтор в этом клиенте; snapshot/assertUnchanged и restorePatches обнаруживают часть конфликтов. runContainerAction показывает локализованную ошибку. Неполная компенсация не объявляется успехом, последняя сохранившаяся копия не удаляется.

**Зависимости и потребители:** containerTemplates.js: liveTree/copyData/expandTemplates/contentOf/parentsOf/ownerItems/sameOwner/validateTemplate/cloneData/containerError/CONTAINER_INTERNAL/STORABLE_TYPES. CONFIG.Item.documentClass native create/update/delete, DialogV2.confirm, canUserModify/canUserCreate, ui.notifications. Потребители: WitcherItem, WitcherContainerSheet, Actor itemMixin. Локальная блокировка и компенсация не являются межклиентской транзакцией.
