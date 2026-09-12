# styles/tab-skills.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/tab-skills.css](../../../../../styles/tab-skills.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 154 |
| Запись перекрёстной сверки | [TASK-0003.049](../../review-log.md#task-0003049) |

## Назначение файла

Общие блоки вкладки навыков и IP, элементы конфигурации и часть оформления прежних таблиц навыков монстра.

## Условия использования

Импорт 9, перед monster-skill-tab.css; собственные правила master после импортов уточняют summary. .tab.skill-info.active имеет более специфичный display:flex. Классы вкладок добавляет настоящий Foundry _prepareTabs, поэтому поиск только буквального active в HBS недостаточен.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 26 CSS rule-узлов и 75 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.grow>div` | `flex-grow: 1` |
| 5 | Корень | `.skills-stats-list` | `display: flex`; `flex-wrap: wrap`; `gap: 10px`; `margin-top: 10px` |
| 12 | Корень | `.skill-column` | `margin: 5px`; `padding: 10px`; `border-radius: 10px`; `border: 1px solid darkgray`; `width: 100%` |
| 19 | `.skill-column` | `h1` | `border: none` |
| 23 | `.skill-column` | `summary` | `display: flex`; `align-items: center`; `gap: 15px`; `border-bottom: 2px solid var(--color-underline-header)` |
| 29 | `.skill-column` → `summary` | `span` | `font-size: 24px` |
| 36 | Корень | `.char-skill` | `padding: 0em` |
| 40 | Корень | `.table-skills` | `min-width: 175px`; `border: none`; `background: none` |
| 47 | Корень | `.char-skill a` | `font-size: 12px`; `display: flex`; `background-color: darkred`; `border-radius: 12px`; `color: white`; `padding: 4px`; `border-style: solid`; `height: 30px` |
| 58 | Корень | `.char-skill:hover` | `outline: none`; `border-color: #9ecaed`; `box-shadow: 0 0 10px #9ecaed` |
| 64 | Корень | `.char-input-skill` | `width: 10px` |
| 68 | Корень | `.char-input-skill-icon` | `width: 10px` |
| 72 | Корень | `.char-input-skill input` | `font-weight: bold`; `width: 30px`; `text-align: center` |
| 78 | Корень | `.skill-info` | `display: flex`; `gap: 5px`; `align-items: center`; `margin-top: 10px` |
| 85 | Корень | `.tab.skill-info` | `display: none` |
| 89 | Корень | `.tab.skill-info.active` | `display: flex` |
| 93 | Корень | `.skill-ip` | `display: flex`; `flex-direction: column`; `gap: 5px`; `background-color: light-dark(#22222210, #e7d1b110)`; `border: 1px solid light-dark(#22222240, #e7d1b140)`; `border-radius: 10px`; `padding: 10px`; `color: light-dark(black, white)`; `flex: 1`; `width: 100%` |
| 105 | `.skill-ip` | `.current-ip` | `display: flex`; `align-items: center`; `gap: 5px` |
| 111 | `.skill-ip` | `span` | `display: flex`; `justify-content: space-between`; `font-size: 20px` |
| 117 | `.skill-ip` | `.IP-value` | `font-weight: bold`; `width: 5ch`; `text-align: center` |
| 123 | `.skill-ip` | `.skillTraining` | `display: flex`; `gap: 5px` |
| 128 | `.skill-ip` | `.extra-skill-value` | `font-weight: bold`; `width: 8ch`; `text-align: center`; `min-width: 30px` |
| 136 | Корень | `.total-skills` | `width: 5ch`; `font-weight: bold`; `text-align: center` |
| 142 | Корень | `.learned-skilled a` | `background-color: darkolivegreen` |
| 146 | Корень | `.not-skilled a` | `background-color: saddlebrown` |
| 150 | Корень | `input[type="checkbox"].skill-checkbox` | `height: 15px`; `width: 15px`; `margin-left: 0px` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

`.skills-stats-list` располагает карточки с переносом; `.skill-column` оформляет группы и summary. Общая текущая вкладка используется Character и Monster. `.skill-info` — flex-ряд, но .tab.skill-info скрыта до .active; `.skill-ip`, current-ip, skillTraining и IP-value оформляют четыре строки расходов и баланс. `.total-skills` относится к двум disabled/readonly полям итогов.

Кнопки текущих навыков — `.char-stat-button.skill` из character-header.css. Правила `.char-skill a`, `.char-input-skill` относятся к старому monster-skill-display, а learned-skilled/not-skilled — к старому custom partial. Это разные DOM-контракты. `.table-skills` остаётся действующей в MonsterConfiguration; `.skill-checkbox` применяется в текущем редакторе модификаторов навыка. `.grow > div` и `.char-skill-icon` не имеют установленного буквального потребителя в module/templates.

Поворот стрелки details и псевдоэлемент summary задаёт сам witcher-styles.css после импортов. CSS не применяет isVisible: для текущего монстра это ограничение HBS описано в issue-00018. Вкладка IP монстра оформляется этим же CSS, хотя её модель и обработчики отличаются — issue-00030.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 9 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/character/tab-skills.hbs](../../../../../templates/partials/character/tab-skills.hbs) | skills-stats-list, skill-column, tab.skill-info, skill-ip, skillTraining | Текущая общая вкладка, вложенная группа skillTabs. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-skill-display.hbs](../../../../../templates/partials/monster/monster-skill-display.hbs) | char-skill, char-input-skill | Старая строка встроенного навыка, gated isVisible. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | char-input-skill, learned-skilled, not-skilled | Старая строка собственного навыка. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../templates/partials/monster/monster-skill-tab.hbs) | skill-column | Старые колонки и панели навыков. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) | table-skills | Текущая конфигурация видимости навыков монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | skill-checkbox | Текущие флаги isProfession/isPickup/isLearned. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../module/actor/sheets/WitcherCharacterSheet.js) | PARTS.skills, TABS.skillTabs, _prepareContext, activateListeners | Текущие вкладки и действия IP персонажа. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../module/actor/sheets/WitcherMonsterSheet.js) | PARTS.skills, TABS.skillTabs, _prepareContext | Тот же HBS и классы активной подгруппы у монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | PARTS.skills | Выбор конфигурационного шаблона. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | PARTS.skills | Выбор редактора флагов и модификаторов. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/character-header.css](../../../../../styles/character-header.css) | .char-stat-button.skill | Нынешние кнопки навыков и цвета флагов. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster-skill-tab.css](../../../../../styles/monster-skill-tab.css) | .skill-list td/span | Старые таблицы; совместно оформляют прежний DOM. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. CSS читает переменные темы: `--color-underline-header`. Их значений файл не объявляет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/partials/character/tab-skills.hbs](../../../../../templates/partials/character/tab-skills.hbs) | skills-stats-list, skill-column, tab.skill-info, skill-ip, skillTraining | Текущая общая вкладка, вложенная группа skillTabs. |
| [templates/partials/monster/monster-skill-display.hbs](../../../../../templates/partials/monster/monster-skill-display.hbs) | char-skill, char-input-skill | Старая строка встроенного навыка, gated isVisible. |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | char-input-skill, learned-skilled, not-skilled | Старая строка собственного навыка. |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../templates/partials/monster/monster-skill-tab.hbs) | skill-column | Старые колонки и панели навыков. |
| [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) | table-skills | Текущая конфигурация видимости навыков монстра. |
| [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | skill-checkbox | Текущие флаги isProfession/isPickup/isLearned. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 154 логических строк и PostCSS 8.5.12 | 26 rule-узлов, 75 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 6/7/13: actual _prepareTabs для обоих Actor; переключение all/ip; четыре строки обучения и два отключённых итога; редактор с тремя skill-checkbox; различие старых a/span. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 9, перед monster-skill-tab.css; собственные правила master после импортов уточняют summary. .tab.skill-info.active имеет более специфичный display:flex. Классы вкладок добавляет настоящий Foundry _prepareTabs, поэтому поиск только буквального active в HBS недостаточен. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00018](../../../../issues/potential/issue-00018.md), [issue-00030](../../../../issues/potential/issue-00030.md), [issue-00187](../../../../issues/potential/issue-00187.md), [issue-00188](../../../../issues/potential/issue-00188.md), [issue-00192](../../../../issues/potential/issue-00192.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003049) |
