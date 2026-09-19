# module/item/containerTemplates.js

## Текущее состояние — 14.3.1.00105

2026-09-19, TASK-0011.005. expandTemplates перед записью единой пачки задаёт каждому вложенному узлу isStored=true и equipped=false, если поле есть. Это исключает промежуточную активацию переносимых бонусов. Поля корня, новые UUID/origin, исходный payload и подсчёт веса прежние; все операции создания проходят WitcherItem/parameterPersistence.

[Проверки и границы](../../../../task-0011-static-checks.md#task-0011005): 72 локальных сценария, B05 впереди. Ниже — датированные прежние срезы; утверждения о сохранении equipped при хранении и неограниченной компенсации EV заменены этим разделом.

[Исходный файл](../../../../../../module/item/containerTemplates.js)

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../issues/closed/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Проверка, сериализация и разворачивание дерева контейнера.

**Основные методы, сущности и действия:** STORABLE_TYPES задаёт прежние девять типов; CONTAINER_INTERNAL — локальный маркер внутренних вызовов. contentOf/ownerItems/sameOwner/parentsOf/liveTree проверяют сохранённое членство в одной коллекции, видимость, дубли и циклы. validateTemplate проверяет {version:1,sourceUuid,items}, узлы {sourceUuid,data,items}. serializeContainer/copyData создают самодостаточный снимок. expandTemplates создаёт новые ID всем узлам, переносит folder/ownership корня и меняет внутренние ActiveEffect.origin; произвольные строковые ссылки не переписывает. describeContainer вычисляет строки, вес всего дерева и incomplete без fromUuidSync и без зависимости от порядка подготовки дочерних контейнеров.

**Зависимости и потребители:** Foundry deepClone/randomID; game.items, Actor.items, game.packs и i18n. Потребители: containerOperations.js, ContainerData, WitcherContainerSheet, WitcherItem и WitcherItems. Шаблон хранится в system.templateContent, экземпляры связаны system.content; ограничения carry и множитель веса не реализуются.
