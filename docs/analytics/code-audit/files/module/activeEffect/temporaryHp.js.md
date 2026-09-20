# module/activeEffect/temporaryHp.js

## Актуальное изменение TASK-0012 — 14.3.1.00139

2026-09-20, dev. temporaryHpSources читает активные allApplicableEffects и source system.changes с точным ключом/положительным объектным остатком; FIFO по createdTime и UUID. temporaryHpTotal суммирует те же строки. spendTemporaryHp планирует расход, обновляет только source строки либо удаляет исчерпанный AE целиком. temporaryHpEffectData создаёт plain type:base/system.changes/img с отдельным сроком.

Связанные потребители/границы: damageMixin, WitcherActorSheet/V1, professionMixin; native AE/update/delete. Статические проверки выполнены; браузер и БД не запускались. [Исходник](../../../../../../module/activeEffect/temporaryHp.js) · [TASK-0012](../../../../../tasks/task-0012-temporary-hp.md) · [Проверки](../../../../task-0012-checks.md).

## Назначение и способы использования

Источники и расход временных ПЗ. temporaryHpSources читает активные allApplicableEffects и source system.changes с точным ключом/положительным объектным остатком; FIFO по createdTime и UUID. temporaryHpTotal суммирует те же строки. spendTemporaryHp планирует расход, обновляет только source строки либо удаляет исчерпанный AE целиком. temporaryHpEffectData создаёт plain type:base/system.changes/img с отдельным сроком.

## Введённые сущности и действия

- `temporaryHpSources` — назначение и взаимодействия описаны выше.
- `temporaryHpTotal` — назначение и взаимодействия описаны выше.
- `spendTemporaryHp` — назначение и взаимодействия описаны выше.
- `temporaryHpEffectData` — назначение и взаимодействия описаны выше.

## Зависимости и потребители

Прямых ES-импортов нет; используется контекст Foundry/Handlebars. Потребители: damageMixin, WitcherActorSheet/V1, professionMixin; native AE/update/delete.

## Проверка

Перекрёстно сопоставлены реальные определения, вызовы и новый контракт TASK-0012. Связи зарегистрированы в индексе; внешние Foundry API остаются границами. [Фасады, команды и пределы проверки](../../../../task-0012-checks.md).
