# module/activeEffect/temporaryHpDuration.js

## Актуальное изменение TASK-0012 — 14.3.1.00139

2026-09-20, dev. temporaryHpCombat выбирает начатый бой получателя. initialTemporaryHpClock очищает привязку шаблона и задаёт фактический старт; temporaryHpDuration готовит ручную/боевую подпись без native time expiration. reconcileTemporaryHp связывает/удаляет раундовые AE через withParameterChanges только на активном GM. registerTemporaryHpHooks подключает Combat/Combatant/AE/ready/userConnected; refreshActor последовательно обрабатывает одного Actor. Минуты/часы/дни не истекают автоматически.

Связанные потребители/границы: WitcherActiveEffect, registerHooks; parameterPersistence, native Hooks/Combat/Actor. Статические проверки выполнены; браузер и БД не запускались. [Исходник](../../../../../../module/activeEffect/temporaryHpDuration.js) · [TASK-0012](../../../../../tasks/task-0012-temporary-hp.md) · [Проверки](../../../../task-0012-checks.md).

## Назначение и способы использования

Боевой срок временных ПЗ. temporaryHpCombat выбирает начатый бой получателя. initialTemporaryHpClock очищает привязку шаблона и задаёт фактический старт; temporaryHpDuration готовит ручную/боевую подпись без native time expiration. reconcileTemporaryHp связывает/удаляет раундовые AE через withParameterChanges только на активном GM. registerTemporaryHpHooks подключает Combat/Combatant/AE/ready/userConnected; refreshActor последовательно обрабатывает одного Actor. Минуты/часы/дни не истекают автоматически.

## Введённые сущности и действия

- `temporaryHpCombat` — назначение и взаимодействия описаны выше.
- `initialTemporaryHpClock` — назначение и взаимодействия описаны выше.
- `temporaryHpDuration` — назначение и взаимодействия описаны выше.
- `reconcileTemporaryHp` — назначение и взаимодействия описаны выше.
- `registerTemporaryHpHooks` — назначение и взаимодействия описаны выше.

## Зависимости и потребители

[parameterPersistence.js](../../../../../../module/actor/parameterPersistence.js) Потребители: WitcherActiveEffect, registerHooks; parameterPersistence, native Hooks/Combat/Actor.

## Проверка

Перекрёстно сопоставлены реальные определения, вызовы и новый контракт TASK-0012. Связи зарегистрированы в индексе; внешние Foundry API остаются границами. [Фасады, команды и пределы проверки](../../../../task-0012-checks.md).
