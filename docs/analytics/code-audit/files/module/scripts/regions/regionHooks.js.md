# module/scripts/regions/regionHooks.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/regions/regionHooks.js](../../../../../../../module/scripts/regions/regionHooks.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ef8117ba6e5a184989e65761d47a068381056e4a` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.022](../../../../../../tasks/task-0003.022.md), 5 файлов, 289 логических строк |
| Запись перекрёстной сверки | [TASK-0003.022](../../../../review-log.md#task-0003022) |

## Назначение файла

Отсчёт длительности регионов текущего участника боя и удаление истёкших через Scene API. Вызывается общим обработчиком updateCombat.

## Условия использования

setup/hooks импортирует функцию; registerHooks подписывает updateCombat и combatHooks вызывает её после applyGeneralCombatHooks без await. Внутри только game.user.isActiveGM ограничивает исполнение. Сам файл не регистрирует Hook.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| countdownDurationOfRegions | export async function; 1–18 | Обработчик длительности | Импорт setup/hooks | Чтение Combat и регионов, запросы setFlag/delete |
| actorUuid | Локальная строка 4 | UUID Actor текущего combatant | combat.combatants.get(current.combatantId).actor.uuid | Разыменование без guard |
| toDelete | Локальный массив 6 | ID подходящих регионов для удаления | Scene.deleteEmbeddedDocuments | Заполняется при duration-1<=0 или NaN |
| filter/forEach | Анонимные callbacks8–15 | Выбор Actor и обработка duration | game.scenes.active.regions | Сравнение flags.TheWitcherTRPG?.actorUuid |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async countdownDurationOfRegions(combat, update, options, userId) | Текущий Combatant с Actor; game.scenes.active; активный GM | Promise<undefined> | Читает Actor UUID → фильтрует регионы активной сцены → при duration-1>0 вызывает setFlag, иначе собирает ID → deleteEmbeddedDocuments('Region', toDelete) | update/options/userId не используются; записи не await/return; исключение при недостающем контексте; удаление запрашивается и с пустым массивом |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| registerHooks/combatHooks | [module/setup/hooks.js](../../../../../../../module/setup/hooks.js) | Регистрация/внешний вызов | updateCombat без проверки изменённых полей | 5–12; hook отдельно исполнен в vm |
| flags.TheWitcherTRPG.duration/actorUuid | [module/data/item/mixin/spellRegionMixin.js](../../../../../../../module/data/item/mixin/spellRegionMixin.js) | Контракт данных | Отбор и decrement | fromItem47–48, duration из damage |
| castSpellMixin | [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | Источник damage.duration | Строка длительности заклинания преобразуется, при пустой duration поля нет | duration ветвь 161–176; полный разбор будущий |
| game.user.isActiveGM; Combat.current/combatants; game.scenes.active | Foundry 14.367.0 User/Combat/Scenes API; client/documents/combat.mjs: 633–647, 822–829 | Контекст события | Активный участник/сцена | current.combatantId может быть null; Combat.scene отличается от active scene |
| Region.setFlag; Scene.deleteEmbeddedDocuments | Foundry 14.367.0 Document/Scene API | Запись | duration и удаление Region | В Node подменены управляемыми Promise; БД не менялась |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/hooks.js](../../../../../../../module/setup/hooks.js) | countdownDurationOfRegions | Импорт и вызов на updateCombat | 2, 12 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Уменьшает флаг только регионов с actorUuid текущего Actor. duration3→setFlag2, строка'2'→число 1; 1/0/отрицательное значение идут на удаление. undefined/нечисловая строка дают NaN и тоже попадают в удаление; отсутствующий флаг Actor вообще не проходит фильтр. Никаких проверок начала боя, round/turn или предыдущего combatant здесь нет.

Выбирается game.scenes.active, не combat.scene и не сцены самих найденных регионов. Визуальные секундные таймеры из другой примеси не учитываются. Функция не меняет флаг напрямую в памяти: отправляет setFlag; изменения в тестовых объектах имитировал сборщик для проверки последовательных вызовов.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Границы/повторы | Группы 15–16 | duration3/строка 2 уменьшаются; 1/0/-1/undefined/text удаляются; чужой Actor пропущен. Два произвольных обновления flags дают 3→2→1 без смены хода | Документы — фасады с зарегистрированными вызовами |
| Контекст/сцена/права | Группы 17–18 | Неактивный GM ничего не делает; отсутствие участника/Actor/active scene даёт TypeError. При Combat на A и active B изменён регион B, регион A не тронут | Реальная смена сцены и Hook-сеть не выполнялись |
| Асинхронность/регистрация | Группы 19–20 | Promise обработчика завершается до setFlag/delete; setup/hooks зарегистрировал updateCombat и передал все 4 аргумента | Обработчик соседней регенерации подменён, собственной полной карточки он здесь не получает |

## Непроверенные участки и открытые вопросы

Все 18 строк прочитаны. Порядок событий в живом Combat, гонки записей/нескольких клиентов, смысл неопределённой длительности, сохранение и игровые правила отсчёта отдельно не подтверждены.

## Связанные проблемы

[issue-00006](../../../../../../issues/potential/issue-00006.md), [issue-00142](../../../../../../issues/potential/issue-00142.md), [issue-00144](../../../../../../issues/potential/issue-00144.md), [issue-00145](../../../../../../issues/potential/issue-00145.md), [issue-00146](../../../../../../issues/potential/issue-00146.md). 6 дополнена повторными обновлениями; 142 — ожидание записей; 144 — неверная сцена; 145 — пустой контекст; 146 — трактовка нечисловой duration.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ef8117ba6e5a184989e65761d47a068381056e4a`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003022) |
