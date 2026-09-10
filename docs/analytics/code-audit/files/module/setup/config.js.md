# module/setup/config.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/setup/config.js](../../../../../../module/setup/config.js) |
| Тип файла | JavaScript |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../../../tasks/task-0002-system-initialization.md); порция 2 |
| Запись перекрёстной сверки | [Журнал сверок](../../../review-log.md) — TASK-0002, порция 2 |

## Назначение файла

Единый экспортируемый объект WITCHER со справочниками и декларативными заготовками. Он содержит метаданные характеристик/навыков, настройки атак, предметов, монстров, критических травм и статусов. Вычисляющего обработчика эффектов в этом файле нет.

## Условия использования

При импорте создаётся WITCHER={} и последовательно заполняются 36 свойств. В init точка входа присваивает объект CONFIG.WITCHER и передаёт statusEffects в CONFIG.statusEffects. Часть файлов импортирует WITCHER напрямую, остальные читают CONFIG или получают его через context.config. Объект не заморожен; ссылки attribute/skill/dmgStat указывают на ранее созданные объекты того же справочника.

## Введённые сущности и действия с ними

| Свойство | Начальная строка | Размер верхнего уровня | Содержание |
| --- | --- | --- | --- |
| `WITCHER.statTypes` | 4 | 10 | Метки девяти характеристик и пустой выбор none. |
| `WITCHER.statMap` | 17 | 21 | Метаданные девяти характеристик, 11 производных значений и reputation: origin/name/label/labelShort. reputation содержит только origin=''. |
| `WITCHER.meleeSkills` | 136 | 5 | Имена пяти навыков ближнего боя. |
| `WITCHER.rangedSkills` | 137 | 3 | Имена трёх дистанционных навыков. |
| `WITCHER.magicSkills` | 138 | 3 | spellcast, ritcraft, hexweave. |
| `WITCHER.verbalCombatSkills` | 139 | 7 | Семь навыков вербального боя. |
| `WITCHER.empatheticVerbalCombatSkills` | 148 | 6 | Шесть навыков без intimidation. |
| `WITCHER.attackOptions` | 150 | 4 | Варианты melee/ranged/spell/itemUse с наборами навыков. |
| `WITCHER.meleeAttackOptions` | 173 | 5 | Подписанные варианты пяти навыков. |
| `WITCHER.rangedAttackOptions` | 196 | 3 | Подписанные варианты трёх навыков. |
| `WITCHER.spellAttackOptions` | 211 | 3 | Подписанные варианты трёх магических навыков. |
| `WITCHER.defenseOptions` | 226 | 6 | Шесть вариантов dodge/reposition/block/parry/parryThrown/magicResist; навыки, типы предметов и дополнительные флаги. parry=-3, parryThrown=-5. |
| `WITCHER.skillGroups` | 265 | 6 | Шесть групп, включая специальную allSkills; поля label/name. |
| `WITCHER.skillMap` | 292 | 52 | 52 записи навыков с ссылкой attribute на объект statMap, label/name, иногда rollLabel/costMultiplier=2. |
| `WITCHER.homelands` | 585 | 26 | 26 ключей происхождения, включая other. |
| `WITCHER.socialStanding` | 614 | 6 | Шесть вариантов отношения. |
| `WITCHER.currency` | 624 | 7 | Семь названий валют, включая falsecoin. |
| `WITCHER.currencyRates` | 634 | 6 | Шесть коэффициентов: bizant=4, ducat=1/3, lintar=2, floren=3, crown=1, oren=1. |
| `WITCHER.currencyConverter` | 643 | 1 | Список excluded=[falsecoin]. |
| `WITCHER.substanceTypes` | 647 | 9 | Девять алхимических субстанций. |
| `WITCHER.Availability` | 659 | 4 | Четыре уровня доступности. |
| `WITCHER.Concealment` | 666 | 4 | Четыре категории сокрытия T/S/L/NA. |
| `WITCHER.craftingLevels` | 673 | 5 | Пять уровней изготовления. |
| `WITCHER.weapon` | 681 | 2 | hands (none/left/right/both) и attacks (normal/fast/strong/joint/half). fast.attackNumber=2, strong.attackPenality=-3 и dmgMulti=*2, joint.attackPenality=-3, half.dmgMulti=/2. |
| `WITCHER.magic` | 712 | 6 | Шесть классов магии с ссылкой skill на skillMap; выбор spellcast/ritcraft/hexweave. |
| `WITCHER.damageTypes` | 733 | 8 | Восемь типов повреждений; fire имеет likeSilver и likeMeteorite. |
| `WITCHER.MonsterTypes` | 771 | 12 | 12 типов монстров. |
| `WITCHER.monsterDifficulty` | 786 | 4 | Четыре уровня сложности. |
| `WITCHER.monsterComplexity` | 793 | 3 | Три уровня сложности поведения. |
| `WITCHER.location` | 800 | 6 | Шесть локализаций тела. |
| `WITCHER.Crit` | 809 | 24 | 24 записи критических травм с локализациями, тяжестью и тремя состояниями; структура отдельно ниже. |
| `WITCHER.critLevel` | 1936 | 4 | simple/complex/difficult/deadly. |
| `WITCHER.critTreatment` | 1943 | 3 | none/stabilized/treated. |
| `WITCHER.verbalCombat` | 1949 | 5 | Пять групп действий: 4 EmpatheticAttacks, 3 AntagonisticAttacks, 4 Defenses, 2 EmpatheticTools и 3 AntagonisticTools. Ссылки skill/dmgStat, строки baseDmg и локализация. |
| `WITCHER.statusEffects` | 2064 | 26 | 26 заготовок статусов с id/name/img и необязательным changes. |
| `WITCHER.armorEffects` | 2407 | 4 | Четыре свойства: reducedVision, fire, poison, bleed. Все refersStatusEffect=true; последние три addsResistance=true. |

