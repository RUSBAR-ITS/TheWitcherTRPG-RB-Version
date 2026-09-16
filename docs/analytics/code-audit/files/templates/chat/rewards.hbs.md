# templates/chat/rewards.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/rewards.hbs](../../../../../../templates/chat/rewards.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.037](../../../../../tasks/task-0003.037.md), 8 файлов, 313 логических строк |
| Запись перекрёстной сверки | [TASK-0003.037](../../../review-log.md#task-0003037) |

## Назначение файла

Общее HTML-сообщение о выдаче награды. Не определяет JavaScript-методов, не начисляет награды и не записывает Actor.

## Условия использования

Рендерится обоими Rewards.handout* после попыток начисления. ChatMessage.create вызывается только при truthy ip/amount.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| div.witcherTRPG / h3 | HBS:1–4 | Заголовок и label | Оба handout | Экранированный текст |
| if ip / if currency | HBS:5–14 | Условные суммы | ip либо currency gate | currency отсутствует в реальном producer |
| each actors as actor | HBS:16–18 | Имена получателей с br | actor.name | Нет фильтра по успешности update |

## Основные функции и методы

Собственных функций и методов нет. if выбирает блоки по truthy ip/currency; each выводит actors; concat строит WITCHER.Currency.<type>, localize получает подпись валюты. Формулы и подсчёт результатов отсутствуют.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| actors/label/ip/amount/type | [module/app/reward/reward.js](../../../../../../module/app/reward/reward.js) | Производитель контекста | Прямой template/renderTemplate | Контекст полностью сопоставлен с потребителем |
| Handlebars helpers / Foundry localize | Handlebars 4.7.9 / Foundry 14.367.0 | Внешние helpers | each/if/lookup/concat по используемым выражениям | Набор определён HBS; реальные шаблоны исполнялись |
| preloadHandlebarsTemplates | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Проверка загрузки | Этот HBS не входит в preload | Доступ через PARTS либо прямой renderTemplate |
| Переводы | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | Локализация | WITCHER.Actor.rewards, WITCHER.rewards или WITCHER.Currency по выражениям | expandObject + Localization/fallback |
| WITCHER.currency | [module/setup/config.js](../../../../../../module/setup/config.js) | Справочник | Тип/подпись валюты | В HBS lookup или WITCHER.Currency.<type>; не rates |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/app/reward/reward.js](../../../../../../module/app/reward/reward.js) | rewards.hbs | Два renderTemplate | handoutIpRewards/handoutCurrencyRewards |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Входы actors[].name, label, ip, currency, amount, type. Все значения выводятся обычными {{}} с экранированием; пользовательский HTML не исполняется в HBS. Реальный денежный producer передаёт amount/type, но не currency; денежный блок скрыт. При принудительном currency=true обнаруживается также отсутствующий WITCHER.rewards.chat.amount. Сообщение не различает магические IP (isMagic не передаётся), не показывает дату журнала/статус записи; author/time — отдельные метаданные ChatMessage.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Ветки/получатели | Группы09–10/19/22–23 | IP показан; валюта скрыта; чат не подтверждает успешность записи | create перехвачен, игровой чат не открыт |

## Непроверенные участки и открытые вопросы

Условие currency и отсутствие amount-переводов установлены; нативный chat render, fallback/модульные переопределения и завершение записей остаются [U014-06](../../../cross-check-0002.md#u014-06) и [U014-05](../../../cross-check-0002.md#u014-05).

## Связанные проблемы

[issue-00028](../../../../../issues/potential/issue-00028.md), [issue-00232](../../../../../issues/potential/issue-00232.md), [issue-00234](../../../../../issues/closed/issue-00234.md). 232 — currency gate без входа;234 — отсутствующий перевод денежного блока;28 — сообщение до подтверждения записей.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003037) |

## Сквозная сверка TASK-0004.014

2026-09-14; rusbar-main, 8256dd3473347494fefb30524700fe7ca1daf75d. Исходник совпадает со срезом TASK-0001; изменено только описание.

В фактическом HBS используются localize/concat, if и each; label/имена/числа — значения контекста, не самостоятельные helpers. IP проверяет ip, денежная ветка — отсутствующий в producer currency. amount/type переданы, но скрыты; отсутствующий chat.amount — отдельная локализационная причина. isMagic/speaker не переданы IP producer, а чат не подтверждает завершение начисления.

Сопоставленные определения и потребители: [module/app/reward/reward.js](../../module/app/reward/reward.js.md), [lang/en.json](../../lang/en.json.md), [lang/ru.json](../../lang/ru.json.md), [module/setup/config.js](../../module/setup/config.js.md).

[Протокол и границы](../../../review-log.md#task-0004014) — TASK-0004.014; процессы [R014-21](../../../cross-check-0002.md#r014-21). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
