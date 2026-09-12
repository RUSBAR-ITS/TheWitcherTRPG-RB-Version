# styles/loot-sheet.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/loot-sheet.css](../../../../../styles/loot-sheet.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 27 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Боковая область Loot, отображение скрытых предметов и ширины пустых крайних ячеек; общие классы переиспользованы расследованием.

## Условия использования

Импорт 11; глобальные selectors действуют вне Loot. Применение silver ограничено tr в table; display:none не ограничен типом тега. Наличие скрываемых данных в HTML само по себе не признано нарушением прав: разрешения документов — отдельный механизм.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 6 CSS-правил и 10 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `.left-loot-border` | 1 | `border-right: solid 1px`; `width: 150px`; `height: 100%` |
| `.loot-img` | 7 | `max-width: 140px`; `margin-top: 10px`; `border-width: 0px` |
| `table tr.hidden-view` | 13 | `background-color: silver` |
| `.hidden-from-view` | 17 | `display: none` |
| `.table-empty-space` | 21 | `width: 30px` |
| `.table-empty-end-space` | 25 | `width: 75px` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

left-loot-border — правая рамка, width 150px/height 100%; loot-img — max-width 140px, margin-top 10px, border-width 0. table tr.hidden-view получает silver. hidden-from-view скрывает элемент display:none, но не убирает Item из контекста/HTML и не меняет разрешения Foundry. Крайние пустые ячейки имеют 30px/75px. У скрытого Item HBS выбирает hidden-view для GM, hidden-from-view для остальных; при false оба класса отсутствуют.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../templates/sheets/actor/loot-sheet.hbs) | left-loot-border/loot-img/table-empty-space/table-empty-end-space | Лист добычи. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) | hidden-view/hidden-from-view | isHidden × isGM управляет классом строки. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/actor/sheets/WitcherLootSheet.js](../../../../../module/actor/sheets/WitcherLootSheet.js) | _prepareContext/_onItemHide | Передаёт isGM и меняет isHidden. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../../../templates/sheets/investigation/mystery-sheet.hbs) | table-empty-space/table-empty-end-space | Таблицы расследования. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/investigation/partials/clue-display.hbs](../../../../../templates/sheets/investigation/partials/clue-display.hbs) | hidden-view/hidden-from-view | Строка улики. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/investigation/partials/obstacle-display.hbs](../../../../../templates/sheets/investigation/partials/obstacle-display.hbs) | hidden-view/hidden-from-view | Строка препятствия. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) | hideItem/контекст | Поведение скрытия расследования задаёт отдельный класс листа. | Исходники, поиск module/templates/styles и AST; границы ниже |



## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../templates/sheets/actor/loot-sheet.hbs) | left-loot-border/loot-img/table-empty-space/table-empty-end-space | Лист добычи. |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) | hidden-view/hidden-from-view | isHidden × isGM управляет классом строки. |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../../../templates/sheets/investigation/mystery-sheet.hbs) | table-empty-space/table-empty-end-space | Таблицы расследования. |
| [templates/sheets/investigation/partials/clue-display.hbs](../../../../../templates/sheets/investigation/partials/clue-display.hbs) | hidden-view/hidden-from-view | Строка улики. |
| [templates/sheets/investigation/partials/obstacle-display.hbs](../../../../../templates/sheets/investigation/partials/obstacle-display.hbs) | hidden-view/hidden-from-view | Строка препятствия. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 6 правил, 10 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | 6 правил / 10 declarations. Группа 13: реальные три row-partials при isHidden=true и isGM=false/true, имя остаётся в HTML, меняется класс. Размеры/контраст и права клиентов не проверены. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | Импорт 11; глобальные selectors действуют вне Loot. Применение silver ограничено tr в table; display:none не ограничен типом тега. Наличие скрываемых данных в HTML само по себе не признано нарушением прав: разрешения документов — отдельный механизм. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы.

## Связанные проблемы

Новой проблемы в пределах данного файла не зарегистрировано. Это не вывод об исправности всех связанных процессов.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |
