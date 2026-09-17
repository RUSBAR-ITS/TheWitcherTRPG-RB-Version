# TASK-0006.025 — Контейнеры, хранение и вес инвентаря

**Актуализация .00035:** затронутые контейнерные/ритуальные сущности, отношения, процессы и адресные тесты обновлены по [issue-00333](../../issues/closed/issue-00333.md#implementation-00035). Описание ниже — исторический результат исходной порции; прежние отсутствие каскада/несогласованные записи контейнера и потеря UUID строки ритуала больше не описывают текущий код. Игровая приёмка нового поведения ожидается.

2026-09-15; rusbar-main, исходный HEAD `7c2450b94fa8381c8337980990bd42acf6d83af3`; рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.025.md), [проверочные запросы](examples/expansion-025-queries.json), [тесты](tests/test_expansion_025.py).

## Результат и границы

Добавлены 36 сущностей, 134 отношения и 10 процессов. Всего 4670 сущностей, 12209 отношений, 373 процесса; 348 границ. Основных источников 158, смежных 99, без определений 358; определения в 257/615 файлах (два словаря complete, 255 partial). Сохранены прежние ID, 12075 отношений и 363 процесса. Уточнены два прежних определения: старый V1 _prepareItems и текущий Monster inventory template.

12 основных файлов и смежные места вызовов/потребители; весь движок, действующие БД и игровая механика не менялись. Выбраны UUID-хранение, перенос/извлечение, вычисление веса и пути UI. Экономика, генерация/экспорт добычи, полная логика mounts и новый механизм вложенности вне задачи.

| Файл | Область и остаток |
| --- | --- |
| [module/data/item/containerData.js](../../../module/data/item/containerData.js) (src-000111) | Раскрыты вся локальная схема, оба метода и plain itemContent; внешние model lifecycle/UUID/сохранение partial. |
| [module/item/sheets/WitcherContainerSheet.js](../../../module/item/sheets/WitcherContainerSheet.js) (src-000166) | Все собственные методы и whitelist раскрыты; общий inherited lifecycle, внешний drag/drop и права не исчерпаны. |
| [templates/sheets/item/container-sheet.hbs](../../../templates/sheets/item/container-sheet.hbs) (src-000598) | Carry/storedWeight/itemContent/remove UUID; общий header/description и все helper/CSS связи не исчерпаны. |
| [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js) (src-000043) | Carried/delete/inline/drop связаны с хранением; прежние методы/процессы сохранены, прочие listeners вне выбранного пути. |
| [module/actor/witcherActor.js](../../../module/actor/witcherActor.js) (src-000047) | getList/getTotalWeight/encumbrance и stored gate addItem; все прочие readers/writers не исчерпаны. |
| [module/data/item/commonItemData.js](../../../module/data/item/commonItemData.js) (src-000109) | Общие поля и calcWeight переиспользованы контейнером; все типы наследников и потребители не исчерпаны. |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) (src-000027) | context.items/containers/weight и общий bind; прочие helpers сохранены частично. |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) (src-000028) | Старый getData фильтр и полное _prepareItems в выбранной области; нет текущей регистрации. |
| [module/actor/sheets/WitcherLootSheet.js](../../../module/actor/sheets/WitcherLootSheet.js) (src-000030) | getList/loot/totalWeight и подключение rows/listeners; buy/hide/экономика не раскрыты полностью. |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) (src-000563) | Локальный ID, quantity/weight inline, edit/delete и hidden CSS; покупка/экономика вне задачи. |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../templates/sheets/actor/tabs/tab-inventory.hbs) (src-000576) | Две категории containers, передача partial и carry UI; остальные секции не исчерпаны. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) (src-000558) | Outer Item ID, carried и nested plain UUID rows; прочие helpers/общие действия partial. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) (src-000029) | _prepareValuables и clothingAndContainers; остальные категории/крафт/развитие не исчерпаны. |
| [module/data/item/valuableData.js](../../../module/data/item/valuableData.js) (src-000154) | Только type как категория valuable; consumable/прочие поля не раскрыты полностью. |
| [templates/sheets/actor/loot-sheet.hbs](../../../templates/sheets/actor/loot-sheet.hbs) (src-000549) | Текущий loot шаблон и row includes; генерация/торговля/все inputs не покрыты. |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) (src-000571) | Текущий Monster inventory template и связь loots→valuable partial; экспорт добычи вне задачи. |

