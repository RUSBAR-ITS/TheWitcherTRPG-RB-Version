# templates/chat/item/partials/item-description/crafting-items.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/chat/item/partials/item-description/crafting-items.hbs](../../../../../../../../../templates/chat/item/partials/item-description/crafting-items.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.048](../../../../../../../../tasks/task-0003.048.md), 16 файлов / 920 логических строк; данный файл — 33 |
| Запись перекрёстной сверки | [TASK-0003.048](../../../../../../review-log.md#task-0003048) |

Актуализация [issue-00001](../../../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Перечень обычных материалов и положительных алхимических требований в сообщении рецепта Item типа diagrams.

## Условия использования

Предзагружается preloadHandlebarsTemplates и включается корневым item-description.hbs без смены контекста. Самостоятельного вызова renderTemplate для этой части в module/ не найдено.

Внешний if требует type='diagrams'. Заголовок WITCHER.Diagram.components показывается при or(craftingComponents,alchemyComponents). Системный or проверяет Boolean аргументов: даже пустой массив/объект truthy; schema alchemyComponents всегда создаёт объект девяти чисел. Поэтому у пустого рецепта заголовок остаётся, но строк может не быть. each craftingComponents не фильтрует нулевое количество и выводит img/name/x/quantity внутри details > summary. Без uuid/недоступного документа модель сохраняет имя; HBS не вызывает fromUuidSync и не повторяет map листа рецепта из issue-00095. img отсутствующей записи станет пустым src, собственного fallback нет. Алхимические строки появляются только при isFormulae и gt(component,0); key задаёт PNG и Inventory.<Capitalized>. Обычные материалы выводятся независимо от isFormulae, поэтому обе группы могут присутствовать вместе. details не имеет тела за пределами summary.

## Введённые сущности и действия с ними

| Сущность | Определение / область | Действия |
| --- | --- | --- |
| HTML-фрагмент | Весь файл | Условия, текст, атрибуты и CSS-классы; нет сохранения документов |
| type | Внешний контекст Item.type | Выбор поддержанных типов |
| Пути чтения | Все буквальные обращения ниже | Готовые поля и справочники, без обновления |

Буквальные пути чтения: `component.img`, `component.name`, `component.quantity`, `item.system.alchemyComponents`, `item.system.craftingComponents`, `item.system.isFormulae`.



## Основные функции и методы

JS-функций/записи нет. each объявляет component/name для обычных материалов (name как индекс не читается) и component/key для веществ. Обе секции читают готовые значения, ничего не списывают и не проверяют наличие у Actor.

Внешние if/each/lookup — Handlebars 4.7.9; eq/or/gt/capitalize — registerHandelbarHelpers системы, localize/concat — Foundry client/applications/handlebars.mjs. Набор реально вызванных helpers определяется выражениями файла, а не всем доступным реестром. if без includeZero не показывает Number 0; стандартное {{}} экранирует текст и атрибуты.

## Используемые сущности и зависимости

| Источник | Используемая сущность | Связь и цель | Основание |
| --- | --- | --- | --- |
| [templates/chat/item/item-description.hbs](../../../../../../../../../templates/chat/item/item-description.hbs) | item/type/config | Единственное прямое включение partial, исходный контекст без hash. | Определение и место обращения сверены |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates/registerHandelbarHelpers | Предзагрузка пяти partial, системные eq/or/gt/capitalize; корень рендерится по запросу. | Определение и место обращения сверены |
| [styles/chat.css](../../../../../../../../../styles/chat.css) | chat-* и list-item-description | Общие размеры и несовпадение непосредственных потомков section. | Определение и место обращения сверены |
| [styles/tab-inventory.css](../../../../../../../../../styles/tab-inventory.css) | item-tags/item-tag, stored-item-* | Общие стили тегов и материалов. | Определение и место обращения сверены |
| [module/data/item/diagramData.js](../../../../../../../../../module/data/item/diagramData.js) | DiagramData.prepareDerivedData/enrichDiagramComponents | Заменяет доступные name/img/type в prepared-массиве; недоступную запись сохраняет. | Определение и место обращения сверены |
| [module/data/item/templates/craftingComponentData.js](../../../../../../../../../module/data/item/templates/craftingComponentData.js) | craftingComponent | id/name/quantity/uuid; img не входит в schema и добавляется при подготовке. | Определение и место обращения сверены |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | or/eq/gt/capitalize | Выбор типа, truthiness контейнеров, положительное число и заглавная буква. | Определение и место обращения сверены |
| [styles/tab-inventory.css](../../../../../../../../../styles/tab-inventory.css) | stored-item-img/stored-item-label | Размер 30×30 и flex-summary; общий стиль не ограничен инвентарём. | Определение и место обращения сверены |

Локализация: [lang/ru.json](../../../../../../../../../lang/ru.json) и [lang/en.json](../../../../../../../../../lang/en.json); настоящий Localization 14.367.0 с expandObject и en fallback. Иконки Font Awesome и обрамление сообщения предоставляет клиент Foundry. Ресурсы assets и внешний клиент не получают карточек этого аудита.

## Известные потребители

| Потребитель | Использование | Условия / основание |
| --- | --- | --- |
| [templates/chat/item/item-description.hbs](../../../../../../../../../templates/chat/item/item-description.hbs) | partial-включение | Без hash/with, полный контекст item/type/config |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и регистрация partial отдельно от фактического показа |

Область поиска — module/ и templates/ текущего checkout. Макросы миров, внешние модули и подменённые шаблоны не проверялись.

## Данные и изменения состояния

Шаблон создаёт HTML-строку, не модифицирует предмет или Actor. Producer передаёт подготовленную модель Item, а не результат сериализации. Имя и img принадлежат Document, system-поля — моделям системы. Сам HBS не обогащает HTML: markup экранируется. После создания стандартного сообщения ядро ChatMessage.renderHTML вызывает TextEditor.enrichHTML (client/documents/chat-message.mjs:414), поэтому сохранённый @UUID/inline roll нельзя объявлять навсегда простым текстом только по первому рендеру. Полный последующий enrichment в браузере здесь не исполнялся.

## Проверки и доказательства

| Что | Метод / источник | Результат | Предел |
| --- | --- | --- | --- |
| Полнота | 33 строк исходного HBS | Все ветви, пути чтения и helpers описаны | Соседние файлы проверены только по связи |
| Рендер/модель | Настоящие Handlebars, модели и helpers | Группы 02–03, 09, 11: корректный diagrams; quantity=0 сохранено; недоступный UUID сохраняет SavedUnknown без картинки, доступный даёт ResolvedName/resolved.png. vitriol=2 показан, rebis=0/aether=-1 пропущены; пустой рецепт даёт заголовок и 0 details. Все девять PNG проверены по существованию, assets вне пофайлового анализа. | UUID/Document/чат — фасады, запись отсутствует |
| Локализация/ресурсы | en/ru expandObject, настоящий Localization; локальные файлы | 66 ключей комплекта: 65 ru, 1 отсутствует en/ru; девять PNG существуют | Другие локали/HTTP не проверены |

## Непроверенные участки и открытые вопросы

Текущая статическая сверка завершена; прежние пофайловые опыты сохраняют свои даты и фасады. Тип diagrams и prepared UUID-компоненты подтверждены DiagramData. quantity ?? 1 сохраняет 0; алхимия требует isFormulae/gt 0 и строит динамический key/PNG. Компонент с недоступным UUID остаётся исходной записью. Непроверенные границы и следующий критерий: [U016-06](../../../../../../cross-check-0002.md#u016-06), [U016-07](../../../../../../cross-check-0002.md#u016-07). Полный браузерный цикл, мир, HTTP и запись в БД не выполнялись; смысл перевода/игровых правил не оценивался.

## Связанные проблемы

[docs/issues/potential/issue-00308.md](../../../../../../../../issues/potential/issue-00308.md). Наблюдения остаются potential; подтверждения и исправления не выполнялись.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | ee24c2605f4db98fad1ff6db024d2b0c26883670; полный файл | Первичная карточка; [перекрёстная сверка](../../../../../../review-log.md#task-0003048) |

## Сквозная сверка TASK-0004.016

2026-09-14; rusbar-main, 0588289c84d955201457f44ec2f8152a9258135e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Тип diagrams и prepared UUID-компоненты подтверждены DiagramData. quantity ?? 1 сохраняет 0; алхимия требует isFormulae/gt 0 и строит динамический key/PNG. Компонент с недоступным UUID остаётся исходной записью.

Сопоставленные определения и потребители: [module/actor/sheets/mixins/itemMixin.js](../../../../../module/actor/sheets/mixins/itemMixin.js.md), [module/setup/handlebars.js](../../../../../module/setup/handlebars.js.md), [module/data/item/diagramData.js](../../../../../module/data/item/diagramData.js.md), [module/data/item/templates/craftingComponentData.js](../../../../../module/data/item/templates/craftingComponentData.js.md), [templates/partials/character/substances.hbs](../../../../partials/character/substances.hbs.md), [module/setup/config.js](../../../../../module/setup/config.js.md), [module/scripts/chat.js](../../../../../module/scripts/chat.js.md), [module/actor/mixins/currencyConverterMixin.js](../../../../../module/actor/mixins/currencyConverterMixin.js.md), [module/data/item/templates/combat/attackOptionsData.js](../../../../../module/data/item/templates/combat/attackOptionsData.js.md), [module/activeEffect/mixins/baseMixin.js](../../../../../module/activeEffect/mixins/baseMixin.js.md).

[Протокол и границы](../../../../../../review-log.md#task-0004016) — TASK-0004.016; процессы [R016-02](../../../../../../cross-check-0002.md#r016-02), [R016-04](../../../../../../cross-check-0002.md#r016-04), [R016-21](../../../../../../cross-check-0002.md#r016-21). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
