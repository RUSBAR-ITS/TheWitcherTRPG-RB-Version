# templates/partials/associated-diagram.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/associated-diagram.hbs](../../../../../../templates/partials/associated-diagram.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../review-log.md#task-0003016) |

## Назначение файла

Представление связанного рецепта на оружии/броне: область drop, имя, картинка и удаление связи.

## Условия использования

Включается в основные формы Weapon/Armor; setup/handlebars предзагружает partial. item.system.associatedDiagram подготовлен unwrapAssociatedDiagram.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| data-type=associatedDiagram | div/table и вложенные элементы | Область drop | Обработчик листа | Сопоставляется с offsetParent.dataset.type |
| associatedDiagram.name / img | Условное представление | Показывает имя/изображение, если name truthy | Связанный документ или индекс | HBS не разрешает UUID |
| remove-associated-diagram | Ссылка с минусом | Удаление связи при наличии name | Примесь/лист | Click→update пустого UUID |
| add-associated-diagram | Ссылка в отсутствии name | Пустой anchor без значка | Нет найденного add-listener | Маркер; фактическая привязка выполняется drop |
| associatedDiagram.description | Выражение HBS | Попытка вывода описания | Верхний путь связанного объекта | У Item описание находится в system.description |

## Основные функции и методы

JavaScript-методов нет. if item.system.associatedDiagram.name выбирает содержимое или текст отсутствующей связи. Картинка имеет data-edit='img', собственного image-handler в partial нет. Есть h3 WITCHER.AssociatedDiagram.title; у remove-ссылки title actions.add, у пустой add-ссылки title actions.remove. Данные запрашивает модель, update выполняет внешний обработчик.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Поставщик связанного объекта | [module/data/item/templates/associatedDiagramData.js](../../../../../../module/data/item/templates/associatedDiagramData.js) | Данные модели | item.system.associatedDiagram | Источник и использование сверены |
| Обработчик drop/remove | [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js) | События / DOM-контракт | data-type / remove-associated-diagram | Источник и использование сверены |
| CommonItemData.description | [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js) | Схема описания | Правильное местоположение system.description | Источник и использование сверены |
| WITCHER.* | [lang/ru.json](../../../../../../lang/ru.json) | Локализация | Заголовок, кнопки, отсутствие связи | Источник и использование сверены |
| Handlebars if/localize | Foundry Handlebars API | Внешний API | Условия и вывод | Источник и использование сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/item/weapon-sheet.hbs](../../../../../../templates/sheets/item/weapon-sheet.hbs) | Этот partial | Прямое включение | Основной лист оружия |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../templates/sheets/item/armor-sheet.hbs) | Этот partial | Прямое включение | Основной лист брони |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Путь | Предзагрузка | loadTemplates |
| [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js) | data-type / remove-associated-diagram | Разбор drop и click | Методы листа/примеси |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Сам partial не создаёт/удаляет документы и не записывает обратную связь. Доступность отображения проверяет name, а не сам UUID. В опыте с настоящим BaseItem name/img выведены, description отсутствует: читается associatedDiagram.description вместо associatedDiagram.system.description. Подсказки добавления/удаления перепутаны независимо от этой ошибки. fromUuidSync также может вернуть индекс, где system.description не загружено; тест с полным BaseItem отделяет неверный путь от этой границы API.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пустая/заполненная связь | Настоящий HBS и BaseItem с system.description | Имя присутствует только при связке; описание не присутствует в обоих вариантах | UUID-карта и BaseItem, не полный client Item |
| Подсказки | HTML и раскрытые ru/en переводы | Минус удаления получил «Добавить рецепт крафта»; пустая add-ссылка — «Удалить рецепт крафта» | Проверка строк, не браузерный tooltip |
| Обработчики | Полный associatedDiagramMixin | Удаление обнуляет соответствующий UUID; привязка — через drop | Реальная геометрия offsetParent не проверена |

## Непроверенные участки и открытые вопросы

Не исполнялись CSS, layout, полное окно и DB. Влияние data-edit=img на общий ItemSheet не устанавливалось. Кнопка add без listener описана как текущая разметка, а не подтверждённый альтернативный способ выбрать документ. Исправление отображения HTML-описания требует отдельного решения.

## Связанные проблемы

[issue-00096](../../../../../issues/potential/issue-00096.md), [issue-00099](../../../../../issues/potential/issue-00099.md), [issue-00080](../../../../../issues/potential/issue-00080.md). Неверный путь текста, перепутанные подсказки и внешний drop.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
