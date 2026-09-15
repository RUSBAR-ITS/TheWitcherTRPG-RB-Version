# TASK-0006.013 — Инвентарь, количество и расходники

2026-09-15, rusbar-main; исходный HEAD 4bb8dd93abad2521698edd4a156d40737469a72c. Рабочее дерево перед порцией чистое. [Задача](../../tasks/task-0006.013.md), [справочник](README.md).

## Область и остаток

Индексирует текущий код и уточняет поиск по нему. Схема v1 и query.py сохранены; исходники, аудит/issues, игровые данные и Git не изменяются. Все новые области partial. Наличие определения не означает полного списка callers.

| Основной исходник | Включено и предел |
| --- | --- |
| [module/actor/witcherActor.js](../../../module/actor/witcherActor.js) (src-000047) | Выбранные inventory/consume/status входы раскрыты; полные бой, локации, лечение, все callers и серверное сохранение остаются .014–.022/ядру. |
| [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js) (src-000043) | Drop/CRUD/quantity/roll и подписки раскрыты; тела улучшений, панелей, картинки и подробностей остаются адресованными входами. Не все DOM callers проиндексированы. |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../module/actor/sheets/interactions/itemContextMenu.js) (src-000034) | Меню consume/gift/delete и сигнатуры раскрыты; полные снятие улучшений, dismantle и динамическое состояние меню вне порции. |
| [module/item/mixins/consumeMixin.js](../../../module/item/mixins/consumeMixin.js) (src-000157) | Локальные тела consume/сообщения раскрыты; полные heal/статус/AE/чат lifecycle и запись в мире делегируются существующим процессам либо внешним API. |
| [module/data/item/templates/consumableData.js](../../../module/data/item/templates/consumableData.js) (src-000136) | Поля и три включения схемы раскрыты; внутренние field constructors, все потребители и экземплярный lifecycle частичны. |
| [module/data/item/templates/consumePropertiesData.js](../../../module/data/item/templates/consumePropertiesData.js) (src-000137) | Четыре поля и вложенные itemEffect раскрыты; метаданные полей, все callers и очистка ядра остаются partial. |
| [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) (src-000184) | Ручные CRUD массивов и render listeners раскрыты; ядро actions/submit и остальные вкладки конфигурации внешние/ранее описанные. |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) (src-000591) | Выбранные поля, data-id и controls сопоставлены; локализация/helper internals/браузерный render частичны. |
| [templates/chat/item/consume.hbs](../../../templates/chat/item/consume.hbs) (src-000496) | Контекст сообщения сопоставлен; DOM, localize, ChatMessage rendering/права/хранение не проверялись. |
| [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) (src-000551) | Флаги и add-item раскрыты; все hash-context callers, локализация и браузерное поведение не развёрнуты. |

Смежные: общие поля/вес .012, три модели с consumable(), itemEffect, Alchemical/Valuable/Mutagen sheets, core и дочерние Actor sheets, восемь текущих inventory partial, две вкладки инвентаря, socket sender/receiver и отдельный query addItem. Полные контейнеры, торговля, улучшения, крафт/разборка/ремонт, бой, магия и лечебный цикл не включены.

## Существенные различия

- quantity — строковое поле CommonItemData. addItem выбирает первое name/type, затем проверяет forcecreate/isStored. Совпавший stored Item ведёт к созданию нового, без поиска следующего свободного стека. Числовые преобразования и отсутствие локальной валидации отражены у писателей.
- removeItem ждёт update/delete; removeItemsOfType не ждёт вложенное удаление. useItem и consumeItem запускают consume и списание отдельно без await. Прямой consume не списывает предмет. Ошибка async consume не останавливает внешний вызов removeItem автоматически.
- Общий вес использует calcWeight с isCarried/!isStored и вес валюты. getList имеет отдельную shield ветвь без stored-фильтра. Текущие _prepareWeapons/_prepareArmor работают с context.items напрямую: нельзя переносить на них фильтры getList.
- Drop собственного документа сортирует; legacy fromDropData превращает его в source-копию. Уникальная замена ждёт обёртку; monster equipped меняет prepared, а addItem может читать source. Сброс профессии ожидается, установка флагов и addItem — нет.
- summary показывает hasQuantity-заголовок, реальные input находятся в строках. data-itemType/data-spellType становятся dataset.itemtype/spelltype. subtype summary не передаёт. inline handler не читает data-dtype. У alchemical строки имя не item-roll: её вход расходования — контекстное меню.
- Меню 14.367 поддерживает onClick(event,target) и callback(target,event). consume использует правильный onClick; giftItem ожидает противоположный legacy порядок. Прямой корректный giftItem ждёт prompt, но не подтверждение addItem/списания. Отмена прекращает путь, выбор себя не исключён.
- Подарок не GM использует socket emitForGM → receiver activeGM → Actor.addItem. Query addItem — отдельный API. Успех emit или true query не является подтверждением сохранения Item.
- consume ждёт только calculateHealValue при doesHeal; HP update, статусы, applySelf и сообщение не ожидаются. HP-лимит делегирован helper, duration в applySelf не передаётся. percentage/varEffect не исполняются этой цепочкой. Прежние AE/статусные определения .008 переиспользованы.
- Редактор расходника работает с типизированными массивами properties.effects/removesEffects. В itemEffect нет id, add создаёт только percentage:100: штатный edit падает до update, remove сохраняет строки. on→checked имеет смысл только после обхода этого барьера, как в прежнем изолированном опыте. Ручные row controls не имеют name; их запись выполняют handlers.
- addsTempHp не определено схемой; formGroup пишет диагностику и возвращает пустую разметку. Это не реализованное временное HP и не остановка всего окна. MutagenData имеет consumable поля, но его основной лист использует общую configuration.
- consume.hbs получает item/messageInfos/statusEffects; выводит только добавляемые статусы. Неизвестный statusEffect даёт undefined метаданные; снимаемые статусы не перечисляются.

