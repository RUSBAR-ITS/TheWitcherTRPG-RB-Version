# module/setup/handlebars.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) |
| Тип файла | JavaScript — шаблоны и helpers |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../../../tasks/task-0002-system-initialization.md); порция 4 |
| Запись перекрёстной сверки | [Журнал сверок](../../../review-log.md) — TASK-0002, порция 4 |

## Назначение файла

Предзагружает 59 шаблонов и регистрирует 17 Handlebars helpers для листов и сообщений.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) вызывает preloadHandlebarsTemplates в init без await, а registerHandelbarHelpers — на верхнем уровне в конце модуля. Импорт самого файла не регистрирует helpers. Экспорт использует фактическое написание Handelbar (без s). Нужны глобальные Handlebars, window, game и foundry.applications.handlebars.

## Введённые сущности и действия с ними

Два экспортированных async function: preloadHandlebarsTemplates и registerHandelbarHelpers. Первая создаёт локальный templatePath; вторая передаёт 17 функций в глобальный реестр Handlebars. Восемь логических/сравнивающих helpers регистрируются одним объектом, остальные девять — отдельными вызовами.

| Helper / аргументы | Результат | Действия и предусловия |
| --- | --- | --- |
| getOwnedComponentCount(actor, componentName) | Количество компонентов | Без actor: warn и 0. Иначе actor.findNeededComponent(name).sum('quantity'); зависит от примеси Actor и расширения Array.prototype. |
| getSetting(setting) | Значение настройки | game.settings.get('TheWitcherTRPG', setting), динамическое имя. |
| window(...props) | Значение по цепочке свойств window | Удаляет последний аргумент options; reduce идёт по свойствам. Промежуточные undefined не проверяются. |
| includes(csv, substr) | Boolean | split(',') → trim каждого элемента → точное includes(substr); csv должен быть строкой. |
| formatModLabel(statCurrent, statMax) | Число | Возвращает current − max; форматирования знака или ограничения диапазона нет. |
| eq(v1,v2), ne(v1,v2) | Boolean | Строгое === / !==. |
| lt, gt, lte, gte(v1,v2) | Boolean | Обычные JS <, >, <=, >= с их правилами преобразования типов. |
| and(...args) | Boolean | Array.every(Boolean) по всем arguments, включая передаваемый Handlebars options (обычно truthy). |
| or(...args) | Boolean | Исключает последний аргумент options; some(Boolean) по остальным. |
| eachLimit(context, limit, options) | HTML-строка | При отсутствии объекта — ''. Object.keys, цикл i < limit без ограничения длиной keys. Для каждого создаёт frame из options.data, data.key; options.fn({lifeEvent: context[key], key}, {data}); объединяет результат. |
| has(value, set) | Boolean | Вызывает set.has(value); ожидает Set или совместимый объект. |
| armorPartsInfo(armor) | Массив описаний частей брони | Семь частей, фильтр положительного max; current/max, процент, цвет и tooltip; подробности ниже. |
| capitalize(str) | Строка | Для нестроки ''; иначе toUpperCase первого символа + остаток, без изменения исходной строки. |

## Основные функции и методы

preloadHandlebarsTemplates() (стр. 1–79) без аргументов возвращает Promise от foundry.applications.handlebars.loadTemplates(templatePath). По локальному ядру /opt/foundryvtt/client/applications/handlebars.mjs:80–85, loadTemplates возвращает Promise.all загрузок; вызов в init не ожидает этот результат. Ошибки загрузки данный файл не перехватывает.

registerHandelbarHelpers() (стр. 82–217) без аргументов возвращает Promise<undefined>, но не содержит await: регистрации выполняются синхронно до возврата Promise. Эти имена занимают общий реестр helpers; другие регистрации могут влиять на итоговую функцию с тем же именем. Точный порядок всех внешних регистраций в работающем клиенте не проверялся.

