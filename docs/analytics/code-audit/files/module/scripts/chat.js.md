# module/scripts/chat.js

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

Действия исполнены через callbacks реального chatMessageListeners; HTML разобран parse5, вместо браузерного DOM использован адаптер. Настоящие модели/методы ремонта на указанных границах; цели, коллекции, DialogV2, update, ChatMessage.create и UUID resolver заменены. Полномочия сервера, конкурентные клики и успешный полный ремонт в мире не проверены.

## Связанные проблемы

[issue-00108](../../../../../issues/potential/issue-00108.md), [issue-00127](../../../../../issues/potential/issue-00127.md), [issue-00249](../../../../../issues/potential/issue-00249.md), [issue-00253](../../../../../issues/potential/issue-00253.md), [issue-00255](../../../../../issues/potential/issue-00255.md), [issue-00256](../../../../../issues/potential/issue-00256.md). Новые карточки описывают исчезнувший источник и невалидную числовую величину лечения. Асинхронность дополняет issue-00127; формулы, кнопки провала и owner уже имеют отдельные issues. Созданный здесь getSpeaker({actor}) не повторяет ошибку actor.actor из issue-00126.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `74322e91edac106c82668f4a47eef53ce1889dc1`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003040) |
