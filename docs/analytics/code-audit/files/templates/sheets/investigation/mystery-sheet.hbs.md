# templates/sheets/investigation/mystery-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../../templates/sheets/investigation/mystery-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.023](../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../review-log.md#task-0003023) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Актуализация issue-00330 — 2026-09-16

Версия 14.3.1.00007, dev, база 031fbb8691ad32ab01fad43253c8736071bb2f8b. [Реализация и проверки](../../../../../../issues/closed/issue-00330.md#реализация-и-проверки--143100007). Ниже сохранён исторический разбор: его сообщения об исправленных подписях/пропусках относятся к прежнему коду. Механики, технические значения и компедиумы этой правкой не изменены.

Изменённые строки текущего файла:

- `2`: `<h1><input name="name" type="text" value="{{actor.name}}" placeholder="{{localize 'WITCHER.Name'}}" /></h1>`
- `3`: `<label>{{localize "WITCHER.Investigation.goal"}}</label>`
- `6`: `<label>{{localize "WITCHER.Investigation.difficulty"}}</label>`
- `9`: `<label>{{localize "WITCHER.Investigation.complexity"}}</label>`


## Назначение файла

Основная часть листа тайны: имя/цель/сложность и две таблицы embedded Items с добавлением улик и препятствий.

## Условия использования

WitcherMysterySheet.PARTS.header загружает файл; module/setup/handlebars.js заранее загружает его и оба partial. Внутри each передаются item, isGM и skills. В файле собственный <form>; внешняя форма наследуется от DocumentSheetV2.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| form / name | 1–2 | Корневая форма и имя Actor | name='name' | Ввод через механизм формы листа |
| system.goal / system.complexity.difficulty / system.complexity.complexity | 4, 7, 10 | Цель, метка и число сложности | Значения из actor.system | Поле type=number только для complexity |
| data-action addItem / data-itemType | 14–15, 35–36 | Добавление embedded Item | clue / obstacle | HTML нормализует data-itemType в data-itemtype; обработчик читает dataset.itemtype |
| each clues as \|item id\| | 31–33 | Строки улик | clue-display.hbs | item=item isGM=../isGM skills=../skills |
| each obstacles as \|item id\| | 49–51 | Строки препятствий | obstacle-display.hbs | Те же параметры partial |
| Заголовки таблиц | 16–30, 38–48 | 12 ячеек улик / 8 препятствий | Локализованные подписи | Строка улики имеет 13 ячеек; строки препятствий совпадают |
| Goal / Difficulty / Complexity / Name | 2–9 | Английские буквальные подписи/placeholder | Без localize | Не меняются при смене языка |

## Основные функции и методы

Программных методов нет. Действия: ввод именных полей формы; addItem по data-action; each вставляет partial для каждой записи. Inline-редактирование Item находится внутри partial и не является прямой записью system Actor.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherMysterySheet | [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | Поставщик контекста/обработчик | actor,clues,obstacles,isGM,skills; addItem | _prepareContext и DEFAULT_OPTIONS.actions |
| MysteryActorData / complexity | [module/data/investigation/mysteryActorData.js](../../../../../../../module/data/investigation/mysteryActorData.js); [module/data/investigation/templates/complexityData.js](../../../../../../../module/data/investigation/templates/complexityData.js) | Контракт полей | Три system-пути | Схемы сверены |
| clue-display.hbs | [templates/sheets/investigation/partials/clue-display.hbs](../../../../../../../templates/sheets/investigation/partials/clue-display.hbs) | Буквальный partial | 32 | Внутри each контекст — текущий Item |
| obstacle-display.hbs | [templates/sheets/investigation/partials/obstacle-display.hbs](../../../../../../../templates/sheets/investigation/partials/obstacle-display.hbs) | Буквальный partial | 50 | Внутри each текущий Item |
| localize / selectOptions | Foundry 14.367.0, client/applications/handlebars.mjs:460–500; forms/fields.mjs:290–360 | Handlebars helpers | Подписи и <option> | Исполнены настоящие selectOptions/prepareSelectOptionGroups; запись DOM заменена HTML-фасадом |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Контекст skills | name/valueAttr/labelAttr | name — ключ передаваемого навыка; label — ключ перевода |
| WITCHER.Investigation.clues; WITCHER.Name; WITCHER.Type; WITCHER.DC; WITCHER.Investigation.skillsUsed; WITCHER.Investigation.timeIncrement; WITCHER.Investigation.timeBonus; WITCHER.Investigation.damage; WITCHER.Investigation.obfuscation; WITCHER.Investigation.penalty; WITCHER.Investigation.focusDamage; WITCHER.Investigation.obstacles; WITCHER.Investigation.successDamage; WITCHER.Investigation.failDamage | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи полей | Статические ключи этого шаблона найдены в en/ru; динамические label picklock/trapcraft — issue-00016 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | mystery-sheet.hbs | PARTS.header | 29 |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | mystery-sheet.hbs | preloadHandlebarsTemplates | 61 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Вход — Actor и массивы документов. Пустые списки оставляют два заголовка таблиц и кнопки добавления. HBS не фильтрует Items по isHidden/owner; partial выбирает классы по isHidden/isGM. Шаблон не вычисляет complexity/difficulty и не уменьшает её после броска. Кнопки добавления не обёрнуты в проверку GM; фактическое разрешение создания остаётся у Document API.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пустая/заполненная тайна | Группы 11/12 | 0 записей → 2 строки заголовков; 2 улики+1 препятствие → 5 строк; скрытые данные присутствуют в HTML | parse5 анализировал HTML, браузерный CSS/доступ не исполнялись |
| Поля и атрибуты | Группы 11/16 | Все system-пути существуют; data-itemtype распознан; выбранные навыки сохранены через partial | Живой submit/HTMLFormElement не проверен |
| Столбцы и подписи | Группы 11/16 | Улики: заголовок 12, строка 13; препятствия 8/8; три английские подписи обходят localize | Реальное выравнивание на экране не оценивалось |

## Непроверенные участки и открытые вопросы

Все 55 строк прочитаны. Реальное внешнее/вложенное form, submit и повторный render — [U015-02](../../../../cross-check-0002.md#u015-02); видимые колонки/права/en/ru — [U015-07](../../../../cross-check-0002.md#u015-07); сохранение и внешнее применение complexity — [U015-03](../../../../cross-check-0002.md#u015-03)/[U015-08](../../../../cross-check-0002.md#u015-08). Структура HBS не заменяет браузерную проверку.

## Связанные проблемы

[issue-00016](../../../../../../issues/closed/issue-00016.md) — подписи picklock/trapcraft в общем словаре навыков; группа 17. [issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00154](../../../../../../issues/potential/issue-00154.md), [issue-00155](../../../../../../issues/closed/issue-00155.md). Тип тайны, несоответствие столбцов улик и непереводимые подписи.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003023) |

## Сквозная сверка TASK-0004.015

2026-09-14; rusbar-main, 7e0d53944f3089cd61667670377aa6770fabc8cf. Исходник совпадает со срезом TASK-0001; изменено только описание.

Основная форма читает живой actor.system для goal/complexity, создаёт clue/obstacle через actions и передаёт каждую строку в соответствующий partial. isGM/skills передаются из родительского контекста, текущий Item сохраняется. Улик заголовок содержит 12 ячеек против 13 в строке с броском; препятствий 8/8. Goal/Difficulty/Complexity — буквальные английские подписи без localize; начальное Easy задаёт модель. Форма не считает успех/прогресс тайны.

Сопоставленные определения и потребители: [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../module/actor/sheets/investigation/WitcherMysterySheet.js.md), [module/data/investigation/mysteryActorData.js](../../../module/data/investigation/mysteryActorData.js.md), [module/data/investigation/templates/complexityData.js](../../../module/data/investigation/templates/complexityData.js.md), [templates/sheets/investigation/partials/clue-display.hbs](partials/clue-display.hbs.md), [templates/sheets/investigation/partials/obstacle-display.hbs](partials/obstacle-display.hbs.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md).

[Протокол и границы](../../../../review-log.md#task-0004015) — TASK-0004.015; процессы [R015-03](../../../../cross-check-0002.md#r015-03), [R015-04](../../../../cross-check-0002.md#r015-04), [R015-05](../../../../cross-check-0002.md#r015-05), [R015-14](../../../../cross-check-0002.md#r015-14), [R015-15](../../../../cross-check-0002.md#r015-15), [R015-16](../../../../cross-check-0002.md#r015-16). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
