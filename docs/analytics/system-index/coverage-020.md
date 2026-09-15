# TASK-0006.020 — Действия чата, GM-доставка и начало хода

2026-09-15; rusbar-main, исходный HEAD `e41ef6627b63a4ba024cc221fd6d2b7e07976148`; рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.020.md).

## Область и остаток

Восемь основных исходников и выбранные смежные участки. Схема v1/CLI сохранены, весь индекс partial. Здесь зафиксирован текущий код, а не подтверждённое выполнение игрового сценария.

| Источник | Включено и границы |
| --- | --- |
| [module/scripts/combat/combat.js](../../../module/scripts/combat/combat.js) (src-000195) | Все функции/listeners/menu и отдельные callbacks; stun/crit proc208–210 переиспользованы. Получатели damage/defense .015/.016/.019; полные травмы .021. Старый bulk helper не имеет найденного штатного caller. |
| [module/scripts/chat.js](../../../module/scripts/chat.js) (src-000193) | Общий listener, полный onShield и вход onRepairRequest; onHeal только адрес .022. Ремонт B09 не раскрыт целиком. |
| [module/setup/queries.js](../../../module/setup/queries.js) (src-000213) | Оба handler и регистрация прочитаны полностью, процессы045/046 сохранены с новыми связями. Выбранные методы entity адресованы; весь региональный lifecycle/permissions/доставка вне области. |
| [module/scripts/socket/socketMessage.js](../../../module/scripts/socket/socketMessage.js) (src-000204) | Полный envelope/emitForGM, три guard и отсутствие acknowledgement; серверный relay и несколько клиентов не исполнялись. |
| [module/setup/socketHook.js](../../../module/setup/socketHook.js) (src-000217) | Полная регистрация/callback: activeGM, мутация data.shift, два UUID типа и unchecked fallback. Ready barrier .006 сохранён. |
| [module/scripts/combat/generalCombatHook.js](../../../module/scripts/combat/generalCombatHook.js) (src-000196) | General, периодический цикл, damage/message ветка полностью. Regeneration — адрес, heal — handoff в .022; wrapper не гарантирует завершения нижнего damage. |
| [module/data/actor/templates/common/combatEffectsData.js](../../../module/data/actor/templates/common/combatEffectsData.js) (src-000074) | Вся фабрика прочитана; поля turnStartEffects и выбранные consumers. Остальные эффекты и все возможные producers не объявлены покрытыми. |
| [templates/chat/combat/statusEffect.hbs](../../../templates/chat/combat/statusEffect.hbs) (src-000488) | Весь короткий шаблон: прямой status, img/localize name/applyCombat; живой рендер не исполнялся. |

## Контракты и маршруты

