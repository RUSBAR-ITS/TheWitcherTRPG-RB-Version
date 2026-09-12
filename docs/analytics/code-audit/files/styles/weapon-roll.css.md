# styles/weapon-roll.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/weapon-roll.css](../../../../../styles/weapon-roll.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.041](../../../../tasks/task-0003.041.md), четыре файла / 687 логических строк; данный файл — 19 |
| Запись перекрёстной сверки | [TASK-0003.041](../../review-log.md#task-0003041) |

## Назначение файла

Четыре правила размеров и выравнивания элементов внутри оружейного диалога.
## Условия использования

[system.json](../../../../../system.json) подключает styles/witcher-styles.css; [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) импортирует этот файл на строке 17, после system-styles.css (строка 4) и attack-sheet.css (строка 3). Правила доступны глобально, но каждый селектор ограничен предком .weapon_roll_sheet.

## Введённые сущности и действия с ними

| Селектор / строки | Все declarations | Потребитель и смысл |
| --- | --- | --- |
| .weapon_roll_sheet input, 1–6 | text-align:center !important; margin:0px 5px; width:30px; float:right | Все input оружейного диалога, включая checkbox/number/text |
| .weapon_roll_sheet td, 8–10 | height:35px | Все ячейки внутри корня, не только верхний attack-sheet |
| .weapon_roll_sheet select, 12–15 | margin:0px 5px; float:right | damageType, location, strike, условные range/ammunition |
| .weapon_roll_sheet label, 17–19 | vertical-align:middle | Подписи внутри корня |

Итого четыре правила, восемь declarations. Переменных, @media, @font-face, url, псевдоклассов и анимаций нет.

## Основные функции и методы

JS-функций нет. CSS читается браузером через @import; применение зависит от соответствия селектора DOM и каскада.

## Используемые сущности и зависимости

| Сущность | Источник | Вид/доказательство |
| --- | --- | --- |
| weapon_roll_sheet | [templates/dialog/combat/weapon-attack.hbs](../../../../../templates/dialog/combat/weapon-attack.hbs) | Корневой div; единственный найденный буквальный потребитель класса в шаблонах |
| input, td, select, label | Тот же шаблон | Потомки root в таблицах/разделах; верхняя секция содержит также attack-sheet |
| div.attack-sheet select/table | [styles/attack-sheet.css](../../../../../styles/attack-sheet.css) | Пересечение: max-width90%, table-layoutfixed и декларация переноса; не заменяют margin/float |
| input.small и общие input | [styles/system-styles.css](../../../../../styles/system-styles.css) и Foundry | У системного input.small width5ch, но этот класс не используется данным HBS; правила ядра целиком не проверены |
| Inline customDmg | [templates/dialog/combat/weapon-attack.hbs](../../../../../templates/dialog/combat/weapon-attack.hbs):224 | width:auto/max-width50% на конкретном input; inline width при обычном каскаде приоритетнее width30px |
| @import | [styles/witcher-styles.css](../../../../../styles/witcher-styles.css):17, [system.json](../../../../../system.json) | Путь подключения; манифест не ссылается на этот CSS напрямую |

## Известные потребители

[styles/witcher-styles.css](../../../../../styles/witcher-styles.css) импортирует ресурс; [templates/dialog/combat/weapon-attack.hbs](../../../../../templates/dialog/combat/weapon-attack.hbs) определяет классы и целевые элементы. Поиск выполнен по module/templates/styles. Шаблон profession-attack использует другой корневой класс и не совпадает с .weapon_roll_sheet.

## Данные и изменения состояния

Влияние только на представление. Файл не меняет значения формы или документы. width30px относится и к checkbox, !important задан только text-align. Inline customDmg не отменяет margin/float/text-align. Реальные размеры, overflow и доступность UI не выводятся только из деклараций.

## Проверки и доказательства

Прочитаны 19 строк; все четыре селектора и восемь declarations сопоставлены с исходным HBS и цепочкой подключения. Группа 28 [docs/analytics/code-audit/review-log.md](../../review-log.md#task-0003041) проверила root в настоящем HBS-рендере/parse5 и точное inline customDmg. Это проверка разметки/каскадных входов, не computedStyle или screenshot браузера.

## Непроверенные участки и открытые вопросы

Непрочитанных участков нет. Браузер, сторонние темы, полные правила Foundry, отображение при изменении масштаба/языка не проверялись.

## Связанные проблемы

Собственной новой проблемы в этом файле по выполненным проверкам не зарегистрировано. [docs/issues/potential/issue-00267.md](../../../../issues/potential/issue-00267.md) относится к соседнему attack-sheet.css; общие селекторы при этом описаны отдельно.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; полный файл | Первичная карточка, определения и потребители сверены; [журнал](../../review-log.md#task-0003041) |
