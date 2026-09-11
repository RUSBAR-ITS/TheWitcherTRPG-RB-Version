# module/actor/sheets/mixins/customSkillMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/customSkillMixin.js](../../../../../../../../module/actor/sheets/mixins/customSkillMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../../review-log.md#task-0003029) |

## Назначение файла

Обработчики собственного embedded Item-навыка: бросок через Actor, удаление Item, открытие сведений о модификаторах и старые операции над массивом modifiers.

## Условия использования

Присоединяется к V2/V1 базовым листам Actor. Поиск Item идёт через ближайший .item и data-item-id. Текущая character/custom-skill-display не создаёт эти селекторы; старый monster-custom-skill-display содержит бросок, удаление и раскрытие, но не кнопки CRUD массива.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| customSkillMixin | export let, 1–62 | Шесть методов | Object.assign базовых листов Actor | Регистрация click/blur и действия над embedded Item |
| Строка modifiers | Локальные массивы обработчиков | name/value; редактор и удаление ожидают id | В SkillItemData поля modifiers нет | Добавление не создаёт id; редактирование сохраняет строку input.value |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| customSkillListener(html) | DOM, actor и методы примеси | Шесть подписок | Click: #custom-rollable, remove-custom-skill, custom-skill-modifier-display, add-custom-skill-modifier, delete-custom-skill-modifier; blur: edit-custom-skill-modifier | Локально заменяет аргумент на $(html), не глобальный jQuery |
| removeCustomSkill(event) | Item ID из currentTarget.closest('.item') | Нет результата | actor.items.get(id).delete() | Нет проверки ID, подтверждения, await или возврата Promise |
| customSkillModifierDisplay(event) | Item ID из currentTarget | Нет результата | Находит Item и пишет инвертированный system.isOpened | update не ожидается |
| _onAddCustomSkillModifier(event) | Item; system.modifiers ?? [] | Promise без результата | Добавляет {name: 'Modifier', value: 0}; update system.modifiers | При существующем массиве мутирует его; id не создаётся; update не ожидается |
| _onRemoveCustomSkillModifier(event) | Item; массив; event.target.dataset.id | Promise без результата | Object.values(...).map; findIndex строгого id; splice; update | Нет массива → TypeError; не найден id → splice(-1,1) удаляет последний; update не ожидается |
| _onEditCustomSkillModifier(event) | Item; currentTarget; closest('.list-modifiers').dataset.id; dataset.field | Promise без результата | Ищет строку с нестрогим сравнением id, записывает element.value и update | Значение строковое; нет id → индекс −1 и TypeError; поле не проверено; update не ожидается |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| rollCustomSkillCheck | [module/actor/mixins/skillMixin.js](../../../../../../../../module/actor/mixins/skillMixin.js) | Метод Actor | Передача события #custom-rollable с сохранением this Actor | customSkillListener |
| SkillItemData | [module/data/item/skillItemData.js](../../../../../../../../module/data/item/skillItemData.js) | Схема Item | isOpened объявлен; modifiers и ID строк не объявлены | Все операции с полями; проверка настоящей модели |
| DOM старого собственного навыка | [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | Контракт селекторов | tbody.item, itemId, #custom-rollable, remove и раскрытие | Буквальные селекторы; CRUD массива отсутствует |
| DOM текущего собственного навыка | [templates/partials/character/custom-skill-display.hbs](../../../../../../../../templates/partials/character/custom-skill-display.hbs) | Сопоставление контракта | Не содержит .item/itemId и custom-обработчиков | Полное чтение и настоящий Handlebars |
| Item.update/delete, Actor.items; $ и события | Foundry VTT / браузер / jQuery | Внешний API | Поиск, изменение и удаление embedded Item | Прямые вызовы; currentTarget отличается от target при удалении модификатора |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | customSkillMixin | Импорт, Object.assign, вызов customSkillListener | activateListeners и прототип |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | customSkillMixin | Те же подключения старого базового листа | Прямой импорт, вызов и Object.assign |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | Три custom-события | Старый шаблон создаёт цели броска/удаления/раскрытия | Буквальные ID и классы; активность родителя проверена отдельно |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

isOpened — корректное поле модели. system.modifiers — ожидаемый кодом, но отсутствующий в текущей схеме список. Настоящая SkillItemData отбрасывает его при создании и updateSource; payload Item.update сам по себе не доказывает сохранение. Удаление Item вызывает стандартный API; собственного восстановления/отмены здесь нет. Обработчики не возвращают завершение операций с документами.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Шесть функций и шаблоны | Полное чтение 62 строк; rg всех шести селекторов в module/templates | Бросок/remove/open есть в старом HBS; кнопок add/edit/delete modifiers в текущих templates не найдено | Сторонние макросы и модули не искались |
| События и модель | Настоящие методы и SkillItemData, записывающий Item | isOpened меняется; добавление выдаёт name/value без id; схема не принимает modifiers; delete вызван | Запись игровых документов подменена |
| Старые массивы | Явно внедрённый modifiers в обход схемы; отсутствующий/неизвестный id | Удаление неизвестного id снимает последнюю строку; edit сохраняет '-3'; отсутствующие список/строка бросают TypeError | Доказывает поведение функции для таких входов, а не доступность этих кнопок в действующем листе |

## Непроверенные участки и открытые вопросы

Не заявляется, что удаление последнего модификатора происходит через действующий интерфейс: цели CRUD сейчас отсутствуют. Подмены Item не проверяют Foundry document-update цикл, сокеты или БД; принятие полей проверено отдельно настоящей DataModel. Старый родитель monster-sheet не является PARTS текущего V2 листа.

## Связанные проблемы

[issue-00187](../../../../../../../issues/potential/issue-00187.md), [issue-00189](../../../../../../../issues/potential/issue-00189.md). Ошибка текущего DOM и рассогласование старого CRUD со схемой разделены; оба наблюдения остаются potential.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003029) |
