# module/actor/mixins/healMixin.js

## Актуализация 2026-09-17 — 14.3.1.00026

М09; [реализация и пределы проверок](../../../../../../issues/closed/issue-00332.md).

createHealMessage возвращает Promise ChatMessage.create после await renderTemplate. calculateHealValue и пределы HP не менялись; сам этот метод не сохраняет HP.

Непосредственные зависимости и потребители: [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js).

Основание: чтение текущего diff относительно `cd6fe2678105977ac220ab59e5fc87e6b3c6a343`; только статические проверки. Датированный разбор ниже сохраняет исходные доказательства и прежние адреса строк; изменённые контракты заменены описанием выше. Игровое исполнение этой версии пока не проверено.

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/healMixin.js](../../../../../../../module/actor/mixins/healMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.020](../../../../../../tasks/task-0003.020.md), 10 файлов, 428 логических строк |
| Запись перекрёстной сверки | [TASK-0003.020](../../../../review-log.md#task-0003020) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Общие методы Actor для расчёта величины лечения с ограничением HP.max и формирования сообщения о лечении. Сам файл HP не записывает.

## Условия использования

healMixin импортируется witcherActor.js и присоединяется к WitcherActor.prototype. calculateHealValue вызывают расходование Item и лечение начала хода; createHealMessage — generalCombatHook. Примесь листа с таким же экспортным именем находится по другому пути и открывает отдых.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| healMixin | Экспортируемый объект, 1–25 | Два метода документа Actor | Named export; Object.assign | Нет автоматического выполнения при импорте |
| heal; messageTemplate; content; chatData | Локальные переменные | Величина лечения, HTML и данные ChatMessage | Внутри методов | Не поля схемы и не новые Item |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async calculateHealValue(value):2–10 | value — число или строка; this.system.derivedStats.hp | Promise<number\|string> | Если includes('d') — await Roll(value).evaluate().total. Сравнивает parseInt(current)+parseInt(heal) с max; при превышении возвращает max−current | Иначе возвращает heal исходного типа. Нет нижнего ограничения/валидации; null/undefined падают на includes; кубиковая ошибка не перехватывается |
| async createHealMessage(heal):12–23 | Величина и Actor-контекст | Promise<void> | await renderTemplate с {actor:this,heal}; getSpeaker({actor:this.actor}); style OTHER; ChatMessage.create | У Actor нет установленного здесь свойства actor; create не await/return. HP не меняет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| derivedStats.hp | [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js) | Чтение данных | 8–10; value/max | hp — SchemaField stat; value числовой, max целочисленный |
| stat | [module/data/actor/templates/common/stats/statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js) | Вложенная схема hp | Типы значения/максимума | Отдельный источник данных, не вызов функции из этой примеси |
| heal.hbs | [templates/chat/combat/heal.hbs](../../../../../../../templates/chat/combat/heal.hbs) | Шаблон | 13–15 | Отображает только heal и подпись; actor внутри шаблона не используется |
| Roll.evaluate; renderTemplate; ChatMessage.getSpeaker/create; CONST.CHAT_MESSAGE_STYLES.OTHER | Foundry 14.367.0: client/dice/roll.mjs; client/documents/chat-message.mjs; приложения Handlebars | Внешние API | 5–6, 15–22 | В опыте Roll выдаёт заданный total; getSpeaker и три private helper исполнены из ядра; create — регистратор |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | healMixin | import 14 и Object.assign 444 | Документ Actor получает оба метода |
| [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js) | calculateHealValue | При doesHeal; parseInt результата, затем actor.update | 8–9; асинхронность расходования отдельно в прежней карточке |
| [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) | calculateHealValue/createHealMessage | При status.heal.amount>0; если результат>0, await HP update и сообщение | 80–86; modifier не передаётся |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Возвращаемое число — запрошенное лечение, ограниченное сверху разностью max−value при переполнении. Функция не обеспечивает неотрицательность: HP=12/max=10 и лечение 3 дают −2. Непереполняющая строка '2' остаётся строкой, '2+3' остаётся '2+3' и будет усечена parseInt в consume; строка без числового начала остаётся строкой. Ветка кубиков определяется буквой d, полноценная проверка формулы делегирована Roll только в этой ветке.

createHealMessage формирует отдельное сообщение OTHER. В вызове из Actor.this.actor получается undefined; Foundry тогда может выбрать управляемый токен или персонажа пользователя. Переданный в шаблон actor:this не исправляет speaker. Ни daysHealed, ни treatment, ни временные HP эти методы не меняют.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Числа/строки и максимум | Настоящий calculateHealValue; Roll-фасад total=6 | HP5/10: 1d6→5, −2→−2, '2' остаётся строкой, '2+3' не вычисляется; HP12/10→−2 | Roll-парсер/случайные кубики и серверная валидация не запускались |
| Субъект чата | Настоящий метод и getSpeaker + 3 helper Foundry; фасады Actor/canvas/user | Лечится id=healed, выбран character id=other; speaker.actor='other' | Нет реального клиента и доставки сообщения |
| Регенерация/расходование | Вызовы двух потребителей сверены по исходникам | generalCombatHook ждёт HP update и передаёт amount без modifier; consume преобразует результат parseInt | Полные процессы повторно не исполнялись |

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. Отдых, calculateHealValue, consume и periodic имеют разные parse/await-границы. .013 сводит действия листов Actor; расходование Item уже сопоставлено в .007. .018 сохраняет вопросы записи HP/STA/Vigor, отказы, повторные клики, синтетический Actor и speaker одноимённых документов. Критерий: отдельно потенциальное восстановление, прирост ресурса, дни и подтверждённое сохранение. Границы: [U012-06](../../../../cross-check-0002.md#u012-06) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00022](../../../../../../issues/potential/issue-00022.md), [issue-00126](../../../../../../issues/potential/issue-00126.md), [issue-00127](../../../../../../issues/potential/issue-00127.md). modifier относится к внешнему обработчику; неправильный speaker и отсутствие ожидания ChatMessage.create относятся к этой примеси.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b09f992960a76d1c75946f402e42d93fa0785008`; полный файл | Первая карточка; [сверка порции и второй серии](../../../../review-log.md#task-0003020) |

## Дополнительная сверка TASK-0003.045

2026-09-12, rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3; исходники не изменены.

Полностью разобран [caller лечения начала хода](../../../../../../../module/scripts/combat/generalCombatHook.js). Группы 18/20 выполнили этот calculateHealValue с amount3: modifier2 не передаётся, приHP19/max20 healedFor1, при полном HP нет heal-message. Ветвь лечения ждёт Actor.update, но параллельная регенерация и предыдущий урон не гарантированно завершены (299). createHealMessage в этих новых проверках — фасад, прежний speaker/ChatMessage-create путь .020 не переоценивается.

[Проверки, результаты и ограничения](../../../../review-log.md#task-0003045). Связанные файлы не засчитываются повторно в покрытии.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

calculateHealValue лишь возвращает heal или разницу max−value по parseInt; если есть includes и строчная d, ожидает Roll.evaluate. Строка без d может остаться строкой; нижнего ограничения 0 нет, HP выше max даёт отрицательную разницу. consume дополнительно parseInt и не ожидает update; periodic ждёт положительное восстановление, передаёт amount без modifier. heal.hbs выводит только heal, Actor не использует.

Примесь Actor передаёт this.actor, хотя this уже Actor; отдых ищет game.actors.getName(this.actor.name). В первом случае возможен fallback на пользователя/токен, во втором — одноимённый документ вместо текущего. Текст actor.name в HBS не исправляет speaker. ChatMessage.create не ожидается.

Сопоставленные определения и потребители: [module/actor/witcherActor.js](../witcherActor.js.md), [module/item/mixins/consumeMixin.js](../../item/mixins/consumeMixin.js.md), [module/scripts/combat/generalCombatHook.js](../../scripts/combat/generalCombatHook.js.md), [templates/chat/combat/heal.hbs](../../../templates/chat/combat/heal.hbs.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-28](../../../../cross-check-0002.md#r012-28), [R012-29](../../../../cross-check-0002.md#r012-29). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
