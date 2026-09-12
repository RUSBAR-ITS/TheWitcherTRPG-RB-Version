# styles/components-list.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/components-list.css](../../../../../styles/components-list.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 20 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Таблица материалов ремонта и оформление итоговой цены, в том числе строки цены в сообщении ремонта.

## Условия использования

Импорт 24, после repair.css (23) и tab-inventory.css (7). Раннее table th задаёт text-align:left; th:nth-child(n+2) имеет большую специфичность (0,1,1 против 0,0,2). Область действия не ограничена окном системы. Другие более конкретные/important правила могут переопределять отдельные ячейки.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 4 CSS-правил и 8 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `table.components-list` | 1 | `margin: 1rem 0` |
| `table.components-list td:nth-child(n+3), th:nth-child(n+2)` | 5 | `text-align: center` |
| `tr.components-price td` | 10 | `font-weight: bold`; `font-size: 1.15em`; `border-top: 1px solid black`; `text-align: right`; `padding: 0.5em 0` |
| `tr.components-price td.total-price` | 18 | `text-align: center` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

table.components-list получает margin 1rem 0. Строки 5–7 содержат два самостоятельных селектора: scoped table.components-list td:nth-child(n+3) и глобальный th:nth-child(n+2). Последний центрирует заголовки любых таблиц со второго DOM-элемента, а не только materials; colspan не учитывается как число DOM-ячеек. tr.components-price td — bold/1.15em, верхняя чёрная рамка, right, padding .5em 0; более конкретный td.total-price центрирует итог. Это оформление, расчёт стоимости здесь отсутствует.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/partials/components-list.hbs](../../../../../templates/partials/components-list.hbs) | table.components-list; tr.components-price; td.total-price | Таблица компонентов, включённая repair-dialog. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/chat/item/repair.hbs](../../../../../templates/chat/item/repair.hbs) | tr.components-price | Стоимость заказа в чате, даже без table.components-list. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/item/mixins/costEditMixin.js](../../../../../module/item/mixins/costEditMixin.js) | _calculateAdditionalCost, total-price/component-cost | Отдельный обработчик суммы и DOM; CSS не проверяет число. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../templates/sheets/item/diagrams-sheet.hbs) | th в таблицах без components-list | Проверенный посторонний потребитель глобальной ветви th:nth-child. | Исходники, поиск module/templates/styles и AST; границы ниже |



## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/partials/components-list.hbs](../../../../../templates/partials/components-list.hbs) | table.components-list; tr.components-price; td.total-price | Таблица компонентов, включённая repair-dialog. |
| [templates/chat/item/repair.hbs](../../../../../templates/chat/item/repair.hbs) | tr.components-price | Стоимость заказа в чате, даже без table.components-list. |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../templates/sheets/item/diagrams-sheet.hbs) | th в таблицах без components-list | Проверенный посторонний потребитель глобальной ветви th:nth-child. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 4 правил, 8 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | 4 правила / 8 declarations. Группа 12 отрендерила repair-dialog с настоящим partial: видны repair-info и components-price. Глобальная ветвь и её пересечение с table th подтверждены AST/каскадом; конечный вид чужих приложений в браузере не проверен. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | Импорт 24, после repair.css (23) и tab-inventory.css (7). Раннее table th задаёт text-align:left; th:nth-child(n+2) имеет большую специфичность (0,1,1 против 0,0,2). Область действия не ограничена окном системы. Другие более конкретные/important правила могут переопределять отдельные ячейки. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы.

## Связанные проблемы

[docs/issues/potential/issue-00309.md](../../../../issues/potential/issue-00309.md). Наблюдения остаются potential; подтверждения и исправления не выполнялись.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |
