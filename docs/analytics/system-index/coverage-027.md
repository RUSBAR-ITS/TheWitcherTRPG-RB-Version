# TASK-0006.027 — Расы, родина и биография персонажа

2026-09-16; rusbar-main, исходный HEAD `481bee90901013c96b725b5c5d912a687e0c1d85`; дерево в начале чистое. [Задача](../../tasks/task-0006.027.md), [запросы](examples/expansion-027-queries.json), [тесты](tests/test_expansion_027.py).

## Результат и пределы

Добавлены 95 сущностей, 334 отношения и 11 процессов. Всего 4795 сущностей, 12708 отношений и 393 процесса (1270 шагов, 2336 переходов); 361 граница. Основных источников 182, смежных 91, без определений 342; определения в 273/615 файлах: 2 complete (en/ru), 271 partial. Отношения в 277 файлах, локальные шаги процессов в 133.

Сохранены все прежние 12374 отношения, 382 процесса и ID/владельцы сущностей. Уточнены пять прежних записей: addSocialStanding, lifepathData, general(), _prepareCharacterData и V2 _onLifeEventDisplay — описание/диапазон/refs. Включены 17 основных исходников задачи и необходимые смежные участки. Профессия остаётся .028, содержимое таблиц генерации биографии не индексируется как алгоритм.

| Файл | Включённая область и остаток |
| --- | --- |
| [module/data/item/raceData.js](../../../module/data/item/raceData.js) (src-000122) | Собственная схема, 4 perk, enrichedText; общие поля/все AE readers вне полного покрытия. |
| [module/data/item/homelandData.js](../../../module/data/item/homelandData.js) (src-000116) | Два поля, metadata, Item форма; внешняя модель/сохранение/все callers partial. |
| [module/data/item/templates/perkData.js](../../../module/data/item/templates/perkData.js) (src-000143) | name/description и четыре экземпляра Race; все внешние потребители не исчерпаны. |
| [module/data/item/templates/socialStandingData.js](../../../module/data/item/templates/socialStandingData.js) (src-000152) | Пять регионов, формы/inline; не автоматическое определение Actor социального выбора. |
| [module/item/sheets/WitcherRaceSheet.js](../../../module/item/sheets/WitcherRaceSheet.js) (src-000176) | PARTS/width, наследование/configuration; внешний sheet lifecycle partial. |
| [module/item/sheets/WitcherHomelandSheet.js](../../../module/item/sheets/WitcherHomelandSheet.js) (src-000171) | PARTS/width, наследование/configuration; внешний sheet lifecycle partial. |
| [templates/sheets/item/race-sheet.hbs](../../../templates/sheets/item/race-sheet.hbs) (src-000608) | Поля perk/socialStanding, formGroup/config; прочие общие поля/стили/локализации не исчерпаны. |
| [templates/sheets/item/homeland-sheet.hbs](../../../templates/sheets/item/homeland-sheet.hbs) (src-000603) | Два именованных поля, other guard/config; внешний submit/права не исполнены. |
| [module/data/actor/templates/character/generalData.js](../../../module/data/actor/templates/character/generalData.js) (src-000068) | Все собственные schema entries/calls; каждый внешний reader/writer general не исчерпан. |
| [module/data/actor/templates/character/general/backgroundData.js](../../../module/data/actor/templates/character/general/backgroundData.js) (src-000061) | HTML value, Actor form/enrich; другие readers не исчерпаны. |
| [module/data/actor/templates/character/general/homelandData.js](../../../module/data/actor/templates/character/general/homelandData.js) (src-000065) | Actor value/otherValue и отдельный Item приоритет; внешние writers не исчерпаны. |
| [module/data/actor/templates/character/general/lifeEventData.js](../../../module/data/actor/templates/character/general/lifeEventData.js) (src-000066) | Четыре schema поля, формы/toggle; варианты внешней записи не исчерпаны. |
| [module/data/actor/templates/character/general/lifeEventsData.js](../../../module/data/actor/templates/character/general/lifeEventsData.js) (src-000067) | 20 фиксированных slots/calls; source/prepared различены, сторонние consumers вне задачи. |
| [module/data/actor/templates/common/lifepathData.js](../../../module/data/actor/templates/common/lifepathData.js) (src-000077) | Четыре числовых поля, attacks.value и конкретные боевые readers; весь AE lifecycle не повторяется. |
| [templates/partials/character/tab-background.hbs](../../../templates/partials/character/tab-background.hbs) (src-000524) | Строки 1–95: общие сведения/биография/events; notes100–127 и все styles/i18n вне порции. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) (src-000029) | Раса/родина _prepareCharacterData, lifeEvents/enriched; профессия .028, прочие подготовки partial. |
| [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs) (src-000526) | Только race блок 263–337; профессию разбирает .028. |
| [module/data/actor/characterData.js](../../../module/data/actor/characterData.js) (src-000054) | Character schema/enrichedText переиспользованы; prepared source граница и counter уточнены. |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) (src-000027) | V2 life event listener/toggle и живой context; прежние процессы partial. |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) (src-000028) | Legacy lifeEvent object toggle; текущая регистрация V1 не утверждается. |
| [module/setup/handlebars.js](../../../module/setup/handlebars.js) (src-000211) | eachLimit выбранная регистрация/тело; другие helpers не исчерпаны. |
| [module/setup/config.js](../../../module/setup/config.js) (src-000209) | homelands/socialStanding maps; остальной CONFIG partial. |
| [module/data/actor/templates/character/general/detailsData.js](../../../module/data/actor/templates/character/general/detailsData.js) (src-000064) | details factory7 schema-полей; generic form/labels, все readers не исчерпаны. |
| [module/data/actor/templates/valueLabelData.js](../../../module/data/actor/templates/valueLabelData.js) (src-000093) | valueLabel schema, подключение details/reputation; все фабричные callers вне порции. |
| [templates/partials/character-header.hbs](../../../templates/partials/character-header.hbs) (src-000520) | Общие сведения 5–42; header действия/остальные bindings вне порции. |

