# styles/system-styles.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/system-styles.css](../../../../../styles/system-styles.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 3f78cbf0372e1da3d5a840e41b456d954c64e403 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.050](../../../../tasks/task-0003.050.md), 7 файлов / 582 логических строк; данный файл — 438 |
| Запись перекрёстной сверки | [TASK-0003.050](../../review-log.md#task-0003050) |

## Назначение файла

Общие CSS-утилиты, оформление окон, инвентаря, магии, сообщений бросков и предметных заголовков; часть прежних селекторов не имеет установленного текущего потребителя.

## Условия использования

Прямой импорт № 4 из witcher-styles.css; перед ним character-header/armor/attack, после — специализированные стили Actor/Item/чата. Большинство правил глобальны. Имя system-styles не ограничивает область корнем системы; .actor .window-header также совпадает с любым окном, имеющим такие классы.

## Введённые сущности и действия с ними

JavaScript-сущностей и полей модели нет. Ниже все 93 rule-узлов и 158 declarations внутри них; внешняя вложенность сохранена. Запятые в селекторе остаются на своём уровне, стрелка обозначает CSS nesting, а не новую HTML-обёртку.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.flex` | `display: flex` |
| 5 | Корень | `.gap` | `gap: 10px` |
| 9 | Корень | `.flex1` | `flex: 1` |
| 13 | Корень | `.chat-icon` | `width: 2em` |
| 17 | Корень | `.chat-icon-small` | `width: 1em` |
| 22 | Корень | `.witcher.sheet nav.sheet-tabs` | `height: fit-content`; `padding: 10px`; `text-align: center`; `background-color: light-dark(#22222210, #e7d1b110)`; `border: 1px solid light-dark(#22222210, #e7d1b110)`; `border-radius: 10px` |
| 31 | Корень | `.witcher.sheet nav.sheet-tabs` | Только вложенность; собственных свойств нет |
| 32 | `.witcher.sheet nav.sheet-tabs` | `a` | `color: light-dark(black, white)`; `text-shadow: none`; `padding: 0px 5px`; `transition: all 0.3s ease`; `border-radius: 5px` |
| 40 | `.witcher.sheet nav.sheet-tabs` | `a:hover` | `background-color: light-dark(#22222210, #e7d1b110)` |
| 44 | `.witcher.sheet nav.sheet-tabs` | `a.active` | `background-color: light-dark(#22222240, #e7d1b140)` |
| 50 | Корень | `.actor .window-header` | `flex: 0 0 30px`; `overflow: hidden`; `padding: 0 8px`; `line-height: 30px`; `border-bottom: 1px solid #000`; `background-color: #1c6888`; `border-radius: 5px 5px 0px 0px` |
| 60 | Корень | `.item-spell .window-header` | `background-color: #ab0d55` |
| 64 | Корень | `.item-diagrams .window-header` | `background-color: #80471b` |
| 68 | Корень | `.item-component .window-header` | `background-color: #80471b` |
| 72 | Корень | `.item-mutagen .window-header` | `background-color: #2a4e0a` |
| 76 | Корень | `.hp-content` | `margin-bottom: -20px` |
| 80 | Корень | `.armor-display` | `display: flex`; `width: 250px` |
| 85 | Корень | `.armor-display input` | `width: 35px` |
| 89 | Корень | `.armor-display label` | `width: 95px`; `display: flex`; `align-items: center`; `justify-content: center` |
| 96 | Корень | `.input-skill` | `width: 25px` |
| 100 | Корень | `.events` | `width: 45px` |
| 104 | Корень | `.weapon-section` | `flex: 1` |
| 108 | Корень | `.weapon-section .flex label` | `margin-right: 5px`; `margin-bottom: 5px` |
| 113 | Корень | `.item-info` | `padding: 5px`; `border-radius: 5px`; `background-color: rgba(25, 25, 25, 0.05)` |
| 119 | Корень | `.label-info` | `margin-left: 5px` |
| 123 | Корень | `.fa-info` | `margin: 5px`; `width: 10px` |
| 128 | Корень | `.item-delete` | `margin: 5px`; `width: 15px` |
| 133 | Корень | `.item-edit` | `margin: 5px` |
| 137 | Корень | `.fa-info` | `margin: 5px`; `width: 10px` |
| 142 | Корень | `.info-filler` | `width: 45px` |
| 146 | Корень | `.qty-filler` | `width: 20px` |
| 150 | Корень | `.weapon-name-header` | `width: 190px` |
| 154 | Корень | `.damage-header` | `width: 50px` |
| 158 | Корень | `.range-header` | `width: 50px` |
| 162 | Корень | `input.range-info` | `width: 70px` |
| 166 | Корень | `input.damage-info` | `width: 55px` |
| 170 | Корень | `input.reliable-info, input.item-quantity` | `background-color: transparent`; `padding: 0`; `max-width: 25px`; `text-align: center`; `transition: all 0.3 ease` |
| 179 | Корень | `input.reliable-info:hover, input.item-quantity:hover` | `background-color: rgba(0, 0, 0, 0.05)`; `transition: all 0.3 ease` |
| 185 | Корень | `.armor-section` | `flex: 1` |
| 189 | Корень | `.armor-section .flex label` | `margin-right: 5px`; `margin-bottom: 5px` |
| 194 | Корень | `.armor-name-header` | `width: 230px` |
| 198 | Корень | `.stopping-header` | `width: 30px` |
| 202 | Корень | `input.stopping-info` | `width: 50px` |
| 206 | Корень | `.invisible` | `display: none` |
| 210 | Корень | `.valuable-section` | `flex: 1`; `margin-right: 10px` |
| 215 | Корень | `.valuable-section .flex label` | `margin-right: 5px`; `margin-bottom: 5px` |
| 220 | Корень | `.valuable-table td` | `padding: 0.25em 0.25em` |
| 224 | Корень | `.component-section` | `flex: 1` |
| 228 | Корень | `.component-section .flex label` | `margin-right: 5px`; `margin-bottom: 5px` |
| 233 | Корень | `.alchemical-effect` | `width: 330px` |
| 237 | Корень | `.learned-data` | `width: 75px` |
| 241 | Корень | `input.weight-data` | `width: 30px` |
| 245 | Корень | `.components-display input` | `width: 25px` |
| 249 | Корень | `.magic-info` | `flex-direction: column`; `gap: 5px`; `background-color: light-dark(#22222210, #e7d1b110)`; `border: 1px solid light-dark(#22222240, #e7d1b140)`; `border-radius: 10px`; `padding: 10px`; `color: white`; `flex: 1` |
| 259 | `.magic-info` | `.focus-item` | `display: flex`; `gap: 5px` |
| 264 | `.magic-info` | `input.focus-value` | `width: 5ch`; `text-align: center` |
| 270 | Корень | `.tab.magic-info` | `display: none` |
| 274 | Корень | `.tab.magic-info.active` | `display: flex` |
| 278 | Корень | `.spell-section` | `min-width: 450px`; `margin-right: 10px`; `flex: 1` |
| 284 | Корень | `.spell-section .flex label` | `margin-right: 5px`; `margin-bottom: 5px` |
| 289 | Корень | `.magic-section .flex label` | `margin-right: 5px`; `margin-bottom: 5px` |
| 294 | Корень | `.magic-section` | `min-width: 400px`; `flex: 1` |
| 299 | Корень | `.magic-value-display` | `margin-right: 10px`; `margin-left: 20px` |
| 304 | Корень | `.dice-success` | `background-color: lightgreen`; `text-align: center` |
| 309 | Корень | `.dice-fail` | `background-color: lightpink`; `text-align: center` |
| 314 | Корень | `.dice-display` | `text-align: center` |
| 318 | Корень | `input.small` | `width: 5ch`; `text-align: center` |
| 323 | Корень | `input.small-medium` | `width: 50px` |
| 327 | Корень | `input.medium` | `width: 100px` |
| 331 | Корень | `input#customCost` | `width: 40px` |
| 335 | Корень | `input.spell-sta` | `width: 25px` |
| 339 | Корень | `input.spell-roll-value` | `width: 200px` |
| 343 | Корень | `.weightbar-overweight` | `background-color: red`; `width: 100%`; `height: 15px` |
| 349 | Корень | `.prof-name` | `flex: 1` |
| 353 | Корень | `.prof-item-delete` | `float: right` |
| 357 | Корень | `.stat-title` | `margin-left: 55px` |
| 361 | Корень | `input.skill-value` | `width: 25px` |
| 365 | Корень | `.perk` | `margin: 5px` |
| 369 | Корень | `.flex-header` | `align-items: center` |
| 373 | Корень | `.add-item` | `margin-right: 5px` |
| 377 | Корень | `.item-img` | `border: none`; `width: 40px`; `height: 40px`; `min-width: 40px`; `min-height: 40px` |
| 385 | Корень | `.description` | `margin: 10px` |
| 389 | Корень | `.error-display` | `color: red` |
| 393 | Корень | `.justify` | `justify-content: space-between` |
| 397 | Корень | `.margin-right` | `margin-right: 15px` |
| 401 | Корень | `.stat-display .stat-modifier-display` | `width: 15px` |
| 405 | Корень | `.value-max-stat-display` | `display: flex`; `gap: 10px`; `justify-content: left`; `align-items: center` |
| 412 | Корень | `.rotate-180` | `transform: rotate(180deg)`; `transition: all 0.3s ease` |
| 417 | Корень | `.sheet-header` | Только вложенность; собственных свойств нет |
| 418 | `.sheet-header` | `.profile-img` | `width: 100px`; `height: 100px` |
| 423 | `.sheet-header` | `.item-name` | `display: flex`; `gap: 15px`; `align-items: center`; `padding-bottom: 5px`; `margin: 0` |
| 430 | `.sheet-header` → `.item-name` | `input` | `height: auto` |
| 434 | `.sheet-header` → `.item-name` | `.configure-item` | `font-size: 16px` |

Не установлены буквальные DOM-потребители для hp-content, armor-display, input-skill, events, info-filler, qty-filler, weapon-name-header, damage-header, range-header, range-info, damage-info, armor-name-header, stopping-header, stopping-info, valuable-table, alchemical-effect, learned-data, weight-data, magic-value-display, dice-display, spell-roll-value, prof-name, prof-item-delete, stat-title, flex-header, justify, stat-modifier-display. Для input#customCost есть динамический HTML в [WitcherLootSheet._onItemBuy](../../../../../module/actor/sheets/WitcherLootSheet.js); поиск одного класса его не обнаруживает. Совпадения events/description/actor с полями модели не засчитывались как CSS-потребители. Для перечисленных остатков наличие HTML во внешних источниках не исключено.

## Основные функции и методы

JavaScript-функций нет; селекторы и каскад обрабатывает браузер.

Повтор .fa-info на строках 123/137 задаёт одинаковые margin/width; это избыточность, без доказанного различия поведения. Второй .witcher.sheet nav.sheet-tabs содержит вложенные a, a:hover и a.active; декларации первого блока продолжают действовать. Корни Actor создаёт WitcherActorSheet.DEFAULT_OPTIONS/classes; Foundry 14 объединяет массивы классов, поэтому Monster также имеет actor. Классы item-spell/item-diagrams/item-component/item-mutagen не найдены среди буквальных системных class-производителей; текущий WitcherItemSheet даёт item. Тип документа сам по себе не доказывает применение этих четырёх правил.

.invisible задаёт display:none. Item/ActiveEffect/heal mixins меняют классы, а не CSS. Более позднее display:flex у .list-item-info или display:grid соседнего CSS нужно сравнивать по полной специфичности: .invisible не объявлен !important. .rotate-180 применяется itemMixin к иконке раскрытия.

Текущая вкладка магии содержит .tab.magic-info; без .active скрыта, с .active имеет display:flex, колонки/фокус — вложенные правила .magic-info. Навигацию и active готовят ActorSheet и ядро, а не этот CSS. Его color:white действует при обоих вариантах light-dark; пригодность контраста в браузере не измерялась.

Утилиты размеров объединяют актуальные поля инвентаря с прежними таблицами. input.reliable-info и input.item-quantity присутствуют в текущем оружейном partial. Оба transition:all 0.3 ease имеют число без единицы времени (issue-00312); PostCSS сохраняет запись, но не подтверждает её допустимость. background-color и прочие отдельные declarations от этого не становятся невалидными.

Глобальные .sheet-header .profile-img и .sheet-header .item-name относятся, например, к текущим листам race/profession. Новый partial item-header имеет другую обёртку: присутствие .profile-img вне .sheet-header не является совпадением. .item-img используется в чатах/компонентах, тогда как нынешний инвентарь в основном использует .item-image/.item-list-image. .weightbar-overweight относится к Loot, отдельно от нового progress.carry-bar.overweight и issue-00311.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и назначение | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import № 4 | Единственное явное подключение. | Исходные определения/обращения, AST и проверки ниже |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../module/actor/sheets/WitcherActorSheet.js) | DEFAULT_OPTIONS, TABS/PARTS | Корень actor, текущие вкладки и active. | Исходные определения/обращения, AST и проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../module/actor/sheets/WitcherMonsterSheet.js) | DEFAULT_OPTIONS, PARTS | Дополняет корень monster и использует общие partial. | Исходные определения/обращения, AST и проверки ниже |
| [module/item/sheets/WitcherItemSheet.js](../../../../../module/item/sheets/WitcherItemSheet.js) | DEFAULT_OPTIONS.classes | Текущий корень item без item-spell и подобных имён. | Исходные определения/обращения, AST и проверки ниже |
| [templates/partials/character/tab-magic.hbs](../../../../../templates/partials/character/tab-magic.hbs) | nav.sheet-tabs, magic-info, focus-item, focus-value, value-max-stat-display | Текущая магия персонажа/монстра, скрытие вкладки focus. | Исходные определения/обращения, AST и проверки ниже |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | weapon-section, armor-section, valuable-section, component-section, small-medium | Текущие разделы инвентаря и валюта. | Исходные определения/обращения, AST и проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | reliable-info, item-quantity, item-info, invisible | Текущие поля и подробности оружия. | Исходные определения/обращения, AST и проверки ниже |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | item-quantity, item-info, invisible | Поля и подробности брони; те же utility-классы. | Исходные определения/обращения, AST и проверки ниже |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../module/actor/sheets/mixins/itemMixin.js) | _onItemDisplayInfo, _onDisplayList | Переключение invisible/rotate-180; состояние раскрытия. | Исходные определения/обращения, AST и проверки ниже |
| [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../module/actor/sheets/mixins/activeEffectMixin.js) | _onActiveEffectDisplayInfo | Переключает invisible у описания эффекта. | Исходные определения/обращения, AST и проверки ниже |
| [module/actor/sheets/mixins/healMixin.js](../../../../../module/actor/sheets/mixins/healMixin.js) | updateHealAmount | Назначает invisible подсказке стерилизации. | Исходные определения/обращения, AST и проверки ниже |
| [templates/dialog/heal/heal-rest.hbs](../../../../../templates/dialog/heal/heal-rest.hbs) | invisible | Начально скрытая подсказка. | Исходные определения/обращения, AST и проверки ниже |
| [module/scripts/rolls/extendedRoll.js](../../../../../module/scripts/rolls/extendedRoll.js) | dice-success, dice-fail | Создаёт цветные элементы результата/критов; reversal меняет назначение классов. | Исходные определения/обращения, AST и проверки ниже |
| [templates/chat/damage/damageToLocation.hbs](../../../../../templates/chat/damage/damageToLocation.hbs) | error-display | Числа шагов урона в сообщении. | Исходные определения/обращения, AST и проверки ниже |
| [templates/dialog/combat/weapon-attack.hbs](../../../../../templates/dialog/combat/weapon-attack.hbs) | error-display, small, item-img | Диалог атаки и сообщения об отсутствии боеприпасов. | Исходные определения/обращения, AST и проверки ниже |
| [templates/partials/components-list.hbs](../../../../../templates/partials/components-list.hbs) | item-img, error-display | Картинка компонента и недостающее количество. | Исходные определения/обращения, AST и проверки ниже |
| [module/app/htmlUtils.js](../../../../../module/app/htmlUtils.js) | flex, gap | Программно создаваемая разметка диалогов. | Исходные определения/обращения, AST и проверки ниже |
| [templates/chat/combat/spellItem.hbs](../../../../../templates/chat/combat/spellItem.hbs) | flex, gap, chat-icon, item-img | Разметка сообщения заклинания. | Исходные определения/обращения, AST и проверки ниже |
| [templates/chat/combat/statusEffect.hbs](../../../../../templates/chat/combat/statusEffect.hbs) | chat-icon-small | Иконка статуса в чате. | Исходные определения/обращения, AST и проверки ниже |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../templates/sheets/actor/loot-sheet.hbs) | weightbar-overweight, small-medium, add-item | Зарегистрированный лист добычи. | Исходные определения/обращения, AST и проверки ниже |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) | item-quantity, item-edit, item-delete, item-img | Строка добычи. | Исходные определения/обращения, AST и проверки ниже |
| [templates/sheets/item/race-sheet.hbs](../../../../../templates/sheets/item/race-sheet.hbs) | sheet-header, item-name, configure-item, perk | Текущий лист расы. | Исходные определения/обращения, AST и проверки ниже |
| [templates/sheets/item/profession-sheet.hbs](../../../../../templates/sheets/item/profession-sheet.hbs) | sheet-header, item-name, configure-item | Текущий лист профессии. | Исходные определения/обращения, AST и проверки ниже |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../templates/partials/monster/monster-inventory-tab.hbs) | flex1, label-info, fa-info, item-edit/delete | Прежняя разметка, не текущий PARTS. | Исходные определения/обращения, AST и проверки ниже |
| [templates/partials/monster/monster-spell-tab.hbs](../../../../../templates/partials/monster/monster-spell-tab.hbs) | magic-info, spell-sta, item-img | Прежняя магия, отдельно от общей вкладки. | Исходные определения/обращения, AST и проверки ниже |
| [styles/tab-inventory-list.css](../../../../../styles/tab-inventory-list.css) | list-item-info, поля списков | Позднейший каскад нынешнего инвентаря. | Исходные определения/обращения, AST и проверки ниже |
| [styles/monster-sheet.css](../../../../../styles/monster-sheet.css) | window-header, labels, profile | Прежние глобальные правила остаются подключены. | Исходные определения/обращения, AST и проверки ниже |
| [styles/item-header.css](../../../../../styles/item-header.css) | новые заголовки Item | Позднейший CSS с другой структурой селекторов. | Исходные определения/обращения, AST и проверки ниже |

