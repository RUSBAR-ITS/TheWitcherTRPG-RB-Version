# styles/tab-inventory-list.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/tab-inventory-list.css](../../../../../styles/tab-inventory-list.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 217 |
| Запись перекрёстной сверки | [TASK-0003.049](../../review-log.md#task-0003049) |

## Назначение файла

Общий каркас списков инвентаря и магии: раскрываемые заголовки, строки, детали Item, изображения и контролы.

## Условия использования

Импорт 26, после tab-inventory.css и system-styles.css. Все правила глобальные. .list-item-info.invisible сильнее .list-item-info и .invisible; hover-селекторы требуют точной структуры непосредственных детей. Условия HBS и обработчики определяют наличие элементов, CSS не ограничивает права пользователя.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 33 CSS rule-узлов и 107 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.list-header, .section-header` | `display: grid`; `align-items: center`; `padding: 5px`; `border-radius: 5px`; `background-color: rgba(0, 0, 0, 0.05)`; `border: 1px solid darkgray`; `margin: 5px 0`; `gap: 20px`; `list-style: none`; `cursor: pointer` |
| 15 | Корень | `.list-header > .chevron-icon` | `width: 16px`; `justify-self: center`; `transition: transform 0.3s ease` |
| 21 | Корень | `details[open] .list-header > .chevron-icon` | `transform: rotate(180deg)` |
| 25 | Корень | `.list-header h2, .section-header h2` | `margin: 0`; `font-size: 24px` |
| 31 | Корень | `.list-header h3, .section-header h3` | `font-size: 18px`; `margin: 0`; `border: none` |
| 38 | Корень | `.list-item-info` | `display: flex`; `flex-direction: column`; `padding: 10px 5px`; `gap: 5px`; `box-shadow: inset -2px 8px 8px -10px light-dark(#9a9991, black), inset -2px -8px 8px -10px light-dark(#9a9991, black)` |
| 48 | Корень | `.list-item-info.invisible` | `display: none` |
| 52 | Корень | `.list-label` | `display: flex`; `flex-direction: row`; `align-items: center`; `gap: 15px` |
| 59 | Корень | `.list-label > span` | `width: 70px`; `text-align: center`; `padding: 5px` |
| 65 | Корень | `.list-header .list-label > span` | `border-left: 1px solid #9a9991`; `box-sizing: border-box`; `height: 27px` |
| 71 | Корень | `.list-details .list-label > span:hover` | `padding: 5px`; `background-color: rgba(255, 255, 255, 0.3)`; `border-radius: 5px`; `box-shadow: -2px 8px 8px -10px #9a9991`; `transition: all 0.3s ease` |
| 79 | Корень | `.list-item-info h3, .list-item-description h3` | `border-bottom: 1px solid #9a9991` |
| 84 | Корень | `.list` | `display: flex`; `flex-direction: column`; `list-style-type: none`; `margin: 0`; `padding: 0`; `gap: 10px` |
| 93 | Корень | `.list-item` | `flex-direction: column` |
| 97 | Корень | `.list-controls` | `display: flex`; `justify-content: center`; `gap: 5px` |
| 103 | Корень | `.list-details` | `display: grid`; `margin: 0 7px`; `border-bottom: 1px solid rgba(25, 24, 19, 0.2)`; `align-items: center`; `justify-content: center`; `gap: 20px`; `transition: all 0.3s ease` |
| 113 | Корень | `.list-details:last-child` | `border: none` |
| 117 | Корень | `.list-details:hover` | `border-radius: 5px`; `background-color: light-dark(#22222210, #e7d1b110)` |
| 122 | Корень | `.list-details:hover > .display-details > img` | `display: none` |
| 126 | Корень | `.list-details:hover > .display-details > span` | `display: flex`; `font-size: 1rem` |
| 131 | Корень | `.display-details` | `display: flex` |
| 135 | Корень | `.display-details > span` | `display: none` |
| 139 | Корень | `.item-list-image` | `flex-wrap: wrap`; `place-content: center`; `text-shadow: none`; `color: var(--color-text-dark-primary)`; `font-size: 24px`; `border-radius: 5px`; `width: 40px`; `height: 40px`; `border: 1px solid light-dark(#19191950, #e7d1b140)` |
| 151 | Корень | `.reliable-armor` | `padding: 0px`; `width: 50px`; `text-align: center` |
| 157 | Корень | `.reliable-details` | `display: flex`; `align-items: center`; `flex-direction: column`; `width: 70px`; `padding: 5px` |
| 165 | Корень | `.reliable-input > span` | `width: 25px` |
| 169 | Корень | `.reliable-input` | `display: flex`; `flex-direction: row`; `align-items: center`; `gap: 5px` |
| 176 | Корень | `.item-equip, .item-repair, .item-chat, .item-carried, .item-learned, .crafting-craft` | `text-shadow: none` |
| 185 | Корень | `a.equipped` | `color: var(--color-text-dark-primary)`; `text-shadow: none` |
| 190 | Корень | `.toggle-hand-icon` | `position: relative`; `display: inline-block`; `cursor: pointer` |
| 196 | Корень | `.toggle-hand-icon input[type='checkbox']` | `position: absolute`; `opacity: 1`; `width: 100%`; `height: 100%`; `top: 0`; `left: 0`; `margin: 0`; `cursor: pointer`; `z-index: 44` |
| 208 | Корень | `.toggle-hand-icon:not(.equipped)` | `color: rgba(25, 25, 25, 0.4)`; `text-shadow: none` |
| 213 | Корень | `.toggle-hand-icon:has(.equipped)` | `color: var(--color-text-dark-primary)`; `text-shadow: none` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

`.list-header/.section-header` создают grid-заголовки; детали строк — `.list-details`. Ширины колонок задаются tab-inventory.css. `.list` делает ol вертикальным flex-контейнером, `.list-item` задаёт только flex-direction и сама не включает display:flex. `.list-controls` располагает действия в строку.

В текущих partial внешний `<details open>` содержит summary с `.list-header`; chevron — непосредственный ребёнок summary из inventory-items-summary.hbs. `details[open] .list-header > .chevron-icon` поворачивает его на 180°, а базовое правило задаёт transition. Селектор допускает любого открытого предка details; в проверенной строке оружия вложенных details нет. Это не JS-флаг pannels и не сохранение состояния.

`.list-item-info` задаёт display:flex и оформление информации, `.list-item-info.invisible` явно подавляет его. _onItemDisplayInfo меняет invisible через .item-info. Глобальная .invisible из system-styles.css сама имеет меньшую специфичность. Hover строки скрывает img и показывает span-книгу внутри `.display-details`; имя Item и фактическое действие определяются разметкой/JS.

Детали надёжности используют reliable-details/reliable-input. Иконки item-equip/repair/chat/carried/learned/crafting-craft сбрасывают text-shadow; a.equipped получает цвет. Блок `.toggle-hand-icon`, включая прозрачность, z-index:44, :not(.equipped) и :has(.equipped), определён целиком, но буквального потребителя в module/templates не найдено. Его нельзя приписывать текущей экипировке: там a.item-equip.equipped, без этой обёртки. Заголовки описаний сообщений также получают глобальное правило .list-item-description h3.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 26 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | chevron-icon, list-label | Прямые дети summary и подписи колонок. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | list*, display-details, reliable-details/input, equipped | Текущий список оружия обоих Actor. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | list*, display-details, item-equip | Броня. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | list*, display-details, item-carried | Вещи и контейнеры. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | list*, display-details | Алхимические Item. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | list*, display-details | Компоненты. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | list*, item-learned, crafting-craft | Рецепты и действия изготовления. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs) | list*, display-details | Ездовые животные. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | list*, display-details | Руны и глифы. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | list*, display-details | Список магии. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | section-header, list-label | Заголовки крупных секций. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/character/substances.hbs](../../../../../templates/partials/character/substances.hbs) | section-header | Секция веществ. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/effect-part.hbs](../../../../../templates/partials/effect-part.hbs) | item-list-image | Изображения ActiveEffect; не весь каркас inventory. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/chat/item/partials/item-description/alchemicals.hbs](../../../../../templates/chat/item/partials/item-description/alchemicals.hbs) | list-item-description | Описания алхимических Item в чате. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/chat/item/partials/item-description/description.hbs](../../../../../templates/chat/item/partials/item-description/description.hbs) | list-item-description | Общее описание Item в чате. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/chat/item/partials/item-description/spell-description.hbs](../../../../../templates/chat/item/partials/item-description/spell-description.hbs) | list-item-description | Описание магии в чате. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../module/actor/sheets/mixins/itemMixin.js) | _onItemDisplayInfo, _onItemEquip, itemListener | Переключение invisible, запрос изменения equipped и привязки действий. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/tab-inventory.css](../../../../../styles/tab-inventory.css) | weapon/armor/valuable/spell header/details | Размеры колонок и теги. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/system-styles.css](../../../../../styles/system-styles.css) | .invisible, .item-info | Исходное скрытие и оформление; уточнено более специфичными правилами этого файла. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. CSS читает переменные темы: `--color-text-dark-primary`. Их значений файл не объявляет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | chevron-icon, list-label | Прямые дети summary и подписи колонок. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | list*, display-details, reliable-details/input, equipped | Текущий список оружия обоих Actor. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | list*, display-details, item-equip | Броня. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | list*, display-details, item-carried | Вещи и контейнеры. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | list*, display-details | Алхимические Item. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | list*, display-details | Компоненты. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | list*, item-learned, crafting-craft | Рецепты и действия изготовления. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs) | list*, display-details | Ездовые животные. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | list*, display-details | Руны и глифы. |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | list*, display-details | Список магии. |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | section-header, list-label | Заголовки крупных секций. |
| [templates/partials/character/substances.hbs](../../../../../templates/partials/character/substances.hbs) | section-header | Секция веществ. |
| [templates/partials/effect-part.hbs](../../../../../templates/partials/effect-part.hbs) | item-list-image | Изображения ActiveEffect; не весь каркас inventory. |
| [templates/chat/item/partials/item-description/alchemicals.hbs](../../../../../templates/chat/item/partials/item-description/alchemicals.hbs) | list-item-description | Описания алхимических Item в чате. |
| [templates/chat/item/partials/item-description/description.hbs](../../../../../templates/chat/item/partials/item-description/description.hbs) | list-item-description | Общее описание Item в чате. |
| [templates/chat/item/partials/item-description/spell-description.hbs](../../../../../templates/chat/item/partials/item-description/spell-description.hbs) | list-item-description | Описание магии в чате. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 217 логических строк и PostCSS 8.5.12 | 33 rule-узлов, 107 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 3/4: настоящий summary/chevron, details open, последовательность img/span, equipped false/true и переключение invisible исходным itemMixin через локальные фасады. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 26, после tab-inventory.css и system-styles.css. Все правила глобальные. .list-item-info.invisible сильнее .list-item-info и .invisible; hover-селекторы требуют точной структуры непосредственных детей. Условия HBS и обработчики определяют наличие элементов, CSS не ограничивает права пользователя. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00063](../../../../issues/potential/issue-00063.md), [issue-00177](../../../../issues/potential/issue-00177.md), [issue-00307](../../../../issues/potential/issue-00307.md), [issue-00310](../../../../issues/potential/issue-00310.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003049) |
