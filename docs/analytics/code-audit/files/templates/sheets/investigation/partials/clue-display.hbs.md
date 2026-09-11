# templates/sheets/investigation/partials/clue-display.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/investigation/partials/clue-display.hbs](../../../../../../../../templates/sheets/investigation/partials/clue-display.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../../review-log.md#task-0003023) |

## Назначение файла

Строка улики в таблице тайны: inline-поля, открытие редактора, GM-действия и бросок навыка.

## Условия использования

Вставляется mystery-sheet.hbs внутри each clues. Явные параметры item/isGM/skills дополняют текущий контекст Item; поэтому selected=system.skillsUsed относится к текущему Item при штатном вызове.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| item.system.isHidden / isGM | 1–9 | Класс строки | item hidden-view для GM; item hidden-from-view для не-GM; item для видимых | Не исключает содержимое из HTML |
| data-item-id | 3, 5, 8 | Идентификатор embedded Item | {{item.id}} | Локальный ключ this.actor.items |
| name | inline-edit; data-field='name' | Редактируемое поле Item | value из item.name | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.type | inline-edit; data-field='system.type' | Редактируемое поле Item | value из item.system.type | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.dc | inline-edit; data-field='system.dc' | Редактируемое поле Item | value из item.system.dc | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.skillsUsed | inline-edit; data-field='system.skillsUsed' | Редактируемое поле Item | value из item.system.skillsUsed | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.timeIncrement | inline-edit; data-field='system.timeIncrement' | Редактируемое поле Item | value из item.system.timeIncrement | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.timeBonus | inline-edit; data-field='system.timeBonus' | Редактируемое поле Item | value из item.system.timeBonus | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.damage | inline-edit; data-field='system.damage' | Редактируемое поле Item | value из item.system.damage | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.obfuscation | inline-edit; data-field='system.obfuscation' | Редактируемое поле Item | value из item.system.obfuscation | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.penalty | inline-edit; data-field='system.penalty' | Редактируемое поле Item | value из item.system.penalty | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.focusDamage | inline-edit; data-field='system.focusDamage' | Редактируемое поле Item | value из item.system.focusDamage | change → _onInlineEdit; skillsUsed получает массив multi-select |
| selectOptions skills | 16 | Варианты навыков | selected=system.skillsUsed, valueAttr=name, labelAttr=label | Сохранённые значения выбираются в контексте each |
| editItem / deleteItem / hideItem / rollClue | data-action | Действия строки | delete/hide только при isGM; edit/roll без этого условия | Исполнение в WitcherMysterySheet |

## Основные функции и методы

Функций JavaScript нет. if выбирает класс строки, selectOptions выводит навыки, data-action передаёт события листу, inline-edit/data-field задают обработку change. Partial не создаёт и не удаляет Item самостоятельно.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherMysterySheet | [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | События/контекст | _onItemEdit/_onItemHide/_onItemDelete/_onInlineEdit/_onRollClue | Все действия сверены с DEFAULT_OPTIONS.actions |
| ClueData | [module/data/investigation/clueData.js](../../../../../../../../module/data/investigation/clueData.js) | Поля Item | isHidden и inline-поля | Полный разбор модели |
| mystery-sheet.hbs | [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../../../templates/sheets/investigation/mystery-sheet.hbs) | Родительский контекст | each + hash item/isGM/skills | Группа 11 подтвердила selected без item. перед system |
| .hidden-view / .hidden-from-view | [styles/loot-sheet.css](../../../../../../../../styles/loot-sheet.css); [styles/witcher-styles.css](../../../../../../../../styles/witcher-styles.css) | CSS через импорт | Класс строки | hidden-view — silver; hidden-from-view — display:none; CSS подключён стилем системы |
| localize / selectOptions | Foundry 14.367.0, client/applications/handlebars.mjs:460–500; forms/fields.mjs:290–360 | Handlebars helpers | Подписи и <option> | Исполнены настоящие selectOptions/prepareSelectOptionGroups; запись DOM заменена HTML-фасадом |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Контекст skills | name/valueAttr/labelAttr | name — ключ передаваемого навыка; label — ключ перевода |
| label из CONFIG.WITCHER.skillMap | [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) | Локализация | Подписи полей | Динамические label берутся из skillMap; picklock/trapcraft — issue-00016 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../../../templates/sheets/investigation/mystery-sheet.hbs) | clue-display.hbs | Буквальный partial внутри each | 32 |
| [module/setup/handlebars.js](../../../../../../../../module/setup/handlebars.js) | clue-display.hbs | preloadHandlebarsTemplates | 62 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Все значения остаются в HTML даже у hidden-from-view. isGM управляет классом и двумя кнопками; owner/editable шаблон не читает. Базовый DocumentSheetV2 отдельно отключает ввод не-редактируемых документов; реальные права API не проверены. У строки 13 td, у заголовка основной формы 12. Бросок расположен в последней ячейке. id и _id — не UUID; getter Document.id ядра возвращает _id.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст и ID | Группы 11/16 | Штатный each передаёт правильные выбранные навыки; data-item-id совпал с документом | Фасады Items; id/_id ядра дополнительно проверены чтением |
| Видимость/GM/owner | Группа 12 | Скрытая строка присутствует с нужным классом; GM-кнопки зависят только от isGM | CSS в браузере и разрешения записи не исполнялись |
| События | Группы 13–15 | data-action/inline-edit соответствуют обработчикам; текстовые true/false/checked преобразуются обработчиком | Payload update перехвачен, сохранение не выполнено |

## Непроверенные участки и открытые вопросы

Все 37 строк прочитаны. Отдельный вызов partial вне each требует собственного system-контекста; такого потребителя в module/templates не найдено. Скрытие по CSS не описывается как разграничение доступа к данным.

## Связанные проблемы

[issue-00016](../../../../../../../issues/potential/issue-00016.md) — подписи picklock/trapcraft в общем словаре навыков; группа 17. [issue-00148](../../../../../../../issues/potential/issue-00148.md), [issue-00149](../../../../../../../issues/potential/issue-00149.md), [issue-00150](../../../../../../../issues/potential/issue-00150.md), [issue-00151](../../../../../../../issues/potential/issue-00151.md), [issue-00152](../../../../../../../issues/potential/issue-00152.md), [issue-00153](../../../../../../../issues/potential/issue-00153.md), [issue-00154](../../../../../../../issues/potential/issue-00154.md). Проблемы находятся в обработчиках броска/редактирования и несовпадении числа столбцов. Ошибка selected из-за отсутствия item. при штатном вызове не обнаружена.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003023) |
