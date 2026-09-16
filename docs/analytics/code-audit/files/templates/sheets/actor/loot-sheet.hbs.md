# templates/sheets/actor/loot-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/loot-sheet.hbs](../../../../../../../templates/sheets/actor/loot-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.035](../../../../../../tasks/task-0003.035.md), 6 файлов, 384 логические строки |
| Запись перекрёстной сверки | [TASK-0003.035](../../../../review-log.md#task-0003035) |

Актуализация [issue-00001](../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Основная форма Actor loot: название, грузоподъёмность/вес, место общей стоимости, изображение, семь валют и шесть таблиц предметов.

## Условия использования

WitcherLootSheet.PARTS.main; также preloadHandlebarTemplates. Не шаблон общего WitcherActorSheet. Все таблицы присутствуют и при пустых массивах. data-itemType у add-item в HTML приводится к dataset.itemtype и читается jQuery listener.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.scrollable / name / system.maxWeight | 1–25 | Имя и предел веса | Форма Actor | SubmitOnChange; весовой блок только maxWeight>0 |
| totalWeight / totalCost / actor.img | 3–34 | Вес, стоимость и изображение | Контекст Loot | totalCost отсутствует; img имеет data-edit, без data-action |
| system.currency.bizant/ducat/lintar/floren/crown/oren/falsecoin | 39–73 | Семь числовых остатков | Форма, data-dtype Number | Прямая запись без обмена |
| weapons/armors/valuables/allComponents/enhancements/loot | 76–128 | Шесть таблиц | each + partial | Первые пять заголовков имеют add-item; общий loot не имеет кнопки добавления |
| weightbar/weightbar-overweight | 9–14 | Визуальный предел | if gte / lt | При равенстве уже overweight; HTML не ограничивает получение Item |

## Основные функции и методы

JS-функций нет. Handlebars localize/if/gt/gte/lt/each строят форму; шесть вызовов одного partial передают item и isGM=../isGM. Сохранение name/maxWeight/currency наследуется от DocumentSheetV2. Подразумеваемая cost-строка не выполняет вычислений. Item-поля строк сохраняются отдельными inline handlers, не общей формой.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| контекст _prepareContext | [module/actor/sheets/WitcherLootSheet.js](../../../../../../../module/actor/sheets/WitcherLootSheet.js) | producer | Все поля/массивы | 44–66; context.totalCost отсутствует |
| loot-item-display | [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../../../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) | шесть literal partial calls | 89,97,104,111,119,125 | item=item isGM=../isGM |
| LootData / currency() | [module/data/actor/lootData.js](../../../../../../../module/data/actor/lootData.js); [module/data/actor/templates/common/currencyData.js](../../../../../../../module/data/actor/templates/common/currencyData.js) | пути полей | system.maxWeight/currency | Схемы NumberField, нет запрета отрицательного maxWeight |
| _onItemAdd / itemListener | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | jQuery .add-item | 76,92,100,107,116 | 61–102 и313–315; type weapon/armor/valuable/component/enhancement |
| localize / if / each / gt / gte / lt | Foundry Handlebars helpers + Handlebars | условия/повтор | 1–130 | Изолированный настоящий рендер; generic helper registration |
| WITCHER.Loot.*, WITCHER.Currency.*, WITCHER.table.*, WITCHER.Item.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | локализация | Подписи | 29 ключей всей порции, раскрытые dotted paths |
| .left-loot-border/.loot-img/.table-empty-* | [styles/loot-sheet.css](../../../../../../../styles/loot-sheet.css) | CSS | 8–34 и таблицы | Подключён styles/witcher-styles.css; полная карточка CSS не создавалась |
| DocumentSheetV2 form/editImage | Foundry /opt/foundryvtt/client/applications/api/document-sheet.mjs | внешнее сохранение и image action | name/system.*, img[data-edit] | Ядро сохраняет форму при editable; editImage требуется data-action, которого здесь нет |
| .currency / .wrapper / .weightbar / .weight-value / .weightbar-overweight / .item-table td | [styles/tab-inventory.css](../../../../../../../styles/tab-inventory.css); [styles/system-styles.css](../../../../../../../styles/system-styles.css); [styles/item-sheets.css](../../../../../../../styles/item-sheets.css); [styles/witcher-styles.css](../../../../../../../styles/witcher-styles.css) | CSS-зависимости | Вес, валюты и таблицы | currency67–71; wrapper/weight180–190; overweight343–347; item-table79–82; центральные @import4,7,15 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherLootSheet.js](../../../../../../../module/actor/sheets/WitcherLootSheet.js) | loot-sheet.hbs | PARTS.main23 | Активный лист |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | loot-sheet.hbs | preload4 | Загрузка partial не отдельный лист |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

HBS не изменяет модель. Для пустого loot рендерится шесть таблиц и семь валютных input; totalCost пуст. При weight6/max6 появляется overweight, max7 — progress, max0 — без шкалы. В режиме observer ядро отключает поля, но anchors add/buy/delete остаются в разметке; права записи не следуют из их присутствия.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Рендер контекста | 02–04,19,23 | Пустой/смешанный loot, весовые пороги, отсутствие image action, disabled полей | Без DOM событий/браузерного вида |
| Сохранение/локализация | Схемы, core form,25 | Прямые поля name/maxWeight/currency; EN/RU | Server update не выполнялся |

## Непроверенные участки и открытые вопросы

Полный клиентский render, скрытие/редактирование картинки и права — [U014-01](../../../../cross-check-0002.md#u014-01); завершение покупки/записи — [U014-02](../../../../cross-check-0002.md#u014-02). Доступ по старому systems/TheWitcherTRPG пути не проверялся через HTTP.

## Связанные проблемы

[issue-00219](../../../../../../issues/potential/issue-00219.md), [issue-00224](../../../../../../issues/potential/issue-00224.md). Данные hidden Item не исключаются этим шаблоном; CSS скрывает строку в partial. Проблемы покупки и drag подробно у producer/строки, без повторных ID.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003035) |

## Дополнительная сверка TASK-0003.036

2026-09-11, `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; исходники не менялись.

Отдельный HBS loot показывает семь денежных полей, но не имеет .open-currency-converter. У него прямое сохранение остатков/покупка; конвертер имеет свой отдельный шаблон/курсы. Не переносить гарантию await update конвертера на четыре независимые записи _onItemBuy из .035.

Карточки процесса: [module/actor/mixins/currencyConverterMixin.js](../../../module/actor/mixins/currencyConverterMixin.js.md), [module/actor/sheets/mixins/currencyConverterMixin.js](../../../module/actor/sheets/mixins/currencyConverterMixin.js.md), [templates/sheets/actor/currencyConverter/currencyConverter.hbs](currencyConverter/currencyConverter.hbs.md), [templates/chat/currency-conversion.hbs](../../chat/currency-conversion.hbs.md).

[Проверки и перекрёстная сверка](../../../../review-log.md#task-0003036). Связанный файл повторно в покрытии не учитывается; правок системы нет.

## Сквозная сверка TASK-0004.014

2026-09-14; rusbar-main, 8256dd3473347494fefb30524700fe7ca1daf75d. Исходник совпадает со срезом TASK-0001; изменено только описание.

Все шесть each подключают один partial с item/isGM; add-item есть для пяти специальных категорий. Форма редактирует maxWeight и семь валют напрямую. Вес подготовлен LootSheet, totalCost нет. loot-img[data-edit] не имеет editImage action. Покупка не конвертирует валюту и не вызывает журнал наград; эти отдельные маршруты сверены в этой порции.

Сопоставленные определения и потребители: [module/actor/sheets/WitcherLootSheet.js](../../../module/actor/sheets/WitcherLootSheet.js.md), [templates/sheets/actor/partials/loot/loot-item-display.hbs](partials/loot/loot-item-display.hbs.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/setup/registerDataModels.js](../../../module/setup/registerDataModels.js.md), [module/data/actor/lootData.js](../../../module/data/actor/lootData.js.md), [module/data/item/commonItemData.js](../../../module/data/item/commonItemData.js.md), [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js.md), [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js.md), [module/actor/sheets/interactions/itemContextMenu.js](../../../module/actor/sheets/interactions/itemContextMenu.js.md), [styles/loot-sheet.css](../../../styles/loot-sheet.css.md), [templates/partials/item-header.hbs](../../partials/item-header.hbs.md), [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js.md), [module/item/witcherItem.js](../../../module/item/witcherItem.js.md).

[Протокол и границы](../../../../review-log.md#task-0004014) — TASK-0004.014; процессы [R014-02](../../../../cross-check-0002.md#r014-02), [R014-03](../../../../cross-check-0002.md#r014-03), [R014-04](../../../../cross-check-0002.md#r014-04), [R014-05](../../../../cross-check-0002.md#r014-05), [R014-24](../../../../cross-check-0002.md#r014-24). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
