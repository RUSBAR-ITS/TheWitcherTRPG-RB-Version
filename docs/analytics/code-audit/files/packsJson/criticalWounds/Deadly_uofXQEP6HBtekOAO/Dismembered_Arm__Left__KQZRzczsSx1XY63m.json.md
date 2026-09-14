# packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left__KQZRzczsSx1XY63m.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left__KQZRzczsSx1XY63m.json](../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left__KQZRzczsSx1XY63m.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-14 |
| Ветка и коммит | rusbar-main, 1cae095ac2f0f009fb1358a888a7afcf5ea5ec2e |
| Изменения относительно коммита | Нет; 94 строк; SHA-256 824a36cc700ac65dc21954d9ae58cd22cbd69c53508d325d513da41bca518280 |
| Задача и порция | [TASK-0003.061](../../../../../../tasks/task-0003.061.md) |
| Запись перекрёстной сверки | [Протокол .061](../../../../review-log.md#task-0003061) |

## Назначение файла

Экспорт Dismembered Arm (Left): состояние none, локация leftArm. Содержит 1 ActiveEffect и 1 изменений. Данные задают шаблон травмы и её переход; действия выполняют потребители системы и Foundry.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

[ready:62–67](../../../../../../../module/TheWitcherTRPG.js) запрашивает четыре поля индекса: system.criticalLevel/location/lesserEffect/treatment; выбор пакета задаёт [criticalWoundsPack](../../../../../../../module/setup/settings.js). Item участвует в исходных кандидатах applyCritWound. Проверен индекс-фасад из настоящих очищенных моделей, не действующий серверный индекс.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Dismembered Arm (Left) | Корневой Item; name:3, _id:5 | ID `KQZRzczsSx1XY63m`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Item.KQZRzczsSx1XY63m` | Загрузка, копирование к Actor, подготовка, лечение/удаление |
| _key / folder / sort | Корневые поля | `"!items!KQZRzczsSx1XY63m"` / `"uofXQEP6HBtekOAO"` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| img / ownership | Корневые поля | `"icons/svg/item-bag.svg"` / `{"default":0,"ugXtPMJIktbl63QV":3}` | Ресурс ядра вне пофайлового анализа; наличие указанного пользователя в мире не подтверждено |
| system / effects | Объекты, строки 7 / 21 | criticalWound / 1 embedded ActiveEffect | Схема и воздействия перечислены далее |

| Поле system | Экспортное значение | Смысл и потребитель |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация; defineSchema её не содержит, очистка модели удаляет поле. |
| description | `"<p>The blow rends your arm from your body or damages it beyond repair. </p>"` | HTMLField; enrichedText/createEnrichedText, редактор и сообщение applyCritWound. Текст не преобразуется в changes. |
| criticalLevel | `"deadly"` | StringField; выбор deadly и исключение автоматического treat из heal; ветви deadly в calculateHealingTime нет. |
| treatment | `"none"` | StringField; выбор none и проверка treated в heal. |
| location | `"leftArm"` | StringField; фильтр applyCritWound и lookup подписи списка. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах first find: false для >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик заживления, редактирование и update в heal. |
| healingTime | `0` | NumberField; для deadly ветви расчёта нет, экспортный 0 сохраняется у Actor. |
| sterilized | `false` | BooleanField; новая стерилизация даёт ещё +2 дня к очередному дню. |
| followUp | `"Compendium.TheWitcherTRPG.criticalWounds.Item.vmRDG8kxeCu3sYQC"` | DocumentUUIDField типа Item; treat загружает адресата или удаляет конечный Item. |

### ActiveEffect 1: Dismembered Arm (Left)

ID `iyJh4F9lnKEynZzt`; _key=`"!items.effects!KQZRzczsSx1XY63m.iyJh4F9lnKEynZzt"`. Origin=`"Item.KQZRzczsSx1XY63m"` — ссылка на мировой Item; существование адресата не проверялось. Цель переноса при transfer=true — Actor-владелец текущего Item; origin не выбирает другого владельца.

Тип `"base"`, name:24; disabled=false, transfer=true, active=true; img=`"icons/svg/item-bag.svg"`, description=`""`, tint=`"#ffffff"`, sort=0, statuses=`["bleed"]`. Flags=`{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`; _stats=`{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. System до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`.

Duration до миграции: `{"rounds":1,"startTime":null,"combat":null,"seconds":null,"turns":null,"startRound":null,"startTurn":null}`. Подготовлено: start=null, value=1, units=rounds, expiry=turnStart, expired=false. rounds=1 сохраняется; без start/контекста боя это не доказывает прекращения через раунд. Core _preCreate задаёт start непосредственно Actor-owned эффектам; updateDuration и полный lifecycle вложенного эффекта не исполнялись. applyAfterCalculations получает false, changes переходят в system.changes/initial. Statuscounter — внешний модуль; в фасаде без регистрации его flags очищаются, работа установленного модуля не проверена.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Источник поля / фактическое значение |
| --- | --- | --- | --- | --- |
| 1 / 46 | `system.combatEffects.turnStartEffects.bleed` | 2 / `"{\"damage\": {\"amount\": 2, \"ignoreArmor\": \"true\"}, \"img\": \"icons/svg/blood.svg\", \"name\": \"WITCHER.statusEffects.bleed\"}"` / `null` | add; `{"damage":{"amount":2,"ignoreArmor":"true"},"img":"icons/svg/blood.svg","name":"WITCHER.statusEffects.bleed"}`; priority=20; phase=initial | SchemaField; [combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js); undefined |

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

Папка: [Deadly](_Folder.json.md). Предшественников по followUp в Deadly нет. Следующий Item: [Dismembered Arm (Left - Stabilized)](Dismembered_Arm__Left___Stabilized__vmRDG8kxeCu3sYQC.json.md), `vmRDG8kxeCu3sYQC`, treatment=stabilized. Реальный treat инициировал создание этого документа, затем удаление текущего. Создание/удаление перехвачены и возвращали pending Promise. Переход загружает другой шаблон с его собственными эффектами; не переписывает изменения прежнего эффекта. На новой подготовке без Item его воздействия не применяются.

Контрольный Actor: восемь unmodifiedMax=5, HP.value=25, dodge.value=athletics.value=8 до эффектов, броня/вес=0. Результат: INT=5, WILL=5, REF=5, DEX=5, BODY=5, SPD=5; BODY.max=5, SPD.max=5; RUN=15, LEAP.value=3, LEAP.max=3, ENC=50, STUN=5, REC=5, HP.max=25, HP.value=25, RESOLVE.max=25, FOCUS.max=15, STA.max=25, STA.value=0; healingTime=0. Навыки: dodge.value=8, dodge.activeEffectModifiers=0; athletics.value=8, athletics.activeEffectModifiers=0; awareness.value=0, awareness.activeEffectModifiers=0. Статусы=`["bleed"]`; turnStartEffects={}. После initial, до расчётов: `{"staMax":0,"spdMax":5,"bodyMax":5}`. Значения прочитаны непосредственно из подготовленных полей; DataModel.toObject возвращает источник и не заменяет такую проверку.

JSON-строка объекта успешно мигрирует; ADD применяется к SchemaField и не создаёт запись. Реальный applyCombatEffects не вызвал урон от этого Item — [issue-00328](../../../../../../issues/potential/issue-00328.md). Диагностические копии исходной левой руки и Spetic Shock с override вместо ADD создавали bleed/poison и передавали amount=2/3 в перехваченный Actor.applyDamage. ignoreArmor очищался в boolean true, spDamage — 0. Следующий этап не сохранил type — прежняя [issue-00021](../../../../../../issues/potential/issue-00021.md); исходные записи ADD до этого пути не доходят. Экспорт не менялся.

None содержит только эффект bleed; stabilized/treated не содержат effects. Неиспользование руки и протезирование описаны HTML, изменений экипировки или действий руки в этих JSON нет. У правого none bleed.name и мировой origin скопированы с левой руки; перенос всё равно относится к владельцу правого Item. Этот эффект не формирует числовой модификатор навыка.

В Deadly calculateHealingTime не имеет отдельной ветви и оставляет экспортный healingTime=0. heal прибавляет дни treated, но условие criticalLevel != deadly запрещает автоматический treat независимо от числа дней. Ручной treat всё равно доступен, включая удаление конечного Item. None/stabilized инициируют update({}); записи не ожидаются.

## Проверки и доказательства

[Протокол .061](../../../../review-log.md#task-0003061): все 23 JSON / 2131 строка прочитаны; 22 Item, Folder, 21 эффект (20 активных), 43 changes и 14 followUp проверены индивидуально. Основной сценарий — 758 утверждений: строгие модели, поля/производные, все treat, восемь heal, восемь вариантов выбора, повтор addItem, подписи Awareness и контроли включённости/переноса. Периодический сценарий — 40 утверждений: семь ADD объектов и отдельный числовой modifier, два override-контроля, положительная проверка модификатора существующей bleed. Всего по Deadly 798. Итоговый повтор всего пакета — ещё 3182 утверждения на 94 Item/4 Folder/79 effects/360 changes/62 переходах и 48 выборах; повтор шести пакетов RollTable — 5223. Всего в .061: 9203 утверждения. Числа относятся к общим сценариям, значения данного документа указаны выше.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. HTML ограничения рук, зрения, спасбросков и протезов не исполняется автоматически. Наблюдаемые штрафы, повтор травмы, Deadly и лечебные бонусы не сверены с рулбуками; новая автоматизация и изменения условий требуют самостоятельного согласования. .017/.018 сохраняют технический охват. Границы: [U012-07](../../../../cross-check-0002.md#u012-07) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. [issue-00328](../../../../../../issues/potential/issue-00328.md) — ADD объекта периодического урона; [issue-00021](../../../../../../issues/potential/issue-00021.md) — потеря типа в отдельном положительном контроле. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-14 — полная карточка в TASK-0003.061 на указанном коммите; исходник не изменён. [Протокол .061](../../../../review-log.md#task-0003061) содержит общие условия и индивидуальные проверки.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Item `KQZRzczsSx1XY63m` («Dismembered Arm (Left)»): `deadly/none/leftArm`; 1 ActiveEffect, 1 changes. Предшественник: нет; `followUp` ведёт к `vmRDG8kxeCu3sYQC` («Dismembered Arm (Left - Stabilized)», `stabilized/leftArm`).

Этот Item участвует в исходных кандидатах индекса по сохранённой степени и локации. Расчёт срока оставляет экспортный `healingTime=0`; `heal` не завершает Deadly автоматически. Сверены адреса: `system.combatEffects.turnStartEffects.bleed`.

Eye DEX−4/−2/−1, Awareness−5/−3/−1; change не содержит условия «зрение» из HTML. Руки содержат только bleed в none; остальные состояния без effects, ограничения/протезы текстовые. Три ADD bleed-объекта не создают записи. Нет автоматического завершения Deadly по дням; ручной переход доступен. Общая связь periodic-записи с обработчиком разобрана в R012-24; status сам по себе не вызывает урон.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js.md), [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs.md), [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left___Stabilized__vmRDG8kxeCu3sYQC.json](Dismembered_Arm__Left___Stabilized__vmRDG8kxeCu3sYQC.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-20](../../../../cross-check-0002.md#r012-20), [R012-24](../../../../cross-check-0002.md#r012-24). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
