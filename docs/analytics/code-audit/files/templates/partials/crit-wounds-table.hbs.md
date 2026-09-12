# templates/partials/crit-wounds-table.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/crit-wounds-table.hbs](../../../../../../templates/partials/crit-wounds-table.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.020](../../../../../tasks/task-0003.020.md), 10 файлов, 428 логических строк |
| Запись перекрёстной сверки | [TASK-0003.020](../../../review-log.md#task-0003020) |

## Назначение файла

Краткая таблица принадлежащих Actor критических травм с ручным счётчиком дней и кнопкой перехода к следующей травме.

## Условия использования

Предзагружается preloadHandlebarsTemplates. В текущих templates найдено включение в tab-effects.hbs, используемый современными CharacterSheet и MonsterSheet. Контекст — document.items.documentsByType.criticalWound и config.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| each critWound i / li.item | 3–4, 39 | Одна строка на Item | data-item-id=critWound.id; data-type=critWound; draggable | i далее не используется; uuid отведён кнопке |
| name/уровень/лечение/локация | 8–19 | Краткое состояние | localize + lookup ../config.* | Описание и изображение не выводятся |
| days-healed inline-edit | 22–30 | Редактирование дней и показ срока | data-field=system.daysHealed; type=number; data-dtype=Number; healingTime disabled | name у inline input отсутствует — нужен специальный обработчик |
| treatCriticalWound | 35–37 | Ручной переход/удаление Item | data-action=treatCriticalWound; data-id=critWound.uuid | Это вызов модели, не установка treatment |

## Основные функции и методы

JavaScript-функций и обработчиков файл не определяет. Handlebars только формирует разметку; выполнение действий и сохранение находятся в перечисленных потребителях.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Схема/вычисления | [module/data/item/criticalWoundData.js](../../../../../../module/data/item/criticalWoundData.js) | Чтение полей | Вся строка | healingTime пересчитан на BODY.max; дни — текущее значение модели |
| critLevel/critTreatment/location | [module/setup/config.js](../../../../../../module/setup/config.js) | Lookup словарей | 12–18 | Локализованные подписи для ключей полей |
| criticalWoundListener/_onTreat | [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) | Событие click | 35–37 | fromUuidSync(data-id) → system.treat |
| _onItemInlineEdit | [module/actor/sheets/mixins/itemMixin.js](../../../../../../module/actor/sheets/mixins/itemMixin.js) | Событие изменения input | 25–26 | Берёт closest('.item').dataset.itemId; update({[data-field]:value}) |
| localize/lookup/each; DocumentCollection | Foundry 14.367.0 / Handlebars 4.7.9 | Внешние helpers/коллекция | documentsByType и рендер | HBS исполнен через Handlebars, HTML разобран parse5 |
| Ключи локализации и CSS | [lang/en.json](../../../../../../lang/en.json); [lang/ru.json](../../../../../../lang/ru.json); [styles/crit-wounds-table.css](../../../../../../styles/crit-wounds-table.css) | Текст/стили | Подписи и обёртки | Ключи en/ru найдены; CSS только сопоставлен |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Путь partial | preloadHandlebarsTemplates, 29 | Предзагрузка, не самостоятельный экран |
| [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | Весь partial | Включение 8, затем повторный собственный цикл | Одна коллекция показана дважды |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Одна строка partial не создаёт/не копирует травму. Вкладка эффекта дополнительно повторяет строки с обогащённым описанием, поэтому один Item виден дважды. Inline-edit передаёт строку: data-dtype не преобразует её в пользовательском обработчике, но NumberField модели очищает '2.5' в 2.5. Это не обнаруженная ошибка типа сохранения. Общие действия редактирования/удаления Item определены вне таблицы.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Partial и родитель | Настоящие HBS + Handlebars/parse5; одна травма | Partial: одна строка; tab-effects: две строки и две кнопки лечения | Не два Item и не доказательство двойного вызова по одному клику |
| Inline-счётчик | Исходный _onItemInlineEdit + настоящая CriticalWoundData | Запрос system.daysHealed='2.5'; модель принимает числом 2.5 | БД и валидация HTML number в браузере не запускались |

## Непроверенные участки и открытые вопросы

Все 40 строк прочитаны. Не проверялись контекстное меню, реальный drag, перерисовка и конкурентное изменение двух полей одного Item.

## Связанные проблемы

[issue-00054](../../../../../issues/potential/issue-00054.md), [issue-00122](../../../../../issues/potential/issue-00122.md). Подтверждено прежнее наблюдение двойного показа; ручные дни попадают в сравнение срока вне проверки treatment.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b09f992960a76d1c75946f402e42d93fa0785008`; полный файл | Первая карточка; [сверка порции и второй серии](../../../review-log.md#task-0003020) |

## Дополнительная сверка TASK-0003.047

2026-09-12, rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; исходники не изменены.

[CSS травм](../../styles/crit-wounds-table.css.md) разобран полностью. Несмотря на имя partial, его корень — ol, класса crit-wounds-table у разметки нет; правила tbody/tr этого CSS не адресуют текущий список. Работают critwound/header/info/days-rest и ширины 40px!important дней/срока. Группа 11 снова получила две строки одного Item в полном tab-effects и одну пару полей в Item-редакторе; [54](../../../../../issues/potential/issue-00054.md) уточнена без нового дубля. Само лечение, inline-save и вычисление healingTime повторно не исполнялись.

[Сценарии, результаты и ограничения](../../../review-log.md#task-0003047). Связанные файлы повторно не засчитываются в покрытие.