Размер означает число ключей объекта или элементов массива, не число всех вложенных сущностей. У skillMap ключ `commonspeech` отличается от name=`commonsp`; это значимо при построении путей.

### Ключи характеристик и навыков

Ниже перечислены все 21 ключ statMap и 52 ключа skillMap. В TASK-0002 они описаны как определения справочника. В TASK-0003.001 дополнительно сопоставлены все 20 записей statMap с непустым origin со схемами [Stats](../data/actor/templates/common/stats/statsData.js.md) и [DerivedStats](../data/actor/templates/common/stats/derivedStatsData.js.md): все пути totalModifiers существуют. В схемах дополнительно есть toxicity (отдельный getToxSuggestions) и shield; reputation в statMap имеет пустой origin. Это проверка путей, не полного применения эффектов. Для общего языка сопоставление с intData и построителем changes выполнено ранее (issue-00004).

| Ключ statMap | origin / name | label / labelShort |
| --- | --- | --- |
| `int` | `stats` / `int` | `WITCHER.StInt` / `WITCHER.Actor.Stat.Int` |
| `ref` | `stats` / `ref` | `WITCHER.StRef` / `WITCHER.Actor.Stat.Ref` |
| `dex` | `stats` / `dex` | `WITCHER.StDex` / `WITCHER.Actor.Stat.Dex` |
| `body` | `stats` / `body` | `WITCHER.StBody` / `WITCHER.Actor.Stat.Body` |
| `spd` | `stats` / `spd` | `WITCHER.StSpd` / `WITCHER.Actor.Stat.Spd` |
| `emp` | `stats` / `emp` | `WITCHER.StEmp` / `WITCHER.Actor.Stat.Emp` |
| `cra` | `stats` / `cra` | `WITCHER.StCra` / `WITCHER.Actor.Stat.Cra` |
| `will` | `stats` / `will` | `WITCHER.StWill` / `WITCHER.Actor.Stat.Will` |
| `luck` | `stats` / `luck` | `WITCHER.StLuck` / `WITCHER.Actor.Stat.Luck` |
| `stun` | `derivedStats` / `stun` | `WITCHER.Actor.DerStat.Stun` |
| `run` | `derivedStats` / `run` | `WITCHER.Actor.DerStat.Run` |
| `leap` | `derivedStats` / `leap` | `WITCHER.Actor.DerStat.Leap` |
| `enc` | `derivedStats` / `enc` | `WITCHER.Actor.DerStat.Enc` |
| `rec` | `derivedStats` / `rec` | `WITCHER.Actor.DerStat.Rec` |
| `woundTreshold` | `derivedStats` / `woundTreshold` | `WITCHER.Actor.DerStat.woundTreshold` |
| `hp` | `derivedStats` / `hp` | `WITCHER.Actor.DerStat.HP` |
| `sta` | `derivedStats` / `sta` | `WITCHER.Actor.DerStat.Sta` |
| `resolve` | `derivedStats` / `resolve` | `WITCHER.Actor.DerStat.Resolve` |
| `focus` | `derivedStats` / `focus` | `WITCHER.Actor.DerStat.Focus` |
| `vigor` | `derivedStats` / `vigor` | `WITCHER.Actor.DerStat.Vigor` |
| `reputation` | `` / нет | Нет |

