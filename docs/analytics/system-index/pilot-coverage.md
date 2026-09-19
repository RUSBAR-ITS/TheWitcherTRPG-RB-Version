# Покрытие пилота TASK-0006.003

2026-09-14; rusbar-main, `85de48d5711a2c45d8bc0d57c308bfc91d68b547`. [Задача](../../tasks/task-0006.003.md), [протокол](review-log.md#task-0006003), [поиск](README.md).

## Состав и границы

В каталоге 615 исходников. Смысловые записи частично охватывают **23 основных и 13 смежных файлов**; 579 остаются только в каталоге. Три исходных файла .001 уже входят в 23: повторного счёта нет.

Всего 400 сущностей: 338 локальных определений, 26 внешних и 36 динамических границ. Связей 977; из них 924 добавлены в .003. Начальные 35 сущностей/53 связи сохранены отдельными частями; добавлены 365 сущностей. Два начальных процесса сохранены без изменения. В .004 добавлены [12 процессов пилота](process-guide.md) с явными границами; вместе с начальными их 14. IQ-07 работает по исполнителям шагов и прикреплённым отношениям.

У всех 36 файлов definitions/relations остаются partial: это охват выбранных областей, а не объявление полного графа файла. Processes имеют отдельное покрытие. Импорт/ссылка на файл не означает, что его внутренние определения и все потребители индексированы. Шаблон wizard.hbs доступен как адрес цели renders, без разбора его внутренностей в .003.

## Основные файлы

Числа в третьем столбце: локальные определения / отношения, место использования которых находится в файле. Границы не входят в число локальных определений; входящие отношения из других файлов не прибавляются.

| Файл | ID | Определения / связи | Включённая область и остаток | Подробности |
| --- | --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../module/TheWitcherTRPG.js) | src-000004 | 1 / 12 | Выбран init и регистрация Actor/ActiveEffect/моделей. Остальные hooks, Sheets, macros/settings/chat/migrations вне пилота. | [Карточка](../code-audit/files/module/TheWitcherTRPG.js.md) |
| [module/setup/registerDataModels.js](../../../module/setup/registerDataModels.js) | src-000214 | 1 / 15 | Назначения Actor, базового/временного ActiveEffect и SkillItemData. Остальные Item/ChatMessage регистрации вне пилота. | [Карточка](../code-audit/files/module/setup/registerDataModels.js.md) |
| [module/setup/config.js](../../../module/setup/config.js) | src-000209 | 85 / 137 | statTypes/statMap/skillMap, контейнеры групп, statusEffects/armorEffects. Прочие разделы и содержимое эффектов/боевых карт вне пилота. | [Карточка](../code-audit/files/module/setup/config.js.md) |
| [module/actor/witcherActor.js](../../../module/actor/witcherActor.js) | src-000047 | 13 / 131 | Подготовка, расчёты статов, temporaryEffects, getList/getTotalWeight/applyStatus и три mixin. Остальные действия Actor и боевые mixin вне пилота. | [Карточка](../code-audit/files/module/actor/witcherActor.js.md) |
| [module/activeEffect/witcherActiveEffect.js](../../../module/activeEffect/witcherActiveEffect.js) | src-000008 | 8 / 36 | Все собственные методы; ключевые обращения changes/phase и подавления. Детальные callback диалога/поле длительности и реализация ядра не раскрыты. | [Карточка](../code-audit/files/module/activeEffect/witcherActiveEffect.js.md) |
| [module/data/activeEffects/witcherActiveEffectData.js](../../../module/data/activeEffects/witcherActiveEffectData.js) | src-000052 | 7 / 9 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/activeEffects/witcherActiveEffectData.js.md) |
| [module/data/actor/commonActorData.js](../../../module/data/actor/commonActorData.js) | src-000055 | 25 / 92 | Схема контейнеров пилота, базовые расчёты и миграции статов. Валюта/adrenaline — смежные входы; остальные вложенные схемы не раскрыты. | [Карточка](../code-audit/files/module/data/actor/commonActorData.js.md) |
| [module/data/actor/templates/common/stats/statData.js](../../../module/data/actor/templates/common/stats/statData.js) | src-000090 | 6 / 6 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/stats/statData.js.md) |
| [module/data/actor/templates/common/stats/statsData.js](../../../module/data/actor/templates/common/stats/statsData.js) | src-000091 | 14 / 67 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/stats/statsData.js.md) |
| [module/data/actor/templates/common/stats/derivedStatsData.js](../../../module/data/actor/templates/common/stats/derivedStatsData.js) | src-000089 | 15 / 42 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/stats/derivedStatsData.js.md) |
| [module/data/actor/templates/common/skills/skillData.js](../../../module/data/actor/templates/common/skills/skillData.js) | src-000086 | 10 / 13 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/skills/skillData.js.md) |
| [module/data/actor/templates/common/skills/skillsData.js](../../../module/data/actor/templates/common/skills/skillsData.js) | src-000087 | 8 / 22 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/skills/skillsData.js.md) |
| [module/data/actor/templates/common/skills/bodyData.js](../../../module/data/actor/templates/common/skills/bodyData.js) | src-000080 | 5 / 12 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/skills/bodyData.js.md) |
| [module/data/actor/templates/common/skills/craData.js](../../../module/data/actor/templates/common/skills/craData.js) | src-000081 | 10 / 22 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/skills/craData.js.md) |
| [module/data/actor/templates/common/skills/dexData.js](../../../module/data/actor/templates/common/skills/dexData.js) | src-000082 | 8 / 19 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/skills/dexData.js.md) |
| [module/data/actor/templates/common/skills/empData.js](../../../module/data/actor/templates/common/skills/empData.js) | src-000083 | 13 / 31 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/skills/empData.js.md) |
| [module/data/actor/templates/common/skills/intData.js](../../../module/data/actor/templates/common/skills/intData.js) | src-000084 | 16 / 40 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/skills/intData.js.md) |
| [module/data/actor/templates/common/skills/refData.js](../../../module/data/actor/templates/common/skills/refData.js) | src-000085 | 11 / 25 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/skills/refData.js.md) |
| [module/data/actor/templates/common/skills/willData.js](../../../module/data/actor/templates/common/skills/willData.js) | src-000088 | 10 / 27 | Схема, вложенные поля и собственные методы; служебные привязки fields и метаданные конструкторов не представлены отдельными узлами. | [Карточка](../code-audit/files/module/data/actor/templates/common/skills/willData.js.md) |
| [module/actor/mixins/modifierMixin.js](../../../module/actor/mixins/modifierMixin.js) | src-000019 | 4 / 17 | addActiveEffects; соседние addAttack/addDefense объявлены без полного процесса боя. Неизвестные группы остаются динамической границей. | [Карточка](../code-audit/files/module/actor/mixins/modifierMixin.js.md) |
| [module/actor/mixins/skillMixin.js](../../../module/actor/mixins/skillMixin.js) | src-000022 | 6 / 50 | Броски встроенного/собственного навыка и социальная добавка. levelUpSkill — адресуемая смежная цель без процесса IP. | [Карточка](../code-audit/files/module/actor/mixins/skillMixin.js.md) |
| [module/actor/sheets/mixins/skillMixin.js](../../../module/actor/sheets/mixins/skillMixin.js) | src-000045 | 7 / 25 | Все четыре метода и выбранные callback; прочий UI и публикация изменений вне пилота. | [Карточка](../code-audit/files/module/actor/sheets/mixins/skillMixin.js.md) |
| [module/scripts/rolls/extendedRoll.js](../../../module/scripts/rolls/extendedRoll.js) | src-000202 | 3 / 45 | extendedRoll/isCrit/isFumble и обращения параметров/вывода. Движок Roll, произвольные callers и полная структура dice/options вне пилота. | [Карточка](../code-audit/files/module/scripts/rolls/extendedRoll.js.md) |

