# templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.027](../../../../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../../../../review-log.md#task-0003027) |

## Назначение файла

Таблица брони и свободных улучшений типа armor: сведения о защите, количество, экипировка, ремонт, сопротивления и установленные/свободные ячейки улучшений.

## Условия использования

Общие weapons/armor producers V2 передают armors в Character и Monster. Строка имеет .item.list-item.draggable и data-item-id, но не data-type. armorPartsInfo читает подготовленную защиту; ремонтная кнопка есть в обоих листах, listener найден только в Character.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| summary/rows:1–45 | Блок HBS | Защита и действия | Рендер через потребителей | hasReliability; armorPartsInfo→icon/color/tooltip; quantity всегда; item-roll/chat/equip/repair |
| tags/description:46–88 | Блок HBS | Тип, сопротивления и вес | Рендер через потребителей | resistance.slashing/piercing/bludgeoning, encumb, weight; description экранирован |
| enhancements:89–130 | Блок HBS | Два источника ячеек | Рендер через потребителей | unless eq текущего Item.type enhancement; enhancementItems и freeEnhancements; effects словарь, percentage>0; name всегда |

## Основные функции и методы

Собственных JS-функций, экспортов и схем нет. В файле используются armorPartsInfo, each, eq, gt, if, localize, or, unless и включения partial. Ветви и поля описаны по блокам выше.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .inline-edit | [itemMixin._onItemInlineEdit](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → data-field/value → Item.update; Number/String очищаются моделью |
| .item-display-info | [itemMixin._onItemDisplayInfo](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → .item-info.toggleClass(invisible) |
| .item-chat | [itemMixin._onItemMessage](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .list-item → item-description → ChatMessage |
| .item-roll | [itemMixin._onItemRoll](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → Actor.useItem с alt/ctrl/shift |
| .item-equip | [itemMixin._onItemEquip](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → toggle system.equipped |
| .enhancement-label | [itemMixin._onEnhancementInfo](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .weapon-enhancement → .enhancement-info |
| .enhancement-weapon-slot | [itemMixin._chooseEnhancement](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → dataset.type; weapon → weapon/rune, иначе armor/glyph |
| .item-repair | [WitcherCharacterSheet._repairItem](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | closest .item → Item.repair; подключено только Character |

Поля name/data-field, буквально присутствующие в файле: `system.quantity`.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ArmorData и вложенные модели | [module/data/item/armorData.js](../../../../../../../../../../module/data/item/armorData.js); [module/data/item/templates/armor/spData.js](../../../../../../../../../../module/data/item/templates/armor/spData.js); [module/data/item/templates/armor/resistanceData.js](../../../../../../../../../../module/data/item/templates/armor/resistanceData.js) | Поля/getters/prepared | equipped/canBeRepaired/resistance/*StoppingPower/freeEnhancements | SP в helper берётся из вложенных моделей; форма не вводит SP напрямую |
| armorPartsInfo | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Helper | Иконки текущего/максимального SP и надёжности щита | Цвета >66 green, >33 orange, иначе red; подписи ног перепутаны — issue-00007 |
| effects и applied | [module/data/item/enhancementData.js](../../../../../../../../../../module/data/item/enhancementData.js) | Вложенные Item | Имена воздействий и percentages | TypedObjectField обрабатывается each; здесь нет передачи статусов в applyStatus |
| item-repair | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Listener | _repairItem→Item.repair | У Monster тот же HBS, но такой listener не найден |
| armorPartsInfo, eq, gt, or | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Системные helpers | Точные вызовы в этом HBS | registerHandelbarHelpers исполнен из исходника; расчёты отделены от UI-записи |
| each, if, localize, unless | Handlebars 4.7.9 / Foundry VTT 14.367.0 | Внешний шаблонный API | Вызовы в этом HBS; core localize/concat: /opt/foundryvtt/client/applications/handlebars.mjs | Рендер настоящий; game.i18n/окружение представлены фасадом, core helper localize/concat дополнительно исполнены |
| Словари и подписи | [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | Контекст и локализация | Точные строковые ключи localize в HBS | 114 статических ключей порции сверены с en/ru; отсутствующие и динамические ключи отражены в issue-00178 |
| Общие поля Item и доступ Document | [module/data/item/commonItemData.js](../../../../../../../../../../module/data/item/commonItemData.js) | Чтение данных | name/id/_id/img у Foundry Document; system.description/quantity/weight/cost/isCarried/isStored/isHidden у модели | quantity StringField; weight/cost NumberField; чтение не означает сохранение |
| Обработчики DOM | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js); [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | DOM→JS | Сопоставление ниже в таблице действий | Селекторы и ближайшие контейнеры проверены по реальному шаблону и определениям |
| Контекстное меню Item | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Внешний listener | Ближайшая .item и data-item-id → меню шести действий | Отдельных menu entries HBS не создаёт; неисправные callbacks issue-00168 не переисполнялись |
| partial inventory-items-summary.hbs | [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| Классы списка, details, progress, изображения | [styles/tab-inventory.css](../../../../../../../../../../styles/tab-inventory.css) | CSS/HTML | grid заголовков/строк, stored-item и carry-bar до привязки селекторов | Полный CSS и вид браузера не проверялись; img без src не получает fallback в HBS, assets вне границ анализа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и кеширование пути; не доказательство активного листа | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | partial tab-inventory-armors.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | partial tab-inventory-armors.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Количество и equipped пишутся в Item внешними обработчиками. system.type выводится как сохранённый код Light/Medium/Heavy/Natural, resistance — с локализованными названиями урона. Заголовок получает Reliability, хотя строка также содержит всегда доступное quantity без своего заголовка. Отсутствующий data-type приводит _chooseEnhancement в else для armor/glyph; класс enhancement-weapon-slot сам по себе не выбирает rune/weapon.

Буквальные пути чтения в этом файле: `armor.id`, `armor.img`, `armor.name`, `armor.system`, `armor.system.canBeRepaired`, `armor.system.description`, `armor.system.encumb`, `armor.system.enhancementItems`, `armor.system.enhancementItems.length`, `armor.system.equipped`, `armor.system.freeEnhancements`, `armor.system.freeEnhancements.length`, `armor.system.quantity`, `armor.system.resistance.bludgeoning`, `armor.system.resistance.piercing`, `armor.system.resistance.slashing`, `armor.system.type`, `armor.system.weight`, `enhancement.id`, `enhancement.img`, `enhancement.name`, `enhancement.system.effects`, `system.quantity`.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 135 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 01,03–04,12,17; реальный Handlebars/модели и обработчики | Три части с SP7/10,5/10,0/10 дали green/orange/red; tooltip левой ноги использовал ключ правой. Пустая ячейка без data-type сформировала выбор glyph. Современная броня имеет quantity при отсутствии hasQuantity. У монстра отрендерены ремонтные кнопки, регистрации listener не найдено. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Весь файл прочитан. Проверены данные рендера и существенные границы, перечисленные выше. Не запускались браузер, серверная запись, DragDrop, реальные броски/производство/ремонт/экспорт или полноценные листы Actor. CSS проверен только до селекторов. Реальный Foundry Document и UI представлены ограниченными фасадами; фактическая регистрация проверена статически. Полные файлы Character/Monster/MountData, валюта/награды и производство остаются за дальнейшими порциями.

## Связанные проблемы

[issue-00007](../../../../../../../../../issues/potential/issue-00007.md), [issue-00063](../../../../../../../../../issues/potential/issue-00063.md), [issue-00081](../../../../../../../../../issues/potential/issue-00081.md), [issue-00084](../../../../../../../../../issues/potential/issue-00084.md), [issue-00089](../../../../../../../../../issues/potential/issue-00089.md), [issue-00168](../../../../../../../../../issues/potential/issue-00168.md), [issue-00171](../../../../../../../../../issues/potential/issue-00171.md), [issue-00175](../../../../../../../../../issues/potential/issue-00175.md), [issue-00177](../../../../../../../../../issues/potential/issue-00177.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003027) |
