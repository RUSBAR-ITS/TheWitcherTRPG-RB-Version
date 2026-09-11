# module/data/actor/templates/common/noteData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/noteData.js](../../../../../../../../../module/data/actor/templates/common/noteData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c34b790379fd98cd7e33ccbeeca085e49297a40f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.003](../../../../../../../../tasks/task-0003.003.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.003](../../../../../../review-log.md#task-0003003) |

## Назначение файла

Фабрика записи заметки в массиве system.notes: заголовок и текст. Этот формат отличается от отдельного Item типа note.

## Условия использования

[module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js):5,56 включает new ArrayField(new SchemaField(note())). Начальный system.notes — пустой массив. Item.note использует другую модель: [module/data/item/noteData.js](../../../../../../../../../module/data/item/noteData.js).

## Введённые сущности и действия с ними

| Поле / сущность | Тип, начальное значение и ограничения | Назначение и действия |
| --- | --- | --- |
| note() | default export, :4–9 | Фабрика записи без собственного ID. |
| title | StringField, initial='' | Заголовок. |
| details | StringField, initial='' | Текст, передаваемый редактору; собственный HTMLField/enriched getter не объявлен. |

## Основные функции и методы

note():4–9 без аргументов возвращает title/details. Индекс массива, добавление, удаление и сохранение находятся у потребителей.

## Используемые сущности и зависимости

| Сущность | Файл определения / API | Связь, место и цель |
| --- | --- | --- |
| fields.StringField | Внешний API Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | Глобальная ссылка :2, поля :6–7. |
| ArrayField и SchemaField | [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | Обёртка :56 задаёт массив записей, сама фабрика возвращает объект полей. |

## Известные потребители

| Файл-потребитель | Обращение и условия |
| --- | --- |
| [module/actor/sheets/mixins/noteMixin.js](../../../../../../../../../module/actor/sheets/mixins/noteMixin.js) | _onNoteAdd:3–10 берёт живой массив, push пустой записи и Actor.update(system.notes); _onNoteDelete:12–17 splice по dataset.noteIndex и пишет массив. noteListener:20–23 связывает .add-note/.delete-note. |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | _prepareGeneralInformation передаёт context.notes=actor.system.notes и отдельно oldNotes из Item.note; V2 подключает noteListener:242, V1 содержит аналогичное представление данных. |
| [templates/partials/character/tab-background.hbs](../../../../../../../../../templates/partials/character/tab-background.hbs) | :100–126 выводит сначала oldNotes, затем notes; индекс используется в name/target system.notes.<индекс>.title/details. |
| [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs); [templates/sheets/actor/partials/monster/tabs/tab-details.hbs](../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-details.hbs) | Аналогичное разделение двух форматов; tab-details включает monster-notes. |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | Кнопка .add-item с data-itemType=note следует общему созданию предмета, а не _onNoteAdd. |

Область поиска: прямые импорты в module, обращения к полям в module/templates и строковые пути в 226 packsJson. Соседние файлы проверялись в пределах указанных обращений. Их полный разбор не объявляется выполненным.

## Данные и изменения состояния

Фабрика не пишет данные. _onNoteAdd/_onNoteDelete изменяют текущий массив до вызова Actor.update. В проверенных шаблонах кнопка добавления создаёт Item.note: .add-note в module/templates вне самого noteListener не найдена. Поэтому наличие метода _onNoteAdd не доказывает его вызов кнопкой текущего интерфейса. Массивные записи удаляются и редактируются по индексу; oldNotes редактируются отдельными действиями Item.

## Проверки и доказательства

Прочитаны 9 строк. В настоящей CommonActorData проверены пустой массив и исходные методы добавления/удаления: перехвачены update с одной пустой записью и затем с []. Шаблоны сопоставлены с контекстом и именами обработчиков.

Файл прочитан полностью; определения и потребители сопоставлены в обе стороны. Изолированные проверки использовали реальные DataModel/TypeDataModel и поля установленного Foundry, а внешние действия — явно указанные подмены. Полный сценарий и результаты находятся в журнале TASK-0003.003.

## Непроверенные участки и открытые вопросы

Не проверены HTML-редактор, обработка формы массива в Foundry, безопасность/обогащение текста, конкурентное редактирование и преобразование старых Item.note. Отсутствие .add-note фиксируется как ограничение доступного пути, без самостоятельного решения об удалении одного из форматов.

## Связанные проблемы

Новых проблем в пределах выполненной проверки не зарегистрировано.


## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.003 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Подтверждено notes:ArrayField(SchemaField(note())):56 общей модели. Эта схема массива не создаёт Item.note и не связывает два вида заметок автоматически.

Карточки сборки: [commonActorData](../../commonActorData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Текущий monster-notes использует массив title/details и индексы в name/data-note-index; отдельно показывает oldNotes как Item. Полный базовый producer передаёт обе группы. Удаление 0 из двух array-заметок оставило Second в перехваченном Actor.update; создание/редактирование в браузере не проверено.

Связи: [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs.md). [Результаты и пределы проверки](../../../../../../review-log.md#task-0003032).
