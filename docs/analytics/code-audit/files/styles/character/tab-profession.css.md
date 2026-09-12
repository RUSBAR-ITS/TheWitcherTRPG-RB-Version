# styles/character/tab-profession.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/character/tab-profession.css](../../../../../../styles/character/tab-profession.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.047](../../../../../tasks/task-0003.047.md), 10 файлов / 661 логических строк; данный файл — 105 |
| Запись перекрёстной сверки | [TASK-0003.047](../../../review-log.md#task-0003047) |

## Назначение файла

Уточняет оформление активной вкладки профессии Character и Monster: заголовки, расположение путей, поля навыков и расовые особенности.

## Условия использования

Прямой @import в [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css):30. Внешние варианты — .application.sheet.witcher.actor и .application.sheet.witcher.monster, затем .tab.profession.active. Несмотря на каталог character, правило явно включает Monster.

## Введённые сущности и действия с ними

Заголовки профессии/расы получают flex и h1/h2. В definingSkill/notes добавляются margin и overflow, в путях — горизонтальный flex без gap. Карточки пути min190/max:none, внутренние поля #222, editor с min-height50 и -webkit-fill-available. .profession-display переносит поля, select.inline-edit ограничен calc(100% - 80px), level max35, скругления 5px. Расовый h3 задаётся только внутри .item .perk. Внешние rule-узлы без declarations сохраняют scope; они не являются самостоятельными визуальными свойствами.

Ниже перечислены все 22 rule-узла и 35 declarations. Внешняя вложенность читается слева направо; списки селекторов на каждом уровне сохраняются. Дочерний селектор без & означает потомка, а не новый глобальный селектор. Директив @import/@keyframes внутри файла нет.

| Строка | Внешняя вложенность | Селектор / шаг | Свойства |
| --- | --- | --- | --- |
| 1 | Корень | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` | Только вложенные правила |
| 3 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` | `.tab.profession.active` | Только вложенные правила |
| 4 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` | `.profession-header, .race-header` | `display: flex`; `width: 100%` |
| 9 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-header, .race-header` | `h1` | `margin: 0`; `margin-right: auto`; `font-size: 36px` |
| 15 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-header, .race-header` | `h2` | `font-size: 24px`; `margin: 0` |
| 21 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` | `.profession-flex, .monster-profession-flex` | `margin-bottom: 20px` |
| 25 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-flex, .monster-profession-flex` | `.profession-card, .profession-notes` | Только вложенные правила |
| 27 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-flex, .monster-profession-flex` → `.profession-card, .profession-notes` | `.editor` | `overflow-y: auto` |
| 32 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-flex, .monster-profession-flex` | `.profession-card` | Только вложенные правила |
| 33 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-flex, .monster-profession-flex` → `.profession-card` | `input, select, .editor` | `color: #222` |
| 41 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` | `.profession-path` | `display: flex`; `flex-direction: row`; `gap: 0px`; `width: 100%` |
| 47 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-path` | `.blue-path, .green-path, .red-path` | `width: 100%` |
| 52 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-path` → `.blue-path, .green-path, .red-path` | `h2` | `font-size: 24px`; `margin-bottom: 5px` |
| 58 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-path` | `.profession-card` | `max-width: none`; `min-width: 190px` |
| 62 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-path` → `.profession-card` | `input, select, .editor` | `color: #222` |
| 68 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-path` → `.profession-card` | `.editor` | `overflow-y: auto`; `min-height: 50px`; `height: -webkit-fill-available` |
| 74 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-path` → `.profession-card` | `.profession-display` | `display: flex`; `flex-wrap: wrap`; `gap: 5px` |
| 79 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-path` → `.profession-card` → `.profession-display` | `.profession-skill-input` | `border-radius: 5px` |
| 83 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-path` → `.profession-card` → `.profession-display` | `select.inline-edit` | `max-width: calc(100% - 80px)`; `height: 32px`; `border-radius: 5px`; `margin: 0` |
| 90 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.profession-path` → `.profession-card` → `.profession-display` | `.profession-level` | `max-width: 35px`; `border-radius: 5px` |
| 98 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` | `.item .perk` | Только вложенные правила |
| 99 | `.application.sheet.witcher.actor, .application.sheet.witcher.monster` → `.tab.profession.active` → `.item .perk` | `h3` | `font-size: 20px`; `margin-bottom: 5px` |

## Основные функции и методы

JavaScript-функций и обработчиков нет. Файл объявляет CSS-правила, применяемые браузером к совпавшей разметке; вычисления свойств и псевдосостояний выполняет внешний CSS engine. calc(100% - 80px) задаёт ограничение ширины select, не игровое вычисление.

## Используемые сущности и зависимости

| Сущность | Файл-источник | Вид / цель связи |
| --- | --- | --- |
| PARTS/TABS/cssClass | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Путь HBS и cssClass profession; _prepareTabs вызывается при контексте |
| PARTS/TABS/cssClass | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Тот же cssClass, отдельный Monster HBS |
| DEFAULT_OPTIONS.classes | [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js) | Классы witcher/sheet/actor; application добавляет ядро |
| Разметка Character | [templates/partials/character/tab-profession.hbs](../../../../../../templates/partials/character/tab-profession.hbs) | section.tab с динамическим cssClass; три пути, race-header и perk |
| Разметка Monster | [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) | section.tab с тем же cssClass; только definingSkill и notes |
| Общая карточка | [styles/profession-sheet.css](../../../../../../styles/profession-sheet.css) | Ранние общие размеры, цвета, редакторы, column/gap10 |
| Расовое содержимое | [styles/race-sheet.css](../../../../../../styles/race-sheet.css) | Высота editor-content, не h3 |
| Общая сетка Actor | [styles/character/sheet.css](../../../../../../styles/character/sheet.css) | Внешний window-content/grid; не задаёт направление profession-path |

Входной ресурс [styles/witcher-styles.css](../../../../../../styles/witcher-styles.css) зарегистрирован в [system.json](../../../../../../system.json); эти соседи проверены в пределах подключения, их полные карточки здесь не создаются. Найденный локальный файл и строка @import не доказывают доступ по HTTP для службы Foundry.

## Известные потребители

Классы profession/active появляются из Foundry ApplicationV2._prepareTabs (client/applications/api/application.mjs:704–717): к заданному cssClass добавляется active для выбранной вкладки. Группа 12 исполнила настоящий метод;13 — HBS с его результатом. Неактивная вкладка не соответствует селектору. Item-профессия имеет похожие классы карточек, но без требуемого внешнего Actor/Monster этот файл её не адресует. Monster-template сейчас не содержит profession-path/race-header, поэтому эти ветви для него не имеют найденного элемента.

Область поиска: все templates/module/styles текущего среза, имена полей/классов в динамических producer и указанные методы ядра. Имена файлов и упоминания в комментариях отделены от создания HTML. Содержимое миров, внешние расширения и пользовательский enriched HTML не обследованы.

## Данные и изменения состояния

Поздний и более специфичный scope заменяет общий profession-path column/gap10 на row/gap0 только у активного Actor. У карточек пути min-width250px становится 190px; definingSkill снаружи profession-path сохраняет общий min250. У редактора внутри пути добавляется min-height50px, height остаётся -webkit-fill-available. У select.inline-edit margin0/height32/radius5 перекрывают общий path-select margin/height26/radius0. Глобальное .perk .editor-content height150px из race-sheet относится к другому элементу. Каскад ядра/модулей и физическая ширина не измерены.

CSS не создаёт документы, не меняет значения полей и не запускает сохранение/игровые действия. Размещение, hover и видимость отделены от JS управления. Файл прочитан целиком: 105 логических строк; переводы строк LF, нет завершающего newline.

## Проверки и доказательства

Группы 06–08/12–14:22 rule-узла и 35 declarations. Реальный _prepareTabs даёт profession active/ profession; HBS Character содержит три цветных пути и 10 карточек, Monster одну карточку без profession-path, Item10 карточек без Actor scope. Порядок imports проверен. Сопоставление selector/scope статическое; browser querySelectorAll/computedStyle не запускались.

Методика — [журнал TASK-0003.047](../../../review-log.md#task-0003047). Использованы PostCSS8.5.12, Handlebars4.7.9 и parse5 из существующих зависимостей Foundry14.367.0. Разбор CSS AST подтверждает структуру, не принятие каждого значения браузером или итоговое computed style.

## Непроверенные участки и открытые вопросы

Полностью прочитаны все правила; непрочитанных частей файла нет. Не запускались мир, браузер, HTTP-загрузка, вычисление раскладки, смена темы, масштабирование и внешние модули. Размеры/цвета из declarations не объявлены измеренными пикселями интерфейса. Изменение оформления и удаление правил не согласовывались.

## Связанные проблемы

Новых проблем не зарегистрировано. Динамический cssClass проверен до вывода о применимости селектора; отсутствующая строка profession в буквальном class HBS не признана ошибкой.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; полный файл | Первичная карточка; [перекрёстная сверка](../../../review-log.md#task-0003047) |
