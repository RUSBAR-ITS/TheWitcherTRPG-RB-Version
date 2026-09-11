# templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.027](../../../../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../../../../review-log.md#task-0003027) |

## Назначение файла

Таблица рецептов и формул: количество, learned, кнопка изготовления, параметры производства и требования компонентов с доступным количеством.

## Условия использования

Все 13 групп рецептов из Character используют этот файл. each diagrams имеет текущий Item; ../config и ../alchemyComponentsList — контекст списка, ../../actor из each craftingComponents — Actor. Компонентные UUID разрешаются заранее DiagramData; сам HBS документы по UUID не ищет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| summary/rows:1–37 | Блок HBS | Управление | Рендер через потребителей | quantity, item-chat, item-learned и безусловная crafting-craft; summary наследует itemType, но отдельно не задаёт |
| tags:38–71 | Блок HBS | Параметры | Рендер через потребителей | isFormulae выбирает alchemyDC/craftingDC; TYPES.Item.+type, craftingLevels[level], craftingTime/cost/investment |
| description:72–77 | Блок HBS | HTML | Рендер через потребителей | Тройные скобки description, без enrichHTML в этом файле |
| components:78–109 | Блок HBS | Два списка требований | Рендер через потребителей | craftingComponents: img/name/getOwnedComponentCount ../../actor/quantity. isFormulae: ../alchemyComponentsList, lookup alchemyComponents по key, count и image |

## Основные функции и методы

Собственных JS-функций, экспортов и схем нет. В файле используются concat, each, getOwnedComponentCount, if, localize, lookup, or и включения partial. Ветви и поля описаны по блокам выше.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .inline-edit | [itemMixin._onItemInlineEdit](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → data-field/value → Item.update; Number/String очищаются моделью |
| .item-display-info | [itemMixin._onItemDisplayInfo](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → .item-info.toggleClass(invisible) |
| .item-chat | [itemMixin._onItemMessage](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .list-item → item-description → ChatMessage |
| .item-learned | [itemMixin._onItemLearned](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → toggle system.learned |
| .crafting-craft | [WitcherCharacterSheet._craftingCraft](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | closest .item → диалог Crafting; не переключается по isFormulae |

Поля name/data-field, буквально присутствующие в файле: `system.quantity`.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DiagramData/enrichDiagramComponents | [module/data/item/diagramData.js](../../../../../../../../../../module/data/item/diagramData.js) | Подготовка данных | craftingComponents, isFormulae, learned, DC/level/type | UUID компонента даёт img/name; недоступный UUID оставляет исходную запись |
| getOwnedComponentCount | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Helper | ../../actor, component.name | Вызывает actor.findNeededComponent(name).sum('quantity'); отсутствие Actor→0 с warn |
| findNeededComponent/getSubstance | [module/actor/mixins/craftingMixin.js](../../../../../../../../../../module/actor/mixins/craftingMixin.js) | Косвенный поиск | Количество ресурса для обычного рецепта и вещества | Первый перебирает все actor.items, второй getList исключает stored; имя/локализованное имя вещества, не UUID |
| alchemyComponentsList | [module/actor/sheets/mixins/alchemyMixin.js](../../../../../../../../../../module/actor/sheets/mixins/alchemyMixin.js) | Producer | key/label/image/count для девяти веществ | count берётся из _prepareSubstances контекста Character |
| _craftingCraft/_alchemyCraft | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | DOM→производство | crafting-craft связывается только с _craftingCraft | Даже formula вызывает skill crafting и проверку craftingComponents; полный realCraft вне порции |
| isAlchemicalCraft/realCraft | [module/item/witcherItem.js](../../../../../../../../../../module/item/witcherItem.js) | Дальнейший вызов | Различие выбора навыка и выбора ресурсов | issue-00101 относится к режиму, новый UI-вход описан в issue-00176 |
| getOwnedComponentCount, or | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Системные helpers | Точные вызовы в этом HBS | registerHandelbarHelpers исполнен из исходника; расчёты отделены от UI-записи |
| concat, each, if, localize, lookup | Handlebars 4.7.9 / Foundry VTT 14.367.0 | Внешний шаблонный API | Вызовы в этом HBS; core localize/concat: /opt/foundryvtt/client/applications/handlebars.mjs | Рендер настоящий; game.i18n/окружение представлены фасадом, core helper localize/concat дополнительно исполнены |
| Словари и подписи | [module/setup/config.js](../../../../../../../../../../module/setup/config.js); [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | Контекст и локализация | lookup CONFIG.WITCHER и точные строковые ключи в HBS | 114 статических ключей порции сверены с en/ru; отсутствующие и динамические ключи отражены в issue-00178 |
| Общие поля Item и доступ Document | [module/data/item/commonItemData.js](../../../../../../../../../../module/data/item/commonItemData.js) | Чтение данных | name/id/_id/img у Foundry Document; system.description/quantity/weight/cost/isCarried/isStored/isHidden у модели | quantity StringField; weight/cost NumberField; чтение не означает сохранение |
| Обработчики DOM | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js); [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | DOM→JS | Сопоставление ниже в таблице действий | Селекторы и ближайшие контейнеры проверены по реальному шаблону и определениям |
| Контекстное меню Item | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Внешний listener | Ближайшая .item и data-item-id → меню шести действий | Отдельных menu entries HBS не создаёт; неисправные callbacks issue-00168 не переисполнялись |
| partial inventory-items-summary.hbs | [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| Классы списка, details, progress, изображения | [styles/tab-inventory.css](../../../../../../../../../../styles/tab-inventory.css) | CSS/HTML | grid заголовков/строк, stored-item и carry-bar до привязки селекторов | Полный CSS и вид браузера не проверялись; img без src не получает fallback в HBS, assets вне границ анализа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и кеширование пути; не доказательство активного листа | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | partial tab-inventory-diagrams.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

learned переключается независимо от кнопки изготовления; кнопка присутствует и при learned=false, isFormulae=true. Связанного результата или кнопки associated-diagram здесь нет: UUID используется в данных компонентов, поэтому issue-00080 не воспроизведена этим маршрутом. Объект alchemyComponents со всеми нулями truthy, вследствие чего заголовок Components может существовать без строк. Описания рецепта выводятся HTML, прочие категории обычно экранируют StringField.

Буквальные пути чтения в этом файле: `component.image`, `component.img`, `component.key`, `component.label`, `component.name`, `component.quantity`, `diagram.id`, `diagram.img`, `diagram.name`, `diagram.system.alchemyComponents`, `diagram.system.alchemyDC`, `diagram.system.cost`, `diagram.system.craftingComponents`, `diagram.system.craftingDC`, `diagram.system.craftingTime`, `diagram.system.description`, `diagram.system.investment`, `diagram.system.isFormulae`, `diagram.system.learned`, `diagram.system.level`, `diagram.system.quantity`, `diagram.system.type`, `system.quantity`.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 114 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 01,07,14–16,19; реальный Handlebars/модели и обработчики | Реальный helper получил Actor и вывел 6/3, включая stored-компонент; вещество — 5/2 через count. Обычный режим исключил алхимические строки. Формула при CRA5/crafting2/alchemy8 передала realCraft формулу с 5+2; нажатие не проверило пять недостающих vitriol. Запись ресурсов заменена фасадом. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Весь файл прочитан. Проверены данные рендера и существенные границы, перечисленные выше. Не запускались браузер, серверная запись, DragDrop, реальные броски/производство/ремонт/экспорт или полноценные листы Actor. CSS проверен только до селекторов. Реальный Foundry Document и UI представлены ограниченными фасадами; фактическая регистрация проверена статически. Полные файлы Character/Monster/MountData, валюта/награды и производство остаются за дальнейшими порциями.

## Связанные проблемы

[issue-00080](../../../../../../../../../issues/potential/issue-00080.md), [issue-00101](../../../../../../../../../issues/potential/issue-00101.md), [issue-00176](../../../../../../../../../issues/potential/issue-00176.md), [issue-00178](../../../../../../../../../issues/potential/issue-00178.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003027) |