## Смежные файлы

Взяты только объявления моделей для регистрации/наследования, конструкторы RollConfig/ChatMessageData, getCustomModifier/addPart, getArmorEcumbrance и подключения skillListener. У листов указан фрагмент activateListeners до вызова skillListener; он не выдаётся за весь метод. В SkillItemData описана собственная схема, но не все обработчики Item-навыка. Для моделей Character/Monster взято начало defineSchema с super; остальная схема вне пилота.

| Файл | ID | Определения / связи | Подробности |
| --- | --- | --- | --- |
| [module/scripts/rollConfig.js](../../../module/scripts/rollConfig.js) | src-000201 | 11 / 11 | [Карточка](../code-audit/files/module/scripts/rollConfig.js.md) |
| [module/chatMessage/chatMessageData.js](../../../module/chatMessage/chatMessageData.js) | src-000050 | 7 / 8 | [Карточка](../code-audit/files/module/chatMessage/chatMessageData.js.md) |
| [module/scripts/helper.js](../../../module/scripts/helper.js) | src-000198 | 2 / 5 | [Карточка](../code-audit/files/module/scripts/helper.js.md) |
| [module/actor/mixins/armorMixin.js](../../../module/actor/mixins/armorMixin.js) | src-000010 | 2 / 5 | [Карточка](../code-audit/files/module/actor/mixins/armorMixin.js.md) |
| [module/data/item/skillItemData.js](../../../module/data/item/skillItemData.js) | src-000124 | 10 / 11 | [Карточка](../code-audit/files/module/data/item/skillItemData.js.md) |
| [module/data/actor/characterData.js](../../../module/data/actor/characterData.js) | src-000054 | 2 / 5 | [Карточка](../code-audit/files/module/data/actor/characterData.js.md) |
| [module/data/actor/monsterData.js](../../../module/data/actor/monsterData.js) | src-000057 | 2 / 5 | [Карточка](../code-audit/files/module/data/actor/monsterData.js.md) |
| [module/data/actor/lootData.js](../../../module/data/actor/lootData.js) | src-000056 | 1 / 2 | [Карточка](../code-audit/files/module/data/actor/lootData.js.md) |
| [module/data/investigation/mysteryActorData.js](../../../module/data/investigation/mysteryActorData.js) | src-000104 | 1 / 2 | [Карточка](../code-audit/files/module/data/investigation/mysteryActorData.js.md) |
| [module/data/activeEffects/witcherTemporaryItemImprovementData.js](../../../module/data/activeEffects/witcherTemporaryItemImprovementData.js) | src-000053 | 5 / 7 | [Карточка](../code-audit/files/module/data/activeEffects/witcherTemporaryItemImprovementData.js.md) |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) | src-000027 | 3 / 7 | [Карточка](../code-audit/files/module/actor/sheets/WitcherActorSheet.js.md) |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) | src-000028 | 3 / 7 | [Карточка](../code-audit/files/module/actor/sheets/WitcherActorSheetV1.js.md) |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | src-000032 | 3 / 7 | [Карточка](../code-audit/files/module/actor/sheets/configurations/WitcherModifiersConfiguration.js.md) |

