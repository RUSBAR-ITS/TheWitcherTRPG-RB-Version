# module/actor/mixins/weaponAttackMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.041](../../../../../../tasks/task-0003.041.md), четыре файла / 687 логических строк; данный файл — 382 |
| Запись перекрёстной сверки | [TASK-0003.041](../../../../review-log.md#task-0003041) |

## Назначение файла

Пять методов Actor: подготовка оружейной атаки, диалог, формулы, объединение свойств урона и выпуск атаки в чат либо непосредственный вызов броска урона.
## Условия использования

Импорт создаёт объект weaponAttackMixin и сохраняет ссылку на Foundry DialogV2; игровых действий при импорте нет. [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) импортирует примесь (7), присоединяет через Object.assign к прототипу (442), а useItem (231) возвращает weaponAttack(item, options). Другой прямой потребитель — doProfessionWeaponAttackRoll (256) из [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js): передаёт skillReplacement и additionalDamageProperties, вызов не ожидает.

Ожидаются принадлежащий Actor Item оружия, подготовленные stats/skills/attackStats/derivedStats/combatEffects/lifepathModifiers и коллекция items. Доступ проверяет вызывающий интерфейс/Foundry; здесь собственной проверки владельца, выбранной цели и боевого хода нет. Монстр поддержан условием addMeleeBonus; остальные пути полагаются на наличие тех же данных. Пустой skill останавливает выполнение уведомлением, неизвестный непустой skill — нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Доступность | Действия |
| --- | --- | --- | --- |
| weaponAttackMixin | Экспортируемый объект, 6–382 | Прототип WitcherActor | Содержит все пять методов ниже |
| DialogV2 | Локальная ссылка, 4 | Только этот модуль | prompt с modal, rejectClose; сохранение результата callback |
| Контекст data | Локальный объект, 57–67 | renderTemplate | item, attackSkill, displayDmgFormula, noAmmo, noThrowable, ammunitionOption, ammunitions, meleeBonus, config |
| ok.callback | Вложенная функция, 104–130 | DialogV2.prompt | Читает 20 полей form.elements; возвращает bool/string без числовой нормализации |
| callbacks filter/forEach | 45, 49–51, 170–175 | Локальные | Отбор боеприпасов, конкатенация option, добавление effects улучшений |
| attack, damage, attFormula, damageFormula | Локальное состояние вызова | Получатели ChatMessageData/rollDamage | attack и damage общие для всех ударов; attFormula создаётся заново, damageFormula накапливается |
| damageModifcation | Локальная строка, 136–138 | Цикл ударов | Именно такое имя в коде; результат mergeDamageProperties прибавляется к damage.formula |

## Основные функции и методы

| Метод | Вход | Результат и основные действия | Ошибки, ожидания, состояние |
| --- | --- | --- | --- |
| weaponAttack, 7–313 | weapon; options={} | Готовит формулы/форму, получает выбор, готовит damage, запрашивает расход, выполняет attackNumber ударов | async; ждёт renderTemplate, prompt, extendedRoll. Не ждёт Actor.update, Item.update, rollDamage; успешного return-значения нет |
| constructBaseAttackFormula, 315–326 | Объект skill из CONFIG.WITCHER.skillMap | Строка stat.value + skill.value + addActiveEffects + addAttackModifiers | Не использует modifiedValue напрямую; неизвестный skill приводит к TypeError |
| mergeDamageProperties, 328–355 | Подготовленные properties и additionalProperties | Возвращает '' либо '+3d6'; меняет первый объект | Два независимых if бронебойности; OR bool, сумма number, конкатенация string, push Array; вложенные objects пропускает |
| handleAttackLocation, 357–365 | location, damage, displayRollDetails | Возвращает modifier и необязательную подпись; пишет location/originalLocation в damage | Вызывает this.getLocationObject; не проверяет цель или hasTailWing |
| handleStrikeType, 367–381 | strike, displayRollDetails | Строка attackPenality и lifepathModifiers.attacks[strike] | Читает целое значение lifepath, не .value; неизвестный strike приводит к TypeError |

Порядок weaponAttack: исходный damage → условный meleeBonus → getItemAttack(options) → необязательная замена skill/alias → проверка пустого skill → контекст и диалог → attackNumber → createBaseDamageObject → необязательный merge → strike/type → STA → ammunition → throwable → effects улучшений → properties.toObject(false) → цикл ударов.

В начале готовится messageDataFlavor с h1, но перед фактическим сообщением строка заменяется целиком. В цикле attack всегда строится даже при rollOnlyDmg; этот режим меняет только конечного получателя.

### Формула атаки и поля формы

Обычная основа — 1d10 + stats[attribute].value + skills[attribute][name].value, затем helpers модификаторов. Профессиональная замена берёт stats[replacement.stat].value + (replacement.level ?? 0), alias=skillName и обходит оба helper. После основы операции идут в следующем порядке:

| Поле/источник | Добавка и условие |
| --- | --- |
| weapon.system.accuracy | Со знаком, если меньше/больше нуля |
| targetOutsideLOS / outsideLOS | −3 / +3 |
| isExtraAttack / isFastDraw | −3 / −3 |
| isProne / isPinned | −2 / +4 |
| isActivelyDodging / isMoving | −2 / −3 |
| isAmbush / isRicochet | +5 / −5 |
| isBlinded / isSilhouetted | −3 / +2 |
| customAim | +value только при value > 0 |
| customAtt | +value, если строка не '0'; отрицательное число даёт синтаксис +-n |
| range | pointBlank +5; medium −2; long −4; extreme −6; none/close/null без добавки |
| location | Строка modifier от getLocationObject |
| strike | attackPenality, затем значение lifepathModifiers.attacks[strike] |

callback читает 12 checkbox: isExtraAttack и одиннадцать позиционных флагов из таблицы; восемь значений: location, ammunition, customAim, range, customAtt, strike, damageType, customDmg. ammunition использует optional chaining; range читается только при truthy weapon.system.range. Остальные контролы считаются существующими. Пределы, взаимная исключительность checkbox и числовая валидация здесь не задаются.

CONFIG.weapon.attacks: normal — один бросок; fast — два; strong/joint — один с −3; half — один. dmgMulti strong '*2'/half '/2' применяется далее в Item.rollDamage, а не здесь. Неизвестный strike получает attackNumber=1 через fallback, но затем падает в handleStrikeType.

### Урон, свойства и расход

База урона — текст weapon.system.damage. meleeBonus учитывается при applyMeleeBonus && (Actor.type==='character' || Actor.system.addMeleeBonus), с правильным знаком. Отдельный preview meleeBonus проверяет только applyMeleeBonus: для монстра возможна разница с формулой. applyRangedMeleeBonus не читается.

customDmg добавляется внутри цикла к общей damageFormula. При fast и customDmg=2: первый damage.formula='2d6+2', второй='2d6+2+2'. damageModifcation от merge прибавляется к итоговой строке на каждой итерации отдельно. Подписи включаются настройкой displayRollsDetails; произвольный текст customDmg остаётся частью формулы.

merge сначала устанавливает improvedArmorPiercing при AP+(AP либо IAP), а следующий if уже видит это значение и возвращает +3d6. Затем объединяет собственные перечисляемые поля по JS-типам. На двух настоящих моделях стандартный defenseMultiplierCap=5 складывается до 10 даже без изменения прочих числовых свойств; назначение такого сложения требует проверки правил. effects — TypedObject, поэтому общая ветка его пропускает. Частичные сторонние plain objects могут давать undefined/NaN при отсутствии полей; штатный профессиональный источник передаёт полную модель.

Дополнительная атака запрашивает STA−3; при результате <0 только уведомление. Боеприпас выбирается среди всех Item type weapon с isAmmo, без проверки quantity, совместимости или isStored. При выборе запрашивается quantity−1 и добавляются его effects; поле quantity исходно StringField из CommonItemData, вычитание приводит к числу. Нет боеприпасов — лишь noAmmo=1 в контексте, исполнение не запрещено. Throwable списывается только при isThrowable && attack.attackOption==='ranged'; отрицательный остаток вызывает return уже после STA/ammo. При fast оба расхода происходят один раз до цикла; корректность кратности по правилам не устанавливалась.

createBaseDamageObject отдаёт properties по ссылке на weapon.system.damageProperties. merge, ammunition и enhancement addEffects меняют подготовленную модель Item до toObject(false). Сохранение этих свойств в БД не запрашивается. enhancementItems разрешаются через this.items.get(element.id), effects берутся из enhancement.system.effects; отсутствующий предмет отдельно не защищён.

## Используемые сущности и зависимости

| Сущность | Источник | Вид / место / цель | Основание |
| --- | --- | --- | --- |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | Прямой import; 303: sender=this, type='attack', system={attacker,attack,damage,defenseOptions} | Конструктор исполнен с фасадом getSpeaker |
| extendedRoll / RollConfig | [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js), [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js) | Прямой import и косвенный default config; 310, ожидается | showCrit/showResult=true, threshold=−1; добавляет system.rollTotal и вызывает Roll.toMessage |
| getItemAttack | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Вызов Item, 30 | Выбор через options.ctrl/alt/shift и attackOptions; весь options передаётся без фильтрации |
| createBaseDamageObject / rollDamage | [module/item/mixins/damageUtilMixin.js](../../../../../../../module/item/mixins/damageUtilMixin.js) | Динамические методы Item, 135/301 | База properties/item/itemUuid/crit/defenseOptions; дальнейшие множители и бросок урона |
| addActiveEffects / addAttackModifiers | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | Методы прототипа Actor, 321–322 | Читают skill activeEffectModifiers, skillGroupModifiers, combatEffects.attackModifier |
| getLocationObject | [module/actor/mixins/locationMixin.js](../../../../../../../module/actor/mixins/locationMixin.js), static в [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Динамический вызов, 358 | Заполняет name/alias/formula/modifier; отдельный путь от getAllLocations |
| WeaponData / isEnoughThrowable | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js), [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Чтение Item.system и метод, 10–177 | quantity — строка; enhancementItems подготовлен из enhancementItemIds; isEnoughThrowable проверяет quantity>0 |
| DamageProperties.addEffects / toObject | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) и Foundry DataModel | 159/174/177, merge | addEffects объединяет dictionary; toObject(false) сериализует подготовленное состояние |
| attackOptions / skillAttack | [module/data/item/templates/combat/attackOptionsData.js](../../../../../../../module/data/item/templates/combat/attackOptionsData.js), [module/data/item/templates/combat/skillAttackData.js](../../../../../../../module/data/item/templates/combat/skillAttackData.js) | Косвенные поля моделей | Имена навыков, флаги, свойства профессиональной атаки |
| stats / skills / attackStats / derivedStats | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js), [module/data/actor/templates/character/attackStatsData.js](../../../../../../../module/data/actor/templates/character/attackStatsData.js) | Пути модели Actor | Значения основы, melee/crit, STA; подготовка характеристик здесь не выполняется |
| lifepathModifiers.attacks | [module/data/actor/templates/common/lifepathData.js](../../../../../../../module/data/actor/templates/common/lifepathData.js) | Чтение 375 | Объект value/label конфликтует со строковой интерполяцией |
| skillMap / statMap / weapon.attacks | [module/setup/config.js](../../../../../../../module/setup/config.js) | Глобальный CONFIG.WITCHER | Названия, параметры удара, attackNumber/attackPenality |
| displayRollsDetails | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | game.settings.get, 8/316 | Влияет на подписи формул, не на величины |
| weapon-attack.hbs | [templates/dialog/combat/weapon-attack.hbs](../../../../../../../templates/dialog/combat/weapon-attack.hbs) | renderTemplate, 69–72 | Девять ключей контекста и 20 возвращаемых полей; подробности в карточке шаблона |
| DialogV2 / renderTemplate / ui.notifications / update | Foundry VTT 14.367.0, /opt/foundryvtt | API окна, шаблона, уведомлений, записи | В изолированных проверках фасады; завершение записей и браузер не проверялись |
| game.i18n.localize | Foundry, [lang/en.json](../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../lang/ru.json) | Подписи CONFIG и WITCHER.Dialog/Weapon/Location/Settings/Actor/Attack/Armor/table/Spell | Динамические ключи перечислены кодом; в запуске localize возвращал ключ, качество переводов этим не проверено |
| AttackMessageData / damageData / DefenseMessageData | [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js), [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js), [module/data/chatMessage/defenseMessageData.js](../../../../../../../module/data/chatMessage/defenseMessageData.js) | Косвенная граница сообщения | Реальные схемы сохраняют UUID/crit в attack, очищают item/ammunition/duration; defense теряет critEffectModifier |