| Ключ skillMap | name | attribute.name | label; дополнительные поля |
| --- | --- | --- | --- |
| `awareness` | `awareness` | `int` | `WITCHER.skills.awareness.label` |
| `business` | `business` | `int` | `WITCHER.skills.business.label` |
| `deduction` | `deduction` | `int` | `WITCHER.skills.deduction.label` |
| `education` | `education` | `int` | `WITCHER.skills.education.label` |
| `commonspeech` | `commonsp` | `int` | `WITCHER.skills.commonSpeech.label`; rollLabel=`WITCHER.skills.commonSpeech.rollLabel`; costMultiplier=2 |
| `eldersp` | `eldersp` | `int` | `WITCHER.skills.elderSpeech.label`; rollLabel=`WITCHER.skills.elderSpeech.rollLabel`; costMultiplier=2 |
| `dwarven` | `dwarven` | `int` | `WITCHER.skills.dwarvenSpeech.label`; rollLabel=`WITCHER.skills.dwarvenSpeech.rollLabel`; costMultiplier=2 |
| `monster` | `monster` | `int` | `WITCHER.skills.monsterLore.label`; rollLabel=`WITCHER.skills.monsterLore.rollLabel`; costMultiplier=2 |
| `socialetq` | `socialetq` | `int` | `WITCHER.skills.socialEtiquette.label` |
| `streetwise` | `streetwise` | `int` | `WITCHER.skills.streetwise.label` |
| `tactics` | `tactics` | `int` | `WITCHER.skills.tactics.label`; rollLabel=`WITCHER.skills.tactics.rollLabel`; costMultiplier=2 |
| `teaching` | `teaching` | `int` | `WITCHER.skills.teaching.label` |
| `wilderness` | `wilderness` | `int` | `WITCHER.skills.wildernessSurvival.label` |
| `brawling` | `brawling` | `ref` | `WITCHER.skills.brawling.label` |
| `dodge` | `dodge` | `ref` | `WITCHER.skills.dodgeEscape.label` |
| `melee` | `melee` | `ref` | `WITCHER.skills.melee.label` |
| `riding` | `riding` | `ref` | `WITCHER.skills.riding.label` |
| `sailing` | `sailing` | `ref` | `WITCHER.skills.sailing.label` |
| `smallblades` | `smallblades` | `ref` | `WITCHER.skills.smallblades.label` |
| `staffspear` | `staffspear` | `ref` | `WITCHER.skills.staffspear.label` |
| `swordsmanship` | `swordsmanship` | `ref` | `WITCHER.skills.swordsmanship.label` |
| `courage` | `courage` | `will` | `WITCHER.skills.courage.label` |
| `hexweave` | `hexweave` | `will` | `WITCHER.skills.hexWeaving.label`; rollLabel=`WITCHER.skills.hexWeaving.rollLabel`; costMultiplier=2 |
| `intimidation` | `intimidation` | `will` | `WITCHER.skills.intimidation.label` |
| `spellcast` | `spellcast` | `will` | `WITCHER.skills.spellCasting.label`; rollLabel=`WITCHER.skills.spellCasting.rollLabel`; costMultiplier=2 |
| `resistmagic` | `resistmagic` | `will` | `WITCHER.skills.resistMagic.label`; rollLabel=`WITCHER.skills.resistMagic.rollLabel`; costMultiplier=2 |
| `resistcoerc` | `resistcoerc` | `will` | `WITCHER.skills.resistCoercion.label` |
| `ritcraft` | `ritcraft` | `will` | `WITCHER.skills.ritualCrafting.label`; rollLabel=`WITCHER.skills.ritualCrafting.rollLabel`; costMultiplier=2 |
| `archery` | `archery` | `dex` | `WITCHER.skills.archery.label` |
| `athletics` | `athletics` | `dex` | `WITCHER.skills.athletics.label` |
| `crossbow` | `crossbow` | `dex` | `WITCHER.skills.crossbow.label` |
| `sleight` | `sleight` | `dex` | `WITCHER.skills.sleightOfHand.label` |
| `stealth` | `stealth` | `dex` | `WITCHER.skills.stealth.label` |
| `alchemy` | `alchemy` | `cra` | `WITCHER.skills.alchemy.label`; rollLabel=`WITCHER.skills.alchemy.rollLabel`; costMultiplier=2 |
| `crafting` | `crafting` | `cra` | `WITCHER.skills.crafting.label`; rollLabel=`WITCHER.skills.crafting.rollLabel`; costMultiplier=2 |
| `disguise` | `disguise` | `cra` | `WITCHER.skills.disguise.label` |
| `firstaid` | `firstaid` | `cra` | `WITCHER.skills.firstaid.label` |
| `forgery` | `forgery` | `cra` | `WITCHER.skills.forgery.label` |
| `picklock` | `picklock` | `cra` | `WITCHER.skills.pickLock.label` |
| `trapcraft` | `trapcraft` | `cra` | `WITCHER.skills.trapCrafting.label`; rollLabel=`WITCHER.skills.trapCrafting.rollLabel`; costMultiplier=2 |
| `physique` | `physique` | `body` | `WITCHER.skills.physique.label` |
| `endurance` | `endurance` | `body` | `WITCHER.skills.endurance.label` |
| `charisma` | `charisma` | `emp` | `WITCHER.skills.charisma.label` |
| `deceit` | `deceit` | `emp` | `WITCHER.skills.deceit.label` |
| `finearts` | `finearts` | `emp` | `WITCHER.skills.fineArts.label` |
| `gambling` | `gambling` | `emp` | `WITCHER.skills.gambling.label` |
| `grooming` | `grooming` | `emp` | `WITCHER.skills.groomingAndStyle.label` |
| `perception` | `perception` | `emp` | `WITCHER.skills.humanPerception.label` |
| `leadership` | `leadership` | `emp` | `WITCHER.skills.leadership.label` |
| `persuasion` | `persuasion` | `emp` | `WITCHER.skills.persuasion.label` |
| `performance` | `performance` | `emp` | `WITCHER.skills.performance.label` |
| `seduction` | `seduction` | `emp` | `WITCHER.skills.seduction.label` |

### Таблица Crit

| ID травмы | Тяжесть | Локализации |
| --- | --- | --- |
| `crackedJaw` | simple | head |
| `disfiguringScar` | simple | head |
| `crackedRibs` | simple | torso |
| `foreignObject` | simple | torso |
| `sprainedArm` | simple | rightArm, leftArm |
| `sprainedLeg` | simple | rightLeg, leftLeg |
| `minorHeadWound` | complex | head |
| `lostTeeth` | complex | head |
| `rupturedSpleen` | complex | torso |
| `brokenRibs` | complex | torso |
| `fracturedArm` | complex | rightArm, leftArm |
| `fracturedLeg` | complex | rightLeg, leftLeg |
| `skullFracture` | difficult | head |
| `concussion` | difficult | head |
| `tornStomach` | difficult | torso |
| `suckingChestWound` | difficult | torso |
| `compoundArmFracture` | difficult | rightArm, leftArm |
| `compoundLegFracture` | difficult | rightLeg, leftLeg |
| `decapitated` | deadly | head |
| `damagedEye` | deadly | head |
| `heartDamage` | deadly | torso |
| `septicShock` | deadly | torso |
| `dismemberedArm` | deadly | rightArm, leftArm |
| `dismemberedLeg` | deadly | rightLeg, leftLeg |

Каждая запись имеет label, description, location[], severity и effect.none/stabilized/treated. В состояниях находятся локализованные описания и массивы stats/derived/skills с именем цели и строкой modifier; встречаются `-1`, `-2`, `/2`, `/4`, а также skillgroup и специальное skill=all. Пустые массивы означают отсутствие записи численного изменения в таблице, а не доказанное отсутствие последствий травмы. Файл эти строки не вычисляет.

Прямых обращений к WITCHER.Crit/CONFIG.WITCHER.Crit/config.Crit в проверенных JS и HBS не найдено. Актуальный просмотренный applyCritWound в damageMixin получает травмы из выбранного компедиума. Поэтому наличие этой таблицы не означает, что именно она управляет текущим лечением и штрафами. Динамический доступ не исключён.

### Заготовки statusEffects

| ID статуса | Число changes | Заданные данные |
| --- | --- | --- |
| `healing` | 1 | turnStartEffects.healing: heal.amount=3 |
| `buffed` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `fire` | 1 | turnStartEffects.fire: damage.amount=5, allLocations='true', type=fire, spDamage='1' |
| `stun` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `poison` | 1 | turnStartEffects.poison: amount=3, ignoreArmor/bypassesShield='true' |
| `disease` | 2 | skillGroupModifiers.disease: allSkills -2; derivedStats.sta.max ×0.75 |
| `prone` | 2 | attackModifier и defenseModifier: записи -2 |
| `bleed` | 1 | turnStartEffects.bleed: amount=2, ignoreArmor/bypassesShield='true' |
| `freeze` | 2 | stats.spd.totalModifiers -3; stats.ref.totalModifiers -1 |
| `staggered` | 2 | attackModifier и defenseModifier: записи -2 |
| `intoxication` | 13 | stats dex/ref/int: -2; десять записей skills.activeEffectModifiers: -3 (seduction, persuasion, leadership, charisma, deceit, socialetq, intimidation, resistcoerc, perception, gambling) |
| `hallucination` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `nausea` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `suffocation` | 1 | turnStartEffects.suffocation: amount=3, ignoreArmor/bypassesShield='true' |
| `blinded` | 3 | attackModifier/defenseModifier: override записей -2; awareness.activeEffectModifiers -5 |
| `shielded` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `invisible` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `unconscious` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `grappled` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `flying` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `frightened` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `aiming` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `deaf` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `reducedVision` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `holdAction` | 0 | Только id/name/img; изменений параметров в заготовке нет |
| `dead` | 0 | Только id/name/img; изменений параметров в заготовке нет |

`changes` содержат key, строковый type (add/multiply/override) и value; часть value — JSON-строки. Все JSON-объекты внутри строк разбираются без ошибки. Значения 'true', '1' и '-2' в части payload действительно строки; их приведение зависит от обработчиков. Уровень changes в заготовке и система хранения действующего ActiveEffect требуют обработки ядром; копирование заготовки не считается выполненным расчётом.

## Основные функции и методы