## Различия, которые важно сохранять при чтении графа

- stat().value, Skill.value и SkillItemData.value — разные определения. Контейнеры Stats/DerivedStats используют общую фабрику stat; конкретный путь экземпляра хранится в payload/context обращения.
- Skill.modifiedValue читает value + activeEffectModifiers. Обычный rollSkillCheck читает Skill.value и отдельно вызывает addActiveEffects; это не вызов getter. Собственный rollCustomSkillCheck читает Item.system.value, затем передаёт Item.name в helper встроенных навыков; его собственное activeEffectModifiers не читается ([issue-00190](../../issues/closed/issue-00190.md)).
- actor.skillMixin и sheet.skillMixin — разные объекты с разными файлами/владельцами. Клик хранится отдельным handler, а установка listener — registers. Связь calls идёт из callback, не означает немедленный бросок при установке listener.
- prepareDerivedData вызывает calculateStats дважды, в строках 49 и 51. Это два разных отношения. У REF/DEX вызовы calculateWeigthEncumbrance также сохранены в двух местах. Включение этих связей не означает нового исполнения расчётов.
- CommonActorData.prepareBaseData выполняет копирование баз. Stats.prepareBaseData не записан как его вызов: Foundry не обходит так произвольные вложенные модели.
- В _preUpdate читается флаг из **частичного payload** data.system, а не старый флаг документа. change.phase записывается во входной changes. [issue-00043](../../issues/closed/issue-00043.md) содержит прежние воспроизведения и уточнение пути мастера.
- Основной active getter и применение changes принадлежат Foundry. Системный isDisabled не приравнен к проверке active. Значения applySelf/OnTarget/OnHit/OnDamage участвуют в isSuppressed.
- showSuccess задаётся в RollConfig и вызывающих методах, но extendedRoll его не читает. toMessage ожидается, последующие setFlag — нет. Отложенный messageData и публикация — разные ветви.
- addDefenseModifiers из modifierMixin объявлен, но позднее заменён defenseMixin при Object.assign. Из этого определения не построен ложный вызов действующего метода Actor.

## Внешние контракты и динамические цели

Внешние узлы имеют location=null и dependency=foundry; локального места реализации им не приписано. Проверена установленная Foundry 14.367.0. package-хеш не доказывает неизменность каждого файла ядра; нижеследующие отпечатки фиксируют дополнительные прочитанные участки, а штатный check автоматически сверяет package.json.

| Файл окружения | Прочитанные участки | SHA-256 |
| --- | --- | --- |
| /opt/foundryvtt/client/documents/actor.mjs | appliedEffects; применение изменений по фазам; allApplicableEffects; prepareData/prepareEmbeddedDocuments | e82580bf9cef39d934c972dee859a3b9ba7ab5f3ebdc7502319dfed1bc214bb3 |
| /opt/foundryvtt/client/documents/active-effect.mjs | target/active; приоритеты; shouldApplyChange; applyChange/applyChangeField | 7eacad67767aaa9840a6249dcd55098d62279fad5cc2bf3fa6d28da4455236b8 |
| /opt/foundryvtt/common/data/active-effect.mjs | Схема changes: key/type/value/phase/priority | d15b7279756b40ce25c7739fa5292fc142b53e9bf948f52f6881f7ca3d2dbc54 |
| /opt/foundryvtt/client/documents/abstract/client-document.mjs | Порядок prepareData, строки 313–320 | a007180e3cf8d465dffe43b11272f289b4cf77a9e301c7d431f48267dfad8e9e |

