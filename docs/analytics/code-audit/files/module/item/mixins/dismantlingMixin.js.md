# module/item/mixins/dismantlingMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/mixins/dismantlingMixin.js](../../../../../../../module/item/mixins/dismantlingMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.034](../../../../../../tasks/task-0003.034.md), 5 файлов, 251 логическая строка |
| Запись перекрёстной сверки | [TASK-0003.034](../../../../review-log.md#task-0003034) |

## Назначение файла

Примесь Item для разбора оружия или брони по связанному рецепту, выдачи компонентов, списания одной единицы и формирования сообщения.

## Условия использования

dismantlingMixin подключён к WitcherItem через import/Object.assign. Внутренний UI-вход — itemContextMenu.dismantableItem/isItemDismantable/dismantleItem. На Foundry 14 этот вход блокируется несовпадением аргументов callback (issue-00168); проверки основной операции здесь выполнены прямым вызовом настоящего метода, без исправления меню.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| dismantableItemTypes | Локальная const; 1 | ['weapon','armor'] | Не экспортируется | Проверяет только canBeDismantled |
| dismantlingMixin | Именованный экспорт; 3–64 | Три метода Item | WitcherItem.prototype | Сам импорт не изменяет инвентарь |
| components / foundItems / unfoundItems | Локальные массивы; 11–34,48–49 | Результаты разбора | Контекст чата/возвращаемое значение | Resolved-ветвь отличается структурой от name-only |
| Callback map / async map / forEach | 11–18;21–32;36 | Нормализовать количество, разрешить UUID, начать выдачу | Внутри dismantle | UUID ожидаются Promise.all; выдача через forEach не ожидается |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| canBeDismantled() | this.type, system.associatedDiagramUuid | false либо значение associatedDiagramUuid (в том числе пустая строка) | includes(type) && uuid | Не строго Boolean; не проверяет наличие рецепта, parent или quantity |
| dismantle() | this.system.associatedDiagramUuid, parent.addItem/removeItem; рабочий UUID API | Promise массива components | await recipe; map требований → половина с минимумом 1; await Promise.all UUID; add найденных; remove(id,1); запустить сообщение; вернуть массив | Нет собственного вызова canBeDismantled и проверки quantity. Отсутствующий recipe/craftingComponents даёт TypeError до записей; resolver rejection передаётся. Add/remove/message без await/return. |
| createDismantleMessage(components) | Массив с item или name; this.actor | Promise<undefined> | filter found/unfound; await renderTemplate; ChatMessage.getSpeaker({actor:this.actor}); style OTHER; ChatMessage.create | Render ожидается, создание ChatMessage не ожидается. Метод не подтверждает завершение выдачи и не меняет количество сам. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| associatedDiagramUuid; unwrapAssociatedDiagram | [module/data/item/templates/associatedDiagramData.js](../../../../../../../module/data/item/templates/associatedDiagramData.js) | данные/связь модели | 5,9 | dismantle разрешает UUID заново, не использует prepared associatedDiagram |
| WeaponData / ArmorData | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js); [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js) | модели источника | Типы weapon/armor и поле associatedDiagramUuid | Схемы передают associatedDiagramUuid, quantity наследуется |
| DiagramData.craftingComponents; craftingComponent | [module/data/item/diagramData.js](../../../../../../../module/data/item/diagramData.js); [module/data/item/templates/craftingComponentData.js](../../../../../../../module/data/item/templates/craftingComponentData.js) | рецепт и требования | 11–18 | name/uuid/quantity; у quantity initial0; prepareDerivedData обогащает имя, сохраняя его при null UUID |
| fromUuid | Foundry 14.367.0: глобальный асинхронный UUID API | разрешение | 9,23 | В тестах карта UUID возвращает Item/null или отклоняет Promise; реальный pack не загружался |
| Math.max / Math.floor / Promise.all | JavaScript | вычисление и асинхронность | 16,20–32 | max(1,floor(quantity/2)); ожидание всех UUID до любых записей |
| WitcherActor.addItem / removeItem | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | изменение инвентаря | 36,38; методы Actor:259–283 | Настоящие тела; create/update/delete заменены. Add объединяет по name/type, не UUID, remove списывает одну единицу |
| CommonItemData.quantity | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | количество источника | removeItem; canBeDismantled quantity не читает | StringField без положительного минимума |
| dismantle.hbs | [templates/chat/item/dismantle.hbs](../../../../../../../templates/chat/item/dismantle.hbs) | renderTemplate | 46–55 | Передаёт item:this, foundItems, unfoundItems; полного preload этого HBS в setup/handlebars нет |
| renderTemplate / ChatMessage.getSpeaker / ChatMessage.create / CONST.CHAT_MESSAGE_STYLES.OTHER | Foundry 14.367.0 | чат | 51–62 | HBS и тело getSpeaker настоящие, получение HTML/создание чата перехвачены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | dismantlingMixin | import:7; Object.assign:374 | Все три функции прототипа совпадают с экспортом |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | canBeDismantled / dismantle | isItemDismantable:165; dismantleItem:171 | Неверный callback-порядок .168 сохранён; прямой корректный вызов обёртки не ждёт dismantle |
| [templates/chat/item/dismantle.hbs](../../../../../../../templates/chat/item/dismantle.hbs) | components → foundItems/unfoundItems | Контекст отображения | HBS читает component.item.img/name либо component.name; quantity/UUID не выводит |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Каждая строка craftingComponents даёт max(1,floor(quantity/2)): −2/0/1/2/3 → 1, 4/5 → 2, 6 → 3. Это зафиксированный алгоритм с комментарием «half…minimum 1», не сверка игровых правил. Количество стопки исходного оружия/брони не умножает выход: всегда запрашивается removeItem(id,1).

