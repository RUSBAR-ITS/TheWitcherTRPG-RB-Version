# styles/monster/details.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/monster/details.css](../../../../../../styles/monster/details.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 36 |
| Запись перекрёстной сверки | [TASK-0003.049](../../../review-log.md#task-0003049) |

## Назначение файла

Активная вкладка сведений монстра: вложенные вкладки, знания, заголовки и числовые пороги.

## Условия использования

Импорт 34. Root/active/details ограничивают специализированные правила. CSS-переменные --spacer-16/8 предоставляет тема ядра; здесь они читаются без fallback. Неактивная внешняя вкладка скрывается ядром, внутренние дополнительно скрываются данным CSS, когда details активна.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 7 CSS rule-узлов и 17 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.application.sheet.witcher.monster` | Только вложенность; собственных свойств нет |
| 2 | `.application.sheet.witcher.monster` | `.tab.active.details` | `display: flex`; `flex-direction: column`; `gap: var(--spacer-16)` |
| 7 | `.application.sheet.witcher.monster` → `.tab.active.details` | `.monster-info` | `margin: 0` |
| 11 | `.application.sheet.witcher.monster` → `.tab.active.details` | `.tab:not(.active)` | `display: none`; `visibility: hidden` |
| 16 | `.application.sheet.witcher.monster` → `.tab.active.details` | `.monster-knowledge` | `display: flex`; `flex-direction: column`; `gap: var(--spacer-8)`; `justify-items: start` |
| 22 | `.application.sheet.witcher.monster` → `.tab.active.details` → `.monster-knowledge` | `h1` | `display: flex`; `align-items: center`; `gap: var(--spacer-8)`; `font-size: 36px`; `margin: 0` |
| 30 | `.application.sheet.witcher.monster` → `.tab.active.details` → `.monster-knowledge` | `input` | `width: 4ch`; `height: 3ch` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

Правила действуют внутри .application.sheet.witcher.monster только на .tab.active.details. Основная вкладка — flex-колонка с gap --spacer-16; monster-info сбрасывает margin. Вложенные .tab:not(.active) получают одновременно display:none и visibility:hidden.

monster-knowledge — flex-колонка с gap --spacer-8; h1 становится строкой с font36 и нулевым margin; input шириной 4ch/высотой 3ch. justify-items:start записан, но это не управление расположением flex-элементов. Старые margin-top10/flex-basis380/flex-grow1 для monster-knowledge сохраняются из monster-sheet.css, как и center/bold для input.

Источники active/details/notes/lore — TABS и _prepareTabs ядра. Изначально primary выбирает stats, а detailTabs — notes. В HBS есть три section.tab: одна внешняя и две внутренние; при открытых details активны две из трёх. Три флага showCommonerSuperstition/showAcademicKnowledge/showMonsterLore определяют наличие блоков знаний независимо от CSS. Текст редакторов формируется formGroup; issue-00013 относится к входу enriched, а не стилям.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 34 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | DEFAULT_OPTIONS, PARTS, TABS, _prepareContext | Регистрация нынешних шаблонов и корневого класса monster; CSS не вызывает JS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | section.tab, detailTabs, nav.sheet-tabs | Обёртка и две вложенные вкладки. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs) | monster-info | Информация во вкладке lore. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | monster-knowledge, h1, input | Условные знания и пороги. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs) | содержимое detailTabs.notes | Внутренний контент скрывается вместе с .tab; собственных совпадений monster-knowledge нет. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) | содержимое detailTabs.notes | Заметки внутри скрываемой секции; оформление заметок в другом CSS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster-sheet.css](../../../../../../styles/monster-sheet.css) | .monster-knowledge и input | Сохраняющиеся базовые flex/margin/типографика. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/tab-background.css](../../../../../../styles/tab-background.css) | .editor, .bg-note | Общие редакторы и заметки внутри details. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. CSS читает переменные темы: `--spacer-16`, `--spacer-8`. Их значений файл не объявляет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | section.tab, detailTabs, nav.sheet-tabs | Обёртка и две вложенные вкладки. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-info.hbs) | monster-info | Информация во вкладке lore. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | monster-knowledge, h1, input | Условные знания и пороги. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) | содержимое detailTabs.notes | Заметки внутри скрываемой секции; оформление заметок в другом CSS. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 36 логических строк и PostCSS 8.5.12 | 7 rule-узлов, 17 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группа 11: actual core TABS + HBS при notes/lore и всех knowledge-флагах off/on: три секции, две active и 0/3 h1; group 14 — остаточные свойства прежнего CSS. Содержимое formGroup заменено маркером. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 34. Root/active/details ограничивают специализированные правила. CSS-переменные --spacer-16/8 предоставляет тема ядра; здесь они читаются без fallback. Неактивная внешняя вкладка скрывается ядром, внутренние дополнительно скрываются данным CSS, когда details активна. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00013](../../../../../issues/potential/issue-00013.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003049) |
