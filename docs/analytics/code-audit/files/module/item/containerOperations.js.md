# module/item/containerOperations.js

## Текущее состояние — 14.3.1.00105

2026-09-19, TASK-0011.005. locationPatches записывает isStored и equipped=false вместе, если предмет экипируемый и помещается/извлекается из хранения. Предыдущий механизм восстановления патчей включает оба поля. createCopy принимает stored, выставляет isStored/equipped до createDocuments; place передаёт назначение и сохраняет снятие при drag с sourceContainer даже на Actor-монстра. Обычный импорт оружия монстру сохраняет прежнее автоэкипирование. UUID, перемещение/копирование, права и вес прежние; обновление Item использует существующие эффекты/parameterPersistence.

[Проверки и границы](../../../../task-0011-static-checks.md#task-0011005): 72 локальных сценария, B05 впереди. Ниже — датированные прежние срезы; утверждения о сохранении equipped при хранении и неограниченной компенсации EV заменены этим разделом.

[Исходный файл](../../../../../../module/item/containerOperations.js)

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../issues/closed/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Ожидаемые операции с содержимым и компенсация частичных записей.

**Основные методы, сущности и действия:** storeItem/importToActor ведут в place: шаблон копируется, свой экземпляр перемещается, между Actor копия создаётся прежде удаления источника. extractItem возвращает вещь в инвентарь; повреждённая внешняя ссылка очищается явно без изменения чужого Item. createContainerDocuments разворачивает шаблоны одной native create пачкой, проверяет результат и чистит только новые ID при отказе. deleteContainerDocuments/deleteTrees подтверждают удаление полного дерева, снимают внешнее членство, проверяют удалённые ID, при отказе пытаются восстановить снимок. withOwners блокирует повтор в этом клиенте; snapshot/assertUnchanged и restorePatches обнаруживают часть конфликтов. runContainerAction показывает локализованную ошибку. Неполная компенсация не объявляется успехом, последняя сохранившаяся копия не удаляется.

**Зависимости и потребители:** containerTemplates.js: liveTree/copyData/expandTemplates/contentOf/parentsOf/ownerItems/sameOwner/validateTemplate/cloneData/containerError/CONTAINER_INTERNAL/STORABLE_TYPES. CONFIG.Item.documentClass native create/update/delete, DialogV2.confirm, canUserModify/canUserCreate, ui.notifications. Потребители: WitcherItem, WitcherContainerSheet, Actor itemMixin. Локальная блокировка и компенсация не являются межклиентской транзакцией.
