# module/data/item/templates/regions/regionPropertiesData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../../../../module/data/item/templates/regions/regionPropertiesData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ef8117ba6e5a184989e65761d47a068381056e4a` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.022](../../../../../../../../tasks/task-0003.022.md), 5 файлов, 289 логических строк |
| Запись перекрёстной сверки | [TASK-0003.022](../../../../../../review-log.md#task-0003022) |

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

Все 56 строк прочитаны. Не проверялись сохранение/слияние поведения с существующей коллекцией, загрузка регионов из БД, несколько GM и фактический вызов пользовательских макросов.

## Связанные проблемы

[issue-00008](../../../../../../../../issues/potential/issue-00008.md), [issue-00009](../../../../../../../../issues/potential/issue-00009.md), [issue-00074](../../../../../../../../issues/potential/issue-00074.md), [issue-00075](../../../../../../../../issues/potential/issue-00075.md), [issue-00076](../../../../../../../../issues/potential/issue-00076.md), [issue-00142](../../../../../../../../issues/potential/issue-00142.md). 8/9 — контракт query; 74/75 — конфигурация; 76 — миграция; 142 — преждевременное завершение региональных операций.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ef8117ba6e5a184989e65761d47a068381056e4a`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003022) |
