# module/scripts/chat.js

## Текущее состояние — 14.3.1.00107

TASK-0011.007: chatMessageListeners теперь читает message и передаёт его вместе с html в **bindEffectDelivery** из [effectDelivery.js](../../../../../../module/scripts/effectDelivery.js). Promise асинхронного связывания перехватывает ошибку; сам Foundry hook его не ожидает. Сервис связывает кнопку инициатора один раз, восстанавливает только состояние карточки после reload, без фоновой отправки. Три прежних обработчика shield/heal/request-repair сохранены.

[Локальная проверка интеграции](../../../../task-0011-static-checks.md#task-0011007); реальный DOM и два клиента проверяются в B07. Историческое «message не читается» ниже относится к прежнему коду.

## Актуализация 2026-09-17 — 14.3.1.00026

М09; [реализация и пределы проверок](../../../../../issues/closed/issue-00332.md).

onShield/onHeal стали async: ожидают Actor.update и возвращают ChatMessage.create. Выбор источника/цели, parseInt и верхний HP cap сохранены. Отсутствующий источник, строковая величина щита и серверная отмена без rejection не объявляются исправленными. DOM-dispatch сам Promise обработчика не ожидает.

Непосредственные зависимости и потребители: [module/actor/mixins/healMixin.js](../../../../../../module/actor/mixins/healMixin.js), [lang/ru.json](../../../../../../lang/ru.json), [lang/en.json](../../../../../../lang/en.json).

Основание: чтение текущего diff относительно `cd6fe2678105977ac220ab59e5fc87e6b3c6a343`; только статические проверки. Датированный разбор ниже сохраняет исходные доказательства и прежние адреса строк; изменённые контракты заменены описанием выше. Игровое исполнение этой версии пока не проверено.

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/chat.js](../../../../../../module/scripts/chat.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.040](../../../../../tasks/task-0003.040.md), 10 файлов, 237 логических строк |
| Запись перекрёстной сверки | [TASK-0003.040](../../../review-log.md#task-0003040) |

## Назначение файла

Подключает к HTML сообщения три действия: применить щит источнику, вылечить выбранного Actor и запросить ремонт предмета. Сами действия читают HTML-атрибуты, а не типизированные system-поля сообщения.

## Условия использования

TheWitcherTRPG.js вызывает Chat.chatMessageListeners(message,html) в renderChatMessageHTML вместе с боевыми/статусными обработчиками. Доступны HTMLElement/querySelector, canvas, game, fromUuidSync, ChatMessage, getInteractActor и RepairSystem. Аргумент message не используется. Кнопки создают spellItem.hbs и repair.hbs.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| chatMessageListeners | export function:4–8 | Регистрация трёх click handlers | Namespace import Chat в точке входа | По одному первому button.shield, button.heal, button.request-repair. |
| onShield / onHeal | Локальные functions:10–24 / 26–48 | Изменение Actor и сообщение о результате | Callbacks, не экспорты | Обычные функции без Promise/await. |
| onRepairRequest | Локальная async function:50–62 | Выбор исполнителя, поиск владельца/Item и запрос ремонта | Callback | Ожидает выбор и processRequest. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| chatMessageListeners(message,html) | HTML сообщения | undefined | querySelector и addEventListener(click,handler) для трёх классов | Нет проверки type, броска, роли или владельца; отсутствующие кнопки пропускаются. |
| onShield(event) | currentTarget.data-shield и data-actor(UUID) | undefined | fromUuidSync; actor?.update shield.value; localized content; getSpeaker({actor}); ChatMessage.create | Передаёт значение строкой. update/create не ожидает; actor.name не защищён при отсутствии Actor. |
| onHeal(event) | currentTarget.data-heal, data-actor | undefined | parseInt; источник по UUID; цель targets.first.actor → controlled[0].actor → user.character; ограничивает сверху hp.max; update; сообщение от источника | Без цели выходит. Нет проверки NaN/отрицательного числа; actor.name после записи цели не защищён; update/create без ожидания. |
| onRepairRequest(event) | event.target.dataset.owner/item; выбранный исполнитель | Promise<void> | await getInteractActor; game.actors?.get(ownerId); owner.items?.get(itemId); guard actor&&owner&&item; await processRequest(owner,item,actor) | owner используется до guard; target может быть дочерним узлом; отмена диалога зависит от helper. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| getInteractActor | [module/scripts/helper.js](../../../../../../module/scripts/helper.js) | named import, async вызов | Выбор персонажа-исполнителя ремонта | Импорт:1; callback:51. |
| RepairSystem | [module/item/systems/repair.js](../../../../../../module/item/systems/repair.js) | default import, вызов singleton | processRequest(owner,item,actor) | Импорт:2, await:60. |
| fromUuidSync / game / canvas / Actor.update / ChatMessage | Foundry 14.367.0, API документов и клиента | внешние глобальные API | Поиск, цели, ресурсы, создание чата и speaker | Все три callback; записи/коллекции в опытах заменены. |
| WITCHER.Combat.shieldApplied / healed | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | локализация | Текст щита и лечения | localize/format:17,41; expandObject и fallback учитываются. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../module/TheWitcherTRPG.js) | chatMessageListeners | Прямой namespace import; renderChatMessageHTML | Строки 2,52–58. |
| [templates/chat/combat/spellItem.hbs](../../../../../../templates/chat/combat/spellItem.hbs) | onShield/onHeal через классы кнопок | data-shield/data-heal, data-actor=Actor UUID | HTML подготовлен castSpell до оценки результата броска. |
| [templates/chat/item/repair.hbs](../../../../../../templates/chat/item/repair.hbs) | onRepairRequest через request-repair | data-owner=world Actor id; data-item=embedded Item id | Строки 69–72; текущая кнопка содержит текст без вложенной иконки. |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Щит заменяется переданной строкой; это не прибавление. Лечение записывает абсолютное hp.value цели; speaker остаётся Actor-источником. Повторные нажатия не блокируются; проверка полномочий остаётся операциям Foundry. При HP5/max20 heal50 даёт20; heal−9 пытается записать−4; '2.8' даёт7; пустой/нечисловой текст приводит к NaN. Если hp уже25/max20, heal0 уменьшает до20. Это наблюдения арифметики, не разрешение менять игровые правила.

