# templates/partials/associated-item.hbs

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../issues/closed/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Отображение связанного рецепта/результата.

**Основные методы, сущности и действия:** Читает подготовленный associatedDiagramView/associatedItemView: описание — enriched system.description, доступность — available. Кнопка удаления связи зависит от сохранённого uuid, поэтому доступна и для недоступного документа. Остальные поля и управление количеством сохранены.

**Зависимости и потребители:** WitcherItemSheet._prepareContext и helpers/linkedItemContext.js; Handlebars localize и обычные обработчики associatedDiagramMixin.

## Предыдущий срез анализа

Датированные сведения ниже относятся к прежнему коду. При расхождении приоритет имеет актуальный раздел выше.

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

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-01](../../../cross-check-0002.md#u007-01), [U007-03](../../../cross-check-0002.md#u007-03), [U007-07](../../../cross-check-0002.md#u007-07). Для этого файла установлены процессы R007-12, R007-10, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00096](../../../../../issues/closed/issue-00096.md). Неверный путь описания связанного Item.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Associated-item partial читает prepared результат рецепта и resultQuantity; имя/иконка приходят от Item, описание ошибочно ищется вне system. Forward ссылка не создаёт обратный рецепт. Данные model/source/UUID и render не означают доступный для записи объект.

Сопоставленные определения и потребители: [module/data/item/diagramData.js](../../module/data/item/diagramData.js.md), [module/item/sheets/WitcherDiagramSheet.js](../../module/item/sheets/WitcherDiagramSheet.js.md), [module/data/item/commonItemData.js](../../module/data/item/commonItemData.js.md), [lang/ru.json](../../lang/ru.json.md), [templates/sheets/item/diagrams-sheet.hbs](../sheets/item/diagrams-sheet.hbs.md), [module/setup/handlebars.js](../../module/setup/handlebars.js.md).

[Протокол и границы](../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-12](../../../cross-check-0002.md#r007-12), [R007-10](../../../cross-check-0002.md#r007-10). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
