# module/data/item/noteData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/noteData.js](../../../../../../../module/data/item/noteData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `12055fee62f01c6de49967044aedef9d7cfe0632` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.033](../../../../../../tasks/task-0003.033.md), 4 файла, 178 логических строк |
| Запись перекрёстной сверки | [TASK-0003.033](../../../../review-log.md#task-0003033) |

## Назначение файла

Модель данных Item типа note: наследует общие поля предмета и явно повторяет строковое поле description.

## Условия использования

NoteData импортируется registerDataModels и назначается CONFIG.Item.dataModels.note; тип note объявлен в system.json. Это отдельная модель от одноимённой фабрики Actor-notes. Специализированного листа note не зарегистрировано: применяется общий WitcherItemSheet с пустым PARTS; существующий note-sheet.hbs не подключён.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная const; 3 | Ссылка на foundry.data.fields | Внутри модуля | Получена при импорте |
| NoteData | default-export класса; 5–16 | TypeDataModel предмета note | CONFIG.Item.dataModels.note | Наследование CommonItemData |
| defineSchema / description | static-метод:7–15; поле:13 | Повторить description:StringField(initial:'') | Схема system | Остальные общие поля сохраняются через ...commonData |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| NoteData.defineSchema() | Доступна Foundry data.fields и родительская схема | Объект схемы из восьми полей | super.defineSchema(); spread; новый StringField description | Нет записи Actor/Item, миграции, обогащения текста или операций массива notes |
| Унаследованные calcWeight; canHaveTemporaryItemImprovement; canBeRepaired | Определены в CommonItemData | Вес по quantity/weight/isCarried/isStored; два false | Сам NoteData не переопределяет их | Наследуемое поведение, не новые определения файла |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | default-import; extends; super.defineSchema | 1,5,9–13 | Восемь общих полей; description повторяет прежний StringField |
| fields.StringField | Foundry 14.367.0, common/data/fields.mjs | схема | 3,13 | Настоящая модель сохраняет строку с HTML; description не HTMLField |
| foundry.abstract.TypeDataModel | Foundry 14.367.0, common/abstract/type-data.mjs | косвенное наследование через CommonItemData | Создание и сериализация system | Импорт настоящего класса/полей и roundtrip |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | NoteData | import:11; CONFIG.Item.dataModels.note:57 | Регистрация прочитана и сопоставлена с манифестом |
| [templates/partials/character/tab-background.hbs](../../../../../../../templates/partials/character/tab-background.hbs) | Item.system.description | 114–115 внутри each oldNotes | Косвенное чтение схемы через реальные note Items; inline-edit пишет тот же путь |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) | Item.system.description | 10–11 внутри each oldNotes | Контракт совпадает с персонажным |
| [templates/sheets/item/note-sheet.hbs](../../../../../../../templates/sheets/item/note-sheet.hbs) | item.system.description | 5: textarea | Шаблон прочитан и изолированно отрендерен; активный потребитель самого шаблона не найден |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Полная схема: description='', quantity='1', weight=0, cost=0, sourcebook='', isHidden=false, isStored=false, isCarried=true. description и quantity — StringField, weight/cost — NumberField, три флага — BooleanField. Форматированный текст остаётся строкой, сама модель не вызывает enrichHTML. Имя и ID относятся к документу Item и не вводятся NoteData. Массив Actor.system.notes хранится другой схемой и автоматически из Item.note не создаётся.

Для quantity='2', weight=3 при обычных флагах calcWeight() возвращает 6. Это унаследованный учёт предмета, отдельного исключения для заметки нет. Из этого не выводятся правила игрового веса заметок.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема и сериализация | Группа 01 | 8 полей, пустое description, строка '<b>Bold & plain</b>' сохранена после roundtrip; вес 6 | Не проверка очистки HTML браузером или безопасности текста |
| Раздельные форматы | Группы 06,15 | Одна Item-note и одна array-note остаются двумя наборами | Нет миграции и чтения действующего мира |
| Создание Item | Группа 07 | Кнопка передаёт {name:'new note',type:'note'} в Item.create({parent:actor}) | Документная запись заменена сборщиком аргументов |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Проверки выполнены в Node 24.16.0 с кодом Foundry 14.367.0, без мира, браузера, HTTP и записи в БД. Модели, методы системы, Handlebars и перечисленные в журнале функции ядра настоящие; Application/DOM и документные операции заменены фасадами. Сохранение через updateSource проверяет модель в памяти и не доказывает серверную запись, разрешение конфликтов или работу ProseMirror в браузере.

## Связанные проблемы

[issue-00057](../../../../../../issues/potential/issue-00057.md), [issue-00153](../../../../../../issues/potential/issue-00153.md). Пустой общий лист относится к регистрации интерфейса; преобразование false/true — к общему inline-handler, а не к defineSchema.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `12055fee62f01c6de49967044aedef9d7cfe0632`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003033) |