Внешняя среда: браузер CSS/DOM; Foundry 14.367.0 — client/applications/api/application.mjs (_prepareTabs и объединение классов), public/css/foundry2.css (общие стили и скрытие неактивных tab[data-tab]). Это внешние API, а не функции CSS системы. Ключей локализации и CSS var(...) в собственных правилах этого файла нет.

## Известные потребители

| Потребитель | Используемая сущность и условия |
| --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import № 4: Единственное явное подключение. |
| [templates/partials/character/tab-magic.hbs](../../../../../templates/partials/character/tab-magic.hbs) | nav.sheet-tabs, magic-info, focus-item, focus-value, value-max-stat-display: Текущая магия персонажа/монстра, скрытие вкладки focus. |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | weapon-section, armor-section, valuable-section, component-section, small-medium: Текущие разделы инвентаря и валюта. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) | reliable-info, item-quantity, item-info, invisible: Текущие поля и подробности оружия. |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | item-quantity, item-info, invisible: Поля и подробности брони; те же utility-классы. |
| [templates/dialog/heal/heal-rest.hbs](../../../../../templates/dialog/heal/heal-rest.hbs) | invisible: Начально скрытая подсказка. |
| [module/scripts/rolls/extendedRoll.js](../../../../../module/scripts/rolls/extendedRoll.js) | dice-success, dice-fail: Создаёт цветные элементы результата/критов; reversal меняет назначение классов. |
| [templates/chat/damage/damageToLocation.hbs](../../../../../templates/chat/damage/damageToLocation.hbs) | error-display: Числа шагов урона в сообщении. |
| [templates/dialog/combat/weapon-attack.hbs](../../../../../templates/dialog/combat/weapon-attack.hbs) | error-display, small, item-img: Диалог атаки и сообщения об отсутствии боеприпасов. |
| [templates/partials/components-list.hbs](../../../../../templates/partials/components-list.hbs) | item-img, error-display: Картинка компонента и недостающее количество. |
| [templates/chat/combat/spellItem.hbs](../../../../../templates/chat/combat/spellItem.hbs) | flex, gap, chat-icon, item-img: Разметка сообщения заклинания. |
| [templates/chat/combat/statusEffect.hbs](../../../../../templates/chat/combat/statusEffect.hbs) | chat-icon-small: Иконка статуса в чате. |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../templates/sheets/actor/loot-sheet.hbs) | weightbar-overweight, small-medium, add-item: Зарегистрированный лист добычи. |
| [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) | item-quantity, item-edit, item-delete, item-img: Строка добычи. |
| [templates/sheets/item/race-sheet.hbs](../../../../../templates/sheets/item/race-sheet.hbs) | sheet-header, item-name, configure-item, perk: Текущий лист расы. |
| [templates/sheets/item/profession-sheet.hbs](../../../../../templates/sheets/item/profession-sheet.hbs) | sheet-header, item-name, configure-item: Текущий лист профессии. |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../templates/partials/monster/monster-inventory-tab.hbs) | flex1, label-info, fa-info, item-edit/delete: Прежняя разметка, не текущий PARTS. |
| [templates/partials/monster/monster-spell-tab.hbs](../../../../../templates/partials/monster/monster-spell-tab.hbs) | magic-info, spell-sta, item-img: Прежняя магия, отдельно от общей вкладки. |

