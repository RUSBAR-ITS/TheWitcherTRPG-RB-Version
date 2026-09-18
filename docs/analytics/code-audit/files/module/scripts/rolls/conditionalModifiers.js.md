# module/scripts/rolls/conditionalModifiers.js

## Текущее состояние

**14.3.1.00065, TASK-0010.007.** chooseRollModifiers вызывает rollContext.collectRollModifiers и resolveRollModifiers. Без кандидатов окна нет. Иначе renderTemplate conditional-modifiers.hbs и DialogV2.prompt; callback читает checked и возвращает IDs. Новый вызов/смена контекста строит новый список без сохранённого выбора. Отмена возвращает null, документы/ресурсы/длительности не пишет. Отдельный manual передаётся в вычислитель; игровое окно произвольного бонуса остаётся потребителю .008.

[Исходник](../../../../../../../module/scripts/rolls/conditionalModifiers.js); [проверка и пределы](../../../../../task-0010-007-checks.md).

## Назначение и использование

Выбор условных строк после определения контекста. chooseRollModifiers вызывает rollContext.collectRollModifiers и resolveRollModifiers. Без кандидатов окна нет. Иначе renderTemplate conditional-modifiers.hbs и DialogV2.prompt; callback читает checked и возвращает IDs. Новый вызов/смена контекста строит новый список без сохранённого выбора. Отмена возвращает null, документы/ресурсы/длительности не пишет. Отдельный manual передаётся в вычислитель; игровое окно произвольного бонуса остаётся потребителю .008.
