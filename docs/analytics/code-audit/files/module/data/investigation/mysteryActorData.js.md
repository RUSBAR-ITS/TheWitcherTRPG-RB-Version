# module/data/investigation/mysteryActorData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/investigation/mysteryActorData.js](../../../../../../../module/data/investigation/mysteryActorData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../review-log.md#task-0003023) |

## Назначение файла

Модель system документа Actor типа mystery: цель расследования и вложенные данные сложности.

## Условия использования

registerDataModels присваивает CONFIG.Actor.dataModels.mystery. Наследует непосредственно TypeDataModel; CommonActorData не включается. Тип mystery отсутствует в system.json, поэтому регистрация модели не доказывает доступность создания Actor в мире.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| complexity | Импорт, 1 | Фабрика вложенных полей | Локально | Вызов в defineSchema |
| fields | const, 3 | Поля Foundry | Локально | Построение схемы |
| MysteryActorData | default class, 5–12 | Тип данных Actor | CONFIG.Actor.dataModels.mystery | Подготовка модели |
| goal | StringField, 8 | Цель расследования | system.goal | Начальное '' |
| complexity | SchemaField, 9 | Пара complexity/difficulty | system.complexity | Начальные 25/'Easy' через фабрику |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Без аргументов; доступен API fields | Два верхних поля | goal + SchemaField(complexity()) | Собственных prepare/migrate/update-методов нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| complexity | [module/data/investigation/templates/complexityData.js](../../../../../../../module/data/investigation/templates/complexityData.js) | ES default import | defineSchema:9 | Фабрика разобрана целиком |
| TypeDataModel / StringField / SchemaField | Foundry 14.367.0, common/abstract/type-data.mjs; common/data/fields.mjs | Наследование/схема | Создание system | Настоящие классы, группа 01 |
| documentTypes.Actor | [system.json](../../../../../../../system.json) | Регистрационный контракт | Отсутствующий mystery | Группа 02, issue-00005 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | MysteryActorData | default import → CONFIG.Actor.dataModels.mystery | 21, 42 |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | actor.system и toObject(false) | Подготовка контекста | _prepareContext |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../../templates/sheets/investigation/mystery-sheet.hbs) | goal и complexity.* | Поля основной формы | 4, 7, 10 |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | type === 'mystery' | Выход prepareDerivedData до расчёта боевых характеристик | 39 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Модель хранит только цель и сложность; имя, ID, права и коллекция Items принадлежат самому Actor. Улики и препятствия не вложены в SchemaField — лист получает embedded Items через getList. Модель не уменьшает complexity, не считает время и не вызывает броски.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема и регистрация | Группы 01/02 | Defaults {goal:'',complexity:{complexity:25,difficulty:'Easy'}}; регистрация указывает настоящий класс | Регистрирующие API подменены, полное создание Actor не выполнено |
| Контекст и поля | Группы 03/16 | goal и оба вложенных пути существуют и совпадают с HBS | Сохранение формы не проверялось |

## Непроверенные участки и открытые вопросы

Все 12 строк прочитаны. Отсутствие типа в манифесте не обходилось. Поведение иных фаз Actor и активных эффектов на тайне целиком этой моделью не проверяется.

## Связанные проблемы

[issue-00005](../../../../../../issues/potential/issue-00005.md). Расхождение регистрации и манифеста дополнено результатами этой порции.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003023) |
