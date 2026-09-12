# module/setup/queries.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/setup/queries.js](../../../../../../module/setup/queries.js) |
| Тип файла | JavaScript — запросы между клиентами |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../../../tasks/task-0002-system-initialization.md); порция 4 |
| Запись перекрёстной сверки | [Журнал сверок](../../../review-log.md) — TASK-0002, порция 4 |

## Назначение файла

Регистрирует два запроса Foundry User.query для эффектов и разрешённых методов документов.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) вызывает registerQueries в init. Сам импорт только определяет константу и функции. Нужен CONFIG.queries; последующие запросы используют Foundry User.query. Этот файл не выбирает пользователя-получателя — это делают отправители.

## Введённые сущности и действия с ними

| Сущность | Доступность | Назначение |
| --- | --- | --- |
| system | Локальная const, стр. 7 | Namespace TheWitcherTRPG |
| applyTemporaryItemImprovementsToActor | Локальная async function, стр. 9 | Обработчик TheWitcherTRPG.applyTemporaryItemImprovements |
| query | Локальная async function, стр. 15 | Обработчик TheWitcherTRPG.query |
| callableFunctions | Локальный объект при каждом query | Три импортированные функции эффектов |
| callableEntityFunctions | Локальный массив при каждом query | Пять имён разрешённых методов |
| registerQueries | Экспорт, стр. 48 | Присваивает два обработчика в CONFIG.queries |

## Основные функции и методы

| Функция | Входы | Результат / действия |
| --- | --- | --- |
| registerQueries() | Нет | undefined; две записи в реестр |
| applyTemporaryItemImprovementsToActor(queryData, {timeout}) | actorUuid, effects; объект options обязателен для деструктуризации | Promise<true>; fromUuidSync → actor.applyTemporaryItemImprovements(effects), без await и проверки actor; timeout не используется |
| query(queryData, {timeout}) | function, data (итерируемые аргументы), uuid для метода документа | Promise<true/false>; сначала таблица функций через in, затем массив методов; unknown → false. timeout не используется |

Три функции: applyStatusEffectToActor, applyActiveEffectToActor, applyActiveEffectToActorViaId. Для них data раскрывается в аргументы. Пять методов: addItem, applyTemporaryItemImprovements, addAdrenaline, restoreReliability, addBehaviorsToRegionUuids. Для них UUID разрешается синхронно, затем вызываются entity[name]?.(...data) и entity.system[name]?.(...data). Это два независимых вызова, не выбор первого подходящего. entity и entity.system сами не защищены optional chaining. Проверки прав, типа документа, формы data и вложенного regionProperties здесь нет. Возврат true не ожидает асинхронный результат.

## Используемые сущности и зависимости

| Сущность | Источник | Связь | Определение / использование |
| --- | --- | --- | --- |
| applyActiveEffectToActor / applyActiveEffectToActorViaId | [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | Именованные импорты / таблица вызовов | Определения стр. 32/14; применение эффектов Actor либо выбор по Item и applyWhen |
| applyStatusEffectToActor | [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | Именованный импорт / таблица вызовов | Стр. 43; UUID Actor, statusEffectId, duration |
| addItem | [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js) | Метод по UUID | Стр. 259; количество/создание Item |
| applyTemporaryItemImprovements | [module/actor/mixins/temporaryEffectMixin.js](../../../../../../module/actor/mixins/temporaryEffectMixin.js) | Метод по UUID / специальный запрос | Стр. 4; примесь WitcherActor.prototype, подключена в witcherActor.js:448 |
| addAdrenaline | [module/actor/mixins/adrenalineMixin.js](../../../../../../module/actor/mixins/adrenalineMixin.js) | Метод по UUID | Стр. 2; подключён в witcherActor.js:453 |
| restoreReliability | [module/item/mixins/repairMixin.js](../../../../../../module/item/mixins/repairMixin.js) | Метод по UUID | Стр. 8; подключён WitcherItem.prototype в [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js) (373) |
| addBehaviorsToRegionUuids | [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../module/data/item/templates/regions/regionPropertiesData.js) | Предполагаемая цель маршрута, несоответствие | Стр. 12: реально вложен в system.regionProperties; заданная маршрутизация туда не доходит |
| CONFIG.queries / fromUuidSync / User.query | Foundry 14.367.0 | Реестр и внешний API | Локальный первичный источник User.query: /opt/foundryvtt/client/documents/user.mjs:283–321; результат возвращается вызывающему клиенту |

## Известные потребители

| Файл | Запрос / условия | Основание |
| --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) | registerQueries в init | стр. 23/49 |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | query для эффектов и отдельный applyTemporaryItemImprovements; выбор активного GM/владельца | стр. 18, 41, 72 |
| [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js) | query applyStatusEffectToActor владельцу Actor | стр. 49 |
| [module/actor/mixins/defenseMixin.js](../../../../../../module/actor/mixins/defenseMixin.js) | query addAdrenaline владельцу атакующего Actor | стр. 213 |
| [module/actor/mixins/professionMixin.js](../../../../../../module/actor/mixins/professionMixin.js) | query applyActiveEffectToActor владельцу цели | стр. 315 |
| [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../module/data/item/templates/regions/regionPropertiesData.js) | query addBehaviorsToRegionUuids активному GM | стр. 19 |
| [module/data/item/mixin/spellRegionMixin.js](../../../../../../module/data/item/mixin/spellRegionMixin.js) | Попытка query deleteSpellVisualEffect, маршрута нет | стр. 161; до отправки возможен ReferenceError |

Поиск по module: буквальные имена обоих запросов и function; внешние макросы/модули не проверялись.

## Данные и изменения состояния

Регистрация меняет только CONFIG.queries. При обработке косвенно возможны создание ActiveEffect/Item, улучшения оружия, изменение адреналина и надёжности. Конкретная запись определяется методом-целью; true сам по себе не подтверждает запись. data здесь явно не копируется.

## Проверки и доказательства

Полный файл (51 строка), все три импортированные функции и определения пяти предполагаемых методов проверены; сопоставлены семь файлов вызывающих сторон. Настоящие обработчики выполнены в vm: addItem и улучшение вернули true при незавершённом Promise; вложенный метод региона не вызван при true; deleteSpellVisualEffect и unknown дали false; constructor дал true через in. Цели и Foundry заменены минимальными объектами.

## Непроверенные участки и открытые вопросы

Сетевой обмен и фактические разрешения User.query не тестировались. Подтверждена маршрутизация в изоляции, не успешность игровых действий. Источники эффектов/моделей проверены только в пределах связей. Фактический контракт true требует отдельного решения.

## Связанные проблемы

[issue-00008](../../../../../issues/potential/issue-00008.md) — преждевременное/пустое подтверждение; [issue-00009](../../../../../issues/potential/issue-00009.md) — маршруты операций регионов.

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 4 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. Прослежены цели Actor whitelist: собственный addItem, temporaryEffectMixin.applyTemporaryItemImprovements и adrenalineMixin.addAdrenaline. AddItem в изолированном выполнении действительно ждёт update/create; query не связывает свой ответ с этим Promise (issue-00008). Полный сетевой маршрут не запускался.

Карточки: [WitcherActor](../actor/witcherActor.js.md), [modifierMixin](../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../review-log.md#task-0003007).

## Уточнение TASK-0003.008

2026-09-10, `c5edcbadd05ff4038a174bd2e2a49785e40ea878`; исходник не изменился относительно исходного среза. Whitelist restoreReliability разрешает вызов метода, присоединённого WitcherItem через repairMixin. Он делегирует RepairSystem.restoreReliability(this). Маршрутизатор пробует entity[function] и entity.system[function] отдельно и не ожидает их; realCraft/checkIfItemHasRollTable в whitelist отсутствуют. Результаты текущего разбора дополняют issue-00008, но не означают выполнения сетевого запроса.

Связанные карточки: [CommonItemData](../data/item/commonItemData.js.md) и [WitcherItem](../item/witcherItem.js.md). [Перекрёстная сверка](../../../review-log.md#task-0003008). Новая запись уточняет связи; исторические результаты прежних порций сохранены.

## Уточнение TASK-0003.009

2026-09-10, `a33bf33add228ae93f96a52046c8feb4ee992921`. Исходник не изменился относительно указанного ранее среза.

Полный разбор отправителей [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) и [module/scripts/statusEffects/applyStatusEffect.js](../../../../../../module/scripts/statusEffects/applyStatusEffect.js) уточнил контракт: обычный owned-маршрут ждёт createEmbeddedDocuments, но ViaId, ToTargets, обработчик временных улучшений и принимающие Queries не связывают свой результат с завершением вложенной операции (issue-00008). Не-владелец посылает отдельный query улучшений со всем списком и общий query обычных эффектов без отдельного duration. При Item, недоступном даже GM, ViaId повторяет тот же запрос без конечной ветви (issue-00045). Три ручных исполнения и наблюдаемые payload не являются запуском сетевого цикла.

[Журнал сверки](../../../review-log.md) — TASK-0003.009; ограничения изолированного выполнения и неподтверждённые проблемы сохранены.

## Уточнение TASK-0003.017

2026-09-10, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; исходники неизменны. [Сверка](../../../review-log.md#task-0003017).

Уточнён разрешённый restoreReliability: [примесь Item](../../../../../../module/item/mixins/repairMixin.js) делегирует [RepairSystem.restoreReliability](../../../../../../module/item/systems/repair.js) и system.repair без ожидания. Однако штатный _doRepair использует emitForGM/socket, не User.query; проверка receiver этой порции не является новым воспроизведением раннего true из [issue-00008](../../../../../issues/potential/issue-00008.md). Контракты двух протоколов остаются раздельными.

## Уточнение TASK-0003.022

2026-09-11, `ef8117ba6e5a184989e65761d47a068381056e4a`; исходник не изменён.

Повторена маршрутизация на настоящей Item-модели с RegionProperties: function addBehaviorsToRegionUuids возвращает true без вызова вложенного метода, так как проверяются только entity/entity.system. deleteSpellVisualEffect отсутствует в allowlist, а player-отправитель сначала падает на item. Даже прямые региональные адаптеры не ожидают записи, что отдельно описано в issue142; ответ true не подтверждает выполнение.

Связанные карточки: [module/data/item/templates/regions/regionPropertiesData.js](../data/item/templates/regions/regionPropertiesData.js.md), [module/data/item/mixin/spellRegionMixin.js](../data/item/mixin/spellRegionMixin.js.md).

[Результаты и пределы сверки](../../../review-log.md#task-0003022).

## Уточнение TASK-0003.028

2026-09-11, `9f16a7ae4bc942df85a105fd37d9a3cb3ef99f4b`: getActorOwner из helper не является подтверждением запроса: он только возвращает активного не-GM OWNER либо activeGM. Без обоих некоторые потребители обращаются к null.query до входа в этот маршрутизатор ([issue-00185](../../../../../issues/potential/issue-00185.md)). [issue-00008](../../../../../issues/potential/issue-00008.md) о return true без ожидания вызванной функции относится к следующему этапу процесса и остаётся актуальным; сам query в .028 повторно не исполнялся.

Полные карточки зависимости: [module/scripts/helper.js](../scripts/helper.js.md). [Перекрёстная сверка](../../../review-log.md#task-0003028). Это уточнение связи; исходный файл не изменён.

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. Разрешённый динамический addAdrenaline теперь разобран: optional=false не пишет, true запускает Actor.update и сразу завершает собственный Promise. Query тоже не ожидает entity[function]; полное завершение записи отсутствует на обоих уровнях. Потребитель defenseMixin выбирает владельца атакующего при crit; сетевой сценарий не запускался.

Сверенные источники: [module/actor/mixins/adrenalineMixin.js](../../../../../../module/actor/mixins/adrenalineMixin.js); [module/actor/mixins/defenseMixin.js](../../../../../../module/actor/mixins/defenseMixin.js). [Итоговая сверка третьей серии, сценарии и ограничения](../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Полный профессиональный producer вызывает getActorOwner(target).query("TheWitcherTRPG.query",{function:"applyActiveEffectToActor",data:[target.uuid,[newEffect]]}) без await. Whitelist query вызывает handler безожидания; ответ true не означает persisted effect(8). В HP caller есть ещё потеря Promise(241).

[module/actor/mixins/professionMixin.js](../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.

## Дополнительная сверка TASK-0003.042

2026-09-12, rusbar-main, 16695cbfc7fec3e0de56660c7cab21bc0304e94b; исходники не изменены.

[skillDefense](../actor/mixins/defenseMixin.js.md) отправляет {uuid:attacker,function:'addAdrenaline',data:[]} на TheWitcherTRPG.query при крите. Имя присутствует в callableEntityFunctions; принимающий handler не исполнялся в этой порции. Отправитель не ждёт query (273), отсутствие владельца — 185; прежние ограничения исполнения query из issue-00008 сохраняются.

[Сверка и ограничения](../../../review-log.md#task-0003042). Уточнение связей не увеличивает покрытие. Код и статусы issues не исправлялись; подтверждение пользователя не получено.
