# TASK-0006.033 — Регионы магии, поведения и длительность

2026-09-16; rusbar-main, исходный HEAD `71475a90dbac72e3abfc9ae9ba5473ec3c148045`, дерево в начале чистое. [Задача](../../tasks/task-0006.033.md), [запросы](examples/expansion-033-queries.json), [тесты](tests/test_expansion_033.py).

<a id="overview"></a>
## Результат и пределы

Добавлены 84 сущностей, 195 отношений и 12 процессов. Всего 5328 сущностей, 14954 отношений, 465 процессов (1537 шагов, 2918 переходов), 433 границ. Определения в 305/615 файлах: два словаря en/ru complete, остальные 303 partial. Роли: 232 основных/73 смежных/310 без определений. Отношения в 309 файлах, локальные шаги процессов в 160.

Внутриметодные промежуточные grid/x/y/direction/shape/regions имеют адреса producer; каждое их повторное чтение и каждый шаг стандартных Array/Promise операций не вынесены в отдельные отношения. Связи ключевых настроек, flags, Macro UUID, документных запросов и query приведены явно. Браузерный submit, cleaning/сохранение и внешние Macro остаются границами.

Все прежние ID/владельцы, 14759 отношений и 453 процесса сохранены. Канонические определения RegionProperties, spellRegionMixin, countdown и две прежние границы уточнены на прежних адресах. Полностью прочитанные локальные методы не превращают внешние контракты, UI и файл в complete. Игровые исходники/данные, аудит/issues, формат/CLI не изменяются.

| Файл | Включённая область и остаток |
| --- | --- |
| [module/data/item/mixin/spellRegionMixin.js](../../../module/data/item/mixin/spellRegionMixin.js) (src-000117) | Все четыре метода и ветви прочитаны; geometry/raw flags/manual/emanation/Promise/таймер индексированы. Сохранение, browser preview и мультиклиентный runtime внешние partial. |
| [module/data/item/templates/regions/regionBehavioursData.js](../../../module/data/item/templates/regions/regionBehavioursData.js) (src-000149) | Все четыре Macro UUID schema fields, labels и потребители; Macro документы/код и реальная доставка событий внешние. |
| [module/data/item/templates/regions/regionPropertiesData.js](../../../module/data/item/templates/regions/regionPropertiesData.js) (src-000150) | Schema, UUID adapter, обе роли, payload и migrateData целиком; core collection update/cleaning и исполнение Macro не объявлены полными. |
| [module/data/item/templates/regions/templatePropertiesData.js](../../../module/data/item/templates/regions/templatePropertiesData.js) (src-000151) | Четыре поля без дополнительных bounds/choices, geometry/timer readers; прежние forms/migrations .031 сохранены, runtime partial. |
| [module/scripts/regions/regionHooks.js](../../../module/scripts/regions/regionHooks.js) (src-000200) | Весь countdown и caller, flag reader/request writer/delete, active Scene/actor/NaN и отсутствие update-фильтра. Бой не запускался. |
| [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs) (src-000596) | Весь шаблон: пять formGroup, отсутствующий field и четыре bindings; reachability старого guard, core form lifecycle/браузер partial. |
| [module/setup/queries.js](../../../module/setup/queries.js) (src-000213) | Региональный whitelist/UUID lookup/два уровня dispatch уточнены; прежние non-region handlers и процессы сохранены, delivery/core частичны. |
| [module/setup/hooks.js](../../../module/setup/hooks.js) (src-000212) | updateCombat→combatHooks→countdown без await, sibling generalCombat прежний .020; регистрация до init, ядро Hook dispatch внешнее. |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) (src-000186) | Региональный PART/guard и общий form host; остальные конфигурационные действия прежних порций сохранены. |
| [module/actor/mixins/castSpellMixin.js](../../../module/actor/mixins/castSpellMixin.js) (src-000011) | Raw roll/damage/options handoff .032 соединён с fromItem; прочие cast сущности и процессы сохранены. |
| [module/data/item/ritualData.js](../../../module/data/item/ritualData.js) (src-000123) | Подключение spellRegionMixin к RitualData, прежние schema/form/migration .031 сохранены. |
| [module/data/item/spellData.js](../../../module/data/item/spellData.js) (src-000125) | Подключение spellRegionMixin к SpellData, прежние schema/form/migration .031 сохранены. |

## Настройки, формы и вход

