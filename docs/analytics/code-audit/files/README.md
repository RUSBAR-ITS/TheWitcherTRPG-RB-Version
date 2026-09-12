# Карточки файлов

Карточки создаются по [шаблону](../templates/file.md) по мере пофайлового разбора. Общий список исходников и статусы находятся в [реестре](../registry.md), правила — в [README исследования](../README.md).

Путь карточки повторяет путь исходника относительно корня системы с добавлением `.md`: например, `module/TheWitcherTRPG.js` → `files/module/TheWitcherTRPG.js.md`.

После TASK-0002 и TASK-0003.001–TASK-0003.053 подготовлены 417 карточек, включая 28 JSON style/lifepath. Текущий реестр содержит 615 файлов; остальные 198 JSON компедиумов поставлены в очередь .054–.061. Другие шесть языков и содержимое packs/ исключены. Этот README — указатель, не карточка исходного файла.

| Файл | Карточка |
| --- | --- |
| system.json | [Манифест](system.json.md) |
| module/TheWitcherTRPG.js | [Точка входа](module/TheWitcherTRPG.js.md) |
| module/setup/config.js | [Конфигурация](module/setup/config.js.md) |
| module/setup/registerDataModels.js | [Модели](module/setup/registerDataModels.js.md) |
| module/setup/registerSheets.js | [Листы](module/setup/registerSheets.js.md) |
| module/setup/settings.js | [Настройки](module/setup/settings.js.md) |
| module/setup/hooks.js | [События боя](module/setup/hooks.js.md) |
| module/setup/handlebars.js | [Шаблоны и helpers](module/setup/handlebars.js.md) |
| module/setup/queries.js | [Запросы](module/setup/queries.js.md) |
| module/setup/socketHook.js | [Сокет](module/setup/socketHook.js.md) |
| module/setup/deprecations.js | [Обработчик уведомлений](module/setup/deprecations.js.md) |

## Общие поля и характеристики — TASK-0003.001

| Файл | Карточка |
| --- | --- |
| module/data/dataUtils.js | [Описание](module/data/dataUtils.js.md) |
| module/data/actor/templates/valueLabelData.js | [Описание](module/data/actor/templates/valueLabelData.js.md) |
| module/data/actor/templates/common/stats/statData.js | [Описание](module/data/actor/templates/common/stats/statData.js.md) |
| module/data/actor/templates/common/stats/statsData.js | [Описание](module/data/actor/templates/common/stats/statsData.js.md) |
| module/data/actor/templates/common/stats/derivedStatsData.js | [Описание](module/data/actor/templates/common/stats/derivedStatsData.js.md) |

## Навыки — TASK-0003.002

| Файл | Карточка |
| --- | --- |
| module/data/actor/templates/common/skills/bodyData.js | [Описание](module/data/actor/templates/common/skills/bodyData.js.md) |
| module/data/actor/templates/common/skills/craData.js | [Описание](module/data/actor/templates/common/skills/craData.js.md) |
| module/data/actor/templates/common/skills/dexData.js | [Описание](module/data/actor/templates/common/skills/dexData.js.md) |
| module/data/actor/templates/common/skills/empData.js | [Описание](module/data/actor/templates/common/skills/empData.js.md) |
| module/data/actor/templates/common/skills/intData.js | [Описание](module/data/actor/templates/common/skills/intData.js.md) |
| module/data/actor/templates/common/skills/refData.js | [Описание](module/data/actor/templates/common/skills/refData.js.md) |
| module/data/actor/templates/common/skills/skillData.js | [Описание](module/data/actor/templates/common/skills/skillData.js.md) |
| module/data/actor/templates/common/skills/skillsData.js | [Описание](module/data/actor/templates/common/skills/skillsData.js.md) |
| module/data/actor/templates/common/skills/willData.js | [Описание](module/data/actor/templates/common/skills/willData.js.md) |

## Общие данные состояния Actor — TASK-0003.003

| Файл | Карточка |
| --- | --- |
| module/data/actor/templates/common/adrenalineData.js | [Описание](module/data/actor/templates/common/adrenalineData.js.md) |
| module/data/actor/templates/common/currencyData.js | [Описание](module/data/actor/templates/common/currencyData.js.md) |
| module/data/actor/templates/common/focusData.js | [Описание](module/data/actor/templates/common/focusData.js.md) |
| module/data/actor/templates/common/lifepathData.js | [Описание](module/data/actor/templates/common/lifepathData.js.md) |
| module/data/actor/templates/common/noteData.js | [Описание](module/data/actor/templates/common/noteData.js.md) |
| module/data/actor/templates/common/reputationData.js | [Описание](module/data/actor/templates/common/reputationData.js.md) |
| module/data/actor/templates/common/temporaryEffectsData.js | [Описание](module/data/actor/templates/common/temporaryEffectsData.js.md) |
| module/data/actor/templates/common/combatEffectsData.js | [Описание](module/data/actor/templates/common/combatEffectsData.js.md) |

## Биография и изменения урона — TASK-0003.004

| Файл | Карточка |
| --- | --- |
| module/data/actor/templates/character/general/backgroundData.js | [Описание](module/data/actor/templates/character/general/backgroundData.js.md) |
| module/data/actor/templates/character/general/detailsData.js | [Описание](module/data/actor/templates/character/general/detailsData.js.md) |
| module/data/actor/templates/character/general/homelandData.js | [Описание](module/data/actor/templates/character/general/homelandData.js.md) |
| module/data/actor/templates/character/general/lifeEventData.js | [Описание](module/data/actor/templates/character/general/lifeEventData.js.md) |
| module/data/actor/templates/character/general/lifeEventsData.js | [Описание](module/data/actor/templates/character/general/lifeEventsData.js.md) |
| module/data/actor/templates/character/generalData.js | [Описание](module/data/actor/templates/character/generalData.js.md) |
| module/data/actor/templates/character/general/damage/damageModificationData.js | [Описание](module/data/actor/templates/character/general/damage/damageModificationData.js.md) |
| module/data/actor/templates/character/general/damage/damageTypeModificationData.js | [Описание](module/data/actor/templates/character/general/damage/damageTypeModificationData.js.md) |

## Журналы, обучение, панели и атаки — TASK-0003.005

| Файл | Карточка |
| --- | --- |
| module/data/actor/templates/character/currencyLogData.js | [Описание](module/data/actor/templates/character/currencyLogData.js.md) |
| module/data/actor/templates/character/ipLogData.js | [Описание](module/data/actor/templates/character/ipLogData.js.md) |
| module/data/actor/templates/character/logData.js | [Описание](module/data/actor/templates/character/logData.js.md) |
| module/data/actor/templates/character/skillTrainingData.js | [Описание](module/data/actor/templates/character/skillTrainingData.js.md) |
| module/data/actor/templates/character/pannelsData.js | [Описание](module/data/actor/templates/character/pannelsData.js.md) |
| module/data/actor/templates/character/attackData.js | [Описание](module/data/actor/templates/character/attackData.js.md) |
| module/data/actor/templates/character/attackStatsData.js | [Описание](module/data/actor/templates/character/attackStatsData.js.md) |

## Сборка моделей Actor — TASK-0003.006

| Файл | Карточка |
| --- | --- |
| module/data/actor/commonActorData.js | [Описание](module/data/actor/commonActorData.js.md) |
| module/data/actor/characterData.js | [Описание](module/data/actor/characterData.js.md) |
| module/data/actor/monsterData.js | [Описание](module/data/actor/monsterData.js.md) |
| module/data/actor/lootData.js | [Описание](module/data/actor/lootData.js.md) |

