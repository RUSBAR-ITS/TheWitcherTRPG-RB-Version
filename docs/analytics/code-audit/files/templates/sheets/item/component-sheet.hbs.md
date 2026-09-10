# templates/sheets/item/component-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/component-sheet.hbs](../../../../../../../templates/sheets/item/component-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../review-log.md#task-0003016) |

## Назначение файла

Основная форма компонента: категория, тип субстанции и описательные поля материала.

## Условия использования

PARTS.main WitcherComponentSheet указывает этот HBS. item/config приходят из общего WitcherItemSheet. Включается item-header; собственные обычные поля сохраняет унаследованная форма.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section / item-header | HTML и partial | Корень class=item.type/scrollable и общая шапка | PARTS.main | Рендер |
| system.type | select | crafting-material, animal-parts, alchemical, minerals, substances | Модель ComponentData | Редактирование категории |
| system.substanceType | Условный select | config.substanceTypes только при type=substances | 9 типов субстанций | Выбор |
| system.rarity | select | config.Availability | ComponentData | Доступность |
| system.location / quantityObtainable / forage | Три input type=text | Текстовые сведения | ComponentData | Ввод |

## Основные функции и методы

JavaScript-методов нет. Используются localize, eq, if, each и три блока {{#select}} (type, substanceType, rarity). Собственных обработчиков/data-action нет. В Foundry 14.367 core initialize не регистрирует helper select, система его также не добавляет; первый безусловный блок останавливает рендер. selectOptions — другой существующий helper, автоматически это имя не заменяет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherComponentSheet / WitcherItemSheet | [module/item/sheets/WitcherComponentSheet.js](../../../../../../../module/item/sheets/WitcherComponentSheet.js); [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | PARTS и контекст | item/config, обработка формы | Источник и использование сверены |
| ComponentData | [module/data/item/componentData.js](../../../../../../../module/data/item/componentData.js) | Контракт полей | Шесть собственных полей | Источник и использование сверены |
| item-header | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | Прямое включение | Имя/изображение/quantity/weight/cost/sourcebook/configuration | Источник и использование сверены |
| CONFIG.WITCHER.substanceTypes / Availability | [module/setup/config.js](../../../../../../../module/setup/config.js) | Данные контекста | Два набора options | Источник и использование сверены |
| eq и прочие системные helpers | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Регистрация helpers | Условия; select не зарегистрирован | Источник и использование сверены |
| WITCHER.* | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи и options | Источник и использование сверены |
| select/localize/each/if | Foundry Handlebars API, /opt/foundryvtt/client/applications/handlebars.mjs | Внешний API | select отсутствует в V14.367 | Источник и использование сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherComponentSheet.js](../../../../../../../module/item/sheets/WitcherComponentSheet.js) | Этот HBS | PARTS.main.template | Прямой путь |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Форма изменяет строковые значения модели через стандартный submit, не запускает добычу или изготовление. В сравнении с общим Item.type=component поле system.type — подкатегория. substanceType сохраняется в данных и при скрытом selector; собственных очисток при смене категории нет. Стандартная настройка clickableImage не включает component.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Штатный набор helpers | Основной HBS, реальный Handlebars, реестры ядра и системы | Missing helper: select до завершения формы | Полного браузера нет |
| Изучение остальных блоков | Временный изолирующий select, возвращающий тело блока без выбора options | 5 категорий: 10/10/10/10/11 именованных полей; substances добавляет substanceType | Это подмена для анализа, не успешный штатный рендер/исправление |
| Схема и локализация | Собственные поля/словари и раскрытые en/ru JSON | Именованные поля существуют в модели, ключи формы найдены | Не интерактивный submit |

## Непроверенные участки и открытые вопросы

Без стороннего helper форма остаётся неисправной в проверенном наборе API. Выбор активного option с временным helper не проверялся и не утверждается. CSS, ширина окна, права и запись не исполнялись.

## Связанные проблемы

[issue-00094](../../../../../../issues/potential/issue-00094.md). Ошибка совместимости helper подтверждена изолированным рендером.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
