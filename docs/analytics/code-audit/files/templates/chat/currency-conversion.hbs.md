# templates/chat/currency-conversion.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/currency-conversion.hbs](../../../../../../templates/chat/currency-conversion.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.036](../../../../../tasks/task-0003.036.md), 4 файла, 164 логические строки |
| Запись перекрёстной сверки | [TASK-0003.036](../../../review-log.md#task-0003036) |

## Назначение файла

HTML сообщения о результате конвертации: заголовок, source сумма/валюта, target валюта, процент комиссии и полученное количество.

## Условия использования

Actor openCurrencyConverter:89–99 рендерит после успешного await update; ChatMessage.create101–105 передаёт HTML, style OTHER и speaker Actor. В preloadHandlebarsTemplates не найден, вызывается по literal пути непосредственно.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| .witcherTRPG / h3 | 1–4 | Обёртка/название обмена | Контекст чата | WITCHER.currencyConverter.title |
| amount / from | 5–7 | Исходная сумма и локализованный ключ валюты | {{amount}} / localize from | Не итоговый баланс |
| to / fee / result | 8–16 | Целевая валюта, комиссия%, результат floor | localize to / {{fee}}% / {{result}} | Курс/остатки отсутствуют; result не вычисляется здесь |

## Основные функции и методы

JS-методов нет. localize обрабатывает title/from/to/fee/result labels и динамические ключи валют. Обычные {{amount}}/{{fee}}/{{result}} экранируются. Параметр actor, передаваемый producer, не используется; имя Actor берётся внешним ChatMessage speaker, а не этим HBS.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| amount/from/to/fee/result, unused actor | [module/actor/mixins/currencyConverterMixin.js](../../../../../../module/actor/mixins/currencyConverterMixin.js) | контекст renderTemplate | 89–99 | from/to — WITCHER.Currency.* labels из CONFIG; result=rounded |
| WITCHER.currencyConverter.*, WITCHER.Currency.* | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json) | локализация | 2–16 | expandObject/Localization; обычные labels + динамические from/to |
| Handlebars localize/escaping | Foundry client/applications/handlebars.mjs; Handlebars4.7.9 | рендер | весь файл | Значения не вычисляются, не изменяют документы |
| ChatMessage.create/getSpeaker | Foundry documents/chat-message.mjs; CONST.CHAT_MESSAGE_STYLES.OTHER | внешнее сообщение | producer101–105 | create не ожидается; speaker принимает настоящий Actor-фасад, корректно даёт actor ID |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/mixins/currencyConverterMixin.js](../../../../../../module/actor/mixins/currencyConverterMixin.js) | currency-conversion.hbs | await renderTemplate после записи | 89–99 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Шаблон выводит объявленный результат операции, не перечитывает wallet после сохранения и не доказывает подтверждение сервера. При неправильном расчёте входа показывает переданное значение, в том числе0/отрицательное; защиты from===to и курса здесь нет. Не создаёт ChatMessage сам и не пишет журнал currencyLog/rewards.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Нормальный/ошибочный путь | 05–14 | После успешного update есть message; при rejected update нет; Number result/fee отображаются | ChatMessage.create — фасад |
| Рендер | 20–21 | Имя actor не выведено;fee10%; hostile from экранирован; переводы проверены | Нет визуального чата/сети |

## Непроверенные участки и открытые вопросы

Формула и HBS сопоставлены; сетевое создание/отказ/порядок ChatMessage после денежного update не исполнялись ([U014-04](../../../cross-check-0002.md#u014-04)).

## Связанные проблемы

[issue-00020](../../../../../issues/potential/issue-00020.md), [issue-00231](../../../../../issues/potential/issue-00231.md). Наличие сообщения не устраняет ошибку same-currency; отсутствие await create фиксируется у producer, не как поведение самого HBS.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003036) |

## Сквозная сверка TASK-0004.014

2026-09-14; rusbar-main, 8256dd3473347494fefb30524700fe7ca1daf75d. Исходник совпадает со срезом TASK-0001; изменено только описание.

Контекст producer после await update содержит amount/from/to/fee/result и неиспользуемое имя actor. HBS выводит данные и localize валют; формулу/запись не выполняет. Speaker установлен в ChatMessage отдельно, create не ожидается. Неуспешный update не достигает этого рендера, отсутствие сообщения не откатывает деньги.

Сопоставленные определения и потребители: [module/actor/mixins/currencyConverterMixin.js](../../module/actor/mixins/currencyConverterMixin.js.md), [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../sheets/actor/currencyConverter/currencyConverter.hbs.md), [module/setup/config.js](../../module/setup/config.js.md), [module/data/actor/templates/common/currencyData.js](../../module/data/actor/templates/common/currencyData.js.md), [module/actor/witcherActor.js](../../module/actor/witcherActor.js.md).

[Протокол и границы](../../../review-log.md#task-0004014) — TASK-0004.014; процессы [R014-14](../../../cross-check-0002.md#r014-14), [R014-16](../../../cross-check-0002.md#r014-16). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
