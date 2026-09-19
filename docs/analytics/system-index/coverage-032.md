# TASK-0006.032 — Сотворение магии: ресурсы, бросок и действия сообщения

**Актуализация 14.3.1.00107 / TASK-0011.007:** [локальные результаты](../task-0011-static-checks.md#task-0011007). STA записывается с await и проверкой возвращённого Document; self/target статусы и AE объединены в collectSpellEffects/createEffectDelivery. Общий preflight предшествует всем эффектам, JSON-карточка сохраняет сроки/получателей/исходный бросок; region остаётся отдельным вызовом без await. proc-000445/451/452 обновлены, прямая доставка через четыре прежних helper больше не описывает castSpell. Ниже сохранён исходный аудит .032; его численность и описание неожидаемых записей относятся к тому срезу. Игровой B07 впереди.

2026-09-16; rusbar-main, исходный HEAD `ce02e31707eec4e590c9d559186c70f33a364f80`, дерево в начале чистое. [Задача](../../tasks/task-0006.032.md), [запросы](examples/expansion-032-queries.json), [тесты](tests/test_expansion_032.py).

<a id="overview"></a>
## Результат и пределы

Добавлены 75 сущностей, 340 отношений и 13 процессов. Всего 5244 сущности, 14759 отношений, 453 процесса (1494 шагов, 2826 переходов), 410 границ. Определения в 304/615 файлах: два словаря en/ru complete, остальные 302 partial. Роли: 227 основных/77 смежных/311 без определений. Отношения в 308 файлах, локальные шаги процессов в 156.

Сохранены прежние ID/владельцы, 14419 отношений и 440 процессов. Уточнены восемь прежних сущностей: castSpellMixin/castSpell, _prepareSpells V2/V1, _onItemDisplayInfo, tab-magic, spellItem и граница editor→cast. Новые определения не делают файл complete. Это справочник текущего кода; игровые исходники, мир, аудит и issues не изменялись.

| Файл | Включённая область и остаток |
| --- | --- |
| [module/actor/mixins/castSpellMixin.js](../../../module/actor/mixins/castSpellMixin.js) (src-000011) | Оба метода и ветвления прочитаны целиком; полный локальный cast индексирован. Runtime/мир/concurrency и общие helpers имеют отдельные partial границы. |
| [templates/dialog/combat/spell-attack.hbs](../../../templates/dialog/combat/spell-attack.hbs) (src-000508) | Все 6 controls/условия, callback и selectOptions; браузерный выбор и submit не воспроизводились. |
| [templates/chat/combat/spellItem.hbs](../../../templates/chat/combat/spellItem.hbs) (src-000487) | Все flavor readers/условия, три действия и status HTML, raw/typed различия; core render/обогащение partial. |
| [templates/partials/character/tab-magic.hbs](../../../templates/partials/character/tab-magic.hbs) (src-000525) | Списки V2, tab groups/vigor, прежние IP/focus сохранены; общий Actor form lifecycle и браузер partial. |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../templates/sheets/actor/partials/character/spell-type-list.hbs) (src-000561) | Списки/ID/handlers и магические поля описания, альтернативные компоненты; немагические fallback поля component/gear не детализированы. |
| [templates/partials/monster/monster-spell-tab.hbs](../../../templates/partials/monster/monster-spell-tab.hbs) (src-000539) | Legacy списки, панели, inline STA/focus; preload/старое inclusion не доказывают активный V2 render, полный legacy runtime не заявлен. |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) (src-000027) | _prepareSpells целиком, связь с context/getList и listeners; прочий ActorSheet уже частично представлен прежними порциями. |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) (src-000028) | _prepareSpells уточнён до полного тела; прочие legacy методы/реальная достижимость остаются partial. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) (src-000029) | Magic PARTS/TABS/context к общим спискам; остальной Character sheet прежний partial. |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js) (src-000031) | Magic PARTS/TABS/context к общим спискам; Monster V2 не включает старый spell tab. |
| [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js) (src-000043) | Переиспользованы listeners/_onItemRoll/displayInfo/SpellDisplay; клавиши теряются в magic useItem dispatch; остальные действия прежние. |
| [module/actor/witcherActor.js](../../../module/actor/witcherActor.js) (src-000047) | useItem/getList/примеси/location стык, прочие Actor процессы прежние partial. |
| [module/data/item/mixin/spellRegionMixin.js](../../../module/data/item/mixin/spellRegionMixin.js) (src-000117) | createSpellRegion/fromItem options mismatch адресован; геометрия/lifecycle/сцена/таймер и callbacks задача .033. |
| [module/scripts/chat.js](../../../module/scripts/chat.js) (src-000193) | onHeal/onShield перечитаны: разные цели и HTML values, прежние процессы сохранены. |
| [module/scripts/combat/combat.js](../../../module/scripts/combat/combat.js) (src-000195) | onDamage callback связывает message с Item.rollDamage, остальной combat прежний. |
| [module/scripts/rolls/extendedRoll.js](../../../module/scripts/rolls/extendedRoll.js) (src-000202) | extendedRoll перечитан целиком для fumble/DC/showResult; прежние процессы неизменны. |
| [module/scripts/statusEffects/applyStatusEffect.js](../../../module/scripts/statusEffects/applyStatusEffect.js) (src-000205) | Raw duration/status self-target и ручная status кнопка; существующие delivery границы сохранены. |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../module/scripts/temporaryEffects/applyActiveEffect.js) (src-000206) | Raw duration/фильтры/query/clone/await проверены для handoff; мир не исполнялся. |
| [templates/sheets/actor/monster-sheet.hbs](../../../templates/sheets/actor/monster-sheet.hbs) (src-000550) | Только legacy magic inclusion: не заявлено покрытие всего монолита. |
| [module/setup/handlebars.js](../../../module/setup/handlebars.js) (src-000211) | Три пути preload, остальные шаблоны/исполнение прежние partial. |

