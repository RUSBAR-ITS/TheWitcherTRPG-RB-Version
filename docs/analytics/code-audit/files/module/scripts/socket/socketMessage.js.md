# module/scripts/socket/socketMessage.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/socket/socketMessage.js](../../../../../../../module/scripts/socket/socketMessage.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.045](../../../../../../tasks/task-0003.045.md), 5 файлов / 336 логических строк; данный файл — 21 |
| Запись перекрёстной сверки | [TASK-0003.045](../../../../review-log.md#task-0003045) |

## Назначение файла

Формирует {type,data} и отправляет запрос игрока в системный сокет при наличии активного GM.

## Условия использования

Импортируется только [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) и [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) в найденной области module. Файл не подписывается на сокет, не регистрирует queries и не выбирает документы. Комментарий ONE gm описывает замысел; фактический отбор активного GM расположен в receiver. Пример SocketMessage.emitGM в комментарии не совпадает с exported emitForGM и найденными callers.

## Введённые сущности и действия с ними

| Сущность | Вид / место | Доступность | Действие |
| --- | --- | --- | --- |
| _createMessage | function:9–11 | local | Создаёт {type,data}, сохраняет ссылку на data |
| emitForGM | async function:13–21 | export | Guards, envelope и socket.emit |
| system.TheWitcherTRPG | Строковый канал:20 | Аргумент emit | Совпадает с системным ID и receiver |

## Основные функции и методы

| Функция | Входы / предусловия | Результат и действия | Ожидания / ошибки |
| --- | --- | --- | --- |
| _createMessage(type,data) | Любые аргументы | Новый объект ровно с двумя ключами | Не валидирует/не клонирует data; нет recipient/requestId |
| emitForGM(type,data) | Глобальный game; socket/user/users | При отсутствии одного из трёх тихий return; если user.isGM — console.error и return; если !users.activeGM — другая console.error и return; иначе await socket.emit(channel,envelope) | Собственный Promise undefined, без результата операции; game целиком не защищён; rejected/throw emit не перехватывается |

Guard isGM запрещает отправку любому GM, даже неактивному. У callers есть отдельные прямые ветви для GM/права update. Наличие activeGM проверяется до отправки; его ID не передаётся. Это общий системный канал, а не сообщение конкретному User. Только receiver сравнивает game.user === game.users.activeGM.

### Что означает await

Локальный Socket.IO 4.8.3 emit возвращает сам Socket; await такого значения не ждёт записи на другом клиенте. При autoConnect:false проверено буферизованное событие без сетевого подключения: sender завершился, sendBuffer содержит envelope, acknowledgement не зарегистрирован. Отправитель не передаёт ack callback и не вызывает emitWithAck. Даже завершённый socket callback GM не включает окончание addItem/restoreReliability: receiver не возвращает их Promise.

## Используемые сущности и зависимости

| Сущность | Источник | Связь / место | Основание |
| --- | --- | --- | --- |
| game.socket.emit | Foundry game.socket / /opt/foundryvtt/node_modules/socket.io-client/build/esm/socket.js | Внешний API:20 | emit формирует пакет и возвращает this; проверен реальный отключённый Socket |
| game.user.isGM / game.users.activeGM | Foundry User/Users | Guards:14–18 | Контролируемые игрок/GM/отсутствующий получатель |
| registerSocketListeners | [module/setup/socketHook.js](../../../../../../../module/setup/socketHook.js) | Receiver того же канала | Разрешены restoreReliability/addItem, data.shift → fromUuidSync → метод документа |
| socket:true / id | [system.json](../../../../../../../system.json) | Декларация системного канала | ID TheWitcherTRPG; sender и receiver используют буквальный префикс |
| addItem / removeItem | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Косвенная операция передачи | sender giftItem отдельно списывает отправителя; addItem выполняет receiver |
| restoreReliability | [module/item/mixins/repairMixin.js](../../../../../../../module/item/mixins/repairMixin.js); [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js); [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Динамический метод Item через mixin | Получатель вызывает по UUID; обновление надёжности далее в RepairSystem |
| console.error | JavaScript host | Два guard-сообщения | Локальная диагностика, не уведомление интерфейса и не результат caller |

## Известные потребители

| Файл | Сущность / аргументы | Условие |
| --- | --- | --- |
| [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js):262–274 | emitForGM('restoreReliability',[data.item.uuid]) | Успешный ремонт, Item нельзя обновить текущему пользователю; при наличии права — прямой update |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js):142–149 | emitForGM('addItem',[receiver,item,1]) | Игрок передаёт Item; GM вызывает receiverActor.addItem напрямую; removeItem после этого не ждёт получения |
| [module/setup/socketHook.js](../../../../../../../module/setup/socketHook.js) | Envelope {type,data} | Не импортирует sender, но подписан на тот же канал |

Сокет не используется обработчиками combat.js/applyDamage.js/generalCombatHook.js. Защита/эффекты могут вызывать иной механизм User.query из [module/setup/queries.js](../../../../../../../module/setup/queries.js); смешивать эти протоколы нельзя. Поиск ограничен module; сторонние макросы/модули не исследованы.

## Данные и изменения состояния

Сам sender создаёт envelope и запускает emit; Actor/Item не обновляет. receiver изменяет свой message.data через shift. Тест общего объекта в памяти не доказывает изменение массива отправителя при настоящей сериализации по сети. В envelope нет сведений о результате, transaction ID или подтверждения получения.

Receiver отбрасывает запрос на неактивном GM/игроке. На активном GM unknown type, null payload и несуществующий документ могут вызвать TypeError. Это отказ данного callback; следующий корректный запрос в локальной проверке по-прежнему выполняется.

## Проверки и доказательства

| Проверка | Фактический результат | Пределы |
| --- | --- | --- |
| 24 | Envelope содержит прежний data; отсутствующие socket/user/users пропускают отправку; GM/нет activeGM дают console.error | game — фасад, отправки нет |
| 25 | Настоящий отключённый Socket.IO: emit возвращает Socket, два события остаются sendBuffer, acks пуст | autoConnect:false, никакого соединения с сервером |
| 26–27 | Настоящий receiver: игрок/другой GM игнорируют, активный GM вызывает оба допустимых метода; shift удаляет UUID; unknown/null/нет UUID/документа отклоняются, следующий корректный запрос работает | Все клиенты представлены последовательными фасадами, сеть не моделировалась |
| 28 | receiver завершился при незавершённом Promise документа | Не подтверждает сохранение Item; служебная отправка и прикладной результат различены |

## Непроверенные участки и открытые вопросы

Прочитаны все 21 строки и полный receiver; callers сверены в пределах условий и аргументов. Не проверены серверная маршрутизация, подключение, сериализация настоящего Item, повторная доставка, смена активного GM во время передачи, права/БД и действующие сторонние модули. Ни количество реально доставленных пакетов, ни гарантии выполнения не выводятся из локальных guards.

## Связанные проблемы

[10](../../../../../../issues/potential/issue-00010.md) — receiver не проверяет тип/структуру запроса и UUID; [169](../../../../../../issues/potential/issue-00169.md) — списание передачи без подтверждения получения. [108](../../../../../../issues/potential/issue-00108.md) — более ранняя отдельная ошибка кнопки запроса ремонта, не ошибка этого sender. [2](../../../../../../issues/potential/issue-00002.md) — ready может не достигнуть регистрации receiver.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 20ce99a1218a82bf46c84570e55587253d0cfbc3; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003045) |
