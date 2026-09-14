# module/actor/sheets/mixins/noteMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/noteMixin.js](../../../../../../../../module/actor/sheets/mixins/noteMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `12055fee62f01c6de49967044aedef9d7cfe0632` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.033](../../../../../../../tasks/task-0003.033.md), 4 файла, 178 логических строк |
| Запись перекрёстной сверки | [TASK-0003.033](../../../../../review-log.md#task-0003033) |

## Назначение файла

Примесь листов Actor для добавления и удаления записей массива system.notes и привязки двух событий интерфейса.

## Условия использования

Экспортируемый noteMixin копируется в прототипы WitcherActorSheet и WitcherActorSheetV1 через Object.assign. Текущие Character/Monster наследуют V2. В V1 есть такое же подключение, но зарегистрированного листа на его основе в module/setup/registerSheets.js не найдено. В текущих шаблонах есть .delete-note; .add-note вне noteListener в module/templates не найден. Кнопки .add-item создают другой вид заметок — Item типа note.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| noteMixin | Именованный экспорт объекта; 1–25 | Три метода листа | Object.assign двух базовых листов | Объект не создаёт документы при импорте |
| _onNoteAdd | async-метод; 3–10 | Добавить пустую запись title/details | Через прототип листа; обработчик .add-note | push в actor.system.notes, затем вызов Actor.update |
| _onNoteDelete | async-метод; 12–17 | Удалить запись по индексу из dataset | Обработчик .delete-note | splice в том же массиве, затем вызов Actor.update |
| noteListener | Метод; 19–23 | Подключить click | Вызывается activateListeners | Оборачивает html в $, привязывает два bound-handler |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _onNoteAdd() | this.actor.system.notes — массив | Promise<undefined> | Берёт ссылку на массив; push({title:'',details:''}); update({'system.notes':notes}) | Запись не await/return; prepared-массив изменён раньше сохранения. Ошибка синхронного update отклонит метод; позднее отклонение возвращённого update Promise не передаётся вызывающему коду. |
| _onNoteDelete(event) | event.currentTarget.dataset.noteIndex; this.actor.system.notes | Promise<undefined> | Читает строку индекса, splice(noteIndex,1), отправляет весь массив | Нет проверки целого/диапазона; применяются преобразования Array.splice. Нет await/return update; preventDefault/stopPropagation здесь не вызываются. |
| noteListener(html) | DOM-элемент или принимаемый jQuery аргумент; методы на this | undefined | $(html).find('.add-note' / '.delete-note').on('click', bound method) | Не создаёт заметок сам; наличие регистрации не означает наличие кнопки. Отписки/off в файле нет. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| notes:ArrayField(SchemaField(note())) | [module/data/actor/commonActorData.js](../../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/noteData.js](../../../../../../../../module/data/actor/templates/common/noteData.js) | данные и определение полей | 3–16: title/details, изменение массива | CommonActorData:56; note(): title/details StringField |
| Actor.update | Foundry 14.367.0: API Document.update; actor передаётся листом | запись документа | 9,16: весь system.notes | В опытах перехвачен вызов; штатная серверная запись не выполнялась |
| $; find; on; bind | jQuery, JavaScript Function.bind | события интерфейса | 19–22 | Регистрация и вызов привязанных функций проверены с jQuery-фасадом |
| Array.push / Array.splice | JavaScript Array | изменение памяти | 5–8 и 15 | Проверены пустой массив, первый/последний элемент и пять нештатных индексов |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | noteMixin; noteListener | import:3, activateListeners:242, Object.assign:319 | Полный импорт класса; совпадение функций прототипа и регистрация проверены |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | noteMixin; noteListener | import:3, activateListeners:220 с html[0], Object.assign:299 | Класс импортирован с фасадом V1; методы совпадают, вызов .delete-note проверен |
| [templates/partials/character/tab-background.hbs](../../../../../../../../templates/partials/character/tab-background.hbs) | .delete-note / data-note-index | 120–121: индекс из @index массива notes | Рендер и удаление после подготовки; .add-note отсутствует |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs) | .delete-note / data-note-index | 16–17: тот же массивный контракт | Сопоставлено с карточкой .032; новый полный рендер монстра здесь не выполнялся |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Сохраняемая структура — [{title,details},…], без ID и связи с Item.note. Оба метода меняют текущий prepared-массив по ссылке. В настоящей CharacterData после вызова массив уже меняется, а toObject() исходных данных остаётся прежним, пока запись подменена. При удержанном Promise update метод уже завершён; при отказе update не выполнен автоматический откат prepared-массива. Принимающий фасад отдельно наблюдал отклонение, чтобы не создавать необработанную ошибку теста.

Для [A,B,C] строка '0' удаляет A, '2' — C, undefined/'bad' — A, '-1' — C, '1.5' — B, '99' не удаляет ничего, но update всё равно вызывается. Текущий HBS выдаёт корректные индексы; нештатные значения переданы программно, достижимость из обычного клика не утверждается. Удаление сдвигает последующие индексы; повторный контекст/рендер выводит обновлённые пути.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Определения/подключение | Группы 02,14 | Три собственных метода, одинаковые функции на V1/V2; привязанный click удаляет заметку | В V1 проверен доступный класс, не его регистрация в клиенте |
| Добавление и удаление | Группы 03–04 | Пустая запись, первый/последний/пустой массив, пять пограничных индексов | Методы настоящие, update перехвачен |
| Завершение/отказ записи | Группа 05 | Оба метода завершаются при pending update; prepared уже изменён, source прежний | Нет настоящего отказа БД и конкурентного клиента |
| Повторный рендер | Группа 12 | После удаления 0 бывшая запись 1 получает form-пути notes.0.* | Сохранение применено к модели в памяти |

## Непроверенные участки и открытые вопросы

Остаются [U013-08](../../../../../cross-check-0002.md#u013-08): указанные там динамические границы и критерии дальнейшей сверки. Нынешняя проверка статическая; прежние изолированные опыты .025/.031/.032/.033 сохраняют даты и фасады. Полный браузерный лист, Document.create/update в БД, внешние модули и несколько клиентов не запускались.

## Связанные проблемы

[issue-00211](../../../../../../../issues/potential/issue-00211.md), [issue-00212](../../../../../../../issues/potential/issue-00212.md). Ожидание записи и проверка индекса описаны отдельно. Отсутствие .add-note зафиксировано как текущий маршрут интерфейса, без решения о смене формата заметок.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `12055fee62f01c6de49967044aedef9d7cfe0632`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003033) |

## Сквозная сверка TASK-0004.013

2026-09-14; rusbar-main, fc53038008e744b2e504d1b9c913045147c25a02. Исходник совпадает со срезом TASK-0001; изменено только описание.

Примесь подключена в V2/V1; текущие Character/Monster HBS используют delete-note по @index, а кнопка добавления создаёт Item через add-item. Оба массива-метода меняют prepared notes до update и не ждут его Promise. splice применяет незащищённое приведение индекса; ошибочные dataset старого опыта были программными. Form-пути/переиндексация прослежены, реальная запись и несколько окон — [U013-08](../../../../../cross-check-0002.md#u013-08).

Сопоставленные определения и потребители: [templates/partials/character/tab-background.hbs](../../../../templates/partials/character/tab-background.hbs.md), [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs.md), [module/data/actor/commonActorData.js](../../../data/actor/commonActorData.js.md), [module/data/actor/templates/common/noteData.js](../../../data/actor/templates/common/noteData.js.md).

[Протокол и границы](../../../../../review-log.md#task-0004013) — TASK-0004.013; процессы [R013-27](../../../../../cross-check-0002.md#r013-27). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