SpellData и RitualData получают spellRegionMixin через Object.assign(prototype); RegionProperties остаётся embedded model по system.regionProperties. WitcherSpellConfigurationSheet наследует PARTS от PropertiesConfiguration; собственный general не заменяет региональный PART. Прежние настройки/миграции .031 и raw producer .032 переиспользованы.

TemplateProperties объявляет createTemplate=false, templateSize=0, templateType='', visualEffectDuration NumberField без явного initial. У size нет min/max/integer, у type нет choices; truthy guard метода не является валидацией геометрии. Choices формы прежней .031 не ограничивают прямые данные модели.

<a id="form"></a>
Региональный HBS содержит пять formGroup. Первый ссылается на отсутствующий createRegionFromTemplate, поэтому в прочитанном ядре логируется ошибка и возвращается пустой фрагмент. Это не обязательное падение всей формы. Четыре остальных связывают schema/value для Macro UUID. Возможность редактирования условна: _configureRenderParts проверяет старое system.createTemplate и может удалить весь PART, независимо от templateProperties.createTemplate. Эти bindings не объявлены прямыми Item.update writers.

| Ключ поведения | Schema | HBS schema/value | Название/смысл |
| --- | --- | --- | --- |
| tokenEnter | regionBehavioursData:5–9 | :9–10 | Вход токена |
| tokenTurnStart | :10–14 | :14–15 | Начало хода токена |
| tokenMoveWithin | :15–19 | :19–20 | Label tokenPreMove, фактическое событие движения внутри после update |
| tokenExit | :20–24 | :24–25 | Выход токена |

Все четыре — DocumentUUIDField(type Macro, required:false). Синтаксически допустимый UUID не гарантирует существования/доступности Macro. В local renderer нет своего выбора событий и запуска Macro.

<a id="migration"></a>
Миграция безусловно пишет source.behaviours.tokenMoveWithin=source.behaviours.tokenPreMove и не удаляет старый ключ сама. Новый-only ключ перезаписывается undefined; при конфликте выигрывает старый. Отсутствующий behaviours вызывает ошибку внутри метода, но migrateDataSafe ядра ловит её, предупреждает и возвращает source для дальнейшей обработки. Из этого не следует обязательное падение загрузки Item. Старые фасадные опыты issue76 не запускались повторно.

<a id="async"></a>
## Запуск и значение завершения

castSpell вызывает optional createSpellRegion(roll,damage,{stamina:origStaCost}) без await, после сообщения и до fumble guard. createSpellRegion при трёх truthy настройках запускает fromItem(...).then(behaviors).then(visual).catch(empty), но не возвращает/ожидает цепочку. Сам async метод разрешается undefined раньше её завершения.

Первый then ожидает addBehaviorsToRegions, однако этот метод не ожидает ни query, ни region.update. UUID adapter также не возвращает и не ждёт внутреннего async метода. Следовательно, завершение этих методов не означает сохранение behaviors. Пустой catch ловит rejection своей цепочки, но не поздние rejections самостоятельно запущенных update/query/delete. Частично созданные регионы не откатываются.

<a id="options"></a>
<a id="raw"></a>
## Raw RegionData и flags

fromItem сначала проверяет type, затем собирает raw RegionData: name/uuid/user/color, shapes=[], elevation bottom0/topnull, restriction disabled move/priority0, behaviors=[], visibility ALWAYS, displayMeasurements=true, locked=false, default ownership NONE. В schema ядра нет raw ключей uuid/user; payload и сохранённый Region не отождествляются. Raw Roll/Item также не объявлены гарантированно сериализованными копиями.

| flags.TheWitcherTRPG | Producer :строка | Локальный consumer / граница |
| --- | --- | --- |
| roll | fromItem:44, исходный Roll | Прямых readers в module/templates не найдено; произвольный Macro вне поиска |
| item | :45, исходный Item | То же; не snapshot документа |
| itemUuid | :46, item.uuid | То же; это не UUID созданного Region |
| duration | :47, damage?.duration | countdown:10–11, JS вычитание; request writer setFlag:11 |
| actorUuid | :48, item.parent.uuid | countdown:8, сравнение с Actor текущего combatant |
| options | :49, flagOptions | Прямых readers в module/templates не найдено |

createSpellRegion передаёт свой options под именем options, а fromItem ожидает flagOptions={}; поэтому штатный handoff {stamina:origStaCost} теряется. Прямой fromItem с flagOptions может передать его. Прежняя граница ent-005244 уточнена, а не продублирована. duration — raw канал .032, не typed ChatMessage.system.damage; единицы здесь не нормализуются. item.parent.uuid требует owned Item неявно.

