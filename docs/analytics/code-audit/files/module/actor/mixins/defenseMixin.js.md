# module/actor/mixins/defenseMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 16695cbfc7fec3e0de56660c7cab21bc0304e94b |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.042](../../../../../../tasks/task-0003.042.md), 5 файлов / 477 логических строк; данный файл — 457 |
| Запись перекрёстной сверки | [TASK-0003.042](../../../../review-log.md#task-0003042) |

## Назначение файла

Одиннадцать методов Actor: выбор и бросок защиты, расход STA, критические результаты и локации, реакции на попадание/успех и спасбросок от оглушения.

## Условия использования

Импортируется в [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js):9; Object.assign:443 переносит методы на прототип. Это происходит после modifierMixin:439, поэтому собственный addDefenseModifiers заменяет одноимённый метод первой примеси; тела совпадают. Импорт сохраняет DialogV2, игровые действия начинаются при вызове.

Внешний вход — executeDefense из [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js):53–65. Он получает Actor через getInteractActor, исходное сообщение через game.messages и передаёт attack, defenseOptions, damage, attackRoll, attacker. Примесь сама не выбирает цель и не проверяет права/состояние боевого хода.

## Введённые сущности и действия с ними

| Сущность | Определение/доступность | Жизненный цикл |
| --- | --- | --- |
| defenseMixin | Экспортируемый объект, 10–457 | Одиннадцать методов Actor ниже |
| DialogV2 | Локальная ссылка, 8 | wait для способа защиты, prompt для средства/навыка |
| additionalOptions / defenseOptionsData | prepareAndExecuteDefense:18–28 | Дополняют стандартные способы вариантами предметов; crushingForce исключает value='parry' |
| buttons и callback | 31–45 | action=option.value; возвращает defenseAction, extraDefense bool, customDef строку |
| chooser и prompt callback | 54–103 | Навыки и предметы; при двух и более пунктах возвращает skillName и itemId из selectedOptions[0].dataset.itemid |
| messageData / crit / stun | skillDefense:192–245 | Базовое сообщение, добавленные фрагменты и данные; затем один roll.toMessage |
| Остальные callbacks | filter/map/forEach в отборе; forEach в addDefenseModifiers | Сбор массивов/строки; не создают отдельных реестров или Hooks |

## Основные функции и методы

| Метод / строки | Входы | Действия и результат | Ошибки / ожидания / состояние |
| --- | --- | --- | --- |
| prepareAndExecuteDefense, 11–121 | attack, список defenseOptions, attackDamageObject, totalAttack, attacker UUID | Два этапа выбора; возвращает this.skillDefense(...) | Ждёт wait/prompt и возвращает Promise защиты; отмена rejectClose отклоняется |
| skillDefense, 123–247 | Навык/модификатор/stagger/block; атака; extra/custom; defenseAction; Item ID; skillOverride | Формула → extendedRoll → crit/query → фрагменты → toMessage → реакции | Ждёт extendedRoll, критическую локацию, шаблоны, toMessage. Нет возвращаемого Roll/message, успех даёт undefined |
| addDefenseModifiers, 249–255 | system.combatEffects.defenseModifier | Строка всех ненулевых value с name-подписью | Положительные значения пишутся без +; этот метод побеждает modifierMixin |
| handleExtraDefense, 257–270 | extraDefense bool | При true запрос STA−1; true/false | При остатке<0 notification/false; update не ожидается |
| handleLifepathModifier, 272–290 | formula, action, additionalTag=Item.type | Для armor добавляет положительные shieldParryBonus/shieldParryThrownBonus | Вторая проверка action='parrythrown' отличается от штатного parryThrown; отрицательные бонусы пропущены |
| createDefenseRollConfig, 292–299 | skill, totalAttack | Новый RollConfig: showResult=false, defense=true, threshold=totalAttack, thresholdDesc=skill.label | Сохраняет showCrit=true; config не пишет данные |
| checkForStun, 301–308 | attackDamageObject | Для torso/head и truthy properties.stun возвращает {modifier}; иначе undefined | Не получает и не проверяет исход броска |
| checkForCrit, 310–353 | defenseRoll, totalAttack | null или {criticalLevel,critdamage,bonusdamage} | Чистое сравнение разности; таблица ниже |
| handleCritLocation, 355–395 | damage.originalLocation/location/crit | При includes('random') бросок 2d6+critLocationModifier; иначе прежняя location по ссылке | Ждёт настоящий Roll.evaluate; стороны конечностей — getRandomInt(2) |
| handleDefenseResults, 397–431 | roll, атака, defenseItemId, stagger/block | Попадание: applyOnHit/remove stun; успех: stagger атакующему/износ предмета | Синхронный метод запускает async-операции без ожидания; отсутствующий Item при block вызывает TypeError |
| stunSave, 433–456 | modifier=0 | 1d10 против derivedStats.stun.value+modifier; при неуспехе applyStatus(stun) | Ждёт extendedRoll, не ждёт applyStatus; reversal=true, defense=false: успех строго меньше порога |

### Выбор вариантов и средства защиты

Стандартный список строится через defenseOptions.map(value → CONFIG.WITCHER.defenseOptions.find). Неизвестные значения остаются undefined; проверки нет. Дополнительные варианты берутся из всех this.items с truthy system.isApplicableDefense?.(attack.attackOption), затем Item.createDefenseOption(attack). Ни isStored, ни equipped здесь не проверяются. Модели оружия и профессии поддерживают контракт; ArmorData — нет. Ветка профессии выбирает первый найденный навык, definingSkill не перебирается, isDefense не учитывается.

crushingForce удаляет только value='parry'. parryThrown и пользовательские значения остаются. Это фактический фильтр, соответствие всех сочетаний правилам не установлено.

Кнопки используют value как action. У предметного wrapper это по умолчанию имя; ProfessionData заменяет его именем навыка. Настоящий DialogV2 v14 сворачивает массив в объект по action, поэтому совпадение имён оставляет последнюю кнопку/callback. Пустой массив ядро отвергает до окна.

chooser складывает все defenseAction.skills (label из skillMap) и Item из getList каждого itemType, исключая isAmmo. Для предмета value=meleeAttackSkill ?? 'melee', label=name, itemId=id. getList('shield') выбирает Armor.location='Shield', включая isStored; обычный getList('weapon') исключает stored. При одном пункте диалог не нужен; при нескольких создаётся HTML select; при нуле skillName/itemId остаются undefined и всё равно передаются в skillDefense.

Второй select использует сырые подписи имён и data-itemId. HTML-парсер приводит атрибут к data-itemid; callback читает dataset.itemid корректно. Для пункта навыка записана строка 'undefined', а не существующий Item ID. На block с brawling позже нечего изнашивать. HTML в имени предмета может добавить option; это проверка подготовленного HTML, не XSS/очистки реального клиента.

### Формула и стоимость

Сначала handleExtraDefense, затем skillMapEntry=skillOverride.skillMapEntry ?? CONFIG.skillMap[skillName]. Основа — stat.value и skillOverride.skill.value либо system.skills[attribute][skillName].value. displayFormula содержит только имена базовых составляющих: он не представляет все числовые добавки.

Формула: 1d10 + stat + skill; modifier со знаком; для отрицательного parry/parryThrown и выбранного Item.defenseProperties.parrying добавляется abs(modifier); затем customDef при значении не '0'; бонусы биографии; this.addActiveEffects(skillName); this.addDefenseModifiers(). customDef остаётся строкой, отрицательное значение даёт допустимое +-n. displayRollsDetails включает подписи.

Профессиональная защита имеет полноценный skillOverride, но chooser пустой, поэтому skillName остаётся undefined. Основа работает через override; addActiveEffects(undefined) возвращает пустую строку, а общие defense modifiers добавляются. В сообщении defense также undefined; это установленный контракт пути, влияние на последующие предметные fumble-сценарии отдельно не проверено.

При statuses.find(stun) и skillName!='resistmagic' вся строка заменяется на 10[Stun], включая профессиональную ветку с undefined skillName. Расход extraDefense при этом уже запрошен. resistmagic сохраняет обычный бросок. Успешная защита включает равенство, поскольку RollConfig.defense=true. Стоимость extraDefense — 1 STA без отдельного штрафа к броску; недостаток останавливает до формулы.

### Критическая тяжесть и локация

| totalAttack − defenseRoll | criticalLevel | critdamage | bonusdamage |
| --- | --- | --- | --- |
| Менее 7 | null | — | — |
| 7–9 | simple | 3 | 5 |
| 10–12 | complex | 5 | 10 |
| 13–14 | difficult | 8 | 15 |
| От 15 | deadly | 10 | 20 |

При randomHuman/randomMonster (фактически любой строке originalLocation, содержащей random) используется 2d6+critLocationModifier; хвост/крыло в этой таблице не выбираются.

| Итог 2d6 с модификатором | Локация | location.critEffect |
| --- | --- | --- |
| <4 | Случайная левая/правая нога | Не задаётся |
| 4–5 | Случайная левая/правая рука | Не задаётся |
| 6–8 | torso | 1 |
| 9–10 | torso | 6 |
| 11 | head | 1 |
| ≥12 | head | 6 |

На прицельной атаке возвращается прежний damage.location. После определения crit примесь присваивает attackDamageObject.location=crit.location, копирует critEffectModifier и вызывает getActorOwner(fromUuidSync(attacker)).query с function='addAdrenaline', uuid attacker, data=[]. Получатель/Actor не защищены от отсутствия; query не ожидается.

### Результат, оглушение и последующие действия

К базовому ChatMessageData добавляются defenseCrit.hbs и defenseStun.hbs через append. Критический шаблон получает только локализуемую criticalLevel, а в system.crit сохраняется сырой объект. checkForStun вызывается независимо от победы/поражения: при успешной защите от атаки со stun по torso/head кнопка остаётся.

После roll.toMessage вызывается handleDefenseResults. При roll.total<totalAttack: applyActiveEffectToActorViaId(this.uuid, damage.itemUuid, 'applyOnHit', damage.duration) и removeStatus([{statusEffect:'stun'}]). При равенстве/успехе: если stagger, applyStatusEffectToActor(attacker,'staggered',1); если block, надёжность −1, либо −2 при crushingForce. Для Item.type='armor' поле reliability, для остальных reliable. Нижнего ограничения нет; broken-уведомление проверяет вычисленный остаток<=0. Износ brawling обращается к отсутствующему Item после уже сформированного сообщения.

stunSave не использует взрывные/критические броски: showCrit=false. Порог value+modifier, reversal=true, defense остаётся false; равенство — провал. Успех не снимает прежний stun, провал запрашивает applyStatus. Интерпретация знака модификатора и границ по книге не менялась.

## Используемые сущности и зависимости

| Сущность | Источник | Вид, место и назначение | Основание |
| --- | --- | --- | --- |
| extendedRoll | [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | Прямой import:1; skillDefense200/stunSave451 | Бросок и success; при защите showResult=false, сообщение позже; при stunSave helper сам отправляет |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js) | Прямой import:2; createDefenseRollConfig/stunSave | defense/reversal/threshold/showCrit/showResult |
| applyStatusEffectToActor | [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | Import:3; stagger:409 | Делегирование/статус атакующего; вызов не ожидается |
| applyActiveEffectToActorViaId | [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | Import:4; попадание 399–404 | Item.effects applyOnHit; UUID/duration; дальше модель/владелец/GM |
| getActorOwner / getRandomInt | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | Import:5; query:213, конечности 384/389 | OWNER либо activeGM; сторона конечности |
| ChatMessageData / append | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | Import:6; 192/227/239/438 | Actor sender, объединение flavor/system/flags |
| Item.createDefenseOption | [module/item/mixins/defenseOptionMixin.js](../../../../../../../module/item/mixins/defenseOptionMixin.js) | Динамический вызов 20 | Имя предмета и модельный option |
| isApplicableDefense / createDefenseOption | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js), [module/data/item/professionData.js](../../../../../../../module/data/item/professionData.js), [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) | Отбор/навык/skillOverride | Настоящие модели испытаны в группах 4–6/11 |
| getList / getLocationObject | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js), [module/actor/mixins/locationMixin.js](../../../../../../../module/actor/mixins/locationMixin.js) | Методы Actor; 63,362–390 | Сортировка/щит/навык, описание локации; точные тела исполнены на фасаде |
| addActiveEffects / перекрытый addDefenseModifiers | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | Метод прототипа/одноимённое определение | AE/группы навыков; Object.assign определяет финальный метод |
| stats / skills / derivedStats / combatEffects | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js), [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js), [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js) | Чтение Actor.system | Значения и модификаторы; Actor preparation в этой задаче не выполняется |
| shieldParryBonus / shieldParryThrownBonus | [module/data/actor/templates/common/lifepathData.js](../../../../../../../module/data/actor/templates/common/lifepathData.js) | handleLifepathModifier | Числовые поля; action с ошибочным регистром |
| defenseOptions / skillMap / critLevel | [module/setup/config.js](../../../../../../../module/setup/config.js) | CONFIG.WITCHER | Стандартные способы, навыки, ключи тяжести |
| displayRollsDetails | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | game.settings.get | Подписи формулы |
| defense.hbs / defenseCrit.hbs / defenseStun.hbs | [templates/chat/combat/defense/defense.hbs](../../../../../../../templates/chat/combat/defense/defense.hbs), [templates/chat/combat/defense/defenseCrit.hbs](../../../../../../../templates/chat/combat/defense/defenseCrit.hbs), [templates/chat/combat/defense/defenseStun.hbs](../../../../../../../templates/chat/combat/defense/defenseStun.hbs) | renderTemplate | Контексты {defenseName,displayFormula}, {crit:{criticalLevel}}, {stun} |
| DefenseMessageData / AttackMessageData | [module/data/chatMessage/defenseMessageData.js](../../../../../../../module/data/chatMessage/defenseMessageData.js), [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js) | Граница до/после сообщения | defense-схема удаляет critEffectModifier; attack-схема удаляет damage.duration |
| removeStatus / applyStatus | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Методы Actor, попадание/спасбросок | В тесте границы с pending Promise; реальное создание ActiveEffect не исполнялось |
| addAdrenaline query | [module/setup/queries.js](../../../../../../../module/setup/queries.js), [module/actor/mixins/adrenalineMixin.js](../../../../../../../module/actor/mixins/adrenalineMixin.js) | Удалённый allowlist-метод | Отправлен запрос, выполнение получателем в этой порции не доказано |
| Roll / DialogV2 / update / i18n / fromUuidSync | Foundry 14.367.0, /opt/foundryvtt | Внешние API | Настоящие Roll/models и извлечённый initializer Dialog; остальные границы перечислены в журнале |
| WITCHER.Dialog/Defense/Settings/Shield/Weapon/Chat/Actor/Spell | [lang/en.json](../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../lang/ru.json) | Локализация строк и ключей CONFIG | В тестах localize возвращал ключ; штатный expandObject/fallback не исполнялся |

