# packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json](../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json) |
| Тип файла | JSON: Item типа criticalWound |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.060](../../../../../../tasks/task-0003.060.md) |
| Запись перекрёстной сверки | [Протокол .060](../../../../review-log.md#task-0003060) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Внутренние UUID направлены на TheWitcherTRPG-RB-Version. ID документов, диапазоны, эффекты и _stats сохранены. Датированные результаты и прежние значения UUID ниже являются историей.

## Назначение файла

Экспорт Torn Stomach: состояние none, локация torso. Вложенных ActiveEffect: 1; изменений: 53. Данные задают шаблон травмы и её переход; действия выполняют потребители системы и Foundry.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

[ready:62–67](../../../../../../../module/TheWitcherTRPG.js) запрашивает четыре поля индекса: system.criticalLevel/location/lesserEffect/treatment; выбор пакета задаёт [criticalWoundsPack](../../../../../../../module/setup/settings.js). Item участвует в исходных кандидатах applyCritWound. Проверен индекс-фасад из настоящих очищенных моделей, не действующий серверный индекс.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Torn Stomach | Корневой Item; name:3, _id:5 | ID `5gnx9xNF52ap9PYi`; UUID `Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.5gnx9xNF52ap9PYi` | Загрузка, копирование к Actor, подготовка, лечение/удаление |
| _key / folder / sort | Корневые поля | `"!items!5gnx9xNF52ap9PYi"` / `"ox3lLmV3zp0K67Ht"` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| img / ownership | Корневые поля | `"icons/svg/item-bag.svg"` / `{"default":0,"ugXtPMJIktbl63QV":3}` | Ресурс ядра вне пофайлового анализа; наличие указанного пользователя в мире не подтверждено |
| system / effects | Объекты, строки 7 / 21 | criticalWound / 1 embedded ActiveEffect | Схема и воздействия перечислены далее |

| Поле system | Экспортное значение | Смысл и потребитель |
| --- | --- | --- |
| htmlFields | `["description"]` | Устаревшая декларация; defineSchema её не содержит, очистка модели удаляет поле. |
| description | `""` | HTMLField; enrichedText/createEnrichedText, редактор и сообщение applyCritWound. Текст не преобразуется в changes. |
| criticalLevel | `"difficult"` | StringField; выбор кандидатов и ветвь difficult расчёта healingTime. |
| treatment | `"none"` | StringField; выбор none и проверка treated в heal. |
| location | `"torso"` | StringField; фильтр applyCritWound и lookup подписи списка. |
| lesserEffect | `false` | BooleanField; при нескольких кандидатах first find: false для >4, true для ≤4. |
| daysHealed | `0` | NumberField; счётчик заживления, редактирование и update в heal. |
| healingTime | `0` | NumberField; у владельца Actor prepareDerivedData рассчитывает max(15−BODY.max,1). |
| sterilized | `false` | BooleanField; новая стерилизация даёт ещё +2 дня к очередному дню. |
| followUp | `"Compendium.TheWitcherTRPG-RB-Version.criticalWounds.Item.EpF0FD1nFXJTJ5Tj"` | DocumentUUIDField типа Item; treat загружает адресата или удаляет конечный Item. |

### ActiveEffect 1: Torn Stomach

ID `uxvX0GUDLr0DqbQV`; _key=`"!items.effects!5gnx9xNF52ap9PYi.uxvX0GUDLr0DqbQV"`. Origin=`"Item.5gnx9xNF52ap9PYi"` — ссылка на мировой Item; существование адресата не проверялось. Цель переноса при transfer=true — Actor-владелец текущего Item; origin не выбирает другого владельца.

Тип `"base"`, name:24; disabled=false, transfer=true; img=`"icons/svg/item-bag.svg"`, description=`""`, tint=`"#ffffff"`, sort=0, statuses=`[]`. Flags=`{"statuscounter":{"value":1,"config":{"type":"default"},"visible":false}}`; _stats=`{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}`. System до миграции: `{"applySelf":false,"applyOnTarget":false,"applyOnHit":false,"applyOnDamage":false}`.

Duration до миграции: `{"startTime":null,"combat":null,"seconds":null,"rounds":null,"turns":null,"startRound":null,"startTurn":null}`. Подготовлено: start=null, value=Infinity, units=seconds, expiry=null, expired=false. Пустая длительность становится неограниченной при prepareBaseData; таймер этой записи не задан. applyAfterCalculations получает false, changes переходят в system.changes/initial. Statuscounter — внешний модуль; в фасаде без регистрации его flags очищаются, работа установленного модуля не проверена.

| № / строка key | Ключ изменения | Исходные mode / value / priority | После миграции и подготовки | Источник поля / фактическое значение |
| --- | --- | --- | --- | --- |
| 1 / 46 | `system.skills.int.awareness.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 2 / 52 | `system.skills.int.business.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 3 / 58 | `system.skills.int.deduction.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 4 / 64 | `system.skills.int.education.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 5 / 70 | `system.skills.int.commonspeech.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | commonspeech отсутствует в схеме; [intData.js](../../../../../../../module/data/actor/templates/common/skills/intData.js) объявляет commonsp; динамический путь=-2 |
| 6 / 76 | `system.skills.int.eldersp.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 7 / 82 | `system.skills.int.dwarven.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 8 / 88 | `system.skills.int.monster.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 9 / 94 | `system.skills.int.socialetq.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 10 / 100 | `system.skills.int.streetwise.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 11 / 106 | `system.skills.int.tactics.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 12 / 112 | `system.skills.int.teaching.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 13 / 118 | `system.skills.int.wilderness.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 14 / 124 | `system.skills.ref.brawling.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 15 / 130 | `system.skills.ref.dodge.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 16 / 136 | `system.skills.ref.melee.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 17 / 142 | `system.skills.ref.riding.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 18 / 148 | `system.skills.ref.sailing.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 19 / 154 | `system.skills.ref.smallblades.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 20 / 160 | `system.skills.ref.staffspear.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 21 / 166 | `system.skills.ref.swordsmanship.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 22 / 172 | `system.skills.will.courage.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 23 / 178 | `system.skills.will.hexweave.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 24 / 184 | `system.skills.will.intimidation.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 25 / 190 | `system.skills.will.spellcast.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 26 / 196 | `system.skills.will.resistmagic.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 27 / 202 | `system.skills.will.resistcoerc.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 28 / 208 | `system.skills.will.ritcraft.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 29 / 214 | `system.skills.dex.archery.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 30 / 220 | `system.skills.dex.athletics.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 31 / 226 | `system.skills.dex.crossbow.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 32 / 232 | `system.skills.dex.sleight.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 33 / 238 | `system.skills.dex.stealth.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 34 / 244 | `system.skills.cra.alchemy.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 35 / 250 | `system.skills.cra.crafting.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 36 / 256 | `system.skills.cra.disguise.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 37 / 262 | `system.skills.cra.firstaid.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 38 / 268 | `system.skills.cra.forgery.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 39 / 274 | `system.skills.cra.picklock.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 40 / 280 | `system.skills.cra.trapcraft.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 41 / 286 | `system.skills.body.physique.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 42 / 292 | `system.skills.body.endurance.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 43 / 298 | `system.skills.emp.charisma.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 44 / 304 | `system.skills.emp.deceit.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 45 / 310 | `system.skills.emp.finearts.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 46 / 316 | `system.skills.emp.gambling.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 47 / 322 | `system.skills.emp.grooming.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 48 / 328 | `system.skills.emp.perception.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 49 / 334 | `system.skills.emp.leadership.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 50 / 340 | `system.skills.emp.persuasion.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 51 / 346 | `system.skills.emp.performance.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 52 / 352 | `system.skills.emp.seduction.activeEffectModifiers` | 2 / `"-2"` / `null` | add; `-2`; priority=20; phase=initial | NumberField; [skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); -2 |
| 53 / 358 | `system.combatEffects.turnStartEffects.acid` | 2 / `"{\"damage\": {\"amount\": 4, \"ignoreArmor\": \"true\", \"spDamage\": \"0\", \"type\": \"acid\"}, \"img\": \"icons/svg/acid.svg\", \"name\": \"Torn Stomach\"}"` / `null` | add; `{"damage":{"amount":4,"ignoreArmor":"true","spDamage":"0","type":"acid"},"img":"icons/svg/acid.svg","name":"Torn Stomach"}`; priority=20; phase=initial | SchemaField; [combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js); запись отсутствует (undefined) |

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

Папка: [Difficult](_Folder.json.md). Предшественников по followUp в Difficult нет. Следующий Item: [Torn Stomach (Stabilized)](Torn_Stomach__Stabilized__EpF0FD1nFXJTJ5Tj.json.md), `EpF0FD1nFXJTJ5Tj`, treatment=stabilized. Реальный treat инициировал создание этого документа, затем удаление текущего. Создание/удаление перехвачены и возвращали pending Promise. Переход загружает другой шаблон с его собственными эффектами; не переписывает изменения прежнего эффекта. На новой подготовке без Item его воздействия не применяются.

Контрольный Actor: восемь unmodifiedMax=5, HP.value=25, dodge.value=athletics.value=8 до эффектов, броня/вес=0. Результат: INT=5, WILL=5, REF=5, DEX=5, BODY=5, SPD=5; BODY.max=5, SPD.max=5; RUN=15, LEAP.value=3, LEAP.max=3, ENC=50, STUN=5, REC=5, HP.max=25, RESOLVE.max=25, FOCUS.max=15; healingTime=10. Навыки: dodge.value=8, dodge.activeEffectModifiers=-2; athletics.value=8, athletics.activeEffectModifiers=-2. Статусы=`[]`; turnStartEffects={}. Значения прочитаны непосредственно из подготовленных полей; сериализация DataModel/toObject возвращает источник и не заменяет такую проверку.

JSON-строка объекта успешно мигрирует; ADD применяется к SchemaField и не создаёт запись. Реальный applyCombatEffects не вызвал урон от этого Item — [issue-00328](../../../../../../issues/potential/issue-00328.md). В отдельных диагностических копиях bleed/suffocation/acid override создавал структуру, очищал ignoreArmor в boolean true и передавал amount=2/3/4 до перехваченного Actor.applyDamage. Экспорт не менялся. В acid-контроле следующий этап терял type — [issue-00021](../../../../../../issues/potential/issue-00021.md); это отдельный достигнутый путь, исходный ADD его не достигает.

52 адреса навыков включают ошибочный commonspeech. 51 объявленное поле получает штраф; динамическое commonspeech.activeEffectModifiers=-2, но настоящее commonsp.activeEffectModifiers=0 — [issue-00004](../../../../../../issues/potential/issue-00004.md). В none есть дополнительная 53-я запись acid; в stabilized/treated её нет. Штрафы навыков меняются −2 → −2 → −1; это данные, без оценки правил.

## Проверки и доказательства

[Протокол .060](../../../../review-log.md#task-0003060): все 25 JSON / 3351 строк прочитаны, корневые ID/_key сверены среди 98 criticalWounds, вложенные _key/ID — в своей области. Все 16 followUp проверены до конечного состояния, без циклов и переходов вне Difficult. Настоящие модели и методы в изолированном Node 24.16.0 прошли 1748 утверждений: 24 Item, Folder, 25 effects/201 changes, подготовленные поля/производные, 24 treat, семь heal, восемь выборов, повторный addItem, исключение эффекта и подпись правой treated ноги. Отдельный сценарий: 43 утверждения, девять исходных периодических записей и три диагностические копии с override вместо ADD. Всего 1791 утверждение. Числа относятся к порции, индивидуальные значения указаны выше.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. ADD SchemaField, NumberField modifier, statuses и очередь начала хода различены. Исходные16 ADD объектов не достигают урона; override-копии только диагностические. Остаются одноимённые источники при удалении, start/expiry/updateDuration/registry, Combat/GM и конечные HP. .017/.018 сохраняют эти границы без исправления экспорта. Границы: [U012-05](../../../../cross-check-0002.md#u012-05) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. [issue-00328](../../../../../../issues/potential/issue-00328.md) — ADD объекта периодического урона; [issue-00021](../../../../../../issues/potential/issue-00021.md) — потеря типа в отдельном положительном контроле. [issue-00004](../../../../../../issues/potential/issue-00004.md) — commonspeech/commonsp. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-13 — полная карточка в TASK-0003.060 на указанном коммите; исходник не изменён. [Протокол .060](../../../../review-log.md#task-0003060) содержит общие условия и индивидуальные проверки.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Item `5gnx9xNF52ap9PYi` («Torn Stomach»): `difficult/none/torso`; 1 ActiveEffect, 53 changes. Предшественник: нет; `followUp` ведёт к `EpF0FD1nFXJTJ5Tj` («Torn Stomach (Stabilized)», `stabilized/torso`).

Этот Item участвует в исходных кандидатах индекса по сохранённой степени и локации. При контрольном `BODY.max=5` срок 10 дней независимо от штрафов к `BODY.value`. Сверены адреса: `skill.activeEffectModifiers`, `system.combatEffects.turnStartEffects.acid`.

В каждом состоянии 52 адреса:51 объявленный навык получает−2/−2/−1, commonspeech отсутствует (настоящее поле commonsp). none дополнительно ADD объекта acid amount4/type acid/ignoreArmor строка true/spDamage строка 0. Миграция объекта не равна созданию записи; ADD блокируется 00328, а диагностический override достигал другой ошибки передачи type (смежная 00021). Общая связь periodic-записи с обработчиком разобрана в R012-24; status сам по себе не вызывает урон.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js.md), [module/actor/witcherActor.js](../../../module/actor/witcherActor.js.md), [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js.md), [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs.md), [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Stabilized__EpF0FD1nFXJTJ5Tj.json](Torn_Stomach__Stabilized__EpF0FD1nFXJTJ5Tj.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-19](../../../../cross-check-0002.md#r012-19), [R012-24](../../../../cross-check-0002.md#r012-24). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
