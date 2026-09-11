# templates/dialog/investigation/chooseEvidenceSkill.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/dialog/investigation/chooseEvidenceSkill.hbs](../../../../../../../templates/dialog/investigation/chooseEvidenceSkill.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../review-log.md#task-0003023) |

## Назначение файла

Содержимое DialogV2 для выбора одного из навыков, разрешённых уликой. Передаёт выбранное строковое имя через select name='selectedSkill'.

## Условия использования

rollClue загружает шаблон только при availableSkills.length > 1 с контекстом {skills}. Кнопки выбора/отмены создаются JavaScript-конфигурацией DialogV2, в HBS кнопок нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| form / cssClass / autocomplete | 1 | Контейнер содержимого | cssClass не передаётся rollClue, становится пустым | Структура HTML; autocomplete off |
| WITCHER.Investigation.evidence.chooseSkill | 2 | Заголовок | localize | Ключ есть в en/ru |
| selectedSkill | select, 4–6 | Выбранное имя | name='selectedSkill' | Читается button.form.elements.selectedSkill.value |
| selectOptions skills | 5 | Список вариантов | valueAttr=name, labelAttr=label, nameAttr=name, localize=true | selected/default в шаблоне не заданы |

## Основные функции и методы

Программных методов нет. selectOptions преобразует переданный массив описаний в option. Чтение value и политика отмены целиком находятся в rollClue/DialogV2.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| rollClue | [module/scripts/investigation/rollClue.js](../../../../../../../module/scripts/investigation/rollClue.js) | Поставщик/обратный вызов | {skills}; selectedSkill callback | CONFIG.WITCHER.skillMap lookup в reduce |
| localize / selectOptions | Foundry 14.367.0, client/applications/handlebars.mjs:460–500; forms/fields.mjs:290–360 | Handlebars helpers | Подписи и <option> | Исполнены настоящие selectOptions/prepareSelectOptionGroups; запись DOM заменена HTML-фасадом |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../module/setup/config.js) | Контекст skills | name/valueAttr/labelAttr | name — ключ передаваемого навыка; label — ключ перевода |
| WITCHER.Investigation.evidence.chooseSkill | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи полей | Статические ключи этого шаблона найдены в en/ru; динамические label picklock/trapcraft — issue-00016 |
| DialogV2._onSubmit/wait | Foundry 14.367.0, client/applications/api/dialog.mjs:261–276, 405–428 | Диалог/результат | Возврат имени либо action/null | Настоящие методы проверены в группе 05 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/scripts/investigation/rollClue.js](../../../../../../../module/scripts/investigation/rollClue.js) | chooseEvidenceSkill.hbs | renderTemplate | 20–23 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Шаблон не читает clueItem напрямую, не проверяет выбранный навык и не запускает бросок. Неизвестное имя в массиве skillsUsed превращается в undefined в JavaScript-поставщике; ядро selectOptions/prepareSelectOptionGroups с valueAttr=name не даёт такой записи пригодного имени, DOM-фасад не выводит option без value/label. При всех неизвестных именах список пуст. Сохранение выбора не является изменением skillsUsed.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Варианты | Группы 06/09 | Два известных навыка доступны; известный+undefined оставляет известный; два undefined дают пустой список | Настоящие helpers, HTML-append заменён фасадом по условиям _appendOption ядра |
| Отмена/закрытие | Группы 05/07 | 'cancel'/null доходят до rollSkill из JavaScript | Сам шаблон не определяет поведение кнопок |

## Непроверенные участки и открытые вопросы

Все 8 строк прочитаны. Реальное окно и принадлежность select вложенным form не исполнялись; вывод о сбое формы не делается. Клавиатурный выбор и поведение пустого select браузера не проверялись.

## Связанные проблемы

[issue-00016](../../../../../../issues/potential/issue-00016.md) — подписи picklock/trapcraft в общем словаре навыков; группа 17. [issue-00148](../../../../../../issues/potential/issue-00148.md), [issue-00150](../../../../../../issues/potential/issue-00150.md). Отмена не проверяется вызывающим кодом; неизвестные навыки не валидируются до построения списка.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003023) |
