# templates/partials/monster/monster-spell-tab.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/monster/monster-spell-tab.hbs](../../../../../../../templates/partials/monster/monster-spell-tab.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `c598d74e34f4be51535de78b38f0601c286c5407` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.039](../../../../../../tasks/task-0003.039.md), 6 файлов, 870 логических строк |
| Запись перекрёстной сверки | [TASK-0003.039](../../../../review-log.md#task-0003039) |

## Назначение файла

Старый табличный интерфейс магии монстра: четыре фокуса и шесть списков spell/ritual/hex/MagicalGift с панелями system.pannels.

## Условия использования

Предзагружается module/setup/handlebars.js и включён в templates/sheets/actor/monster-sheet.hbs:302. Текущий зарегистрированный WitcherMonsterSheet использует PARTS и общую tab-magic.hbs, а не этот монолит. Наличие старого HBS и ссылки в нём не доказывает его отображение действующим листом.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| magic-info / focus inputs | 1–26 | Восемь полей четырёх фокусов | name=system.focus1–4.name/value | Привязка формы старого листа |
| spell[data-spelltype] | 27–223 | noviceSpell,journeymanSpell,masterSpell,ritual,hex,magicalgift | Шесть панелей | spell-display и флаги pannels.*IsOpen |
| tbody.item / spell-roll / item-edit / item-delete / inline-edit | Повторяются в шести группах | Строка Item с действиями | data-item-id=_id, data-field=system.stamina | Картинка draggable=true, класс dragable с одной g |

## Основные функции и методы

Собственного JavaScript нет. each выводит элементы; if/unless меняют классы таблиц и иконки стрелки. У magicalgift две отдельные условные ветви открытия table. Контракт кликов и записи хранится в itemMixin.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Старый монолитный monster-sheet.hbs | [templates/sheets/actor/monster-sheet.hbs](../../../../../../../templates/sheets/actor/monster-sheet.hbs) | Literal consumer | Строка 302, magic tab | Связь обнаружена поиском; действующий V2 его не выбирает |
| V1 и V2 _prepareSpells | [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Одинаковый исторический контекст | noviceSpells/journeymanSpells/masterSpells/rituals/hexes/magicalgift | Совпадение структуры данных не равнозначно регистрации старого листа |
| itemListener и _onSpellDisplay/_onItemInlineEdit/_onItemEdit/_onItemDelete/_onItemRoll | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | DOM selectors | spell-display,item-edit,item-delete,inline-edit,spell-roll | Стабильные .item/.spell с ID и spelltype |
| Pannels / focus | [module/data/actor/templates/character/pannelsData.js](../../../../../../../module/data/actor/templates/character/pannelsData.js); [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/focusData.js](../../../../../../../module/data/actor/templates/common/focusData.js) | Поля Actor | noviceSpellIsOpen/journeymanSpellIsOpen/masterSpellIsOpen/ritualIsOpen/hexIsOpen/magicalgiftIsOpen; focus1–4 | Флаги меняет _onSpellDisplay, HBS сам не пишет |
| Данные магии | [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js); [module/data/item/hexData.js](../../../../../../../module/data/item/hexData.js); [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js) | Item-поля | _id,img,name,system.stamina | Не отображает staminaIsVar отдельно |
| Предзагрузка/регистрация текущего листа | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js); [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [templates/partials/character/tab-magic.hbs](../../../../../../../templates/partials/character/tab-magic.hbs) | Загрузка и альтернативный текущий путь | Старый HBS загружается, текущий PARTS.magic иной | Область поиска module/templates; внешние листы/миры не проверены |
| Локализация | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | localize | Названия групп, focus.first/second/third/fourth/name | Все literal ключи доступны после раскрытия |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | HBS | preloadHandlebarsTemplates | Предзагрузка |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../../templates/sheets/actor/monster-sheet.hbs) | Partial старой вкладки | Literal включение 302 | Нет доказательства использования монолита текущим листом |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Форма содержит system.focus1.name/value, focus2.name/value, focus3.name/value, focus4.name/value (type=text). В каждом tbody Item есть input с data-field=system.stamina, data-dtype=Number, без name; inline-handler передаёт value строкой в Item.update. data-spelltype noviceSpell/journeymanSpell/masterSpell/ritual/hex/magicalgift превращается в путь system.pannels.<type>IsOpen. Закрытая таблица остаётся в DOM с invisible; открытая получает skill-list item-list.

Действия: редактирование, изображение/drag, сотворение, изменение STA, удаление. Здесь нет добавления, item-chat или item-learned. Шаблон читает _id, в современном списке — id. Неполное закрытие td у кнопок delete в исходнике обрабатывается HTML-парсером; браузерная разметка и CSS не проверялись.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Чтение/поиск потребителя | rg по всем module/templates, регистрация Sheets | Найдено старое включение и предзагрузка; текущий monster использует общий HBS | Нет внешних модулей/макросов |
| Изолированный рендер | Группа 04 | Шесть панелей, восемь focus-полей, строка Item с edit/inline STA | parse5; не запуск старого листа |

## Непроверенные участки и открытые вопросы

Файлы порции прочитаны целиком. Проверка: Foundry 14.367.0, Node 24.16.0, реальные модели/методы, Roll/extendedRoll, Handlebars 4.7.9, expandObject и core Localization с fallback. Диалог, Application/DOM, вывод Roll.toAnchor, запись Actor/Item/ChatMessage, UUID resolver, создание/clone ActiveEffect, canvas и query заменены фасадами. Реальные браузер, HTTP, БД, компедиумы, сетевые клиенты и жизненный цикл эффекта не запускались. Текстовые формулы проверены как поведение кода, без выбора правил книг.

## Связанные проблемы

Наличие старого шаблона само по себе не зарегистрировано как неисправность.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `c598d74e34f4be51535de78b38f0601c286c5407`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003039) |
