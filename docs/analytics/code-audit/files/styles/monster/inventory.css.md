# styles/monster/inventory.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/monster/inventory.css](../../../../../../styles/monster/inventory.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 15 |
| Запись перекрёстной сверки | [TASK-0003.049](../../../review-log.md#task-0003049) |

## Назначение файла

Специализация общих секций инвентаря монстра и кнопки экспорта добычи.

## Условия использования

Импорт 31, позднее глобальных секций system-styles.css. Все три ветви списка остаются внутри обоих scopes. Правила активируются только для inventory.active; состояние задают TABS/ядро.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 4 CSS rule-узлов и 4 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.application.sheet.witcher.monster` | Только вложенность; собственных свойств нет |
| 2 | `.application.sheet.witcher.monster` | `.tab.active.inventory` | Только вложенность; собственных свойств нет |
| 3 | `.application.sheet.witcher.monster` → `.tab.active.inventory` | `.weapon-section, .armor-section, .valuable-section` | `flex: none`; `margin: 0` |
| 9 | `.application.sheet.witcher.monster` → `.tab.active.inventory` → `.weapon-section, .armor-section, .valuable-section` | `.export-loot` | `margin-top: 5px`; `width: 100%` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

Под .application.sheet.witcher.monster и .tab.active.inventory три секции weapon/armor/valuable получают flex:none и margin:0. Вложенная .export-loot занимает width100% и margin-top5. Четыре rule-узла включают два контейнера вложенности, один список секций и правило кнопки; всего четыре declarations.

Текущий HBS выводит три секции и использует общие списки предметов; кнопка экспорта находится внутри valuable-section и остаётся даже при пустом loots. У заголовка монстра есть отдельная ссылка export-loot вне .tab.active.inventory — правило полной ширины туда не попадает. CSS не экспортирует предметы, не считает множитель и не назначает тип папки.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 31 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | DEFAULT_OPTIONS, PARTS, TABS, _prepareContext | Регистрация нынешних шаблонов и корневого класса monster; CSS не вызывает JS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | tab, weapon-section, armor-section, valuable-section, export-loot | Прямой consumer; exportLoot привязан через data-action. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../templates/sheets/actor/partials/monster/header.hbs) | export-loot вне вкладки | Проверенный контрпример: вложенный селектор этой кнопки не касается. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/system-styles.css](../../../../../../styles/system-styles.css) | .weapon-section/.armor-section/.valuable-section | Ранний flex:1 и margin-right10 у valuables заменяются. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/character-header.css](../../../../../../styles/character-header.css) | .export-loot | Общий цвет кнопки сохраняется. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/tab-inventory.css](../../../../../../styles/tab-inventory.css) | header/details классы | Общие колонки, теги, улучшения списков. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/tab-inventory-list.css](../../../../../../styles/tab-inventory-list.css) | .list-* | Каркас общих partial списков. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. Обращений var(...) в этом файле нет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | tab, weapon-section, armor-section, valuable-section, export-loot | Прямой consumer; exportLoot привязан через data-action. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 15 логических строк и PostCSS 8.5.12 | 4 rule-узлов, 4 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группа 12: три секции и одна кнопка export-loot с data-action=exportLoot в настоящем HBS; группа 9 отдельно проверяет заголовок. AST flex:none/margin0 и общей области. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 31, позднее глобальных секций system-styles.css. Все три ветви списка остаются внутри обоих scopes. Правила активируются только для inventory.active; состояние задают TABS/ядро. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00177](../../../../../issues/potential/issue-00177.md), [issue-00206](../../../../../issues/potential/issue-00206.md), [issue-00207](../../../../../issues/potential/issue-00207.md), [issue-00208](../../../../../issues/potential/issue-00208.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003049) |
