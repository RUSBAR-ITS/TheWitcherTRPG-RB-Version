# styles/monster-skill-tab.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/monster-skill-tab.css](../../../../../styles/monster-skill-tab.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 42 |
| Запись перекрёстной сверки | [TASK-0003.049](../../review-log.md#task-0003049) |

## Назначение файла

Прежние группы навыков монстра и общие таблицы старой вкладки магии.

## Условия использования

Импорт 10 после tab-skills.css. Классы глобальны и не ограничены MonsterSheet. Красный span-стиль сильнее одноклассового цвета ссылки в отношении собственного span; визуальное сочетание со старой таблицей в браузере не проверялось.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 7 CSS rule-узлов и 22 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.monster-skill` | `display: flex` |
| 5 | Корень | `.skill-display` | `position: relative`; `width: 250px`; `font-weight: bold`; `font-size: large` |
| 12 | Корень | `.expander` | `position: absolute`; `right: 0px` |
| 17 | Корень | `.skill-list td` | `padding: 1px` |
| 21 | Корень | `.skill-list span` | `display: flex`; `background-color: darkred`; `border-radius: 12px`; `color: white`; `padding: 4px`; `border-style: solid`; `width: 220px`; `height: 30px` |
| 32 | Корень | `.skill-list span:hover` | `outline: none`; `border-color: #9ecaed`; `box-shadow: 0 0 10px #9ecaed` |
| 38 | Корень | `.input-skill input` | `width: 30px`; `text-align: center`; `font-weight: bold` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

`.monster-skill` включает flex; `.skill-display` получает relative/ширину 250 и жирный крупный шрифт; `.expander` абсолютна справа. `.skill-list td` задаёт padding:1px. `.skill-list span` рисует красную кнопку шириной 220 и высотой 30; hover меняет рамку/тень. `.input-skill input` — отдельный селектор с шириной 30, center/bold.

Старый monster-skill-tab создаёт skill-display/expander, таблицы skill-list и строки monster-skill-display. У встроенной строки текст находится в a без span: правило .skill-list span на этот текст не совпадает, зато .char-skill a из tab-skills.css совпадает. Собственный старый навык содержит a > span; он получает оба вложенных оформления. Это различие старого DOM, не доказательство сбоя нынешнего листа.

Старый monster-spell-tab использует skill-list на таблицах магии, поэтому padding применяется и там. Текущий WitcherMonsterSheet.PARTS.skills выбирает общий character/tab-skills.hbs с карточками, а PARTS.magic — общий tab-magic; рассматриваемые прежние таблицы этим листом не выбраны. input-skill встречается как стиль в system-styles.css, но буквального DOM-класса input-skill в module/templates не найдено.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 10 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../templates/partials/monster/monster-skill-tab.hbs) | monster-skill, skill-display, expander, skill-list | Старая вкладка групп навыков. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-skill-display.hbs](../../../../../templates/partials/monster/monster-skill-display.hbs) | td.char-skill > a | Встроенная строка внутри skill-list; span отсутствует. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | td > a > span | Собственная строка внутри skill-list; span получает стиль. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/monster/monster-spell-tab.hbs](../../../../../templates/partials/monster/monster-spell-tab.hbs) | table.skill-list | Старая магия, тот же padding td. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../../../module/actor/sheets/WitcherMonsterSheet.js) | PARTS.skills/magic | Текущий маршрут выбирает общие character templates. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../templates/sheets/actor/monster-sheet.hbs) | старые partial навыков/магии | Родитель прежних вкладок; не нынешний PARTS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/tab-skills.css](../../../../../styles/tab-skills.css) | .char-skill a, .char-input-skill, learned-skilled/not-skilled | Соседнее оформление прежних строк. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/system-styles.css](../../../../../styles/system-styles.css) | .input-skill, .invisible | Старая утилита ширины и скрытие таблиц. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. Обращений var(...) в этом файле нет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../templates/partials/monster/monster-skill-tab.hbs) | monster-skill, skill-display, expander, skill-list | Старая вкладка групп навыков. |
| [templates/partials/monster/monster-skill-display.hbs](../../../../../templates/partials/monster/monster-skill-display.hbs) | td.char-skill > a | Встроенная строка внутри skill-list; span отсутствует. |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | td > a > span | Собственная строка внутри skill-list; span получает стиль. |
| [templates/partials/monster/monster-spell-tab.hbs](../../../../../templates/partials/monster/monster-spell-tab.hbs) | table.skill-list | Старая магия, тот же padding td. |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../templates/sheets/actor/monster-sheet.hbs) | старые partial навыков/магии | Родитель прежних вкладок; не нынешний PARTS. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 42 логических строк и PostCSS 8.5.12 | 7 rule-узлов, 22 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группа 13: реальный старый HBS скрывает isVisible=false, у встроенного навыка нет span; собственный learned-навык даёт один span. PARTS нынешнего монстра не ссылается на monster-skill-tab. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 10 после tab-skills.css. Классы глобальны и не ограничены MonsterSheet. Красный span-стиль сильнее одноклассового цвета ссылки в отношении собственного span; визуальное сочетание со старой таблицей в браузере не проверялось. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00018](../../../../issues/potential/issue-00018.md), [issue-00187](../../../../issues/potential/issue-00187.md), [issue-00192](../../../../issues/potential/issue-00192.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003049) |
