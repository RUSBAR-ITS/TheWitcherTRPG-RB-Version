# templates/partials/character/substances.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/character/substances.hbs](../../../../../../../templates/partials/character/substances.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.034](../../../../../../tasks/task-0003.034.md), 5 файлов, 251 логическая строка |
| Запись перекрёстной сверки | [TASK-0003.034](../../../../review-log.md#task-0003034) |

## Назначение файла

Текущая панель девяти алхимических веществ: иконки, суммарные количества и раскрываемые таблицы компонентов.

## Условия использования

Включена безусловно во вкладку инвентаря персонажа templates/sheets/actor/tabs/tab-inventory.hbs:212, выбранную PARTS.inventory. Также предзагружается setup/handlebars:13. Читает отдельные system.pannels.*IsOpen, *Count и substances*; alchemyComponentsList не используется.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| .substances-section / .substances-menu / .substances-item | 1–78 | Панель девяти групп | Вложенная разметка инвентаря | Есть всегда, даже при пустом запасе |
| input[type=image].item-substance-display.substance | 8–76 | Открыть/закрыть группу | data-subtype, src, data-tooltip | Нет name/data-action; click обрабатывает itemMixin, preventDefault отменяет обычное действие image-input |
| sub-open / system.pannels.<key>IsOpen | 7–77 | Состояние кнопки группы | Условный CSS-класс | Тот же флаг управляет таблицей |
| substances<Label> / <key>Count | 13–104 | Массивы и суммарные количества | Контекст _prepareSubstances | Суммы отображаются в span, не редактируются здесь |
| tab-inventory-components partial | 80,83,86,89,92,95,98,101,104 | Таблица открытой группы | components, itemType='component', subtype, header, hasQuantity=true | Девять обращений к одному HBS; тип конкретного компонента остаётся в вложенном Item |

## Основные функции и методы

Программных функций нет. Девять if выбирают класс sub-open, ещё девять if — таблицы. localize переводит заголовок Substances и девять имён. У vermilion между закрывающей кавычкой class и type нет пробела; parse5 всё равно прочитал type=image и нужные классы. Само это форматирование не объявлено функциональной проблемой.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| _prepareSubstances / _prepareContext | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | контекст | 220–237: девять массивов/сумм | Полный текущий контекст отрендерен на пустом и смешанном наборе |
| getSubstance | [module/actor/mixins/craftingMixin.js](../../../../../../../module/actor/mixins/craftingMixin.js) | косвенный поиск | Поиск каждого массива | Stored исключены, quantity0 остаётся |
| Array.prototype.sum | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | суммирование у producer | Number(system.quantity ?? 0) | Пустая панель: девять нулей; vitriol 1+2=3 |
| pannels; CommonActorData | [module/data/actor/templates/character/pannelsData.js](../../../../../../../module/data/actor/templates/character/pannelsData.js); [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js) | схема флагов | vitriolIsOpen…fulgurIsOpen | Девять BooleanField с initialfalse; updateSource открыл vitriol |
| _onSubstanceDisplay / itemListener | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | событие | 284–291,334: .item-substance-display | closest('.substance').dataset.subtype → system.pannels.<key>IsOpen; preventDefault |
| tab-inventory-components.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | partial | 80–104 | Таблица Item, inline quantity, chat/details; subtype передаётся дальше |
| inventory-items-summary.hbs | [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | косвенный partial | Через components:3 | Не выводит data-subtype на кнопке add-item, хотя получает subtype |
| Переводы | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | localize | Substances и девять имён | Десять уникальных ключей этого HBS доступны в en/ru |
| Иконки | assets/images/{vitriol,rebis,aether,quebrith,hydragenum,vermilion,sol,caelum,fulgur}.png — вне анализа | src | 11–75 | Все девять путей существуют |
| .substances-menu / .substances-item / .sub-open / .substance-img | [styles/substances.css](../../../../../../../styles/substances.css) | CSS | Панель, раскрытие, иконки | Файл подключён styles/witcher-styles.css; внешний вид не проверен |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | Весь partial | 212: безусловное включение | Текущий PARTS.inventory WitcherCharacterSheet |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Путь HBS | preloadHandlebarsTemplates:13 | Предзагрузка отдельно от UI-вызова |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Фиксированные группы: vitriol, rebis, aether, quebrith, hydragenum, vermilion, sol, caelum, fulgur. Для каждой key используются system.pannels.<key>IsOpen, <key>Count, массив substances<Label>, иконка <key>.png и Inventory.<Label>. Открытая группа без запасов всё равно выводит пустую таблицу с кнопкой добавления. Указанный subtype доходит до общего summary-контекста, но не до DOM-кнопки — прежняя issue-00173.

Шаблон только читает данные; click отдельно меняет флаг Actor, inline-edit/создание/чат принадлежат вложенным обработчикам Item. Смена флага не изменяет количество веществ. Вложенный input quantity имеет data-field, поэтому относится к Item, а не обычному Actor-form.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пустая/полная панель | Группа 06 | 9 иконок/нулей, 0 таблиц; при всех флагах — 9 таблиц, 10 компонентов, stored не отображён | Полный HBS и два настоящих partial, DOM разобран parse5 |
| Кнопки | Группа 07 | preventDefault; update витриола; add-item потерял subtype и создал обычный component | Item.create заменён перехватом |
| Переводы/пути | Группы 05–06,21 | 10 ключей en/ru, 9 существующих PNG | HTTP и CSS-отрисовка не проверены |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Проверки выполнены в Node 24.16.0 с установленным кодом Foundry 14.367.0. Использованы реальные модели и методы системы; Application/Document-оболочки, DOM, UUID-резолвер, запись документов и чат заменены фасадами. Мир, браузер, HTTP и БД не запускались. Точные границы и сценарии приведены в журнале .034; чтение соседних определений не засчитывается как их новый полный разбор.

## Связанные проблемы

[issue-00173](../../../../../../issues/potential/issue-00173.md). Дополнен существующий issue о подтипе. Разные способы поиска в ремесле и панели описаны без изменения поведения.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003034) |
