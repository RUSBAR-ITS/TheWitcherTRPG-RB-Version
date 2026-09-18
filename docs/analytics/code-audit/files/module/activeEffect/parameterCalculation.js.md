# module/activeEffect/parameterCalculation.js

## Текущее состояние — 14.3.1.00062

2026-09-18, TASK-0010.004. **Назначение:** Чистая арифметика числовых модификаторов.

**Сущности, действия и зависимости:** calculateOperations: ADD→MULTIPLY→OVERRIDE по приоритету, без промежуточного округления. calculateParameter: value/cap/advancement/fullExtra/rollModifier/rollExtra/optionalChanges, округление и границы; finite/limit — внутренние проверки. Только числовые входы, нет Foundry или записи. Потребитель — parameterPreparation.js.

[Исходник](../../../../../../module/activeEffect/parameterCalculation.js), [проверки и границы](../../../../task-0010-004-checks.md). Реальные методы Foundry с двойниками хранения/UI; браузерная приёмка отложена.
