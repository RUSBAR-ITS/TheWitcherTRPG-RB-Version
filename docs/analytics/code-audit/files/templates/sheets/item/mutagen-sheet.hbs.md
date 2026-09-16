# templates/sheets/item/mutagen-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/mutagen-sheet.hbs](../../../../../../../templates/sheets/item/mutagen-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Основная форма Item mutagen; включает общий item-header и собственные поля предмета.

## Условия использования

Путь указан в WitcherMutagenSheet.PARTS.main. Контекст приходит через WitcherItemSheet._prepareContext и override специализированного листа; обычные поля формы сохраняет унаследованный DocumentSheet, не HBS.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Корневой section.scrollable / item-header | HTML и partial | Основная область и общие поля/действия | PARTS.main | Рендер |
| Источник/описание | Два input text | system.source; system.effect | MutagenData | Именованные поля |
| Сложность/малая мутация | input text | system.alchemyDC; system.minorMutation | MutagenData | alchemyDC приводится NumberField при обработке моделью |

## Основные функции и методы

Собственных JavaScript-функций и методов нет. Шаблон использует localize; общий header дополнительно использует системные helpers. Собственные поля: source, effect, alchemyDC, minorMutation. Цвет намеренно следует проверять в partial: при item.type=='mutagen' он выводит system.type вместо cost.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherMutagenSheet | [module/item/sheets/WitcherMutagenSheet.js](../../../../../../../module/item/sheets/WitcherMutagenSheet.js) | Контекст / регистрация PARTS | item, config | Определение и обращение сверены |
| Модель system | [module/data/item/mutagenData.js](../../../../../../../module/data/item/mutagenData.js) | Контракт полей | Именованные system.* | Определение и обращение сверены |
| item-header | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | Прямое включение partial | img/name/quantity/weight/sourcebook/configureItem; cost либо type | Определение и обращение сверены |
| Общий обработчик формы / configureItem | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Наследование поведения | Сохранение и открытие configuration | Определение и обращение сверены |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../module/setup/config.js) | Данные через контекст | Availability/Concealment, когда использованы; категории задаёт лист | Определение и обращение сверены |
| WITCHER.* | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Подписи и словари листа | Определение и обращение сверены |
| Handlebars helpers | Foundry Handlebars API | Внешний API | if/each/selectOptions/localize по используемым блокам | Определение и обращение сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherMutagenSheet.js](../../../../../../../module/item/sheets/WitcherMutagenSheet.js) | Этот шаблон | PARTS.main.template | Прямой путь |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Шаблон не запускает consume и не списывает количество. Под собственными полями нет isConsumable/consumeProperties. Color selector исправен. Стандартная настройка clickableImageItemTypes добавляет в header checkbox system.clickableImage; отсутствующее поле модели описано ранее в issue-00063.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | Полный HBS и item-header; все варианты контекста | Все собственные поля сопоставлены со схемой и sheet | Не весь файл зависимости получает новый статус |
| HTML/контекст | Настоящий Handlebars + parse5; настоящие _prepareContext | 3 цвета: по 10 именованных полей; ровно один selector system.type из header | selectOptions — ограниченный генератор; реальный DocumentSheet/сохранение не запускались |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-01](../../../../cross-check-0002.md#u007-01), [U007-08](../../../../cross-check-0002.md#u007-08). Для этого файла установлены процессы R007-02, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00093](../../../../../../issues/potential/issue-00093.md), [issue-00063](../../../../../../issues/potential/issue-00063.md). Связанные проблемы configuration/header; самостоятельной логики применения в HBS нет.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Главный HBS мутагена содержит поля его модели и общий header с выбором типа. Отсутствие consumable controls здесь не единственная причина: штатный sheet не создаёт специализированную configuration. Наличие модели consumable не означает доступную настройку или автоматизацию мутации.

Сопоставленные определения и потребители: [module/item/sheets/WitcherMutagenSheet.js](../../../module/item/sheets/WitcherMutagenSheet.js.md), [module/data/item/mutagenData.js](../../../module/data/item/mutagenData.js.md), [templates/partials/item-header.hbs](../../partials/item-header.hbs.md), [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js.md), [module/setup/config.js](../../../module/setup/config.js.md), [lang/ru.json](../../../lang/ru.json.md).

[Протокол и границы](../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-02](../../../../cross-check-0002.md#r007-02). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