## Доказательства и issues

Сопоставлены текущие исходники, поздние карточки и R003-12, R006-12/15/16/17, R007-03/04/05/06. Прочитаны связанные issues 00034/00045/00049/00060/00091/00092/00093/00116/00153/00168/00169/00172/00174/00175/00225 с уточнениями. Это ссылки на прежние датированные доказательства; их опыты заново не выполнялись, статусы не менялись. Ограничения ID, несовпадение callback и неподтверждённая доставка представлены отдельными границами.

## Внешние контракты

Прочитаны локальные исходники установленной Foundry 14.367.0. Ядро обозначено внешними границами и не добавляется в каталог 615 исходников.

| Путь ядра | Участок | SHA-256 |
| --- | --- | --- |
| /opt/foundryvtt/client/applications/ux/context-menu.mjs | 611–624: порядок аргументов onClick/callback | 78ca291bf89b79486e45c7adaf8b04ed829d5858912ba0fe6f16946b727e6470 |
| /opt/foundryvtt/common/abstract/data.mjs | 820–827: toObject(source=true) | 11bb7f848c707803607accfa9f6b946c7cbfe8b17781ff562b468bdc77b934e5 |
| /opt/foundryvtt/client/applications/handlebars.mjs | 531–541: formGroup отсутствующего поля | 0c5959e0ebdf5847277fba3284d76ee535084e022d087659fd0791e5ccd3545c |

## Процессы

<a id="proc-000135"></a>

### proc-000135 — Actor: выбрать способ использования Item

Вход useItem(itemId,options); attack/magic делегируются, списание только в consume ветке.

<a id="proc-000136"></a>

### proc-000136 — Actor: объединить стек или создать Item

Вход addItem; сопоставление только по name/type и только первое совпадение.

<a id="proc-000137"></a>

### proc-000137 — Actor: уменьшить стек или удалить последнюю единицу

Вход removeItem(itemId,quantityToRemove); guard отсутствующего Item отсутствует.

<a id="proc-000138"></a>

### proc-000138 — Actor: запустить удаление всех Item типа

Вход removeItemsOfType; завершение async обёртки не означает окончания удаления.

<a id="proc-000139"></a>

### proc-000139 — Actor: получить отсортированный список

Вход getList(name); shield и остальные типы имеют разные фильтры.

<a id="proc-000140"></a>

### proc-000140 — Actor sheet: Drop, уникальность и создание

Вход _onDropItem; ядро Drop остаётся внешним, каждый локальный guard сохранён.

<a id="proc-000141"></a>

### proc-000141 — Инвентарь: кнопка создания Item

click .add-item → dataset → Item.create(parent Actor); subtype из summary не приходит.

<a id="proc-000142"></a>

### proc-000142 — Инвентарь: ручное редактирование поля

change .inline-edit; количество — выбранный конкретный dataset.field.

<a id="proc-000143"></a>

### proc-000143 — Инвентарь: _onItemEquip

Событие строки .item; отсутствующий Item не защищён guard.

<a id="proc-000144"></a>

### proc-000144 — Инвентарь: _onItemCarried

Событие строки .item; отсутствующий Item не защищён guard.

<a id="proc-000145"></a>

### proc-000145 — Инвентарь: _onItemLearned

Событие строки .item; отсутствующий Item не защищён guard.

<a id="proc-000146"></a>

### proc-000146 — Инвентарь: _onItemDelete

Событие строки .item; отсутствующий Item не защищён guard.

<a id="proc-000147"></a>

### proc-000147 — Инвентарь: имя предмета вызывает useItem

click .item-roll или .spell-roll; расходник без такой кнопки имеет отдельное контекстное меню.

