# module/actor/sheets/WitcherActorSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a2670a0a10c62b28d836b1a57577c4836f14cf20` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.025](../../../../../../tasks/task-0003.025.md), 2 файла, 625 логических строк |
| Запись перекрёстной сверки | [TASK-0003.025](../../../../review-log.md#task-0003025) |

## Назначение файла

Общий класс листов персонажа и монстра V2. Собирает контекст для дочерних PARTS, подключает 11 объектов поведения через Object.assign и предоставляет общие действия. При загрузке также изменяет Array.prototype двумя вспомогательными методами.

## Условия использования

В registerSheets регистрируются WitcherCharacterSheet и WitcherMonsterSheet, которые импортируют и расширяют этот класс. Собственных PARTS/TABS и прямой регистрации здесь нет. WitcherLootSheet и WitcherMysterySheet имеют отдельные ветви наследования от ActorSheetV2. Наличие файла WitcherActorSheetV1 не означает его использование. Требуются Foundry 14.367.0, CONFIG.WITCHER, jQuery и подготовленные Item/ActiveEffect.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherActorSheet | default class:33 | HandlebarsApplicationMixin(ActorSheetV2) | Экспорт для двух наследников | Экземпляр привязан к Actor; методы контекста и событий |
| statMap, skillMap | Поля:34–35 | Ссылки на CONFIG.WITCHER | Публичные поля экземпляра | Не копии справочника; используются примесями |
| uniqueTypes | Массив:37 | profession/race/homeland | Потребитель itemMixin._isUniqueItem | Наследник может переопределить |
| configuration | Поле:40 | undefined по умолчанию | _renderConfigureDialog | MonsterSheet создаёт конфигурацию; общий класс не создаёт окно |
| DEFAULT_OPTIONS | static:43–55 | Resizable, width=800, classes witcher/sheet/actor, submitOnChange=true, closeOnSubmit=false | Слияние опций внешним ApplicationV2 | Дочерний CharacterSheet задаёт width=900 |
| Array.prototype.sum / cost | Присваивания:18–32 | Сумма поля; общая стоимость | Все массивы текущего JS realm | Побочный эффект импорта, enumerable/writable/configurable |
| 11 Object.assign | 310–323 | stat → skill → customSkill → item → activeEffect → deathsave → criticalWound → note → heal → currency → contextMenu | Копирование членов в prototype | Коллизий имён между этими объектами при сверке не найдено; это не наследование отдельных классов |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext(options) | Actor с CommonActorData, документами и itemTypes.criticalWound | Promise<context> | await super; настройки и CONFIG; system/schema/items; сумма HP; шесть последовательных _prepare*; категории effects; isGM | context.system — живая модель; ошибки обогащения отвергают Promise; Item/system не сохраняются |
| _renderConfigureDialog() | configuration может отсутствовать | Promise<void> | configuration?.render(true) | Не ожидает render; отсутствие конфигурации безопасно |
| _prepareCustomSkills(context) | Все actor.items; CONFIG.WITCHER.statMap | customSkills по девяти основным name | type===skill; attribute должен точно совпасть с именем группы | Сохраняет исходный порядок actor.items; неизвестные/пустые attribute не отображаются через группы |
| _prepareGeneralInformation(context) | context.actor | oldNotes и notes | getList('note'); actor.system.notes | notes ссылается на массив модели; старый Item note не преобразуется |
| _prepareSpells(context) | getList | spells, noviceSpells, journeymanSpells, masterSpells, hexes, rituals, magicalgift | Три разрешённых class и три level; MagicalGift независимо от level | getList исключает isStored, сортирует sort; неизвестные class/level остаются лишь в общем spells |
| _prepareItems(context) | Отфильтрованные и сортированные context.items | enhancements/runeItems/glyphItems/containers, totalWeight/totalCost, criticalWounds | Не applied улучшения; вес Actor, cost массива; Promise.all enrichedText всех itemTypes.criticalWound | cost не включает stored и валюту; criticalWounds создаётся после успешного обогащения |
| _prepareWeapons(context) | weapon либо enhancement c type='weapon' и applied==false | context.weapons | Если enhancements>0 и не равно enhancementItemIds.length, создаёт массив длины по циклу i<enhancements, сохраняя прежние элементы или {} | Меняет system.enhancementItems настоящего Item; может обрезать реальные улучшения; не меняет source/ID и не вызывает update |
| _prepareArmor(context) | armor либо enhancement c type='armor' и applied==false | context.armors | Только фильтрация | V2 не дополняет слоты; freeEnhancements готовится в ArmorData |
| _onRender(context,options) | this.element — DOM | Promise<void> | await super._onRender; activateListeners(this.element) | Полный DOM и частичный повторный browser render не исполнялись |
| activateListeners(html) | DOM; методы всех 11 примесей | Привязки событий | Локальный jquery=$(html), шесть click и focusin; 11 вызовов listener/contextMenu с DOM | Нет собственного проверки isEditable; базовый Foundry отключает форму, сохранение проверяет Document; Обход прав доступа не проверялся |
| _onInitRoll(event) | Actor | Promise<void> | rollInitiative({createCombatants:true,rerollInitiative:true}) | Не ожидает/возвращает результат Actor; event не используется |
| _onCritRoll(event) | Roll и ChatMessage API | Promise<void> | await new Roll('1d10x10').evaluate({async:true}); new ChatMessageData(actor); toMessage | Ожидает оценку, не публикацию; без RollConfig/extendedRoll; данные переданы реальным ChatMessageData |
| _onRecoverSta(event) | sta.value/max и rec.value | Promise после render; два async callback | Модальное окно, Recovery Action: value+rec.value; Full Recovery: max; если value>=max, уведомление и return | Render не означает выбор/закрытие; update не ожидается; добавление не ограничено max |
| _onVerbalCombat() | actor.verbalCombat из actor/mixins/verbalCombatMixin | Promise<void> | Вызывает Actor.verbalCombat без аргументов | Не ожидает вложенный prompt/бросок; отмена в реальном потребителе использует rejectClose=true |
| _onLifeEventDisplay(event) | closest('.life-events-card').dataset.event, lifeEvents как массив с key | update path system.general.lifeEvents.<key>.isOpened | preventDefault; find(event.key===dataset.event); инверсия isOpened | Без найденной записи TypeError; источник формы массива — CharacterSheet; update не ожидается |
| Array.prototype.sum(prop) | Массив объектов с system; имя поля | Числовая сумма Number(system[prop]??0) | Устанавливается при вычислении модуля прямым присваиванием | Глобальное enumerable расширение; NaN от нечислового значения, отсутствие system вызывает TypeError |
| Array.prototype.cost() | Массив объектов с system.quantity/cost | Math.ceil суммы произведений Number | Количество/цена nullish→0; округляется итог, не каждая строка | Глобальное enumerable расширение; dice-строка даёт NaN |

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
| currencyConverterMixin | [module/actor/sheets/mixins/currencyConverterMixin.js](../../../../../../../module/actor/sheets/mixins/currencyConverterMixin.js) | Именованный import; Object.assign prototype | currencyConverterListeners: .open-currency-converter → actor.handleCurrencyConverter | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| itemContextMenu | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Именованный import; Object.assign prototype | itemContextMenu: ContextMenu на .item, шесть пунктов через собственные фабрики | Определение export и точки listener просмотрены; тела внешних примесей не засчитываются полностью |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | default import; constructor | _onCritRoll: speaker от actor, type=base, flavor undefined, пустые system и flags.TheWitcherTRPG | constructor(actor,flavor,type='base',system={},flags) |
| statMap, skillMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | CONFIG.WITCHER, ссылка | Поля экземпляра; customSkills группируются по name записей origin='stats' | В statMap 9 основных характеристик; derivedStats в группы не входят |
| useOptionalAdrenaline, displayRollsDetails, useOptionalVerbalCombat, displayRep | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | game.settings.get | Четыре настройки контекста; displayRollDetails изменяет глобальную формулу инициативы | Имена регистрации сопоставлены со строками чтения |
| getList, getTotalWeight, update, verbalCombat | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js); [module/actor/mixins/verbalCombatMixin.js](../../../../../../../module/actor/mixins/verbalCombatMixin.js) | Actor; метод примеси и внешний Document.update | Сортированные списки без stored, общий вес всех calcWeight и валюты; общие действия | getList/getTotalWeight исполнены; verbalCombat ожидает prompt с rejectClose=true |
| system, notes, combatEffects.temporaryEffects.temporaryHp | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/temporaryEffectsData.js](../../../../../../../module/data/actor/templates/common/temporaryEffectsData.js) | Поля DataModel | Подготовка списка заметок и суммы временного HP; сумма в схему не входит | Настоящие CharacterData/MonsterData и source после подготовки проверены |
| CharacterData, MonsterData | [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js); [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Типы Actor через schema | Оба зарегистрированных наследника общего листа используют CommonActorData | Пустые реальные модели проходят _prepareContext |
| enhancements, enhancementItemIds, enhancementItems | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js); [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js); [module/data/item/enhancementData.js](../../../../../../../module/data/item/enhancementData.js); [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | Поля и getter подготовленной модели | Фильтры weapon/armor/enhancement; список слотов оружия меняет enhancementsEffects | prepareDerivedData разрешает ID; getter читает текущий enhancementItems |
| quantity, cost, weight, isStored, isHidden, isCarried | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Поля общей модели Item | Array.cost; основной фильтр проверяет только isStored; расчёт веса — отдельный метод модели | Number(quantity), Number(cost); не оценка dice-формул |
| SkillItemData.attribute | [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js) | Item type=skill | Группы customSkills из всей actor.items без собственной сортировки; пустой/неизвестный attribute теряется для этих групп | 8 полей модели; isStored/isHidden в её схеме отсутствуют |
| SpellData.class/level | [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js); [module/data/item/hexData.js](../../../../../../../module/data/item/hexData.js); [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js) | Типы Item и фильтры | novice/journeyman/master × Spells/Invocations/Witcher, magicalgift отдельно; hexes/rituals через getList | Группа 06 с настоящей SpellData и 20 сочетаниями |
| CriticalWoundData.enrichedText; createEnrichedText | [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js); [module/data/dataUtils.js](../../../../../../../module/data/dataUtils.js) | Модель → асинхронное обогащение | V2 словарь criticalWounds[uuid] содержит description={value,enriched,systemField} | _prepareItems ждёт Promise.all; отказы доходят до вызывающего |
| isAppliedTemporaryItemImprovement, isTemporaryItemImprovement, isDisabled | [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Геттеры ActiveEffect | Первый читает system.isTransferred; категории также используют isTemporary | Getter-определения просмотрены; isSuppressed и isDisabled различаются |
| sta.value/max, rec.value | [module/data/actor/templates/common/stats/statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js) | Поля Character/Monster через DerivedStats | _onRecoverSta: добавление REC либо запись max | value NumberField без динамического max; source модели принимает 12 при max=10 |
| HandlebarsApplicationMixin, ActorSheetV2, Actor, Roll, DialogV2, $, CONFIG.Combat | Foundry VTT 14.367.0 и jQuery браузера | Внешний API | Наследование, базовый контекст/render/Drop; Initiative/createCombatants, Roll.toMessage, диалог STA | /opt/foundryvtt/client/applications/sheets/actor-sheet.mjs:131,200,212; client/documents/actor.mjs:305,492; методы API/DOM частично подменены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | WitcherActorSheet; sum | default import и extends; await super._prepareContext, super.activateListeners; sum у веществ/компонентов | PARTS задаёт шаблоны; _prepareCharacterData добавляет race/profession enrichedText |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | WitcherActorSheet | default import/extends; общий контекст + profession/loot/lore; configuration | Зарегистрирован для monster; header без кнопки recover-sta |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | Наследники V2 | Косвенная регистрация Character и Monster; общий класс сам не зарегистрирован | Loot/Mystery наследуют ActorSheetV2 напрямую; V1 не импортирован |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Array.prototype.sum | getOwnedComponentCount: findNeededComponent(...).sum('quantity') | Зависимость через побочный эффект загрузки ActorSheet; прямого импорта нет |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | Array.prototype.cost | _prepareItems вызывает context.items.cost() | Определения sum/cost в V1 нет; нужен ранее вычисленный V2-модуль |
| [templates/partials/character-header.hbs](../../../../../../../templates/partials/character-header.hbs) | Общие действия, useVerbalCombat | init-roll, crit-roll, recover-sta, verbal-button | click selectors:47–53 |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../../templates/sheets/actor/partials/monster/header.hbs) | Общие действия, configuration | configure-actor, init-roll, crit-roll, verbal-button | Header текущего MonsterSheet |
| [templates/partials/character/tab-background.hbs](../../../../../../../templates/partials/character/tab-background.hbs) | notes и lifeEvents; _onLifeEventDisplay | life-events-card data-event из key и кнопки раскрытия | Рендер массива делает дочерний CharacterSheet |
| [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs) | customSkills | lookup по ключу system.skills; общий список и вкладки | SPD/LUCK не входят в цикл групп skills; полный разбор SkillItem/интерфейса завершён в TASK-0003.029 |
| [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | effects, criticalWounds | Категории и lookup словаря по critWound.uuid с последующим enriched | Список самих травм идёт из document.items.documentsByType, не из словаря |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | weapons, enhancementItems | Показывает улучшения и пустые слоты {} | Шаблон потребляет именно массив модели после листа |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | armors | Подготовленные enhancementItems и freeEnhancements | Источники массива/свободных слотов различаются с оружием |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Подготовка создаёт новый context и массивы filter/sort, но элементы остаются настоящими Item. context.system и context.notes — ссылки; сортировка context.items не переставляет actor.items. temporaryHpSum записывается в подготовленную модель и отсутствует в её source. CONFIG.Combat.initiative.formula изменяется глобально при каждом контексте, без game.settings.set. _prepareWeapons меняет подготовленное enhancementItems; UUID/ID и source сохраняются. Травмы обогащаются все из itemTypes.criticalWound; словарь нужен описаниям, а не применению эффектов. Категории складывают Actor.allApplicableEffects с переносимыми временными улучшениями на не помещённых в контейнер Item без дедупликации. allApplicableEffects сам учитывает transfer, но не isStored и не подавление; классификация по isDisabled не равна числовому применению effects. Общий лист не выбирает race/profession и не делает их enrichedText — это дочерний CharacterSheet. Стоимость считается, однако прямой HBS-потребитель totalCost найден только в отдельном LootSheet, который этот контекст не наследует; отсутствие показателя у loot не объявлено выполненным разбором LootSheet.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Класс, поля, опции и композиция | Группа 01, все Object.assign и export | 11 примесей V2, 10 V1; дубли имён не найдены | Методы внешних примесей вне запланированных границ не разобраны полностью |
| Пустые Actor, фильтры, источники, повтор | Группы 02–07,09,17; реальные модели | Character/Monster и оба API проходят; sort/storage, вес/стоимость, 20 сочетаний class/level, customSkills, сумма HP проверены | Actor/базовые листы представлены фасадами |
| Живые улучшения и source | Группа 08; реальные WeaponData и enhancementsEffects | После _prepareWeapons 2 ID и 2 воздействия превращаются в 1 подготовленный элемент и 1 воздействие; source неизменен | Атака/запись/переподготовка мира не запускались |
| Травмы и категории эффектов | Группы 10–11; реальная CriticalWoundData, createEnrichedText, core generator | value/enriched/systemField доступны; ошибка обогащения отклоняет Promise; e включён дважды при transfer+isTransferred | TextEditor и ActiveEffect-документы подменены; геттеры изучены отдельно |
| Действия и DOM-входы | Группы 12–16 | STA 9+3→12 при max=10; return при >=max; pending операции; семь общих привязок, 11 входов примесей; skillListener заменяет jQuery | Нет browser/Document.update/Roll/диалогов мира; slot/context применялись в памяти |
| Регистрация и потребители; общая сверка | rg по module/templates, определения методов и PARTS; .021–.025 | 37 новых файлов не пересекаются с прежними 168; границы V1/V2/Item/Actor различены | Структурная сверка всех связей не является выполнением всех игровых процессов |

## Непроверенные участки и открытые вопросы

Не запускались Foundry-мир, настоящие листы в браузере, частичный рендер и повторные привязки на сохранённом DOM, доступ разных пользователей, запись в БД, полный бой и реальные dice/ChatMessage. Изолированно выполнялись неизменённые тела двух классов с заменёнными import/base/UI границами; настоящие модели, генератор Foundry и skillMixin импортированы/извлечены отдельно. Ошибки сборки первоначального фасада исправлены в памяти, исходники не изменялись. Полный Character теперь описан в TASK-0003.031; полные Monster/Loot и ещё не описанные примеси остаются вне покрытия. SkillItemData и две skill-примеси описаны полностью в .029, ChatMessageData — в .028. Порядок и содержимое race/profession enrichment сверены до определения в дочернем классе; issue-00109 не исправлена.

## Связанные проблемы

[issue-00024](../../../../../../issues/potential/issue-00024.md), [issue-00054](../../../../../../issues/potential/issue-00054.md), [issue-00084](../../../../../../issues/potential/issue-00084.md), [issue-00109](../../../../../../issues/potential/issue-00109.md), [issue-00127](../../../../../../issues/potential/issue-00127.md), [issue-00164](../../../../../../issues/potential/issue-00164.md), [issue-00165](../../../../../../issues/potential/issue-00165.md), [issue-00166](../../../../../../issues/potential/issue-00166.md), [issue-00167](../../../../../../issues/potential/issue-00167.md). Новые наблюдения: STA, дубли эффектов, обрезка улучшений, глобальный jQuery. Прежние карточки отделяют изменение lifeEvents, повтор травм в HBS, сбор воздействий брони, enrichedText расы/профессии и ожидание лечения. Категоризация листа не устраняет ни один из этих разрывов.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a2670a0a10c62b28d836b1a57577c4836f14cf20`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003025) |

## Уточнение TASK-0003.026

2026-09-11, `rusbar-main`, `45a63062a2bd55939fef430609fc5dddc350b0e9`. Полностью разобраны подключаемые itemMixin и itemContextMenu: 19 и 15 методов, 23 привязки и шесть menu entries. ContextMenu jQuery=false различает onClick(event,target) и callback(target,event); removeEnhancement/giftItem/dismantleItem используют несовместимые legacy callback (issue-00168). Delete со старой сигнатурой корректен. Сам общий V2 лишь подключает эти объекты; числовые действия принадлежат Item/Actor.

Определения: [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) и [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003026). Полный разбор новых соседних файлов вне порции не засчитывается.

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Полностью описаны 12 HBS инвентаря: общий контекст поставляет items/weapons/armors/runeItems/glyphItems/containers и totalWeight; totalCost в текущей вкладке не выводится. getList/items исключают stored, но сохраняют hidden. В полной матрице 45 Item распределены по разделам Character, девять веществ видны только при открытых pannels. Одинаковые таблицы оружия/брони потребляются Monster; listener ремонта находится только в Character.

Связанные шаблоны: [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs); [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs). [Проверки и ограничения](../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.

## Уточнение TASK-0003.028

2026-09-11, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`: _onCritRoll:253–256 использует ChatMessageData(this.actor) и непосредственно Roll('1d10x10').toMessage. Новый полный разбор ChatMessageData подтвердил: flavor здесь undefined, но append/extendedRoll не вызываются, поэтому наблюдение undefinedsuffix из изолированного append к этому пути не переносится. Правильный объект Actor передаётся в getSpeaker; класс ChatMessageData — обычный контейнер, не схема message.system.

Полные карточки зависимости: [module/chatMessage/chatMessageData.js](../../chatMessage/chatMessageData.js.md). [Перекрёстная сверка](../../../../review-log.md#task-0003028). Это уточнение связи; исходный файл не изменён.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Полностью разобраны две skill-примеси и SkillItemData. _prepareCustomSkills возвращает сами embedded Items в девяти originstat-группах, без обёртки skill. Текущий tab-skills использует только семь system.skills-групп, custom partial читает неверный контекст и вызывает builtin handler. Старые custom-селекторы присутствуют в legacy monster-строке, но не в текущей.

Сверенные связи: [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js); [module/actor/sheets/mixins/customSkillMixin.js](../../../../../../../module/actor/sheets/mixins/customSkillMixin.js); [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js); [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs); [templates/partials/character/custom-skill-display.hbs](../../../../../../../templates/partials/character/custom-skill-display.hbs). Полные карточки новых файлов — в [указателе порции](../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. Полностью описаны statMixin/deathsaveMixin. statListener использует локальную обёртку html, skillListener по-прежнему меняет глобальную jQuery; death-minus означает reset0. Общий контекст displayRep/useAdrenaline взят из настроек; totalStats не готовится базой. Character/MonsterSheet остаются вне полного покрытия.

Сверенные источники: [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js); [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js); [templates/partials/character/tab-stats.hbs](../../../../../../../templates/partials/character/tab-stats.hbs). [Итоговая сверка третьей серии, сценарии и ограничения](../../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Полностью импортирован дочерний WitcherCharacterSheet; выполнены super._prepareContext и оба activateListeners. Дочерний контекст использует тот же system и уже отфильтрованные по isStored items. Собственные .alchemy-potion/.crafting-craft/.item-repair/.manualIpReward/.saveIpSpending/.open-rewards дополняют базовые обработчики. Группы 01–06,17–18,23.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](WitcherCharacterSheet.js.md); [templates/partials/character-header.hbs](../../../templates/partials/character-header.hbs.md); [templates/sheets/actor/partials/character/sidebar.hbs](../../../templates/sheets/actor/partials/character/sidebar.hbs.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).
