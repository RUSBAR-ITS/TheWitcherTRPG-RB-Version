# module/actor/sheets/mixins/healMixin.js

## Актуализация 2026-09-17 — 14.3.1.00049

**Назначение:** Существующий однодневный отдых.

**Методы и действия:** После ресурсов последовательно ожидает heal по снимку травм. rejected/failed прекращает успешный общий отчёт, сообщает о возможном частичном восстановлении, не повторяет/не откатывает уже выполненное. HP/STA/vigor и speaker сохранены.

**Непосредственные зависимости/потребители:** [module/item/criticalWoundOperations.js](../../../../../../../../module/item/criticalWoundOperations.js), [module/data/item/criticalWoundData.js](../../../../../../../../module/data/item/criticalWoundData.js). Foundry Document/Roll/Collection/UI — внешние API.

[Проверки и пределы](../../../../../../task-0009-lifecycle-checks.md). Ниже сохранены датированные срезы; для изменённых операций действует описание .00049.

## Актуализация 2026-09-17 — 14.3.1.00026

М09, частично; [реализация и пределы проверок](../../../../../../../issues/closed/issue-00332.md).

recoverActor после записи ресурсов последовательно ожидает heal по снимку criticalWound и затем ChatMessage.create. Уведомление следует после сохранения сообщения. Отказ ожидаемой записи останавливает этот путь. Ограничение: heal → treat пока не ждёт внутренних create/delete (TASK-0009); формулы ресурсов, sticky-поля контекста и выбор DOM не менялись.

Непосредственные зависимости и потребители: [module/data/item/criticalWoundData.js](../../../../../../../../module/data/item/criticalWoundData.js).

