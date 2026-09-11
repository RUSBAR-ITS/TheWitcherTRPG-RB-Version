# templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `8b938d44a042749df027d8b58e28bb1d79638091` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.032](../../../../../../../../../../tasks/task-0003.032.md), 13 файлов, 973 логические строки |
| Запись перекрёстной сверки | [TASK-0003.032](../../../../../../../../review-log.md#task-0003032) |

## Назначение файла

Показывает два вида заметок монстра: старые embedded Item type note и записи массива system.notes. Добавление в заголовке создаёт Item; удаление массива выполняет noteMixin. Все 22 строки прочитаны.

## Условия использования

Текущий tab-details.notes и предзагрузка. oldNotes/notes подготавливает базовый _prepareGeneralInformation.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| .add-item | 2 | Создать старый Item-note | data-itemType='note' | В HTML dataset имя становится itemtype; itemMixin._onItemAdd |
| each oldNotes | 4–12 | Item заметки | data-item-id=note._id; .inline-edit name/system.description | textarea читает system.description текущего each-контекста Item, не корневого Actor |
| each notes | 13–21 | Заметки массива | system.notes.<index>.title/details | title input, editor details, delete-note с index; .add-note в файле нет |

## Основные функции и методы

Программных функций и экспортов нет. Ниже описаны поля/условия разметки и их контракт с моделями и обработчиками; собственной записи документа файл не выполняет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| MonsterData и CommonActorData | [module/data/actor/monsterData.js](../../../../../../../../../../../module/data/actor/monsterData.js); [module/data/actor/commonActorData.js](../../../../../../../../../../../module/data/actor/commonActorData.js) | модель/поля | system и systemFields | Пути сверены с определениями, использованы настоящие модели |
| Контекст листа | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | PARTS/подготовка | actor/document/system, опции, записи enrichedText | Полный _prepareContext выполнен с Application-фасадом |
| helpers и переводы | [module/setup/handlebars.js](../../../../../../../../../../../module/setup/handlebars.js); [lang/en.json](../../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../../lang/ru.json) | Handlebars/локализация | localize, concat, eq/gte, checked, selectOptions, formGroup/editor по месту | Системные helpers и core helpers сверены; DOM-элементы формы заменены |
| NoteData; note schema | [module/data/item/noteData.js](../../../../../../../../../../../module/data/item/noteData.js); [module/data/actor/templates/common/noteData.js](../../../../../../../../../../../module/data/actor/templates/common/noteData.js) | два типа данных | Item.system.description и Array(title/details) | Оба определения прочитаны как зависимости; полные карточки новой заметочной цепочки — .033 |
| itemListener/_onItemAdd/_onItemInlineEdit/_onItemDelete | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | события | Старая модель заметок | Пути и data-item-id совпадают |
| noteListener/_onNoteDelete | [module/actor/sheets/mixins/noteMixin.js](../../../../../../../../../../../module/actor/sheets/mixins/noteMixin.js) | события | Удаление массива | splice по data-note-index; update не await |
| CSS-селекторы | [styles/monster/details.css](../../../../../../../../../../../styles/monster/details.css) | оформление | Контейнер деталей | Прочитаны нужные селекторы; полный CSS вне порции |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | partial | detailTabs.notes | Путь/обращение сверены в исходнике |
| [module/setup/handlebars.js](../../../../../../../../../../../module/setup/handlebars.js) | путь | preloadHandlebarsTemplates | Путь/обращение сверены в исходнике |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | старые note-селекторы | itemListener | Путь/обращение сверены в исходнике |
| [module/actor/sheets/mixins/noteMixin.js](../../../../../../../../../../../module/actor/sheets/mixins/noteMixin.js) | delete-note | noteListener | Путь/обращение сверены в исходнике |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Старые name/description имеют data-field без name и сохраняются Item-handler, поэтому не входят в обычный payload. В each контекст — Item: {{system.description}} корректно читает note.system.description. Новые title/details используют индексы массива. Core editor получает raw note.details; обогащение не вызывается здесь. Сохранение редактора/создание заметок в браузере не проверены; полный процесс .033.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Два вида заметок | 11 | Один Item textarea со строкой <Old>, две array-delete кнопки, add-item и отсутствие add-note; title по индексу 1; удаление 0 оставляет Second | Настоящий noteMixin с перехватом update; editor-input фасад |

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Мир, браузер, HTTP-доступ, Document.update и работа нескольких клиентов не запускались. Настоящие модели, Handlebars, core helpers и вычисления использовались с фасадами Application/DOM и перехватом записи; подробные границы — в журнале .032. CSS и ресурсы проверены только как зависимости, соседние файлы вне порции не засчитываются в покрытие.

## Связанные проблемы

Новой самостоятельной ошибки в проверенном контракте заметок не зарегистрировано; смешение двух способов хранения описано без решения о миграции.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `8b938d44a042749df027d8b58e28bb1d79638091`; полный файл | Первая карточка; [сверка порции](../../../../../../../../review-log.md#task-0003032) |
