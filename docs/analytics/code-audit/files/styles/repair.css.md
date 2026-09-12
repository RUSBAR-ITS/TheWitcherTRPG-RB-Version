# styles/repair.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/repair.css](../../../../../styles/repair.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 23 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Выравнивание сводки ремонта и два независимых ограничения высоты прокручиваемых частей диалога.

## Условия использования

Импорт 23, после special-skill-table.css и до components-list.css. Общая шапка задаёт .information text-align:center по наследованию; прямые td:first/last правила repair побеждают наследуемое выравнивание. CSS чата repair-message-section расположен отдельно, у него нет корня .repair.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 5 CSS-правил и 8 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `table.repair-info td:first-child` | 1 | `text-align: left` |
| `table.repair-info td:last-child` | 5 | `text-align: right` |
| `table.repair-info td` | 9 | `font-weight: bold`; `font-size: 1.15em` |
| `.repair .components-list-container` | 15 | `overflow-y: scroll`; `max-height: calc(60vh - 50px)` |
| `.repair general` | 20 | `overflow-y: scroll`; `max-height: calc(25vh)` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

В table.repair-info первая td выравнивается влево, последняя вправо; все td bold и 1.15em. Если ячейка одновременно первая/последняя, более позднее last-child победит при равной специфичности. .repair .components-list-container имеет overflow-y:scroll и max-height:calc(60vh - 50px); .repair general — scroll и max-height:calc(25vh). Это ограничения отдельных областей, не вычисление общей высоты окна. general — нестандартный тег реально присутствующего HBS.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/dialog/repair-dialog.hbs](../../../../../templates/dialog/repair-dialog.hbs) | repair, general, table.information.repair-info | Сводка сложности/повреждений. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/partials/components-list.hbs](../../../../../templates/partials/components-list.hbs) | components-list-container | Вложенная прокручиваемая таблица материалов. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/item/systems/repair.js](../../../../../module/item/systems/repair.js) | prepareDialogTemplate/prepareData | Контекст и открытие окна; арифметика в Repair/RepairData. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [styles/item-header.css](../../../../../styles/item-header.css) | information/general/item-header-tablerow | Flex и размеры шапки комбинируются с ограничением высоты. | Исходники, поиск module/templates/styles и AST; границы ниже |



## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/dialog/repair-dialog.hbs](../../../../../templates/dialog/repair-dialog.hbs) | repair, general, table.information.repair-info | Сводка сложности/повреждений. |
| [templates/partials/components-list.hbs](../../../../../templates/partials/components-list.hbs) | components-list-container | Вложенная прокручиваемая таблица материалов. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 5 правил, 8 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | 5 правил / 8 declarations. Группа 12 проверила соответствие исходной разметке и наличие двух разных контейнеров. Код расчёта/обычного ремонта с ранее известными блокировками не запускался. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | Импорт 23, после special-skill-table.css и до components-list.css. Общая шапка задаёт .information text-align:center по наследованию; прямые td:first/last правила repair побеждают наследуемое выравнивание. CSS чата repair-message-section расположен отдельно, у него нет корня .repair. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы.

## Связанные проблемы

Новой проблемы в пределах данного файла не зарегистрировано. Это не вывод об исправности всех связанных процессов.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |
