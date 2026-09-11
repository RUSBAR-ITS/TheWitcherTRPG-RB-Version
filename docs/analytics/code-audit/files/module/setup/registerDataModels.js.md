# module/setup/registerDataModels.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/setup/registerDataModels.js](../../../../../../module/setup/registerDataModels.js) |
| Тип файла | JavaScript — регистрация |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../../../tasks/task-0002-system-initialization.md); порция 3 |
| Запись перекрёстной сверки | [Журнал сверок](../../../review-log.md) — TASK-0002, порция 3 |

## Назначение файла

Регистрирует модели данных Actor, Item, ActiveEffect и ChatMessage и класс документа сообщения чата.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) — обработчик init, вызывает функцию после назначения классов документов.

Сам импорт определяет функцию; запись в CONFIG происходит только при её вызове. Требуются CONFIG.*.dataModels и foundry.utils.mergeObject.

## Введённые сущности и действия с ними

| Ключ реестра | Импортированная модель | Файл определения |
| --- | --- | --- |
| Actor.character | `CharacterData` | [module/data/actor/characterData.js](../../../../../../module/data/actor/characterData.js) |
| Actor.monster | `MonsterData` | [module/data/actor/monsterData.js](../../../../../../module/data/actor/monsterData.js) |
| Actor.loot | `LootData` | [module/data/actor/lootData.js](../../../../../../module/data/actor/lootData.js) |
| Actor.mystery | `MysteryActorData` | [module/data/investigation/mysteryActorData.js](../../../../../../module/data/investigation/mysteryActorData.js) |
| Item.base | `CommonItemData` | [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js) |
| Item.alchemical | `AlchemicalData` | [module/data/item/alchemicalData.js](../../../../../../module/data/item/alchemicalData.js) |
| Item.armor | `ArmorData` | [module/data/item/armorData.js](../../../../../../module/data/item/armorData.js) |
| Item.container | `ContainerData` | [module/data/item/containerData.js](../../../../../../module/data/item/containerData.js) |
| Item.component | `ComponentData` | [module/data/item/componentData.js](../../../../../../module/data/item/componentData.js) |
| Item.criticalWound | `CriticalWoundData` | [module/data/item/criticalWoundData.js](../../../../../../module/data/item/criticalWoundData.js) |
| Item.diagrams | `DiagramData` | [module/data/item/diagramData.js](../../../../../../module/data/item/diagramData.js) |
| Item.enhancement | `EnhancementData` | [module/data/item/enhancementData.js](../../../../../../module/data/item/enhancementData.js) |
| Item.mount | `MountData` | [module/data/item/mountData.js](../../../../../../module/data/item/mountData.js) |
| Item.mutagen | `MutagenData` | [module/data/item/mutagenData.js](../../../../../../module/data/item/mutagenData.js) |
| Item.note | `NoteData` | [module/data/item/noteData.js](../../../../../../module/data/item/noteData.js) |
| Item.profession | `ProfessionData` | [module/data/item/professionData.js](../../../../../../module/data/item/professionData.js) |
| Item.homeland | `HomelandData` | [module/data/item/homelandData.js](../../../../../../module/data/item/homelandData.js) |
| Item.race | `RaceData` | [module/data/item/raceData.js](../../../../../../module/data/item/raceData.js) |
| Item.spell | `SpellData` | [module/data/item/spellData.js](../../../../../../module/data/item/spellData.js) |
| Item.hex | `HexData` | [module/data/item/hexData.js](../../../../../../module/data/item/hexData.js) |
| Item.ritual | `RitualData` | [module/data/item/ritualData.js](../../../../../../module/data/item/ritualData.js) |
| Item.valuable | `ValuableData` | [module/data/item/valuableData.js](../../../../../../module/data/item/valuableData.js) |
| Item.weapon | `WeaponData` | [module/data/item/weaponData.js](../../../../../../module/data/item/weaponData.js) |
| Item.clue | `ClueData` | [module/data/investigation/clueData.js](../../../../../../module/data/investigation/clueData.js) |
| Item.obstacle | `ObstacleData` | [module/data/investigation/obstacleData.js](../../../../../../module/data/investigation/obstacleData.js) |
| Item.skill | `SkillItemData` | [module/data/item/skillItemData.js](../../../../../../module/data/item/skillItemData.js) |
| ActiveEffect.base | `WitcherActiveEffectData` | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../module/data/activeEffects/witcherActiveEffectData.js) |
| ActiveEffect.temporaryItemImprovement | `WitcherTemporaryItemImprovementData` | [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) |
| ChatMessage.base | `BaseMessageData` | [module/data/chatMessage/baseMessageData.js](../../../../../../module/data/chatMessage/baseMessageData.js) |
| ChatMessage.attack | `AttackMessageData` | [module/data/chatMessage/attackMessageData.js](../../../../../../module/data/chatMessage/attackMessageData.js) |
| ChatMessage.defense | `DefenseMessageData` | [module/data/chatMessage/defenseMessageData.js](../../../../../../module/data/chatMessage/defenseMessageData.js) |
| ChatMessage.damage | `DamageMessageData` | [module/data/chatMessage/damageMessageData.js](../../../../../../module/data/chatMessage/damageMessageData.js) |

