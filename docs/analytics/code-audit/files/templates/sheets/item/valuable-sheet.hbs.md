# templates/sheets/item/valuable-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/valuable-sheet.hbs](../../../../../../../templates/sheets/item/valuable-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

## Назначение файла

Основная форма Item valuable; включает общий item-header и собственные поля предмета.

## Условия использования

Путь указан в WitcherValuableSheet.PARTS.main. Контекст приходит через WitcherItemSheet._prepareContext и override специализированного листа; обычные поля формы сохраняет унаследованный DocumentSheet, не HBS.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Корневой section.scrollable / item-header | HTML и partial | Основная область и общие поля/действия | PARTS.main | Рендер |
| Тип/доступность/скрытность | select | system.type; system.avail; system.conceal | selects.type / config.Availability / config.Concealment | Именованные поля |
| Описание | textarea, rows=5 | system.description | ValuableData/CommonItemData | Текст |

## Основные функции и методы

Собственных JavaScript-функций и методов нет. Шаблон использует selectOptions, localize; общий header дополнительно использует системные helpers. Собственные поля: type, avail, conceal, description. Настройки расходования открываются общей кнопкой configureItem из header, а не полями основного шаблона.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherValuableSheet | [module/item/sheets/WitcherValuableSheet.js](../../../../../../../module/item/sheets/WitcherValuableSheet.js) | Контекст / регистрация PARTS | item, config, selects | Определение и обращение сверены |
| Модель system | [module/data/item/valuableData.js](../../../../../../../module/data/item/valuableData.js) | Контракт полей | Именованные system.* | Определение и обращение сверены |
| item-header | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | Прямое включение partial | img/name/quantity/weight/sourcebook/configureItem; cost либо type | Определение и обращение сверены |
| Общий обработчик формы / configureItem | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Наследование поведения | Сохранение и открытие configuration | Определение и обращение сверены |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../module/setup/config.js) | Данные через контекст | Availability/Concealment, когда использованы; категории задаёт лист | Определение и обращение сверены |
| WITCHER.* | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи и словари листа | Определение и обращение сверены |
| Handlebars helpers | Foundry Handlebars API | Внешний API | if/each/selectOptions/localize по используемым блокам | Определение и обращение сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherValuableSheet.js](../../../../../../../module/item/sheets/WitcherValuableSheet.js) | Этот шаблон | PARTS.main.template | Прямой путь |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Шаблон не запускает consume и не списывает количество. effect/quality определены в модели, но в этой основной форме не выведены. Стандартная настройка добавляет system.clickableImage в header; связанный разрыв схемы уже описан в issue-00063.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Полный HBS и item-header; все варианты контекста | Все собственные поля сопоставлены со схемой и sheet | Не весь файл зависимости получает новый статус |
| HTML/контекст | Настоящий Handlebars + parse5; настоящие _prepareContext | 7 категорий: по 10 именованных полей | selectOptions — ограниченный генератор; реальный DocumentSheet/сохранение не запускались |

## Непроверенные участки и открытые вопросы

Браузер, CSS, права пользователя и фактический submit не проверялись. Наличие текстового поля не означает автоматического выполнения описанного эффекта. Для mutagen выбор типа найден в общем header, а не объявлен отсутствующим.

## Связанные проблемы

[issue-00091](../../../../../../issues/potential/issue-00091.md), [issue-00092](../../../../../../issues/potential/issue-00092.md), [issue-00063](../../../../../../issues/potential/issue-00063.md). Связанные проблемы configuration/header; самостоятельной логики применения в HBS нет.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
