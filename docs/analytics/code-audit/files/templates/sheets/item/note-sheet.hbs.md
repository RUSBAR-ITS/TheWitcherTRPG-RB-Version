# templates/sheets/item/note-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/note-sheet.hbs](../../../../../../../templates/sheets/item/note-sheet.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `12055fee62f01c6de49967044aedef9d7cfe0632` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.033](../../../../../../tasks/task-0003.033.md), 4 файла, 178 логических строк |
| Запись перекрёстной сверки | [TASK-0003.033](../../../../review-log.md#task-0003033) |

## Назначение файла

Старый самостоятельный HTML-шаблон заметки-предмета: форма с именем и многострочным описанием.

## Условия использования

В module/ и templates/ не найдено выбора note-sheet.hbs через PARTS, template, renderTemplate, partial или предзагрузку. Общий WitcherItemSheet зарегистрирован для note, но имеет PARTS={}; автоматического выбора шаблона по item.type в нём нет. Поэтому карточка описывает разметку и изолированный рендер, а не работающую текущую форму.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| form / cssClass / autocomplete=off | 1–8 | Внешняя форма старого листа | Самостоятельный HBS | Класс из контекста; нет tabs/actions/helpers |
| item.name / input[name='item.name'] | 4 | Отобразить/ввести имя | text-input с placeholder Name | Путь name формы включает лишний для стандартного Item-прямого update префикс item; фактического submit-потребителя не найдено |
| item.system.description / textarea[name='system.description'] | 5 | Строковое описание | textarea rows=10 | Имя form-поля соответствует system.description, значение берётся из item.system |

## Основные функции и методы

Программных функций, экспортов, partial и helper-вызовов нет. Три Handlebars-подстановки: cssClass, item.name, item.system.description. Они экранируются стандартным движком.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| NoteData.description | [module/data/item/noteData.js](../../../../../../../module/data/item/noteData.js) | данные | 5: item.system.description | StringField; HTML внутри textarea показывается текстом |
| Item.name | Foundry 14.367.0: документ Item | данные | 4 | Имя является полем документа, не его system; стандартный путь обновления name |
| item / cssClass | Контекст старого листа; действующий поставщик этого HBS не установлен | контекст | 1,4–5 | В изолированном render передан fixture. WitcherItemSheet._prepareContext содержит item, но данный шаблон не выбирает. |
| Handlebars escaping | Handlebars 4.7.9 | интерполяция | Все три подстановки | Текст '<N &>' и '<b>D &</b>' восстановлен из отрендеренных input/textarea без HTML-узлов описания |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |


Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Сам шаблон не создаёт и не обновляет Item. Изолированная FormDataExtended получила {'item.name':'<N &>','system.description':'<b>D &</b>'}; ключа name нет. Это указывает на дополнительную проверку пути имени при будущем подключении формы, но не доказывает сбой сохранения в текущем UI, где маршрут не подключён. Нельзя переносить на этот файл обработчики .inline-edit из tab-background: здесь нет соответствующих классов/data-field.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Разметка | Группа 08 | Одна form, один text-input, одна textarea; два строковых поля payload | Нет браузерного submit и настоящего листа-потребителя |
| Достижимость | Поиск rg по module/templates, полные registerSheets и WitcherItemSheet; прежняя проверка issue-00057 | Нет выбора HBS; текущий общий класс имеет пустой PARTS | Прежний изолированный core _renderHTML из issue-00057 не выдаётся за повторно выполненный здесь |

## Непроверенные участки и открытые вопросы

Остаются [U013-06](../../../../cross-check-0002.md#u013-06): указанные там динамические границы и критерии дальнейшей сверки. Нынешняя проверка статическая; прежние изолированные опыты .025/.031/.032/.033 сохраняют даты и фасады. Полный браузерный лист, Document.create/update в БД, внешние модули и несколько клиентов не запускались.

## Связанные проблемы

[issue-00057](../../../../../../issues/potential/issue-00057.md). Дополнена существующая проблема отключённого note-листа с уточнением полей старого шаблона; отдельный дубликат не создан.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `12055fee62f01c6de49967044aedef9d7cfe0632`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003033) |

## Сквозная сверка TASK-0004.013

2026-09-14; rusbar-main, fc53038008e744b2e504d1b9c913045147c25a02. Исходник совпадает со срезом TASK-0001; изменено только описание.

Старая 8 строчная форма note имеет input item.name и textarea system.description. Выбора через PARTS/template/partial/preload не найдено; общий зарегистрированный ItemSheet с PARTS={} не выбирает её по типу. Изолированный render не объявлен ошибкой активного сохранения имени. Для вывода о работе формы нужен реальный consumer и согласованный разбор submit: [U013-06](../../../../cross-check-0002.md#u013-06).

Сопоставленные определения и потребители: [module/data/item/noteData.js](../../../module/data/item/noteData.js.md), [templates/partials/character/tab-background.hbs](../../partials/character/tab-background.hbs.md), [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../actor/partials/monster/tabs/partials/monster-notes.hbs.md), [module/data/item/commonItemData.js](../../../module/data/item/commonItemData.js.md), [module/setup/registerDataModels.js](../../../module/setup/registerDataModels.js.md), [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js.md), [module/item/sheets/WitcherItemSheet.js](../../../module/item/sheets/WitcherItemSheet.js.md), [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js.md).

[Протокол и границы](../../../../review-log.md#task-0004013) — TASK-0004.013; процессы [R013-26](../../../../cross-check-0002.md#r013-26), [R013-28](../../../../cross-check-0002.md#r013-28). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
