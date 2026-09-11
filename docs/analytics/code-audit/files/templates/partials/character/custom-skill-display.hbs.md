# templates/partials/character/custom-skill-display.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/character/custom-skill-display.hbs](../../../../../../../templates/partials/character/custom-skill-display.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Предполагаемая строка собственного Item-навыка на текущей общей вкладке. Фактический контракт расходится с переданным Item: шаблон ожидает skill.*, а получает Item.name и Item.system.*.

## Условия использования

Вызывается из character/tab-skills внутри each customSkills без hash. _prepareCustomSkills передаёт embedded Items. В актуальной форме персонажа и монстра это действующий путь отображения собственного навыка.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| a.char-stat-button.skill | Строка 1 | Кнопка с общим встроенным действием | data-action=rollSkill; data-skill={{name}}; data-stat={{stat}} | name становится Item.name; stat отсутствует |
| skill.label/value/флаги | Строки 3–21 | Ожидаемое шаблоном значение | Такого вложенного skill у переданного Item нет | Подпись, число и флаги не выводятся из Item.system |

## Основные функции и методы

JS-функций и редактируемых полей нет. gte/or/if оформляют skill.value и три флага, localize — skill.label. Существующий слушатель выбирает встроенный навык по data-skill. В шаблоне нет .item, data-item-id, #custom-rollable и целей удаления/раскрытия собственного Item.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Item-контекст partial | [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs) | Два буквальных вызова без hash | each lookup ../customSkills skillKey | Вызовы не передают skill/name/stat как встроенному partial |
| _prepareCustomSkills | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Источник Item-контекста | actor.items type=skill сгруппированы по attribute | Ни обёртки skill, ни преобразования в встроенную модель |
| SkillItemData | [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js) | Реальная схема Item | value/label/флаги находятся в system; document.name отдельно | Сопоставление всех чтений HBS |
| skillListener / rollSkillCheck | [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js); [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | Действующий DOM-обработчик | Общее data-action=rollSkill вызывает skillMap[Item.name] | Контракт handler и Actor |
| customSkillListener | [module/actor/sheets/mixins/customSkillMixin.js](../../../../../../../module/actor/sheets/mixins/customSkillMixin.js) | Отсутствующий DOM-контракт | Собственный бросок требует #custom-rollable и itemId | Эти атрибуты HBS не создаёт |
| gte / or / localize | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные/core helper и preload | Знак, иконки и подпись | Определения и список предзагрузки |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs) | Весь HBS | Два вызова внутри групп собственных навыков | Буквальные partial ссылки |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Весь HBS | preload | Буквальная ссылка |
| [module/actor/sheets/mixins/skillMixin.js](../../../../../../../module/actor/sheets/mixins/skillMixin.js) | data-action=rollSkill | Привязывает встроенный обработчик к custom-строке | Общий селектор |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Сохранения нет. Обычный Item с именем 'My skill' создаёт data-skill='My skill', пустой data-stat и пустые подпись/значение. Это не отсутствие данных Item: его system.value в проверке был задан. При совпадении имени со встроенным ключом обработчик будет выбирать встроенный навык; уникальный ID Item не передаётся.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение и поток контекста | 23 строки; _prepareCustomSkills → tab-skills → partial → skillListener | Разрыв Item.system против skill.* и Item ID против builtin key | Модель и producer проверены до определений |
| Настоящий Handlebars и обработчик | SkillItemData с именем, attribute, value; реальный родитель; вызов привязанного handler | Две пустые строки, Item.name в data-skill; неизвестный ключ вызывает TypeError в rollSkillCheck | Оболочка embedded Item и привязка DOM контролируются; мир не запускался |

## Непроверенные участки и открытые вопросы

Поведение сторонних листов/модулей и макросов неизвестно. Предлагаемый способ исправления не выбирался; карточка описывает существующий путь и точное рассогласование.

## Связанные проблемы

[issue-00187](../../../../../../issues/potential/issue-00187.md). Одна общая проблема включает неверное отображение и ошибочную маршрутизацию броска; дубли не создавались.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |
