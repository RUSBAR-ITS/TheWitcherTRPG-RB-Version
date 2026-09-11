# module/actor/sheets/WitcherActorSheetV1.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a2670a0a10c62b28d836b1a57577c4836f14cf20` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.025](../../../../../../tasks/task-0003.025.md), 2 файла, 625 логических строк |
| Запись перекрёстной сверки | [TASK-0003.025](../../../../review-log.md#task-0003025) |

## Назначение файла

Класс листа Actor на прежнем API foundry.appv1.sheets.ActorSheet. Хранит синхронный getData, общие действия и 10 примесей. В текущем дереве module/templates не найдены его импорт, зарегистрированный экземпляр или наследник; его код описан как не подключённая ветвь, без приписывания поведения действующим листам.

## Условия использования

Нет прямой или косвенной регистрации через registerSheets. Текущие WitcherCharacterSheet/WitcherMonsterSheet импортируют WitcherActorSheet (V2), а Loot/Mystery имеют свои базовые классы. Если V1 будет подключён извне, нужны CommonActorData, CONFIG.WITCHER, jQuery и Array.prototype.cost, который устанавливает другой модуль V2. Сам V1 массивы не расширяет; собственный шаблон/defaultOptions не задаёт.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherActorSheetV1 | default class:14 | Наследует foundry.appv1.sheets.ActorSheet | Экспорт есть, потребитель в checkout не найден | Базовый legacy API; getData синхронный |
| statMap, skillMap | Поля:15–16 | Ссылки на CONFIG.WITCHER | Примеси и customSkills | Не копирует справочники |
| uniqueTypes | Массив:18 | profession/race/homeland | itemMixin._isUniqueItem | Потенциальное переопределение в наследнике |
| configuration | Поле:21 | undefined | _renderConfigureDialog | optional render безопасен при отсутствии |
| 10 Object.assign | 290–302 | stat → skill → customSkill → item → activeEffect → deathsave → criticalWound → note → heal → contextMenu | Копирование в prototype | Нет currencyConverterMixin; дубли имён этих примесей не найдены |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| getData() | Actor с CommonActorData; super.getData синхронный | context | Настройки/CONFIG; actor.toObject(false).system, фильтр Item, сумма HP; шесть _prepare* без await; категории и isGM | Копия system, но items — живые документы; не создаёт systemFields/criticalWounds/enrichedText |
| _renderConfigureDialog() | configuration может отсутствовать | Promise<void> | configuration?.render(true) | Не ожидает render; отсутствие конфигурации безопасно |
| _prepareCustomSkills(context) | Все actor.items; CONFIG.WITCHER.statMap | customSkills по девяти основным name | type===skill; attribute должен точно совпасть с именем группы | Сохраняет исходный порядок actor.items; неизвестные/пустые attribute не отображаются через группы |
| _prepareGeneralInformation(context) | context.actor | oldNotes и notes | getList('note'); actor.system.notes | notes ссылается на массив модели; старый Item note не преобразуется |
| _prepareSpells(context) | getList | spells, noviceSpells, journeymanSpells, masterSpells, hexes, rituals, magicalgift | Три разрешённых class и три level; MagicalGift независимо от level | getList исключает isStored, сортирует sort; неизвестные class/level остаются лишь в общем spells |
| _prepareItems(context) | context.items | enhancements, runeItems, glyphItems, containers, totalWeight, totalCost | Те же фильтры V2; context.items.cost() зависит от глобального расширения в V2 | Синхронный; не вызывает criticalWound.enrichedText |
| _prepareWeapons(context) | weapon либо enhancement c type='weapon' и applied==false | context.weapons | Если enhancements>0 и не равно enhancementItemIds.length, создаёт массив длины по циклу i<enhancements, сохраняя прежние элементы или {} | Меняет system.enhancementItems настоящего Item; может обрезать реальные улучшения; не меняет source/ID и не вызывает update |
| _prepareArmor(context) | Те же type/applied фильтры | context.armors и padding enhancementItems | При enhancements>0 и несовпадении длины ID создаёт массив по циклу; пустой JSON {} заменяет новым {} | Меняет подготовленную ArmorData; V2 такого цикла не содержит; source не записывает |
| activateListeners(html) | jQuery-обёртка с DOM в html[0] | Семь общих привязок, десять внешних listener/contextMenu | Сначала super.activateListeners(html); свои .find; примесям передаёт html[0]; focusin→_onFocusIn | Нет конвертера валют; проверка V1 на фасаде, не браузерное использование |
| _onInitRoll(event) | Actor | Promise<void> | rollInitiative({createCombatants:true,rerollInitiative:true}) | Не ожидает/возвращает результат Actor; event не используется |
| _onCritRoll(event) | Roll и ChatMessage API | Promise<void> | await new Roll('1d10x10').evaluate({async:true}); new ChatMessageData(actor); toMessage | Ожидает оценку, не публикацию; без RollConfig/extendedRoll; данные переданы реальным ChatMessageData |
| _onRecoverSta(event) | sta.value/max и rec.value | Promise после render; два async callback | Модальное окно, Recovery Action: value+rec.value; Full Recovery: max; если value>=max, уведомление и return | Render не означает выбор/закрытие; update не ожидается; добавление не ограничено max |
| _onVerbalCombat() | actor.verbalCombat из actor/mixins/verbalCombatMixin | Promise<void> | Вызывает Actor.verbalCombat без аргументов | Не ожидает вложенный prompt/бросок; отмена в реальном потребителе использует rejectClose=true |
| _onLifeEventDisplay(event) | lifeEvents — объект по ключу dataset.event | update system.general.lifeEvents.<key>.isOpened | preventDefault; обращение lifeEvents[dataset.event] и инверсия | В отличие от V2 не требует find/массива; отсутствующая запись даёт TypeError; update не ожидается |
| _canDragStart(selector) | Любой selector | true | Без проверки в override | Внешний API V1 обычно проверяет права; этот класс не подключён |
| _canDragDrop(selector) | Любой selector | true | Без проверки в override | itemMixin._onDropItem отдельно проверяет actor.isOwner; не доказательство обхода серверных прав |
| _onFocusIn(event) | currentTarget с select() | undefined | currentTarget.select() | В V2 это inline callback, в V1 отдельный метод |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| statMixin | [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js) | Именованный import; Object.assign prototype | statListener: .stat-roll, .reputation-roll, .luck-minus/reset, .adrenaline-minus/plus | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| skillMixin | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | Именованный import; Object.assign prototype | skillListener: .profession-roll, .skill-display, data-action=rollSkill/level-up; calc_total_skills доступен наследнику | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| customSkillMixin | [module/actor/sheets/mixins/customSkillMixin.js](../../../../../../../module/actor/sheets/mixins/customSkillMixin.js) | Именованный import; Object.assign prototype | customSkillListener: #custom-rollable, .remove-custom-skill, раскрытие и редактирование модификаторов | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| itemMixin | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | Именованный import; Object.assign prototype | itemListener: CRUD, inline-edit, carried/equipped/learned, enhancements, item/spell roll; _onDropItem для inherited Drop | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| activeEffectMixin | [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../../../module/actor/sheets/mixins/activeEffectMixin.js) | Именованный import; Object.assign prototype | prepareActiveEffectCategories; activeEffectListener для .effect-control/display | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| deathsaveMixin | [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | Именованный import; Object.assign prototype | deathSaveListener: .death-roll, .death-minus/plus | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| criticalWoundMixin | [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) | Именованный import; Object.assign prototype | criticalWoundListener: .add-crit, .delete-crit, data-action=treatCriticalWound | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| noteMixin | [module/actor/sheets/mixins/noteMixin.js](../../../../../../../module/actor/sheets/mixins/noteMixin.js) | Именованный import; Object.assign prototype | noteListener: .add-note/delete-note | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| healMixin | [module/actor/sheets/mixins/healMixin.js](../../../../../../../module/actor/sheets/mixins/healMixin.js) | Именованный import; Object.assign prototype | healListeners: .heal-button, открытие отдыха; методы recoverActor и restDialogListener принадлежат примеси | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| itemContextMenu | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Именованный import; Object.assign prototype | itemContextMenu: ContextMenu на .item, шесть пунктов через собственные фабрики | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | default import; constructor | _onCritRoll: speaker от actor, type=base, flavor undefined, пустые system и flags.TheWitcherTRPG | constructor(actor,flavor,type='base',system={},flags) |
| statMap, skillMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | CONFIG.WITCHER, ссылка | Поля экземпляра; customSkills группируются по name записей origin='stats' | В statMap 9 основных характеристик; derivedStats в группы не входят |
| useOptionalAdrenaline, displayRollsDetails, useOptionalVerbalCombat, displayRep | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | game.settings.get | Четыре настройки контекста; displayRollDetails изменяет глобальную формулу инициативы | Имена регистрации сопоставлены со строками чтения |
| getList, getTotalWeight, update, verbalCombat | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js); [module/actor/mixins/verbalCombatMixin.js](../../../../../../../module/actor/mixins/verbalCombatMixin.js) | Actor; метод примеси и внешний Document.update | Сортированные списки без stored, общий вес всех calcWeight и валюты; общие действия | getList/getTotalWeight исполнены; verbalCombat ожидает prompt с rejectClose=true |
| system, notes, combatEffects.temporaryEffects.temporaryHp | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/temporaryEffectsData.js](../../../../../../../module/data/actor/templates/common/temporaryEffectsData.js) | Поля DataModel | temporaryHpSum добавляется в копию system, notes отдельно берётся из живого actor.system | Настоящие CharacterData/MonsterData и source после подготовки проверены |
| CharacterData, MonsterData | [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js); [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Типы Actor через schema | Оба зарегистрированных наследника общего листа используют CommonActorData | Обе реальные модели проверены на getData V1 через фасад; действующие листы наследуют V2 |
| enhancements, enhancementItemIds, enhancementItems | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js); [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js); [module/data/item/enhancementData.js](../../../../../../../module/data/item/enhancementData.js); [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | Поля и getter подготовленной модели | Фильтры weapon/armor/enhancement; список слотов оружия меняет enhancementsEffects | prepareDerivedData разрешает ID; getter читает текущий enhancementItems |
| quantity, cost, weight, isStored, isHidden, isCarried | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Поля общей модели Item | Array.cost; основной фильтр проверяет только isStored; расчёт веса — отдельный метод модели | Number(quantity), Number(cost); не оценка dice-формул |
| SkillItemData.attribute | [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js) | Item type=skill | Группы customSkills из всей actor.items без собственной сортировки; пустой/неизвестный attribute теряется для этих групп | 8 полей модели; isStored/isHidden в её схеме отсутствуют |
| SpellData.class/level | [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js); [module/data/item/hexData.js](../../../../../../../module/data/item/hexData.js); [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js) | Типы Item и фильтры | novice/journeyman/master × Spells/Invocations/Witcher, magicalgift отдельно; hexes/rituals через getList | Группа 06 с настоящей SpellData и 20 сочетаниями |
| isAppliedTemporaryItemImprovement, isTemporaryItemImprovement, isDisabled | [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Геттеры ActiveEffect | Первый читает system.isTransferred; категории также используют isTemporary | Getter-определения просмотрены; isSuppressed и isDisabled различаются |
| sta.value/max, rec.value | [module/data/actor/templates/common/stats/statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js) | Поля Character/Monster через DerivedStats | _onRecoverSta: добавление REC либо запись max | value NumberField без динамического max; source модели принимает 12 при max=10 |
| foundry.appv1.sheets.ActorSheet, Actor, Roll, DialogV2, $ | Foundry VTT 14.367.0 и jQuery браузера | Внешнее наследование/API | super.getData/activateListeners; общие действия как у V2 | /opt/foundryvtt/client/appv1/sheets/actor-sheet.mjs:82–89; UI и запись подменены |
| Array.prototype.cost | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Глобальный побочный эффект другого модуля | _prepareItems: context.items.cost() | V1 не определяет и не импортирует helper; точка определения в V2:26–32 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | Контроль отсутствия регистрации | Не импортирует WitcherActorSheetV1 и не регистрирует его | Отрицательный результат поиска — не вызов |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Контроль цепочки наследования | extends WitcherActorSheet, не WitcherActorSheetV1 | Текущий маршрут персонажа — V2 |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Контроль цепочки наследования | extends WitcherActorSheet, не WitcherActorSheetV1 | Текущий маршрут монстра — V2 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

context.system — сериализованная копия actor.toObject(false).system; временная сумма HP остаётся в этой копии. При этом context.items содержит настоящие Item, context.notes — actor.system.notes, statMap/skillMap/config — общие справочники. _prepareWeapons и _prepareArmor меняют подготовленные enhancementItems исходных документов. CONFIG.Combat.initiative.formula, побочные эффекты примесей и вызовы update одинаково способны затронуть общее состояние, если класс будет подключён. getData не обогащает травмы и не выбирает расу/профессию. Нельзя переносить вывод «копия system» на весь контекст. Собственных Array-расширений и definitions PARTS/TABS/DEFAULT_OPTIONS здесь нет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Класс, поля, опции и композиция | Группа 01, все Object.assign и export | Десять примесей без currency; DEFAULT_OPTIONS принадлежат V2/внешнему ядру, не этому файлу | Методы внешних примесей вне запланированных границ не разобраны полностью |
| Пустые Actor, фильтры, источники, повтор | Группы 02–07,09,17; реальные модели | Синхронный getData у настоящих Character/Monster; копия system, живые Item; V1 padding брони | Actor/базовые листы представлены фасадами |
| Живые улучшения и source | Группа 08; реальные WeaponData и enhancementsEffects | После _prepareWeapons 2 ID и 2 воздействия превращаются в 1 подготовленный элемент и 1 воздействие; source неизменен | Атака/запись/переподготовка мира не запускались |
| Действия и DOM-входы | Группы 12–16 | STA и общие действия совпадают; handler lifeEvents работает с объектом; семь общих привязок, десять входов примесей | Нет browser/Document.update/Roll/диалогов мира; slot/context применялись в памяти |
| Регистрация и потребители; общая сверка | rg по module/templates, определения методов и PARTS; .021–.025 | 37 новых файлов не пересекаются с прежними 168; границы V1/V2/Item/Actor различены | Структурная сверка всех связей не является выполнением всех игровых процессов |

## Непроверенные участки и открытые вопросы

В репозитории не найден активный маршрут V1: прежний monster-sheet.hbs сам по себе не регистрирует этот класс. Контекст и методы исполнены на фасаде внешнего ActorSheet, с реальными TypeDataModel и перехваченными операциями. Изолированное исполнение не подтверждает совместимость полного V1-приложения с Foundry 14, браузером или внешними модулями. Полный разбор внешних примесей, кроме уже описанных ранее, отложен по плану. Методы getData/_prepare* собственно V1 синхронны; асинхронные новые override в гипотетическом наследнике не проверялись.

## Связанные проблемы

[issue-00024](../../../../../../issues/potential/issue-00024.md), [issue-00054](../../../../../../issues/potential/issue-00054.md), [issue-00127](../../../../../../issues/potential/issue-00127.md), [issue-00164](../../../../../../issues/potential/issue-00164.md), [issue-00165](../../../../../../issues/potential/issue-00165.md), [issue-00166](../../../../../../issues/potential/issue-00166.md), [issue-00167](../../../../../../issues/potential/issue-00167.md). Наблюдения общих тел применимы при подключении V1; не заявлены как доказанная неисправность действующего V1 UI. issue-00024 относится к активной V2-ветви: здесь lifeEvents ожидается объектом. V1 не производит criticalWounds для современного tab-effects.hbs; сам этот HBS назначен наследникам V2.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a2670a0a10c62b28d836b1a57577c4836f14cf20`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003025) |

## Уточнение TASK-0003.026

2026-09-11, `rusbar-main`, `45a63062a2bd55939fef430609fc5dddc350b0e9`. Полностью описаны itemMixin и itemContextMenu, подключённые через Object.assign. У V1 Drop-данные проходят fromDropData→toObject до сравнения parent: parent отсутствует, сортировка своего Item не выбирается. Это проверено на фасаде, а активного потребителя V1 в checkout нет. Общий ContextMenu имеет те же несовместимые callbacks (issue-00168); передачу html[0] нельзя путать с порядком аргументов entry.

Определения: [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) и [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003026). Полный разбор новых соседних файлов вне порции не засчитывается.

## Уточнение TASK-0003.028

2026-09-11, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`: _onCritRoll:230–233 использует ChatMessageData(this.actor) и непосредственно Roll('1d10x10').toMessage. Новый полный разбор ChatMessageData подтвердил: flavor здесь undefined, но append/extendedRoll не вызываются, поэтому наблюдение undefinedsuffix из изолированного append к этому пути не переносится. Правильный объект Actor передаётся в getSpeaker; класс ChatMessageData — обычный контейнер, не схема message.system.

Полные карточки зависимости: [module/chatMessage/chatMessageData.js](../../chatMessage/chatMessageData.js.md). [Перекрёстная сверка](../../../../review-log.md#task-0003028). Это уточнение связи; исходный файл не изменён.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Полные карточки skillMixin/customSkillMixin уточняют старые события и итог навыков. V1 _prepareCustomSkills аналогично передаёт Items; monster-custom-skill-display согласован с itemId/броском/remove/open, но не содержит CRUD массива modifiers. Регистрация V1 активным листом по-прежнему не установлена.

Сверенные связи: [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js); [module/actor/sheets/mixins/customSkillMixin.js](../../../../../../../module/actor/sheets/mixins/customSkillMixin.js); [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../../../templates/partials/monster/monster-custom-skill-display.hbs). Полные карточки новых файлов — в [указателе порции](../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. Оба stat/death mixin теперь описаны полностью и используются теми же прототипными методами. Старый monster-sheet содержит stat/death селекторы; текущий V2 использует отдельные header/tab-stats. Полная регистрация/работа V1 в Foundry14 не установлена.

Сверенные источники: [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js); [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js); [templates/partials/character/tab-stats.hbs](../../../../../../../templates/partials/character/tab-stats.hbs). [Итоговая сверка третьей серии, сценарии и ограничения](../../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Полный старый monster-sheet.hbs сопоставлен с базовым контрактом V1. Ни выбора этого HBS через template в V1, ни регистрации V1 не найдено. Изолированный render старого HBS с текущей моделью не является запуском старого листа.

Связи: [templates/sheets/actor/monster-sheet.hbs](../../../templates/sheets/actor/monster-sheet.hbs.md); [templates/partials/monster/monster-details-tab.hbs](../../../templates/partials/monster/monster-details-tab.hbs.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003032).

## Уточнение TASK-0003.033

2026-09-11, `12055fee62f01c6de49967044aedef9d7cfe0632`. noteMixin полностью разобран: три функции прототипа совпадают с экспортом; activateListeners с html[0] привязывает и вызывает удаление. V1 toggle по исходному объекту ключа 10 передаёт isOpened=true. Регистрации действующего V1-листа по-прежнему не найдено; текущий tab-background не объявляется его шаблоном.

Связи: [module/actor/sheets/mixins/noteMixin.js](mixins/noteMixin.js.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003033).

## Дополнительная сверка TASK-0003.036

2026-09-11, `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; исходники не менялись.

Отрицательная сверка полного маршрута конвертера: в V1 нет import/Object.assign/currencyConverterListeners и activateListeners196–228 его не вызывает. Одинаковое имя Actor-примеси не означает одинаковые возможности листов. Текущий Character использует V2, поэтому отсутствие подключения в V1 не зарегистрировано как новая пользовательская ошибка.

Карточки процесса: [module/actor/mixins/currencyConverterMixin.js](../mixins/currencyConverterMixin.js.md), [module/actor/sheets/mixins/currencyConverterMixin.js](mixins/currencyConverterMixin.js.md), [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs.md), [templates/chat/currency-conversion.hbs](../../../templates/chat/currency-conversion.hbs.md).

[Проверки и перекрёстная сверка](../../../../review-log.md#task-0003036). Связанный файл повторно в покрытии не учитывается; правок системы нет.

## Дополнительная сверка TASK-0003.039

2026-09-11, `c598d74e34f4be51535de78b38f0601c286c5407`; исходники не менялись.

Исторический _prepareSpells имеет ту же структуру шести массивов; старый monster-spell-tab читает её и system.pannels. Его обнаруженный literal consumer — monster-sheet.hbs:302; актуальный зарегистрированный WitcherMonsterSheet использует общую tab-magic.hbs. Старый лист в браузере не запускался.

[templates/partials/monster/monster-spell-tab.hbs](../../../../../../../templates/partials/monster/monster-spell-tab.hbs) — [карточка](../../../templates/partials/monster/monster-spell-tab.hbs.md).

[Сценарии, методика и пределы проверки](../../../../review-log.md#task-0003039). Соседние определения проверены в пределах связи; это не расширяет состав шести полностью разобранных файлов.
