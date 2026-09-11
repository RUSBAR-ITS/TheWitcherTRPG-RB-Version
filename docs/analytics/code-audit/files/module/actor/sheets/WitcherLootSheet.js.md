# module/actor/sheets/WitcherLootSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/WitcherLootSheet.js](../../../../../../../module/actor/sheets/WitcherLootSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `1d29f681ffed1c46b9c05b0eff09935300c3bf7d` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.035](../../../../../../tasks/task-0003.035.md), 6 файлов, 384 логические строки |
| Запись перекрёстной сверки | [TASK-0003.035](../../../../review-log.md#task-0003035) |

## Назначение файла

Лист Actor типа loot: готовит категории продаваемых/получаемых предметов, открывает покупку и переключает видимость строки. Наследует непосредственно Foundry ActorSheetV2 через HandlebarsApplicationMixin, а не WitcherActorSheet; поэтому не получает его totalCost, подготовку оружия/брони, настройки и навыки.

## Условия использования

registerSheets регистрирует класс по умолчанию для loot. Импорт определяет класс и присоединяет itemMixin/itemContextMenu через Object.assign (174–175). PARTS.main загружает единственный HBS; TABS пуст. DEFAULT_OPTIONS задаёт buyItem/hideItem и сохранение формы при изменении без закрытия. Внешний ActorSheetV2 предоставляет drag/drop и форму. get/set методов для монтируемого Actor mount здесь нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherLootSheet | default class:8–172 | Контекст и действия добычи | registerSheets:113–116 | Создание листа Actor loot |
| DEFAULT_OPTIONS / PARTS / TABS | static:10–29 | Два action, form submitOnChange/closeOnSubmit, main.scrollable=['']; без вкладок | Foundry ApplicationV2 | Шаблон loot-sheet.hbs |
| uniqueTypes | поле экземпляра:31 | profession, race, homeland | itemMixin._isUniqueItem | Влияет на Drop и удаление старого типа |
| coinOptions / percentOptions / Characteroptions / content | локальные строки:80–133 | Шесть валют, проценты 50/100/125/150/175/200; список доступных Actor | Диалог покупки | Имена Actor вставляются в строку HTML без экранирования; все OWNER, включая продавца |
| calcTotalCost / applyPercentage | function внутри script строки:99–113 | Пересчёт чисел формы, не схемы Actor | Только текст content и inline onChange | Первая qty×customCost; вторая ceil(cost×percentage/100), затем произведение |
| ok.callback | callback:140–147 | Четыре строковых значения формы | DialogV2.prompt | itemQty→numberOfItem, costTotalValue→totalCost, character→characterId, coinType |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _canDragStart / _canDragDrop(selector):34–41 | Любой selector | true | Разрешают вход DragDrop | Не являются разрешением записи; _onDropItem отдельно требует actor.isOwner |
| _prepareContext(options):44–66 | super context и this.document | Promise context | actor/system; getList weapon/armor/valuable/component; enhancement без applied; loot=mount+mutagens+container+alchemical+diagrams; totalWeight; isGM | getList исключает stored и сортирует; mutagens не зарегистрирован; totalCost не устанавливается; исходные Item не меняются |
| _onRender(context,options):68–73 | element | undefined | super._onRender; itemListener; itemContextMenu | super не ожидается; нет собственной DragDrop-конфигурации; только регистрация listeners |
| _onItemBuy(event,element):75–161 | closest('.item').dataset.itemId; найденный Item; prompt | Promise<void> | Собирает content, OWNER-Actor (user.character selected), await prompt с rejectClose:true; buyer.currency[coinType]>=totalCost; затем removeItem→addItem→buyer.update→seller.update | Четыре операции без await/return/компенсации. Нет проверки запаса, диапазона, согласованности цены, повторного OWNER, отличия buyer/seller. Missing buyer/Item → TypeError; неизвестная валюта/нехватка→Not Enough Coins; отмена отклоняет Promise |
| _onItemHide(event,element):163–169 | Item по строке | Promise<void> | item.update({'system.isHidden': !old}) | Запись не ожидается; собственная проверка isGM отсутствует; GM ограничен показом кнопки |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| itemContextMenu, itemMixin | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js); [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | прямой импорт + Object.assign | 1–2,174–175; listeners68–73; inherited _onDropItem | Полные mixin-определения и назначение prototype; меню отличается от buyItem action |
| getList / getTotalWeight / removeItem / addItem / removeItemsOfType | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | вызовы документа | 49–62,152–153; inherited Drop | getList250–257; addItem259–273; removeItem275–283; real методы в группах02–17 |
| LootData.maxWeight / currency / calcCurrencyWeight | [module/data/actor/lootData.js](../../../../../../../module/data/actor/lootData.js) | модель контекста/валюты | context.system; currency150,155–158 | Схема loot не содержит skills; weight использует валюту |
| currency() | [module/data/actor/templates/common/currencyData.js](../../../../../../../module/data/actor/templates/common/currencyData.js) | семь NumberField | buyer/seller.system.currency[coinType] | Шесть валют в prompt; falsecoin только в листе; обмена курсов нет |
| CommonItemData.quantity / cost / isStored / isHidden / calcWeight | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | вход расчётов | Строковое quantity, числовой cost; hide | Схема/группы01,04–15; price initial из cost; total editable |
| MountData / EnhancementData / MutagenData | [module/data/item/mountData.js](../../../../../../../module/data/item/mountData.js); [module/data/item/enhancementData.js](../../../../../../../module/data/item/enhancementData.js); [module/data/item/mutagenData.js](../../../../../../../module/data/item/mutagenData.js) | типы getList | enhancement.applied, mount; ошибочное mutagens | registerDataModels ключ mutagen, не mutagens; applied только фильтр |
| main | [templates/sheets/actor/loot-sheet.hbs](../../../../../../../templates/sheets/actor/loot-sheet.hbs) | путь PARTS | 23 | Единственный HBS листа; связь обратная |
| ActorSheetV2 / HandlebarsApplicationMixin / DialogV2 | Foundry 14.367.0: /opt/foundryvtt/client/applications/{sheets/actor-sheet.mjs,api/document-sheet.mjs,api/application.mjs,api/dialog.mjs} | наследование + окно + dispatch | 4–6,8,44,69,135 | Actor dragSelector .draggable; document editable OWNER; action.call(this,event,target); dialog._renderHTML присваивает innerHTML, wait rejectClose |
| game.actors / user / i18n / ui.notifications / document | Foundry globals; browser document | выбор покупателя, localize, уведомления, inline script | 80–158 | testUserPermission OWNER; getElementById только внутри текста script. UI автора/БД не моделировались полностью |
| WITCHER.Currency.* / WITCHER.Loot.* | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | локализация диалога | coinOptions и подписи75–148 | Прямые ключи входят в29 проверенных по всей порции; game.i18n.localize после раскрытия dotted paths |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherLootSheet | import3; register Actors loot113–116 | makeDefault:true |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../../../templates/sheets/actor/loot-sheet.hbs) | actor/system и массивы, totalWeight/isGM; buyItem/hideItem | PARTS.main и вложенные строки | Шесть списков; totalCost consumer без producer |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../../../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) | _onItemBuy / _onItemHide | data-action и Item ID | 19–22 |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Actor(type:'loot') и лист | Косвенно exportLoot→регистрация loot | 181–204; копируются все Items, не только context.loots |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Контекст хранит ссылки на actor/system и Item, создаёт отсортированные массивы; schema source не изменяет. Купленный Item при совпадении name+type складывается по количеству и сохраняет прежние свойства покупателя; иначе копируется toObject со всеми полями, включая isHidden/isStored. Цена целиком берётся из editable costTotalValue в выбранной валюте; штатного курса тут нет. Изолированно stock2, запрос5 удалил источник и передал5; итог −10 увеличил деньги покупателя100→110 и уменьшил продавца5→−5. При удержанных четырёх записях handler уже завершён, повтор выдаёт одинаковые абсолютные остатки. Покупка самим продавцом может конкурировать с удалением/увеличением и двумя изменениями одной валюты; это конкретные payload и порядок фасада, не доказательство серверного результата. isHidden скрывает строку CSS, но данные остаются в HTML; это не средство конфиденциальности.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Весь класс | nl/rg; группы02–18,21–26 | Категории, типы, методы и callbacks прочитаны; 26 групп всей порции прошли | Границы ниже |
| Покупка | Группы05–14 | Норма, нехватка, неизвестная валюта, отмена, отсутствие покупателя, 0/−1/0.5/5 quantity, 0/−10/0.25/0.5 price, stacking, self, pending записи | Выбор формы и запись подменены; min/step браузера не исполнялись |
| Права / Drop | Группы16–18,23–24 и core sources | OWNER guard для Item Drop; сортировка; profession→TypeError без skills; GM/owner/observer permission; поля disabled, anchors остаются | Нет утверждения об обходе прав сервера |
| Диалог и переводы | 22,25–26 | 29 прямых ключей порции найдены EN/RU после expandObject+Localization; script вручную даёт20/26; core присваивает строку innerHTML | Автоматическое исполнение script в браузере не проверено |

## Непроверенные участки и открытые вопросы

Исполнены настоящие методы системы и модели Foundry 14.367.0 в изолированном Node 24.16.0. Коллекции документов, окна, запись и базовый Application — фасады; HBS — настоящий Handlebars 4.7.9, разбор HTML — parse5. Полный клиент, DOM-события, сервер, права реальной БД, сетевые гонки и сохранение мира не проверялись. Пути systems/TheWitcherTRPG сохранены как в исходниках; доступ по HTTP здесь не проверялся. Покупка не вызывает checkIfItemHasRollTable; это отдельный этап exportLoot (.032). Валютный обмен (.036) и награды (.037) остаются вне полного разбора. Внутренние глобальные calcTotalCost/applyPercentage не проверены как реально установленные функции окна; требуют клиентской проверки. CSS/локализации исследованы только как зависимости.

## Связанные проблемы

[issue-00034](../../../../../../issues/potential/issue-00034.md), [issue-00039](../../../../../../issues/potential/issue-00039.md), [issue-00040](../../../../../../issues/potential/issue-00040.md), [issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00166](../../../../../../issues/potential/issue-00166.md), [issue-00168](../../../../../../issues/potential/issue-00168.md), [issue-00169](../../../../../../issues/potential/issue-00169.md), [issue-00206](../../../../../../issues/potential/issue-00206.md), [issue-00207](../../../../../../issues/potential/issue-00207.md), [issue-00208](../../../../../../issues/potential/issue-00208.md), [issue-00218](../../../../../../issues/potential/issue-00218.md), [issue-00219](../../../../../../issues/potential/issue-00219.md), [issue-00220](../../../../../../issues/potential/issue-00220.md), [issue-00221](../../../../../../issues/potential/issue-00221.md), [issue-00222](../../../../../../issues/potential/issue-00222.md), [issue-00223](../../../../../../issues/potential/issue-00223.md), [issue-00224](../../../../../../issues/potential/issue-00224.md), [issue-00225](../../../../../../issues/potential/issue-00225.md), [issue-00226](../../../../../../issues/potential/issue-00226.md). Новые наблюдения 218–226 остаются potential. Старые 34/39/40/63/166/168/169 сопоставлены по конкретным маршрутам: не все действуют в Loot. Исправления и решения по механике отсутствуют.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003035) |

## Дополнительная сверка TASK-0003.036

2026-09-11, `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; исходники не менялись.

Покупка не вызывает полный конвертер валют, не использует currencyRates и не получает его листовой listener. В .036 уточнён более ранний шаг DialogV2: _initializeApplicationOptions184–199 выполняет foundry.utils.cleanHTML для строкового content. Core helpers.cleanNode70–84 с allowlist common/constants1845+ удаляет script и inline onchange. В .035 изолированно вызывался _renderHTML после этого этапа, поэтому он не доказывал, что исходный script дойдёт до DOM. Issue226 дополнен этим источником; браузерный маршрут/полная DOM-очистка не исполнялись. У конвертера .036 HBS не содержит script/inline событий.

Карточки процесса: [module/actor/mixins/currencyConverterMixin.js](../mixins/currencyConverterMixin.js.md), [module/actor/sheets/mixins/currencyConverterMixin.js](mixins/currencyConverterMixin.js.md), [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs.md), [templates/chat/currency-conversion.hbs](../../../templates/chat/currency-conversion.hbs.md).

[Проверки и перекрёстная сверка](../../../../review-log.md#task-0003036). Связанный файл повторно в покрытии не учитывается; правок системы нет.
