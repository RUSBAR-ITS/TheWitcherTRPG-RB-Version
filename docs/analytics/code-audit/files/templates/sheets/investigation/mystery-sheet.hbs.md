# templates/sheets/investigation/mystery-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../../templates/sheets/investigation/mystery-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../review-log.md#task-0003023) |

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

Все 55 строк прочитаны. Вложенность form указана как факт структуры; отказ сохранения из одного этого факта не утверждается. Реальное отображение и обработка прав в браузере не проверялись.

## Связанные проблемы

[issue-00016](../../../../../../issues/potential/issue-00016.md) — подписи picklock/trapcraft в общем словаре навыков; группа 17. [issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00154](../../../../../../issues/potential/issue-00154.md), [issue-00155](../../../../../../issues/potential/issue-00155.md). Тип тайны, несоответствие столбцов улик и непереводимые подписи.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003023) |
