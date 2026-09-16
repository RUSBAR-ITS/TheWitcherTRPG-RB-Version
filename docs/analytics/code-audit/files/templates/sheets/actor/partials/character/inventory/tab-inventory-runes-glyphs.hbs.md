# templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.027](../../../../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../../../../review-log.md#task-0003027) |

Актуализация [issue-00001](../../../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Таблица свободных рун/глифов: количество, тип, вес, стоимость, названия воздействий и процент наложения статусов.

## Условия использования

Общий ActorSheet выделяет unapplied enhancement, затем type=rune/glyph. Character включает соответствующие списки. applied отбирает producer, этот partial не скрывает переданный Item сам.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| summary/rows:1–27 | Блок HBS | Список | Рендер через потребителей | enhancements; summary header/itemType/hasQuantity, img/name/quantity/chat |
| tags/effects:28–62 | Блок HBS | Данные улучшений | Рендер через потребителей | type/weight/cost truthy; each effects, percentage>0→statusEffect и %, все name отдельным списком |

## Основные функции и методы

Собственных JS-функций, экспортов и схем нет. В файле используются each, gt, if, localize и включения partial. Ветви и поля описаны по блокам выше.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .inline-edit | [itemMixin._onItemInlineEdit](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → data-field/value → Item.update; Number/String очищаются моделью |
| .item-display-info | [itemMixin._onItemDisplayInfo](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → .item-info.toggleClass(invisible) |
| .item-chat | [itemMixin._onItemMessage](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .list-item → item-description → ChatMessage |

Поля name/data-field, буквально присутствующие в файле: `system.quantity`.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| EnhancementData/itemEffect | [module/data/item/enhancementData.js](../../../../../../../../../../module/data/item/enhancementData.js); [module/data/item/templates/itemEffectData.js](../../../../../../../../../../module/data/item/templates/itemEffectData.js) | Схемы Item | effects — TypedObjectField; statusEffect/name/percentage | Словарь each работает; name экранируется, statusEffect не локализуется |
| gt | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Системные helpers | Точные вызовы в этом HBS | registerHandelbarHelpers исполнен из исходника; расчёты отделены от UI-записи |
| each, if, localize | Handlebars 4.7.9 / Foundry VTT 14.367.0 | Внешний шаблонный API | Вызовы в этом HBS; core localize/concat: /opt/foundryvtt/client/applications/handlebars.mjs | Рендер настоящий; game.i18n/окружение представлены фасадом, core helper localize/concat дополнительно исполнены |
| Словари и подписи | [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | Контекст и локализация | Точные строковые ключи localize в HBS | 114 статических ключей порции сверены с en/ru; отсутствующие и динамические ключи отражены в issue-00178 |
| Общие поля Item и доступ Document | [module/data/item/commonItemData.js](../../../../../../../../../../module/data/item/commonItemData.js) | Чтение данных | name/id/_id/img у Foundry Document; system.description/quantity/weight/cost/isCarried/isStored/isHidden у модели | quantity StringField; weight/cost NumberField; чтение не означает сохранение |
| Обработчики DOM | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | DOM→JS | Сопоставление ниже в таблице действий | Селекторы и ближайшие контейнеры проверены по реальному шаблону и определениям |
| Контекстное меню Item | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Внешний listener | Ближайшая .item и data-item-id → меню шести действий | Отдельных menu entries HBS не создаёт; неисправные callbacks issue-00168 не переисполнялись |
| partial inventory-items-summary.hbs | [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| Классы списка, details, progress, изображения | [styles/tab-inventory.css](../../../../../../../../../../styles/tab-inventory.css) | CSS/HTML | grid заголовков/строк, stored-item и carry-bar до привязки селекторов | Полный CSS и вид браузера не проверялись; img без src не получает fallback в HBS, assets вне границ анализа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и кеширование пути; не доказательство активного листа | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | partial tab-inventory-runes-glyphs.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Применение к оружию/броне выполняется через их свободные ячейки, собственной кнопки equip у руны/глифа нет. Отображение названий/процентов не означает вызов applyStatus. Строковый statusEffect показан непосредственно; это значение конфигурации, не разрешённый здесь ID ActiveEffect.

Буквальные пути чтения в этом файле: `enhancement.id`, `enhancement.img`, `enhancement.name`, `enhancement.system.cost`, `enhancement.system.effects`, `enhancement.system.quantity`, `enhancement.system.type`, `enhancement.system.weight`, `system.quantity`.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 67 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 01,04,11,17; реальный Handlebars/модели и обработчики | Словарь двух эффектов: statusEffect с 25% показан, при 0% не показан процент; оба имени присутствуют. Установки/лечения/наложения статусов не исполнялись. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Исходник и текущие связи сопоставлены в TASK-0004.006. Прежние ссылки на будущий пофайловый разбор TASK-0003 больше не являются очередью: он завершён. Остались конкретные границы сквозной проверки: [U006-01](../../../../../../../cross-check-0002.md#u006-01); [U006-03](../../../../../../../cross-check-0002.md#u006-03). Отображение записи не означает применение эффекта; quantity меняет Item, а установку выполняет отдельный chooser.

## Связанные проблемы

[issue-00063](../../../../../../../../../issues/potential/issue-00063.md), [issue-00084](../../../../../../../../../issues/potential/issue-00084.md), [issue-00089](../../../../../../../../../issues/potential/issue-00089.md), [issue-00168](../../../../../../../../../issues/potential/issue-00168.md), [issue-00171](../../../../../../../../../issues/potential/issue-00171.md), [issue-00175](../../../../../../../../../issues/potential/issue-00175.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003027) |

## Сквозная сверка TASK-0004.006

2026-09-14; rusbar-main, a176c4f18879f2e5a63b93bc15345fc26d9f535a. Исходник совпадает со срезом TASK-0001; изменено только описание.

Runes/glyphs получают not-applied Enhancement Items из подготовки листа. Each корректно читает TypedObject effects: percentage>0 выводит statusEffect/процент, name остаётся при нуле. Отображение записи не означает применение эффекта; quantity меняет Item, а установку выполняет отдельный chooser.

Сопоставленные определения и потребители: [module/actor/sheets/mixins/itemMixin.js](../../../../../../module/actor/sheets/mixins/itemMixin.js.md), [module/data/item/armorData.js](../../../../../../module/data/item/armorData.js.md), [module/data/item/enhancementData.js](../../../../../../module/data/item/enhancementData.js.md), [module/data/item/weaponData.js](../../../../../../module/data/item/weaponData.js.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004006) — TASK-0004.006; процессы [R006-11](../../../../../../../cross-check-0002.md#r006-11), [R006-17](../../../../../../../cross-check-0002.md#r006-17). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
