# templates/sheets/item/hex-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/hex-sheet.hbs](../../../../../../../templates/sheets/item/hex-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

## Назначение файла

Форма Item hex: имя/изображение/книга, STA, опасность, описание и условие снятия порчи.

## Условия использования

PARTS.main WitcherHexSheet. Контекст — item, selects.danger, showConfig. Самостоятельный заголовок без включения spell-header.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| name/sourcebook | input4, 38 | Имя документа и книга | name=name / system.sourcebook | Обычная форма |
| configureItem | a data-action6 | Открытие общей конфигурации | Только showConfig | Действие базового WitcherItemSheet |
| img[data-edit=img]; clickableImage | 11–22 | Картинка и условный checkbox | Settings + isGM; checkboxname=system.clickableImage | У img отсутствует data-action=editImage в обеих ветвях |
| stamina/danger | 50–53 | Стоимость и опасность | system.stamina=text / system.danger=select | selectOptions selects.danger; значения Low/Medium/High |
| effect/liftRequirement | textarea60, 64 | Описание и требование снятия | system.* | Простой текст |

## Основные функции и методы

Собственных функций нет. if/and/or/includes/getSetting/window управляют картинкой; selectOptions строит опасность; configureItem обрабатывается классом листа.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| eq/and/or/includes/getSetting/window | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные helpers | Условия, CSV типов изображений и доступ к game.user | Определения 94–128 прочитаны |
| clickableImageItemTypes/clickableImageCheckboxForGMOnly | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | Настройки через helpers | Условия checkbox картинки | default valuable / true |
| localize, checked, selectOptions; if/unless/each | Foundry14.367.0, client/applications/handlebars.mjs; Handlebars4.7.9 | Helpers/шаблонизация | Поля и условия | HBS исполнялся; UI helpers заменены по прочитанному контракту |
| Ключи WITCHER.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи и title | Literal-ключи проверены; динамические перечислены отдельно |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Базовый контекст/форма | item, config, showConfig; submitOnChange/configureItem | _prepareContext/DEFAULT_OPTIONS |
| WitcherHexSheet | [module/item/sheets/WitcherHexSheet.js](../../../../../../../module/item/sheets/WitcherHexSheet.js) | Загрузчик/контекст | selects.danger | PARTS/main/createSelects |
| HexData | [module/data/item/hexData.js](../../../../../../../module/data/item/hexData.js) | Поля | stamina: Number; остальные String | Реальная модель в Node |
| DocumentSheetV2/ApplicationV2 | Foundry14.367.0, client/applications/api/document-sheet.mjs: 61, 242, 383; application.mjs: 1920–1951 | Маршрут изображений | editImage требует action; data-edit используется также для disabled CSS | Ядро прочитано, FilePicker не запускался |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherHexSheet.js](../../../../../../../module/item/sheets/WitcherHexSheet.js) | Этот HBS | PARTS.main | 6 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Только представление и names формы. system.clickableImage отсутствует в HexData и CommonItemData. data-edit не является data-action текущего ApplicationV2; самостоятельного обработчика картинки в WitcherHexSheet нет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Форма | Группы 12, 15 | Medium selected; поля STA/effect/liftRequirement существуют; checkbox картинки появляется по настройкам | Синтетический контекст/настоящая модель |
| Подписи и картинка | JSON en/ru + исходный HBS и ядро | DangerLow/Medium/High не найдены; img без editImage action | В браузере отказ FilePicker не воспроизводился |

## Непроверенные участки и открытые вопросы

Все 66 строк прочитаны. Фактическая запись/перерисовка, права и действие порчи не проверялись.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00136](../../../../../../issues/potential/issue-00136.md), [issue-00137](../../../../../../issues/potential/issue-00137.md). 63 — необъявленный checkbox; 136 — отсутствующий маршрут редактирования изображения; 137 — опасность.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |
