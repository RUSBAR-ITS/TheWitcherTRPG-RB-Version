# module/data/actor/templates/character/currencyLogData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/character/currencyLogData.js](../../../../../../../../../module/data/actor/templates/character/currencyLogData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.005](../../../../../../../../tasks/task-0003.005.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.005](../../../../../../review-log.md#task-0003005) |

## Назначение файла

Определяет одну запись журнала валют: пояснение, числовое изменение и ключ валюты. Итоговый путь записи — system.logs.currencyLog[index] у персонажа.

## Условия использования

При импорте локальная const fields получает foundry.data.fields. Default export — фабрика определения схемы; каждый вызов создаёт новые поля. Очистку, начальные значения и валидацию применяет Foundry при создании/обновлении модели. Единственный прямой импорт — Log; defineSchema оборачивает результат в SchemaField внутри ArrayField. Сам массив может быть пустым: определение полей записи не создаёт запись автоматически.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 1 | Доступ к классам полей | Локальная ссылка | Читается фабрикой |
| currencyLog | function, 3–9 | Схема одной записи | Default export | Возвращает три поля |
| label | StringField, 5 | Пользовательское пояснение | В записи журнала | initial='' |
| amount | NumberField, 6 | Сумма изменения | В записи журнала | initial=0; min/max/integer не заданы |
| type | StringField, 7 | Ключ валюты | В записи журнала | initial=''; choices не заданы |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| currencyLog(); 3–9 | Доступен foundry.data.fields | {label:StringField,amount:NumberField,type:StringField} | Создаёт новые определения полей при каждом вызове | Синхронно; без записи документов, обработчиков событий и собственного catch |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| StringField, NumberField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Глобальный API | 1,5–7: определения полей | Вызвана настоящая модель Log с пустой записью |
| Локальные импорты | Отсутствуют | — | Фабрика не обновляет баланс и не локализует label | Все 9 строк |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/templates/character/logData.js](../../../../../../../../../module/data/actor/templates/character/logData.js) | currencyLog() | Log.defineSchema: ArrayField(SchemaField(...)) | Импорт 1, поле 10 |
| [module/data/actor/templates/character/logData.js](../../../../../../../../../module/data/actor/templates/character/logData.js) | Log.addCurrencyReward | push записи в живой массив и передача всего массива в Actor.update | 31–37 |
| [module/data/actor/characterData.js](../../../../../../../../../module/data/actor/characterData.js) | Log как EmbeddedDataField | Схема logs в CharacterData | Импорт 4; поле 30 |
| [module/actor/rewardsSheet.js](../../../../../../../../../module/actor/rewardsSheet.js) | system.logs.currencyLog | _prepareContext передаёт document.system и CONFIG.WITCHER | 48–53 |
| [templates/sheets/actor/rewards/currency.hbs](../../../../../../../../../templates/sheets/actor/rewards/currency.hbs) | Поля записей | each выводит label и amount; тип через lookup config.currency и localize | 3–11; PARTS.currency RewardsSheet:33–36 |

Потребители искались по именам файлов/экспортов, точным и динамическим путям в module/, templates/ и packsJson/. В 226 JSON-компедиумах строковых ссылок с префиксами system.logs, system.skillTrainingN, system.pannels, system.attackStats не найдено. Бинарные packs, действующие БД и внешние макросы не проверялись.

## Данные и изменения состояния

type — строка, не UUID валютного документа. Для формы выдачи и чтения записи используется WITCHER.currency из config.js:624–632; схема не ограничивает type этим словарём. Отрицательный amount схемой не запрещён; арифметику выполняет Log.addCurrencyReward. В записи нет собственного ID, даты, UUID автора или ссылки на исходный навык/награду. В проверенных потребителях label показывается как текст, не ключ локализации. Фабрика не вызывает push/update, не удаляет записи и не ведёт пересчёт баланса по истории.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Defaults записи и массива | Настоящие Log({currencyLog:[{}]}) и CharacterData({}) | Запись содержит ровно три указанных поля; оба массива CharacterData.logs первоначально пусты | Без документа Actor |
| Схема ↔ создание ↔ вывод | Log, CharacterData, RewardsSheet и шаблон журнала | Установлена цепочка создания/сохранения/просмотра | HTML и сохранение не выполнялись |
| Фактическая запись | Исходный метод Log с перехватом Actor.update | crown=100, amount=5 → запись {label:'reward',amount:5,type:'crown'} и баланс 105 | Захвачены аргументы, а не запись БД |

## Непроверенные участки и открытые вопросы

Сопоставлены форма записи, настоящее Log и вызывающие методы. Удержанные Promise и dryRun в .005/.029/.037 не доказывают итоговый серверный баланс. Остаток — [U003-03](../../../../../../cross-check-0002.md#u003-03)/07; поддержка опыта других типов Actor не выбрана.

## Связанные проблемы

[issue-00028](../../../../../../../../issues/potential/issue-00028.md) — Log не возвращает Promise записи, возможны конфликтующие остатки при последовательных вызовах до завершения update.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.005 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Дополнительная сверка TASK-0003.037

2026-09-11, `rusbar-main`, `639fde4bad4a7ba4c538d3b08ddc5cfd846ca75e`; исходники не менялись.

Фактический reader rewards/currency.hbs берёт label/amount/type и локализует тип lookup ../config.currency. Схема не содержит даты или enum у type. Группа15 с неизвестным type сохранила его в модели истории, не создав соответствующий баланс; это подкрепляет235, но не доказывает серверное сохранение некорректного patch.

[module/actor/mixins/rewardsMixin.js](../../../../actor/mixins/rewardsMixin.js.md), [module/actor/rewardsSheet.js](../../../../actor/rewardsSheet.js.md), [module/app/reward/reward.js](../../../../app/reward/reward.js.md), [templates/chat/rewards.hbs](../../../../../templates/chat/rewards.hbs.md).

[Перекрёстная сверка и ограничения](../../../../../../review-log.md#task-0003037). Связанные файлы повторно в покрытие не добавлялись; исходники и статусы issues не менялись.

## Сквозная сверка TASK-0004.003

2026-09-14; rusbar-main, b4aeecb967caf97700cc565a670d6347b933619f. Исходник совпадает со срезом TASK-0001; изменено только описание.

Запись {label,amount,type} вкладывается в ArrayField Log.currencyLog. type — произвольная строка без choices, не ссылка на документ; баланс находится отдельно в currency. Log делает push до update и вычисляет абсолютный остаток с исходным amount; фабрика не нормализует аргумент до арифметики. Имена для показа валют берутся из CONFIG.WITCHER.currency.

Сопоставленные определения и потребители: [module/data/actor/templates/character/logData.js](logData.js.md), [module/data/actor/templates/common/currencyData.js](../common/currencyData.js.md), [module/app/reward/reward.js](../../../../app/reward/reward.js.md).

[Протокол и границы](../../../../../../review-log.md#task-0004003) — TASK-0004.003; процессы [R003-07](../../../../../../cross-check-0002.md#r003-07). Новое исполнение N01 протокола ограничено моделями и собственными расчётами Actor; остальные перечисленные опыты относятся к прежним порциям.
