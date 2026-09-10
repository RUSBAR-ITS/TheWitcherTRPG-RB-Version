# module/data/item/templates/craftingComponentData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/craftingComponentData.js](../../../../../../../../module/data/item/templates/craftingComponentData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../../review-log.md#task-0003016) |

## Назначение файла

Фабрика схемы одной строки материала в craftingComponents рецепта; связывает внутренний ID строки с необязательным UUID Item.

## Условия использования

Единственный прямой импорт найден в DiagramData.defineSchema, внутри ArrayField(SchemaField(...)). При импорте создаётся alias fields, при вызове — объект DataFields.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| craftingComponent | default function | Схема строки | Импорт DiagramData | Вызов при defineSchema |
| fields | Локальный alias | foundry.data.fields | Внутри модуля | Конструкторы |
| id | StringField | initial: () => foundry.utils.randomID() | craftingComponents[].id | Стабильный ID сохраняемой строки |
| name | StringField initial='' | Имя материала | craftingComponents[].name | Вручную или из связанного Item |
| quantity | NumberField initial=0 | Требуемое количество | craftingComponents[].quantity | Нет min/max/integer |
| uuid | DocumentUUIDField | Связь с документом | craftingComponents[].uuid | В тесте по умолчанию null |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| craftingComponent() | Без аргументов | Объект четырёх полей | Создаёт DataFields; callback id вызывает randomID при initial записи | Не создаёт Item; не ищет материалы |
| initial callback id | Инициализация отсутствующего id | Строка randomID | Отдельный ID новой строки | Не UUID предмета и не индекс массива |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| foundry.data.fields / DocumentUUIDField | Foundry DataField API | Внешний API | Схема полей | Определение и потребитель сверены |
| foundry.utils.randomID | Foundry utilities | Внешний API | Initial ID строки | Определение и потребитель сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/diagramData.js](../../../../../../../../module/data/item/diagramData.js) | craftingComponent() | Прямой импорт, массив SchemaField | defineSchema |
| [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../../module/item/sheets/WitcherDiagramSheet.js) | id/name/quantity/uuid | Поиск id при edit/remove; UUID при drop и map | Контракт строки |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../../../../templates/sheets/item/diagrams-sheet.hbs) | id/name/quantity | data-id и inputs | Две таблицы known/unknown |
| [module/item/witcherItem.js](../../../../../../../../module/item/witcherItem.js) | name/quantity | realCraft | Поиск по имени, не id |
| [module/item/mixins/dismantlingMixin.js](../../../../../../../../module/item/mixins/dismantlingMixin.js) | uuid/quantity/name | dismantle | Разрешение результата разборки |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

В отличие от itemEffect расходования здесь id реально входит в модель. Добавление из UI не передаёт id: следующий конструктор модели генерирует 16 символов. Существующие id сохраняются; два drop одного UUID создают две строки с разными id, не суммируют quantity. _onAddComponent передаёт quantity='': настоящая NumberField очищает его в null, тогда как отсутствие поля даёт initial=0. Поле имени может обновляться подготовкой по UUID, но идентичность строки остаётся её id.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема | Реальная DiagramData с двумя строками | Разные 16-символьные ID, uuid=null | В памяти |
| CRUD/повтор | Настоящие методы листа + очистка payload моделью | Edit '4'→4; remove по row1 сохраняет row2; add ''→null; повторный drop создаёт два id | update перехвачен |

## Непроверенные участки и открытые вопросы

Foundry 14.367.0, Node 24.16.0. Настоящие модели и код исполнялись изолированно; документы мира, сеть, браузерный submit и БД не запускались. UUID-валидация и разрешение документа — разные операции; наличие синтаксически допустимой строки не гарантирует доступ к Item. Нет собственных правил объединения повторных компонентов.

## Связанные проблемы

[issue-00095](../../../../../../../issues/potential/issue-00095.md). ID строки исправен; при неразрешённом UUID ошибается подготовка контекста листа.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
