# styles/attack-sheet.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/attack-sheet.css](../../../../../styles/attack-sheet.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.041](../../../../tasks/task-0003.041.md), четыре файла / 687 логических строк; данный файл — 16 |
| Запись перекрёстной сверки | [TASK-0003.041](../../review-log.md#task-0003041) |

## Назначение файла

Оформление таблиц и select в секции attack-sheet; дополнительно глобальные отступы изображений внутри h2.
## Условия использования

[system.json](../../../../../system.json) подключает [styles/witcher-styles.css](../../../../../styles/witcher-styles.css), где @import attack-sheet.css находится на строке 3. Он загружается раньше system-styles.css и weapon-roll.css. Три первых правила ограничены div.attack-sheet, последнее действует на любой h2 img.

## Введённые сущности и действия с ними

| Селектор / строки | Все declarations | Назначение / область |
| --- | --- | --- |
| div.attack-sheet table, 1–3 | table-layout:fixed | Верхние таблицы оружейного и профессионального диалогов |
| div.attack-sheet table tr td, 5–7 | word-wrap:break-all | Заявка на перенос содержимого; значение не входит в грамматику этого свойства |
| div.attack-sheet select, 9–11 | max-width:90% | Select внутри attack-sheet; нижний ammunition вне этого div правилу не соответствует |
| h2 img, 13–16 | margin-right:10px; margin-bottom:10px | Любое изображение внутри h2; совпадает с нижним заголовком оружейного диалога вне attack-sheet |

Четыре правила, пять declarations; функций, переменных, ресурсов url, @media, шрифтов и анимаций нет.

## Основные функции и методы

JS-функций нет. Применение CSS определяется DOM, валидностью declaration и каскадом. Само наличие правила не доказывает ожидаемый перенос или размер таблицы.

## Используемые сущности и зависимости

| Сущность | Источник | Вид/место/основание |
| --- | --- | --- |
| div.flex.attack-sheet | [templates/dialog/combat/weapon-attack.hbs](../../../../../templates/dialog/combat/weapon-attack.hbs):3; [templates/dialog/combat/profession-attack.hbs](../../../../../templates/dialog/combat/profession-attack.hbs):3 | Два найденных буквальных потребителя; верхние таблицы, tr/td/select |
| h2.flex > img.item-img | [templates/dialog/combat/weapon-attack.hbs](../../../../../templates/dialog/combat/weapon-attack.hbs):199–203 | Совпадает с последним правилом, хотя находится вне div.attack-sheet |
| weapon_roll_sheet select/td | [styles/weapon-roll.css](../../../../../styles/weapon-roll.css) | Дополняет отступы/float/height, не ограничивает глобальный h2 img |
| .item-img / .flex | [styles/system-styles.css](../../../../../styles/system-styles.css):377/1 | Изображение 40px и flex-контейнер; полный каскад ядра не исследован |
| @import | [styles/witcher-styles.css](../../../../../styles/witcher-styles.css):3; [system.json](../../../../../system.json) | Загрузка на уровне всей системы |
| word-wrap / overflow-wrap | W3C CSS Text Module Level 3 §5.4 | word-wrap — legacy alias overflow-wrap; разрешены normal, break-word, anywhere |

Валидация word-wrap опирается на [W3C CSS Text Level 3, 2026-08-14](https://www.w3.org/TR/2026/CRD-css-text-3-20260814/#overflow-wrap-property), а не на имя свойства или догадку. break-all — значение другого свойства word-break. Из этого следует невалидность данной declaration; конкретный перенос в браузере зависит также от других правил.

## Известные потребители

Импортирует [styles/witcher-styles.css](../../../../../styles/witcher-styles.css). Именованный класс найден в двух шаблонах: [templates/dialog/combat/weapon-attack.hbs](../../../../../templates/dialog/combat/weapon-attack.hbs) и [templates/dialog/combat/profession-attack.hbs](../../../../../templates/dialog/combat/profession-attack.hbs). Для глобального h2 img область не ограничивается этими потребителями: он применим также к подходящему HTML чата, редакторов и внешних модулей. Наличие такой широкой области само по себе не зарегистрировано как дефект без примера нежелательного результата.

## Данные и изменения состояния

Документы/формулы не меняются. Селекторы покрывают верхние таблицы, тогда как h2 img намеренно не ограничен классом в написанном коде. У правила table-layout:fixed здесь нет сопутствующей width; итоговый алгоритм размещения требует браузерной проверки.

## Проверки и доказательства

Полностью прочитаны 16 строк. Прослежены @import, оба шаблона, позиция h2/img относительно div.attack-sheet, пересечение с weapon-roll/system-styles. Группа 28 [docs/analytics/code-audit/review-log.md](../../review-log.md#task-0003041) сверила классы и исходную declaration; грамматика отдельно проверена по W3C. CSS-парсер браузера, computedStyle, реальный перенос длинного текста и другие темы не запускались.

## Непроверенные участки и открытые вопросы

Непрочитанных участков нет. Выбор желаемой стратегии переноса, необходимость ограничивать h2 img и визуальная проверка требуют отдельного согласования. Нормативная невалидность и конкретный визуальный дефект — разные выводы.

## Связанные проблемы

[docs/issues/potential/issue-00267.md](../../../../issues/potential/issue-00267.md) — word-wrap:break-all. Статус potential, исправления не выполнялись.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; полный файл | Первичная карточка, определения и потребители сверены; [журнал](../../review-log.md#task-0003041) |
