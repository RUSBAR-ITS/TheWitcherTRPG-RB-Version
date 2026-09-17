# packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json

## Текущий срез — 14.3.1.00016

| Поле | Значение |
| --- | --- |
| Источник | [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json](../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json) |
| Проверено | 2026-09-16; `dev`; база `095395276b97f0ffe916495e26be3938cf8fdcf8` + исправление [issue-00331 / К01](../../../../../../issues/closed/issue-00331.md) |
| Тип / назначение | Экспорт Item criticalWound: шаблон травмы, его эффекты и следующий этап лечения |
| Имя / ID | Minor Head Wound / `wPRuwd7RdLWnWmnb` |
| Строк / SHA-256 | 104 / `3503f78aab66a45f4b15343aab91966ab06d33211bc68f28c81c05d26a1bd152` |

### Выполненные исправления

B14: анатомическая локация. Остальные поля сохранены. Текущие значения и связи перечислены ниже; архив в конце описывает прежние срезы.

| Поле system | Текущее значение |
| --- | --- |
| `htmlFields` | ["description"] |
| `description` | "" |
| `criticalLevel` | "complex" |
| `treatment` | "none" |
| `location` | "head" |
| `lesserEffect` | false |
| `daysHealed` | 0 |
| `healingTime` | 0 |
| `sterilized` | false |
| `followUp` | "Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.EnwgL7ApZTdHgMbD" |

1 ActiveEffect; 3 changes. ID и `_key` сохранённых эффектов, origin, transfer, duration и несвязанные значения сохранены.

#### Minor Head Wound — J7E3yf7R3ZvwDodi

Строка `_id`: 36. `disabled=false`, `transfer=true`; statuses: `[]`.

| key | mode | value | priority |
| --- | --- | --- | --- |
| `system.stats.int.totalModifiers` | 2 | "-1" | null |
| `system.stats.will.totalModifiers` | 2 | "-1" | null |
| `system.derivedStats.stun.totalModifiers` | 2 | "-1" | null |

### Действия и зависимости

[system.json](../../../../../../../system.json) регистрирует criticalWounds; [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) (`applyCritWound`) читает индекс treatment/location/criticalLevel/lesserEffect, выбирает Item и добавляет его Actor. [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) определяет поля и выполняет treat/heal; [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) и Foundry обрабатывают ActiveEffect. Исправление descriptions само по себе не меняет расчёты.

Следующий этап: [Minor Head Wound (Stabilized)](../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json) — `Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.EnwgL7ApZTdHgMbD`.

### Проверка и границы

Источник входит в 48 изменённых JSON [issue-00331 / К01](../../../../../../issues/closed/issue-00331.md). Все 226 JSON разобраны; 316 documentUuid/followUp разрешимы. Временная сборка шести пакетов и обратное извлечение совпали с исходниками, включая неизменённые документы. Полный клиент Foundry и действующие packs не проверялись; копии уже импортированных документов мира не обновлялись.

Проверки настоящих Roll/методов RollTable и потребителей травм, фасады окружения и нерешённые ограничения 00320/00328/00036 перечислены в issue-00331. Значения Actor и жизненный цикл эффектов этой порцией повторно не проверялись.

## Архив анализа до 14.3.1.00016

**Ниже сохранены датированные доказательства прежнего состояния. Старые числа результатов/эффектов, тексты, ссылки, номера строк и заявления об отсутствии исправлений не описывают текущий JSON. Актуальный срез находится выше.**

<details>
<summary>Предыдущие пофайловые исследования и проверки</summary>

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json](../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.059](../../../../../../tasks/task-0003.059.md) |
| Запись перекрёстной сверки | [Протокол .059](../../../../review-log.md#task-0003059) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Внутренние UUID направлены на TheWitcherTRPG-RB-Version. ID документов, диапазоны, эффекты и _stats сохранены. Датированные результаты и прежние значения UUID ниже являются историей.

## Назначение файла

Экспорт Minor Head Wound: состояние none, локация torso. Содержит 1 ActiveEffect и 3 изменений. Данные задают шаблон травмы и её переход; действия выполняют потребители системы и Foundry.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

[ready:62–67](../../../../../../../module/TheWitcherTRPG.js) запрашивает четыре поля индекса: system.criticalLevel/location/lesserEffect/treatment; выбор пакета задаёт [criticalWoundsPack](../../../../../../../module/setup/settings.js). Item участвует в исходных кандидатах applyCritWound. Проверен индекс-фасад из настоящих очищенных моделей, не действующий серверный индекс.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Minor Head Wound | Корневой Item; name:2, _id:4 | ID `wPRuwd7RdLWnWmnb`; UUID `Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.wPRuwd7RdLWnWmnb` | Загрузка, копирование к Actor, подготовка, лечение/удаление |
| _key / folder / sort | Корневые поля | `"!items!wPRuwd7RdLWnWmnb"` / `"YcLLKtwU75uE8tdC"` / `400000` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| img / ownership | Корневые поля | `"icons/svg/item-bag.svg"` / `{"default":0,"ugXtPMJIktbl63QV":3}` | Ресурс ядра вне пофайлового анализа; наличие указанного пользователя в мире не подтверждено |
| system / effects | Объекты, строки 6 / 20 | criticalWound / 1 embedded ActiveEffect | Схема и воздействия перечислены далее |

| Поле system | Экспортное значение | Смысл и потребитель |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация; defineSchema её не содержит, очистка модели удаляет поле. |
| description | `""` | HTMLField; enrichedText/createEnrichedText, редактор и сообщение applyCritWound. Текст не преобразуется в changes. |
| criticalLevel | `"complex"` | StringField; выбор кандидатов и ветвь complex расчёта healingTime. |
| treatment | `"none"` | StringField; выбор none и проверка treated в heal. |
| location | `"torso"` | StringField; фильтр applyCritWound и lookup подписи списка. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах first find: false для >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик заживления, редактирование и update в heal. |
| healingTime | `0` | NumberField; у владельца Actor prepareDerivedData рассчитывает max(12−BODY.max,1). |
| sterilized | `false` | BooleanField; новая стерилизация даёт ещё +2 дня к очередному дню. |
| followUp | `"Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.EnwgL7ApZTdHgMbD"` | DocumentUUIDField типа Item; treat загружает адресата или удаляет конечный Item. |

### ActiveEffect 1: Minor Head Wound

ID `J7E3yf7R3ZvwDodi`; экспортный _key=`"!items.effects!wPRuwd7RdLWnWmnb.J7E3yf7R3ZvwDodi"`. Origin=`"Item.wPRuwd7RdLWnWmnb"` — ссылка на мировой Item; разрешение такого UUID в действующем мире не проверялось. Она не становится ссылкой на компедиум при совпадении последнего ID и не задаёт цель применения. Цель при transfer=true — Actor-владелец этого Item.

Тип `"base"`, name:23; disabled=false, transfer=true; img=`"icons/svg/item-bag.svg"`, description=`""`, tint=`"#ffffff"`, sort=0, statuses=`[]`. Flags=`{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`; _stats=`{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. System до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`.

Duration до миграции: `{"startTime":null,"combat":null,"seconds":null,"rounds":null,"turns":null,"startRound":null,"startTurn":null}`. Ядро преобразует её в start=null, duration={value:null,units:"seconds",expiry:null,expired:false}; после prepareBaseData value=Infinity. Тикающего срока в данных нет, updateDuration/registry в сценарии не запускались. applyAfterCalculations получает false; все changes мигрируют в system.changes и фазу initial. Флаги statuscounter принадлежат внешнему модулю; без его регистрации ядро очищает их в изолированном окружении, что не доказывает потерю флагов в мире.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Источник поля |
| --- | --- | --- | --- | --- |
| 1 / 45 | `system.stats.int.totalModifiers` | 2 / `"-1"` / `null` | add; -1; priority=20; phase=initial | NumberField; [statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js) |
| 2 / 51 | `system.stats.will.totalModifiers` | 2 / `"-1"` / `null` | add; -1; priority=20; phase=initial | NumberField; [statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js) |
| 3 / 57 | `system.derivedStats.stun.totalModifiers` | 2 / `"-1"` / `null` | add; -1; priority=20; phase=initial | NumberField; [derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js) |

Повторение ID эффекта у разных Item не является коллизией внутри одной коллекции effects. _key каждого вложенного эффекта указывает на собственного владельца, независимо от origin и отображаемого имени.

## Основные функции и методы

JSON не вводит собственных функций или обработчиков. Действия принадлежат следующим потребителям:

| Метод | Вход / условие | Результат и граница ожидания |
| --- | --- | --- |
| applyCritWound → addItem | Уровень, локация, critEffect и индекс | Выбор Item, запрос добавления и чат; повтор name/type может попасть в quantity |
| prepareDerivedData → calculateHealingTime | Родитель Actor | healingTime=max(12−BODY.max,1), вычисление без самостоятельной записи |
| treat | followUp или null | await fromUuid; createEmbeddedDocuments без await; затем delete без await |
| heal | treated и sterilized | +1 день, впервые со стерилизацией ещё +2; по достижении healingTime → treat; иначе update без await |
| allApplicableEffects → applyActiveEffects | Активные transfer-эффекты Item | Фаза/приоритет, применение через NumberField и подготовленные значения Actor; исходный JSON не записывается |

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
| BaseItem/BaseActor/BaseActiveEffect, NumberField | Foundry 14.367.0; /opt/foundryvtt/common/documents/ и common/data/fields.mjs | Внешнее ядро | Настоящие классы, строгая валидация и штатная миграция |
| ActiveEffect.prepareBaseData/applyChange; Actor.applyActiveEffects | Foundry 14.367.0; /opt/foundryvtt/client/documents/active-effect.mjs и actor.mjs | Внешнее ядро | Реальные методы с фасадом окружения; все целевые поля NumberField |

## Известные потребители

| Потребитель | Используемые данные | Условия и доказательство |
| --- | --- | --- |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | criticalLevel/treatment/location/lesserEffect и UUID | applyCritWound:312–345; девять проверок выбора на очищенном индексе |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | name/type и модификаторы Actor | addItem:259–273 и расчёты; реальные методы |
| [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) | UUID и system.treat | _onTreat:12–17; статическая связь, treat исполнен отдельно |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Item и followUp | _onDropItem:17–21 сохраняет item.uuid; браузер не запускался |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../../templates/sheets/item/criticalWound-sheet.hbs) | Имя/изображение/system | Редактор полей и UUID; статическое чтение |
| [templates/partials/crit-wounds-table.hbs](../../../../../../../templates/partials/crit-wounds-table.hbs) | Локация, лечение, дни, UUID | lookup локации:18; кнопка вызывает treat |
| [module/actor/sheets/mixins/healMixin.js](../../../../../../../module/actor/sheets/mixins/healMixin.js) | system.heal | recoverActor:88 без ожидания; статическая связь, heal исполнен отдельно |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | derivedStats.stun.value | stunSave:433–454 формирует threshold; сам спасбросок в этой порции не исполнялся |