<a id="entry"></a>
## Списки Actor и вход в применение

Оба зарегистрированных листа V2, Character и Monster, используют tab-magic и общий spell-type-list. Шесть magicTabs: all, magic, rituals, hexes, magicalGift, focus. В all и отдельных вкладках повторены те же шесть групп: три уровня заклинаний, ритуалы, порчи, магические дары. Повторный показ не создаёт новые Item.

_prepareContext передаёт настоящие документы и ожидает _prepareSpells. getList(type) исключает isStored и сортирует по sort. Для novice/journeyman/master допускаются class Spells/Invocations/Witcher; MagicalGift выбирается по class независимо от level. Hex/Ritual — отдельные типы. learned/hidden не фильтруются здесь; неизвестный class/level может остаться лишь в context.spells, который эти partials напрямую не выводят.

Каждая строка spell-type-list несёт spell.id в data-item-id. itemListener привязывает .spell-roll к _onItemRoll; он вызывает useItem(id,{alt,ctrl,shift}) без await/return. useItem проверяет существование Item и тип spell/hex/ritual, затем возвращает castSpell(item), уже без keyboard options. Прямой вызов castSpell таких guards не имеет. item-display-info только раскрывает .item-info; item-chat запускает отдельный вывод описания Item, не cast.

inventory-items-summary получает itemType и унаследованный spellType и формирует add-item; создание Item относится к прежним общим действиям. Vigor, magicIP и четыре focus слота формы отделены от параметров prompt. MagicIP/focus writers переиспользованы из .030/.031.

<a id="legacy"></a>
## Старый лист монстра

monster-spell-tab загружается preload и включается в старый monster-sheet.hbs:302. У него шесть собственных таблиц, spell._id в строках, .spell-roll, переключение system.pannels по .spell-display и .inline-edit STA. _prepareSpells V1 формирует аналогичные группы.

Текущая registerSheets регистрирует Monster V2 с PARTS.magic=tab-magic. Поэтому наличие старого partial и listeners не доказывает его исполнение в текущем листе. Связи legacy помечены условными. В активном V2 используются native details, а не прежние панели. Подключение старого листа внешним модулем или пользовательским кодом здесь не проверялось.

<a id="ev"></a>

