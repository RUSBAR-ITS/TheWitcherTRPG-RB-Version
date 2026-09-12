# styles/profession-sheet.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/profession-sheet.css](../../../../../styles/profession-sheet.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.047](../../../../tasks/task-0003.047.md), 10 файлов / 661 логических строк; данный файл — 240 |
| Запись перекрёстной сверки | [TASK-0003.047](../../review-log.md#task-0003047) |

## Назначение файла

Задаёт общие карточки и цветовые ветки профессии, поля навыков, заметки и анимацию кнопки броска в Item и Actor.

## Условия использования

Прямой @import в [styles/witcher-styles.css](../../../../../styles/witcher-styles.css):12. Правила глобальные и охватывают несколько редакторов: принадлежность файла к sheet не ограничивает его Item. Actor получает дополнительные правила из более позднего [styles/character/tab-profession.css](../../../../../styles/character/tab-profession.css).

## Введённые сущности и действия с ними

Определяющий навык и заметки серые; skillPath1/2/3 — голубая, зелёная и красная группы. Есть самостоятельные select/header/body правила каждого пути. Общий profession-flex — строка, monster-profession-flex — колонка; profession-path здесь колонка с gap10px. Базовая карточка min250/max400px; у monster-profession-flex и profession-path max-width снимается более специфичными правилами. Вложенные редакторы прокручиваются; height150px переопределяется -webkit-fill-available внутри пути. skill-path-name имеет margin/width!important. Никаких listeners/бросков/выбора навыка CSS не реализует.

Ниже перечислены все 44 rule-узла и 106 declarations. Внешняя вложенность читается слева направо; списки селекторов на каждом уровне сохраняются. Дочерний селектор без & означает потомка, а не новый глобальный селектор. Объявлен @keyframes vibrate:11; его шаги включены в таблицу.

| Строка | Внешняя вложенность | Селектор / шаг | Свойства |
| --- | --- | --- | --- |
| 1 | Корень | `.profession-roll` | `font-size: 20px`; `color: black`; `display: flex` |
| 7 | Корень | `.profession-card i` | `margin: 0px 0px 0px 5px` |
| 12 | `@keyframes vibrate` | `0%` | `transform: translateX(0)` |
| 15 | `@keyframes vibrate` | `25%` | `transform: translateX(-2px)` |
| 18 | `@keyframes vibrate` | `50%` | `transform: translateX(2px)` |
| 21 | `@keyframes vibrate` | `75%` | `transform: translateX(-2px)` |
| 24 | `@keyframes vibrate` | `100%` | `transform: translateX(0)` |
| 29 | Корень | `.profession-roll:hover i` | `animation: vibrate 0.2s linear infinite` |
| 33 | Корень | `.profession-roll i` | `display: inline-block` |
| 37 | Корень | `.profession-layout` | `flex-direction: column`; `display: flex`; `align-items: center` |
| 43 | Корень | `.profession-notes` | `width: 100%`; `min-width: 250px`; `max-width: 810px`; `margin: 5px`; `margin-top: 5px`; `border-radius: 5px` |
| 52 | Корень | `.profession-notes-header` | `background-color: #818181`; `padding: 8px 10px`; `font-weight: bold`; `font-size: 16px`; `border-radius: 5px 5px 0 0` |
| 60 | Корень | `.profession-notes .editor` | `height: 150px`; `border-radius: 0 0 5px 5px`; `padding: 0px 0px 0px 5px` |
| 66 | Корень | `input.profession-level` | `width: 35px`; `padding: 5px`; `border-radius: 0 5px 0 0`; `background-color: rgba(255, 255, 255, 60%)` |
| 73 | Корень | `input.profession-skill-input` | `border-radius: 5px 0 0 0`; `background-color: rgba(255, 255, 255, 60%)` |
| 78 | Корень | `.defining-skill-select` | `background-color: rgb(255 255 255 / 60%)`; `border-radius: 0`; `margin: 0 5px 0 5px`; `height: 26px` |
| 85 | Корень | `.defining-skill-header` | `background-color: #818181`; `color: white`; `align-items: center`; `border-radius: 5px 5px 0 0`; `padding: 5px` |
| 93 | Корень | `.defining-skill` | `background-color: #c3c3c3` |
| 97 | Корень | `.first-path-select` | `background-color: rgb(255 255 255 / 60%)`; `border-radius: 0`; `margin: 0 5px 0 5px`; `height: 26px` |
| 104 | Корень | `.first-path-header` | `background-color: #859ecd`; `color: white`; `align-items: center`; `border-radius: 5px 5px 0 0`; `padding: 5px` |
| 112 | Корень | `.first-path` | `background-color: #c4d3ef` |
| 116 | Корень | `.second-path-select` | `background-color: rgb(255 255 255 / 60%)`; `border-radius: 0`; `margin: 0 5px 0 5px`; `height: 26px` |
| 123 | Корень | `.second-path-header` | `background-color: #9ccd85`; `color: white`; `align-items: center`; `border-radius: 5px 5px 0 0`; `padding: 5px` |
| 131 | Корень | `.second-path` | `background-color: #cdebbf` |
| 135 | Корень | `.third-path-select` | `background-color: rgb(255 255 255 / 60%)`; `border-radius: 0`; `margin: 0 5px 0 5px`; `height: 26px` |
| 142 | Корень | `.third-path-header` | `background-color: #cd8585`; `color: white`; `align-items: center`; `border-radius: 5px 5px 0 0`; `padding: 5px` |
| 150 | Корень | `.third-path` | `background-color: #edc9c9` |
| 154 | Корень | `.profession-flex` | `display: flex`; `flex-direction: row`; `justify-content: flex-start` |
| 160 | Корень | `.monster-profession-flex` | `display: flex`; `flex-direction: column`; `justify-content: flex-start`; `width: 100%` |
| 166 | `.monster-profession-flex` | `.profession-card` | `width: 100%`; `max-width: none` |
| 172 | Корень | `.profession-card .editor` | `height: 150px`; `border-radius: 0 0 5px 5px`; `padding: 0px 0px 0px 5px` |
| 178 | Корень | `.profession-card` | `min-width: 250px`; `max-width: 400px`; `margin: 5px`; `border-radius: 5px` |
| 185 | Корень | `.skill-path-name` | `margin: 5px !important`; `width: 97.5% !important` |
| 190 | Корень | `.profession-flex` | `margin-bottom: 20px` |
| 193 | `.profession-flex` | `.profession-card, .profession-notes` | Только вложенные правила |
| 195 | `.profession-flex` → `.profession-card, .profession-notes` | `.editor` | `overflow-y: auto` |
| 200 | `.profession-flex` | `.profession-card` | Только вложенные правила |
| 201 | `.profession-flex` → `.profession-card` | `input, select, .editor` | `color: #222` |
| 209 | Корень | `.profession-path` | `display: flex`; `flex-direction: column`; `gap: 10px`; `width: 100%` |
| 215 | `.profession-path` | `.blue-path, .green-path, .red-path` | `width: 100%` |
| 220 | `.profession-path` → `.blue-path, .green-path, .red-path` | `h2` | `font-size: 24px`; `margin-bottom: 5px` |
| 226 | `.profession-path` | `.profession-card` | `max-width: none` |
| 229 | `.profession-path` → `.profession-card` | `input, select, .editor` | `color: #222` |
| 235 | `.profession-path` → `.profession-card` | `.editor` | `overflow-y: auto`; `height: -webkit-fill-available` |

## Основные функции и методы

JavaScript-функций и обработчиков нет. Файл объявляет CSS-правила, применяемые браузером к совпавшей разметке; вычисления свойств и псевдосостояний выполняет внешний CSS engine. 

## Используемые сущности и зависимости

| Сущность | Файл-источник | Вид / цель связи |
| --- | --- | --- |
| Профессия Item | [templates/sheets/item/profession-sheet.hbs](../../../../../templates/sheets/item/profession-sheet.hbs) | 10 карточек, три skill-path-name, formInput; нет profession-roll |
| Профессия Character | [templates/partials/character/tab-profession.hbs](../../../../../templates/partials/character/tab-profession.hbs) | 10 карточек, три цветных пути, кнопки бросков и legacy editor helper |
| Профессия Monster | [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) | Один definingSkill, заметки, monster-profession-flex; трёх путей нет |
| Карточка настройки навыка | [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | Использует общий profession-card; это дополнительный consumer |
| Listener профессии | [module/actor/sheets/mixins/skillMixin.js](../../../../../module/actor/sheets/mixins/skillMixin.js) | Назначает click .profession-roll; собственно анимация не бросает кубик |
| Действие Actor | [module/actor/mixins/professionMixin.js](../../../../../module/actor/mixins/professionMixin.js) | Читает .profession-display.dataset в _onProfessionRoll |
| Актуальный Item producer | [module/item/sheets/WitcherProfessionSheet.js](../../../../../module/item/sheets/WitcherProfessionSheet.js) | PARTS и подготовка professionSkills/statOptions |
| Уточнения Actor | [styles/character/tab-profession.css](../../../../../styles/character/tab-profession.css) | Поздние и более специфичные правила активной вкладки |
| Общие элементы | [styles/system-styles.css](../../../../../styles/system-styles.css) | flex, заголовки; импорт 4 раньше |
| Другой editor selector | [styles/item-sheets.css](../../../../../styles/item-sheets.css) | Позже: .description .editor height75px; текущая profession-card не помещена в .description |

Входной ресурс [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) зарегистрирован в [system.json](../../../../../system.json); эти соседи проверены в пределах подключения, их полные карточки здесь не создаются. Найденный локальный файл и строка @import не доказывают доступ по HTTP для службы Foundry.

## Известные потребители

HBS и JS перечислены выше. Вкладки Actor используют старый helper editor внутри текущих V2 PARTS; это не означает, что сами листы legacy. Item использует formInput → prose-mirror; ядро добавляет .editor динамически (группа 15). В конфигурации skillPathSkillPart используется только часть общих классов; не все 44 rule-узла применимы к каждому окну.

Область поиска: все templates/module/styles текущего среза, имена полей/классов в динамических producer и указанные методы ядра. Имена файлов и упоминания в комментариях отделены от создания HTML. Содержимое миров, внешние расширения и пользовательский enriched HTML не обследованы.

## Данные и изменения состояния

Повторный .profession-flex добавляет margin-bottom20px и вложенные цвета/overflow. .monster-profession-flex .profession-card побеждает более позднюю простую .profession-card по специфичности, сохраняя max-width:none. .profession-path .profession-card .editor побеждает height150px. Для активного Actor [styles/character/tab-profession.css](../../../../../styles/character/tab-profession.css) задаёт profession-path row/gap0 и min-width190px в карточках пути; Item без родительского actor/monster остаётся на общем column/gap10. Цвета #222 назначены вложенным полям/редактору, белый — header. Полный каскад тем/модулей не вычислялся.

CSS не создаёт документы, не меняет значения полей и не запускает сохранение/игровые действия. Размещение, hover и видимость отделены от JS управления. Файл прочитан целиком: 240 логических строк; переводы строк LF, есть завершающий newline.

## Проверки и доказательства

Группы 06–08/13/15:44 rule-узла,106 declarations и один @keyframes vibrate. Его пять шагов:0→−2→+2→−2→0px по X; hover запускает 0.2s linear infinite на i. Рендер HBS: Character10 карточек/10 кнопок, Monster1 карточка, Item10 карточек/0 кнопок/3 поля пути. Профессия/форма — данные-фасады; переход hover, прокрутка и визуальная анимация не исполнялись.

Методика — [журнал TASK-0003.047](../../review-log.md#task-0003047). Использованы PostCSS8.5.12, Handlebars4.7.9 и parse5 из существующих зависимостей Foundry14.367.0. Разбор CSS AST подтверждает структуру, не принятие каждого значения браузером или итоговое computed style.

## Непроверенные участки и открытые вопросы

Полностью прочитаны все правила; непрочитанных частей файла нет. Не запускались мир, браузер, HTTP-загрузка, вычисление раскладки, смена темы, масштабирование и внешние модули. Размеры/цвета из declarations не объявлены измеренными пикселями интерфейса. Изменение оформления и удаление правил не согласовывались.

## Связанные проблемы

Новых проблем не зарегистрировано. Прежние проблемы действий/данных профессии этим CSS не подтверждаются и не исправляются.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003047) |
