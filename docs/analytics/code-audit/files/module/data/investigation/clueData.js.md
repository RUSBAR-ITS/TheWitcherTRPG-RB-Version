# module/data/investigation/clueData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/investigation/clueData.js](../../../../../../../module/data/investigation/clueData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../review-log.md#task-0003023) |

## Назначение файла

Самостоятельная TypeDataModel улики: скрытие, навыки, DC, время и текстовые значения последствий.

## Условия использования

Регистрируется как CONFIG.Item.dataModels.clue. CommonItemData не наследует. Хранение embedded Item в тайне не задано моделью: владельца передаёт лист при Item.create. Тип отсутствует в documentTypes.Item.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 1 | API полей Foundry | Локально | Построение схемы |
| ClueData | default class, 3 | Модель Item.clue | CONFIG.Item.dataModels.clue | Обработка данных |
| isHidden | BooleanField, 7 | Скрытие строки | system.isHidden | Чтение/редактирование; default false |
| type | StringField, 9 | Текстовый тип улики | system.type | Чтение/редактирование; default "" |
| dc | NumberField, 10 | Редактируемая DC | system.dc | Чтение/редактирование; default 14 |
| skillsUsed | ArrayField(StringField), 11 | Имена навыков | system.skillsUsed | Чтение/редактирование; default [] |
| timeIncrement | StringField, 12 | Текст интервала | system.timeIncrement | Чтение/редактирование; default "" |
| timeBonus | NumberField, 13 | Числовой бонус времени | system.timeBonus | Чтение/редактирование; default 0 |
| damage | StringField, 15 | Текст/формула ущерба | system.damage | Чтение/редактирование; default "" |
| obfuscation | NumberField, 16 | Обфускация | system.obfuscation | Чтение/редактирование; default 0 |
| penalty | StringField, 18 | Текст штрафа | system.penalty | Чтение/редактирование; default "" |
| focusDamage | StringField, 19 | Текст/формула урона фокусу | system.focusDamage | Чтение/редактирование; default "1d6" |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | API fields | Словарь 10 полей | BooleanField/StringField/NumberField/ArrayField(StringField) | Собственных миграций, расчётов и записей нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| TypeDataModel и поля | Foundry 14.367.0, common/abstract/type-data.mjs; common/data/fields.mjs | Внешнее наследование/схема | defineSchema | Настоящие модели, группа 01 |
| documentTypes.Item | [system.json](../../../../../../../system.json) | Контракт типа | Отсутствующий clue | Группа 02 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | ClueData | Импорт/регистрация | 19, 67 |
| [module/item/sheets/investigation/WitcherClueSheet.js](../../../../../../../module/item/sheets/investigation/WitcherClueSheet.js) | item.system | Редактор V1 | getData/template |
| [templates/sheets/investigation/clue-sheet.hbs](../../../../../../../templates/sheets/investigation/clue-sheet.hbs) | system.* | Именованные поля формы | Все поля кроме isHidden |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | system.isHidden и выбранные data-field | Переключение скрытия, inline edit | _onItemHide/_onInlineEdit |
| [templates/sheets/investigation/partials/clue-display.hbs](../../../../../../../templates/sheets/investigation/partials/clue-display.hbs) | Все поля system | Строка embedded Item | Контекст each сохраняет system |
| [module/scripts/investigation/rollClue.js](../../../../../../../module/scripts/investigation/rollClue.js) | skillsUsed | Выбор навыка | 8–44 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Значения схемы создаются/очищаются в памяти; сохранение выполняет внешний Document API. skillsUsed — массив строк без выбора из skillMap, принимает неизвестное имя и пустую строку; DC не имеет min/max/integer. damage/focusDamage/penalty/timeIncrement — строки, не вычисленные результаты; обфускация и время не используются rollClue.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Defaults и допуски | Группа 01 | Получено {"isHidden":false,"type":"","dc":14,"skillsUsed":[],"timeIncrement":"","timeBonus":0,"damage":"","obfuscation":0,"penalty":"","focusDamage":"1d6"}; неизвестные навыки допускаются | Серверный Item и БД не создавались |
| Пути формы/списка | Группы 04/11/16 | Схема соответствует именам формы, multi-select показывает выбранные навыки | DOM-элемент multi-select полностью не запускался |
| Использование навыков | Группы 06/09 | Неверное имя доходит до rollSkill и ломает обращение к skillMapEntry; dc не передаётся | Игровое применение остальных значений не утверждается |

## Непроверенные участки и открытые вопросы

Прочитаны все 22 строк. Правила выбора навыков и применения последствий не изменялись. Отсутствие автоматизации текстовых полей не объявлено само по себе ошибкой.

## Связанные проблемы

[issue-00005](../../../../../../issues/potential/issue-00005.md), [issue-00150](../../../../../../issues/potential/issue-00150.md), [issue-00151](../../../../../../issues/potential/issue-00151.md). 5 — тип; 150 — неконтролируемые имена навыков; 151 — неиспользуемая DC при броске.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003023) |
