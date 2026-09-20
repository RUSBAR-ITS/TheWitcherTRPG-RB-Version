# module/scripts/temporaryHpCalculation.js

## Актуальное изменение TASK-0012 — 14.3.1.00139

2026-09-20, dev. resolveTemporaryHpReference читает source/target base/effective через resolveRollTarget и skillIdentity. temporaryHpFormulaData разрешает только использованные aliases. validateTemporaryHpFormulas проверяет полные строки через Roll.validate. calculateTemporaryHp независимо вычисляет формулу за каждый пункт либо один раз в Fix, округляет всю сумму и отдельно вычисляет срок. Нет записи Actor/AE и eval.

Связанные потребители/границы: professionMixin; native Roll, rollContext, skillIdentity. Статические проверки выполнены; браузер и БД не запускались. [Исходник](../../../../../../module/scripts/temporaryHpCalculation.js) · [TASK-0012](../../../../../tasks/task-0012-temporary-hp.md) · [Проверки](../../../../task-0012-checks.md).

## Назначение и способы использования

Расчёт временных ПЗ. resolveTemporaryHpReference читает source/target base/effective через resolveRollTarget и skillIdentity. temporaryHpFormulaData разрешает только использованные aliases. validateTemporaryHpFormulas проверяет полные строки через Roll.validate. calculateTemporaryHp независимо вычисляет формулу за каждый пункт либо один раз в Fix, округляет всю сумму и отдельно вычисляет срок. Нет записи Actor/AE и eval.

## Введённые сущности и действия

- `resolveTemporaryHpReference` — назначение и взаимодействия описаны выше.
- `temporaryHpFormulaData` — назначение и взаимодействия описаны выше.
- `validateTemporaryHpFormulas` — назначение и взаимодействия описаны выше.
- `calculateTemporaryHp` — назначение и взаимодействия описаны выше.

## Зависимости и потребители

[rollContext.js](../../../../../../module/actor/rollContext.js), [skillIdentity.js](../../../../../../module/item/skillIdentity.js) Потребители: professionMixin; native Roll, rollContext, skillIdentity.

## Проверка

Перекрёстно сопоставлены реальные определения, вызовы и новый контракт TASK-0012. Связи зарегистрированы в индексе; внешние Foundry API остаются границами. [Фасады, команды и пределы проверки](../../../../task-0012-checks.md).
