# templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.027](../../../../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../../../../review-log.md#task-0003027) |

Актуализация [issue-00001](../../../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Актуализация issue-00330 — 2026-09-16

Версия 14.3.1.00007, dev, база 031fbb8691ad32ab01fad43253c8736071bb2f8b. [Реализация и проверки](../../../../../../../../../issues/open/issue-00330.md#реализация-и-проверки--143100007). Ниже сохранён исторический разбор: его сообщения об исправленных подписях/пропусках относятся к прежнему коду. Механики, технические значения и компедиумы этой правкой не изменены.

Изменённые строки текущего файла:

- `36`: `<span class="item-tag" data-tooltip="{{localize "WITCHER.Item.Availability"}}">`
- `67`: `<span>{{localize "WITCHER.Inventory.containerWeight"}}: {{valuable.system.storedWeight}}</span>`
- `68`: `<span class="bulk-max">{{localize "WITCHER.Inventory.containerCapacity"}}: {{valuable.system.carry}}</span>`


## Назначение файла

Общая таблица ценностей, контейнеров и добычи монстра: количество, переносимость, доступность/скрытность, вес/цена, описание и содержимое контейнера.

## Условия использования

Character передаёт семь групп ценностей/контейнеров; Monster — loots разных Item.type. Наличие полей зависит от модели каждого элемента: например ContainerData не определяет avail/conceal. ../config читается из контекста списка.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| summary/rows:1–33 | Блок HBS | Строки | Рендер через потребителей | quantity всегда; item-chat и item-carried; классы/подсказки по isCarried |
| tags/description:34–58 | Блок HBS | Сведения | Рендер через потребителей | lookup Availability/Concealment, weight/cost, description |
| container:59–95 | Блок HBS | Снимки содержимого | Рендер через потребителей | eq valuable.type container; storedWeight/carry→progress; each itemContent, uuid/name/img/weight/description |

## Основные функции и методы

Собственных JS-функций, экспортов и схем нет. В файле используются each, eq, if, localize, lookup и включения partial. Ветви и поля описаны по блокам выше.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .inline-edit | [itemMixin._onItemInlineEdit](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → data-field/value → Item.update; Number/String очищаются моделью |
| .item-display-info | [itemMixin._onItemDisplayInfo](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → .item-info.toggleClass(invisible) |
| .item-chat | [itemMixin._onItemMessage](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .list-item → item-description → ChatMessage |
| .item-carried | [itemMixin._onItemCarried](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → toggle system.isCarried |

Поля name/data-field, буквально присутствующие в файле: `system.quantity`.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ValuableData/ContainerData | [module/data/item/valuableData.js](../../../../../../../../../../module/data/item/valuableData.js); [module/data/item/containerData.js](../../../../../../../../../../module/data/item/containerData.js) | Схема и prepared-данные | type/isCarried/storedWeight/carry/itemContent | itemContent создаётся resolve UUID в ContainerData, не является ItemDocument |
| Списки ценностей/добычи | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Producer | _prepareValuables/_prepareLoot | В loots могут быть enhancement/components/diagrams/alchemical/mutagen; лишние для модели поля пусты |
| eq | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Системные helpers | Точные вызовы в этом HBS | registerHandelbarHelpers исполнен из исходника; расчёты отделены от UI-записи |
| each, if, localize, lookup | Handlebars 4.7.9 / Foundry VTT 14.367.0 | Внешний шаблонный API | Вызовы в этом HBS; core localize/concat: /opt/foundryvtt/client/applications/handlebars.mjs | Рендер настоящий; game.i18n/окружение представлены фасадом, core helper localize/concat дополнительно исполнены |
| Словари и подписи | [module/setup/config.js](../../../../../../../../../../module/setup/config.js); [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | Контекст и локализация | lookup CONFIG.WITCHER и точные строковые ключи в HBS | 114 статических ключей порции сверены с en/ru; отсутствующие и динамические ключи отражены в issue-00178 |
| Общие поля Item и доступ Document | [module/data/item/commonItemData.js](../../../../../../../../../../module/data/item/commonItemData.js) | Чтение данных | name/id/_id/img у Foundry Document; system.description/quantity/weight/cost/isCarried/isStored/isHidden у модели | quantity StringField; weight/cost NumberField; чтение не означает сохранение |
| Обработчики DOM | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | DOM→JS | Сопоставление ниже в таблице действий | Селекторы и ближайшие контейнеры проверены по реальному шаблону и определениям |
| Контекстное меню Item | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Внешний listener | Ближайшая .item и data-item-id → меню шести действий | Отдельных menu entries HBS не создаёт; неисправные callbacks issue-00168 не переисполнялись |
| partial inventory-items-summary.hbs | [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| Классы списка, details, progress, изображения | [styles/tab-inventory.css](../../../../../../../../../../styles/tab-inventory.css) | CSS/HTML | grid заголовков/строк, stored-item и carry-bar до привязки селекторов | Полный CSS и вид браузера не проверялись; img без src не получает fallback в HBS, assets вне границ анализа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и кеширование пути; не доказательство активного листа | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | partial tab-inventory-valuables.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | partial tab-inventory-valuables.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Вложенный details.stored-item несёт data-item-id=полный UUID, но не класс .item: общие обработчики .item относятся к внешнему контейнеру. Для содержимого нет собственных quantity/edit/delete/drag handlers. weight внутри — вес единицы, а storedWeight сверху уже содержит quantity*weight. Weight/Max Weight записаны английским текстом.

Буквальные пути чтения в этом файле: `storedItem.description`, `storedItem.img`, `storedItem.name`, `storedItem.uuid`, `storedItem.weight`, `system.quantity`, `valuable.id`, `valuable.img`, `valuable.name`, `valuable.system.avail`, `valuable.system.carry`, `valuable.system.conceal`, `valuable.system.cost`, `valuable.system.description`, `valuable.system.isCarried`, `valuable.system.itemContent`, `valuable.system.quantity`, `valuable.system.storedWeight`, `valuable.system.weight`, `valuable.type`.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 101 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 01,09–12,14,16–19; реальный Handlebars/модели и обработчики | Контейнер с двумя единицами по3 вывел storedWeight6/max12, UUID вложенной строки и только один редактируемый quantity контейнера. Неизвестные и отсутствующие avail/conceal дали пустые подписи; известные ключи словарей разрешены. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Исходник и текущие связи сопоставлены в TASK-0004.006. Прежние ссылки на будущий пофайловый разбор TASK-0003 больше не являются очередью: он завершён. Остались конкретные границы сквозной проверки: [U006-01](../../../../../../../cross-check-0002.md#u006-01); [U006-02](../../../../../../../cross-check-0002.md#u006-02); [U006-07](../../../../../../../cross-check-0002.md#u006-07). Weight/Max Weight написаны литералами; Availability указывает отсутствующий ключ.

## Связанные проблемы

[issue-00063](../../../../../../../../../issues/potential/issue-00063.md), [issue-00175](../../../../../../../../../issues/potential/issue-00175.md), [issue-00178](../../../../../../../../../issues/closed/issue-00178.md), [issue-00179](../../../../../../../../../issues/closed/issue-00179.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003027) |

## Сквозная сверка TASK-0004.006

2026-09-14; rusbar-main, a176c4f18879f2e5a63b93bc15345fc26d9f535a. Исходник совпадает со срезом TASK-0001; изменено только описание.

Valuables и контейнеры используют isCarried, quantity и общий item-chat. У container показаны storedWeight/carry и prepared itemContent; вложенный details имеет UUID без .item и собственного inline quantity. Weight/Max Weight написаны литералами; Availability указывает отсутствующий ключ.

Сопоставленные определения и потребители: [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js.md), [module/data/item/containerData.js](../../../../../../module/data/item/containerData.js.md), [templates/sheets/item/container-sheet.hbs](../../../../item/container-sheet.hbs.md), [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004006) — TASK-0004.006; процессы [R006-13](../../../../../../../cross-check-0002.md#r006-13), [R006-17](../../../../../../../cross-check-0002.md#r006-17), [R006-20](../../../../../../../cross-check-0002.md#r006-20). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