После создания каждому элементу regions присваиваются region.item и region.actorSheet. Это обычные runtime properties без update, не документные flags. Их дальнейшее использование извне не проверялось.

## Геометрия и сцена

Размер shape = Item.templateSize * canvas.scene.grid.size / canvas.scene.grid.distance; gridBased=!grid.isGridless, x/y/direction=0. При отсутствующей grid последующие чтения не защищены.

| type | Raw shape |
| --- | --- |
| circle | circle radius=size |
| cone | cone radius=size, angle90, curvature flat, rotation0 |
| rect | rectangle width=height=size, anchors0, rotation.toNearest(90,floor) |
| ray | line length=size??canvas.dimensions.distance, width=grid.size, rotation0; NaN не заменяется ?? |
| emanation | Начальный circle; core API затем заменяет shapes/elevation |

Unknown type логирует shape (ещё undefined) и возвращает null. Этот null при штатной цепочке затем не проходит обработку regions в behaviors; ошибка цепочки поглощается, это не успешное создание.

<a id="manual"></a>
Ручная ветка вызывает regions.push(await Promise.all(this.drawPreview(regionData))). drawPreview — async, отдаёт Promise, а Promise.all требует iterable. Preview запускается до rejection fromItem; отмена не исправляет тип аргумента. Поэтому успешное UI размещение ещё может создать Region, но штатная continuation behaviors/visual не получает корректного массива.

Сам drawPreview минимизирует все registered applications без await, ждёт optional legend.close до try. Только placeRegion(create:true) находится внутри try/catch и при rejection возвращает null. Core placeRegion возвращает один Region либо null/undefined, не массив; отмена→null. Восстановления окон нет. Permission/paused/интерактивное размещение/сохранение принадлежат ядру, браузер не запускался.

<a id="emanation"></a>
Эманация получает dependent TokenDocument без scene/linked/concreteOnly фильтров API. Synthetic Actor по умолчанию отдаёт свой Token. Локальный filter сравнивает token.scene (Scene object) с game.user.viewedScene (ID), поэтому обычные значения не исключают просмотренную сцену. Range=size/2/currentGrid.distance вычислен по canvas Scene. Core трактует range в grid units, умножает на distancePixels сцены токена и создаёт Region с parent token.parent, заменяя shapes/elevation, добавляя attachment/levels. Параметр gridBased из локального shape не передан четвёртым аргументом и не меняет default core false.

<a id="void"></a>
Promise.all ждёт эманации; API допускает void при предотвращённом создании. Результат не фильтруется, region.item у undefined вызывает ошибку. Пустой список токенов даёт []; уже созданные документы при другом отказе не откатываются.

<a id="dispatch"></a>
<a id="visualquery"></a>
## Behavior payload и GM query

GM перебирает Object.keys(this.behaviours), оставляет truthy UUID и строит name='Execute Macro on '+event, type='executeMacro', system.events=[event], system.uuid=uuid. Нет _id/everyone, разрешения UUID или вызова Macro. Для каждого Region отправляется region.update({behaviors}) без await. Результат изменения embedded collection, merge/замена и права сохранения здесь не выводятся из одного payload.

Non-GM посылает TheWitcherTRPG.query: function=addBehaviorsToRegionUuids, uuid=Item.uuid, data=[массив Region UUID]. activeGM не проверяется, query не ожидается, метод возвращается сразу. При прямом вызове адаптер map(fromUuidSync) не фильтрует null/тип, затем вызывает addBehaviorsToRegions без await.

Whitelist query разрешает имя addBehaviorsToRegionUuids. Но receiver разрешает Item и отдельно пробует entity[name] и entity.system[name]. Вложенный entity.system.regionProperties не посещается; штатный метод там. Это два вызова, не fallback. Затем true независимо от отсутствия методов/их завершения; отсутствующая entity/system может бросить. Сохранён прежний boundary ent-004468, прямой calls query→RegionProperties не выдуман.

deleteSpellVisualEffect пытается отправить имя deleteSpellVisualEffect со свободным item.uuid. При обычном отсутствии item аргументы бросают до отправки; при отсутствии activeGM ошибка может возникнуть раньше. Даже корректно изготовленный packet с таким именем whitelist не допускает и receiver возвращает false. Возврата после non-GM ветки нет. User.query core отдельно проверяет registration/permission/active target и возвращает socket Promise; локальный sender его не ждёт.

