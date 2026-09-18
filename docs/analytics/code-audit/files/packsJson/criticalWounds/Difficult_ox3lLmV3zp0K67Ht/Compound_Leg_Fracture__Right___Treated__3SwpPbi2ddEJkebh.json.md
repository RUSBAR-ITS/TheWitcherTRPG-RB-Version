# packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json

## Текущий численный контракт — 14.3.1.00069

TASK-0010.010: численные строки находятся в `system.changes`, с `type`/`phase` и настройками канала. Классификация: П: 1, Р: 2. П — параметр, Р — бросок, Р? — выбор условия; native — периодика. Все fullEffect/shiftsCap/affectsAdvancement выключены. Исключения: нет. UUID/стадия/переходы/заживление, прочие поля Item/AE сохранены.

Цели/операции и контрольные значения каждой строки — [матрица .010](../../../../../task-0010-010-content-matrix.md). Потребители: [WitcherActiveEffectData](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js), [parameterPreparation](../../../../../../../module/actor/parameterPreparation.js), [derivedPreparation](../../../../../../../module/actor/derivedPreparation.js), [rollContext](../../../../../../../module/actor/rollContext.js). Методы сам JSON не объявляет. Чисто статусные строки остаются native. Локальная подготовка прошла; установленная база будет обновляться в .011, мир — .013. Датированные значения прежнего анализа ниже заменены этим контрактом в затронутой части.


## Актуальный контракт — 14.3.1.00049

Шаблон criticalWound; существующие UUID, имя, описание, effects/changes/statuses/priority/transfer и папка сохранены. `followUp` и сохраняемый `healingTime` удалены. Новые данные управляют общими операциями, специальных правил по ID в коде нет.

| Поле | Значение |
| --- | --- |
| `woundTypeId` | `"compound-leg-fracture"` |
| `location` | `"rightLeg"` |
| `treatment` | `"treated"` |
| `cannotStabilize` | `true` |
| `cannotTreat` | `true` |
| `canHeal` | `true` |
| `healingDuration` | `"max(15-@body,1)"` |
| `stabilizedWound` | `null` |
| `treatedWound` | `null` |
| `daysHealed` | `0` |
| `sterilized` | `false` |

Используется через [module/item/criticalWoundOperations.js](../../../../../../../module/item/criticalWoundOperations.js) и [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js). Цели с тем же ID/местом проверены; полный список — [матрица](../../../../../critical-wounds-content-matrix.md). JSON/сборка/установка сверены; [протокол](../../../../../task-0009-lifecycle-checks.md). Численный пересчёт эффектов остаётся TASK-0010. Старые датированные сведения ниже не описывают новые переходы.

## Текущий срез — 14.3.1.00016

| Поле | Значение |
| --- | --- |
| Источник | [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json](../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json) |
| Проверено | 2026-09-16; `dev`; база `095395276b97f0ffe916495e26be3938cf8fdcf8` + исправление [issue-00331 / К01](../../../../../../issues/closed/issue-00331.md) |
| Тип / назначение | Экспорт Item criticalWound: шаблон травмы, его эффекты и следующий этап лечения |
| Имя / ID | Compound Leg Fracture (Right - Treated) / `3SwpPbi2ddEJkebh` |
| Строк / SHA-256 | 104 / `cd65b84b34813a10efeb6a8901382951d702f7c6c55e93a8d81a1923a9d51752` |

### Выполненные исправления

B16: исправить сторону в имени эффекта. Остальные поля сохранены. Текущие значения и связи перечислены ниже; архив в конце описывает прежние срезы.

| Поле system | Текущее значение |
| --- | --- |
| `htmlFields` | ["description"] |
| `description` | "" |
| `criticalLevel` | "difficult" |
| `treatment` | "treated" |
| `location` | "rightLeg" |
| `lesserEffect` | false |
| `daysHealed` | 0 |
| `healingTime` | 0 |
| `sterilized` | false |
| `followUp` | null |

1 ActiveEffect; 3 changes. ID и `_key` сохранённых эффектов, origin, transfer, duration и несвязанные значения сохранены.

#### Compound Leg Fracture (Right - Treated) — HPHyTnnqile8vU2V

Строка `_id`: 36. `disabled=false`, `transfer=true`; statuses: `[]`.

