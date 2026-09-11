# templates/partials/character/skill-display.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/character/skill-display.hbs](../../../../../../../templates/partials/character/skill-display.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Строка встроенного навыка текущей вкладки Actor: локализованная подпись, итоговый modifiedValue, флаги происхождения и действие броска.

## Условия использования

Получает hash skill/name/stat от character/tab-skills. Общая вкладка используется персонажем и монстром. skill — подготовленная модель Skill, а name — ключ из system.skills, который слушатель ищет в skillMap.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| a.char-stat-button.skill | Весь HBS, 24 строки | Кнопка броска | data-action=rollSkill, data-skill=name, data-stat=stat | Рендерится без условия isVisible |
| Класс и иконки происхождения | Строки 1, 11–23 | isProfession/isPickup/isLearned | Класс выбирается с приоритетом profession → pickup → learned | Иконки проверяются независимо, поэтому возможны все три |
| modifiedValue | Строки 5–9 | Подготовленное значение с активным модификатором | getter Skill | Ноль и положительные числа выводятся с '+', отрицательные без добавочного знака |

## Основные функции и методы

JS-функций и редактируемых полей нет. gte выбирает оформление modifiedValue; or включает контейнер иконок; if выводит каждую подпись. Roll-событие связывает sheet/skillMixin.skillListener, вычисление выполняет actor/skillMixin.rollSkillCheck. data-stat не используется этим обработчиком для определения навыка.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Skill.modifiedValue / label / флаги | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js) | Модель контекста | modifiedValue = value + activeEffectModifiers; isProfession/isPickup/isLearned | Поля HBS и getter |
| skill/name/stat | [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs) | Hash partial | Два вызова из system.skills | Явно переданные аргументы |
| skillListener | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | DOM-событие | data-action=rollSkill и data-skill | querySelectorAll и lookup this.skillMap |
| rollSkillCheck | [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | Метод Actor через слушатель | Бросок по описанию карты, не тексту подписи | Связь handler → Actor |
| gte / or / localize | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные и core helper; предзагрузка | Ветвление знака и флагов, локализация | Определения helper; ключи lang/en.json и lang/ru.json |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs) | Весь HBS | Два partial вызова с hash | Буквальные ссылки |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Весь HBS | preload | Буквальная ссылка |
| [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | rollSkill DOM | Назначает обработчик клика строке | Селектор data-action |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Шаблон ничего не сохраняет и не пересчитывает. Изменённое значение берётся из модели; activeEffectModifiers отдельно здесь не редактируется. isVisible игнорируется: тот же false, который скрывает старую monster-строку, не скрывает текущую.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение и модель | 24 строки, getter и partial/hash | Контракт Skill отличается от Item-навыка | Не требует преобразования в Item |
| Настоящий Handlebars | Ноль, отрицательное modifiedValue; сочетания трёх флагов; isVisible=false | Знаки корректны; класс приоритетный, иконки независимые; false не убирает anchor | DOM не подключался к браузерному Application |
| Встречная видимость | Тот же Skill в monster/monster-skill-display | Старый partial пуст при false; текущий присутствует | Старый родитель не является активным PARTS V2 |

## Непроверенные участки и открытые вопросы

Правило показа флагов как игровых категорий не интерпретировалось. Проверка Roll находится в карточке Actor-примеси; данный HBS формулу не задаёт.

## Связанные проблемы

[issue-00004](../../../../../../issues/potential/issue-00004.md), [issue-00015](../../../../../../issues/potential/issue-00015.md), [issue-00016](../../../../../../issues/potential/issue-00016.md), [issue-00018](../../../../../../issues/potential/issue-00018.md). Путь commonsp, подписи и видимость соотнесены с существующими issues; новых по одной этой строке не создавалось.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |
