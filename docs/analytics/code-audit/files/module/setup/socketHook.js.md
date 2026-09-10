# module/setup/socketHook.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/setup/socketHook.js](../../../../../../module/setup/socketHook.js) |
| Тип файла | JavaScript — сокет |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `3252300787c348e11f95098c345a6af7704b690c`; исходник совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Изменения относительно коммита | Нет |
| Задача и порция | [TASK-0002](../../../../../tasks/task-0002-system-initialization.md); порция 4 |
| Запись перекрёстной сверки | [Журнал сверок](../../../review-log.md) — TASK-0002, порция 4 |

## Назначение файла

Принимает сообщения системного сокета на активном GM и вызывает addItem или restoreReliability по UUID.

## Условия использования

[module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) вызывает registerSocketListeners в ready после загрузки индекса травм. Требуются game.socket и game.user; без них функция возвращается до подписки. Для обработки необходимо game.user === game.users.activeGM.

## Введённые сущности и действия с ними

| Сущность | Где | Действие |
| --- | --- | --- |
| registerSocketListeners | Экспорт const function, стр. 1 | Подписка на канал |
| SYSTEM_SOCKET | Локальная строка, стр. 2 | system.TheWitcherTRPG |
| callableFunctions | Локальный объект, стр. 4 | restoreReliability/addItem → маркер uuid |
| async callback(message) | game.socket.on, стр. 11 | Проверка активного GM, журналирование и вызов метода UUID |

## Основные функции и методы

| Функция | Вход / результат | Действия |
| --- | --- | --- |
| registerSocketListeners() | Нет → undefined | Устанавливает один listener, не сохраняет ссылку для снятия, нет защиты от повторной регистрации |
| callback(message) | {type, data}; data ожидается массивом [uuid, ...args] → Promise<undefined> | При type addItem/restoreReliability: shift извлекает UUID с изменением массива; fromUuidSync; вызов метода на документе. Результат метода не ожидается и не возвращается |

Другой type попадает в прямой вызов `callableFunctions[type](...data)`. Проверки существования документа, метода или структуры message нет. Это отдельный протокол от CONFIG.queries; callback не предоставляет прикладного подтверждения выполнения отправителю.

## Используемые сущности и зависимости

| Сущность | Источник | Связь | Определение / использование |
| --- | --- | --- | --- |
| game.socket.on / game.users.activeGM / fromUuidSync | Foundry и Socket.IO клиента | Глобальные API | Регистрация, выбор единственного получателя, разрешение UUID |
| emitForGM | [module/scripts/socket/socketMessage.js](../../../../../../module/scripts/socket/socketMessage.js) | Согласованный формат канала | Стр. 13–20, message={type,data}; отправитель запрещает вызов GM, требует активного GM |
| addItem | [module/actor/witcherActor.js](../../../../../../module/actor/witcherActor.js) | Динамический метод Actor | Стр. 259: добавить количество либо Item |
| restoreReliability | [module/item/mixins/repairMixin.js](../../../../../../module/item/mixins/repairMixin.js) | Динамический метод Item | Стр. 8; примесь в [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js) (373); вызывает [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) RepairSystem.restoreReliability, стр. 289 |
| socket: true | [system.json](../../../../../../system.json) | Декларация системного канала | Манифест; префикс соответствует system.id |

## Известные потребители

| Файл | Связь | Основание |
| --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) | Вызов регистрации в ready | стр. 90 |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | emitForGM('addItem', [receiver, item, 1]) при передаче предмета | стр. 146 |
| [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) | emitForGM('restoreReliability', [data.item.uuid]) | стр. 272 |
| [module/scripts/socket/socketMessage.js](../../../../../../module/scripts/socket/socketMessage.js) | Передаёт message через этот же канал | стр. 20 |

В проверенной области module найдены эти два прикладных отправителя; неизвестный type в штатных вызовах не найден.

## Данные и изменения состояния

Регистрирует listener; обработка логирует полученный объект и изменяет message.data через shift. Изменение Actor/Item косвенное, в методе целевого документа. Объекты данных миров в рамках исследования не изменялись.

## Проверки и доказательства

Прочитаны все 24 строки, сверены канал, оба отправителя и методы получателей. Исходный listener выполнен в vm: addItem передал остаток аргументов нужному UUID; массив после вызова не содержит UUID; unknown у активного GM → TypeError, у другого пользователя → ранний return.

## Непроверенные участки и открытые вопросы

Реальный Socket.IO, несколько клиентов, права записи и восстановление надёжности не выполнялись. Наличие listener зависит от прохождения предыдущих шагов ready. Поведение при неизвестном type не означает потерю всей дальнейшей подписки.

## Связанные проблемы

[issue-00010](../../../../../issues/potential/issue-00010.md) — неизвестный type; [issue-00002](../../../../../issues/potential/issue-00002.md) — регистрация может быть не достигнута из ready.

## История актуализации

2026-09-10 — первичный разбор полного файла на указанном коммите; сверка порции 4 отражена в журнале. Файлы зависимостей проверены в пределах определений и обращений, без объявления их полного разбора.
