# templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs

## Актуализация 2026-09-19 — 14.3.1.00115

Ввод system.quantity сделан числовым: type=number,min=0,step=1,required; значение берётся из CommonItemData.quantity. Обработчик sheet.itemMixin._onItemInlineEdit проверяет целое неотрицательное значение до Item.update, отклоняя пустой/дробный ввод. Расположение остальных колонок и действия предметов сохранены.

[Результаты107 статических проверок и границы](../../../../../../../../task-0011-static-checks.md#quantity-installed-00115). Ниже сохранён исходный пофайловый аудит на его дату; при расхождении текущий контракт описан выше.

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.027](../../../../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../../../../review-log.md#task-0003027) |

Актуализация [issue-00001](../../../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Таблица компонентов: количество, тип, редкость, добываемое количество, сложность сбора, вес/цена и место нахождения.

## Условия использования

Вкладка персонажа передаёт alchemicalTreatments/craftingMaterials/ingotsAndMinerals/hidesAndAnimalParts. substances.hbs включает тот же шаблон для девяти веществ с itemType=component и subtype. Summary получает subtype, но не выводит соответствующий data-атрибут.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| summary/rows:1–27 | Блок HBS | Заголовок и действия | Рендер через потребителей | header/itemType/subtype/hasQuantity; количество, описание и чат |
| tags/location:28–70 | Блок HBS | Сведения о компоненте | Рендер через потребителей | type/rarity/quantityObtainable/forage/weight/cost truthy; location выводится всегда |

## Основные функции и методы

Собственных JS-функций, экспортов и схем нет. В файле используются each, if, localize и включения partial. Ветви и поля описаны по блокам выше.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .inline-edit | [itemMixin._onItemInlineEdit](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → data-field/value → Item.update; Number/String очищаются моделью |
| .item-display-info | [itemMixin._onItemDisplayInfo](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → .item-info.toggleClass(invisible) |
| .item-chat | [itemMixin._onItemMessage](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .list-item → item-description → ChatMessage |

Поля name/data-field, буквально присутствующие в файле: `system.quantity`.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ComponentData | [module/data/item/componentData.js](../../../../../../../../../../module/data/item/componentData.js) | Схема Item | type/rarity/quantityObtainable/forage/location/substanceType | Строковые 0 отображаются как truthy; weight/cost — числовые общие поля |
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
| [templates/partials/character/substances.hbs](../../../../../../../../../../templates/partials/character/substances.hbs) | partial tab-inventory-components.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | partial tab-inventory-components.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

data-field=system.quantity относится к ближайшей .item, ввод text/data-dtype=Number передаётся обработчику. itemType/subtype управляют созданием, не фильтрацией текущих строк. Строка location не является редактируемым полем этого шаблона.

Буквальные пути чтения в этом файле: `component.id`, `component.img`, `component.name`, `component.system.cost`, `component.system.forage`, `component.system.location`, `component.system.quantity`, `component.system.quantityObtainable`, `component.system.rarity`, `component.system.type`, `component.system.weight`, `system.quantity`.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 75 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 01,06,10–11,17; реальный Handlebars/модели и обработчики | Проверены 0/1/2 строки, quantity='0', rarity/forage='0', location. subtype=vitriol дошёл до summary-контекста, но отсутствует на кнопке. Открытие девяти панелей восстановило девять скрытых списков в полном контексте. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Исходник и текущие связи сопоставлены в TASK-0004.006. Прежние ссылки на будущий пофайловый разбор TASK-0003 больше не являются очередью: он завершён. Остались конкретные границы сквозной проверки: [U006-01](../../../../../../../cross-check-0002.md#u006-01); [U006-04](../../../../../../../cross-check-0002.md#u006-04). Подтип передан partial-контекстом, но отсутствует в summary dataset; ручной add создаёт общий component.

## Связанные проблемы

[issue-00063](../../../../../../../../../issues/potential/issue-00063.md), [issue-00173](../../../../../../../../../issues/potential/issue-00173.md), [issue-00175](../../../../../../../../../issues/potential/issue-00175.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003027) |

## Уточнение TASK-0003.034

2026-09-11, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`. Теперь полностью описан верхний substances: все девять вызовов передают components, itemType=component, subtype, header и hasQuantity. Полный рендер дал десять строк по девяти группам, stored исключён producer. Подтип доходит в summary-контекст, но не в DOM-кнопку (issue-00173).

Связи: [templates/partials/character/substances.hbs](../../../../../partials/character/substances.hbs.md). [Результаты и пределы проверки](../../../../../../../review-log.md#task-0003034).

## Сквозная сверка TASK-0004.006

2026-09-14; rusbar-main, a176c4f18879f2e5a63b93bc15345fc26d9f535a. Исходник совпадает со срезом TASK-0001; изменено только описание.

Компоненты выводят type/rarity/forage/quantityObtainable/location, общий quantity и item-chat. Строковый '0' отличается по truthiness от числового0. Подтип передан partial-контекстом, но отсутствует в summary dataset; ручной add создаёт общий component.

Сопоставленные определения и потребители: [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](inventory-items-summary.hbs.md), [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](tab-inventory-alchemical.hbs.md), [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](tab-inventory-armors.hbs.md), [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](tab-inventory-mounts.hbs.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004006) — TASK-0004.006; процессы [R006-17](../../../../../../../cross-check-0002.md#r006-17), [R006-18](../../../../../../../cross-check-0002.md#r006-18). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
