# module/item/collections/WitcherItems.js

[Исходный файл](../../../../../../../module/item/collections/WitcherItems.js)

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../../issues/closed/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Штатный импорт контейнеров в мировую коллекцию Items.

**Основные методы, сущности и действия:** _prepareImportDocument отключает keepId для контейнера до ветки замены существующего документа Foundry. fromCompendium сериализует полное дерево, очищает content/isStored и не сохраняет ID корня. Другие Item делегируются ядру без изменения поведения.

**Зависимости и потребители:** Наследует foundry.documents.collections.Items; serializeContainer из containerTemplates.js. CONFIG.Item.collection регистрируется в module/TheWitcherTRPG.js; WitcherItem.createDocuments разворачивает payload. Покрывает Import и Import All через соответствующие границы ядра.
