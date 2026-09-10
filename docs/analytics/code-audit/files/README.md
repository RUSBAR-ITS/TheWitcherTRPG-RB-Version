# Карточки файлов

Карточки создаются по [шаблону](../templates/file.md) по мере пофайлового разбора. Общий список исходников и статусы находятся в [реестре](../registry.md), правила — в [README исследования](../README.md).

Путь карточки повторяет путь исходника относительно корня системы с добавлением `.md`: например, `module/TheWitcherTRPG.js` → `files/module/TheWitcherTRPG.js.md`.

После TASK-0002 и TASK-0003.001–TASK-0003.008 подготовлены и сверены 56 карточек. Этот README служит указателем и не входит в подсчёт описанных файлов.

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
