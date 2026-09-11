# module/actor/sheets/WitcherCharacterSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.031](../../../../../../tasks/task-0003.031.md), 3 файла, 711 логических строк |
| Запись перекрёстной сверки | [TASK-0003.031](../../../../review-log.md#task-0003031) |

## Назначение файла

Специализированный ActorSheetV2 для character. Собирает контекст персонажа и его вкладок, создаёт окно журналов наград, подключает шесть собственных listeners, выполняет диалоги алхимии/ремесла и передаёт действия ремонта, IP и конфигурации соседним объектам. Полностью прочитаны 481 строка, все 17 собственных методов и оба Craft-callback.

## Условия использования

registerSheets импортирует default WitcherCharacterSheet и назначает его makeDefault для character (105–108). Наследуется от WitcherActorSheet; импорт файла также импортирует базовую цепочку и её Array.prototype.sum/cost. При создании экземпляра uniqueTypes повторно задаёт profession/race/homeland, rewards создаётся как RewardsSheet({document:this.actor}). DEFAULT_OPTIONS/PARTS/TABS описывают UI; слияние настроек и жизненный цикл принадлежат Foundry. Собственного конструктора, метода сохранения формы и _onRender нет; базовый _onRender вызывает переопределённый activateListeners. В конце Object.assign добавляет alchemyMixin. DialogV2 на строке 9 захвачен, но в теле файла не используется: оба диалога изготовления используют глобальный Dialog.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherCharacterSheet | Класс, 11–479 | Специализированный лист character | default export; registerSheets | Создание, подготовка, render и обработчики |
| DialogV2 | Локальная константа, 9 | Ссылка на API | Не экспортируется | Не вызывается этим файлом |
| uniqueTypes; rewards | Поля экземпляра, 12–14 | Уникальные типы и связанное окно наград | Наследуемые операции Drop; _renderRewards | Повторяет три типа; RewardsSheet создаётся сразу |
| DEFAULT_OPTIONS | static, 17–26 | width=900 и три actions | Foundry Application | openAttributeDialog/openDerivedDialog/openModifiers |
| PARTS | static, 28–69 | 10 частей: sidebar/header/tabs/stats/skills/profession/inventory/magic/background/effects | Foundry HandlebarsApplication | Девять HBS системы, tabs — core generic navigation |
| TABS | static, 71–108 | primary:7, skillTabs:9, magicTabs:6 | _prepareTabs | Начальная stats/all/all; primary labelPrefix WITCHER.Actor.tabs |
| Два Craft-callback | Анонимные async, 295–347 и 388–435 | Параметры диалога и запуск броска/изготовления | Dialog.buttons.Craft.callback | Читают flags и текущие stats/skills; используют ранее рассчитанную достаточность компонентов |
| Object.assign(..., alchemyMixin) | 481 | _prepareAlchemyComponentsList | Прототип класса | Получает девять записей веществ из соседней примеси |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| activateListeners; 110 | DOM листа | void | Вызывает super; click для .alchemy-potion/.crafting-craft/.item-repair/.manualIpReward/.saveIpSpending/.open-rewards | Соседние listeners также выполняются; skillListener меняет глобальную jQuery |
| _prepareContext; 122 | options; Actor и все базовые поля | Promise<context> | super → _prepareCharacterData → diagrams → crafting → substances → alchemy → valuables → alchemyComponentsList → lifeEvents → enrichedText → три набора tabs | context.system остаётся живой ссылкой; Object.entries заменяет lifeEvents массивом; counter подставляется через \|\| |
| _prepareCharacterData; 151 | context.actor | Promise<void> | Берёт первый getList profession/homeland/race; enrich profession/race; суммы stats/skills/profession | Результат зависит от фильтрации/сортировки getList; описания Item и фон — разные структуры |
| _prepareDiagramFormulas; 173 | Actor.getList('diagrams') | void, 13 групп в context | alchemicalItemDiagrams: alchemical либо пустой type; potion/decoction/oil; enhancement/ingredient/weapon/armor/elderfolk weapon/elderfolk armor/ammunition/bomb/trap | Неизвестный type остаётся в diagrams, но не в именованных группах; isFormulae не читается |
| _prepareCrafting; 193 | Actor.getList('component') | void | allComponents; craftingMaterials = crafting-material/component; ingotsAndMinerals = minerals; hidesAndAnimalParts = animal-parts | Рецепты и готовые вещи не смешиваются с этими тремя группами |
| _prepareAlchemy; 202 | context.items | void | alchemicalItems = valuable/alchemical-item либо alchemical с type ''/alchemical; witcherPotions = potion/decoction; oils; alchemicalTreatments = component/alchemical; mutagens = Item type mutagen | Не изменяет Item; вход уже отфильтрован базовым листом по isStored |
| _prepareSubstances; 217 | Actor.getSubstance; Array.sum | void | Пары substancesVitriol/Rebis/Aether/Quebrith/Hydragenum/Vermilion/Sol/Caelum/Fulgur и соответствующие *Count = sum('quantity') | Числа берутся из Item.system.quantity через базовую Array.sum, не из Item.quantity |
| _prepareValuables; 240 | context.items | void | valuables; clothingAndContainers; general: genera/general/пусто; foodAndDrinks/toolkits/questItems; mounts; mountAccessories | context.general — список предметов, отдельный от system.general биографии |
| _alchemyCraft; 258 | event.currentTarget.closest('.item').dataset.itemId | Promise<void> при открытии | Собирает HTML и достаточность веществ, hasDiagram/realCraft, создаёт Dialog | На настоящем WitcherItem падает в 270: populateAlchemyCraftComponentsList отсутствует; окно и callback не достигаются |
| Alchemy Craft callback; 295 | html.find(...).prop('checked'); подготовленный item | Promise (void или результат уведомления) | CRA.value + alchemy.value, +2 за рецепт, addActiveEffects('alchemy'), DC=alchemyDC; при !isAlchemicalCraft заменяет skill на crafting | Fallback сохраняет alchemy DC/имя/modifier; realCraft не await, preview await extendedRoll; свежий label undefined ломает replace; недостаточность использует associatedItem.name |
| _craftingCraft; 354 | Item diagrams и event | Promise<void> при открытии | Проверяет все craftingComponents по имени, sum(quantity); создаёт HTML, flags и Dialog | Предварительно не фильтрует компоненты по quantity>0; событие не preventDefault; неизвестный Item не проверяется |
| Crafting Craft callback; 388 | checkboxes, Actor.stats.cra/skills.cra.crafting | Promise (void или результат уведомления) | 1d10 + CRA.value + crafting.value; +2; addActiveEffects('crafting'); RollConfig threshold=craftingDC | При realCraft проверяет сохранённый bool достаточности, не await item.realCraft; preview await extendedRoll; нехватка без associatedItem даёт TypeError |
| _repairItem; 442 | Item ID | Promise<void> | await item.repair() | Дожидается соседнего метода; неизвестный Item не обработан |
| _addIpReward; 448 | Actor | Promise<void> | actor.addIpReward() | Не возвращает/не ожидает вложенную операцию; event не используется |
| _saveIpSpending; 452 | Два первых sibling input: title/value | Promise<void> | Положительный ввод умножает на -1, отрицательный оставляет строкой; logs.addIpReward(label,value) без isMagic | Баланс 10 и ввод '-3' дают строку '10-3'; Log не возвращает update |
| _renderRewards; 460 | rewards | Promise<void> | rewards?.render(true) | Не ожидает render; не создаёт окно заново |
| #openAttributeDialog; #openDerivedDialog; 464/466 | actions без аргументов | Promise<void> | Пустые тела | Публичные ссылки на private static методы хранятся в actions; потребитель вне файла не найден |
| #openModifiers; 468 | event, target.dataset.type/skillKey; this.document | Promise<void> | preventDefault; new WitcherModifiersConfiguration({document,skillKey,type}).render(true) | Лист не валидирует type/key и не ожидает render |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherActorSheet; _prepareContext/_onRender/activateListeners; Array.sum/cost | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | import, наследование, вызов | Базовый контекст, listeners, форма, суммы | Импорт 1; super в 111/123; 221–237/369 |
| RollConfig; extendedRoll | [module/scripts/rollConfig.js](../../../../../../../module/scripts/rollConfig.js); [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | named import, создание/вызов | Настройка DC/сообщений и preview | Импорты 2–3; 326/346/414/434; настоящие Roll/парсер |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../module/chatMessage/chatMessageData.js) | default import | speaker/flavor/type=base | 4, 265/361; конструктор проверен |
| alchemyMixin._prepareAlchemyComponentsList | [module/actor/sheets/mixins/alchemyMixin.js](../../../../../../../module/actor/sheets/mixins/alchemyMixin.js) | named import, Object.assign | Девять иконок/ключей/количеств | 5, 131, 481; определение прочитано, полная карточка — .034 |
| RewardsSheet | [module/actor/rewardsSheet.js](../../../../../../../module/actor/rewardsSheet.js) | default import, new | Окно, привязанное к этому Actor | 6,14,460; определение/контекст прочитаны; полная карточка — .037 |
| WitcherModifiersConfiguration | [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | default import, new | Конфигурация по type/skillKey | 7,468–477; полный класс описан в .030 |
| getList/getTotalWeight; addIpReward; calc_total_skills_profession | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js); [module/actor/mixins/rewardsMixin.js](../../../../../../../module/actor/mixins/rewardsMixin.js); [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | динамические методы Actor | Списки/суммы и выдача награды | getList:250 сортирует sort и исключает isStored; reward wrapper передаёт game.api.rewards.ip |
| getSubstance/findNeededComponent; alchemyCraftComponentsList/isAlchemicalCraft/realCraft/repair | [module/actor/mixins/craftingMixin.js](../../../../../../../module/actor/mixins/craftingMixin.js); [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js); [module/item/mixins/repairMixin.js](../../../../../../../module/item/mixins/repairMixin.js); [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | методы Actor/Item | Проверка компонентов, бросок, выдача результата, ремонт | Определения до вызовов сверены; отсутствующий populate... подтверждён |
| addActiveEffects; calc_total_stats; calc_total_skills | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js); [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js); [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | примеси Actor/листа | Строка эффекта и суммы | Имена crafting/alchemy; суммы 72/0/0 в пустом подготовленном примере |
| CharacterData.enrichedText; general.lifeEvents; logs.addIpReward | [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js); [module/data/actor/templates/character/generalData.js](../../../../../../../module/data/actor/templates/character/generalData.js); [module/data/actor/templates/character/general/lifeEventsData.js](../../../../../../../module/data/actor/templates/character/general/lifeEventsData.js); [module/data/actor/templates/character/logData.js](../../../../../../../module/data/actor/templates/character/logData.js) | чтение/изменение модели | Фон, биография и списание IP | 133–142,452–457; настоящие модели и updateSource |
| RaceData/ProfessionData.enrichedText; HomelandData.value/otherValue | [module/data/item/raceData.js](../../../../../../../module/data/item/raceData.js); [module/data/item/professionData.js](../../../../../../../module/data/item/professionData.js); [module/data/item/homelandData.js](../../../../../../../module/data/item/homelandData.js) | модель Item | Первый выбранный Item и подписи заголовка | 151–168; шаблон получает raw Item и отдельно enrichedText |
| DiagramData/ComponentData; Skill.label/value | [module/data/item/diagramData.js](../../../../../../../module/data/item/diagramData.js); [module/data/item/componentData.js](../../../../../../../module/data/item/componentData.js); [module/data/actor/templates/common/skills/craData.js](../../../../../../../module/data/actor/templates/common/skills/craData.js); [module/data/actor/templates/common/skills/skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js) | чтение полей | Режим/компоненты/DC и skillName.replace | Миграция DiagramData и Craft отличена от подготовленных значений |
| Девять PARTS системы | [templates/partials/character-header.hbs](../../../../../../../templates/partials/character-header.hbs); [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs); [templates/partials/character/tab-stats.hbs](../../../../../../../templates/partials/character/tab-stats.hbs); [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs); [templates/partials/character/tab-profession.hbs](../../../../../../../templates/partials/character/tab-profession.hbs); [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs); [templates/partials/character/tab-magic.hbs](../../../../../../../templates/partials/character/tab-magic.hbs); [templates/partials/character/tab-background.hbs](../../../../../../../templates/partials/character/tab-background.hbs); [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | пути HBS, контекст | Текущие вкладки и две панели | 28–69; PARTS — фактический выбор; не только предзагрузка |
| CONFIG.WITCHER; displayRollsDetails; Handlebars helpers | [module/setup/config.js](../../../../../../../module/setup/config.js); [module/setup/settings.js](../../../../../../../module/setup/settings.js); [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | настройки/локализация/рендер | Названия навыков, группы, детализация броска | Флаг считывается при открытии диалога; helpers/словарь сверены |
| ActorSheetV2/HandlebarsApplicationMixin; Dialog; jQuery; game.i18n | Foundry 14.367.0; jQuery и внешние API | внешний жизненный цикл | Форма, render, events, локализация | Локальные client/applications/api/application.mjs:2134–2161; helpers/localization.mjs:435; базовые Application/DOM подменены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | default WitcherCharacterSheet | makeDefault для character | import:1; регистрация:105–108 |
| [templates/partials/character-header.hbs](../../../../../../../templates/partials/character-header.hbs) | _renderRewards; унаследованные общие/death/heal actions | click в заголовке | Селекторы 47–66; собственный .open-rewards |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | контекст ресурсов; унаследованные stat actions | PARTS.sidebar и форма | Пути и условные поля сверены |
| [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs) | _saveIpSpending/_addIpReward/_renderRewards/#openModifiers | Кнопки обучения/IP и редактирования | Соседние input title/value и data-action |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | Подготовленные списки, награды и ремесленные действия | Вкладка инвентаря и вложенные строки | Контексты групп сопоставлены; ошибка маршрута формул — issue-00176 |
| [templates/partials/character/tab-background.hbs](../../../../../../../templates/partials/character/tab-background.hbs) | system.general.lifeEvents и enrichedText | Фон/события жизни | Массив/ключи и контракт базового toggle |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Записи this.actor.update непосредственно в этом классе отсутствуют: выполняются через Item, Log и примеси. Собственная подготовка меняет context и живую general.lifeEvents; сохранённый source в проверке не изменился, подготовленный toObject(false) читает ошибочные записи (issue-00024). Первый список уникального типа выбирается по getList после фильтра isStored/sort.

Оба callback строят формулу по текущим CRA.value/Skill.value и addActiveEffects; hasDiagram добавляет +2. Обычный strict успех наследуется от extendedRoll: больше DC, равенство — неуспех. Предварительная достаточность компонентов вычисляется до выбора пользователя и может устареть; realCraft проверяет запасы ещё раз. Простой бросок не списывает компоненты. RealCraft может завершить callback до записей. Закрытые ветви алхимии проверялись только с явно добавленным в fixture адаптером отсутствующего API — это не исправление системы и не работающий штатный маршрут.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Весь класс/конфигурация/контекст | Группы 01–06,17–18,23 | 10 PARTS, TABS 7/9/6; live system, фильтры/суммы и listeners; 20 событий становятся массивом | Full Application/DOM/экраны подменены; все собственные методы прочитаны |
| Изготовление | Группы 07–15,24 | Реальные Roll/парсер и realCraft; DC=10, 10 неуспешно; +2 работает; missing API/associatedItem и пустая аннотация дают ошибки | 13–15 требуют адаптера populate... только в fixture; запись Actor/Item/ChatMessage перехвачена |
| IP и ожидание операций | 16–17 | '3' даёт 7, '-3' даёт '10-3' и отказ NumberField; repair ждёт Promise, reward wrapper — нет | Сохранение в БД/гонки не проверялись |
| Шаблоны и локализация | 19–26; настоящие Handlebars, parse5, FormDataExtended, Localization | Поля/флаги/ключи сверены; core JSON expandObject и string fallback учтены | TextEditor enrichHTML и конструкторы DOM подменены |

## Непроверенные участки и открытые вопросы

Браузер, реальный Document.update, частичный render, сетевые вызовы и все игровые ветви соседних классов не запускались. Сохранённые данные миров/компедиумов не исследовались. _alchemyCraft без адаптера останавливается на issue-00037; результаты ветвей 13–15 условные, пригодные для понимания кода после входной границы. Пустые подписи свежей модели (issue-00015) отличены от повторно загруженной модели с мигрированными label. Не установлена частота состояний, приводящих к пустым аннотациям эффектов. Разметка UI не считается проверенной в браузере. 49 буквальных переводимых ключей и три префикса проверены отдельно; другие языки/внешние переводы не проверялись.

## Связанные проблемы

[issue-00015](../../../../../../issues/potential/issue-00015.md), [issue-00024](../../../../../../issues/potential/issue-00024.md), [issue-00028](../../../../../../issues/potential/issue-00028.md), [issue-00037](../../../../../../issues/potential/issue-00037.md), [issue-00038](../../../../../../issues/potential/issue-00038.md), [issue-00041](../../../../../../issues/potential/issue-00041.md), [issue-00101](../../../../../../issues/potential/issue-00101.md), [issue-00109](../../../../../../issues/potential/issue-00109.md), [issue-00167](../../../../../../issues/potential/issue-00167.md), [issue-00176](../../../../../../issues/potential/issue-00176.md), [issue-00200](../../../../../../issues/potential/issue-00200.md), [issue-00201](../../../../../../issues/potential/issue-00201.md), [issue-00202](../../../../../../issues/potential/issue-00202.md), [issue-00204](../../../../../../issues/potential/issue-00204.md). Существующие наблюдения сверены по указанным входам. Новые проблемы имеют статус potential; корректировка механики и исправления не выполнялись.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003031) |

## Уточнение TASK-0003.033

2026-09-11, `12055fee62f01c6de49967044aedef9d7cfe0632`. Полный tab-background подтверждён как PARTS.background. Группы 09–13 прошли через настоящий дочерний и базовый контекст: Item-родина заменяет редакторы, raw/enriched background передаются правильно; note Items и массив независимы. Повторная подготовка сохраняет UI-ключи 10/20, но prepared-модель по схеме остаётся нарушенной (issue-00024). Программный counter=21 создаёт пустую карточку (issue-00213).

Связи: [templates/partials/character/tab-background.hbs](../../../templates/partials/character/tab-background.hbs.md); [module/actor/sheets/mixins/noteMixin.js](mixins/noteMixin.js.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003033).
