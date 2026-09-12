# styles/item-sheets.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/item-sheets.css](../../../../../styles/item-sheets.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 117 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Общие классы форм Item: опции, колонки, таблицы, поля воздействий, блоки магии и редактор описания. Некоторые глобальные правила также достигают Loot и расследований.

## Условия использования

Импорт 15, позже profession-sheet.css и раньше item-header.css. item-table в нынешних списках Actor часто стоит на ol: правило td там не совпадает; старый monster-inventory-tab содержит настоящую table. Простое присутствие класса не доказывает применение каждой декларации. .description с textarea не получает высоту .editor; в diagrams редактор создаётся helper. Дополнительные table.item-table есть в valuable/hex; .itemname — в clue/obstacle. Позднее .item-header конкретизирует общую шапку.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 22 CSS-правил и 51 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `.itemname` | 1 | `text-align: center` |
| `.item-options` | 5 | `display: flex`; `text-align: center`; `justify-content: space-around`; `margin-top: 1px`; `height: 54px` |
| `.item-option-tickbox` | 13 | `display: flex`; `height: 27px`; `justify-content: space-between`; `align-items: center`; `padding: 0 5px` |
| `.item-column` | 21 | `text-align: center`; `width: 168px` |
| `.item-column label` | 26 | `display: block` |
| `.item-row` | 30 | `display: flex`; `text-align: center` |
| `.item-second-column` | 35 | `text-align: center`; `width: 50%` |
| `.item-second-column label` | 40 | `display: block`; `width: 100%` |
| `.weapon-dmg-type` | 45 | `display: flex`; `flex-wrap: wrap`; `padding: 0`; `width: 100px`; `margin: auto` |
| `.weapon-dmg-type label` | 54 | `display: flex`; `margin: auto`; `align-items: center` |
| `.item-bottom-table` | 60 | `text-align: center` |
| `.item-bottom-table input` | 64 | `display: block`; `width: 75px`; `height: 27px`; `margin: auto` |
| `.item-effect` | 71 | `width: 90% !important` |
| `.item-bottom-table-one` | 75 | `width: 200px` |
| `.item-table td` | 79 | `text-align: center`; `padding: 0.25em 0.25em` |
| `.item-table td.effect-text-area` | 84 | `display: flex`; `flex-direction: column`; `width: 100%` |
| `.item-table td.effect-text-area → label` | 89 | `text-align: start` |
| `.spell-template-damage` | 94 | `width: 15em`; `margin-top: 0.6em` |
| `.spell-template-damage input` | 99 | `float: right` |
| `.spell-template-damage div` | 103 | `display: flex`; `height: 27px`; `justify-content: space-between`; `align-items: center` |
| `.description .editor` | 110 | `height: 75px` |
| `.description label` | 114 | `display: flex`; `justify-content: center` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

Все правила перечислены ниже. item-options — строка высотой 54px, tickbox — строка 27px с padding 0 5px, item-column — 168px. weapon-dmg-type — flex-wrap и ширина 100px, его labels — flex. Таблицы item-bottom-table центрируются, input — 75×27, item-bottom-table-one — 200px. item-effect задаёт width 90% !important. .item-table td получает center и padding .25em; td.effect-text-area — колонка шириной 100%, вложенный label — text-align:start. spell-template-damage — 15em/margin-top .6em; input float:right, div — flex высотой 27px. .description .editor — height 75px, label центрируется. .item-row и .item-second-column с их дочерним label не имеют найденных HTML/JS-потребителей в module/templates; это не самостоятельная ошибка.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/weapon-sheet.hbs](../../../../../templates/sheets/item/weapon-sheet.hbs) | item-options/column/tickbox, weapon-dmg-type, item-bottom-table-one | Форма оружия, флаги и тип урона. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/component-sheet.hbs](../../../../../templates/sheets/item/component-sheet.hbs) | item-options/item-column | Выбор типа/свойств компонента; прежняя проблема helper select ограничивает штатный рендер. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/enhancement-sheet.hbs](../../../../../templates/sheets/item/enhancement-sheet.hbs) | item-options/column, item-bottom-table/item-effect | Форма улучшения. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/armor-sheet.hbs](../../../../../templates/sheets/item/armor-sheet.hbs) | item-table/item-bottom-table/item-effect | Броня и её воздействия. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/alchemical-sheet.hbs](../../../../../templates/sheets/item/alchemical-sheet.hbs) | item-table td.effect-text-area | Текст эффекта и выравнивание label. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../templates/sheets/item/diagrams-sheet.hbs) | item-table/item-bottom-table/item-effect, description/editor | Редактор рецепта и legacy editor. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/spell-sheet.hbs](../../../../../templates/sheets/item/spell-sheet.hbs) | spell-template-damage/item-table | Поля области/магии. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/ritual-sheet.hbs](../../../../../templates/sheets/item/ritual-sheet.hbs) | spell-template-damage/item-table | Аналогичный блок ритуала. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) | item-bottom-table/item-effect | Редактор предметных воздействий. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) | item-bottom-table/item-effect | Конфигурация расходования. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | item-bottom-table/item-effect | Эффекты магии. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | item-bottom-table/item-effect | Профессиональные атаки и пороги. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/partials/associated-item.hbs](../../../../../templates/partials/associated-item.hbs) | item-bottom-table/description | Связанный результат рецепта. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/partials/associated-diagram.hbs](../../../../../templates/partials/associated-diagram.hbs) | item-bottom-table/description | Связанный рецепт. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../templates/sheets/actor/loot-sheet.hbs) | table.item-table | Общие td Loot. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../../../templates/sheets/investigation/mystery-sheet.hbs) | table.item-table | Общие td расследования. | Исходники, поиск module/templates/styles и AST; границы ниже |



## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/sheets/item/weapon-sheet.hbs](../../../../../templates/sheets/item/weapon-sheet.hbs) | item-options/column/tickbox, weapon-dmg-type, item-bottom-table-one | Форма оружия, флаги и тип урона. |
| [templates/sheets/item/component-sheet.hbs](../../../../../templates/sheets/item/component-sheet.hbs) | item-options/item-column | Выбор типа/свойств компонента; прежняя проблема helper select ограничивает штатный рендер. |
| [templates/sheets/item/enhancement-sheet.hbs](../../../../../templates/sheets/item/enhancement-sheet.hbs) | item-options/column, item-bottom-table/item-effect | Форма улучшения. |
| [templates/sheets/item/armor-sheet.hbs](../../../../../templates/sheets/item/armor-sheet.hbs) | item-table/item-bottom-table/item-effect | Броня и её воздействия. |
| [templates/sheets/item/alchemical-sheet.hbs](../../../../../templates/sheets/item/alchemical-sheet.hbs) | item-table td.effect-text-area | Текст эффекта и выравнивание label. |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../templates/sheets/item/diagrams-sheet.hbs) | item-table/item-bottom-table/item-effect, description/editor | Редактор рецепта и legacy editor. |
| [templates/sheets/item/spell-sheet.hbs](../../../../../templates/sheets/item/spell-sheet.hbs) | spell-template-damage/item-table | Поля области/магии. |
| [templates/sheets/item/ritual-sheet.hbs](../../../../../templates/sheets/item/ritual-sheet.hbs) | spell-template-damage/item-table | Аналогичный блок ритуала. |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) | item-bottom-table/item-effect | Редактор предметных воздействий. |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) | item-bottom-table/item-effect | Конфигурация расходования. |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | item-bottom-table/item-effect | Эффекты магии. |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | item-bottom-table/item-effect | Профессиональные атаки и пороги. |
| [templates/partials/associated-item.hbs](../../../../../templates/partials/associated-item.hbs) | item-bottom-table/description | Связанный результат рецепта. |
| [templates/partials/associated-diagram.hbs](../../../../../templates/partials/associated-diagram.hbs) | item-bottom-table/description | Связанный рецепт. |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../templates/sheets/actor/loot-sheet.hbs) | table.item-table | Общие td Loot. |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../../../templates/sheets/investigation/mystery-sheet.hbs) | table.item-table | Общие td расследования. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 22 правил, 51 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | 22 AST-правила / 51 declaration, включая вложенный label и !important. Поиск имён классов выполнен в module/templates, реальные class-атрибуты сверены отдельно от совпадений путей/полей. Браузерные размеры редакторов не измерялись. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | Импорт 15, позже profession-sheet.css и раньше item-header.css. item-table в нынешних списках Actor часто стоит на ol: правило td там не совпадает; старый monster-inventory-tab содержит настоящую table. Простое присутствие класса не доказывает применение каждой декларации. .description с textarea не получает высоту .editor; в diagrams редактор создаётся helper. Дополнительные table.item-table есть в valuable/hex; .itemname — в clue/obstacle. Позднее .item-header конкретизирует общую шапку. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы.

## Связанные проблемы

Новой проблемы в пределах данного файла не зарегистрировано. Это не вывод об исправности всех связанных процессов.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |
