# module/data/investigation/obstacleData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/investigation/obstacleData.js](../../../../../../../module/data/investigation/obstacleData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../review-log.md#task-0003023) |

## Назначение файла

Самостоятельная TypeDataModel препятствия: скрытие, навыки, DC и текстовые значения последствий успеха/неудачи.

## Условия использования

Регистрируется как CONFIG.Item.dataModels.obstacle. CommonItemData не наследует. Хранение embedded Item в тайне не задано моделью: владельца передаёт лист при Item.create. Тип отсутствует в documentTypes.Item.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 1 | API полей Foundry | Локально | Построение схемы |
| ObstacleData | default class, 3 | Модель Item.obstacle | CONFIG.Item.dataModels.obstacle | Обработка данных |
| isHidden | BooleanField, 7 | Скрытие строки | system.isHidden | Чтение/редактирование; default false |
| type | StringField, 9 | Текстовый тип препятствия | system.type | Чтение/редактирование; default "" |
| dc | NumberField, 10 | Редактируемая DC | system.dc | Чтение/редактирование; default 14 |
| skillsUsed | ArrayField(StringField), 11 | Имена навыков | system.skillsUsed | Чтение/редактирование; default [] |
| successDamage | StringField, 13 | Текст/формула при успехе | system.successDamage | Чтение/редактирование; default "2" |
| failDamage | StringField, 14 | Текст/формула при неудаче | system.failDamage | Чтение/редактирование; default "1d6+2" |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | API fields | Словарь 6 полей | BooleanField/StringField/NumberField/ArrayField(StringField) | Собственных миграций, расчётов и записей нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| TypeDataModel и поля | Foundry 14.367.0, common/abstract/type-data.mjs; common/data/fields.mjs | Внешнее наследование/схема | defineSchema | Настоящие модели, группа 01 |
| documentTypes.Item | [system.json](../../../../../../../system.json) | Контракт типа | Отсутствующий obstacle | Группа 02 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | ObstacleData | Импорт/регистрация | 20, 68 |
| [module/item/sheets/investigation/WitcherObstacleSheet.js](../../../../../../../module/item/sheets/investigation/WitcherObstacleSheet.js) | item.system | Редактор V1 | getData/template |
| [templates/sheets/investigation/obstacle-sheet.hbs](../../../../../../../templates/sheets/investigation/obstacle-sheet.hbs) | system.* | Именованные поля формы | Все поля кроме isHidden |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | system.isHidden и выбранные data-field | Переключение скрытия, inline edit | _onItemHide/_onInlineEdit |
| [templates/sheets/investigation/partials/obstacle-display.hbs](../../../../../../../templates/sheets/investigation/partials/obstacle-display.hbs) | Все поля system | Строка embedded Item | Контекст each сохраняет system |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Значения схемы создаются/очищаются в памяти; сохранение выполняет внешний Document API. skillsUsed — массив строк без выбора из skillMap, принимает неизвестное имя и пустую строку; DC не имеет min/max/integer. successDamage/failDamage — строки, не выполненные Roll. В текущей строке препятствия отсутствует действие броска.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Defaults и допуски | Группа 01 | Получено {"isHidden":false,"type":"","dc":14,"skillsUsed":[],"successDamage":"2","failDamage":"1d6+2"}; неизвестные навыки допускаются | Серверный Item и БД не создавались |
| Пути формы/списка | Группы 04/11/16 | Схема соответствует именам формы, multi-select показывает выбранные навыки | DOM-элемент multi-select полностью не запускался |
| Использование навыков | Группы 06/09 | Данные редактируются; локальный бросок препятствия не найден | Игровое применение остальных значений не утверждается |

## Непроверенные участки и открытые вопросы

Прочитаны все 17 строк. Правила выбора навыков и применения последствий не изменялись. Отсутствие автоматизации текстовых полей не объявлено само по себе ошибкой.

## Связанные проблемы

[issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00150](../../../../../../issues/potential/issue-00150.md). 5 — тип; 150 — схема навыков без проверки имён (для препятствия последствие при броске не воспроизводилось).

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003023) |