Без UUID остаётся {name,uuid,quantity}, материал не ищется по имени и не создаётся, но попадает в сообщение неизвестных. С UUID результат становится {item:resolved,quantity}; name/uuid теряются, даже если resolved=null. Такая запись относится к unfoundItems, но HBS уже нечего вывести как имя. Пустой рецепт и полностью неизвестные материалы всё равно сопровождаются списанием исходного предмета.

После всех разрешений найденные элементы независимо запускают parent.addItem. Затем стартуют удаление источника и сообщение, не ожидая их завершения. При исходной стопке Iron=5 и двух строках выхода по 2 обе операции при задержке update отправляют 7; в фасаде итог 7, не 9. Это пример конкурентных запросов, не доказанная гонка БД. При quantity источника 0/−1 прямой метод всё равно выдаёт материалы, а removeItem удаляет источник.

Не предусмотрены диалог подтверждения/отмена, проверка документа рецепта/типа результата UUID и компенсация частичного сбоя. Ошибку резолвера до выдачи проверили; отказ реальной записи и серверный откат не запускались.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Допуск/меню | Группа 10 | canBeDismantled возвращает UUID для weapon, '' без UUID, false для component; callback меню даёт TypeError до resolve | Порядок callback сверён с core context-menu.mjs:611–624; браузер не запускался |
| Выход/количество | Группы 11–12,16 | Смешанные найденные/неизвестные; половина с минимумом; источник 3→2, 9→8; 0/−1 тоже дают материалы | Штатный UI разбора блокирован issue-00168 |
| Недоступные ссылки | Группы 13–15 | Null/пустой/неподходящий рецепт или rejection до записей; null компонент теряет имя и источник списывается; name-only сохраняет имя | UUID API подменён |
| Порядок | Группы 17–19 | dismantle возвращает при pending add/remove/render; helper возвращает при pending chat; две выдачи в одну стопку отправляют [7,7] | Управляемые Promise, без сервера |
| Сообщение | Группы 11,20 | OTHER, speaker Actor; раздельные списки; количества не выводятся | HTML отрендерен в изоляции |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Проверки выполнены в Node 24.16.0 с установленным кодом Foundry 14.367.0. Использованы реальные модели и методы системы; Application/Document-оболочки, DOM, UUID-резолвер, запись документов и чат заменены фасадами. Мир, браузер, HTTP и БД не запускались. Точные границы и сценарии приведены в журнале .034; чтение соседних определений не засчитывается как их новый полный разбор. Новые наблюдения основной операции относятся к прямому вызову и будущему исправленному входу меню; доступность из текущего клика не утверждается.

## Связанные проблемы

[issue-00168](../../../../../../issues/potential/issue-00168.md), [issue-00214](../../../../../../issues/potential/issue-00214.md), [issue-00215](../../../../../../issues/potential/issue-00215.md), [issue-00216](../../../../../../issues/potential/issue-00216.md), [issue-00217](../../../../../../issues/potential/issue-00217.md). Новые issues разделяют ожидание операций, отсутствие проверки рецепта, потерю имени и нулевой запас. Исправления не выполнялись.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003034) |
