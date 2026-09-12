# styles/activeEffect.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/activeEffect.css](../../../../../styles/activeEffect.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.047](../../../../tasks/task-0003.047.md), 10 файлов / 661 логических строк; данный файл — 96 |
| Запись перекрёстной сверки | [TASK-0003.047](../../review-log.md#task-0003047) |

## Назначение файла

Оформляет общий список ActiveEffect на листах Actor и в конфигурации Item: заголовки, строки, кнопки и скрываемое описание.

## Условия использования

Прямой @import в [styles/witcher-styles.css](../../../../../styles/witcher-styles.css):21; входной CSS указан в [system.json](../../../../../system.json):23. Селекторы глобальные, без .witcher или типа документа. Это оформление [списка эффектов](../../../../../templates/partials/effect-part.hbs), а не специальная таблица changes в [редакторе ActiveEffect](../../../../../module/activeEffect/WitcherActiveEffectSheet.js).

## Введённые сущности и действия с ними

Два блока .effects-header дополняют друг друга: сетка из трёх гибких колонок и 100px под управление плюс фон/рамка. В .effect-first-row две колонки, внутри .effect-display — три. .effect-row задаёт вертикальный flex и нижнюю границу, hover подсвечивает, last-child убирает границу. nth-child(n + 2) проверяет положение среди всех детей ol, включая вложенные ol, не порядковый номер только заголовков. .effect-name > img ограничивает картинку 40×40; .effect-name > h4 не находит текущий заголовок, потому что шаблон выводит p. Это отдельное неиспользуемое правило, не доказанная поломка списка.

Ниже перечислены все 17 rule-узла и 35 declarations. Внешняя вложенность читается слева направо; списки селекторов на каждом уровне сохраняются. Дочерний селектор без & означает потомка, а не новый глобальный селектор. Директив @import/@keyframes внутри файла нет.

| Строка | Внешняя вложенность | Селектор / шаг | Свойства |
| --- | --- | --- | --- |
| 1 | Корень | `.effects-list` | `padding: 0` |
| 7 | Корень | `.effects-header` | `display: grid`; `grid-template-columns: 1fr 1fr 1fr 100px` |
| 12 | Корень | `.effects-header` | `padding: 5px`; `border-radius: 5px`; `background-color: rgba(0, 0, 0, 0.05)`; `border: 1px solid darkgray` |
| 18 | `.effects-header` | `h3` | `font-size: 18px`; `margin: 0` |
| 24 | Корень | `.effects-header:nth-child(n + 2)` | `margin-top: 5px` |
| 30 | Корень | `.effect-first-row` | `display: grid`; `grid-template-columns: 1fr 100px`; `width: 100%` |
| 36 | Корень | `.effect-display` | `display: grid`; `grid-template-columns: 1fr 1fr 1fr`; `width: 100%` |
| 42 | Корень | `.effect-list` | `padding: 0`; `margin: 0` |
| 47 | Корень | `.effect-row` | `padding: 10px 5px 10px`; `border-bottom: 1px rgba(25, 24, 19, 0.2) solid`; `display: flex`; `flex-direction: column` |
| 54 | Корень | `.effect-row:hover` | `border-radius: 5px`; `background-color: rgba(25, 25, 25, 0.05)` |
| 59 | Корень | `.effect-row:last-child` | `border-bottom: none` |
| 63 | Корень | `.effect-name` | `display: flex`; `gap: 10px`; `align-items: center` |
| 69 | Корень | `.effect-name > img` | `max-width: 40px`; `max-height: 40px` |
| 74 | Корень | `.effect-name > h4` | `margin-bottom: 0` |
| 78 | Корень | `.effect-name, .effect-source, .effect-duration, a.effect-control` | `text-shadow: none` |
| 85 | Корень | `.effect-source, .effect-duration, .effect-control` | `align-self: center` |
| 92 | Корень | `.effect-description` | `padding: 10px 120px 0 50px`; `width: 100%` |

## Основные функции и методы

JavaScript-функций и обработчиков нет. Файл объявляет CSS-правила, применяемые браузером к совпавшей разметке; вычисления свойств и псевдосостояний выполняет внешний CSS engine. 

## Используемые сущности и зависимости

| Сущность | Файл-источник | Вид / цель связи |
| --- | --- | --- |
| effects/section/effect, классы списка | [templates/partials/effect-part.hbs](../../../../../templates/partials/effect-part.hbs) | Единственный найденный producer классов; четыре категории, данные и кнопки |
| prepareActiveEffectCategories / activeEffectListener / _onActiveEffectDisplayInfo | [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../module/actor/sheets/mixins/activeEffectMixin.js) | Категории и переключение invisible по клику для непустого описания |
| PARTS.activeEffects / категории | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Тот же partial; действия create/edit/toggle/delete, собственного раскрытия не найдено |
| .invisible | [styles/system-styles.css](../../../../../styles/system-styles.css) | display:none; этот CSS описание только размещает |
| .effect-list | [styles/armor-sheet.css](../../../../../styles/armor-sheet.css) | Раньше импортирован: margin-left:10px; flex:1 |
| Загрузка | [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import21 после armor-sheet:2 и system-styles:4 |

Входной ресурс [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) зарегистрирован в [system.json](../../../../../system.json); эти соседи проверены в пределах подключения, их полные карточки здесь не создаются. Найденный локальный файл и строка @import не доказывают доступ по HTTP для службы Foundry.

## Известные потребители

[templates/partials/effect-part.hbs](../../../../../templates/partials/effect-part.hbs) включён в [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) и [templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs](../../../../../templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs). Листы Character/Monster используют общую вкладку effects; Item-конфигурация имеет отдельный маршрут. Старый [templates/sheets/actor/monster-sheet.hbs](../../../../../templates/sheets/actor/monster-sheet.hbs) тоже включает effect-part; это legacy-маршрут из уточнения .032, а не текущий лист Monster по умолчанию. [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../module/actor/sheets/mixins/activeEffectMixin.js) читает .effect-row/.effect-description/.effect-display/.effect-control; CSS не создаёт этих действий.

Область поиска: все templates/module/styles текущего среза, имена полей/классов в динамических producer и указанные методы ядра. Имена файлов и упоминания в комментариях отделены от создания HTML. Содержимое миров, внешние расширения и пользовательский enriched HTML не обследованы.

## Данные и изменения состояния

У .effect-list одинаковая специфичность с [styles/armor-sheet.css](../../../../../styles/armor-sheet.css): более поздний margin:0 сбрасывает прежний margin-left:10px, padding тоже 0; flex:1 из раннего правила остаётся, поскольку не переопределён. .invisible из system-styles сохраняет display:none даже при padding/width описания. Общие Foundry .flexrow/.item и сторонние стили не сводились в полные computed styles.

CSS не создаёт документы, не меняет значения полей и не запускает сохранение/игровые действия. Размещение, hover и видимость отделены от JS управления. Файл прочитан целиком: 96 логических строк; переводы строк LF, есть завершающий newline.

## Проверки и доказательства

Группы 06/08–10: PostCSS перечислил все 17 rule-узлов и 35 declarations; настоящий partial с категоризацией отрисовал четыре заголовка, строку, p вместо h4 и invisible description. suppressed скрывает строку только при наличии @root.actor. Настоящий Actor-toggle переключил invisible для текста, для пустого текста не переключил. DOM/jQuery и данные эффектов — фасады; CSS hover и геометрия браузером не проверены.

Методика — [журнал TASK-0003.047](../../review-log.md#task-0003047). Использованы PostCSS8.5.12, Handlebars4.7.9 и parse5 из существующих зависимостей Foundry14.367.0. Разбор CSS AST подтверждает структуру, не принятие каждого значения браузером или итоговое computed style.

## Непроверенные участки и открытые вопросы

Полностью прочитаны все правила; непрочитанных частей файла нет. Не запускались мир, браузер, HTTP-загрузка, вычисление раскладки, смена темы, масштабирование и внешние модули. Размеры/цвета из declarations не объявлены измеренными пикселями интерфейса. Изменение оформления и удаление правил не согласовывались.

## Связанные проблемы

[56](../../../../issues/potential/issue-00056.md) уточнена: описание Item скрывает общий .invisible; данный CSS не добавляет отсутствующий listener. [54](../../../../issues/potential/issue-00054.md) относится к соседнему списку травм, не к повторной отрисовке эффектов. Новых issues нет.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003047) |
