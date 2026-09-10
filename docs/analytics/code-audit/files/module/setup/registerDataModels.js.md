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

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 3 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.