**Обновление 2026-09-19, .00105:** [TASK-0011.005](../task-0011-static-checks.md#task-0011005) ограничила компенсацию min(EV,max(0,ignoredEvWhenCasting)); EV уже после общего ignoredArmorEncumbrance. Manual/optional остаются в prepareCheck, не обрезаются. Утверждения о полном ignore и addActiveEffects ниже относятся к исходному срезу; современный вход описан также в .008/.00066.
## Формула основного броска

castSpell сначала получает createBaseDamageObject, затем собирает `1d10 + WILL.value + skills.will[usedSkill.name].value`. getUsedSkill каждой модели переиспользован из .031. Характеристика возвращённой записи карты не заменяет WILL и группу skills.will. Метаданные getItemAttack формируются другим методом и могут расходиться с формулой; клавиши в этот вызов не передаются (прежняя issue64).

addActiveEffects(usedSkill.name) и addAttackModifiers добавляют подготовленные модификаторы. getArmorEcumbrance уже возвращает неотрицательный EV. Только при EV>0 код добавляет −EV и полный positive ignoredEvWhenCasting. Ограничения компенсации величиной EV нет: EV1 и ignore3 дают +2; при EV0 компенсация не добавляется (issue254). Настройка displayRollsDetails изменяет подписи формулы.

После prompt знаковые сравнения customModifier определяют добавление его строки; extra attack добавляет −3 к броску и +3 к оплате. causeDamages дополнительно вызывает getLocationObject и добавляет modifier зоны. Без causeDamages location control отсутствует и зона не применяется.

<a id="prompt"></a>
## Диалог и значения controls

| Control | Когда присутствует | Callback / предел |
| --- | --- | --- |
| location | causeDamages | .value либо undefined; randomHuman/randomMonster и семь конкретных зон |
| isExtraAttack | всегда | .checked boolean |
| staCost | staminaIsVar | .value строка, HTML value=1; иначе Number модели stamina |
| focus | хотя бы один положительный слот | .value либо 0; selectOptions без blank |
| secondFocus | то же | .value либо 0; blank='' |
| customMod | всегда | .value строка, HTML value=0 |

Четыре положительных focus.value становятся options со своими числовыми value и label name(value). selectOptions ядра не подменяет их ключом focusN. Первый select не имеет blank, второй имеет; запрета выбрать тот же фокус дважды нет. Слоты не расходуются и не изменяются.

STA/custom inputs текстовые, без min/max/step/required. Свой callback читает DOM непосредственно, не использует FormDataExtended или NumberField очистку. DialogV2.prompt ожидается с rejectClose:true. Закрытие отвергает Promise; локального catch нет, запрос STA ещё не запускался. Фактическое браузерное взаимодействие не воспроизводилось.

<a id="cost"></a>
## Оплата STA отделена от силы

Сначала `origStaCost=staCostTotal`, затем из total вычитается сумма Number(focusValue)+Number(secondFocusValue), при extra добавляется 3, при total<1 назначается 1. Новое STA — текущее значение минус total. Только newSta<0 приводит к уведомлению и раннему return. При NaN сравнения не срабатывают, и запрос update получает NaN. Нулевой/отрицательный исходный ввод может дать оплату1 и отдельную нулевую/отрицательную силу (issue245).

Actor.update запрашивает абсолютное system.derivedStats.sta.value без await. Ошибка последующих вычислений не отменяет уже запущенный запрос. Возвращённый Roll не доказывает сохранение STA; два параллельных применения читают подготовленное значение независимо (issue251). Vigor в castSpell не проверяется. Минимум относится к оплате, не к origStaCost. Исходная величина используется для variable damage/shield/percentage и третьего аргумента createSpellRegion.

<a id="multiply"></a>
## calcStaminaMulti

Метод делает parseInt(origStaCost), удаляет первый /STA, при наличии d умножает префикс перед первым d и приклеивает первую оставшуюся часть; иначе выполняет JS умножение. Не вызывает Roll и не является общим разборщиком формул.

| Вход | Результат из выражений метода |
| --- | --- |
| STA3, 2d6+1/STA | 6d6+1 |
| STA2.9, 2/STA | 4 |
| STA3, 2+1/STA | NaN |
| value=null/undefined | Ошибка чтения .replace |

Это вычислительные примеры чтения кода, не новый запуск игрового сценария. Полные выражения, дробная сила и несколько d не поддерживаются обычным масштабированием (issue246).

<a id="prepared"></a>
## Raw damage, shield и heal

createBaseDamageObject отдаёт properties ссылкой на prepared Item.system.damageProperties. При causeDamages && staminaIsVar масштабируется damage, затем каждый varEffect.percentage присваивается обратно через этот alias. toObject(false) вызывается позднее, уже после формирования flavor. Повторное применение до пересоздания prepared модели может накапливать множитель; это не Item.update и не доказанное изменение source/БД (issue247). Optional chaining после Object.values не защищает его аргумент undefined.

Raw damage получает formula, location, originalLocation и type; actual rollDamage запускается лишь кнопкой позднее. createsShield независимо задаёт raw shield и при variable масштабирует его. doesHeal независимо задаёт raw heal, но variable ветка обращается к свободному идентификатору heal, вызывая ReferenceError до вызова calcStaminaMulti. Это происходит после запроса STA и до основного броска/сообщения (issue134).

<a id="heal"></a>
## Действия damage, shield и heal

| Кнопка / helper | Откуда значение | Получатель и ожидание |
| --- | --- | --- |
| damage / onDamage | typed message.system.damage; Item по system.attack.itemUuid | Item.rollDamage без await; дальнейшие процессы .017 и нанесения урона отдельны |
| shield / onShield | raw data-shield; data-actor из Actor источника | В update источника передаётся строка для shield.value без Roll и await; хранение проходит NumberField |
| heal / onHeal | parseInt(raw data-heal) | Первая target.actor → первая controlled.actor → user.character; update HP без await, только верхнее ограничение max |

Тип строки относится к аргументу update, а не к гарантированному типу сохранённого поля. Формула в shield не бросается; heal вида 2d6 становится числом2 (issue249). Отрицательное heal снижает HP, нечисловое даёт NaN; нижнего ограничения нет (issue256). Actor из data-actor у лечения нужен для текста источника, а не выбора получателя. При отсутствующем источнике оба обработчика обращаются к actor.name без guard; у heal запрос HP уже мог быть запущен, у shield используется optional update (issue255). Обработчики onDamage/onHeal/onShield и их прежние процессы не продублированы новым обработчиком.

<a id="duration"></a>
## Длительность: raw, HTML и typed сообщение

Truthy duration сначала очищается от всех нецифровых символов: результат строка, единицы и границы чисел потеряны. Если regex NdM найден где угодно, бросается первый пробельный токен, а не само совпадение; raw duration становится total этого отдельного Roll, текст — anchor и остаток исходной строки. Несколько чисел/единицы не нормализуются; ошибка формулы возможна после запроса STA (issue250).

Raw duration непосредственно передаётся status/AE helpers и региону, а также data-duration ручной status ссылки. В typed chat.damageData schema объявлены itemUuid/formula/crit/strike/type/originalLocation/location/properties; duration, heal, shield и raw item там отсутствуют. При очистке SchemaField эти лишние поля не становятся сохранённым system.damage (issue257). HTML flavor уже создан, его data-heal/data-shield/data-duration — отдельный канал. Поэтому нельзя делать вывод о наличии длительности downstream по её существованию в local damage.

Региональная issue146 описывает дальнейший отсчёт без корректной числовой длительности. Здесь зафиксирована граница producer; весь отсчёт относится к .033.

<a id="message"></a>
## Публикация, fumble и DC

Legacy подготовка selfEffects описания проверяет .length и вызывает forEach, но актуальное поле — TypedObject. Такие записи пропускаются в flavor, хотя последующая Object.values доставка их читает (issue133). Статус ищется в CONFIG.WITCHER.statusEffects. Все кнопки формируются до основного Roll и не проверяют его fumble.

После await renderTemplate properties заменяются plain копией; создаётся обычный ChatMessageData(type attack), затем RollConfig({showResult:false}). Threshold остаётся −1. difficultyCheck ритуала выводится только текстом в HBS; в extendedRoll он не передаётся, проверка success по DC не производится (issue252).

extendedRoll ожидается и сохраняет rollTotal; критический/провальный первый d10 приводит к отдельному броску и итоговому Roll с options.fumble. showResult:false предотвращает его собственную публикацию; cast затем отдельно ожидает roll.toMessage(messageData). В прочитанном ядре toMessage строит typed ChatMessage и возвращает create Promise. Публикация не подтверждает выполнение других ранее/позднее запущенных Promise.

При fumble опубликованные кнопки damage/heal/shield остаются и их обработчики не вводят проверку fumble (issue253). Неуспех по DC, fumble и ошибка JavaScript — разные ветви.

<a id="delivery"></a>
## Статусы и ActiveEffect

После await toMessage сначала вызывается optional createSpellRegion, затем проверяется !roll.options.fumble. Только внутри этого условия идут четыре независимых вызова: status self через Object.values(selfEffects??{}), AE self с applySelf, status targets с onCastEffects, AE targets с applyOnTarget. Ни один не ожидается castSpell. Ошибка async helper не обязательно останавливает оставшиеся вызовы; синхронная ошибка вычисления аргумента может остановить тело.

Status ID и embedded ActiveEffect — разные каналы. Прямой status вызов не передаёт percentage/varEffect. Self получает this.uuid; Targets helper использует game.user.targets на момент его запуска. При пустых targets status helper возвращает; при выбранных целях Hex/Ritual передают отсутствующее onCastEffects и Object.values(undefined) отвергает отдельный Promise (issue248).

AE helper меняет duration.rounds у переданных эффектов, затем создаёт собственные копии с очищенными флагами применения. Для чужого Actor отправляет query; в этой ветке duration не передаётся отдельным аргументом, хотя source effects уже изменены. Владельческий createEmbeddedDocuments ожидается внутри helper, но не родительским cast. Query/status-toggle/таймер иммунитета и интеграция StatusCounter остаются прежними внешними границами .008. Ручная a.apply-status выбирает getCurrentCharacter и является отдельным поздним действием.

<a id="region"></a>
## Передача региону и отсутствие расхода компонентов

cast передаёт createSpellRegion(roll,rawDamage,{stamina:origStaCost}) до fumble guard и без await. Примесь Spell/Ritual проверяет template create/type/size, затем запускает fromItem(...,{roll,damage,options}). fromItem ожидает flagOptions и по умолчанию пишет пустой options; переданная stamina теряется этим именованием (issue139). В flags.duration используется raw damage.duration. Геометрия, сцена, behaviours/Macro, удаление визуализации и отсчёт остаются [TASK-0006.033](../../tasks/task-0006.033.md).

В castSpell/calcStaminaMulti нет чтения списков ritualComponentUuids/alternateRitualComponentUuids и нет их уменьшения/удаления. V2 показывает только альтернативный prepared список с прежними name/img несовпадениями, сообщение перебирает main и печатает alternate целиком (issue135). Эти отображения не являются расходом материалов. Отсутствие операции в прочитанных телах не исключает внешний Macro или модуль.

## Сверка доказательств

Прочитаны оба метода castSpellMixin целиком, все семь основных областей, указанные непосредственные consumers/helpers и актуальные контракты ядра ниже. Сопоставлены релевантные разделы семи карточек и полностью R009-07–R009-14, R011-07 [позднего аудита](../code-audit/cross-check-0002.md). Полностью перечитаны существующие issues 133–135,139,146,245–257. Issue64 используется как ранее проверенная граница .031, а не новое воспроизведение. Исторические даты/запуски не переписываются.

| Ядро Foundry 14.367.0 | Прочитанные строки и контракт | SHA-256 |
| --- | --- | --- |
| `/opt/foundryvtt/client/applications/api/dialog.mjs` | 264–276,369–375,405–424: prompt→wait; собственный button callback ожидается; close при rejectClose отвергает Promise. | `4e2d299eaa931d96df1839e64a2defc60b6b95ee89a3e1d32d60b99040899343` |
| `/opt/foundryvtt/client/applications/handlebars.mjs` | 460–499: selectOptions: object value/label, blank передаётся select builder; числовой value перекрывает имя focusN. | `0c5959e0ebdf5847277fba3284d76ee535084e022d087659fd0791e5ccd3545c` |
| `/opt/foundryvtt/client/dice/roll.mjs` | 926–953: toMessage включает rolls, создаёт typed ChatMessage и возвращает create Promise при create=true. | `a27f498f7b3864a1baa7cebbb1ccb611f9796720b4a4d153df779803b995c7ff` |
| `/opt/foundryvtt/common/data/fields.mjs` | 1066–1097,1100–1145: SchemaField cleaning и prune неизвестных keys; поля, которых нет в damageData, не становятся объявленной частью сообщения. | `efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01` |

Node/DOM/мир/сеть и несколько клиентов не запускались. Прочитанное ядро обозначено boundary, не полное индексирование Foundry.

## Новые процессы

<a id="proc-000441"></a>
### proc-000441 — Списки магии в Actor контексте

_prepareContext ожидает _prepareSpells; отдельный от последующего DOM события.

`list` | `groups` | `other`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000442"></a>
### proc-000442 — V2 список магии → useItem → castSpell

Независимый клик существующего .spell-roll в активном V2 DOM.

`click` | `handler` | `dispatch` | `cast`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000443"></a>
### proc-000443 — Формула броска магии: WILL, навык и EV

До prompt; никакой STA/сообщения ещё нет.

`base` | `mods` | `ev`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000444"></a>
### proc-000444 — Выбор STA, фокусов и параметров магии

Prompt ожидается до расхода ресурса; собственный callback возвращает строки.

`focus` | `render` | `wait` | `callback`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000445"></a>
### proc-000445 — Исходная сила и фактическая оплата STA

После подтверждения prompt; origStaCost живёт отдельно от total.

`price` | `guard` | `write` | `display`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000446"></a>
### proc-000446 — Ограниченный множитель calcStaminaMulti

Прямой метод и его callers; без ядра Roll.

`int` | `dice` | `numeric`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000447"></a>
### proc-000447 — Raw duration и текст сообщения

Truthy Item duration; после запроса STA, до основной атаки.

`guard` | `parse` | `roll` | `text`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000448"></a>
### proc-000448 — Подготовка damage и процентов эффектов

Независимый producer rawDamage при causeDamages; не нанесение урона.

`guard` | `scale` | `effects` | `location`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000449"></a>
### proc-000449 — Raw shield и heal в одном применении

Независимые флаги; без автоматического применения ресурса.

`shield` | `heal`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000450"></a>
### proc-000450 — Flavor → typed сообщение → основной бросок

После raw producers; создание сообщения ожидается отдельно от STA.

`self-info` | `flavor` | `plain` | `roll` | `publish`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000451"></a>
### proc-000451 — После сообщения: region, fumble, статусы и AE

toMessage уже завершился; запуски region и helpers не ожидаются.

`region` | `fumble` | `status-self` | `ae-self` | `status-target` | `ae-target` | `return`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000452"></a>
### proc-000452 — Полное локальное исполнение castSpell

Вход от useItem либо прямой вызов; вложенные этапы раскрыты отдельными процессами.

`formula` | `prompt` | `cost` | `sta` | `payload` | `flavor` | `roll` | `region` | `guard` | `effects` | `return`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

<a id="proc-000453"></a>
### proc-000453 — Три действия сообщения магии имеют разных получателей

Позднее независимое DOM событие; сообщение уже сохранено, отображение кнопки не вызов.

`buttons` | `damage` | `shield` | `heal`; ветви, условия и sync/await/scheduled/unknown сохранены в JSONL.

## Проверки

Проверены все 278 тестовых методов в 31 модуле и 855 примеров CLI, включая 43 новых по IQ-01–IQ-08; ошибок в итоговых результатах нет. Исторические проверки выполняются на предусмотренных прежними тестами срезах. Это проверки справочника по исходникам, без запуска игрового сценария. Перекрёстно сверены исходные адреса/владельцы, оба конца отношений, readers/writers, ветви и выходы, refs/facets/роли. [Протокол](review-log.md#task-0006032). Следующая — [TASK-0006.033](../../tasks/task-0006.033.md); родитель in-progress.