- module/TheWitcherTRPG.js:52–58 регистрирует renderChatMessageHTML и вызывает пять групп listeners без await. 136–141 добавляют контекстные действия; init:49 регистрирует queries. Ready:90 подключает socket после прежнего pack.getIndex barrier. Наличие определения callback не означает исполнение до клика.
- Attack listener берёт первую button.damage; onDamage получает Item по message.system.attack.itemUuid и передаёт ту же prepared message.system.damage в rollDamage без guard/await. Actor текущего пользователя здесь не выбирается. Старый addAttackChatListeners использует jQuery each и передаёт jQuery в querySelector; штатные callers в module/templates не найдены.
- Defense listener подписывает все stun/crit-stun. Их прежние proc-000208/209 ждут getInteractActor, но не stunSave. Меню защиты читает li.dataset.messageId в visible; onClick получает target.dataset.messageId, затем executeDefense передаёт пять prepared полей сообщения в prepareAndExecuteDefense. Guard Actor есть только внутри executeDefense, guard message отсутствует.
- Три crit пункта proc-000210 независимы: applyCritDamage, applyBonusCritDamage, applyCritWound получают message.system.crit. .crit-taken является маркером доступности, получатель заново выбирается getInteractActor, не по defenderUUID. Полные receiver и состояние травм закреплены за .021.
- getInteractActor сначала берёт controlled token, затем character; иначе выбор среди owned Actors с hasPlayerOwner. Ноль кандидатов/отмена диалога не превращаются в гарантированного Actor. Процессы выбора .016 переиспользованы. Другой helper getActorOwner предпочитает активного владельца non-GM, затем GM; его выбор не равен activeGM системного сокета.
- Общий chatMessageListeners подписывает только первые shield/heal/request-repair, не проверяет type/fumble и не использует message. Щит читает currentTarget.getAttribute: строка data-shield и UUID data-actor. actor?.update защищает только вызов update; actor.name ниже не защищён. Формула строки не вычисляется; update/create запускаются без await, applyMode здесь нет. Полный onHeal — .022.
- Repair request читает event.target.dataset.owner/item как локальные ID, после выбора исполнителя. owner.items читается до guard owner. Только затем actor&&owner&&item → await RepairSystem.processRequest. Прочитан выбранный processRequest и границы _doRepair/restoreReliability; full B09 и все стадии ремонта не покрыты.
- CONFIG.queries содержит два имени, не совпадающих с socket type. Общий query: обычный объект трёх callableFunctions проверяется через in; пять entity-имён — массив includes. UUID разрешается синхронно, затем независимо пробуются entity[function] и entity.system[function]. Оба вызова без await; true возможно даже при отсутствии обоих optional методов. entity/system сами не защищены от отсутствия; неизвестное имя возвращает false. Параметр timeout в обоих handlers не используется.
- Отдельный query улучшений читает actorUuid/effects, вызывает Actor.applyTemporaryItemImprovements без await и возвращает true. User.query ядра ожидает ответ удалённого handler, но это не добавляет ожидание дочернего метода. Процессы045/046 сохранены по ID/шагам/переходам и дополнены свидетельствами. Существующие AE/status senders .008 и defense.addAdrenaline переиспользованы.
- addItem и restoreReliability имеют реальные Item gift/repair socket senders; из этого не следует общий сетевой путь damage/defense. Вложенный addBehaviorsToRegionUuids находится в item.system.regionProperties: query не обходит этот уровень. Смежный deleteSpellVisualEffect использует необъявленный item до отправки и имя вне whitelist; фиктивный успешный вызов/полный region lifecycle не добавлены.
- emitForGM: ранний return без socket/user/users; текущему GM — ошибка/return; без activeGM — ошибка/return. Envelope новый, data остаётся ссылкой. await game.socket.emit передаёт только envelope, без callback acknowledgement. Прочитанный Socket.IO возвращает сам Socket; ожидание этого значения не подтверждает выполнение на GM.
- Receiver подписывается только при socket/user и обрабатывает сообщение лишь при user===users.activeGM. restoreReliability/addItem используют data.shift (мутация), fromUuidSync и прямой метод без await. Иной type попадает в непроверенный lookup-вызов. Форма message/data, UUID/метод и собственность ключа не валидируются; generic fallback не назван строгим whitelist.
- updateCombat callback принимает четыре аргумента, combatHooks передаёт General именно Combat. Нет фильтра смены хода и guard текущего combatant/Actor. isActiveGM проверяет идентичность user активному GM. Затем regeneration и periodic запускаются без await; полный countdownRegions остаётся прежней границей, а regeneration — .022.
- applyCombatEffects перебирает Object.values prepared turnStartEffects, не actor.statuses. Каждая запись ожидает локальный applyCombatEffect; пустая карта не производит урон. Ранее исследованный SchemaField ADD может не заполнить карту; внешнее чтение _applyChangeAdd подтверждает возврат исходного value, не готовое состояние конкретного Actor.
- applyCombatEffect сначала проверяет truthy amount (без modifier), ждёт render statusEffect.hbs(status), затем запускает ChatMessage.create без await. damage требует amount>0; итог amount+(modifier??0) может быть неположительным. Plain payload содержит effects[], torso, оба bypassArmor из ignoreArmor и bypassShield, но не type. nonLethal выбирает sta, иначе hp. Await applyDamageFromStatus не включает его Actor.applyDamage (.019).
- Heal следует самостоятельной ветвью после damage: amount>0, calculateHealValue(amount), положительный результат → await update/сообщение. Это точный handoff .022; heal.modifier объявлен, выбранный consumer его не читает. Никакой очереди завершённых записей damage/heal этим индексом не доказано.
- statusEffect.hbs получает status без wrapper: img и localize name, статическая строка applyCombat. Шаблон не содержит кнопок применения. Динамический name не превращён в выдуманный перечень локализаций; literal keys привязаны к прежним en/ru определениям.

## Доказательства и ограничения

Прочитаны восемь основных исходников целиком и их поздние карточки TASK-0004.002/.003/.005/.011; группы R002-09/10/11 и R011-06/09/20/22/23. Из соседей прочитаны регистрации entry/hooks, helper выбора/владельца, выбранные AE/status senders, defense:207–224, gift:114–150, repairMixin и выбранные Repair methods, RegionProperties:1–55, spellRegionMixin:154–171, кнопки spellItem:42–67/repair:66–73 и config:2065–2108. Остальные прежние источники/получатели переиспользованы в уже проверенных пределах.
Полные связанные issues прочитаны: 00002/00006/00008/00009/00010/00021/00022/00045/00108/00149/00169/00185/00239/00249/00253/00255/00258/00291/00299/00328. Их прежние даты, воспроизведения и ограничения сохраняются; статусы не менялись, новых карточек и исправлений нет. Чтение старого опыта не названо новым запуском.
Дополнительно прочитаны следующие внешние участки установленного ядра14/Socket.IO. SHA256 относится к целому файлу, область чтения — только указанным строкам. Это внешние доказательства, не новые системные sources и не исполнение кода.

| Файл вне репозитория | Прочитанные строки | SHA256 |
| --- | --- | --- |
| `/opt/foundryvtt/client/documents/user.mjs` | 86–88; 289–321 | `43e0837d478838959c8676a319ce4af44196bc1e7fc0ae98e8c4f2976aab9682` |
| `/opt/foundryvtt/client/documents/chat-message.mjs` | 394–410; 437–457 | `446c041c59b3f097e5c3358a528181e368e072be9cfe55fa928fa92932e55c5b` |
| `/opt/foundryvtt/client/applications/ux/context-menu.mjs` | 611–625 | `78ca291bf89b79486e45c7adaf8b04ed829d5858912ba0fe6f16946b727e6470` |
| `/opt/foundryvtt/client/applications/sidebar/tabs/chat.mjs` | 398–404 | `d05316c465d0ff93504bf2d9101784680e5e349bed5108e7dc2453751dd84736` |
| `/opt/foundryvtt/client/applications/api/application.mjs` | 2230–2246 | `b5aef80d3e042a4a856be9dd875c72a5224988d62046ba770f25376f4291faa0` |
| `/opt/foundryvtt/node_modules/socket.io-client/build/esm/socket.js` | 238–275 | `35c27b8a59101c99cc7175ac09a7bde85145f4999417a97660e5415b07b7e6bd` |
| `/opt/foundryvtt/common/data/fields.mjs` | 1390–1392 | `efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01` |

ChatMessage передаёт в render hook HTMLElement; _createContextMenu устанавливает jQuery:false, ContextMenu вызывает onClick(event,target), legacy callback остаётся отдельной ветвью. User.query ожидает протокольный ответ, Socket.emit без callback — нет. Ядро/permissions/сеть/смена GM, сохранение документа, живой DOM, несколько клиентов и завершённый бой не проверялись. Ни код движка, ни игровые данные не изменены.

## Процессы

<a id="proc-000045"></a>

### proc-000045 — Общий query: whitelist и запуск обработчика

Объявленные whitelist выбранного участка; in также видит наследуемые свойства обычного объекта. Для них цель оставлена за границей. Вызов не ожидается. Entity/system пути generic оставлены динамическими, timeout здесь не используется.

<a id="proc-000046"></a>

### proc-000046 — Специализированный query: передача улучшения Actor

Нет guard UUID и ожидания Actor-метода; return true не означает завершённый выбор оружия/запись.

<a id="proc-000292"></a>

### proc-000292 — Чат: старый массовый helper

Явный вызов addAttackChatListeners(html); штатный caller не найден.

<a id="proc-000293"></a>

### proc-000293 — Чат: callback старого обхода

Каждый найденный .chat-message; несовпадение jQuery/HTMLElement не обходится.

<a id="proc-000294"></a>

### proc-000294 — Чат: регистрация кнопки урона

renderChatMessageHTML → attackChatMessageListeners(message,html); callback отложен до click.

<a id="proc-000295"></a>

### proc-000295 — Чат: Item для броска урона

click button.damage; Actor пользователя здесь не выбирается.

<a id="proc-000296"></a>

### proc-000296 — Чат: регистрация stun и crit-stun

renderChatMessageHTML → defenseChatMessageListeners; callbacks proc-000208/209 выполняются позже.

<a id="proc-000297"></a>

### proc-000297 — Чат: пункты меню защиты

getChatMessageContextOptions; внешний ContextMenu вызывает visible/onClick.

<a id="proc-000298"></a>

### proc-000298 — Чат: доступность защиты

ContextMenu.visible(li); li является HTMLElement в прочитанном ядре14.

<a id="proc-000299"></a>

### proc-000299 — Чат: выбор Actor для защиты

ContextMenu.onClick(event,target); выбранный Actor не берётся из defenderUUID.

<a id="proc-000300"></a>

### proc-000300 — Чат: передача параметров защиты

executeDefense(actor,messageId); актуальные prepared поля сообщения.

<a id="proc-000301"></a>

### proc-000301 — Чат: регистрация щита, лечения и ремонта

renderChatMessageHTML вызывает общий listener; message не читается.

<a id="proc-000302"></a>

### proc-000302 — Чат: применение указанного щита

click button.shield; UUID Actor и строка щита из currentTarget.