armorPartsInfo объявляет head, torso, leftArm, rightArm, leftLeg, rightLeg, shield с локализованными именами и Font Awesome icon. Для фильтра max используется armor[key]?.modifiedMaxStoppingPower ?? armor.reliabilityMax; current аналогично с modifiedStoppingPower/reliability. Процент — Math.round(current/max*100), если max > 0, иначе 0. green при percentage > 66, orange при > 33, иначе red; исходное gray затем всегда заменяется. Возвращает key/name/icon/current/max/percentage/color/tooltip, где tooltip содержит имя и current / max. Ограничения процента до 100 нет. Имена локализации ног перепутаны (issue-00007).

## Используемые сущности и зависимости

| Сущность | Источник | Связь | Определение / обращение |
| --- | --- | --- | --- |
| findNeededComponent | [module/actor/mixins/craftingMixin.js](../../../../../../module/actor/mixins/craftingMixin.js) | Динамический метод Actor | Определение стр. 15; helper getOwnedComponentCount, строка 90; подключён к WitcherActor.prototype в [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js) (451) |
| Array.prototype.sum | [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) | Неявная зависимость от изменения прототипа | Стр. 18–24: сумма Number(item.system[prop] ?? 0); helper вызывает sum('quantity'). Этот файл напрямую не импортируется здесь |
| Настройки TheWitcherTRPG | [module/setup/settings.js](../../../../../../module/setup/settings.js) | Чтение через game.settings | Helper getSetting, строка 94; конкретный ключ передаёт шаблон |
| WITCHER.Location.*; WITCHER.Actor.Shield | [lang/ru.json](../../../../../../lang/ru.json); [lang/en.json](../../../../../../lang/en.json) | Локализация | armorPartsInfo; значения leftLeg/rightLeg проверены в JSON, остальные восемь языков целиком не проверялись |
| Handlebars.registerHelper/createFrame | Handlebars среды Foundry | Внешний API | Регистрация функций, контекст eachLimit |
| foundry.applications.handlebars.loadTemplates | Foundry 14.367.0 | Внешний API | Список templatePath передаётся одной операцией |
| window / game | Среда браузера и Foundry | Глобальный доступ | helper window может прочитать произвольную цепочку, getSetting и armorPartsInfo используют game |
| fa-* классы иконок | Font Awesome среды Foundry | Ресурс интерфейса | Строки icon в parts; наличие конкретного глифа в браузере не проверялось |

Список templatePath — 59 файлов, все существуют при сопоставлении URL-префикса systems/TheWitcherTRPG/ с корнем checkout. Это зависимости загрузки, не доказательство отображения каждого шаблона:

