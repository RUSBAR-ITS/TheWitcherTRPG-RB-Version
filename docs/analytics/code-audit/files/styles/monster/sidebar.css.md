# styles/monster/sidebar.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/monster/sidebar.css](../../../../../../styles/monster/sidebar.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 59 |
| Запись перекрёстной сверки | [TASK-0003.049](../../../review-log.md#task-0003049) |

## Назначение файла

Текущая боковая панель монстра: портрет, значок категории, состояние ранений и естественная броня.

## Условия использования

Импорт 33, после monster-sheet.css (5) и monster/sheet.css (32). Селекторы портрета и значка более специфичны; размеры 375×545/75×75 заменяются на 130×260/48×48. Новый margin у armor label не отменяет width/float старого CSS.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 9 CSS rule-узлов и 34 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.application.sheet.witcher.monster` | Только вложенность; собственных свойств нет |
| 2 | `.application.sheet.witcher.monster` | `.monster-sidebar` | `display: flex`; `flex-direction: column` |
| 6 | `.application.sheet.witcher.monster` → `.monster-sidebar` | `.img-view` | `position: relative` |
| 9 | `.application.sheet.witcher.monster` → `.monster-sidebar` → `.img-view` | `.monster-img` | `height: 260px`; `width: 130px`; `border-radius: 3px`; `object-fit: cover`; `cursor: pointer` |
| 17 | `.application.sheet.witcher.monster` → `.monster-sidebar` → `.img-view` | `.cat-img` | `position: absolute`; `top: 0`; `left: 0`; `height: 48px`; `width: 48px` |
| 25 | `.application.sheet.witcher.monster` → `.monster-sidebar` → `.img-view` | `.wound-state` | `display: flex`; `justify-content: center`; `align-items: center`; `padding: 5px`; `position: absolute`; `width: 40px`; `height: 40px`; `right: 0`; `bottom: 0`; `background: rgba(34, 34, 34, 0.4)`; `backdrop-filter: blur(4px)`; `border-radius: 5px 0px 3px`; `font-size: 28px` |
| 42 | `.application.sheet.witcher.monster` → `.monster-sidebar` | `.monster-armor-list` | `display: flex`; `flex-direction: column`; `gap: 5px`; `margin-top: 10px` |
| 48 | `.application.sheet.witcher.monster` → `.monster-sidebar` → `.monster-armor-list` | `.monster-armor` | `display: flex`; `align-items: center`; `gap: 5px` |
| 53 | `.application.sheet.witcher.monster` → `.monster-sidebar` → `.monster-armor-list` → `.monster-armor` | `label` | `margin: 0` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

Под корнем .application.sheet.witcher.monster sidebar становится flex-колонкой. .img-view задаёт relative. Фото .monster-img получает 130×260, radius3, cover и pointer; .cat-img — 48×48 и top/left0. Внутри .img-view блок wound-state — 40×40 в правом нижнем углу, translucent-фон и blur.

`.monster-armor-list` — колонка с gap5 и margin-top10; .monster-armor — ряд с gap5/align:center; у label margin0. Остальные свойства глобального monster-sheet.css не сбрасываются: justify-content:flex-end у ряда и width90/bold/float у подписи продолжают участвовать.

Шкалы HP/STA/toxicity/focus/resolve и optional-stats-section существуют в этом HBS, но оформлены character-header.css. Файл не рассчитывает SP, не выбирает категорию и не решает, ранен ли Actor: значения/иконку определяет sidebar.hbs. Изображения assets находятся вне пофайлового аудита; URL задаёт шаблон, а не CSS.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 33 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | DEFAULT_OPTIONS, PARTS, TABS, _prepareContext | Регистрация нынешних шаблонов и корневого класса monster; CSS не вызывает JS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | monster-sidebar, img-view, monster-img, cat-img, wound-state, monster-armor-list/armor | Прямой текущий DOM; четыре поля естественной брони и общие ресурсы. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster-sheet.css](../../../../../../styles/monster-sheet.css) | .monster-img, .cat-img, .monster-armor label | Старые глобальные размеры/подписи; часть переопределена. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/character-header.css](../../../../../../styles/character-header.css) | status-section, progress-*, optional-stats-section | Общее оформление ресурсов и переключателей. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/sheet.css](../../../../../../styles/monster/sheet.css) | .monster-sidebar grid-row | Размещение панели на трёх строках. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. Обращений var(...) в этом файле нет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | monster-sidebar, img-view, monster-img, cat-img, wound-state, monster-armor-list/armor | Прямой текущий DOM; четыре поля естественной брони и общие ресурсы. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 59 логических строк и PostCSS 8.5.12 | 9 rule-узлов, 34 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 8/14: настоящий sidebar с четырьмя/пятью шкалами и двумя switch; AST полного набора переопределённых и сохраняющихся свойств. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 33, после monster-sheet.css (5) и monster/sheet.css (32). Селекторы портрета и значка более специфичны; размеры 375×545/75×75 заменяются на 130×260/48×48. Новый margin у armor label не отменяет width/float старого CSS. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00203](../../../../../issues/potential/issue-00203.md), [issue-00205](../../../../../issues/potential/issue-00205.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003049) |
