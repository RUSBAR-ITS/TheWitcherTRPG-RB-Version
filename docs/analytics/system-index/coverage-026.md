# TASK-0006.026 — Улучшения предметов и мутагены

2026-09-16; rusbar-main, исходный HEAD `4d4ad775e8b85bd8354b4ee3cd7083a5706b9096`; рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.026.md), [проверочные запросы](examples/expansion-026-queries.json), [тесты](tests/test_expansion_026.py).

## Результат и границы

Добавлены 30 сущностей, 165 отношений и 9 процессов. Всего 4700 сущностей, 12374 отношений, 382 процесса (1236 шагов, 2276 переходов); 354 границы. Основных источников 166, смежных 95, без определений 354; определения в 261/615 файлах (два словаря complete, 259 partial). Отношения в 265 файлах, локальные шаги процессов — в 128.

Сохранены все прежние 12209 отношений, 373 процесса и ID/владельцы сущностей. Уточнены четыре прежних записи: context.runeItems/glyphItems (описание/refs), _chooseEnhancement и removeEnhancement (описание/диапазон/refs). Прежние процессы подготовки Weapon/Armor, SP/resistance, расходования и временных улучшений переиспользуются. Полного покрытия движка или игрового исполнения не заявляется.

12 основных файлов и необходимые смежные определения. Уточнение исходного плана: src523 substances.hbs подключён текущим inventory, но содержит девять веществ, не мутагены. Для мутагенов фактический путь — Character._prepareAlchemy → inventory → alchemical partial (src552). Тип мутагена выбирается в общем item-header (src-000532), включённом mutagen-sheet.

| Файл | Включённая область и остаток |
| --- | --- |
| [module/data/item/enhancementData.js](../../../module/data/item/enhancementData.js) (src-000114) | Собственная схема, миграции, типы и поля улучшения; все внешние inherited contracts и читатели не исчерпаны. |
| [module/data/item/mutagenData.js](../../../module/data/item/mutagenData.js) (src-000119) | Собственные поля, consumable включение и граница текст/исполнение; другие подсистемы алхимии вне задачи. |
| [module/item/sheets/WitcherEnhancementSheet.js](../../../module/item/sheets/WitcherEnhancementSheet.js) (src-000169) | Все собственные методы, типы и PARTS; полный inherited lifecycle/UI вне этой порции. |
| [module/item/sheets/WitcherMutagenSheet.js](../../../module/item/sheets/WitcherMutagenSheet.js) (src-000174) | Все собственные методы/PARTS, общий config и базовая configuration; внешние submit/AE lifecycle partial. |
| [templates/sheets/item/enhancement-sheet.hbs](../../../templates/sheets/item/enhancement-sheet.hbs) (src-000601) | Именованные поля и keyed effect editor; header/description, все локализации и CSS связи не исчерпаны. |
| [templates/sheets/item/mutagen-sheet.hbs](../../../templates/sheets/item/mutagen-sheet.hbs) (src-000605) | Четыре описательных input; общий header/config/submit разобраны как соседние контракты, не полный браузерный цикл. |
| [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js) (src-000043) | Выбор/поздний callback установки и известные listeners; прежние процессы сохранены, другие участки не исчерпаны. |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) (src-000027) | Текущие категории enhancement и prepared writer слотов оружия; прежние helpers сохранены частично. |
| [module/data/item/weaponData.js](../../../module/data/item/weaponData.js) (src-000155) | ID→prepared wrappers, миграция и потребители переиспользованы; все виды ремонта/принадлежности и readers не исчерпаны. |
| [module/data/item/armorData.js](../../../module/data/item/armorData.js) (src-000108) | ID→prepared wrappers/free slots/SP/resistance из .018; все маршруты и внешнее исполнение не исчерпаны. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) (src-000557) | Свободные rune/glyph и effects вывод; прежние quantity/chat/общие действия, не все UI зависимости. |
| [templates/partials/character/substances.hbs](../../../templates/partials/character/substances.hbs) (src-000523) | Подключение текущим inventory подтверждено; это вещества, не мутагены. Девять pannels/крафт и все control writers вне порции. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) (src-000029) | _prepareAlchemy только mutagens категория; остальные фильтры и алхимия целиком не индексировались. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) (src-000552) | Вывод полей мутагена через общий alchemical partial; все категории/кнопки не исчерпаны. |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../templates/sheets/actor/tabs/tab-inventory.hbs) (src-000576) | Входы mutagens/runes/glyphs/substances и прежние секции; весь inventory partial. |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../module/actor/sheets/interactions/itemContextMenu.js) (src-000034) | Прямое тело снятия и legacy menu boundary; все внешние completion/ownership не исчерпаны. |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) (src-000028) | Сопоставление старого prepared writer оружия/брони; активная регистрация V1 отсутствует. |