<a id="race"></a>
## Разные владельцы и выбранный Item

| Данные | Владелец и использование |
| --- | --- |
| RaceData | Item, CommonItemData + HTML description, четыре SchemaField(perk()), региональный socialStanding |
| perk().name/description | Общая фабрика четырёх описательных особенностей; строки/HTML, без числового бонуса или changes |
| socialStanding().north/nilfgaard/skellige/dolBlathanna/mahakam | Пять строк Item; формы предлагают шесть значений config.socialStanding, схема choices не задаёт |
| HomelandData.value/otherValue | Item TypeDataModel, не наследник CommonItemData; metadata type=homeland |
| general().homeland → homeland().value/otherValue | Отдельные строки Actor.general.homeland, не копия выбранного Item |
| general().race/name | Строки Actor; показанное имя расы берётся из context.race.name, а не general.race |
| general().socialStanding | Текущий выбор Actor, читаемый addSocialStanding; регион Item и homeland автоматически его не определяют |
| general().background/details/age | HTML биографии, семь valueLabel сведений и возраст; пол находится отдельно в CharacterData.gender |

Drop переиспользует proc-000140: guard isOwner, same-Actor sort, _isUniqueItem по uniqueTypes, await removeItemsOfType, затем actor.addItem без await. Race и homeland входят в уникальные типы. Это не глобальное ограничение количества Item при всех способах создания; кнопка add и внешний импорт — другие входы. getList(type) фильтрует !isStored и сортирует по sort; _prepareCharacterData берёт [0]. У HomelandData нет собственного isStored: undefined не исключает его этим фильтром. Никакого копирования Item homeland.value в Actor.general.homeland в этом пути нет.

В background/header наличие context.homeland переключает показ на Item.value/otherValue. Без Item доступны поля Actor; скрытие альтернативы не очищает данные. Config.homelands содержит 26 опций включая other, но обе модели принимают строки без choices. Предпочтение Item — правило отображения, а не миграция.

Текст perk не парсится в модификаторы в прочитанных drop/prepare/enrich путях. Embedded ActiveEffect остаётся отдельным документом Item: общий transfer/lifecycle и WitcherActiveEffect.isSuppressed описаны в прежних порциях .005/.008. Ни наличие текста, ни наличие Item не заменяет проверок эффекта. Расовые компедиумы/правила бонусов не добавлены.

<a id="forms"></a>
## Формы и обогащение

RaceSheet/HomelandSheet задают PARTS и width600, наследуют WitcherItemSheet с submitOnChange и общей WitcherConfigurationSheet. В базовом context config — ссылка CONFIG.WITCHER, data — Item.system, enrichedText — результат optional метода модели. У HomelandData собственного enrichedText нет.

