# module/actor/sheets/mixins/itemMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../module/actor/sheets/mixins/itemMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `45a63062a2bd55939fef430609fc5dddc350b0e9` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.026](../../../../../../../tasks/task-0003.026.md), 2 файла, 528 логических строк |
| Запись перекрёстной сверки | [TASK-0003.026](../../../../../review-log.md#task-0003026) |

## Назначение файла

Объект примеси действий Item в листе Actor: Drop и уникальные типы, создание, переключатели, inline-edit, улучшения, раскрытие информации, использование и отправка описания в чат. Сам класс листа и модель данных не определяет.

## Условия использования

WitcherActorSheet, WitcherActorSheetV1 и WitcherLootSheet импортируют itemMixin и копируют его члены в prototype через Object.assign. Действующие Character/Monster наследуют первый; V1 не найден в регистрации. itemListener получает DOM и оборачивает его через $. _onDropItem вызывается унаследованным ActorSheet API. Перед записью проверка owner есть у Drop; прочие действия используют Document API и не имеют собственной общей проверки прав.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| itemMixin | export let:6–344 | 19 методов, включая регистрацию 23 обработчиков | Object.assign в трёх классах листов | Публичные функции вызываются с this листа |
| DialogV2 | Локальная const:4 | foundry.applications.api.DialogV2 | При вычислении модуля | _chooseEnhancement открывает prompt; это не импорт системы |
| itemData, delta, newEnhancementList, dialogData | Локальные объекты отдельных действий | Данные создания, флаги профессии, ID улучшений, контекст чата | Не являются схемами | newEnhancementList — ссылка на prepared-массив, а не копия |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _onDropItem(event,item):7–55 | actor.isOwner; Item либо Drop-данные; uniqueTypes на листе | Promise<false / результат сортировки / undefined> | Не WitcherItem→await Item.implementation.fromDropData→toObject. Тот же parent UUID→_onSortItem. Для uniqueTypes await removeItemsOfType. Monster weapon: equipped=true в prepared. Profession: сброс всех isProfession, затем установка выбранных. addItem(item) | Последние actor.update(delta)/addItem не ожидаются; removeItemsOfType тоже не ждёт внутреннего delete. После конвертации parent теряется; flag monster не входит в toObject source |
| _isUniqueItem(item):57–59 | this.uniqueTypes | boolean | includes(item.type) | У текущих трёх листов profession/race/homeland; массив не определён здесь |
| _onItemAdd(event):61–102 | currentTarget.dataset.itemtype/spelltype/subtype | Promise после Item.create | name='new <type>'; spellNovice/Journeyman/Master→Spells и level; magicalgift→MagicalGift; component alchemical/substances/component; valuable→general; diagram→alchemical novice isFormulae | Item.create(itemData,{parent:actor}) ожидается. Проверка diagram в единственном числе не совпадает с зарегистрированным diagrams; штатный diagrams создаётся с defaults |
| _onItemEquip(event):104–110 | closest('.item').dataset.itemId | Promise после update | preventDefault; toggle system.equipped | Нет Item→TypeError; update ожидается |
| _onItemCarried(event):112–118 | Тот же поиск ID | Promise после update | toggle system.isCarried | update ожидается; правила веса находятся в модели |
| _onItemLearned(event):120–126 | ID рецепта | Promise после update | toggle system.learned | Это learned у DiagramData, не isLearned у SkillItemData |
| _onItemInlineEdit(event):128–145 | closest('.item'), dataset.field и value | Promise Item.update | preventDefault/stopPropagation; 'false'→true, 'true'/'checked'→false; остальные значения без преобразования | Игнорирует input.type/checked/data-dtype; числовая очистка относится к схеме. Общий механизм issue-00153 |
| _onItemEdit(event):147–154 | ID Item | undefined | Останавливает событие, item.sheet.render(true) | Render не возвращается; отсутствие Item не обработано |
| _onItemShow(event):156–173 | ID Item, глобальный legacy Dialog | Promise<void> | Окно title=name, img HTML; width=520, resizable=true, пустые buttons | event.preventDefault указан без вызова; stopPropagation вызван. В текущих таблицах .item-show не найден; реальный browser legacy Dialog не запускался |
| _onItemDelete(event):175–180 | ID Item | Promise<void> | Останавливает событие; Item.delete() | Не ожидает удаления; не чистит ссылки контейнеров/улучшений |
| _chooseEnhancement(event):182–237 | ID и data-type внешнего .item; actor.getList('enhancement') | Promise<void> сразу после открытия prompt | Для weapon: rune/weapon, иначе armor/glyph; только applied==false. Prompt с выбором. Callback push ID, update родителя, update имени '(Applied)'/applied/quantity=1, при исходном quantity>1 forcecreate остатка | getList исключает stored; не проверяет quantity, вместимость или повтор ID. Нет списка→сообщение, но OK остаётся с обращением к отсутствующему select. Promise prompt/записи/остаток не ожидаются |
| _onItemDisplayInfo(event):239–245 | closest('.item') | Изменение CSS | preventDefault/stopPropagation; .item-info.toggleClass('invisible') | Игровые данные не пишет |
| _onDisplayList(event):247–257 | closest('.weapon-section'), .weapon-list, .fa-chevron-up | Изменение CSS | toggle invisible и rotate-180 | Ожидает старый DOM-контракт; в современных таблицах используется details. Нет элемента→TypeError; актуальный такой trigger в templates не найден |
| _onEnhancementInfo(event):259–265 | closest('.weapon-enhancement') | Изменение CSS | toggle .enhancement-info после остановки события | На пустом slot этот предок отсутствует; реальная jQuery-выборка может быть пустой, авария только из этого факта не утверждается |
| _onItemRoll(event):267–273 | ID Item, altKey/ctrlKey/shiftKey | Promise<void> | actor.useItem(id,{alt,ctrl,shift}) | Результат использования/броска не ожидает; неизвестный ID обрабатывает Actor.useItem |
| _onSpellDisplay(event):275–282 | closest('.spell').dataset.spelltype | undefined | toggle system.pannels.<spelltype>IsOpen через actor.update | Поля pan(n)els названы pannels в схеме; update не ожидается |
| _onSubstanceDisplay(event):284–291 | closest('.substance').dataset.subtype | undefined | toggle system.pannels.<subtype>IsOpen | update не ожидается; dataset веществ присутствует в substances.hbs |
| _onItemMessage(event):293–310 | closest('.list-item').dataset.itemId | Promise<void> | Контекст {item,type,config:WITCHER}; await renderTemplate item-description; ChatMessage.create(style=IC,speaker=getSpeaker({actor:actor.name})) | Не ждёт создания чата; actor передаётся строкой вместо документа. Вход .list-item присутствует в текущих таблицах |
| itemListener(html):312–343 | DOM либо jQuery-совместимый ввод | undefined | 23 привязки: click, change и отдельный stopPropagation для .inline-edit | Повтор на том же DOM не снимает обработчики; полный частичный render не проверялся |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WITCHER | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Именованный import | _onItemMessage передаёт справочник целиком как config | Экспорт WITCHER; HBS tags читает справочники по типу Item |
| WitcherItem | [module/item/witcherItem.js](../../../../../../../../module/item/witcherItem.js) | default import, instanceof | Разделяет современный Item и legacy Drop-данные | Класс extends внешний Item; используемый toObject наследуется от Foundry |
| getList/addItem/removeItemsOfType/useItem; update | [module/actor/witcherActor.js](../../../../../../../../module/actor/witcherActor.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js); [module/actor/sheets/WitcherLootSheet.js](../../../../../../../../module/actor/sheets/WitcherLootSheet.js) | this.actor и поля листов | Списки/добавление/уникальность/действие, uniqueTypes | Actor.addItem использует source toObject и по умолчанию quantity=1; root листы задают три уникальных типа |
| professionSkills, system.skills.<attr>.<skill>.isProfession | [module/data/item/professionData.js](../../../../../../../../module/data/item/professionData.js); [module/data/actor/templates/common/skills/skillsData.js](../../../../../../../../module/data/actor/templates/common/skills/skillsData.js); [module/data/actor/templates/common/skills/skillData.js](../../../../../../../../module/data/actor/templates/common/skills/skillData.js) | Схемы producer/consumer | Drop профессии: сброс и установка флагов | Обход ключей проверен с реальной ProfessionData; unknown даёт attr=undefined |
| quantity/isCarried и данные создания | [module/data/item/commonItemData.js](../../../../../../../../module/data/item/commonItemData.js); [module/data/item/componentData.js](../../../../../../../../module/data/item/componentData.js); [module/data/item/diagramData.js](../../../../../../../../module/data/item/diagramData.js); [module/data/item/valuableData.js](../../../../../../../../module/data/item/valuableData.js); [module/data/item/spellData.js](../../../../../../../../module/data/item/spellData.js) | Поля моделей | _onItemAdd, Carried/Learned/InlineEdit | defaults и очистка моделей проверены; поля quantity — StringField, learned — BooleanField |
| enhancementItemIds/equipped; applied/type/quantity | [module/data/item/weaponData.js](../../../../../../../../module/data/item/weaponData.js); [module/data/item/armorData.js](../../../../../../../../module/data/item/armorData.js); [module/data/item/enhancementData.js](../../../../../../../../module/data/item/enhancementData.js) | Поля DataModel, prepared/source | Drop оружия монстру, установка улучшений и разделение стека | Реальные модели и source toObject; три операции записи подменены отдельно |
| pannels.*IsOpen | [module/data/actor/templates/character/pannelsData.js](../../../../../../../../module/data/actor/templates/character/pannelsData.js) | Схема Actor | Spell/SubstanceDisplay строят путь из dataset | Сверено написание pannels и существующие флаги |
| Item.create/fromDropData/toObject, ActorSheet._onSortItem, Document.update/delete | Foundry VTT 14.367.0 | Внешний API | Создание и сортировка встроенного Item, преобразование и запись | /opt/foundryvtt/client/applications/sheets/actor-sheet.mjs:341–350,376–405; appv1/sheets/actor-sheet.mjs:247–260 |
| DialogV2.prompt, legacy Dialog, $, ChatMessage, CONST | Foundry VTT 14.367.0 и jQuery | Глобальные API | Окна, DOM и чат | Core DialogV2.prompt/wait и ChatMessage.getSpeaker просмотрены; реальный getSpeaker исполнен с классами-фасадами |
| item-description.hbs | [templates/chat/item/item-description.hbs](../../../../../../../../templates/chat/item/item-description.hbs) | Литеральный renderTemplate | Единственный собственный путь HBS: _onItemMessage | Корневой шаблон включает пять partial; реальный Handlebars-рендер с контекстом |
| description/spell-description/alchemicals/crafting-items/tags | [templates/chat/item/partials/item-description/description.hbs](../../../../../../../../templates/chat/item/partials/item-description/description.hbs); [templates/chat/item/partials/item-description/spell-description.hbs](../../../../../../../../templates/chat/item/partials/item-description/spell-description.hbs); [templates/chat/item/partials/item-description/alchemicals.hbs](../../../../../../../../templates/chat/item/partials/item-description/alchemicals.hbs); [templates/chat/item/partials/item-description/crafting-items.hbs](../../../../../../../../templates/chat/item/partials/item-description/crafting-items.hbs); [templates/chat/item/partials/item-description/tags.hbs](../../../../../../../../templates/chat/item/partials/item-description/tags.hbs) | Косвенный HBS consumer | Поля Item, type и config; текстовые описания через двойные скобки | StringField effect экранируется, markup и @UUID остаются текстом; это не признано самостоятельной ошибкой |
| Ключи WITCHER.Enhancement.*, WITCHER.Dialog.Enhancement | [lang/en.json](../../../../../../../../lang/en.json) | Локализация | Выбор улучшения/сообщение о пустом списке | Вызов game.i18n.localize, без редактирования словаря |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | itemMixin, itemListener, _onDropItem | import/Object.assign; itemListener с DOM; Drop через ядро | Действующие Character/Monster наследуют общий V2 |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | itemMixin | import/Object.assign; itemListener(html[0]); legacy Drop | Класс V1 не зарегистрирован |
| [module/actor/sheets/WitcherLootSheet.js](../../../../../../../../module/actor/sheets/WitcherLootSheet.js) | itemMixin | import/Object.assign; itemListener(this.element) | Отдельный ActorSheetV2; полный файл не засчитан |
| [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | _onItemAdd | data-itemType и data-spellType превращаются HTML parser в lowercase dataset | subtype не записывается в data-subtype — issue-00173 |
| [templates/partials/character/substances.hbs](../../../../../../../../templates/partials/character/substances.hbs) | _onSubstanceDisplay и создание компонентов | data-subtype на иконках; subtype у partial списка | Потеря subtype именно на кнопке добавления, не на иконке |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | ItemMessage/ItemRoll/ItemDisplayInfo/Add | .item.list-item и item-chat/spell-roll/item-display-info | spellType доступен во вложенном контексте; его потеря не обнаружена |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | Equip/InlineEdit/Message/Enhancement | data-type=weapon, item-id, пустой слот и вложенное улучшение | Сверены DOM-фрагменты до selector/dataset |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | Equip/Message/Enhancement | data-type отсутствует; freeEnhancements имеет класс enhancement-weapon-slot | dataset.type=undefined ведёт в else для armor/glyph, имя класса не выбирает weapon |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | InlineEdit/Message/Add | quantity, .item.list-item, общий header | Создание группы vitriol дало обычный component |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | Learned/InlineEdit/Message | Использует system.learned | Модель DiagramData подтверждает путь |
| [templates/partials/item-image.hbs](../../../../../../../../templates/partials/item-image.hbs) | _onItemShow | Условная .item-show при настройке и clickableImage; включена лишь прежним monster-inventory-tab.hbs | Текущий зарегистрированный MonsterSheet не использует этот путь; issue-00063 |

Область поиска: module/ и templates/ текущего checkout. Типы документов сверены с `system.json`, регистрация листов — с `module/setup/registerSheets.js`. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Drop сначала может удалить уникальные Item и сбросить профессиональные флаги, затем инициировать добавление без ожидания; исход нового процесса не атомарен. В современной ветви item остаётся исходным Document: assignment equipped меняет только prepared-модель, а addItem копирует сохранённый source. В legacy ветви toObject создаёт plain data и теряет parent до проверки сортировки. Установка улучшения push меняет живой enhancementItemIds до update; source модели ещё прежний. Применённое улучшение становится quantity=1, остаток копируется forcecreate с указанным числом; данные копии зависят от source в момент toObject. В проверке синхронного commit использован искусственный вариант update-фасада, не доказанная очередность штатной записи Foundry. Основные действия Equip/Carried/Learned/Create/InlineEdit ожидают или возвращают операцию; большинство остальных только запускают её. Раскрытие описаний и списка меняет DOM, переключение pannels пишет Actor. Чат получает исходный Item и строковый actor.name; реальный speaker выбирает другой контекст.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота и источники | 344 строки; 19 методов, 23 привязки; imports и три Object.assign | Все собственные определения описаны, один прямой HBS | Полные таблицы инвентаря относятся к .027 |
| Drop/уникальность/создание | Группы 04–08; настоящие itemMixin/WitcherItem/модели и Actor-методы | Owner false→return, same-parent→sort; conversion не сортирует; потеря equipped; повтор расы и unknown profession; варианты создания/контекст HBS | Item/Actor базы, source-сериализация документа и операции БД заданы фасадом |
| UI и действия | Группы 09–12; настоящий код и DOM-фасады | Toggle/inline payload, 23 привязки, useItem modifiers, pannels, выбор типов улучшений | Не реальный browser; старые DOM-кнопки не выдаются за найденные современные |
| Улучшения | Группы 13–14,21 | Дубли ID и нулевое количество допустимы; отказ update не отменяет другую запись; stale ID уже добавлен до ошибки | Синхронный commit-фасад — отдельный контроль, не реальный порядок сервера |
| Чат | Группы 19–20; настоящий Handlebars и core getSpeaker | Контекст отрендерен, .list-item найден в HBS; actor.name выбирает fallback, переданный Actor выбирает владельца | Шаблоны чата просмотрены по потребляемым данным, полного покрытия не получили |

## Непроверенные участки и открытые вопросы

Не запускались мир, браузер, права разных клиентов, реальный серверный порядок записей, полный бой/изготовление, настоящий socket/query. Сортировка проверена как выбор ветви и передача Item в _onSortItem; тело сортировки Foundry прочитано, DOM и updateEmbeddedDocuments не исполнялись. Отмена выбора улучшения моделировалась возвратом null без callback; базовый rejectClose=false проверен статически. Точка .item-show есть в item-image.hbs, подключённом только прежним monster-inventory-tab.hbs; текущие PARTS её не используют (issue-00063). Для .weapon-list-display вход в templates не найден. Это не исключает внешние вызовы. Полный разбор дочерних листов, чата и внешних действий остаётся по плану.

## Связанные проблемы

[issue-00034](../../../../../../../issues/potential/issue-00034.md), [issue-00116](../../../../../../../issues/potential/issue-00116.md), [issue-00153](../../../../../../../issues/potential/issue-00153.md), [issue-00166](../../../../../../../issues/potential/issue-00166.md), [issue-00170](../../../../../../../issues/potential/issue-00170.md), [issue-00171](../../../../../../../issues/potential/issue-00171.md), [issue-00172](../../../../../../../issues/potential/issue-00172.md), [issue-00173](../../../../../../../issues/potential/issue-00173.md), [issue-00175](../../../../../../../issues/potential/issue-00175.md), [issue-00063](../../../../../../../issues/potential/issue-00063.md). Новые наблюдения относятся к выбору/установке улучшения, подготовленному equipped, созданию компонентов и speaker. Inline-преобразование дополнено в существующей issue-00153, неизвестный навык — issue-00116, замена расы — issue-00034; дубли новых ID не создавались.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `45a63062a2bd55939fef430609fc5dddc350b0e9`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003026) |

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Пофайловая сверка HBS уточнила DOM: современная броня не имеет data-type=armor; dataset.type=undefined ведёт _chooseEnhancement в else и отбирает armor/glyph. Предыдущее описание этого атрибута исправлено. Все восемь inline-редакторов передают quantity; toggles equipped/carried/learned проверены по отрендеренным входам. У container.stored-item data-item-id содержит UUID, но .item отсутствует: общий поиск выбирает внешний контейнер.

Связанные шаблоны: [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs); [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs); [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../../../templates/partials/monster/monster-inventory-tab.hbs). [Проверки и ограничения](../../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Уточнён потребитель _onItemInlineEdit: старый monster-custom-skill-display передаёт data-field=system.value и Item ID. Реальный метод выдаёт строку '-2.5'; настоящая NumberField SkillItemData принимает −2.5. Это проверка преобразования модели, не записи в мире. Новая текущая custom-строка этого inline поля не содержит.

Сверенные связи: [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../../../../templates/partials/monster/monster-custom-skill-display.hbs); [module/data/item/skillItemData.js](../../../../../../../../module/data/item/skillItemData.js). Полные карточки новых файлов — в [указателе порции](../../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. monster-notes .add-item/data-itemType='note' проходит HTML-преобразование в dataset.itemtype; старые Item title/textarea имеют data-field и item-id. В each {{system.description}} читает system текущего note, не Actor. Нет имени обычной формы; отдельный _onItemInlineEdit остаётся необходим. Конкретный полный цикл создания заметок перенесён в .033 по плану.

Связи: [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs.md). [Результаты и пределы проверки](../../../../../review-log.md#task-0003032).

## Уточнение TASK-0003.033

2026-09-11, `12055fee62f01c6de49967044aedef9d7cfe0632`. Полный tab-background связывает .add-item/note, .inline-edit data-field=name/system.description и .item-delete. Группа 07 выполнила настоящие методы: Item.create получил {name:'new note',type:'note'} и parent Actor; описание HTML передано строкой, literal false/true/checked преобразованы как в issue-00153. Item.delete перехвачен; array-notes остались прежними.

Связи: [templates/partials/character/tab-background.hbs](../../../../templates/partials/character/tab-background.hbs.md); [module/data/item/noteData.js](../../../data/item/noteData.js.md). [Результаты и пределы проверки](../../../../../review-log.md#task-0003033).

## Уточнение TASK-0003.034

2026-09-11, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`. Полный substances HBS создаёт .item-substance-display с data-subtype для всех девяти ключей. Настоящий _onSubstanceDisplay вызвал preventDefault и update system.pannels.vitriolIsOpen. После открытия кнопка add-item из вложенного summary всё ещё не имеет data-subtype: _onItemAdd создал обычный component (issue-00173).

Связи: [templates/partials/character/substances.hbs](../../../../templates/partials/character/substances.hbs.md). [Результаты и пределы проверки](../../../../../review-log.md#task-0003034).

## Дополнительная сверка TASK-0003.035

2026-09-11, `rusbar-main`, `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; исходники не менялись.

WitcherLootSheet Object.assign174 подключает itemMixin и вызывает itemListener в _onRender. Его HBS поддерживает .add-item/.inline-edit/.item-edit/.item-delete; buy/hide идут отдельными actions. Общий _onDropItem по-прежнему требует actor.isOwner даже при _canDragDrop=true, делает сортировку своего Item, копирует чужой mount, uniqueTypes race/profession/homeland. В Loot нет skills: profession вызывает TypeError после removeItemsOfType (новый issue225). Inline quantity0.5 передан строкой и сохранён строкой; Number dtype сам этот handler не применяет.

Полные карточки порции: [module/actor/sheets/WitcherLootSheet.js](../WitcherLootSheet.js.md), [templates/sheets/actor/loot-sheet.hbs](../../../../templates/sheets/actor/loot-sheet.hbs.md), [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../../templates/sheets/actor/partials/loot/loot-item-display.hbs.md), [module/data/item/mountData.js](../../../data/item/mountData.js.md), [module/item/sheets/WitcherMountSheet.js](../../../item/sheets/WitcherMountSheet.js.md), [templates/sheets/item/mount-sheet.hbs](../../../../templates/sheets/item/mount-sheet.hbs.md).

[Проверки, общая сверка 31 файла с прежними 247 и ограничения](../../../../../review-log.md#task-0003035). Связанный файл повторно в покрытии не учитывается; исправления не выполнялись.
