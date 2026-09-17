# module/data/item/containerData.js

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../../issues/closed/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Модель экземпляра/шаблона контейнера и вес дерева.

**Основные методы, сущности и действия:** defineSchema добавляет nullable ObjectField templateContent с validateTemplate к прежним carry/storedWeight/content. calcWeight заново вызывает describeContainer: свой quantity*weight плюс вес всех потомков, только если isCarried и не isStored. prepareDerivedData записывает prepared storedWeight/itemContent/contentIncomplete. carry остаётся полем без ограничения вместимости.

**Зависимости и потребители:** CommonItemData; describeContainer и validateTemplate из module/item/containerTemplates.js. WitcherActor.getTotalWeight читает calcWeight; листы читают itemContent/contentIncomplete. Старые прямые fromUuidSync и сумма только ближайшего уровня удалены.

## Предыдущий срез анализа

Датированные сведения ниже относятся к прежнему коду. При расхождении приоритет имеет актуальный раздел выше.

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

Исходник и текущие связи сопоставлены в TASK-0004.006. Прежние ссылки на будущий пофайловый разбор TASK-0003 больше не являются очередью: он завершён. Остались конкретные границы сквозной проверки: [U006-02](../../../../cross-check-0002.md#u006-02); [U006-05](../../../../cross-check-0002.md#u006-05). Self/cycle не рекурсивны; carry — показанный максимум без ограничения помещения.

## Связанные проблемы

[issue-00156](../../../../../../issues/closed/issue-00156.md), [issue-00158](../../../../../../issues/closed/issue-00158.md), [issue-00159](../../../../../../issues/closed/issue-00159.md), [issue-00160](../../../../../../issues/closed/issue-00160.md), [issue-00162](../../../../../../issues/closed/issue-00162.md), [issue-00163](../../../../../../issues/potential/issue-00163.md). Недоступные UUID, согласованность членства, циклы, вес вложенности, удаление контейнера и назначение вместимости.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `66cd03705dbc398eba0026284a298b5fbe337035`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003024) |

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Современная строка valuable.type=container читает prepared itemContent/storedWeight/carry: две единицы по3 дают progress6/max12. Вложенный details имеет полный UUID в data-item-id, но не класс .item, не предоставляет отдельного редактора количества. Это снимок, а не встроенный документ; обращений к UUID сам HBS не выполняет.

Связанные шаблоны: [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs). [Проверки и ограничения](../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.

## Сквозная сверка TASK-0004.006

2026-09-14; rusbar-main, a176c4f18879f2e5a63b93bc15345fc26d9f535a. Исходник совпадает со срезом TASK-0001; изменено только описание.

Одиннадцать полей, включая строковый массив UUID content. Подготовка обнуляет storedWeight/itemContent и считает только непосредственные quantity×weight; дочерний storedWeight не включён. Missing/холодный индекс прерывает с частичным результатом. Self/cycle не рекурсивны; carry — показанный максимум без ограничения помещения.

Сопоставленные определения и потребители: [module/data/item/commonItemData.js](commonItemData.js.md), [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs.md), [templates/sheets/item/container-sheet.hbs](../../../templates/sheets/item/container-sheet.hbs.md), [module/actor/witcherActor.js](../../actor/witcherActor.js.md).

[Протокол и границы](../../../../review-log.md#task-0004006) — TASK-0004.006; процессы [R006-13](../../../../cross-check-0002.md#r006-13), [R006-14](../../../../cross-check-0002.md#r006-14). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
