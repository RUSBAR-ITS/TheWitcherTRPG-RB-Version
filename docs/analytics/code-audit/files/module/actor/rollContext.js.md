# module/actor/rollContext.js

## Текущее состояние

**14.3.1.00066, TASK-0010.008.** Builtin key, Item ID, profession ID+definingSkill/skillPathN.skillM, stat/derived. Item-навык берёт modifiedValue, профессия level+own activeEffectModifiers с её baseCap; отрицательный навык допустим. Собственные/manual/allSkills учитываются раздельно; совпадение имени со встроенным навыком не меняет цель. Остальной коллектор .007 сохранён.

[Исходник](../../../../../../module/actor/rollContext.js); [проверка и пределы](../../../../task-0010-008-checks.md).

## Назначение и использование

Адреса и числовые вклады одной проверки. resolveRollTarget разрешает builtin key, Item ID, profession ID+валидный slot, stat/derived key. Названия служат подписями. collectRollModifiers снимает контекст actualStat/groups/action/strike/comparison/threshold, источники prepared input/contextualChanges, собственные/manual/group/combat/strike вклады и optional кандидатов по source UUID+индексу. resolveRollModifiers пересчитывает выбранные операции через parameterCalculation.calculateParameter; выдаёт contributions/baseTotal/modifierTotal/total/threshold. Обратный порог увеличивается на modifierTotal. Зависимости: parameterPreparation/derivedPreparation через Actor.parameterModifiers, реальные Item/Actor модели и CONFIG.WITCHER. Не записывает документы и не создаёт Roll. Входы игровых действий подключаются в .008.
