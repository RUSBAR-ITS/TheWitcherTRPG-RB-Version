# module/item/containerOperations.js

[Исходный файл](../../../../../../module/item/containerOperations.js)

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../issues/open/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Ожидаемые операции с содержимым и компенсация частичных записей.

**Основные методы, сущности и действия:** storeItem/importToActor ведут в place: шаблон копируется, свой экземпляр перемещается, между Actor копия создаётся прежде удаления источника. extractItem возвращает вещь в инвентарь; повреждённая внешняя ссылка очищается явно без изменения чужого Item. createContainerDocuments разворачивает шаблоны одной native create пачкой, проверяет результат и чистит только новые ID при отказе. deleteContainerDocuments/deleteTrees подтверждают удаление полного дерева, снимают внешнее членство, проверяют удалённые ID, при отказе пытаются восстановить снимок. withOwners блокирует повтор в этом клиенте; snapshot/assertUnchanged и restorePatches обнаруживают часть конфликтов. runContainerAction показывает локализованную ошибку. Неполная компенсация не объявляется успехом, последняя сохранившаяся копия не удаляется.

**Зависимости и потребители:** containerTemplates.js: liveTree/copyData/expandTemplates/contentOf/parentsOf/ownerItems/sameOwner/validateTemplate/cloneData/containerError/CONTAINER_INTERNAL/STORABLE_TYPES. CONFIG.Item.documentClass native create/update/delete, DialogV2.confirm, canUserModify/canUserCreate, ui.notifications. Потребители: WitcherItem, WitcherContainerSheet, Actor itemMixin. Локальная блокировка и компенсация не являются межклиентской транзакцией.