<a id="macro"></a>
## Внешнее исполнение Macro

Ядро ExecuteMacroRegionBehavior разрешает system.uuid, проверяет Macro, затем выбирает исполнителя: everyone, иначе event.user при его canUserExecute и isSelf, иначе активный eligible user по role вниз и ID вверх. Нет подходящих пользователей — без исполнения. Контекст macro.execute содержит speaker, actor/token события, scene, region, behavior, event. Actor здесь может быть actor вошедшего токена, а не flags.actorUuid источника заклинания.

tokenMoveWithin относится к post-update movement; label tokenPreMove не превращает его в pre-movement callback. Система задаёт только подписку через payload. Реальные события, доступность Macro и произвольное содержимое документа не индексированы как доказанное локальное выполнение.

<a id="timer"></a>
<a id="combat"></a>
## Два независимых удаления

| | visualEffectDuration | flags.duration / updateCombat |
| --- | --- | --- |
| Вход | deleteSpellVisualEffect после цепочки или прямо | registerHooks при загрузке → updateCombat → combatHooks |
| Клиент | isGM в ветви отправки, без раннего return | Только isActiveGM |
| Условие | regions && Number field >0 | Совпадение flags.actorUuid с Actor текущего combatant |
| Единица | Секунды, setTimeout(value*1000) | Одно вычитание на подходящее updateCombat; не гарантированно один ход/раунд |
| Изменение | Только отложенное delete | duration−1>0 → setFlag, иначе ID на delete |
| Scene | Будущая canvas.scene в callback | game.scenes.active, не combat.scene |
| Ожидание | Нет хранения handle/await delete | Нет await setFlag/delete, даже delete([]) |

Оба таймера не синхронизированы. duration 3 даёт запрос2, строка '2' даёт число1; 1/0/отрицательное/undefined/нечисловое дают delete, поскольку duration−1>0 ложно. Это чтение выражений JS, не новый runtime опыт. Не проверяются update.turn/round, started, текущий combatant/actor или active Scene. generalCombat запускается соседним async вызовом без await; его прежний .020 процесс сохранён. registerQueries вызывается на init, в отличие от раннего registerHooks.

<a id="core"></a>
## Сверка доказательств и внешних контрактов

Восемь первичных файлов и восемь их карточек прочитаны полностью. Сопоставлены R002-09/10, R009-15–22 [позднего аудита](../code-audit/cross-check-0002.md), полные issues 6/8/9/74/75/76/138–147. Их даты и пределы доказательств не изменялись. Исторические Node/фасадные опыты не выданы за новые, мир/БД/UI/сеть/мультиклиент не запускались. Смежные registration/model/config/cast/generalCombat участки перечитаны; прежние иные handlers и контент не расширялись.

| Ядро Foundry 14.367.0 | Прочитанные строки и контракт | SHA-256 |
| --- | --- | --- |
| `/opt/foundryvtt/client/data/region-behaviors/execute-macro.mjs` | 13–64: Schema events/uuid/everyone; lookup Macro, выбор исполнителя, await macro.execute(context). | `9726d9b1a922d45275eb255a8e3c0c53472c86c8f5ba9660bc997dc9cffef47c` |
| `/opt/foundryvtt/client/documents/region.mjs` | 1306–1336: createTokenEmanation: grid units, persisted Token, parent token.parent, перезапись shapes/elevation; Region|void. | `2ffe97d95c12ee0edfe19397fc68630fd91b14021d02922f4cc6013e76835ec2` |
| `/opt/foundryvtt/client/documents/actor.mjs` | 585–617: getDependentTokens, synthetic Actor, defaults linked/concreteOnly false, список сцен. | `e82580bf9cef39d934c972dee859a3b9ba7ab5f3ebdc7502319dfed1bc214bb3` |
| `/opt/foundryvtt/client/documents/user.mjs` | 48–52,283–321: viewedScene ID; User.query registration, permission, active target, сериализуемый packet, socket Promise. | `43e0837d478838959c8676a319ce4af44196bc1e7fc0ae98e8c4f2976aab9682` |
| `/opt/foundryvtt/client/documents/token.mjs` | 100–107,2973–2999: scene alias parent; TOKEN_MOVE_WITHIN handler после update/movement, не tokenPreMove. | `44b8f03c161d8f077991167d652924228fe2f88b2b47ef4354b98df1a83feba7` |
| `/opt/foundryvtt/common/abstract/data.mjs` | 884–899: migrateDataSafe ловит исключение и возвращает source. | `11bb7f848c707803607accfa9f6b946c7cbfe8b17781ff562b468bdc77b934e5` |
| `/opt/foundryvtt/client/canvas/layers/regions.mjs` | 688–782,1162–1207: placeRegion single Promise, permission/paused/cancel, один Region/null/undefined; Scene захвачена preview. | `8e7f306bacc623a81d47096d906ead893f3c074a44914bb17790ce1c6c221cf7` |
| `/opt/foundryvtt/common/data/fields.mjs` | 3399–3457: DocumentUUIDField проверяет UUID/тип Macro, не существование документа. | `efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01` |
| `/opt/foundryvtt/client/applications/handlebars.mjs` | 525–546: formGroup missing field логирует и даёт empty SafeString. | `0c5959e0ebdf5847277fba3284d76ee535084e022d087659fd0791e5ccd3545c` |
| `/opt/foundryvtt/common/documents/region.mjs` | 23–132: Region schema/embedded behaviors и permissions; uuid/user нет в schema. | `558f8de77714a636babda056b0d9292acf389641b34e1d3dfb7d4d0ba6581718` |

