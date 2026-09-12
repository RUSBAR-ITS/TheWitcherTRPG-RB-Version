# templates/partials/character/tab-background.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/character/tab-background.hbs](../../../../../../../templates/partials/character/tab-background.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `12055fee62f01c6de49967044aedef9d7cfe0632` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.033](../../../../../../tasks/task-0003.033.md), 4 файла, 178 логических строк |
| Запись перекрёстной сверки | [TASK-0003.033](../../../../review-log.md#task-0003033) |

## Назначение файла

Текущая вкладка биографии персонажа: родина, семь описательных полей, пол/возраст/положение, богатое описание, жизненные события и два вида заметок.

## Условия использования

Выбирается WitcherCharacterSheet.PARTS.background, tab primary/background; предзагружается setup/handlebars. Внешний section использует tabs.background.cssClass. Работает с контекстом V2, включая notes/oldNotes, homeland и enrichedText. Наличие V1 методов заметок не означает, что V1 получает данный шаблон и его контекст.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| primary/background; .background-info | Разметка; 1–54 | Основные сведения | PARTS.background | Имя вкладки фиксировано; программных функций нет |
| system.general.homeland.value / otherValue | 9–15 и 18–25 | Редактор родины при отсутствии homeland Item | select/input либо только label | Item-родина скрывает Actor-редакторы; значение 'other' раскрывает дополнительный текст |
| system.general.details.<dt>.value; system.gender; system.general.age; system.general.socialStanding | 27–49 | Семь описательных полей и три общих | input/select | details.label динамически локализуется; age number с data-dtype=Number |
| system.general.background.value | 52: formGroup | Богатое описание | enrichedText.general.background.{systemField,value,enriched} | Передаёт корректные raw/enriched значения; toggled=true |
| system.lifeEventCounter; eachLimit; lifeEvent.key/value/details/isOpened | 56–98 | Первые N событий | counter number min=1,max=20; .life-event-display | Открытые: input/textarea; закрытые: значение span; data-event берётся из lifeEvent.key |
| oldNotes: Item.note | 105–117 | Старые заметки-предметы | data-item-id, .inline-edit, .item-delete | Имя/описание без name, используются data-field=name/system.description |
| notes: Actor.system.notes | 118–125 | Массив title/details | input name=system.notes.<@index>.title; editor target=system.notes.<@index>.details | Удаление .delete-note / data-note-index; editor button=true |
| .add-item / data-itemType=note | 103 | Создать новую Item-note | itemMixin._onItemAdd | HTML нормализует атрибут data-itemtype; dataset.itemtype совпадает с handler |

## Основные функции и методы

JS-функций и экспортов нет. Условия if/unless выбирают родину и раскрытые события; each перебирает детали/заметки, eachLimit — события. Helpers localize, selectOptions, eq, lookup, formGroup, editor и concat читают контекст и формируют HTML. Шаблон не вызывает Actor.update сам.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherCharacterSheet._prepareContext / _prepareCharacterData | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | контекст; PARTS; TABS | background:59–62; lifeEvents:133–137; homeland:155; enrichedText | Полный текущий контекст использован в проверках |
| _prepareGeneralInformation / _onLifeEventDisplay | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | контекст и обработчики | oldNotes=getList('note'), notes=system.notes; click по data-event | V2 передаёт system ссылкой; toggle ищет lifeEvent.key через find |
| getList | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | чтение Items | oldNotes/homeland: фильтр типа, !isStored, сортировка sort | Смешанный набор подтвердил исключение stored Item |
| CharacterData; gender/lifeEventCounter; enrichedText | [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js) | схема и обогащение | gender:StringField; counter:NumberField(initial20); background | Schema counter не задаёт min/max; это атрибуты HTML |
| general; details; homeland; background | [module/data/actor/templates/character/generalData.js](../../../../../../../module/data/actor/templates/character/generalData.js); [module/data/actor/templates/character/general/detailsData.js](../../../../../../../module/data/actor/templates/character/general/detailsData.js); [module/data/actor/templates/character/general/homelandData.js](../../../../../../../module/data/actor/templates/character/general/homelandData.js); [module/data/actor/templates/character/general/backgroundData.js](../../../../../../../module/data/actor/templates/character/general/backgroundData.js) | определения полей | 7 details с value/label; homeland value/otherValue; background.value HTMLField; age/socialStanding | Поля сверены с формой и updateSource |
| lifeEvents / lifeEvent | [module/data/actor/templates/character/general/lifeEventsData.js](../../../../../../../module/data/actor/templates/character/general/lifeEventsData.js); [module/data/actor/templates/character/general/lifeEventData.js](../../../../../../../module/data/actor/templates/character/general/lifeEventData.js) | схема | 20 ключей 10–200; decade/value/details/isOpened | key не является полем схемы, добавляется подготовкой листа |
| notes / note() | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/noteData.js](../../../../../../../module/data/actor/templates/common/noteData.js) | схема | title/details StringField в массиве | Чтение, indexed form и переиндексация после удаления |
| NoteData | [module/data/item/noteData.js](../../../../../../../module/data/item/noteData.js) | модель Item.note | Описание oldNotes | {{system.description}} внутри each читает именно Item.system |
| HomelandData | [module/data/item/homelandData.js](../../../../../../../module/data/item/homelandData.js) | модель Item.homeland | homeland.system.value/otherValue | Изолированный контекст со своей Item-родиной |
| createEnrichedText | [module/data/dataUtils.js](../../../../../../../module/data/dataUtils.js) | вызов через CharacterData | background.value → {systemField,value,enriched} | Содержание raw и enriched различалось, formGroup получил оба правильно |
| WITCHER.homelands / socialStanding | [module/setup/config.js](../../../../../../../module/setup/config.js) | варианты select и lookup | 9–24,46–47 | Вместе с details.label и прямыми ключами проверены 45 локализаций |
| eachLimit / eq; preloadHandlebarsTemplates | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | регистрация helpers и шаблона | 12,21,66–95 | eachLimit не ограничивает N длиной коллекции; @key и lifeEvent.key различаются |
| _onItemAdd / _onItemInlineEdit / _onItemDelete / itemListener | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | события Item | 103–115; изменение description/name по Item ID | Создание ожидается, inline возвращает update, delete не ждёт запись |
| _onNoteDelete / noteListener | [module/actor/sheets/mixins/noteMixin.js](../../../../../../../module/actor/sheets/mixins/noteMixin.js) | события массива | 121 | Индекс @index; текущей кнопки .add-note нет |
| formGroup/editor/selectOptions/localize/concat/lookup | Foundry 14.367.0 и Handlebars 4.7.9 | внешние helpers | 52,123 и общие поля | formGroup/editor/selectOptions выполнялись из ядра; DOM-input/editor заменены фасадами |
| Переводы | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | локализация | Шесть прямых ключей, config и labels | 45 уникальных ключей существуют в обоих языках после expandObject |
| .life-events / .character-notes / .bg-note / .background-info | [styles/tab-background.css](../../../../../../../styles/tab-background.css) | стили | Сетка карточек/заметок, раскрытие кнопки удаления, блоки сведений | Селекторы прочитаны; CSS и внешний вид не засчитаны в покрытие |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Весь HBS | PARTS.background:59–62 | Актуальный системный потребитель |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Путь шаблона | preloadHandlebarsTemplates:12 | Предзагрузка, отдельная от выбора PARTS |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Actor-форма пишет пути general.homeland, general.details, gender, general.age/socialStanding, general.background.value, lifeEventCounter и открытые general.lifeEvents.<key>.value/details; title/details массива заметок используют индекс. Закрытые события не отправляют свои скрытые поля — прежние details сохраняются при частичном updateSource. Кнопка life-event-display отдельно изменяет isOpened, без удаления события. Уменьшение counter ограничивает вывод, а не удаляет записи.