Дополнительно CONFIG.ChatMessage.documentClass = WitcherChatMessage. Всего 4 модели Actor, 22 Item (включая base), 2 ActiveEffect, 4 ChatMessage; 33 импорта с учётом класса документа. Комментарий о template.json не является действующим объявлением типов: сопоставление выполнялось с system.json.

## Основные функции и методы

| Функция | Вход / результат | Действия и условия |
| --- | --- | --- |
| registerDataModels() | Без аргументов; undefined; синхронная | mergeObject дополняет Actor/Item.dataModels; присваивания ActiveEffect/ChatMessage заменяют указанные ключи. Остальные ключи явно не удаляются. |

Конструкторы импортированных моделей здесь не вызываются. Схемы, миграции и prepare-методы выполняет дальнейший жизненный цикл документов.

## Используемые сущности и зависимости

| Сущность | Файл / API | Вид связи | Место / назначение | Доказательство |
| --- | --- | --- | --- | --- |
| `MonsterData` | [module/data/actor/monsterData.js](../../../../../../module/data/actor/monsterData.js) | ES import → регистрация | Actor.dataModels.monster | стр. 6: `export default class MonsterData extends CommonActorData {` |
| `ContainerData` | [module/data/item/containerData.js](../../../../../../module/data/item/containerData.js) | ES import → регистрация | Item.dataModels.container | стр. 5: `export default class ContainerData extends CommonItemData {` |
| `LootData` | [module/data/actor/lootData.js](../../../../../../module/data/actor/lootData.js) | ES import → регистрация | Actor.dataModels.loot | стр. 5: `export default class LootData extends foundry.abstract.TypeDataModel {` |
| `CharacterData` | [module/data/actor/characterData.js](../../../../../../module/data/actor/characterData.js) | ES import → регистрация | Actor.dataModels.character | стр. 9: `export default class CharacterData extends CommonActorData {` |
| `ValuableData` | [module/data/item/valuableData.js](../../../../../../module/data/item/valuableData.js) | ES import → регистрация | Item.dataModels.valuable | стр. 6: `export default class ValuableData extends CommonItemData {` |
| `WeaponData` | [module/data/item/weaponData.js](../../../../../../module/data/item/weaponData.js) | ES import → регистрация | Item.dataModels.weapon | стр. 12: `export default class WeaponData extends CommonItemData {` |
| `EnhancementData` | [module/data/item/enhancementData.js](../../../../../../module/data/item/enhancementData.js) | ES import → регистрация | Item.dataModels.enhancement | стр. 6: `export default class EnhancementData extends CommonItemData {` |
| `MountData` | [module/data/item/mountData.js](../../../../../../module/data/item/mountData.js) | ES import → регистрация | Item.dataModels.mount | стр. 5: `export default class MountData extends CommonItemData {` |
| `AlchemicalData` | [module/data/item/alchemicalData.js](../../../../../../module/data/item/alchemicalData.js) | ES import → регистрация | Item.dataModels.alchemical | стр. 6: `export default class AlchemicalData extends CommonItemData {` |
| `MutagenData` | [module/data/item/mutagenData.js](../../../../../../module/data/item/mutagenData.js) | ES import → регистрация | Item.dataModels.mutagen | стр. 6: `export default class MutagenData extends CommonItemData {` |
| `NoteData` | [module/data/item/noteData.js](../../../../../../module/data/item/noteData.js) | ES import → регистрация | Item.dataModels.note | стр. 5: `export default class NoteData extends CommonItemData {` |
| `CommonItemData` | [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js) | ES import → регистрация | Item.dataModels.base | стр. 3: `export default class CommonItemData extends foundry.abstract.TypeDataModel {` |
| `ComponentData` | [module/data/item/componentData.js](../../../../../../module/data/item/componentData.js) | ES import → регистрация | Item.dataModels.component | стр. 5: `export default class ComponentData extends CommonItemData {` |
| `RaceData` | [module/data/item/raceData.js](../../../../../../module/data/item/raceData.js) | ES import → регистрация | Item.dataModels.race | стр. 8: `export default class RaceData extends CommonItemData {` |
| `ProfessionData` | [module/data/item/professionData.js](../../../../../../module/data/item/professionData.js) | ES import → регистрация | Item.dataModels.profession | стр. 8: `export default class ProfessionData extends CommonItemData {` |
| `SpellData` | [module/data/item/spellData.js](../../../../../../module/data/item/spellData.js) | ES import → регистрация | Item.dataModels.spell | стр. 15: `export default class SpellData extends CommonItemData {` |
| `DiagramData` | [module/data/item/diagramData.js](../../../../../../module/data/item/diagramData.js) | ES import → регистрация | Item.dataModels.diagrams | стр. 6: `export default class DiagramData extends CommonItemData {` |
| `ArmorData` | [module/data/item/armorData.js](../../../../../../module/data/item/armorData.js) | ES import → регистрация | Item.dataModels.armor | стр. 11: `export default class ArmorData extends CommonItemData {` |
| `ClueData` | [module/data/investigation/clueData.js](../../../../../../module/data/investigation/clueData.js) | ES import → регистрация | Item.dataModels.clue | стр. 3: `export default class ClueData extends foundry.abstract.TypeDataModel{` |
| `ObstacleData` | [module/data/investigation/obstacleData.js](../../../../../../module/data/investigation/obstacleData.js) | ES import → регистрация | Item.dataModels.obstacle | стр. 3: `export default class ObstacleData extends foundry.abstract.TypeDataModel{` |
| `MysteryActorData` | [module/data/investigation/mysteryActorData.js](../../../../../../module/data/investigation/mysteryActorData.js) | ES import → регистрация | Actor.dataModels.mystery | стр. 5: `export default class MysteryActorData extends foundry.abstract.TypeDataModel {` |
| `WitcherActiveEffectData` | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../module/data/activeEffects/witcherActiveEffectData.js) | ES import → регистрация | ActiveEffect.dataModels.base | стр. 3: `export default class WitcherActiveEffectData extends foundry.data.ActiveEffectTypeDataModel {` |
| `SkillItemData` | [module/data/item/skillItemData.js](../../../../../../module/data/item/skillItemData.js) | ES import → регистрация | Item.dataModels.skill | стр. 3: `export default class SkillItemData extends foundry.abstract.TypeDataModel {` |
| `HexData` | [module/data/item/hexData.js](../../../../../../module/data/item/hexData.js) | ES import → регистрация | Item.dataModels.hex | стр. 6: `export default class HexData extends CommonItemData {` |
| `RitualData` | [module/data/item/ritualData.js](../../../../../../module/data/item/ritualData.js) | ES import → регистрация | Item.dataModels.ritual | стр. 10: `export default class RitualData extends CommonItemData {` |
| `AttackMessageData` | [module/data/chatMessage/attackMessageData.js](../../../../../../module/data/chatMessage/attackMessageData.js) | ES import → регистрация | ChatMessage.dataModels.attack | стр. 8: `export default class AttackMessageData extends BaseMessageData {` |
| `WitcherChatMessage` | [module/chatMessage/witcherChatMessage.js](../../../../../../module/chatMessage/witcherChatMessage.js) | ES import → регистрация | ChatMessage.documentClass | стр. 1: `export default class WitcherChatMessage extends ChatMessage {` |
| `WitcherTemporaryItemImprovementData` | [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) | ES import → регистрация | ActiveEffect.dataModels.temporaryItemImprovement | стр. 3: `export default class WitcherTemporaryItemImprovementData extends foundry.data.ActiveEffectTypeDataModel {` |
| `HomelandData` | [module/data/item/homelandData.js](../../../../../../module/data/item/homelandData.js) | ES import → регистрация | Item.dataModels.homeland | стр. 3: `export default class HomelandData extends foundry.abstract.TypeDataModel {` |
| `BaseMessageData` | [module/data/chatMessage/baseMessageData.js](../../../../../../module/data/chatMessage/baseMessageData.js) | ES import → регистрация | ChatMessage.dataModels.base | стр. 3: `export default class BaseMessageData extends foundry.abstract.DataModel {` |
| `DefenseMessageData` | [module/data/chatMessage/defenseMessageData.js](../../../../../../module/data/chatMessage/defenseMessageData.js) | ES import → регистрация | ChatMessage.dataModels.defense | стр. 6: `export default class DefenseMessageData extends BaseMessageData {` |
| `DamageMessageData` | [module/data/chatMessage/damageMessageData.js](../../../../../../module/data/chatMessage/damageMessageData.js) | ES import → регистрация | ChatMessage.dataModels.damage | стр. 7: `export default class DamageMessageData extends BaseMessageData {` |
| `CriticalWoundData` | [module/data/item/criticalWoundData.js](../../../../../../module/data/item/criticalWoundData.js) | ES import → регистрация | Item.dataModels.criticalWound | стр. 5: `export default class CriticalWoundData extends foundry.abstract.TypeDataModel {` |

Внешние зависимости: глобальный CONFIG (четыре реестра) и foundry.utils.mergeObject. Проверена форма записей из настоящего тела функции; внутреннее устройство mergeObject в изолированной проверке заменено Object.assign.

## Известные потребители

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) — обработчик init, вызывает функцию после назначения классов документов.

[system.json](../../../../../../system.json) задаёт объявленные типы; [module/setup/registerSheets.js](../../../../../../module/setup/registerSheets.js) регистрирует листы тех же типов. Дальнейший потребитель CONFIG — механизм документов и листов Foundry; прямого создания Actor/Item здесь нет.

## Данные и изменения состояния

Изменяются глобальные реестры и класс ChatMessage только в памяти клиента. Данные миров и компедиумов функция не записывает.

## Проверки и доказательства

Полный файл прочитан. Все 33 импортов сопоставлены с существующими экспортами и точными регистрациями. Исходная функция выполнена в Node vm с заменами импортов и API; полученные регистрации сведены в таблицу выше. Ключи сопоставлены с JSON-манифестом и соседним регистратором. Это проверка вызовов регистрации, не загрузка реальных классов в Foundry.

## Непроверенные участки и открытые вопросы

Схемы и поведение самих моделей/листов за пределами проверки определений не анализировались полностью. Мир не запускался, окна не открывались, сохранённые настройки листов и создание незаявленных типов не проверялись.

## Связанные проблемы

[issue-00005](../../../../../issues/potential/issue-00005.md) — четыре типа зарегистрированы в коде, но отсутствуют в манифесте.

## Дополнительная сверка вложенных моделей

2026-09-10, TASK-0003.001: [Stats](../data/actor/templates/common/stats/statsData.js.md) и [DerivedStats](../data/actor/templates/common/stats/derivedStatsData.js.md) разобраны полностью. Они включены в CommonActorData через EmbeddedDataField (строки 33–34) и наследуются зарегистрированными CharacterData/MonsterData; отдельными типами Actor здесь не регистрируются. Общие фабрики [stat](../data/actor/templates/common/stats/statData.js.md), [valueLabel](../data/actor/templates/valueLabelData.js.md) и [createEnrichedText](../data/dataUtils.js.md) также не являются регистрируемыми типами. Выводы сопоставлены с таблицами выше; полный разбор остальных моделей остаётся последующим подзадачам.

## Дополнительная сверка навыков — TASK-0003.002

2026-09-10, HEAD `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d`; исходник не изменён.

Дополнительно полностью разобраны [Skill](../data/actor/templates/common/skills/skillData.js.md), семь групп и [фабрика skills](../data/actor/templates/common/skills/skillsData.js.md). CommonActorData включает фабрику в SchemaField(:39), CharacterData и MonsterData наследуют эту структуру. Вложенный Skill не регистрируется отдельным типом документа и отличается от Item.skill → SkillItemData в таблице выше. Полный разбор моделей документов остаётся последующим порциям.

