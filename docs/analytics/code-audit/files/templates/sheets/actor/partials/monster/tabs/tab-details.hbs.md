# templates/sheets/actor/partials/monster/tabs/tab-details.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../../../../review-log.md#task-0003032) |

## Назначение файла

Собирает текущую вкладку сведений из четырёх partial и двух внутренних вкладок notes/lore. Полностью прочитаны 18 строк.

## Условия использования

PARTS.details MonsterSheet. Внешняя группа primary/details, внутренняя detailTabs из TABS и _prepareTabs ядра.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section details | 1 | Внешняя вкладка | tabs.details.cssClass/data-group=primary | Показ выбранной части |
| nav/detailTabs | 2–7 | Навигация notes/lore | data-action=tab, data-group=detailTabs | Итерирует подготовленные записи с id/label/cssClass |
| notes section | 9–12 | Статусы и заметки | detailTabs.notes | Подключает monster-status и monster-notes |
| lore section | 14–17 | Сведения и знания | detailTabs.lore | Подключает monster-info и monster-knowledge |

## Основные функции и методы

Программных функций и экспортов нет. Ниже описаны поля/условия разметки и их контракт с моделями и обработчиками; собственной записи документа файл не выполняет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| TABS.detailTabs/_prepareContext | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | контекст | tabs/details и detailTabs | 7 основных и 2 внутренних; initial notes |
| Четыре partial | [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs); [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs); [templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs); [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | Handlebars partial | Две секции | Все четыре отдельно описаны в этой порции |
| localize/core tab action | Foundry 14.367.0 ApplicationV2/Handlebars | UI | Навигация | Настоящий _prepareTabs; настоящий клик в браузере не выполнялся |
| CSS-селекторы | [styles/monster/details.css](../../../../../../../../../../styles/monster/details.css) | оформление | .tab.active.details/.tab:not(.active) | Прочитаны нужные селекторы; полный CSS вне порции |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | HBS details | PARTS.details | Путь/обращение сверены в исходнике |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Сам файл полей ввода не объявляет и данные не меняет. Вложенные partial наследуют текущий контекст целиком. Положение notes/lore и соответствие data-group сверены.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Сборка | 13 | Одна nav и по одному status/notes/info/knowledge | Четыре настоящих partial; UI-элементы редакторов заменены |

## Непроверенные участки и открытые вопросы

Остаются [U013-07](../../../../../../../cross-check-0002.md#u013-07): указанные там динамические границы и критерии дальнейшей сверки. Нынешняя проверка статическая; прежние изолированные опыты .025/.031/.032/.033 сохраняют даты и фасады. Полный браузерный лист, Document.create/update в БД, внешние модули и несколько клиентов не запускались.

## Связанные проблемы

[issue-00013](../../../../../../../../../issues/potential/issue-00013.md). Неверное enriched находится во вложенном monster-knowledge, не в механизме подключения частей.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003032) |

## Дополнительная сверка TASK-0003.049

2026-09-12, rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814. Исходный файл не изменён.

Полностью описан monster/details.css. Настоящие TABS/_prepareTabs и HBS при notes/lore дают три section.tab, из которых две active при открытой внешней details. Вложенная неактивная секция адресуется display:none/visibility:hidden. show*-флаги знаний независимо дают 0/3 h1. У monster-knowledge сохраняются margin-top10/flex-basis380/flex-grow1 старого monster-sheet.css. Передача enriched остаётся предметом issue-00013, оформление её не исправляет.

Карточки CSS: [styles/monster/details.css](../../../../../../styles/monster/details.css.md), [styles/monster-sheet.css](../../../../../../styles/monster-sheet.css.md), [styles/tab-background.css](../../../../../../styles/tab-background.css.md).

[Методика и результаты](../../../../../../../review-log.md#task-0003049). Соседний файл повторно в покрытие не включён; браузер и БД не запускались.

## Сквозная сверка TASK-0004.013

2026-09-14; rusbar-main, fc53038008e744b2e504d1b9c913045147c25a02. Исходник совпадает со срезом TASK-0001; изменено только описание.

PARTS.details Monster собирает четыре partial: notes содержит status+notes, lore — info+knowledge. Внешняя primary/details и внутренняя detailTabs имеют самостоятельную активность; initial notes. Прежние core tabs/HBS опыты не доказывают переключение/геометрию браузера; данные дочерних partial сверены отдельно. [U013-01](../../../../../../../cross-check-0002.md#u013-01), [U013-07](../../../../../../../cross-check-0002.md#u013-07).

Сопоставленные определения и потребители: [templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs](partials/monster-info.hbs.md), [module/data/actor/monsterData.js](../../../../../../module/data/actor/monsterData.js.md), [styles/monster/details.css](../../../../../../styles/monster/details.css.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004013) — TASK-0004.013; процессы [R013-17](../../../../../../../cross-check-0002.md#r013-17). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