## Известные потребители

| Файл | Сущность / условие | Основание |
| --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | import/Object.assign | 9/443; все методы доступны Actor |
| [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) | executeDefense → prepareAndExecuteDefense | Получает поля исходного сообщения; return результата не передаёт |
| Тот же combat.js | defenseChatMessageListeners → stunSave | button.stun берёт attackWeaponProperties.stun, crit-stun без аргумента; Actor выбирается getInteractActor заново |
| Эта примесь | Вспомогательные методы | Цепочка skillDefense и stunSave, см. таблицу выше |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | Косвенный consumer crit в applyCritWound | По меню чата: crit.location/criticalLevel/critEffect/critEffectModifier выбирают травму |

Поиск всех одиннадцати имён выполнен по module/templates; внешние макросы не перечислены. Соседние источники, не входящие в порцию, не получили статус полного разбора.

## Данные и изменения состояния

Дополнительная защита запрашивает Actor.update; block — Item.update. Query, status/applyOnHit/removeStatus и applyStatus спасброска не ожидаются. Возврат метода не доказывает сохранения или выполнения на другом клиенте. Ошибка позже по пути возможна после расхода или после сообщения.

attackDamageObject не копируется. Если это prepared damage исходного AttackMessageData, критическая защита меняет его location в памяти: в группе 33 torso→leftLeg, _source остался torso. Последствия повторных защит в реальном клиенте не проверены; отдельная проблема без такого сценария не зарегистрирована.

