# Реестр файлов системы

Исследуемый срез: `15da5b225535e34af4e132c701b5353ef4eb667f`, ветка `rusbar-main`, дата инвентаризации 2026-09-10.

В реестре **621 файл** после [согласованных исключений](README.md#согласованные-исключения). Состав сверяется по самим путям с Git и фактическим деревом; результаты находятся в [журнале](review-log.md). Пути в первом столбце относительны корню репозитория и ведут к исходным файлам рабочего checkout; соответствие указанному коммиту подтверждено при инвентаризации.

После TASK-0002, TASK-0003.001–TASK-0003.015 проверены описания **121 файлов**, для **500 файлов** разбор не начат. Назначения и ссылки заполнены только для прочитанных и сверенных файлов. «Не подготовлено» означает отсутствие карточки; просмотр отдельных определений в зависимостях не меняет статус их файлов.

Последняя [сверка TASK-0003.015](review-log.md#task-0003015) выполнена на `7edb814aa870da75c7ad7633536e899a8d07e205`: все 621 исходник совпадают с базовым срезом выше. Статус «Проверено» относится к документации и не означает отсутствие ошибок или проверку запуска Foundry.

[Правила статусов и оформления](README.md#реестр-и-карточки), [шаблон карточки](templates/file.md).

| Файл | Краткое назначение | Подробное описание | Статус анализа |
| --- | --- | --- | --- |
| [build.json](../../../build.json) | Не установлено | Не подготовлено | Не начат |
| [lang/de.json](../../../lang/de.json) | Не установлено | Не подготовлено | Не начат |
| [lang/en.json](../../../lang/en.json) | Не установлено | Не подготовлено | Не начат |
| [lang/es.json](../../../lang/es.json) | Не установлено | Не подготовлено | Не начат |
| [lang/fr.json](../../../lang/fr.json) | Не установлено | Не подготовлено | Не начат |
| [lang/it.json](../../../lang/it.json) | Не установлено | Не подготовлено | Не начат |
| [lang/pl.json](../../../lang/pl.json) | Не установлено | Не подготовлено | Не начат |
| [lang/ptbr.json](../../../lang/ptbr.json) | Не установлено | Не подготовлено | Не начат |
| [lang/ru.json](../../../lang/ru.json) | Не установлено | Не подготовлено | Не начат |
| [module/TheWitcherTRPG.js](../../../module/TheWitcherTRPG.js) | Точка входа: жизненный цикл, реестры документов, API, чат и макросы | [Карточка](files/module/TheWitcherTRPG.js.md) | Проверено |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../module/activeEffect/WitcherActiveEffectSheet.js) | Лист ActiveEffect: системная вкладка, мастер добавления изменений и автодополнение. | [Описание](files/module/activeEffect/WitcherActiveEffectSheet.js.md) | Проверено |
| [module/activeEffect/mixins/baseMixin.js](../../../module/activeEffect/mixins/baseMixin.js) | Каталог путей характеристик, навыков, биографии, атак и изменений урона для мастера. | [Описание](files/module/activeEffect/mixins/baseMixin.js.md) | Проверено |
| [module/activeEffect/mixins/temporaryItemImprovementMixin.js](../../../module/activeEffect/mixins/temporaryItemImprovementMixin.js) | Три подсказки путей урона для временного улучшения Item. | [Описание](files/module/activeEffect/mixins/temporaryItemImprovementMixin.js.md) | Проверено |
| [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js) | Документ ActiveEffect: подавление, фазы изменений, выбор навыка и подготовка длительности. | [Описание](files/module/activeEffect/witcherActiveEffect.js.md) | Проверено |
| [module/actor/mixins/adrenalineMixin.js](../../../module/actor/mixins/adrenalineMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/armorMixin.js](../../../module/actor/mixins/armorMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/castSpellMixin.js](../../../module/actor/mixins/castSpellMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/craftingMixin.js](../../../module/actor/mixins/craftingMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/currencyConverterMixin.js](../../../module/actor/mixins/currencyConverterMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/damageUtilMixin.js](../../../module/actor/mixins/damageUtilMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/defenseMixin.js](../../../module/actor/mixins/defenseMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/healMixin.js](../../../module/actor/mixins/healMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/locationMixin.js](../../../module/actor/mixins/locationMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/modifierMixin.js](../../../module/actor/mixins/modifierMixin.js) | Фрагменты формул из модификаторов навыков, групп, атаки и защиты. | [Описание](files/module/actor/mixins/modifierMixin.js.md) | Проверено |
| [module/actor/mixins/professionMixin.js](../../../module/actor/mixins/professionMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/rewardsMixin.js](../../../module/actor/mixins/rewardsMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/skillMixin.js](../../../module/actor/mixins/skillMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/temporaryEffectMixin.js](../../../module/actor/mixins/temporaryEffectMixin.js) | Выбор оружия, передача временных улучшений и сообщение в чат. | [Описание](files/module/actor/mixins/temporaryEffectMixin.js.md) | Проверено |
| [module/actor/mixins/verbalCombatMixin.js](../../../module/actor/mixins/verbalCombatMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/mixins/weaponAttackMixin.js](../../../module/actor/mixins/weaponAttackMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/rewardsSheet.js](../../../module/actor/rewardsSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/WitcherLootSheet.js](../../../module/actor/sheets/WitcherLootSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../module/actor/sheets/interactions/itemContextMenu.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/activeEffectMixin.js](../../../module/actor/sheets/mixins/activeEffectMixin.js) | Категории эффектов Actor, управление документами и раскрытие описаний. | [Описание](files/module/actor/sheets/mixins/activeEffectMixin.js.md) | Проверено |
| [module/actor/sheets/mixins/alchemyMixin.js](../../../module/actor/sheets/mixins/alchemyMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/criticalWoundMixin.js](../../../module/actor/sheets/mixins/criticalWoundMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/currencyConverterMixin.js](../../../module/actor/sheets/mixins/currencyConverterMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/customSkillMixin.js](../../../module/actor/sheets/mixins/customSkillMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../module/actor/sheets/mixins/deathSaveMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/healMixin.js](../../../module/actor/sheets/mixins/healMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/noteMixin.js](../../../module/actor/sheets/mixins/noteMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/skillMixin.js](../../../module/actor/sheets/mixins/skillMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/sheets/mixins/statMixin.js](../../../module/actor/sheets/mixins/statMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/actor/witcherActor.js](../../../module/actor/witcherActor.js) | Документ Actor: подготовка характеристик, статусы, предметы, локации и подключение 17 примесей. | [Описание](files/module/actor/witcherActor.js.md) | Проверено |
| [module/app/htmlUtils.js](../../../module/app/htmlUtils.js) | Не установлено | Не подготовлено | Не начат |
| [module/app/reward/reward.js](../../../module/app/reward/reward.js) | Не установлено | Не подготовлено | Не начат |
| [module/chatMessage/chatMessageData.js](../../../module/chatMessage/chatMessageData.js) | Не установлено | Не подготовлено | Не начат |
| [module/chatMessage/witcherChatMessage.js](../../../module/chatMessage/witcherChatMessage.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/activeEffects/witcherActiveEffectData.js](../../../module/data/activeEffects/witcherActiveEffectData.js) | Системная модель обычного эффекта: changes ядра и пять флагов применения. | [Описание](files/module/data/activeEffects/witcherActiveEffectData.js.md) | Проверено |
| [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) | Модель временного улучшения: changes, флаги применения и передачи. | [Описание](files/module/data/activeEffects/witcherTemporaryItemImprovementData.js.md) | Проверено |
| [module/data/actor/characterData.js](../../../module/data/actor/characterData.js) | Модель персонажа: биография, опыт, обучение, журналы и обогащение текста. | [Описание](files/module/data/actor/characterData.js.md) | Проверено |
| [module/data/actor/commonActorData.js](../../../module/data/actor/commonActorData.js) | Общая модель Actor: 19 полей, подготовка базовых максимумов, масса валют и миграции. | [Описание](files/module/data/actor/commonActorData.js.md) | Проверено |
| [module/data/actor/lootData.js](../../../module/data/actor/lootData.js) | Модель хранилища добычи: вместимость, описание, валюты и масса монет. | [Описание](files/module/data/actor/lootData.js.md) | Проверено |
| [module/data/actor/monsterData.js](../../../module/data/actor/monsterData.js) | Модель монстра: сведения, броня, сопротивления, настройки и три блока знаний. | [Описание](files/module/data/actor/monsterData.js.md) | Проверено |
| [module/data/actor/templates/character/attackData.js](../../../module/data/actor/templates/character/attackData.js) | Строковая пара label/value для punch и kick | [Карточка](files/module/data/actor/templates/character/attackData.js.md) | Проверено |
| [module/data/actor/templates/character/attackStatsData.js](../../../module/data/actor/templates/character/attackStatsData.js) | Общие данные ближнего боя и модификаторы критов | [Карточка](files/module/data/actor/templates/character/attackStatsData.js.md) | Проверено |
| [module/data/actor/templates/character/currencyLogData.js](../../../module/data/actor/templates/character/currencyLogData.js) | Поля одной записи журнала валют | [Карточка](files/module/data/actor/templates/character/currencyLogData.js.md) | Проверено |
| [module/data/actor/templates/character/general/backgroundData.js](../../../module/data/actor/templates/character/general/backgroundData.js) | HTML-поле биографии персонажа | [Карточка](files/module/data/actor/templates/character/general/backgroundData.js.md) | Проверено |
| [module/data/actor/templates/character/general/damage/damageModificationData.js](../../../module/data/actor/templates/character/general/damage/damageModificationData.js) | Параметры flat, multiplication и applyAP для типа урона | [Карточка](files/module/data/actor/templates/character/general/damage/damageModificationData.js.md) | Проверено |
| [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](../../../module/data/actor/templates/character/general/damage/damageTypeModificationData.js) | Семь наборов изменений урона общей модели Actor | [Карточка](files/module/data/actor/templates/character/general/damage/damageTypeModificationData.js.md) | Проверено |
| [module/data/actor/templates/character/general/detailsData.js](../../../module/data/actor/templates/character/general/detailsData.js) | Семь текстовых подробностей персонажа с подписями | [Карточка](files/module/data/actor/templates/character/general/detailsData.js.md) | Проверено |
| [module/data/actor/templates/character/general/homelandData.js](../../../module/data/actor/templates/character/general/homelandData.js) | Ключ родины и свободный текст в биографии Actor | [Карточка](files/module/data/actor/templates/character/general/homelandData.js.md) | Проверено |
| [module/data/actor/templates/character/general/lifeEventData.js](../../../module/data/actor/templates/character/general/lifeEventData.js) | Поля одной записи события жизни и состояние раскрытия | [Карточка](files/module/data/actor/templates/character/general/lifeEventData.js.md) | Проверено |
| [module/data/actor/templates/character/general/lifeEventsData.js](../../../module/data/actor/templates/character/general/lifeEventsData.js) | Двадцать событий жизни с ключами 10–200 | [Карточка](files/module/data/actor/templates/character/general/lifeEventsData.js.md) | Проверено |
| [module/data/actor/templates/character/generalData.js](../../../module/data/actor/templates/character/generalData.js) | Сборка общих сведений персонажа в system.general | [Карточка](files/module/data/actor/templates/character/generalData.js.md) | Проверено |
| [module/data/actor/templates/character/ipLogData.js](../../../module/data/actor/templates/character/ipLogData.js) | Поля одной записи журнала очков развития | [Карточка](files/module/data/actor/templates/character/ipLogData.js.md) | Проверено |
| [module/data/actor/templates/character/logData.js](../../../module/data/actor/templates/character/logData.js) | Модель журналов и операции наград/расходов | [Карточка](files/module/data/actor/templates/character/logData.js.md) | Проверено |
| [module/data/actor/templates/character/pannelsData.js](../../../module/data/actor/templates/character/pannelsData.js) | 22 флага раскрытия разделов интерфейса Actor | [Карточка](files/module/data/actor/templates/character/pannelsData.js.md) | Проверено |
| [module/data/actor/templates/character/skillTrainingData.js](../../../module/data/actor/templates/character/skillTrainingData.js) | Пара name/value ручного обучения персонажа | [Карточка](files/module/data/actor/templates/character/skillTrainingData.js.md) | Проверено |
| [module/data/actor/templates/common/adrenalineData.js](../../../module/data/actor/templates/common/adrenalineData.js) | Поля количества адреналина и его подписи | [Карточка](files/module/data/actor/templates/common/adrenalineData.js.md) | Проверено |
| [module/data/actor/templates/common/combatEffectsData.js](../../../module/data/actor/templates/common/combatEffectsData.js) | Модификаторы атаки/защиты, воздействия начала хода и временные HP | [Карточка](files/module/data/actor/templates/common/combatEffectsData.js.md) | Проверено |
| [module/data/actor/templates/common/currencyData.js](../../../module/data/actor/templates/common/currencyData.js) | Семь числовых остатков валют Actor | [Карточка](files/module/data/actor/templates/common/currencyData.js.md) | Проверено |
| [module/data/actor/templates/common/focusData.js](../../../module/data/actor/templates/common/focusData.js) | Имя и значение одного слота фокусировки | [Карточка](files/module/data/actor/templates/common/focusData.js.md) | Проверено |
| [module/data/actor/templates/common/lifepathData.js](../../../module/data/actor/templates/common/lifepathData.js) | Модификаторы защиты, нагрузки брони, магии и типов удара | [Карточка](files/module/data/actor/templates/common/lifepathData.js.md) | Проверено |
| [module/data/actor/templates/common/noteData.js](../../../module/data/actor/templates/common/noteData.js) | Заголовок и текст записи массива заметок | [Карточка](files/module/data/actor/templates/common/noteData.js.md) | Проверено |
| [module/data/actor/templates/common/reputationData.js](../../../module/data/actor/templates/common/reputationData.js) | Числовая репутация: схема stat, подготовка max и миграция | [Карточка](files/module/data/actor/templates/common/reputationData.js.md) | Проверено |
| [module/data/actor/templates/common/skills/bodyData.js](../../../module/data/actor/templates/common/skills/bodyData.js) | Два навыка BODY и миграция подписей | [Карточка](files/module/data/actor/templates/common/skills/bodyData.js.md) | Проверено |
| [module/data/actor/templates/common/skills/craData.js](../../../module/data/actor/templates/common/skills/craData.js) | Семь навыков CRA и миграция подписей | [Карточка](files/module/data/actor/templates/common/skills/craData.js.md) | Проверено |
| [module/data/actor/templates/common/skills/dexData.js](../../../module/data/actor/templates/common/skills/dexData.js) | Пять навыков DEX и миграция подписей | [Карточка](files/module/data/actor/templates/common/skills/dexData.js.md) | Проверено |
| [module/data/actor/templates/common/skills/empData.js](../../../module/data/actor/templates/common/skills/empData.js) | Десять навыков EMP и миграция подписей | [Карточка](files/module/data/actor/templates/common/skills/empData.js.md) | Проверено |
| [module/data/actor/templates/common/skills/intData.js](../../../module/data/actor/templates/common/skills/intData.js) | Тринадцать навыков INT и миграция подписей | [Карточка](files/module/data/actor/templates/common/skills/intData.js.md) | Проверено |
| [module/data/actor/templates/common/skills/refData.js](../../../module/data/actor/templates/common/skills/refData.js) | Восемь навыков REF и миграция подписей | [Карточка](files/module/data/actor/templates/common/skills/refData.js.md) | Проверено |
| [module/data/actor/templates/common/skills/skillData.js](../../../module/data/actor/templates/common/skills/skillData.js) | Общая модель навыка: значение, модификаторы, флаги и modifiedValue | [Карточка](files/module/data/actor/templates/common/skills/skillData.js.md) | Проверено |
| [module/data/actor/templates/common/skills/skillsData.js](../../../module/data/actor/templates/common/skills/skillsData.js) | Сборка семи групп навыков для общей схемы Actor | [Карточка](files/module/data/actor/templates/common/skills/skillsData.js.md) | Проверено |
| [module/data/actor/templates/common/skills/willData.js](../../../module/data/actor/templates/common/skills/willData.js) | Семь навыков WILL и миграция подписей | [Карточка](files/module/data/actor/templates/common/skills/willData.js.md) | Проверено |
| [module/data/actor/templates/common/stats/derivedStatsData.js](../../../module/data/actor/templates/common/stats/derivedStatsData.js) | Схема 12 производных параметров и миграция шести исходных значений | [Карточка](files/module/data/actor/templates/common/stats/derivedStatsData.js.md) | Проверено |
| [module/data/actor/templates/common/stats/statData.js](../../../module/data/actor/templates/common/stats/statData.js) | Общая схема пяти полей характеристики, ресурса и репутации | [Карточка](files/module/data/actor/templates/common/stats/statData.js.md) | Проверено |
| [module/data/actor/templates/common/stats/statsData.js](../../../module/data/actor/templates/common/stats/statsData.js) | Модель 10 показателей stats, копирование базовых максимумов и миграция | [Карточка](files/module/data/actor/templates/common/stats/statsData.js.md) | Проверено |
| [module/data/actor/templates/common/temporaryEffectsData.js](../../../module/data/actor/templates/common/temporaryEffectsData.js) | Словарь временных HP с записями name/value | [Карточка](files/module/data/actor/templates/common/temporaryEffectsData.js.md) | Проверено |
| [module/data/actor/templates/valueLabelData.js](../../../module/data/actor/templates/valueLabelData.js) | Фабрика строкового значения и ключа его подписи | [Карточка](files/module/data/actor/templates/valueLabelData.js.md) | Проверено |
| [module/data/chatMessage/attackMessageData.js](../../../module/data/chatMessage/attackMessageData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/chatMessage/baseMessageData.js](../../../module/data/chatMessage/baseMessageData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/chatMessage/damageMessageData.js](../../../module/data/chatMessage/damageMessageData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/chatMessage/defenseMessageData.js](../../../module/data/chatMessage/defenseMessageData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/chatMessage/templates/attackData.js](../../../module/data/chatMessage/templates/attackData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/chatMessage/templates/critData.js](../../../module/data/chatMessage/templates/critData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/chatMessage/templates/damageData.js](../../../module/data/chatMessage/templates/damageData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/chatMessage/templates/locationData.js](../../../module/data/chatMessage/templates/locationData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/dataUtils.js](../../../module/data/dataUtils.js) | Подготовка HTML, исходного текста и определения поля для листов Actor/Item | [Карточка](files/module/data/dataUtils.js.md) | Проверено |
| [module/data/investigation/clueData.js](../../../module/data/investigation/clueData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/investigation/mysteryActorData.js](../../../module/data/investigation/mysteryActorData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/investigation/obstacleData.js](../../../module/data/investigation/obstacleData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/investigation/templates/complexityData.js](../../../module/data/investigation/templates/complexityData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/alchemicalData.js](../../../module/data/item/alchemicalData.js) | Модель алхимического Item с текстовыми свойствами и настройками расходования. | [Описание](files/module/data/item/alchemicalData.js.md) | Проверено |
| [module/data/item/armorData.js](../../../module/data/item/armorData.js) | Модель брони и щитов: SP, сопротивления, улучшения, ремонт и миграции. | [Описание](files/module/data/item/armorData.js.md) | Проверено |
| [module/data/item/commonItemData.js](../../../module/data/item/commonItemData.js) | Общая модель части типов Item: поля описания/количества/массы, calcWeight и признаки возможностей. | [Карточка](files/module/data/item/commonItemData.js.md) | Проверено |
| [module/data/item/componentData.js](../../../module/data/item/componentData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/containerData.js](../../../module/data/item/containerData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/diagramData.js](../../../module/data/item/diagramData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/enhancementData.js](../../../module/data/item/enhancementData.js) | Модель предмета улучшения: бонус SP, сопротивления, эффекты и миграция. | [Описание](files/module/data/item/enhancementData.js.md) | Проверено |
| [module/data/item/hexData.js](../../../module/data/item/hexData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/homelandData.js](../../../module/data/item/homelandData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/mixin/spellRegionMixin.js](../../../module/data/item/mixin/spellRegionMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/mountData.js](../../../module/data/item/mountData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/mutagenData.js](../../../module/data/item/mutagenData.js) | Модель мутагена: категория, источник, мутация и настройки расходования. | [Описание](files/module/data/item/mutagenData.js.md) | Проверено |
| [module/data/item/noteData.js](../../../module/data/item/noteData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/professionData.js](../../../module/data/item/professionData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/raceData.js](../../../module/data/item/raceData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/ritualData.js](../../../module/data/item/ritualData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/skillItemData.js](../../../module/data/item/skillItemData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/spellData.js](../../../module/data/item/spellData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/armor/resistanceData.js](../../../module/data/item/templates/armor/resistanceData.js) | Три сопротивления брони и их объединение с улучшениями. | [Описание](files/module/data/item/templates/armor/resistanceData.js.md) | Проверено |
| [module/data/item/templates/armor/spData.js](../../../module/data/item/templates/armor/spData.js) | Исходные и вычисленные значения SP одной локации брони. | [Описание](files/module/data/item/templates/armor/spData.js.md) | Проверено |
| [module/data/item/templates/associatedDiagramData.js](../../../module/data/item/templates/associatedDiagramData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/combat/attackOptionsData.js](../../../module/data/item/templates/combat/attackOptionsData.js) | Общие поля вариантов атаки, навыков, бонусов урона и метательного свойства. | [Описание](files/module/data/item/templates/combat/attackOptionsData.js.md) | Проверено |
| [module/data/item/templates/combat/damagePropertiesData.js](../../../module/data/item/templates/combat/damagePropertiesData.js) | Вложенные свойства урона: флаги, эффекты, объединение, представление и миграция. | [Описание](files/module/data/item/templates/combat/damagePropertiesData.js.md) | Проверено |
| [module/data/item/templates/combat/defenseOptionsData.js](../../../module/data/item/templates/combat/defenseOptionsData.js) | Поле множества разрешённых способов защиты от атаки. | [Описание](files/module/data/item/templates/combat/defenseOptionsData.js.md) | Проверено |
| [module/data/item/templates/combat/defensePropertiesData.js](../../../module/data/item/templates/combat/defensePropertiesData.js) | Вложенная модель применимости собственной защиты и её модификатора. | [Описание](files/module/data/item/templates/combat/defensePropertiesData.js.md) | Проверено |
| [module/data/item/templates/combat/skillAttackData.js](../../../module/data/item/templates/combat/skillAttackData.js) | Схема атаки профессионального навыка с общими боевыми свойствами. | [Описание](files/module/data/item/templates/combat/skillAttackData.js.md) | Проверено |
| [module/data/item/templates/combat/skillDefenseData.js](../../../module/data/item/templates/combat/skillDefenseData.js) | Схема включения защиты профессионального навыка и DefenseProperties. | [Описание](files/module/data/item/templates/combat/skillDefenseData.js.md) | Проверено |
| [module/data/item/templates/componentData.js](../../../module/data/item/templates/componentData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/consumableData.js](../../../module/data/item/templates/consumableData.js) | Фабрика признака isConsumable и вложенных consumeProperties. | [Описание](files/module/data/item/templates/consumableData.js.md) | Проверено |
| [module/data/item/templates/consumePropertiesData.js](../../../module/data/item/templates/consumePropertiesData.js) | Вложенная схема лечения и массивов добавляемых/снимаемых статусов. | [Описание](files/module/data/item/templates/consumePropertiesData.js.md) | Проверено |
| [module/data/item/templates/craftingComponentData.js](../../../module/data/item/templates/craftingComponentData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/effectDerivedStatData.js](../../../module/data/item/templates/effectDerivedStatData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/effectSkillData.js](../../../module/data/item/templates/effectSkillData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/effectStatData.js](../../../module/data/item/templates/effectStatData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/itemEffectData.js](../../../module/data/item/templates/itemEffectData.js) | Фабрика четырёх полей одной записи предметного воздействия. | [Описание](files/module/data/item/templates/itemEffectData.js.md) | Проверено |
| [module/data/item/templates/perkData.js](../../../module/data/item/templates/perkData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/profession/skillUsageData.js](../../../module/data/item/templates/profession/skillUsageData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/profession/temporaryHealthData.js](../../../module/data/item/templates/profession/temporaryHealthData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/profession/thresholdData.js](../../../module/data/item/templates/profession/thresholdData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/professionPathData.js](../../../module/data/item/templates/professionPathData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/professionSkillData.js](../../../module/data/item/templates/professionSkillData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/regions/regionBehavioursData.js](../../../module/data/item/templates/regions/regionBehavioursData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/regions/regionPropertiesData.js](../../../module/data/item/templates/regions/regionPropertiesData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/regions/templatePropertiesData.js](../../../module/data/item/templates/regions/templatePropertiesData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/socialStandingData.js](../../../module/data/item/templates/socialStandingData.js) | Не установлено | Не подготовлено | Не начат |
| [module/data/item/templates/weaponTypeData.js](../../../module/data/item/templates/weaponTypeData.js) | Пять полей описания типа оружия и четырёх видов урона. | [Описание](files/module/data/item/templates/weaponTypeData.js.md) | Проверено |
| [module/data/item/valuableData.js](../../../module/data/item/valuableData.js) | Модель прочего предмета с категорией, скрытностью и расходованием. | [Описание](files/module/data/item/valuableData.js.md) | Проверено |
| [module/data/item/weaponData.js](../../../module/data/item/weaponData.js) | Модель оружия: боевые свойства, улучшения, защита, ремонт и миграция. | [Описание](files/module/data/item/weaponData.js.md) | Проверено |
| [module/data/migrations/damagePropertiesMigration.js](../../../module/data/migrations/damagePropertiesMigration.js) | Перенос пяти прежних полей Weapon/Spell внутрь damageProperties. | [Описание](files/module/data/migrations/damagePropertiesMigration.js.md) | Проверено |
| [module/item/mixins/consumeMixin.js](../../../module/item/mixins/consumeMixin.js) | Применение Item: лечение Actor, статусы, applySelf ActiveEffect и чат. | [Описание](files/module/item/mixins/consumeMixin.js.md) | Проверено |
| [module/item/mixins/costEditMixin.js](../../../module/item/mixins/costEditMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/mixins/damageUtilMixin.js](../../../module/item/mixins/damageUtilMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/mixins/defenseOptionMixin.js](../../../module/item/mixins/defenseOptionMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/mixins/dismantlingMixin.js](../../../module/item/mixins/dismantlingMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/mixins/repairMixin.js](../../../module/item/mixins/repairMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherAlchemicalSheet.js](../../../module/item/sheets/WitcherAlchemicalSheet.js) | Лист алхимии с категориями и конфигурацией расходования. | [Описание](files/module/item/sheets/WitcherAlchemicalSheet.js.md) | Проверено |
| [module/item/sheets/WitcherArmorSheet.js](../../../module/item/sheets/WitcherArmorSheet.js) | Лист брони: контекст, варианты ношения, конфигурация и рецепт. | [Описание](files/module/item/sheets/WitcherArmorSheet.js.md) | Проверено |
| [module/item/sheets/WitcherComponentSheet.js](../../../module/item/sheets/WitcherComponentSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherContainerSheet.js](../../../module/item/sheets/WitcherContainerSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherCriticalWoundSheet.js](../../../module/item/sheets/WitcherCriticalWoundSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherDiagramSheet.js](../../../module/item/sheets/WitcherDiagramSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherEnhancementSheet.js](../../../module/item/sheets/WitcherEnhancementSheet.js) | Лист улучшения с вариантами его категории. | [Описание](files/module/item/sheets/WitcherEnhancementSheet.js.md) | Проверено |
| [module/item/sheets/WitcherHexSheet.js](../../../module/item/sheets/WitcherHexSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherHomelandSheet.js](../../../module/item/sheets/WitcherHomelandSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js) | Общий лист Item: контекст, форма, редактор предметных воздействий, конфигурация и Drop. | [Описание](files/module/item/sheets/WitcherItemSheet.js.md) | Проверено |
| [module/item/sheets/WitcherMountSheet.js](../../../module/item/sheets/WitcherMountSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherMutagenSheet.js](../../../module/item/sheets/WitcherMutagenSheet.js) | Лист мутагена: категории цветов и унаследованная конфигурация. | [Описание](files/module/item/sheets/WitcherMutagenSheet.js.md) | Проверено |
| [module/item/sheets/WitcherProfessionSheet.js](../../../module/item/sheets/WitcherProfessionSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherRaceSheet.js](../../../module/item/sheets/WitcherRaceSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherRitualSheet.js](../../../module/item/sheets/WitcherRitualSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherSkillItemSheet.js](../../../module/item/sheets/WitcherSkillItemSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherSpellSheet.js](../../../module/item/sheets/WitcherSpellSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/WitcherValuableSheet.js](../../../module/item/sheets/WitcherValuableSheet.js) | Лист прочего предмета с категориями и конфигурацией расходования. | [Описание](files/module/item/sheets/WitcherValuableSheet.js.md) | Проверено |
| [module/item/sheets/WitcherWeaponSheet.js](../../../module/item/sheets/WitcherWeaponSheet.js) | Лист оружия: контекст, флаги типа урона и связанный рецепт. | [Описание](files/module/item/sheets/WitcherWeaponSheet.js.md) | Проверено |
| [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) | Специализация общей конфигурации с вкладкой SP брони. | [Описание](files/module/item/sheets/configurations/WitcherArmorConfigurationSheet.js.md) | Проверено |
| [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Базовая конфигурация Item: вкладки, категории и действия над ActiveEffect. | [Описание](files/module/item/sheets/configurations/WitcherConfigurationSheet.js.md) | Проверено |
| [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) | Редактор флага расходования, лечения и двух массивов статусов. | [Описание](files/module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js.md) | Проверено |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Общая конфигурация урона, защиты, регионов и предметных воздействий. | [Описание](files/module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js.md) | Проверено |
| [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/investigation/WitcherClueSheet.js](../../../module/item/sheets/investigation/WitcherClueSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/investigation/WitcherObstacleSheet.js](../../../module/item/sheets/investigation/WitcherObstacleSheet.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/sheets/mixins/associatedDiagramMixin.js](../../../module/item/sheets/mixins/associatedDiagramMixin.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/systems/repair.js](../../../module/item/systems/repair.js) | Не установлено | Не подготовлено | Не начат |
| [module/item/witcherItem.js](../../../module/item/witcherItem.js) | Документ Item: миграция магии, выбор атаки, изготовление, генерация добычи, улучшения и пять примесей. | [Карточка](files/module/item/witcherItem.js.md) | Проверено |
| [module/scripts/chat.js](../../../module/scripts/chat.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/combat/applyDamage.js](../../../module/scripts/combat/applyDamage.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/combat/combat.js](../../../module/scripts/combat/combat.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/combat/generalCombatHook.js](../../../module/scripts/combat/generalCombatHook.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/damageInstance.js](../../../module/scripts/damageInstance.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/helper.js](../../../module/scripts/helper.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/investigation/rollClue.js](../../../module/scripts/investigation/rollClue.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/regions/regionHooks.js](../../../module/scripts/regions/regionHooks.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/rollConfig.js](../../../module/scripts/rollConfig.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/rolls/extendedRoll.js](../../../module/scripts/rolls/extendedRoll.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/rolls/fumble.js](../../../module/scripts/rolls/fumble.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/socket/socketMessage.js](../../../module/scripts/socket/socketMessage.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/statusEffects/applyStatusEffect.js](../../../module/scripts/statusEffects/applyStatusEffect.js) | Применение статусов, ссылки чата, иммунитеты и интеграция statuscounter. | [Описание](files/module/scripts/statusEffects/applyStatusEffect.js.md) | Проверено |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../module/scripts/temporaryEffects/applyActiveEffect.js) | Применение и копирование ActiveEffect в Actor, маршруты целей и Queries. | [Описание](files/module/scripts/temporaryEffects/applyActiveEffect.js.md) | Проверено |
| [module/scripts/verbalCombat/verbalCombat.js](../../../module/scripts/verbalCombat/verbalCombat.js) | Не установлено | Не подготовлено | Не начат |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../module/scripts/verbalCombat/verbalCombatDefense.js) | Не установлено | Не подготовлено | Не начат |
| [module/setup/config.js](../../../module/setup/config.js) | Объект WITCHER: справочники, варианты действий, травмы и заготовки статусов | [Карточка](files/module/setup/config.js.md) | Проверено |
| [module/setup/deprecations.js](../../../module/setup/deprecations.js) | Экспортирует пустую функцию уведомлений deprecationWarnings; проверки устаревания не выполняет. | [Карточка](files/module/setup/deprecations.js.md) | Проверено |
| [module/setup/handlebars.js](../../../module/setup/handlebars.js) | Предзагружает 59 шаблонов и регистрирует 17 Handlebars helpers для листов и сообщений. | [Карточка](files/module/setup/handlebars.js.md) | Проверено |
| [module/setup/hooks.js](../../../module/setup/hooks.js) | Подключает updateCombat к обработке эффектов боя и отсчёту длительности регионов. | [Карточка](files/module/setup/hooks.js.md) | Проверено |
| [module/setup/queries.js](../../../module/setup/queries.js) | Регистрирует два запроса Foundry User.query для эффектов и разрешённых методов документов. | [Карточка](files/module/setup/queries.js.md) | Проверено |
| [module/setup/registerDataModels.js](../../../module/setup/registerDataModels.js) | Регистрирует модели данных Actor, Item, ActiveEffect и ChatMessage и класс документа сообщения чата. | [Карточка](files/module/setup/registerDataModels.js.md) | Проверено |
| [module/setup/registerSheets.js](../../../module/setup/registerSheets.js) | Регистрирует общие и специализированные листы Actor/Item и заменяет стандартный редактор ActiveEffect. | [Карточка](files/module/setup/registerSheets.js.md) | Проверено |
| [module/setup/settings.js](../../../module/setup/settings.js) | Регистрирует девять мировых настроек и формирует варианты выбора Item-компедиума травм. | [Карточка](files/module/setup/settings.js.md) | Проверено |
| [module/setup/socketHook.js](../../../module/setup/socketHook.js) | Принимает сообщения системного сокета на активном GM и вызывает addItem или restoreReliability по UUID. | [Карточка](files/module/setup/socketHook.js.md) | Проверено |
| [package.json](../../../package.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Dwarf___Gnome_Profession_TjKh0NMxyyYxjSDt.json](../../../packsJson/character-generator-sub-tables/Dwarf___Gnome_Profession_TjKh0NMxyyYxjSDt.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Elf_Profession_zEykV0pe3YUlaDTd.json](../../../packsJson/character-generator-sub-tables/Elf_Profession_zEykV0pe3YUlaDTd.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Family_Fate__Elderland_W6mgmCP3219eYdf0.json](../../../packsJson/character-generator-sub-tables/Family_Fate__Elderland_W6mgmCP3219eYdf0.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Family_Fate__Nilfgaard_VstrJuRw43OKcuGr.json](../../../packsJson/character-generator-sub-tables/Family_Fate__Nilfgaard_VstrJuRw43OKcuGr.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Family_Status__Elderland_GOp8mGE4MiGaqjk2.json](../../../packsJson/character-generator-sub-tables/Family_Status__Elderland_GOp8mGE4MiGaqjk2.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Family_Status__Nilfgaard_6WXA7KAOHjeqCCRn.json](../../../packsJson/character-generator-sub-tables/Family_Status__Nilfgaard_6WXA7KAOHjeqCCRn.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Family_Status__Northern_EeOlp8UMRiYS1AEt.json](../../../packsJson/character-generator-sub-tables/Family_Status__Northern_EeOlp8UMRiYS1AEt.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json](../../../packsJson/character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json](../../../packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Family_and_Parents__Northern_xAVQucslVR12q2kc.json](../../../packsJson/character-generator-sub-tables/Family_and_Parents__Northern_xAVQucslVR12q2kc.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Human_Profession_ZSSaEVLn53BVQ77b.json](../../../packsJson/character-generator-sub-tables/Human_Profession_ZSSaEVLn53BVQ77b.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Most_Influential_Friend__Elderland_eATe1gk2PaKG1K9r.json](../../../packsJson/character-generator-sub-tables/Most_Influential_Friend__Elderland_eATe1gk2PaKG1K9r.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json](../../../packsJson/character-generator-sub-tables/Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json](../../../packsJson/character-generator-sub-tables/Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Nilfgaard_Vassal_Origin_IEPMPHNGahrfyCWI.json](../../../packsJson/character-generator-sub-tables/Nilfgaard_Vassal_Origin_IEPMPHNGahrfyCWI.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Origin__Elderland_f17QrlT4P5u8m65o.json](../../../packsJson/character-generator-sub-tables/Origin__Elderland_f17QrlT4P5u8m65o.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Origin__Human_Lands_de64KicDG5R7FFO9.json](../../../packsJson/character-generator-sub-tables/Origin__Human_Lands_de64KicDG5R7FFO9.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Origin__Nilfgaard_DAfZ8BGKmclyyFYc.json](../../../packsJson/character-generator-sub-tables/Origin__Nilfgaard_DAfZ8BGKmclyyFYc.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Origin__Northern_Kingdom_u0EwVGZtkHA4Knoa.json](../../../packsJson/character-generator-sub-tables/Origin__Northern_Kingdom_u0EwVGZtkHA4Knoa.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Parental_Fate__Elderland_jZVPaCIoQxFZiyRu.json](../../../packsJson/character-generator-sub-tables/Parental_Fate__Elderland_jZVPaCIoQxFZiyRu.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Parents__Elderland_zSTMrICDELIRaNyL.json](../../../packsJson/character-generator-sub-tables/Parents__Elderland_zSTMrICDELIRaNyL.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Parents__Nilfgaard_Nnf1BMSJOnc5Mx3m.json](../../../packsJson/character-generator-sub-tables/Parents__Nilfgaard_Nnf1BMSJOnc5Mx3m.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Parents__Northern_SGuXziIZzzst1LVJ.json](../../../packsJson/character-generator-sub-tables/Parents__Northern_SGuXziIZzzst1LVJ.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Siblings__Age_0PcW1kFO5g40cELc.json](../../../packsJson/character-generator-sub-tables/Siblings__Age_0PcW1kFO5g40cELc.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Siblings__Dwarves_Halflings_Ty1Hs3G4BXkkTu67.json](../../../packsJson/character-generator-sub-tables/Siblings__Dwarves_Halflings_Ty1Hs3G4BXkkTu67.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Siblings__Elves_6QuZTatyIKElcCKz.json](../../../packsJson/character-generator-sub-tables/Siblings__Elves_6QuZTatyIKElcCKz.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Siblings__Feelings_About_You_ACf1JfCfVtJWw5DG.json](../../../packsJson/character-generator-sub-tables/Siblings__Feelings_About_You_ACf1JfCfVtJWw5DG.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Siblings__Gender_QbkrG0W11fREICK8.json](../../../packsJson/character-generator-sub-tables/Siblings__Gender_QbkrG0W11fREICK8.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Siblings__Nilfgaard_Vw40FuwmhTGp7Q4V.json](../../../packsJson/character-generator-sub-tables/Siblings__Nilfgaard_Vw40FuwmhTGp7Q4V.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Siblings__Northern_rLxCo0JWiGvTlapE.json](../../../packsJson/character-generator-sub-tables/Siblings__Northern_rLxCo0JWiGvTlapE.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Siblings__Personality_zNQCbwyK1biYFszn.json](../../../packsJson/character-generator-sub-tables/Siblings__Personality_zNQCbwyK1biYFszn.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator-sub-tables/Which_Parent_7fAXpaJLFwlWxkWX.json](../../../packsJson/character-generator-sub-tables/Which_Parent_7fAXpaJLFwlWxkWX.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Background_Generator__Dwarves_PCAssN2Ms7yLzuCv.json](../../../packsJson/character-generator/Background_Generator__Dwarves_PCAssN2Ms7yLzuCv.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Background_Generator__Elves_L8o8Rz85um05VUW4.json](../../../packsJson/character-generator/Background_Generator__Elves_L8o8Rz85um05VUW4.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Background_Generator__Halfling_ioZTpiW6W2eVwRiY.json](../../../packsJson/character-generator/Background_Generator__Halfling_ioZTpiW6W2eVwRiY.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json](../../../packsJson/character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Background_Generator__RandomCharacter_CIpykDUYYuJB0zLv.json](../../../packsJson/character-generator/Background_Generator__RandomCharacter_CIpykDUYYuJB0zLv.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Life_Event_Generator_4Y8IpS3ArbbP2gGc.json](../../../packsJson/character-generator/Life_Event_Generator_4Y8IpS3ArbbP2gGc.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Siblings_Generator_Lem0B3XxmJeEVQms.json](../../../packsJson/character-generator/Siblings_Generator_Lem0B3XxmJeEVQms.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Style_and_Values_CjaIcLRWSlzwI6ly.json](../../../packsJson/character-generator/Style_and_Values_CjaIcLRWSlzwI6ly.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Witcher_Background_Generator_C5d6zkIMvS9gDWEN.json](../../../packsJson/character-generator/Witcher_Background_Generator_C5d6zkIMvS9gDWEN.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Witcher_Lifepath__Cautious_Decade_09MXduRik0BKuUqa.json](../../../packsJson/character-generator/Witcher_Lifepath__Cautious_Decade_09MXduRik0BKuUqa.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Witcher_Lifepath__Non_Neutral_Decade_obLsbuoNixBUbeAy.json](../../../packsJson/character-generator/Witcher_Lifepath__Non_Neutral_Decade_obLsbuoNixBUbeAy.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Witcher_Lifepath__Normal_Decade_dsvsdl2GfKCWKsEO.json](../../../packsJson/character-generator/Witcher_Lifepath__Normal_Decade_dsvsdl2GfKCWKsEO.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/character-generator/Witcher_Lifepath__Risky_Decade_6zn78Gj7lZtJfS90.json](../../../packsJson/character-generator/Witcher_Lifepath__Risky_Decade_6zn78Gj7lZtJfS90.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Complex_Critical_p3EAPCnu8RDawpWR.json](../../../packsJson/combat/Complex_Critical_p3EAPCnu8RDawpWR.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Deadly_Critical_GoXapMH54rEUWaZn.json](../../../packsJson/combat/Deadly_Critical_GoXapMH54rEUWaZn.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Difficult_Critical_VIup1SZTMKCSGGbT.json](../../../packsJson/combat/Difficult_Critical_VIup1SZTMKCSGGbT.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Human_Damage_Location_jKFIdFvv4P49JXPU.json](../../../packsJson/combat/Human_Damage_Location_jKFIdFvv4P49JXPU.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Monster_Damage_Location_KYyK6F8JHhA3hOu7.json](../../../packsJson/combat/Monster_Damage_Location_KYyK6F8JHhA3hOu7.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Mounted_Control_Loss_VVb2zLR4NLdMLVQQ.json](../../../packsJson/combat/Mounted_Control_Loss_VVb2zLR4NLdMLVQQ.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Mounted_Control_Loss__Mount_XRdHZOmutZ3yzGRe.json](../../../packsJson/combat/Mounted_Control_Loss__Mount_XRdHZOmutZ3yzGRe.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Mounted_Control_Loss__Personal_KWLoKiOHKXXnq5E4.json](../../../packsJson/combat/Mounted_Control_Loss__Personal_KWLoKiOHKXXnq5E4.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Scatter__Direction_and_Distance_qTOHZYKhe5GN3Ciw.json](../../../packsJson/combat/Scatter__Direction_and_Distance_qTOHZYKhe5GN3Ciw.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Simple_Critical_SkHR3GrB2e3Tz1v4.json](../../../packsJson/combat/Simple_Critical_SkHR3GrB2e3Tz1v4.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/combat/Vehicle_Control_Loss_zO7eKgtDOAH0qnow.json](../../../packsJson/combat/Vehicle_Control_Loss_zO7eKgtDOAH0qnow.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs_VfgJzcV75cGqsjuF.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs_VfgJzcV75cGqsjuF.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Stabilized__4LmC6nGwRM0PpNl7.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Stabilized__4LmC6nGwRM0PpNl7.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Treated__77evBMjaJOlKTaRv.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Treated__77evBMjaJOlKTaRv.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Left__Z2L7diKDSE9L7E9d.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Left__Z2L7diKDSE9L7E9d.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Left___Stabilized__eCiJjDqfUyaXCW2z.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Left___Stabilized__eCiJjDqfUyaXCW2z.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Left___Treated__kPIkW1AXuybKZPEh.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Left___Treated__kPIkW1AXuybKZPEh.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Right__ZOyO6WlnMTDjzBj9.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Right__ZOyO6WlnMTDjzBj9.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Right___Stabilized__t9bcLB3zDGUX9Uuq.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Right___Stabilized__t9bcLB3zDGUX9Uuq.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Right___Treated__djnBTcYyGVsykdoy.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Arm__Right___Treated__djnBTcYyGVsykdoy.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Stabilized__LF0C1HVgY4hNZOFE.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Stabilized__LF0C1HVgY4hNZOFE.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Treated__nM9wqZXmrkFRRGTW.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Treated__nM9wqZXmrkFRRGTW.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left__r34NuXwHfPGZCpTu.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left__r34NuXwHfPGZCpTu.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right__yI6kHQM8voHrBF2h.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right__yI6kHQM8voHrBF2h.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth_IMLpjhiZ0yg6hjKI.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth_IMLpjhiZ0yg6hjKI.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Stabilized__wccN560fe7WQgT0N.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Stabilized__wccN560fe7WQgT0N.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Treated__yHU7iYTocbAok2wH.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Treated__yHU7iYTocbAok2wH.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Treated__KsYEWWO5KlPHSdCy.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Treated__KsYEWWO5KlPHSdCy.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen__Stabilized__d8uhnIErEmsGtf94.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen__Stabilized__d8uhnIErEmsGtf94.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen__Treated__kFcie7Io28kKittg.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen__Treated__kFcie7Io28kKittg.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen_rHrrGeB9A8bNCiC2.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Ruptured_Spleen_rHrrGeB9A8bNCiC2.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/_Folder.json](../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/_Folder.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Stabilized__LNy3P3HUw2Ja9DNu.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Stabilized__LNy3P3HUw2Ja9DNu.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Treated__XQeXSAhvjrQZNpAE.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Treated__XQeXSAhvjrQZNpAE.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left__KQZRzczsSx1XY63m.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left__KQZRzczsSx1XY63m.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left___Stabilized__vmRDG8kxeCu3sYQC.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left___Stabilized__vmRDG8kxeCu3sYQC.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left___Treated__8Z1iHJLXrFm2i3Fb.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left___Treated__8Z1iHJLXrFm2i3Fb.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right__ZxvWPJPDD9fm34Pc.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right__ZxvWPJPDD9fm34Pc.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right___Stabilized__hKgvgj4lJ74wPt8N.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right___Stabilized__hKgvgj4lJ74wPt8N.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right___Treated__gPeOdwZ0OTVF9E3w.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right___Treated__gPeOdwZ0OTVF9E3w.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Stabilized__lck0EEySmuLZXMrA.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Stabilized__lck0EEySmuLZXMrA.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Treated__eYEp1CPif98mDm2U.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Treated__eYEp1CPif98mDm2U.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Stabilized__vYza9bpK13G36YRV.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Stabilized__vYza9bpK13G36YRV.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Treated__KFbDbrS3OCs0C1h4.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Treated__KFbDbrS3OCs0C1h4.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Separated_Spine_Decapitated_MvrwnSrEqsTRdaeY.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Separated_Spine_Decapitated_MvrwnSrEqsTRdaeY.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Stabilized__LM6Kkh0ib6ux4WQp.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Stabilized__LM6Kkh0ib6ux4WQp.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Treated__vkr5MXhnalPp8yJJ.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Treated__vkr5MXhnalPp8yJJ.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/_Folder.json](../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/_Folder.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Stabilized__tdcGSOZGCUhNArDc.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Stabilized__tdcGSOZGCUhNArDc.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left__saPd4IMUCv5qZE60.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left__saPd4IMUCv5qZE60.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Stabilized__NHNctAuhsapGZXiP.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Stabilized__NHNctAuhsapGZXiP.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Treated__ujz1IMKCXoJF9w91.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Treated__ujz1IMKCXoJF9w91.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right__c3H8Xx7WYCcM37k6.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right__c3H8Xx7WYCcM37k6.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Stabilized__NiGtzaHs4dUj8Pmd.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Stabilized__NiGtzaHs4dUj8Pmd.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Treated__kfyfxEVsMRUDDk1A.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Treated__kfyfxEVsMRUDDk1A.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion_IK7pM8p3NcM4thcz.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion_IK7pM8p3NcM4thcz.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Stabilized__AFkm8KjxkwYxOCQo.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Stabilized__AFkm8KjxkwYxOCQo.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Treated__ItXAMwWil2A7IqRv.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Treated__ItXAMwWil2A7IqRv.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture_UImIh794nOy21jg2.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture_UImIh794nOy21jg2.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture__Stabilized__ikv3qioEgGJG6Olw.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture__Stabilized__ikv3qioEgGJG6Olw.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture__Treated__v4RVIshohh1PPuAu.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture__Treated__v4RVIshohh1PPuAu.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Stabilized__cfQ2OHPNVVKMDsDo.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Stabilized__cfQ2OHPNVVKMDsDo.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Treated__wFul3Zr7mMaKjA5I.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Treated__wFul3Zr7mMaKjA5I.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound_tiVrEesPSzZ64HpZ.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound_tiVrEesPSzZ64HpZ.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Stabilized__EpF0FD1nFXJTJ5Tj.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Stabilized__EpF0FD1nFXJTJ5Tj.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Treated__Mg1jn99OitVPdvje.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Treated__Mg1jn99OitVPdvje.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/_Folder.json](../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/_Folder.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw_UnWBI9Sgu4AJv1z1.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw_UnWBI9Sgu4AJv1z1.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Stabilized__h15wRehQQoIkxcf0.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Stabilized__h15wRehQQoIkxcf0.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Treated__AODuTRNu2RtJJhLD.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Treated__AODuTRNu2RtJJhLD.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs_7TzGQ2y4yZnG01im.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs_7TzGQ2y4yZnG01im.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Stabilized__2c4PbGjd0segbvmr.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Stabilized__2c4PbGjd0segbvmr.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Treated__oe4y6zxH2WUR9gSj.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Treated__oe4y6zxH2WUR9gSj.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar_8tqapNHVCmSwijJw.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar_8tqapNHVCmSwijJw.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Stabilized__AJeuZeFF29nEI5fc.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Stabilized__AJeuZeFF29nEI5fc.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Treated__kbeASc2PnnkYc5SR.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Treated__kbeASc2PnnkYc5SR.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Stabilized__fnYssldrMLVqbF22.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Stabilized__fnYssldrMLVqbF22.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Treated__rgRGVfLBlHMwUvGy.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object__Treated__rgRGVfLBlHMwUvGy.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object_mylVzp10NMor44XR.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Foreign_Object_mylVzp10NMor44XR.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left___Stabilized__01Seyu22NaDnctCi.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left___Stabilized__01Seyu22NaDnctCi.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left___Treated__q5vr9VLD2tEkL1ux.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left___Treated__q5vr9VLD2tEkL1ux.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left__quAixM7zp2bD9lXz.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left__quAixM7zp2bD9lXz.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right___Stabilized__yGy3oWvmpX6WMm56.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right___Stabilized__yGy3oWvmpX6WMm56.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right___Treated__YiusbDXfFDhqwtQT.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right___Treated__YiusbDXfFDhqwtQT.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right__umPVfrJeNU65S48O.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right__umPVfrJeNU65S48O.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left__XPoH413WkKQUgrnw.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left__XPoH413WkKQUgrnw.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right__VhwzsUlv5csYSJTM.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right__VhwzsUlv5csYSJTM.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Stabilized__fNiSVOJzpaxVvZTE.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Stabilized__fNiSVOJzpaxVvZTE.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Treated__8qatuNeEROueRDcZ.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Treated__8qatuNeEROueRDcZ.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Allies__Closeness_IswiqefPmaHECa5X.json](../../../packsJson/lifepath/Allies__Closeness_IswiqefPmaHECa5X.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Allies__Gender_QFHhoiXtIBYkL8Rd.json](../../../packsJson/lifepath/Allies__Gender_QFHhoiXtIBYkL8Rd.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Allies__Generator_Va7NF10ETcMvndFo.json](../../../packsJson/lifepath/Allies__Generator_Va7NF10ETcMvndFo.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Allies__How_You_Met_BqAizN8u9r6nMSyK.json](../../../packsJson/lifepath/Allies__How_You_Met_BqAizN8u9r6nMSyK.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Allies__Position_5sroduMneFqG9INx.json](../../../packsJson/lifepath/Allies__Position_5sroduMneFqG9INx.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Allies__Where_Are_They__W19e7rtl3ycrMhQU.json](../../../packsJson/lifepath/Allies__Where_Are_They__W19e7rtl3ycrMhQU.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json](../../../packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Enemies__Gender_FMondgMHlPLSy3cq.json](../../../packsJson/lifepath/Enemies__Gender_FMondgMHlPLSy3cq.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Enemies__Generator_7AXmeCSRkK3ktJ9Y.json](../../../packsJson/lifepath/Enemies__Generator_7AXmeCSRkK3ktJ9Y.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Enemies__How_Far_Has_It_Escalated__BLiqJBssahtqPqVf.json](../../../packsJson/lifepath/Enemies__How_Far_Has_It_Escalated__BLiqJBssahtqPqVf.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Enemies__Position_WeN4QhEHL468Ushx.json](../../../packsJson/lifepath/Enemies__Position_WeN4QhEHL468Ushx.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Enemies__Power_9mYMTKkCuU2ElJdx.json](../../../packsJson/lifepath/Enemies__Power_9mYMTKkCuU2ElJdx.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Enemies__The_Cause_U9R1ct2xP13y6R7j.json](../../../packsJson/lifepath/Enemies__The_Cause_U9R1ct2xP13y6R7j.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Enemies__What_Is_Their_Power__sH1XIFHObBFdbjTI.json](../../../packsJson/lifepath/Enemies__What_Is_Their_Power__sH1XIFHObBFdbjTI.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Enemies__Who_Was_Wronged_cz5KlvgE7I7QV57H.json](../../../packsJson/lifepath/Enemies__Who_Was_Wronged_cz5KlvgE7I7QV57H.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Fortune_Z0eeWQI3R8v4YNLd.json](../../../packsJson/lifepath/Fortune_Z0eeWQI3R8v4YNLd.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Fortune_or_Misfortune_qKwYD3GHlGxCmiir.json](../../../packsJson/lifepath/Fortune_or_Misfortune_qKwYD3GHlGxCmiir.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Misfortune_JNbvihde5EGIFPdB.json](../../../packsJson/lifepath/Misfortune_JNbvihde5EGIFPdB.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Romance_CDgdx129wZvINn16.json](../../../packsJson/lifepath/Romance_CDgdx129wZvINn16.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Romance__Problematic_Love_l7k0hSL3iRzjJcYs.json](../../../packsJson/lifepath/Romance__Problematic_Love_l7k0hSL3iRzjJcYs.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/lifepath/Romance__Romantic_Tragedy_Jmvpwp9FRwRhDWZu.json](../../../packsJson/lifepath/Romance__Romantic_Tragedy_Jmvpwp9FRwRhDWZu.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/style/Style__Affectations_4RWDMDzNdnz2kgwU.json](../../../packsJson/style/Style__Affectations_4RWDMDzNdnz2kgwU.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/style/Style__Clothing_BuyEb4FcAyQL2hov.json](../../../packsJson/style/Style__Clothing_BuyEb4FcAyQL2hov.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/style/Style__Hair_Style_Ov9xIpAdWEPZCIoH.json](../../../packsJson/style/Style__Hair_Style_Ov9xIpAdWEPZCIoH.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/style/Style__Personality_TOQz3ETDronoeEDt.json](../../../packsJson/style/Style__Personality_TOQz3ETDronoeEDt.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/style/Values__Feelings_on_People_4eCXMVEfRx4PivWH.json](../../../packsJson/style/Values__Feelings_on_People_4eCXMVEfRx4PivWH.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/style/Values__Ideals_s5EjP50ddIVoitHT.json](../../../packsJson/style/Values__Ideals_s5EjP50ddIVoitHT.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/style/Values__Valued_Person_y1WCi6n2Kpwqb27P.json](../../../packsJson/style/Values__Valued_Person_y1WCi6n2Kpwqb27P.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_A7jt3mfuFTEQiXRv.json](../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_A7jt3mfuFTEQiXRv.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_G9iWzbiGQloX7sls.json](../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_G9iWzbiGQloX7sls.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go__u2n9HR4RhSt1QV3l.json](../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go__u2n9HR4RhSt1QV3l.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json](../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json](../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json](../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json](../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json](../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json](../../../packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json](../../../packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Are_They_Alive__2l9nl4ndvdgtn2SJ.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Are_They_Alive__2l9nl4ndvdgtn2SJ.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Closeness_TLO7kA1RyxfxP2D8.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Closeness_TLO7kA1RyxfxP2D8.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Gender_bw2dbovLaFTJJ8EP.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Gender_bw2dbovLaFTJJ8EP.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Generator_47kWQhpq3yeAG74c.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Generator_47kWQhpq3yeAG74c.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_You_Met_pr3upjAFiZVHdOXp.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_You_Met_pr3upjAFiZVHdOXp.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Position_zG6aQ2srMV79PDHY.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Position_zG6aQ2srMV79PDHY.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Where_Are_They__LPwYvTqPg52QQ9IU.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Where_Are_They__LPwYvTqPg52QQ9IU.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Benefit_Outcome_snt4khwSoq2rdeZa.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Benefit_Outcome_snt4khwSoq2rdeZa.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Cautious_Outcome_jhPNDSApv5lQlUk3.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Cautious_Outcome_jhPNDSApv5lQlUk3.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies_Generator_iwGZ1Sj0v9iBqvSk.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies_Generator_iwGZ1Sj0v9iBqvSk.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Are_They_Alive__eywzppppagpC4HYO.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Are_They_Alive__eywzppppagpC4HYO.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__How_Did_They_Die__SwPXh5SRHrwfXyWP.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__How_Did_They_Die__SwPXh5SRHrwfXyWP.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__How_Far_Has_It_Escalated__8iZB8b98GEbOQfBQ.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__How_Far_Has_It_Escalated__8iZB8b98GEbOQfBQ.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Position_9m5zE1WyAI4xslyk.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Position_9m5zE1WyAI4xslyk.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Power_1QUG4e60Iqom24ac.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__Power_1QUG4e60Iqom24ac.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__The_Cause_FR7XLvWHdkOwUtnC.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__The_Cause_FR7XLvWHdkOwUtnC.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__What_Is_Their_Power__xxaxFJfMA29gLFOm.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Enemies__What_Is_Their_Power__xxaxFJfMA29gLFOm.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Events_zVS3tsoiyTdjwU7i.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Events_zVS3tsoiyTdjwU7i.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Wounds_q2Cdg3rDUsu3xYLd.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Danger___Wounds_q2Cdg3rDUsu3xYLd.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Dangers_QDAhRAIL7LNz9gME.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Dangers_QDAhRAIL7LNz9gME.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Hunt_Generator_vTIEP2TnU2n4hwY3.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt_Generator_vTIEP2TnU2n4hwY3.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___How_Did_It_End__n13vBwJk61euGPa1.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___How_Did_It_End__n13vBwJk61euGPa1.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___Was_There_a_Twist__uLX85Bx2Jimqmx6o.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___Was_There_a_Twist__uLX85Bx2Jimqmx6o.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___What_Was_the_Prey__ZozZLNSgKpwEltsY.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___What_Was_the_Prey__ZozZLNSgKpwEltsY.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___What_Was_the_Twist__ZyRLAmxDu5SVt7rg.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___What_Was_the_Twist__ZyRLAmxDu5SVt7rg.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___Where_Was_the_Prey__PUVAGxwjXlFhXrhv.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Hunt___Where_Was_the_Prey__PUVAGxwjXlFhXrhv.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Non_Neutral_Outcome_sARR2vzegIiAh3uU.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Non_Neutral_Outcome_sARR2vzegIiAh3uU.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Normal_Outcome_Lu49KrUT3wDY1bJr.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Normal_Outcome_Lu49KrUT3wDY1bJr.json) | Не установлено | Не подготовлено | Не начат |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Risky_Outcome_R6BzlpXysvPx6O5c.json](../../../packsJson/witcher-lifepath/Witcher_Lifepath__Risky_Outcome_R6BzlpXysvPx6O5c.json) | Не установлено | Не подготовлено | Не начат |
| [styles/activeEffect.css](../../../styles/activeEffect.css) | Не установлено | Не подготовлено | Не начат |
| [styles/armor-sheet.css](../../../styles/armor-sheet.css) | Не установлено | Не подготовлено | Не начат |
| [styles/attack-sheet.css](../../../styles/attack-sheet.css) | Не установлено | Не подготовлено | Не начат |
| [styles/character-header.css](../../../styles/character-header.css) | Не установлено | Не подготовлено | Не начат |
| [styles/character/sheet.css](../../../styles/character/sheet.css) | Не установлено | Не подготовлено | Не начат |
| [styles/character/tab-profession.css](../../../styles/character/tab-profession.css) | Не установлено | Не подготовлено | Не начат |
| [styles/chat.css](../../../styles/chat.css) | Не установлено | Не подготовлено | Не начат |
| [styles/components-list.css](../../../styles/components-list.css) | Не установлено | Не подготовлено | Не начат |
| [styles/configurations/modifier-configuration.css](../../../styles/configurations/modifier-configuration.css) | Не установлено | Не подготовлено | Не начат |
| [styles/container-sheet.css](../../../styles/container-sheet.css) | Не установлено | Не подготовлено | Не начат |
| [styles/crit-wounds-table.css](../../../styles/crit-wounds-table.css) | Не установлено | Не подготовлено | Не начат |
| [styles/currency-converter.css](../../../styles/currency-converter.css) | Не установлено | Не подготовлено | Не начат |
| [styles/dialog.css](../../../styles/dialog.css) | Не установлено | Не подготовлено | Не начат |
| [styles/item-header.css](../../../styles/item-header.css) | Не установлено | Не подготовлено | Не начат |
| [styles/item-sheets.css](../../../styles/item-sheets.css) | Не установлено | Не подготовлено | Не начат |
| [styles/loot-sheet.css](../../../styles/loot-sheet.css) | Не установлено | Не подготовлено | Не начат |
| [styles/monster-sheet.css](../../../styles/monster-sheet.css) | Не установлено | Не подготовлено | Не начат |
| [styles/monster-skill-tab.css](../../../styles/monster-skill-tab.css) | Не установлено | Не подготовлено | Не начат |
| [styles/monster/details.css](../../../styles/monster/details.css) | Не установлено | Не подготовлено | Не начат |
| [styles/monster/header.css](../../../styles/monster/header.css) | Не установлено | Не подготовлено | Не начат |
| [styles/monster/inventory.css](../../../styles/monster/inventory.css) | Не установлено | Не подготовлено | Не начат |
| [styles/monster/sheet.css](../../../styles/monster/sheet.css) | Не установлено | Не подготовлено | Не начат |
| [styles/monster/sidebar.css](../../../styles/monster/sidebar.css) | Не установлено | Не подготовлено | Не начат |
| [styles/profession-sheet.css](../../../styles/profession-sheet.css) | Не установлено | Не подготовлено | Не начат |
| [styles/race-sheet.css](../../../styles/race-sheet.css) | Не установлено | Не подготовлено | Не начат |
| [styles/repair.css](../../../styles/repair.css) | Не установлено | Не подготовлено | Не начат |
| [styles/rewards.css](../../../styles/rewards.css) | Не установлено | Не подготовлено | Не начат |
| [styles/special-skill-table.css](../../../styles/special-skill-table.css) | Не установлено | Не подготовлено | Не начат |
| [styles/substances.css](../../../styles/substances.css) | Не установлено | Не подготовлено | Не начат |
| [styles/system-styles.css](../../../styles/system-styles.css) | Не установлено | Не подготовлено | Не начат |
| [styles/tab-background.css](../../../styles/tab-background.css) | Не установлено | Не подготовлено | Не начат |
| [styles/tab-inventory-list.css](../../../styles/tab-inventory-list.css) | Не установлено | Не подготовлено | Не начат |
| [styles/tab-inventory.css](../../../styles/tab-inventory.css) | Не установлено | Не подготовлено | Не начат |
| [styles/tab-skills.css](../../../styles/tab-skills.css) | Не установлено | Не подготовлено | Не начат |
| [styles/weapon-roll.css](../../../styles/weapon-roll.css) | Не установлено | Не подготовлено | Не начат |
| [styles/witcher-styles.css](../../../styles/witcher-styles.css) | Не установлено | Не подготовлено | Не начат |
| [system.json](../../../system.json) | Манифест пакета: ресурсы, компедиумы, локализации и подтипы документов | [Карточка](files/system.json.md) | Проверено |
| [templates/chat/combat/defense/defense.hbs](../../../templates/chat/combat/defense/defense.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/combat/defense/defenseCrit.hbs](../../../templates/chat/combat/defense/defenseCrit.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/combat/defense/defenseStun.hbs](../../../templates/chat/combat/defense/defenseStun.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/combat/heal.hbs](../../../templates/chat/combat/heal.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/combat/regeneration.hbs](../../../templates/chat/combat/regeneration.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/combat/spellItem.hbs](../../../templates/chat/combat/spellItem.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/combat/statusEffect.hbs](../../../templates/chat/combat/statusEffect.hbs) | Уведомление об обработке воздействия из turnStartEffects. | [Описание](files/templates/chat/combat/statusEffect.hbs.md) | Проверено |
| [templates/chat/currency-conversion.hbs](../../../templates/chat/currency-conversion.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/damage/damageToAllLocations.hbs](../../../templates/chat/damage/damageToAllLocations.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/damage/damageToLocation.hbs](../../../templates/chat/damage/damageToLocation.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/damage/shieldAbsorbs.hbs](../../../templates/chat/damage/shieldAbsorbs.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/damage/spAbsorbs.hbs](../../../templates/chat/damage/spAbsorbs.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/heal/resting-status.hbs](../../../templates/chat/heal/resting-status.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/item/appliedTemporaryItemImprovements.hbs](../../../templates/chat/item/appliedTemporaryItemImprovements.hbs) | Сообщение со списком временных улучшений выбранного оружия. | [Описание](files/templates/chat/item/appliedTemporaryItemImprovements.hbs.md) | Проверено |
| [templates/chat/item/consume.hbs](../../../templates/chat/item/consume.hbs) | Шаблон сообщения о лечении и добавляемых статусах при расходовании. | [Описание](files/templates/chat/item/consume.hbs.md) | Проверено |
| [templates/chat/item/dismantle.hbs](../../../templates/chat/item/dismantle.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/item/item-description.hbs](../../../templates/chat/item/item-description.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/item/partials/item-description/alchemicals.hbs](../../../templates/chat/item/partials/item-description/alchemicals.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/item/partials/item-description/crafting-items.hbs](../../../templates/chat/item/partials/item-description/crafting-items.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/item/partials/item-description/description.hbs](../../../templates/chat/item/partials/item-description/description.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/item/partials/item-description/spell-description.hbs](../../../templates/chat/item/partials/item-description/spell-description.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/item/partials/item-description/tags.hbs](../../../templates/chat/item/partials/item-description/tags.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/item/repair.hbs](../../../templates/chat/item/repair.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/chat/rewards.hbs](../../../templates/chat/rewards.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/activeEffects/wizard.hbs](../../../templates/dialog/activeEffects/wizard.hbs) | Выбор пути или группы путей в диалоге мастера/навыка. | [Описание](files/templates/dialog/activeEffects/wizard.hbs.md) | Проверено |
| [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/combat/spell-attack.hbs](../../../templates/dialog/combat/spell-attack.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/combat/variableDamage.hbs](../../../templates/dialog/combat/variableDamage.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/combat/weapon-attack.hbs](../../../templates/dialog/combat/weapon-attack.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/deprecations/lifepathModifiers.hbs](../../../templates/dialog/deprecations/lifepathModifiers.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/deprecations/statSkillModifiers.hbs](../../../templates/dialog/deprecations/statSkillModifiers.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/heal/heal-rest.hbs](../../../templates/dialog/heal/heal-rest.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/investigation/chooseEvidenceSkill.hbs](../../../templates/dialog/investigation/chooseEvidenceSkill.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/repair-dialog.hbs](../../../templates/dialog/repair-dialog.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/verbal-combat-defense.hbs](../../../templates/dialog/verbal-combat-defense.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/dialog/verbal-combat.hbs](../../../templates/dialog/verbal-combat.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/associated-diagram.hbs](../../../templates/partials/associated-diagram.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/associated-item.hbs](../../../templates/partials/associated-item.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/character-header.hbs](../../../templates/partials/character-header.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/character/custom-skill-display.hbs](../../../templates/partials/character/custom-skill-display.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/character/skill-display.hbs](../../../templates/partials/character/skill-display.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/character/substances.hbs](../../../templates/partials/character/substances.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/character/tab-background.hbs](../../../templates/partials/character/tab-background.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/character/tab-magic.hbs](../../../templates/partials/character/tab-magic.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/character/tab-skills.hbs](../../../templates/partials/character/tab-skills.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/character/tab-stats.hbs](../../../templates/partials/character/tab-stats.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/components-list.hbs](../../../templates/partials/components-list.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/crit-wounds-table.hbs](../../../templates/partials/crit-wounds-table.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/effect-part.hbs](../../../templates/partials/effect-part.hbs) | Общий список эффектов с источниками, длительностью, описаниями и действиями. | [Описание](files/templates/partials/effect-part.hbs.md) | Проверено |
| [templates/partials/item-header.hbs](../../../templates/partials/item-header.hbs) | Общая шапка предметных форм: имя, картинка, количество, вес, цена/тип и источник. | [Описание](files/templates/partials/item-header.hbs.md) | Проверено |
| [templates/partials/item-image.hbs](../../../templates/partials/item-image.hbs) | Картинка списка предметов с условной кнопкой увеличения; потребитель — прежний инвентарь монстра. | [Описание](files/templates/partials/item-image.hbs.md) | Проверено |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../templates/partials/monster/monster-custom-skill-display.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/monster/monster-details-tab.hbs](../../../templates/partials/monster/monster-details-tab.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../templates/partials/monster/monster-inventory-tab.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/monster/monster-skill-display.hbs](../../../templates/partials/monster/monster-skill-display.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/monster/monster-skill-tab.hbs](../../../templates/partials/monster/monster-skill-tab.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/monster/monster-spell-tab.hbs](../../../templates/partials/monster/monster-spell-tab.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/partials/spell-header.hbs](../../../templates/partials/spell-header.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/activeEffect/system-specific.hbs](../../../templates/sheets/activeEffect/system-specific.hbs) | Системные флаги фазы и условий применения ActiveEffect. | [Описание](files/templates/sheets/activeEffect/system-specific.hbs.md) | Проверено |
| [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/configuration/monster/general.hbs](../../../templates/sheets/actor/configuration/monster/general.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/configuration/monster/header.hbs](../../../templates/sheets/actor/configuration/monster/header.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/loot-sheet.hbs](../../../templates/sheets/actor/loot-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/monster-sheet.hbs](../../../templates/sheets/actor/monster-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../templates/sheets/actor/partials/character/sidebar.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/character/tab-effects.hbs](../../../templates/sheets/actor/partials/character/tab-effects.hbs) | Вкладка травм, лечения и активных эффектов персонажа/монстра. | [Описание](files/templates/sheets/actor/partials/character/tab-effects.hbs.md) | Проверено |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/monster/header.hbs](../../../templates/sheets/actor/partials/monster/header.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../templates/sheets/actor/partials/monster/sidebar.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/rewards/currency.hbs](../../../templates/sheets/actor/rewards/currency.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/rewards/header.hbs](../../../templates/sheets/actor/rewards/header.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/rewards/ip.hbs](../../../templates/sheets/actor/rewards/ip.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../templates/sheets/actor/tabs/tab-inventory.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/investigation/clue-sheet.hbs](../../../templates/sheets/investigation/clue-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../templates/sheets/investigation/mystery-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/investigation/obstacle-sheet.hbs](../../../templates/sheets/investigation/obstacle-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/investigation/partials/clue-display.hbs](../../../templates/sheets/investigation/partials/clue-display.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/investigation/partials/obstacle-display.hbs](../../../templates/sheets/investigation/partials/obstacle-display.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/alchemical-sheet.hbs](../../../templates/sheets/item/alchemical-sheet.hbs) | Основная форма категории, доступности, времени и описания алхимии. | [Описание](files/templates/sheets/item/alchemical-sheet.hbs.md) | Проверено |
| [templates/sheets/item/armor-sheet.hbs](../../../templates/sheets/item/armor-sheet.hbs) | Основная форма брони, щита, сопротивлений и предметных воздействий. | [Описание](files/templates/sheets/item/armor-sheet.hbs.md) | Проверено |
| [templates/sheets/item/component-sheet.hbs](../../../templates/sheets/item/component-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs) | Общий фрагмент выбора вариантов атаки и соответствующих навыков. | [Описание](files/templates/sheets/item/configuration/partials/attackOptionsPart.hbs.md) | Проверено |
| [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs) | Обёртка вкладки ActiveEffect Item с общим partial списка. | [Описание](files/templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs.md) | Проверено |
| [templates/sheets/item/configuration/tabs/armorGeneral.hbs](../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) | Общая конфигурация исходных SP и максимумов шести частей тела. | [Описание](files/templates/sheets/item/configuration/tabs/armorGeneral.hbs.md) | Проверено |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) | Вкладка расходования: лечение, добавление и снятие статусов. | [Описание](files/templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs.md) | Проверено |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) | Форма свойств урона, собственных воздействий и воздействий улучшений. | [Описание](files/templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs.md) | Проверено |
| [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs) | Форма применимости защиты, парирования и модификатора. | [Описание](files/templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs.md) | Проверено |
| [templates/sheets/item/configuration/tabs/general.hbs](../../../templates/sheets/item/configuration/tabs/general.hbs) | Условные поля вариантов атаки, навыков, бонусов, типа урона и защиты. | [Описание](files/templates/sheets/item/configuration/tabs/general.hbs.md) | Проверено |
| [templates/sheets/item/configuration/tabs/header.hbs](../../../templates/sheets/item/configuration/tabs/header.hbs) | Локализованный заголовок базовой конфигурации Item. | [Описание](files/templates/sheets/item/configuration/tabs/header.hbs.md) | Проверено |
| [templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs) | Региональная форма: запрошенный флаг и четыре ссылки на макросы. | [Описание](files/templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs.md) | Проверено |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/container-sheet.hbs](../../../templates/sheets/item/container-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../templates/sheets/item/criticalWound-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/diagrams-sheet.hbs](../../../templates/sheets/item/diagrams-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/enhancement-sheet.hbs](../../../templates/sheets/item/enhancement-sheet.hbs) | Форма категории улучшения, его физических бонусов и воздействий. | [Описание](files/templates/sheets/item/enhancement-sheet.hbs.md) | Проверено |
| [templates/sheets/item/hex-sheet.hbs](../../../templates/sheets/item/hex-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/homeland-sheet.hbs](../../../templates/sheets/item/homeland-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/mount-sheet.hbs](../../../templates/sheets/item/mount-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/mutagen-sheet.hbs](../../../templates/sheets/item/mutagen-sheet.hbs) | Основная форма источника, воздействия и малой мутации; общая шапка. | [Описание](files/templates/sheets/item/mutagen-sheet.hbs.md) | Проверено |
| [templates/sheets/item/note-sheet.hbs](../../../templates/sheets/item/note-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/profession-sheet.hbs](../../../templates/sheets/item/profession-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/race-sheet.hbs](../../../templates/sheets/item/race-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/ritual-sheet.hbs](../../../templates/sheets/item/ritual-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/skill-item-sheet.hbs](../../../templates/sheets/item/skill-item-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/spell-sheet.hbs](../../../templates/sheets/item/spell-sheet.hbs) | Не установлено | Не подготовлено | Не начат |
| [templates/sheets/item/valuable-sheet.hbs](../../../templates/sheets/item/valuable-sheet.hbs) | Основная форма категории, доступности, скрытности и описания предмета. | [Описание](files/templates/sheets/item/valuable-sheet.hbs.md) | Проверено |
| [templates/sheets/item/weapon-sheet.hbs](../../../templates/sheets/item/weapon-sheet.hbs) | Основная форма оружия и боеприпасов с областью рецепта. | [Описание](files/templates/sheets/item/weapon-sheet.hbs.md) | Проверено |
| [utils/extract.mjs](../../../utils/extract.mjs) | Не установлено | Не подготовлено | Не начат |
| [utils/packs.mjs](../../../utils/packs.mjs) | Не установлено | Не подготовлено | Не начат |
