# styles/witcher-styles.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 3f78cbf0372e1da3d5a840e41b456d954c64e403 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.050](../../../../tasks/task-0003.050.md), 7 файлов / 582 логических строк; данный файл — 77 |
| Запись перекрёстной сверки | [TASK-0003.050](../../review-log.md#task-0003050) |

## Назначение файла

Единственная CSS-точка входа манифеста: подключает все 35 остальных CSS, объявляет шрифт Thewitcher и общие классы сетки/раскрытия навыков.

## Условия использования

[system.json](../../../../../system.json):23 объявляет styles/witcher-styles.css; браузер загружает относительные @import в указанном ниже порядке, затем собственные правила. Файл не импортируется через JavaScript. Все 36 CSS реестра представлены один раз, дочерних импортов нет.

## Введённые сущности и действия с ними

JavaScript-сущностей и полей модели нет. Ниже все 6 rule-узлов и 16 declarations внутри них; внешняя вложенность сохранена. Запятые в селекторе остаются на своём уровне, стрелка обозначает CSS nesting, а не новую HTML-обёртку.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 45 | Корень | `.witcher-style` | `font-family: Thewitcher` |
| 49 | Корень | `.skill-column details summary > *` | `display: inline` |
| 53 | Корень | `.skill-column details[open] > summary::before` | `transform: rotate(-135deg) translatey(-0.3em)` |
| 57 | Корень | `.skill-column summary` | `list-style: none`; `padding-left: 4px`; `cursor: pointer` |
| 63 | Корень | `.skill-column summary::before` | `display: inline-block`; `content: ''`; `border-right: 2px solid`; `border-bottom: 2px solid`; `position: relative`; `left: 0`; `height: 0.75em`; `width: 0.75em`; `transform: rotate(45deg) translatey(-0.1em)` |
| 75 | Корень | `.grid` | `display: grid` |

@font-face:40–43: font-family:'Thewitcher'; src:url('./fonts/thewitcher2.ttf'). Это ещё два объявления, вне rule-узлов. Шрифт [thewitcher2.ttf](../../../../../styles/fonts/thewitcher2.ttf) существует; ресурс исключён из пофайлового аудита, собственной карточки не получает.

| № импорта | Строка | Файл и полная карточка |
| --- | --- | --- |
| 1 | 1 | [styles/character-header.css](character-header.css.md) |
| 2 | 2 | [styles/armor-sheet.css](armor-sheet.css.md) |
| 3 | 3 | [styles/attack-sheet.css](attack-sheet.css.md) |
| 4 | 4 | [styles/system-styles.css](system-styles.css.md) |
| 5 | 5 | [styles/monster-sheet.css](monster-sheet.css.md) |
| 6 | 6 | [styles/tab-background.css](tab-background.css.md) |
| 7 | 7 | [styles/tab-inventory.css](tab-inventory.css.md) |
| 8 | 8 | [styles/currency-converter.css](currency-converter.css.md) |
| 9 | 9 | [styles/tab-skills.css](tab-skills.css.md) |
| 10 | 10 | [styles/monster-skill-tab.css](monster-skill-tab.css.md) |
| 11 | 11 | [styles/loot-sheet.css](loot-sheet.css.md) |
| 12 | 12 | [styles/profession-sheet.css](profession-sheet.css.md) |
| 13 | 13 | [styles/race-sheet.css](race-sheet.css.md) |
| 14 | 14 | [styles/crit-wounds-table.css](crit-wounds-table.css.md) |
| 15 | 15 | [styles/item-sheets.css](item-sheets.css.md) |
| 16 | 16 | [styles/substances.css](substances.css.md) |
| 17 | 17 | [styles/weapon-roll.css](weapon-roll.css.md) |
| 18 | 18 | [styles/container-sheet.css](container-sheet.css.md) |
| 19 | 19 | [styles/chat.css](chat.css.md) |
| 20 | 20 | [styles/item-header.css](item-header.css.md) |
| 21 | 21 | [styles/activeEffect.css](activeEffect.css.md) |
| 22 | 22 | [styles/special-skill-table.css](special-skill-table.css.md) |
| 23 | 23 | [styles/repair.css](repair.css.md) |
| 24 | 24 | [styles/components-list.css](components-list.css.md) |
| 25 | 25 | [styles/dialog.css](dialog.css.md) |
| 26 | 26 | [styles/tab-inventory-list.css](tab-inventory-list.css.md) |
| 27 | 27 | [styles/rewards.css](rewards.css.md) |
| 28 | 29 | [styles/character/sheet.css](character/sheet.css.md) |
| 29 | 30 | [styles/character/tab-profession.css](character/tab-profession.css.md) |
| 30 | 32 | [styles/monster/header.css](monster/header.css.md) |
| 31 | 33 | [styles/monster/inventory.css](monster/inventory.css.md) |
| 32 | 34 | [styles/monster/sheet.css](monster/sheet.css.md) |
| 33 | 35 | [styles/monster/sidebar.css](monster/sidebar.css.md) |
| 34 | 36 | [styles/monster/details.css](monster/details.css.md) |
| 35 | 38 | [styles/configurations/modifier-configuration.css](configurations/modifier-configuration.css.md) |

## Основные функции и методы

JavaScript-функций нет; селекторы и каскад обрабатывает браузер.

@font-face определяет Thewitcher, но само объявление не заставляет интерфейс его использовать. [module/TheWitcherTRPG.js](../../../../../module/TheWitcherTRPG.js):77–87 добавляет witcher-style к элементам .game и #chat-log при useWitcherFont только после успешного getIndex (issue-00002). Селектор .witcher-style задаёт наследуемый font-family. [module/setup/settings.js](../../../../../module/setup/settings.js) регистрирует настройку.

Четыре правила .skill-column настраивают summary/details: содержимое summary становится inline, маркер заменяется рамками псевдоэлемента, [open] получает поворот −135° вместо 45°. Более специфичное правило открытого details действует, хотя стоит раньше общего ::before. Current tab-skills.hbs используется персонажем и монстром; прежний monster-skill-tab.hbs тоже содержит skill-column, но не является текущим PARTS.

.grid — глобальный display:grid. Его явные текущие потребители: [templates/sheets/item/spell-sheet.hbs](../../../../../templates/sheets/item/spell-sheet.hbs):41/45, [templates/sheets/item/hex-sheet.hbs](../../../../../templates/sheets/item/hex-sheet.hbs):58/62 и [templates/sheets/item/valuable-sheet.hbs](../../../../../templates/sheets/item/valuable-sheet.hbs):27. Это сетки полей/описания предметов; число колонок сам utility-класс не задаёт.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и назначение | Основание |
| --- | --- | --- | --- |
| [system.json](../../../../../system.json) | styles | Загрузка входного файла, строка 23. | Исходные определения/обращения, AST и проверки ниже |
| [module/TheWitcherTRPG.js](../../../../../module/TheWitcherTRPG.js) | ready; witcher-style | Динамический потребитель font-family при включённой настройке. | Исходные определения/обращения, AST и проверки ниже |
| [module/setup/settings.js](../../../../../module/setup/settings.js) | useWitcherFont | Регистрирует условие добавления класса. | Исходные определения/обращения, AST и проверки ниже |
| [templates/partials/character/tab-skills.hbs](../../../../../templates/partials/character/tab-skills.hbs) | skill-column; details/summary | Текущий общий шаблон навыков; маркировка раскрывающихся блоков. | Исходные определения/обращения, AST и проверки ниже |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../templates/partials/monster/monster-skill-tab.hbs) | skill-column | Прежний шаблон, отдельно от текущего зарегистрированного листа. | Исходные определения/обращения, AST и проверки ниже |