oldNotes не являются форм-полями Actor: inline-edit использует Item ID и data-field. Значение {{system.description}} находится в контексте each oldNotes и корректно относится к заметке. Заголовки, inputs и textarea экранируются Handlebars. Для notes.details вызывается core editor с исходной строкой, engine=prosemirror, editable=true и collaborate=false по умолчанию; явного enrichHTML для массива нет. Для general.background передаются raw value и обогащённое enriched.

При повторной подготовке lifeEvent.key остаётся 10/20 и т. д., но массив записывается в prepared-модель вместо объекта схемы (issue-00024). Обычный HTML counter задаёт 1–20. Программный counter=21 создаёт 21-ю пустую карточку с data-event='', toggle которой вызывает TypeError; counter=0 заменяется на длину (20), -1 не выводит карточек, 1.5 выводит две. Нативная валидация браузера для этих входов не проверена.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Смешанные заметки/экранирование | Группы 06–07 | Stored Item скрыт, оба формата независимы; inline принимает HTML как строку, false/true изменяет общий handler | Нет настоящего Item.create/update/delete |
| Родина и описание | Группа 09 | Item-родина скрывает select; 7 details inputs; background получает правильные raw/enriched | enrichHTML и создание custom element подменены |
| События | Группы 10–11,13 | 20 ключей модели; открытие/закрытие, повторный контекст, unknown key и программные границы counter | Не игровой генератор биографии |
| Форма и переиндексация | Группы 12–13 | Изменены notes.1.*, затем удаление даёт notes.0.*; event10 сохраняет value, скрытый event20 сохраняет details | FormDataExtended/_processFormData настоящие; DOM и редакторные значения заданы фасадом |
| Локализация | Группа 15 | 45 уникальных ключей найдены в en и ru | Другие языки и клиентский UI не проверены |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Проверки выполнены в Node 24.16.0 с кодом Foundry 14.367.0, без мира, браузера, HTTP и записи в БД. Модели, методы системы, Handlebars и перечисленные в журнале функции ядра настоящие; Application/DOM и документные операции заменены фасадами. Сохранение через updateSource проверяет модель в памяти и не доказывает серверную запись, разрешение конфликтов или работу ProseMirror в браузере. Генераторы биографии в packsJson, редактирование действующих заметок мира, обновление нескольких открытых окон и безопасность произвольного HTML не исследованы. Проверена передача значений редактору, но не его DOM-жизненный цикл.