<a id="models"></a>
## Разные носители изменений

| Носитель | Данные и реальный путь |
| --- | --- |
| Item enhancement | type/avail/applied, stopping, bludgeoning/slashing/piercing, effects: TypedObject(itemEffect). Общие quantity/weight/flags наследуются от CommonItemData |
| system.effects.<ключ> | itemEffect.name/statusEffect/percentage/varEffect; ключ словаря — не ActiveEffect ID. Словарь участвует в свойствах оружия/брони |
| ActiveEffect temporaryItemImprovement | Отдельная модель .008, выбор оружия, копирование embedded ActiveEffect, isTransferred/duration и WitcherItem.applyActiveEffects |
| Item mutagen | type/source/effect/alchemyDC/minorMutation + consumable(). effect и minorMutation — строки, consumeProperties и item.effects — отдельные механизмы |

EnhancementSheet.createSelects предлагает weapon/rune/armor/glyph; schema type остаётся StringField без choices. Только type=armor показывает avail/stopping/resistance; select статуса берёт statusEffects для weapon/rune, armorEffects — в остальных случаях. Общие add/edit/remove используют data-target=system.effects и ключ строки. _onChangeForm запускает super и _onEditEffect без ожидания; последний определяет checkbox по value=='on', поэтому строковый on превращается в checked (прежний issue60). У percentage модель 0–100, поля varEffect в этой форме нет. Обычные именованные поля сохраняются общим form-contract, а не данным обработчиком.

EnhancementData.migrateData сначала обращается к статическому this.effects, затем helper преобразует только непустой source.effects Array в TypedObject с randomID ключами. Пустой массив/словарь helper не меняет; дальнейший clean принадлежит модели. Старая миграция Weapon/Armor дополнительно дописывает _id из enhancementItems без дедупликации — уже существующие определения/процессы и issue78, не новая миграция данных.

<a id="installation"></a>
## Установка и снятие

1. Свободный слот → общий itemListener → _chooseEnhancement. И оружие, и броня используют CSS enhancement-weapon-slot; ветвь зависит от data-type ближайшего .item. У weapon есть data-type=weapon, у armor его нет, поэтому выполняется else.
2. getList('enhancement') исключает stored; фильтр исключает applied и отбирает weapon/rune либо armor/glyph. Количество показывается в option, но не проверяется. При отсутствии кандидатов остаётся OK без select. Prompt не ожидается и не возвращается; отмена не вызывает callback.
3. Поздний OK читает ID, берёт живой parent.enhancementItemIds и делает push. Нет проверки дубликата, вместимости, выбранного номера слота или актуальности ID. Затем parent.update без await.
4. Только теперь разрешается выбранный Item и читается его старое количество. Stale ID приводит к ошибке после push и запуска первой записи. Второй независимый update задаёт name+'(Applied)', applied=true, quantity=1; даже quantity=0 не имеет guard.
5. Если старое количество >1, вызывается addItem(item, oldQuantity-1, true) без await. Forcecreate ведёт в toObject() → переопределение quantity → createEmbeddedDocuments. Копируется _source на момент вызова; без общего ожидания нельзя утверждать, что остаток обязательно получил старый либо уже изменённый applied/name. Записи сервера в этой задаче не исполнялись.

При прямом правильном removeEnhancement(event,target) сначала запускается update улучшения applied=false/name.replace первого '(Applied)', затем update родителя с фильтром всех совпадений ID. Quantity и слияние стека не затрагиваются; обе записи не ожидаются. Штатный legacy menu callback получает target,event и ломается раньше основной операции (issue168). Видимость пункта по applied не доказывает работоспособный вход. В графе сохранена прежняя граница menu, новый процесс описывает только тело при правильном прямом вызове.

<a id="prepared"></a>
## Подготовленные ссылки и потребители

EnhancementItemIds — локальные ID Actor.items, не UUID. Weapon/Armor prepareDerivedData при непустом списке создают wrappers name/img/system/id: system ссылается на найденную модель, это не глубокая копия и не сам Item Document. Missing ID пропускается, дубли сохраняются; parent.actor.items без владельца бросает исключение (issue77). Armor дополнительно отбрасывает falsy ID перед разрешением, но freeEnhancements считает длину исходного массива; отрицательная/дробная длина new Array блокирует последующий SP/resistance (issue82).

