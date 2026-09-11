# module/actor/sheets/interactions/itemContextMenu.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `45a63062a2bd55939fef430609fc5dddc350b0e9` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.026](../../../../../../../tasks/task-0003.026.md), 2 файла, 528 логических строк |
| Запись перекрёстной сверки | [TASK-0003.026](../../../../../review-log.md#task-0003026) |

## Назначение файла

Примесь контекстного меню Item на Actor-листах: собирает шесть пунктов и делегирует редактирование, расходование, снятие улучшений, передачу, разборку и удаление. Содержит условия видимости и действия; не определяет новый Document или схему.

## Условия использования

Подключается Object.assign к WitcherActorSheet, WitcherActorSheetV1 и WitcherLootSheet. V2 получает DOM; V1 передаёт html[0]. Меню создаётся на '.item' с jQuery:false. Foundry 14.367 поддерживает и onClick(event,target), и устаревший callback(target,event); одинаковыми их считать нельзя. Три callbacks написаны под новый порядок, delete callback — под старый. Все дальнейшие проверки gift/removeEnhancement/dismantle отдельно выполнены прямым вызовом с правильной сигнатурой и не объявляются успешным UI-маршрутом.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| itemContextMenu | export let:5–184 | 15 методов | Object.assign в трёх классах Actor-листов | Публичные методы с this листа |
| DialogV2 | Локальная const:3 | API prompt | При вычислении модуля | giftItem ждёт выбор получателя |
| Шесть ContextMenuEntry | editItem/consumableItem/removableEnhancement/giftableItem/dismantableItem/deleteItem | label, icon, onClick либо callback, visible | Собраны при itemContextMenu(html) | 2 новых onClick, 4 legacy callback, 4 предиката visible |
| giftableTypes | Локальный массив isItemGiftable:100–110 | 9 типов Item | Создаётся при каждом предикате | alchemical, armor, component, diagrams, enhancement, mount, mutagen, valuable, weapon |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| itemContextMenu(html):6–20 | DOM контейнер | undefined | new foundry.applications.ux.ContextMenu(html,'.item',[6 entries],{jQuery:false}) | Ссылку хранит только локальный contextMenu; повторные создания/закрытие в browser не проверены |
| editItem():22–31 | this.actor | Entry: onClick(event,target) | ID из target.dataset.itemId; item.sheet.render(true) | Без visible; render не ждёт. Современная сигнатура корректна |
| consumableItem():33–40 | Методы consumeItem/isItemConsumable | Entry: onClick + visible | Два bind(this) | onClick использует правильные аргументы |
| isItemConsumable(itemHtml):42–46 | DOM itemHtml.dataset.itemId | false либо system.isConsumable | Missing Item→false | Тип/количество/права отдельно не проверяет |
| consumeItem(pointerEvent,target):48–57 | Целевой Item и isConsumable | undefined либо результат notifications.error | Если не consumable — уведомление и return; иначе item.consume(), actor.removeItem(id,1) | Обе операции не ждёт; missing ID даёт TypeError, нулевое количество не запрещено |
| removableEnhancement():59–66 | removeEnhancement/isEnhancementRemovable | Entry: callback + visible | callback=this.removeEnhancement.bind(this) | Старый callback передаёт DOM первым, PointerEvent вторым, а метод ожидает наоборот |
| isEnhancementRemovable(itemHtml):68–73 | DOM ID | false либо system.applied | Без Item→false | Не проверяет type, наличие родителя или количество |
| removeEnhancement(pointerEvent,target):75–88 | DOM улучшения, его внешний parentElement.closest('.item') | undefined | update applied=false и name.replace('(Applied)',''); затем parent.update списка ID без выбранного | Записи не ожидаются; при отсутствующем DOM-родителе первая уже инициирована. Не удаляет Item, не объединяет остатки; фильтр удаляет все совпавшие ID |
| giftableItem():90–97 | giftItem/isItemGiftable | Entry: callback + visible | Связывает передачу с девятью типами | Та же ошибка порядка legacy callback |
| isItemGiftable(itemHtml):99–115 | DOM ID | boolean | Missing Item→false; includes в девяти типах | container/race/profession/homeland/spell исключены; enhancement допускается даже applied; quantity не проверяет |
| giftItem(pointerEvent,target):117–150 | ID Item; game.actors с hasPlayerOwner | Promise<void> после выбора и инициирования операций | Опции всех player-owned world Actor, включая отправителя. await prompt(rejectClose:true), GM→fromUuidSync(receiver).addItem(item), игрок→emitForGM('addItem',[receiver,item,1]); removeItem(id,1) | Передача одной единицы; не ждёт получателя/emit/removal, нет подтверждения, rollback, target guard. Отмена отклоняет Promise до списания. Связи embedded Item не переписываются |
| dismantableItem():152–159 | dismantleItem/isItemDismantable | Entry: callback + visible | Существующее написание dismantable | Та же ошибка порядка legacy callback |
| isItemDismantable(itemHtml):161–166 | DOM ID | false либо результат item.canBeDismantled() | Missing Item→false | Реальная примесь возвращает truthy UUID для weapon/armor, не обязательно boolean; доступность UUID и quantity не проверяет |
| dismantleItem(pointerEvent,target):168–172 | ID Item | Promise<void> | item.dismantle() | Не ожидает возврат компонентов/записи; сам qty не уменьшает, делегирует Item |
| deleteItem():174–183 | this.actor | Entry: callback(target) | Аргумент назван event, но это DOM: dataset.itemId→item.delete() | Старое поле работает в Foundry 14.367 с jQuery:false; отсутствуют visible/confirm/await |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| emitForGM | [module/scripts/socket/socketMessage.js](../../../../../../../../module/scripts/socket/socketMessage.js) | Именованный import | giftItem при !game.user.isGM | Проверяет socket/user/users/activeGM; без GM пишет console.error и возвращается, подтверждения выполнения нет |
| registerSocketListeners | [module/setup/socketHook.js](../../../../../../../../module/setup/socketHook.js) | Косвенный получатель сообщения | system.TheWitcherTRPG, type=addItem; receiver UUID удаляется из data через shift | Только activeGM исполняет `fromUuidSync(...)[type](...args)`, не ждёт результат |
| consume, isConsumable, canBeDismantled, dismantle | [module/item/witcherItem.js](../../../../../../../../module/item/witcherItem.js); [module/item/mixins/consumeMixin.js](../../../../../../../../module/item/mixins/consumeMixin.js); [module/item/mixins/dismantlingMixin.js](../../../../../../../../module/item/mixins/dismantlingMixin.js) | Методы Item/примесей | Условия и действия меню | consume не списывает qty: это делает caller. dismantle добавляет найденные компоненты и списывает 1; getter допуска проверяет тип и associatedDiagramUuid |
| addItem/removeItem | [module/actor/witcherActor.js](../../../../../../../../module/actor/witcherActor.js) | Методы Actor | Передача, расходование, получение остатков разборки | addItem default quantity=1; removeItem при newQuantity<=0 удаляет документ; оба ожидают свои операции, callers меню — нет |
| applyActiveEffectToActorViaId | [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | Косвенный helper consume | Применение applySelf по UUID источника | Последний предмет может быть удалён до окончания consume; это прежняя issue-00034/00045 |
| quantity/isConsumable/applied/associatedDiagramUuid | [module/data/item/commonItemData.js](../../../../../../../../module/data/item/commonItemData.js); [module/data/item/valuableData.js](../../../../../../../../module/data/item/valuableData.js); [module/data/item/enhancementData.js](../../../../../../../../module/data/item/enhancementData.js); [module/data/item/weaponData.js](../../../../../../../../module/data/item/weaponData.js); [module/data/item/armorData.js](../../../../../../../../module/data/item/armorData.js) | Поля моделей | Предикаты и изменения | Нулевое StringField quantity допускается; наличие UUID не подтверждает существование рецепта |
| ContextMenu, DialogV2.prompt, game.actors/users/socket, fromUuidSync, Document | Foundry VTT 14.367.0 | Внешний API | Диспетчер callbacks, выбор получателя, передача и записи | /opt/foundryvtt/client/applications/ux/context-menu.mjs:74–109,375–381,611–624; DialogV2.wait rejectClose; живые записи подменены |
| labels WITCHER.Item.ContextMenu.* | [lang/en.json](../../../../../../../../lang/en.json) | Локализация внешним меню и notification | 6 подписей и NotConsumable; icon классы Font Awesome | Записаны строковые ключи текущего кода; локализации/стили не менялись |
| data-item-id вложенного улучшения | [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | DOM-связь | removeEnhancement ищет внешний .item по parentElement | Вложенные .item.weapon-enhancement находятся внутри Item оружия/брони; внешний список runes/glyphs иной |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | itemContextMenu | import/Object.assign; activateListeners вызывает itemContextMenu(html) | Character/Monster V2 используют меню |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | itemContextMenu | import/Object.assign; itemContextMenu(html[0]) | V1 не имеет зарегистрированного наследника |
| [module/actor/sheets/WitcherLootSheet.js](../../../../../../../../module/actor/sheets/WitcherLootSheet.js) | itemContextMenu | import/Object.assign; _onRender вызывает itemContextMenu(this.element) | Отдельный V2-класс; полная карточка будет позже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | Шесть entries по условиям | Внешние и вложенные .item с data-item-id | Внешний Foundry подставляет DOM контекстной цели |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | Шесть entries по условиям | Аналогичный вложенный DOM улучшений | Права и реальные browser-события отдельно не воспроизводились |

Область поиска: module/ и templates/ текущего checkout. Типы документов сверены с `system.json`, регистрация листов — с `module/setup/registerSheets.js`. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Меню держит this листа через bind и замыкания. Visibility — только отбор пунктов интерфейса: она не является проверкой прав операции и не повторяется в gift/removeEnhancement/dismantle. consumeItem повторно проверяет isConsumable, но не количество. Передача копирует одну единицу в Actor с hasPlayerOwner и списывает одну; world Actor не равен выбранному на сцене token, токены в selector не перебираются. Отправитель остаётся допустимым получателем. При отсутствии activeGM emitForGM возвращается без отправки, а списание продолжается. Сетевой пакет несёт Item-объект; реальная сериализация socket не тестировалась. removeEnhancement меняет имя/applied, затем ID родительского Item; pending/отказ одного update не отменяет другого. Dismantle делегирует расчёт floor(quantity/2) с минимумом 1 внешней примеси; ненайденные компоненты не создаются, отчёт получает найденные/ненайденные. Это описание кода, не независимое подтверждение правил TRPG.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| ContextMenu API | Группы 01–02; реальный _onClickItem ядра в минимальном классе с private-полями | 2 onClick, 4 callback. Edit/delete работают; removal синхронно падает, gift/dismantle возвращают rejected Promise | Создание меню/DOM не выполнялось в клиенте; ядро исполняло dispatch настоящими аргументами |
| Предикаты и DOM | Группы 03,14 | Missing Item скрыт; 9 giftable типов; applied независимо от type. Direct removal обновляет обе записи, stale parent даёт частичное начало | Menu failure исправлением не обходили: дальнейшие методы вызывались изолированно с корректными аргументами |
| Передача и сокет | Группы 15–16 | Нет GM→нет emit, но delete инициирован; rejected add не останавливает remove; self-recipient включён; cancel не списывает; активный GM принимает реальный envelope | emit/socket delivery/DB представлены фасадами, не сетевой эксперимент |
| Расходование и разборка | Группы 17–18 | quantity2→update1, quantity1/0→delete после consume; реальные dismantle/canBeDismantled рассчитали 5→2 и 0→1, создали найденный компонент | В consume применение заменено pending Promise; для dismantle UUID/записи/чат подменены |
| Границы await | Группы 14–18,21 | Callback-действия запускают операции без общей границы завершения; данные source и ссылка в DOM различаются | Фактическая потеря игровых документов в действующем мире не проверялась |

## Непроверенные участки и открытые вопросы

Все 184 строки и 15 методов прочитаны. Полный файл dismantlingMixin, socketMessage и шаблоны чата не засчитаны: здесь проверены вызываемые определения, а не вся отдельная задача этих подсистем. Правила обмена предметами, подтверждение GM, удаление связанных effects/content/IDs, нескольких пользователей и реальная сериализация socket не исследовались до выполнения. Нарушение серверных прав не установлено. Удаление связано с legacy callback корректно; переписывать все четыре callback по одному шаблону без проверки нельзя.

## Связанные проблемы

[issue-00034](../../../../../../../issues/potential/issue-00034.md), [issue-00045](../../../../../../../issues/potential/issue-00045.md), [issue-00049](../../../../../../../issues/potential/issue-00049.md), [issue-00168](../../../../../../../issues/potential/issue-00168.md), [issue-00169](../../../../../../../issues/potential/issue-00169.md), [issue-00174](../../../../../../../issues/potential/issue-00174.md). issue-00168 отделяет поломку входа меню от поведения внутренних методов; issue-00169 описывает отсутствие подтверждения передачи и списание, issue-00174 — расходование нулевого остатка. Старые async/UUID/status наблюдения уточнены без повторных ID.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `45a63062a2bd55939fef430609fc5dddc350b0e9`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003026) |
