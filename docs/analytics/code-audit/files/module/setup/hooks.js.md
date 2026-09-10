# module/setup/hooks.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/setup/hooks.js](../../../../../../module/setup/hooks.js) |
| Тип файла | JavaScript — события |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../../../tasks/task-0002-system-initialization.md); порция 4 |
| Запись перекрёстной сверки | [Журнал сверок](../../../review-log.md) — TASK-0002, порция 4 |

## Назначение файла

Подключает updateCombat к обработке эффектов боя и отсчёту длительности регионов.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) вызывает registerHooks на верхнем уровне (стр. 25), до init. Hooks.on лишь регистрирует callback; обработчики выполняются позднее при updateCombat на клиенте.

## Введённые сущности и действия с ними

| Сущность | Доступность | Действие |
| --- | --- | --- |
| registerHooks | export function, стр. 4 | Регистрирует один callback updateCombat |
| callback updateCombat | Анонимная стрелка, стр. 5 | Передаёт combat, update, options, userId в combatHooks |
| combatHooks | Локальная функция, стр. 10 | Запускает две импортированные функции в порядке ниже |

## Основные функции и методы

| Функция | Вход / результат | Действия и асинхронность |
| --- | --- | --- |
| registerHooks() | Без аргументов → undefined | Вызов Hooks.on; ID регистрации не сохраняет и не возвращает |
| updateCombat callback / combatHooks | combat, update, options, userId → undefined | applyGeneralCombatHooks(combat), затем countdownDurationOfRegions(combat, update, options, userId); Promise обеих функций не ожидаются |

Проверок изменённых полей, текущего combatant, активной сцены или пользователя в этом файле нет. Обе зависимые функции сами проверяют game.user.isActiveGM. Они обращаются к текущему участнику без защитного условия; countdown читает регионы активной сцены. Последовательность вызовов не равна последовательному завершению асинхронных операций.

## Используемые сущности и зависимости

| Сущность | Источник | Связь | Где / доказательство |
| --- | --- | --- | --- |
| applyGeneralCombatHooks | [module/scripts/combat/generalCombatHook.js](../../../../../../module/scripts/combat/generalCombatHook.js) | Именованный импорт / вызов | Определение стр. 3; вызов hooks.js:11. Запускает регенерацию monster и turnStartEffects |
| countdownDurationOfRegions | [module/scripts/regions/regionHooks.js](../../../../../../module/scripts/regions/regionHooks.js) | Именованный импорт / вызов | Определение стр. 1; hooks.js:12. Уменьшает duration регионов текущего Actor или удаляет их |
| Hooks.on('updateCombat') | Foundry | Подписка на событие | hooks.js:5; четыре аргумента callback |

## Известные потребители

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) — импорт registerHooks и вызов при загрузке. Остальные вызовы registerHooks/combatHooks вне файла в проверенной области module не обнаружены. После регистрации callback вызывает Foundry; один только импорт не выполняет эффекты боя.

## Данные и изменения состояния

В файле меняется только реестр подписок. Через зависимости возможны сообщения чата, изменения HP/STA от регенерации/статусов, обновление flags регионов и удаление Region. Это косвенные записи, не прямые update в hooks.js.

## Проверки и доказательства

Все 13 строк прочитаны, оба импорта и их определения проверены. Исходный файл и оба обработчика выполнены вместе в vm с подменой Foundry. update={flags:{example:true}} при том же текущем участнике привёл к записи HP 5→7 и duration региона 3→2. Подробности сценария — в журнале и issue-00006.

## Непроверенные участки и открытые вопросы

Межклиентская доставка Hooks, смена/завершение боя и отсутствие активной сцены не воспроизводились. Зависимые файлы не считаются полностью описанными карточками этого этапа. Ошибки async функций не перехватываются данным модулем.

## Связанные проблемы

[issue-00006](../../../../../issues/potential/issue-00006.md) — действия начала хода при произвольном updateCombat.

## Дополнительная сверка — TASK-0003.003

2026-09-10, HEAD `c34b790379fd98cd7e33ccbeeca085e49297a40f`; исходники не изменены.

Полностью разобрана схема [combatEffects](../data/actor/templates/common/combatEffectsData.js.md), включая turnStartEffects. registerHooks только назначает updateCombat; чтение словаря и запись повреждения/лечения находятся в generalCombatHook и его зависимостях. Существующая [issue-00006](../../../../../issues/potential/issue-00006.md) дополнена связью со схемой. Изолированное выполнение обработчика выявило потерю damage.type и игнорирование heal.modifier; эти наблюдения выделены в issue-00021/00022.

[Сценарии и результаты TASK-0003.003](../../../review-log.md#task-0003003).

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 4 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.

2026-09-10 — TASK-0003.003: актуализированы связи с полностью разобранными структурами состояния Actor; ограничения полного клиента сохранены.

## Уточнение TASK-0003.009

2026-09-10, `a33bf33add228ae93f96a52046c8feb4ee992921`. Исходник не изменился относительно указанного ранее среза.

Прослежена ветвь updateCombat → applyGeneralCombatHooks → applyCombatEffects → applyCombatEffect → [templates/chat/combat/statusEffect.hbs](../../../../../../templates/chat/combat/statusEffect.hbs). Контекст — элемент system.combatEffects.turnStartEffects; до рендера проверяются heal.amount/damage.amount, затем сообщение и сами воздействия выполняет generalCombatHook.js. Шаблон не содержит a.apply-status и не вызывает [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js); интерактивные ссылки чата создают другие файлы. Ранее выявленные условия updateCombat не менялись.

[Журнал сверки](../../../review-log.md) — TASK-0003.009; ограничения изолированного выполнения и неподтверждённые проблемы сохранены.
