# templates/sheets/investigation/partials/obstacle-display.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/investigation/partials/obstacle-display.hbs](../../../../../../../../templates/sheets/investigation/partials/obstacle-display.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../../review-log.md#task-0003023) |

## Актуализация N01–N08 — 14.3.1.00010

2026-09-16, dev, база aeb527c6e6402e8a5f940a2c3ad0020d7e5b35e4. Отображаемые placeholder/tooltip используют `WITCHER.Name`. Привязки name/data-field, классы действий, условия шаблона и введённые имена сохранены.

[Реализация и адресные проверки](../../../../../../../issues/closed/issue-00330.md#реализация-n01n08--143100010). Датированные разборы ниже сохраняют результаты прежних срезов.


## Назначение файла

Строка препятствия в таблице тайны: inline-поля, открытие редактора, GM-действия скрытия/удаления.

## Условия использования

Вставляется mystery-sheet.hbs внутри each obstacles. Явные параметры item/isGM/skills дополняют текущий контекст Item; поэтому selected=system.skillsUsed относится к текущему Item при штатном вызове.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| item.system.isHidden / isGM | 1–9 | Класс строки | item hidden-view для GM; item hidden-from-view для не-GM; item для видимых | Не исключает содержимое из HTML |
| data-item-id | 3, 5, 8 | Идентификатор embedded Item | {{item._id}} | Локальный ключ this.actor.items |
| name | inline-edit; data-field='name' | Редактируемое поле Item | value из item.name | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.type | inline-edit; data-field='system.type' | Редактируемое поле Item | value из item.system.type | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.dc | inline-edit; data-field='system.dc' | Редактируемое поле Item | value из item.system.dc | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.skillsUsed | inline-edit; data-field='system.skillsUsed' | Редактируемое поле Item | value из item.system.skillsUsed | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.successDamage | inline-edit; data-field='system.successDamage' | Редактируемое поле Item | value из item.system.successDamage | change → _onInlineEdit; skillsUsed получает массив multi-select |
| system.failDamage | inline-edit; data-field='system.failDamage' | Редактируемое поле Item | value из item.system.failDamage | change → _onInlineEdit; skillsUsed получает массив multi-select |
| selectOptions skills | 16 | Варианты навыков | selected=system.skillsUsed, valueAttr=name, labelAttr=label | Сохранённые значения выбираются в контексте each |
| editItem / deleteItem / hideItem | data-action | Действия строки | delete/hide только при isGM; edit без этого условия | Исполнение в WitcherMysterySheet |

## Основные функции и методы

Функций JavaScript нет. if выбирает класс строки, selectOptions выводит навыки, data-action передаёт события листу, inline-edit/data-field задают обработку change. Partial не создаёт и не удаляет Item самостоятельно.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherMysterySheet | [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | События/контекст | _onItemEdit/_onItemHide/_onItemDelete/_onInlineEdit | Все действия сверены с DEFAULT_OPTIONS.actions |
| ObstacleData | [module/data/investigation/obstacleData.js](../../../../../../../../module/data/investigation/obstacleData.js) | Поля Item | isHidden и inline-поля | Полный разбор модели |
| mystery-sheet.hbs | [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../../../templates/sheets/investigation/mystery-sheet.hbs) | Родительский контекст | each + hash item/isGM/skills | Группа 11 подтвердила selected без item. перед system |
| .hidden-view / .hidden-from-view | [styles/loot-sheet.css](../../../../../../../../styles/loot-sheet.css); [styles/witcher-styles.css](../../../../../../../../styles/witcher-styles.css) | CSS через импорт | Класс строки | hidden-view — silver; hidden-from-view — display:none; CSS подключён стилем системы |
| localize / selectOptions | Foundry 14.367.0, client/applications/handlebars.mjs:460–500; forms/fields.mjs:290–360 | Handlebars helpers | Подписи и <option> | Исполнены настоящие selectOptions/prepareSelectOptionGroups; запись DOM заменена HTML-фасадом |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Контекст skills | name/valueAttr/labelAttr | name — ключ передаваемого навыка; label — ключ перевода |
| label из CONFIG.WITCHER.skillMap | [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) | Локализация | Подписи полей | Динамические label берутся из skillMap; picklock/trapcraft — issue-00016 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../../../templates/sheets/investigation/mystery-sheet.hbs) | obstacle-display.hbs | Буквальный partial внутри each | 50 |
| [module/setup/handlebars.js](../../../../../../../../module/setup/handlebars.js) | obstacle-display.hbs | preloadHandlebarsTemplates | 63 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Все значения остаются в HTML даже у hidden-from-view. isGM управляет классом и двумя кнопками; owner/editable шаблон не читает. Базовый DocumentSheetV2 отдельно отключает ввод не-редактируемых документов; реальные права API не проверены. У строки и заголовка по 8 td. Действия rollClue здесь нет. id и _id — не UUID; getter Document.id ядра возвращает _id.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст и ID | Группы 11/16 | Штатный each передаёт правильные выбранные навыки; data-item-id совпал с документом | Фасады Items; id/_id ядра дополнительно проверены чтением |
| Видимость/GM/owner | Группа 12 | Скрытая строка присутствует с нужным классом; GM-кнопки зависят только от isGM | CSS в браузере и разрешения записи не исполнялись |
| События | Группы 13–15 | data-action/inline-edit соответствуют обработчикам; текстовые true/false/checked преобразуются обработчиком | Payload update перехвачен, сохранение не выполнено |

## Непроверенные участки и открытые вопросы

Все 28 строк прочитаны. Отдельный вызов partial вне each не найден; native multi-select/render — [U015-02](../../../../../cross-check-0002.md#u015-02); приведение inline и сохранение — [U015-03](../../../../../cross-check-0002.md#u015-03); CSS/полномочия — [U015-07](../../../../../cross-check-0002.md#u015-07); внешний consumer последствий — [U015-08](../../../../../cross-check-0002.md#u015-08).

## Связанные проблемы

[issue-00016](../../../../../../../issues/closed/issue-00016.md) — подписи picklock/trapcraft в общем словаре навыков; группа 17. [issue-00152](../../../../../../../issues/potential/issue-00152.md), [issue-00153](../../../../../../../issues/potential/issue-00153.md). Преждевременное завершение hide и преобразование текстовых значений находятся в листе; число столбцов совпадает.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003023) |

## Сквозная сверка TASK-0004.015

2026-09-14; rusbar-main, 7e0d53944f3089cd61667670377aa6770fabc8cf. Исходник совпадает со срезом TASK-0001; изменено только описание.

Partial вызывается внутри each obstacle и сохраняет текущий Item для selected=system.skillsUsed. item._id адресует документ так же, как id в соседней строке. edit/delete/hide/inline сходятся в MysterySheet; отдельного roll-action нет. Восемь td совпадают с восемью заголовками. isHidden меняет класс строки, GM условие — содержимое служебной ячейки. successDamage/failDamage передаются как редактируемый текст, не как исполнение Roll.

Сопоставленные определения и потребители: [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../module/actor/sheets/investigation/WitcherMysterySheet.js.md), [templates/sheets/investigation/mystery-sheet.hbs](../mystery-sheet.hbs.md), [module/data/investigation/obstacleData.js](../../../../module/data/investigation/obstacleData.js.md), [templates/sheets/investigation/obstacle-sheet.hbs](../obstacle-sheet.hbs.md), [styles/loot-sheet.css](../../../../styles/loot-sheet.css.md).

[Протокол и границы](../../../../../review-log.md#task-0004015) — TASK-0004.015; процессы [R015-03](../../../../../cross-check-0002.md#r015-03), [R015-05](../../../../../cross-check-0002.md#r015-05), [R015-06](../../../../../cross-check-0002.md#r015-06), [R015-07](../../../../../cross-check-0002.md#r015-07), [R015-14](../../../../../cross-check-0002.md#r015-14), [R015-15](../../../../../cross-check-0002.md#r015-15). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
