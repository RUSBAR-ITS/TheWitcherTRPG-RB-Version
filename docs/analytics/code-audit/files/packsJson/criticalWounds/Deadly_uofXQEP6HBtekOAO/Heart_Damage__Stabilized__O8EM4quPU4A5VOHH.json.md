# packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json

## Текущий численный контракт — 14.3.1.00069

TASK-0010.010: численные строки находятся в `system.changes`, с `type`/`phase` и настройками канала. Классификация: П: 3. П — параметр, Р — бросок, Р? — выбор условия; native — периодика. Все fullEffect/shiftsCap/affectsAdvancement выключены. Исключения: stats.body → sta. UUID/стадия/переходы/заживление, прочие поля Item/AE сохранены.

Цели/операции и контрольные значения каждой строки — [матрица .010](../../../../../task-0010-010-content-matrix.md). Потребители: [WitcherActiveEffectData](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js), [parameterPreparation](../../../../../../../module/actor/parameterPreparation.js), [derivedPreparation](../../../../../../../module/actor/derivedPreparation.js), [rollContext](../../../../../../../module/actor/rollContext.js). Методы сам JSON не объявляет. Чисто статусные строки остаются native. Локальная подготовка прошла; установленная база будет обновляться в .011, мир — .013. Датированные значения прежнего анализа ниже заменены этим контрактом в затронутой части.


## Актуальный контракт — 14.3.1.00049

Шаблон criticalWound; существующие UUID, имя, описание, effects/changes/statuses/priority/transfer и папка сохранены. `followUp` и сохраняемый `healingTime` удалены. Новые данные управляют общими операциями, специальных правил по ID в коде нет.

| Поле | Значение |
| --- | --- |
| `woundTypeId` | `"heart-damage"` |
| `location` | `"torso"` |
| `treatment` | `"stabilized"` |
| `cannotStabilize` | `true` |
| `cannotTreat` | `false` |
| `canHeal` | `false` |
| `healingDuration` | `""` |
| `stabilizedWound` | `null` |
| `treatedWound` | `"Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.Me9fgalLrB0i9Z2O"` |
| `daysHealed` | `0` |
| `sterilized` | `false` |

