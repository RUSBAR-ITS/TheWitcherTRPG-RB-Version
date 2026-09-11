# module/data/chatMessage/baseMessageData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/chatMessage/baseMessageData.js](../../../../../../../module/data/chatMessage/baseMessageData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.040](../../../../../../tasks/task-0003.040.md), 10 файлов, 237 логических строк |
| Запись перекрёстной сверки | [TASK-0003.040](../../../../review-log.md#task-0003040) |

## Назначение файла

Базовая схема message.system с единственным полем rollTotal. Даёт общий родительский класс трём моделям боевых сообщений.

## Условия использования

BaseMessageData extends foundry.abstract.DataModel; это обычный DataModel, не TypeDataModel. TypeDataField ChatMessage использует зарегистрированный класс. static metadata.type='base' сопоставляется регистратором, а не задаёт тип внешнего документа самостоятельно.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| BaseMessageData | default class:3 | База моделей чата | Регистрация base и три прямых наследника | Подготовка/валидация штатными методами DataModel. |
| metadata | static Object.freeze:7–9 | type: base | Свойство класса | Содержимое заморожено. |
| rollTotal | NumberField:13 | Числовой итог броска | system.rollTotal | Нет явных initial/min/max/integer; пустое значение undefined. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | foundry.data.fields | {rollTotal:NumberField} | Создаёт единственное поле | Синхронно, записей документов нет. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| fields / DataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/data.mjs; /opt/foundryvtt/common/data/fields.mjs | внешний API | defineSchema, очистка, валидация и подготовка | Настоящие fields/DataModel и BaseChatMessage в Node; не браузер. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | класс и metadata.type | CONFIG.ChatMessage.dataModels[type]; документ через documentClass | registerDataModels:76–80. |
| [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js) | BaseMessageData / defineSchema | extends; super.defineSchema() | Прямой импорт. |
| [module/data/chatMessage/defenseMessageData.js](../../../../../../../module/data/chatMessage/defenseMessageData.js) | BaseMessageData / defineSchema | extends; super.defineSchema() | Прямой импорт. |
| [module/data/chatMessage/damageMessageData.js](../../../../../../../module/data/chatMessage/damageMessageData.js) | BaseMessageData / defineSchema | extends; super.defineSchema() | Прямой импорт. |
| [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | system.rollTotal | Заполняет итог непосредственно перед сообщением | extendedRoll присваивает roll.total в обычный system. |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Схема не вычисляет Roll и не копирует rolls[0].total сама. extendedRoll записывает rollTotal; обычный Item.rollDamage отправляет Roll другим путём и может оставить system.rollTotal undefined. BaseMessageData не хранит arbitrary-поля системного payload: TypeDataField очищает значения, отсутствующие в схеме. Изменение prepared-поля само по себе не меняет _source.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Исходная модель | Группы 01–03 | По умолчанию undefined; '7' очищается в 7; допустимы −3/0/1.5; 'abc' вызывает валидационную ошибку | Не правила диапазонов броска. |
| Регистрация base | Настоящий BaseChatMessage, группа 02 | Без type выбирается base, system — BaseMessageData | Не сохранение сообщения сервером. |
| prepared и source | Группа 03 на наследнике | Изменение rollTotal меняет getter; toObject(true) сохраняет исходный итог | Запись update не моделировалась. |

## Непроверенные участки и открытые вопросы

Локальные Foundry 14.367.0 и Node 24.16.0. Ядро полей, DataModel и общий BaseChatMessage настоящие; game/CONFIG и соседние документы представлены минимальными фасадами. Браузерный WitcherChatMessage, серверная запись, загрузка старой истории и несколько клиентов не запускались. Область итоговой сверки серии не заменяет полный разбор оставшихся боевых примесей.

## Связанные проблемы

[issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00184](../../../../../../issues/potential/issue-00184.md). Базовый тип допустим ядром; асинхронные flags extendedRoll относятся к отправителю. Самостоятельных новых проблем базовой схемы не зарегистрировано.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `74322e91edac106c82668f4a47eef53ce1889dc1`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003040) |
