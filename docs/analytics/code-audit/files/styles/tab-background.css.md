# styles/tab-background.css

| Поле | Значение |
| --- | --- |
| Исходный файл | [styles/tab-background.css](../../../../../styles/tab-background.css) |
| Тип файла | CSS |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.049](../../../../tasks/task-0003.049.md), 13 файлов / 2178 логических строк; данный файл — 172 |
| Запись перекрёстной сверки | [TASK-0003.049](../../review-log.md#task-0003049) |

## Назначение файла

Общие стили биографии, событий жизни, заметок и редакторов; часть правил применяется вне вкладки персонажа.

## Условия использования

Импорт 6, после system-styles.css и monster-sheet.css. Нет корневого .witcher или .background у большинства правил. Внутренний div.tab.body.background не имеет data-tab; найденное правило ядра .tab[data-tab]:not(.active) не скрывает его автоматически. Высота редактора, прокрутка и фактическая доступность полей зависят также от ядра и формы.

## Введённые сущности и действия с ними

Файл не вводит JS-классы, функции, поля модели или обработчики. Определены 28 CSS rule-узлов и 76 declarations; таблица охватывает файл полностью. Пустой внешний rule-узел может задавать область вложенных правил. Стрелка → обозначает вложенность CSS, а не дополнительный элемент HTML; список через запятую остаётся на своём уровне.

| Строка | Внешняя область | Селектор | Все объявления свойств |
| --- | --- | --- | --- |
| 1 | Корень | `.editor` | `border-radius: 5px`; `background: light-dark(#22222210, #e7d1b110)`; `height: 250px`; `padding: 5px` |
| 8 | Корень | `.tox.tox-tinymce` | `min-height: 200px`; `min-width: 200px` |
| 13 | Корень | `.life-events, .character-notes` | `display: grid`; `grid-template-columns: 1fr 1fr 1fr`; `gap: 10px` |
| 19 | Корень | `.life-events-header, .notes-header` | `display: flex`; `justify-content: space-between`; `align-items: center`; `padding: 5px`; `border-radius: 5px`; `background-color: rgba(0, 0, 0, 0.05)`; `border: 1px solid darkgray`; `margin-top: 20px`; `margin-bottom: 5px` |
| 30 | `.life-events-header, .notes-header` | `span` | `font-size: 24px` |
| 35 | Корень | `.life-events-card` | `border-radius: 5px`; `background-color: rgba(0, 0, 0, 0.05)`; `border: 1px solid darkgray` |
| 41 | Корень | `.life-events-header > h2, .notes-header > h2` | `margin: 0`; `border-bottom: none`; `opacity: 0.8` |
| 47 | Корень | `.life-events-card-header` | `display: grid`; `grid-template-columns: 10% 80% 10%`; `padding: 8px 4px`; `align-items: center` |
| 53 | `.life-events-card-header` | `span` | `font-size: 18px` |
| 58 | Корень | `.padding` | `padding: 5px 10px` |
| 62 | Корень | `.life-events-controls` | `justify-self: center` |
| 66 | Корень | `.life-events-decades` | `display: flex`; `text-align: end` |
| 71 | Корень | `.add-item` | `margin-right: 5px` |
| 75 | Корень | `.bg-note` | `display: flex`; `flex-direction: column`; `gap: 5px`; `border-radius: 5px`; `padding: 5px`; `background-color: rgba(0, 0, 0, 0.05)`; `border: 1px solid darkgray` |
| 85 | Корень | `.note-header` | `display: flex`; `flex-direction: row` |
| 90 | Корень | `.note-header > a` | `display: none` |
| 94 | Корень | `.note-header:hover > a` | `display: inline-block`; `text-align: center`; `text-shadow: none`; `color: #d02323` |
| 101 | Корень | `.item-delete` | `margin: 5px`; `width: 15px` |
| 106 | Корень | `.modifier-display` | `min-width: 100px` |
| 110 | Корень | `.background-info` | `display: flex`; `flex-direction: column`; `gap: 20px` |
| 116 | Корень | `.general-section` | `display: grid`; `grid-template-columns: 1fr 1fr 1fr`; `gap: 10px` |
| 122 | Корень | `.general-homeland, .general-info` | `display: flex`; `flex-direction: column`; `gap: 5px`; `padding: 10px`; `border-radius: 10px`; `background-color: light-dark(#22222210, #e7d1b110)`; `border: 1px solid light-dark(#22222240, #e7d1b140)` |
| 132 | Корень | `.homeland-select` | `display: flex`; `gap: 5px` |
| 137 | Корень | `.background-description` | `overflow-y: auto` |
| 141 | Корень | `textarea.life-events-details, textarea.inline-edit` | `resize: vertical`; `height: auto` |
| 147 | Корень | `input.life-events-decades` | `width: 4ch`; `text-align: center` |
| 152 | Корень | `input.details, select.details, input.life-events-details, textarea.life-events-details, input.life-events-decades, textarea.inline-edit, input.inline-edit` | `border: none`; `transition: box-shadow 0.1s ease`; `flex-grow: 1` |
| 164 | Корень | `input.details:hover, select.details:hover, input.life-events-details:hover, textarea.life-events-details:hover, input.life-events-decades:hover, textarea.inline-edit:hover, input.inline-edit:hover` | `box-shadow: 0 0 5px var(--color-shadow-primary)` |

## Основные функции и методы

JavaScript-функций нет. Сопоставление селекторов, каскад и отрисовку выполняет браузер.

`.life-events` и `.character-notes` создают три колонки; заголовки и карточки получают фон, рамку и отступы. Состояние события задаёт HBS: `isOpened` меняет текст на input и добавляет textarea, CSS лишь оформляет существующие узлы. `lifeEventCounter` и eachLimit определяют число карточек, а не grid. `.general-section` также имеет три колонки; `.background-info` располагает общие сведения и редактор вертикально.

`.note-header > a` скрывает удаление старой Item-заметки до hover. Новые заметки массива system.notes и заметки монстра имеют `.flex` вместо `.note-header`: это правило к их кнопкам не относится. `.bg-note`, `.inline-edit`, `.item-delete`, `.add-item` остаются общими. CSS не даёт права на удаление и не проверяет editable.

Глобальная `.editor` задаёт высоту 250px и фон всем совпадающим редакторам. Это не только буквальная разметка HBS: Foundry создаёт `.editor` и `.editor-content` в HTMLProseMirrorElement._buildElements; старый helper editor и текущий formGroup — разные пути создания. `.tox.tox-tinymce` относится к прежнему редактору; текущая установка использует ProseMirror. `.padding` и `.modifier-display` — самостоятельные глобальные утилиты, без доказанного текущего потребителя в module/templates.

Последние правила меняют размеры textarea и бордер/тень полей details, life-events-details и inline-edit, включая hover. `.life-events-decades` присутствует и на span, и на input; ширина 4ch ограничена input.

## Используемые сущности и зависимости

| Файл-источник | Сущность | Вид связи, место и цель | Основание |
| --- | --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Прямое подключение; номер импорта 6 (счёт импортов, не строка файла). | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [system.json](../../../../../system.json) | styles | Манифест подключает master stylesheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/partials/character/tab-background.hbs](../../../../../templates/partials/character/tab-background.hbs) | background-info, general-section, life-events*, note-header, bg-note | Текущий PARTS.background персонажа; события, старые и новые заметки, formGroup/editor. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) | bg-note, inline-edit, item-delete, add-item | Текущая вложенная вкладка notes монстра; без note-header. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../module/actor/sheets/WitcherCharacterSheet.js) | PARTS.background; _prepareContext | Подключение HBS и подготовка массива событий; источник контекста, не вызов CSS. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/mixins/noteMixin.js](../../../../../module/actor/sheets/mixins/noteMixin.js) | noteListener, _onNoteAdd, _onNoteDelete | Действия массива заметок; события жизни обрабатываются отдельно в WitcherActorSheet. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../module/actor/sheets/mixins/itemMixin.js) | itemListener, _onItemInlineEdit, _onItemDelete | Изменение старых Item-заметок через классы inline-edit/item-delete. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/system-styles.css](../../../../../styles/system-styles.css) | .item-delete, .invisible | Более ранние глобальные правила; item-delete здесь повторяет размеры. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [styles/character/tab-profession.css](../../../../../styles/character/tab-profession.css) | .editor-content | Соседние правила редакторов; одинаковое имя editor не ограничивает вкладкой background. | Исходники и сопоставление с полным AST; специальные проверки ниже |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../module/actor/sheets/WitcherActorSheet.js) | activateListeners, _onLifeEventDisplay | Переключение состояния события. | Исходники и сопоставление с полным AST; специальные проверки ниже |

