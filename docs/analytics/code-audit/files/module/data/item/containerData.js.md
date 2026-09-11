# module/data/item/containerData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/containerData.js](../../../../../../../module/data/item/containerData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `66cd03705dbc398eba0026284a298b5fbe337035` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.024](../../../../../../tasks/task-0003.024.md), 3 файла, 136 логических строк |
| Запись перекрёстной сверки | [TASK-0003.024](../../../../review-log.md#task-0003024) |

## Назначение файла

Модель контейнера: хранит массив UUID содержимого, готовит строки itemContent и суммарный storedWeight, рассчитывает вклад контейнера в вес Actor.

## Условия использования

registerDataModels регистрирует ContainerData для Item.container; тип объявлен в system.json. Наследует CommonItemData. Подготовка выполняется вызовом system.prepareDerivedData из ClientDocumentMixin.prepareData, а не getter листа.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| CommonItemData / fields | import 1 / const 3 | Базовая модель и API полей | Локально | Наследование и расширение схемы |
| ContainerData | default class, 5–43 | Тип данных контейнера | CONFIG.Item.dataModels.container | Схема, подготовка, вес |
| carry | NumberField, 11 | Заявленная вместимость | system.carry | Начальное 0; min/max/integer не заданы |
| storedWeight | NumberField, 12 | Сумма веса содержимого | system.storedWeight | Начальное 0; пересчитывается в prepareDerivedData |
| content | ArrayField(StringField), 13 | Список строковых UUID | system.content | Начальное []; нет DocumentUUIDField, unique/типового ограничения |
| itemContent | Подготовленный массив, 28–39 | Данные строк UI | system.itemContent, вне схемы | name,img,quantity,weight,description,uuid; порядок content |
| quantity/weight/isCarried/isStored и остальные общие поля | Унаследованы из CommonItemData | 8 полей базы; всего 11 | system | quantity — строка '1', weight 0, isCarried true, isStored false |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | super.defineSchema() | 11 полей | Разворачивает восемь общих и добавляет carry/storedWeight/content | Собственных миграций/CRUD нет |
| calcWeight() | isCarried, isStored, quantity, weight, storedWeight | Число либо NaN при неподходящих данных | Если carried&&!stored: quantity*weight+storedWeight; иначе 0 | storedWeight не умножается на quantity; carry не применяется |
| prepareDerivedData() | Массив content, синхронно разрешаемые Item UUID | undefined; prepared поля изменены | super; storedWeight=0; при truthy content itemContent=[]; forEach fromUuidSync; сумма quantity*weight; снимок полей | Нет guard null/system и фильтра повторов; исключение прерывает цикл; дочерний calcWeight не вызывается |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | ES default import/extends | defineSchema/calcWeight-поля | Полная база, восемь полей; canBeRepaired/canHaveTemporaryItemImprovement false |
| fields, TypeDataModel.prepareDerivedData | Foundry 14.367.0 common/data/fields.mjs; common/abstract/type-data.mjs:153 | Схема/внешняя база | NumberField/ArrayField/StringField; пустой базовый prepareDerivedData | Настоящие поля/модели, группы 01–04 |
| fromUuidSync | Foundry 14.367.0 client/utils/helpers.mjs:188–214 | Синхронный UUID resolver | 30 | Может вернуть документ, индекс компедиума без system или null; strict embedded-компедиум может бросить исключение |
| ClientDocumentMixin.prepareData/_safePrepareData | Foundry 14.367.0 client/documents/abstract/client-document.mjs:276–285, 313–320 | Жизненный цикл | Вызов system.prepareDerivedData и перехват ошибок | Настоящий _safePrepareData проверен с Hooks-фасадом |
| WitcherItem | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Класс документа/жизненный цикл | system модели | Собственной очистки связей content/isStored при удалении нет |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | ContainerData | Импорт/CONFIG.Item.dataModels.container | 2, 50 |
| [module/item/sheets/WitcherContainerSheet.js](../../../../../../../module/item/sheets/WitcherContainerSheet.js) | content и isStored у содержимого | Drop/removal | 33–52 |
| [templates/sheets/item/container-sheet.hbs](../../../../../../../templates/sheets/item/container-sheet.hbs) | storedWeight/carry/itemContent | Форма/строки | 6–37 |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | calcWeight/getList | Сумма веса, фильтр isStored | 245–257 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | storedWeight/carry/itemContent | Прогресс и список содержимого | 59–89 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

content содержит ссылки на исходные документы, не вложенные Item-копии. itemContent — подготовленные строки, не документы: UI получает сохранённый UUID и снимки полей. storedWeight имеет поле схемы, но подготовка обнуляет/пересчитывает его без Document.update. Повторная успешная подготовка не накапливает результат. При недоступном UUID остаётся частичный список/сумма, _safePrepareData ядра журналирует ошибку; полный отказ загрузки Item этим не доказан.

Вес: собственный quantity*weight плюс одна сумма содержимого. Содержимое учитывается независимо от его isCarried/isStored; прямой вклад скрытого Item обнуляет его модель. Вложенный контейнер учитывается только по своей оболочке, его storedWeight пропускается. Рекурсивного обхода нет: ссылка на себя/цикл не вызывает здесь рекурсию, но может обнулить вклад через isStored. carry используется UI как предел индикатора, в расчёте веса и Drop не проверяется.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема/подготовка | Группы 01–03 | 11 полей; пустой контейнер → []; предмет 2×3 → storedWeight 6; повторная подготовка сохраняет 6; двойная ссылка → 12 | Настоящие модели; UUID-источники подменены |
| Недоступная ссылка/индекс | Группа 03 | null и индекс без system дают TypeError; перед плохой ссылкой остаются подготовленные строки; настоящий safe-wrapper регистрирует ошибку | Сам fromUuidSync исполнен с parseUuid/коллекцией-фасадом; живой компедиум не загружался |
| Вес и вложенность | Группы 04/08/09 | Контейнер quantity2/weight2 + содержимое 6 → 10; nested outer1+inner2+leaf6 → итог 3; самоссылка/цикл дают 0 через stored | Actor.getTotalWeight настоящий, документы/монеты подменены |

## Непроверенные участки и открытые вопросы

Все 43 строки прочитаны. Не выполнялись загрузка/сохранение коллекций, восстановление источника, реальное перемещение документов или правила вместимости TRPG. _source и БД не объявлены изменёнными только из-за мутации prepared-данных.

## Связанные проблемы

[issue-00156](../../../../../../issues/potential/issue-00156.md), [issue-00158](../../../../../../issues/potential/issue-00158.md), [issue-00159](../../../../../../issues/potential/issue-00159.md), [issue-00160](../../../../../../issues/potential/issue-00160.md), [issue-00162](../../../../../../issues/potential/issue-00162.md), [issue-00163](../../../../../../issues/potential/issue-00163.md). Недоступные UUID, согласованность членства, циклы, вес вложенности, удаление контейнера и назначение вместимости.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `66cd03705dbc398eba0026284a298b5fbe337035`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003024) |