Текущий _prepareWeapons и V1 при положительной ёмкости и несовпадении с числом ID заменяют live enhancementItems массивом ровно на число слотов: дополняют {} либо обрезают. Source ID при этом не изменяется (issue166). V2 _prepareArmor только фильтрует, V1 также переписывает prepared slots. Свободные runeItems/glyphItems исключают applied и поступают в свой partial; weapon/armor улучшения выводятся в соответствующих списках.

Боевой weaponAttack читает непустые prepared entries, заново разрешает id через Actor.items и вызывает damage.properties.addEffects(enhancement.system.effects). DamageProperties.enhancementsEffects также собирает словарь для представления; одинаковые ключи при spread перезаписываются. Нельзя подменять этот путь прямым применением ActiveEffect или гарантировать удвоение статуса при дублирующемся ID.

У брони effectsWithEnhancements/enhancementsEffects собирают словарь, ResistanceData делает OR, SpData добавляет stopping только при подходящем базовом max. Прежние процессы .018 сохранены: [покрытие](coverage-018.md). Actor.prepareDerivedData читает собственный armor.system.effects с flat(), а не объединённый getter (issue84); подготовленные resistance-checkbox могут попасть обратно в базу при submit (issue88, прежняя модельная проверка). Текущее исследование не является повторным браузерным воспроизведением этих issues или новым расчётом боя.

<a id="mutagen"></a>
## Мутаген: форма, список и применение

MutagenSheet ожидает общий context и пишет Availability.WITCHER и type=getTypes() в ссылку на CONFIG.WITCHER. Собственный шаблон включает item-header: там только для Item.type=mutagen select system.type берёт red/green/blue. Ни схема type, ни эти опции не исполняют мутацию. Четыре собственных поля — source/effect/alchemyDC/minorMutation; alchemyDC имеет text input без data-dtype, но NumberField модели. Общая форма типизируется/валидируется при сохранении.

Character._prepareAlchemy выделяет type=mutagen из уже отфильтрованных context.items. Inventory передаёт их как alchemicals=mutagens в общий partial: там показаны effect/minorMutation, inline quantity, item-info/chat и общее меню. Substances.hbs подключён отдельной секцией substancesIsOpen и работает с веществами/счётчиками, а не мутагенами.

Модель включает isConsumable=false и consumeProperties. MutagenSheet наследует обычную WitcherConfigurationSheet с ActiveEffects; специализированная ConsumableConfiguration не назначена. Поэтому наличие полей расходования в модели не означает наличие соответствующей вкладки в этом листе. Через общий configureItem можно работать с embedded ActiveEffect. Наследованный canHaveTemporaryItemImprovement=false ограничивает соответствующую кнопку; это не всеобщая проверка импортированного эффекта.

При item.isConsumable Actor.useItem запускает consume и removeItem(1) без await. Меню consumeItem имеет отдельный system.isConsumable guard и тот же порядок. Сам consume читает consumeProperties: возможно ожидает calculateHealValue, затем update HP без await, applyStatus/removeStatus, applyActiveEffectToActorViaId(...,'applySelf') и сообщение. ViaId фильтрует item.effects по effect.system.applySelf; не превращает текст effect/minorMutation или записи consumeProperties в changes. Полный прежний процесс proc-000149 и перенос .008 сохранены. Если списание последнего Item успело завершиться раньше UUID resolve после лечения, действует прежняя граница .013/.008; общего commit нет. Новая автоматическая мутация при добавлении/расходовании не приписана системе.

<a id="core"></a>
## Доказательства и внешние контракты

Foundry 14.367.0; проверены следующие участки установленного ядра. Внешние файлы не добавлены в каталог 615; hashes фиксируют прочитанный код, не исполнение UI/БД.

| Файл | Строки | Контракт | SHA256 |
| --- | --- | --- | --- |
| `/opt/foundryvtt/client/applications/api/dialog.mjs` | 369–375,405–425 | prompt всегда добавляет OK, wait по умолчанию rejectClose=false; закрытие не вызывает ok callback. | `4e2d299eaa931d96df1839e64a2defc60b6b95ee89a3e1d32d60b99040899343` |
| `/opt/foundryvtt/client/applications/ux/context-menu.mjs` | 611–625 | onClick(event,target), legacy callback(target,event). | `78ca291bf89b79486e45c7adaf8b04ed829d5858912ba0fe6f16946b727e6470` |
| `/opt/foundryvtt/common/abstract/data.mjs` | 812–830 | toObject(source=true) копирует _source; false использует schema transformed values. | `11bb7f848c707803607accfa9f6b946c7cbfe8b17781ff562b468bdc77b934e5` |
| `/opt/foundryvtt/client/applications/api/document-sheet.mjs` | 431–434,465–469,486–509,525–531 | Общий form change/submit, expandObject, validate с clean/addTypes, await update. | `7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01` |