Внешние определения: Foundry VTT 14.367.0, `client/applications/api/application.mjs` — _prepareTabs, _initializeApplicationOptions и #mergeApplicationOptions; `public/css/foundry2.css` — общие классы/темы и .tab[data-tab]:not(.active). ApplicationV2 создаёт .application/.window-content. Состояния hover/checked/open и vendor-псевдоэлементы принадлежат браузеру. CSS читает переменные темы: `--color-shadow-primary`. Их значений файл не объявляет. Установленное ядро — внешний источник, отдельная карточка в реестр системы не добавляется.

## Известные потребители

| Файл-потребитель | Сопоставляемые сущности | Условия и способ |
| --- | --- | --- |
| [styles/witcher-styles.css](../../../../../styles/witcher-styles.css) | @import | Загружает весь CSS один раз |
| [templates/partials/character/tab-background.hbs](../../../../../templates/partials/character/tab-background.hbs) | background-info, general-section, life-events*, note-header, bg-note | Текущий PARTS.background персонажа; события, старые и новые заметки, formGroup/editor. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) | bg-note, inline-edit, item-delete, add-item | Текущая вложенная вкладка notes монстра; без note-header. |

Корневые классы и выбор PARTS перечислены в таблице зависимостей. JS-обработчик класса — связь с состоянием/действием, а не вызов CSS-функции. Для правил .tab/window-content набор текущих вкладок задаётся PARTS указанных листов, включая вложенную навигацию. У старого HBS наличие класса не подтверждает текущую регистрацию. Поиск проведён в module/, templates/ и styles/; совпадения полей/имён исключались вручную, динамические классы проверены по producer и ядру. Внешние темы, модули, enriched HTML пользователя и макросы мира в область поиска не входят.

