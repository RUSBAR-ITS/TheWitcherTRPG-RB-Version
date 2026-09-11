# module/actor/mixins/castSpellMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `c598d74e34f4be51535de78b38f0601c286c5407` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.039](../../../../../../tasks/task-0003.039.md), 6 файлов, 870 логических строк |
| Запись перекрёстной сверки | [TASK-0003.039](../../../../review-log.md#task-0003039) |

## Назначение файла

Два метода Actor: полное сотворение spell/hex/ritual и масштабирование отдельных значений по исходной стоимости STA. Объединяет бросок, диалог, расход ресурса, параметры урона/щита/лечения, сообщение, область и эффекты.

## Условия использования

castSpellMixin импортируется в witcherActor.js:5 и добавляется Object.assign:445. WitcherActor.useItem:224–235 разрешает Item по ID, для spell/hex/ritual возвращает castSpell(item); отсутствующий ID пропускается. Прямой вызов castSpell(undefined) не защищён. Один путь используется персонажем и монстром; флаги клавиш из useItem здесь не передаются в getItemAttack.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| castSpellMixin | named export let:12–287 | Контракт двух методов | WitcherActor.prototype | Вызовы из useItem и программно |
| DialogV2 | local const:10 | Ссылка на Foundry API | prompt:94 | Читает значения формы в ok.callback; rejectClose:true |
| templateInfo/data/handlebarFocusOptions | Локальные объекты castSpell | Контексты двух HBS, до четырёх фокусов | Не сохраняются как документы | actor, staCostDisplay, spellSource, durationText, selfEffects |
| damage/messageData/config/roll | Локальные данные результата | Урон, attack-сообщение, бросок | createBaseDamageObject → ChatMessageData → Roll | properties сначала ссылка на модель Item, затем toObject(false) |
| Встроенные callbacks | prompt.ok:99; forEach/filter:184,217,253–266 | Поля формы, масштабирование и применение воздействий | Внутри castSpell | forEach и вызовы внешних async-методов не создают общей цепочки ожидания |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| castSpell(spellItem) | Принадлежащий Actor Item; system.getUsedSkill; WILL и skills.will | Promise<Roll>; при недостаточной STA результат notifications.error; при ошибке rejection | Формула → диалог → расчёт STA/update → duration/damage/shield/heal → HBS → extendedRoll/toMessage → область → эффекты | await для HBS, prompt, duration Roll, extendedRoll, toMessage; update/область/эффекты не ожидает. STA запрашивается до разбора формул. Проверка !roll.options.fumble только у эффектов |
| calcStaminaMulti(origStaCost,value) | Стоимость parseInt; число либо строка | Число или строка кубов, возможно NaN; null/undefined дают TypeError | Удаляет первый /STA. Если есть d: умножает только префикс до первого d, остаток сохраняет; иначе staminaMulti*value | Не общий парсер формул; 3 и 2d6+1/STA → 6d6+1; 2.9 и 2/STA → 4; 3 и 2+1/STA → NaN |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | Прямой default import:1 | new(this, chatMessage, attack, payload):238 | Speaker от текущего Actor; flavor содержит HBS |
| applyActiveEffectToActor / applyActiveEffectToTargets | [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | Прямые named imports:2–5 | applySelf/applyOnTarget:256–266 | Получают отфильтрованные Item.effects и damage.duration; owned clone/remote query |
| applyStatusEffectToActor / applyStatusEffectToTargets | [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | Прямые named imports:8 | selfEffects Object.values и onCastEffects:253–262 | Проценты этих записей здесь не разыгрываются; целевой helper требует словарь при наличии целей |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js) | Прямой named import:6 | new({showResult:false}):245 | threshold остаётся −1; DC ритуала не передаётся |
| extendedRoll | [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | Прямой named import:7 | Бросок:247; затем ручной await toMessage | Крит/провал по первому d10; options.fumble используется после сообщения |
| createBaseDamageObject | [module/item/mixins/damageUtilMixin.js](../../../../../../../module/item/mixins/damageUtilMixin.js) | Метод Item через Object.assign | 16; itemUuid, crit, properties | properties — исходная system.damageProperties, без clone |
| getItemAttack | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Метод Item | 240 без options | Item UUID присутствует; первый attackOptions, метаданные skill могут отличаться от getUsedSkill |
| SpellData/HexData/RitualData.getUsedSkill | [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js); [module/data/item/hexData.js](../../../../../../../module/data/item/hexData.js); [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js) | Методы моделей | 27 и чтение данных магии | Сначала skillMap, затем CONFIG.magic по type/class; spellcasting fallback на spellcast |
| WILL, focus1–4, STA, lifepathModifiers | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/focusData.js](../../../../../../../module/data/actor/templates/common/focusData.js); [module/data/actor/templates/common/skills/willData.js](../../../../../../../module/data/actor/templates/common/skills/willData.js); [module/data/actor/templates/common/lifepathData.js](../../../../../../../module/data/actor/templates/common/lifepathData.js) | Поля Actor | 23–79,115–133 | Характеристика и навык уже подготовлены; фокусы — числовые значения |
| addActiveEffects / addAttackModifiers | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | Методы Actor | 32–33 | Добавка навыка/групп и боевой attackModifier, включая магию без урона |
| getArmorEcumbrance | [module/actor/mixins/armorMixin.js](../../../../../../../module/actor/mixins/armorMixin.js) | Метод Actor | 35–47 | Сумма equipped armor.encumb минус ignoredArmorEncumbrance, минимум 0; затем ignoredEvWhenCasting без ограничения остатком EV |
| getLocationObject | [module/actor/mixins/locationMixin.js](../../../../../../../module/actor/mixins/locationMixin.js); [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Делегирование статическому методу | 192–198 | Локация и modifier; head −6, torso −1, конечности −3, случайные +0 |
| DamageProperties / itemEffect | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js); [module/data/item/templates/itemEffectData.js](../../../../../../../module/data/item/templates/itemEffectData.js) | Вложенные модели | 184–187 и 236 | varEffect меняет percentage в подготовленной модели Item; toObject(false) отправляет текущие данные |
| createSpellRegion | [module/data/item/mixin/spellRegionMixin.js](../../../../../../../module/data/item/mixin/spellRegionMixin.js) | Опциональный метод SpellData/RitualData | 250, до проверки fumble | Передаёт roll,damage,{stamina:origStaCost}; внутри options/flagOptions расходятся |
| Диалог/результат | [templates/dialog/combat/spell-attack.hbs](../../../../../../../templates/dialog/combat/spell-attack.hbs); [templates/chat/combat/spellItem.hbs](../../../../../../../templates/chat/combat/spellItem.hbs) | Литеральные renderTemplate пути | 88–91;227–234 | Причина появления полей и кнопок прослежена |
| CONFIG.WITCHER и displayRollsDetails | [module/setup/config.js](../../../../../../../module/setup/config.js); [module/setup/settings.js](../../../../../../../module/setup/settings.js) | Глобальный справочник/настройка | statMap.will, statusEffects.find, названия навыков | Положительные фокусы включают селекты; статус ищется по ID |
| AttackMessageData / damageData | [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js); [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js) | Типизированный потребитель | Системный тип attack | shield/heal/duration не поля damageData; кнопки несут их в HTML flavor |
| onShield / onHeal, onDamage, defense | [module/scripts/chat.js](../../../../../../../module/scripts/chat.js); [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js); [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | Последующие действия пользователя | Кнопки сообщения и контекст защиты | Полный бой не запускается castSpell; щит/лечение отдельно рассмотрены в пределах связи |
| DialogV2, Roll, User.targets, Document.update | Foundry 14.367.0, /opt/foundryvtt | Внешние API | Асинхронные окна, броски, изменения документов | Реальные Roll/fields; окна/запись/query подменены |
| Локализация | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Подписи и динамические ключи | WITCHER.Spell.*, Dialog.*, Settings.Custom, MinValue | Раскрытые словари и настоящий fallback; Water отсутствует в обоих, customModifier только en |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | castSpellMixin / castSpell | import5, Object.assign445, useItem235 | Два метода становятся Actor API |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | castSpell через useItem | _onItemRoll и .spell-roll | Item ID из ближайшей .item |
| [templates/dialog/combat/spell-attack.hbs](../../../../../../../templates/dialog/combat/spell-attack.hbs) | data и callback формы | Шесть возможных полей | Диалог внутри castSpell |
| [templates/chat/combat/spellItem.hbs](../../../../../../../templates/chat/combat/spellItem.hbs) | spellItem/templateInfo/damage | Формирует flavor до броска | Кнопки и ссылки |
| [module/data/item/mixin/spellRegionMixin.js](../../../../../../../module/data/item/mixin/spellRegionMixin.js) | roll/damage/options | createSpellRegion receives original STA | Продолжение без await |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Формула: 1d10 + stats.will.value + skills.will[usedSkill.name].value + addActiveEffects + addAttackModifiers. При armorEnc>0 вычитает EV и целиком прибавляет положительный ignoredEvWhenCasting. customMod добавляется только при числовом сравнении <0/>0; строка 1d6 игнорируется. Extra даёт −3 к броску. Для урона добавляется modifier локации. Собственного сравнения со difficultyCheck, vigor.max, наличием компонентов или изученностью нет.

Фокус: в список входят focus1–4 с value>0, первый выбран по HTML умолчанию, второй имеет пустой вариант. Один и тот же фокус можно выбрать дважды; отдельной проверки допуска второго нет. Стоимость = max(1, Number(origStaCost)−Number(focusValue)−Number(secondFocusValue)+(extra?3:0)); NaN обходит проверки <1/<0. При достаточной STA вызывает this.update(newSta) без await. Исходное значение origStaCost сохраняется для силы и области, а не уменьшенная фокусом цена.

Duration: непустая строка сначала лишается всех нецифровых символов. При совпадении /\d+d\d+/g бросается только первый отделённый пробелом токен; результат передаётся числом и вставляется anchor в durationText. Единицы не преобразуются. Пустой текст оставляет undefined, текст без цифр — пустую строку. 1 hour 30 minutes → "130". Передача duration не доказывает сохранение срока эффекта (issue-00044).

Ветки causeDamages, createsShield, doesHeal независимы. Damage: формула или '0'; variable масштабирует формулу и varEffect.percentages, потом location/originalLocation/type. Щит: формула или '0', при variable calcStaminaMulti. Лечение: строка или '0'; variable обращается к необъявленной heal. До этого уже вызван STA update. properties эффекта урона меняются в памяти Item; исходный _source остаётся прежним, до пересчёта повторное сотворение повторно умножает процент.

Подготовка описания selfEffects использует .length/.forEach и пропускает текущий словарь. В старом массиве показываются только записи со statusEffect; блок имени без статуса пустой. Само применение после не-fumble использует Object.values, независимо от процента: статусы себе/целям и Item.effects с applySelf/applyOnTarget. При отсутствии целей helper статусов выходит до Object.values; при цели у hex/ritual onCastEffects undefined вызывает отсоединённый отказ. На fumble всё равно уже созданы сообщение с кнопками и вызов области. await castSpell ждёт сообщение, но не завершение update/эффектов/области; запись ресурса, её откат и сохранение результатов этим не доказаны.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Основные ветви и UI | Группы 01–13 | Все типы магии, списки/формы/стоимость/отмена, модификаторы, actual attack UUID | Контекст Application/DOM фасад |
| Формулы, модели, действия чата | Группы 14–26 | Мутация процента, heal ReferenceError, parseInt и щит, эффекты, fumble/DC/duration | Записи заменены; данные настоящих моделей |
| Ожидания и внешние границы | Группы 27–33 | STA update не ожидается, options теряются, remote запросы захвачены; i18n fallback | Не сеть/БД; core API placement заменён |

## Непроверенные участки и открытые вопросы

Файлы порции прочитаны целиком. Проверка: Foundry 14.367.0, Node 24.16.0, реальные модели/методы, Roll/extendedRoll, Handlebars 4.7.9, expandObject и core Localization с fallback. Диалог, Application/DOM, вывод Roll.toAnchor, запись Actor/Item/ChatMessage, UUID resolver, создание/clone ActiveEffect, canvas и query заменены фасадами. Реальные браузер, HTTP, БД, компедиумы, сетевые клиенты и жизненный цикл эффекта не запускались. Текстовые формулы проверены как поведение кода, без выбора правил книг.

## Связанные проблемы

[issue-00003](../../../../../../issues/potential/issue-00003.md), [issue-00008](../../../../../../issues/potential/issue-00008.md), [issue-00009](../../../../../../issues/potential/issue-00009.md), [issue-00033](../../../../../../issues/potential/issue-00033.md), [issue-00044](../../../../../../issues/potential/issue-00044.md), [issue-00064](../../../../../../issues/potential/issue-00064.md), [issue-00128](../../../../../../issues/potential/issue-00128.md), [issue-00133](../../../../../../issues/potential/issue-00133.md), [issue-00134](../../../../../../issues/potential/issue-00134.md), [issue-00135](../../../../../../issues/potential/issue-00135.md), [issue-00137](../../../../../../issues/potential/issue-00137.md), [issue-00138](../../../../../../issues/potential/issue-00138.md), [issue-00139](../../../../../../issues/potential/issue-00139.md), [issue-00142](../../../../../../issues/potential/issue-00142.md), [issue-00146](../../../../../../issues/potential/issue-00146.md), [issue-00186](../../../../../../issues/potential/issue-00186.md), [issue-00245](../../../../../../issues/potential/issue-00245.md), [issue-00246](../../../../../../issues/potential/issue-00246.md), [issue-00247](../../../../../../issues/potential/issue-00247.md), [issue-00248](../../../../../../issues/potential/issue-00248.md), [issue-00249](../../../../../../issues/potential/issue-00249.md), [issue-00250](../../../../../../issues/potential/issue-00250.md), [issue-00251](../../../../../../issues/potential/issue-00251.md), [issue-00252](../../../../../../issues/potential/issue-00252.md), [issue-00253](../../../../../../issues/potential/issue-00253.md), [issue-00254](../../../../../../issues/potential/issue-00254.md). Все регистрации остаются potential. Ранние проблемы областей/длительности не переименованы в новые; новая карточка ожидания относится к собственному castSpell.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `c598d74e34f4be51535de78b38f0601c286c5407`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003039) |
