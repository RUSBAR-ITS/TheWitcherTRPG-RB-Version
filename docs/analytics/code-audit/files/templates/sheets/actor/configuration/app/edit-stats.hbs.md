# templates/sheets/actor/configuration/app/edit-stats.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `aa6af106e86a9c75fe050d599f961c8fadb74f1b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.030](../../../../../../../../tasks/task-0003.030.md), 9 файлов, 424 логических строк |
| Запись перекрёстной сверки | [TASK-0003.030](../../../../../../review-log.md#task-0003030) |

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

Wrapper сам не исправляет различие max/unmodifiedMax или игнорируемых вычисляемых параметров. Все свойства числового ввода описаны в дочерней карточке.

## Связанные проблемы

[issue-00194](../../../../../../../../issues/potential/issue-00194.md), [issue-00195](../../../../../../../../issues/potential/issue-00195.md). Обе проблемы локализованы в контрактах формы с моделью и подготовкой Actor.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003030) |