| Файл шаблона | Проверка |
| --- | --- |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../templates/sheets/actor/monster-sheet.hbs) | Существует |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../../templates/sheets/actor/loot-sheet.hbs) | Существует |
| [templates/partials/character-header.hbs](../../../../../../templates/partials/character-header.hbs) | Существует |
| [templates/partials/character/tab-skills.hbs](../../../../../../templates/partials/character/tab-skills.hbs) | Существует |
| [templates/partials/character/skill-display.hbs](../../../../../../templates/partials/character/skill-display.hbs) | Существует |
| [templates/partials/character/custom-skill-display.hbs](../../../../../../templates/partials/character/custom-skill-display.hbs) | Существует |
| [templates/partials/character/tab-profession.hbs](../../../../../../templates/partials/character/tab-profession.hbs) | Существует |
| [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs) | Существует |
| [templates/partials/character/substances.hbs](../../../../../../templates/partials/character/substances.hbs) | Существует |
| [templates/partials/character/tab-magic.hbs](../../../../../../templates/partials/character/tab-magic.hbs) | Существует |
| [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | Существует |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | Существует |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | Существует |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | Существует |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | Существует |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | Существует |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | Существует |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs) | Существует |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | Существует |
| [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | Существует |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | Существует |
| [templates/partials/crit-wounds-table.hbs](../../../../../../templates/partials/crit-wounds-table.hbs) | Существует |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../../templates/partials/monster/monster-skill-tab.hbs) | Существует |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../templates/partials/monster/monster-inventory-tab.hbs) | Существует |
| [templates/partials/monster/monster-details-tab.hbs](../../../../../../templates/partials/monster/monster-details-tab.hbs) | Существует |
| [templates/partials/monster/monster-spell-tab.hbs](../../../../../../templates/partials/monster/monster-spell-tab.hbs) | Существует |
| [templates/partials/monster/monster-skill-display.hbs](../../../../../../templates/partials/monster/monster-skill-display.hbs) | Существует |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | Существует |
| [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) | Существует |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../templates/sheets/actor/partials/monster/header.hbs) | Существует |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | Существует |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs) | Существует |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | Существует |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) | Существует |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs) | Существует |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) | Существует |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) | Существует |
| [templates/partials/item-header.hbs](../../../../../../templates/partials/item-header.hbs) | Существует |
| [templates/partials/spell-header.hbs](../../../../../../templates/partials/spell-header.hbs) | Существует |
| [templates/partials/item-image.hbs](../../../../../../templates/partials/item-image.hbs) | Существует |
| [templates/partials/associated-item.hbs](../../../../../../templates/partials/associated-item.hbs) | Существует |
| [templates/partials/associated-diagram.hbs](../../../../../../templates/partials/associated-diagram.hbs) | Существует |
| [templates/partials/effect-part.hbs](../../../../../../templates/partials/effect-part.hbs) | Существует |
| [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs) | Существует |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | Существует |
| [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) | Существует |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../templates/sheets/investigation/mystery-sheet.hbs) | Существует |
| [templates/sheets/investigation/partials/clue-display.hbs](../../../../../../templates/sheets/investigation/partials/clue-display.hbs) | Существует |
| [templates/sheets/investigation/partials/obstacle-display.hbs](../../../../../../templates/sheets/investigation/partials/obstacle-display.hbs) | Существует |
| [templates/dialog/verbal-combat.hbs](../../../../../../templates/dialog/verbal-combat.hbs) | Существует |
| [templates/dialog/repair-dialog.hbs](../../../../../../templates/dialog/repair-dialog.hbs) | Существует |
| [templates/chat/damage/damageToLocation.hbs](../../../../../../templates/chat/damage/damageToLocation.hbs) | Существует |
| [templates/chat/item/repair.hbs](../../../../../../templates/chat/item/repair.hbs) | Существует |
| [templates/chat/item/partials/item-description/alchemicals.hbs](../../../../../../templates/chat/item/partials/item-description/alchemicals.hbs) | Существует |
| [templates/chat/item/partials/item-description/crafting-items.hbs](../../../../../../templates/chat/item/partials/item-description/crafting-items.hbs) | Существует |
| [templates/chat/item/partials/item-description/description.hbs](../../../../../../templates/chat/item/partials/item-description/description.hbs) | Существует |
| [templates/chat/item/partials/item-description/spell-description.hbs](../../../../../../templates/chat/item/partials/item-description/spell-description.hbs) | Существует |
| [templates/chat/item/partials/item-description/tags.hbs](../../../../../../templates/chat/item/partials/item-description/tags.hbs) | Существует |
| [templates/partials/components-list.hbs](../../../../../../templates/partials/components-list.hbs) | Существует |

Префикс ресурсов связан с system.id из [system.json](../../../../../../system.json). HTTP-доступ не проверялся; известное замечание о каталоге системы см. issue-00001.