Группа 22 подтвердила critEffectModifier=6 перед DefenseMessageData и его отсутствие после схемы; группа 32 исполнила applyCritWound: сырой crit выбрал greater, очищенный — lesser при getRandomInt=1. UUID-каталог/добавление Item/сообщение были фасадами. Это не новая issue:258. Группа 31 показала потерю top-level damage.duration=4 в AttackMessageData и undefined у applyOnHit:257. Поля effects.duration из предыдущей порции — отдельная точка той же ограниченной схемы.

## Проверки и доказательства

Все 457 строк прочитаны, включая 11 методов и оба callback окна. [Журнал .042](../../../../review-log.md#task-0003042) содержит 33 группы: стандартные/предметные/профессиональные варианты, дубли action настоящего Dialog initializer, отмена, пустые пути, ±модификаторы, равенство, все пороги/локации, отсутствие получателя, износ, статусы и схемы/consumer травмы. Итоговые assertions выполнены.

## Непроверенные участки и открытые вопросы

Непрочитанных участков файла нет. Actor/Item-документы, UI/DOM form, user/query/persistence и большинство extendedRoll-исходов — фасады; реальные модели и разбор Roll применены отдельно. Группа 19 использовала настоящий extendedRoll и детерминированные Roll, но toMessage заменён. Полный мир, права, таймауты, RNG-распределение, HP/броня, реальное применение статусов/травм, локализация и допустимость сочетаний по книге не проверялись.

## Связанные проблемы

Новые [docs/issues/potential/issue-00268.md](../../../../../../issues/potential/issue-00268.md)–[docs/issues/potential/issue-00276.md](../../../../../../issues/potential/issue-00276.md): дубли кнопок, пустой выбор, brawling-block, регистр parryThrown, stun после успеха, async-границы, stored-предметы, HTML имён, расход до ошибки. Ранее зарегистрированы [docs/issues/potential/issue-00033.md](../../../../../../issues/potential/issue-00033.md), [docs/issues/potential/issue-00071.md](../../../../../../issues/potential/issue-00071.md), [docs/issues/potential/issue-00072.md](../../../../../../issues/potential/issue-00072.md), [docs/issues/potential/issue-00079.md](../../../../../../issues/potential/issue-00079.md), [docs/issues/potential/issue-00085.md](../../../../../../issues/potential/issue-00085.md), [docs/issues/potential/issue-00182.md](../../../../../../issues/potential/issue-00182.md), [docs/issues/potential/issue-00185.md](../../../../../../issues/potential/issue-00185.md), [docs/issues/potential/issue-00257.md](../../../../../../issues/potential/issue-00257.md), [docs/issues/potential/issue-00258.md](../../../../../../issues/potential/issue-00258.md). Исправления/подтверждение статусов не выполнялись.

Отдельный прежний предел: [docs/issues/potential/issue-00031.md](../../../../../../issues/potential/issue-00031.md) — ReferenceError внутри WitcherActor.applyStatus при непустых иммунитетах. В данной порции applyStatus заменён границей запроса; реальный этот метод заново не исполнялся. addAdrenaline на стороне Actor читает useOptionalAdrenaline перед update; наличие query само по себе не доказывает прироста куба.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 16695cbfc7fec3e0de56660c7cab21bc0304e94b; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003042) |