Основание: чтение текущего diff относительно `cd6fe2678105977ac220ab59e5fc87e6b3c6a343`; только статические проверки. Датированный разбор ниже сохраняет исходные доказательства и прежние адреса строк; изменённые контракты заменены описанием выше. Игровое исполнение этой версии пока не проверено.

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/healMixin.js](../../../../../../../../module/actor/sheets/mixins/healMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.020](../../../../../../../tasks/task-0003.020.md), 10 файлов, 428 логических строк |
| Запись перекрёстной сверки | [TASK-0003.020](../../../../../review-log.md#task-0003020) |

Актуализация [issue-00001](../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Диалог дневного восстановления: расчёт HP по REC и четырём галочкам, восстановление STA/Vigor, продвижение заживления критических травм и отчёт в чат.

## Условия использования

const DialogV2 захватывается при импорте. Named export healMixin смешивается с WitcherActorSheet/WitcherActorSheetV1. Их activateListeners вызывает healListeners; jQuery click на .heal-button открывает немодальный DialogV2. В проверенных шаблонах кнопка найдена в character-header, отдельного входа этой кнопки для современного монстра не найдено; наличие примеси у базового листа само по себе не создаёт кнопку.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| DialogV2; healMixin | Alias 1; экспорт 3–123 | Диалог и пять методов примеси | Object.assign на листы Actor | Alias зависит от готового API Foundry |
| dialogData | Объект в _onHeal, 9–18 | Контекст формы и сообщения | totalRec, actor, isResting/isSterilized/isHealingHand/isHealingTent=false, daysHealed=1 | Передаётся в замыкания; actualWoundList не создаётся |
| Кнопки heal/cancel | 24–41 | Подтверждение/отмена | DialogV2 buttons; modal=false | heal читает глобальные checkbox; cancel пустой |
| change-слушатели четырёх checkbox | 110–121 | Пересчёт отображаемого лечения | restDialogListener | Все вызывают updateHealAmount с тем же dialogData |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _onHeal():4–46 | this.actor.system.derivedStats.rec | Promise<void> | Начальное floor(rec.max/2), контекст, await шаблон, new DialogV2(...).render({force:true}), затем listeners | Открытие/отмена не пишут Actor; переменная document — глобальный DOM |
| async updateHealAmount(totalRec,rec,dialogData):48–76 | Четыре глобальных checkbox; rec.max | Promise<void> | Начинает с floor(REC/2); resting заменяет на REC; sterilized +2, healing-hand +3, healing-tent +2; меняет totalRec/DOM | true флаги resting/sterilized не сбрасывает при выключении; hand/tent флаги вообще не меняет. Переданный totalRec перезаписывается |
| async recoverActor(isResting,isSterilized,dialogData):78–102 | Actor, рассчитанный totalRec, флаги из callback | Promise<void> | await Actor.update: hp=min(hp+totalRec,max), sta=max, vigor=max. forEach criticalWound→heal({sterilized}); render/chat и уведомление | Не ждёт heal каждого Item и ChatMessage.create; повторно сумму не вычисляет. isResting используется только в уведомлении, чат берёт dialogData.isResting |
| healListeners(html):104–107 | DOM или jQuery-обёртка | void | $(html).find('.heal-button').on('click',this._onHeal.bind(this)) | Регистрирует обработчик, не открывает окно сразу |
| restDialogListener(document,totalRec,rec,dialogData):109–122 | DOM с четырьмя ID | void | По одному change на resting/sterilized/healing-hand/healing-tent | Нет ограничения окном/очистки слушателей; querySelector(null) не проверяется |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| heal-rest.hbs | [templates/dialog/heal/heal-rest.hbs](../../../../../../../../templates/dialog/heal/heal-rest.hbs) | Рендер формы | 22–23 | Четыре повторяемых HTML id и два элемента вывода |
| resting-status.hbs | [templates/chat/heal/resting-status.hbs](../../../../../../../../templates/chat/heal/resting-status.hbs) | Рендер сообщения | 91–93 | isResting/totalRec/daysHealed; actualWoundList отсутствует в producer |
| CriticalWoundData.heal | [module/data/item/criticalWoundData.js](../../../../../../../../module/data/item/criticalWoundData.js) | Динамический вызов | 88, для каждого Item типа criticalWound | Тreated +1/+2; завершение вызывает переход; Promise не дожидается update |
| REC/HP/STA/Vigor | [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); [module/data/actor/templates/common/stats/statData.js](../../../../../../../../module/data/actor/templates/common/stats/statData.js) | Чтение/запись путей Actor | 5, 80–85 | Числовые value/max общей схемы; REC.max получен до открытия |
| heal-button | [templates/partials/character-header.hbs](../../../../../../../../templates/partials/character-header.hbs) | DOM-вход | healListeners | Кнопка 51; наличие слушателя у монстра не означает наличие кнопки |
| DialogV2; document.querySelector; $; ChatMessage; game.actors.getName; ui.notifications | Foundry 14.367.0, DOM, jQuery; client/documents/chat-message.mjs | Внешние API | Весь цикл UI/записи | В опыте DOM/Dialog/Actor.update/chat представлены фасадами |
| WITCHER.Heal.*, WITCHER.Chat.*, WITCHER.Button.Cancel | [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) | Локализация | Заголовки, информация, уведомление, сообщение | В общей проверке 44 ключей пропусков нет |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | healMixin / healListeners | import 7; вызов 243; Object.assign 320 | Базовый современный лист |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | healMixin / healListeners | import 7; вызов 221; Object.assign 300 | Предшествующий класс; зарегистрированный текущий лист проверяется отдельно |
| [templates/partials/character-header.hbs](../../../../../../../../templates/partials/character-header.hbs) | _onHeal через heal-button | Клик по кнопке восстановления | 51 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Дневное восстановление не использует calculateHealValue и не бросает кубики. REC=7 даёт 3 в активный день; resting даёт 7, все четыре галочки — 14. HP ограничивается максимумом, STA и Vigor полностью восстанавливаются; другие шкалы, временные HP и effects не сбрасываются. Травмы получают heal вне зависимости от isResting; конкретное начисление дней определяет их treatment.

Все элементы ищутся от document, а DialogV2 немодален. При двух окнах одинаковые ID адресуют первые найденные checkbox и надписи, несколько слушателей могут обновлять одну надпись по разным REC. Данные dialogData.isResting/isSterilized могут оставаться true после выключения; фактический callback читает свежие checkbox, но сообщение использует старый объект.

Отчёт выводит totalRec до ограничения HP; actualWoundList никогда не добавляется, поэтому блок заживления скрыт. Даже daysHealed=1 в объекте не является итогом фактических лечений. Speaker определяется через game.actors.getName(this.actor.name), что может выбрать другой одноимённый Actor и не идентифицирует синтетического Actor токена.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Открытие/отмена | Настоящий _onHeal и cancel; Dialog/DOM-фасады | modal=false, render force=true, четыре слушателя; записи 0 | Браузерный жизненный цикл DialogV2 не исполнялся |
| Галочки | Настоящий updateHealAmount, REC=7 | Все включены →14; все выключены →3, но isResting/isSterilized=true. Hand/tent в контексте остались false | Проверены данные/DOM-фасады, не внешние модули |
| Два диалога | Два _onHeal, один document.querySelector-фасад | На первом resting 2 слушателя; REC7/20 обновили один extra-info до +20 | Коллизия модели DOM воспроизведена изолированно |
| Восстановление/чат | recoverActor, HP9/max10, totalRec3; heal — pending | Запрошены HP10, STA20, Vigor3; чат уже создан при pending heal, показывает 3 вместо прироста 1; раздел травм отсутствует | Сохранение и действие травмы не завершались в реальном мире |
| Субъект/сообщение | Перехват getName и getSpeaker | Вместо id текущего Actor передан найденный по имени; чат resting при уведомлении active | Статическая привязка; выбранный Actor в опыте — фасад |

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. Producer, поля контекста и selectors сопоставлены; .013/.016 сводят листы, шаблоны, стили и en/ru. Остаются настоящий DialogV2, два одновременно открытых окна, inline-edit/drop и computedStyle/доставка чата. Старые DOM/HBS-фасады не доказывают браузерную доступность. Границы: [U012-03](../../../../../cross-check-0002.md#u012-03) и [U012-08](../../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00123](../../../../../../../issues/potential/issue-00123.md), [issue-00124](../../../../../../../issues/potential/issue-00124.md), [issue-00125](../../../../../../../issues/potential/issue-00125.md), [issue-00126](../../../../../../../issues/potential/issue-00126.md), [issue-00127](../../../../../../../issues/potential/issue-00127.md). Разделены адресация полей, состояние галочек, состав отчёта, выбор Actor сообщения и ожидание записи. Аналогичная глобальная адресация ремонта отмечена в issue-00106, но затронут другой диалог.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b09f992960a76d1c75946f402e42d93fa0785008`; полный файл | Первая карточка; [сверка порции и второй серии](../../../../../review-log.md#task-0003020) |

## Уточнение TASK-0003.025

2026-09-11, `rusbar-main`, `a2670a0a10c62b28d836b1a57577c4836f14cf20`. Оба общих класса подключают healMixin; healListeners получает DOM и через $ связывает .heal-button с _onHeal. Отдельная .recover-sta вызывает собственный _onRecoverSta общего листа, а не recoverActor: у неё два callback без ожидания update. При 9/10 и REC=3 передаётся 12 (issue-00164); раннее завершение дополняет issue-00127. Открытие модального окна не означает завершение отдыха.

Общие определения: [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) и [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js). [Методика и перекрёстная сверка](../../../../../review-log.md#task-0003025). Это точечное уточнение связей; полный разбор новых соседних файлов не засчитывается.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Сверен контракт кнопки header .heal-button и базового healListeners; сами методы лечения уже описаны в .020. В .031 проверены наличие/данные элементов и общая привязка, полный отдых/лечение заново не запускались.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../WitcherCharacterSheet.js.md); [templates/partials/character-header.hbs](../../../../templates/partials/character-header.hbs.md). [Методика и ограничения сверки](../../../../../review-log.md#task-0003031).

## Уточнение TASK-0003.058

2026-09-12; rusbar-main, 5283da15a49422fc339c44add4e7d7d02c174ce4; исходник не изменён.

recoverActor:88 вызывает heal каждого criticalWound без ожидания. Настоящий heal проверен на Foreign Object: treated +1 день, новая стерилизация +2 дополнительно, достижение healingTime=3 инициирует удаление; none/stabilized направляют update({}) при нулевых днях. Внешний диалог отдыха/чат не запускались; issue-00127 уточнена.

[Карточки Simple](../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json.md), [протокол, методы и ограничения](../../../../../review-log.md#task-0003058). Реальные записи в мир не выполнялись; состояния issues не менялись.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Старт totalRec=floor(REC.max/2); отдых заменяет на REC.max, стерилизация+2, Healing Hand+3, tent+2. Четыре фиксированных ID ищутся глобальным document, а не окном; listeners двух окон могут попадать в первое. Снятие флагов не сбрасывает dialogData.isResting/isSterilized; Hand/tent численно действуют, но флаги контекста не обновляются. CSS подсказки не исправляет состояние producer.

HP ограничен min(value+totalRec,max), STA и Vigor устанавливаются в max. После этого все criticalWound получают текущий checkbox стерилизации без ожидания. recoverActor и callback не дают барьера сохранения всех дней/переходов, поскольку heal/treat не ожидают внутренние записи. Уведомление читает свежий isResting.

В чат идёт потенциальный totalRec, не фактический прирост HP; постоянный daysHealed1 не итог каждого Item. actualWoundList отсутствует и блок дней скрыт. Старый isResting послеon→off даёт текст отдыха при уведомлении active. Шаблон выводит контекст, не ждёт документы и не рассчитывает лечение.

Примесь Actor передаёт this.actor, хотя this уже Actor; отдых ищет game.actors.getName(this.actor.name). В первом случае возможен fallback на пользователя/токен, во втором — одноимённый документ вместо текущего. Текст actor.name в HBS не исправляет speaker. ChatMessage.create не ожидается.

Сопоставленные определения и потребители: [module/data/item/criticalWoundData.js](../../../data/item/criticalWoundData.js.md), [templates/dialog/heal/heal-rest.hbs](../../../../templates/dialog/heal/heal-rest.hbs.md), [templates/chat/heal/resting-status.hbs](../../../../templates/chat/heal/resting-status.hbs.md), [module/actor/sheets/WitcherActorSheet.js](../WitcherActorSheet.js.md), [templates/partials/character-header.hbs](../../../../templates/partials/character-header.hbs.md).

[Протокол и границы](../../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-25](../../../../../cross-check-0002.md#r012-25), [R012-26](../../../../../cross-check-0002.md#r012-26), [R012-27](../../../../../cross-check-0002.md#r012-27), [R012-29](../../../../../cross-check-0002.md#r012-29). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
