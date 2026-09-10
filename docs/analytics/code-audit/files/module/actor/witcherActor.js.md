# module/actor/witcherActor.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.007](../../../../../tasks/task-0003.007.md), одна порция из двух файлов |
| Запись перекрёстной сверки | [TASK-0003.007](../../../review-log.md#task-0003007) |

## Назначение файла

Центральный документ Actor системы: расширяет Foundry Actor, рассчитывает характеристики и производные параметры, управляет статусами и предметами, предоставляет локации попаданий. Подключает 17 объектов примесей; схемы system определяются отдельными моделями.

## Условия использования

Default export WitcherActor extends глобальный Actor. [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js):12,33 назначает класс CONFIG.Actor.documentClass во время init. Это класс документа для всех типов Actor, а не модель только персонажа. Свои боевые вычисления prepareDerivedData пропускает для loot/mystery. Собственных defineSchema, constructor, prepareData, prepareBaseData, applyActiveEffects и getRollData здесь нет: они принадлежат ядру.

Файл целиком прочитан: 454 строки, 19 импортов, 19 собственных определений (getter, 16 методов экземпляра, два статических метода), 17 Object.assign. Примеси анализируются здесь на уровне экспорта, состава подключаемых методов и проверенных вызовов; полный разбор остальных mixin-файлов не выполнен.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherActor | class:21–436 | Документ Actor | Default export; CONFIG.Actor.documentClass | Наследование ядра, собственные методы и дополнение прототипа |
| temporaryEffects | getter:26–33 | Список временных эффектов для потребителей | Прототип WitcherActor | Добавляет эффекты предметов с system.isTransferred к списку родителя |
| 17 Object.assign | 438–454 | Подключение методов из примесей | WitcherActor.prototype | Копирует перечислимые свойства в указанном порядке; более позднее имя заменяет прежнее |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| get temporaryEffects:26–33 | super.temporaryEffects, items[].effects[] | Массив эффектов | concat всех isAppliedTemporaryItemImprovement из предметов | Без записи; добавленная часть сама не фильтрует disabled/transfer/isTemporary и не устраняет дубли. |
| prepareDerivedData:35–54 | Документ с моделью и предметами | undefined | super; выход loot/mystery; статусы экипированной брони; два calculateStats и производные расчёты | Память; applyStatus вызывается без await. Свои синхронные ошибки не перехватываются. |
| calculateStats:56–69 | stats, reputation | undefined | calculateStat для int/ref/dex/body/spd/emp/cra/will; прибавляет modifiers к luck/toxicity.max; reputation.value=max | Память; повторный вызов повторяет прибавки max. |
| calculateStat(stat):71–107 | Ключ одного из восьми stat; HP, healthState, броня/вес | undefined | Считает локальные модификаторы и делитель; floor результата | Записывает stats[stat].value и applied-флаги healthState; базой служит unmodifiedMax, не max. |
| calculateWeigthEncumbrance:109–121 | body.max/totalModifiers, enc.totalModifiers, getTotalWeight | Числовой штраф | При превышении вместимости ceil(разница/5), иначе0 | Без записи; написание Weigth сохранено. |
| calculateFixedDerivedStats:123–148 | Текущие stats и max, derivedStats.totalModifiers | undefined | Вычисляет шесть пар value/max, формулы ниже | Память; эффекты, ранее изменившие эти поля, могут быть перезаписаны. |
| calculateDerivedStats:150–156 | Модель | undefined | Пять вызовов calculateDerivedStat: hp, sta, resolve, focus, vigor | Память, последовательно. |
| calculateDerivedStat(stat):158–189 | Ключ показателя; BODY/WILL/INT; customStat | undefined | Автоматическая база hp/sta и max; специальные resolve/focus | Пишет unmodifiedMax для автоматических hp/sta, max и прежний totalModifiers; value не меняет. |
| calculateAttackStats:191–196 | stats.body.value, attackStats | undefined | Прибавляет бонус BODY и строит punch/kick | Память; += для meleeBonus, прямое присваивание строк ударов. |
| async applyStatus(effects):198–213 | Массив объектов statusEffect либо null/undefined | Promise<undefined> | Отбирает статусные записи, включает отсутствующие, проверяет иммунитет | toggleStatusEffect не ожидается; ошибка statusEffectId при непустых иммунитетах — issue-00031. undefined внутри массива не защищён. |
| async removeStatus(effects):215–223 | Массив объектов statusEffect | Promise<undefined> | Отключает найденные активные статусы | Без await toggle; входной массив обязателен, catch нет. |
| async useItem(itemId,options):225–243 | ID в this.items, опции оружия | Promise результата выбранной ветки либо undefined | Оружие→weaponAttack(item,options); spell/hex/ritual→castSpell(item); затем consumable→consume/removeItem | Неизвестный ID/прочий тип дают undefined. Первые две ветки возвращают Promise цели; consume/removeItem не ожидаются. |
| getTotalWeight:245–248 | items[].system.calcWeight?, system.calcCurrencyWeight | Math.ceil суммы | Сумма масс всех items плюс монеты; отсутствующий метод/результат предмета даёт0 через ?? | Не использует maxWeight, не фильтрует isStored самостоятельно. |
| getList(name):250–257 | Строка типа или shield | Отсортированный массив Items | Обычный тип: type==name && !isStored; shield: armor && location=='Shield'; sort по sort | В специальной ветке shield фильтра isStored нет; массив результата, не удаление документов. |
| async addItem(addItem,numberOfItem=1,forcecreate=false):259–273 | Item либо объект с name/type/system | Promise<undefined> | Первое совпадение name/type: увеличить quantity, если не stored и не forcecreate; иначе toObject/исходный объект и createEmbeddedDocuments | Ожидает update/create. В ветке raw object может менять переданный system.quantity; устанавливает количество только при truthy numberOfItem. Не возвращает созданный Item. |
| async removeItem(itemId,quantityToRemove):275–283 | Существующий Item, вычитаемое количество | Promise<undefined> | Если остаток<=0 — delete, иначе update quantity | Обе операции ожидаются; нет защиты неизвестного ID, отрицательного количества или нечислового значения. |
| async removeItemsOfType(type):285–290 | Тип Item | Promise<undefined> | Вызывает deleteEmbeddedDocuments со всеми ID этого типа, включая stored | Не возвращает/не ожидает удаление: issue-00034. |
| static getAllLocations:292–300 | Ожидает this.type/system для добавления хвоста | Массив имён локаций | Шесть стандартных, tailWing при monster && hasTailWing | Обычный вызов на классе не имеет экземпляра: issue-00032. |
| static getLocationObject(location):302–435 | Имя локации или randomHuman/randomMonster | {name,alias,formula,modifier} | Случайное распределение либо фиксированная таблица; локализация alias | Не пишет данные; RNG/getRandomInt и game.i18n; неизвестный ключ сохраняется в name с параметрами торса. |

### Формулы и поля

Обозначения: U — unmodifiedMax, V — value, X — max, T — totalModifiers; P — calculateWeigthEncumbrance(), A — getArmorEcumbrance(). Для восьми характеристик локальная добавка равна T; у REF/DEX вычитается A+2P, у SPD — P. При HP<=0 и !deathState.ignored делитель равен3 для всех восьми. Иначе при HP<woundTreshold.value и !woundThreshold.ignored делитель равен2 только у REF/DEX/INT/WILL; у остальных1. Результат floor((U+добавка)/делитель), без общего минимума1/максимума10. deathState.applied сбрасывается каждый вызов; woundThreshold.applied сбрасывается только в ветке вне deathState.

P = max(0, ceil((getTotalWeight()−((BODY.X+BODY.T)×10+ENC.T))/5)), с явной проверкой превышения до ceil. Собственная getArmorEcumbrance примеси суммирует encumb экипированной брони, вычитает lifepathModifiers.ignoredArmorEncumbrance и ограничивает снизу0. Источник BODY.X здесь отличается от BODY.U/V.

B=floor((BODY.V+WILL.V)/2), M=floor((BODY.X+WILL.X)/2). Полные фиксированные расчёты:

| Показатель | value | max |
| --- | --- | --- |
| stun | clamp(B,1,10)+T | clamp(M,1,10) |
| run | SPD.V×3+T | SPD.V×3 |
| leap | floor(SPD.V×3/5+T) | floor(SPD.X×3/5) |
| enc | BODY.V×10+T | BODY.V×10 |
| rec | B+T | M |
| woundTreshold | M+T | M |

Бонус stun прибавляется после clamp; это не ограничение конечного stun.value. Далее для hp/sta при !customStat исходная база становится B×5 и max=floor(B×5+T); при customStat max=U+T. Для resolve/focus при !customStat max=floor((WILL.V+INT.V)/2)×5/×3 соответственно, затем +T; при customStat max=U+T. У vigor max=U+T. shield здесь не рассчитывается. Текущие hp/sta/resolve/focus/vigor.value этот этап не обновляет.

Бонус ближнего боя C=ceil((BODY.V−6)/2)×2; attackStats.meleeBonus+=C, punch.value='1d6+'+C, kick.value='1d6+'+(4+C). Отрицательное C может дать строку 1d6+-4. Миграция meleeBonus и исходные максимумы описаны в CommonActorData, не определяются этим методом.

Массу конкретного предмета рассчитывает его модель: CommonItemData.calcWeight:18–20 возвращает quantity×weight только при isCarried && !isStored, иначе0; [ContainerData.calcWeight](../../../../../../module/data/item/containerData.js):17–19 при том же условии прибавляет storedWeight. Таким образом, отсутствие фильтра в getTotalWeight не означает, что он обязательно учитывает спрятанные предметы дважды; фильтрация делегирована модели. Полный расчёт содержимого контейнера остаётся вне этой порции.

### Локации

| Вход | formula | modifier | Распределение/alias |
| --- | --- | --- | --- |
| head | 3 | -6 | LocationHead |
| torso | 1 | -1 | LocationTorso |
| rightArm / leftArm | 0.5 | -3 | LocationRight/Left + LocationArm |
| rightLeg / leftLeg | 0.5 | -2 | LocationRight/Left + LocationLeg |
| tailWing | 0.5 | +0 | WITCHER.Dialog.attackTail |
| randomHuman | 3/1/0.5 | +0 | 1=head;2–4=torso;5=rightArm;6=leftArm;7–8=rightLeg;9–10=leftLeg |
| randomMonster | 3/1/0.5 | +0 | 1=head;2–5=torso;6–7=rightLeg;8–9=leftLeg;10=tailWing |
| Прочее | 1 | -1 | Alias торса; name остаётся входным неизвестным значением |

Случайные ветки используют WITCHER.Location.Random для alias; они не читают hasTailWing. getRandomInt(10) определён как floor(Math.random()×10)+1. Диапазон и распределение следуют из кода; случайные исходы проверялись подменой возвращаемого числа1–10.

### Подготовка и ActiveEffect

В Foundry14.367.0 сначала ClientDocument.prepareData вызывает system.prepareBaseData (у персонажа/монстра CommonActorData), затем Actor.prepareBaseData очищает overrides/statuses/учёт фаз, готовятся вложенные документы и вызывается applyActiveEffects('initial'). Затем system.prepareDerivedData, собственный WitcherActor.prepareDerivedData и после выхода из super.prepareData — applyActiveEffects('final'). Модели этой системы не переопределяют prepareDerivedData.

Собственная последовательность: статусы экипированной брони → calculateStats → calculateFixedDerivedStats → calculateStats → calculateDerivedStats → calculateAttackStats. Второй проход учитывает уже рассчитанный порог ран; при этом luck/toxicity.max прибавляются дважды (issue-00012). applyStatus получает элементы WITCHER.armorEffects по id: отсутствие совпадения оставляет undefined в массиве, собственная проверка этого случая не предусмотрена.

Actor.allApplicableEffects ядра включает собственные эффекты и эффекты Items с transfer=true. Далее ядро оставляет effect.active: !disabled && !isSuppressed. Системный WitcherActiveEffect.isSuppressed проверяет parent.system.isActive/equipped===false и флаги applySelf/applyOnTarget/applyOnHit/applyOnDamage. Дополнительный isDisabled системы не используется ядром active; duration.expired не читается переопределённым isSuppressed напрямую. Удаление истёкших эффектов — отдельный механизм, здесь не проверен.

Каждое system.changes[] выбирается по phase и непустому key, изменения всех подходящих эффектов сортируются по priority. Приоритеты по умолчанию ядра: multiply10, add20 (CONST.ACTIVE_EFFECT_CHANGE_TYPES); явный priority имеет значение. Числовые изменения обслуживает DataField.applyChange; нет общего принудительного правила «сложение перед умножением» в WitcherActor. applyAfterCalculations — поле системы; WitcherActiveEffect._preUpdate:114–118 преобразует его в phase переданных changes. Сам Actor читает phase, не эту галочку. Полный редактор и миграции эффектов — TASK-0003.009/010.

Изолированный исходный проход ядра с BODY.max8, multiply0.5/priority10, add2/20 и переносимым add3/20 дал9 в initial, финальный add1 дал10. Disabled, непереносимый Item-эффект и подавленный эффект не вошли в арифметику. Это проверка порядка на настоящих полях с адаптером применения изменений; не полный клиент. Изменение max в initial может быть проигнорировано при вычислении value или перезаписано производным расчётом — issue-00036.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| getRandomInt | [module/scripts/helper.js](../../../../../../module/scripts/helper.js) | Именованный импорт:1 | getLocationObject:308,346 | Определение:73–75; floor(random×max)+1. |
| WITCHER.armorEffects | [module/setup/config.js](../../../../../../module/setup/config.js); [карточка](../setup/config.js.md) | Импорт WITCHER:2 / чтение | prepareDerivedData:46 | Поиск записи id по statusEffect брони. |
| 17 объектов mixin | Точные исходники и имена в таблице ниже | Импорты:3–19 / Object.assign:438–454 | Добавление методов прототипа; вызовы weaponAttack/castSpell/getArmorEcumbrance | Все экспорты и имена проверены; полные тела остальных примесей не заявлены разобранными. |
| Actor; super.temporaryEffects; super.prepareDerivedData; allApplicableEffects; appliedEffects; getRollData | Foundry14.367.0: /opt/foundryvtt/client/documents/actor.mjs:149–168,212–274,305–315,325–327,428–473; client/documents/abstract/client-document.mjs:313–319 | Наследование / вызов | Документ и этапы подготовки | Прочитан код ядра; часть методов исполнена изолированно. |
| items/effects, update/createEmbeddedDocuments/deleteEmbeddedDocuments/toggleStatusEffect | Foundry Actor/ClientDocument API14.367.0; /opt/foundryvtt/client/documents/actor.mjs и abstract/client-document.mjs | Коллекции и операции документов | Действия с предметами/статусами | В сценариях записи подменены контролируемыми Promise; реальной БД нет. |
| Item.isConsumable, consume, system.calcWeight | [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js); [module/item/mixins/consumeMixin.js](../../../../../../module/item/mixins/consumeMixin.js); [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js) | Динамическое чтение / вызов | useItem:238–240; getTotalWeight:246 | isConsumable getter:72–73; consume:4; конкретную массу задаёт модель Item, общий метод calcWeight — commonItemData. |
| isAppliedTemporaryItemImprovement, isSuppressed | [module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js) | Динамические getters | temporaryEffects:30; фильтрация ядра | isTransferred:26–27; suppression:4–16; active ядра:210. |
| CommonActorData / CharacterData / MonsterData / LootData | [commonActorData](../data/actor/commonActorData.js.md), [characterData](../data/actor/characterData.js.md), [monsterData](../data/actor/monsterData.js.md), [lootData](../data/actor/lootData.js.md) | Регистрация моделей / чтение и изменение system | Поля расчётов, статусов, валют, инвентаря | Определения моделей и их статусы не смешаны с документом. |
| game.i18n.localize; ключи WITCHER.Armor.Location*, WITCHER.Location.Random, WITCHER.Dialog.attackTail | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json); Foundry Localization API | Глобальный API / строки | getLocationObject:343–424 | Точные ключи указаны в таблице локаций; перевод в runtime заменён меткой. |
| Number, Math.floor/ceil; Math.clamp; Set.find; Object.assign; setTimeout | ECMAScript; расширения /opt/foundryvtt/common/primitives/_module.mjs | Внешний API | Расчёты, коллекции статусов, подключение примесей | В проверках загружены primitives ядра; таймер не исполняет реальные статусы. |

### Полная карта подключаемых методов

| Порядок / строка | Импорт и источник | Подключаемые имена |
| --- | --- | --- |
| 1 / 438 | professionMixin — [module/actor/mixins/professionMixin.js](../../../../../../module/actor/mixins/professionMixin.js) | calc_total_skills_profession, _onProfessionRoll, doProfessionAttackRoll, doProfessionWeaponAttackRoll, doProfessionSkillUsage, doProfessionThreshold, doProfessionSkillRoll, findSkillWithName, findSkillWithNameInSkillPath |
| 2 / 439 | modifierMixin — [module/actor/mixins/modifierMixin.js](../../../../../../module/actor/mixins/modifierMixin.js) | addActiveEffects, addAttackModifiers, addDefenseModifiers |
| 3 / 440 | damageMixin — [module/actor/mixins/damageMixin.js](../../../../../../module/actor/mixins/damageMixin.js) | applyDamage, handleShield, applyDamageToLocation, applyDamageToAllLocations, updateDerivedStat, calculateDamageWithLocation, createDamageBlockedBySp, createDamageResultMessage, applyCritDamage, applyBonusCritDamage, applyCritWound, calculateHealingTime |
| 4 / 441 | damageUtilMixin — [module/actor/mixins/damageUtilMixin.js](../../../../../../module/actor/mixins/damageUtilMixin.js) | getFlatDamageMod, getMultiDamageMod |
| 5 / 442 | weaponAttackMixin — [module/actor/mixins/weaponAttackMixin.js](../../../../../../module/actor/mixins/weaponAttackMixin.js) | weaponAttack, constructBaseAttackFormula, mergeDamageProperties, handleAttackLocation, handleStrikeType |
| 6 / 443 | defenseMixin — [module/actor/mixins/defenseMixin.js](../../../../../../module/actor/mixins/defenseMixin.js) | prepareAndExecuteDefense, skillDefense, addDefenseModifiers, handleExtraDefense, handleLifepathModifier, createDefenseRollConfig, checkForStun, checkForCrit, handleCritLocation, handleDefenseResults, stunSave |
| 7 / 444 | healMixin — [module/actor/mixins/healMixin.js](../../../../../../module/actor/mixins/healMixin.js) | calculateHealValue, createHealMessage |
| 8 / 445 | castSpellMixin — [module/actor/mixins/castSpellMixin.js](../../../../../../module/actor/mixins/castSpellMixin.js) | castSpell, calcStaminaMulti |
| 9 / 446 | verbalCombatMixin — [module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js) | verbalCombat, createVerbalCombatFlags |
| 10 / 447 | locationMixin — [module/actor/mixins/locationMixin.js](../../../../../../module/actor/mixins/locationMixin.js) | getAllLocations, getLocationObject |
| 11 / 448 | temporaryEffectMixin — [module/actor/mixins/temporaryEffectMixin.js](../../../../../../module/actor/mixins/temporaryEffectMixin.js) | applyTemporaryItemImprovements |
| 12 / 449 | armorMixin — [module/actor/mixins/armorMixin.js](../../../../../../module/actor/mixins/armorMixin.js) | getArmorEcumbrance, getLocationArmor, getArmors, getArmorSp, getStackedArmorSp, getArmorDiffBonus, calculateArmorResistances, applySpDamage, applyAlwaysSpDamage, applySpDamageToItemArmor, applySpDamageToMonsterArmor |
| 13 / 450 | rewardsMixin — [module/actor/mixins/rewardsMixin.js](../../../../../../module/actor/mixins/rewardsMixin.js) | addIpReward, addCurrencyReward |
| 14 / 451 | craftingMixin — [module/actor/mixins/craftingMixin.js](../../../../../../module/actor/mixins/craftingMixin.js) | getSubstance, findNeededComponent, findComponentByUuid |
| 15 / 452 | currencyConverterMixin — [module/actor/mixins/currencyConverterMixin.js](../../../../../../module/actor/mixins/currencyConverterMixin.js) | handleCurrencyConverter, getCurrencyRates, openCurrencyConverter |
| 16 / 453 | adrenalineMixin — [module/actor/mixins/adrenalineMixin.js](../../../../../../module/actor/mixins/adrenalineMixin.js) | addAdrenaline |
| 17 / 454 | skillMixin — [module/actor/mixins/skillMixin.js](../../../../../../module/actor/mixins/skillMixin.js) | levelUpSkill, rollSkill, rollSkillCheck, addSocialStanding, rollCustomSkillCheck |