Функций, методов и callback нет. Есть присваивания объектам и создание ссылок между их частями. Единственное явное арифметическое выражение в справочниках — 1/3 для ducat; формулы урона и строки модификаторов сохраняются как данные. Сам файл не бросает кости и не применяет минимумы/максимумы характеристик.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| statMap, skillMap | Внутри этого файла | Ссылки на объекты | attribute, magic.skill, verbalCombat.skill/dmgStat | Прочитаны присваивания; импортов нет |
| Ключи локализации | [en](../../../../../../lang/en.json), [es](../../../../../../lang/es.json), [ptbr](../../../../../../lang/ptbr.json), [fr](../../../../../../lang/fr.json), [de](../../../../../../lang/de.json), [it](../../../../../../lang/it.json), [ru](../../../../../../lang/ru.json), [pl](../../../../../../lang/pl.json) | Семантическая ссылка по строке | Подписи и описания | Языки объявлены в system.json; полнота перевода всех ключей не проверялась |
| Формат статуса и changes | Foundry 14.367.0 | Внешний контракт данных | statusEffects | Прочитаны config.mjs, client/documents/active-effect.mjs и миграция change.mode→type в common/documents/active-effect.mjs |
| Поля навыков | [module/data/actor/templates/common/skills/intData.js](../../../../../../module/data/actor/templates/common/skills/intData.js); [module/data/actor/templates/common/skills/skillData.js](../../../../../../module/data/actor/templates/common/skills/skillData.js) | Строковые пути и имена | skillMap и changes.activeEffectModifiers | Модель объявляет commonsp и activeEffectModifiers |
| Поля параметров/боевых эффектов | [module/data/actor/templates/common/stats/statData.js](../../../../../../module/data/actor/templates/common/stats/statData.js); [module/data/actor/templates/common/combatEffectsData.js](../../../../../../module/data/actor/templates/common/combatEffectsData.js); [module/data/actor/commonActorData.js](../../../../../../module/data/actor/commonActorData.js) | Строковые пути | changes.totalModifiers, combatEffects, skillGroupModifiers | Проверены определения соответствующих полей; полный разбор моделей вне порции |
| Изображения статусов | `icons/svg/*` ядра и `assets/images/statusEffects/*` системы | Ресурсы | img в статусах | Вне границ пофайлового анализа |

## Известные потребители

