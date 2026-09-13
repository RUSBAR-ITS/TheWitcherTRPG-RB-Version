# packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json](../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-13 |
| Ветка и коммит | rusbar-main, d26e3381a7290807b8e76f9817d0f7a603c0e61a |
| Изменения относительно коммита | Нет; 104 строк; SHA-256 981c304c7b86e04efed19a913033920b4f2228fdfd483cef98d29569cd3a72f2 |
| Задача и порция | [TASK-0003.059](../../../../../../tasks/task-0003.059.md) |
| Запись перекрёстной сверки | [Протокол .059](../../../../review-log.md#task-0003059) |

## Назначение файла

Экспорт Fractured Leg (Right - Stabilized): состояние stabilized, локация rightLeg. Содержит 1 ActiveEffect и 3 изменений. Данные задают шаблон травмы и её переход; действия выполняют потребители системы и Foundry.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

[ready:62–67](../../../../../../../module/TheWitcherTRPG.js) запрашивает четыре поля индекса: system.criticalLevel/location/lesserEffect/treatment; выбор пакета задаёт [criticalWoundsPack](../../../../../../../module/setup/settings.js). Item исключается из исходного выбора по treatment и используется через followUp или ручное добавление. Проверен индекс-фасад из настоящих очищенных моделей, не действующий серверный индекс.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Fractured Leg (Right - Stabilized) | Корневой Item; name:3, _id:97 | ID `WNjcD3F3Hs5IdAaa`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Item.WNjcD3F3Hs5IdAaa` | Загрузка, копирование к Actor, подготовка, лечение/удаление |
| _key / folder / sort | Корневые поля | `"!items!WNjcD3F3Hs5IdAaa"` / `"YcLLKtwU75uE8tdC"` / `2300000` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| img / ownership | Корневые поля | `"icons/svg/item-bag.svg"` / `{"default":0,"ugXtPMJIktbl63QV":3}` | Ресурс ядра вне пофайлового анализа; наличие указанного пользователя в мире не подтверждено |
| system / effects | Объекты, строки 6 / 20 | criticalWound / 1 embedded ActiveEffect | Схема и воздействия перечислены далее |

| Поле system | Экспортное значение | Смысл и потребитель |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация; defineSchema её не содержит, очистка модели удаляет поле. |
| description | `""` | HTMLField; enrichedText/createEnrichedText, редактор и сообщение applyCritWound. Текст не преобразуется в changes. |
| criticalLevel | `"complex"` | StringField; выбор кандидатов и ветвь complex расчёта healingTime. |
| treatment | `"stabilized"` | StringField; выбор none и проверка treated в heal. |
| location | `"rightLeg"` | StringField; фильтр applyCritWound и lookup подписи списка. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах first find: false для >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик заживления, редактирование и update в heal. |
| healingTime | `0` | NumberField; у владельца Actor prepareDerivedData рассчитывает max(12−BODY.max,1). |
| sterilized | `false` | BooleanField; новая стерилизация даёт ещё +2 дня к очередному дню. |
| followUp | `"Compendium.TheWitcherTRPG.criticalWounds.Item.Aa8wCz1OGM4gflmc"` | DocumentUUIDField типа Item; treat загружает адресата или удаляет конечный Item. |

### ActiveEffect 1: Fractured Leg (Left)

ID `hF9ez6RQNIpixxd9`; экспортный _key=`"!items.effects!WNjcD3F3Hs5IdAaa.hF9ez6RQNIpixxd9"`. Origin=`"Item.r34NuXwHfPGZCpTu"` — ссылка на мировой Item; разрешение такого UUID в действующем мире не проверялось. Она не становится ссылкой на компедиум при совпадении последнего ID и не задаёт цель применения. Цель при transfer=true — Actor-владелец этого Item.

Тип `"base"`, name:23; disabled=false, transfer=true; img=`"icons/svg/item-bag.svg"`, description=`""`, tint=`"#ffffff"`, sort=0, statuses=`[]`. Flags=`{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`; _stats=`{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. System до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`.

Duration до миграции: `{"startTime":null,"combat":null,"seconds":null,"rounds":null,"turns":null,"startRound":null,"startTurn":null}`. Ядро преобразует её в start=null, duration={value:null,units:"seconds",expiry:null,expired:false}; после prepareBaseData value=Infinity. Тикающего срока в данных нет, updateDuration/registry в сценарии не запускались. applyAfterCalculations получает false; все changes мигрируют в system.changes и фазу initial. Флаги statuscounter принадлежат внешнему модулю; без его регистрации ядро очищает их в изолированном окружении, что не доказывает потерю флагов в мире.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Источник поля |
| --- | --- | --- | --- | --- |
| 1 / 45 | `system.stats.spd.totalModifiers` | 2 / `"-2"` / `null` | add; -2; priority=20; phase=initial | NumberField; [statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js) |
| 2 / 51 | `system.skills.ref.dodge.activeEffectModifiers` | 2 / `"-2"` / `null` | add; -2; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js) |
| 3 / 57 | `system.skills.dex.athletics.activeEffectModifiers` | 2 / `"-2"` / `null` | add; -2; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js) |

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
| [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | skills.*.activeEffectModifiers, effect.name | addActiveEffects:1–23; фрагменты dodge правой ноги реально получены |

Текстовая [Complex Critical](../../../../../../../packsJson/combat/Complex_Critical_p3EAPCnu8RDawpWR.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Папка: [Complex](_Folder.json.md). Предшественник: [Fractured Leg (Right)](Fractured_Leg__Right__yI6kHQM8voHrBF2h.json.md). Следующий Item: [Fractured Leg (Right - Treated)](Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json.md), `Aa8wCz1OGM4gflmc`, treatment=treated. Реальный treat инициировал создание этого документа, затем удаление текущего. Создание/удаление перехвачены и возвращали pending Promise. Переход загружает другой шаблон с его собственными эффектами; не переписывает изменения прежнего эффекта. На новой подготовке без Item его воздействия не применяются.

Контрольный Actor: восемь unmodifiedMax=5, HP.value=25, броня/вес=0. Результат: INT=5, WILL=5, REF=5, DEX=5, BODY=5, SPD=3; BODY.max=5; RUN=9, LEAP=1, ENC=50, STUN=5, REC=5, HP.max=25, RESOLVE.max=25, FOCUS.max=15; healingTime=7. Все changes дали числовые значения своих целевых полей. Производные рассчитываются из полученных характеристик; базовый max не заменяется totalModifiers.

Отображаемое имя эффекта — Fractured Leg (Left), хотя Item имеет location=rightLeg. Реальный addActiveEffects('dodge') при displayRollsDetails=true вернул `" +-2[Fractured Leg (Left)]"`. Это неверная подпись источника штрафа, [issue-00326](../../../../../../issues/potential/issue-00326.md).

## Проверки и доказательства

[Протокол .059](../../../../review-log.md#task-0003059): все 25 JSON / 2058 строк прочитаны, корневые ID/_key сверены среди 98 criticalWounds, вложенные _key/ID — в своей области. Все 16 followUp проверены до конечного состояния, без циклов и переходов вне Complex. Настоящие модели и методы в изолированном Node 24.16.0 прошли 772 утверждения: 24 Item, Folder, 16 effects/61 changes, числовые поля/производные, 24 treat, семь heal, девять выборов, повторный addItem, исключение эффекта и три подписи правой ноги. Число относится к порции, индивидуальные значения указаны выше.

## Непроверенные участки и открытые вопросы

Сценарий использует реальные BaseItem/BaseActor и системные модели, настоящий WitcherActiveEffect с фасадом ClientDocumentMixin/registry. Подготовка и фазы вызваны явно; полный клиентский lifecycle, updateDuration, _preCreate/_preUpdate, calculateAttackStats, браузер и сеть не запускались. fromUuid и индекс представлены Map/массивом настоящих документов; записи и чат перехватывались, броня и вес заданы нулём. Для подписи формулы список appliedEffects задан из реальных активных эффектов; полный бросок/чат не воспроизводился. Внешние модули, действующие packs/ и игровые правила не проверены. Прохождение локальных сценариев не доказывает сохранение в мире или HTTP-доступ службы.

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. [issue-00326](../../../../../../issues/potential/issue-00326.md) — подпись эффекта правой ноги. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-13 — полная карточка в TASK-0003.059 на указанном коммите; исходник не изменён. [Протокол .059](../../../../review-log.md#task-0003059) содержит общие условия и индивидуальные проверки.
