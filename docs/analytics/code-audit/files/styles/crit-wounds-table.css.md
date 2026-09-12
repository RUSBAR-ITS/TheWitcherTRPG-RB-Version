# styles/crit-wounds-table.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/crit-wounds-table.css](../../../../../styles/crit-wounds-table.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.047](../../../../tasks/task-0003.047.md), 10 файлов / 661 логических строк; данный файл — 134 |
| Запись перекрёстной сверки | [TASK-0003.047](../../review-log.md#task-0003047) |

## Назначение файла

Оформляет заголовки и поля критических травм в списке Actor и редакторе Item; также содержит правила прежней табличной разметки без найденных текущих элементов.

## Условия использования

Прямой @import в [styles/witcher-styles.css](../../../../../styles/witcher-styles.css):14. Селекторы глобальные. Текущий [templates/partials/crit-wounds-table.hbs](../../../../../templates/partials/crit-wounds-table.hbs) — ol/li, поэтому совпадение имени partial с .crit-wounds-table не доказывает наличие одноимённого HTML-класса.

## Введённые сущности и действия с ними

Действующие группы: контейнер crit-wounds и заголовок, сетка critwound-header (2fr 1fr100px), flex critwound-info/select, колонка дней, поля формы и их hover-тень, add-crit, подпись healing-time-lable и две ширины 40px!important. В текущей сетке header найдено два непосредственных дочерних блока, хотя объявлено три колонки; геометрический дефект без браузера не утверждается. Блоки для tbody/tr/textarea прежней таблицы, .critwound-display и её width33.33px сохраняются в CSS, но найденный HBS их не создаёт.

Ниже перечислены все 26 rule-узла и 52 declarations. Внешняя вложенность читается слева направо; списки селекторов на каждом уровне сохраняются. Дочерний селектор без & означает потомка, а не новый глобальный селектор. Директив @import/@keyframes внутри файла нет.

| Строка | Внешняя вложенность | Селектор / шаг | Свойства |
| --- | --- | --- | --- |
| 1 | Корень | `.crit-wounds` | `flex-grow: 1` |
| 5 | Корень | `.critwound-data` | `display: flex`; `flex-direction: column` |
| 10 | Корень | `.crit-wounds-header` | `display: flex`; `justify-content: space-between`; `padding: 5px`; `border-radius: 5px`; `background-color: rgba(0, 0, 0, 0.05)`; `border: 1px solid darkgray`; `margin-top: 10px` |
| 20 | Корень | `.crit-wounds-header-name` | `margin-bottom: 0`; `border-bottom: none`; `opacity: 0.8` |
| 26 | Корень | `.critwound-header` | `display: grid`; `grid-template-columns: 2fr 1fr 100px`; `align-items: center`; `padding: 10px 5px 0px` |
| 33 | Корень | `.critwound-info` | `display: flex`; `gap: 5px`; `flex-wrap: wrap` |
| 38 | `.critwound-info` | `select` | `width: max-content` |
| 42 | `.critwound-info` | `.wound-name` | `width: -webkit-fill-available` |
| 47 | Корень | `.critwound-days-rest` | `display: flex`; `flex-direction: column`; `gap: 5px`; `align-items: start`; `margin: 0 auto` |
| 55 | Корень | `.critwound-display` | `display: grid`; `grid-template-columns: 2fr 1fr` |
| 60 | Корень | `.critwound-display, .delete-crit` | `width: 33.33px` |
| 65 | Корень | `.critwound-controls` | `display: flex`; `justify-content: end` |
| 70 | Корень | `.crit-wounds-table` | `border: none`; `margin: 0` |
| 75 | Корень | `.crit-wounds-table > tbody > tr` | `background-color: rgba(0, 0, 0, 0)`; `border-bottom: 1px rgba(25, 24, 19, 0.2) solid` |
| 80 | Корень | `.crit-wounds-table > tbody` | `background-color: rgba(0, 0, 0, 0)` |
| 83 | Корень | `.crit-wounds-table > tbody > tr:last-child` | `background-color: rgba(0, 0, 0, 0)`; `border-bottom: 0px` |
| 88 | Корень | `.crit-wounds-table` | `background-color: rgba(0, 0, 0, 0)` |
| 92 | Корень | `.critwound input, .critwound select, .critwound textarea` | `border: none`; `transition: box-shadow 0.1s ease` |
| 99 | Корень | `.critwound input:hover, .critwound select:hover, .critwound textarea:hover` | `box-shadow: 0 0 5px var(--color-shadow-primary)` |
| 105 | Корень | `.critwounds-description:not(.invisible)` | `padding: 10px 5px 1rem 5px` |
| 109 | Корень | `.crit-wound-description, .crit-wound-mod-description` | `padding-bottom: 0.5rem` |
| 114 | Корень | `.crit-wounds-table textarea` | `resize: vertical` |
| 118 | Корень | `.add-crit` | `margin: 5px`; `width: 15px` |
| 123 | Корень | `.healing-time-lable` | `height: 32px`; `align-content: center` |
| 128 | Корень | `.days-healed` | `width: 40px !important` |
| 132 | Корень | `.healing-time` | `width: 40px !important` |

## Основные функции и методы

JavaScript-функций и обработчиков нет. Файл объявляет CSS-правила, применяемые браузером к совпавшей разметке; вычисления свойств и псевдосостояний выполняет внешний CSS engine. var(--color-shadow-primary) читает внешнюю переменную темы.

## Используемые сущности и зависимости

| Сущность | Файл-источник | Вид / цель связи |
| --- | --- | --- |
| Заголовок и два списка | [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | crit-wounds/header/name/add-crit и собственный цикл травм |
| Первый список | [templates/partials/crit-wounds-table.hbs](../../../../../templates/partials/crit-wounds-table.hbs) | critwound/header/info/days-rest, поля дней/лечения; ol/li |
| Редактор Item | [templates/sheets/item/criticalWound-sheet.hbs](../../../../../templates/sheets/item/criticalWound-sheet.hbs) | Те же поля/классы; select внутри critwound-info, без wound-name |
| treat/add и старый delete listener | [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) | JS управляет Item; .delete-crit иском в listener, но HTML-кнопка не найдена |
| Общие классы | [styles/system-styles.css](../../../../../styles/system-styles.css) | flex и invisible; скрытие не определяется этим CSS |
| Импорт | [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Порядок 14, до item-sheets:15 |

Входной ресурс [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) зарегистрирован в [system.json](../../../../../system.json); эти соседи проверены в пределах подключения, их полные карточки здесь не создаются. Найденный локальный файл и строка @import не доказывают доступ по HTTP для службы Foundry.

## Известные потребители

Три HBS выше имеют действующие классы. В module/templates не найдены элементы с классами critwound-data, critwound-display, critwound-controls, crit-wounds-table, critwounds-description, crit-wound-description, crit-wound-mod-description, wound-name, delete-crit. Последний встречается только в JS-listener. Имена файлов/partials исключены из доказательства наличия CSS-потребителя; внешние модули не проверены.

Область поиска: все templates/module/styles текущего среза, имена полей/классов в динамических producer и указанные методы ядра. Имена файлов и упоминания в комментариях отделены от создания HTML. Содержимое миров, внешние расширения и пользовательский enriched HTML не обследованы.

## Данные и изменения состояния

Повторные .crit-wounds-table объединяют border/margin/background; :last-child снимает нижнюю рамку лишь у последнего tr внутри такой таблицы. :not(.invisible) задаёт padding, не показ/скрытие. width40px!important у days-healed/healing-time сильнее обычных правил ширины. --color-shadow-primary предоставляет тема Foundry (/opt/foundryvtt/public/css/foundry2.css:95/255); наличие var без fallback не проверено по всем темам. -webkit-fill-available используется только у не найденного .wound-name. Общее .description .editor из item-sheets относится к другим элементам, не к ширине дней.

CSS не создаёт документы, не меняет значения полей и не запускает сохранение/игровые действия. Размещение, hover и видимость отделены от JS управления. Файл прочитан целиком: 134 логических строк; переводы строк LF, нет завершающего newline.

## Проверки и доказательства

Группы 06/08/11:26 rule-узлов,52 declarations, два important; реальный Handlebars/parse5 получил две строки и два поля days-healed на один Item в текущей вкладке, одну пару в Item-редакторе. Классов crit-wounds-table/critwound-display в результате нет. Повторный список — прежняя issue54; применения лечения и computed styles не исполнялись.

Методика — [журнал TASK-0003.047](../../review-log.md#task-0003047). Использованы PostCSS8.5.12, Handlebars4.7.9 и parse5 из существующих зависимостей Foundry14.367.0. Разбор CSS AST подтверждает структуру, не принятие каждого значения браузером или итоговое computed style.

## Непроверенные участки и открытые вопросы

Полностью прочитаны все правила; непрочитанных частей файла нет. Не запускались мир, браузер, HTTP-загрузка, вычисление раскладки, смена темы, масштабирование и внешние модули. Размеры/цвета из declarations не объявлены измеренными пикселями интерфейса. Изменение оформления и удаление правил не согласовывались.

## Связанные проблемы

[54](../../../../issues/potential/issue-00054.md) дополнена: дублирование сохраняется независимо от старых табличных CSS-правил. Отсутствующие HTML-потребители и неиспользуемые правила не зарегистрированы отдельными проблемами.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003047) |
