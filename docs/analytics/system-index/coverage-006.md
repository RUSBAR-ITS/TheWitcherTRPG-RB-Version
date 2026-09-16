# Покрытие TASK-0006.006 — подключение документов и интерфейсов

2026-09-15; rusbar-main, исходный HEAD `983e6fda1d00beb87d22dba5c41aac518d2b3310`. [Задача](../../tasks/task-0006.006.md), [манифест](manifest.json), [протокол](review-log.md#task-0006006).

Добавлены 236 сущностей, 624 отношения и 9 процессов. Накопленный набор: **615 источников, 636 сущностей, 1601 отношение, 23 процесса, 145 шагов и 200 переходов**. Все прежние ID сохранены. У registerDataModels и init дополнены описание/refs в существующей части; отдельные копии этих сущностей не созданы.

В накопленном индексе 27 основных и 81 смежный файл имеют частичные определения; 507 файлов пока только в каталоге определений. В .006 семь основных исходников, из них три уже входили в пилот. 72 файла впервые получили минимальные определения, преимущественно импортированных моделей и листов. Это адреса объявлений и непосредственных границ, а не полный разбор 72 файлов.

## Основные области

| Исходник / ID | Включено | Остаток |
| --- | --- | --- |
| [system.json](../../../system.json), src-000481 | id/compatibility, esmodules, styles, languages, packFolders, 25 явно объявленных типов, семь пакетов | Остальные поля; содержимое ресурсов. Ссылки шести исключённых языков остаются только в декларации |
| [TheWitcherTRPG.js](../../../module/TheWitcherTRPG.js), src-000004 | Верхний уровень, init/ready, game.api, подписки чата/Polyglot/hotbar и прямые вызовы | Тела createMacro, LanguageProvider и подсистем за целями вызовов |
| [registerDataModels.js](../../../module/setup/registerDataModels.js), src-000214 | 32 назначения моделей (4 Actor, 22 Item, 2 AE, 4 ChatMessage) и ChatMessage.documentClass; классы/импорты | Конструирование документов, схемы и миграции импортированных классов |
| [registerSheets.js](../../../module/setup/registerSheets.js), src-000215 | 21 Item, 4 Actor, 1 AE; отдельный unregister core AE; классы/базы/PARTS/template | Фактический выбор/рендер/сохранение листов, настройки выбора ядра |
| [hooks.js](../../../module/setup/hooks.js), src-000212 | registerHooks, updateCombat callback, combatHooks; оба вызова без await | Бой, регенерация, эффекты начала хода и регионы внутри смежных обработчиков |
| [settings.js](../../../module/setup/settings.js), src-000216 | Все девять настроек, тип/scope/default/choices; getAllCompendia; чтения ready и пяти мест пилота | Прочие читатели, динамические ключи, запись settings и её последствия |
| [config.js](../../../module/setup/config.js), src-000209 | Прежние stat/skill maps, контейнеры эффектов; подключение WITCHER к CONFIG | Остальные боевые карты и содержимое statusEffects/armorEffects |

## Адреса назначений моделей

Назначение CONFIG и объявление documentTypes — разные записи. Регистрация класса не вызывает его конструктор и не добавляет тип в game.model. В явном манифесте отсутствуют Actor.mystery и Item.clue/obstacle/skill; Item.base — вспомогательная регистрация. Допустимость базовых AE/ChatMessage описана в поздних уточнениях [R002-02](../code-audit/cross-check-0002.md#r002-02) и [issue-00005](../../issues/potential/issue-00005.md).

| Ключ назначения | Узел поля | Целевой класс / ID | Строка регистратора |
| --- | --- | --- | --- |
| CONFIG.Actor.dataModels.character | ent-000459 | CharacterData / ent-000164 | 38 |
| CONFIG.Actor.dataModels.monster | ent-000460 | MonsterData / ent-000166 | 39 |
| CONFIG.Actor.dataModels.loot | ent-000461 | LootData / ent-000168 | 40 |
| CONFIG.Actor.dataModels.mystery | ent-000462 | MysteryActorData / ent-000169 | 42 |
| CONFIG.Item.dataModels.base | ent-000463 | CommonItemData / ent-000403 | 47 |
| CONFIG.Item.dataModels.alchemical | ent-000464 | AlchemicalData / ent-000408 | 48 |
| CONFIG.Item.dataModels.armor | ent-000465 | ArmorData / ent-000416 | 49 |
| CONFIG.Item.dataModels.container | ent-000466 | ContainerData / ent-000402 | 50 |
| CONFIG.Item.dataModels.component | ent-000467 | ComponentData / ent-000411 | 51 |
| CONFIG.Item.dataModels.criticalWound | ent-000468 | CriticalWoundData / ent-000428 | 52 |
| CONFIG.Item.dataModels.diagrams | ent-000469 | DiagramData / ent-000415 | 53 |
| CONFIG.Item.dataModels.enhancement | ent-000470 | EnhancementData / ent-000406 | 54 |
| CONFIG.Item.dataModels.mount | ent-000471 | MountData / ent-000407 | 55 |
| CONFIG.Item.dataModels.mutagen | ent-000472 | MutagenData / ent-000409 | 56 |
| CONFIG.Item.dataModels.note | ent-000473 | NoteData / ent-000410 | 57 |
| CONFIG.Item.dataModels.profession | ent-000474 | ProfessionData / ent-000413 | 58 |
| CONFIG.Item.dataModels.homeland | ent-000475 | HomelandData / ent-000425 | 59 |
| CONFIG.Item.dataModels.race | ent-000476 | RaceData / ent-000412 | 60 |
| CONFIG.Item.dataModels.spell | ent-000477 | SpellData / ent-000414 | 61 |
| CONFIG.Item.dataModels.hex | ent-000478 | HexData / ent-000419 | 62 |
| CONFIG.Item.dataModels.ritual | ent-000479 | RitualData / ent-000420 | 63 |
| CONFIG.Item.dataModels.valuable | ent-000480 | ValuableData / ent-000404 | 64 |
| CONFIG.Item.dataModels.weapon | ent-000481 | WeaponData / ent-000405 | 65 |
| CONFIG.Item.dataModels.clue | ent-000482 | ClueData / ent-000417 | 67 |
| CONFIG.Item.dataModels.obstacle | ent-000483 | ObstacleData / ent-000418 | 68 |
| CONFIG.Item.dataModels.skill | ent-000484 | SkillItemData / ent-000182 | 70 |
| CONFIG.ActiveEffect.dataModels.base | ent-000485 | WitcherActiveEffectData / ent-000170 | 73 |
| CONFIG.ActiveEffect.dataModels.temporaryItemImprovement | ent-000486 | WitcherTemporaryItemImprovementData / ent-000177 | 74 |
| CONFIG.ChatMessage.documentClass | ent-000487 | WitcherChatMessage / ent-000423 | 76 |
| CONFIG.ChatMessage.dataModels.base | ent-000488 | BaseMessageData / ent-000422 | 77 |
| CONFIG.ChatMessage.dataModels.attack | ent-000489 | AttackMessageData / ent-000421 | 78 |
| CONFIG.ChatMessage.dataModels.defense | ent-000490 | DefenseMessageData / ent-000426 | 79 |
| CONFIG.ChatMessage.dataModels.damage | ent-000491 | DamageMessageData / ent-000427 | 80 |

## Листы и шаблоны

26 регистраций задают namespace=witcher и makeDefault=true. Types у общего Item-листа и ActiveEffect не заданы; остальные фильтры сохранены в payload отношений. Эти параметры передаются ядру; сохранённый пользовательский выбор может влиять на фактический default. `WitcherProfessionSheet` из default import разрешается в класс `WitcheProfessionSheet` (ent-000448), имя исходника не исправлялось.

В PARTS/get template внесены 49 адресов template/return (41 системный, 8 ядра; 43 уникальных), сопоставленных с R002-03. Дополнительно учтён `PARTS.changes.templates` со ссылкой на core change.hbs: всего 50 ссылок, 44 уникальных адреса. Это декларативные refers, не вызовы renders. Исходники шаблонов остаются в каталоге, без нового анализа HBS.

`WitcherItemSheet.PARTS` — ent-000524, пустой объект на строке 30. Общая регистрация без types сама по себе не подключает note-sheet.hbs. [Issue-00057](../../issues/potential/issue-00057.md) содержит более позднюю сверку заметок; её статус сохранён.

## Настройки и чтения

| Настройка | ID | Начало объявления | Тип / default |
| --- | --- | --- | --- |
| criticalWoundsPack | ent-000570 | 2 | StringField; initial/default TheWitcherTRPG.criticalWounds, blank=false, nullable=false, choices=getAllCompendia |
| useOptionalAdrenaline | ent-000572 | 17 | Boolean; false |
| useOptionalVerbalCombat | ent-000573 | 25 | Boolean; false |
| silverTrait | ent-000574 | 37 | Boolean; false |
| displayRollsDetails | ent-000575 | 46 | Boolean; false |
| useWitcherFont | ent-000576 | 54 | Boolean; false |
| displayRep | ent-000577 | 61 | Boolean; false |
| clickableImageItemTypes | ent-000578 | 69 | String; valuable |
| clickableImageCheckboxForGMOnly | ent-000579 | 77 | Boolean; true |

Все настройки имеют scope=world и config=true. Полные буквальные параметры, включая name/hint, сохранены в узлах setting и отношениях registers. `choices: getAllCompendia` представлен как passes: системный registerSettings передаёт функцию, а момент её вызова выбирает поле ядра. Она допускает любые Item-пакеты и строит collection → title; содержимое травм не проверяет.

У criticalWoundsPack включено чтение ready:64. У displayRollsDetails — пять мест: modifierMixin.addActiveEffects:3, skillMixin.rollSkillCheck:55, addSocialStanding:86, rollCustomSkillCheck:144 и helper.addPart:78. Внешние по отношению к этой порции читатели не подразумеваются отсутствующими. Для setting используется neighbors с relation=reads; команда field предназначена для полей/getter.

## Процессы

Все девять новых процессов partial. Порядок выражен переходами с условиями. Sync после вызова async означает отсутствие await у вызывающего; он не подтверждает завершение действий функции. Регистрация callback не является выполнением его тела.

| Процесс | Вход и граница |
| --- | --- |
| <a id="proc-000015"></a>proc-000015 — Выполнение entry и отложенные подписки | Верхний уровень entry после импортов. Серверный барьер id/каталога описан R002-01. Регистрация callbacks не выполняет init/ready. Синхронные исключения смежных функций не развёрнуты. |
| <a id="proc-000016"></a>proc-000016 — init: документы, API и регистраторы | Локальная последовательность init, без создания документов/окон. preload запускается без await; внутренности helpers/query/ядра вне порции. При синхронном исключении последовательность прервётся. |
| <a id="proc-000017"></a>proc-000017 — registerDataModels: четыре реестра | Все 32 назначения dataModels и ChatMessage.documentClass. Отсутствующие mystery/clue/obstacle/skill в manifest не добавляются регистратором; Item.base вспомогательный, base AE/Chat допускаются ядром. Внутренности mergeObject и создание документов вне порции. |
| <a id="proc-000018"></a>proc-000018 — registerSheets: реестры Item, Actor и ActiveEffect | 21+4+1 регистрации и отдельный unregister core ActiveEffect. Очередь/выбор листа Foundry, PARTS render и сохранение документов — внешняя граница. types листа не объявляют новые типы документа. |
| <a id="proc-000019"></a>proc-000019 — registerSettings: объявления девяти настроек | Девять последовательных game.settings.register; регистрация и чтение/изменение world setting разделены. Вызов choices полем ядра имеет отдельный вход; он не является следующим шагом этого процесса. |
| <a id="proc-000020"></a>proc-000020 — choices: список Item-компедиумов | Локальная filter/reduce getAllCompendia; перечень зависит от game.packs. В содержимое/доступность выбранной травмы функция не заглядывает. |
| <a id="proc-000021"></a>proc-000021 — ready: индекс компедиума и зависимое продолжение | Локальный ready: lookup → await getIndex → hotbarDrop → шрифт → сокет → пустые deprecations. Pending ждёт без повторного вызова getIndex. Пустой fulfilled индекс допускает продолжение; будущий applyCritWound — отдельная граница R002-05/issue-00289. Внутренности компедиума, DOM, socket/macro и поздняя смена setting не раскрыты. |
| <a id="proc-000022"></a>proc-000022 — updateCombat: передача двум обработчикам | hooks.js не фильтрует update/options/userId. Оба смежных обработчика async, их Promise не ожидаются. Active GM guards/текущий combatant проверяются внутри; итог записей HP/регионов и порядок их завершения не утверждаются. |
| <a id="proc-000023"></a>proc-000023 — hotbarDrop: условный запуск макроса | Только callback строк 70–75; createMacro и исполнение команды макроса — смежная граница. Callback не возвращает/не ждёт Promise createMacro. |

Для ready разделены три состояния: отсутствующий pack, отклонённый getIndex и успешно полученный пустой индекс. Первые два не достигают hotbar/font/socket; пустой fulfilled индекс допускает продолжение, а отказ позднего applyCritWound относится к другой границе ([issue-00289](../../issues/potential/issue-00289.md)). Петля index означает ожидание одного Promise и не является повтором запроса.

Серверная проверка имени каталога/id остаётся предусловием entry ([R002-01](../code-audit/cross-check-0002.md#r002-01), [issue-00001](../../issues/closed/issue-00001.md)). Её историческое воспроизведение не выдано за новое выполнение сервера. Guard регистратора сокета может вернуть без подписки; пустая deprecationWarnings не создаёт предупреждений.

## Смежные файлы этой порции

В таблице перечислены файлы с новыми локальными определениями .006 сверх семи основных. Уже имевшийся пилотный охват сохраняется отдельно в sources.jsonl. Здесь добавлены только объявления классов/баз, PARTS/template или адреса прямых функций; остальные тела не проиндексированы. Входящие ссылки на HBS/CSS/JSON сами по себе не меняют покрытие их определений.

| ID | Файл | Добавленные определения |
| --- | --- | --- |
| src-000005 | [module/activeEffect/WitcherActiveEffectSheet.js](../../../module/activeEffect/WitcherActiveEffectSheet.js) | WitcherActiveEffectConfig; WitcherActiveEffectConfig.PARTS |
| src-000029 | [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) | WitcherCharacterSheet; WitcherCharacterSheet.PARTS |
| src-000030 | [module/actor/sheets/WitcherLootSheet.js](../../../module/actor/sheets/WitcherLootSheet.js) | WitcherLootSheet; WitcherLootSheet.PARTS |
| src-000031 | [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js) | WitcherMonsterSheet; WitcherMonsterSheet.PARTS |
| src-000035 | [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | WitcherMysterySheet; WitcherMysterySheet.PARTS |
| src-000049 | [module/app/reward/reward.js](../../../module/app/reward/reward.js) | Rewards; Rewards.handoutIpRewards; Rewards.handoutCurrencyRewards |
| src-000051 | [module/chatMessage/witcherChatMessage.js](../../../module/chatMessage/witcherChatMessage.js) | WitcherChatMessage |
| src-000094 | [module/data/chatMessage/attackMessageData.js](../../../module/data/chatMessage/attackMessageData.js) | AttackMessageData |
| src-000095 | [module/data/chatMessage/baseMessageData.js](../../../module/data/chatMessage/baseMessageData.js) | BaseMessageData |
| src-000096 | [module/data/chatMessage/damageMessageData.js](../../../module/data/chatMessage/damageMessageData.js) | DamageMessageData |
| src-000097 | [module/data/chatMessage/defenseMessageData.js](../../../module/data/chatMessage/defenseMessageData.js) | DefenseMessageData |
| src-000103 | [module/data/investigation/clueData.js](../../../module/data/investigation/clueData.js) | ClueData |
| src-000105 | [module/data/investigation/obstacleData.js](../../../module/data/investigation/obstacleData.js) | ObstacleData |
| src-000107 | [module/data/item/alchemicalData.js](../../../module/data/item/alchemicalData.js) | AlchemicalData |
| src-000108 | [module/data/item/armorData.js](../../../module/data/item/armorData.js) | ArmorData |
| src-000109 | [module/data/item/commonItemData.js](../../../module/data/item/commonItemData.js) | CommonItemData |
| src-000110 | [module/data/item/componentData.js](../../../module/data/item/componentData.js) | ComponentData |
| src-000111 | [module/data/item/containerData.js](../../../module/data/item/containerData.js) | ContainerData |
| src-000112 | [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js) | CriticalWoundData |
| src-000113 | [module/data/item/diagramData.js](../../../module/data/item/diagramData.js) | DiagramData |
| src-000114 | [module/data/item/enhancementData.js](../../../module/data/item/enhancementData.js) | EnhancementData |
| src-000115 | [module/data/item/hexData.js](../../../module/data/item/hexData.js) | HexData |
| src-000116 | [module/data/item/homelandData.js](../../../module/data/item/homelandData.js) | HomelandData |
| src-000118 | [module/data/item/mountData.js](../../../module/data/item/mountData.js) | MountData |
| src-000119 | [module/data/item/mutagenData.js](../../../module/data/item/mutagenData.js) | MutagenData |
| src-000120 | [module/data/item/noteData.js](../../../module/data/item/noteData.js) | NoteData |
| src-000121 | [module/data/item/professionData.js](../../../module/data/item/professionData.js) | ProfessionData |
| src-000122 | [module/data/item/raceData.js](../../../module/data/item/raceData.js) | RaceData |
| src-000123 | [module/data/item/ritualData.js](../../../module/data/item/ritualData.js) | RitualData |
| src-000125 | [module/data/item/spellData.js](../../../module/data/item/spellData.js) | SpellData |
| src-000154 | [module/data/item/valuableData.js](../../../module/data/item/valuableData.js) | ValuableData |
| src-000155 | [module/data/item/weaponData.js](../../../module/data/item/weaponData.js) | WeaponData |
| src-000163 | [module/item/sheets/WitcherAlchemicalSheet.js](../../../module/item/sheets/WitcherAlchemicalSheet.js) | WitcherAlchemicalSheet; WitcherAlchemicalSheet.PARTS |
| src-000164 | [module/item/sheets/WitcherArmorSheet.js](../../../module/item/sheets/WitcherArmorSheet.js) | WitcherArmorSheet; WitcherArmorSheet.PARTS |
| src-000165 | [module/item/sheets/WitcherComponentSheet.js](../../../module/item/sheets/WitcherComponentSheet.js) | WitcherComponentSheet; WitcherComponentSheet.PARTS |
| src-000166 | [module/item/sheets/WitcherContainerSheet.js](../../../module/item/sheets/WitcherContainerSheet.js) | WitcherContainerSheet; WitcherContainerSheet.PARTS |
| src-000167 | [module/item/sheets/WitcherCriticalWoundSheet.js](../../../module/item/sheets/WitcherCriticalWoundSheet.js) | WitcherCriticalWoundSheet; WitcherCriticalWoundSheet.PARTS |
| src-000168 | [module/item/sheets/WitcherDiagramSheet.js](../../../module/item/sheets/WitcherDiagramSheet.js) | WitcherDiagramSheet; WitcherDiagramSheet.PARTS |
| src-000169 | [module/item/sheets/WitcherEnhancementSheet.js](../../../module/item/sheets/WitcherEnhancementSheet.js) | WitcherEnhancementSheet; WitcherEnhancementSheet.PARTS |
| src-000170 | [module/item/sheets/WitcherHexSheet.js](../../../module/item/sheets/WitcherHexSheet.js) | WitcherHexSheet; WitcherHexSheet.PARTS |
| src-000171 | [module/item/sheets/WitcherHomelandSheet.js](../../../module/item/sheets/WitcherHomelandSheet.js) | WitcherHomelandSheet; WitcherHomelandSheet.PARTS |
| src-000172 | [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js) | WitcherItemSheet; WitcherItemSheet.PARTS |
| src-000173 | [module/item/sheets/WitcherMountSheet.js](../../../module/item/sheets/WitcherMountSheet.js) | WitcherMountSheet; WitcherMountSheet.PARTS |
| src-000174 | [module/item/sheets/WitcherMutagenSheet.js](../../../module/item/sheets/WitcherMutagenSheet.js) | WitcherMutagenSheet; WitcherMutagenSheet.PARTS |
| src-000175 | [module/item/sheets/WitcherProfessionSheet.js](../../../module/item/sheets/WitcherProfessionSheet.js) | WitcheProfessionSheet; WitcheProfessionSheet.PARTS |
| src-000176 | [module/item/sheets/WitcherRaceSheet.js](../../../module/item/sheets/WitcherRaceSheet.js) | WitcherRaceSheet; WitcherRaceSheet.PARTS |
| src-000177 | [module/item/sheets/WitcherRitualSheet.js](../../../module/item/sheets/WitcherRitualSheet.js) | WitcherRitualSheet; WitcherRitualSheet.PARTS |
| src-000178 | [module/item/sheets/WitcherSkillItemSheet.js](../../../module/item/sheets/WitcherSkillItemSheet.js) | WitcherSkillItemSheet; WitcherSkillItemSheet.PARTS |
| src-000179 | [module/item/sheets/WitcherSpellSheet.js](../../../module/item/sheets/WitcherSpellSheet.js) | WitcherSpellSheet; WitcherSpellSheet.PARTS |
| src-000180 | [module/item/sheets/WitcherValuableSheet.js](../../../module/item/sheets/WitcherValuableSheet.js) | WitcherValuableSheet; WitcherValuableSheet.PARTS |
| src-000181 | [module/item/sheets/WitcherWeaponSheet.js](../../../module/item/sheets/WitcherWeaponSheet.js) | WitcherWeaponSheet; WitcherWeaponSheet.PARTS |
| src-000188 | [module/item/sheets/investigation/WitcherClueSheet.js](../../../module/item/sheets/investigation/WitcherClueSheet.js) | WitcherClueSheet; WitcherClueSheet.template |
| src-000189 | [module/item/sheets/investigation/WitcherObstacleSheet.js](../../../module/item/sheets/investigation/WitcherObstacleSheet.js) | WitcherObstacleSheet; WitcherObstacleSheet.template |
| src-000192 | [module/item/witcherItem.js](../../../module/item/witcherItem.js) | WitcherItem |
| src-000193 | [module/scripts/chat.js](../../../module/scripts/chat.js) | chatMessageListeners |
| src-000194 | [module/scripts/combat/applyDamage.js](../../../module/scripts/combat/applyDamage.js) | addDamageMessageContextOptions |
| src-000195 | [module/scripts/combat/combat.js](../../../module/scripts/combat/combat.js) | attackChatMessageListeners; defenseChatMessageListeners; addDefenseOptionsContextMenu; addCritMessageContextOptions |
| src-000196 | [module/scripts/combat/generalCombatHook.js](../../../module/scripts/combat/generalCombatHook.js) | applyGeneralCombatHooks |
| src-000200 | [module/scripts/regions/regionHooks.js](../../../module/scripts/regions/regionHooks.js) | countdownDurationOfRegions |
| src-000203 | [module/scripts/rolls/fumble.js](../../../module/scripts/rolls/fumble.js) | addFumbleContextOptions |
| src-000205 | [module/scripts/statusEffects/applyStatusEffect.js](../../../module/scripts/statusEffects/applyStatusEffect.js) | chatMessageListeners |
| src-000206 | [module/scripts/temporaryEffects/applyActiveEffect.js](../../../module/scripts/temporaryEffects/applyActiveEffect.js) | applyActiveEffectToActorViaId |
| src-000207 | [module/scripts/verbalCombat/verbalCombat.js](../../../module/scripts/verbalCombat/verbalCombat.js) | chatMessageListeners; addVerbalCombatMessageContextOptions |
| src-000208 | [module/scripts/verbalCombat/verbalCombatDefense.js](../../../module/scripts/verbalCombat/verbalCombatDefense.js) | addVerbalCombatDefenseMessageContextOptions |
| src-000210 | [module/setup/deprecations.js](../../../module/setup/deprecations.js) | deprecationWarnings |
| src-000211 | [module/setup/handlebars.js](../../../module/setup/handlebars.js) | preloadHandlebarsTemplates; registerHandelbarHelpers |
| src-000213 | [module/setup/queries.js](../../../module/setup/queries.js) | registerQueries |
| src-000217 | [module/setup/socketHook.js](../../../module/setup/socketHook.js) | registerSocketListeners |

## Проверка и ограничения

[16 запросов](examples/expansion-006-queries.json) задают ожидания по исходникам для IQ-01–IQ-08. [Тесты расширения](tests/test_expansion_006.py) проверяют все модельные назначения, листы, настройки, ветви/адреса процессов, старые ID и refs поздних уточнений. Прямой и обратный поиск проверяет общий приёмочный тест для всех отношений текущего набора.

Фиксированные размеры пилота проверяются на его исходных JSONL-частях; прежние справочные запросы продолжают выполняться на расширенном наборе. Это сохранение прежних проверок, а не объявление нового графа старым пилотом. Подробные результаты команд и проверки сохранности фиксируются в [протоколе .006](review-log.md#task-0006006).

Настоящий игровой код, ядро Foundry, браузер, мир, БД и сеть этой порцией не исполнялись. Содержимое компедиумов не проверялось по правилам. Issues и документы большого аудита не менялись. Следующая согласованная порция — [TASK-0006.007](../../tasks/task-0006.007.md), редактор ActiveEffect и мастер изменений.
