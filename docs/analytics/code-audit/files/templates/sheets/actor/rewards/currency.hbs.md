# templates/sheets/actor/rewards/currency.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/rewards/currency.hbs](../../../../../../../../templates/sheets/actor/rewards/currency.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.037](../../../../../../../tasks/task-0003.037.md), 8 файлов, 313 логических строк |
| Запись перекрёстной сверки | [TASK-0003.037](../../../../../review-log.md#task-0003037) |

## Назначение файла

Вкладка просмотра валютного журнала. Не определяет JavaScript-методов, не начисляет награды и не записывает Actor.

## Условия использования

Часть PARTS RewardsSheet; окно открывает CharacterSheet. Контекст готовит RewardsSheet._prepareContext и базовое ядро.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.tab | HBS:1 | Вкладка primary/currency | tabs.currency.cssClass | Показ/скрытие ядром |
| each system.logs.currencyLog as currencyLog | HBS:3–10 | Строки .logEntry внутри .logs | label/amount/type | Вывод lookup ../config.currency |

## Основные функции и методы

Собственных функций и методов нет. each перебирает currencyLog; lookup получает перевод типа из config.currency на уровень выше контекста цикла; localize выводит его.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| PARTS.currency/system/config/tabs.currency | [module/actor/rewardsSheet.js](../../../../../../../../module/actor/rewardsSheet.js) | Производитель контекста | Прямой template/renderTemplate | Контекст полностью сопоставлен с потребителем |
| Handlebars helpers / Foundry localize | Handlebars 4.7.9 / Foundry 14.367.0 | Внешние helpers | each/if/lookup/concat по используемым выражениям | Набор определён HBS; реальные шаблоны исполнялись |
| preloadHandlebarsTemplates | [module/setup/handlebars.js](../../../../../../../../module/setup/handlebars.js) | Проверка загрузки | Этот HBS не входит в preload | Доступ через PARTS либо прямой renderTemplate |
| Переводы | [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) | Локализация | WITCHER.Actor.rewards, WITCHER.rewards или WITCHER.Currency по выражениям | expandObject + Localization/fallback |
| Массив журнала и схема записи | [module/data/actor/templates/character/logData.js](../../../../../../../../module/data/actor/templates/character/logData.js); [module/data/actor/templates/character/currencyLogData.js](../../../../../../../../module/data/actor/templates/character/currencyLogData.js) | Данные модели | Поля строки цикла | Без timestamp и собственного пересчёта |
| .logEntry | [styles/rewards.css](../../../../../../../../styles/rewards.css) | CSS | display:flex;justify-content:space-around | Подключён styles/witcher-styles.css:27 |
| WITCHER.currency | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Справочник | Тип/подпись валюты | В HBS lookup или WITCHER.Currency.<type>; не rates |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/rewardsSheet.js](../../../../../../../../module/actor/rewardsSheet.js) | currency.hbs | PARTS при рендере окна | PARTS.currency |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Входы system.logs.currencyLog[].label/amount/type, config.currency и tabs.currency.cssClass. Подпись количества использует существующий WITCHER.rewards.dialog.currency. lookup ../config.currency корректно выходит из контекста each; неизвестный type не получает подпись. Нет полей name, дат, суммы, сортировки, конвертации или редактирования.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный контекст | Группы20–22 | Рендер всех PARTS; форма без полей даёт {} | Без браузерного render |
| Значения/порядок/переводы | Группы21–23 | Реальные модели и EN/RU, escaped label | При отсутствии записей просто нет строк |

## Непроверенные участки и открытые вопросы

Просмотр не начисляет наград. Native вкладка/localize/lookup и соответствие истории подтверждённому кошельку — [U014-06](../../../../../cross-check-0002.md#u014-06); unknown type и серверное применение — [U014-05](../../../../../cross-check-0002.md#u014-05).

## Связанные проблемы

[issue-00028](../../../../../../../issues/potential/issue-00028.md), [issue-00235](../../../../../../../issues/potential/issue-00235.md). 28 описывает завершение записи;235 — неизвестный тип входной награды.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003037) |

## Сквозная сверка TASK-0004.014

2026-09-14; rusbar-main, 8256dd3473347494fefb30524700fe7ca1daf75d. Исходник совпадает со срезом TASK-0001; изменено только описание.

В фактическом HBS each читает system.logs.currencyLog; amount/label берутся из строки, lookup ../config.currency[type] передаёт ключ localize. Таблица не использует rates и не пересчитывает баланс, в ней нет имён полей. Unknown type — отдельная граница producer/модели; Boolean IP к этой вкладке не относится.

Сопоставленные определения и потребители: [module/actor/rewardsSheet.js](../../../../module/actor/rewardsSheet.js.md), [templates/sheets/actor/rewards/header.hbs](header.hbs.md), [templates/sheets/actor/rewards/ip.hbs](ip.hbs.md), [module/actor/sheets/WitcherCharacterSheet.js](../../../../module/actor/sheets/WitcherCharacterSheet.js.md), [module/data/actor/templates/character/logData.js](../../../../module/data/actor/templates/character/logData.js.md), [module/data/actor/templates/character/ipLogData.js](../../../../module/data/actor/templates/character/ipLogData.js.md), [module/data/actor/templates/character/currencyLogData.js](../../../../module/data/actor/templates/character/currencyLogData.js.md), [module/setup/config.js](../../../../module/setup/config.js.md), [styles/rewards.css](../../../../styles/rewards.css.md), [module/app/reward/reward.js](../../../../module/app/reward/reward.js.md), [module/data/actor/templates/common/currencyData.js](../../../../module/data/actor/templates/common/currencyData.js.md).

[Протокол и границы](../../../../../review-log.md#task-0004014) — TASK-0004.014; процессы [R014-22](../../../../../cross-check-0002.md#r014-22), [R014-23](../../../../../cross-check-0002.md#r014-23). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