Используется через [module/item/criticalWoundOperations.js](../../../../../../../module/item/criticalWoundOperations.js) и [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js). Цели с тем же ID/местом проверены; полный список — [матрица](../../../../../critical-wounds-content-matrix.md). JSON/сборка/установка сверены; [протокол](../../../../../task-0009-lifecycle-checks.md). Численный пересчёт эффектов остаётся TASK-0010. Старые датированные сведения ниже не описывают новые переходы.

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json](../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.061](../../../../../../tasks/task-0003.061.md) |
| Запись перекрёстной сверки | [Протокол .061](../../../../review-log.md#task-0003061) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Внутренние UUID направлены на TheWitcherTRPG-RB-Version. ID документов, диапазоны, эффекты и _stats сохранены. Датированные результаты и прежние значения UUID ниже являются историей.

## Назначение файла

Экспорт Heart Damage (Stabilized): состояние stabilized, локация torso. Содержит 1 ActiveEffect и 3 изменений. Данные задают шаблон травмы и её переход; действия выполняют потребители системы и Foundry.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

[ready:62–67](../../../../../../../module/TheWitcherTRPG.js) запрашивает четыре поля индекса: system.criticalLevel/location/lesserEffect/treatment; выбор пакета задаёт [criticalWoundsPack](../../../../../../../module/setup/settings.js). Item исключается из исходного выбора по treatment и используется через followUp или ручное добавление. Проверен индекс-фасад из настоящих очищенных моделей, не действующий серверный индекс.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Heart Damage (Stabilized) | Корневой Item; name:3, _id:97 | ID `O8EM4quPU4A5VOHH`; UUID `Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.O8EM4quPU4A5VOHH` | Загрузка, копирование к Actor, подготовка, лечение/удаление |
| _key / folder / sort | Корневые поля | `"!items!O8EM4quPU4A5VOHH"` / `"uofXQEP6HBtekOAO"` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| img / ownership | Корневые поля | `"icons/svg/item-bag.svg"` / `{"default":0,"ugXtPMJIktbl63QV":3}` | Ресурс ядра вне пофайлового анализа; наличие указанного пользователя в мире не подтверждено |
| system / effects | Объекты, строки 6 / 20 | criticalWound / 1 embedded ActiveEffect | Схема и воздействия перечислены далее |

| Поле system | Экспортное значение | Смысл и потребитель |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация; defineSchema её не содержит, очистка модели удаляет поле. |
| description | `"<ul><li><p>halve your Stamina, SPD, and BODY</p></li></ul>"` | HTMLField; enrichedText/createEnrichedText, редактор и сообщение applyCritWound. Текст не преобразуется в changes. |
| criticalLevel | `"deadly"` | StringField; выбор deadly и исключение автоматического treat из heal; ветви deadly в calculateHealingTime нет. |
| treatment | `"stabilized"` | StringField; выбор none и проверка treated в heal. |
| location | `"torso"` | StringField; фильтр applyCritWound и lookup подписи списка. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах first find: false для >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик заживления, редактирование и update в heal. |
| healingTime | `0` | NumberField; для deadly ветви расчёта нет, экспортный 0 сохраняется у Actor. |
| sterilized | `false` | BooleanField; новая стерилизация даёт ещё +2 дня к очередному дню. |
| followUp | `"Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.Me9fgalLrB0i9Z2O"` | DocumentUUIDField типа Item; treat загружает адресата или удаляет конечный Item. |

### ActiveEffect 1: Heart Damage (Stabilized)

ID `NbNfYdReYhlODejB`; _key=`"!items.effects!O8EM4quPU4A5VOHH.NbNfYdReYhlODejB"`. Origin=`"Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.O8EM4quPU4A5VOHH"` — UUID текущего Item в компедиуме, сопоставлен с экспортом. Цель переноса при transfer=true — Actor-владелец текущего Item; origin не выбирает другого владельца.

Тип `"base"`, name:23; disabled=false, transfer=true, active=true; img=`"icons/svg/item-bag.svg"`, description=`""`, tint=`"#ffffff"`, sort=0, statuses=`[]`. Flags=`{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`; _stats=`{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. System до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`.

Duration до миграции: `{"startTime":null,"combat":null,"seconds":null,"rounds":null,"turns":null,"startRound":null,"startTurn":null}`. Подготовлено: start=null, value=Infinity, units=seconds, expiry=null, expired=false. Пустая длительность становится неограниченной при prepareBaseData; таймер этой записи не задан. applyAfterCalculations получает false, changes переходят в system.changes/initial. Statuscounter — внешний модуль; в фасаде без регистрации его flags очищаются, работа установленного модуля не проверена.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Источник поля / фактическое значение |
| --- | --- | --- | --- | --- |
| 1 / 45 | `system.stats.body.max` | 1 / `"0.5"` / `null` | multiply; `0.5`; priority=10; phase=initial | NumberField; [statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js); 3 |
| 2 / 51 | `system.stats.spd.max` | 1 / `"0.5"` / `null` | multiply; `0.5`; priority=10; phase=initial | NumberField; [statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js); 3 |
| 3 / 57 | `system.derivedStats.sta.max` | 1 / `"0.5"` / `null` | multiply; `0.5`; priority=10; phase=initial | NumberField; [derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); 25 |

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

Текстовая [Deadly Critical](../../../../../../../packsJson/combat/Deadly_Critical_GoXapMH54rEUWaZn.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Папка: [Deadly](_Folder.json.md). Предшественник: [Heart Damage](Heart_Damage_PVraD16y2VWkOH6J.json.md). Следующий Item: [Heart Damage (Treated)](Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json.md), `Me9fgalLrB0i9Z2O`, treatment=treated. Реальный treat инициировал создание этого документа, затем удаление текущего. Создание/удаление перехвачены и возвращали pending Promise. Переход загружает другой шаблон с его собственными эффектами; не переписывает изменения прежнего эффекта. На новой подготовке без Item его воздействия не применяются.

Контрольный Actor: восемь unmodifiedMax=5, HP.value=25, dodge.value=athletics.value=8 до эффектов, броня/вес=0. Результат: INT=5, WILL=5, REF=5, DEX=5, BODY=5, SPD=5; BODY.max=3, SPD.max=3; RUN=15, LEAP.value=3, LEAP.max=1, ENC=50, STUN=5, REC=5, HP.max=25, HP.value=25, RESOLVE.max=25, FOCUS.max=15, STA.max=25, STA.value=0; healingTime=0. Навыки: dodge.value=8, dodge.activeEffectModifiers=0; athletics.value=8, athletics.activeEffectModifiers=0; awareness.value=0, awareness.activeEffectModifiers=0. Статусы=`[]`; turnStartEffects={}. После initial, до расчётов: `{"staMax":0,"spdMax":3,"bodyMax":3}`. Значения прочитаны непосредственно из подготовленных полей; DataModel.toObject возвращает источник и не заменяет такую проверку.

Множитель адресует max, а calculateStat читает unmodifiedMax+totalModifiers: SPD.value/BODY.value не вычисляются из изменённого max. Целочисленный NumberField округляет 5×0.25 до 1, 5×0.5 до 3. RUN и LEAP.value используют value, LEAP.max — max; последствия различаются — [issue-00036](../../../../../../issues/potential/issue-00036.md). Выключенное изменение сюда не применяется.

STA.max до initial равен 0 в этом свежем Actor; множитель оставляет 0. calculateDerivedStats затем заново присваивает максимум через BODY.value/WILL.value и STA.totalModifiers: получено 25. Это проверка перезаписи поля, а не доказательство сохранения множителя до final — [issue-00036](../../../../../../issues/potential/issue-00036.md).

В Deadly calculateHealingTime не имеет отдельной ветви и оставляет экспортный healingTime=0. heal прибавляет дни treated, но условие criticalLevel != deadly запрещает автоматический treat независимо от числа дней. Ручной treat всё равно доступен, включая удаление конечного Item. None/stabilized инициируют update({}); записи не ожидаются.

## Проверки и доказательства

[Протокол .061](../../../../review-log.md#task-0003061): все 23 JSON / 2131 строка прочитаны; 22 Item, Folder, 21 эффект (20 активных), 43 changes и 14 followUp проверены индивидуально. Основной сценарий — 758 утверждений: строгие модели, поля/производные, все treat, восемь heal, восемь вариантов выбора, повтор addItem, подписи Awareness и контроли включённости/переноса. Периодический сценарий — 40 утверждений: семь ADD объектов и отдельный числовой modifier, два override-контроля, положительная проверка модификатора существующей bleed. Всего по Deadly 798. Итоговый повтор всего пакета — ещё 3182 утверждения на 94 Item/4 Folder/79 effects/360 changes/62 переходах и 48 выборах; повтор шести пакетов RollTable — 5223. Всего в .061: 9203 утверждения. Числа относятся к общим сценариям, значения данного документа указаны выше.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. ADD SchemaField, NumberField modifier, statuses и очередь начала хода различены. Исходные16 ADD объектов не достигают урона; override-копии только диагностические. Остаются одноимённые источники при удалении, start/expiry/updateDuration/registry, Combat/GM и конечные HP. .017/.018 сохраняют эти границы без исправления экспорта. Границы: [U012-05](../../../../cross-check-0002.md#u012-05) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/closed/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/closed/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/closed/issue-00288.md) — повтор name/type. [issue-00036](../../../../../../issues/potential/issue-00036.md) — max/value и перезапись производного максимума. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-14 — полная карточка в TASK-0003.061 на указанном коммите; исходник не изменён. [Протокол .061](../../../../review-log.md#task-0003061) содержит общие условия и индивидуальные проверки.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Item `O8EM4quPU4A5VOHH` («Heart Damage (Stabilized)»): `deadly/stabilized/torso`; 1 ActiveEffect, 3 changes. Предшественник: `PVraD16y2VWkOH6J`; `followUp` ведёт к `Me9fgalLrB0i9Z2O` («Heart Damage (Treated)», `treated/torso`).

Этот Item отсекается начальным фильтром `treatment=none`, но доступен через ссылку предыдущего состояния. Расчёт срока оставляет экспортный `healingTime=0`; `heal` не завершает Deadly автоматически. Сверены адреса: `system.stats.body.max`, `system.stats.spd.max`, `system.derivedStats.sta.max`.

Heart none/stabilized: BODY/SPD.max×0.25/×0.5, STA.max тоже; calculateStat вычисляет value отдельно, calculateDerivedStat перезаписывает STA.max. Treated: числовой ADD2 к bleed.damage.modifier; при пустой карте запись не появляется, при существующей amount2 даёт modifier2 и запрос урона 4. Spetic: INT/WILL/REF/DEX−3/−1/нет, STA.max×0.25/×0.5, treated STA.totalModifiers−5; poison только none. Death save Heart задан текстом.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js.md), [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs.md), [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json](Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json.md), [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json](Heart_Damage_PVraD16y2VWkOH6J.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-22](../../../../cross-check-0002.md#r012-22). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
