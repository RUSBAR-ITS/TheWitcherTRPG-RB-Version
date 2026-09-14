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

Исходник и связи сопоставлены в TASK-0004.010. Штатный перевод/fallback, browser sanitization и реальная отрисовка не исполнялись; старый localize был фасадом. Остаток: [U010-03](../../../../../cross-check-0002.md#u010-03), [U010-06](../../../../../cross-check-0002.md#u010-06). Прежние опыты сохраняют свои даты и фасады; нового исполнения нет.

## Связанные проблемы

Собственная новая проблема не зарегистрирована. [docs/issues/potential/issue-00033.md](../../../../../../../issues/potential/issue-00033.md) относится к числовой формуле производителя, которую этот фрагмент не вычисляет.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 16695cbfc7fec3e0de56660c7cab21bc0304e94b; полный файл | Первичная карточка; [перекрёстная сверка](../../../../../review-log.md#task-0003042) |

## Сквозная сверка TASK-0004.010

2026-09-14; rusbar-main, ac3978e901dd3549639225028f79aca54d1ace2f. Исходник совпадает со срезом TASK-0001; изменено только описание.

Producer передаёт defenseName и displayFormula; последний описывает основу, не все модификаторы или замену на10 при stun. Сопоставлены стандартная и профессиональная подписи, экранирование HBS и отдельные crit/stun append. HTML не является хранилищем критического объекта или результата броска.

Сопоставленные определения и потребители: [module/actor/mixins/defenseMixin.js](../../../../module/actor/mixins/defenseMixin.js.md), [module/setup/config.js](../../../../module/setup/config.js.md), [module/data/item/professionData.js](../../../../module/data/item/professionData.js.md), [lang/en.json](../../../../lang/en.json.md), [lang/ru.json](../../../../lang/ru.json.md), [module/chatMessage/chatMessageData.js](../../../../module/chatMessage/chatMessageData.js.md).

[Протокол и границы](../../../../../review-log.md#task-0004010) — TASK-0004.010; процессы [R010-09](../../../../../cross-check-0002.md#r010-09), [R010-12](../../../../../cross-check-0002.md#r010-12). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