## Связанные проблемы

[issue-00024](../../../../../../issues/potential/issue-00024.md), [issue-00153](../../../../../../issues/potential/issue-00153.md), [issue-00211](../../../../../../issues/potential/issue-00211.md), [issue-00212](../../../../../../issues/potential/issue-00212.md), [issue-00213](../../../../../../issues/potential/issue-00213.md). Старый note-sheet не используется этой вкладкой; его отсутствие в PARTS не мешает встроенным полям oldNotes.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `12055fee62f01c6de49967044aedef9d7cfe0632`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003033) |

## Дополнительная сверка TASK-0003.049

2026-09-12, rusbar-main, 523c9b2616e19058b18f812ae0361c8a86366814. Исходный файл не изменён.

Полностью разобран tab-background.css. Сетки general-section/life-events/character-notes имеют три колонки. Hover-скрытие .note-header > a касается только старых Item-заметок этого HBS: новые используют .flex, как и заметки монстра. Глобальная .editor относится и к DOM, создаваемому ядром; настоящий HTMLProseMirrorElement._buildElements отдельно подтвердил editor/editor-content с фасадом базового элемента. В HBS-проверке formGroup/editor заменены маркерами. Внутренний div.tab.body.background без data-tab не совпадает с .tab[data-tab]:not(.active) из ядра.

Карточки CSS: [styles/tab-background.css](../../../styles/tab-background.css.md).

[Методика и результаты](../../../../review-log.md#task-0003049). Соседний файл повторно в покрытие не включён; браузер и БД не запускались.

## Уточнение TASK-0003.053

2026-09-12, rusbar-main, 93beea0953821c9d8f080f815e686dc4da0c6f9e; исходник не изменён.

Повторно прочитаны строки 57–95 вместе с lifeEventData/lifeEventsData и подготовкой массива в WitcherCharacterSheet: форма читает и редактирует value/details/isOpened по ключам 10…200. RollTable draw или перенос из 21 таблицы lifepath здесь не вызывается. Самостоятельно разыгранное жизненное событие может служить материалом для ввода пользователем; автоматическая запись/интерпретация описанного бонуса не обнаружена. Обработчики формы повторно не исполнялись.

[21 карточка lifepath](../../../README.md#таблицы-жизненных-событий--task-0003053), [перекрёстная сверка и пределы проверки](../../../../review-log.md#task-0003053).

## Уточнение TASK-0003.054

2026-09-12, rusbar-main, 63e9a79fefa7743fcf709b2fa19ddbe144f353a0; исходник не изменён.

Повторно сверены поля Actor.general.homeland, показ homeland Item и formGroup биографии (7–25,51–53) с 35 таблицами создания персонажа. Форма не вызывает эти RollTable и не переносит описанные родственников, вещи и бонусы в Actor автоматически. Корневые description трёх Family Status выводятся только в сообщении самих таблиц; текст биографии Actor редактируется отдельным полем. Ошибка глубины RandomCharacter (issue-00320) возникает при вложенном draw до сообщения и не вызвана этим HBS.

[35 карточек подтаблиц](../../../README.md#подтаблицы-создания-персонажа--task-0003054), [перекрёстная сверка и пределы](../../../../review-log.md#task-0003054).
