# templates/dialog/verbal-combat.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/dialog/verbal-combat.hbs](../../../../../../templates/dialog/verbal-combat.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, a69f11d2e4c4318cfbf635dabad97b0062c63c20 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.046](../../../../../tasks/task-0003.046.md), 5 файлов / 301 логических строк; данный файл — 14 |
| Запись перекрёстной сверки | [TASK-0003.046](../../../review-log.md#task-0003046) |

## Назначение файла

Выводит все группы действий словесного боя в radio-списке и текстовое поле пользовательского модификатора.

## Условия использования

[module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js) загружает путь systems/TheWitcherTRPG/templates/dialog/verbal-combat.hbs и передаёт {verbalCombat:CONFIG.WITCHER.verbalCombat}. HTML становится content у DialogV2.prompt. Сам шаблон не содержит form: оболочку окна задаёт Foundry.

## Введённые сущности и действия с ними

| Сущность | Вид / место | Действие |
| --- | --- | --- |
| h1 / div / h2 | Разметка:1–4 | Общий заголовок и название каждой группы |
| each verbalCombat as groupData groupName | Цикл:3–12 | Пять групп в порядке CONFIG |
| each groupData as verbalData verbalName | Цикл:5–11 |16 действий; name берётся из entry |
| input[name=verbalCombat] | Radio:7–8 | id/value=verbalName, data-group=groupName, атрибут checked у каждого |
| label[for=verbalName] | label:9 | Локализованное имя действия |
| input[name=customModifiers] | Текстовое поле:13 | Начальное value0; type не задан |
| concat / localize | Helpers:1,4,9,13 | Имена групп, действий, общая подпись |

## Основные функции и методы

JS-функций нет. Два вложенных each и concat формируют список, localize получает ключи WITCHER.verbalCombat.Title, `WITCHER.verbalCombat.<groupName>`, verbalData.name и WITCHER.Dialog.customModifier. Core concat возвращает SafeString; здесь он объединяет ключи локализации, а не пользовательский HTML. Значения input/label не заключены в кавычки в исходной разметке; текущие ключи CONFIG состоят из подходящих простых имён.

## Используемые сущности и зависимости

| Сущность | Источник | Связь / основание |
| --- | --- | --- |
| verbalCombat | [module/setup/config.js](../../../../../../module/setup/config.js) |5 групп/16 записей; таблица skill/damage — в [карточке producer](../../module/actor/mixins/verbalCombatMixin.js.md) |
| renderTemplate / form callback | [module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js) | Передача контекста; чтение checked radio и customModifiers |
| localize / concat / each | Foundry14.367.0 / Handlebars; client/applications/handlebars.mjs:199 | Настоящие Handlebars и извлечённый concat; локализация через словари |
| Ключи перевода | [lang/en.json](../../../../../../lang/en.json), [lang/ru.json](../../../../../../lang/ru.json) | Группы, имена и customModifier; последний отсутствует в ru, en fallback |
| radio id/value/name/data-group | DOM | Граница обратного чтения; producer ищет radio глобальным document.querySelector |

## Известные потребители

Единственный найденный прямой renderTemplate — [module/actor/mixins/verbalCombatMixin.js](../../../../../../module/actor/mixins/verbalCombatMixin.js). [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) использует то же имя radio при глобальном поиске, поэтому является пересекающимся DOM-consumer, но этот HBS не загружает. Список найден поиском module/templates.

## Данные и изменения состояния

Создаёт HTML, не пишет Actor/flags. В сырой разметке checked есть у всех 16 radio. Какое поле окажется выбранным после полноценного browser form lifecycle, в этой проверке не устанавливалось. Повторяющиеся id/name разных окон и глобальный поиск позволяют смешать выбор одного окна с модификатором другого; проблема в границе callback, не в CONFIG арифметике.

## Проверки и доказательства

Группы 01/24: настоящий Handlebars/core concat отрисовал 16 radio и 5 h2 с en/ru названиями; checked присутствует 16 раз. Группа 05: submitted form содержит Seduce/custom4, но глобальный radio Intimidate приводит к броску Intimidate с+4. Группа 26: ключ customModifier отсутствует в ru, присутствует в en. parse5 проверяет структуру, не интерактивное поведение radio.

## Непроверенные участки и открытые вопросы

Вся разметка прочитана (14 логических строк, завершающего newline нет). Не проверялись браузерная нормализация checked, клики label, CSS/расположение окна и сторонние группы CONFIG. Выбор начального действия и изменение механики не согласовывались.

## Связанные проблемы

[303](../../../../../issues/potential/issue-00303.md) — общий глобальный radio; [186](../../../../../issues/potential/issue-00186.md) — существующий пропуск русской подписи. Новых самостоятельных правил выбора/нумерации действий не вводилось.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | a69f11d2e4c4318cfbf635dabad97b0062c63c20; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003046) |
