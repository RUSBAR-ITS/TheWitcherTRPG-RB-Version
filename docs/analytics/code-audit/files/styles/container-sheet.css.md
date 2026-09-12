# styles/container-sheet.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/container-sheet.css](../../../../../styles/container-sheet.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 33 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Расположение строк содержимого на отдельном листе контейнера и строки фактического веса/вместимости.

## Условия использования

Импорт 18, после weapon-roll.css, до chat.css. Общий item-header в начале листа обрабатывается другим CSS. storedWeight в инвентаре является полем данных, но class=storedWeight там не найден: интерфейс вложенного контейнера в инвентаре использует другие классы из tab-inventory.css.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 6 CSS-правил и 14 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `.container-item` | 1 | Контейнер вложенных правил; собственных declarations нет |
| `.container-item → .header` | 3 | `display: flex`; `padding-top: 5px`; `padding-bottom: 5px` |
| `.container-item → .header input` | 9 | `max-width: 90%`; `margin-right: 10px` |
| `.container-item → .quantity-weight` | 14 | `display: flex` |
| `.container-item .item-content` | 20 | `display: block`; `border-style: inset`; `margin: 5px`; `padding: 5px` |
| `.storedWeight` | 27 | `display: flex`; `gap: 10px`; `text-align: center`; `font-size: 1.2em` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

Внутри .container-item header — flex с вертикальным padding 5px; его input max-width 90% и margin-right 10px. quantity-weight — flex. .container-item .item-content — block с inset-рамкой и margin/padding 5px. .storedWeight — flex/gap 10px, text-align:center/font-size 1.2em. Корень container-item группирует правила. .header здесь класс div, item-content имеет одновременно тег и класс. Никакого ограничения вместимости CSS не вводит.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/item/container-sheet.hbs](../../../../../templates/sheets/item/container-sheet.hbs) | container-item/header/quantity-weight/item-content/storedWeight | Единственный HTML-потребитель этих составных правил. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/item/sheets/WitcherContainerSheet.js](../../../../../module/item/sheets/WitcherContainerSheet.js) | PARTS; remove-item | Выбор шаблона и извлечение Item. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/data/item/containerData.js](../../../../../module/data/item/containerData.js) | itemContent/storedWeight/carry | Подготовленные значения строк; вес — вычисление модели. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/item/sheets/WitcherItemSheet.js](../../../../../module/item/sheets/WitcherItemSheet.js) | context.data=context.item.system | Связь контекста с подготовленной моделью. | Исходники, поиск module/templates/styles и AST; границы ниже |



## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/sheets/item/container-sheet.hbs](../../../../../templates/sheets/item/container-sheet.hbs) | container-item/header/quantity-weight/item-content/storedWeight | Единственный HTML-потребитель этих составных правил. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 6 правил, 14 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | 6 AST-правил / 14 declarations; все конечные selectors имеют конкретные элементы container-sheet.hbs. Значения inputs и remove-item UUID просмотрены в исходном HBS; повторная запись в контейнер не выполнялась. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | Импорт 18, после weapon-roll.css, до chat.css. Общий item-header в начале листа обрабатывается другим CSS. storedWeight в инвентаре является полем данных, но class=storedWeight там не найден: интерфейс вложенного контейнера в инвентаре использует другие классы из tab-inventory.css. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы.

## Связанные проблемы

Новой проблемы в пределах данного файла не зарегистрировано. Это не вывод об исправности всех связанных процессов.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |
