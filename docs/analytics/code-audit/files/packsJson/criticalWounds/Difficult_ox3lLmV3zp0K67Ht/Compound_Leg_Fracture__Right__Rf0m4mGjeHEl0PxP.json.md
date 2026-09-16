# packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json](../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.060](../../../../../../tasks/task-0003.060.md) |
| Запись перекрёстной сверки | [Протокол .060](../../../../review-log.md#task-0003060) |

Актуализация [issue-00001](../../../../../../issues/open/issue-00001.md), 2026-09-16: Внутренние UUID направлены на TheWitcherTRPG-RB-Version. ID документов, диапазоны, эффекты и _stats сохранены. Датированные результаты и прежние значения UUID ниже являются историей.

## Назначение файла

Экспорт Compound Leg Fracture (Right): состояние none, локация rightLeg. Вложенных ActiveEffect: 2; изменений: 4. Данные задают шаблон травмы и её переход; действия выполняют потребители системы и Foundry.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

[ready:62–67](../../../../../../../module/TheWitcherTRPG.js) запрашивает четыре поля индекса: system.criticalLevel/location/lesserEffect/treatment; выбор пакета задаёт [criticalWoundsPack](../../../../../../../module/setup/settings.js). Item участвует в исходных кандидатах applyCritWound. Проверен индекс-фасад из настоящих очищенных моделей, не действующий серверный индекс.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Compound Leg Fracture (Right) | Корневой Item; name:3, _id:153 | ID `Rf0m4mGjeHEl0PxP`; UUID `Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.Rf0m4mGjeHEl0PxP` | Загрузка, копирование к Actor, подготовка, лечение/удаление |
| _key / folder / sort | Корневые поля | `"!items!Rf0m4mGjeHEl0PxP"` / `"ox3lLmV3zp0K67Ht"` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| img / ownership | Корневые поля | `"icons/svg/item-bag.svg"` / `{"default":0,"ugXtPMJIktbl63QV":3}` | Ресурс ядра вне пофайлового анализа; наличие указанного пользователя в мире не подтверждено |
| system / effects | Объекты, строки 6 / 20 | criticalWound / 2 embedded ActiveEffect | Схема и воздействия перечислены далее |

| Поле system | Экспортное значение | Смысл и потребитель |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация; defineSchema её не содержит, очистка модели удаляет поле. |
| description | `"<p>Quarter SPD, Dodge/Escape, and Athletics</p>"` | HTMLField; enrichedText/createEnrichedText, редактор и сообщение applyCritWound. Текст не преобразуется в changes. |
| criticalLevel | `"difficult"` | StringField; выбор кандидатов и ветвь difficult расчёта healingTime. |
| treatment | `"none"` | StringField; выбор none и проверка treated в heal. |
| location | `"rightLeg"` | StringField; фильтр applyCritWound и lookup подписи списка. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах first find: false для >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик заживления, редактирование и update в heal. |
| healingTime | `0` | NumberField; у владельца Actor prepareDerivedData рассчитывает max(15−BODY.max,1). |
| sterilized | `false` | BooleanField; новая стерилизация даёт ещё +2 дня к очередному дню. |
| followUp | `"Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.QCugb1JqpiFyBEN4"` | DocumentUUIDField типа Item; treat загружает адресата или удаляет конечный Item. |

### ActiveEffect 1: Compound Leg Fracture (Left)

ID `j4w4dskXupoQQTmq`; _key=`"!items.effects!Rf0m4mGjeHEl0PxP.j4w4dskXupoQQTmq"`. Origin=`"Item.flpxY7FVPGevwfcg"` — ссылка на мировой Item; существование адресата не проверялось. Цель переноса при transfer=true — Actor-владелец текущего Item; origin не выбирает другого владельца.

Тип `"base"`, name:23; disabled=false, transfer=true; img=`"icons/svg/item-bag.svg"`, description=`""`, tint=`"#ffffff"`, sort=0, statuses=`["bleed"]`. Flags=`{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`; _stats=`{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. System до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`.

Duration до миграции: `{"rounds":1,"startTime":null,"combat":null,"seconds":null,"turns":null,"startRound":null,"startTurn":null}`. Подготовлено: start=null, value=1, units=rounds, expiry=turnStart, expired=false. rounds=1 сохраняется; без start/контекста боя это не доказывает прекращения через раунд. Core _preCreate задаёт start непосредственно Actor-owned эффектам; updateDuration и полный lifecycle вложенного эффекта не исполнялись. applyAfterCalculations получает false, changes переходят в system.changes/initial. Statuscounter — внешний модуль; в фасаде без регистрации его flags очищаются, работа установленного модуля не проверена.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Источник поля / фактическое значение |
| --- | --- | --- | --- | --- |
| 1 / 45 | `system.combatEffects.turnStartEffects.bleed` | 2 / `"{\"damage\": {\"amount\": 2, \"ignoreArmor\": \"true\"}, \"img\": \"icons/svg/blood.svg\", \"name\": \"WITCHER.statusEffects.bleed\"}"` / `null` | add; `{"damage":{"amount":2,"ignoreArmor":"true"},"img":"icons/svg/blood.svg","name":"WITCHER.statusEffects.bleed"}`; priority=20; phase=initial | SchemaField; [combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js); запись отсутствует (undefined) |

Повторение ID эффекта у разных Item не коллизия внутри одной коллекции effects. Вложенный _key указывает собственного владельца независимо от origin/name.

### ActiveEffect 2: Compound Leg Fracture (Right)

ID `8XtVtB8xyDhcBZGv`; _key=`"!items.effects!Rf0m4mGjeHEl0PxP.8XtVtB8xyDhcBZGv"`. Origin=`"Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.Rf0m4mGjeHEl0PxP"` — UUID текущего Item в компедиуме, сопоставлен с экспортом. Цель переноса при transfer=true — Actor-владелец текущего Item; origin не выбирает другого владельца.

Тип `"base"`, name:79; disabled=false, transfer=true; img=`"icons/svg/item-bag.svg"`, description=`""`, tint=`"#ffffff"`, sort=0, statuses=`[]`. Flags=`{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`; _stats=`{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. System до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`.

Duration до миграции: `{"startTime":null,"combat":null,"seconds":null,"rounds":null,"turns":null,"startRound":null,"startTurn":null}`. Подготовлено: start=null, value=Infinity, units=seconds, expiry=null, expired=false. Пустая длительность становится неограниченной при prepareBaseData; таймер этой записи не задан. applyAfterCalculations получает false, changes переходят в system.changes/initial. Statuscounter — внешний модуль; в фасаде без регистрации его flags очищаются, работа установленного модуля не проверена.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Источник поля / фактическое значение |
| --- | --- | --- | --- | --- |
| 1 / 101 | `system.stats.spd.max` | 1 / `"0.25"` / `null` | multiply; `0.25`; priority=10; phase=initial | NumberField; [statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js); 1 |
| 2 / 107 | `system.skills.ref.dodge.value` | 1 / `"0.25"` / `null` | multiply; `0.25`; priority=10; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); 2 |
| 3 / 113 | `system.skills.dex.athletics.value` | 1 / `"0.25"` / `null` | multiply; `0.25`; priority=10; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); 2 |

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
| statusEffect.hbs; localize name | [Шаблон сообщения](../../../../../../../templates/chat/combat/statusEffect.hbs); [en](../../../../../../../lang/en.json) / [ru](../../../../../../../lang/ru.json) | Представление / локализация | Строка 2 выводит img/name; bleed/suffocation — существующие ключи WITCHER.statusEffects, Torn Stomach — обычная строка; amount шаблон не выводит |

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
| [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) → [module/scripts/combat/applyDamage.js](../../../../../../../module/scripts/combat/applyDamage.js) → [module/scripts/damageInstance.js](../../../../../../../module/scripts/damageInstance.js) | combatEffects.turnStartEffects.* | applyCombatEffects:41–45 читает Object.values; statuses не заменяет запись урона; реальный handler на исходных данных получил пустой набор |

