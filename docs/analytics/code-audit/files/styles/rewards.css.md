# styles/rewards.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/rewards.css](../../../../../styles/rewards.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 4 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Горизонтальное расположение одной записи журнала IP или валюты в окне RewardsSheet.

## Условия использования

Импорт 27 перед character/sheet.css. RewardsSheet имеет extended-sheet, поэтому правила основного листа с :not(.extended-sheet) исключают это окно. Глобальная .logEntry не ограничена Actor, но других совпадений в module/templates не найдено.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 1 CSS-правил и 2 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `.logEntry` | 1 | `display: flex`; `justify-content: space-around` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

Единственное .logEntry задаёт display:flex и justify-content:space-around. В обеих вкладках каждая запись содержит три label. CSS не определяет сортировку, суммы, даты, перенос строк или цвет и не управляет выдачей награды. Имя класса чувствительно к регистру: logEntry.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/actor/rewards/ip.hbs](../../../../../templates/sheets/actor/rewards/ip.hbs) | div.logEntry | label, ip, isMagic в одной записи. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/actor/rewards/currency.hbs](../../../../../templates/sheets/actor/rewards/currency.hbs) | div.logEntry | label, amount и локализованный type. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/actor/rewardsSheet.js](../../../../../module/actor/rewardsSheet.js) | PARTS.ip/currency; _prepareContext | Выбор двух шаблонов и system.logs/config. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/data/actor/templates/character/logData.js](../../../../../module/data/actor/templates/character/logData.js) | ipLog/currencyLog | Исходные массивы записей; изменение массива — вне CSS. | Исходники, поиск module/templates/styles и AST; границы ниже |



## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/sheets/actor/rewards/ip.hbs](../../../../../templates/sheets/actor/rewards/ip.hbs) | div.logEntry | label, ip, isMagic в одной записи. |
| [templates/sheets/actor/rewards/currency.hbs](../../../../../templates/sheets/actor/rewards/currency.hbs) | div.logEntry | label, amount и локализованный type. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 1 правил, 2 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | 1 правило / 2 declarations. Группа 14: обе настоящие вкладки дают по одной logEntry для массива из одной записи; никакая запись Actor не выполнялась. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | Импорт 27 перед character/sheet.css. RewardsSheet имеет extended-sheet, поэтому правила основного листа с :not(.extended-sheet) исключают это окно. Глобальная .logEntry не ограничена Actor, но других совпадений в module/templates не найдено. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Проверки локальные: Foundry 14.367.0, Node 24.16.0, Handlebars 4.7.9, PostCSS 8.5.12. Модели, helpers, методы и HBS — реальные исходники; UUID resolver, Actor/DOM/ChatMessage и отдельные вспомогательные helpers представлены указанными в журнале фасадами. Не запускались мир, браузер, HTTP, БД, установка пакетов или сборка. Совпадение селектора и существование файла не доказывают конечный вид или доступ службы.

## Связанные проблемы

Новой проблемы в пределах данного файла не зарегистрировано. Это не вывод об исправности всех связанных процессов.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |
