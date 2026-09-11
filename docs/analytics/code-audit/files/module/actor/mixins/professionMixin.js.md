# module/actor/mixins/professionMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.038](../../../../../../tasks/task-0003.038.md), 4 файла, 965 логических строк |
| Запись перекрёстной сверки | [TASK-0003.038](../../../../review-log.md#task-0003038) |

## Назначение файла

Девять методов Actor для суммы и поиска профессиональных навыков, выбора пути применения, броска, профессиональной атаки и временного здоровья. Источником служит первая не помещённая на хранение профессия Actor по sort; основное дерево и ветви хранятся в Item.

## Условия использования

Импорт professionMixin в witcherActor.js:12 и Object.assign:438. skillListener примеси листа вызывает Actor._onProfessionRoll по клику .profession-roll. CharacterSheet использует calc_total_skills_profession при подготовке totalProfSkills. Собственной проверки GM/ownership нет; сохранение и query зависят от вызываемого API.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| professionMixin | named export let:8–415 | Девять методов Actor | Object.assign(WitcherActor.prototype,professionMixin) | Вызовы из листов/программно |
| DialogV2 | local const:6 | API окон | prompt для атаки/оружия/порога | callback возвращает значения формы; rejectClose:true |
| attack/damage/messageData | Локальные объекты | Контекст броска и payload attack-чата | doProfessionAttackRoll | Не отдельные документы до toMessage |
| Встроенные callbacks | prompt.ok, filter/map/forEach | Чтение checked/value, сбор оружия/порогов | Методы примеси | forEach не организует ожидание внешних операций |
| newEffect/queryData | doProfessionSkillUsage | Временные HP и query | queryData заполняется, но не используется при вызове | Actual query передаёт target.uuid и массив ActiveEffect |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| calc_total_skills_profession() | getList(profession)[0] | Number | Суммирует Number(level) definingSkill и 9 ветвей | Нет профессии→0; порядок/скрытые/нулевые уровни не фильтрует; иных профессий не суммирует |
| _onProfessionRoll(event) | Ближайший .profession-display.dataset.name | Promise<void> | findSkillWithName(name).skill; приоритет isAttack→hasCustomEffect→hasThresholds→обычный бросок | Нет await/return делегированного метода; unknown/нет профессии→TypeError |
| doProfessionAttackRoll(skill) | skillAttack; stat/level Actor; usesWeapon branch | Promise<void> либо делегированное завершение chooser | Без оружия: формулы, HBS, prompt,14 значений, damage/location, attack ChatMessageData, await extendedRoll | Отмена→rejection; специальный isExtraAttack штрафует−3 без списания STA; attack.name отсутствует |
| doProfessionWeaponAttackRoll(skill) | Item weapon с первым attackOptions способности | Promise<void> | Фильтрует .system.attackOptions.has(first); select choosen; передаёт weaponAttack(skillReplacement,additionalDamageProperties) | Нет ожидания weaponAttack, проверки пустого списка/исчезнувшего Item; остальные attackOptions не предлагают выбор |
| doProfessionSkillUsage(skill) | skillUsage; this либо targets.first().actor | Promise<void> | applyOnTarget определяет цель; HP: threshold=target.stat.max×multiplier; skillRoll(showResult:false); toMessage; при rollOver>0 создаёт effect и query владельцу | applySelf не читается; hasCustomEffect/addTemporaryHealth разводятся dispatcher/методом; toMessage/query не ожидаются |
| doProfessionThreshold(skill) | thresholds.thresholds словарь | Promise<void> | Одна запись без окна; иначе select id=threshold; берёт name/value и вызывает skillRoll | Пустой/пропавший key→TypeError; select по id доступен form.elements; вызов броска без return/await |
| doProfessionSkillRoll(skill, {threshold,thresholdDesc,showResult=true}={threshold:0,showResult:true}) | stat по skill.stat, level\|\|0; getCustomModifier | Promise<Roll> | 1d10+stat.value+level+custom; ChatMessageData(this.actor); RollConfig showCrit=true, threshold/desc/showResult; return extendedRoll | Unknown stat падает до prompt; this.actor у Actor отсутствует → speaker fallback. Без аргумента threshold0, с объектом без threshold —undefined |
| findSkillWithName(skillName) | Первая профессия | {skill,path} либо undefined | Точное совпадение definingSkill, затем пути 1/2/3; внутри путь 1/2/3 | Совпадения имён/пустые имена выбирают первое; найденный путь проверяется дважды; без профессии не защищён |
| findSkillWithNameInSkillPath(skillPath,skillName) | Объект трёх навыков | {skill,path} либо null | Сравнивает skill1→skill2→skill3 | Сам не проверяет отсутствующий skillPath; не меняет данные |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| extendedRoll | [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | Named import:1 | Броски skill/attack | Настоящий Roll; threshold строгий > для обычного броска; showResult:false возвращает messageData |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js) | Named import:2 | doProfessionSkillRoll | Устанавливает showCrit/threshold/thresholdDesc/showResult; attack использует defaults |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | Default import:3 | Формирует speaker/flavor/type/system | Attack передаёт this; skill передаёт this.actor |
| getActorOwner/getCustomModifier | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | Named import:4 | Получатель query/отдельный prompt модификатора | Owner: active non-GM OWNER, иначе activeGM; prompt возвращает строку и addPart |
| WitcherActor/getList/getLocationObject | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Смешивание/динамические методы | Первая не помещённая на хранение профессия, статические локации | getList250+ сортирует sort; getLocationObject302+; обёртка locationMixin |
| locationMixin.getLocationObject | [module/actor/mixins/locationMixin.js](../../../../../../../module/actor/mixins/locationMixin.js) | Делегирование Actor→static | Атака,210 | torso−1, head−6, arm−3, leg−2; random через getRandomInt |
| modifierMixin.addActiveEffects | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | Динамический вызов | attack.name158 | У attack определены skill/alias, name нет; addActiveEffects(undefined) возвращает пусто |
| weaponAttack/mergeDamageProperties | [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | Динамическое делегирование | skillReplacement и additionalDamageProperties | Обычная база/stat заменяются; ветка оружия использует свои cost/ammo/strike/properties; effects object не объединяется |
| prepareAndExecuteDefense | [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | Последующий потребитель | Защита по сообщению | Дополнительные защиты отбираются у Item.system; проф-примесь сама защиту не отправляет |
| ProfessionData/professionPath/professionSkill | [module/data/item/professionData.js](../../../../../../../module/data/item/professionData.js); [module/data/item/templates/professionPathData.js](../../../../../../../module/data/item/templates/professionPathData.js); [module/data/item/templates/professionSkillData.js](../../../../../../../module/data/item/templates/professionSkillData.js) | Данные | Все ветви/поиск/levels | definingSkill плюс 3×3; произвольные String name/stat |
| SkillUsage/TemporaryHealth/Threshold | [module/data/item/templates/profession/skillUsageData.js](../../../../../../../module/data/item/templates/profession/skillUsageData.js); [module/data/item/templates/profession/temporaryHealthData.js](../../../../../../../module/data/item/templates/profession/temporaryHealthData.js); [module/data/item/templates/profession/thresholdData.js](../../../../../../../module/data/item/templates/profession/thresholdData.js) | Вложенные модели | Цель, DC,HP и пороги | Настоящие модели в сценариях |
| skillAttack/attackOptions/defenseOptions/DamageProperties | [module/data/item/templates/combat/skillAttackData.js](../../../../../../../module/data/item/templates/combat/skillAttackData.js); [module/data/item/templates/combat/attackOptionsData.js](../../../../../../../module/data/item/templates/combat/attackOptionsData.js); [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../../module/data/item/templates/combat/defenseOptionsData.js); [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | Данные атаки | Set вариантов; damageFormulaOverride/applyMeleeBonus/properties | deepClone в direct attack; передача модели в weaponAttack |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../module/setup/config.js) | Глобальная конфигурация | statMap/damageTypes и подписи | stat/skill maps и locale labels; неизвестный stat не защищён |
| displayRollsDetails | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | Setting | Вид подписей формул | Меняет аннотации, не ожидаемые суммы |
| profession-attack.hbs | [templates/dialog/combat/profession-attack.hbs](../../../../../../../templates/dialog/combat/profession-attack.hbs) | renderTemplate | Прямой путь 87–90 | attackSkill/displayDmgFormula/meleeBonus/config |
| registerQueries/applyActiveEffectToActor | [module/setup/queries.js](../../../../../../../module/setup/queries.js); [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | query/API | TheWitcherTRPG.query function applyActiveEffectToActor | data:[target.uuid,[newEffect]]; clone у получателя, затем createEmbeddedDocuments |
| TemporaryEffects | [module/data/actor/templates/common/temporaryEffectsData.js](../../../../../../../module/data/actor/templates/common/temporaryEffectsData.js) | Путь назначения effect | temporaryHp.<skillName> → name/value | Схема ожидает числовой value; не прямой прирост derivedStats.hp |
| AttackMessageData/damageData/attackData | [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js); [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js); [module/data/chatMessage/templates/attackData.js](../../../../../../../module/data/chatMessage/templates/attackData.js) | Тип сообщения | attack, damage, defenseOptions, rollTotal | attack.itemUuid/damage.itemUuid отсутствуют в producer; лишнее damage.item не входит в schema |
| attackChatMessageListeners/onDamage/executeDefense | [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) | Потребитель сообщения | Кнопка damage/контекст защиты | onDamage требует attack.itemUuid; defense читает attackRoll/options/damage/attacker |
| ActiveEffect/миграция | Foundry14.367.0: common/documents/active-effect.mjs:152–241 | Конструктор/совместимость | changes(mode2)/duration.rounds — старый ввод | Реальная migrateData преобразует system.changes/type/value и duration; icon не превращается в img |
| WitcherActiveEffectData/регистрация | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js); [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js); [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Тип/документ эффекта | baseType + apply flags; CONFIG.ActiveEffect.documentClass | Полный lifecycle конструктора не исполнялся |
| DialogV2, Roll, fromUuid, User.query | Foundry14.367.0 | Внешние API | prompt, dice, message/query; DOM .checked/.value | Реальный Roll и данные; окна/query/запись — фасады |
| Локализация | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Текст/подписи | WITCHER.Dialog/Attack/Armor/table/profession | expandObject и core Localization/fallback; имена способности — пользовательские строки |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | professionMixin | import12/Object.assign438 | Методы на Actor |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | calc_total_skills_profession | _prepareCharacterData170 | totalProfSkills |
| [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | _onProfessionRoll | skillListener31; стрелочный callback к Actor | Клик .profession-roll |
| [templates/partials/character/tab-profession.hbs](../../../../../../../templates/partials/character/tab-profession.hbs) | Данные выбора навыка | data-name используется через listener | Кнопки десяти навыков |
| [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) | Данные выбора навыка | Одна кнопка definingSkill через тот же listener | Нет отдельных методов монстра |
| [templates/dialog/combat/profession-attack.hbs](../../../../../../../templates/dialog/combat/profession-attack.hbs) | Контекст direct attack | Поля читаются callback по name | 14 полей |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Обычный бросок: 1d10+stat.value+(level||0)+custom. Нет явного чтения связанных базовых навыков/их activeEffectModifiers, общего addAttackModifiers или skillDefense. Эффекты, уже вошедшие в stat.value, остаются учтёнными. Порог проверяется extendedRoll; equality не успех, rollOver=total−threshold. Ни один собственный метод не расходует STA; только вызываемый weaponAttack содержит собственное списание 3 для extra.

Direct attack: damageFormulaOverride плюс meleeBonus при applyMeleeBonus и (character либо addMeleeBonus). Прочие атака-модификаторы: targetOutsideLOS−3, outsideLOS+3, isExtraAttack−3, isProne−2, isPinned+4, isActivelyDodging−2, isMoving−3, isAmbush+5, isBlinded−3, isSilhouetted+2; customAtt/customDmg строки добавляются через "+", если != "0". Пустые custom значения не валидируются. Потом modifier выбранной локации. damage содержит properties clone, crit modifiers, type, formula, location/originalLocation; attackOption берётся первым из Set. Не читаются отдельные meleeAttackSkill/rangedAttackSkill/spellAttackSkill/itemUseAttackSkill, не добавляется itemUuid. Переданный meleeBonus для UI не учитывает monster.addMeleeBonus, хотя формула учитывает.

HP: цель — первая выбранная, только если applyOnTarget, иначе this при любом applySelf. При addTemporaryHealth DC=target.stats[configured stat].max×multiplier. Бросок выводится вручную; только положительный rollOver даёт эффект. duration: replace первого @level→match(/\d+\*?\d+/g)[0]→eval; это не общий парсер выражений. value: строковое соединение min(rollOver,maxRollOver)+temporaryHp.value; только наличие "d" запускает Roll.evaluate. Не-dice "+2" остаётся выражением в вручную собранном JSON. Имя также вставляется без JSON escaping и входит в dotted key. В эффекте origin=this.uuid, icon=profession.img, changes ADD temporaryHp.<skillName>, duration.rounds. Query владельцу не ожидается. HP не меняются до обработки эффекта получателем; повтор/stack/expiry и реальная сеть здесь не доказаны.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Основной API | Группы 01–06 | Первая профессия, поиск/приоритет, отмена, реальные skill Rolls и speaker fallback | Dispatcher отсоединяет Promise; ошибки прямых методов проверены отдельно |
| Атаки/данные сообщения | Группы 07–12/21 | Формулы/модификаторы/STA, фильтр оружия; реальная AttackMessageData не получает UUID | Запись/weaponAttack в основном делегирующем тесте заменены; полный урон не выполнен |
| HP/пороги/защита | Группы 13–17/22–24 | Успех/равенство, цели,cap, duration/JSON, существующие 71/72; core migrations | ActiveEffect/query — фасады; отдельная migrateData настоящая |

## Непроверенные участки и открытые вопросы

Полностью прочитан файл; соседние определения проверены в пределах вызовов. 24 группы изолированных сценариев: реальные модели/методы, Roll/extendedRoll, Handlebars 4.7.9 и отдельные функции ядра Foundry 14.367.0 на Node24.16.0. Dialog, DOM/Application, ActiveEffect-конструктор, запись Actor/Item/ChatMessage и query — фасады. Core миграция ActiveEffect выполнена отдельно на payload. Браузерные события/валидация/сохранение, полный жизненный цикл эффекта, HTTP, БД и несколько клиентов не запускались. Игровые требования сверх кода не выбирались.

## Связанные проблемы

[issue-00008](../../../../../../issues/potential/issue-00008.md), [issue-00069](../../../../../../issues/potential/issue-00069.md), [issue-00071](../../../../../../issues/potential/issue-00071.md), [issue-00072](../../../../../../issues/potential/issue-00072.md), [issue-00110](../../../../../../issues/potential/issue-00110.md), [issue-00113](../../../../../../issues/potential/issue-00113.md), [issue-00114](../../../../../../issues/potential/issue-00114.md), [issue-00115](../../../../../../issues/potential/issue-00115.md), [issue-00117](../../../../../../issues/potential/issue-00117.md), [issue-00118](../../../../../../issues/potential/issue-00118.md), [issue-00119](../../../../../../issues/potential/issue-00119.md), [issue-00236](../../../../../../issues/potential/issue-00236.md), [issue-00237](../../../../../../issues/potential/issue-00237.md), [issue-00238](../../../../../../issues/potential/issue-00238.md), [issue-00239](../../../../../../issues/potential/issue-00239.md), [issue-00240](../../../../../../issues/potential/issue-00240.md), [issue-00241](../../../../../../issues/potential/issue-00241.md), [issue-00242](../../../../../../issues/potential/issue-00242.md), [issue-00243](../../../../../../issues/potential/issue-00243.md), [issue-00244](../../../../../../issues/potential/issue-00244.md). Новые наблюдения и уточнения разделены по месту отказа; регистрации не являются согласованием исправлений. Использование core migrations не означает запуск полного эффекта.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003038) |
