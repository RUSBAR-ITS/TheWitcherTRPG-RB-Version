# styles/race-sheet.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/race-sheet.css](../../../../../styles/race-sheet.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.047](../../../../tasks/task-0003.047.md), 10 файлов / 661 логических строк; данный файл — 3 |
| Запись перекрёстной сверки | [TASK-0003.047](../../review-log.md#task-0003047) |

## Назначение файла

Задаёт высоту 150px содержимому редактора внутри расовой особенности; применяется также в расовом блоке Character.

## Условия использования

Прямой @import в [styles/witcher-styles.css](../../../../../styles/witcher-styles.css):13. Единственный глобальный селектор — .perk .editor-content, без ограничения классом Item/race или конкретным окном.

## Введённые сущности и действия с ними

Устанавливает height150px на вложенный editor-content, не на весь .perk и не на внешний .editor. Не задаёт min/max-height, overflow, редактируемость, число особенностей или ActiveEffect. Отсутствие буквального editor-content в HBS не означает отсутствие потребителя: класс генерируется ядром.

Ниже перечислены все 1 rule-узла и 1 declarations. Внешняя вложенность читается слева направо; списки селекторов на каждом уровне сохраняются. Дочерний селектор без & означает потомка, а не новый глобальный селектор. Директив @import/@keyframes внутри файла нет.

| Строка | Внешняя вложенность | Селектор / шаг | Свойства |
| --- | --- | --- | --- |
| 1 | Корень | `.perk .editor-content` | `height: 150px` |

## Основные функции и методы

JavaScript-функций и обработчиков нет. Файл объявляет CSS-правила, применяемые браузером к совпавшей разметке; вычисления свойств и псевдосостояний выполняет внешний CSS engine. 

## Используемые сущности и зависимости

| Сущность | Файл-источник | Вид / цель связи |
| --- | --- | --- |
| .perk / formGroup | [templates/sheets/item/race-sheet.hbs](../../../../../templates/sheets/item/race-sheet.hbs) | Четыре особенности; текущие поля prose-mirror |
| PARTS.main | [module/item/sheets/WitcherRaceSheet.js](../../../../../module/item/sheets/WitcherRaceSheet.js) | Подключает race-sheet.hbs; ширина 600 в JS |
| .perk / editor | [templates/partials/character/tab-profession.hbs](../../../../../templates/partials/character/tab-profession.hbs) | Четыре описания расы на текущем Character с legacy editor helper |
| .perk margin | [styles/system-styles.css](../../../../../styles/system-styles.css) | margin5px, применяется к внешнему контейнеру |
| Заголовок особенности | [styles/character/tab-profession.css](../../../../../styles/character/tab-profession.css) | В активной вкладке Actor задаёт h3; другое свойство/элемент |

Входной ресурс [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) зарегистрирован в [system.json](../../../../../system.json); эти соседи проверены в пределах подключения, их полные карточки здесь не создаются. Найденный локальный файл и строка @import не доказывают доступ по HTTP для службы Foundry.

## Известные потребители

[templates/sheets/item/race-sheet.hbs](../../../../../templates/sheets/item/race-sheet.hbs) и [templates/partials/character/tab-profession.hbs](../../../../../templates/partials/character/tab-profession.hbs) создают .perk. Foundry14.367.0 HTMLProseMirrorElement._buildElements (/opt/foundryvtt/client/applications/elements/prosemirror-editor.mjs:143–158) добавляет .editor родителю и div.editor-content внутри; настоящий метод исполнен отдельно. Обёртки formGroup/formInput в тестовом HBS заменены, поэтому факт динамического класса подтверждается отдельной проверкой ядра, не самим фасадом helper.

Область поиска: все templates/module/styles текущего среза, имена полей/классов в динамических producer и указанные методы ядра. Имена файлов и упоминания в комментариях отделены от создания HTML. Содержимое миров, внешние расширения и пользовательский enriched HTML не обследованы.

## Данные и изменения состояния

[styles/system-styles.css](../../../../../styles/system-styles.css) задаёт margin .perk, [styles/character/tab-profession.css](../../../../../styles/character/tab-profession.css) — размеры h3. Они не переопределяют height editor-content напрямую. Размер внешнего редактора из иных правил и внутренние стили Foundry могут влиять на итоговый размер/прокрутку; computed styles не снимались. Никаких @keyframes, состояний, CSS-переменных или URL.

CSS не создаёт документы, не меняет значения полей и не запускает сохранение/игровые действия. Размещение, hover и видимость отделены от JS управления. Файл прочитан целиком: 3 логических строк; переводы строк LF, нет завершающего newline.

## Проверки и доказательства

Группы 06/14–15: один rule/одна declaration; HBS Item создаёт четыре .perk/prose-mirror, Character четыре .perk с тестовым legacy editor. Настоящий HTMLProseMirrorElement на фасаде базового элемента создал editor-content и кнопку toggle, добавил editor/prosemirror/inactive. Редактор ProseMirror не активировался, документ не сохранялся.

Методика — [журнал TASK-0003.047](../../review-log.md#task-0003047). Использованы PostCSS8.5.12, Handlebars4.7.9 и parse5 из существующих зависимостей Foundry14.367.0. Разбор CSS AST подтверждает структуру, не принятие каждого значения браузером или итоговое computed style.

## Непроверенные участки и открытые вопросы

Полностью прочитаны все правила; непрочитанных частей файла нет. Не запускались мир, браузер, HTTP-загрузка, вычисление раскладки, смена темы, масштабирование и внешние модули. Размеры/цвета из declarations не объявлены измеренными пикселями интерфейса. Изменение оформления и удаление правил не согласовывались.

## Связанные проблемы

Новых проблем не зарегистрировано. Связанные с обогащением текста вопросы относятся к [109](../../../../issues/potential/issue-00109.md), а не к этой высоте; заново весь путь enrichedText не проверялся.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 2f94c6c29e298ccf73d67ccc2e5fb8fc358dae2c; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003047) |
