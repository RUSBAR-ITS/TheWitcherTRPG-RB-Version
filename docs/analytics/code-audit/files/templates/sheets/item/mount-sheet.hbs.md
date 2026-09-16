# templates/sheets/item/mount-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/mount-sheet.hbs](../../../../../../../templates/sheets/item/mount-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.035](../../../../../../tasks/task-0003.035.md), 6 файлов, 384 логические строки |
| Запись перекрёстной сверки | [TASK-0003.035](../../../../review-log.md#task-0003035) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Форма Item mount: общий заголовок, текстовое описание и таблица dex/control/speed/hp. Не содержит расчётов, кнопок броска или связи с отдельным Actor.

## Условия использования

WitcherMountSheet.PARTS.main. Подключает item-header, получает item из базового _prepareContext. В отличие от note-sheet в этой порции путь явно включён активным PARTS.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.{{item.type}}.scrollable | 1 | Корневой фрагмент | PARTS main | CSS класс mount |
| item-header | 2 | Общие поля/изображение/configureItem | partial | name/quantity/weight/cost/sourcebook и условный clickableImage |
| system.description | textarea:4 | Исходный текст описания | Форма Item | Обычное экранирование; не editor enriched HTML |
| system.dex / control / speed / hp | inputs14–17 | Три текстовых и одно числовое значение | name system.* | HP type=text data-dtype Number; нулевой HP выводится0 |
| WITCHER.Mount.Dex / ControlMod / Speed / Hp | labels8–11 | Четыре подписи | localize | Регистр Hp именно такой |

## Основные функции и методы

JS-функций нет. partial и localize — основные операции HBS; обычные {{item.system.*}} экранируют значение. Foundry FormDataExtended учитывает Number для HP, затем MountData очищает схему; dex/control/speed остаются String. Нет if по HP или вычислений speed.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherMountSheet | [module/item/sheets/WitcherMountSheet.js](../../../../../../../module/item/sheets/WitcherMountSheet.js) | PARTS consumer / выбор шаблона | Весь файл | 11 |
| WitcherItemSheet._prepareContext | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | контекст | item/data/config/showConfig | 45–60 |
| MountData | [module/data/item/mountData.js](../../../../../../../module/data/item/mountData.js) | пути модели | system.description/dex/control/speed/hp | 12 полей с CommonItemData |
| item-header | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | literal partial | 2 | Настоящий partial в тестах19–20 |
| WITCHER.Mount.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | локализация | 8–11 | Прямые ключи доступны после expandObject и fallback |
| FormDataExtended / DocumentSheetV2 | Foundry /opt/foundryvtt/client/applications/{ux/form-data-extended.mjs,api/document-sheet.mjs} | сбор и обработка формы | name/system.* + data-dtype | Настоящие обработчики данных с фасадом form; реальные DOM submit/БД не исполнялись |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherMountSheet.js](../../../../../../../module/item/sheets/WitcherMountSheet.js) | mount-sheet.hbs | PARTS.main11 | Активный шаблон Item mount |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Шаблон только вводит значения. В группе20 dex7→'7',control−2→'-2',speed'2d6',hp0 сохранили типы после FormDataExtended/_processFormData/MountData; quantity2 из header снова String в модели. textarea содержала экранированный '<p>Horse</p>'; тест form-фасада не использовался для доказательства сохранения textarea (он читает value-атрибут).

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Рендер/поля | 19–20 | Общий header с editImage, четыре поля, HP0; описание HTML экранировано | Не visual/браузер |
| Локализация | 25 | Все четыре ключа EN/RU существуют | Другие языки вне полного анализа |

## Непроверенные участки и открытые вопросы

Схема и связи header/main установлены; нативный submit/reset, textarea.value, FilePicker и реальные сохранённые типы — [U014-07](../../../../cross-check-0002.md#u014-07). Верховой бой не моделировался.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md). Собственной новой проблемы в числовом HP или строковых параметрах не установлено; inherited clickableImage отдельно описан.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003035) |

## Сквозная сверка TASK-0004.014

2026-09-14; rusbar-main, 8256dd3473347494fefb30524700fe7ca1daf75d. Исходник совпадает со срезом TASK-0001; изменено только описание.

Mount PARTS.main и inherited ItemSheet context сопоставлены с общим header и пятью полями description/dex/control/speed/hp. HP использует Number dtype, dex/control/speed текстовые; схема и UI не определяют автоматику верхового боя. В отличие от изображения Loot, общий header содержит data-action=editImage.

Сопоставленные определения и потребители: [module/data/item/mountData.js](../../../module/data/item/mountData.js.md), [module/item/sheets/WitcherMountSheet.js](../../../module/item/sheets/WitcherMountSheet.js.md), [module/data/item/commonItemData.js](../../../module/data/item/commonItemData.js.md), [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js.md), [templates/partials/item-header.hbs](../../partials/item-header.hbs.md).

[Протокол и границы](../../../../review-log.md#task-0004014) — TASK-0004.014; процессы [R014-07](../../../../cross-check-0002.md#r014-07). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