Исчезнувший источник: shield не пишет, но падает на actor.name; heal с доступной целью вызывает update и затем падает. В repair отсутствие Item при существующем owner даёт тихий выход; отсутствующий owner вызывает TypeError раньше guard. currentTarget применяется только для heal/shield; repair использует target. Наличие дочерней иконки — граничный DOM-сценарий, не факт о текущем HBS. Native addEventListener с тем же handler на том же узле не нужно считать созданием дубля.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Привязка и щит | Группы 13–14 | Пропуск отсутствующих элементов; первая кнопка каждого типа; строковые shield7/0/−2; корректный speaker | DOM фасад, create/update перехвачены. |
| Лечение и источник | Группы 15–18 | Приоритет трёх целей; cap сверху; отрицательный/NaN; удалённый источник; parseInt('1d6')=1 | Не серверная валидация итоговой записи HP. |
| Асинхронность | Группа 19 | Callback вернул undefined и создал отчёт до завершения удержанного update | Отказ DB не воспроизводился; отсутствие await у heal также видно в коде. |
| Запрос ремонта | Группы 20–23 | Правильные owner/item/artisan; ожидание processRequest; ошибки owner/вложенного target/отмены; настоящий ранний выход prepareData без схемы | Не выполнены полный ремонт, расчёт стоимости и реальная выдача Item. |
| HTML и перевод | Группа 24; сверка 63 файлов | Атрибуты repair HBS соответствуют обработчику; два ключа доступны en/ru | Браузер, движок событий и внешние модули не запускались. |

## Непроверенные участки и открытые вопросы

Callbacks/HBS и полная граница поиска ремонтируемого Item установлены. .013/.016 — реальные dataset/DOM ([U011-03](../../../cross-check-0002.md#u011-03)), .018 — конкурентные клики, сохранение HP/shield и права/доставка ремонта ([U011-02](../../../cross-check-0002.md#u011-02)/[U011-06](../../../cross-check-0002.md#u011-06)). Старые фасады не доказывают успешный ремонт в мире.

## Связанные проблемы

[issue-00108](../../../../../issues/potential/issue-00108.md), [issue-00127](../../../../../issues/closed/issue-00127.md), [issue-00249](../../../../../issues/potential/issue-00249.md), [issue-00253](../../../../../issues/potential/issue-00253.md), [issue-00255](../../../../../issues/potential/issue-00255.md), [issue-00256](../../../../../issues/potential/issue-00256.md). Новые карточки описывают исчезнувший источник и невалидную числовую величину лечения. Асинхронность дополняет issue-00127; формулы, кнопки провала и owner уже имеют отдельные issues. Созданный здесь getSpeaker({actor}) не повторяет ошибку actor.actor из issue-00126.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `74322e91edac106c82668f4a47eef53ce1889dc1`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003040) |

## Сквозная сверка TASK-0004.011

2026-09-14; rusbar-main, 55e56567f42ed2da8850d913f28d727113ebdbd3. Исходник совпадает со срезом TASK-0001; изменено только описание.

Установлены три самостоятельных действия: shield заменяет поле источника строкой; heal выбирает target/controlled/character и parseInt с верхним cap; repair выбирает мастера helper и owner/item через dataset. Отсутствующий source Actor проверен не везде, а owner.items читается до guard. Ни создание сообщения, ни update heal/shield не ожидаются. RepairSystem и GM sender имеют отдельные этапы.

Сопоставленные определения и потребители: [module/scripts/socket/socketMessage.js](socket/socketMessage.js.md), [module/scripts/combat/combat.js](combat/combat.js.md), [module/scripts/helper.js](helper.js.md), [module/item/systems/repair.js](../item/systems/repair.js.md), [module/TheWitcherTRPG.js](../TheWitcherTRPG.js.md).

[Протокол и границы](../../../review-log.md#task-0004011) — TASK-0004.011; процессы [R011-06](../../../cross-check-0002.md#r011-06), [R011-07](../../../cross-check-0002.md#r011-07), [R011-08](../../../cross-check-0002.md#r011-08), [R011-23](../../../cross-check-0002.md#r011-23). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