## Документ Actor и строковые модификаторы — TASK-0003.007

| Файл | Карточка |
| --- | --- |
| module/actor/witcherActor.js | [Описание](module/actor/witcherActor.js.md) |
| module/actor/mixins/modifierMixin.js | [Описание](module/actor/mixins/modifierMixin.js.md) |

## Документ Item и общая модель предмета — TASK-0003.008

| Файл | Карточка |
| --- | --- |
| module/data/item/commonItemData.js | [Описание](module/data/item/commonItemData.js.md) |
| module/item/witcherItem.js | [Описание](module/item/witcherItem.js.md) |

## Документ ActiveEffect и применение воздействий — TASK-0003.009

| Файл | Карточка |
| --- | --- |
| module/activeEffect/witcherActiveEffect.js | [Описание](module/activeEffect/witcherActiveEffect.js.md) |
| module/data/activeEffects/witcherActiveEffectData.js | [Описание](module/data/activeEffects/witcherActiveEffectData.js.md) |
| module/data/activeEffects/witcherTemporaryItemImprovementData.js | [Описание](module/data/activeEffects/witcherTemporaryItemImprovementData.js.md) |
| module/actor/mixins/temporaryEffectMixin.js | [Описание](module/actor/mixins/temporaryEffectMixin.js.md) |
| module/scripts/temporaryEffects/applyActiveEffect.js | [Описание](module/scripts/temporaryEffects/applyActiveEffect.js.md) |
| module/scripts/statusEffects/applyStatusEffect.js | [Описание](module/scripts/statusEffects/applyStatusEffect.js.md) |
| templates/chat/item/appliedTemporaryItemImprovements.hbs | [Описание](templates/chat/item/appliedTemporaryItemImprovements.hbs.md) |
| templates/chat/combat/statusEffect.hbs | [Описание](templates/chat/combat/statusEffect.hbs.md) |

## Интерфейс эффектов и мастер изменений — TASK-0003.010

| Файл | Карточка |
| --- | --- |
| module/activeEffect/WitcherActiveEffectSheet.js | [Описание](module/activeEffect/WitcherActiveEffectSheet.js.md) |
| module/activeEffect/mixins/baseMixin.js | [Описание](module/activeEffect/mixins/baseMixin.js.md) |
| module/activeEffect/mixins/temporaryItemImprovementMixin.js | [Описание](module/activeEffect/mixins/temporaryItemImprovementMixin.js.md) |
| module/actor/sheets/mixins/activeEffectMixin.js | [Описание](module/actor/sheets/mixins/activeEffectMixin.js.md) |
| templates/dialog/activeEffects/wizard.hbs | [Описание](templates/dialog/activeEffects/wizard.hbs.md) |
| templates/sheets/activeEffect/system-specific.hbs | [Описание](templates/sheets/activeEffect/system-specific.hbs.md) |
| templates/partials/effect-part.hbs | [Описание](templates/partials/effect-part.hbs.md) |
| templates/sheets/actor/partials/character/tab-effects.hbs | [Описание](templates/sheets/actor/partials/character/tab-effects.hbs.md) |
| module/item/sheets/WitcherItemSheet.js | [Описание](module/item/sheets/WitcherItemSheet.js.md) |
| module/item/sheets/configurations/WitcherConfigurationSheet.js | [Описание](module/item/sheets/configurations/WitcherConfigurationSheet.js.md) |
| templates/partials/item-header.hbs | [Описание](templates/partials/item-header.hbs.md) |
| templates/partials/item-image.hbs | [Описание](templates/partials/item-image.hbs.md) |
| templates/sheets/item/configuration/tabs/header.hbs | [Описание](templates/sheets/item/configuration/tabs/header.hbs.md) |
| templates/sheets/item/configuration/tabs/general.hbs | [Описание](templates/sheets/item/configuration/tabs/general.hbs.md) |
| templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs | [Описание](templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs.md) |

## Вложенные боевые модели — TASK-0003.012

| Файл | Карточка |
| --- | --- |
| module/data/item/templates/combat/attackOptionsData.js | [Описание](module/data/item/templates/combat/attackOptionsData.js.md) |
| module/data/item/templates/combat/damagePropertiesData.js | [Описание](module/data/item/templates/combat/damagePropertiesData.js.md) |
| module/data/item/templates/combat/defenseOptionsData.js | [Описание](module/data/item/templates/combat/defenseOptionsData.js.md) |
| module/data/item/templates/combat/defensePropertiesData.js | [Описание](module/data/item/templates/combat/defensePropertiesData.js.md) |
| module/data/item/templates/combat/skillAttackData.js | [Описание](module/data/item/templates/combat/skillAttackData.js.md) |
| module/data/item/templates/combat/skillDefenseData.js | [Описание](module/data/item/templates/combat/skillDefenseData.js.md) |
| module/data/item/templates/weaponTypeData.js | [Описание](module/data/item/templates/weaponTypeData.js.md) |
| module/data/item/templates/armor/resistanceData.js | [Описание](module/data/item/templates/armor/resistanceData.js.md) |
| module/data/item/templates/armor/spData.js | [Описание](module/data/item/templates/armor/spData.js.md) |
| module/data/migrations/damagePropertiesMigration.js | [Описание](module/data/migrations/damagePropertiesMigration.js.md) |

## Оружие и конфигурация боевых свойств — TASK-0003.013

| Файл | Карточка |
| --- | --- |
| module/data/item/weaponData.js | [Описание](module/data/item/weaponData.js.md) |
| module/item/sheets/WitcherWeaponSheet.js | [Описание](module/item/sheets/WitcherWeaponSheet.js.md) |
| module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js | [Описание](module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js.md) |
| templates/sheets/item/weapon-sheet.hbs | [Описание](templates/sheets/item/weapon-sheet.hbs.md) |
| templates/sheets/item/configuration/partials/attackOptionsPart.hbs | [Описание](templates/sheets/item/configuration/partials/attackOptionsPart.hbs.md) |
| templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs | [Описание](templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs.md) |
| templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs | [Описание](templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs.md) |
| templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs | [Описание](templates/sheets/item/configuration/tabs/regionPropertiesConfiguration.hbs.md) |

## Броня и улучшения предметов — TASK-0003.014

| Файл | Карточка |
| --- | --- |
| module/data/item/armorData.js | [Описание](module/data/item/armorData.js.md) |
| module/data/item/enhancementData.js | [Описание](module/data/item/enhancementData.js.md) |
| module/data/item/templates/itemEffectData.js | [Описание](module/data/item/templates/itemEffectData.js.md) |
| module/item/sheets/WitcherArmorSheet.js | [Описание](module/item/sheets/WitcherArmorSheet.js.md) |
| module/item/sheets/WitcherEnhancementSheet.js | [Описание](module/item/sheets/WitcherEnhancementSheet.js.md) |
| module/item/sheets/configurations/WitcherArmorConfigurationSheet.js | [Описание](module/item/sheets/configurations/WitcherArmorConfigurationSheet.js.md) |
| templates/sheets/item/armor-sheet.hbs | [Описание](templates/sheets/item/armor-sheet.hbs.md) |
| templates/sheets/item/enhancement-sheet.hbs | [Описание](templates/sheets/item/enhancement-sheet.hbs.md) |
| templates/sheets/item/configuration/tabs/armorGeneral.hbs | [Описание](templates/sheets/item/configuration/tabs/armorGeneral.hbs.md) |

## Расходуемые предметы — TASK-0003.015

| Файл | Карточка |
| --- | --- |
| module/data/item/alchemicalData.js | [Описание](module/data/item/alchemicalData.js.md) |
| module/data/item/mutagenData.js | [Описание](module/data/item/mutagenData.js.md) |
| module/data/item/valuableData.js | [Описание](module/data/item/valuableData.js.md) |
| module/data/item/templates/consumableData.js | [Описание](module/data/item/templates/consumableData.js.md) |
| module/data/item/templates/consumePropertiesData.js | [Описание](module/data/item/templates/consumePropertiesData.js.md) |
| module/item/sheets/WitcherAlchemicalSheet.js | [Описание](module/item/sheets/WitcherAlchemicalSheet.js.md) |
| module/item/sheets/WitcherMutagenSheet.js | [Описание](module/item/sheets/WitcherMutagenSheet.js.md) |
| module/item/sheets/WitcherValuableSheet.js | [Описание](module/item/sheets/WitcherValuableSheet.js.md) |
| module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js | [Описание](module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js.md) |
| module/item/mixins/consumeMixin.js | [Описание](module/item/mixins/consumeMixin.js.md) |
| templates/sheets/item/alchemical-sheet.hbs | [Описание](templates/sheets/item/alchemical-sheet.hbs.md) |
| templates/sheets/item/mutagen-sheet.hbs | [Описание](templates/sheets/item/mutagen-sheet.hbs.md) |
| templates/sheets/item/valuable-sheet.hbs | [Описание](templates/sheets/item/valuable-sheet.hbs.md) |
| templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs | [Описание](templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs.md) |
| templates/chat/item/consume.hbs | [Описание](templates/chat/item/consume.hbs.md) |

## Компоненты и рецепты — TASK-0003.016

| Файл | Карточка |
| --- | --- |
| module/data/item/componentData.js | [Описание](module/data/item/componentData.js.md) |
| module/data/item/diagramData.js | [Описание](module/data/item/diagramData.js.md) |
| module/data/item/templates/craftingComponentData.js | [Описание](module/data/item/templates/craftingComponentData.js.md) |
| module/data/item/templates/associatedDiagramData.js | [Описание](module/data/item/templates/associatedDiagramData.js.md) |
| module/item/sheets/WitcherComponentSheet.js | [Описание](module/item/sheets/WitcherComponentSheet.js.md) |
| module/item/sheets/WitcherDiagramSheet.js | [Описание](module/item/sheets/WitcherDiagramSheet.js.md) |
| module/item/sheets/mixins/associatedDiagramMixin.js | [Описание](module/item/sheets/mixins/associatedDiagramMixin.js.md) |
| templates/sheets/item/component-sheet.hbs | [Описание](templates/sheets/item/component-sheet.hbs.md) |
| templates/sheets/item/diagrams-sheet.hbs | [Описание](templates/sheets/item/diagrams-sheet.hbs.md) |
| templates/partials/components-list.hbs | [Описание](templates/partials/components-list.hbs.md) |
| templates/partials/associated-diagram.hbs | [Описание](templates/partials/associated-diagram.hbs.md) |
| templates/partials/associated-item.hbs | [Описание](templates/partials/associated-item.hbs.md) |

## Ремонт предметов — TASK-0003.017

| Файл | Карточка |
| --- | --- |
| module/item/systems/repair.js | [Описание](module/item/systems/repair.js.md) |
| module/item/mixins/repairMixin.js | [Описание](module/item/mixins/repairMixin.js.md) |
| module/item/mixins/costEditMixin.js | [Описание](module/item/mixins/costEditMixin.js.md) |
| templates/dialog/repair-dialog.hbs | [Описание](templates/dialog/repair-dialog.hbs.md) |
| templates/chat/item/repair.hbs | [Описание](templates/chat/item/repair.hbs.md) |

## Раса и родина — TASK-0003.018

| Файл | Карточка |
| --- | --- |
| module/data/item/raceData.js | [Модель расы: четыре текстовые особенности, региональное социальное положение и подготовка HTML.](module/data/item/raceData.js.md) |
| module/data/item/homelandData.js | [Модель предмета родины: ключ выбора и дополнительное название.](module/data/item/homelandData.js.md) |
| module/data/item/templates/perkData.js | [Фабрика имени и HTML-описания расовой особенности.](module/data/item/templates/perkData.js.md) |
| module/data/item/templates/socialStandingData.js | [Фабрика пяти региональных строк социального положения расы.](module/data/item/templates/socialStandingData.js.md) |
| module/item/sheets/WitcherRaceSheet.js | [Лист расы: основной шаблон и наследование общих действий Item.](module/item/sheets/WitcherRaceSheet.js.md) |
| module/item/sheets/WitcherHomelandSheet.js | [Лист родины: основной шаблон и наследование общих действий Item.](module/item/sheets/WitcherHomelandSheet.js.md) |
| templates/sheets/item/race-sheet.hbs | [Форма расы: особенности, источник, пять регионов и доступ к конфигурации.](templates/sheets/item/race-sheet.hbs.md) |
| templates/sheets/item/homeland-sheet.hbs | [Форма родины: выбор страны, условное название и доступ к конфигурации.](templates/sheets/item/homeland-sheet.hbs.md) |

## Профессия, навыки и конфигурация — TASK-0003.019

| Файл | Карточка |
| --- | --- |
| module/data/item/professionData.js | [Модель профессии: навыки, HTML, список базовых навыков и выбор защиты.](module/data/item/professionData.js.md) |
| module/data/item/templates/professionPathData.js | [Фабрика пути профессии: название и три навыка.](module/data/item/templates/professionPathData.js.md) |
| module/data/item/templates/professionSkillData.js | [Фабрика профессионального навыка: базовые поля и четыре вида настроек.](module/data/item/templates/professionSkillData.js.md) |
| module/data/item/templates/profession/skillUsageData.js | [Модель использования способности и выбора получателя.](module/data/item/templates/profession/skillUsageData.js.md) |
| module/data/item/templates/profession/temporaryHealthData.js | [Модель порога, формулы и длительности временного здоровья.](module/data/item/templates/profession/temporaryHealthData.js.md) |
| module/data/item/templates/profession/thresholdData.js | [Модель включения и словаря порогов профессионального навыка.](module/data/item/templates/profession/thresholdData.js.md) |
| module/item/sheets/WitcherProfessionSheet.js | [Лист профессии: шаблон, специальная конфигурация и варианты выбора.](module/item/sheets/WitcherProfessionSheet.js.md) |
| module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js | [Конфигурация путей профессии, поиск навыков и CRUD воздействий/порогов.](module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js.md) |
| templates/sheets/item/profession-sheet.hbs | [Основная форма профессии: десять навыков, заметки, пути и базовые навыки.](templates/sheets/item/profession-sheet.hbs.md) |
| templates/sheets/item/configuration/partials/profession/skillPathPart.hbs | [Фрагмент вкладки пути с тремя редакторами навыка.](templates/sheets/item/configuration/partials/profession/skillPathPart.hbs.md) |
| templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs | [Форма механик навыка: атака, защита, использование, HP и пороги.](templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs.md) |
| templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs | [Фрагмент выбора видов атаки и условных флагов профессии.](templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs.md) |

