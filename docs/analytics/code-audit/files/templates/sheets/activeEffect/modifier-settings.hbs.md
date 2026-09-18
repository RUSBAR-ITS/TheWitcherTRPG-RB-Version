# templates/sheets/activeEffect/modifier-settings.hbs

## Текущее состояние — 14.3.1.00074

Вместо select multiple используется сворачиваемый details с native multi-checkbox. selectOptions помечает сохранённые excludedDerived, имя поля прежнее. Summary показывает выбранные подписи или локализованное отсутствие выбора. Потребители — change.hbs и wizard.hbs; контекст/события — WitcherActiveEffectSheet, значения — modifierContext.

[Проверки и границы](../../../../../task-0010-013-browser-checks.md#checkboxes-00074): локальный стенд; повтор в мире ожидается после запуска. Предыдущие датированные сведения сохранены ниже.

## Текущее состояние — 14.3.1.00073

Общий partial получает класс witcher-modifier-settings; строки шести галочек — modifier-flag, исключения производных — stacked. styles/activeEffect.css отдаёт названиям свободную ширину; данные/имена полей/обработчики сохраняются. Потребители: wizard.hbs и change.hbs; контекст и переключение каналов — WitcherActiveEffectSheet/modifierContext.

[Исправление и проверки](../../../../../task-0010-013-browser-checks.md#fixes-00073). Локальные проверки, без запуска Foundry; повтор в мире ожидается. Ниже сохранены предыдущие датированные сведения.

## Текущее состояние — 14.3.1.00061

2026-09-18, TASK-0010.003. **Назначение:** Общая форма шести флагов и исключений производных.

**Сущности, действия и зависимости:** modifierInputs задаёт имя, состояние и доступность checkbox; multiple select использует derivedChoices. Работает и в строке AE, и в мастере. Данные/переключение поставляет WitcherActiveEffectSheet и modifierContext.js.

[Исходник](../../../../../../../templates/sheets/activeEffect/modifier-settings.hbs), [проверки и границы](../../../../../task-0010-003-checks.md). Статическая проверка; игровая приёмка не проводилась. Численный контракт следующих стадий ещё не внедрён.