Один повтор имени среди примесей: addDefenseModifiers из modifierMixin перезаписан defenseMixin (443 после439). Их тела сейчас совпадают; оба определения сохранены в карте. Методы getAllLocations/getLocationObject примеси — методы экземпляра, а одноимённые методы класса статические: это два разных уровня, не перезапись статического метода. Других повторов между подключёнными именами не найдено.

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) | WitcherActor; useItem | Назначает CONFIG.Actor.documentClass; createMacro пишет команду fromUuidSync(...).useItem(...) | 12,33,157; макрос вызывается позднее. |
| [module/setup/queries.js](../../../../../../module/setup/queries.js) | addItem; applyTemporaryItemImprovements; addAdrenaline | Whitelist методов: fromUuidSync(uuid), entity[name] и entity.system[name] | 23–26,39–43; addItem собственный, остальные из двух примесей. Ответ true не ожидает операции: issue-00008. |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | applyTemporaryItemImprovements | Прямой вызов владельцем либо query другому владельцу | 70–79; специальный маршрут в queries:9–12. |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/WitcherLootSheet.js](../../../../../../module/actor/sheets/WitcherLootSheet.js) | getTotalWeight, getList, allApplicableEffects | Подготовка контекста инвентаря и эффектов | ActorSheet:87–91,162; LootSheet:48–61. |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../module/actor/sheets/mixins/itemMixin.js) | removeItemsOfType; addItem; useItem | Смена уникального Item, добавление/использование | 20,54,232,268; await удаления не ожидает БД (issue-00034). |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../module/actor/sheets/interactions/itemContextMenu.js); [module/actor/sheets/WitcherLootSheet.js](../../../../../../module/actor/sheets/WitcherLootSheet.js) | addItem/removeItem | Удаление, передача, покупка | contextMenu:56,144–149; LootSheet:155–156; не полный аудит межклиентской передачи. |
| [module/item/mixins/consumeMixin.js](../../../../../../module/item/mixins/consumeMixin.js); [module/actor/mixins/defenseMixin.js](../../../../../../module/actor/mixins/defenseMixin.js) | applyStatus/removeStatus | Потребление и снятие/наложение stun | consume:13–14; defense:406,454. |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js); [module/item/mixins/dismantlingMixin.js](../../../../../../module/item/mixins/dismantlingMixin.js); [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) | addItem/removeItem | Крафт, разбор, ремонт | Item:236,242; dismantling:36–38; repair:264. |
| [module/actor/mixins/locationMixin.js](../../../../../../module/actor/mixins/locationMixin.js); [module/item/mixins/damageUtilMixin.js](../../../../../../module/item/mixins/damageUtilMixin.js) | Статические getAllLocations/getLocationObject | Обёртки экземпляра / построение локации урона Item | location:4–9; Item damageUtil:40. |
| [module/actor/mixins/damageMixin.js](../../../../../../module/actor/mixins/damageMixin.js) | getList/addItem; getAllLocations/getLocationObject через примесь | Повреждения, критическая травма, урон всем локациям | 85–86,336; вызовы локаций прослежены до static. |

Область поиска — module/, templates/, packsJson/ и относящееся к жизненному циклу локальное ядро. getList также вызывают специализированные листы и многие примеси, перечисленные в карте; чтение типа через getList не равнозначно созданию предмета. game.TheWitcherTRPG в module/ не найден: фактический публичный объект — game.api, чьи rewards вызываются rewardsMixin и обслуживаются Rewards; Actor как конструктор хранится в CONFIG.Actor.documentClass. Внешние макросы и модули мира не исследованы.

## Данные и изменения состояния

Расчёты изменяют подготовленный system в памяти; собственный расчёт не сохраняет числовые значения через update. Однако prepareDerivedData вызывает applyStatus, а тот вызывает документный toggleStatusEffect, то есть весь метод нельзя описывать как полностью лишённый внешних действий. Add/remove Items используют документные create/update/delete; useItem делегирует оружие/магию/потребление. Асинхронная сигнатура сама по себе не означает ожидание всех вложенных действий.

getList/addItem сравнивают тип/имя, не ID источника компедиума. addItem берёт первое совпадение, даже если оно stored; последующее условие тогда создаёт новый Item, не ищет другое совпадение. Forcecreate всегда выбирает создание. RemoveItemsOfType захватывает ID до удаления. Эти особенности зафиксированы как контракт текущего кода; не все признаны ошибками.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота класса/примесей | 454 строки, исходный класс в vm с родителем-двойником; оригинальные объекты 17 примесей | 19 собственных определений, карта всех экспортированных имён, один совпадающий addDefenseModifiers | Собственные тела сохранены; импортируемые зависимости, не нужные в сценариях, не исполнялись. |
| Подготовка/здоровье | Настоящая CharacterData, исходные методы Actor; BODY/WILL/etc8; HP40/7/0 | INT8/4/2; BODY8/8/2. Порядок: stats→fixed→stats→derived→attacks; loot/mystery выходят | Без полноценного Foundry Actor и сетевых статусов. |
| Перегруз | BODY.max8, масса81, броня0, прочие modifiers0 | P1; REF6,DEX6,SPD7 из исходных8 | Повторное вычитание подтверждено; соответствие правилу не оценено. |
| Строки и грамматика | Исходные modifierMixin/constructBaseAttackFormula; реальная grammar.pegjs, peggy и RollParser ядра | Отрицательный/нулевой modifier парсятся; положительный даёт SyntaxError без '+' | Без Roll.evaluate, кубов и сообщений. |
| Операции предметов | Оригинальные методы; контролируемые update/delete/create Promise | addItem ожидает update. removeItemsOfType возвращается до удаления; добавление одноимённого Item меняет старый, затем его удаление оставляет0 | Имитирована только граница записи, не серверная конкуренция. |
| Фазы | Исходные core applyActiveEffects/allApplicableEffects/shouldApplyChange/applyChangeField; настоящие NumberField | multiply→add→transfer add в initial; final add позднее; suppression/disabled проверены | Static applyChange заменён адаптером к оригинальному applyChangeField; legacy shim отключён для современных входов. |
| Изменения max | Нормализованные числовые initial multiply0.25 по трём путям Heart Damage; реальный расчёт Actor | SPD/BODY.max2, value8; STA.max10 до расчёта и40 после | Не импорт JSON-документа в мир; действующий packs не читался. |
| Локации | 8 прямых входов, перебор RNG1–10 двух веток | Таблицы соответствуют исходнику; неизвестный name сохраняется | Распределение RNG не статистически тестировалось. |

## Непроверенные участки и открытые вопросы

Файл полностью прочитан. Не выполнены полный жизненный цикл Foundry Document, мир, БД, браузер, сетевые Queries, наследуемые операции токенов и все боевые методы примесей. Полная инвентарная модель и миграции/редактор ActiveEffect остаются TASK-0003.008–010 и последующим порциям. Наличие max и value не трактуется как согласованный новый алгоритм характеристик. Поведение raw objects и неожиданных ID описано по ветвям кода, не исчерпывающему перебору входов.

## Связанные проблемы

- [issue-00008](../../../../../issues/potential/issue-00008.md) — query не ждёт операций Actor.
- [issue-00012](../../../../../issues/potential/issue-00012.md) — повторная прибавка luck/toxicity.max.
- [issue-00031](../../../../../issues/potential/issue-00031.md) — неопределённый ID при проверке иммунитетов.
- [issue-00032](../../../../../issues/potential/issue-00032.md) — потерянный this монстра в static getAllLocations.
- [issue-00033](../../../../../issues/potential/issue-00033.md) — положительные модификаторы формул без знака операции.
- [issue-00034](../../../../../issues/potential/issue-00034.md) — преждевременное завершение операций Actor с предметами.
- [issue-00035](../../../../../issues/potential/issue-00035.md) — двойной штраф перегруза REF/DEX.
- [issue-00036](../../../../../issues/potential/issue-00036.md) — изменения max эффектами не доходят до value либо перезаписываются подготовкой.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.007 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.008