## Известные потребители

| Файл | Связь | Доказательство |
| --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Импорт, Object.assign; useItem → weaponAttack | 7, 231, 442; возвращает Promise |
| [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | doProfessionWeaponAttackRoll → weaponAttack | 256–259; передаёт две дополнительные настройки без модификаторов клавиш |
| Этот же файл | Четыре вспомогательных метода | 138, 187, 292–293; иных прямых вызовов найдено не было |

Поиск выполнен по module и templates; доступность методов на прототипе допускает внешние макросы, которые не перечисляются автоматически.

## Данные и изменения состояния

При обычной атаке формируется новый ChatMessageData для каждого удара; его system.damage указывает на один и тот же локальный объект. attacker и attack.itemUuid/damage.itemUuid заданы до сообщения, damage.crit содержит оба модификатора. Flavor содержит attack-message, h1/item-img, локализованную локацию и button.damage; закрывающий div в исходной строке не дописывается. Кнопку связывает attackChatMessageListeners/onDamage из [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js): fromUuidSync(message.system.attack.itemUuid) → Item.rollDamage(message.system.damage). executeDefense того же файла передаёт attack, defenseOptions, damage, attackRoll, attacker в Actor.prepareAndExecuteDefense из [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js). Обработка HTML ядром и кликов — соседний маршрут; не доказательство визуальной неисправности.

В AttackMessageData остаются определённые схемой поля: raw Item и ammunition удаляются, critEffectModifier сохраняется. Эффекту, которому перед границей вручную добавили duration, схема этот ключ удаляет. Сам weaponAttack длительность не создаёт. Потеря critEffectModifier происходит позднее в DefenseMessageData, а не в производителе атаки.

Update-запросы отделены от доказанного сохранения: локальный тест оставлял их Promise незавершёнными, а метод всё равно доходил до броска/возвращался. При rollOnlyDmg два вызова fast могут одновременно держать один damage; окончания этих вызовов weaponAttack не ждёт.

## Проверки и доказательства

Полностью прочитаны 382 строки. В [docs/analytics/code-audit/review-log.md](../../../../review-log.md#task-0003041) записаны 28 групп: обычная/дальняя/профессиональная атака, ±/0, 12 checkbox, шесть дальностей, пять strike, девять location, отмена, расход и ранние ошибки, общие ссылки, merge, реальные модели и формулы. Все итоговые assertions выполнены.

Нативный weaponAttack и все четыре helper исполнены; настоящие WeaponData, DamageProperties, ChatMessageData, modifierMixin, getItemAttack/createBaseDamageObject/static getLocationObject. Реальный Roll v14 разбирал формулы; минимальные броски использованы как детерминированный контроль. Один проход extendedRoll выполнен до подменённого toMessage (fumble 8−1=7). Actor, коллекция документов, UI, запись и доставляемый HTML — локальные фасады. Это проверка кода на фиксированных данных, не игровой прогон.

## Непроверенные участки и открытые вопросы

Непрочитанных участков самого файла нет. Не проверены браузерный DialogV2, полный Actor lifecycle, подготовка после реального update, отклонение прав записи, конкурентные клиенты, реальное сохранение/доставка сообщений, защита/HP и случайное распределение локаций. Правильность AP/кратности боеприпасов по рулбуку и допустимые комбинации модификаторов требуют отдельного решения. Соседи проверены только до нужных определений; их покрытие не увеличено.

## Связанные проблемы

Новые: [docs/issues/potential/issue-00259.md](../../../../../../issues/potential/issue-00259.md) — накопление customDmg; [docs/issues/potential/issue-00260.md](../../../../../../issues/potential/issue-00260.md) — нулевой/отсутствующий ammo; [docs/issues/potential/issue-00261.md](../../../../../../issues/potential/issue-00261.md) — расход до позднего отказа; [docs/issues/potential/issue-00262.md](../../../../../../issues/potential/issue-00262.md) — не ожидаются update/rollDamage; [docs/issues/potential/issue-00263.md](../../../../../../issues/potential/issue-00263.md) — последовательные ветви AP; [docs/issues/potential/issue-00264.md](../../../../../../issues/potential/issue-00264.md) — служебные options нарушают выбор attackOption; [docs/issues/potential/issue-00266.md](../../../../../../issues/potential/issue-00266.md) — сырая HTML-строка имени ammo. [docs/issues/potential/issue-00265.md](../../../../../../issues/potential/issue-00265.md) относится к условию шаблона, [docs/issues/potential/issue-00267.md](../../../../../../issues/potential/issue-00267.md) — к CSS.

Ранее зарегистрированные: [docs/issues/potential/issue-00019.md](../../../../../../issues/potential/issue-00019.md) (lifepath), [docs/issues/potential/issue-00033.md](../../../../../../issues/potential/issue-00033.md) (положительный attackModifier), [docs/issues/potential/issue-00061.md](../../../../../../issues/potential/issue-00061.md), [docs/issues/potential/issue-00064.md](../../../../../../issues/potential/issue-00064.md), [docs/issues/potential/issue-00065.md](../../../../../../issues/potential/issue-00065.md) (источники пустого/неизвестного skill), [docs/issues/potential/issue-00066.md](../../../../../../issues/potential/issue-00066.md) (ranged melee bonus), [docs/issues/potential/issue-00069.md](../../../../../../issues/potential/issue-00069.md), [docs/issues/potential/issue-00070.md](../../../../../../issues/potential/issue-00070.md) (merge/prepared свойства), [docs/issues/potential/issue-00237.md](../../../../../../issues/potential/issue-00237.md) (замещение), [docs/issues/potential/issue-00242.md](../../../../../../issues/potential/issue-00242.md) (undefined weapon), [docs/issues/potential/issue-00244.md](../../../../../../issues/potential/issue-00244.md) (preview монстра), [docs/issues/potential/issue-00257.md](../../../../../../issues/potential/issue-00257.md), [docs/issues/potential/issue-00258.md](../../../../../../issues/potential/issue-00258.md) (схемы сообщений). [docs/issues/potential/issue-00238.md](../../../../../../issues/potential/issue-00238.md) не переносится: оружейная extra-атака запрашивает STA−3. [docs/issues/potential/issue-00182.md](../../../../../../issues/potential/issue-00182.md) относится к последующей обработке fumble; здесь sender передан как Actor. [docs/issues/potential/issue-00032.md](../../../../../../issues/potential/issue-00032.md) — getAllLocations, а не выбор одиночной локации.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; полный файл | Первичная карточка, определения и потребители сверены; [журнал](../../../../review-log.md#task-0003041) |
