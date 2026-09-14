# module/actor/mixins/rewardsMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/rewardsMixin.js](../../../../../../../module/actor/mixins/rewardsMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.037](../../../../../../tasks/task-0003.037.md), 8 файлов, 313 логических строк |
| Запись перекрёстной сверки | [TASK-0003.037](../../../../review-log.md#task-0003037) |

## Назначение файла

Две обёртки WitcherActor для открытия выдачи награды с заранее выбранным текущим Actor.

## Условия использования

После Object.assign к WitcherActor.prototype и регистрации game.api.rewards в init. Статические импорты отсутствуют. Обёртки передают массив [this]; это не немедленное начисление: пользователь сначала отвечает в диалоге. Сам UI выдачи открывается только для GM благодаря проверке в Rewards.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| rewardsMixin | export let, строки 1–9 | Примесь методов Actor | Object.assign в witcherActor.js:450 | Делегирование публичному API |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| addIpReward() | this — Actor; game.api.rewards.ip уже установлен | Promise<void>, не Promise результата API | Вызывает ip([this]) | Нет await/return; завершение диалога и записи не передаётся вызывающему коду |
| addCurrencyReward() | this — Actor; API currency установлен | Promise<void> | Вызывает currency([this]) | Та же потеря ожидания; своих проверок типа/прав нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| game.api.rewards.ip/currency | [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) | Динамический API | Оба метода | init:39–41 устанавливает ссылки на Rewards.handout* |
| Rewards.handoutIpRewards/handoutCurrencyRewards | [module/app/reward/reward.js](../../../../../../../module/app/reward/reward.js) | Косвенный вызов | Получает [this] | Проверка GM, диалог и журнал находятся в Rewards |
| WitcherActor | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Смешивание прототипа | Носитель this | import15/Object.assign450 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | rewardsMixin | Импорт и Object.assign ко всем Actor | 15/450 |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Actor.addIpReward | _addIpReward:448–450 вызывает без await; listener .manualIpReward | 116/448–450 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Нет собственных данных, update или ChatMessage. IP-обёртка найдена в CharacterSheet; вызов addCurrencyReward из UI в module/templates не найден, метод доступен программно. Поддержка метода прототипом не означает наличие logs у monster/loot.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Обёртки/API | Группа16; статическая сверка main/Actor | Оба wrapper завершаются при удержанном API Promise | Подменён только API; отказ сетевой записи не запускался |
| Маршрут IP | Группы06/09/14/17–19 | GM gate и ограничения получателей находятся ниже | См. карточку Rewards |

## Непроверенные участки и открытые вопросы

API и схемы сопоставлены; реальный GM UI, stale UUID, совместимость сторонних Actor и исход частичных записей остаются [U014-05](../../../../cross-check-0002.md#u014-05). Отсутствие return/await доказано кодом, окончательная БД не проверена.

## Связанные проблемы

[issue-00028](../../../../../../issues/potential/issue-00028.md), [issue-00233](../../../../../../issues/potential/issue-00233.md). issue28 уточнена уровнем Actor/API; issue233 относится к получателям нижнего слоя, не к регистрации примеси.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003037) |

## Сквозная сверка TASK-0004.014

2026-09-14; rusbar-main, 8256dd3473347494fefb30524700fe7ca1daf75d. Исходник совпадает со срезом TASK-0001; изменено только описание.

Оба async wrapper передают [this] в опубликованный game.api.rewards и завершаются без ожидания результата API. GM gate и форма находятся в Rewards.handout*, а Log отвечает за историю/остаток. Наличие метода у любого WitcherActor не гарантирует logs у его модели; Monster/Loot требуют отдельной проверки совместимости, уже описанной issue00233.

Сопоставленные определения и потребители: [module/app/reward/reward.js](../../app/reward/reward.js.md), [module/TheWitcherTRPG.js](../../TheWitcherTRPG.js.md), [module/actor/witcherActor.js](../witcherActor.js.md), [module/actor/sheets/WitcherCharacterSheet.js](../sheets/WitcherCharacterSheet.js.md), [module/data/actor/templates/character/logData.js](../../data/actor/templates/character/logData.js.md), [module/data/actor/characterData.js](../../data/actor/characterData.js.md), [module/data/actor/monsterData.js](../../data/actor/monsterData.js.md), [module/data/actor/lootData.js](../../data/actor/lootData.js.md).

[Протокол и границы](../../../../review-log.md#task-0004014) — TASK-0004.014; процессы [R014-17](../../../../cross-check-0002.md#r014-17), [R014-19](../../../../cross-check-0002.md#r014-19), [R014-20](../../../../cross-check-0002.md#r014-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