Общий form lifecycle сопоставлен также с [порцией .024](coverage-024.md#core-form): await update внутри handler не означает await DOM change; submit сохраняет форму, а не только последнее поле. Прочитаны R006-03/04/10/11, R007-01/05, R013-04/08 с уточнениями, полные связанные issue60/77/78/82/83/84/88/166/170/171 и соседний issue168. Их прежние даты и ограничения фасадов сохранены. Аудит/issues здесь используются для чтения; новое исполнение игровых методов или мира не проводилось.

## Новые процессы и существующие продолжения

<a id="proc-000374"></a>
### proc-000374 — Лист улучшения: контекст и типы

Подготовка WitcherEnhancementSheet; inherited configuration отдельно.

Шаги: base → selects → assign. Условия и выходы заданы в JSONL; список не заменяет ветвление.

<a id="proc-000375"></a>
### proc-000375 — Улучшение: редактирование записи system.effects

Выбран change data-action=editEffect; add/remove доступны отдельными общими методами.

Шаги: form → change → payload → update. Условия и выходы заданы в JSONL; список не заменяет ветвление.

<a id="proc-000376"></a>
### proc-000376 — Лист мутагена: общий config и цвета

Подготовка WitcherMutagenSheet; описательные поля отдельно от ActiveEffect.

Шаги: base → config → return. Условия и выходы заданы в JSONL; список не заменяет ветвление.

<a id="proc-000377"></a>
### proc-000377 — Мутаген: сохранение описательных полей

Именованные inputs через общий ItemSheetV2 submit; текст не интерпретируется как бонус.

Шаги: input → submit. Условия и выходы заданы в JSONL; список не заменяет ветвление.

<a id="proc-000378"></a>
### proc-000378 — Постоянное улучшение: список и открытие выбора

click свободного слота; data-type родительской строки определяет ветвь.

Шаги: target → filter → prompt. Условия и выходы заданы в JSONL; список не заменяет ветвление.

<a id="proc-000379"></a>
### proc-000379 — Постоянное улучшение: подтверждение и разделение стека

Поздний Dialog ok.callback; два Item и возможный create копии без общего ожидания.

Шаги: selection → push → parent → chosen → applied → stack → copy. Условия и выходы заданы в JSONL; список не заменяет ветвление.

<a id="proc-000380"></a>
### proc-000380 — Постоянное улучшение: тело снятия при корректном вызове

Только прямой вызов(event,target); legacy callback(target,event) не доказывает достижимость этого тела через UI.

Шаги: chosen → clear → parent. Условия и выходы заданы в JSONL; список не заменяет ветвление.

<a id="proc-000381"></a>
### proc-000381 — Улучшение: миграция массива предметных воздействий

Подготовка сырых данных модели; не миграция БД мира.

Шаги: static → guard → map → super. Условия и выходы заданы в JSONL; список не заменяет ветвление.

<a id="proc-000382"></a>
### proc-000382 — Мутаген: текущая категория и строка инвентаря

Character._prepareContext после базового !isStored списка; вещества подключены отдельной секцией.

Шаги: classify → section → row. Условия и выходы заданы в JSONL; список не заменяет ветвление.

Прежние продолжения: proc-000158 (Weapon prepared), proc-000244 (Armor prepared), proc-000256/259 (SP/resistance), proc-000163 (словарь улучшений), proc-000149 (consume), proc-000036 (временное улучшение). Их записи сохранены целиком; новые связи ведут к тем же сущностям/полям, а не к копиям определений.

## Проверки

Проверены все 216 тестовых методов и 634 CLI-примера, включая 26 новых; для двух изменившихся запросов отдельно проверен текущий расширенный ответ. После адаптации исторического среза повторные проверки затронутых .013/.023 прошли. Это проверки справочника по исходникам, без запуска игрового сценария. Перекрёстно сверены исходные адреса/владельцы, source/prepared, разные документы, оба конца отношений, достижимость шагов/выходов и facets/роли. [Протокол](review-log.md#task-0006026). Следующая — [TASK-0006.027](../../tasks/task-0006.027.md); родитель in-progress.