При подготовке Actor ядро запускает initial-изменения после подготовки вложенных документов, а final — после общего prepareData с системными расчётами. Само применение поля выполняет ActiveEffect.applyChange. Эти внутренние вызовы ядра описаны как внешний контракт и в прежнем аудите; для них не выдуманы calls со строкой системного override.

Динамическая запись хранит фактическое выражение и причину неопределённости: this.skillMap, CONFIG.WITCHER[modifier.group], выбранный DOM Item, change.key/phase, необязательные modifiers и поля generic messageData. Для стандартных потребителей добавлены конкретные отношения с условиями. Это не исчерпывающий анализ всех возможных callers/значений.

## Проверенные запросы

13 CLI-случаев находятся в [pilot-queries.json](examples/pilot-queries.json); исходные ожидаемые случаи .001 сохранены в [queries.json](examples/queries.json) и проверяются на временном представлении начальных трёх файлов.

| Вопрос | Случаи | Содержательный результат |
| --- | --- | --- |
| IQ-01 | P01, P02 | Два владельца activeEffectModifiers и два разных skillMixin |
| IQ-02 | P01–P03, P10 | Владелец/адрес поля и отдельная динамическая цель изменения фазы |
| IQ-03 | P04–P06 | init-регистрация Actor/ActiveEffect и два входа rollSkillCheck |
| IQ-04 | P07 | Getter читает два поля Skill |
| IQ-05 | P06, P08 | Входящие вызовы и читатели поля с разными местами обращения |
| IQ-06 | P08, P09, P12 | Чтение activeEffectModifiers, вычисление stat().value; отсутствие чтения showSuccess в охваченном участке |
| IQ-08 | P10, P11 | Граница неизвестной цели, карточка, раздел аудита и issue |
| IQ-07 | P13 после .004 | Явные шаги Actor в proc-000004/000005; дополнительные PR-случаи описаны в [процессах](process-guide.md) |

Пустой результат P12 не является утверждением об отсутствии читателей во всей системе. В .003 P13 возвращал not_indexed; в .004 ожидаемый ответ обновлён под внесённые процессы. Все непустые ответы этих случаев имеют partial, подтверждённую свежесть и адреса для перехода к исходникам.

## Адреса для TASK-0006.004

Ниже сохранён перечень узлов, переданных из .003. В .004 порядок, ветви, await и выходы оформлены в [процессах](process-guide.md); начальные proc-000001/proc-000002 сохранены.

| Область | Уже адресуемые сущности |
| --- | --- |
| Регистрация классов/моделей | ent-000329 — init callback; ent-000328 — registerDataModels; ent-000277 — WitcherActor; ent-000311 — WitcherActiveEffect |
| Подготовка и два расчёта статов | ent-000141 — CommonActorData.prepareBaseData; ent-000280 — WitcherActor.prepareDerivedData; ent-000281 — WitcherActor.calculateStats; ent-000282 — WitcherActor.calculateStat |
| Фиксированные и прочие производные | ent-000284 — WitcherActor.calculateFixedDerivedStats; ent-000285 — WitcherActor.calculateDerivedStats; ent-000286 — WitcherActor.calculateDerivedStat |
| Активность, создание и фаза эффекта | ent-000313 — WitcherActiveEffect.isSuppressed; ent-000317 — WitcherActiveEffect._preCreate; ent-000318 — WitcherActiveEffect.chooseSkill; ent-000319 — WitcherActiveEffect._preUpdate |
| Клик и обычный бросок навыка | ent-000382 — sheet.skillMixin.skillListener/rollSkill click; ent-000301 — actor.skillMixin.rollSkill; ent-000302 — actor.skillMixin.rollSkillCheck; ent-000296 — actor.modifierMixin.addActiveEffects |
| Собственный навык и общая обработка Roll | ent-000304 — actor.skillMixin.rollCustomSkillCheck; ent-000369 — extendedRoll; ent-000360 — getCustomModifier; ent-000341 — RollConfig |
| Начальный getter / миграция | ent-000016 — Skill.modifiedValue; ent-000032 — Intelligence.migrateData |

Отношения для шага получать через neighbors с подходящим kind; различать место вызова и определение целевого метода. Например, у ent-000280 связи calls содержат оба calculateStats, а у ent-000369 — отдельные конструкции/evaluate, условную публикацию и сохранение флагов. Полный граф остальных подсистем не построен.
