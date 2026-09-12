# styles/monster-sheet.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/monster-sheet.css](../../../../../styles/monster-sheet.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 304 |
| Запись перекрёстной сверки | [TASK-0003.049](../../review-log.md#task-0003049) |

## Назначение файла

Прежний полный интерфейс монстра и несколько общих правил, которые продолжают влиять на текущие PARTS монстра.

## Условия использования

Импорт 5, перед background/inventory/skills и всеми новыми monster/*.css. Глобальные правила продолжают участвовать в каскаде. Наличие legacy-файла на диске/в preload не означает выбор листом; реальный маршрут определяется registerSheets и PARTS.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 51 CSS rule-узлов и 148 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.monster-flex` | `display: flex`; `flex-wrap: wrap` |
| 6 | Корень | `.monster-flex-small` | `flex-grow: 1`; `flex-basis: 100%` |
| 11 | Корень | `.break` | `height: 0`; `flex-basis: 100%` |
| 16 | Корень | `.monster-main` | `display: flex`; `min-height: 630px`; `flex-wrap: wrap` |
| 22 | Корень | `.monster-sheet-left-column` | `padding-right: 10px`; `flex-basis: 180px`; `flex: none` |
| 28 | Корень | `.monster-left-sidebar` | `width: 180px`; `flex: none` |
| 33 | Корень | `.monster-left-sidebar input` | `font-weight: bold`; `margin-right: 1px`; `margin-bottom: 1px`; `text-align: center` |
| 40 | Корень | `.monster-stat-title label` | `font-weight: bold`; `margin-left: 4px` |
| 45 | Корень | `.monster-stat-title` | `display: flex`; `justify-content: flex-end` |
| 50 | Корень | `.monster-stat-lable` | `display: inline-block`; `width: 65px`; `font-weight: bold`; `text-align: center` |
| 57 | Корень | `.monster-stat-modmax` | `font-weight: bold`; `text-align: center` |
| 62 | Корень | `.monster-stat-display` | `display: flex`; `text-align: center`; `justify-content: flex-end` |
| 68 | Корень | `.monster-stat-button` | `width: 65px`; `height: 26px`; `background-color: darkred`; `border-radius: 12px`; `color: white`; `padding: 5px`; `border-style: solid`; `border-width: 1px` |
| 79 | Корень | `.monster-stat-button:hover` | `outline: none`; `border-color: #9ecaed`; `box-shadow: 0 0 10px #9ecaed` |
| 85 | Корень | `.monster-stat-display label` | `font-weight: bold`; `width: 55px`; `margin: 5px`; `display: flex`; `align-items: center`; `justify-content: center` |
| 94 | Корень | `.monster-armor` | `display: flex`; `justify-content: flex-end` |
| 99 | Корень | `.monster-armor label` | `font-weight: bold`; `float: left`; `width: 90px`; `margin: 5px` |
| 106 | Корень | `.monster-custom` | `display: flex`; `justify-content: flex-end` |
| 111 | Корень | `.monster-custom label` | `margin: 5px`; `width: 90px`; `font-weight: bold` |
| 117 | Корень | `.monster-custom-details` | `margin-left: 15px`; `flex-direction: column` |
| 122 | Корень | `.monster-HPSTA` | `display: flex`; `justify-content: flex-end` |
| 127 | Корень | `.monster-HPSTA label` | `font-weight: bold`; `width: 65px`; `margin: 5px`; `display: flex`; `align-items: center`; `justify-content: center` |
| 136 | Корень | `.monster-header-center` | `min-width: 380px`; `flex: none`; `margin: 0 20px 0 20px` |
| 142 | Корень | `.monster-center-top` | `display: flex`; `margin-bottom: 1px` |
| 147 | Корень | `.monster-center-top label, .monster-center-top select, .monster-center-top input` | `font-weight: bold`; `text-align: center` |
| 154 | Корень | `.monster-center-top select` | `height: 26px` |
| 158 | Корень | `.monster-center-top div` | `display: flex`; `flex-direction: column`; `margin-right: 3px` |
| 164 | Корень | `.monster-type` | `width: 110px` |
| 168 | Корень | `.monster-difficulity, .monster-bounty` | `width: 80px` |
| 173 | Корень | `.monster-complexity` | `width: 90px` |
| 177 | Корень | `.monster-img` | `width: 375px`; `height: 545px` |
| 182 | Корень | `.cat-img` | `position: absolute`; `height: 75px`; `width: 75px`; `top: 10px`; `left: 10px`; `border: none` |
| 191 | Корень | `.monster-knowledge` | `margin-top: 10px`; `flex-basis: 380px`; `flex-grow: 1` |
| 197 | Корень | `.monster-knowledge label, .monster-knowledge input` | `font-weight: bold`; `text-align: center` |
| 203 | Корень | `.monster-right-sidebar` | `flex: 1 0`; `overflow: hidden`; `width: 100%`; `width: -moz-available`; `width: -webkit-fill-available`; `width: fill-available` |
| 212 | Корень | `.monster-right-buttons` | `display: flex`; `margin-bottom: 10px`; `justify-content: flex-start` |
| 218 | Корень | `.monster-right-attributes` | `font-size: 15px` |
| 222 | Корень | `.monster-right-attributes .right-element` | `height: 45px`; `width: 45px`; `margin: 0 0 5px 5px` |
| 228 | Корень | `.monster-right-attributes .right-image` | `height: 100%` |
| 232 | Корень | `.monster-right-attributes .right-value` | `font-size: 15px`; `bottom: 40px`; `position: relative`; `left: 20px` |
| 239 | Корень | `.monster-right-attributes .death-section` | `margin: 10px 0 0 20px` |
| 243 | Корень | `.monster-right-top` | `padding: 10px`; `flex-basis: 270px`; `background-color: lightslategrey`; `border-radius: 10px`; `color: black`; `display: flex`; `justify-content: center` |
| 253 | Корень | `.monster-right-row` | `display: flex`; `justify-content: flex-start` |
| 258 | Корень | `.monster-crit-wounds-section` | `margin-top: 10px` |
| 262 | Корень | `.monster-button-roll` | `width: 126.5px` |
| 266 | Корень | `.monster-button-column` | `width: 115px`; `margin-left: 2.5px` |
| 271 | Корень | `.monster-button-roll a` | `display: flex`; `width: 110px`; `height: 30px`; `align-items: center`; `justify-content: center`; `background-color: darkred`; `border-radius: 12px`; `color: white`; `border-style: solid`; `border-color: white`; `border-width: 1px`; `margin: 0 auto` |
| 286 | Корень | `.monster-button-roll a:hover` | `outline: none`; `border-color: #9ecaed`; `box-shadow: 0 0 10px #9ecaed` |
| 292 | Корень | `.monster-custom input:hover` | `outline: none`; `border-color: #9ecaed`; `box-shadow: 0 0 10px #9ecaed` |
| 298 | Корень | `.modifier-flex` | `flex: 1` |
| 302 | Корень | `.img-view` | `position: relative` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

51 правило покрывает старый flex-каркас (.monster-main, monster-flex, monster-sheet-left-column, break), левую колонку характеристик, кнопки и подписи статов, естественную броню, HP/STA, центр с категорией/угрозой/ценой и портретом, знания, правую панель ресурсов/кнопок и контейнеры модификаторов. Имена monster-stat-lable и monster-difficulity сохранены буквально. Все свойства перечислены ниже, включая повторные width у monster-right-sidebar: 100%, -moz-available, -webkit-fill-available, fill-available.

Это глобальные selectors, несмотря на имя файла. Основной потребитель большинства блоков — templates/sheets/actor/monster-sheet.hbs и его старые partial. Текущий зарегистрированный WitcherMonsterSheet использует PARTS, а не этот шаблон. Но .monster-img, .cat-img, .img-view, .monster-armor и .monster-knowledge совпадают с новым интерфейсом; считать весь файл неиспользуемым нельзя.

Поздний monster/sidebar.css заменяет размер портрета 375×545 на 130×260, значка категории 75×75/top-left10 на 48×48/top-left0. У .monster-armor сохраняется justify-content:flex-end; у label — bold, float:left, width:90px, но margin:5px заменён на 0. Свойства не исчезают только потому, что существует новый CSS. .monster-knowledge сохраняет margin-top:10px, flex-basis:380px, flex-grow:1; в текущих активных details к ним добавляется flex-колонка. Поскольку родитель details/lore и размер окна влияют на геометрию, фактические размеры без браузера не заявляются.

Старые .right-element/right-image/right-value уточняют базовые правила character-header.css. .monster-header-center относится к прежнему центру; текущий заголовок имеет иное имя. Не найден буквальный потребитель некоторых утилит (monster-flex-small, monster-stat-lable/modmax, monster-custom*, modifier-flex и др.); полный список ниже относится только к проверенной области, не к сторонним модулям.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 5 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../templates/sheets/actor/monster-sheet.hbs) | monster-main, monster-left-sidebar, monster-stat-*, monster-center-top, monster-right-*, img-view | Главный старый полный шаблон. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../templates/partials/monster/monster-inventory-tab.hbs) | monster-flex | Старый инвентарь. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | monster-img, cat-img, img-view, monster-armor | Действующие совпадения в новом sidebar. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | monster-knowledge | Действующая область знаний. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../module/actor/sheets/WitcherMonsterSheet.js) | PARTS | Текущий выбор отдельных шаблонов; старый полный HBS отсутствует. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../module/actor/sheets/WitcherActorSheetV1.js) | WitcherActorSheetV1 | Соседний прежний базовый API; наличие класса не регистрирует старый MonsterSheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/setup/registerSheets.js](../../../../../module/setup/registerSheets.js) | Actors.registerSheet types:monster | Регистрирует нынешний WitcherMonsterSheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/character-header.css](../../../../../styles/character-header.css) | .right-element, .right-image, .right-value | Общее оформление прежних ресурсных индикаторов. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/sidebar.css](../../../../../styles/monster/sidebar.css) | .monster-sidebar .img-view/.monster-armor | Переопределение фото и margin, сохранение прочих свойств. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/details.css](../../../../../styles/monster/details.css) | .tab.active.details .monster-knowledge | Добавляет оформление знаний, не сбрасывая flex-basis/margin. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/header.css](../../../../../styles/monster/header.css) | .monster-header | Новый заголовок вместо прежнего monster-header-center. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. Обращений var(...) в этом файле нет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../templates/sheets/actor/monster-sheet.hbs) | monster-main, monster-left-sidebar, monster-stat-*, monster-center-top, monster-right-*, img-view | Главный старый полный шаблон. |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../templates/partials/monster/monster-inventory-tab.hbs) | monster-flex | Старый инвентарь. |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | monster-img, cat-img, img-view, monster-armor | Действующие совпадения в новом sidebar. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-knowledge.hbs) | monster-knowledge | Действующая область знаний. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 304 логических строк и PostCSS 8.5.12 | 51 rule-узлов, 148 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 9/10/13/14: сравнение текущих классов с прежними, источники старых навыков, текущий root, AST размеров/остаточных свойств и порядок импортов. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 5, перед background/inventory/skills и всеми новыми monster/*.css. Глобальные правила продолжают участвовать в каскаде. Наличие legacy-файла на диске/в preload не означает выбор листом; реальный маршрут определяется registerSheets и PARTS. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00018](../../../../issues/potential/issue-00018.md), [issue-00180](../../../../issues/potential/issue-00180.md), [issue-00209](../../../../issues/potential/issue-00209.md), [issue-00210](../../../../issues/potential/issue-00210.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003049) |
