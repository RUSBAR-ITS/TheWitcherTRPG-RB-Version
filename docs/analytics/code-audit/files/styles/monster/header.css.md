# styles/monster/header.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/monster/header.css](../../../../../../styles/monster/header.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 68 |
| Запись перекрёстной сверки | [TASK-0003.049](../../../review-log.md#task-0003049) |

## Назначение файла

Оформление текущего заголовка монстра: имя, сведения о типе и угрозе, действия и счётчик смерти.

## Условия использования

Импорт 30 после общей сетки (28) и до monster/sheet (32). Вложенный корень с четырьмя классами ограничивает влияние. Отсутствует :not(.extended-sheet), но нынешняя MonsterConfiguration не содержит monster и здесь не совпадает.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 12 CSS rule-узлов и 33 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.application.sheet.witcher.monster` | Только вложенность; собственных свойств нет |
| 2 | `.application.sheet.witcher.monster` | `.monster-header` | `display: flex`; `flex-direction: column` |
| 6 | `.application.sheet.witcher.monster` → `.monster-header` | `.input-name` | `display: flex`; `flex-direction: row`; `align-items: center`; `gap: 10px`; `margin: 0` |
| 13 | `.application.sheet.witcher.monster` → `.monster-header` → `.input-name` | `.configure-actor` | `font-size: 1rem` |
| 18 | `.application.sheet.witcher.monster` → `.monster-header` | `.monster-general` | `margin-top: 5px`; `margin-bottom: 5px` |
| 23 | `.application.sheet.witcher.monster` → `.monster-header` | `.monster-general > span > *` | `border: none` |
| 27 | `.application.sheet.witcher.monster` → `.monster-header` | `.monster-actions` | `display: flex`; `align-items: center`; `gap: 20px`; `margin-top: 12px` |
| 33 | `.application.sheet.witcher.monster` → `.monster-header` → `.monster-actions` | `.monster-button-list` | `display: flex`; `gap: 10px`; `flex-wrap: wrap` |
| 39 | `.application.sheet.witcher.monster` → `.monster-header` → `.monster-actions` | `.action` | `display: flex`; `justify-content: space-between`; `align-items: center`; `border: 1px solid light-dark(#22222240, #e7d1b140)`; `border-radius: 5px`; `padding: 5px 10px 5px`; `width: 125px` |
| 48 | `.application.sheet.witcher.monster` → `.monster-header` → `.monster-actions` → `.action` | `h3` | `margin: 0`; `font-weight: 300` |
| 53 | `.application.sheet.witcher.monster` → `.monster-header` → `.monster-actions` → `.action` | `.death-counter` | `display: flex`; `flex-direction: row`; `align-items: center`; `gap: 5px` |
| 59 | `.application.sheet.witcher.monster` → `.monster-header` → `.monster-actions` → `.action` → `.death-counter` | `h3` | `margin: 0`; `font-weight: 300` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

Корень `.application.sheet.witcher.monster` ограничивает все правила. `.monster-header` — flex-колонка; `.input-name` — строка имени и шестерёнки configure-actor, размер которой 1rem. `.monster-general` имеет вертикальные отступы; непосредственные элементы внутри span избавляются от рамок, но обычный текст не становится отдельным элементом.

`.monster-actions` — ряд с gap20/margin-top12; monster-button-list допускает перенос и gap10. `.action` — карточка 125px с рамкой и выравниванием; h3 без внешнего отступа/weight300. death-counter получает собственный ряд/gap5, вложенный h3 повторяет margin/weight. Цвета кнопок init/death/crit/verbal/export-loot задаёт character-header.css.

HTML содержит monster-header, а не monster-header-center; правила позиционирования старого имени из sheet CSS не совпадают с новым header. Автоматическое grid-размещение само по себе не является дефектом. В отличие от character-header.hbs, незакрытой ссылки наград здесь нет.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 30 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | DEFAULT_OPTIONS, PARTS, TABS, _prepareContext | Регистрация нынешних шаблонов и корневого класса monster; CSS не вызывает JS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../templates/sheets/actor/partials/monster/header.hbs) | monster-header, input-name, configure-actor, monster-general/actions/button-list, action/death-counter | Единственный установленный текущий consumer вложенного корня. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) | _renderConfigureDialog, activateListeners | Привязка configure-actor к окну конфигурации; действия не выполняет CSS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/character-header.css](../../../../../../styles/character-header.css) | button-roll и классы конкретных действий | Общие размеры, цвета и hover кнопок. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster-sheet.css](../../../../../../styles/monster-sheet.css) | .monster-header-center, .monster-center-top | Прежний заголовок с другим именем; не прямая замена текущих правил. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/sheet.css](../../../../../../styles/monster/sheet.css) | .window-content .monster-header-center | Сетка задаёт позицию прежнего имени, текущий header размещается автоматически. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. Обращений var(...) в этом файле нет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../templates/sheets/actor/partials/monster/header.hbs) | monster-header, input-name, configure-actor, monster-general/actions/button-list, action/death-counter | Единственный установленный текущий consumer вложенного корня. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 68 логических строк и PostCSS 8.5.12 | 12 rule-узлов, 33 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 9/10: настоящий header содержит пять button-roll при useVerbalCombat=true, configure-actor и monster-header; monster-header-center отсутствует. Core merge подтверждает root. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 30 после общей сетки (28) и до monster/sheet (32). Вложенный корень с четырьмя классами ограничивает влияние. Отсутствует :not(.extended-sheet), но нынешняя MonsterConfiguration не содержит monster и здесь не совпадает. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00209](../../../../../issues/potential/issue-00209.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003049) |