Результаты и пределы проверок — в [журнале TASK-0003.002](../../../review-log.md#task-0003002).

## Дополнительная сверка — TASK-0003.003

2026-09-10, HEAD `c34b790379fd98cd7e33ccbeeca085e49297a40f`; исходники не изменены.

Полностью разобраны [Reputation](../data/actor/templates/common/reputationData.js.md), [TemporaryEffects](../data/actor/templates/common/temporaryEffectsData.js.md) и шесть фабрик полей (adrenaline/currency/focus/lifepathData/note/combatEffects). Они входят в CommonActorData; currency также включена в LootData. Ни одна из этих восьми структур не регистрируется здесь отдельным типом документа. Запись массива [note](../data/actor/templates/common/noteData.js.md) отличается от зарегистрированной Item.note.

[Сценарии и результаты TASK-0003.003](../../../review-log.md#task-0003003).

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 3 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.

2026-09-10 — TASK-0003.002: уточнены связи моделей навыков и их потребителей, добавлены взаимные ссылки и фактические ограничения проверки.

2026-09-10 — TASK-0003.003: актуализированы связи с полностью разобранными структурами состояния Actor; ограничения полного клиента сохранены.

## Уточнение TASK-0003.004

2026-09-10, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26`. Проверена вложенность зарегистрированных CharacterData и MonsterData: [generalData](../data/actor/templates/character/generalData.js.md) подключается только CharacterData:16, а [damageTypeModificationData](../data/actor/templates/character/general/damage/damageTypeModificationData.js.md) подключается CommonActorData:49 и наследуется обоими. Настоящие экземпляры подтвердили эти пути; у Monster нет general, у Loot нет damageTypeModification. Регистрация Item.HomelandData создаёт отдельную схему и не переиспользует фабрику родины Actor.

[Перекрёстная сверка TASK-0003.004](../../../review-log.md#task-0003004).

## Уточнение TASK-0003.005

2026-09-10, `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609`. Уточнены вложенные структуры: CharacterData содержит [Log](../data/actor/templates/character/logData.js.md) через EmbeddedDataField и четыре [skillTraining](../data/actor/templates/character/skillTrainingData.js.md); CommonActorData содержит [pannels](../data/actor/templates/character/pannelsData.js.md) и [attackStats](../data/actor/templates/character/attackStatsData.js.md). Настоящие CharacterData/MonsterData подтвердили владельцев: у монстра нет logs, полей IP и обучения, но есть панели/атаки. Связанный общий шаблон разобран в [issue-00030](../../../../../issues/potential/issue-00030.md).

[Сверка TASK-0003.005](../../../review-log.md#task-0003005).

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Сверены три регистрации Actor.character/monster/loot и их реальные схемы: 29/53/3 верхних поля. CommonActorData с 19 общими полями используется наследованием и отдельным типом не регистрируется. Все 37 ранее описанных файлов данных достижимы через импорты этих четырёх моделей. Actor.mystery и связанные части issue-00005 остаются вне этой порции.

Карточки сборки: [commonActorData](../data/actor/commonActorData.js.md), [characterData](../data/actor/characterData.js.md), [monsterData](../data/actor/monsterData.js.md), [lootData](../data/actor/lootData.js.md). [Сверка TASK-0003.006](../../../review-log.md#task-0003006).

## Уточнение TASK-0003.008

2026-09-10, `c5edcbadd05ff4038a174bd2e2a49785e40ea878`; исходник не изменился относительно исходного среза. CommonItemData непосредственно зарегистрирована как base; ещё 16 из 22 типов Item используют её прямых наследников. CriticalWoundData, HomelandData, SkillItemData, ClueData и ObstacleData — отдельные TypeDataModel. canHaveTemporaryItemImprovement и canBeRepaired не задаются реестром: базовые геттеры false переопределяются конкретными моделями.

Связанные карточки: [CommonItemData](../data/item/commonItemData.js.md) и [WitcherItem](../item/witcherItem.js.md). [Перекрёстная сверка](../../../review-log.md#task-0003008). Новая запись уточняет связи; исторические результаты прежних порций сохранены.

## Уточнение TASK-0003.009

2026-09-10, `a33bf33add228ae93f96a52046c8feb4ee992921`. Исходник не изменился относительно указанного ранее среза.

Сверены две отдельные модели: [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../module/data/activeEffects/witcherActiveEffectData.js) (changes ядра + пять BooleanField) и [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) (changes + три BooleanField, metadata.type). Temporary-модель прямо наследует ActiveEffectTypeDataModel, не WitcherActiveEffectData. changes в 14.367 имеет key/type/value/phase/priority; начальные type=add, phase=initial, value='', priority=undefined до клиентской подготовки. Настоящие модели выполнены изолированно; источник схемы проверен в common/data/active-effect.mjs.

[Журнал сверки](../../../review-log.md) — TASK-0003.009; ограничения изолированного выполнения и неподтверждённые проблемы сохранены.

## Уточнение TASK-0003.012

2026-09-10, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9`; исходник не изменён. Десять файлов [TASK-0003.012](../../../../../tasks/task-0003.012.md) не добавляют новых document types. [DamageProperties](../../../../../../module/data/item/templates/combat/damagePropertiesData.js), [DefenseProperties](../../../../../../module/data/item/templates/combat/defensePropertiesData.js), [ResistanceData](../../../../../../module/data/item/templates/armor/resistanceData.js) и [SpData](../../../../../../module/data/item/templates/armor/spData.js) — вложенные DataModel; остальные фабрики создают поля. AttackMessageData/DefenseMessageData используют экземпляры DamageProperties, а DamageMessageData включает defineSchema с заменой effects на ArrayField/applied. Регистрация ChatMessage type не означает одинаковую runtime-структуру properties.

Результат и границы — [сверка TASK-0003.012](../../../review-log.md#task-0003012).

## Уточнение TASK-0003.013

2026-09-10, `8cca18e14b75ec53028ee6bc49a837597de4d9af`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003013).

Полный разбор [module/data/item/weaponData.js](../../../../../../module/data/item/weaponData.js) подтвердил 36 верхних полей схемы с CommonItemData, attackOptions, defenseOptions, вложенными DamageProperties/DefenseProperties и associatedDiagramUuid. Изолированные вызовы выполнялись на настоящих зарегистрированных моделях. Региональные схемы Spell прочитаны точечно для путей полей и миграции, их статус полного разбора не повышен. Подготовка Weapon с enhancementItemIds без Actor дала исключение ([issue-00077](../../../../../issues/potential/issue-00077.md)).

## Уточнение TASK-0003.014

2026-09-10, `0fa589bd300856ff309f362afcb66d6fa43401ab`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003014).

Полные [module/data/item/armorData.js](../../../../../../module/data/item/armorData.js) и [module/data/item/enhancementData.js](../../../../../../module/data/item/enhancementData.js) содержат 27 и 16 верхних полей соответственно; общая [module/data/item/templates/itemEffectData.js](../../../../../../module/data/item/templates/itemEffectData.js) содержит четыре. У Armor два определения location, фактически остаётся StringField; Shield не отдельный тип Item. Настоящие зарегистрированные модели использованы для проверки всех миграций и подготовленных значений, документы мира не создавались.

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003015).