RaceData.enrichedText последовательно вызывает createEnrichedText для perk1–4. Общий helper возвращает raw value, enriched HTML и systemField из schema.getField. Race Item formGroup использует все три; Actor _prepareCharacterData готовит enrichedText.race, но tab-profession:274/278/284/288 передаёт editor raw race.system.perkN.description. Сохранён прежний issue109: обогащённый результат не используется этим consumer. Target editor имеет вид race.system.perkN.description; корректное сохранение вложенного Item через этот target в браузере не установлено. Для него записана граница, а не вымышленный Item writer.

Именованные поля собственной формы Race обновляют Item; региональные select на Actor не имеют name, используют data-field и общий itemMixin.itemListener/.inline-edit/change → _onItemInlineEdit. Последний определяет Item через ближайший .item data-item-id=race._id, читает data-field/value и возвращает Item.update. Это не запись general.socialStanding Actor. Кнопки item-edit/delete/add направлены к существующим общим handlers.

Background form сохраняет Actor: details.<dt>.value, gender, general.age/socialStanding/homeland/background, lifeEventCounter и видимые поля событий. В отличие от race editor, formGroup background передаёт enrichedText.general.background правильно. Внешний DocumentSheetV2 handler expands formData, validate(clean/addTypes), затем await update существующего документа. Это чтение установленного ядра; DOM change не означает ожидания commit вызывающей стороной. HTML max20 не ограничение NumberField и не доказательство браузерного сохранения произвольного counter.

## Социальная поправка и параметры lifepath

addSocialStanding вызывается rollSkillCheck:67 и возвращает строку добавки к формуле только для character. При EMP charisma/leadership/persuasion/seduction tolerated/toleratedFeared даёт−1, иначе hated/hatedFeared−2. Feared/toleratedFeared/hatedFeared отдельно даёт charisma−1; WILL intimidation+1. Пустой/неподходящий выбор не добавляет модификатор. У метода нет чтения региональных строк Race или определения региона по homeland; атрибут не изменяется.

lifepathModifiers в CommonActorData — отдельная schema от lifeEvents. Числовой ignoredArmorEncumbrance вычитается до max(..., 0), shieldParryBonus/shieldParryThrownBonus учитываются только >0 при armor/parry или parrythrown. ignoredEvWhenCasting >0 добавляется только при armorEnc>0. attacks.<ключ> — SchemaField({value}), но мастер и handleStrikeType используют attacks.strong/joint без .value; сохранена связь с issue19. Реальные consumers переиспользованы: боевые процессы proc-000183/196 и прежний armour/castSpell маршрут. Текст события биографии не объявлен источником автоматической записи lifepathModifiers.

<a id="life-events"></a>
## LifeEvents: источник, представление и редактирование

1. Schema lifeEvents() создаёт 20 слотов с ключами 10–200; внутри decade1–20, value/details пустые, isOpened=false. Поля key нет. lifeEventCounter NumberField(initial20) не имеет min/max.
2. Базовый V2 context.system ссылается на actor.system. Character _prepareContext:133–136 заменяет prepared general.lifeEvents массивом Object.entries(...).map(([key, value])=>({key,...value})). Это изменение живой подготовленной модели; вызова update source здесь нет. При повторном map прежний value.key перекрывает индекс массива и сохраняет UI-ключ.
3. Counter присваивается как counter||length: 0 становится 20 при штатных слотах. Отрицательное, дробное или 21 truthy и не ограничивается. Исходная schema по-прежнему адресует 10–200; toObject(false) читает подготовленную модель через schema, toObject() копирует _source. Связь с issue24 не означает нового воспроизведения его прежнего опыта.
4. eachLimit проверяет только object, затем i<limit без ограничения keys.length. Его data.key — индекс списка, а background использует this.lifeEvent.key для data-event и имён формы. При 21 helper получает undefined последним элементом и HBS допускает пустую карточку; issue213. Browser input min1/max20 и модельные пределы различены.
5. Click .life-event-display → V2 _onLifeEventDisplay ищет prepared event по key, инвертирует isOpened и запускает Actor.update('system.general.lifeEvents.<key>.isOpened') без await/return. При отсутствующей записи чтение isOpened даёт ошибку до update. V1 обращается к объекту по dataset.event; это отдельный legacy handler, не текущая регистрация.
6. Только раскрытые отрисованные карточки имеют inputs value/details. Уменьшение counter скрывает карточки; рассмотренное тело не удаляет их source записи. Именованный form submit и toggle являются разными writers, source/prepared пути не слиты.

