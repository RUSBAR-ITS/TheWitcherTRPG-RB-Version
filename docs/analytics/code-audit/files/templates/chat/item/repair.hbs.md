# templates/chat/item/repair.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/item/repair.hbs](../../../../../../../templates/chat/item/repair.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.017](../../../../../../tasks/task-0003.017.md), одна порция из пяти файлов |
| Запись перекрёстной сверки | [TASK-0003.017](../../../../review-log.md#task-0003017) |

## Назначение файла

Информационная карточка ремонта и запрос в чат: предмет/владелец, DC с пояснением, повреждения, компоненты, стоимость заказа и кнопка другого исполнителя.

## Условия использования

Предзагружается setup/handlebars.js:69; RepairSystem.renderChatTemplate передаёт {data,isRequest,isOrder,showComponents}. HTML становится flavor будущего Roll.toMessage либо content обычного ChatMessage. На renderChatMessageHTML точка входа вызывает Chat.chatMessageListeners; тот находит button.request-repair и подписывает onRepairRequest. Сам HBS JS-обработчик не объявляет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| repair-message-section / chat-item-header | HTML,1–9 | Заголовок и картинка | data.item.img/name; при isRequest data.actor.name | Не устанавливает speaker; это задача caller |
| repair-section с DC и повреждениями | HTML,11–29 | repairDC/repairDCFormula и таблица переходов | data.damagedLocations; label/reliabilityValue/maxReliabilityValue | Условный вывод; нет сохранения |
| showComponents блок / три each | HTML,31–66 | owned, missing, unknown материалы | Каждая строка помечена (1) | unknown использует icons/svg/item-bag.svg; общий guard зависит от caller |
| isOrder / tr.components-price | HTML,60–64 | Итоговая стоимость заказа | data.repairPrice | Внутри showComponents |
| button.request-repair | HTML,69–72 | Начать обработку опубликованного запроса | data-owner=actor.id, data-item=item.id | Только при isRequest; передаются локальные ID, не UUID |

## Основные функции и методы

Собственных функций/классов нет. if выбирает заголовок, список повреждений/материалов, стоимость заказа и кнопку. each выводит готовые массивы. Обработчик click расположен в module/scripts/chat.js, вызывается после регистрации через renderChatMessageHTML.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| RepairData / isRequest / isOrder / showComponents | [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | Контекст | renderChatTemplate:250–260; потребители initMessageData/sendRepairInfoToChat | isRequest — аргумент, isOrder — artisan!==null; showComponents не учитывает unknown |
| onRepairRequest / chatMessageListeners | [module/scripts/chat.js](../../../../../../../module/scripts/chat.js) | DOM-контракт | button.request-repair, data-owner/item; callback50–62 | getInteractActor→game.actors.get(ownerId)→owner.items.get(itemId)→processRequest |
| getInteractActor | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js) | Косвенный вызов по кнопке | Выбор artisan по controlled token/character или выбору owned Actor | getCurrentCharacter:3–5, getInteractActor:11–22, chooseFromAvailableActors:32–57 |
| Chat.chatMessageListeners | [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Регистрация hook и последующий вызов | renderChatMessageHTML:52–58 | Регистрация не равна нажатию кнопки; цепочка сверена |
| Предзагрузка | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | loadTemplates | 69 | Тот же путь HBS |
| WITCHER.Repair.*, WITCHER.ComponentsList.totalPrice | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | localize | Подписи действия/DC/повреждений/материалов/цены/кнопки | Все соответствующие ключи существуют в en/ru |
| .repair-message-section / .repair-section > table / .request-repair | [styles/chat.css](../../../../../../../styles/chat.css) | CSS | 51–63, расположение/таблица/ширина кнопки | Прочитан фрагмент; полный аудит CSS ещё не выполнен |
| localize/if/each; img, button.dataset; ChatMessage/Actor collections | Handlebars 4.7.9; Web DOM и Foundry 14.367.0 | Внешние API | Подстановки и внешний click-путь | Handlebars/parse5 настоящие, DOM/коллекции/запись — фасады |
| icons/svg/item-bag.svg и data.item.img/component.img | Иконки Foundry / ресурсы документов | Изображения | Unknown и предметы | Изображения не загружались; assets вне границ исследования |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | HTML результата/запроса | renderChatTemplate→initMessageData(flavor) или sendRepairInfoToChat(content) | Сверены оба caller |
| [module/scripts/chat.js](../../../../../../../module/scripts/chat.js) | button.request-repair и dataset | chatMessageListeners и onRepairRequest | Listener исполнен из исходника |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | HBS путь | Предзагрузка | 69 |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Только отображение: (1) — фиксированный текст, не операция списания. Цена видна при isOrder внутри showComponents. Собственная формула броска/оценка успеха не здесь: extendedRoll дополняет flavor после initMessageData. Даже GM-сообщение об обычном ремонте само по себе не подтверждает завершение update.

Путь ID рассчитан на owner из game.actors. Проверка owner выполняется в onRepairRequest после обращения owner.items; при исчезнувшем Actor происходит TypeError раньше общего if. У synthetic token Actor и удалённых Items поведение зависит от внешнего поиска; полный сценарий synthetic Actor здесь не проверен. Только unknownComponents при пустых owned/missing не отображаются из-за showComponents=0, хотя собственный each для unknown предусмотрен.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Охват/контекст | 73 логические строки, весь HBS; RepairSystem и chat.js50–62 | Все ветви, поля и callback-контракт описаны | Листинг других разделов chat.js не даёт полной карточки этого файла |
| Только unknown | Настоящий renderChatTemplate/HBS с UNIQUE_UNKNOWN и пустыми owned/missing | Имя материала и таблица/цена скрыты, кнопка запроса присутствует | Источник showComponents — RepairSystem, а не отсутствие each в шаблоне |
| Смешанный список | Настоящий HBS с missing/unknown и artisan | Unknown выводится, заказная цена присутствует | Фактическая оплата не выполняется |
| Кнопка и ID | Настоящий chatMessageListeners/onRepairRequest; controlled artisan и world-owner в фасадах | Правильные ID открыли processRequest; отсутствие owner дало TypeError items | Мир/удаление Actor/браузер не запускались |

## Непроверенные участки и открытые вопросы

Шаблон прочитан полностью, рендер реальный. Foundry 14.367/Node 24.16, без клиентского чата, DOM событий браузера, сохранения сообщения, сети и permission проверок сервера. Synthetic token Actor не тестировался; обнаруженный missing-owner сценарий подтверждён отдельно на фасаде.

## Связанные проблемы

[issue-00102](../../../../../../issues/potential/issue-00102.md), [issue-00107](../../../../../../issues/potential/issue-00107.md), [issue-00108](../../../../../../issues/potential/issue-00108.md), [issue-00081](../../../../../../issues/potential/issue-00081.md), [issue-00100](../../../../../../issues/potential/issue-00100.md). 102 — источник не даёт повреждения;107 — скрытый список только unknown;108 — отсутствующий owner в обработчике кнопки. 81 — сообщение/восстановление не ожидаются;100 — отображение нечисловой цены из внешнего обработчика.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.017 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
