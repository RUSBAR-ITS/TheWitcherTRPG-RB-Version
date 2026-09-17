# module/data/fields/turnStartEffectField.js

Исходник: [module/data/fields/turnStartEffectField.js](../../../../../../../module/data/fields/turnStartEffectField.js); дата 2026-09-17, ветка dev, 14.3.1.00026. Статус: проверено по исходнику; исполнение в Foundry отложено. Основание: [issue-00332](../../../../../../issues/closed/issue-00332.md).

## Назначение

Поддержать ADD JSON-объекта для одной записи `system.combatEffects.turnStartEffects.<id>` без изменения общего SchemaField Foundry. Хранение и применение остальных полей системы не затрагиваются.

## Сущности и основные методы

| Сущность | Действие |
| --- | --- |
| `TurnStartEffectField` | Default export, наследник SchemaField |
| `_castChangeDelta(raw, replacementData={})` | Подставляет data refs, JSON.parse строку, требует plain object. Не заполняет отсутствующие поля до объединения |
| `_applyChangeAdd(value, delta, model, change)` | Возвращает mergeObject(value??{}, delta, inplace:false); базовые amount не суммирует |
| `TurnStartDamageModifierField` | Именованный export, наследник NumberField только для damage.modifier |
| `_applyChangeAdd(value, delta, model, change)` числового поля | Возвращает (value??0)+delta; отсутствующее значение считается нулём |

## Используемые сущности и действия

Foundry: SchemaField/NumberField и их штатный applyChange; `_replaceDataRefs`, `foundry.utils.isPlainObject`, `foundry.utils.mergeObject`; стандартный JSON.parse. Ошибка JSON или не-объект вызывает исключение в обработке изменения; eval не используется. Штатный applyChange после операции продолжает clean/validate/initialize. Последовательность изменений определяется Foundry priority.

## Зависимости и потребители

[module/data/actor/templates/common/combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js) импортирует оба класса: первый вложен в TypedObjectField(turnStartEffects), второй назначен damage.modifier. [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) читает подготовленные записи и требует amount: один modifier не запускает урон. JSON Heart Damage (Treated) задаёт ADD +2 с priority60 после штатной OVERRIDE-записи кровотечения priority50.

## Границы

Одинаковые явные поля объектов заменяются согласно priority; отсутствующее в delta поле сохраняет предыдущее значение. Это не политика суммирования всех эффектов. heal.modifier и другие SchemaField/NumberField не меняются. Наличие только числового модификатора допускает неактивную запись до появления amount. Пользовательские нестандартные приоритеты исполняются как заданы; независимость от любого порядка OVERRIDE не обещается.
