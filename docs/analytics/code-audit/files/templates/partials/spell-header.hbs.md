# templates/partials/spell-header.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/spell-header.hbs](../../../../../../templates/partials/spell-header.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../review-log.md#task-0003021) |

## Назначение файла

Заголовок редактора Item spell: имя, конфигурация, изображение, класс, уровень, источник и книга.

## Условия использования

Предварительно загружается loadHandlebarsTemplates из setup/handlebars; буквально включён в spell-sheet.hbs. Контекст тот же, что у WitcherSpellSheet.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| name/configureItem | 3–5 | Имя Item и кнопка конфигурации | name; data-action=configureItem при showConfig | Обработчик базового листа |
| img/editImage/clickableImage | 10–21 | Изображение и необъявленный системный checkbox | data-action=editImage/data-edit=img; settings и isGM | Обе ветви изображения содержат editImage |
| class | 30–32 | Класс магии | system.class; id=profession-select | selects.class; ID не означает модель профессии |
| level | 40–49 | Уровень обычной магии либо дара | system.level | Для MagicalGift список minor gift/major gift; иначе novice/journeyman/master |
| source | 53–71 | Стихия либо традиция | system.source | Spells/Witcher→sourceElements; Invocations→sourceClass; для MagicalGift нет поля |
| sourcebook | 79 | Книга | system.sourcebook | Общее String-поле |

## Основные функции и методы

Собственных JS-функций нет. eq/or/and/includes/getSetting/window выбирают ветви; selectOptions выводит словари createSelects. Элементы editImage и configureItem используют разные унаследованные действия.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| eq/and/or/includes/getSetting/window | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Системные helpers | Условия, CSV типов изображений и доступ к game.user | Определения 94–128 прочитаны |
| clickableImageItemTypes/clickableImageCheckboxForGMOnly | [module/setup/settings.js](../../../../../../module/setup/settings.js) | Настройки через helpers | Условия checkbox картинки | default valuable / true |
| localize, checked, selectOptions; if/unless/each | Foundry14.367.0, client/applications/handlebars.mjs; Handlebars4.7.9 | Helpers/шаблонизация | Поля и условия | HBS исполнялся; UI helpers заменены по прочитанному контракту |
| Ключи WITCHER.* | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | Локализация | Подписи и title | Literal-ключи проверены; динамические перечислены отдельно |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../module/item/sheets/WitcherItemSheet.js) | Базовый контекст/форма | item, config, showConfig; submitOnChange/configureItem | _prepareContext/DEFAULT_OPTIONS |
| WitcherSpellSheet | [module/item/sheets/WitcherSpellSheet.js](../../../../../../module/item/sheets/WitcherSpellSheet.js) | Контекст | selects.class/levelSpell/levelMagicalGift/sourceElements/sourceClass | createSelects прочитан |
| SpellData; CommonItemData | [module/data/item/spellData.js](../../../../../../module/data/item/spellData.js); [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js) | Схемы | class/level/source/sourcebook | Все поля кроме clickableImage объявлены |
| DocumentSheetV2.editImage | Foundry14.367.0 client/applications/api/document-sheet.mjs | Унаследованное действие | Выбор картинки Item | Action есть в обеих ветвях; FilePicker не открывался |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Этот partial | Предзагрузка шаблона | 51 |
| [templates/sheets/item/spell-sheet.hbs](../../../../../../templates/sheets/item/spell-sheet.hbs) | Этот partial | Буквальное включение | 2 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Заголовок не нормализует классы/источники и не мигрирует данные. При пустой модели select может визуально показывать первый option, но шаблон не присваивает Spells в модель; это не защита от TypeError getUsedSkill. Скрытые source/level значения здесь не очищаются. clickableImage относится к отдельной известной проблеме схемы.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Ветви классов/STA | Группа 11, настоящий partial в spell-sheet | Для 4 классов выбраны соответствующие поля уровня/источника | Только HTML, без browser change/submit |
| Картинка/словарь | Группа 15 и чтение ядра | editImage присутствует; Water хранится с заглавной буквы, но label sourceElements — water | Динамический ключ чата проверен отдельно |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Несколько окон/id, реальные FilePicker/submit и CSS/изображения не проверялись. Остаток: [U009-01](../../../cross-check-0002.md#u009-01), [U009-07](../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00063](../../../../../issues/potential/issue-00063.md), [issue-00064](../../../../../issues/potential/issue-00064.md), [issue-00137](../../../../../issues/closed/issue-00137.md). 63 — checkbox вне схемы; 64 — пустая модель не исправляется отображением select; 137 — source Water в потребителе.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003021) |

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

Partial подключён spell-sheet и предзагрузкой; общий header используется магическим Item, а не Actor-списком. Оба img имеют editImage, в отличие от Hex/Ritual. Условия class управляют level/source/domain, поля сверены с selects модели/листа и en/ru.

Сопоставленные определения и потребители: [module/setup/handlebars.js](../../module/setup/handlebars.js.md), [module/setup/settings.js](../../module/setup/settings.js.md), [lang/en.json](../../lang/en.json.md), [lang/ru.json](../../lang/ru.json.md), [module/item/sheets/WitcherItemSheet.js](../../module/item/sheets/WitcherItemSheet.js.md), [module/item/sheets/WitcherSpellSheet.js](../../module/item/sheets/WitcherSpellSheet.js.md), [module/data/item/spellData.js](../../module/data/item/spellData.js.md), [module/data/item/commonItemData.js](../../module/data/item/commonItemData.js.md), [templates/sheets/item/spell-sheet.hbs](../sheets/item/spell-sheet.hbs.md).

[Протокол и границы](../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-03](../../../cross-check-0002.md#r009-03). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
