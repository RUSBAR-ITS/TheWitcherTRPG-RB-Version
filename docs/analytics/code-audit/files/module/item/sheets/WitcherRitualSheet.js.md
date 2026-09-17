# module/item/sheets/WitcherRitualSheet.js

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../../issues/closed/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Редактирование основного и альтернативного списка компонентов.

**Основные методы, сущности и действия:** _onEditComponent/_onRemoveComponent проверяют имя списка; edit допускает только конечное quantity, находит первую строку по сохранённому UUID и ожидает update копии массива. Remove сохраняет прежнюю семантику удаления всех совпадений UUID. Отсутствующий UUID/строка не меняет другой список.

**Зависимости и потребители:** ritualData.js предоставляет внешний uuid; ritual-sheet.hbs пишет его в data-uuid. Drop не перерабатывался.

## Предыдущий срез анализа

Датированные сведения ниже относятся к прежнему коду. При расхождении приоритет имеет актуальный раздел выше.

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherRitualSheet.js](../../../../../../../module/item/sheets/WitcherRitualSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Редактор Item ritual и обработчики двух списков компонентов: перенос Item, изменение количества и удаление ссылок.

## Условия использования

registerSheets регистрирует лист для ritual. _onRender базового WitcherItemSheet вызывает activateListeners; DragDrop базового листа разрешает документ и передаёт Item в _onDropItem. Своя configuration не создаётся: используется обычный WitcherConfigurationSheet.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherRitualSheet | default class; 3–82 | Наследник WitcherItemSheet | Items.registerSheet, ritual | Контекст и события |
| static PARTS.main | 4–9 | ritual-sheet.hbs, scrollable:[''] | ApplicationV2 | Рендер формы |
| selects.levelSpell/templateType | 20–35 | novice/journeyman/master; rect/circle/cone/ray/emanation | context.selects | Локализуемые варианты |
| .edit-component blur; .remove-component click | 40–42, замыкания bind | События строк | jQuery.on при каждом activateListeners | Вызов методов ниже; это не data-action |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options) | Базовый контекст | Promise контекста | await super; selects=createSelects | Без записи |
| createSelects() | Нет | Два словаря | Возвращает варианты | Не ограничивает схему |
| activateListeners(html) | DOM листа; global $ | undefined | super; привязывает blur/click | Предварительной проверки isEditable здесь нет; Drop проверяется родителем |
| async _onDropItem(event, item) | Truthy Item; event.target.closest | Promise<undefined> | Внутри .alternateComponents → альтернативный массив, всё остальное → основной; push{uuid, quantity: 1}; update массива | Тип/дубликат не фильтруется; массив меняется до update; Promise update не возвращается и не ожидается |
| _onEditComponent(event) | currentTarget.closest('.list-item').dataset.uuid/target; dataset.field/value | undefined | findIndex по UUID; меняет поле первой найденной записи; item.update | value остаётся строкой; findIndex=-1 вызывает TypeError; update не ожидается |
| _onRemoveComponent(event) | dataset.uuid/target | undefined | filter убирает все записи с UUID; item.update | Нет возврата Promise; одинаковые ссылки удаляются вместе; пустой dataset не удаляет сохранённый непустой UUID |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Импорт/наследование | Базовый контекст, submitOnChange, configureItem, DragDrop и _onRender | Родитель прочитан; собственный createSelects дополняет контекст |
| CONFIG.WITCHER; ключи WITCHER.* | [module/setup/config.js](../../../../../../../module/setup/config.js) | Контекст через родителя | config для полей/вариантов | _prepareContext в базовом листе |
| localize/selectOptions | Foundry14.367.0 /opt/foundryvtt/client/applications/handlebars.mjs; Handlebars4.7.9 | Внешний UI | Варианты передаются HBS | Настоящий HBS; фасады helpers/ItemSheetV2, полный браузер не запускался |
| Ключи подписей | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Значения createSelects | JSON en/ru проверены с раскрытием dotted ключей |
| ritual-sheet.hbs | [templates/sheets/item/ritual-sheet.hbs](../../../../../../../templates/sheets/item/ritual-sheet.hbs) | PARTS/DOM contract | Строки dataset.uuid/target/field, контейнер alternateComponents | Сверены оба списка |
| RitualData; component() | [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js); [module/data/item/templates/componentData.js](../../../../../../../module/data/item/templates/componentData.js) | Контракт данных | Два сохранённых ArrayField | UUID не является уникальным ID строки; quantity Number |
| jQuery $; Element.closest; Item.update | jQuery/DOM и Foundry14.367.0 Item API | События/запись | activateListeners и CRUD | В Node использованы façade события и управляемые Promise update; DB не вызывается |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherRitualSheet | Импорт/регистрация | 22, 92–94 |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | activateListeners/_onDropItem | Базовый _onRender и _onDropDocument динамически вызывают переопределения | Родитель прочитан |
| [templates/sheets/item/ritual-sheet.hbs](../../../../../../../templates/sheets/item/ritual-sheet.hbs) | Обработчики/варианты | blur/click и Drop-зоны | Полный разбор |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Drop/edit мутируют подготовленный массив самого item.system до записи; remove строит новый массив. Обработчики передают целый массив в update. Успешное завершение async Drop не означает окончания сохранения. При отказе façade update добавленная запись остаётся в текущей памяти; реальное восстановление после ошибки/нового prepare в клиенте не проверено. Поле quantity становится числом при очистке моделью, несмотря на строку event.value.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| События/маршрут | Группы 09–10 | Связаны blur/click; Drop вне alternate идёт в основной список; null Item пропускается по коду | DOM заменён объектами, правовой UI ядра не исполнялся |
| Неизвестный/повторный UUID | Группы 07–08; настоящий RitualData/HBS/обработчики | Неизвестный: edit TypeError, remove не меняет список. Повторный: изменение первой и удаление всех | Resolver заменён картой |
| Сохранение/типы | Группа 09 | await Drop заканчивается с pending update; отказ не отменяет push; quantity'7' очищается до 7 | Настоящая БД, гонки клиентов не воспроизведены |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Реальные drop/submit, конкурентные окна, packs и восстановление при отказе записи не запускались. Остаток: [U009-01](../../../../cross-check-0002.md#u009-01), [U009-07](../../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00058](../../../../../../issues/potential/issue-00058.md), [issue-00059](../../../../../../issues/potential/issue-00059.md), [issue-00098](../../../../../../issues/closed/issue-00098.md), [issue-00129](../../../../../../issues/potential/issue-00129.md), [issue-00130](../../../../../../issues/closed/issue-00130.md), [issue-00131](../../../../../../issues/potential/issue-00131.md), [issue-00132](../../../../../../issues/potential/issue-00132.md), [issue-00136](../../../../../../issues/potential/issue-00136.md), [issue-00137](../../../../../../issues/closed/issue-00137.md). Новые 129–132 описывают собственный путь ритуала; 58/59 — унаследованный Drop; 98 — подсказки; 136/137 — представление.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |

## Уточнение TASK-0003.022

2026-09-11, `ef8117ba6e5a184989e65761d47a068381056e4a`; исходник не изменён.

Словарь templateType соответствует тем же пяти ветвям примеси. Лист не создаёт регионы и не исполняет макросы; его основная форма всё ещё записывает прежние верхние пути. Наличие пункта emanation само по себе не гарантирует правильный выбор сцены/размера.

Связанные карточки: [module/data/item/templates/regions/templatePropertiesData.js](../../data/item/templates/regions/templatePropertiesData.js.md).

[Результаты и пределы сверки](../../../../review-log.md#task-0003022).

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

RitualSheet связывает общий контекст, level/template selects и форму с двумя массивами компонентов. Сопоставлены DOM dataset, выбор main/alternate, drop любого Item, edit первого UUID и remove всех совпадений. prepared mutation до не ожидаемого update отделена от фактической записи; старые поля области принадлежат HBS.

Сопоставленные определения и потребители: [module/item/sheets/WitcherItemSheet.js](WitcherItemSheet.js.md), [module/setup/config.js](../../setup/config.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md), [templates/sheets/item/ritual-sheet.hbs](../../../templates/sheets/item/ritual-sheet.hbs.md), [module/data/item/ritualData.js](../../data/item/ritualData.js.md), [module/data/item/templates/componentData.js](../../data/item/templates/componentData.js.md), [module/setup/registerSheets.js](../../setup/registerSheets.js.md).

[Протокол и границы](../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-01](../../../../cross-check-0002.md#r009-01), [R009-03](../../../../cross-check-0002.md#r009-03), [R009-05](../../../../cross-check-0002.md#r009-05). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