## Критические травмы, лечение и отдых — TASK-0003.020

| Файл | Карточка |
| --- | --- |
| module/data/item/criticalWoundData.js | [Описание](module/data/item/criticalWoundData.js.md) |
| module/item/sheets/WitcherCriticalWoundSheet.js | [Описание](module/item/sheets/WitcherCriticalWoundSheet.js.md) |
| module/actor/sheets/mixins/criticalWoundMixin.js | [Описание](module/actor/sheets/mixins/criticalWoundMixin.js.md) |
| module/actor/mixins/healMixin.js | [Описание](module/actor/mixins/healMixin.js.md) |
| module/actor/sheets/mixins/healMixin.js | [Описание](module/actor/sheets/mixins/healMixin.js.md) |
| templates/sheets/item/criticalWound-sheet.hbs | [Описание](templates/sheets/item/criticalWound-sheet.hbs.md) |
| templates/partials/crit-wounds-table.hbs | [Описание](templates/partials/crit-wounds-table.hbs.md) |
| templates/dialog/heal/heal-rest.hbs | [Описание](templates/dialog/heal/heal-rest.hbs.md) |
| templates/chat/heal/resting-status.hbs | [Описание](templates/chat/heal/resting-status.hbs.md) |
| templates/chat/combat/heal.hbs | [Описание](templates/chat/combat/heal.hbs.md) |

## Магические предметы, формы и компоненты ритуалов — TASK-0003.021

| Файл | Карточка |
| --- | --- |
| module/data/item/spellData.js | [Описание](module/data/item/spellData.js.md) |
| module/data/item/hexData.js | [Описание](module/data/item/hexData.js.md) |
| module/data/item/ritualData.js | [Описание](module/data/item/ritualData.js.md) |
| module/data/item/templates/componentData.js | [Описание](module/data/item/templates/componentData.js.md) |
| module/item/sheets/WitcherSpellSheet.js | [Описание](module/item/sheets/WitcherSpellSheet.js.md) |
| module/item/sheets/WitcherHexSheet.js | [Описание](module/item/sheets/WitcherHexSheet.js.md) |
| module/item/sheets/WitcherRitualSheet.js | [Описание](module/item/sheets/WitcherRitualSheet.js.md) |
| module/item/sheets/configurations/WitcherSpellConfigurationSheet.js | [Описание](module/item/sheets/configurations/WitcherSpellConfigurationSheet.js.md) |
| templates/sheets/item/spell-sheet.hbs | [Описание](templates/sheets/item/spell-sheet.hbs.md) |
| templates/sheets/item/hex-sheet.hbs | [Описание](templates/sheets/item/hex-sheet.hbs.md) |
| templates/sheets/item/ritual-sheet.hbs | [Описание](templates/sheets/item/ritual-sheet.hbs.md) |
| templates/sheets/item/configuration/tabs/spellGeneral.hbs | [Описание](templates/sheets/item/configuration/tabs/spellGeneral.hbs.md) |
| templates/partials/spell-header.hbs | [Описание](templates/partials/spell-header.hbs.md) |

## Области заклинаний и события регионов — TASK-0003.022

| Файл | Карточка |
| --- | --- |
| module/data/item/templates/regions/templatePropertiesData.js | [Описание](module/data/item/templates/regions/templatePropertiesData.js.md) |
| module/data/item/templates/regions/regionBehavioursData.js | [Описание](module/data/item/templates/regions/regionBehavioursData.js.md) |
| module/data/item/templates/regions/regionPropertiesData.js | [Описание](module/data/item/templates/regions/regionPropertiesData.js.md) |
| module/data/item/mixin/spellRegionMixin.js | [Описание](module/data/item/mixin/spellRegionMixin.js.md) |
| module/scripts/regions/regionHooks.js | [Описание](module/scripts/regions/regionHooks.js.md) |

## Расследования, улики и препятствия — TASK-0003.023

| Файл | Карточка |
| --- | --- |
| module/data/investigation/templates/complexityData.js | [Описание](module/data/investigation/templates/complexityData.js.md) |
| module/data/investigation/mysteryActorData.js | [Описание](module/data/investigation/mysteryActorData.js.md) |
| module/data/investigation/clueData.js | [Описание](module/data/investigation/clueData.js.md) |
| module/data/investigation/obstacleData.js | [Описание](module/data/investigation/obstacleData.js.md) |
| module/actor/sheets/investigation/WitcherMysterySheet.js | [Описание](module/actor/sheets/investigation/WitcherMysterySheet.js.md) |
| module/item/sheets/investigation/WitcherClueSheet.js | [Описание](module/item/sheets/investigation/WitcherClueSheet.js.md) |
| module/item/sheets/investigation/WitcherObstacleSheet.js | [Описание](module/item/sheets/investigation/WitcherObstacleSheet.js.md) |
| module/scripts/investigation/rollClue.js | [Описание](module/scripts/investigation/rollClue.js.md) |
| templates/sheets/investigation/mystery-sheet.hbs | [Описание](templates/sheets/investigation/mystery-sheet.hbs.md) |
| templates/sheets/investigation/clue-sheet.hbs | [Описание](templates/sheets/investigation/clue-sheet.hbs.md) |
| templates/sheets/investigation/obstacle-sheet.hbs | [Описание](templates/sheets/investigation/obstacle-sheet.hbs.md) |
| templates/sheets/investigation/partials/clue-display.hbs | [Описание](templates/sheets/investigation/partials/clue-display.hbs.md) |
| templates/sheets/investigation/partials/obstacle-display.hbs | [Описание](templates/sheets/investigation/partials/obstacle-display.hbs.md) |
| templates/dialog/investigation/chooseEvidenceSkill.hbs | [Описание](templates/dialog/investigation/chooseEvidenceSkill.hbs.md) |

## Контейнеры и хранение предметов — TASK-0003.024

| Файл | Карточка |
| --- | --- |
| module/data/item/containerData.js | [Описание](module/data/item/containerData.js.md) |
| module/item/sheets/WitcherContainerSheet.js | [Описание](module/item/sheets/WitcherContainerSheet.js.md) |
| templates/sheets/item/container-sheet.hbs | [Описание](templates/sheets/item/container-sheet.hbs.md) |

## Общие листы Actor — TASK-0003.025

| Файл | Карточка |
| --- | --- |
| module/actor/sheets/WitcherActorSheet.js | [Описание](module/actor/sheets/WitcherActorSheet.js.md) |
| module/actor/sheets/WitcherActorSheetV1.js | [Описание](module/actor/sheets/WitcherActorSheetV1.js.md) |

## Действия инвентаря и контекстное меню Item — TASK-0003.026

| Файл | Карточка |
| --- | --- |
| module/actor/sheets/mixins/itemMixin.js | [Описание](module/actor/sheets/mixins/itemMixin.js.md) |
| module/actor/sheets/interactions/itemContextMenu.js | [Описание](module/actor/sheets/interactions/itemContextMenu.js.md) |

## Вкладки и таблицы инвентаря Actor — TASK-0003.027

| Файл | Карточка |
| --- | --- |
| templates/sheets/actor/tabs/tab-inventory.hbs | [Описание](templates/sheets/actor/tabs/tab-inventory.hbs.md) |
| templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs | [Описание](templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs.md) |
| templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs | [Описание](templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs.md) |
| templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs | [Описание](templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs.md) |
| templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs | [Описание](templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs.md) |
| templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs | [Описание](templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs.md) |
| templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs | [Описание](templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs.md) |
| templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs | [Описание](templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs.md) |
| templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs | [Описание](templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs.md) |
| templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs | [Описание](templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs.md) |
| templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs | [Описание](templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs.md) |
| templates/partials/monster/monster-inventory-tab.hbs | [Описание](templates/partials/monster/monster-inventory-tab.hbs.md) |