## Известные потребители

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) вызывает обе экспортированные функции. Таблица ниже фиксирует буквальные вызовы helpers в templates/**/*.hbs; поиск охватывает {{helper, {{#helper и (helper. Динамические имена и внешние шаблоны не исключены.

| Шаблон-потребитель | Helpers и строки |
| --- | --- |
| [templates/chat/combat/spellItem.hbs](../../../../../../templates/chat/combat/spellItem.hbs) | eq (59) |
| [templates/chat/damage/damageToLocation.hbs](../../../../../../templates/chat/damage/damageToLocation.hbs) | or (21) |
| [templates/chat/item/partials/item-description/alchemicals.hbs](../../../../../../templates/chat/item/partials/item-description/alchemicals.hbs) | eq (2, 6, 13); or (2) |
| [templates/chat/item/partials/item-description/crafting-items.hbs](../../../../../../templates/chat/item/partials/item-description/crafting-items.hbs) | capitalize (24); eq (2); gt (20); or (3) |
| [templates/chat/item/partials/item-description/description.hbs](../../../../../../templates/chat/item/partials/item-description/description.hbs) | eq (2); or (2) |
| [templates/chat/item/partials/item-description/spell-description.hbs](../../../../../../templates/chat/item/partials/item-description/spell-description.hbs) | eq (2); or (2) |
| [templates/chat/item/partials/item-description/tags.hbs](../../../../../../templates/chat/item/partials/item-description/tags.hbs) | eq (1, 45, 85, 125, 145, 180, 210, 238, 290); gt (201, 303); or (1, 125, 238) |
| [templates/dialog/combat/weapon-attack.hbs](../../../../../../templates/dialog/combat/weapon-attack.hbs) | eq (31, 240); or (31) |
| [templates/partials/character-header.hbs](../../../../../../templates/partials/character-header.hbs) | eq (23, 32) |
| [templates/partials/character/custom-skill-display.hbs](../../../../../../templates/partials/character/custom-skill-display.hbs) | gte (4); or (10) |
| [templates/partials/character/skill-display.hbs](../../../../../../templates/partials/character/skill-display.hbs) | gte (5); or (11) |
| [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs) | eachLimit (66); eq (12, 21) |
| [templates/partials/character/tab-profession.hbs](../../../../../../templates/partials/character/tab-profession.hbs) | eq (25, 56, 79, 102, 128, 151, 174, 200, 223, 246) |
| [templates/partials/character/tab-skills.hbs](../../../../../../templates/partials/character/tab-skills.hbs) | capitalize (14, 38) |
| [templates/partials/character/tab-stats.hbs](../../../../../../templates/partials/character/tab-stats.hbs) | formatModLabel (25, 27, 30, 57, 59, 62, 101, 103, 106); eq (9, 27, 30, 59, 62, 78, 79, 80, 81, 82, 83, 103, 106); gt (27, 30, 59, 62, 103, 106); gte (13, 20, 25, 45, 52, 57, 89, 96, 101); or (40, 77) |
| [templates/partials/components-list.hbs](../../../../../../templates/partials/components-list.hbs) | eq (25); and (25) |
| [templates/partials/effect-part.hbs](../../../../../../templates/partials/effect-part.hbs) | eq (7); and (7, 18) |
| [templates/partials/item-header.hbs](../../../../../../templates/partials/item-header.hbs) | getSetting (10); window (10); includes (10); eq (10, 42, 52); and (10); or (10) |
| [templates/partials/item-image.hbs](../../../../../../templates/partials/item-image.hbs) | getSetting (1); includes (1); and (1) |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | or (3, 7, 11) |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../templates/partials/monster/monster-inventory-tab.hbs) | eq (89, 92, 96, 106, 130, 147, 192, 210, 233, 264) |
| [templates/partials/spell-header.hbs](../../../../../../templates/partials/spell-header.hbs) | getSetting (10); window (10); includes (10); eq (10, 40, 45, 53, 63); and (10); or (10, 53) |
| [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | eq (2, 6) |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) | eq (2) |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../../templates/sheets/actor/loot-sheet.hbs) | lt (12); gt (3); gte (9) |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../templates/sheets/actor/monster-sheet.hbs) | eq (11, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 277, 291); gt (225, 230, 235, 240, 245, 250, 255, 260, 265); gte (46) |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | eq (76) |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | armorPartsInfo (19); eq (89); gt (103); or (90) |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | getOwnedComponentCount (87); or (78) |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | gt (49) |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | eq (59) |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | eq (84); gt (52, 100) |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | gte (6, 8, 23) |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | gte (5, 7, 24) |
| [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) | eq (28) |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | gte (7) |
| [templates/sheets/item/alchemical-sheet.hbs](../../../../../../templates/sheets/item/alchemical-sheet.hbs) | eq (9, 25); or (9, 25) |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../templates/sheets/item/armor-sheet.hbs) | eq (60, 67, 74, 83, 106, 122); or (74, 83, 106) |
| [templates/sheets/item/component-sheet.hbs](../../../../../../templates/sheets/item/component-sheet.hbs) | eq (17) |
| [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs) | has (4, 14, 25) |
| [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) | has (4, 8) |
| [templates/sheets/item/configuration/tabs/general.hbs](../../../../../../templates/sheets/item/configuration/tabs/general.hbs) | has (6, 16, 27) |
| [templates/sheets/item/enhancement-sheet.hbs](../../../../../../templates/sheets/item/enhancement-sheet.hbs) | eq (11, 56); or (56) |
| [templates/sheets/item/hex-sheet.hbs](../../../../../../templates/sheets/item/hex-sheet.hbs) | getSetting (11); window (11); includes (11); eq (11); and (11); or (11) |
| [templates/sheets/item/homeland-sheet.hbs](../../../../../../templates/sheets/item/homeland-sheet.hbs) | eq (10) |
| [templates/sheets/item/ritual-sheet.hbs](../../../../../../templates/sheets/item/ritual-sheet.hbs) | getSetting (7); window (7); includes (7); eq (7, 61, 70, 91, 98); and (7); or (7) |
| [templates/sheets/item/spell-sheet.hbs](../../../../../../templates/sheets/item/spell-sheet.hbs) | eq (6, 9, 13, 16, 22, 25, 29, 32, 46, 73, 78, 81, 84, 89, 104, 110, 116) |