Внешняя среда: браузер CSS/DOM; Foundry 14.367.0 — client/applications/api/application.mjs (_prepareTabs и объединение классов), public/css/foundry2.css (общие стили и скрытие неактивных tab[data-tab]). Это внешние API, а не функции CSS системы. Ключей локализации и CSS var(...) в собственных правилах этого файла нет.

## Известные потребители

| Потребитель | Используемая сущность и условия |
| --- | --- |
| [system.json](../../../../../system.json) | styles: Загрузка входного файла, строка 23. |
| [module/TheWitcherTRPG.js](../../../../../module/TheWitcherTRPG.js) | ready; witcher-style: Динамический потребитель font-family при включённой настройке. |
| [templates/partials/character/tab-skills.hbs](../../../../../templates/partials/character/tab-skills.hbs) | skill-column; details/summary: Текущий общий шаблон навыков; маркировка раскрывающихся блоков. |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../templates/partials/monster/monster-skill-tab.hbs) | skill-column: Прежний шаблон, отдельно от текущего зарегистрированного листа. |

Область поиска — module/, templates/, styles/ и манифест. Прежний шаблон не объявляется текущим на основании одного CSS-класса; выбор действующих PARTS сверялся с листами. CSS не импортирует классы JavaScript. Сторонние темы, пользовательский HTML и макросы не исследованы.

## Данные и изменения состояния

Файл меняет представление элементов при совпадении селекторов. Не создаёт и не обновляет Actor/Item/эффекты, не вычисляет характеристики и не сохраняет состояние флажков. CSS-класс, отключённый input и скрытый элемент не являются проверкой прав на сервере.

## Проверки и доказательства

Полное чтение 77 логических строк; PostCSS 8.5.12. C01/C02: 35 уникальных импортов, все 36 CSS, единственный URL шрифта существует; исходный ready при font=true добавил два класса, при false — ни одного, при отсутствующем pack до классов не дошёл.

[Методика, результаты и сверка серии](../../review-log.md#task-0003050). Настоящие HBS/helpers и отдельный callback ready исполнены в Node 24.16.0; Handlebars 4.7.9, parse5 из Foundry. Контексты и документные/DOM-операции заданы фасадами; исходники и БД не менялись. AST проверяет структуру и полноту документации, не итоговую отрисовку.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Браузер, HTTP-загрузка шрифта, computedStyle, размеры/переполнение, реальное переключение вкладок, hover и поддержка nesting/light-dark в конкретном клиенте не проверялись. Локальное существование ресурса не доказывает доступ службы Foundry.

## Связанные проблемы

[issue-00002](../../../../issues/potential/issue-00002.md). Сохраняют статус potential; регистрация не означает подтверждения или исправления.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 3f78cbf0372e1da3d5a840e41b456d954c64e403; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003050) |
