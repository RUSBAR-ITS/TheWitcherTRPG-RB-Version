# module/actor/mixins/adrenalineMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/adrenalineMixin.js](../../../../../../../module/actor/mixins/adrenalineMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.030](../../../../../../tasks/task-0003.030.md), 9 файлов, 424 логических строк |
| Запись перекрёстной сверки | [TASK-0003.030](../../../../review-log.md#task-0003030) |

Актуализация [issue-00001](../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Условное добавление одной единицы адреналина Actor по мировой настройке useOptionalAdrenaline.

## Условия использования

Именованный adrenalineMixin присоединён WitcherActor. Прямой листовой потребитель — _onAdrenalinePlus; динамический — разрешённый метод системного query, вызываемый при критическом результате защиты для атакующего.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| adrenalineMixin / addAdrenaline | export let и async метод,1–7 | Одна операция ресурса | Object.assign Actor.prototype | При включённой опции посылает update value+1 |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| addAdrenaline() | game.settings и system.adrenaline.value | Promise<void> | Проверяет useOptionalAdrenaline; если true, update system.adrenaline.value+1 | Не ограничивает максимум/минимум; update не ожидается/не возвращается; false не меняет документ |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| useOptionalAdrenaline | [module/setup/settings.js](../../../../../../../module/setup/settings.js) | Мировая настройка | Boolean/defaultfalse/configtrue | registerSettings:17–24 |
| adrenaline / CommonActorData | [module/data/actor/templates/common/adrenalineData.js](../../../../../../../module/data/actor/templates/common/adrenalineData.js); [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js) | Поля схем | value NumberField0 без min/max/integer | this.system.adrenaline.value |
| Actor.update / game.settings.get | Foundry 14.367 | Внешний API | Чтение настройки, отправка документной записи | Весь метод |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | adrenalineMixin | Прямой import и Object.assign | 18,453 |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../../module/actor/sheets/mixins/statMixin.js) | addAdrenaline | _onAdrenalinePlus вызывает без await | 119 |
| [module/setup/queries.js](../../../../../../../module/setup/queries.js) | Имя addAdrenaline | Разрешено callableEntityFunctions; entity[function] | query:26,40–41 |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | Динамическое addAdrenaline | При crit ищет владельца атакующего и посылает query | 210–217 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Пишет только system.adrenaline.value. Добавляет к текущему значению, не читает максимума и не устанавливает конкретный игровой потолок. При выключенной опции ручной/дистанционный вызов метода одинаково ничего не пишет. Query отдельно не ожидает вложенный вызов — дополнительная граница завершения.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный файл и динамические потребители | 7 строк; Actor, statMixin, defenseMixin и query | Одна запись, guard настройки; два пути вызова | Полная defense-процедура не разбиралась |
| Изолированный метод | Группа 06 с настоящей моделью и удержанным update | false→0 записей; true и value0/10/−1/0.5 →1/11/0/1.5; await add/листового плюса не ждёт записи | Сеть/query не запускались |

## Непроверенные участки и открытые вопросы

Сопоставлены источники чисел и исходные обработчики; исполнения Roll/формы из .028–.031 остаются историческими. Реальный клиент, произвольные входы внешних модулей и доставка сообщений не проверены. Точный остаток — [U003-03](../../../../cross-check-0002.md#u003-03)/04/05.

## Связанные проблемы

[issue-00008](../../../../../../issues/potential/issue-00008.md), [issue-00197](../../../../../../issues/potential/issue-00197.md). Проверена граница Promise в самой операции и её связи с уже описанным query.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003030) |

## Сквозная сверка TASK-0004.003

2026-09-14; rusbar-main, b4aeecb967caf97700cc565a670d6347b933619f. Исходник совпадает со срезом TASK-0001; изменено только описание.

Мировая useOptionalAdrenaline разрешает прибавку 1 к system.adrenaline.value. Schema NumberField не задаёт потолок, метод также не ограничивает результат. Ручной плюс листа и дистанционное действие доходят до этого метода, однако он не возвращает Promise update; await обёртки не подтверждает запись (00197). Минус ресурса — отдельный ожидающий обработчик.

Сопоставленные определения и потребители: [module/actor/witcherActor.js](../witcherActor.js.md), [module/data/actor/templates/common/adrenalineData.js](../../data/actor/templates/common/adrenalineData.js.md), [module/actor/sheets/mixins/statMixin.js](../sheets/mixins/statMixin.js.md), [module/setup/queries.js](../../setup/queries.js.md).

[Протокол и границы](../../../../review-log.md#task-0004003) — TASK-0004.003; процессы [R003-11](../../../../cross-check-0002.md#r003-11). Новое исполнение N01 протокола ограничено моделями и собственными расчётами Actor; остальные перечисленные опыты относятся к прежним порциям.
