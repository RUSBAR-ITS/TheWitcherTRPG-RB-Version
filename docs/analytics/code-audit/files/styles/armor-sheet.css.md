# styles/armor-sheet.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/armor-sheet.css](../../../../../styles/armor-sheet.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 929ac4c6d90509ce06ef0795be380925e8b59e69 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.043](../../../../tasks/task-0003.043.md), 3 файла / 320 логических строк; данный файл — 24 |
| Запись перекрёстной сверки | [TASK-0003.043](../../review-log.md#task-0003043) |

## Назначение файла

Шесть глобальных правил оформления локаций, списка эффектов и строк SP старого инвентаря монстра.

## Условия использования

[system.json](../../../../../system.json):23 подключает [styles/witcher-styles.css](../../../../../styles/witcher-styles.css), который импортирует armor-sheet.css вторым ресурсом (строка 2). Все селекторы глобальные, без ограничения корнем листа брони. Файл не содержит import, url, переменных, @media, анимаций, псевдоклассов или !important.

## Введённые сущности и действия с ними

| Селектор / строки | Все declarations | Потребитель / назначение |
| --- | --- | --- |
| .effect-list, 1–4 | margin-left:10px; flex:1 | ol в общем effect-part; отступ и размер flex-элемента |
| .sp-table, 5–7 | flex:1 | Буквальный потребитель не найден в module/templates |
| .sp, 9–11 | align-items:center | div.flex.sp в старом monster-inventory-tab |
| .sp i, 13–16 | height:20px; width:20px | Иконки локаций внутри этих строк |
| .location-table, 18–20 | width:100px | th заголовка актуального armor-sheet для не-щита |
| .icon-spacer, 22–24 | width:10px | Пустые div старых строк SP |

Итого шесть правил и восемь declarations, проверено PostCSS. Отсутствие завершающей точки с запятой у flex перед закрывающей скобкой не является синтаксической ошибкой.

## Основные функции и методы

Программных функций нет. CSS влияет на представление совпавшего DOM. .sp сам не включает display:flex: это делает соседний класс .flex. flex:1 у списка/таблицы влияет на распределение пространства только при подходящем родительском layout.

## Используемые сущности и зависимости

| Сущность | Источник | Связь / доказательство |
| --- | --- | --- |
| @import | [styles/witcher-styles.css](../../../../../styles/witcher-styles.css):2 | Подключение раньше system-styles.css и activeEffect.css |
| .location-table | [templates/sheets/item/armor-sheet.hbs](../../../../../templates/sheets/item/armor-sheet.hbs):61 | Заголовок в unless Shield; текущий PARTS main WitcherArmorSheet |
| PARTS.main / регистрация armor | [module/item/sheets/WitcherArmorSheet.js](../../../../../module/item/sheets/WitcherArmorSheet.js), [module/setup/registerSheets.js](../../../../../module/setup/registerSheets.js) | Путь текущего HBS |
| .effect-list | [templates/partials/effect-part.hbs](../../../../../templates/partials/effect-part.hbs):16 | Список ActiveEffect, не таблица system.effects брони |
| .sp / .sp i / .icon-spacer | [templates/partials/monster/monster-inventory-tab.hbs](../../../../../templates/partials/monster/monster-inventory-tab.hbs) | Старые input SP; сохранённый partial загружается, но не используется текущим MonsterSheet |
| .flex / общие таблицы и иконки | [styles/system-styles.css](../../../../../styles/system-styles.css), [styles/item-sheets.css](../../../../../styles/item-sheets.css), Foundry CSS | Соседний layout/каскад; computedStyle не проверен |
| .effect-list margin/padding | [styles/activeEffect.css](../../../../../styles/activeEffect.css):42–45 | Позже задаёт margin:0 и padding:0 при той же специфичности |
| Ресурсы partial | [module/setup/handlebars.js](../../../../../module/setup/handlebars.js) | Предзагрузка; наличие partial не равно его использованию активным листом |
| Актуальный инвентарь монстра | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../module/actor/sheets/WitcherMonsterSheet.js), [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | Другой PARTS и общий современный список брони |

Оба .effect-list имеют одинаковую специфичность (0,1,0): в проверенном порядке ресурсов более поздний margin:0 перекрывает margin-left:10px. flex:1 сохраняется. Это вывод из системных declarations; полный каскад ядра/модулей и визуальный результат не вычислялись.

## Известные потребители

Прямой импорт — witcher-styles.css. Буквальные совпадения классов найдены у актуального armor-sheet, общего effect-part и старого monster-inventory-tab. В текущей таблице брони нет sp-table, sp или icon-spacer. Активный MonsterSheet использует современный tab-inventory-armors; сохранённый templates/sheets/actor/monster-sheet.hbs ссылается на старый partial, но не указан в PARTS зарегистрированного листа.

## Данные и изменения состояния

CSS не изменяет поля SP, resistance, effects, EV и документы. Актуальная форма редактирует базовые stoppingPower/maxStoppingPower, не рассчитанный суммарный SP Actor. В Shield-ветке показывает reliability; заголовок .location-table там отсутствует. Общий effect-list относится к ActiveEffect, таблица предметных воздействий armor-sheet использует item-bottom-table/list-item.

## Проверки и доказательства

Все 24 строки прочитаны. [Группы 28–29](../../review-log.md#task-0003043): PostCSS разобрал шесть правил/восемь declarations; проверен порядок импортов; настоящий Handlebars с фасадами helpers/partials и parse5 дали один .location-table для FullCover и ноль для Shield. Свойства модели для HBS переданы собственными полями отдельного объекта.

Поиск точных классов выполнен по module/templates/styles. .sp-table не имеет найденных внутренних потребителей; динамический DOM сторонних модулей не исследован. Отсутствие использования само по себе не зарегистрировано как ошибка.

## Непроверенные участки и открытые вопросы

Непрочитанных частей нет. Не запускались HTTP-загрузка, браузер, computedStyle, responsive layout, полные helpers Foundry и реальные листы. Правила доступа не менялись.

## Связанные проблемы

Новых CSS issues не зарегистрировано. [issue-00180](../../../../issues/potential/issue-00180.md) описывает устаревшие поля старого monster partial; наличие подходящих стилей не делает эти поля актуальными. Карточка проблемы не расширялась без повторения её предметной проверки.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 929ac4c6d90509ce06ef0795be380925e8b59e69; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003043) |
