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

Проверены локальные исходники Foundry 14.367.0, Node 24.16.0, настоящие модели/методы/HBS и отдельные core-функции. Dialog, базовые приложения, коллекции и запись документов подменены; EventTarget настоящий Node, не браузерный DOM. Мир, сеть, права и транзакции реальной БД не запускались. HTML min/max/step не выдаются за серверную валидацию. Курсы и экономические правила не менялись. Способ доставки/отказ сообщения не тестировался в сети. Формула экономического обмена полностью находится в producer.

## Связанные проблемы

[issue-00020](../../../../../issues/potential/issue-00020.md), [issue-00231](../../../../../issues/potential/issue-00231.md). Наличие сообщения не устраняет ошибку same-currency; отсутствие await create фиксируется у producer, не как поведение самого HBS.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; полный файл | Первая карточка; [сверка порции](../../../review-log.md#task-0003036) |
