# styles/character-header.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/character-header.css](../../../../../styles/character-header.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 758 |
| Запись перекрёстной сверки | [TASK-0003.049](../../review-log.md#task-0003049) |

## Назначение файла

Общие кнопки характеристик и навыков, заголовок персонажа, ресурсы и переключатели обоих Actor; также поля конфигурации и прежние боковые панели.

## Условия использования

Импорт 1, раньше остальных стилей системы. Более поздний CSS может переопределять общие имена, а правила с корнем .application.sheet.witcher.monster имеют большую специфичность. У файла нет собственного root-scope, @media или imports; light-dark()/CSS-переменные и vendor-элементы исполняет браузер. Карта ниже охватывает 128 правил, включая пустые контейнеры вложенности, и 352 declarations.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 128 CSS rule-узлов и 352 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.char-header` | `display: flex`; `flex-direction: row` |
| 6 | Корень | `.char-sidebar` | `display: flex`; `flex-direction: column` |
| 11 | Корень | `.stat-grid` | `display: flex`; `flex-wrap: wrap`; `gap: 10px` |
| 17 | Корень | `.char-stat-title` | `font-weight: bold`; `margin-bottom: 5px` |
| 22 | Корень | `.char-stat-button, .char-derived-button` | `display: flex`; `flex-direction: column`; `justify-content: center`; `align-items: center`; `border: 1px solid light-dark(#22222240, #e7d1b140)`; `color: light-dark(black, white)`; `transition: all 0.3s ease`; `min-width: 160px`; `min-height: 50px`; `box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.25)`; `border-radius: 3px`; `padding: 0 10px`; `text-shadow: none` |
| 38 | `.char-stat-button, .char-derived-button` | `.label` | `font-size: 18px` |
| 42 | `.char-stat-button, .char-derived-button` | `.mod` | `display: flex`; `justify-content: center`; `gap: 20px`; `font-size: 14px`; `width: 56px` |
| 49 | `.char-stat-button, .char-derived-button` → `.mod` | `.max, .stat-mod-zero` | `color: light-dark(#174FC8, #7099F0)` |
| 54 | `.char-stat-button, .char-derived-button` → `.mod` | `.stat-mod-plus` | `color: light-dark(#299446, #56C574)` |
| 58 | `.char-stat-button, .char-derived-button` → `.mod` | `.stat-mod-minus` | `color: light-dark(#EB2B2B, #E86363)` |
| 63 | `.char-stat-button, .char-derived-button` | `.skill-icons` | `display: flex`; `gap: 10px`; `font-size: 14px`; `margin: 5px 0`; `color: light-dark(black, white)` |
| 72 | Корень | `.char-stat-button:hover` | `background: light-dark(#22222240, #e7d1b140)` |
| 76 | Корень | `.char-stat-button.skill` | Только вложенность; собственных свойств нет |
| 77 | `.char-stat-button.skill` | `.label, .skill-icons` | `font-size: 14px` |
| 83 | Корень | `.char-stat-button.skill.profession` | `background: rgba(85, 107, 47, 0.35)` |
| 86 | Корень | `.char-stat-button.skill.profession:hover` | `background: rgba(107, 142, 35, 0.45)` |
| 90 | Корень | `.char-stat-button.skill.learned` | `background: rgba(32, 95, 171, 0.35)` |
| 93 | Корень | `.char-stat-button.skill.learned:hover` | `background: rgba(60, 130, 210, 0.45)` |
| 97 | Корень | `.char-stat-button.skill.pickup` | `background: rgba(175, 50, 50, 0.35)` |
| 100 | Корень | `.char-stat-button.skill.pickup:hover` | `background: rgba(210, 70, 70, 0.45)` |
| 104 | Корень | `.reputation-button` | `width: 105px`; `text-transform: uppercase` |
| 109 | Корень | `.stat-info, .derived-info` | `align-items: center` |
| 114 | Корень | `.stat-modifiers, .skill-modifiers, .derived-modifiers` | `margin-top: 5px` |
| 120 | Корень | `.stat-info > h4, .char-stat-label, .stat-mod, .derived-info` | `margin-bottom: 0` |
| 127 | Корень | `.stat-mod` | `height: 30px`; `width: 35px`; `place-content: center` |
| 133 | Корень | `.stat-max` | `height: 30px`; `width: 35px` |
| 138 | Корень | `input.stat-max` | `border: none`; `padding: 0`; `line-height: 20px` |
| 144 | Корень | `input.header-stat` | `font-weight: bold`; `width: 35px`; `height: 30px` |
| 150 | Корень | `.total-stats` | `display: flex`; `gap: 20px`; `border: 1px solid light-dark(#22222240, #e7d1b140)`; `border-radius: 3px`; `align-items: center`; `justify-content: center`; `height: 50px`; `min-width: 160px`; `padding: 0 10px` |
| 162 | Корень | `.total-stats > h4` | `margin-bottom: 0`; `border-bottom: none`; `font-weight: bold` |
| 168 | Корень | `.total-stats-label` | Только вложенность; собственных свойств нет |
| 171 | Корень | `input.total-stats-show` | `width: 35px`; `font-weight: bold`; `text-align: center` |
| 177 | Корень | `.char-stat-label` | `width: 70px`; `height: 30px`; `background-color: rgba(255, 255, 255, 0.2)`; `border-radius: 10px 0 0 10px`; `color: black`; `padding: 0 5px 0`; `place-content: center` |
| 187 | Корень | `.char-header-center` | `flex-grow: 1`; `height: fit-content` |
| 191 | `.char-header-center` | `h1` | `margin-bottom: 0` |
| 196 | Корень | `.header-center label` | `font-weight: bold` |
| 200 | Корень | `input.charname` | `height: auto`; `border: none` |
| 205 | Корень | `.char-center-middle` | `display: flex`; `flex-direction: column`; `margin-bottom: 2px`; `margin-top: 2px` |
| 212 | Корень | `.char-general` | `margin-top: 5px`; `margin-bottom: 5px` |
| 217 | Корень | `.char-general > span > *` | `border: none` |
| 221 | Корень | `.char-actions` | `display: flex`; `align-items: center`; `gap: 20px`; `margin-top: 12px` |
| 227 | `.char-actions` | `.action` | `display: flex`; `justify-content: space-between`; `align-items: center`; `border: 1px solid light-dark(#22222240, #e7d1b140)`; `border-radius: 5px`; `padding: 5px 10px 5px`; `width: 125px` |
| 236 | `.char-actions` → `.action` | `h3` | `margin: 0`; `font-weight: 300` |
| 241 | `.char-actions` → `.action` | `.death-counter` | `display: flex`; `flex-direction: row`; `align-items: center`; `gap: 5px` |
| 247 | `.char-actions` → `.action` → `.death-counter` | `h3` | `margin: 0`; `font-weight: 300` |
| 255 | Корень | `.char-image` | `position: relative` |
| 258 | `.char-image` | `.witcher-actor-img` | `height: 130px`; `width: 130px`; `border-radius: 3px`; `object-fit: cover` |
| 265 | `.char-image` | `.wound-state` | `display: flex`; `justify-content: center`; `align-items: center`; `padding: 5px`; `position: absolute`; `width: 40px`; `height: 40px`; `right: 0`; `bottom: 0`; `background: rgba(34, 34, 34, 0.4)`; `backdrop-filter: blur(4px)`; `border-radius: 5px 0px 3px`; `font-size: 28px` |
| 283 | Корень | `.core-stats-list` | `margin: 10px 0` |
| 287 | Корень | `.core-stats-label` | `text-align: center`; `display: inline-block`; `width: 60px` |
| 293 | Корень | `.core-stats.minmax` | `text-align: center`; `display: inline-block` |
| 298 | Корень | `.char-right-sidebar` | `justify-items: center`; `color: light-dark(black, white)` |
| 303 | Корень | `.right-element` | `float: left`; `margin: auto`; `width: 50%`; `height: 110px`; `text-align: center` |
| 311 | Корень | `.right-image` | `height: 75px`; `margin-left: 20px`; `margin-right: 20px`; `border: 0` |
| 318 | Корень | `.right-row` | `size: 75px` |
| 322 | Корень | `.right-row label` | `position: relative` |
| 326 | Корень | `input.right-value` | `position: relative`; `bottom: 55px`; `width: 40px`; `font-size: 25px`; `border: none`; `background: none`; `color: #000` |
| 336 | Корень | `.right-value::placeholder` | `color: black` |
| 340 | Корень | `.right-max` | `position: relative`; `bottom: 84px`; `left: 54px`; `border: none`; `text-align: left`; `width: 50px`; `font-size: 25px`; `color: #000` |
| 351 | Корень | `.right-top` | `display: flex`; `margin-bottom: 10px`; `justify-content: center` |
| 357 | Корень | `.char-button-list` | `display: flex`; `gap: 10px`; `flex-wrap: wrap` |
| 363 | Корень | `.optional-stats-collum` | `display: grid`; `grid-template-columns: 90px 90px`; `gap: 10px`; `margin-bottom: 10px` |
| 370 | Корень | `.button-roll` | `display: flex`; `width: 30px`; `height: 30px`; `align-items: center`; `justify-content: center`; `border-radius: 50%`; `font-size: 18px`; `text-align: center` |
| 381 | Корень | `a.button-roll:hover` | `text-shadow: none` |
| 385 | Корень | `.init-roll` | `background-color: #a4a7f2`; `color: #372362` |
| 390 | Корень | `.init-roll:hover` | `background-color: #7e81db` |
| 394 | Корень | `.death-roll` | `background-color: #f2a4a4`; `color: #622323` |
| 399 | Корень | `.death-roll:hover` | `background-color: #e06d6d` |
| 403 | Корень | `.heal-button, .button-roll.export-loot` | `background-color: #aff2a4`; `color: #236231` |
| 409 | Корень | `.heal-button:hover, .button-roll.export-loot:hover` | `background-color: #79cc6b` |
| 414 | Корень | `.crit-roll` | `background-color: #f2d3a4`; `color: #573f22` |
| 419 | Корень | `.crit-roll:hover` | `background-color: #dbb06f` |
| 423 | Корень | `.recover-sta` | `background-color: #a4ccf2`; `color: #1d384d` |
| 428 | Корень | `.recover-sta:hover` | `background-color: #71a8da` |
| 432 | Корень | `.verbal-button` | `background-color: #f2a4ea`; `color: #592362` |
| 437 | Корень | `.verbal-button:hover` | `background-color: #e366d7` |
| 441 | Корень | `.global-modifier-column` | `flex: 1` |
| 445 | Корень | `.progress-container > h3` | `border-bottom: none`; `margin: 0` |
| 450 | Корень | `.death-counter > i` | `padding-top: 2px`; `padding-bottom: 3px` |
| 455 | Корень | `.status-section` | `display: flex`; `flex-direction: column`; `margin-top: 10px`; `gap: 5px` |
| 462 | Корень | `.hp-bar, .sta-bar, .toxicity-bar, .focus-bar, .resolve-bar` | `height: 20px`; `width: 130px` |
| 471 | Корень | `.hp-bar, .hp-bar::-webkit-progress-bar` | `border: none`; `background-color: rgba(153, 6, 6, 0.1)`; `border-radius: 0 5px 5px 5px` |
| 478 | Корень | `.hp-bar::-webkit-progress-value` | `background-color: #e30000`; `border-radius: 0 5px 5px 5px` |
| 482 | Корень | `.hp-bar::-moz-progress-value, .hp-bar::-moz-progress-bar` | `border-radius: 0 5px 5px 5px` |
| 487 | Корень | `.hp-bar::-moz-progress-bar` | `background-color: #e30000` |
| 491 | Корень | `.sta-bar, .sta-bar::-webkit-progress-bar` | `border: none`; `background-color: rgba(23, 114, 153, 0.1)`; `border-radius: 0 5px 5px 5px` |
| 498 | Корень | `.sta-bar::-webkit-progress-value` | `background-color: #14abec`; `border-radius: 0 5px 5px 5px` |
| 503 | Корень | `.sta-bar::-moz-progress-value, .sta-bar::-moz-progress-bar` | `border-radius: 0 5px 5px 5px` |
| 508 | Корень | `.sta-bar::-moz-progress-bar` | `background-color: #14abec` |
| 512 | Корень | `.toxicity-bar, .toxicity-bar::-webkit-progress-bar` | `border: none`; `background-color: rgba(41, 153, 23, 0.1)`; `border-radius: 0 5px 5px 5px` |
| 519 | Корень | `.toxicity-bar::-webkit-progress-value` | `background-color: #2eb917`; `border-radius: 0 5px 5px 5px` |
| 524 | Корень | `.toxicity-bar::-moz-progress-bar, .toxicity-bar::-moz-progress-value` | `border-radius: 0 5px 5px 5px` |
| 529 | Корень | `.toxicity-bar::-moz-progress-bar` | `background-color: #2eb917` |
| 533 | Корень | `.focus-bar, .focus-bar::-webkit-progress-bar` | `border: none`; `background-color: #7C14EC10`; `border-radius: 0 5px 5px 5px` |
| 540 | Корень | `.focus-bar::-webkit-progress-value` | `background-color: #7C14EC`; `border-radius: 0 5px 5px 5px` |
| 545 | Корень | `.focus-bar::-moz-progress-bar, .focus-bar::-moz-progress-value` | `border-radius: 0 5px 5px 5px` |
| 550 | Корень | `.focus-bar::-moz-progress-bar` | `background-color: #7C14EC` |
| 554 | Корень | `.resolve-bar, .resolve-bar::-webkit-progress-bar` | `border: none`; `background-color: #59236210`; `border-radius: 0 5px 5px 5px` |
| 561 | Корень | `.resolve-bar::-webkit-progress-value` | `background-color: #f2a4ea`; `border-radius: 0 5px 5px 5px` |
| 566 | Корень | `.resolve-bar::-moz-progress-bar, .resolve-bar::-moz-progress-value` | `border-radius: 0 5px 5px 5px` |
| 571 | Корень | `.resolve-bar::-moz-progress-bar` | `background-color: #f2a4ea` |
| 575 | Корень | `.progress-container` | `display: flex`; `flex-direction: column`; `align-items: start`; `margin-top: 5px`; `position: relative`; `width: max-content`; `filter: drop-shadow(0px 2px 4px rgba(0, 0, 0, 0.25))` |
| 585 | Корень | `.progress-text` | `display: flex`; `flex-direction: row`; `position: absolute`; `width: 100%`; `height: 20px`; `text-align: center`; `justify-content: center`; `bottom: 0`; `left: 0`; `font-weight: bold`; `color: white`; `font-size: 18px`; `margin: 0` |
| 601 | Корень | `.progress-input` | `justify-content: center`; `border: none` |
| 606 | Корень | `.progress-header` | `padding: 5px`; `border-radius: 3px 3px 0px 0px`; `font-size: 14px`; `color: white` |
| 613 | Корень | `.progress-header.hp` | `background: #550000` |
| 617 | Корень | `.progress-header.stamina` | `background: #073142` |
| 621 | Корень | `.progress-header.toxicity` | `background: #104208` |
| 625 | Корень | `.progress-header.focus` | `background: #220742` |
| 629 | Корень | `.progress-header.resolve` | `background: #592362` |
| 633 | Корень | `input.progress-input, .progress-total` | `background-color: rgba(0, 0, 0, 0)`; `line-height: 20px`; `width: 60px`; `height: 20px`; `border: none`; `font-weight: bold`; `color: white`; `font-size: 18px`; `text-align: center` |
| 646 | Корень | `.optional-stats-section` | `display: flex`; `flex-direction: column`; `gap: 10px`; `max-width: 130px`; `margin-top: 10px` |
| 653 | `.optional-stats-section` | `.optional-stat` | Только вложенность; собственных свойств нет |
| 654 | `.optional-stats-section` → `.optional-stat` | `.optional-name` | `display: flex`; `flex-direction: row`; `align-items: center`; `gap: 5px`; `background-color: light-dark(transparent, black)`; `border: 1px solid light-dark(black, transparent)`; `height: 25px`; `padding-left: 3px`; `border-radius: 5px 5px 0 0`; `font-weight: bold` |
| 667 | `.optional-stats-section` → `.optional-stat` | `.optional-info` | `display: flex`; `flex-direction: row`; `align-items: center`; `place-content: center`; `border-radius: 0 0 5px 5px`; `height: 35px`; `border: 1px solid black`; `text-align: center`; `gap: 5px` |
| 679 | `.optional-stats-section` → `.optional-stat` | `.optional-name, .optional-info` | Только вложенность; собственных свойств нет |
| 681 | `.optional-stats-section` → `.optional-stat` → `.optional-name, .optional-info` | `h4, h3` | `margin: 0` |
| 689 | Корень | `.optional-stats-section .switch` | `position: relative`; `display: inline-block`; `width: 42px`; `height: 22px` |
| 696 | Корень | `.optional-stats-section .switch input` | `opacity: 0`; `width: 0`; `height: 0` |
| 702 | Корень | `.optional-stats-section .switch .slider` | `position: absolute`; `cursor: pointer`; `inset: 0`; `background-color: #7a7a7a`; `transition: 0.2s ease`; `border-radius: 999px` |
| 711 | Корень | `.optional-stats-section .switch .slider:before` | `position: absolute`; `content: ''`; `height: 18px`; `width: 18px`; `left: 2px`; `top: 2px`; `background-color: #ffffff`; `transition: 0.2s ease`; `border-radius: 50%` |
| 723 | Корень | `.optional-stats-section .switch input:checked + .slider` | `background-color: #2d7d46` |
| 727 | Корень | `.optional-stats-section .switch input:checked + .slider:before` | `transform: translateX(20px)` |
| 731 | Корень | `.optional-buttons` | `place-content: center`; `align-content: center`; `width: 20px`; `height: 25px` |
| 738 | Корень | `.char-resource-modifier` | `border: 1px solid black`; `color: light-dark(black, white)`; `border-radius: 5px` |
| 743 | `.char-resource-modifier` | `.resource-modifiers` | `overflow-y: auto`; `height: 130px` |
| 747 | `.char-resource-modifier` → `.resource-modifiers` | `input.list-mod-edit.medium` | `width: 75px` |
| 753 | Корень | `.resource-title` | `background-color: black`; `color: white`; `padding: 5px` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

Большой файл не ограничен заголовком и почти весь глобален. Строки 1–201: flex-каркас, stat-grid, кнопки char-stat-button/char-derived-button, подписи, максимумы и цвет изменения; `.stat-mod-plus/zero/minus` поступают из HBS по сравнению value/max. На текущих навыках приоритет класса profession → pickup → learned задаёт skill-display.hbs, а не CSS. skill-icons могут одновременно перечислять несколько признаков. `.total-stats-label` — пустое правило; итоговые числа вычисляет JS.

Следующая группа оформляет char-header-center, имя, char-general и char-actions: кнопки, IP, счётчик смерти. Общие классы button-roll, init-roll, death-roll, crit-roll, heal-button, recover-sta, verbal-button и export-loot используются также у монстра и в других шаблонах. CSS задаёт цвета и hover, но не обработчики бросков и не их доступность.

`.char-image` позиционирует портрет 130×130 и wound-state. `.right-*`, `.char-right-sidebar`, core-stats-label, optional-stats-collum и родственные селекторы сохраняют прежний интерфейс; часть right-element/right-image/right-value ещё встречается в старом полном шаблоне монстра. У `.right-row` задано `size:75px`, однако буквальной .right-row в module/templates не найдено; работоспособность этой декларации не подтверждена. Имена с опечатками приведены буквально.

Пять семейств progress — HP, STA, toxicity, focus и resolve. Заданы размеры 130×20, фон дорожки, vendor-псевдоэлементы заполнения и радиусы. Далее общая рамка progress-container, абсолютный progress-text, подписи progress-header и поля progress-input/progress-total. HBS передаёт value/max, временные HP и условия вывода; расчёта ресурсов в CSS нет. Wound-state сравнивает HP с unmodifiedMax в HBS, тогда как progress.max использует текущий max — различать issue-00203 и фактическую шкалу.

Последний большой блок optional-stats-section оформляет vigor, shield, ignored-состояния, luck и опциональный adrenaline. `.switch` скрывает исходный input через opacity/размеры; `.slider:before` рисует бегунок, checked + slider меняет фон и перемещение на 20px. Это соседние input/span, а не самостоятельный переключатель JS. `.optional-buttons` задаёт размеры контролов. Финальный char-resource-modifier/resource-modifiers/resource-title определён, но буквальных потребителей в module/templates не найдено.

Есть смешанные списки `::-moz-progress-value, ::-moz-progress-bar` для радиуса; применение первого имени и всего списка в конкретном движке не проверено. Отдельные правила `::-moz-progress-bar` задают цвет. Эти оговорки не означают проверенную отрисовку Firefox.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 1 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/character-header.hbs](../../../../../templates/partials/character-header.hbs) | char-header-center, char-general/actions/button-list, button-roll, death-counter | Текущий заголовок персонажа; учитывать восстановление незакрытого anchor HTML-парсером. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/character/tab-stats.hbs](../../../../../templates/partials/character/tab-stats.hbs) | stat-grid, char-stat-button, char-derived-button, mod, max, stat-mod-* | Текущая общая вкладка характеристик Character/Monster. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/character/skill-display.hbs](../../../../../templates/partials/character/skill-display.hbs) | char-stat-button.skill, profession/pickup/learned, label, skill-icons | Текущие встроенные навыки. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/character/custom-skill-display.hbs](../../../../../templates/partials/character/custom-skill-display.hbs) | char-stat-button.skill, label, skill-icons | Текущие собственные навыки; контекст рассматривается отдельно в issue-00187. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | char-sidebar, char-image, progress-*, optional-stats-section, switch/slider | Текущая боковая панель персонажа. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | status-section, progress-*, optional-stats-section, switch/slider | Текущая боковая панель монстра; фото/wound-state дополнены monster/sidebar.css. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../templates/sheets/actor/partials/monster/header.hbs) | button-roll, init/death/crit/verbal/export-loot, death-counter | Текущие кнопки монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | export-loot | Отдельная кнопка экспорта в инвентаре монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../templates/sheets/actor/monster-sheet.hbs) | right-element, right-image, right-value, button-roll | Старый полный шаблон монстра; не PARTS зарегистрированного MonsterSheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) | header-stat, stat-max | Текущие числовые поля настройки базы характеристик. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | header-stat, stat-max, skill-modifiers | Текущая конфигурация навыков. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../module/actor/sheets/WitcherActorSheet.js) | DEFAULT_OPTIONS, _prepareContext, activateListeners | Подключает контекст настроек и общих действий; CSS не вызывает методы. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../module/actor/sheets/WitcherCharacterSheet.js) | PARTS, TABS, activateListeners | Регистрация текущего заголовка, панели, характеристик и навыков. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../module/actor/sheets/WitcherMonsterSheet.js) | PARTS, TABS | Потребление общих шаблонов/стилей у монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/mixins/statMixin.js](../../../../../module/actor/sheets/mixins/statMixin.js) | statListener | Связь stat-roll, luck и прочих контролов с поведением. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/mixins/skillMixin.js](../../../../../module/actor/sheets/mixins/skillMixin.js) | skillListener | Навыки и связанный UI; игровые вычисления вне CSS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | deathsaveMixin | Контролы спасброска и счётчика смерти. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster-sheet.css](../../../../../styles/monster-sheet.css) | .monster-right-attributes .right-* | Более поздние размеры прежней панели монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/sidebar.css](../../../../../styles/monster/sidebar.css) | .monster-sidebar .img-view, .wound-state | Фото монстра и индикатор состояния. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/monster/header.css](../../../../../styles/monster/header.css) | .monster-header .monster-actions | Специфичная раскладка заголовка монстра. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/character/sheet.css](../../../../../styles/character/sheet.css) | .window-content | Сетка, в которую попадает текущий header/sidebar. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../templates/partials/monster/monster-inventory-tab.hbs) | button-roll, export-loot | Старая кнопка экспорта; у нынешнего инвентаря отдельный HBS. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. Обращений var(...) в этом файле нет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/partials/character-header.hbs](../../../../../templates/partials/character-header.hbs) | char-header-center, char-general/actions/button-list, button-roll, death-counter | Текущий заголовок персонажа; учитывать восстановление незакрытого anchor HTML-парсером. |
| [templates/partials/character/tab-stats.hbs](../../../../../templates/partials/character/tab-stats.hbs) | stat-grid, char-stat-button, char-derived-button, mod, max, stat-mod-* | Текущая общая вкладка характеристик Character/Monster. |
| [templates/partials/character/skill-display.hbs](../../../../../templates/partials/character/skill-display.hbs) | char-stat-button.skill, profession/pickup/learned, label, skill-icons | Текущие встроенные навыки. |
| [templates/partials/character/custom-skill-display.hbs](../../../../../templates/partials/character/custom-skill-display.hbs) | char-stat-button.skill, label, skill-icons | Текущие собственные навыки; контекст рассматривается отдельно в issue-00187. |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | char-sidebar, char-image, progress-*, optional-stats-section, switch/slider | Текущая боковая панель персонажа. |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | status-section, progress-*, optional-stats-section, switch/slider | Текущая боковая панель монстра; фото/wound-state дополнены monster/sidebar.css. |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../templates/sheets/actor/partials/monster/header.hbs) | button-roll, init/death/crit/verbal/export-loot, death-counter | Текущие кнопки монстра. |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | export-loot | Отдельная кнопка экспорта в инвентаре монстра. |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../templates/sheets/actor/monster-sheet.hbs) | right-element, right-image, right-value, button-roll | Старый полный шаблон монстра; не PARTS зарегистрированного MonsterSheet. |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) | header-stat, stat-max | Текущие числовые поля настройки базы характеристик. |
| [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | header-stat, stat-max, skill-modifiers | Текущая конфигурация навыков. |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../templates/partials/monster/monster-inventory-tab.hbs) | button-roll, export-loot | Старая кнопка экспорта; у нынешнего инвентаря отдельный HBS. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 758 логических строк и PostCSS 8.5.12 | 128 rule-узлов, 352 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 7–10/14: три состояния знака модификатора, приоритет флагов навыка; оба sidebar по 4/5 шкал, input + slider, adrenaline только у персонажа; число кнопок header и восстановление reward anchor; связь с конфигурацией и старым CSS. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 1, раньше остальных стилей системы. Более поздний CSS может переопределять общие имена, а правила с корнем .application.sheet.witcher.monster имеют большую специфичность. У файла нет собственного root-scope, @media или imports; light-dark()/CSS-переменные и vendor-элементы исполняет браузер. Карта ниже охватывает 128 правил, включая пустые контейнеры вложенности, и 352 declarations. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00187](../../../../issues/potential/issue-00187.md), [issue-00198](../../../../issues/potential/issue-00198.md), [issue-00199](../../../../issues/potential/issue-00199.md), [issue-00202](../../../../issues/potential/issue-00202.md), [issue-00203](../../../../issues/potential/issue-00203.md), [issue-00205](../../../../issues/potential/issue-00205.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003049) |
