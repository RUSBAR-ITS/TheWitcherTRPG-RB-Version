# templates/sheets/item/alchemical-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/alchemical-sheet.hbs](../../../../../../../templates/sheets/item/alchemical-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

## Назначение файла

Основная форма Item alchemical; включает общий item-header и собственные поля предмета.

## Условия использования

Путь указан в WitcherAlchemicalSheet.PARTS.main. Контекст приходит через WitcherItemSheet._prepareContext и override специализированного листа; обычные поля формы сохраняет унаследованный DocumentSheet, не HBS.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Корневой section.scrollable / item-header | HTML и partial | Основная область и общие поля/действия | PARTS.main | Рендер |
| Категория/доступность | select | system.type / system.avail | config.type / config.Availability | Именованные поля |
| Длительность/токсичность | input text | system.time; system.toxicity только potion/decoction | Данные AlchemicalData | Текстовые свойства |
| Описание воздействия | textarea, rows=10 | system.effect | Данные AlchemicalData | Текст, не коллекция эффектов |

## Основные функции и методы

Собственных JavaScript-функций и методов нет. Шаблон использует or/eq, selectOptions, localize; общий header дополнительно использует системные helpers. Собственные поля: type, avail, time, effect; toxicity только для potion/decoction. Настройки расходования открываются общей кнопкой configureItem из header, а не полями основного шаблона.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherAlchemicalSheet | [module/item/sheets/WitcherAlchemicalSheet.js](../../../../../../../module/item/sheets/WitcherAlchemicalSheet.js) | Контекст / регистрация PARTS | item, config | Определение и обращение сверены |
| Модель system | [module/data/item/alchemicalData.js](../../../../../../../module/data/item/alchemicalData.js) | Контракт полей | Именованные system.* | Определение и обращение сверены |
| item-header | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | Прямое включение partial | img/name/quantity/weight/sourcebook/configureItem; cost либо type | Определение и обращение сверены |
| Общий обработчик формы / configureItem | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Наследование поведения | Сохранение и открытие configuration | Определение и обращение сверены |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../module/setup/config.js) | Данные через контекст | Availability/Concealment, когда использованы; категории задаёт лист | Определение и обращение сверены |
| WITCHER.* | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи и словари листа | Определение и обращение сверены |
| Handlebars helpers | Foundry Handlebars API | Внешний API | if/each/selectOptions/localize по используемым блокам | Определение и обращение сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherAlchemicalSheet.js](../../../../../../../module/item/sheets/WitcherAlchemicalSheet.js) | Этот шаблон | PARTS.main.template | Прямой путь |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Шаблон не запускает consume и не списывает количество. toxicity и time редактируются строками и не задают автоматически механику consume. Условия potion/decoction управляют только видимостью toxicity.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Полный HBS и item-header; все варианты контекста | Все собственные поля сопоставлены со схемой и sheet | Не весь файл зависимости получает новый статус |
| HTML/контекст | Настоящий Handlebars + parse5; настоящие _prepareContext | 4 категории: 9/10/10/9 именованных полей | selectOptions — ограниченный генератор; реальный DocumentSheet/сохранение не запускались |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-01](../../../../cross-check-0002.md#u007-01), [U007-04](../../../../cross-check-0002.md#u007-04), [U007-08](../../../../cross-check-0002.md#u007-08). Для этого файла установлены процессы R007-02, R007-01, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00091](../../../../../../issues/potential/issue-00091.md), [issue-00092](../../../../../../issues/potential/issue-00092.md). Связанные проблемы configuration/header; самостоятельной логики применения в HBS нет.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Главный HBS alchemical включает общую шапку и поля модели; time/toxicity зависят от type. Настройка consumable располагается в отдельной configuration, а не в основном HBS. Текстовое значение поля не доказывает автоматического срока/токсичности.

Сопоставленные определения и потребители: [module/item/sheets/WitcherAlchemicalSheet.js](../../../module/item/sheets/WitcherAlchemicalSheet.js.md), [module/data/item/alchemicalData.js](../../../module/data/item/alchemicalData.js.md), [templates/partials/item-header.hbs](../../partials/item-header.hbs.md), [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js.md), [module/setup/config.js](../../../module/setup/config.js.md), [lang/ru.json](../../../lang/ru.json.md).

[Протокол и границы](../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-02](../../../../cross-check-0002.md#r007-02), [R007-01](../../../../cross-check-0002.md#r007-01). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
