# templates/sheets/item/mount-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/mount-sheet.hbs](../../../../../../../templates/sheets/item/mount-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `1d29f681ffed1c46b9c05b0eff09935300c3bf7d` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.035](../../../../../../tasks/task-0003.035.md), 6 файлов, 384 логические строки |
| Запись перекрёстной сверки | [TASK-0003.035](../../../../review-log.md#task-0003035) |

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

Исполнены настоящие методы системы и модели Foundry 14.367.0 в изолированном Node 24.16.0. Коллекции документов, окна, запись и базовый Application — фасады; HBS — настоящий Handlebars 4.7.9, разбор HTML — parse5. Полный клиент, DOM-события, сервер, права реальной БД, сетевые гонки и сохранение мира не проверялись. Пути systems/TheWitcherTRPG сохранены как в исходниках; доступ по HTTP здесь не проверялся.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md). Собственной новой проблемы в числовом HP или строковых параметрах не установлено; inherited clickableImage отдельно описан.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003035) |
