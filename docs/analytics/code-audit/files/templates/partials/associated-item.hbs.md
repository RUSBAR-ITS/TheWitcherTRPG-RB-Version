# templates/partials/associated-item.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/associated-item.hbs](../../../../../../templates/partials/associated-item.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../review-log.md#task-0003016) |

## Назначение файла

Представление результата изготовления в рецепте: область drop, имя, картинка, количество результата и удаление связи.

## Условия использования

Включается diagrams-sheet.hbs; предзагружается setup/handlebars. item.system.associatedItem подготовлен DiagramData.prepareDerivedData.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| data-type=associatedItem | div/table и вложенные элементы | Область drop | Обработчик листа | Сопоставляется с offsetParent.dataset.type |
| associatedItem.name / img | Условное представление | Показывает имя/изображение, если name truthy | Связанный документ или индекс | HBS не разрешает UUID |
| remove-associated-item | Ссылка с минусом | Удаление связи при наличии name | Примесь/лист | Click→update пустого UUID |
| add-associated-item | Ссылка в отсутствии name | Anchor со знаком плюс | Нет найденного add-listener | Маркер; фактическая привязка выполняется drop |
| associatedItem.description | Выражение HBS | Попытка вывода описания | Верхний путь связанного объекта | У Item описание находится в system.description |
| system.resultQuantity | Text input, data-dtype=Number | Количество результата | Модель DiagramData | Только когда associatedItem.name существует |

## Основные функции и методы

JavaScript-методов нет. if item.system.associatedItem.name выбирает содержимое или текст отсутствующей связи. Картинка имеет data-edit='img', собственного image-handler в partial нет. Кнопки используют WITCHER.Item.RemoveAssociatedItem/AddAssociatedItem; отсутствие результата — WITCHER.craft.AssociatedItemMissing. Данные запрашивает модель, update выполняет внешний обработчик.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Поставщик связанного объекта | [module/data/item/diagramData.js](../../../../../../module/data/item/diagramData.js) | Данные модели | item.system.associatedItem | Источник и использование сверены |
| Обработчик drop/remove | [module/item/sheets/WitcherDiagramSheet.js](../../../../../../module/item/sheets/WitcherDiagramSheet.js) | События / DOM-контракт | data-type / remove-associated-item | Источник и использование сверены |
| CommonItemData.description | [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js) | Схема описания | Правильное местоположение system.description | Источник и использование сверены |
| WITCHER.* | [lang/ru.json](../../../../../../lang/ru.json) | Локализация | Заголовок, кнопки, отсутствие связи | Источник и использование сверены |
| Handlebars if/localize | Foundry Handlebars API | Внешний API | Условия и вывод | Источник и использование сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../../templates/sheets/item/diagrams-sheet.hbs) | Этот partial | Прямое включение | Основной лист рецепта |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Путь | Предзагрузка | loadTemplates |
| [module/item/sheets/WitcherDiagramSheet.js](../../../../../../module/item/sheets/WitcherDiagramSheet.js) | data-type / remove-associated-item | Разбор drop и click | Методы листа/примеси |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Сам partial не создаёт/удаляет документы и не записывает обратную связь. Доступность отображения проверяет name, а не сам UUID. В опыте с настоящим BaseItem name/img выведены, description отсутствует: читается associatedItem.description вместо associatedItem.system.description. resultQuantity показан только для доступного результата; при отсутствии имени input скрыт. fromUuidSync также может вернуть индекс, где system.description не загружено; тест с полным BaseItem отделяет неверный путь от этой границы API.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пустая/заполненная связь | Настоящий HBS и BaseItem с system.description | Имя присутствует только при связке; описание не присутствует в обоих вариантах | UUID-карта и BaseItem, не полный client Item |
| Количество | Два состояния associatedItem | resultQuantity отображается только при name | Полный submit не запускался |
| Обработчики | Полный WitcherDiagramSheet | Удаление обнуляет соответствующий UUID; привязка — через drop | Реальная геометрия offsetParent не проверена |

## Непроверенные участки и открытые вопросы

Не исполнялись CSS, layout, полное окно и DB. Влияние data-edit=img на общий ItemSheet не устанавливалось. Кнопка add без listener описана как текущая разметка, а не подтверждённый альтернативный способ выбрать документ. Исправление отображения HTML-описания требует отдельного решения.

## Связанные проблемы

[issue-00096](../../../../../issues/potential/issue-00096.md). Неверный путь описания связанного Item.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
