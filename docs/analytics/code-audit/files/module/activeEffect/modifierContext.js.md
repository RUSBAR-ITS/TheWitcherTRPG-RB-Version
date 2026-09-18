# module/activeEffect/modifierContext.js

## Текущее состояние — 14.3.1.00061

2026-09-18, TASK-0010.003. **Назначение:** Общие настройки и определение цели числового модификатора.

**Сущности, действия и зависимости:** MODIFIER_DEFAULTS; DERIVED_MODIFIER_TARGETS; getEffectTargetType; supportsModifierChange; modifierSettings; switchModifierChannel; derivedModifierChoices. Объекты настроек копируются. Проверка ключа не вычисляет значение. Используются CONFIG.WITCHER.statMap и game.i18n; consumers — модель базового AE и WitcherActiveEffectSheet.

[Исходник](../../../../../../module/activeEffect/modifierContext.js), [проверки и границы](../../../../task-0010-003-checks.md). Статическая проверка; игровая приёмка не проводилась. Численный контракт следующих стадий ещё не внедрён.