Область поиска — module/, templates/, styles/ и манифест. Прежний шаблон не объявляется текущим на основании одного CSS-класса; выбор действующих PARTS сверялся с листами. CSS не импортирует классы JavaScript. Сторонние темы, пользовательский HTML и макросы не исследованы.

## Данные и изменения состояния

Файл меняет представление элементов при совпадении селекторов. Не создаёт и не обновляет Actor/Item/эффекты, не вычисляет характеристики и не сохраняет состояние флажков. CSS-класс, отключённый input и скрытый элемент не являются проверкой прав на сервере.

## Проверки и доказательства

Полное чтение 438 логических строк; PostCSS 8.5.12. C03–C05: настоящий HBS отдыха содержит скрытую подсказку; текущая focus-вкладка даёт active/неактивный класс и шесть focus-value; оружейный partial содержит reliable-info, item-quantity и скрытые детали. Сверены все 93 rule-узла/158 declarations. Повторные .047–.049 сопоставили методы переключения классов, корневые классы и старые/новые шаблоны.

[Методика, результаты и сверка серии](../../review-log.md#task-0003050). Настоящие HBS/helpers и отдельный callback ready исполнены в Node 24.16.0; Handlebars 4.7.9, parse5 из Foundry. Контексты и документные/DOM-операции заданы фасадами; исходники и БД не менялись. AST проверяет структуру и полноту документации, не итоговую отрисовку.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Браузер, HTTP-загрузка шрифта, computedStyle, размеры/переполнение, реальное переключение вкладок, hover и поддержка nesting/light-dark в конкретном клиенте не проверялись. Локальное существование ресурса не доказывает доступ службы Foundry.

## Связанные проблемы

[issue-00312](../../../../issues/potential/issue-00312.md). Сохраняют статус potential; регистрация не означает подтверждения или исправления.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 3f78cbf0372e1da3d5a840e41b456d954c64e403; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003050) |
