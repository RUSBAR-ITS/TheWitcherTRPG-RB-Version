# styles/substances.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/substances.css](../../../../../styles/substances.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 73 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Панель девяти алхимических веществ, активное состояние группы и общий размер иконок веществ в панели, рецепте и HTML списка алхимии.

## Условия использования

Импорт 16. Переменные цвета --color-border-light-tertiary/--color-underline-header принадлежат окружению темы; первые две используются только правилами без текущего совпадения. --color-shadow-primary используется активной кнопкой и определён core-темой. Нет собственного @media; девять кнопок располагаются одной flex-строкой без flex-wrap в этом файле.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 12 CSS-правил и 38 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `.substances-section > span` | 1 | `display: block`; `text-align: center`; `border: 1px solid var(--color-border-light-tertiary)`; `margin: 1px`; `border-radius: 10px` |
| `.substances` | 9 | `display: flex` |
| `.substances-section table` | 13 | `margin: 0 0 0.5em 0` |
| `.substance-type-subheader` | 17 | `font-size: large`; `border-bottom: 1px solid var(--color-underline-header)` |
| `.substances-menu` | 22 | `display: flex`; `gap: 3px`; `font-size: 1rem`; `background-color: transparent` |
| `.substances-menu:hover` | 29 | `border-radius: 5px`; `background-color: rgba(25, 25, 25, 0.05)` |
| `.substances-item` | 34 | `display: flex`; `align-items: center`; `gap: 10px`; `padding: 5px`; `background-color: transparent`; `box-shadow: none`; `border: 1px solid transparent`; `border-radius: 5px` |
| `.sub-open` | 45 | `background-color: rgba(25, 25, 25, 0.05)`; `border: solid 1px #9a9991`; `border-radius: 5px` |
| `.substances-item:hover` | 51 | `padding: 5px`; `background-color: rgba(255, 255, 255, 0.3)`; `border-radius: 5px`; `box-shadow: -2px 8px 8px -10px #9a9991`; `transition: all 0.3s ease` |
| `.substance-img` | 59 | `height: 25px`; `width: 25px`; `margin: 0`; `border: none`; `border-radius: 50%` |
| `.item-substance-display:hover` | 67 | `box-shadow: 0 0 5px var(--color-shadow-primary)` |
| `.item-substance-display:active` | 71 | `transform: scale(1.2)` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

substances-menu — flex/gap 3px, hover с полупрозрачным фоном. substances-item — flex с gap 10px/padding 5px, прозрачными фоном/рамкой; sub-open задаёт серую рамку и фон. Более специфичный substances-item:hover временно меняет фон, тень и transition .3s ease; sub-open не управляет видимостью списка, список выбирает HBS if. substance-img — 25×25, круглая, без margin/border. item-substance-display:hover добавляет тень var(--color-shadow-primary), :active scale(1.2). Старые .substances, .substance-type-subheader, .substances-section > span и .substances-section table не имеют совпадений в текущей панели: там div/span внутри кнопок и ol списков; system.type='substances' не CSS-класс.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/partials/character/substances.hbs](../../../../../templates/partials/character/substances.hbs) | substances-section/menu/item, sub-open, substance-img, item-substance-display | Панель и девять условных флагов. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../module/actor/sheets/mixins/itemMixin.js) | itemListener/_onSubstanceDisplay | click → update system.pannels.<key>IsOpen, не прямое переключение sub-open. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/data/actor/templates/character/pannelsData.js](../../../../../module/data/actor/templates/character/pannelsData.js) | vitriolIsOpen…fulgurIsOpen | Состояния группы Actor. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../templates/sheets/item/diagrams-sheet.hbs) | substance-img | Девять иконок в th формулы. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/item/witcherItem.js](../../../../../module/item/witcherItem.js) | alchemyCraftComponentsList, HTML substance-img | Динамический HTML изображения и количества каждого положительного вещества. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | partial substances.hbs | Действующая Character-вкладка. | Исходники, поиск module/templates/styles и AST; границы ниже |



## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/partials/character/substances.hbs](../../../../../templates/partials/character/substances.hbs) | substances-section/menu/item, sub-open, substance-img, item-substance-display | Панель и девять условных флагов. |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../templates/sheets/item/diagrams-sheet.hbs) | substance-img | Девять иконок в th формулы. |
| [module/item/witcherItem.js](../../../../../module/item/witcherItem.js) | alchemyCraftComponentsList, HTML substance-img | Динамический HTML изображения и количества каждого положительного вещества. |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | partial substances.hbs | Действующая Character-вкладка. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 12 правил, 38 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | 12 правил / 38 declarations. Группа 15: девять отдельных update payload и девять рендеров с единственным sub-open, все девять PNG существуют. Вложенный список заменён явно обозначенным partial-фасадом; полный список ранее проверен в .034. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | Импорт 16. Переменные цвета --color-border-light-tertiary/--color-underline-header принадлежат окружению темы; первые две используются только правилами без текущего совпадения. --color-shadow-primary используется активной кнопкой и определён core-темой. Нет собственного @media; девять кнопок располагаются одной flex-строкой без flex-wrap в этом файле. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Текущая статическая сверка завершена; прежние пофайловые опыты сохраняют свои даты и фасады. Девять data-subtype соответствуют system.pannels.<subtype>IsOpen и .sub-open. Actor.update запускает itemMixin; CSS только отображает группу и картинки 25×25, не списывает ингредиенты. Непроверенные границы и следующий критерий: [U016-05](../../cross-check-0002.md#u016-05). Полный браузерный цикл, мир, HTTP и запись в БД не выполнялись; смысл перевода/игровых правил не оценивался.

## Связанные проблемы

Новой проблемы в пределах данного файла не зарегистрировано. Это не вывод об исправности всех связанных процессов.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |

## Сквозная сверка TASK-0004.016

2026-09-14; rusbar-main, 0588289c84d955201457f44ec2f8152a9258135e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Девять data-subtype соответствуют system.pannels.<subtype>IsOpen и .sub-open. Actor.update запускает itemMixin; CSS только отображает группу и картинки 25×25, не списывает ингредиенты. Подключение: импорт № 16 в общем CSS; 12 правил / 38 деклараций.

Сопоставленные определения и потребители: [module/actor/sheets/mixins/itemMixin.js](../module/actor/sheets/mixins/itemMixin.js.md), [templates/partials/character/substances.hbs](../templates/partials/character/substances.hbs.md), [styles/witcher-styles.css](witcher-styles.css.md).

[Протокол и границы](../../review-log.md#task-0004016) — TASK-0004.016; процессы [R016-11](../../cross-check-0002.md#r016-11). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