В этой области для ne и lte вызовов не найдено; это не доказывает отсутствие внешних потребителей. Шаблоны могут содержать неиспользуемые в текущих листах части; достижимость каждого рендера не установлена.

## Данные и изменения состояния

Меняет реестры helpers и, через loadTemplates, кэш/partials шаблонов ядра. Helpers читают Actor, настройки, window и переданный контекст, рассчитывают значения для отображения. eachLimit создаёт frame и вызывает переданную функцию рендера; игровые документы не обновляются.

## Проверки и доказательства

Полностью прочитаны 217 строк. Сопоставлены 59 путей, 17 имён helpers и их буквальные вызовы в шаблонах. Проверены реальные определения findNeededComponent и Array.prototype.sum. В vm исходные регистрации собраны подменным Handlebars; исходные helper-функции вызваны на контрольных данных: CSV с пробелом → true; eq(1,'1') → false; 7−10 → −3; and/or → false/true; capitalize('witcher') → Witcher; eachLimit с одним ключом и limit=3 вызывает рендер трижды, последние два контекста с undefined; подписи ног воспроизвели перепутанные ключи. loadTemplates заменён сборщиком путей.

## Непроверенные участки и открытые вопросы

Настоящий движок Handlebars и HTML листов не рендерились, запросы шаблонов по HTTP не выполнялись. Зависимость sum проверена по источнику определения, а не посредством реального импорта всех листов. eachLimit за границей массива описан как поведение; достижимость такого входа через текущую модель lifeEvents отдельно не установлена.

## Связанные проблемы

[issue-00007](../../../../../issues/potential/issue-00007.md) — подписи ног; [issue-00001](../../../../../issues/potential/issue-00001.md) — известное замечание о регистрации каталога и путях.

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 4 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.

## Уточнение TASK-0003.004

