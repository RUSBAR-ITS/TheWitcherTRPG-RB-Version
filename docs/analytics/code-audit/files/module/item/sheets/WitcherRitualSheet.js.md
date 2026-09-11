# module/item/sheets/WitcherRitualSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherRitualSheet.js](../../../../../../../module/item/sheets/WitcherRitualSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

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

Все 82 строки прочитаны. Не установлено поведение конкурентных правок/пакетов и восстановление интерфейса после отказа записи. Запись игровых документов не выполнялась.

## Связанные проблемы

[issue-00058](../../../../../../issues/potential/issue-00058.md), [issue-00059](../../../../../../issues/potential/issue-00059.md), [issue-00098](../../../../../../issues/potential/issue-00098.md), [issue-00129](../../../../../../issues/potential/issue-00129.md), [issue-00130](../../../../../../issues/potential/issue-00130.md), [issue-00131](../../../../../../issues/potential/issue-00131.md), [issue-00132](../../../../../../issues/potential/issue-00132.md), [issue-00136](../../../../../../issues/potential/issue-00136.md), [issue-00137](../../../../../../issues/potential/issue-00137.md). Новые 129–132 описывают собственный путь ритуала; 58/59 — унаследованный Drop; 98 — подсказки; 136/137 — представление.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |
