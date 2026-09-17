# module/rollTable/witcherRollTable.js

Исходник: [module/rollTable/witcherRollTable.js](../../../../../../module/rollTable/witcherRollTable.js); дата 2026-09-17, ветка dev, 14.3.1.00026. Статус: проверено по исходнику; исполнение в Foundry отложено. Основание: [issue-00332](../../../../../issues/closed/issue-00332.md).

## Назначение

Документ RollTable для мира системы с согласованным пределом рекурсивной глубины 10. Метод скопирован из Foundry 14.367 `/opt/foundryvtt/client/documents/roll-table.mjs`; отличие предела `_depth > 5` → `_depth > 10`. Корень имеет глубину 0.

## Сущности и основные методы

- `WitcherRollTable` — default export, наследник `foundry.documents.RollTable`.
- `roll({roll, recursive=true, normalize=true, _depth=0}={})` — асинхронный метод, возвращающий прежние `{roll, results}`. Сохраняет доступные результаты, normalize для пустой формулы, проверки исчерпания/диапазонов, внутренние таблицы и порядок вложенной выдачи. `_depth > 10` отклоняет Promise, цикл останавливается той же защитой.

## Используемые сущности и действия

Foundry: `foundry.documents.RollTable`, `foundry.dice.Roll.defaultImplementation`, `foundry.utils.fromUuid`, `game.i18n.localize`, `ui.notifications`, методы текущей таблицы и TableResult. `Roll`, `_loc` и `fromUuid` оригинального модуля заменены доступными в системе публичными объектами. Остальной текст метода сверен с установленным ядром.

## Зависимости и потребители

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) импортирует класс и присваивает `CONFIG.RollTable.documentClass` в init. Унаследованные draw/drawMany и листы должны вызывать override roll; реальные конструкторы таблиц мира/компедиумов и нормализованной копии проверяются после перезапуска. [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js) — косвенный потребитель через найденную RollTable; компедиумы генерации персонажа — через рекурсивные ссылки. Прямых импортов JS системы внутри этого файла нет.

## Границы

Предел действует на все таблицы мира этой системы, включая модульные. Нового поиска циклов нет. Обновление Foundry требует сравнить копию со штатным методом. Ошибки UI-кнопки при отклонении roll отдельно не исправлены.
