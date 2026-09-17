# templates/sheets/item/diagrams-sheet.hbs

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../../issues/closed/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Строки компонентов рецепта.

**Основные методы, сущности и действия:** Недоступный компонент сохраняет uuid/id/quantity и редактируемое сохранённое имя; виден локализованный признак отсутствия.

**Зависимости и потребители:** WitcherDiagramSheet._prepareContext/_onEditComponent; linkedItemContext; WITCHER.LinkedItem.unavailable.

## Предыдущий срез анализа

Датированные сведения ниже относятся к прежнему коду. При расхождении приоритет имеет актуальный раздел выше.

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/diagrams-sheet.hbs](../../../../../../../templates/sheets/item/diagrams-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.016](../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../review-log.md#task-0003016) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Актуализация issue-00330 — 2026-09-16

Версия 14.3.1.00007, dev, база 031fbb8691ad32ab01fad43253c8736071bb2f8b. [Реализация и проверки](../../../../../../issues/closed/issue-00330.md#реализация-и-проверки--143100007). Ниже сохранён исторический разбор: его сообщения об исправленных подписях/пропусках относятся к прежнему коду. Механики, технические значения и компедиумы этой правкой не изменены.

Изменённые строки текущего файла:

- `94`: `<th><a class="add-component" title="{{localize "WITCHER.Item.AddComponent"}}"><i`
- `103`: `<a class="remove-component" title="{{localize "WITCHER.Item.RemoveComponent"}}"><i`
- `121`: `<a class="remove-component" title="{{localize "WITCHER.Item.RemoveComponent"}}"><i`


## Назначение файла

Основная форма рецепта/формулы: режим, категория, сложности, время, инвестиции, результат, описание и два представления списка материалов.

## Условия использования

PARTS.main WitcherDiagramSheet. Включает item-header и associated-item; контекст item/config/selects/knownCraftingComponents/unknownCraftingComponents приходит от листа.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section / два partial | HTML | Шапка и результат изготовления | PARTS.main | Рендер |
| isFormulae/type/level | Checkbox и два select | Режим, категория, уровень | system | Изменение формы |
| alchemyDC/craftingDC | Взаимоисключающие text inputs, data-dtype=Number | Выбор по isFormulae | system | Сложность |
| craftingTime / investment | Text inputs; investment только не-формула | Время и инвестиции | system | investment с data-dtype=Number |
| description | editor target=system.description | Rich-text редактор | Данные Item / editable | UI Foundry |
| alchemyComponents.* | 9 number inputs и иконки | Требования vitriol/rebis/aether/quebrith/hydragenum/vermilion/sol/caelum/fulgur | Только isFormulae | Редактирование чисел |
| knownCraftingComponents | each / строки list-item | img/name и quantity; id строки | Контекст листа | name — span, quantity — input |
| unknownCraftingComponents | each / строки list-item | Редактируемые name/quantity | Контекст листа | data-id / data-field |
| add-component/remove-component/edit-component | CSS-классы действий | Добавление, удаление, blur-редактирование | activateListeners листа | Ручное обновление массива |

## Основные функции и методы

JavaScript-функций нет. if/unless isFormulae выбирают словарь типа, поле DC, инвестиции и алхимическую таблицу. Список craftingComponents остаётся видимым в обоих режимах. selectOptions использует selects.formulaTypes/diagramTypes и config.craftingLevels; оба select имеют id=type-select. Данные компонентов не имеют form name: их пишет listener по blur. У known имя выведено span.edit-component без data-field, а количество — input[data-field=quantity]. У unknown редактируются name и quantity.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherDiagramSheet | [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../module/item/sheets/WitcherDiagramSheet.js) | Контекст / события | PARTS, списки, словари, четыре listeners | Источник и использование сверены |
| DiagramData / craftingComponent | [module/data/item/diagramData.js](../../../../../../../module/data/item/diagramData.js); [module/data/item/templates/craftingComponentData.js](../../../../../../../module/data/item/templates/craftingComponentData.js) | Схема | Именованные поля и ID материалов | Источник и использование сверены |
| item-header | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | Прямой partial | Общие поля | Источник и использование сверены |
| associated-item | [templates/partials/associated-item.hbs](../../../../../../../templates/partials/associated-item.hbs) | Прямой partial | UUID-результат / resultQuantity / удаление | Источник и использование сверены |
| CONFIG.WITCHER.craftingLevels | [module/setup/config.js](../../../../../../../module/setup/config.js) | Словарь | novice/journeyman/master/grand-master/witcher | Источник и использование сверены |
| WITCHER.* | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Заголовки; два ключа действий имеют начальный пробел | Источник и использование сверены |
| Девять иконок субстанций | [assets/images](../../../../../../../assets/images) | Ресурсы, вне границ пофайлового анализа | vitriol.png … fulgur.png; файлы только отображаются | Источник и использование сверены |
| editor/selectOptions/checked/localize/if/unless/each | Foundry Handlebars API | Внешний API | Генерация UI | Источник и использование сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../module/item/sheets/WitcherDiagramSheet.js) | Этот шаблон и классы действий | PARTS.main; activateListeners | Прямые ссылки |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Обычные поля идут в стандартную форму; таблицы материалов обслуживают ручные события. Не записывает встречную associatedDiagramUuid результата. Переключение isFormulae само не очищает alchemyDC/craftingDC или требования другого режима. realCraft выбирает ветвь по положительному alchemyDC, поэтому флаг и фактический состав ресурсов могут расходиться.

Два title используют строки ' WITCHER.Item.AddComponent' и ' WITCHER.Item.RemoveComponent' с пробелом. Локализация их не находит, хотя варианты без пробела существуют. Неразрешённый UUID остаётся в known: у такого компонента пустое имя/картинка из-за подготовки контекста, не из-за отсутствия сохранённого имени модели.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Два режима | Реальные _prepareContext и HBS; 3 материала и связанный результат | Не-формула: 12 именованных полей; формула:20; description-editor не входит в эти числа | editor — явный фасад, не widget |
| ID и события | Настоящие модели/методы, parse5 | ID строки сохраняется с BaseItem; ручные quantity/name не имеют name | Браузерный blur не моделировался |
| Локализация | Раскрытые en/ru JSON и исходный localize-контракт | Оба ключа с пробелом не определены в обоих языках | CSS-подсказка браузера не открывалась |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-01](../../../../cross-check-0002.md#u007-01), [U007-03](../../../../cross-check-0002.md#u007-03), [U007-06](../../../../cross-check-0002.md#u007-06), [U007-07](../../../../cross-check-0002.md#u007-07). Для этого файла установлены процессы R007-09, R007-10, R007-11, R007-13, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00095](../../../../../../issues/closed/issue-00095.md), [issue-00096](../../../../../../issues/closed/issue-00096.md), [issue-00097](../../../../../../issues/potential/issue-00097.md), [issue-00098](../../../../../../issues/closed/issue-00098.md), [issue-00101](../../../../../../issues/potential/issue-00101.md). Проблемы контекста, результата, миграции, подсказок и выбора механизма изготовления.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Форма рецепта использует isFormulae для выбора количества полей и ручных списков; реальный Item расход выбирает alchemyDC. Known/unknown компоненты приходят из sheet, где fallback может быть утрачен; span.edit-component не равен text input. Подсказки add/remove компонентов имеют начальный пробел; Drop/CRUD обслуживают отдельные handlers.

Сопоставленные определения и потребители: [module/item/sheets/WitcherDiagramSheet.js](../../../module/item/sheets/WitcherDiagramSheet.js.md), [module/data/item/diagramData.js](../../../module/data/item/diagramData.js.md), [module/data/item/templates/craftingComponentData.js](../../../module/data/item/templates/craftingComponentData.js.md), [templates/partials/item-header.hbs](../../partials/item-header.hbs.md), [templates/partials/associated-item.hbs](../../partials/associated-item.hbs.md), [module/setup/config.js](../../../module/setup/config.js.md), [lang/ru.json](../../../lang/ru.json.md).

[Протокол и границы](../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-09](../../../../cross-check-0002.md#r007-09), [R007-10](../../../../cross-check-0002.md#r007-10), [R007-11](../../../../cross-check-0002.md#r007-11), [R007-13](../../../../cross-check-0002.md#r007-13). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
