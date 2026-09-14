# styles/item-header.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/item-header.css](../../../../../styles/item-header.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 77 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Общие размеры и расположение элементов шапки Item и шапки диалога ремонта; стили ограничены предком .item-header.

## Условия использования

Прямой импорт 20, после item-sheets.css (15) и chat.css (19). .itemname из item-sheets.css добавляет text-align:center; вложенное правило шапки не отменяет его. Теги general/itemimage реально есть в HBS. Совпадение .information/.item-header-tablerow у расы и профессии вне .item-header не включает правила этого файла; их отдельные стили уже разобраны в .047.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 15 CSS-правил и 33 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `.item-header` | 1 | Контейнер вложенных правил; собственных declarations нет |
| `.item-header → .itemname` | 3 | `display: flex`; `gap: 15px`; `align-items: center`; `padding-bottom: 5px`; `margin: 0` |
| `.item-header → .itemname → input` | 10 | `height: auto` |
| `.item-header → .itemname → .configure-item` | 14 | `font-size: 16px` |
| `.item-header → img` | 19 | `height: 100px`; `width: 100px`; `border-radius: 20%` |
| `.item-header → itemimage` | 25 | `display: flex`; `flex-direction: column` |
| `.item-header → itemimage>div` | 30 | `display: flex`; `align-items: center` |
| `.item-header → itemimage>div input[type="checkbox"]` | 35 | `margin: 3px 5px 0 0` |
| `.item-header → .information` | 39 | `width: 70%`; `margin-left: 5px`; `text-align: center`; `border: none`; `background: none` |
| `.item-header → .item-header-tablerow` | 47 | `display: flex`; `justify-content: center` |
| `.item-header → .item-header-tablerow → td` | 51 | `width: 100%`; `align-content: center` |
| `.item-header → .item-header-tablerow → td → input` | 55 | `text-align: center` |
| `.item-header → .item-header-tablerow input` | 61 | `display: block`; `width: 75px`; `margin: auto` |
| `.item-header → .item-header-tablerow select` | 67 | `display: block`; `margin: auto` |
| `.item-header → general` | 72 | `display: flex`; `justify-content: space-evenly`; `gap: 10px` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

Вложенность является CSS nesting, файл не SCSS. Пустое корневое правило группирует дочерние selectors. .itemname — flex/gap 15px/центр по поперечной оси, padding-bottom 5px/margin 0; его input имеет height auto, configure-item — 16px. Любой img внутри шапки — 100×100 с border-radius 20%. itemimage и general — селекторы HTML-тегов, не классов; первый создаёт колонку, его непосредственный div — строку, checkbox внутри этой ветви получает margin. information — ширина 70%, центрирование, прозрачный фон, нет border. Строка таблицы — flex, td шириной 100%, input центрирован. Общий input строки ограничен 75px, display block/margin auto; select тоже block/margin auto. general — flex/space-evenly/gap 10px. У spell-header дополнительный item-header-wrapper меняет, какой div является непосредственным потомком itemimage.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/partials/item-header.hbs](../../../../../templates/partials/item-header.hbs) | header.item-header, itemimage, general, information | Общая шапка десяти листов; itemname/configure-item и поля количества/цены. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/partials/spell-header.hbs](../../../../../templates/partials/spell-header.hbs) | item-header и item-header-wrapper | Шапка магии с теми же базовыми правилами. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/hex-sheet.hbs](../../../../../templates/sheets/item/hex-sheet.hbs) | собственный header.item-header | Встроенная шапка порчи. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/ritual-sheet.hbs](../../../../../templates/sheets/item/ritual-sheet.hbs) | собственный header.item-header | Встроенная шапка ритуала. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/dialog/repair-dialog.hbs](../../../../../templates/dialog/repair-dialog.hbs) | header.item-header, information.repair-info | Повторное использование общего оформления в диалоге. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/item/sheets/WitcherItemSheet.js](../../../../../module/item/sheets/WitcherItemSheet.js) | configureItem, editImage, _prepareContext | Поведение gear/img задают data-action и ядро, а не CSS. | Исходники, поиск module/templates/styles и AST; границы ниже |



## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/partials/item-header.hbs](../../../../../templates/partials/item-header.hbs) | header.item-header, itemimage, general, information | Общая шапка десяти листов; itemname/configure-item и поля количества/цены. |
| [templates/partials/spell-header.hbs](../../../../../templates/partials/spell-header.hbs) | item-header и item-header-wrapper | Шапка магии с теми же базовыми правилами. |
| [templates/sheets/item/hex-sheet.hbs](../../../../../templates/sheets/item/hex-sheet.hbs) | собственный header.item-header | Встроенная шапка порчи. |
| [templates/sheets/item/ritual-sheet.hbs](../../../../../templates/sheets/item/ritual-sheet.hbs) | собственный header.item-header | Встроенная шапка ритуала. |
| [templates/dialog/repair-dialog.hbs](../../../../../templates/dialog/repair-dialog.hbs) | header.item-header, information.repair-info | Повторное использование общего оформления в диалоге. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 15 правил, 33 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | Все 15 правил / 33 declarations сопоставлены с общей шапкой, spell/hex/ritual и repair. Вложенные scopes сохранены в AST; исправление структуры HTML или браузерная оценка flex на tr не выполнялись. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | Прямой импорт 20, после item-sheets.css (15) и chat.css (19). .itemname из item-sheets.css добавляет text-align:center; вложенное правило шапки не отменяет его. Теги general/itemimage реально есть в HBS. Совпадение .information/.item-header-tablerow у расы и профессии вне .item-header не включает правила этого файла; их отдельные стили уже разобраны в .047. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Текущая статическая сверка завершена; прежние пофайловые опыты сохраняют свои даты и фасады. item-header оформляет image/name/general/itemimage и named quantity/weight/cost. Отрисовка кнопки configureItem/изображения связана с actions ItemSheet; CSS не выполняет действие и не задаёт числовое приведение. Непроверенные границы и следующий критерий: [U016-03](../../cross-check-0002.md#u016-03). Полный браузерный цикл, мир, HTTP и запись в БД не выполнялись; смысл перевода/игровых правил не оценивался.

## Связанные проблемы

Новой проблемы в пределах данного файла не зарегистрировано. Это не вывод об исправности всех связанных процессов.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |

## Сквозная сверка TASK-0004.016

2026-09-14; rusbar-main, 0588289c84d955201457f44ec2f8152a9258135e. Исходник совпадает со срезом TASK-0001; изменено только описание.

item-header оформляет image/name/general/itemimage и named quantity/weight/cost. Отрисовка кнопки configureItem/изображения связана с actions ItemSheet; CSS не выполняет действие и не задаёт числовое приведение. Подключение: импорт № 20 в общем CSS; 15 правил / 33 деклараций.

Сопоставленные определения и потребители: [module/item/sheets/WitcherItemSheet.js](../module/item/sheets/WitcherItemSheet.js.md), [templates/partials/item-header.hbs](../templates/partials/item-header.hbs.md), [styles/witcher-styles.css](witcher-styles.css.md).

[Протокол и границы](../../review-log.md#task-0004016) — TASK-0004.016; процессы [R016-07](../../cross-check-0002.md#r016-07). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
