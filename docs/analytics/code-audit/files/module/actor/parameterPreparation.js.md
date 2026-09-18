# module/actor/parameterPreparation.js

## Текущее состояние

**14.3.1.00065, TASK-0010.007.** parameterTarget дополнен числовыми .value групп, attack/defense и strong/joint. Эти строки проходят тот же native numeric resolver и вычислитель; prepared .value содержит параметрический вклад, rollExtra и optionalChanges остаются отдельно. prepareParameterInputs снимает baseline существующих объектов; prepareSkillParameters готовит их вместе с builtin навыками. Ненумерические целые объекты статусов остаются native. Не создаёт произвольную группу без её определения; numeric targets требуют существующего объекта. Объект initial + optional numeric final проверен через установленный lifecycle.

[Исходник](../../../../../../module/actor/parameterPreparation.js); [проверка и пределы](../../../../task-0010-007-checks.md).

## Текущее состояние — 14.3.1.00063

2026-09-18, TASK-0010.005. **Назначение:** Сбор числовых строк Actor и временного контекста.

**Методы, сущности, действия и зависимости:** parameterTarget теперь включает derivedStats.max/totalModifiers и value фиксированных показателей. Текущие hp/sta/resolve/focus/vigor/shield.value остаются native, как luck/toxicity.value. prepareParameterInputs собирает derived inputs с ручной/начальной базой, nativeOffset и собственными строками; calculateActorParameter сохраняет contextualChanges отдельно в states.contexts. Источники: modifierContext, parameterCalculation, RESOURCE_STATS из derivedStatData и нативный Foundry. Потребитель нового контекста — derivedPreparation; действующие primary/builtin маршруты .004 сохранены.

[Исходник](../../../../../../module/actor/parameterPreparation.js), [проверки и границы](../../../../task-0010-005-checks.md). Браузерная приёмка отложена. Ниже, если есть, сохранены датированные предыдущие срезы; изменённые расчёты описаны здесь.

