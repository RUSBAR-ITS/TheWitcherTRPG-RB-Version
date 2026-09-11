# module/actor/sheets/WitcherMonsterSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../review-log.md#task-0003032) |

## Назначение файла

Текущий специализированный лист монстра V2: выбирает части интерфейса и вкладки, дополняет базовый контекст профессией/добычей/знаниями, открывает конфигурации и экспортирует копию Actor в loot. Все 224 строки, шесть собственных методов и два вложенных callback прочитаны.

## Условия использования

registerSheets импортирует default WitcherMonsterSheet и регистрирует makeDefault для monster (109–112). Наследуется от WitcherActorSheet, отдельного конструктора/activateListeners/_onRender/сохранения формы не имеет. Базовые события и форма наследуются; configuration создаётся на экземпляр. Глобальный DialogV2 захвачен при импорте. Старый monster-sheet.hbs не выбран PARTS и не найден как template общего V1.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherMonsterSheet | export default class: 7 | ActorSheet для monster | registerSheets | Наследует базовые примеси и контекст |
| DEFAULT_OPTIONS | static: 9 | Размер 900×800, классы witcher/sheet/monster | Foundry merge | actions openModifiers/exportLoot с private static функциями |
| PARTS | static: 21 | 10 частей: sidebar/header/tabs/stats/skills/profession/inventory/details/magic/effects | Foundry | 9 HBS системы и core templates/generic/tab-navigation.hbs |
| TABS | static: 62 | primary7, skillTabs9, magicTabs6, detailTabs2 | _prepareTabs | initial stats/all/all/notes; details.notes/lore |
| configuration | поле: 109 | Экземпляр WitcherMonsterConfigurationSheet({document:this.actor}) | Базовый _renderConfigureDialog | Открывается через .configure-actor, повторно не создаётся при каждом клике |
| DialogV2 | const: 5 | API prompt | Захват внешнего API при загрузке | Отмена при rejectClose=true отклоняет Promise |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext; 111 | options, базовый Actor-контекст | Promise<context> | await super; _prepareCharacterData, _prepareLoot; четыре группы tabs; systemFields; merge await system.enrichedText() | system остаётся общей ссылкой; явных Actor.update нет; totalStats/totalSkills/IP не добавляются |
| _prepareCharacterData; 131 | context.actor | void | Первый getList('profession')[0] | Не обогащает профессию и не считает totalStats; getList исключает stored и сортирует |
| _prepareLoot; 136 | context.items после базового фильтра | void, context.loots | component/crafting-material/container/enhancement/valuable/animal-parts/diagrams/alchemical/mutagen | enhancement повторён в предикате; weapon/armor не входят в loots, но экспорт от этого списка не зависит |
| getOrCreateFolder; 153 | game.folders, текущая локаль | Promise<Folder\|null> | Ищет по имени WITCHER.Loot.Name и типу CONST.FOLDER_DOCUMENT_TYPES[0]; иначе Folder.create с sorting='a', content=[], parent=null | Современный первый тип — ActiveEffect; возврат поддерживает Folder и [Folder]; отказ create не перехвачен |
| #exportLoot; 169 | this=лист, результат prompt | Promise<void> | Prompt multiple; await папки и Actor.create({...actor.toObject(),type:'loot',name:имя+'--'+Loot.Name,folder:folder?.id}); async forEach Item; await render | Нет локального фильтра Items, удаления оригинала или проверки множителя; внешний Promise не ждёт forEach |
| prompt.ok.callback; 177 | event/button/dialog | строка input.value | button.form.elements.multiple.value | Не valueAsNumber, без проверки min/целого; rejectClose обрабатывается ядром |
| export Item callback; 190 | скопированный Item, multiplier | Promise<void>, не собран внешним методом | Для string с 'd' multiplier раз Roll.evaluate, sum ceil(total); иначе Number(quantity)*multiplier. await checkIfItemHasRollTable; при falsy item.update | Условия циклов и умножения по-разному ведут себя для отрицательных/дробных значений; update не await; неизвестная формула может отклонить несобранный Promise |
| #openModifiers; 213 | event,target.dataset.type/skillKey | Promise<void> | preventDefault, new WitcherModifiersConfiguration({document:this.document,skillKey,type})?.render(true) | Валидация типа/ключа и ожидание render отсутствуют; механизм уже описан .030 |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherMonsterConfigurationSheet | [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | default import/создание | configuration: 109 | Определение класса и общий _renderConfigureDialog сверены |
| WitcherActorSheet | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | default import/наследование | super._prepareContext и унаследованные события | Полный базовый контекст выполнен |
| WitcherModifiersConfiguration | [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | default import/создание | #openModifiers | Публичный action указывает private static метод |
| getList, toObject; calculateStats/calculateDerivedStats | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Actor и соседний расчёт | Профессия, ресурсы; сериализация для экспорта | getList: 250; реальные числовые методы, payload toObject контролируемый |
| MonsterData.enrichedText; поля Monster/CommonActor | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js); [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/dataUtils.js](../../../../../../../module/data/dataUtils.js) | модель/чтение | systemFields/enrichedText.lore; Item/notes/health | 3 createEnrichedText возвращают raw value отдельно от enriched |
| checkIfItemHasRollTable | [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | вызов Item | Экспорт: 203 | Нет таблицы→false, один pack→генерация и удаление; настоящий метод выполнен отдельно с API-фасадами |
| LootData; WitcherLootSheet | [module/data/actor/lootData.js](../../../../../../../module/data/actor/lootData.js); [module/actor/sheets/WitcherLootSheet.js](../../../../../../../module/actor/sheets/WitcherLootSheet.js) | контракт результата | Actor type loot и newLoot.sheet.render | Полный Loot-лист остаётся .035; экспорт копирует все Items, а не context.loots |
| 9 системных PARTS | [templates/sheets/actor/partials/monster/header.hbs](../../../../../../../templates/sheets/actor/partials/monster/header.hbs); [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs); [templates/partials/character/tab-stats.hbs](../../../../../../../templates/partials/character/tab-stats.hbs); [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs); [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs); [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs); [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs); [templates/partials/character/tab-magic.hbs](../../../../../../../templates/partials/character/tab-magic.hbs); [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | HBS пути/контекст | PARTS: 21–59 | Сверены явные пути и потребители; чужие вкладки читаются в пределах контракта |
| stat/skill/death/note/item listeners | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js); [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js); [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js); [module/actor/sheets/mixins/noteMixin.js](../../../../../../../module/actor/sheets/mixins/noteMixin.js); [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | унаследованные действия | Общий activateListeners: 217–248 | item-repair/saveIpSpending отсутствуют; issue-00177/00030 |
| Настройки, локализация | [module/setup/config.js](../../../../../../../module/setup/config.js); [module/setup/settings.js](../../../../../../../module/setup/settings.js); [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | глобальные данные | Подписи tabs/prompt, Loot.Name; флаги базового контекста | 67 полных ключей порции, 2 префикса, en/ru после expandObject |
| DialogV2.prompt; Folder.create; Actor.create; Roll; HandlebarsApplication/ActorSheetV2 | Foundry 14.367.0: client/applications/api/dialog.mjs, application.mjs, common/constants.mjs: 542, common/documents/actor.mjs: 112 | внешний API | Диалог, документы, вкладки, кубики | Настоящая константа/Roll; создание и render подменены. canUserCreate ядра проверяет ACTOR_CREATE; фактические права клиента не тестировались |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | default class | makeDefault monster | import: 2, регистрация 109–112 |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../../templates/sheets/actor/partials/monster/header.hbs) | exportLoot и configuration | data-action exportLoot; .configure-actor через базовый listener | 30/6 |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | ресурсный контекст | PARTS.sidebar | Поля и inherited editImage |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | tabs.details/detailTabs и lore | PARTS.details | Сборка четырёх partial |
| [templates/partials/character/tab-stats.hbs](../../../../../../../templates/partials/character/tab-stats.hbs) | контекст stats/openModifiers | PARTS.stats | totalStats не подготовлен |
| [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs) | skillTabs/openModifiers | PARTS.skills | Видимость/IP отдельно от флагов конфигурации |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | loots | PARTS.inventory | Таблица добычи, ремонт без listener |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | configuration и activateListeners | Унаследованный render | Динамическое this на экземпляре Monster |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Контекст обновляется в памяти, наследует все побочные действия базовой подготовки. _prepareLoot не удаляет/не переносит Item. Экспорт создаёт новый Actor из полной сериализации: в контролируемом payload сохраняются items/effects/ownership/flags/prototypeToken и исходный _id; создающая подсистема Foundry может нормализовать их, поэтому это не утверждение о фактически сохранённом ID/правах. Исходный Actor не обновляется. Количества изменяются только у копии; валюту код не умножает. Диалог отмены не создаёт папку/Actor. Если папка/Actor создаются, последующая ошибка не откатывает уже сделанную работу. Обработка таблиц может создавать/увеличивать Item и удалять генератор. Сопоставление папки зависит от текущего перевода Loot.Name.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Конфигурация/контекст | Группы 01–05, 14, 24 | 7/9/6/2 вкладки; профессия по sort; 9 типов loots; отсутствуют totalStats и IP handlers | Application/DOM фасады; модели настоящие |
| Экспорт | 15–21 | ActiveEffect-папка, копирование всех Items, отрицательные количества, несобранные Promise, отказ prompt без записи | Actor/Folder/create/update/render подменены |
| Roll и таблицы | 18, 22 | Два настоящих d6=2+3 дают 5; checkIfItemHasRollTable false либо генерация двух результатов | Контролируемые результаты и перехват записи/чата |
| Шаблоны и ключи | 06–13, 23–25 | Новые/старые маршруты различены, fields и helpers сверены | Нет браузера/настоящей валидации диалога |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Мир, браузер, HTTP-доступ, Document.update и работа нескольких клиентов не запускались. Настоящие модели, Handlebars, core helpers и вычисления использовались с фасадами Application/DOM и перехватом записи; подробные границы — в журнале .032. CSS и ресурсы проверены только как зависимости, соседние файлы вне порции не засчитываются в покрытие.

## Связанные проблемы

[issue-00004](../../../../../../issues/potential/issue-00004.md), [issue-00013](../../../../../../issues/potential/issue-00013.md), [issue-00018](../../../../../../issues/potential/issue-00018.md), [issue-00030](../../../../../../issues/potential/issue-00030.md), [issue-00032](../../../../../../issues/potential/issue-00032.md), [issue-00039](../../../../../../issues/potential/issue-00039.md), [issue-00040](../../../../../../issues/potential/issue-00040.md), [issue-00167](../../../../../../issues/potential/issue-00167.md), [issue-00177](../../../../../../issues/potential/issue-00177.md), [issue-00180](../../../../../../issues/potential/issue-00180.md), [issue-00192](../../../../../../issues/potential/issue-00192.md), [issue-00199](../../../../../../issues/potential/issue-00199.md), [issue-00203](../../../../../../issues/potential/issue-00203.md), [issue-00205](../../../../../../issues/potential/issue-00205.md), [issue-00206](../../../../../../issues/potential/issue-00206.md), [issue-00207](../../../../../../issues/potential/issue-00207.md), [issue-00208](../../../../../../issues/potential/issue-00208.md), [issue-00209](../../../../../../issues/potential/issue-00209.md). Прежние наблюдения дополнены по фактическим маршрутам. Новые остаются potential; игровые правила и код не изменялись.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003032) |

## Уточнение TASK-0003.033

2026-09-11, `12055fee62f01c6de49967044aedef9d7cfe0632`. Общая noteMixin получила полный разбор .033; механизм массива и Item-note независим. Вход монстра через описанный monster-notes совпадает с персонажным по .delete-note/@index и .add-item/note. Новый полный рендер монстра здесь не выполнялся; выводы .032 сохранены.

Связи: [module/actor/sheets/mixins/noteMixin.js](mixins/noteMixin.js.md); [module/data/item/noteData.js](../../data/item/noteData.js.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003033).

## Дополнительная сверка TASK-0003.035

2026-09-11, `rusbar-main`, `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; исходники не менялись.

Сверен конечный consumer exportLoot: Actor.create(type:'loot') выбирает WitcherLootSheet, который не наследует WitcherActorSheet и собирает свои массивы. Все исходные Items копируются в payload экспортируемого Actor (.032), но строками становятся только поддержанные категории. В частности mutagen не выводится из-за mutagens (новый issue218). Issues206 (тип Folder),207 (async forEach/обновления) и208 (multiplier) не исправлены и не воспроизводились заново; создание/запись реального Actor не доказаны тестом новой таблицы. Покупка сама не вызывает checkIfItemHasRollTable.

Полные карточки порции: [module/actor/sheets/WitcherLootSheet.js](WitcherLootSheet.js.md), [templates/sheets/actor/loot-sheet.hbs](../../../templates/sheets/actor/loot-sheet.hbs.md), [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../templates/sheets/actor/partials/loot/loot-item-display.hbs.md), [module/data/item/mountData.js](../../data/item/mountData.js.md), [module/item/sheets/WitcherMountSheet.js](../../item/sheets/WitcherMountSheet.js.md), [templates/sheets/item/mount-sheet.hbs](../../../templates/sheets/item/mount-sheet.hbs.md).

[Проверки, общая сверка 31 файла с прежними 247 и ограничения](../../../../review-log.md#task-0003035). Связанный файл повторно в покрытии не учитывается; исправления не выполнялись.

## Дополнительная сверка TASK-0003.036

2026-09-11, `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; исходники не менялись.

Monster наследует currencyConverterListeners базового V2, но PARTS.inventory45 указывает на свой HBS без .open-currency-converter. Прямой Actor.openCurrencyConverter совместим с MonsterData (группа05); стандартная кнопка монстра из этого не следует. Экспорт loot и его курсы/покупка остаются отдельными процессами.

Карточки процесса: [module/actor/mixins/currencyConverterMixin.js](../mixins/currencyConverterMixin.js.md), [module/actor/sheets/mixins/currencyConverterMixin.js](mixins/currencyConverterMixin.js.md), [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs.md), [templates/chat/currency-conversion.hbs](../../../templates/chat/currency-conversion.hbs.md).

[Проверки и перекрёстная сверка](../../../../review-log.md#task-0003036). Связанный файл повторно в покрытии не учитывается; правок системы нет.

## Дополнительная сверка TASK-0003.037

2026-09-11, `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; исходники не менялись.

Полный маршрут .037 подтвердил: экземпляр RewardsSheet и _renderRewards создаёт CharacterSheet. MonsterSheet наследует общий tab-skills с IP-разделом, но не его обработчики наград; прежняя issue30 сохраняется. Независимый API Rewards может выбрать player-owned monster и упасть на logs (233), даже без клика по этой вкладке.

[module/actor/mixins/rewardsMixin.js](../mixins/rewardsMixin.js.md), [module/actor/rewardsSheet.js](../rewardsSheet.js.md), [module/app/reward/reward.js](../../app/reward/reward.js.md), [templates/chat/rewards.hbs](../../../templates/chat/rewards.hbs.md).

[Перекрёстная сверка и ограничения](../../../../review-log.md#task-0003037). Связанные файлы повторно в покрытие не добавлялись; исходники и статусы issues не менялись.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

PARTS.profession41 → отдельный HBS50 строк, только definingSkill/notes. _prepareCharacterData133 выбирает profession, не считает ветви/не готовит enriched. Общий listener запускает ту же professionMixin на Actor; отсутствие ветвей в UI не удаляет их из Item/поиска.

[module/actor/mixins/professionMixin.js](../mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.

## Дополнительная сверка TASK-0003.039

2026-09-11, `c598d74e34f4be51535de78b38f0601c286c5407`; исходники не менялись.

PARTS.magic использует общий character/tab-magic.hbs с теми же шестью magicTabs. Старый monster-spell-tab присутствует только в монолитном monster-sheet.hbs/предзагрузке. Группа 04: текущая вкладка показывает Item в all и специальной группе. Поле magic.magicImprovementPoints в общей вкладке не имеет схемы MonsterData; уточнена issue-00192, браузерная запись не проверялась.

[templates/partials/character/tab-magic.hbs](../../../../../../../templates/partials/character/tab-magic.hbs) — [карточка](../../../templates/partials/character/tab-magic.hbs.md); [templates/partials/monster/monster-spell-tab.hbs](../../../../../../../templates/partials/monster/monster-spell-tab.hbs) — [карточка](../../../templates/partials/monster/monster-spell-tab.hbs.md).

[Сценарии, методика и пределы проверки](../../../../review-log.md#task-0003039). Соседние определения проверены в пределах связи; это не расширяет состав шести полностью разобранных файлов.