| Файл-потребитель | Свойства WITCHER | Строки обращений | Способ использования |
| --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) | `statusEffects` | 31 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/activeEffect/mixins/baseMixin.js](../../../../../../module/activeEffect/mixins/baseMixin.js) | `statMap`, `skillGroups`, `skillMap` | 15, 17, 43, 45, 49, 72, 74 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js) | `skillMap` | 74, 76 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/mixins/castSpellMixin.js](../../../../../../module/actor/mixins/castSpellMixin.js) | `statMap`, `statusEffects` | 25, 221 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/mixins/currencyConverterMixin.js](../../../../../../module/actor/mixins/currencyConverterMixin.js) | `currency`, `currencyRates`, `currencyConverter` | 10, 12, 18, 19, 22, 32, 70, 94, 95 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/mixins/damageMixin.js](../../../../../../module/actor/mixins/damageMixin.js) | `damageTypes` | 212 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/mixins/defenseMixin.js](../../../../../../module/actor/mixins/defenseMixin.js) | `defenseOptions`, `skillMap`, `critLevel` | 23, 57, 136, 203, 224 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/mixins/modifierMixin.js](../../../../../../module/actor/mixins/modifierMixin.js) | `skillMap` | 4 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/mixins/professionMixin.js](../../../../../../module/actor/mixins/professionMixin.js) | `statMap` | 156, 361 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js) | `statMap`, `magicSkills`, `skillMap` | 8, 12, 43, 137 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js) | `verbalCombat` | 14, 38 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../module/actor/mixins/weaponAttackMixin.js) | `statMap`, `skillMap`, `weapon` | 134, 181, 185, 369 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) | `statMap`, `skillMap` | 34, 35, 105, 106, 107 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | `statMap`, `skillMap` | 15, 16, 80, 81, 82 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | `statMap`, `skillMap` | 7, 8, 57, 58 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | `statMap`, `skillMap` | 48, 49, 68, 69, 71, 72, 74 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | `skillMap` | 47 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js) | `armorEffects` | 46 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/app/reward/reward.js](../../../../../../module/app/reward/reward.js) | `currency` | 123, 124 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/data/item/hexData.js](../../../../../../module/data/item/hexData.js) | `skillMap`, `magic` | 24, 25, 26 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/data/item/ritualData.js](../../../../../../module/data/item/ritualData.js) | `skillMap`, `magic` | 41, 42, 43 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/data/item/spellData.js](../../../../../../module/data/item/spellData.js) | `skillMap`, `magic` | 64, 65, 66 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/data/item/templates/combat/attackOptionsData.js](../../../../../../module/data/item/templates/combat/attackOptionsData.js) | `meleeSkills`, `rangedSkills` | 9, 10, 39 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../module/data/item/templates/combat/defenseOptionsData.js) | `defenseOptions` | 6 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/mixins/consumeMixin.js](../../../../../../module/item/mixins/consumeMixin.js) | `statusEffects` | 25 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/mixins/damageUtilMixin.js](../../../../../../module/item/mixins/damageUtilMixin.js) | `weapon`, `statusEffects` | 35, 36, 37, 57 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/sheets/WitcherAlchemicalSheet.js](../../../../../../module/item/sheets/WitcherAlchemicalSheet.js) | `Availability` | 17 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/sheets/WitcherArmorSheet.js](../../../../../../module/item/sheets/WitcherArmorSheet.js) | `Availability` | 19 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/sheets/WitcherMutagenSheet.js](../../../../../../module/item/sheets/WitcherMutagenSheet.js) | `Availability` | 14 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/sheets/WitcherProfessionSheet.js](../../../../../../module/item/sheets/WitcherProfessionSheet.js) | `statTypes`, `skillMap` | 23, 27, 30 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/sheets/WitcherSkillItemSheet.js](../../../../../../module/item/sheets/WitcherSkillItemSheet.js) | `statMap` | 31, 32, 33 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/sheets/WitcherWeaponSheet.js](../../../../../../module/item/sheets/WitcherWeaponSheet.js) | `meleeSkills`, `rangedSkills`, `skillMap` | 21, 22, 23 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/sheets/investigation/WitcherClueSheet.js](../../../../../../module/item/sheets/investigation/WitcherClueSheet.js) | `skillMap` | 26 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/sheets/investigation/WitcherObstacleSheet.js](../../../../../../module/item/sheets/investigation/WitcherObstacleSheet.js) | `skillMap` | 26 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) | `statMap`, `skillMap` | 207, 333 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js) | `skillMap` | 67 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/scripts/investigation/rollClue.js](../../../../../../module/scripts/investigation/rollClue.js) | `skillMap` | 19 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/scripts/rolls/fumble.js](../../../../../../module/scripts/rolls/fumble.js) | `meleeSkills`, `rangedSkills` | 35, 49, 83 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | `statusEffects` | 79 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | `verbalCombat` | 25, 56 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/chat/item/partials/item-description/tags.hbs](../../../../../../templates/chat/item/partials/item-description/tags.hbs) | `Availability`, `Concealment`, `craftingLevels`, `weapon` | 16, 129, 133, 164, 316, 322 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/dialog/combat/profession-attack.hbs](../../../../../../templates/dialog/combat/profession-attack.hbs) | `damageTypes` | 19 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/dialog/combat/weapon-attack.hbs](../../../../../../templates/dialog/combat/weapon-attack.hbs) | `weapon` | 80 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs) | `homelands`, `socialStanding` | 10, 20, 47 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/partials/character/tab-profession.hbs](../../../../../../templates/partials/character/tab-profession.hbs) | `statTypes`, `socialStanding` | 21, 51, 74, 97, 123, 146, 169, 195, 218, 241, 303, 308, 313, 318, 323 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/partials/crit-wounds-table.hbs](../../../../../../templates/partials/crit-wounds-table.hbs) | `location`, `critLevel`, `critTreatment` | 13, 16, 18 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../templates/sheets/actor/monster-sheet.hbs) | `MonsterTypes`, `monsterDifficulty`, `monsterComplexity` | 101, 107, 113 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | `Availability` | 45 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | `craftingLevels` | 57 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | `Availability`, `Concealment` | 38, 42 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | `Concealment`, `weapon` | 65, 71 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | `location`, `critLevel`, `critTreatment` | 24, 27, 30 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../templates/sheets/actor/partials/monster/header.hbs) | `monsterDifficulty`, `monsterComplexity` | 14, 18 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs) | `statusEffects` | 8 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) | `statTypes` | 21 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/actor/rewards/currency.hbs](../../../../../../templates/sheets/actor/rewards/currency.hbs) | `currency` | 8 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/alchemical-sheet.hbs](../../../../../../templates/sheets/item/alchemical-sheet.hbs) | `Availability` | 21 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../templates/sheets/item/armor-sheet.hbs) | `Availability`, `armorEffects` | 39, 150, 167 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/component-sheet.hbs](../../../../../../templates/sheets/item/component-sheet.hbs) | `substanceTypes`, `Availability` | 21, 40 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs) | `attackOptions`, `meleeAttackOptions`, `rangedAttackOptions`, `spellAttackOptions` | 2, 9, 19, 30 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) | `attackOptions` | 2 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | `attackOptions`, `statusEffects` | 52, 69, 76 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) | `statusEffects` | 32, 53 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) | `statusEffects` | 45, 74 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](../../../../../../templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs) | `attackOptions` | 11 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/configuration/tabs/general.hbs](../../../../../../templates/sheets/item/configuration/tabs/general.hbs) | `attackOptions`, `meleeAttackOptions`, `rangedAttackOptions`, `spellAttackOptions`, `defenseOptions`, `damageTypes` | 4, 11, 21, 32, 38, 42 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | `defenseOptions`, `damageTypes`, `statusEffects` | 18, 40, 47, 48 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../templates/sheets/item/criticalWound-sheet.hbs) | `location`, `critLevel`, `critTreatment` | 10, 13, 16 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../../templates/sheets/item/diagrams-sheet.hbs) | `craftingLevels` | 29 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/enhancement-sheet.hbs](../../../../../../templates/sheets/item/enhancement-sheet.hbs) | `Availability`, `statusEffects`, `armorEffects` | 23, 57, 59 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/homeland-sheet.hbs](../../../../../../templates/sheets/item/homeland-sheet.hbs) | `homelands` | 8 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/profession-sheet.hbs](../../../../../../templates/sheets/item/profession-sheet.hbs) | `statTypes` | 31, 52, 64, 76, 92, 104, 116, 132, 144, 156 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/race-sheet.hbs](../../../../../../templates/sheets/item/race-sheet.hbs) | `socialStanding` | 58, 63, 68, 73, 78 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/valuable-sheet.hbs](../../../../../../templates/sheets/item/valuable-sheet.hbs) | `Availability`, `Concealment` | 17, 22 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |
| [templates/sheets/item/weapon-sheet.hbs](../../../../../../templates/sheets/item/weapon-sheet.hbs) | `Availability`, `Concealment`, `weapon` | 68, 77, 83 | Прямое обращение к WITCHER/CONFIG.WITCHER либо config в шаблоне |

