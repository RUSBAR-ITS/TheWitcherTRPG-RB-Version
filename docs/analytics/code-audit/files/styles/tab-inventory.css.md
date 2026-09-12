# styles/tab-inventory.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/tab-inventory.css](../../../../../styles/tab-inventory.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 297 |
| Запись перекрёстной сверки | [TASK-0003.049](../../review-log.md#task-0003049) |

## Назначение файла

Оформление инвентаря, нагрузки, валют, тегов Item, улучшений и содержимого контейнеров; общие правила используются также в сообщениях и Loot.

## Условия использования

Импорт 7. Глобальные правила действуют также в чате и других листах. tab-inventory-list.css (26) задаёт grid-контейнеры; components-list.css (24) содержит более специфичный глобальный th:nth-child(n+2). Цвета progress зависят от vendor-псевдоэлемента и appearance ядра; computed styles не проверялись.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 48 CSS rule-узлов и 147 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `table th` | `padding: 0.25em`; `text-align: left` |
| 6 | Корень | `.enhancement-img, .enhancement-slot, .stored-item-img` | `height: 30px`; `width: 30px`; `border-radius: 5px`; `border: 1px solid rgba(25, 24, 19, 0.6)` |
| 15 | Корень | `.enhancement-label, .stored-item-label` | `display: flex`; `align-items: center`; `gap: 10px` |
| 22 | Корень | `.enhancement-label:hover, .stored-item-label:hover` | `cursor: pointer`; `text-shadow: none`; `background-color: rgba(25, 25, 25, 0.1)` |
| 29 | Корень | `.stored-item-info` | `margin-top: 5px` |
| 33 | Корень | `.enhancement-effects-name` | `margin-top: 5px` |
| 37 | Корень | `.enhancement-list` | `display: flex`; `flex-direction: column`; `gap: 5px` |
| 43 | Корень | `.item-tags` | `display: flex`; `flex-direction: row`; `flex-wrap: wrap`; `gap: 10px` |
| 50 | Корень | `.item-tag` | `background-color: 1px solid light-dark(#22222240, #e7d1b140)`; `color: light-dark(black, white)`; `padding: 5px`; `border-radius: 5px`; `border: 1px solid darkgray` |
| 58 | Корень | `.item-enhancement` | `height: 30px`; `width: 30px` |
| 63 | Корень | `.no-margin` | `margin: 0px` |
| 67 | Корень | `.currency` | `flex: 1`; `display: flex`; `flex-direction: column` |
| 73 | Корень | `.wrapper` | `position: relative` |
| 77 | Корень | `.carry-section` | `display: flex`; `flex-direction: column`; `gap: 15px`; `position: sticky`; `top: 0`; `width: 100%`; `background-color: light-dark(#22222210, #e7d1b110)`; `border: 1px solid light-dark(#22222240, #e7d1b140)`; `border-radius: 10px`; `padding: 10px`; `color: light-dark(black, white)`; `flex: 1`; `backdrop-filter: blur(10px)`; `z-index: 1` |
| 93 | `.carry-section` | `.carry-labels` | `position: absolute`; `display: flex`; `justify-content: space-between`; `align-items: center`; `top: 0`; `font-size: 12px`; `color: #eee`; `padding: 0 10px`; `padding-right: 30px`; `height: 100%`; `width: 100%` |
| 107 | `.carry-section` | `progress.carry-bar` | `width: 100%`; `height: 20px`; `background-color: transparent` |
| 113 | `.carry-section` | `progress.carry-bar::-webkit-progress-bar` | `background-color: #888`; `border-radius: 4px` |
| 118 | `.carry-section` | `progress.carry-bar.overweight::-moz-progress-bar` | `background-color: #d04747` |
| 122 | `.carry-section` | `progress.carry-bar.overweight:-webkit-progress-value` | `background-color: #d04747` |
| 126 | `.carry-section` | `progress.carry-bar::-moz-progress-bar` | `background-color: #1a3b8b`; `border-radius: 4px` |
| 131 | `.carry-section` | `progress.carry-bar::-webkit-progress-value` | `background-color: #1a3b8b`; `border-radius: 4px` |
| 137 | Корень | `.currency-section` | `display: flex`; `flex-direction: column`; `gap: 15px`; `background-color: light-dark(#22222210, #e7d1b110)`; `border: 1px solid light-dark(#22222240, #e7d1b140)`; `border-radius: 10px`; `padding: 10px`; `color: light-dark(black, white)`; `flex: 1` |
| 148 | `.currency-section` | `span` | `display: flex`; `justify-content: space-between`; `font-size: 20px` |
| 154 | `.currency-section` | `.currency-list` | `display: flex`; `gap: 5px` |
| 159 | `.currency-section` | `.currency-actions` | `display: flex`; `gap: 8px`; `align-items: center`; `justify-content: flex-end` |
| 166 | `.currency-section` | `.currency-actions a` | `display: inline-flex`; `align-items: center`; `justify-content: center`; `width: 28px`; `height: 28px`; `border-radius: 4px` |
| 175 | `.currency-section` | `.currency-actions a:hover` | `background-color: rgba(25, 25, 25, 0.1)` |
| 180 | Корень | `.weightbar` | `background-color: grey`; `width: 100%`; `height: 12px` |
| 186 | Корень | `.weight-value` | `color: white`; `position: absolute`; `right: 10px` |
| 192 | Корень | `.item-img-wrapper` | `position: relative`; `display: flex`; `cursor: pointer`; `height: 44px` |
| 199 | Корень | `.item-img-wrapper .item-show` | `position: absolute`; `width: 40px`; `height: 40px`; `z-index: 1`; `display: flex`; `justify-content: center`; `align-items: center` |
| 209 | Корень | `.item-img-wrapper .item-show:hover` | `background: rgba(0, 0, 0, 0.3)` |
| 213 | Корень | `.item-img-wrapper .item-show .fa` | `display: none`; `color: rgb(200, 200, 200)`; `font-size: 28px` |
| 219 | Корень | `.item-img-wrapper .item-show:hover .fa` | `display: inline-block` |
| 223 | Корень | `.weapon-header` | `grid-template-columns: 33px 2fr 1fr` |
| 227 | Корень | `.weapon-details` | `grid-template-columns: 40px 2fr 1fr` |
| 230 | Корень | `.weapon-enhancement, .container-stored-item` | `display: flex`; `flex-direction: column`; `gap: 5px` |
| 237 | Корень | `.armor-header` | `grid-template-columns: 33px 1fr 1fr` |
| 241 | Корень | `.armor-details` | `grid-template-columns: 40px 1fr 1fr` |
| 245 | Корень | `.valuable-header, .spell-header` | `grid-template-columns: 33px 6fr 1fr` |
| 250 | Корень | `.valuables-list-header, .spell-list-header` | `grid-template-columns: 33px 1.5fr 1fr` |
| 255 | Корень | `.valuable-details, .spell-details` | `grid-template-columns: 40px 1.5fr 1fr` |
| 260 | Корень | `.progress-bar-stored-weight` | `position: relative`; `width: 100%`; `margin-bottom: 5px` |
| 266 | Корень | `.progress-bar-stored-weight progress` | `width: 100%`; `background-color: transparent` |
| 271 | Корень | `.progress-bar-stored-weight progress::-webkit-progress-bar` | `background-color: #888`; `border-radius: 4px` |
| 276 | Корень | `.progress-bar-stored-weight progress::-webkit-progress-value` | `background-color: #1a3b8b`; `border-radius: 4px` |
| 281 | Корень | `.progress-bar-stored-weight progress::-moz-progress-bar` | `background-color: #1a3b8b`; `border-radius: 4px` |
| 286 | Корень | `.progress-bar-stored-weight-labels` | `position: absolute`; `display: flex`; `justify-content: space-between`; `align-items: center`; `top: 0`; `font-size: 12px`; `color: #eee`; `padding: 0 5px`; `height: 100%`; `width: 100%` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

Файл объединяет несколько блоков: общий `table th`; изображения/ярлыки улучшений и хранимых предметов; теги; панели нагрузки и валют; старую шкалу Loot и helper картинки; размеры колонок списков; шкалу вместимости контейнера.

`.item-tags` переносит теги, `.item-tag` оформляет текст и рамку. Значение background-color содержит `1px solid` и не является цветом — существующая issue-00310. Теги используются и в чате, поэтому это глобальная связь. `.stored-item-label:hover`/`.enhancement-label:hover` меняют фон и курсор, а раскрытие данных выполняет JS.

`.carry-section` — sticky-панель с top:0, z-index:1 и blur; абсолютные `.carry-labels` накладываются на progress. HBS даёт `.overweight` при `totalWeight >= enc.value`, включая точное равенство. В Gecko красное правило специфичнее обычного синего; запись WebKit имеет один `:` — issue-00311. Этот файл не считает вес и не устанавливает штраф. Отдельная шкала `.progress-bar-stored-weight` не содержит состояния перегруза.

`.currency-section` располагает список валют и кнопки действий. `.currency` общая также для Loot и Rewards. `.weightbar/.weight-value/.wrapper` остаются потребителями старой шкалы Loot. `.item-img-wrapper` и `.item-show .fa` обслуживают прежний item-image helper; текущие строки используют display-details и правила tab-inventory-list.css.

Колонки различаются: weapon-header 33px/2fr/1fr, weapon-details 40px/2fr/1fr; armor-header 33px/1fr/1fr и armor-details 40px/1fr/1fr; valuable-header/spell-header 33px/6fr/1fr, вложенные заголовки 33px/1.5fr/1fr, строки 40px/1.5fr/1fr. Сам display:grid задаёт соседний CSS. Эти значения не определяют поля Item и не синхронизируют размеры отдельным алгоритмом.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 7 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | carry-section, carry-bar, overweight, currency-section, valuable-header | Текущий инвентарь персонажа, порог >=, валюты и разделы. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | weapon-header/details/enhancement, enhancement-list, item-tag | Оружие, ячейки и установленные улучшения. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | armor-header/details, weapon-enhancement, item-tag | Броня использует также общий блок улучшений оружия. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | container-stored-item, progress-bar-stored-weight, stored-item-info | Контейнеры и прочие вещи. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | stored-item-img/label, valuable-details | Компоненты рецепта и строка чертежа. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | item-tag, valuables-list-header, valuable-details | Алхимические Item. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | item-tag, valuables-list-header, valuable-details | Компоненты. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs) | item-tag, valuables-list-header, valuable-details | Ездовые животные. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | enhancement-effects-name, item-tag, valuable-details | Руны и глифы. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | spell-list-header/details, item-tag, stored-item-info | Текущие строки магии обоих Actor. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/character/substances.hbs](../../../../../templates/partials/character/substances.hbs) | valuable-header | Заголовок веществ. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/item-image.hbs](../../../../../templates/partials/item-image.hbs) | item-img-wrapper, item-show, .fa | Старый helper изображения; не текущие inventory PARTS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../templates/partials/monster/monster-inventory-tab.hbs) | enhancement-slot, item-enhancement, no-margin | Старый инвентарь монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../templates/sheets/actor/loot-sheet.hbs) | weightbar, weight-value, wrapper, currency | Текущий зарегистрированный лист Loot на V1. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/rewards/currency.hbs](../../../../../templates/sheets/actor/rewards/currency.hbs) | currency | Текущий журнал наград. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/chat/item/item-description.hbs](../../../../../templates/chat/item/item-description.hbs) | item-tags | Обёртка тегов сообщения Item. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/chat/item/partials/item-description/tags.hbs](../../../../../templates/chat/item/partials/item-description/tags.hbs) | item-tag, item-tags | Теги типов Item. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/chat/item/partials/item-description/crafting-items.hbs](../../../../../templates/chat/item/partials/item-description/crafting-items.hbs) | stored-item-img/label | Компоненты рецепта в сообщении. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../module/actor/sheets/WitcherActorSheet.js) | _prepareGeneralInformation, _prepareWeapons, _prepareArmor | Производитель totalWeight и списков; CSS не вызывает эти методы. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../module/actor/sheets/mixins/itemMixin.js) | _onEnhancementInfo, itemListener | Раскрытие enhancement-info; экипировка и Item-действия. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/tab-inventory-list.css](../../../../../styles/tab-inventory-list.css) | .list-header, .section-header, .list-details | Более поздний display:grid и оформление списков. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/components-list.css](../../../../../styles/components-list.css) | th:nth-child(n+2) | Более позднее глобальное центрирование заголовков — issue-00309. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/inventory.css](../../../../../styles/monster/inventory.css) | .tab.active.inventory .weapon-section/.armor-section/.valuable-section | Текущая специализация секций монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. Обращений var(...) в этом файле нет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | carry-section, carry-bar, overweight, currency-section, valuable-header | Текущий инвентарь персонажа, порог >=, валюты и разделы. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | weapon-header/details/enhancement, enhancement-list, item-tag | Оружие, ячейки и установленные улучшения. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | armor-header/details, weapon-enhancement, item-tag | Броня использует также общий блок улучшений оружия. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs) | container-stored-item, progress-bar-stored-weight, stored-item-info | Контейнеры и прочие вещи. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | stored-item-img/label, valuable-details | Компоненты рецепта и строка чертежа. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs) | item-tag, valuables-list-header, valuable-details | Алхимические Item. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | item-tag, valuables-list-header, valuable-details | Компоненты. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-mounts.hbs) | item-tag, valuables-list-header, valuable-details | Ездовые животные. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-runes-glyphs.hbs) | enhancement-effects-name, item-tag, valuable-details | Руны и глифы. |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | spell-list-header/details, item-tag, stored-item-info | Текущие строки магии обоих Actor. |
| [templates/partials/character/substances.hbs](../../../../../templates/partials/character/substances.hbs) | valuable-header | Заголовок веществ. |
| [templates/partials/item-image.hbs](../../../../../templates/partials/item-image.hbs) | item-img-wrapper, item-show, .fa | Старый helper изображения; не текущие inventory PARTS. |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../templates/partials/monster/monster-inventory-tab.hbs) | enhancement-slot, item-enhancement, no-margin | Старый инвентарь монстра. |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../templates/sheets/actor/loot-sheet.hbs) | weightbar, weight-value, wrapper, currency | Текущий зарегистрированный лист Loot на V1. |
| [templates/sheets/actor/rewards/currency.hbs](../../../../../templates/sheets/actor/rewards/currency.hbs) | currency | Текущий журнал наград. |
| [templates/chat/item/item-description.hbs](../../../../../templates/chat/item/item-description.hbs) | item-tags | Обёртка тегов сообщения Item. |
| [templates/chat/item/partials/item-description/tags.hbs](../../../../../templates/chat/item/partials/item-description/tags.hbs) | item-tag, item-tags | Теги типов Item. |
| [templates/chat/item/partials/item-description/crafting-items.hbs](../../../../../templates/chat/item/partials/item-description/crafting-items.hbs) | stored-item-img/label | Компоненты рецепта в сообщении. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 297 логических строк и PostCSS 8.5.12 | 48 rule-узлов, 147 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 2–4/6/12: carry при 9/10, 10/10, 11/10; реальные строки оружия, скрытая информация и изменение equipped; AST значений цвета; три секции инвентаря монстра. Все 48 правил и 147 declarations перечислены. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 7. Глобальные правила действуют также в чате и других листах. tab-inventory-list.css (26) задаёт grid-контейнеры; components-list.css (24) содержит более специфичный глобальный th:nth-child(n+2). Цвета progress зависят от vendor-псевдоэлемента и appearance ядра; computed styles не проверялись. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00063](../../../../issues/potential/issue-00063.md), [issue-00177](../../../../issues/potential/issue-00177.md), [issue-00178](../../../../issues/potential/issue-00178.md), [issue-00179](../../../../issues/potential/issue-00179.md), [issue-00307](../../../../issues/potential/issue-00307.md), [issue-00309](../../../../issues/potential/issue-00309.md), [issue-00310](../../../../issues/potential/issue-00310.md), [issue-00311](../../../../issues/potential/issue-00311.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003049) |