## Общий бросок и вспомогательные функции — TASK-0003.028

| Файл | Карточка |
| --- | --- |
| module/scripts/rollConfig.js | [Описание](module/scripts/rollConfig.js.md) |
| module/scripts/rolls/extendedRoll.js | [Описание](module/scripts/rolls/extendedRoll.js.md) |
| module/scripts/rolls/fumble.js | [Описание](module/scripts/rolls/fumble.js.md) |
| module/scripts/helper.js | [Описание](module/scripts/helper.js.md) |
| module/chatMessage/chatMessageData.js | [Описание](module/chatMessage/chatMessageData.js.md) |

## Навыки: броски, развитие и пользовательские навыки — TASK-0003.029

| Файл | Карточка |
| --- | --- |
| module/data/item/skillItemData.js | [Описание](module/data/item/skillItemData.js.md) |
| module/item/sheets/WitcherSkillItemSheet.js | [Описание](module/item/sheets/WitcherSkillItemSheet.js.md) |
| module/actor/mixins/skillMixin.js | [Описание](module/actor/mixins/skillMixin.js.md) |
| module/actor/sheets/mixins/skillMixin.js | [Описание](module/actor/sheets/mixins/skillMixin.js.md) |
| module/actor/sheets/mixins/customSkillMixin.js | [Описание](module/actor/sheets/mixins/customSkillMixin.js.md) |
| templates/sheets/item/skill-item-sheet.hbs | [Описание](templates/sheets/item/skill-item-sheet.hbs.md) |
| templates/partials/character/tab-skills.hbs | [Описание](templates/partials/character/tab-skills.hbs.md) |
| templates/partials/character/skill-display.hbs | [Описание](templates/partials/character/skill-display.hbs.md) |
| templates/partials/character/custom-skill-display.hbs | [Описание](templates/partials/character/custom-skill-display.hbs.md) |
| templates/partials/monster/monster-skill-tab.hbs | [Описание](templates/partials/monster/monster-skill-tab.hbs.md) |
| templates/partials/monster/monster-skill-display.hbs | [Описание](templates/partials/monster/monster-skill-display.hbs.md) |
| templates/partials/monster/monster-custom-skill-display.hbs | [Описание](templates/partials/monster/monster-custom-skill-display.hbs.md) |
| templates/sheets/actor/configuration/partials/skillConfiguration.hbs | [Описание](templates/sheets/actor/configuration/partials/skillConfiguration.hbs.md) |
| templates/sheets/actor/configuration/app/edit-skills.hbs | [Описание](templates/sheets/actor/configuration/app/edit-skills.hbs.md) |

## Характеристики, модификаторы и проверки состояния — TASK-0003.030

| Файл | Карточка |
| --- | --- |
| module/actor/sheets/mixins/statMixin.js | [Описание](module/actor/sheets/mixins/statMixin.js.md) |
| module/actor/sheets/configurations/WitcherModifiersConfiguration.js | [Описание](module/actor/sheets/configurations/WitcherModifiersConfiguration.js.md) |
| module/actor/sheets/mixins/deathSaveMixin.js | [Описание](module/actor/sheets/mixins/deathSaveMixin.js.md) |
| module/actor/mixins/adrenalineMixin.js | [Описание](module/actor/mixins/adrenalineMixin.js.md) |
| templates/partials/character/tab-stats.hbs | [Описание](templates/partials/character/tab-stats.hbs.md) |
| templates/sheets/actor/configuration/app/edit-stats.hbs | [Описание](templates/sheets/actor/configuration/app/edit-stats.hbs.md) |
| templates/sheets/actor/configuration/app/partials/stats-block.hbs | [Описание](templates/sheets/actor/configuration/app/partials/stats-block.hbs.md) |
| templates/dialog/deprecations/statSkillModifiers.hbs | [Описание](templates/dialog/deprecations/statSkillModifiers.hbs.md) |
| templates/dialog/deprecations/lifepathModifiers.hbs | [Описание](templates/dialog/deprecations/lifepathModifiers.hbs.md) |

## Лист персонажа, заголовок и боковая панель — TASK-0003.031

| Файл | Карточка |
| --- | --- |
| module/actor/sheets/WitcherCharacterSheet.js | [Описание](module/actor/sheets/WitcherCharacterSheet.js.md) |
| templates/partials/character-header.hbs | [Описание](templates/partials/character-header.hbs.md) |
| templates/sheets/actor/partials/character/sidebar.hbs | [Описание](templates/sheets/actor/partials/character/sidebar.hbs.md) |

## Лист монстра, конфигурация и шаблоны — TASK-0003.032

| Файл | Карточка |
| --- | --- |
| module/actor/sheets/WitcherMonsterSheet.js | [Описание](module/actor/sheets/WitcherMonsterSheet.js.md) |
| module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js | [Описание](module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js.md) |
| templates/sheets/actor/partials/monster/header.hbs | [Описание](templates/sheets/actor/partials/monster/header.hbs.md) |
| templates/sheets/actor/partials/monster/sidebar.hbs | [Описание](templates/sheets/actor/partials/monster/sidebar.hbs.md) |
| templates/sheets/actor/partials/monster/tabs/tab-details.hbs | [Описание](templates/sheets/actor/partials/monster/tabs/tab-details.hbs.md) |
| templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs | [Описание](templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs.md) |
| templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs | [Описание](templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs.md) |
| templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs | [Описание](templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs.md) |
| templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs | [Описание](templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs.md) |
| templates/sheets/actor/configuration/monster/header.hbs | [Описание](templates/sheets/actor/configuration/monster/header.hbs.md) |
| templates/sheets/actor/configuration/monster/general.hbs | [Описание](templates/sheets/actor/configuration/monster/general.hbs.md) |
| templates/sheets/actor/monster-sheet.hbs | [Описание](templates/sheets/actor/monster-sheet.hbs.md) |
| templates/partials/monster/monster-details-tab.hbs | [Описание](templates/partials/monster/monster-details-tab.hbs.md) |

## Биография и заметки — TASK-0003.033

| Файл | Карточка |
| --- | --- |
| module/actor/sheets/mixins/noteMixin.js | [Описание](module/actor/sheets/mixins/noteMixin.js.md) |
| module/data/item/noteData.js | [Описание](module/data/item/noteData.js.md) |
| templates/partials/character/tab-background.hbs | [Описание](templates/partials/character/tab-background.hbs.md) |
| templates/sheets/item/note-sheet.hbs | [Описание](templates/sheets/item/note-sheet.hbs.md) |

## Компоненты, алхимическая панель и разбор предметов — TASK-0003.034

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/craftingMixin.js | [Описание](module/actor/mixins/craftingMixin.js.md) |
| module/actor/sheets/mixins/alchemyMixin.js | [Описание](module/actor/sheets/mixins/alchemyMixin.js.md) |
| module/item/mixins/dismantlingMixin.js | [Описание](module/item/mixins/dismantlingMixin.js.md) |
| templates/partials/character/substances.hbs | [Описание](templates/partials/character/substances.hbs.md) |
| templates/chat/item/dismantle.hbs | [Описание](templates/chat/item/dismantle.hbs.md) |