Область поиска — все JS в module и HBS в templates. Строковые ключи локализации отделялись от обращений к объекту. Для шаблонов проверена передача CONFIG.WITCHER через базовые листы WitcherActorSheet, WitcherItemSheet и WitcherConfigurationSheet; достижимость каждого старого шаблона из текущего UI отдельно не доказывалась.

Динамические группы читают [module/actor/mixins/modifierMixin.js](../../../../../../module/actor/mixins/modifierMixin.js) (строка 28) и [module/activeEffect/mixins/baseMixin.js](../../../../../../module/activeEffect/mixins/baseMixin.js) (строки 43–50). Поэтому отсутствие буквального обращения к verbalCombatSkills/empatheticVerbalCombatSkills не означает отсутствие использования. В [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) объект публикуется целиком (строки 30–31); это общая связь для всех свойств.

## Данные и изменения состояния

Изменяется только создаваемый объект конфигурации в памяти. Модели Actor, Item и ActiveEffect здесь не создаются; загрузка компедиумов, лечение, обработка начала хода и запись документов выполняются потребителями. WITCHER.Crit, WITCHER.statusEffects и документы criticalWound — разные структуры; их нельзя приравнивать без прослеживания конкретного потребителя.

## Проверки и доказательства

Все 2431 строки прочитаны порциями 1–360, 361–710, 711–1110, 1111–1510, 1511–1935 и 1936–2431. Модуль без импортов загружен из его текста в Node: 36 свойств, 52 навыка, 24 записи Crit, 26 статусов, 4 свойства брони; JSON-строки изменений корректны. Собраны обращения к каждому свойству и проверены места передачи context.config. Для двух расхождений зависимых обработчиков выполнены изолированные проверки на настоящих данных WITCHER, описанные в карточках проблем.

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Не сверялись числа с рулбуками, полнота всех локализаций и применение каждого статуса в Foundry. Внутренние алгоритмы перечисленных потребителей разобраны только в местах связи. Отсутствие прямого потребителя Crit ограничено выполненным поиском; это не доказательство недостижимости при динамическом доступе. Строковые формулы здесь не дают основания утверждать порядок или ограничения фактического расчёта.

## Связанные проблемы

[issue-00003](../../../../../issues/potential/issue-00003.md) — обращение querySelector к массиву статусов в интеграции statuscounter.

[issue-00004](../../../../../issues/potential/issue-00004.md) — несовпадение ключа commonspeech и имени поля commonsp при выборе навыка эффекта.

## Дополнительная сверка навыков — TASK-0003.002

2026-09-10, HEAD `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d`; исходник не изменён.

Все 52 записи skillMap сопоставлены с семью группами реальной схемы CommonActorData по attribute.name/name: пути существуют, лишних или недостающих навыков не найдено. Полные группы и индекс путей из компедиумов — в [карточке skills](../data/actor/templates/common/skills/skillsData.js.md). Ключ commonspeech отличается от name=commonsp; дополненная [issue-00004](../../../../../issues/potential/issue-00004.md) содержит проявления в подсказках, конфигурации, кнопках, формулах и трёх JSON.

Сверка label/rollLabel с восемью языками обнаружила отсутствующие ключи picklock.label и trapcraft.label/rollLabel; подробности — [issue-00016](../../../../../issues/potential/issue-00016.md). Стоимость из magicSkills/skillMap используется в levelUpSkill; наблюдение расхода магических очков записано в [issue-00017](../../../../../issues/potential/issue-00017.md). Это уточнение потребителей справочника, не изменение его значений.