Полностью описаны и реально созданы [module/data/item/alchemicalData.js](../../../../../../module/data/item/alchemicalData.js), [module/data/item/mutagenData.js](../../../../../../module/data/item/mutagenData.js), [module/data/item/valuableData.js](../../../../../../module/data/item/valuableData.js). Три регистрации Item ведут к моделям с 15 верхними полями каждая; consumable() добавляет isConsumable и EmbeddedDataField(ConsumablePropertiesData). Исходные четыре поля вложенной модели не содержат addsTempHp, а записи массивов не содержат id. Сама регистрация не подключает редактор этих полей.

## Уточнение TASK-0003.016

2026-09-10, `53f74994011383cb544cabac96285430f00cb38a`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003016).

Полностью описаны регистрации ComponentData→component и DiagramData→diagrams: [module/data/item/componentData.js](../../../../../../module/data/item/componentData.js), [module/data/item/diagramData.js](../../../../../../module/data/item/diagramData.js). В реальных моделях 14/20 верхних полей. [module/data/item/templates/craftingComponentData.js](../../../../../../module/data/item/templates/craftingComponentData.js) даёт строке id/name/quantity/uuid с генерируемым ID, а [module/data/item/templates/associatedDiagramData.js](../../../../../../module/data/item/templates/associatedDiagramData.js) включается в Weapon/Armor независимо. Модели связанного Item и строки требования рецепта не смешиваются.