## Добыча и торговля — TASK-0003.035

| Файл | Карточка |
| --- | --- |
| module/actor/sheets/WitcherLootSheet.js | [Описание](module/actor/sheets/WitcherLootSheet.js.md) |
| templates/sheets/actor/loot-sheet.hbs | [Описание](templates/sheets/actor/loot-sheet.hbs.md) |
| templates/sheets/actor/partials/loot/loot-item-display.hbs | [Описание](templates/sheets/actor/partials/loot/loot-item-display.hbs.md) |
| module/data/item/mountData.js | [Описание](module/data/item/mountData.js.md) |
| module/item/sheets/WitcherMountSheet.js | [Описание](module/item/sheets/WitcherMountSheet.js.md) |
| templates/sheets/item/mount-sheet.hbs | [Описание](templates/sheets/item/mount-sheet.hbs.md) |

## Обмен валюты — TASK-0003.036

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/currencyConverterMixin.js | [Описание](module/actor/mixins/currencyConverterMixin.js.md) |
| module/actor/sheets/mixins/currencyConverterMixin.js | [Описание](module/actor/sheets/mixins/currencyConverterMixin.js.md) |
| templates/sheets/actor/currencyConverter/currencyConverter.hbs | [Описание](templates/sheets/actor/currencyConverter/currencyConverter.hbs.md) |
| templates/chat/currency-conversion.hbs | [Описание](templates/chat/currency-conversion.hbs.md) |

## Награды — TASK-0003.037

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/rewardsMixin.js | [Описание](module/actor/mixins/rewardsMixin.js.md) |
| module/actor/rewardsSheet.js | [Описание](module/actor/rewardsSheet.js.md) |
| module/app/reward/reward.js | [Описание](module/app/reward/reward.js.md) |
| module/app/htmlUtils.js | [Описание](module/app/htmlUtils.js.md) |
| templates/sheets/actor/rewards/header.hbs | [Описание](templates/sheets/actor/rewards/header.hbs.md) |
| templates/sheets/actor/rewards/ip.hbs | [Описание](templates/sheets/actor/rewards/ip.hbs.md) |
| templates/sheets/actor/rewards/currency.hbs | [Описание](templates/sheets/actor/rewards/currency.hbs.md) |
| templates/chat/rewards.hbs | [Описание](templates/chat/rewards.hbs.md) |

## Применение профессий — TASK-0003.038

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/professionMixin.js | [Описание](module/actor/mixins/professionMixin.js.md) |
| templates/partials/character/tab-profession.hbs | [Описание](templates/partials/character/tab-profession.hbs.md) |
| templates/sheets/actor/partials/monster/tabs/tab-profession.hbs | [Описание](templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md) |
| templates/dialog/combat/profession-attack.hbs | [Описание](templates/dialog/combat/profession-attack.hbs.md) |

## Магия Actor — TASK-0003.039

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/castSpellMixin.js | [Описание](module/actor/mixins/castSpellMixin.js.md) |
| templates/partials/character/tab-magic.hbs | [Описание](templates/partials/character/tab-magic.hbs.md) |
| templates/sheets/actor/partials/character/spell-type-list.hbs | [Описание](templates/sheets/actor/partials/character/spell-type-list.hbs.md) |
| templates/partials/monster/monster-spell-tab.hbs | [Описание](templates/partials/monster/monster-spell-tab.hbs.md) |
| templates/dialog/combat/spell-attack.hbs | [Описание](templates/dialog/combat/spell-attack.hbs.md) |
| templates/chat/combat/spellItem.hbs | [Описание](templates/chat/combat/spellItem.hbs.md) |

## Сообщения чата — TASK-0003.040

| Файл | Карточка |
| --- | --- |
| module/chatMessage/witcherChatMessage.js | [Описание](module/chatMessage/witcherChatMessage.js.md) |
| module/data/chatMessage/baseMessageData.js | [Описание](module/data/chatMessage/baseMessageData.js.md) |
| module/data/chatMessage/attackMessageData.js | [Описание](module/data/chatMessage/attackMessageData.js.md) |
| module/data/chatMessage/defenseMessageData.js | [Описание](module/data/chatMessage/defenseMessageData.js.md) |
| module/data/chatMessage/damageMessageData.js | [Описание](module/data/chatMessage/damageMessageData.js.md) |
| module/data/chatMessage/templates/attackData.js | [Описание](module/data/chatMessage/templates/attackData.js.md) |
| module/data/chatMessage/templates/critData.js | [Описание](module/data/chatMessage/templates/critData.js.md) |
| module/data/chatMessage/templates/damageData.js | [Описание](module/data/chatMessage/templates/damageData.js.md) |
| module/data/chatMessage/templates/locationData.js | [Описание](module/data/chatMessage/templates/locationData.js.md) |
| module/scripts/chat.js | [Описание](module/scripts/chat.js.md) |

## Оружейная атака — TASK-0003.041

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/weaponAttackMixin.js | [Описание](module/actor/mixins/weaponAttackMixin.js.md) |
| templates/dialog/combat/weapon-attack.hbs | [Описание](templates/dialog/combat/weapon-attack.hbs.md) |
| styles/weapon-roll.css | [Описание](styles/weapon-roll.css.md) |
| styles/attack-sheet.css | [Описание](styles/attack-sheet.css.md) |

## Защита — TASK-0003.042

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/defenseMixin.js | [Описание](module/actor/mixins/defenseMixin.js.md) |
| module/item/mixins/defenseOptionMixin.js | [Описание](module/item/mixins/defenseOptionMixin.js.md) |
| templates/chat/combat/defense/defense.hbs | [Описание](templates/chat/combat/defense/defense.hbs.md) |
| templates/chat/combat/defense/defenseCrit.hbs | [Описание](templates/chat/combat/defense/defenseCrit.hbs.md) |
| templates/chat/combat/defense/defenseStun.hbs | [Описание](templates/chat/combat/defense/defenseStun.hbs.md) |

## Броня и локации — TASK-0003.043

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/armorMixin.js | [Описание](module/actor/mixins/armorMixin.js.md) |
| module/actor/mixins/locationMixin.js | [Описание](module/actor/mixins/locationMixin.js.md) |
| styles/armor-sheet.css | [Описание](styles/armor-sheet.css.md) |

## Формирование и применение урона — TASK-0003.044

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/damageMixin.js | [Описание](module/actor/mixins/damageMixin.js.md) |
| module/item/mixins/damageUtilMixin.js | [Описание](module/item/mixins/damageUtilMixin.js.md) |
| module/scripts/damageInstance.js | [Описание](module/scripts/damageInstance.js.md) |
| module/actor/mixins/damageUtilMixin.js | [Описание](module/actor/mixins/damageUtilMixin.js.md) |
| templates/dialog/combat/variableDamage.hbs | [Описание](templates/dialog/combat/variableDamage.hbs.md) |
| templates/chat/damage/damageToLocation.hbs | [Описание](templates/chat/damage/damageToLocation.hbs.md) |
| templates/chat/damage/damageToAllLocations.hbs | [Описание](templates/chat/damage/damageToAllLocations.hbs.md) |
| templates/chat/damage/shieldAbsorbs.hbs | [Описание](templates/chat/damage/shieldAbsorbs.hbs.md) |
| templates/chat/damage/spAbsorbs.hbs | [Описание](templates/chat/damage/spAbsorbs.hbs.md) |

