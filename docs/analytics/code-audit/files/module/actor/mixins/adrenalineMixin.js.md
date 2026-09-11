# module/actor/mixins/adrenalineMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/adrenalineMixin.js](../../../../../../../module/actor/mixins/adrenalineMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `aa6af106e86a9c75fe050d599f961c8fadb74f1b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.030](../../../../../../tasks/task-0003.030.md), 9 файлов, 424 логических строк |
| Запись перекрёстной сверки | [TASK-0003.030](../../../../review-log.md#task-0003030) |

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

Доступность активного владельца для query относится к прежним наблюдениям; здесь не проверялись sockets, параллельное получение адреналина и правила его траты. Отсутствие потолка не объявлено нарушением рулбука.

## Связанные проблемы

[issue-00008](../../../../../../issues/potential/issue-00008.md), [issue-00197](../../../../../../issues/potential/issue-00197.md). Проверена граница Promise в самой операции и её связи с уже описанным query.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003030) |