## Дополнительная сверка TASK-0003.045

2026-09-12, rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3; исходники не изменены.

Проверен полностью [маршрут чата](../../../../../../../module/scripts/combat/combat.js). executeDefense передаёт attack, defenseOptions, damage, attackRoll, attacker из выбранного сообщения; его Actor выбирается helper, отсутствующий Actor отсекается. stunSave на button.stun получает attackWeaponProperties.stun, на crit-stun — без аргумента. Все кнопки stun связываются отдельно, вложенный target не меняет сообщение. Группа 23 подтверждает, что critical menu получает уже очищенный crit без modifier (258). Полные исходы skillDefense/stunSave из .042 заново не запускались.

[Проверки, результаты и ограничения](../../../../review-log.md#task-0003045). Связанные файлы не засчитываются повторно в покрытии.

## Уточнение TASK-0003.057 — боевые таблицы

2026-09-12, rusbar-main 8573642b0136f80b8ae3456de51e1b7f637ec7f3; исходник не изменён.

handleCritLocation исполнен для сумм0,2,3,4,5,6,8,9,10,11,12,14 и явной локации: 12+ → head/critEffect6, 11 → head/1, 9–10 → torso/6, 6–8 → torso/1, 4–5 → случайная рука, ниже4 → случайная нога. Ни checkForCrit, ни handleCritLocation не вызывают четыре Combat Critical RollTable. Таблицы используют обычный 2d6, handler учитывает critLocationModifier.

[Карточки Combat](../../../README.md#боевые-таблицы--task-0003057), [перекрёстная сверка](../../../../review-log.md#task-0003057). Для issue-00322/00323/00324 см. [реестр проблем](../../../../../../issues/potential/../README.md). Пределы изолированных сценариев сохранены отдельно от запуска мира.