## Чат, Combat и сокет GM — TASK-0003.045

| Файл | Карточка |
| --- | --- |
| module/scripts/combat/combat.js | [Описание](module/scripts/combat/combat.js.md) |
| module/scripts/combat/applyDamage.js | [Описание](module/scripts/combat/applyDamage.js.md) |
| module/scripts/combat/generalCombatHook.js | [Описание](module/scripts/combat/generalCombatHook.js.md) |
| templates/chat/combat/regeneration.hbs | [Описание](templates/chat/combat/regeneration.hbs.md) |
| module/scripts/socket/socketMessage.js | [Описание](module/scripts/socket/socketMessage.js.md) |

## Словесный бой — TASK-0003.046

| Файл | Карточка |
| --- | --- |
| module/actor/mixins/verbalCombatMixin.js | [Описание](module/actor/mixins/verbalCombatMixin.js.md) |
| module/scripts/verbalCombat/verbalCombat.js | [Описание](module/scripts/verbalCombat/verbalCombat.js.md) |
| module/scripts/verbalCombat/verbalCombatDefense.js | [Описание](module/scripts/verbalCombat/verbalCombatDefense.js.md) |
| templates/dialog/verbal-combat.hbs | [Описание](templates/dialog/verbal-combat.hbs.md) |
| templates/dialog/verbal-combat-defense.hbs | [Описание](templates/dialog/verbal-combat-defense.hbs.md) |

## Способности, эффекты и модификаторы: поля и оформление — TASK-0003.047

| Файл | Карточка |
| --- | --- |
| module/data/item/templates/effectDerivedStatData.js | [Описание](module/data/item/templates/effectDerivedStatData.js.md) |
| module/data/item/templates/effectSkillData.js | [Описание](module/data/item/templates/effectSkillData.js.md) |
| module/data/item/templates/effectStatData.js | [Описание](module/data/item/templates/effectStatData.js.md) |
| styles/activeEffect.css | [Описание](styles/activeEffect.css.md) |
| styles/configurations/modifier-configuration.css | [Описание](styles/configurations/modifier-configuration.css.md) |
| styles/crit-wounds-table.css | [Описание](styles/crit-wounds-table.css.md) |
| styles/profession-sheet.css | [Описание](styles/profession-sheet.css.md) |
| styles/special-skill-table.css | [Описание](styles/special-skill-table.css.md) |
| styles/race-sheet.css | [Описание](styles/race-sheet.css.md) |
| styles/character/tab-profession.css | [Описание](styles/character/tab-profession.css.md) |

## Представление предметов: сообщения, листы и служебные диалоги — TASK-0003.048

| Файл | Карточка |
| --- | --- |
| styles/chat.css | [Описание](styles/chat.css.md) |
| styles/item-header.css | [Описание](styles/item-header.css.md) |
| styles/item-sheets.css | [Описание](styles/item-sheets.css.md) |
| styles/container-sheet.css | [Описание](styles/container-sheet.css.md) |
| styles/components-list.css | [Описание](styles/components-list.css.md) |
| styles/substances.css | [Описание](styles/substances.css.md) |
| styles/loot-sheet.css | [Описание](styles/loot-sheet.css.md) |
| styles/repair.css | [Описание](styles/repair.css.md) |
| styles/currency-converter.css | [Описание](styles/currency-converter.css.md) |
| styles/rewards.css | [Описание](styles/rewards.css.md) |
| templates/chat/item/item-description.hbs | [Описание](templates/chat/item/item-description.hbs.md) |
| templates/chat/item/partials/item-description/alchemicals.hbs | [Описание](templates/chat/item/partials/item-description/alchemicals.hbs.md) |
| templates/chat/item/partials/item-description/crafting-items.hbs | [Описание](templates/chat/item/partials/item-description/crafting-items.hbs.md) |
| templates/chat/item/partials/item-description/description.hbs | [Описание](templates/chat/item/partials/item-description/description.hbs.md) |
| templates/chat/item/partials/item-description/spell-description.hbs | [Описание](templates/chat/item/partials/item-description/spell-description.hbs.md) |
| templates/chat/item/partials/item-description/tags.hbs | [Описание](templates/chat/item/partials/item-description/tags.hbs.md) |

## Стили Actor: персонаж, монстр и общие вкладки — TASK-0003.049

| Файл | Карточка |
| --- | --- |
| styles/character-header.css | [Описание](styles/character-header.css.md) |
| styles/character/sheet.css | [Описание](styles/character/sheet.css.md) |
| styles/tab-background.css | [Описание](styles/tab-background.css.md) |
| styles/tab-inventory.css | [Описание](styles/tab-inventory.css.md) |
| styles/tab-inventory-list.css | [Описание](styles/tab-inventory-list.css.md) |
| styles/tab-skills.css | [Описание](styles/tab-skills.css.md) |
| styles/monster-sheet.css | [Описание](styles/monster-sheet.css.md) |
| styles/monster-skill-tab.css | [Описание](styles/monster-skill-tab.css.md) |
| styles/monster/header.css | [Описание](styles/monster/header.css.md) |
| styles/monster/sidebar.css | [Описание](styles/monster/sidebar.css.md) |
| styles/monster/details.css | [Описание](styles/monster/details.css.md) |
| styles/monster/inventory.css | [Описание](styles/monster/inventory.css.md) |
| styles/monster/sheet.css | [Описание](styles/monster/sheet.css.md) |

## Подключение ресурсов, базовые стили и инструменты компедиумов — TASK-0003.050

| Файл | Карточка |
| --- | --- |
| styles/witcher-styles.css | [Описание](styles/witcher-styles.css.md) |
| styles/system-styles.css | [Описание](styles/system-styles.css.md) |
| styles/dialog.css | [Описание](styles/dialog.css.md) |
| package.json | [Описание](package.json.md) |
| build.json | [Описание](build.json.md) |
| utils/packs.mjs | [Описание](utils/packs.mjs.md) |
| utils/extract.mjs | [Описание](utils/extract.mjs.md) |

## Локализации en/ru — TASK-0003.051

| Файл | Карточка |
| --- | --- |
| lang/en.json | [Английский словарь](lang/en.json.md) |
| lang/ru.json | [Русский словарь](lang/ru.json.md) |

## Запланированный разбор компедиумов

