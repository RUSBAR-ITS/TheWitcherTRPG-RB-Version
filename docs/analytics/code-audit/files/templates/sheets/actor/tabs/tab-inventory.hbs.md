# templates/sheets/actor/tabs/tab-inventory.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.027](../../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../../review-log.md#task-0003027) |

## Назначение файла

Основная вкладка инвентаря персонажа: отображает переносимый вес/предел, семь валют и категории предметов через девять различных partial. Не рассчитывает вес/стоимость и не хранит список предметов.

## Условия использования

WitcherCharacterSheet.PARTS.inventory передаёт контекст общего V2 и специализированные списки. Корневой section использует tabs.inventory.cssClass, data-group=primary и data-tab=inventory. Оружие/броня присутствуют даже при пустых массивах; остальные группы — по if массива. Панели веществ отдельно управляются pannels во вложенном partial.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section/carry:1–8 | Блок HBS | Вкладка и индикатор | Рендер через потребителей | totalWeight, system.derivedStats.enc.value; gte добавляет overweight при равенстве и превышении |
| currency:10–59 | Блок HBS | Семь полей | Рендер через потребителей | bizant, ducat, lintar, floren, crown, oren, falsecoin; name=system.currency.*, number/data-dtype=Number |
| weapon/armor:61–67 | Блок HBS | Два безусловных partial | Рендер через потребителей | weapons: damage/reliability/quantity; armors: reliability без hasQuantity |
| valuables:69–112 | Блок HBS | Восемь групп | Рендер через потребителей | questItems, general, foodAndDrinks, toolkits, clothingAndContainers, mounts, mountAccessories, containers; только containers получает itemType=container |
| diagrams:114–176 | Блок HBS | 13 групп рецептов | Рендер через потребителей | alchemicalItemDiagrams, oilDiagrams, potionDiagrams, decoctionDiagrams, ingredientDiagrams, ammunitionDiagrams, weaponDiagrams, enhancementDiagrams, armorDiagrams, elderfolkWeaponDiagrams, elderfolkArmorDiagrams, bombDiagrams, trapDiagrams |
| alchemy/crafting:178–245 | Блок HBS | Алхимия, вещества и материалы | Рендер через потребителей | alchemicalItems, oils, witcherPotions, mutagens; alchemicalTreatments; substances partial; craftingMaterials, ingotsAndMinerals, hidesAndAnimalParts, runeItems, glyphItems |

## Основные функции и методы

Собственных JS-функций нет. if выбирает заполненные категории, partial передаёт именованные массивы и header, gte только назначает CSS-класс. hasQuantity=true задаётся категориям предметов, кроме брони. Кнопки верхних групп создают valuable/diagrams/alchemical/component; все подтипы рецептов используют один общий шаблон. Формы валюты обрабатываются общим submitOnChange V2.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .add-item | [itemMixin._onItemAdd](../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | dataset.itemtype/spelltype/subtype → Item.create({parent:actor}) |
| .open-rewards | [WitcherCharacterSheet._renderRewards](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | rewards?.render(true) |
| .open-currency-converter | [currencyConverterListeners](../../../../../../../../module/actor/sheets/mixins/currencyConverterMixin.js) | actor.handleCurrencyConverter; валютные поля отдельно через submit |

Поля name/data-field, буквально присутствующие в файле: `system.currency.bizant`, `system.currency.crown`, `system.currency.ducat`, `system.currency.falsecoin`, `system.currency.floren`, `system.currency.lintar`, `system.currency.oren`.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Контекст и PARTS.inventory | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Регистрация/подготовка | _prepareContext, _prepareDiagramFormulas, _prepareCrafting, _prepareSubstances, _prepareAlchemy, _prepareValuables | Входные массивы сверены до каждого фильтра; 45 представительных Item отображены при открытых девяти панелях |
| items/weapons/armors/containers/runeItems/glyphItems/totalWeight/totalCost | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Общий producer | _prepareContext, _prepareWeapons, _prepareArmor, _prepareItems | items исключает isStored, сохраняет isHidden; стоимость готовится, но здесь не отображается |
| getTotalWeight/calcCurrencyWeight/calcWeight | [module/actor/witcherActor.js](../../../../../../../../module/actor/witcherActor.js); [module/data/actor/commonActorData.js](../../../../../../../../module/data/actor/commonActorData.js); [module/data/item/commonItemData.js](../../../../../../../../module/data/item/commonItemData.js); [module/data/item/containerData.js](../../../../../../../../module/data/item/containerData.js) | Вычисление вне HBS | Панель Carry | Item: carried&&!stored; контейнер включает storedWeight, Actor добавляет 0.001 на монету и округляет вверх |
| Семь полей currency | [module/data/actor/templates/common/currencyData.js](../../../../../../../../module/data/actor/templates/common/currencyData.js) | Схема Actor | Ввод name=system.currency.* | NumberField с initial=0, без локальных min/max |
| .open-currency-converter | [module/actor/sheets/mixins/currencyConverterMixin.js](../../../../../../../../module/actor/sheets/mixins/currencyConverterMixin.js) | DOM→метод Actor | currencyConverterListeners→actor.handleCurrencyConverter | Окно конвертера целиком не исполнялось |
| .open-rewards | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | DOM→окно | _onRender→_renderRewards→rewards.render(true) | RewardsSheet остаётся вне полного разбора |
| gte | [module/setup/handlebars.js](../../../../../../../../module/setup/handlebars.js) | Системные helpers | Точные вызовы в этом HBS | registerHandelbarHelpers исполнен из исходника; расчёты отделены от UI-записи |
| if, localize | Handlebars 4.7.9 / Foundry VTT 14.367.0 | Внешний шаблонный API | Вызовы в этом HBS; core localize/concat: /opt/foundryvtt/client/applications/handlebars.mjs | Рендер настоящий; game.i18n/окружение представлены фасадом, core helper localize/concat дополнительно исполнены |
| Словари и подписи | [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) | Контекст и локализация | Точные строковые ключи localize в HBS | 114 статических ключей порции сверены с en/ru; отсутствующие и динамические ключи отражены в issue-00178 |
| Обработчики DOM | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../module/actor/sheets/mixins/itemMixin.js); [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/mixins/currencyConverterMixin.js](../../../../../../../../module/actor/sheets/mixins/currencyConverterMixin.js) | DOM→JS | Сопоставление ниже в таблице действий | Селекторы и ближайшие контейнеры проверены по реальному шаблону и определениям |
| partial substances.hbs | [templates/partials/character/substances.hbs](../../../../../../../../templates/partials/character/substances.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-alchemical.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-armors.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-components.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-diagrams.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-mounts.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-runes-glyphs.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-valuables.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| partial tab-inventory-weapons.hbs | [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| Классы списка, details, progress, изображения | [styles/tab-inventory.css](../../../../../../../../styles/tab-inventory.css) | CSS/HTML | grid заголовков/строк, stored-item и carry-bar до привязки селекторов | Полный CSS и вид браузера не проверялись; img без src не получает fallback в HBS, assets вне границ анализа |
| handleCurrencyConverter | [module/actor/mixins/currencyConverterMixin.js](../../../../../../../../module/actor/mixins/currencyConverterMixin.js) | Метод Actor | Вызван .open-currency-converter через примесь листа | Проверена точка вызова и определение; полный конвертер вне задачи |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | PARTS.inventory | Зарегистрированный V2 вызывает рендер части inventory | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Ввод валюты относится к Actor; кнопки добавления и строки таблиц — к встроенным Item. Шаблон не меняет isStored/isHidden, не фильтрует их сам. totalCost в контексте есть, но собственного итога цены нет. Carry/Max Carry — буквальные английские строки. При пустом инвентаре остаются валюты, заголовки и меню веществ; наличие девяти image-input веществ не означает девять валют.

Буквальные пути чтения в этом файле: `alchemical.hbs`, `system.currency.bizant`, `system.currency.crown`, `system.currency.ducat`, `system.currency.falsecoin`, `system.currency.floren`, `system.currency.lintar`, `system.currency.oren`, `system.derivedStats.enc.value`.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 247 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 01,10–11,14,18; реальный Handlebars/модели и обработчики | Пустой контекст: 0 строк Item и 7 валют. Полный контекст: 45 Item, каждый ровно один раз при открытых панелях; закрытые панели скрывают девять веществ. Вес 4 при hidden carried, stored исключён; 1001 монета даёт округлённый вес 2. При весе 9/10/11 и ENC10 класс overweight появляется при 10/11. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Весь файл прочитан. Проверены данные рендера и существенные границы, перечисленные выше. Не запускались браузер, серверная запись, DragDrop, реальные броски/производство/ремонт/экспорт или полноценные листы Actor. CSS проверен только до селекторов. Реальный Foundry Document и UI представлены ограниченными фасадами; фактическая регистрация проверена статически. Полные файлы Character/Monster/MountData, валюта/награды и производство остаются за дальнейшими порциями.

## Связанные проблемы

[issue-00173](../../../../../../../issues/potential/issue-00173.md), [issue-00176](../../../../../../../issues/potential/issue-00176.md), [issue-00179](../../../../../../../issues/potential/issue-00179.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003027) |

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. PARTS.inventory Character напрямую подключает вкладку. Полный _prepareContext готовит все списки diagrams/crafting/alchemy/substances/valuables из отфильтрованных items. _craftingCraft и _alchemyCraft описаны полностью в .031; проверки соседей .034 будут уточнять контракты без повторного подсчёта класса.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../../../module/actor/sheets/WitcherCharacterSheet.js.md). [Методика и ограничения сверки](../../../../../review-log.md#task-0003031).

## Уточнение TASK-0003.034

2026-09-11, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`. Полностью разобран включаемый substances.hbs: безусловный partial:212, девять иконок/сумм, флаги и таблицы. Он не потребляет alchemyComponentsList. Смена плашки вызывает отдельный Item-mixin handler, а .crafting-craft остаётся прежним входом WitcherCharacterSheet; различие с алхимическим действием не исправлялось.

Связи: [templates/partials/character/substances.hbs](../../../partials/character/substances.hbs.md); [module/actor/sheets/mixins/alchemyMixin.js](../../../../module/actor/sheets/mixins/alchemyMixin.js.md). [Результаты и пределы проверки](../../../../../review-log.md#task-0003034).

## Дополнительная сверка TASK-0003.036

2026-09-11, `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; исходники не менялись.

Полностью прослежен .open-currency-converter14–16: CharacterSheet PARTS→базовый activateListeners→currencyConverterListeners→Actor.handleCurrencyConverter→openCurrencyConverter. Кнопка не data-action. Этот маршрут теперь проверен с реальными методами/моделями и фасадами Dialog/update; браузерное окно целиком не запускалось. Независимая .open-rewards остаётся зависимостью будущей .037.

Карточки процесса: [module/actor/mixins/currencyConverterMixin.js](../../../../module/actor/mixins/currencyConverterMixin.js.md), [module/actor/sheets/mixins/currencyConverterMixin.js](../../../../module/actor/sheets/mixins/currencyConverterMixin.js.md), [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../currencyConverter/currencyConverter.hbs.md), [templates/chat/currency-conversion.hbs](../../../chat/currency-conversion.hbs.md).

[Проверки и перекрёстная сверка](../../../../../review-log.md#task-0003036). Связанный файл повторно в покрытии не учитывается; правок системы нет.

## Дополнительная сверка TASK-0003.037

2026-09-11, `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; исходники не менялись.

Отдельная .open-rewards17 открывает RewardsSheet через CharacterSheet, а не диалог начисления и не конвертер валюты. Окно показывает журналы; его currency history не включает автоматически все обмены/покупки, поскольку те пишут баланс другими методами.

[module/actor/mixins/rewardsMixin.js](../../../../module/actor/mixins/rewardsMixin.js.md), [module/actor/rewardsSheet.js](../../../../module/actor/rewardsSheet.js.md), [module/app/reward/reward.js](../../../../module/app/reward/reward.js.md), [templates/chat/rewards.hbs](../../../chat/rewards.hbs.md).

[Перекрёстная сверка и ограничения](../../../../../review-log.md#task-0003037). Связанные файлы повторно в покрытие не добавлялись; исходники и статусы issues не менялись.
