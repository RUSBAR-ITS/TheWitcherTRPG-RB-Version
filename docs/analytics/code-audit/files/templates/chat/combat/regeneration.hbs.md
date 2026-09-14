# templates/chat/combat/regeneration.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/combat/regeneration.hbs](../../../../../../../templates/chat/combat/regeneration.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.045](../../../../../../tasks/task-0003.045.md), 5 файлов / 336 логических строк; данный файл — 8 |
| Запись перекрёстной сверки | [TASK-0003.045](../../../../review-log.md#task-0003045) |

## Назначение файла

Выводит имя монстра, текущее HP и настроенное значение регенерации в сообщении для активного GM.

## Условия использования

Единственный найденный прямой renderTemplate находится в applyMonsterRegeneration из [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js):16–21. До вызова отсекаются не-monster, нулевая регенерация и dead. Контекст {actor} формируется до update HP. Выбор whisper/speaker/style делает вызывающий JS.

## Введённые сущности и действия с ними

| Сущность | Вид / строки | Действия |
| --- | --- | --- |
| div → h3 + div → два p | HTML:1–8 | Контейнер, имя и две подписи со значениями |
| actor.name | Выражение:2 | Экранированное имя |
| actor.system.derivedStats.hp.value | Выражение:4 | HP перед запросом регенерации |
| actor.system.regeneration | Выражение:5 | Настроенный размер, не фактически восстановленное HP |
| localize WITCHER.Actor.Hp / WITCHER.Monster.regeneration | Helpers:4–5 | Перевод подписей |

## Основные функции и методы

Собственных JS-функций, событий, ветвлений, циклов и partial нет. Handlebars выполняет два localize и три чтения actor. Все значения используются в двойных фигурных скобках; имя экранируется.

## Используемые сущности и зависимости

| Сущность | Источник | Связь / основание |
| --- | --- | --- |
| actor / renderTemplate | [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) | Producer context {actor}; сообщение формируется перед HP update |
| regeneration | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | NumberField; схема не требует положительности |
| derivedStats.hp.value | [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js) | Ресурс Actor |
| name | Foundry Actor document | Верхнеуровневое поле, не actor.system.name |
| WITCHER.Actor.Hp / WITCHER.Monster.regeneration | [lang/en.json](../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../lang/ru.json) | Два ключа localize |
| Handlebars / localize | Foundry 14.367.0 | Штатная интерполяция; в Node настоящий Handlebars и фасад localize |
| div, h3, p | HTML и стили клиента | Нет собственных классов/ID; конкретный визуальный каскад не установлен |

## Известные потребители

[module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) — applyMonsterRegeneration, прямой путь systems/TheWitcherTRPG/templates/chat/combat/regeneration.hbs. В module/templates иных путей загрузки не найдено. Сообщение показывает Foundry ChatMessage; сам HBS не определяет получателей.

## Данные и изменения состояния

Создаётся HTML. Шаблон не лечит Actor, не меняет данные и не подтверждает update. При HP19/max20 и regeneration2 сообщение показывает 19 и 2, хотя запрос увеличивает HP лишь на 1. HP.max и результат Math.min в контексте напрямую не выводятся. При полном HP сообщение по-прежнему создаётся.

## Проверки и доказательства

Группа 15: настоящий applyMonsterRegeneration и Handlebars получили имя <A>, HP19 и regeneration2. HTML содержит &lt;A&gt;,19 и 2; отдельно update запросил 20, whisper содержит текущего GM. Контроль с полным HP также запросил 20. Группа 16 проверила допустимую схемой отрицательную регенерацию. DOM/браузер и сохранённый ChatMessage не создавались.

## Непроверенные участки и открытые вопросы

Контекст/подстановки и ограничение HP установлены. .016/.018 сохраняют HTTP/CSS/тему/реальный чат ([U011-03](../../../../cross-check-0002.md#u011-03)); .018 — порядок update ([U011-02](../../../../cross-check-0002.md#u011-02)). Изменение текста configured→фактически healed и политика отрицательной регенерации требуют решения ([U011-07](../../../../cross-check-0002.md#u011-07)).

## Связанные проблемы

Прямых самостоятельных ошибок HBS в данной порции не зарегистрировано. [6](../../../../../../issues/potential/issue-00006.md) и [299](../../../../../../issues/potential/issue-00299.md) относятся к условиям запуска/ожиданию JS и могут влиять на количество сообщений и фактическое восстановление.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 20ce99a1218a82bf46c84570e55587253d0cfbc3; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003045) |

## Сквозная сверка TASK-0004.011

2026-09-14; rusbar-main, 55e56567f42ed2da8850d913f28d727113ebdbd3. Исходник совпадает со срезом TASK-0001; изменено только описание.

Producer передаёт имя Actor, HP до обновления и configured regeneration; cap применяется только в запросе update, поэтому сообщение не показывает фактически прибавленный остаток до max. Имя/числа экранируются HBS; сообщение whisper GM. Create/update не ожидаются после render, и при full HP сообщение всё равно может появиться.

Сопоставленные определения и потребители: [module/scripts/combat/generalCombatHook.js](../../../module/scripts/combat/generalCombatHook.js.md).

[Протокол и границы](../../../../review-log.md#task-0004011) — TASK-0004.011; процессы [R011-21](../../../../cross-check-0002.md#r011-21). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