## Новые процессы

<a id="proc-000454"></a>
### proc-000454 — Региональные формы: достижимость и четыре Macro UUID

Наследованная конфигурация Spell; render и submit — внешние этапы.

`guard`, `template`, `uuids`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000455"></a>
### proc-000455 — Миграция события региона tokenPreMove → tokenMoveWithin

Embedded model migration; не live документный update.

`assign`, `super`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000456"></a>
### proc-000456 — createSpellRegion: раннее завершение и независимая цепочка

Вход от castSpell либо прямой вызов; цепочка не return/await внешнего async метода.

`guard`, `launch`, `behaviors`, `visual`, `catch`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000457"></a>
### proc-000457 — fromItem: raw flags и выбор геометрии

Отдельно от выполнения placement/emanation; parent Actor/grid необходимы неявно.

`type`, `payload`, `scale`, `shape`, `return`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000458"></a>
### proc-000458 — fromItem: ручное размещение или эманации

После формирования raw RegionData; результат должен быть массивом документов.

`branch`, `tokens`, `manual`, `attach`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000459"></a>
### proc-000459 — drawPreview: окна, размещение и отмена

Независимый async метод; fromItem ошибочно передаёт его Promise в Promise.all.

`windows`, `place`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000460"></a>
### proc-000460 — UUID регионов → вложенный behavior метод

Прямой вызов RegionProperties, не доказанный результат обычного GM query.

`resolve`, `invoke`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000461"></a>
### proc-000461 — Настройка behaviors: GM update либо запрос GM

На входе массив Region; реальные события/Macro выполняет ядро позже.

`owner`, `query`, `array`, `update`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000462"></a>
### proc-000462 — ExecuteMacro payload и внешнее исполнение

Система только строит объект; callback ядра отделён внешней границей.

`payload`, `executor`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000463"></a>
### proc-000463 — Региональный GM query: whitelist и глубина владельца

Receiver только для региональных packet; остальные handlers прежних процессов сохранены.

`whitelist`, `resolve`, `dispatch`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000464"></a>
### proc-000464 — Визуальная длительность: секунды и будущая canvas Scene

Отдельный запуск после цепочки behaviors либо прямой вызов.

`role`, `query`, `guard`, `schedule`, `callback`; ветви и sync/await/scheduled/unknown записаны в JSONL.

<a id="proc-000465"></a>
### proc-000465 — updateCombat: отсчёт регионов активной сцены

Независимо от визуального таймера; произвольное updateCombat, не только смена хода.

`hook`, `fanout`, `role`, `context`, `duration`, `delete`; ветви и sync/await/scheduled/unknown записаны в JSONL.

## Проверки

Проверены все 288 тестовых методов в 32 модулях и 897 примеров CLI, включая 42 новых по IQ-01–IQ-08; ошибок в итоговых результатах нет. Исторические проверки выполняются на предусмотренных прежними тестами срезах. Это проверки справочника по исходникам, без запуска игрового сценария. Перекрёстно сверены исходные адреса/владельцы, оба конца отношений, readers/writers, ветви/выходы, refs/facets/роли. [Протокол](review-log.md#task-0006033). Следующая — [TASK-0006.034](../../tasks/task-0006.034.md); родитель in-progress.