Текстовая [Difficult Critical](../../../../../../../packsJson/combat/Difficult_Critical_VIup1SZTMKCSGGbT.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Папка: [Difficult](_Folder.json.md). Предшественников по followUp в Difficult нет. Следующий Item: [Compound Leg Fracture (Right - Stabilized)](Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json.md), `QCugb1JqpiFyBEN4`, treatment=stabilized. Реальный treat инициировал создание этого документа, затем удаление текущего. Создание/удаление перехвачены и возвращали pending Promise. Переход загружает другой шаблон с его собственными эффектами; не переписывает изменения прежнего эффекта. На новой подготовке без Item его воздействия не применяются.

Контрольный Actor: восемь unmodifiedMax=5, HP.value=25, dodge.value=athletics.value=8 до эффектов, броня/вес=0. Результат: INT=5, WILL=5, REF=5, DEX=5, BODY=5, SPD=5; BODY.max=5, SPD.max=1; RUN=15, LEAP.value=3, LEAP.max=0, ENC=50, STUN=5, REC=5, HP.max=25, RESOLVE.max=25, FOCUS.max=15; healingTime=10. Навыки: dodge.value=2, dodge.activeEffectModifiers=0; athletics.value=2, athletics.activeEffectModifiers=0. Статусы=`["bleed"]`; turnStartEffects={}. Значения прочитаны непосредственно из подготовленных полей; сериализация DataModel/toObject возвращает источник и не заменяет такую проверку.

JSON-строка объекта успешно мигрирует; ADD применяется к SchemaField и не создаёт запись. Реальный applyCombatEffects не вызвал урон от этого Item — [issue-00328](../../../../../../issues/potential/issue-00328.md). В отдельных диагностических копиях bleed/suffocation/acid override создавал структуру, очищал ignoreArmor в boolean true и передавал amount=2/3/4 до перехваченного Actor.applyDamage. Экспорт не менялся. В acid-контроле следующий этап терял type — [issue-00021](../../../../../../issues/potential/issue-00021.md); это отдельный достигнутый путь, исходный ADD его не достигает.

Множитель изменяет SPD.max и два skill.value. calculateStat читает unmodifiedMax+totalModifiers, поэтому SPD.value остаётся 5. NumberField max целочисленный: 5×0.25 → 1, 5×0.5 → 3. RUN/LEAP.value читают value, LEAP.max зависит от изменённого max — [issue-00036](../../../../../../issues/potential/issue-00036.md).

В цепочках правых переломов у stabilized перепутаны rightArm/rightLeg, при переходе к treated возвращается исходная локация — [issue-00327](../../../../../../issues/potential/issue-00327.md). Модель/treat не исправляют это поле.

У bleed-эффекта имя Compound Leg Fracture (Left), у второго эффекта множителей — правильное Right. Первый не адресует dodge.activeEffectModifiers; ошибочная подпись формулы здесь не воспроизводилась — [issue-00326](../../../../../../issues/potential/issue-00326.md).

## Проверки и доказательства

[Протокол .060](../../../../review-log.md#task-0003060): все 25 JSON / 3351 строк прочитаны, корневые ID/_key сверены среди 98 criticalWounds, вложенные _key/ID — в своей области. Все 16 followUp проверены до конечного состояния, без циклов и переходов вне Difficult. Настоящие модели и методы в изолированном Node 24.16.0 прошли 1748 утверждений: 24 Item, Folder, 25 effects/201 changes, подготовленные поля/производные, 24 treat, семь heal, восемь выборов, повторный addItem, исключение эффекта и подпись правой treated ноги. Отдельный сценарий: 43 утверждения, девять исходных периодических записей и три диагностические копии с override вместо ADD. Всего 1791 утверждение. Числа относятся к порции, индивидуальные значения указаны выше.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. min1 срока отличается от отсутствия общего clamp характеристики; max/value/totalModifiers и priority сопоставлены. Остаются пользовательские изменения полей/приоритетов/фаз, другие сочетания эффектов и конкурентное heal до сохранения sterilized. Критерий: учитывать конкретный путь/фазу и prepared-поле, не сериализованный _source; новый порядок/потолок не вводится. Границы: [U012-04](../../../../cross-check-0002.md#u012-04) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. [issue-00328](../../../../../../issues/potential/issue-00328.md) — ADD объекта периодического урона; [issue-00021](../../../../../../issues/potential/issue-00021.md) — потеря типа в отдельном положительном контроле. [issue-00036](../../../../../../issues/potential/issue-00036.md) — max/value характеристики. [issue-00327](../../../../../../issues/potential/issue-00327.md) — локации стабилизированных правых переломов. [issue-00326](../../../../../../issues/potential/issue-00326.md) — имя левой ноги у правого Item. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-13 — полная карточка в TASK-0003.060 на указанном коммите; исходник не изменён. [Протокол .060](../../../../review-log.md#task-0003060) содержит общие условия и индивидуальные проверки.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Item `Rf0m4mGjeHEl0PxP` («Compound Leg Fracture (Right)»): `difficult/none/rightLeg`; 2 ActiveEffect, 4 changes. Предшественник: нет; `followUp` ведёт к `QCugb1JqpiFyBEN4` («Compound Leg Fracture (Right - Stabilized)», `stabilized/rightArm`).

Этот Item участвует в исходных кандидатах индекса по сохранённой степени и локации. При контрольном `BODY.max=5` срок 10 дней независимо от штрафов к `BODY.value`. Сверены адреса: `system.combatEffects.turnStartEffects.bleed`, `system.stats.spd.max`, `skill.value`.

Множители адресуют SPD.max и dodge/athletics.value; treated использует totalModifiers/activeEffectModifiers. При базе 5 и навыках 8 none даёт SPD.max1/value5 и навыки 2, stabilized max3/value5 и навыки 4. Правая stabilized имеет rightArm (00327), treated-эффект назван Left (00326). Round1 у bleed не подтверждает автоматическое снятие. Общая связь periodic-записи с обработчиком разобрана в R012-24; status сам по себе не вызывает урон.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js.md), [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs.md), [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json](Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-17](../../../../cross-check-0002.md#r012-17), [R012-24](../../../../cross-check-0002.md#r012-24). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
