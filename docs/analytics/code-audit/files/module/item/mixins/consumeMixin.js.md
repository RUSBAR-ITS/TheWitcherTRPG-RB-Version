# module/item/mixins/consumeMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

## Назначение файла

Добавляет WitcherItem применение расходуемого предмета: лечение владельца, добавление/снятие статусов, перенос applySelf ActiveEffect и сообщение в чат.

## Условия использования

witcherItem.js импортирует consumeMixin и выполняет Object.assign(WitcherItem.prototype, consumeMixin). Основные вызовы — Actor.useItem и itemContextMenu.consumeItem. Они проверяют isConsumable и отдельно вызывают Actor.removeItem(item.id,1); сам consume этого не делает. Ожидается Item, принадлежащий Actor.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| consumeMixin | named export let, объект | Два метода Item | Object.assign в witcherItem.js | Вызов по действию пользователя |
| properties; messageInfos; heal | Локальные данные consume | Настройки и рассчитанное число лечения | Внутри метода | Передаются в update и чат |
| messageTemplate; statusEffects; content; chatData | Локальные данные createConsumeMessage | Путь HBS, разрешённые статусы, HTML и данные ChatMessage | Внутри метода | Подготовка сообщения |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async consume() | this.system.consumeProperties; this.actor; this.uuid | Promise<void>, завершение не означает окончания записей | Если doesHeal: await calculateHealValue, parseInt, запрос HP update; applyStatus; removeStatus; applyActiveEffectToActorViaId(actor.uuid,item.uuid,'applySelf'); createConsumeMessage | Ожидает только calculateHealValue; остальные операции не await/return; без Actor бросает TypeError; flag/quantity не проверяет |
| async createConsumeMessage(messageInfos) | effects массив, CONFIG.WITCHER.statusEffects; Actor для speaker | Promise<void> | map: {name,statusEffect:find(id)}; await renderTemplate; ChatMessage.getSpeaker; style OTHER; ChatMessage.create | create не await/return; неизвестный/пустой ID даёт undefined metadata, не отфильтровывается |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| applyActiveEffectToActorViaId | [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | Прямой импорт / вызов | Передаёт UUID владельца/предмета и applySelf; duration не передаётся | Определение и обращение сверены |
| calculateHealValue | [module/actor/mixins/healMixin.js](../../../../../../../module/actor/mixins/healMixin.js) | Динамический метод Actor / примесь | Текст heal; положительное лечение ограничивается hp.max до parseInt | Определение и обращение сверены |
| applyStatus / removeStatus; useItem / removeItem | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Динамические методы Actor / обратный маршрут | Статусы; расход количества вынесен во входной маршрут | Определение и обращение сверены |
| consumeProperties | [module/data/item/templates/consumePropertiesData.js](../../../../../../../module/data/item/templates/consumePropertiesData.js) | Контракт модели | doesHeal/heal/effects/removesEffects | Определение и обращение сверены |
| CONFIG.WITCHER.statusEffects | [module/setup/config.js](../../../../../../../module/setup/config.js) | Динамическая конфигурация | Разрешение id для представления | Определение и обращение сверены |
| Шаблон consume | [templates/chat/item/consume.hbs](../../../../../../../templates/chat/item/consume.hbs) | renderTemplate | {item:this,messageInfos,statusEffects} | Определение и обращение сверены |
| renderTemplate / ChatMessage / CONST.CHAT_MESSAGE_STYLES | Foundry API | Внешний API | HTML, speaker, создание сообщения | Определение и обращение сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | consumeMixin | Импорт и Object.assign | Примесь WitcherItem |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Item.consume() | useItem после проверки типа и isConsumable | Рядом отдельный removeItem |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Item.consume() | consumeItem для flagged Item | Рядом отдельный removeItem |
| [templates/chat/item/consume.hbs](../../../../../../../templates/chat/item/consume.hbs) | messageInfos; statusEffects; item | Рендер сообщения | Параметры вызова renderTemplate |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

consume запрашивает изменение system.derivedStats.hp.value, Actor-статусов и ActiveEffect, но не меняет system.quantity, time или toxicity предмета и токсичность Actor. applyStatus/removeStatus фильтруют по statusEffect и вызывают toggleStatusEffect; percentage/varEffect не учитываются. Ветка иммунитетов applyStatus содержит ранее зарегистрированный statusEffectId (issue-00031). Список обычных статусов и Item.effects — разные механизмы. Helper отбирает Item.effects по system.applySelf; дальнейшее копирование на Actor сбрасывает флаги применения. В тесте один applySelf эффект передан в createEmbeddedDocuments, второй отфильтрован; заданная duration.value=3 сохранилась, текст time не использован.

При задержанном calculateHealValue и quantity=1 реальный Actor.useItem запускает consume, затем removeItem. В контролируемом порядке delete удалил источник из UUID-фасада до продолжения consume; helper запросил активного GM вместо создания эффектов локально. Это воспроизведение возможного порядка, не измерение частоты сбоя в мире. Чат может создаваться до окончания HP/status/effect/update/delete. Отсутствие Actor не обработано: даже optional chaining у update следует после обращения this.actor.calculateHealValue.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Лечение/статусы/ActiveEffect | Настоящие consume, healMixin, методы Actor и applyActiveEffect helper; настоящие BaseActiveEffect | HP8/10+5→запрос10; fire percentage=0 всё равно toggle; poison снимается; передан только ApplySelf; quantity2 остаётся2 | update/toggle/createEmbeddedDocuments — pending фасады |
| Границы Promise | Незавершённые записи/ChatMessage.create | consume завершается; сообщение сформировано, хотя записи не завершены | Отказы/сеть не исполнялись |
| Входы/количество | Настоящие useItem, removeItem и context menu | flag=false блокирует входы; прямой consume(false) выполняется; menu quantity2→update1; последняя единица с задержкой лечения удаляется до UUID-поиска | Удаление и query перехвачены |
| Отсутствие Actor / чат | Item.actor=null; четыре массива для сообщения | TypeError calculateHealValue или applyStatus; [] без картинок, name-only/unknown с src='', fire с иконкой | Полный клиент и доставка чата не проверялись |

## Непроверенные участки и открытые вопросы

Реальный код и Foundry 14.367.0 исполнялись в изолированном Node 24.16.0, без DB/мира. Actor — DataModel-фасад, Item/DOM/UUID/GM query/чат и операции записи подменены. Не проверялись Roll с кубиками, серверная валидация HP для пустого/невалидного heal, конкурентное лечение, повторные клики и реальная сеть. Правила токсичности, длительности и мутаций не выводятся из отсутствующих ветвей. Связь с issue-00049 установлена по вызову toggleStatusEffect без active:true; выключенный статус этим сценарием повторно не исполнялся.

## Связанные проблемы

[issue-00008](../../../../../../issues/potential/issue-00008.md), [issue-00031](../../../../../../issues/potential/issue-00031.md), [issue-00034](../../../../../../issues/potential/issue-00034.md), [issue-00045](../../../../../../issues/potential/issue-00045.md), [issue-00049](../../../../../../issues/potential/issue-00049.md). Уточнены существующие границы статусов, Promise и UUID-поиска; отдельных дубликатов нет.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.020

2026-09-11, `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008`; проверены связи с критическими травмами, лечением и отдыхом. Полный первоначальный разбор и его ограничения сохранены.

| Связь | Файл | Результат проверки |
| --- | --- | --- |
| calculateHealValue | [module/actor/mixins/healMixin.js](../../../../../../../module/actor/mixins/healMixin.js) | Полностью разобран: только строки с 'd' идут в Roll; обычная строка возвращается без вычисления, если не переполняет HP. consume далее применяет parseInt. Для '2+3' это 2; допустимость такого ввода требует уточнения контракта, новых правил не выбрано. |
| heal/treat критической травмы | [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) | consume не вызывает их: расходование восстанавливает HP/статусы/effects, дневное заживление — отдельная примесь листа. |

[Сверка порции и итоговая сверка 96 файлов второй серии](../../../../review-log.md#task-0003020); браузер, мир и записи в БД не запускались.
