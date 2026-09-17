# module/item/sheets/helpers/linkedItemContext.js

[Исходный файл](../../../../../../../../module/item/sheets/helpers/linkedItemContext.js)

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../../../issues/closed/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Асинхронная подготовка связанного Item для листов.

**Основные методы, сущности и действия:** linkedItemContext(uuid,fallback) сохраняет UUID/ID/имя/количество строки при недоступном документе; возвращает available/missing/img и enriched description. Полный документ загружается через await fromUuid; описание берётся из system.description. Ошибка разрешения даёт fallback, а не запись в исходник.

**Зависимости и потребители:** Foundry fromUuid и TextEditor.enrichHTML; WitcherItemSheet._prepareContext и WitcherDiagramSheet._prepareContext — потребители. secrets зависит от isOwner, relativeTo — сам связанный Item.