<a id="storage"></a>
## Хранение и две записи

ContainerData наследует CommonItemData (quantity — строка, weight — число, isCarried=true/isStored=false), добавляет carry/storedWeight NumberField initial0 и content ArrayField(StringField). Content содержит UUID исходных Item. Подготовленный itemContent — plain snapshots name/img/quantity/weight/description/uuid; эти строки не документы.

Общий ItemSheet._onDrop проверяет isEditable назначения, разрешает класс документа и ожидает fromDropData. Dispatcher ожидает container override; его undefined превращается в null. Внутри override проверяются только наличие Item, девять типов и отсутствие UUID в текущем content. Затем push в prepared массив, container.update(content), source.update(isStored=true): оба Promise не ожидаются и не возвращаются. Ни копии, ни смены parent нет. Source owner/parent, другое членство, self/cycle и carry в guard не входят. Это не утверждение об обходе серверных прав.

Девять типов: weapon, armor, enhancement, valuable, alchemical, component, diagrams, mutagen, container. Mount/spell не допускаются этим методом. Актёрский drop/addItem работает иначе: тот же Actor ведёт к сортировке, внешний — к прежнему addItem. AddItem проверяет первый name/type; если он stored, создаёт новый документ, не ищет следующее совпадение. В копировании нет сброса isStored или переноса content-ссылок. Существующий путь добавления/передачи сохранён, а не продублирован новым процессом.

Извлечение получает data-uuid, удаляет первое совпадение (если найдено), разрешает UUID и независимо запускает два update. Nonmember тоже получает isStored=false; другие контейнеры не проверяются. При null/индексе без update запрос контейнера уже запущен до ошибки source.update. Если resolver сам бросил, до обоих update путь не доходит, хотя splice уже выполнен. Успешный возврат обоих обработчиков не означает завершение записи.

Удаление самого контейнера из строки или меню запускает обычный Item.delete; соответствующих _onDelete у WitcherItem/CommonItemData/ContainerData нет. Content не является embedded содержимым, поэтому модельная очистка isStored отсутствует. Оставшийся stored Item по-прежнему исключён обычным getList/весом. Внешние hooks и сервер не исполнялись.

<a id="weight"></a>
## Вес и вместимость

| Участок | Формула / условие |
| --- | --- |
| CommonItemData.calcWeight | carried && !stored ? quantity × weight : 0 |
| ContainerData.prepareDerivedData | storedWeight=0; при truthy content itemContent=[]; для каждой ссылки += source.quantity × source.weight |
| ContainerData.calcWeight | carried && !stored ? quantity × weight + storedWeight : 0 |
| Actor.getTotalWeight | ceil(сумма optional item.system.calcWeight() либо0 + system.calcCurrencyWeight()) |
| Actor.calculateWeigthEncumbrance | capacity=(body.max+body.totalModifiers)×10+enc.totalModifiers; при total>capacity ceil((total-capacity)/5), иначе0 |

Container quantity умножает только оболочку, не storedWeight. Флаги исходного предмета не проверяются при суммировании содержимого. Повторный prepare обнуляет сумму; одинаковые UUID в импортированном массиве учитываются повторно. Нет рекурсивного обхода: дочерний storedWeight не включён, а собственный вклад stored дочернего контейнера равен0. Self/cycle сами по себе не вызывают здесь рекурсию. На первой плохой ссылке остаётся частичный подготовленный результат; core safe-wrapper ловит исключение без локального восстановления.

Carry — редактируемая справочная вместимость/максимум progress. Ни drop, ни расчёт веса её не сравнивают с суммой. Автоматическое запрещение перегруза не объявляется правилом. Показатель нагрузки UI читает enc.value, тогда как штраф использует приведённую формулу capacity. В существующем calculateStat штраф веса вычитается дважды для REF/DEX и один раз для SPD; прежний расчёт не изменён.

<a id="views"></a>
## Списки и интерфейс

| Представление | Путь |
| --- | --- |
| Общий V2 | context.items=actor.items.filter(!isStored).sort(sort); isHidden/isCarried здесь не исключают строку; containers выделяются по Item.type |
| Старый V1 | Та же фильтрация live items; system из toObject(false); _prepareItems синхронный. Текущая регистрация отсутствует |
| Character | valuable.system.type=containers входит в clothingAndContainers; настоящий Item.type=container идёт отдельным массивом в тот же partial |
| Строка valuable | outer .item/data-item-id=локальный ID; carried отдельный await update. Только Item.type=container показывает content/progress |
| Вложенная строка | details.stored-item/data-item-id=полный UUID; класса .item и собственных контролов редактирования нет; closest(.item) у общего меню возвращает контейнер |
| Loot | getList скрывает stored, но не isHidden; loot=mount+mutagen+container+alchemical+diagrams. В .00029 исправлен тип mutagen по issue-00218. Вес независимо по всем items+валюте |
| Loot row | Item ID, quantity/weight inline, edit/delete; isHidden меняет CSS, не авторизацию; предметы контейнера не разворачиваются. img.dragable/data-id отличается от core .draggable/dataset.itemId; нативный draggable сам не доказывает Foundry UUID-пакет |
| Текущий Monster | PARTS.inventory → src571, valuables=loots; нет отдельной секции containers. Старый monster-sheet → src536 лишь прежний/preload путь |

Shield — исключение getList: armor.location=Shield без фильтра isStored. TotalCost считает только context.items, totalWeight — все предметы через calcWeight. Эти разные списки/суммы не объединены.

Меню Gift не допускает container в giftableTypes. Для допустимых Item текущий legacy callback передаёт target,event, а giftItem ожидает event,target; прежний issue-00168 остаётся границей входа. Прямой корректный вызов тела и socket addItem уже описаны в .013; они не доказывают достижимость через сломанное меню и не обеспечивают перенос содержимого контейнера.

<a id="core"></a>
## Внешние контракты и доказательства

Foundry 14.367.0. Внешние файлы не включены в каталог 615. Ниже зафиксированы прочитанные участки и SHA256 целых файлов; тест проверяет hashes, CLI freshness отдельно сохраняет зависимость package.json.

| Core файл | Строки | Проверенный участок | SHA256 |
| --- | --- | --- | --- |
| `/opt/foundryvtt/client/utils/helpers.mjs` | 188–209 | fromUuidSync: Document/cache/index/null и strict embedded compendium exception. | `21d7b80e8f7ac7b8e4c53aef622f36ec1867ca6be75ae7bb21c959df733d314c` |
| `/opt/foundryvtt/client/documents/abstract/client-document.mjs` | 276–285,313–320,539–557 | Safe prepare, вызов model derived и forwarding _onDelete. | `a007180e3cf8d465dffe43b11272f289b4cf77a9e301c7d431f48267dfad8e9e` |
| `/opt/foundryvtt/common/abstract/type-data.mjs` | 238–250 | Базовые _preDelete/_onDelete не очищают произвольные UUID. | `c63bbcfb576a90a3b9880a28dc7a66e5bd90d33dad0da12559cdc7a631e9b2c7` |
| `/opt/foundryvtt/client/applications/ux/context-menu.mjs` | 611–624 | onClick(event,target), legacy callback(target,event). | `78ca291bf89b79486e45c7adaf8b04ed829d5858912ba0fe6f16946b727e6470` |

| `/opt/foundryvtt/client/applications/sheets/item-sheet.mjs` | 1–26,60–64 | ItemSheetV2 наследует DocumentSheetV2; item getter и внешний render. | `20a6427810422668d19dafcea1418d68b5faf4d9ef96b8196a2e1bc6b5e236cb` |
| `/opt/foundryvtt/client/applications/api/document-sheet.mjs` | 465–536 | Общая форма: editable, typing/validation и await update существующего документа. | `7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01` |

