# module/item/sheets/WitcherContainerSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherContainerSheet.js](../../../../../../../module/item/sheets/WitcherContainerSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `66cd03705dbc398eba0026284a298b5fbe337035` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.024](../../../../../../tasks/task-0003.024.md), 3 файла, 136 логических строк |
| Запись перекрёстной сверки | [TASK-0003.024](../../../../review-log.md#task-0003024) |

## Назначение файла

Лист контейнера на базе WitcherItemSheet: допускает девять типов Item, добавляет UUID в content и удаляет ссылки, меняя isStored исходного Item.

## Условия использования

registerSheets назначает класс по умолчанию для container. PARTS.main загружает форму контейнера. Общий _onDrop проверяет isEditable, разрешает Document и передаёт Item в собственный _onDropItem. Drop Actor/Folder остаётся маршрутом базового листа с отсутствующими методами.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | default import, 1 | Общая база V2 | extends | Контекст data=item.system, конфигурация и Drop |
| WitcherContainerSheet | default class, 3–54 | Специализированный лист | Item.container | Drop/removal/UI |
| storableItems | Поле экземпляра, 4–15 | Девять типов | weapon,armor,enhancement,valuable,alchemical,component,diagrams,mutagen,container | Сравнение item.type; все девять объявлены в манифесте |
| PARTS.main | static, 17–23 | Шаблон и прокрутка | container-sheet.hbs; scrollable:[''] | Единственная часть листа |
| click listener .remove-item | _onRender, 28–30 | Удаление ссылки из UI | bind(this) → _onRemoveItem | Обработчик устанавливается непосредственно на элементы |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _onRender(context,options) | Отрендеренный this.element | undefined | Вызывает super, назначает click на .remove-item | Не возвращает/ожидает async super._onRender; база позже привязывает DragDrop |
| async _onDropItem(event,item) | Item; storableItems; this.item.system.content | Promise<undefined> | Guard item/type/отсутствие uuid в этом content; push; container.update; item.update(isStored=true) | Мутирует массив до записи; оба update не ждёт/возвращает; не проверяет owner/parent/self/cycle/членство в другом контейнере/carry |
| _onRemoveItem(event) | currentTarget.dataset.uuid; resolver | undefined | preventDefault; indexOf; splice только при найденном index; fromUuidSync; container.update; item.update(isStored=false) | При index=-1 всё равно меняет исходный Item; нет null/update guard; обе записи не ожидаются |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | ES default import/extends | Контекст, configuration, _onDrop/_onDropDocument/_onRender | Полный исходник сверён; группы 13/14 |
| ContainerData / CommonItemData | [module/data/item/containerData.js](../../../../../../../module/data/item/containerData.js); [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Поля моделей | content и system.isStored | Полные модели для групп 01–12 |
| container-sheet.hbs | [templates/sheets/item/container-sheet.hbs](../../../../../../../templates/sheets/item/container-sheet.hbs) | PARTS.main | 19 | remove-item/data-uuid; поля |
| documentTypes.Item | [system.json](../../../../../../../system.json) | Словарь допустимых типов | storableItems | Все девять присутствуют; unsupported spell в проверке пропущен |
| fromUuidSync | Foundry 14.367.0 client/utils/helpers.mjs:188–214 | UUID resolver | _onRemoveItem:50 | Документ/индекс/null; разрешение не проверяет право записи |
| Item.update / parent / isOwner | Foundry 14.367.0 Document API; client/documents/item.mjs; common/abstract/document.mjs | Запись/идентичность | Два независимых обновления | Проверены payload и ожидание через фасады; реальные права сервера не обойдены и не проверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherContainerSheet | Импорт/регистрация container | 6; 44–47 |
| [templates/sheets/item/container-sheet.hbs](../../../../../../../templates/sheets/item/container-sheet.hbs) | _onRemoveItem и базовый контекст | Клик .remove-item по UUID | 17–18 |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | _onDropItem override | Динамическая диспетчеризация Item | _onDropDocument:130 |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

При помещении создаётся только строка ссылки; источник не копируется и не переходит к другому Actor. Проверка повтора локальна текущему контейнеру. already-stored Item может войти во второй content, при снятии любой ссылки его isStored сбрасывается без поиска оставшихся контейнеров. Элементы из мира/другого Actor/компедиума не запрещены собственной логикой.

При удалении UUID, которого нет в content, обработчик всё равно отправляет isStored=false разрешённому источнику. При отсутствующем документе массив уже укорочен, update контейнера запущен, затем обращение item.update падает. При отказе одной из двух асинхронных записей нет общего ожидания, отката или повторного согласования двух сторон. Реальный исход БД этим не моделируется.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Допуск и членство | Группы 05/07/08/10/11 | Один и тот же UUID в текущем контейнере повторно не добавлен; два контейнера, self/cycle и чужой parent допущены; nonmember removal сбрасывает flag | Источник/запись — фасады |
| Асинхронность | Группа 06 | Drop разрешается при pending update; remove возвращает undefined; массив уже изменён до отказа одной записи | Управляемые Promise, их отказы перехвачены стендом; реальных записей нет |
| Общий маршрут | Группы 13/14 | isEditable=false останавливает Drop; Item попадает в override; результат базового dispatcher null; hook dropItemSheetData не вызван; Actor даёт TypeError | DragDrop/fromDropData/UI подменены |

## Непроверенные участки и открытые вопросы

Все 54 строки прочитаны. Реальные ACL, несколько клиентов, Drop компедиума с загрузкой, отказ сетевого обновления и удаление контейнера в мире не выполнялись. Имеющийся isEditable относится к листу назначения; проверка isOwner источника собственным кодом отсутствует, но это не доказательство обхода серверных прав.

## Связанные проблемы

[issue-00034](../../../../../../issues/potential/issue-00034.md), [issue-00058](../../../../../../issues/potential/issue-00058.md), [issue-00059](../../../../../../issues/potential/issue-00059.md), [issue-00156](../../../../../../issues/potential/issue-00156.md), [issue-00157](../../../../../../issues/potential/issue-00157.md), [issue-00158](../../../../../../issues/potential/issue-00158.md), [issue-00159](../../../../../../issues/potential/issue-00159.md), [issue-00161](../../../../../../issues/potential/issue-00161.md), [issue-00162](../../../../../../issues/potential/issue-00162.md), [issue-00163](../../../../../../issues/potential/issue-00163.md). 34 сопоставлена по ожиданию, но причина двух update здесь отдельная (157). Для 58 собственный Item-обработчик существует; проблема Actor/Folder сохраняется. 59 — унаследованный пропуск hook.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `66cd03705dbc398eba0026284a298b5fbe337035`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003024) |