## Проверенные внешние контракты и прежний аудит

Foundry14.367.0; hashes фиксируют прочитанные участки установленного ядра, не его исполнение.

| Файл | Строки | Контракт | SHA256 |
| --- | --- | --- | --- |
| `/opt/foundryvtt/common/abstract/data.mjs` | 820–826 | toObject(source=true) копирует _source, false использует текущую модель и схему. | `11bb7f848c707803607accfa9f6b946c7cbfe8b17781ff562b468bdc77b934e5` |
| `/opt/foundryvtt/client/applications/api/document-sheet.mjs` | 431–434, 465–469, 486–509, 525–531 | Общий submit: expandObject, validate clean/addTypes; await update существующего документа. Чтение ядра, не UI/БД. | `7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01` |

Прочитаны R003-06/08, R008-01/02/03, R013-09/24/25 позднего аудита с уточнениями; полные связанные issue19/21/22/24/25/26/27/109/213. Урон/лечение соседних issue21/22/25/26/27 не расширяют область этой порции. Даты, статусы potential и ограничения прежних изолированных опытов сохранены; новые игровые запуски, мир/БД/браузер/несколько клиентов не проверялись. Аудит/issues используются для чтения.

## Новые процессы и существующие продолжения

<a id="proc-000383"></a>
### proc-000383 — Персонаж: выбор расы и родины и обогащение

После общего getList/drop .013; выбор Item и enriched не переносит поля в Actor.

Шаги: select → enrich → finish. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000384"></a>
### proc-000384 — Раса: обогащение четырёх особенностей

RaceData.enrichedText; source HTML и результаты отображения различены.

Шаги: perk1 → perk2 → perk3 → perk4. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000385"></a>
### proc-000385 — Раса: именованная форма Item

Редактирование Item в RaceSheet; описания корректно переданы formGroup.

Шаги: fields → submit. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000386"></a>
### proc-000386 — Раса на Actor: региональный socialStanding inline

Изменение select внутри .item data-item-id=race._id.

Шаги: select → resolve → write. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000387"></a>
### proc-000387 — Родина: Item имеет приоритет над полями Actor

Подготовленный context.homeland из первого getList; нет копирования между владельцами.

Шаги: branch → actor → item. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000388"></a>
### proc-000388 — Родина Item: выбор значения и другая родина

HomelandSheet наследует общий submit, модель не CommonItemData.

Шаги: choice → submit. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000389"></a>
### proc-000389 — Социальное положение Actor: добавка к навыковому броску

addSocialStanding(attribute, skillName); caller rollSkillCheck:67; регион Item не выбирается автоматически.

Шаги: type → emp → will → return. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000390"></a>
### proc-000390 — Биография: словарь модели в живой массив представления

Фрагмент Character._prepareContext после соседних подготовок, system ссылается на Actor.

Шаги: map → counter → enriched. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000391"></a>
### proc-000391 — Биография: eachLimit и ключи карточек

Шаблон background передаёт prepared events/counter; не schema bounds validation.

Шаги: guard → loop → card → return. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000392"></a>
### proc-000392 — Биография: раскрытие события V2

click .life-event-display; canonical V2 handler, V1 объектный вариант отдельно адресован.

Шаги: dataset → lookup → write. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

<a id="proc-000393"></a>
### proc-000393 — Биография: именованные поля и сохранение события

Actor form, отдельно от раскрытия карточки и Item inline edit.

Шаги: fields → event → submit. Условия, циклы и выходы — в JSONL; этот список не заменяет ветвление.

Общие процессы drop/создания, подготовки DataModel, createEnrichedText (proc-000111), inline Item, ActiveEffect и боевых расчётов сохранены. Новые процессы адресуют выбранные участки тех же сущностей, а не создают копии общих алгоритмов.

## Проверки

Проверены все 226 тестовых методов в 26 модулях и 665 CLI-примеров, включая 31 новый по IQ-01–IQ-08; ошибок в итоговых результатах нет. Исторические проверки выполняются на предусмотренных прежними тестами срезах. Это проверки справочника по исходникам, без запуска игрового сценария. Перекрёстно сверены определения/владельцы, source/prepared, оба конца отношений, ветви/выходы, refs и facets/роли. [Протокол](review-log.md#task-0006027). Следующая — [TASK-0006.028](../../tasks/task-0006.028.md); родитель in-progress.