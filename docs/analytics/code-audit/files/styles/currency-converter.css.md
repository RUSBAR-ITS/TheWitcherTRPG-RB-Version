# styles/currency-converter.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/currency-converter.css](../../../../../styles/currency-converter.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.048](../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 39 |
| Запись перекрёстной сверки | [TASK-0003.048](../../review-log.md#task-0003048) |

## Назначение файла

Сетка балансов и четырёх полей содержимого диалога конвертации валют.

## Условия использования

Импорт 8, сразу после tab-inventory.css. Все вложенные правила ограничены корнем currency-converter. light-dark выбирается браузером по color-scheme окружения; свой color-scheme/@media файл не устанавливает. Сетка полей остаётся четырёхколоночной: breakpoint здесь нет.

## Введённые сущности и действия с ними

Программных экспортов, классов JS и полей модели нет. Собственные сущности — 6 CSS-правил и 21 declarations. В таблице перечислены все selectors и свойства; знак → сохраняет реальную вложенность, а не обозначает дополнительный HTML-элемент.

| Селектор и внешние scopes | Строка | Полный набор declarations |
| --- | --- | --- |
| `.currency-converter` | 1 | `display: flex`; `flex-direction: column`; `gap: 12px` |
| `.currency-converter .converter-balances` | 7 | `display: grid`; `grid-template-columns: repeat(auto-fit, minmax(120px, 1fr))`; `gap: 6px 12px`; `background-color: light-dark(#22222210, #e7d1b110)`; `border: 1px solid light-dark(#22222240, #e7d1b140)`; `border-radius: 8px`; `padding: 8px` |
| `.currency-converter .converter-balance` | 17 | `display: flex`; `justify-content: space-between`; `font-size: 12px` |
| `.currency-converter .converter-fields` | 23 | `display: grid`; `grid-template-columns: repeat(4, minmax(0, 1fr))`; `gap: 8px` |
| `.currency-converter label` | 29 | `display: flex`; `flex-direction: column`; `gap: 4px`; `font-size: 12px` |
| `.currency-converter input, .currency-converter select` | 36 | `width: 100%` |

## Основные функции и методы

JavaScript-функций нет. Браузер сопоставляет selectors с DOM и применяет каскад; CSS не вызывает методы системы.

currency-converter — flex-колонка/gap 12px. converter-balances — grid repeat(auto-fit,minmax(120px,1fr)), gap 6px 12px, фон/рамка light-dark(), border-radius 8px/padding 8px. converter-balance — flex/space-between/font-size 12px. converter-fields — четыре minmax(0,1fr) колонки/gap 8px. labels — вертикальные flex/gap 4px/font-size 12px. input/select — width 100%. Результат обмена не относится к этому CSS: отдельный chat/currency-conversion.hbs не содержит корень currency-converter.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи / место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Единственное подключение этого файла в системных стилях. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [system.json](../../../../../system.json) | styles | Загружает styles/witcher-styles.css. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs) | currency-converter/converter-balances/balance/fields | Содержимое DialogV2: остатки и amount/from/to/fee. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [module/actor/mixins/currencyConverterMixin.js](../../../../../module/actor/mixins/currencyConverterMixin.js) | openCurrencyConverter | Готовит options/currencies, вызывает DialogV2.input и рассчитывает обмен. | Исходники, поиск module/templates/styles и AST; границы ниже |
| [templates/chat/currency-conversion.hbs](../../../../../templates/chat/currency-conversion.hbs) | отдельный результат | Проверенный отрицательный потребитель: классов данного CSS нет. | Исходники, поиск module/templates/styles и AST; границы ниже |



## Известные потребители

| Файл-потребитель | Способ использования | Доказательство |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | Прямой @import | Путь найден один раз |
| [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs) | currency-converter/converter-balances/balance/fields | Содержимое DialogV2: остатки и amount/from/to/fee. |

Поиск проведён в module/, templates/ и styles/ текущего checkout. Совпадение имени файла или поля не выдаётся за CSS-потребителя; старые и динамические элементы различены в описании. Внешние модули, переопределённые темы и мировые макросы не исследованы.

## Данные и изменения состояния

Стили не изменяют Item, Actor, ActiveEffect или настройки. Они оформляют DOM; игровые флаги, условия HBS и обработчики классов описаны выше. Файл не содержит расчёта характеристик, стоимости или количества.

## Проверки и доказательства

| Проверка | Источник / сценарий | Результат | Предел |
| --- | --- | --- | --- |
| Полный разбор | Исходный файл; PostCSS AST | 6 правил, 21 declarations, все вложенные scopes учтены | PostCSS не валидирует семантику значения CSS и не является браузером |
| Потребители/состояния | Чтение указанных HBS/JS и локальные сценарии | 6 правил / 21 declaration. Группа 14: четыре label и balances/fields, отдельный результат без корневого класса. selectOptions в этой проверке — фасад; настоящие варианты/валидация разобраны в .036. | Без визуального рендера |
| Каскад | system.json и styles/witcher-styles.css | Импорт 8, сразу после tab-inventory.css. Все вложенные правила ограничены корнем currency-converter. light-dark выбирается браузером по color-scheme окружения; свой color-scheme/@media файл не устанавливает. Сетка полей остаётся четырёхколоночной: breakpoint здесь нет. | Сторонние стили/темы не охвачены |

## Непроверенные участки и открытые вопросы

Текущая статическая сверка завершена; прежние пофайловые опыты сохраняют свои даты и фасады. Все шесть правил ограничены .currency-converter: auto-fit балансы и четырёхколоночные поля. Одноимённые данные сообщения о конвертации не получают этот scope; операции валюты описаны в .014. Непроверенные границы и следующий критерий: [U016-03](../../cross-check-0002.md#u016-03). Полный браузерный цикл, мир, HTTP и запись в БД не выполнялись; смысл перевода/игровых правил не оценивался.

## Связанные проблемы

Новой проблемы в пределах данного файла не зарегистрировано. Это не вывод об исправности всех связанных процессов.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003048) |

## Сквозная сверка TASK-0004.016

2026-09-14; rusbar-main, 0588289c84d955201457f44ec2f8152a9258135e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Все шесть правил ограничены .currency-converter: auto-fit балансы и четырёхколоночные поля. Одноимённые данные сообщения о конвертации не получают этот scope; операции валюты описаны в .014. Подключение: импорт № 8 в общем CSS; 6 правил / 21 деклараций.

Сопоставленные определения и потребители: [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../templates/sheets/actor/currencyConverter/currencyConverter.hbs.md), [templates/sheets/actor/rewards/currency.hbs](../templates/sheets/actor/rewards/currency.hbs.md), [module/actor/rewardsSheet.js](../module/actor/rewardsSheet.js.md), [module/actor/mixins/currencyConverterMixin.js](../module/actor/mixins/currencyConverterMixin.js.md), [styles/witcher-styles.css](witcher-styles.css.md).

[Протокол и границы](../../review-log.md#task-0004016) — TASK-0004.016; процессы [R016-10](../../cross-check-0002.md#r016-10). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
