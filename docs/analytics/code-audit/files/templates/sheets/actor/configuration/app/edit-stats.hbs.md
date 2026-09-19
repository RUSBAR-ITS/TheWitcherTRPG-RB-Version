# templates/sheets/actor/configuration/app/edit-stats.hbs

## Текущее состояние — 14.3.1.00077

2026-09-19, TASK-0010.014–.018. Прокручиваемая modifier-list с общей шапкой колонок; выбирает source/prepared контекст stats или derivedStats, подключает stats-block. Локализация колонок WITCHER.Editor; запись остаётся в существующем обработчике.

[Исходник](../../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs), [реализация и проверки](../../../../../../../task-0010-ui-fixes.md). Локальная проверка пройдена; реальная игровая/визуальная приёмка ожидается (HTTP502). Следующие датированные разделы описывают прежние срезы.


| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.030](../../../../../../../../tasks/task-0003.030.md), 9 файлов, 424 логических строк |
| Запись перекрёстной сверки | [TASK-0003.030](../../../../../../review-log.md#task-0003030) |

Актуализация [issue-00001](../../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Обёртка редактора характеристик: выбирает system.stats или system.derivedStats и передаёт их общему stats-block.

## Условия использования

PARTS.stats WitcherModifiersConfiguration; контекст type/system. type='stats' передаёт также reputation из родительского system; type='derivedStats' её не передаёт. При прочих значениях остаётся пустой div.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| div.edit-stats / if type | Весь HBS,11 строк | Выбор содержимого | eq type stats/derivedStats | Не выбирает сам PARTS |
| with stats и hash partial | 3–8 | Контекст общего блока | stats=stats; reputation=../system.reputation только в первом случае | @root сохраняется у partial |

## Основные функции и методы

Собственных функций нет. Два буквальных вызова одного stats-block; локальная переменная stats обозначает разные модели по type. Имена input создаёт дочерний partial, форма и submit принадлежат классу конфигурации.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| stats-block.hbs | [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) | Буквальный partial,2 вызова | Создаёт поля для выбранной группы | 4,8 |
| WitcherModifiersConfiguration | [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | Контекст/PARTS | type/system, стандартная форма | PARTS.stats и _prepareContext |
| Stats / DerivedStats / Reputation | [module/data/actor/templates/common/stats/statsData.js](../../../../../../../../../module/data/actor/templates/common/stats/statsData.js); [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); [module/data/actor/templates/common/reputationData.js](../../../../../../../../../module/data/actor/templates/common/reputationData.js) | Данные system | Группа и optional reputation | with и ../system.reputation |
| eq / if / with | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Системный eq и встроенные Handlebars helpers | Выбор группы | Helper eq; собственный preload этого HBS отсутствует |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | Весь HBS | PARTS.stats | Буквальный путь 35 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Не пишет данные и не ограничивает числовые поля. type влияет только на содержимое этой части; edit-skills отдельно проверяет skillKey. В текущих обычных вызовах открывается один содержательный набор.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный файл и контекст | 11 строк; два partial и оба openModifiers | stats/derivedStats/прочие ветви установлены | Статическая область module/templates |
| Настоящий рендер/форма | Группы 11,14–15 | stats10 полей, derived12; другие type без stats полей; reputation передана правильно | Document.update подменён; FormDataExtended настоящий |

## Непроверенные участки и открытые вопросы

Сверены producer контекста, HBS и именованные поля. Реальная обработка FormDataExtended из .030 — изолированное историческое доказательство; браузер, права и серверный submit не запускались. Точный остаток — [U003-04](../../../../../../cross-check-0002.md#u003-04).

## Связанные проблемы

[issue-00194](../../../../../../../../issues/potential/issue-00194.md), [issue-00195](../../../../../../../../issues/potential/issue-00195.md). Обе проблемы локализованы в контрактах формы с моделью и подготовкой Actor.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003030) |

## Сквозная сверка TASK-0004.003

2026-09-14; rusbar-main, b4aeecb967caf97700cc565a670d6347b933619f. Исходник совпадает со срезом TASK-0001; изменено только описание.

Wrapper выбирает system.stats либо system.derivedStats по type и дважды ссылается на один partial. Только обычная ветвь передаёт reputation; @root.type остаётся адресатом динамического name. Wrapper не рассчитывает max, не ограничивает поля и не устраняет max→unmodifiedMax у дочернего partial.

Сопоставленные определения и потребители: [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js.md), [templates/sheets/actor/configuration/app/partials/stats-block.hbs](partials/stats-block.hbs.md), [module/data/actor/commonActorData.js](../../../../../module/data/actor/commonActorData.js.md).

[Протокол и границы](../../../../../../review-log.md#task-0004003) — TASK-0004.003; процессы [R003-10](../../../../../../cross-check-0002.md#r003-10). Новое исполнение N01 протокола ограничено моделями и собственными расчётами Actor; остальные перечисленные опыты относятся к прежним порциям.
