# module/actor/mixins/professionMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.038](../../../../../../tasks/task-0003.038.md), 4 файла, 965 логических строк |
| Запись перекрёстной сверки | [TASK-0003.038](../../../../review-log.md#task-0003038) |

Актуализация [issue-00001](../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

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
| registerQueries/applyActiveEffectToActor | [module/setup/queries.js](../../../../../../../module/setup/queries.js); [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | query/API | TheWitcherTRPG-RB-Version.query function applyActiveEffectToActor | data:[target.uuid,[newEffect]]; clone у получателя, затем createEmbeddedDocuments |
| TemporaryEffects | [module/data/actor/templates/common/temporaryEffectsData.js](../../../../../../../module/data/actor/templates/common/temporaryEffectsData.js) | Путь назначения effect | temporaryHp.<skillName> → name/value | Схема ожидает числовой value; не прямой прирост derivedStats.hp |
| AttackMessageData/damageData/attackData | [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js); [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js); [module/data/chatMessage/templates/attackData.js](../../../../../../../module/data/chatMessage/templates/attackData.js) | Тип сообщения | attack, damage, defenseOptions, rollTotal | attack.itemUuid/damage.itemUuid отсутствуют в producer; лишнее damage.item не входит в schema |
| attackChatMessageListeners/onDamage/executeDefense | [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) | Потребитель сообщения | Кнопка damage/контекст защиты | onDamage требует attack.itemUuid; defense читает attackRoll/options/damage/attacker |
| ActiveEffect/миграция | Foundry 14.367.0: common/documents/active-effect.mjs:152–241 | Конструктор/совместимость | changes(mode2)/duration.rounds — старый ввод | Реальная migrateData преобразует system.changes/type/value и duration; icon не превращается в img |
| WitcherActiveEffectData/регистрация | [module/data/activeEffects/witcherActiveEffectData.js](../../../../../../../module/data/activeEffects/witcherActiveEffectData.js); [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js); [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Тип/документ эффекта | baseType + apply flags; CONFIG.ActiveEffect.documentClass | Полный lifecycle конструктора не исполнялся |
| DialogV2, Roll, fromUuid, User.query | Foundry 14.367.0 | Внешние API | prompt, dice, message/query; DOM .checked/.value | Реальный Roll и данные; окна/query/запись — фасады |
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

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-09, R008-10, R008-11, R008-12, R008-13, R008-14, R008-15, R008-16, R008-17, R008-18, R008-19; оставшиеся границы: [U008-02](../../../../cross-check-0002.md#u008-02), [U008-03](../../../../cross-check-0002.md#u008-03), [U008-04](../../../../cross-check-0002.md#u008-04), [U008-05](../../../../cross-check-0002.md#u008-05), [U008-08](../../../../cross-check-0002.md#u008-08). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00008](../../../../../../issues/potential/issue-00008.md), [issue-00069](../../../../../../issues/potential/issue-00069.md), [issue-00071](../../../../../../issues/potential/issue-00071.md), [issue-00072](../../../../../../issues/potential/issue-00072.md), [issue-00110](../../../../../../issues/potential/issue-00110.md), [issue-00113](../../../../../../issues/potential/issue-00113.md), [issue-00114](../../../../../../issues/potential/issue-00114.md), [issue-00115](../../../../../../issues/potential/issue-00115.md), [issue-00117](../../../../../../issues/potential/issue-00117.md), [issue-00118](../../../../../../issues/potential/issue-00118.md), [issue-00119](../../../../../../issues/potential/issue-00119.md), [issue-00236](../../../../../../issues/potential/issue-00236.md), [issue-00237](../../../../../../issues/potential/issue-00237.md), [issue-00238](../../../../../../issues/potential/issue-00238.md), [issue-00239](../../../../../../issues/potential/issue-00239.md), [issue-00240](../../../../../../issues/potential/issue-00240.md), [issue-00241](../../../../../../issues/potential/issue-00241.md), [issue-00242](../../../../../../issues/potential/issue-00242.md), [issue-00243](../../../../../../issues/potential/issue-00243.md), [issue-00244](../../../../../../issues/potential/issue-00244.md). Новые наблюдения и уточнения разделены по месту отказа; регистрации не являются согласованием исправлений. Использование core migrations не означает запуск полного эффекта.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003038) |

### Дополнительная сверка TASK-0003.040

2026-09-11, `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1`; исходники прежние. Прямое применение способности отправляет attack без itemUuid; настоящий AttackMessageData оставляет null. Фабрика attackData не выводит ссылку из других данных и не проверяет существование Item. Кнопка combat.onDamage разрешает именно message.system.attack.itemUuid и ожидает rollDamage. Это уточняет issue-00239, а не создаёт её дубль. Метод getItemAttack является отдельным вызываемым API.

Сопоставленные исходники: [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js), [module/data/chatMessage/templates/attackData.js](../../../../../../../module/data/chatMessage/templates/attackData.js). Полные новые описания: [attackMessageData.js](../../data/chatMessage/attackMessageData.js.md), [attackData.js](../../data/chatMessage/templates/attackData.js.md).

[Сверка порции и всей серии .031–.040](../../../../review-log.md#task-0003040). Уточнение связи не означает повторной проверки всех сценариев соседнего файла; мир/БД и браузер не запускались.

## Дополнительная сверка TASK-0003.041

2026-09-12, rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; исходник не изменён.

[weaponAttack](weaponAttackMixin.js.md) теперь разобран полностью. doProfessionWeaponAttackRoll передаёт две служебные настройки; getItemAttack ошибочно учитывает их в выборе клавиш для оружия с несколькими режимами (issue-00264). Замещение по-прежнему обходит helpers модификаторов (issue-00237). Пустой weapon воспроизведён на входе weaponAttack (issue-00242); дополнительная оружейная атака запрашивает STA−3, поэтому issue-00238 остаётся про прямую профессиональную атаку.

[Сверка и ограничения](../../../../review-log.md#task-0003041). Уточнение связи не увеличивает пофайловое покрытие; исправления не выполнялись.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

У Actor закреплены девять методов профессии. Поиск по имени и приоритет dispatcher связывают UI с обычным броском, порогом, HP или атакой; прямая и оружейная ветви имеют разные модификаторы и ресурсы. Payload HP не равен изменению derivedStats.hp, а созданная кнопка damage не получает Item UUID. Разделены найденные причины и границы ожидания Promise.

Сопоставленные определения и потребители: [module/scripts/rolls/extendedRoll.js](../../scripts/rolls/extendedRoll.js.md), [module/scripts/rollConfig.js](../../scripts/rollConfig.js.md), [module/chatMessage/chatMessageData.js](../../chatMessage/chatMessageData.js.md), [module/scripts/helper.js](../../scripts/helper.js.md), [module/actor/witcherActor.js](../witcherActor.js.md), [module/actor/mixins/locationMixin.js](locationMixin.js.md), [module/actor/mixins/modifierMixin.js](modifierMixin.js.md), [module/actor/mixins/weaponAttackMixin.js](weaponAttackMixin.js.md), [module/actor/mixins/defenseMixin.js](defenseMixin.js.md), [module/data/item/professionData.js](../../data/item/professionData.js.md), [module/data/item/templates/professionPathData.js](../../data/item/templates/professionPathData.js.md), [module/data/item/templates/professionSkillData.js](../../data/item/templates/professionSkillData.js.md), [module/data/item/templates/profession/skillUsageData.js](../../data/item/templates/profession/skillUsageData.js.md), [module/data/item/templates/profession/temporaryHealthData.js](../../data/item/templates/profession/temporaryHealthData.js.md), [module/data/item/templates/profession/thresholdData.js](../../data/item/templates/profession/thresholdData.js.md), [module/data/item/templates/combat/skillAttackData.js](../../data/item/templates/combat/skillAttackData.js.md), [module/data/item/templates/combat/attackOptionsData.js](../../data/item/templates/combat/attackOptionsData.js.md), [module/data/item/templates/combat/defenseOptionsData.js](../../data/item/templates/combat/defenseOptionsData.js.md), [module/data/item/templates/combat/damagePropertiesData.js](../../data/item/templates/combat/damagePropertiesData.js.md), [module/setup/config.js](../../setup/config.js.md), [module/setup/settings.js](../../setup/settings.js.md), [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs.md), [module/setup/queries.js](../../setup/queries.js.md), [module/scripts/temporaryEffects/applyActiveEffect.js](../../scripts/temporaryEffects/applyActiveEffect.js.md), [module/data/actor/templates/common/temporaryEffectsData.js](../../data/actor/templates/common/temporaryEffectsData.js.md), [module/data/chatMessage/attackMessageData.js](../../data/chatMessage/attackMessageData.js.md), [module/data/chatMessage/templates/damageData.js](../../data/chatMessage/templates/damageData.js.md), [module/data/chatMessage/templates/attackData.js](../../data/chatMessage/templates/attackData.js.md), [module/scripts/combat/combat.js](../../scripts/combat/combat.js.md), [module/data/activeEffects/witcherActiveEffectData.js](../../data/activeEffects/witcherActiveEffectData.js.md), [module/setup/registerDataModels.js](../../setup/registerDataModels.js.md), [module/TheWitcherTRPG.js](../../TheWitcherTRPG.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md), [module/actor/sheets/WitcherCharacterSheet.js](../sheets/WitcherCharacterSheet.js.md), [module/actor/sheets/mixins/skillMixin.js](../sheets/mixins/skillMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md).

[Протокол и границы](../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-09](../../../../cross-check-0002.md#r008-09), [R008-10](../../../../cross-check-0002.md#r008-10), [R008-11](../../../../cross-check-0002.md#r008-11), [R008-12](../../../../cross-check-0002.md#r008-12), [R008-13](../../../../cross-check-0002.md#r008-13), [R008-14](../../../../cross-check-0002.md#r008-14), [R008-15](../../../../cross-check-0002.md#r008-15), [R008-16](../../../../cross-check-0002.md#r008-16), [R008-17](../../../../cross-check-0002.md#r008-17), [R008-18](../../../../cross-check-0002.md#r008-18), [R008-19](../../../../cross-check-0002.md#r008-19). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