[TASK-0003.052–TASK-0003.061](../../../tasks/task-0003-remaining-files.md#компедиумы-task-0003052task-0003061) охватывают 226 файлов packsJson. Семь JSON style и 21 JSON lifepath описаны ниже; 198 файлов следующих порций пока не имеют карточек. Вложенные результаты и эффекты учитываются внутри карточки владельца.

## Таблицы стиля и ценностей — TASK-0003.052

| Исходник | Карточка | Охват |
| --- | --- | --- |
| packsJson/style/Style__Affectations_4RWDMDzNdnz2kgwU.json | [Style: Affectations](packsJson/style/Style__Affectations_4RWDMDzNdnz2kgwU.json.md) | 10 текстовых результатов |
| packsJson/style/Style__Clothing_BuyEb4FcAyQL2hov.json | [Style: Clothing](packsJson/style/Style__Clothing_BuyEb4FcAyQL2hov.json.md) | 10 текстовых результатов |
| packsJson/style/Style__Hair_Style_Ov9xIpAdWEPZCIoH.json | [Style: Hair Style](packsJson/style/Style__Hair_Style_Ov9xIpAdWEPZCIoH.json.md) | 10 текстовых результатов |
| packsJson/style/Style__Personality_TOQz3ETDronoeEDt.json | [Style: Personality](packsJson/style/Style__Personality_TOQz3ETDronoeEDt.json.md) | 10 текстовых результатов |
| packsJson/style/Values__Feelings_on_People_4eCXMVEfRx4PivWH.json | [Values: Feelings on People](packsJson/style/Values__Feelings_on_People_4eCXMVEfRx4PivWH.json.md) | 10 текстовых результатов |
| packsJson/style/Values__Ideals_s5EjP50ddIVoitHT.json | [Values: Ideals](packsJson/style/Values__Ideals_s5EjP50ddIVoitHT.json.md) | 10 текстовых результатов |
| packsJson/style/Values__Valued_Person_y1WCi6n2Kpwqb27P.json | [Values: Valued Person](packsJson/style/Values__Valued_Person_y1WCi6n2Kpwqb27P.json.md) | 10 текстовых результатов |

[Перекрёстная сверка](../review-log.md#task-0003052): связи, настоящие модели Foundry и изолированные броски/вывод. Новых issues нет.

## Таблицы жизненных событий — TASK-0003.053

| Файл | Назначение |
| --- | --- |
| [packsJson/lifepath/Allies__Closeness_IswiqefPmaHECa5X.json](packsJson/lifepath/Allies__Closeness_IswiqefPmaHECa5X.json.md) | Описывает степень близости с союзником: пять текстовых вариантов с разной шириной диапазонов. |
| [packsJson/lifepath/Allies__Gender_QFHhoiXtIBYkL8Rd.json](packsJson/lifepath/Allies__Gender_QFHhoiXtIBYkL8Rd.json.md) | Описывает гендер союзника: три текстовых варианта с диапазонами 1–4, 5–8 и 9–10. |
| [packsJson/lifepath/Allies__Generator_Va7NF10ETcMvndFo.json](packsJson/lifepath/Allies__Generator_Va7NF10ETcMvndFo.json.md) | Собирает описание союзника из пяти подтаблиц: гендер, положение, знакомство, близость и местонахождение. |
| [packsJson/lifepath/Allies__How_You_Met_BqAizN8u9r6nMSyK.json](packsJson/lifepath/Allies__How_You_Met_BqAizN8u9r6nMSyK.json.md) | Задаёт десять текстовых обстоятельств знакомства с союзником. |
| [packsJson/lifepath/Allies__Position_5sroduMneFqG9INx.json](packsJson/lifepath/Allies__Position_5sroduMneFqG9INx.json.md) | Задаёт десять текстовых вариантов положения или роли союзника. |
| [packsJson/lifepath/Allies__Where_Are_They__W19e7rtl3ycrMhQU.json](packsJson/lifepath/Allies__Where_Are_They__W19e7rtl3ycrMhQU.json.md) | Задаёт четыре текстовых региона, где находится союзник. |
| [packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json](packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json.md) | Выбирает генератор врага при 1 или генератор союзника при 2, затем раскрывает выбранный составной результат. |
| [packsJson/lifepath/Enemies__Gender_FMondgMHlPLSy3cq.json](packsJson/lifepath/Enemies__Gender_FMondgMHlPLSy3cq.json.md) | Описывает гендер врага; используется также генератором врагов ведьмачьего жизненного пути. |
| [packsJson/lifepath/Enemies__Generator_7AXmeCSRkK3ktJ9Y.json](packsJson/lifepath/Enemies__Generator_7AXmeCSRkK3ktJ9Y.json.md) | Собирает описание врага из семи подтаблиц: гендер, положение, причина, пострадавшая сторона, уровень силы, эскалация и источник силы. |
| [packsJson/lifepath/Enemies__How_Far_Has_It_Escalated__BLiqJBssahtqPqVf.json](packsJson/lifepath/Enemies__How_Far_Has_It_Escalated__BLiqJBssahtqPqVf.json.md) | Описывает степень эскалации конфликта с врагом: пять текстовых вариантов по две грани d10. |
| [packsJson/lifepath/Enemies__Position_WeN4QhEHL468Ushx.json](packsJson/lifepath/Enemies__Position_WeN4QhEHL468Ushx.json.md) | Задаёт десять текстовых вариантов положения или роли врага. |
| [packsJson/lifepath/Enemies__Power_9mYMTKkCuU2ElJdx.json](packsJson/lifepath/Enemies__Power_9mYMTKkCuU2ElJdx.json.md) | Выводит текстовый уровень силы врага от 1 до 10; числового поля Actor эти результаты не задают. |
| [packsJson/lifepath/Enemies__The_Cause_U9R1ct2xP13y6R7j.json](packsJson/lifepath/Enemies__The_Cause_U9R1ct2xP13y6R7j.json.md) | Задаёт десять текстовых причин конфликта с врагом. |
| [packsJson/lifepath/Enemies__What_Is_Their_Power__sH1XIFHObBFdbjTI.json](packsJson/lifepath/Enemies__What_Is_Their_Power__sH1XIFHObBFdbjTI.json.md) | Описывает источник силы врага: общественное влияние, знания, физическая сила, слуги или магия. |
| [packsJson/lifepath/Enemies__Who_Was_Wronged_cz5KlvgE7I7QV57H.json](packsJson/lifepath/Enemies__Who_Was_Wronged_cz5KlvgE7I7QV57H.json.md) | Определяет текстом, кто пострадал в конфликте; два результата на d2. |
| [packsJson/lifepath/Fortune_Z0eeWQI3R8v4YNLd.json](packsJson/lifepath/Fortune_Z0eeWQI3R8v4YNLd.json.md) | Задаёт десять удачных событий с описанными наградами и двумя встроенными бросками. |
| [packsJson/lifepath/Fortune_or_Misfortune_qKwYD3GHlGxCmiir.json](packsJson/lifepath/Fortune_or_Misfortune_qKwYD3GHlGxCmiir.json.md) | Выбирает Misfortune при 1 или Fortune при 2 и раскрывает один текстовый результат выбранной таблицы. |
| [packsJson/lifepath/Misfortune_JNbvihde5EGIFPdB.json](packsJson/lifepath/Misfortune_JNbvihde5EGIFPdB.json.md) | Задаёт десять неудачных событий, включая последствия и десять встроенных бросков в описаниях. |
| [packsJson/lifepath/Romance_CDgdx129wZvINn16.json](packsJson/lifepath/Romance_CDgdx129wZvINn16.json.md) | Выбирает тип романтического события; для трагедии и проблемных отношений объединяет заголовок с результатом подтаблицы. |
| [packsJson/lifepath/Romance__Problematic_Love_l7k0hSL3iRzjJcYs.json](packsJson/lifepath/Romance__Problematic_Love_l7k0hSL3iRzjJcYs.json.md) | Задаёт десять текстовых обстоятельств проблемных отношений; подтаблица Romance. |
| [packsJson/lifepath/Romance__Romantic_Tragedy_Jmvpwp9FRwRhDWZu.json](packsJson/lifepath/Romance__Romantic_Tragedy_Jmvpwp9FRwRhDWZu.json.md) | Задаёт десять текстовых исходов романтической трагедии; подтаблица Romance. |

[Перекрёстная сверка](../review-log.md#task-0003053): 21 RollTable, 139 результатов, рекурсия и inline-броски. Зарегистрирована [issue-00319](../../../issues/potential/issue-00319.md); JSON не менялись.
