# templates/partials/components-list.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/components-list.hbs](../../../../../../templates/partials/components-list.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../review-log.md#task-0003016) |

## Назначение файла

Общий табличный partial для материалов: наличие, нехватка, требуемое количество и необязательные цены. В текущих потребителях используется диалогом ремонта.

## Условия использования

Предзагружается setup/handlebars и включается repair-dialog.hbs с components, showCost=isRequest, canEditCost и totalPrice=data.repairPrice. Прямого включения в diagrams-sheet.hbs нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| components | Массив контекста | img/name/quantity/missingQuantity/required/cost | Внешний Repair.prepareDialogTemplate | Рендер строк |
| showCost / canEditCost | Флаги контекста | Колонка стоимости и возможность редактирования | Родительский partial-вызов | Условия |
| component-cost | input type=number с data-dtype=Number | Ввод цены, когда canEditCost и cost===0 | Внешний costEditMixin | Без name/value; DOM-обработчик change |
| total-price | span id=total-price и data-price=totalPrice | Начальная и отображаемая цена | Контекст / costEditMixin | Обновление innerText |

## Основные функции и методы

JavaScript-функций нет. each components выводит количество и, если missingQuantity truthy, ошибку в скобках; колонка required берётся готовой. showCost включает цены и итог. and(canEditCost,eq(cost,0)) выводит пустое числовое поле; остальные цены — текст. Ни суммирование, ни определение требований в HBS не выполняется.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Repair.prepareDialogTemplate / RepairData.repairPrice | [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) | Источник контекста | Нормализованные rows и цена | Источник и использование сверены |
| repair-dialog.hbs | [templates/dialog/repair-dialog.hbs](../../../../../../templates/dialog/repair-dialog.hbs) | Включающий шаблон | Передаёт все параметры | Источник и использование сверены |
| costEditMixin.attachHtmlListeners/_calculateAdditionalCost | [module/item/mixins/costEditMixin.js](../../../../../../module/item/mixins/costEditMixin.js) | DOM-контракт | component-cost / total-price / data-price | Источник и использование сверены |
| and/eq | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Helpers | Проверка редактируемой нулевой цены | Источник и использование сверены |
| WITCHER.ComponentsList.* | [lang/ru.json](../../../../../../lang/ru.json) | Локализация | Пять заголовков | Источник и использование сверены |
| Handlebars if/each/localize | Foundry Handlebars API | Внешний API | Представление | Источник и использование сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/dialog/repair-dialog.hbs](../../../../../../templates/dialog/repair-dialog.hbs) | Этот partial | components / showCost=isRequest / canEditCost / totalPrice | Единственное прямое включение в templates |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Путь partial | Предзагрузка | loadTemplates |
| [module/item/mixins/costEditMixin.js](../../../../../../module/item/mixins/costEditMixin.js) | Селекторы input и total-price | Глобальный document-поиск, change | Обработка UI |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Поле цены не сохраняется как свойство рецепта/компонента. Repair передаёт required=1 и missingQuantity=1 для неизвестного/недостающего материала; HBS не выводит это из craftingComponents.quantity. Внешний обработчик суммирует input, меняет total-price и передаёт additionalCost в RepairData. Пустое поле даёт parseInt('')=NaN, которое ??0 не заменяет; это отдельно воспроизведено как связь с потребителем.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Три состояния | Настоящий partial: showCost/canEditCost false/false,true/false,true/true | 0/0/1 editable inputs для cost0 и cost7; data-price15; missingQuantity показано | Не диалог браузера |
| Цена | Настоящий _calculateAdditionalCost с DOM-фасадом | '2','3'→additional5,total20; '2',''→NaN/NaN | Не проведён ремонт, денег не списывали |
| Связи | repair-dialog и prepareDialogTemplate прочитаны до формирования контекста | Стоимость и требования задаёт внешний код | Полный repair.js относится к TASK-0003.017 |

## Непроверенные участки и открытые вопросы

Полный процесс ремонта, конкурирующие окна, права, округление денег и стоимость по игровым правилам не проверялись. Global DOM-поиск не считается доказательством сбоя нескольких диалогов без отдельного сценария.

## Связанные проблемы

[issue-00100](../../../../../issues/potential/issue-00100.md). Нечисловой итог находится в обработчике, которому этот partial даёт пустые поля.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.017

2026-09-10, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; исходники неизменны. [Сверка](../../../review-log.md#task-0003017).

Полностью разобраны [RepairSystem](../../../../../../module/item/systems/repair.js), [costEditMixin](../../../../../../module/item/mixins/costEditMixin.js) и [диалог](../../../../../../templates/dialog/repair-dialog.hbs). Строки всегда required1, owned quantity0 получает missingQuantity1, но обычный guard не проверяет его ([issue-00104](../../../../../issues/potential/issue-00104.md)). showCost включён при artisan; canEditCost определяется GM. Цена — только отображение, платёж не выполняется. Настоящий обработчик подтвердил прежний NaN ([issue-00100](../../../../../issues/potential/issue-00100.md)) и глобальный поиск полей/первого total в условии двух DOM-контекстов ([issue-00106](../../../../../issues/potential/issue-00106.md)). Браузерная достижимость нескольких modal окон не проверена.

## Дополнительная сверка TASK-0003.048

2026-09-12, rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670; исходники не изменены.

Полностью разобраны [styles/components-list.css](../../../../../../styles/components-list.css) и [styles/repair.css](../../../../../../styles/repair.css). Таблица и цена — отдельные области: components-price используется также сообщением ремонта. Группа 12 отрендерила текущий repair-dialog с настоящим partial. th:nth-child(n+2) в components-list.css не ограничен table.components-list — [docs/issues/potential/issue-00309.md](../../../../../issues/potential/issue-00309.md). Scroll/max-height задаёт .repair .components-list-container; расчёт/изменение цены остаются у costEditMixin.

[Сценарии, результаты и ограничения](../../../review-log.md#task-0003048). Связанные файлы повторно не засчитываются в покрытие.
