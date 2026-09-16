# module/data/item/templates/regions/regionBehavioursData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/regions/regionBehavioursData.js](../../../../../../../../../module/data/item/templates/regions/regionBehavioursData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ef8117ba6e5a184989e65761d47a068381056e4a` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.022](../../../../../../../../tasks/task-0003.022.md), 5 файлов, 289 логических строк |
| Запись перекрёстной сверки | [TASK-0003.022](../../../../../../review-log.md#task-0003022) |

## Актуализация issue-00330 — 2026-09-16

Версия 14.3.1.00007, dev, база 031fbb8691ad32ab01fad43253c8736071bb2f8b. [Реализация и проверки](../../../../../../../../issues/open/issue-00330.md#реализация-и-проверки--143100007). Ниже сохранён исторический разбор: его сообщения об исправленных подписях/пропусках относятся к прежнему коду. Механики, технические значения и компедиумы этой правкой не изменены.

Изменённые строки текущего файла:

- `18`: `label: 'WITCHER.Item.RegionProperties.tokenMoveWithin'`


## Назначение файла

Фабрика четырёх UUID-полей макросов для событий региона. Предоставляет декларативные настройки, а не сами обработчики движения.

## Условия использования

RegionProperties.defineSchema вызывает фабрику внутри SchemaField behaviours. На основе непустых полей createRegionBehaviour создаёт записи executeMacro; их исполнение принадлежит ядру.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const; 1 | API Foundry | Локально | Создание полей |
| regionBehaviours | default function; 3–26 | Фабрика схемы событий | Импорт RegionProperties | Каждый вызов создаёт поля |
| tokenEnter | DocumentUUIDField; 5–9 | Вход токена | type=Macro, required=false; label tokenEnter | Пустое значение не создаёт поведение |
| tokenTurnStart | DocumentUUIDField; 10–14 | Начало хода токена в регионе | type=Macro, required=false; label tokenTurnStart | Ключ соответствует CONST.REGION_EVENTS |
| tokenMoveWithin | DocumentUUIDField; 15–19 | Перемещение в пределах региона | type=Macro, required=false; label tokenPreMove | Имя поля современное, подпись осталась прежней |
| tokenExit | DocumentUUIDField; 20–24 | Выход токена | type=Macro, required=false; label tokenExit | Передаётся в system.events поведения |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| regionBehaviours() | Нет | {tokenEnter, tokenTurnStart, tokenMoveWithin, tokenExit} | Создаёт четыре DocumentUUIDField | Не разрешает UUID и не исполняет макрос |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DocumentUUIDField; CONST.REGION_EVENTS | Foundry 14.367.0, common/data/fields.mjs; common/constants.mjs: 2009–2193 | Схема/сопоставление события | type Macro и четыре значения событий | Проверены настоящие поля и константы |
| Ключи RegionProperties | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Локализация | Четыре label | Все определены; tokenPreMove обещает выполнение до движения |
| ExecuteMacroRegionBehaviorType | Foundry 14.367.0, client/data/region-behaviors/execute-macro.mjs; base.mjs | Внешний потребитель событий | events Set и UUID Macro; resolve/permission/execute | Настоящий тип исполнен с подменённым Macro/UUID resolver |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../../../../module/data/item/templates/regions/regionPropertiesData.js) | regionBehaviours() | Импорт, SchemaField, перебор keys | 1, 8, 29–31 |
| [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs) | behaviours.* и label | Четыре formGroup | 9–30 |
| [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | behaviours косвенно | Вложенная RegionProperties | 36 |
| [module/data/item/ritualData.js](../../../../../../../../../module/data/item/ritualData.js) | behaviours косвенно | Вложенная RegionProperties | 33 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Поле UUID проверяет синтаксис и тип документа; существование и возможность исполнения макроса проверяет ExecuteMacroRegionBehaviorType позже через асинхронный fromUuid/canUserExecute. Неизвестный корректный UUID может храниться в модели. Пустые поля дают null. Никаких Hooks эта фабрика не регистрирует.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема без миграции RegionProperties | Группа 01: фабрика в тестовой DataModel | Все 4 Macro UUID допустимы; Item UUID отвергается; keys входят в CONST.REGION_EVENTS | Тестовая оболочка нужна, чтобы отдельно проверить фабрику, не потеряв tokenMoveWithin в миграции |
| Ядро executeMacro | Группа 02 | Все 4 события приняты реальным типом, everyone=false; найденный Macro-фасад получает event/scene/region; отсутствующий сообщает ошибку и не исполняется | Реальные макросы/клиенты не вызывались |
| Подписи и движение | Группа 20; TokenDocument.#onUpdateHandleMoveWithinRegionEvents: 2973–2999 | Ключи en/ru существуют, но tokenPreMove противоречит маршруту события после изменения | Браузерное перемещение не выполнялось |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Прежний опыт .022 исполнял только разрешённую ветвь Macro-фасада. Живые enter/exit/move, несколько клиентов и внешний пользовательский код не проверены. Остаток: [U009-06](../../../../../../cross-check-0002.md#u009-06), [U009-07](../../../../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00076](../../../../../../../../issues/potential/issue-00076.md), [issue-00147](../../../../../../../../issues/potential/issue-00147.md). 76 — потеря нового значения миграцией родителя; 147 — устаревшая подпись события, отдельная от миграции.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ef8117ba6e5a184989e65761d47a068381056e4a`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003022) |

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

Четыре Macro UUID сопоставлены со SchemaField, генерацией executeMacro и ядром событий. tokenMoveWithin хранится под новым именем, но подписан ключом tokenPreMove; en/ru обещают момент до движения. Миграция значения находится в RegionProperties и отличается по причине от ошибочной подписи. Core выбор клиента/контекст Macro прочитаны отдельно.

Сопоставленные определения и потребители: [lang/en.json](../../../../../lang/en.json.md), [lang/ru.json](../../../../../lang/ru.json.md), [module/data/item/templates/regions/regionPropertiesData.js](regionPropertiesData.js.md), [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs.md), [module/data/item/spellData.js](../../spellData.js.md), [module/data/item/ritualData.js](../../ritualData.js.md).

[Протокол и границы](../../../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-18](../../../../../../cross-check-0002.md#r009-18), [R009-20](../../../../../../cross-check-0002.md#r009-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