## Уточнение TASK-0003.018

2026-09-10, `rusbar-main`, `29319a7a7e1dfc0663edbc15166f3b6a19682a2f`. Импорты RaceData и HomelandData разрешаются в [module/data/item/raceData.js](../../../../../../module/data/item/raceData.js) и [module/data/item/homelandData.js](../../../../../../module/data/item/homelandData.js); обе модели зарегистрированы для соответствующих Item-типов. Настоящие модели Foundry 14 в памяти дали 13 и 2 верхнеуровневых поля. RaceData наследует CommonItemData и переопределяет description как HTMLField; HomelandData напрямую наследует TypeDataModel, не получает общую схему предмета.

[Перекрёстная сверка](../../../review-log.md#task-0003018). Исходники не изменены; это уточнение проверенных связей, а не повторный полный разбор файла.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. [ProfessionData](../../../../../../module/data/item/professionData.js) импортирован строкой 15 и включён в Item.profession. Настоящая модель дала 14 верхнеуровневых полей, основной навык и 3 пути по 3 навыка. SkillUsage/TemporaryHealth/Threshold являются вложенными DataModel, отдельных documentTypes для них нет.

[Перекрёстная сверка](../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Уточнение TASK-0003.020

2026-09-11, `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008`; проверены связи с критическими травмами, лечением и отдыхом. Полный первоначальный разбор и его ограничения сохранены.

| Связь | Файл | Результат проверки |
| --- | --- | --- |
| CriticalWoundData | [module/data/item/criticalWoundData.js](../../../../../../module/data/item/criticalWoundData.js) | Прямой import 33 и CONFIG.Item.dataModels.criticalWound 52 подтверждены. 9 полей; вычисления сроков в модели, эффекты в отдельном механизме. |

[Сверка порции и итоговая сверка 96 файлов второй серии](../../../review-log.md#task-0003020); браузер, мир и записи в БД не запускались.

## Уточнение TASK-0003.021

Проверено 2026-09-11 на `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; исходник не менялся.

Импорты 16/24/25 и dataModels61–63 связывают spell/hex/ritual с полностью разобранными моделями. Общая фабрика templates/componentData.js — внутренняя схема строки RitualData; её не следует путать с зарегистрированным Item ComponentData.

Сверенные карточки: [module/data/item/spellData.js](../data/item/spellData.js.md), [module/data/item/hexData.js](../data/item/hexData.js.md), [module/data/item/ritualData.js](../data/item/ritualData.js.md).

[Результаты и пределы сверки](../../../review-log.md#task-0003021).

## Уточнение TASK-0003.023

2026-09-11, `538dbac9bb9432c123fe4f3c00ab788b58517afb`; исходник не изменился. Полностью разобраны MysteryActorData (два верхних поля), ClueData (десять полей) и ObstacleData (шесть полей). Все три напрямую наследуют TypeDataModel и не получают CommonActorData/CommonItemData через эту регистрацию. Реальный registerDataModels исполнен с настоящими тремя моделями, подменёнными прочими импортами и регистрационным окружением; ключи mystery/clue/obstacle указывают ожидаемые классы. Декларации system.json по-прежнему расходятся с этими ключами.

Связанные карточки: [module/data/investigation/mysteryActorData.js](../data/investigation/mysteryActorData.js.md), [module/data/investigation/clueData.js](../data/investigation/clueData.js.md), [module/data/investigation/obstacleData.js](../data/investigation/obstacleData.js.md), [module/data/investigation/templates/complexityData.js](../data/investigation/templates/complexityData.js.md).

[Перекрёстная сверка порции](../../../review-log.md#task-0003023). БД, мир, исходники и права доступа не менялись.

## Уточнение TASK-0003.024

2026-09-11, `66cd03705dbc398eba0026284a298b5fbe337035`; исходник не изменился. Для container подтверждён ContainerData extends CommonItemData, 11 полей схемы (8 общих и carry/storedWeight/content). itemContent — prepared-массив вне схемы, storedWeight имеет поле схемы и пересчитывается при подготовке. Тип container объявлен в манифесте. Реестр назначает класс; расчёт происходит позже в system.prepareDerivedData через жизненный цикл документа.

Связанные карточки: [module/data/item/containerData.js](../data/item/containerData.js.md).

[Перекрёстная сверка порции](../../../review-log.md#task-0003024). Мир, БД, код и метаданные доступа не менялись.

## Уточнение TASK-0003.028

2026-09-11, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`: Регистрация ChatMessage:76–80 связывает base/attack/defense/damage с соответствующими моделями. Новый разбор fumble.js проверил точное сравнение constructor с AttackMessageData/DefenseMessageData; остальные классы при options.fumble=true могут дать видимый пункт без действия ([issue-00183](../../../../../issues/potential/issue-00183.md)). ChatMessageData из module/chatMessage/chatMessageData.js — отдельный обычный контейнер параметров, в этом реестре не регистрируется.

Полные карточки зависимости: [module/scripts/rolls/fumble.js](../scripts/rolls/fumble.js.md), [module/chatMessage/chatMessageData.js](../chatMessage/chatMessageData.js.md). [Перекрёстная сверка](../../../review-log.md#task-0003028). Это уточнение связи; исходный файл не изменён.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Импорт SkillItemData и регистрация CONFIG.Item.dataModels.skill теперь сопоставлены с полной карточкой: 8 полей, без CommonItemData/modifiers/modifiedValue/isVisible. Встроенный Skill Actor и Item type skill — разные модели и пути данных.

Сверенные связи: [module/data/item/skillItemData.js](../../../../../../module/data/item/skillItemData.js); [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js). Полные карточки новых файлов — в [указателе порции](../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.033

2026-09-11, `12055fee62f01c6de49967044aedef9d7cfe0632`. NoteData полностью описан: default-import:11 и CONFIG.Item.dataModels.note:57 сопоставлены с классом и manifest Item.note. Общие поля сохраняются; массив Actor-notes остаётся самостоятельным. Повторного исполнения регистрационного API в .033 не было.

Связи: [module/data/item/noteData.js](../data/item/noteData.js.md). [Результаты и пределы проверки](../../../review-log.md#task-0003033).
