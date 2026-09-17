# packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json

## Текущий срез — 14.3.1.00016

| Поле | Значение |
| --- | --- |
| Источник | [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json](../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json) |
| Проверено | 2026-09-16; `dev`; база `095395276b97f0ffe916495e26be3938cf8fdcf8` + исправление [issue-00331 / К01](../../../../../../issues/closed/issue-00331.md) |
| Тип / назначение | Экспорт Item criticalWound: шаблон травмы, его эффекты и следующий этап лечения |
| Имя / ID | Heart Damage (Treated) / `Me9fgalLrB0i9Z2O` |
| Строк / SHA-256 | 92 / `c19721fe4751082c00e403f81c8ed12e7f6e42db4602e464a2ca8b5ce2112dbf` |

### Выполненные исправления

B17: восстановить конкретное пропущенное условие в description. Остальные поля сохранены. Текущие значения и связи перечислены ниже; архив в конце описывает прежние срезы.

| Поле system | Текущее значение |
| --- | --- |
| `htmlFields` | ["description"] |
| `description` | "<p>You permanently take 2 additional points of damage from bleeding.</p>" |
| `criticalLevel` | "deadly" |
| `treatment` | "treated" |
| `location` | "torso" |
| `lesserEffect` | false |
| `daysHealed` | 0 |
| `healingTime` | 0 |
| `sterilized` | false |
| `followUp` | null |

1 ActiveEffect; 1 changes. ID и `_key` сохранённых эффектов, origin, transfer, duration и несвязанные значения сохранены.

#### Heart Damage (Treated) — XgSpUpmyyZ494OLI

Строка `_id`: 36. `disabled=false`, `transfer=true`; statuses: `[]`.

| key | mode | value | priority |
| --- | --- | --- | --- |
| `system.combatEffects.turnStartEffects.bleed.damage.modifier` | 2 | "2" | null |

### Действия и зависимости

[system.json](../../../../../../../system.json) регистрирует criticalWounds; [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) (`applyCritWound`) читает индекс treatment/location/criticalLevel/lesserEffect, выбирает Item и добавляет его Actor. [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) определяет поля и выполняет treat/heal; [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) и Foundry обрабатывают ActiveEffect. Исправление descriptions само по себе не меняет расчёты.

Следующий этап: `followUp=null`; `treat()` удаляет конечный Item.

### Проверка и границы

Источник входит в 48 изменённых JSON [issue-00331 / К01](../../../../../../issues/closed/issue-00331.md). Все 226 JSON разобраны; 316 documentUuid/followUp разрешимы. Временная сборка шести пакетов и обратное извлечение совпали с исходниками, включая неизменённые документы. Полный клиент Foundry и действующие packs не проверялись; копии уже импортированных документов мира не обновлялись.

Проверки настоящих Roll/методов RollTable и потребителей травм, фасады окружения и нерешённые ограничения 00320/00328/00036 перечислены в issue-00331. Значения Actor и жизненный цикл эффектов этой порцией повторно не проверялись.

## Архив анализа до 14.3.1.00016

**Ниже сохранены датированные доказательства прежнего состояния. Старые числа результатов/эффектов, тексты, ссылки, номера строк и заявления об отсутствии исправлений не описывают текущий JSON. Актуальный срез находится выше.**

