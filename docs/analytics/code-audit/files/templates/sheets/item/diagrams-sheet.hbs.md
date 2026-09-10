# templates/sheets/item/diagrams-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/diagrams-sheet.hbs](../../../../../../../templates/sheets/item/diagrams-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../review-log.md#task-0003016) |

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

Не проверялись FormDataExtended, полный ProseMirror, сохранение одновременно открытых окон и внешние stylesheet. Повторяющийся id select отмечен как разметка, без заявления о конкретном сбое выбора. Span.edit-component не объявлен редактируемым text input.

## Связанные проблемы

[issue-00095](../../../../../../issues/potential/issue-00095.md), [issue-00096](../../../../../../issues/potential/issue-00096.md), [issue-00097](../../../../../../issues/potential/issue-00097.md), [issue-00098](../../../../../../issues/potential/issue-00098.md), [issue-00101](../../../../../../issues/potential/issue-00101.md). Проблемы контекста, результата, миграции, подсказок и выбора механизма изготовления.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