Текстовая [Complex Critical](../../../../../../../packsJson/combat/Complex_Critical_p3EAPCnu8RDawpWR.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Папка: [Complex](_Folder.json.md). Предшественников по followUp в Complex нет. Следующий Item: [Minor Head Wound (Stabilized)](Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json.md), `EnwgL7ApZTdHgMbD`, treatment=stabilized. Реальный treat инициировал создание этого документа, затем удаление текущего. Создание/удаление перехвачены и возвращали pending Promise. Переход загружает другой шаблон с его собственными эффектами; не переписывает изменения прежнего эффекта. На новой подготовке без Item его воздействия не применяются.

Контрольный Actor: восемь unmodifiedMax=5, HP.value=25, броня/вес=0. Результат: INT=4, WILL=4, REF=5, DEX=5, BODY=5, SPD=5; BODY.max=5; RUN=15, LEAP=3, ENC=50, STUN=3, REC=4, HP.max=20, RESOLVE.max=20, FOCUS.max=12; healingTime=7. Все changes дали числовые значения своих целевых полей. Производные рассчитываются из полученных характеристик; базовый max не заменяется totalModifiers.

Все три Minor Head Wound содержат location=torso. В исходном состоянии конкурируют с Ruptured Spleen за complex/torso/lesserEffect=false; порядок индекса меняет выбор. У головы единственный кандидат Lost Teeth. Реальные очищенные модели это не исправляют — [issue-00324](../../../../../../issues/closed/issue-00324.md).

## Проверки и доказательства

[Протокол .059](../../../../review-log.md#task-0003059): все 25 JSON / 2058 строк прочитаны, корневые ID/_key сверены среди 98 criticalWounds, вложенные _key/ID — в своей области. Все 16 followUp проверены до конечного состояния, без циклов и переходов вне Complex. Настоящие модели и методы в изолированном Node 24.16.0 прошли 772 утверждения: 24 Item, Folder, 16 effects/61 changes, числовые поля/производные, 24 treat, семь heal, девять выборов, повторный addItem, исключение эффекта и три подписи правой ноги. Число относится к порции, индивидуальные значения указаны выше.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. 98 JSON и62 followUp проверены; состав установленного packs/ и серверный getIndex не читались. .017 сводит манифест/экспорты/таблицы, включая выбор кандидатов и пустые tailWing. Критерий: источник нужного Item и индексные поля подтверждены отдельно от текста RollTable и предположений по рулбуку. Границы: [U012-02](../../../../cross-check-0002.md#u012-02) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. [issue-00324](../../../../../../issues/closed/issue-00324.md) — состав кандидатов complex/head/torso. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-13 — полная карточка в TASK-0003.059 на указанном коммите; исходник не изменён. [Протокол .059](../../../../review-log.md#task-0003059) содержит общие условия и индивидуальные проверки.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Item `wPRuwd7RdLWnWmnb` («Minor Head Wound»): `complex/none/torso`; 1 ActiveEffect, 3 changes. Предшественник: нет; `followUp` ведёт к `EnwgL7ApZTdHgMbD` («Minor Head Wound (Stabilized)», `stabilized/torso`).

Этот Item участвует в исходных кандидатах индекса по сохранённой степени и локации. При контрольном `BODY.max=5` срок 7 дней независимо от штрафов к `BODY.value`. Сверены адреса: `system.stats.int.totalModifiers`, `system.stats.will.totalModifiers`, `system.derivedStats.stun.totalModifiers`.

Ribs: BODY−2/−1/−1, REF−1/−1/нет, DEX−1 только none. Teeth:10 навыковых адресов−3/−2/−1; 1d10 в HTML не автоматический бросок. Minor Head Wound всех состояний имеет torso: none INT/WILL/STUN−1, stabilized INT/WILL−1, treated WILL−1. Это изменяет состав кандидатов head/torso; все UUID существуют.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js.md), [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs.md), [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json](Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-13](../../../../cross-check-0002.md#r012-13). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.

</details>