## Данные и изменения состояния

CSS не читает Actor/Item напрямую и не выполняет update/create/delete. Вход — DOM-классы, атрибуты, структура и псевдосостояния. Наличие/доступность полей и методы изменения данных задаются HBS, DocumentSheet и системными обработчиками. Цвет, скрытие или курсор не являются проверкой прав и не заменяют игровое правило.

## Проверки и доказательства

| Проверка | Сценарий / источник | Фактический результат | Предел |
| --- | --- | --- | --- |
| Полный файл | Чтение 172 логических строк и PostCSS 8.5.12 | 28 rule-узлов, 76 declarations; все scopes и свойства перечислены | AST не подтверждает семантическую допустимость CSS |
| Потребители и состояния | Настоящие HBS, системные helpers, указанные методы и статические контексты | Группы 5/6/15: две карточки событий, открытая с input/textarea; две заметки с разными контролами; настоящий _buildElements ProseMirror создаёт классы редактора. В HBS-прогоне содержимое formGroup/editor заменено маркером и не использовано как доказательство DOM ядра. | Handlebars 4.7.9/parse5 без браузерной раскладки |
| Каскад и регистрация | system.json, master, DEFAULT_OPTIONS/PARTS, соседние CSS | Импорт 6, после system-styles.css и monster-sheet.css. Нет корневого .witcher или .background у большинства правил. Внутренний div.tab.body.background не имеет data-tab; найденное правило ядра .tab[data-tab]:not(.active) не скрывает его автоматически. Высота редактора, прокрутка и фактическая доступность полей зависят также от ядра и формы. | Итоговые computed styles/размеры не измерялись |

Методика и результаты — [журнал TASK-0003.049](../../review-log.md#task-0003049). Изолированные сценарии выполнены через Node 24.16.0 из stdin, без файлов стенда. DOM, запись и редакторные formGroup/editor в HBS представлены явно ограниченными фасадами; отдельно выполнен настоящий ProseMirror _buildElements с фасадом базового элемента. Системные игровые расчёты этим прогоном не проверяются.

## Непроверенные участки и открытые вопросы

Непрочитанных частей файла нет. Не проверены реальная отрисовка, нативное переключение details, hover/focus, keyboard/touch, размеры окна, переполнение, computedStyle, поддержка vendor-элементов, вложенности/light-dark в конкретном браузере и сторонние темы. Для отмеченных старых/неустановленных потребителей нужен фактический сценарий подключения, прежде чем удалять либо исправлять CSS. HTTP системы, мир и БД не запускались; доступ службы и игровые записи не проверялись.

## Связанные проблемы

[issue-00024](../../../../issues/potential/issue-00024.md), [issue-00057](../../../../issues/potential/issue-00057.md), [issue-00211](../../../../issues/potential/issue-00211.md), [issue-00212](../../../../issues/potential/issue-00212.md), [issue-00213](../../../../issues/potential/issue-00213.md), [issue-00153](../../../../issues/potential/issue-00153.md). Связь с конкретным условием, шаблоном или каскадом описана выше. Статусы остаются potential; CSS-анализ не подтверждает исправление или закрытие.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 523c9b2616e19058b18f812ae0361c8a86366814; полный файл | Первичная карточка; [перекрёстная сверка](../../review-log.md#task-0003049) |
