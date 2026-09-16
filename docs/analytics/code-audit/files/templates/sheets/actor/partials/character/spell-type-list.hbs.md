# templates/sheets/actor/partials/character/spell-type-list.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.039](../../../../../../../../tasks/task-0003.039.md), 6 файлов, 870 логических строк |
| Запись перекрёстной сверки | [TASK-0003.039](../../../../../../review-log.md#task-0003039) |

Актуализация [issue-00001](../../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Актуализация issue-00330 — 2026-09-16

Версия 14.3.1.00007, dev, база 031fbb8691ad32ab01fad43253c8736071bb2f8b. [Реализация и проверки](../../../../../../../../issues/closed/issue-00330.md#реализация-и-проверки--143100007). Ниже сохранён исторический разбор: его сообщения об исправленных подписях/пропусках относятся к прежнему коду. Механики, технические значения и компедиумы этой правкой не изменены.

Изменённые строки текущего файла:

- `38`: `{{#if (eq spell.system.source "Water")}}{{localize "WITCHER.Spell.water"}}{{else}}{{localize (concat "WITCHER.Spell." spell.system.source)}}{{/if}}`
- `50`: `{{ localize (concat "WITCHER.Spell.danger" spell.system.danger) }}`


## Назначение файла

Универсальный список spell/hex/ritual: раскрываемые details, название с применением, STA, описание, теги и альтернативные компоненты ритуала. Общий summary даёт добавление Item.

## Условия использования

Двенадцать включений из tab-magic.hbs; предварительная загрузка из setup/handlebars.js. Получает массив spells и header/itemType; имя переменной spell не ограничивает тип Item. Поиск не обнаружил самостоятельного подключения вне общей вкладки.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| details / summary | 1–5 | Локальное раскрытие списка | open по умолчанию; inventory-items-summary partial | Панели system.pannels не используются |
| li.item.list-item.draggable | 8 | Строка Item | data-item-id=spell.id | Носитель контекстного меню, применения, описания и перетаскивания |
| item-display-info / spell-roll / item-chat | 10–33 | Три действия строки | itemListener; внешние методы | Развёртывание описания, useItem, отправка описания в чат |
| item-info и item-tags | 35–173 | Описание/теги/материалы | Нативный HBS each/if | Содержимое Item экранировано обычными скобками |
| stored-item | 120–164 | Альтернативный компонент | data-item-id=component.name | В RitualData объект имеет item/quantity/img, имя находится в item.name |

## Основные функции и методы

Функций JavaScript нет. each по spells и alternateRitualComponents; if по полям Item. localize/concat формируют подписи. Встроенное details раскрывается браузером; собственных DOM-listeners шаблон не определяет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| tab-magic.hbs | [templates/partials/character/tab-magic.hbs](../../../../../../../../../templates/partials/character/tab-magic.hbs) | Источник контекста | spells/header/itemType/spellType | Два показа каждой группы |
| inventory-items-summary.hbs | [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | Literal partial:3 | header,itemType,subtype; spellType наследуется | Кнопка add-item, data-itemType/data-spellType |
| _prepareSpells | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Подготовка массивов | Группы из getList; все Item включая не имеющие learned | Не фильтрует learned |
| itemListener / _onItemRoll / _onItemDisplayInfo / _onItemMessage | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | DOM selectors | spell-roll,item-display-info,item-chat,add-item | Item ID из ближайшей .item/.list-item; _onItemRoll не ждёт useItem |
| editItem / deleteItem / itemContextMenu | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Контекстное меню .item | Редактирование через onClick и Item.sheet.render | Отдельных item-edit/item-delete кнопок в текущей строке нет; конфигурация меню не означает проверенный браузерный callback удаления |
| SpellData/HexData/RitualData | [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js); [module/data/item/hexData.js](../../../../../../../../../module/data/item/hexData.js); [module/data/item/ritualData.js](../../../../../../../../../module/data/item/ritualData.js) | Данные Item | stamina,staminaIsVar, source/level/danger, effect/sideEffect/liftRequirement, components/alternateRitualComponents | Имена/значения зависят от типа; ritual.prepareDerivedData разрешает UUID |
| useItem / castSpell | [module/actor/witcherActor.js](../../../../../../../../../module/actor/witcherActor.js); [module/actor/mixins/castSpellMixin.js](../../../../../../../../../module/actor/mixins/castSpellMixin.js) | Косвенное действие | Клик по имени | Передаётся ID; unknown ID пропускается |
| Handlebars/localize/concat/eq | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Шаблонизация | Core helpers и системный eq | Полный файл исполняется Handlebars 4.7.9; Foundry 14.367 |
| Локализация/ресурсы | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Подписи | localize, динамический concat, изображения Item | Настоящие expandObject/Localization; пользовательские img и Font Awesome, без исследования assets |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/partials/character/tab-magic.hbs](../../../../../../../../../templates/partials/character/tab-magic.hbs) | Partial spell-type-list | Двенадцать literal включений | Шесть групп all и отдельные вкладки |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | HBS | preloadHandlebarsTemplates | Предзагрузка |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Верхняя строка: spell.img/id/name, staminaIsVar → Variable, иначе stamina; кнопка item-chat. Теги при truthy: source (Element), level, danger, range, preparationTime, difficultyCheck, duration, defence. source/level/danger строят WITCHER.Spell.<value>; Water сохраняется с несовпадающим регистром. Описание: effect, sideEffect, liftRequirement; текст экранируется.

Компоненты: components — свободный текст; ritualComponents не перебирается. alternateRitualComponents перебирается как подготовленный массив: item.img/name и при наличии system.type/rarity/quantityObtainable/forage/weight/cost/location. quantity конкретной записи не выводится; component.name отсутствует в подготовленной RitualData, поэтому data-item-id пустой. Тут нет кнопок редактирования этих вложенных компонентов. Название и картинка разрешённого Item остаются видны.

Нет input, item-learned и прямых кнопок Item.edit/delete; редактирование существует в общем контекстном меню. Специального пути изучения, расходов IP и проверки learned этот HBS не вводит. Обработчик _onItemLearned в itemMixin существует, но шаблон его не вызывает. Разворачивание описания меняет классы DOM, не system.effect.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный рендер списков | Группы 03–05/29 | Действия, пустые списки, наследование spellType, отображение компонентов | Рендер и parse5; не HTML browser |
| Путь редактирования/применения | Группа 31 | editItem.onClick открывает sheet; _onItemRoll передаёт ID и клавиши useItem | Реальные тела методов, .sheet/useItem фасады |
| Локализация | Группа 30 | Water остаётся ключом; остальные literal подписи доступны | Core fallback en/ru; переводы модулей не подключались |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Сохранение новых Item, реальный contextmenu/DOM и активное отображение всех ветвей не запускались; .039 HBS/методы были изолированы. Остаток: [U009-01](../../../../../../cross-check-0002.md#u009-01), [U009-02](../../../../../../cross-check-0002.md#u009-02), [U009-07](../../../../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00135](../../../../../../../../issues/potential/issue-00135.md), [issue-00137](../../../../../../../../issues/closed/issue-00137.md). Уточнено различие списка Actor и сообщения ритуала; строка списка умеет показывать имя альтернативы, сообщение вставляет весь массив.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `c598d74e34f4be51535de78b38f0601c286c5407`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003039) |

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

Partial получает spells/header/itemType/spellType от tab-magic, выводит summary и li.item с itemId; .spell-roll ведёт в _onItemRoll/useItem. Динамические подписи зависят от en/ru; эффекты здесь текстовые, альтернативные компоненты показывают имена без количества. Редактирование также связано с контекстным меню.

Сопоставленные определения и потребители: [templates/partials/character/tab-magic.hbs](../../../../partials/character/tab-magic.hbs.md), [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](inventory/inventory-items-summary.hbs.md), [module/actor/sheets/WitcherActorSheet.js](../../../../../module/actor/sheets/WitcherActorSheet.js.md), [module/actor/sheets/mixins/itemMixin.js](../../../../../module/actor/sheets/mixins/itemMixin.js.md), [module/actor/sheets/interactions/itemContextMenu.js](../../../../../module/actor/sheets/interactions/itemContextMenu.js.md), [module/data/item/spellData.js](../../../../../module/data/item/spellData.js.md), [module/data/item/hexData.js](../../../../../module/data/item/hexData.js.md), [module/data/item/ritualData.js](../../../../../module/data/item/ritualData.js.md), [module/actor/witcherActor.js](../../../../../module/actor/witcherActor.js.md), [module/actor/mixins/castSpellMixin.js](../../../../../module/actor/mixins/castSpellMixin.js.md), [module/setup/handlebars.js](../../../../../module/setup/handlebars.js.md), [lang/en.json](../../../../../lang/en.json.md), [lang/ru.json](../../../../../lang/ru.json.md).

[Протокол и границы](../../../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-07](../../../../../../cross-check-0002.md#r009-07). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
