# Карточки файлов

Карточки создаются по [шаблону](../templates/file.md) по мере пофайлового разбора. Общий список исходников и статусы находятся в [реестре](../registry.md), правила — в [README исследования](../README.md).

Путь карточки повторяет путь исходника относительно корня системы с добавлением `.md`: например, `module/TheWitcherTRPG.js` → `files/module/TheWitcherTRPG.js.md`.

После TASK-0002 и TASK-0003.001–TASK-0003.020 подготовлены и сверены 168 карточек. Этот README служит указателем и не входит в подсчёт описанных файлов.

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
