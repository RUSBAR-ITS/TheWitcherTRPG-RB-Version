# module/scripts/rolls/prepareCheck.js

## Текущее состояние

**14.3.1.00066, TASK-0010.008.** prepareCheck ждёт числовой ручной ввод при promptManual, затем conditionalModifiers.chooseRollModifiers. null отменяет действие. Формирует 1d10 с formatRollContributions; при обратном сравнении поправки уже в threshold, куб без добавок. dontAddAttr исключает характеристику. Документы не пишет; потребитель расходует ресурс после выбора.

[Исходник](../../../../../../../module/scripts/rolls/prepareCheck.js); [проверка и пределы](../../../../../task-0010-008-checks.md).

## Назначение и использование

Общий вход подготовки проверки. prepareCheck ждёт числовой ручной ввод при promptManual, затем conditionalModifiers.chooseRollModifiers. null отменяет действие. Формирует 1d10 с formatRollContributions; при обратном сравнении поправки уже в threshold, куб без добавок. dontAddAttr исключает характеристику. Документы не пишет; потребитель расходует ресурс после выбора.
