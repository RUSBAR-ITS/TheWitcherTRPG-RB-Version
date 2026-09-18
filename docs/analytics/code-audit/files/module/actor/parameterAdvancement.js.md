# module/actor/parameterAdvancement.js

## Текущее состояние — 14.3.1.00064

2026-09-18, TASK-0010.006. **Назначение:** Расчёт допуска/цены и покупка уровня.

**Методы, сущности, действия и зависимости:** retainedBaseLimit определяет допустимую приобретённую базу по потолку и отмеченным строкам; положительный бонус не отнимает уровни ниже обычного потолка. advancementQuote проверяет тип character, input/source, отдельно цену и предел. purchaseParameter берёт source-балансы и копию ipLog, делит магическую/обычную оплату, проверяет средства и ожидает один Actor.update. Нет вызова Log.addIpReward. Зависимости: parameterCalculation.calculateOperations/calculateParameter, parameterPreparation.prepareParameterInputs, Foundry utils/i18n/notifications. Потребители — actor.skillMixin и parameterPersistence.

[Исходник](../../../../../../module/actor/parameterAdvancement.js), [проверки/границы](../../../../task-0010-006-checks.md). Ниже, если есть, сохранены датированные предыдущие срезы; изменённые операции описаны здесь.