2026-09-10, `c5edcbadd05ff4038a174bd2e2a49785e40ea878`; исходник не изменился относительно исходного среза. Полный разбор основы Item уточнил getTotalWeight: общая модель считает quantity×weight только при isCarried && !isStored, ContainerData добавляет storedWeight, независимые модели могут не иметь calcWeight. isConsumable документа — system.isConsumable ?? false, а не проверка типа. В realCraft сам Item не ожидает Actor.addItem/removeItem, хотя эти методы Actor ожидают свою запись (issue-00038). Item-эффекты обрабатываются до производных данных модели одним проходом без phase, в отличие от Actor. При точечной проверке applyTemporaryItemImprovements установлена потеря system.changes в передаваемом объекте (issue-00042); полный разбор примеси отложен.

Связанные карточки: [CommonItemData](../data/item/commonItemData.js.md) и [WitcherItem](../item/witcherItem.js.md). [issue-00038](../../../../../issues/potential/issue-00038.md); [issue-00042](../../../../../issues/potential/issue-00042.md). [Перекрёстная сверка](../../../review-log.md#task-0003008). Новая запись уточняет связи; исторические результаты прежних порций сохранены.

## Уточнение TASK-0003.009

2026-09-10, `a33bf33add228ae93f96a52046c8feb4ee992921`. Исходник не изменился относительно указанного ранее среза.

Полностью разобрана примесь [module/actor/mixins/temporaryEffectMixin.js](../../../../../../module/actor/mixins/temporaryEffectMixin.js): один подключённый метод выбирает weapon и создаёт embedded ActiveEffect на Item; Actor.temporaryEffects лишь добавляет эффекты с isTransferred в возвращаемый список. Исходная передача теряет system.changes, что теперь проверено также настоящей моделью Foundry (issue-00042). Полный [module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js) уточнил фазу _preUpdate: Actor использует change.phase, а обработчик частичного обновления может назначить initial или упасть при отсутствии changes (issue-00043). Отдельный [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js) не тождественен собственному applyStatus: у него локальный statusEffectId определён, но есть другие ветви иммунитета/disabled (issues-00003/00049). Полный интерфейс остаётся TASK-0003.010.

[Журнал сверки](../../../review-log.md) — TASK-0003.009; ограничения изолированного выполнения и неподтверждённые проблемы сохранены.

## Уточнение TASK-0003.010

2026-09-10, `247d3d86e344238a1445377c686eb6455146693c`; исходник прежнего среза не изменён.

Уточнена цепочка отображения: Actor-листы готовят allApplicableEffects плюс переданные улучшения, [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../../module/actor/sheets/mixins/activeEffectMixin.js) группирует их, а [templates/partials/effect-part.hbs](../../../../../../templates/partials/effect-part.hbs) скрывает suppressed-строки при наличии actor. Открытие/toggle Item-эффекта разрешаются по его parent.uuid, удаление из чужого родителя блокируется собственным обработчиком. Изменение состояния документа остаётся API ядра; шаблон не исполняет бонусы.

[Общая сверка первой серии](../../../review-log.md) — TASK-0003.010. Полный клиент и БД не запускались.

## Уточнение TASK-0003.012

2026-09-10, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9`; исходник не изменён. Связи импортированных mixin уточнены по [DamageProperties](../../../../../../module/data/item/templates/combat/damagePropertiesData.js), [DefenseProperties](../../../../../../module/data/item/templates/combat/defensePropertiesData.js) и [SpData](../../../../../../module/data/item/templates/armor/spData.js). defenseMixin отбирает предметы через system.isApplicableDefense(attack.attackOption), затем Item.createDefenseOption; модель защит сама возвращает только modifier и пустые skills/itemTypes. weaponAttackMixin добавляет контекстные effects в подготовленную модель предмета. Сопоставление с моделями выявило [issue-00066](../../../../../issues/potential/issue-00066.md), [issue-00069](../../../../../issues/potential/issue-00069.md), [issue-00070](../../../../../issues/potential/issue-00070.md) и [issue-00073](../../../../../issues/potential/issue-00073.md). Это точечная сверка функций-потребителей, не их полный пофайловый разбор.

Результат и границы — [сверка TASK-0003.012](../../../review-log.md#task-0003012).

## Уточнение TASK-0003.014

2026-09-10, `0fa589bd300856ff309f362afcb66d6fa43401ab`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003014).

После полного разбора [module/data/item/armorData.js](../../../../../../module/data/item/armorData.js) и [module/data/item/templates/itemEffectData.js](../../../../../../module/data/item/templates/itemEffectData.js) проверена фактическая ветвь prepareDerivedData брони. map(system.effects).flat() не разворачивает TypedObjectField; заполненное effects.own.statusEffect=fire дало [] для applyStatus ([issue-00084](../../../../../issues/potential/issue-00084.md)). Контроль со старым массивом дошёл до CONFIG.armorEffects, но эти записи имеют id, а applyStatus требует statusEffect; реальный метод не вызвал перехваченный toggleStatusEffect ([issue-00089](../../../../../issues/potential/issue-00089.md)). Поэтому прежнее описание порядка «статусы брони → расчёты» является порядком вызовов, а не подтверждением применения статусов. getList('shield') отдельно отбирает Item.armor по location='Shield'; ошибка дополнительной защиты не отменяет этот путь.

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003015).

Полностью прослежен потребитель [module/item/mixins/consumeMixin.js](../../../../../../module/item/mixins/consumeMixin.js). useItem проверяет item.isConsumable, запускает consume() и removeItem(id,1) без ожидания обоих. Настоящий removeItem при quantity2 запросил update1; при quantity1 и контролируемой задержке calculateHealValue запросил delete до продолжения consume. Отсутствующий затем UUID источника попал в GM query helper. Это возможный порядок с фасадами, не проверка частоты в мире. applyStatus/removeStatus принимают массивы {statusEffect}, игнорируют percentage/varEffect и не ждут toggle; UI расходования использует именно такие массивы. Дефекты иммунитетов и раннего завершения описаны существующими issues, а разрыв коллекции брони не переносится на эту массивную схему.

## Уточнение TASK-0003.016

2026-09-10, `53f74994011383cb544cabac96285430f00cb38a`; исходник неизменен. [Перекрёстная сверка](../../../review-log.md#task-0003016).

Уточнены потребители полей [module/data/item/componentData.js](../../../../../../module/data/item/componentData.js) и [module/data/item/templates/craftingComponentData.js](../../../../../../module/data/item/templates/craftingComponentData.js). Примесь [module/actor/mixins/craftingMixin.js](../../../../../../module/actor/mixins/craftingMixin.js) предоставляет getSubstance/findNeededComponent/findComponentByUuid. Реальные методы с модельными компонентами показали: поиск имени включает isStored=true, getSubstance исключает сохранённую субстанцию, UUID-метод сравнивает _stats.compendiumSource. Изготовление использует поиск по имени; ремонт сначала ищет имя, затем разрешает UUID недостающего материала. Это разные критерии, не эквивалентные способы найти один Item; общий контракт инвентаря не менялся.

## Уточнение TASK-0003.017

2026-09-10, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; исходники неизменны. [Сверка](../../../review-log.md#task-0003017).

[RepairSystem](../../../../../../module/item/systems/repair.js) вызывает findNeededComponent из [craftingMixin](../../../../../../module/actor/mixins/craftingMixin.js) и выбирает первый Item, затем _doRepair вызывает removeItem(_id,1) для каждой owned-записи. removeItem:275–283 действительно ждёт delete/update; потеря ожидания находится у caller ремонта, а не в этом методе. При artisan списывается его инвентарь, предмет принадлежит owner. Подбор включает quantity0/isStoredtrue; нулевое количество UI показывает как нехватку, но guard не проверяет ([issue-00104](../../../../../issues/potential/issue-00104.md)). Списания кошелька в пяти ремонтных файлах нет.
