# templates/chat/combat/defense/defense.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/combat/defense/defense.hbs](../../../../../../../../templates/chat/combat/defense/defense.hbs) |
| Тип файла | Handlebars / HTML |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 16695cbfc7fec3e0de56660c7cab21bc0304e94b |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.042](../../../../../../../tasks/task-0003.042.md), 5 файлов / 477 логических строк; данный файл — 2 |
| Запись перекрёстной сверки | [TASK-0003.042](../../../../../review-log.md#task-0003042) |

## Назначение файла

Базовый фрагмент сообщения защиты: локализованное название и пояснение основы формулы.

## Условия использования

[module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js):183–191 вызывает renderTemplate после построения числовой формулы, но до extendedRoll. Фрагмент передаётся в ChatMessageData(this,...,'defense',...). В этом файле не создаётся документ и не назначаются обработчики.

## Введённые сущности и действия с ними

| Узел | Строка | Назначение |
| --- | --- | --- |
| h1 | 1 | localize('WITCHER.Defense.name'), затем localize(defenseName) |
| p | 2 | Экранированный displayFormula; числовое вычисление не выполняется |

## Основные способы использования

JS-функций, partial, условий, полей ввода, script и кнопок нет. Шаблон выводит два входных поля. defenseName — label стандартного способа либо skillOverride.skillMapEntry.label. displayFormula собран заранее из 1d10 и названий характеристики/навыка; модификаторы и замена на 10[Stun] в него не переносятся. Его нельзя принимать за полную фактическую формулу броска.

## Используемые сущности и зависимости

| Сущность | Источник | Связь / основание |
| --- | --- | --- |
| defenseName/displayFormula | [module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js) | Явный контекст renderTemplate |
| defenseAction.label / skillMapEntry.label/attribute.labelShort | [module/setup/config.js](../../../../../../../../module/setup/config.js), [module/data/item/professionData.js](../../../../../../../../module/data/item/professionData.js) | Источники названий; профессию выбирает override |
| localize | Foundry Handlebars, [lang/en.json](../../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../../lang/ru.json) | Статический WITCHER.Defense.name и динамический defenseName; исходные helpers системы не импортируются |
| renderTemplate/ChatMessageData | Foundry 14.367.0, [module/chatMessage/chatMessageData.js](../../../../../../../../module/chatMessage/chatMessageData.js) | Доставка HTML в flavor через производителя |
| h1/p | Браузер/Foundry CSS | Собственных CSS-классов в шаблоне нет; полный каскад не проверен |

## Известные потребители

Единственный найденный путь загрузки — [module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js). Дальнейшие crit/stun-фрагменты дописываются отдельно. Поиск выполнен по module/templates.

## Данные и изменения состояния

Выход — HTML-строка, без записи Actor/Item/ChatMessage. Обе динамические строки экранируются обычной вставкой Handlebars. Документ сообщения и rollTotal формируются другими файлами.

## Проверки и доказательства

Прочитаны обе логические строки (последняя без LF). Группы 01/06 [сверки .042](../../../../../review-log.md#task-0003042) проверили контекст штатной и профессиональной защиты. Группа 27: настоящий Handlebars экранирует `defenseName='<x>'` и `displayFormula='1d10 < 5'`. localize — фасад возвращения ключа, поэтому тест не проверяет перевод.

## Непроверенные участки и открытые вопросы

Непрочитанных участков нет. Локализация через expandObject/fallback, визуальная отрисовка и очистка HTML реальным клиентом не запускались. Неполный displayFormula описан как текущее назначение, отдельным дефектом без подтверждения ожидания не объявлен.

## Связанные проблемы

Собственная новая проблема не зарегистрирована. [docs/issues/potential/issue-00033.md](../../../../../../../issues/potential/issue-00033.md) относится к числовой формуле производителя, которую этот фрагмент не вычисляет.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 16695cbfc7fec3e0de56660c7cab21bc0304e94b; полный файл | Первичная карточка; [перекрёстная сверка](../../../../../review-log.md#task-0003042) |