<a id="proc-000303"></a>

### proc-000303 — Чат: вход запроса ремонта

click button.request-repair; полная реализация ремонта B09 остаётся за границей.

<a id="proc-000304"></a>

### proc-000304 — GM query: два имени регистрации

init → registerQueries(); режим передачи User.query отделён от системного сокета.

<a id="proc-000305"></a>

### proc-000305 — GM socket: создание сообщения

_createMessage(type,data); не проверяет значение аргументов.

<a id="proc-000306"></a>

### proc-000306 — GM socket: условия отправки

emitForGM(type,data); только вызванный отправителем системный маршрут.

<a id="proc-000307"></a>

### proc-000307 — GM socket: подписка получателя

ready вызывает после getIndex базового pack; ранний сбой ready может не дать регистрации.

<a id="proc-000308"></a>

### proc-000308 — GM socket: UUID и dispatch

Получено событие system.TheWitcherTRPG; не handler User.query.

<a id="proc-000309"></a>

### proc-000309 — Начало хода: Actor и две ветви

updateCombat → combatHooks → applyGeneralCombatHooks(combat); передан сам Combat, без фильтра update.

<a id="proc-000310"></a>

### proc-000310 — Начало хода: обход записей периодики

applyCombatEffects(actor); prepared turnStartEffects, не множество статусов.

<a id="proc-000311"></a>

### proc-000311 — Начало хода: сообщение и периодический урон

applyCombatEffect(actor,status); heal после damage — отдельная передача в .022.

<a id="proc-000312"></a>

### proc-000312 — Периодика: объявление схемы

Фабрика combatEffects(); фактическое наполнение карты зависит от эффектов/ядра.

<a id="proc-000313"></a>

### proc-000313 — Периодика: текст сообщения

renderTemplate(statusEffect.hbs,status); шаблон только отображает данные.

## Проверки

Проверены 162 тестовых метода: 161 прошёл в общем прогоне (1224.928 с), один — повторно после уточнения исторического ожидания (2.234 с). Все 453 CLI-примера прошли, включая 32 новых. Это проверки справочника по исходникам, без исполнения игрового сценария.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
PYTHONPATH=docs/analytics/system-index/tests python3 -B -m unittest test_expansion_008.EffectLifecycleExpansion.test_ordinary_effect_mutation_clone_and_query_payload -v
git diff --check
~~~

До общего прогона прошли 32 новых ожидания поиска и восемь отдельных проверок .020: регистрация/исполнение, выбор документов и shield, repair input, query, socket, Combat/периодика, payload/шаблон и накопленный граф. Сверка тестов с исходниками уточнила конкретные имена переменных/методов, кавычки ключей и строки helper/mapping; эта предварительная проверка не названа успешным общим прогоном.

У 421 прежнего CLI-примера не изменились проверяемые списки ID/концов связей при сравнении с исходным набором .019. Их тесты и ожидания сохранены; 16 seed-примеров продолжают проверяться на собственном историческом наборе. Численные итоги .019 теперь закреплены историческим диапазоном; содержательные проверки .019 не удалены. Общий прогон завершился с одной ошибкой старого ожидания .008: оно ограничивало все refers функции одним creation lifecycle. Новая ссылка на CONFIG query на строке41 не относится к созданию на строке67. Проверка уточнена до source206:67 и сохранила точное ожидание ent-000317; затем этот тест отдельно прошёл. Все остальные 161 метода и все CLI-случаи прошли в общем прогоне. Граф/примеры не менялись; повторный полный прогон не выполнялся.

Проверены прямые/обратные связи (11393 отношения), принадлежность шагов/отношений, достижимость выходов и три аспекта покрытия 615 sources. Все 11181 прежнее отношение и 289/291 прежних процессов неизменны. У proc-000045/046 дополнены только refs и relations выбранных шагов: ID, порядок, переходы, условия и выходы сохранены. Шестнадцать прежних сущностей уточнены с сохранением ID/владельцев/видов; остальные прежние сущности сохранены. Окончательные ссылки, актуальность и сохранность после обновления навигации записаны в журнале.


## Итог и следующая порция

Добавлены 70 сущностей, 212 отношений и 22 процесса; 13 новых динамических/внешних границ. Накоплено 4473 сущности, 11393 связи и 313 процессов (1040 шагов, 1889 переходов); 318 границ. Определения есть в 243/615 файлах: два словаря complete по строковым ключам, 241 файл partial; роли 136 основных/107 смежных, 372 без определений.

TASK-0006.020 done; следующая — [TASK-0006.021](../../tasks/task-0006.021.md), критические травмы. Родитель остаётся in-progress. Окончательная сверка — в [журнале](review-log.md#task-0006020).