FromUuidSync использует cache или index компедиума, не загружает полный документ по сети; при отсутствующем id/collection возвращает null, embedded compendium strict вызывает исключение. Наличие индекса не гарантирует system/update. Редактирование carry использует общий ItemSheetV2 form-contract, уже раскрытый в [порции .024](coverage-024.md#core-form): вся форма, типизация и model validation, await update внутри handler; DOM change не ждёт запись. Локальные точки подключения ItemSheet18–21/78–83, context.data54 и container input11 сверены.

Прочитаны поздние R003-12, R006-12/13/14/15/17, R013-03/08. Основные [issue-00156](../../issues/closed/issue-00156.md)–[issue-00163](../../issues/potential/issue-00163.md) и [issue-00168](../../issues/potential/issue-00168.md) сохраняют даты и фасады прежних опытов. В этой задаче — чтение кода/графа; повторного исполнения JS/мира/БД нет. Новые issues не создавались, статусы/тексты аудита не менялись.

## Процессы

<a id="proc-000364"></a>
### proc-000364 — Контейнер: помещение исходного Item

Редактируемый ItemSheet; ядро разрешает drop document. Actor drop/addItem — отдельный процесс.

Шаги: resolve → dispatch → guard → push → container → source. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

<a id="proc-000365"></a>
### proc-000365 — Контейнер: извлечение ссылки по UUID

click .remove-item; не .item-delete и не перемещение parent.

Шаги: event → splice → resolve → container → source. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

<a id="proc-000366"></a>
### proc-000366 — Контейнер: подготовка веса и снимков содержимого

Model prepareDerivedData; ошибки может перехватить внешний safe-wrapper, частичный результат не откатывается.

Шаги: reset → rows → resolve → sum. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

<a id="proc-000367"></a>
### proc-000367 — Контейнер: прямой вклад в вес Actor

Вызывается полиморфно из getTotalWeight для каждой модели.

Шаги: formula. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

<a id="proc-000368"></a>
### proc-000368 — Инвентарь: общий вес и штраф характеристик

Во время calculateStat(ref/dex/spd), а также getTotalWeight из UI. Прежние расчёты характеристик сохранены.

Шаги: capacity → items → coins → penalty. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

<a id="proc-000369"></a>
### proc-000369 — Инвентарь Character: видимость контейнеров и вес

Текущий V2; выбранный путь context→категории→HBS, остальные helper остаются за границей.

Шаги: filter → base → category → render → rows. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

<a id="proc-000370"></a>
### proc-000370 — Инвентарь V1: старые фильтры и суммы

Незарегистрированный V1; проверены локальные тела, не активная форма.

Шаги: filter → groups. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

<a id="proc-000371"></a>
### proc-000371 — Loot: списки stored и строки инвентаря

Текущий PARTS.main loot-sheet; экономика и генерация вне охвата.

Шаги: lists → weight → view → row. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

<a id="proc-000372"></a>
### proc-000372 — Контейнер: удаление без освобождения UUID-содержимого

Действие .item-delete; для context-menu аналогичный delete без await.

Шаги: delete → lifecycle. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

<a id="proc-000373"></a>
### proc-000373 — Контейнер: редактирование справочной вместимости

input system.carry в ItemSheetV2; не guard размещения.

Шаги: input → submit. Условия/циклы/выходы заданы в JSONL; линейный перечень не заменяет ветвление.

## Проверки

Проверены все 206 тестовых методов и 608 CLI-примеров, включая 27 новых; после исправлений повторные проверки затронутых тестов прошли. Это проверки справочника по исходникам, без запуска игрового сценария. Перекрёстно проверены исходные адреса/владельцы, обе стороны отношений, достижимость шагов/выходов, facets/роли, ссылки, актуальность и метаданные доступа. [Протокол](review-log.md#task-0006025). Следующая — [TASK-0006.026](../../tasks/task-0006.026.md), родитель in-progress.