| key | mode | value | priority |
| --- | --- | --- | --- |
| `system.stats.spd.totalModifiers` | 2 | "-2" | null |
| `system.skills.ref.dodge.activeEffectModifiers` | 2 | "-2" | null |
| `system.skills.dex.athletics.activeEffectModifiers` | 2 | "-2" | null |

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
| Исходный файл | [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json](../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-13 |
| Ветка и коммит | rusbar-main, aef03ca01b0db5887653d2b1301a4fe814372a3e |
| Изменения относительно коммита | Нет; 104 строк; SHA-256 1df534e56e546df10efeefd8f0913350139bb9078c96ec0ca98e1778bf2dc3da |
| Задача и порция | [TASK-0003.060](../../../../../../tasks/task-0003.060.md) |
| Запись перекрёстной сверки | [Протокол .060](../../../../review-log.md#task-0003060) |

## Назначение файла

Экспорт Compound Leg Fracture (Right - Treated): состояние treated, локация rightLeg. Вложенных ActiveEffect: 1; изменений: 3. Данные задают шаблон травмы и её переход; действия выполняют потребители системы и Foundry.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

[ready:62–67](../../../../../../../module/TheWitcherTRPG.js) запрашивает четыре поля индекса: system.criticalLevel/location/lesserEffect/treatment; выбор пакета задаёт [criticalWoundsPack](../../../../../../../module/setup/settings.js). Item исключается из исходного выбора по treatment и используется через followUp или ручное добавление. Проверен индекс-фасад из настоящих очищенных моделей, не действующий серверный индекс.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Compound Leg Fracture (Right - Treated) | Корневой Item; name:3, _id:97 | ID `3SwpPbi2ddEJkebh`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Item.3SwpPbi2ddEJkebh` | Загрузка, копирование к Actor, подготовка, лечение/удаление |
| _key / folder / sort | Корневые поля | `"!items!3SwpPbi2ddEJkebh"` / `"ox3lLmV3zp0K67Ht"` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| img / ownership | Корневые поля | `"icons/svg/item-bag.svg"` / `{"default":0,"ugXtPMJIktbl63QV":3}` | Ресурс ядра вне пофайлового анализа; наличие указанного пользователя в мире не подтверждено |
| system / effects | Объекты, строки 6 / 20 | criticalWound / 1 embedded ActiveEffect | Схема и воздействия перечислены далее |

| Поле system | Экспортное значение | Смысл и потребитель |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация; defineSchema её не содержит, очистка модели удаляет поле. |
| description | `""` | HTMLField; enrichedText/createEnrichedText, редактор и сообщение applyCritWound. Текст не преобразуется в changes. |
| criticalLevel | `"difficult"` | StringField; выбор кандидатов и ветвь difficult расчёта healingTime. |
| treatment | `"treated"` | StringField; выбор none и проверка treated в heal. |
| location | `"rightLeg"` | StringField; фильтр applyCritWound и lookup подписи списка. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах first find: false для >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик заживления, редактирование и update в heal. |
| healingTime | `0` | NumberField; у владельца Actor prepareDerivedData рассчитывает max(15−BODY.max,1). |
| sterilized | `false` | BooleanField; новая стерилизация даёт ещё +2 дня к очередному дню. |
| followUp | `null` | DocumentUUIDField типа Item; treat загружает адресата или удаляет конечный Item. |

### ActiveEffect 1: Compound Leg Fracture (Left - Treated)

ID `HPHyTnnqile8vU2V`; _key=`"!items.effects!3SwpPbi2ddEJkebh.HPHyTnnqile8vU2V"`. Origin=`"Item.kfyfxEVsMRUDDk1A"` — ссылка на мировой Item; существование адресата не проверялось. Цель переноса при transfer=true — Actor-владелец текущего Item; origin не выбирает другого владельца.

Тип `"base"`, name:23; disabled=false, transfer=true; img=`"icons/svg/item-bag.svg"`, description=`""`, tint=`"#ffffff"`, sort=0, statuses=`[]`. Flags=`{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`; _stats=`{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. System до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`.

Duration до миграции: `{"startTime":null,"combat":null,"seconds":null,"rounds":null,"turns":null,"startRound":null,"startTurn":null}`. Подготовлено: start=null, value=Infinity, units=seconds, expiry=null, expired=false. Пустая длительность становится неограниченной при prepareBaseData; таймер этой записи не задан. applyAfterCalculations получает false, changes переходят в system.changes/initial. Statuscounter — внешний модуль; в фасаде без регистрации его flags очищаются, работа установленного модуля не проверена.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Источник поля / фактическое значение |
| --- | --- | --- | --- | --- |
| 1 / 45 | `system.stats.spd.totalModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js); -2 |
| 2 / 51 | `system.skills.ref.dodge.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 3 / 57 | `system.skills.dex.athletics.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |

Повторение ID эффекта у разных Item не коллизия внутри одной коллекции effects. Вложенный _key указывает собственного владельца независимо от origin/name.

## Основные функции и методы

JSON не вводит собственных функций или обработчиков. Действия принадлежат следующим потребителям:

| Метод | Вход / условие | Результат и граница ожидания |
| --- | --- | --- |
| applyCritWound → addItem | Уровень, локация, critEffect и индекс | Выбор Item, запрос добавления и чат; повтор name/type может попасть в quantity |
| prepareDerivedData → calculateHealingTime | Родитель Actor | healingTime=max(15−BODY.max,1), вычисление без самостоятельной записи |
| treat | followUp или null | await fromUuid; createEmbeddedDocuments без await; затем delete без await |
| heal | treated и sterilized | +1 день, впервые со стерилизацией ещё +2; по достижении healingTime → treat; иначе update без await |
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
| ActiveEffect.prepareBaseData/applyChange; Actor.applyActiveEffects | Foundry 14.367.0; /opt/foundryvtt/client/documents/active-effect.mjs и actor.mjs | Внешнее ядро | Реальные методы с фасадом окружения; 189 изменений адресуют NumberField, девять — SchemaField, три пути commonspeech отсутствуют в схеме |

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
| [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | skills.*.activeEffectModifiers, effect.name | addActiveEffects:1–23; фрагмент dodge правой treated ноги реально получен |

Текстовая [Difficult Critical](../../../../../../../packsJson/combat/Difficult_Critical_VIup1SZTMKCSGGbT.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Папка: [Difficult](_Folder.json.md). Предшественник: [Compound Leg Fracture (Right - Stabilized)](Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json.md). followUp=null; реальный treat инициировал только удаление текущего Item. Создание/удаление перехвачены и возвращали pending Promise. Переход загружает другой шаблон с его собственными эффектами; не переписывает изменения прежнего эффекта. На новой подготовке без Item его воздействия не применяются.

Контрольный Actor: восемь unmodifiedMax=5, HP.value=25, dodge.value=athletics.value=8 до эффектов, броня/вес=0. Результат: INT=5, WILL=5, REF=5, DEX=5, BODY=5, SPD=3; BODY.max=5, SPD.max=5; RUN=9, LEAP.value=1, LEAP.max=3, ENC=50, STUN=5, REC=5, HP.max=25, RESOLVE.max=25, FOCUS.max=15; healingTime=10. Навыки: dodge.value=8, dodge.activeEffectModifiers=-2; athletics.value=8, athletics.activeEffectModifiers=-2. Статусы=`[]`; turnStartEffects={}. Значения прочитаны непосредственно из подготовленных полей; сериализация DataModel/toObject возвращает источник и не заменяет такую проверку.

В цепочках правых переломов у stabilized перепутаны rightArm/rightLeg, при переходе к treated возвращается исходная локация — [issue-00327](../../../../../../issues/closed/issue-00327.md). Модель/treat не исправляют это поле.

Настоящий addActiveEffects('dodge') при displayRollsDetails=true дал `" +-2[Compound Leg Fracture (Left - Treated)]"`: эффект подписан левой ногой — [issue-00326](../../../../../../issues/closed/issue-00326.md).

## Проверки и доказательства

[Протокол .060](../../../../review-log.md#task-0003060): все 25 JSON / 3351 строк прочитаны, корневые ID/_key сверены среди 98 criticalWounds, вложенные _key/ID — в своей области. Все 16 followUp проверены до конечного состояния, без циклов и переходов вне Difficult. Настоящие модели и методы в изолированном Node 24.16.0 прошли 1748 утверждений: 24 Item, Folder, 25 effects/201 changes, подготовленные поля/производные, 24 treat, семь heal, восемь выборов, повторный addItem, исключение эффекта и подпись правой treated ноги. Отдельный сценарий: 43 утверждения, девять исходных периодических записей и три диагностические копии с override вместо ADD. Всего 1791 утверждение. Числа относятся к порции, индивидуальные значения указаны выше.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. min1 срока отличается от отсутствия общего clamp характеристики; max/value/totalModifiers и priority сопоставлены. Остаются пользовательские изменения полей/приоритетов/фаз, другие сочетания эффектов и конкурентное heal до сохранения sterilized. Критерий: учитывать конкретный путь/фазу и prepared-поле, не сериализованный _source; новый порядок/потолок не вводится. Границы: [U012-04](../../../../cross-check-0002.md#u012-04) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/closed/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/closed/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/closed/issue-00288.md) — повтор name/type. [issue-00327](../../../../../../issues/closed/issue-00327.md) — локации стабилизированных правых переломов. [issue-00326](../../../../../../issues/closed/issue-00326.md) — имя левой ноги у правого Item. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-13 — полная карточка в TASK-0003.060 на указанном коммите; исходник не изменён. [Протокол .060](../../../../review-log.md#task-0003060) содержит общие условия и индивидуальные проверки.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Item `3SwpPbi2ddEJkebh` («Compound Leg Fracture (Right - Treated)»): `difficult/treated/rightLeg`; 1 ActiveEffect, 3 changes. Предшественник: `QCugb1JqpiFyBEN4`; `followUp=null`: ручной `treat()` запрашивает удаление этого Item.

Этот Item отсекается начальным фильтром `treatment=none`, но доступен через ссылку предыдущего состояния. При контрольном `BODY.max=5` срок 10 дней независимо от штрафов к `BODY.value`. Сверены адреса: `system.stats.spd.totalModifiers`, `skill.activeEffectModifiers`.

Множители адресуют SPD.max и dodge/athletics.value; treated использует totalModifiers/activeEffectModifiers. При базе 5 и навыках 8 none даёт SPD.max1/value5 и навыки 2, stabilized max3/value5 и навыки 4. Правая stabilized имеет rightArm (00327), treated-эффект назван Left (00326). Round1 у bleed не подтверждает автоматическое снятие.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js.md), [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs.md), [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json](Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-17](../../../../cross-check-0002.md#r012-17). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.

</details>
