# styles/character/sheet.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/character/sheet.css](../../../../../../styles/character/sheet.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 29 |
| Запись перекрёстной сверки | [TASK-0003.049](../../../review-log.md#task-0003049) |

## Назначение файла

Общая сетка основных листов Character и Monster: боковая панель, заголовок, навигация и содержимое вкладок.

## Условия использования

Импорт 28. monster/sheet.css (32) повторяет сетку для monster. modifier-configuration.css (35) имеет дополнительный класс, поэтому override относится к конфигурации, а не основному Actor. Core создаёт window-content и стандартную tab-navigation; эти определения внешние, не в файлах системы.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 6 CSS rule-узлов и 11 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.application.sheet.witcher.actor:not(.extended-sheet), .application.sheet.witcher.monster:not(.extended-sheet)` | Только вложенность; собственных свойств нет |
| 3 | `.application.sheet.witcher.actor:not(.extended-sheet), .application.sheet.witcher.monster:not(.extended-sheet)` | `.window-content` | `display: grid`; `grid-template-columns: 130px 1fr`; `grid-template-rows: 130px 70px 1fr`; `gap: 10px 30px` |
| 9 | `.application.sheet.witcher.actor:not(.extended-sheet), .application.sheet.witcher.monster:not(.extended-sheet)` → `.window-content` | `.char-sidebar` | `grid-row: 1 / span 3` |
| 13 | `.application.sheet.witcher.actor:not(.extended-sheet), .application.sheet.witcher.monster:not(.extended-sheet)` → `.window-content` | `.char-header-center, .monster-header-center` | `grid-column: 2`; `grid-row: 1` |
| 19 | `.application.sheet.witcher.actor:not(.extended-sheet), .application.sheet.witcher.monster:not(.extended-sheet)` → `.window-content` | `.sheet-tabs.tabs` | `grid-column: 2`; `grid-row: 2` |
| 24 | `.application.sheet.witcher.actor:not(.extended-sheet), .application.sheet.witcher.monster:not(.extended-sheet)` → `.window-content` | `.tab` | `grid-column: 2`; `grid-row: 3` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

Корневой список содержит `.application.sheet.witcher.actor:not(.extended-sheet)` и `.application.sheet.witcher.monster:not(.extended-sheet)`. Вложенный window-content получает колонки 130px/1fr, строки 130px/70px/1fr, gap 10px/30px. char-sidebar занимает три строки; header — колонку 2/строку 1, nav.sheet-tabs.tabs — 2/2, .tab — 2/3.

Foundry конкатенирует массивы DEFAULT_OPTIONS.classes. Поэтому текущий Monster имеет одновременно actor и monster и совпадает с обеими ветвями. .application добавляет ядро. На основном Character применяется actor-ветвь. MonsterConfiguration содержит extended-sheet и исключается; WitcherModifiersConfiguration не имеет extended-sheet, но более специфичный modifier-configuration.css меняет display window-content на inherit.

Наследование CSS-вложенности — селекторы потомков, не непосредственных детей: внутренние nav/.tab также получают grid-позиции, но они действуют как позиции только в соответствующем grid-контейнере. Видимость вкладок не определяется здесь. `.monster-header-center` принадлежит старому полному шаблону; текущий header имеет .monster-header и рассчитывает на автоматическое размещение. Это не доказательство нарушенной раскладки.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 28 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) | DEFAULT_OPTIONS.classes | Базовые witcher/sheet/actor. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | PARTS.sidebar/header/tabs/stats/skills/... | Текущий лист персонажа, унаследованные классы. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | DEFAULT_OPTIONS.classes, PARTS | Добавляет monster; actor сохраняется при штатном merge. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | DEFAULT_OPTIONS.classes | extended-sheet исключает основную сетку. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | DEFAULT_OPTIONS.classes | actor/modifier-configuration без extended-sheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/character-header.hbs](../../../../../../templates/partials/character-header.hbs) | char-header-center | Заголовок на позиции 2/1. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | char-sidebar | Панель на трёх строках. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../templates/sheets/actor/monster-sheet.hbs) | monster-header-center | Старое имя заголовка; текущий PARTS не использует полный шаблон. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/sheet.css](../../../../../../styles/monster/sheet.css) | .window-content, .monster-sidebar | Повтор общей сетки и добавление размещения sidebar монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/configurations/modifier-configuration.css](../../../../../../styles/configurations/modifier-configuration.css) | .application.sheet.witcher.actor.modifier-configuration:not(.extended-sheet) .window-content | Более позднее/специфичное display:inherit отменяет grid у конфигурации. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. Обращений var(...) в этом файле нет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/partials/character-header.hbs](../../../../../../templates/partials/character-header.hbs) | char-header-center | Заголовок на позиции 2/1. |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | char-sidebar | Панель на трёх строках. |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../templates/sheets/actor/monster-sheet.hbs) | monster-header-center | Старое имя заголовка; текущий PARTS не использует полный шаблон. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 29 логических строк и PostCSS 8.5.12 | 6 rule-узлов, 11 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 9/10/14: классы из DEFAULT_OPTIONS прогнаны через настоящий core merge; установлены actor+monster, исключение extended-sheet и override конфигурации; текущий monster-header-center отсутствует в HBS. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 28. monster/sheet.css (32) повторяет сетку для monster. modifier-configuration.css (35) имеет дополнительный класс, поэтому override относится к конфигурации, а не основному Actor. Core создаёт window-content и стандартную tab-navigation; эти определения внешние, не в файлах системы. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00202](../../../../../issues/potential/issue-00202.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003049) |
