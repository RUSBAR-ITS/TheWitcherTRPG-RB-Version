# module/item/sheets/WitcherDiagramSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../module/item/sheets/WitcherDiagramSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../review-log.md#task-0003016) |

## Назначение файла

Редактор рецепта: контекст известных/ручных компонентов, категории формул и чертежей, список материалов и связь с результатом изготовления.

## Условия использования

Зарегистрирован как makeDefault для Item type=diagrams. _prepareContext вызывается при рендере; базовый WitcherItemSheet._onRender после Core/DragDrop вызывает override activateListeners. Собственной configuration нет — остаётся общая WitcherConfigurationSheet.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherDiagramSheet | default class extends WitcherItemSheet | Лист diagrams | Регистрация registerSheets | Контекст, рендер, события |
| PARTS.main | static object | diagrams-sheet.hbs; scrollable=[''] | HBM | Основная форма |
| knownCraftingComponents | Массив контекста | Записи с truthy uuid | _prepareContext | id записи + spread fromUuidSync + quantity |
| unknownCraftingComponents | Массив контекста | Записи без uuid | _prepareContext | Оригинальные записи модели |
| selects.formulaTypes / selects.diagramTypes | Словари контекста | 4 вида формул / 9 видов рецептов | createSelects | Выбор system.type |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options) | Контекст super; craftingComponents массив | context | filter по наличию uuid; map доступных/недоступных UUID; createSelects | fromUuidSync без catch; объект слева ?? всегда существует, резервная component недостижима |
| createSelects() | Без аргументов | Два словаря | formulaTypes: alchemical/potion/decoction/oil; diagramTypes: ingredients/weapon/armor/armor-enhancement/elderfolk-weapon/elderfolk-armor/ammunition/bomb/traps | Ключи локализации; schema.type не имеет choices |
| activateListeners(html) | DOM основной формы | undefined | super; .add-component click, .edit-component blur, .remove-component click, .remove-associated-item click | Слушатели через bind(this); нет add-associated-item handler |
| async _onDropItem(event, item) | Item от базового drop; event.target.offsetParent | Promise<void> | Если offsetParent.dataset.type==associatedItem: update UUID результата; иначе push {name,quantity:1,uuid} в материалы | Не проверяет тип компонента/результата; null offsetParent бросает; update не await/return |
| _onEditComponent(event) | closest.list-item.dataset.id; data-field; value | undefined | findIndex по obj.id; присваивает поле; update всего массива | Количество передаётся строкой; ID должен существовать; prepared-массив меняется до update |
| _onAddComponent(event) | preventDefault | undefined | push {name:'component',quantity:''}; update массива | id создаёт модель при очистке; quantity=''→null в опыте |
| _onRemoveComponent(event) | ID строки из DOM | undefined | filter по item.id!==id; update нового массива | Не await; UUID связанного Item не удаляет |
| async _onRemoveAssociatedItem(event) | preventDefault | Promise<void> | update system.associatedItemUuid='' | Не await; не меняет resultQuantity и обратную ссылку результата |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Прямой импорт / наследование | Контекст, Item drop, вызов activateListeners и submit | Определение и обращение сверены |
| diagrams-sheet.hbs | [templates/sheets/item/diagrams-sheet.hbs](../../../../../../../templates/sheets/item/diagrams-sheet.hbs) | PARTS.main.template | Форма и классы событий | Определение и обращение сверены |
| DiagramData / craftingComponent() | [module/data/item/diagramData.js](../../../../../../../module/data/item/diagramData.js); [module/data/item/templates/craftingComponentData.js](../../../../../../../module/data/item/templates/craftingComponentData.js) | Контракт модели | Массив строк, ID/UUID, resultQuantity | Определение и обращение сверены |
| fromUuidSync | Foundry 14.367: /opt/foundryvtt/client/utils/helpers.mjs:188 | Глобальный API | Разрешение известных компонентов | Определение и обращение сверены |
| Item.update / DOM | Foundry и браузерные API | Внешний API | Запись и события | Определение и обращение сверены |
| WITCHER.Alchemy.* / WITCHER.Diagram.* | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | 4/9 вариантов категорий | Определение и обращение сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherDiagramSheet | Импорт/регистрация diagrams | makeDefault |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../../../templates/sheets/item/diagrams-sheet.hbs) | knownCraftingComponents/unknownCraftingComponents/selects; обработчики | Представление и события | Пути и классы |
| [templates/partials/associated-item.hbs](../../../../../../../templates/partials/associated-item.hbs) | _onRemoveAssociatedItem / _onDropItem | Удаление и область associatedItem | Включение из main |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Внутренний ID строки не совпадает с UUID связанного Item. С настоящим BaseItem его id — getter и не попадает в spread, поэтому id строки сохранён; name/img/type берутся из перечислимых свойств Item. Spread также копирует другие поля документа, но этот объект служит только контекстом. Недоступный fromUuidSync возвращает null; map всё равно создаёт {id,quantity}, теряя сохранённое имя из модели. Такие записи остаются known, а не unknown.

Редактирование/добавление/drop передают весь подготовленный craftingComponents; создаваемые id и типы полей проверяет модель. Изменение quantity '4' очистилось в 4, добавление пустой строки — в null. Повторный drop того же Item создал две отдельные строки. Для результата разрешён любой Item, который передал базовый drop; ограничений на document.type/subtype здесь нет. Очистка ссылки запрашивает update, но не удаляет связанный документ.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст | Настоящие модели и BaseItem; доступный, отсутствующий и пустой UUID | Два known/один unknown; ID сохранён; у недоступного known нет name/img | UUID-карта, не реальный pack |
| CRUD | Реальные методы и последующая очистка payload DiagramData | Add генерирует id; edit меняет 2→4; remove удаляет только row1; повторные UUID имеют разные ID | update/DOM фасады |
| Drop/удаление связи | associatedItem/другая область/null; два удаления | UUID результата или новая строка; null даёт TypeError; clear='' | Геометрия реального DOM не проверена |
| Listener chain | Настоящий базовый _onRender и override | click/blur/click/click зарегистрированы | Без браузера |
| Формы | Настоящий HBS с двумя режимами и связанным результатом | 12/20 именованных полей; editor представлен отдельным фасадом | Не полный submit |

## Непроверенные участки и открытые вопросы

Не запускались полный клиент/БД, Item.fromDropData и реальный файловый/компедиумный picker. Ошибку offsetParent не следует считать воспроизведённой на конкретной браузерной цели. Посторонний ID/удаление строки другим окном не моделировались. Формирование known через spread с настоящим BaseItem не доказывает все варианты индекса пакета.

## Связанные проблемы

[issue-00095](../../../../../../issues/potential/issue-00095.md), [issue-00080](../../../../../../issues/potential/issue-00080.md), [issue-00098](../../../../../../issues/potential/issue-00098.md), [issue-00096](../../../../../../issues/potential/issue-00096.md), [issue-00101](../../../../../../issues/potential/issue-00101.md). Потеря имени, общий риск offsetParent, подписи и представление результата; режим crafting определяется другим кодом.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
