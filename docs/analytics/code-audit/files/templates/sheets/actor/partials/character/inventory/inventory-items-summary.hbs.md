# templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.027](../../../../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../../../../review-log.md#task-0003027) |

## Назначение файла

Общий фрагмент заголовка списков: шеврон, header, условные подписи урона/надёжности/STA/количества и кнопка создания Item. Суммирование веса/цены/количества здесь отсутствует.

## Условия использования

Подключается восемью категориями инвентаря и spell-type-list.hbs. Hash partial добавляет поля к унаследованному контексту; непереданный явно hasQuantity/spellType может оставаться доступным. Содержит только внутреннюю разметку summary, не собственный details.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| 1–3 | Блок HBS | Шеврон/header | Рендер через потребителей | Статическая иконка и h3 |
| 4–15 | Блок HBS | Четыре независимых флага | Рендер через потребителей | hasDamage/hasReliability/hasStaCost/hasQuantity |
| 16–23 | Блок HBS | Кнопка | Рендер через потребителей | if itemType; data-itemType={{itemType}}, data-spellType={{spellType}}; subtype отсутствует |

## Основные функции и методы

Собственных JS-функций, экспортов и схем нет. В файле используются if, localize. Ветви и поля описаны по блокам выше.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .add-item | [itemMixin._onItemAdd](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | dataset.itemtype/spelltype/subtype → Item.create({parent:actor}) |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| _onItemAdd/itemListener | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | DOM→создание | add-item с lowercase dataset.itemtype/spelltype | HTML parser понижает буквы имён атрибутов; subtype не появляется из контекста автоматически |
| if, localize | Handlebars 4.7.9 / Foundry VTT 14.367.0 | Внешний шаблонный API | Вызовы в этом HBS; core localize/concat: /opt/foundryvtt/client/applications/handlebars.mjs | Рендер настоящий; game.i18n/окружение представлены фасадом, core helper localize/concat дополнительно исполнены |
| Словари и подписи | [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | Контекст и локализация | Точные строковые ключи localize в HBS | 114 статических ключей порции сверены с en/ru; отсутствующие и динамические ключи отражены в issue-00178 |
| Обработчики DOM | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | DOM→JS | Сопоставление ниже в таблице действий | Селекторы и ближайшие контейнеры проверены по реальному шаблону и определениям |
| Классы списка, details, progress, изображения | [styles/tab-inventory.css](../../../../../../../../../../styles/tab-inventory.css) | CSS/HTML | grid заголовков/строк, stored-item и carry-bar до привязки селекторов | Полный CSS и вид браузера не проверялись; img без src не получает fallback в HBS, assets вне границ анализа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и кеширование пути; не доказательство активного листа | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | partial inventory-items-summary.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | partial inventory-items-summary.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | partial inventory-items-summary.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | partial inventory-items-summary.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | partial inventory-items-summary.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs) | partial inventory-items-summary.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | partial inventory-items-summary.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | partial inventory-items-summary.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | partial inventory-items-summary.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

has* задают наличие подписей, не фильтруют строки и не определяют поля модели. itemType управляет только наличием плюсика. Раскрытие details — штатное действие HTML. Нажатие плюсика обрабатывается itemMixin, но поведение всплытия/браузера здесь не проверялось.

Системные поля Item/Actor непосредственно в этом фрагменте не читаются; входы header/has*/itemType/spellType описаны выше.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 23 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 01,06,18; реальный Handlebars/модели и обработчики | Все 32 сочетания четырёх флагов и itemType скомпилированы/отрендерены. spellType=spellMaster сохранён в data-spelltype; subtype=vitriol не имеет DOM-атрибута. При itemType отсутствующем кнопки нет. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Весь файл прочитан. Проверены данные рендера и существенные границы, перечисленные выше. Не запускались браузер, серверная запись, DragDrop, реальные броски/производство/ремонт/экспорт или полноценные листы Actor. CSS проверен только до селекторов. Реальный Foundry Document и UI представлены ограниченными фасадами; фактическая регистрация проверена статически. Полные файлы Character/Monster/MountData, валюта/награды и производство остаются за дальнейшими порциями.

## Связанные проблемы

[issue-00173](../../../../../../../../../issues/potential/issue-00173.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003027) |

## Уточнение TASK-0003.034

2026-09-11, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`. Полный вход substances→components→summary подтверждён рендером. Кнопка имеет data-itemtype=component, data-subtype отсутствует; настоящий _onItemAdd с полученными атрибутами создаёт system.type=component. Отсутствие подтипа не связано с потерей HBS-контекста.

Связи: [templates/partials/character/substances.hbs](../../../../../partials/character/substances.hbs.md). [Результаты и пределы проверки](../../../../../../../review-log.md#task-0003034).