2026-09-10, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26`. Установлен источник данных eachLimit: [lifeEventsData](../data/actor/templates/character/general/lifeEventsData.js.md) задаёт 20 ключей, WitcherCharacterSheet._prepareContext:133–137 преобразует объект в массив с key. Исходный helper при limit=2 передал записи с key 10/20. CharacterData допускает счётчик 21 без диапазона, eachLimit передаёт для него один undefined; HTML-ввод min=1,max=20 прочитан, обход его в обычном UI не проверялся. [issue-00024](../../../../../issues/potential/issue-00024.md) относится к изменению модели подготовкой листа, не к определению helper.

[Перекрёстная сверка TASK-0003.004](../../../review-log.md#task-0003004).

## Уточнение TASK-0003.008

2026-09-10, `c5edcbadd05ff4038a174bd2e2a49785e40ea878`; исходник не изменился относительно исходного среза. Helper подсчёта компонентов в строке 91 вызывает ownedComponent.sum('quantity'). Определение Array.prototype.sum найдено в module/actor/sheets/WitcherActorSheet.js:18–24: суммирует Number(this[i].system[prop] ?? 0). Это соответствует строковой quantity общей модели Item. Сам calcWeight не использует helper или sum.

Связанные карточки: [CommonItemData](../data/item/commonItemData.js.md) и [WitcherItem](../item/witcherItem.js.md). Определение потребителя: [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js). [Перекрёстная сверка](../../../review-log.md#task-0003008). Новая запись уточняет связи; исторические результаты прежних порций сохранены.

## Уточнение TASK-0003.010

2026-09-10, `247d3d86e344238a1445377c686eb6455146693c`; исходник прежнего среза не изменён.

Полностью разобраны предзагружаемые [templates/partials/effect-part.hbs](../../../../../../templates/partials/effect-part.hbs) и [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs). Первый используют Actor V2/V1 и Item-конфигурация с разными обработчиками; второй вместе с crit-wounds-table.hbs дважды выводит одну травму (issue-00054). and/eq определены этим файлом; not/localize/formGroup/selectOptions предоставляются ядром. Wizard и system-specific рендерятся по путям листа; им не приписана отсутствующая регистрация в preload.

[Общая сверка первой серии](../../../review-log.md) — TASK-0003.010. Полный клиент и БД не запускались.

## Уточнение TASK-0003.011

2026-09-10, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b`; содержимое исходника совпадает с предыдущим срезом.

Сверены [item-header](../../templates/partials/item-header.hbs.md) (10 прямых предметных форм), [item-image](../../templates/partials/item-image.hbs.md) и три шаблона базовой Item-конфигурации. Исходные getSetting/includes/window/has исполнены в Handlebars-матрицах. item-image включается лишь в прежний monster-inventory-tab; текущий MonsterSheet использует другие PARTS. Предзагрузка старого monster-sheet и его partial не доказывает отображение текущим листом. Поля general сверены на 22 реальных схемах Item с фасадом toFormGroup; itemUseAttackSkill не выводится, заголовок spell использует ranged.

