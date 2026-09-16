# module/item/mixins/consumeMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

Актуализация [issue-00001](../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

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

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-02](../../../../cross-check-0002.md#u007-02), [U007-04](../../../../cross-check-0002.md#u007-04), [U007-07](../../../../cross-check-0002.md#u007-07). Для этого файла установлены процессы R007-04, R007-05, R007-06, а не полный клиентский lifecycle.

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

## Уточнение TASK-0003.026

2026-09-11, `rusbar-main`, `45a63062a2bd55939fef430609fc5dddc350b0e9`. Полностью разобран caller itemContextMenu.consumeItem: после isConsumable запускает consume и removeItem(id,1) без ожидания. Группа 17 проверила quantity2→update1 и quantity1/0→delete; consume в этой группе заменён pending Promise. Прежний сценарий удаления последнего источника до применения UUID из .015 остаётся отдельным доказательством issue-00034/00045. Нарушение запрета нулевого количества зарегистрировано как potential issue-00174.

Определения: [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) и [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003026). Полный разбор новых соседних файлов вне порции не засчитывается.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Consume ждёт только расчёт лечения; parseInt, HP cap, toggles статусов, applySelf и чат имеют разные ветви и ожидания. Сам метод не проверяет actor/флаг/запас. Списывают внешние callers без ожидания consume; последний Item может исчезнуть до UUID-копирования AE. Percentage/varEffect и снятые статусы в сообщении не обрабатываются.

Сопоставленные определения и потребители: [module/scripts/temporaryEffects/applyActiveEffect.js](../../scripts/temporaryEffects/applyActiveEffect.js.md), [module/actor/mixins/healMixin.js](../../actor/mixins/healMixin.js.md), [module/actor/witcherActor.js](../../actor/witcherActor.js.md), [module/data/item/templates/consumePropertiesData.js](../../data/item/templates/consumePropertiesData.js.md), [module/setup/config.js](../../setup/config.js.md), [templates/chat/item/consume.hbs](../../../templates/chat/item/consume.hbs.md), [module/item/witcherItem.js](../witcherItem.js.md), [module/actor/sheets/interactions/itemContextMenu.js](../../actor/sheets/interactions/itemContextMenu.js.md).

[Протокол и границы](../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-04](../../../../cross-check-0002.md#r007-04), [R007-05](../../../../cross-check-0002.md#r007-05), [R007-06](../../../../cross-check-0002.md#r007-06). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
