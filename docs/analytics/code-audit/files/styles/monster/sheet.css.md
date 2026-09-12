# styles/monster/sheet.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/monster/sheet.css](../../../../../../styles/monster/sheet.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 27 |
| Запись перекрёстной сверки | [TASK-0003.049](../../../review-log.md#task-0003049) |

## Назначение файла

Сетка текущего листа монстра с размещением monster-sidebar на трёх строках.

## Условия использования

Импорт 32; повтор общей сетки из импорта 28. Текущий root включает actor и monster; extended-sheet исключается. Видимость/активность вкладок обеспечивает ядро и специализированные CSS, не этот файл.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 6 CSS rule-узлов и 11 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.application.sheet.witcher.monster:not(.extended-sheet)` | Только вложенность; собственных свойств нет |
| 2 | `.application.sheet.witcher.monster:not(.extended-sheet)` | `.window-content` | `display: grid`; `grid-template-columns: 130px 1fr`; `grid-template-rows: 130px 70px 1fr`; `gap: 10px 30px` |
| 8 | `.application.sheet.witcher.monster:not(.extended-sheet)` → `.window-content` | `.monster-sidebar` | `grid-row: 1 / span 3` |
| 12 | `.application.sheet.witcher.monster:not(.extended-sheet)` → `.window-content` | `.monster-header-center` | `grid-column: 2`; `grid-row: 1` |
| 17 | `.application.sheet.witcher.monster:not(.extended-sheet)` → `.window-content` | `.sheet-tabs.tabs` | `grid-column: 2`; `grid-row: 2` |
| 22 | `.application.sheet.witcher.monster:not(.extended-sheet)` → `.window-content` | `.tab` | `grid-column: 2`; `grid-row: 3` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

Под .application.sheet.witcher.monster:not(.extended-sheet) window-content получает тот же grid, что character/sheet.css: 130px/1fr, 130px/70px/1fr, gap10px/30px. monster-sidebar занимает grid-row 1/span3. monster-header-center задана позиция 2/1; sheet-tabs.tabs — 2/2, .tab — 2/3.

Повтор четырёх свойств контейнера и позиций nav/tab не создаёт второй grid: оба файла применяются к одному элементу. Дополнение этого файла — размещение именно monster-sidebar вместо char-sidebar. Текущий header имеет .monster-header; ему не назначена явная позиция правилом .monster-header-center. Нельзя объявлять ошибку расположения без проверки автоматического grid-placement.

Внутренние .tab и nav также совпадают с селекторами потомков, но назначение grid-row/column не превращает их родителя в grid. Старый полный monster-sheet.hbs сам не даёт корня ApplicationV2; наличие в нём monster-header-center не делает его текущим зарегистрированным листом.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 32 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | DEFAULT_OPTIONS, PARTS, TABS, _prepareContext | Регистрация нынешних шаблонов и корневого класса monster; CSS не вызывает JS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | monster-sidebar | Текущая панель на трёх строках. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../templates/sheets/actor/partials/monster/header.hbs) | monster-header | Автоматическое размещение; старый header-center не совпадает. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | tab и внутренний nav.sheet-tabs | Пример вложенных потомков, не нового grid-контейнера. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | tab | Текущий контент в позиции 2/3. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | DEFAULT_OPTIONS.classes extended-sheet | Конфигурация исключена. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/character/sheet.css](../../../../../../styles/character/sheet.css) | .window-content и grid-позиции | Ранний общий набор для actor/monster. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/sidebar.css](../../../../../../styles/monster/sidebar.css) | .monster-sidebar | Внутреннее flex-оформление панели отдельно от grid-position. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../templates/sheets/actor/monster-sheet.hbs) | monster-header-center | Прежний полный HBS, где старое имя ещё есть. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. Обращений var(...) в этом файле нет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | monster-sidebar | Текущая панель на трёх строках. |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | tab и внутренний nav.sheet-tabs | Пример вложенных потомков, не нового grid-контейнера. |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | tab | Текущий контент в позиции 2/3. |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../templates/sheets/actor/monster-sheet.hbs) | monster-header-center | Прежний полный HBS, где старое имя ещё есть. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 27 логических строк и PostCSS 8.5.12 | 6 rule-узлов, 11 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 9/10/14: current header-name, реальный core merge классов, одинаковые grid declarations; 6 rule-узлов и 11 declarations. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 32; повтор общей сетки из импорта 28. Текущий root включает actor и monster; extended-sheet исключается. Видимость/активность вкладок обеспечивает ядро и специализированные CSS, не этот файл. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

Новых наблюдений для этого файла не зарегистрировано. Это не вывод об исправности всего интерфейса.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003049) |
