# templates/sheets/actor/currencyConverter/currencyConverter.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/currencyConverter/currencyConverter.hbs](../../../../../../../../templates/sheets/actor/currencyConverter/currencyConverter.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.036](../../../../../../../tasks/task-0003.036.md), 4 файла, 164 логические строки |
| Запись перекрёстной сверки | [TASK-0003.036](../../../../../review-log.md#task-0003036) |

## Назначение файла

Содержимое диалога обмена: доступные балансы и четыре поля amount/from/to/fee. Форму и кнопку подтверждения создаёт DialogV2 вокруг этого фрагмента.

## Условия использования

Единственный literal renderTemplate — Actor currencyConverterMixin:36–42. В preloadHandlebarsTemplates файл не найден; загружается по пути при открытии. Контекст только options/currencies; названия балансов локализуются, значения выводятся обычными {{}}.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| .currency-converter/.converter-balances/.converter-balance | 1–9 | Список остатков currencies | each currencies | label и value; excluded уже отфильтрован producer |
| .converter-fields / amount | 11–15 | Сумма source валюты | input number name=amount | min1/step1/value1/data-dtype Number; required отсутствует |
| from / to | 16–27 | Две валюты | selectOptions options localize=true | selected crown/selected oren, одинаковые варианты, не исключают выбор друг друга |
| fee | 28–31 | Процент комиссии | input number name=fee | min0/max100/step1/value0/data-dtype Number; required отсутствует |

## Основные функции и методы

Программных методов нет. each выводит currencies, localize обрабатывает label/подписи, selectOptions создаёт оба набора options. Нет скрипта пересчёта, onChange, callback, проверки from!==to или собственных form/submit. Input показывает ограничения интерфейса; семантику и финальную проверку выполняет caller/core.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| options/currencies | [module/actor/mixins/currencyConverterMixin.js](../../../../../../../../module/actor/mixins/currencyConverterMixin.js) | контекст renderTemplate | 36–42 | {value,label} и {key,label,value}; значение currencyData[key] |
| WITCHER.currency / excluded | [module/setup/config.js](../../../../../../../../module/setup/config.js) | опосредованные options | 624–645 | По умолчанию6 валют, не7; falsecoin скрыт на подготовке |
| currency() | [module/data/actor/templates/common/currencyData.js](../../../../../../../../module/data/actor/templates/common/currencyData.js) | значения model | span value | Семь NumberField, контекст может отфильтровать часть |
| localize / selectOptions / each | Foundry client/applications/handlebars.mjs; Handlebars4.7.9 | helpers | 3–7,13–30 | Настоящий selectOptions и Handlebars; два select независимы |
| WITCHER.currencyConverter.amount/from/to/fee, WITCHER.Currency.* | [lang/en.json](../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../lang/ru.json) | локализация | Подписи и значения options | expandObject+Localization;16 ключей маршрута включая соседнюю кнопку |
| .currency-converter и вложенные классы | [styles/currency-converter.css](../../../../../../../../styles/currency-converter.css) | CSS | 1–37 | Вертикальная обёртка, grid балансов/четырёх полей; импорт8 styles/witcher-styles.css |
| FormDataExtended / DialogV2 | Foundry client/applications/{ux/form-data-extended.mjs,api/dialog.mjs} | сбор/проверка формы | amount/fee Number, from/to String | Blank numeric→null. Dialog content проходит cleanHTML; input/select/name/min/max/step/data-* разрешены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/mixins/currencyConverterMixin.js](../../../../../../../../module/actor/mixins/currencyConverterMixin.js) | currencyConverter.hbs | await renderTemplate при открытии | 36–42 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

HTML не меняет Actor. Обычный начальный набор FormDataExtended: {amount:1,from:'crown',to:'oren',fee:0}. Пустой numeric input→null, а не Number0; дальнейшая арифметика может привести null к0. При всех excluded отрисованы0 options; окно не блокируется producer. Если удалить конфигурацию excluded, falsecoin появляется без собственного курса. Здесь не определяется курс либо комиссия, кроме начального ввода0.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Форма/helper | 02,04,12 | Два независимых select,6обычных валют,0при исключении всех; Number/String/null; ограничения HTML | Фасад элементов, не нативная browser validity |
| Локализация/CSS | 21; чтение CSS/allowlist core | Labels16 ключей маршрута доступныEN/RU; формы разрешеныcleanHTML | Видимый layout/очистка в DOM не выполнялись |

## Непроверенные участки и открытые вопросы

Проверены локальные исходники Foundry 14.367.0, Node 24.16.0, настоящие модели/методы/HBS и отдельные core-функции. Dialog, базовые приложения, коллекции и запись документов подменены; EventTarget настоящий Node, не браузерный DOM. Мир, сеть, права и транзакции реальной БД не запускались. HTML min/max/step не выдаются за серверную валидацию. Курсы и экономические правила не менялись. Пустые options, unknown key и altered CONFIG исполнялись как контролируемые случаи; штатная конфигурация предоставляет шесть известных валют. Общие балансы не обновляются реактивно в открытом диалоге.

## Связанные проблемы

[issue-00020](../../../../../../../issues/potential/issue-00020.md), [issue-00227](../../../../../../../issues/potential/issue-00227.md), [issue-00228](../../../../../../../issues/potential/issue-00228.md), [issue-00229](../../../../../../../issues/potential/issue-00229.md). Одинаковые from/to разрешены вариантами; отрицательный/дробный ввод проверен на уровне data/API. Видимость limits не доказывает невозможность вызова обработчика с другим вводом.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `32d8fdd029ce4c6401db25f0d9645445ac0f8ca2`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003036) |

## Дополнительная сверка TASK-0003.048

2026-09-12, rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670; исходники не изменены.

Полный [styles/currency-converter.css](../../../../../../../../styles/currency-converter.css) содержит 6 правил/21 declaration: auto-fit сетка балансов и фиксированные четыре колонки полей. Группа 14 подтверждает четыре label и отсутствие класса currency-converter в отдельном результате [templates/chat/currency-conversion.hbs](../../../../../../../../templates/chat/currency-conversion.hbs). Светлый/тёмный вариант задаёт light-dark в окружении темы, CSS не определяет собственный color-scheme. В этой порции selectOptions — фасад; прежняя проверка настоящего helper/формы .036 сохраняется.

[Сценарии, результаты и ограничения](../../../../../review-log.md#task-0003048). Связанные файлы повторно не засчитываются в покрытие.