<a id="proc-000148"></a>

### proc-000148 — Меню: проверка флага, применение и списание

onClick(event,target) соответствует ядру; visible проверяет флаг и наличие Item, но не quantity.

<a id="proc-000149"></a>

### proc-000149 — Расходник: лечение, статусы, ActiveEffect и сообщение

Прямой Item.consume; здесь нет guards isConsumable/quantity/actor и нет списания.

<a id="proc-000150"></a>

### proc-000150 — Actor: снять перечисленные присутствующие статусы

Вход removeStatus(effects), в том числе из consume; не await реального toggle.

<a id="proc-000151"></a>

### proc-000151 — Расходник: сообщение применения

Вход createConsumeMessage(messageInfos); статусы сообщения — только properties.effects.

<a id="proc-000152"></a>

### proc-000152 — Передача Item при прямом корректном вызове giftItem

Вход giftItem(event,target). Штатный legacy menu передаёт target,event и обычно падает на target.dataset до prompt; этот барьер указан первым.

<a id="proc-000153"></a>

### proc-000153 — Редактор расходника: добавить запись массива

action addEffect; target effects/removesEffects, не ActiveEffect.

<a id="proc-000154"></a>

### proc-000154 — Редактор расходника: поиск записи и изменение

focusout input/input select; штатная схема не содержит id, поэтому update обычно недостижим.

<a id="proc-000155"></a>

### proc-000155 — Редактор расходника: удалить запись массива

action removeEffect; строгий фильтр по id, которого нет в itemEffect.

## Проверки

Пройдены 104 тестовых метода (unittest, 478.882 с), включая 26 новых CLI-случаев; накоплено 247 CLI-примеров. Это проверки справочника, без исполнения игрового сценария.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
git diff --check
~~~

Проверены фактические декларации/владельцы и обращения к полям, guards и ожидания количества/consume, 23 UI-подписки, восемь строк количества, конфигурация и известные барьеры ID/callback. Сверены все связи в обоих направлениях, местоположения, достижимость выходов новых процессов, участие в процессах и три аспекта coverage. Прочитаны три внешних контракта с хешами выше.

Первая структурная проверка выявила два локальных boundary без owner: им задан файловый владелец. При сверке адресов поправлены имена исходных обработчиков и строки присваиваний itemData. Ожидания привязаны к реальным foundItem/newQuantity, а не условным именам описания. Текущий результат проверен после этих уточнений. Первый общий прогон (104 теста, 474.364 с) выявил одно устаревшее ожидание .008: список процессов Actor был ограничен тремя прежними ID. Историческая тройка сохранена отдельной проверкой, шесть новых процессов Actor проверяются в .013. Количественный итог .012 также проверяется по историческим частям; прежние семантические тесты продолжают работать с накопленным графом. Формат v1 и query.py не менялись.

## Матрица справочных запросов

| Запрос | Примеры | Независимый ориентир |
| --- | --- | --- |
| IQ-01 | INV-01 | quantity — StringField CommonItemData |
| IQ-02 | INV-02/26 | Прежний ID consume и отдельный UI-флаг hasQuantity |
| IQ-03 | INV-03/25 | EmbeddedDataField и наследование конфигурации |
| IQ-04 | INV-08/09/16/23 | Четыре поля веса, useItem, вызовы consume, два маршрута подарка |
| IQ-05 | INV-04/10/24 | Три потребителя фабрики, два caller consume, receiver addItem |
| IQ-06 | INV-05/06/07/17 | Писатели quantity и HP; consume не пишет количество |
| IQ-07 | INV-11–15/20/21 | Guards, создание/удаление, Drop, ожидания и ошибки редактора/меню |
| IQ-08 | INV-18/19/22 | Отсутствующие id/addsTempHp и отдельные issues передачи |

[26 примеров](examples/expansion-013-queries.json), [тесты](tests/test_expansion_013.py). Актуальность после наполнения: valid/current, 615 исходников, реестр, 690 документов и package Foundry 14.367.0. Окончательная проверка ссылок и сохранности фиксируется в [журнале](review-log.md#task-0006013).

## Итог и следующая порция

Добавлены 142 сущности, 552 отношения и 21 процесс. 3696 сущностей, 8459 связей и 155 процессов (578 шагов, 957 переходов). Определения есть в 197/615 файлах: два словаря complete по строковым ключам, 195 файлов partial; роли 74 основных/123 смежных, 418 без определений.

TASK-0006.013 done; следующая — [TASK-0006.014](../../tasks/task-0006.014.md), настройки оружия, атаки, защиты и свойств урона. Родитель TASK-0006 остаётся in-progress. Полный граф пока не заявлен; отсутствующие результаты поиска в partial области не доказывают отсутствия зависимости. Браузер, игровой мир, сохранение документов и передача между клиентами этим прогоном не подтверждаются.