<details>
<summary>Предыдущие пофайловые исследования и проверки</summary>

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json](../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-14 |
| Ветка и коммит | rusbar-main, 1cae095ac2f0f009fb1358a888a7afcf5ea5ec2e |
| Изменения относительно коммита | Нет; 92 строк; SHA-256 6d5924ab4eba118f194e930c73f21213ab11cc59797ef743fcf6553561b717fe |
| Задача и порция | [TASK-0003.061](../../../../../../tasks/task-0003.061.md) |
| Запись перекрёстной сверки | [Протокол .061](../../../../review-log.md#task-0003061) |

## Назначение файла

Экспорт Heart Damage (Treated): состояние treated, локация torso. Содержит 1 ActiveEffect и 1 изменений. Данные задают шаблон травмы и её переход; действия выполняют потребители системы и Foundry.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

[ready:62–67](../../../../../../../module/TheWitcherTRPG.js) запрашивает четыре поля индекса: system.criticalLevel/location/lesserEffect/treatment; выбор пакета задаёт [criticalWoundsPack](../../../../../../../module/setup/settings.js). Item исключается из исходного выбора по treatment и используется через followUp или ручное добавление. Проверен индекс-фасад из настоящих очищенных моделей, не действующий серверный индекс.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Heart Damage (Treated) | Корневой Item; name:3, _id:85 | ID `Me9fgalLrB0i9Z2O`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Item.Me9fgalLrB0i9Z2O` | Загрузка, копирование к Actor, подготовка, лечение/удаление |
| _key / folder / sort | Корневые поля | `"!items!Me9fgalLrB0i9Z2O"` / `"uofXQEP6HBtekOAO"` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| img / ownership | Корневые поля | `"icons/svg/item-bag.svg"` / `{"default":0,"ugXtPMJIktbl63QV":3}` | Ресурс ядра вне пофайлового анализа; наличие указанного пользователя в мире не подтверждено |
| system / effects | Объекты, строки 6 / 20 | criticalWound / 1 embedded ActiveEffect | Схема и воздействия перечислены далее |

| Поле system | Экспортное значение | Смысл и потребитель |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация; defineSchema её не содержит, очистка модели удаляет поле. |
| description | `""` | HTMLField; enrichedText/createEnrichedText, редактор и сообщение applyCritWound. Текст не преобразуется в changes. |
| criticalLevel | `"deadly"` | StringField; выбор deadly и исключение автоматического treat из heal; ветви deadly в calculateHealingTime нет. |
| treatment | `"treated"` | StringField; выбор none и проверка treated в heal. |
| location | `"torso"` | StringField; фильтр applyCritWound и lookup подписи списка. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах first find: false для >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик заживления, редактирование и update в heal. |
| healingTime | `0` | NumberField; для deadly ветви расчёта нет, экспортный 0 сохраняется у Actor. |
| sterilized | `false` | BooleanField; новая стерилизация даёт ещё +2 дня к очередному дню. |
| followUp | `null` | DocumentUUIDField типа Item; treat загружает адресата или удаляет конечный Item. |

### ActiveEffect 1: Heart Damage (Treated)

ID `XgSpUpmyyZ494OLI`; _key=`"!items.effects!Me9fgalLrB0i9Z2O.XgSpUpmyyZ494OLI"`. Origin=`"Item.Me9fgalLrB0i9Z2O"` — ссылка на мировой Item; существование адресата не проверялось. Цель переноса при transfer=true — Actor-владелец текущего Item; origin не выбирает другого владельца.

Тип `"base"`, name:23; disabled=false, transfer=true, active=true; img=`"icons/svg/item-bag.svg"`, description=`""`, tint=`"#ffffff"`, sort=0, statuses=`[]`. Flags=`{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`; _stats=`{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. System до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`.

Duration до миграции: `{"startTime":null,"combat":null,"seconds":null,"rounds":null,"turns":null,"startRound":null,"startTurn":null}`. Подготовлено: start=null, value=Infinity, units=seconds, expiry=null, expired=false. Пустая длительность становится неограниченной при prepareBaseData; таймер этой записи не задан. applyAfterCalculations получает false, changes переходят в system.changes/initial. Statuscounter — внешний модуль; в фасаде без регистрации его flags очищаются, работа установленного модуля не проверена.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Источник поля / фактическое значение |
| --- | --- | --- | --- | --- |
| 1 / 45 | `system.combatEffects.turnStartEffects.bleed.damage.modifier` | 2 / `"2"` / `null` | add; `2`; priority=20; phase=initial | NumberField; [combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js); undefined |

Значение в последнем столбце прочитано после подготовки Actor, поэтому может отличаться от результата фазы initial. Повторение ID эффекта у разных Item не коллизия внутри одной коллекции effects. Вложенный _key указывает собственного владельца независимо от origin/name.

## Основные функции и методы

JSON не вводит собственных функций или обработчиков. Действия принадлежат следующим потребителям:

| Метод | Вход / условие | Результат и граница ожидания |
| --- | --- | --- |
| applyCritWound → addItem | Уровень, локация, critEffect и индекс | Выбор Item, запрос добавления и чат; повтор name/type может попасть в quantity |
| prepareDerivedData → calculateHealingTime | Родитель Actor | Ветви deadly нет, healingTime остаётся 0 без записи |
| treat | followUp или null | await fromUuid; createEmbeddedDocuments без await; затем delete без await |
| heal | treated и sterilized | +1 день, впервые со стерилизацией ещё +2; deadly исключён из автоматического treat; update без await |
| allApplicableEffects → applyActiveEffects | Активные transfer-эффекты Item | Фаза/приоритет, применение через DataField и подготовленные значения Actor; multiply=10 раньше add=20; исходный JSON не записывается |

## Используемые сущности и зависимости

| Сущность | Источник | Вид связи | Место/цель и доказательство |
| --- | --- | --- | --- |
| criticalWounds | [system.json](../../../../../../../system.json) | Регистрация | Строки 28,52–56; Item-пакет и packFolders |
| compilePack / extractPack | [utils/packs.mjs](../../../../../../../utils/packs.mjs), [utils/extract.mjs](../../../../../../../utils/extract.mjs) | Сборка/экспорт | Рекурсивные JSON и folders:true; статически, без записи |
| CriticalWoundData.defineSchema/treat/heal | [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) | Модель и переходы | Поля system и followUp; реальные вызовы на всех документах |
| registerDataModels | [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | Реестр | criticalWound:52 и base:73 |
| WitcherItem.migrateData/migrateSpells | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Миграция документа | Статически: Hexes/Rituals здесь отсутствуют; исполнялся BaseItem с реальной системной моделью |
| WitcherActiveEffectData.defineSchema | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js) | Наследование схемы | super сохраняет system.changes; флаги по умолчанию false |
| WitcherActiveEffect.isSuppressed | [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Подавление и применение | Настоящий класс; disabled/transfer/applySelf-контроли |
| CharacterData/CommonActorData | [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js) | Схема Actor | Настоящие модели и базовая подготовка |
| calculateStats/calculateFixedDerivedStats/calculateDerivedStats | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Расчёт | Настоящие методы после initial effects; вес/броня=0 |
| ready/getIndex | [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Подготовка индекса | 62–67: четыре запрошенных поля; серверный getIndex не исполнялся |
| criticalWoundsPack | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | Настройка | Выбор пакета по ключу; проверен код и индекс-фасад |
| BaseItem/BaseActor/BaseActiveEffect, NumberField/SchemaField | Foundry 14.367.0; /opt/foundryvtt/common/documents/ и common/data/fields.mjs | Внешнее ядро | Настоящие классы, строгая валидация и штатная миграция |
| ActiveEffect.prepareBaseData/applyChange; Actor.applyActiveEffects | Foundry 14.367.0; /opt/foundryvtt/client/documents/active-effect.mjs и actor.mjs | Внешнее ядро | Реальные методы с фасадом окружения; в этой порции 36 изменений адресуют NumberField, семь — SchemaField; один числовой вложенный путь требует уже существующей bleed-записи |

## Известные потребители

| Потребитель | Используемые данные | Условия и доказательство |
| --- | --- | --- |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | criticalLevel/treatment/location/lesserEffect и UUID | applyCritWound:312–345; восемь проверок выбора на очищенном индексе |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | name/type и модификаторы Actor | addItem:259–273 и расчёты; реальные методы |
| [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) | UUID и system.treat | _onTreat:12–17; статическая связь, treat исполнен отдельно |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Item и followUp | _onDropItem:17–21 сохраняет item.uuid; браузер не запускался |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../../templates/sheets/item/criticalWound-sheet.hbs) | Имя/изображение/system | Редактор полей и UUID; статическое чтение |
| [templates/partials/crit-wounds-table.hbs](../../../../../../../templates/partials/crit-wounds-table.hbs) | Локация, лечение, дни, UUID | lookup локации:18; кнопка вызывает treat |
| [module/actor/sheets/mixins/healMixin.js](../../../../../../../module/actor/sheets/mixins/healMixin.js) | system.heal | recoverActor:88 без ожидания; статическая связь, heal исполнен отдельно |
| [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) → [module/scripts/combat/applyDamage.js](../../../../../../../module/scripts/combat/applyDamage.js) → [module/scripts/damageInstance.js](../../../../../../../module/scripts/damageInstance.js) | combatEffects.turnStartEffects.* | applyCombatEffects:41–45 читает Object.values; statuses не заменяет запись урона; реальный handler на исходных данных получил пустой набор |

Текстовая [Deadly Critical](../../../../../../../packsJson/combat/Deadly_Critical_GoXapMH54rEUWaZn.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Папка: [Deadly](_Folder.json.md). Предшественник: [Heart Damage (Stabilized)](Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json.md). followUp=null; реальный treat инициировал только удаление текущего Item. Создание/удаление перехвачены и возвращали pending Promise. Переход загружает другой шаблон с его собственными эффектами; не переписывает изменения прежнего эффекта. На новой подготовке без Item его воздействия не применяются.

Контрольный Actor: восемь unmodifiedMax=5, HP.value=25, dodge.value=athletics.value=8 до эффектов, броня/вес=0. Результат: INT=5, WILL=5, REF=5, DEX=5, BODY=5, SPD=5; BODY.max=5, SPD.max=5; RUN=15, LEAP.value=3, LEAP.max=3, ENC=50, STUN=5, REC=5, HP.max=25, HP.value=25, RESOLVE.max=25, FOCUS.max=15, STA.max=25, STA.value=0; healingTime=0. Навыки: dodge.value=8, dodge.activeEffectModifiers=0; athletics.value=8, athletics.activeEffectModifiers=0; awareness.value=0, awareness.activeEffectModifiers=0. Статусы=`[]`; turnStartEffects={}. После initial, до расчётов: `{"staMax":0,"spdMax":5,"bodyMax":5}`. Значения прочитаны непосредственно из подготовленных полей; DataModel.toObject возвращает источник и не заменяет такую проверку.

Единственное изменение — ADD 2 к bleed.damage.modifier, NumberField. При пустом turnStartEffects исходного Actor путь отсутствует: ядро выдало предупреждение проверки числа, запись не появилась, обработчик не вызвал урон. При заранее заданном Actor.bleed с amount=2 реальная схема создала modifier=0; тот же эффект поднял его до 2, обработчик передал урон 4. Это модификатор уже существующего кровотечения, не создание bleed и не ADD объекта из issue-00328. Источник с пустым description сам не обещает создать отдельное кровотечение.

В Deadly calculateHealingTime не имеет отдельной ветви и оставляет экспортный healingTime=0. heal прибавляет дни treated, но условие criticalLevel != deadly запрещает автоматический treat независимо от числа дней. Ручной treat всё равно доступен, включая удаление конечного Item. None/stabilized инициируют update({}); записи не ожидаются.

## Проверки и доказательства

[Протокол .061](../../../../review-log.md#task-0003061): все 23 JSON / 2131 строка прочитаны; 22 Item, Folder, 21 эффект (20 активных), 43 changes и 14 followUp проверены индивидуально. Основной сценарий — 758 утверждений: строгие модели, поля/производные, все treat, восемь heal, восемь вариантов выбора, повтор addItem, подписи Awareness и контроли включённости/переноса. Периодический сценарий — 40 утверждений: семь ADD объектов и отдельный числовой modifier, два override-контроля, положительная проверка модификатора существующей bleed. Всего по Deadly 798. Итоговый повтор всего пакета — ещё 3182 утверждения на 94 Item/4 Folder/79 effects/360 changes/62 переходах и 48 выборах; повтор шести пакетов RollTable — 5223. Всего в .061: 9203 утверждения. Числа относятся к общим сценариям, значения данного документа указаны выше.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. ADD SchemaField, NumberField modifier, statuses и очередь начала хода различены. Исходные16 ADD объектов не достигают урона; override-копии только диагностические. Остаются одноимённые источники при удалении, start/expiry/updateDuration/registry, Combat/GM и конечные HP. .017/.018 сохраняют эти границы без исправления экспорта. Границы: [U012-05](../../../../cross-check-0002.md#u012-05) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-14 — полная карточка в TASK-0003.061 на указанном коммите; исходник не изменён. [Протокол .061](../../../../review-log.md#task-0003061) содержит общие условия и индивидуальные проверки.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Item `Me9fgalLrB0i9Z2O` («Heart Damage (Treated)»): `deadly/treated/torso`; 1 ActiveEffect, 1 changes. Предшественник: `O8EM4quPU4A5VOHH`; `followUp=null`: ручной `treat()` запрашивает удаление этого Item.

Этот Item отсекается начальным фильтром `treatment=none`, но доступен через ссылку предыдущего состояния. Расчёт срока оставляет экспортный `healingTime=0`; `heal` не завершает Deadly автоматически. Сверены адреса: `system.combatEffects.turnStartEffects.bleed.damage.modifier`.

Heart none/stabilized: BODY/SPD.max×0.25/×0.5, STA.max тоже; calculateStat вычисляет value отдельно, calculateDerivedStat перезаписывает STA.max. Treated: числовой ADD2 к bleed.damage.modifier; при пустой карте запись не появляется, при существующей amount2 даёт modifier2 и запрос урона 4. Spetic: INT/WILL/REF/DEX−3/−1/нет, STA.max×0.25/×0.5, treated STA.totalModifiers−5; poison только none. Death save Heart задан текстом. Общая связь periodic-записи с обработчиком разобрана в R012-24; status сам по себе не вызывает урон.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js.md), [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs.md), [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json](Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-22](../../../../cross-check-0002.md#r012-22), [R012-24](../../../../cross-check-0002.md#r012-24). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.

</details>