Результаты и пределы проверок — в [журнале TASK-0003.002](../../../review-log.md#task-0003002).

## Дополнительная сверка — TASK-0003.003

2026-09-10, HEAD `c34b790379fd98cd7e33ccbeeca085e49297a40f`; исходники не изменены.

Семь валют WITCHER.currency совпали со [схемой currency](../data/actor/templates/common/currencyData.js.md); rates содержит шесть ключей, falsecoin исключён из конвертера. Под [combatEffects](../data/actor/templates/common/combatEffectsData.js.md) обнаружены 11 изменений statusEffects: пять записей начала хода и шесть модификаторов атаки/защиты. Схема и передача damage/heal проверены; [issue-00021](../../../../../issues/potential/issue-00021.md) фиксирует потерю типа fire. Это наблюдение обработчика, значения config не исправлялись.

[Сценарии и результаты TASK-0003.003](../../../review-log.md#task-0003003).

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 2 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.

2026-09-10 — TASK-0003.002: уточнены связи моделей навыков и их потребителей, добавлены взаимные ссылки и фактические ограничения проверки.

2026-09-10 — TASK-0003.003: актуализированы связи с полностью разобранными структурами состояния Actor; ограничения полного клиента сохранены.

## Уточнение TASK-0003.004

2026-09-10, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26`. Сопоставлены homelands:585–612 (26 вариантов) с [homelandData](../data/actor/templates/character/general/homelandData.js.md) и двумя ветками Actor/Item в шаблонах; socialStanding:614–621 (6 вариантов) — с [generalData](../data/actor/templates/character/generalData.js.md) и addSocialStanding:85–132. Эти словари ограничивают варианты формы, но не StringField choices.

Семь типов [damageTypeModification](../data/actor/templates/character/general/damage/damageTypeModificationData.js.md) сопоставлены с damageTypes:733–768 (в конфигурации есть дополнительный silver). Отсутствие silver в схеме оставлено вопросом, а не объявлено ошибкой. Проверен 51 связанный ключ переводов en/ru после foundry.utils.expandObject; в том числе составной JSON-ключ background.other. Это соответствует нормализации загрузчика Foundry /opt/foundryvtt/client/helpers/localization.mjs:365–368.

[Перекрёстная сверка TASK-0003.004](../../../review-log.md#task-0003004).

## Уточнение TASK-0003.005

2026-09-10, `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609`. Сверены семь ключей WITCHER.currency с использованием type в [журнале валют](../data/actor/templates/character/currencyLogData.js.md) и lookup шаблона. Три пути getOtherSuggestions подтверждены в [attackStats](../data/actor/templates/character/attackStatsData.js.md). Проверены 11 ключей en/ru: Punch/Kick, подписи трёх числовых модификаторов, пяти полей журналов и SkillName. Конфигурация и схемы не менялись.

[Сверка TASK-0003.005](../../../review-log.md#task-0003005).

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. WitcherActor.prepareDerivedData читает WITCHER.armorEffects по id; modifierMixin читает skillMap и массивы групп. Положительный combatEffects.attackModifier/defenseModifier даёт строку без '+' (issue-00033). Среди 17 примесей addDefenseModifiers перезаписывается defenseMixin; другие повторяющиеся имена примесей не найдены.

Карточки: [WitcherActor](../actor/witcherActor.js.md), [modifierMixin](../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../review-log.md#task-0003007).

## Уточнение TASK-0003.008

2026-09-10, `c5edcbadd05ff4038a174bd2e2a49785e40ea878`; исходник не изменился относительно исходного среза. WitcherItem.getItemAttack:67 читает WITCHER.skillMap[attackSkill]?.label и возвращает ключ, не локализованный текст. Выбор варианта зависит от порядка Set attackOptions и ctrl/alt/shift, а не от порядка skillMap. При неизвестном skill отсутствует alias; методы Item не создают карту навыков.

Связанные карточки: [CommonItemData](../data/item/commonItemData.js.md) и [WitcherItem](../item/witcherItem.js.md). [Перекрёстная сверка](../../../review-log.md#task-0003008). Новая запись уточняет связи; исторические результаты прежних порций сохранены.

## Уточнение TASK-0003.009

2026-09-10, `a33bf33add228ae93f96a52046c8feb4ee992921`. Исходник не изменился относительно указанного ранее среза.

[module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js) превращает skillMap в 52 варианта выбора пути навыка; label служит ключом результирующего объекта. [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js) обращается к CONFIG.WITCHER.statusEffects как к DOM через querySelector, хотя это массив (issue-00003); ошибка возникает после toggle и до таймера снятия статуса по иммунитету. Определения turnStartEffects сверены с контекстом [templates/chat/combat/statusEffect.hbs](../../../../../../templates/chat/combat/statusEffect.hbs): renderer передаёт объект действия боя, шаблон только выводит img/name.

[Журнал сверки](../../../review-log.md) — TASK-0003.009; ограничения изолированного выполнения и неподтверждённые проблемы сохранены.
