# module/data/item/templates/regions/regionPropertiesData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../../../../module/data/item/templates/regions/regionPropertiesData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.022](../../../../../../../../tasks/task-0003.022.md), 5 файлов, 289 логических строк |
| Запись перекрёстной сверки | [TASK-0003.022](../../../../../../review-log.md#task-0003022) |

Актуализация [issue-00001](../../../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Вложенная модель макросов региона. Преобразует заполненные настройки behaviours в данные RegionBehavior executeMacro и отправляет обновления регионам; для игрока делегирует операцию через query активному GM.

## Условия использования

Входит в SpellData/RitualData через EmbeddedDataField. После создания областей createSpellRegion вызывает addBehaviorsToRegions. Для UUID предусмотрен адаптер addBehaviorsToRegionUuids; отправленный запрос маршрутизатор не находит на нужном уровне вложенности.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| regionBehaviours; fields | Импорт 1 / const3 | Фабрика событий и API | Локально | Построение схемы |
| RegionProperties | default class5–56 | Наследник DataModel | system.regionProperties | Методы настройки/миграции |
| behaviours | SchemaField; 8 | Четыре необязательных Macro UUID | system.regionProperties.behaviours | Перебор только truthy значений |
| behaviors | Локальный массив; 27 | Данные embedded RegionBehavior | Аргумент region.update | Каждый регион получает список из текущих настроек; данные без _id |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Фабрика regionBehaviours | {behaviours: SchemaField} | Создаёт вложенные поля | Нет записи |
| async addBehaviorsToRegionUuids(regionUuids) | Массив UUID | Promise<undefined> | map(fromUuidSync) → addBehaviorsToRegions | Не ожидает и не возвращает внутренний Promise; null не отфильтрован |
| async addBehaviorsToRegions(regions) | Массив Region; parent.parent=Item | Promise<undefined> | Не-GM: activeGM.query с Item UUID и массивом UUID; GM: строит поведения и region.update({behaviors}) | Ни query, ни update не ожидаются; нет защиты отсутствующего GM/region; update-слияние решает ядро |
| createRegionBehaviour(event, uuid) | Строка события/UUID | {name, type:'executeMacro', system:{events:[event], uuid}} | Имя 'Execute Macro on '+event; один event | Не проверяет существование Macro, не исполняет код, не задаёт _id/everyone |
| static migrateData(source) | Ожидается source.behaviours | source через super | tokenMoveWithin = tokenPreMove без условий | Затирает актуальный ключ; без behaviours бросает TypeError, который migrateDataSafe ядра регистрирует и поглощает |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| regionBehaviours | [module/data/item/templates/regions/regionBehavioursData.js](../../../../../../../../../module/data/item/templates/regions/regionBehavioursData.js) | Импорт/фабрика | defineSchema | Все 4 поля сверены |
| DataModel, SchemaField, fromUuidSync | Foundry 14.367.0; common/abstract/data.mjs: 890–899; common/data/fields.mjs; client/utils/uuid.mjs | Модель/UUID/миграция | Подготовка данных и синхронное разрешение регионов | Настоящие поля, UUID resolver заменён картой |
| game.user.isGM; game.users.activeGM.query | Foundry 14.367.0 User/Users | Права/запрос | addBehaviorsToRegions | Отсутствие activeGM даёт исключение; реальной сети нет |
| query | [module/setup/queries.js](../../../../../../../../../module/setup/queries.js) | RPC-контракт | function addBehaviorsToRegionUuids, uuid Item, data:[regionUuids] | Маршрутизатор проверяет только entity/entity.system; метода на этих уровнях нет |
| Region.update / ExecuteMacroRegionBehaviorType | Foundry 14.367.0 common/documents/region.mjs; client/data/region-behaviors/execute-macro.mjs | Запись/потребитель данных | behaviors и последующее событие | Изменять непустые behaviors может GM; core тип принимает system.events/uuid |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | RegionProperties | Импорт/EmbeddedDataField | 10, 36 |
| [module/data/item/ritualData.js](../../../../../../../../../module/data/item/ritualData.js) | RegionProperties | Импорт/EmbeddedDataField | 4, 33 |
| [module/data/item/mixin/spellRegionMixin.js](../../../../../../../../../module/data/item/mixin/spellRegionMixin.js) | addBehaviorsToRegions | После результата fromItem | 10 |
| [module/setup/queries.js](../../../../../../../../../module/setup/queries.js) | addBehaviorsToRegionUuids | Строка allowlist, но неверная глубина доступа | 30, 39–43 |
| [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs) | behaviours.schema/value | Форма настройки | Четыре event-поля; несуществующий createRegionFromTemplate отдельно |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | system.regionProperties | Условия tabs/PARTS | _prepareTabs/_configureRenderParts |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Создание описаний behaviors происходит в памяти. region.update передаёт список без ID; эта проверка фиксирует отправленный payload, не подтверждает порядок добавления/слияния существующих embedded документов в БД. При пустых настройках отправляется behaviors:[]. Поля существующих регионов напрямую не меняются до API-записи. Возврат методов раньше записи не является её подтверждением. migrateData мутирует входной source.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Миграция обеих моделей | Группа 03 | Новый tokenMoveWithin →null; старый переносится; при конфликте побеждает старый. Пустой regionProperties логирует отказ миграции, затем получает defaults | Настоящие модели и migrateDataSafe; logger заменён сборщиком |
| GM и UUID | Группа 04 | Payload executeMacro/events/uuid без _id; await обоих adapters не ждёт управляемые записи; null Region отвергается | Region.update/UUID заменены |
| Игрок/query | Группа 05 | Запрос с Item UUID возвращает true без вызова вложенного метода; deleteSpellVisualEffect отклоняется; activeGM=null даёт TypeError | Реальный код маршрутизатора в vm; нет сети/прав живого клиента |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Не проверены merge сохранённой коллекции RegionBehavior, живой query, права и реальное исполнение Macro; присланный массив не равен конечной коллекции. Остаток: [U009-04](../../../../../../cross-check-0002.md#u009-04), [U009-06](../../../../../../cross-check-0002.md#u009-06), [U009-08](../../../../../../cross-check-0002.md#u009-08). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00008](../../../../../../../../issues/potential/issue-00008.md), [issue-00009](../../../../../../../../issues/potential/issue-00009.md), [issue-00074](../../../../../../../../issues/potential/issue-00074.md), [issue-00075](../../../../../../../../issues/potential/issue-00075.md), [issue-00076](../../../../../../../../issues/potential/issue-00076.md), [issue-00142](../../../../../../../../issues/potential/issue-00142.md). 8/9 — контракт query; 74/75 — конфигурация; 76 — миграция; 142 — преждевременное завершение региональных операций.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ef8117ba6e5a184989e65761d47a068381056e4a`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003022) |

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

Прослежены SchemaField→миграция→UUID adapter→GM payload behaviors. Присваивание прежнего tokenPreMove перезаписывает новый ключ; ошибка пустого behaviours перехватывается migrateDataSafe. Оба адаптера завершаются до завершения update/query. У player разрешённое имя находится глубже уровней поиска query, поэтому true не доказывает вызов.

Сопоставленные определения и потребители: [module/data/item/templates/regions/regionBehavioursData.js](regionBehavioursData.js.md), [module/setup/queries.js](../../../../setup/queries.js.md), [module/data/item/spellData.js](../../spellData.js.md), [module/data/item/ritualData.js](../../ritualData.js.md), [module/data/item/mixin/spellRegionMixin.js](../../mixin/spellRegionMixin.js.md), [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs.md), [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../item/sheets/configurations/WitcherPropertiesConfigurationSheet.js.md).

[Протокол и границы](../../../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-18](../../../../../../cross-check-0002.md#r009-18), [R009-19](../../../../../../cross-check-0002.md#r009-19), [R009-20](../../../../../../cross-check-0002.md#r009-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