[TASK-0003.011 — сценарии и сверка](../../../review-log.md#task-0003011).

## Уточнение TASK-0003.012

2026-09-10, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9`; исходник не изменён. armorPartsInfo читает modifiedStoppingPower/modifiedMaxStoppingPower, определённые в [SpData](../../../../../../module/data/item/templates/armor/spData.js). У них persisted:false: после base→derived 7/10 с улучшением2 превращаются в9/12, а source сохраняет7/10. Шесть ключей ArmorData совпали с helper; shield использует fallback reliability. Подписи ног по-прежнему относятся к [issue-00007](../../../../../issues/potential/issue-00007.md).

Результат и границы — [сверка TASK-0003.012](../../../review-log.md#task-0003012).

## Уточнение TASK-0003.014

2026-09-10, `0fa589bd300856ff309f362afcb66d6fa43401ab`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003014).

Полностью разобраны [templates/sheets/item/armor-sheet.hbs](../../../../../../templates/sheets/item/armor-sheet.hbs) и [templates/sheets/item/configuration/tabs/armorGeneral.hbs](../../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs). Пары schema/name/value и подписи leftLeg/rightLeg в этих формах верны; issue-00007 по-прежнему локализована в armorPartsInfo инвентаря. Исполнены шесть вариантов location и двенадцать schema-полей конфигурации. Старый тест самого armorPartsInfo не повторялся; ключи локализации проверены по JSON.

Отдельно установлено отсутствие четырёх русских подсказок в armorGeneral.hbs: [issue-00090](../../../../../issues/potential/issue-00090.md). Это не меняет правильную привязку полей к сторонам.

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003015).

Прослежена цепочка main→item-header в [templates/sheets/item/alchemical-sheet.hbs](../../../../../../templates/sheets/item/alchemical-sheet.hbs), [templates/sheets/item/mutagen-sheet.hbs](../../../../../../templates/sheets/item/mutagen-sheet.hbs), [templates/sheets/item/valuable-sheet.hbs](../../../../../../templates/sheets/item/valuable-sheet.hbs): getSetting/window/includes/has из этого файла участвуют в общих условиях header. Цвет мутагена выводится там же. formGroup и selectOptions в [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) относятся к API Foundry, не определяются системным handlebars.js. В проверке использован оригинальный core formGroup; widgets и selectOptions имели ограниченные фасады.

## Уточнение TASK-0003.016

2026-09-10, `53f74994011383cb544cabac96285430f00cb38a`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003016).

Полностью разобраны предзагружаемые [templates/partials/components-list.hbs](../../../../../../templates/partials/components-list.hbs), [templates/partials/associated-diagram.hbs](../../../../../../templates/partials/associated-diagram.hbs), [templates/partials/associated-item.hbs](../../../../../../templates/partials/associated-item.hbs). components-list включается только repair-dialog; другие два — листами оружия/брони и рецепта. В [templates/sheets/item/component-sheet.hbs](../../../../../../templates/sheets/item/component-sheet.hbs) вызван устаревший #select: ни этот файл, ни initialize helpers Foundry14.367 его не регистрируют. Реальный рендер остановился на Missing helper: select; временный диагностический helper для изучения оставшихся полей не записан в систему.

## Уточнение TASK-0003.017

2026-09-10, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; исходники неизменны. [Сверка](../../../review-log.md#task-0003017).

Полностью прочитаны предзагружаемые [repair-dialog](../../../../../../templates/dialog/repair-dialog.hbs) и [repair chat](../../../../../../templates/chat/item/repair.hbs). Первый получает data/components/isRequest/canEditCost и включает [components-list](../../../../../../templates/partials/components-list.hbs); второй — data/isRequest/isOrder/showComponents. Пути preload/render совпадают. Отсутствующий damagedLocations не вызывает ошибки HBS, но не рисует строки. showComponents исключает случай только unknown; это [issue-00107](../../../../../issues/potential/issue-00107.md). Рендер изолированный, настоящего HTTP-клиента не было.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. loadHandlebarTemplates предзагружает [skillPathSkillPart](../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) и [profAttackOptionsPart](../../../../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) строками 58–59. [skillPathPart](../../../../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) загружается как PARTS трёх вкладок и включает первый partial, тот — второй. Helper has147–149 использует Set.has; в рендере профессии проверены пустой и включённые варианты.

[Перекрёстная сверка](../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Уточнение TASK-0003.020

2026-09-11, `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008`; проверены связи с критическими травмами, лечением и отдыхом. Полный первоначальный разбор и его ограничения сохранены.

| Связь | Файл | Результат проверки |
| --- | --- | --- |
| crit-wounds-table.hbs | [templates/partials/crit-wounds-table.hbs](../../../../../../templates/partials/crit-wounds-table.hbs) | Предзагрузка 29 → включение tab-effects. Partial выводит одну строку на Item, родитель дополнительно повторяет цикл. |
| Динамические шаблоны лечения | [module/actor/sheets/mixins/healMixin.js](../../../../../../module/actor/sheets/mixins/healMixin.js) | heal-rest/resting-status загружаются явным renderTemplate; отсутствие в preload не означает недоступности. |
| heal.hbs | [templates/chat/combat/heal.hbs](../../../../../../templates/chat/combat/heal.hbs) | Actor.createHealMessage загружает отдельный HBS через renderTemplate. |

[Сверка порции и итоговая сверка 96 файлов второй серии](../../../review-log.md#task-0003020); браузер, мир и записи в БД не запускались.
