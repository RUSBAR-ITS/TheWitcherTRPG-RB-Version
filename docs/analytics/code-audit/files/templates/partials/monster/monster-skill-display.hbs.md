# templates/partials/monster/monster-skill-display.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/monster/monster-skill-display.hbs](../../../../../../../templates/partials/monster/monster-skill-display.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Старая строка встроенного навыка монстра: условная видимость, бросок и прямой ввод базового уровня.

## Условия использования

Принимает skill/name/stat от monster-skill-tab. Этот родитель относится к старому monster-sheet.hbs, а действующий V2 использует character-строку. Требуется модель Skill и слушатель sheet/skillMixin.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| if skill.isVisible | Весь HBS, 13 строк | Условие существования tbody | Читает системный флаг Skill | false полностью убирает строку |
| tbody / td / input | Строки 2–10 | Навык с действием броска и полем value | data-skill=name; data-stat=stat; data-action=rollSkill | input.name собирается из stat/name |

## Основные функции и методы

JS-функций нет. localize выводит skill.label. При isVisible=true input name='system.skills.{{stat}}.{{name}}.value' содержит skill.value; обработчик броска читает data-skill. В отличие от текущей character-строки здесь показан базовый value и есть редактор, а не modifiedValue.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Skill | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js) | Модель контекста | isVisible, label, value | Условие и input |
| Hash skill/name/stat | [templates/partials/monster/monster-skill-tab.hbs](../../../../../../../templates/partials/monster/monster-skill-tab.hbs) | Буквальный parent partial | Один из семи фиксированных атрибутов | Все семь вызовов |
| skillListener | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | DOM-событие | data-action=rollSkill | Связь с rollSkillCheck Actor |
| Foundry form / localize / preload | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Core API и предзагрузка | Стандартное именованное поле и перевод | Список preload; самостоятельного submit нет |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../../../templates/partials/monster/monster-skill-tab.hbs) | Весь HBS | Семь partial-вызовов | Буквальные ссылки |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Весь HBS | Предзагрузка | Буквальная ссылка |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Путь сохраняемого базового значения задаётся input.name. isVisible здесь лишь читается; конфигурируется через skillConfiguration. Активные добавки отдельно не показываются. Текущая character-строка не наследует это условие видимости.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полный шаблон | 13 строк; hash; schema; handler | Один динамический путь value; одна граница isVisible | Без JS |
| Настоящий Handlebars | Одинаковая модель с false/true, отрицательным/нулевым value | При false вывод пуст; при true корректный путь system.skills.<stat>.<name>.value | Сохранение формы старого ActorSheet не исполнялось |

## Непроверенные участки и открытые вопросы

Старый шаблон не является текущим PARTS монстра. Видимость проверена сравнением с реальным HBS текущей вкладки; глобальная политика показа навыков не изменялась.

## Связанные проблемы

[issue-00004](../../../../../../issues/potential/issue-00004.md), [issue-00015](../../../../../../issues/potential/issue-00015.md), [issue-00016](../../../../../../issues/potential/issue-00016.md), [issue-00018](../../../../../../issues/potential/issue-00018.md). Подписи, commonsp и различие видимости отражены в прежних наблюдениях.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |
