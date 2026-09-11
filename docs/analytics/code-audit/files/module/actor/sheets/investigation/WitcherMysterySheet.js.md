# module/actor/sheets/investigation/WitcherMysterySheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/investigation/WitcherMysterySheet.js](../../../../../../../../module/actor/sheets/investigation/WitcherMysterySheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `538dbac9bb9432c123fe4f3c00ab788b58517afb` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.023](../../../../../../../tasks/task-0003.023.md), 14 файлов, 449 логических строк |
| Запись перекрёстной сверки | [TASK-0003.023](../../../../../review-log.md#task-0003023) |

## Назначение файла

Лист Actor-тайны на ApplicationV2. Готовит списки улик/препятствий, добавляет и редактирует embedded Items, переключает видимость строк и запускает rollClue.

## Условия использования

registerSheets регистрирует WitcherMysterySheet по умолчанию для mystery. Наследует HandlebarsApplicationMixin(ActorSheetV2). Единственная PARTS.header содержит весь mystery-sheet.hbs; TABS пуст. Конструктор и обработчик формы унаследованы. Отсутствие mystery в манифесте сохраняется.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| rollClue | Named import, 1 | Проверка улики | Локальная функция | Вызов из _onRollClue |
| HandlebarsApplicationMixin / ActorSheetV2 | const, 3–4 | База листа | Foundry applications | Наследование |
| WitcherMysterySheet | default class, 6–115 | Лист тайны | Actor.mystery | Открытие/контекст/действия |
| DEFAULT_OPTIONS | static, 8–25 | 1120×600; classes witcher/sheet/actor | form и actions | submitOnChange=true; closeOnSubmit=false |
| actions.addItem/editItem/deleteItem/hideItem/rollClue | 18–24 | Соответствие data-action методам | Делегирование ApplicationV2 | Методы вызываются с this листа |
| PARTS.header / TABS | 27–33 | Одна основная часть, без вкладок | HandlebarsApplicationMixin | Загрузка HBS |
| actor/system/clues/obstacles/isGM/skills | _prepareContext, 39–47 | Контекст документа, списков и словаря навыков | HBS | system из toObject(false); actor — сам документ |
| change listener | _onRender, 55–57 | Inline-редактирование | Каждый .inline-edit | bind(this) → _onInlineEdit |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options) | Лист с document; super._prepareContext | Контекст HBS | await super; toObject(false); getList('clue'/'obstacle'); game.user.isGM; CONFIG.WITCHER.skillMap | Не пишет Actor/Item |
| _onRender(context,options) | Отрендеренный element | undefined | Вызывает super и добавляет change на .inline-edit | Promise async super не ожидает; внешний жизненный цикл целиком не запускался |
| static async _onItemAdd(event,element) | dataset.itemtype; this.actor | Promise<undefined> после Item.create | preventDefault; {name:'new '+type,type}; parent=this.actor | Ожидает создание; нет собственного фильтра типа/прав |
| static _onItemEdit(event,element) | closest('.item').dataset.itemId | undefined | Находит только this.actor.items.get(id); sheet.render(true) | Нет guards отсутствующей строки/Item; render не возвращает |
| static async _onItemDelete(event,element) | Локальный Item ID | Promise результата delete() | preventDefault; get(id).delete() | Ожидает удаление; нет подтверждающего диалога или guards |
| static _onItemHide(event,element) | Локальный Item ID | undefined | update({'system.isHidden':!item.system.isHidden}) | Не ожидает/возвращает Promise записи |
| _onInlineEdit(event) | currentTarget с value, data-field и строкой Item | Результат item.update | Берёт поле из dataset.field; значение из element.value; преобразует строки false/true/checked | 'false' → true, 'true'/'checked' → false; преобразование применяется и к text/number/multi-select, не проверяет тип элемента |
| static _onRollClue(event,element) | Локальный Item ID | undefined | get(id) → rollClue(clue) | Не ожидает результат, не перехватывает отказ; preventDefault не вызывается |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| rollClue | [module/scripts/investigation/rollClue.js](../../../../../../../../module/scripts/investigation/rollClue.js) | ES named import | _onRollClue:113 | Полный разбор функции; группы 06–10/15 |
| WitcherActor.getList | [module/actor/witcherActor.js](../../../../../../../../module/actor/witcherActor.js) | Метод документа | _prepareContext:43–44 | 250–257: filter по типу и !isStored, сортировка sort; скрытие не фильтруется |
| MysteryActorData, ClueData, ObstacleData | [module/data/investigation/mysteryActorData.js](../../../../../../../../module/data/investigation/mysteryActorData.js); [module/data/investigation/clueData.js](../../../../../../../../module/data/investigation/clueData.js); [module/data/investigation/obstacleData.js](../../../../../../../../module/data/investigation/obstacleData.js) | Контракт данных | Контекст, создание, isHidden/data-field | Модели разобраны целиком |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Реестр через CONFIG | _prepareContext:47 | Словарь label/name/attribute |
| mystery-sheet.hbs | [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../../../templates/sheets/investigation/mystery-sheet.hbs) | PARTS.header | 29 | Все имена actions/полей сверены |
| HandlebarsApplicationMixin / ActorSheetV2 / Item.create / Document API | Foundry 14.367.0, client/applications/sheets/actor-sheet.mjs; api/document-sheet.mjs; api/application.mjs; common/abstract/document.mjs | Наследование/CRUD/права | Базовая форма, события, create/update/delete | UI и записи в сценариях заменены фасадами; владелец — Actor |
| game.user.isGM / isEditable | Foundry 14.367.0 User; DocumentSheetV2._onRender:269–272 | Права/показ | Флаг GM для HBS; базовый лист отключает ввод для не editable | Скрытие кнопки не заменяет разрешения Document API |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../../module/setup/registerSheets.js) | WitcherMysterySheet | Импорт/регистрация mystery | 8; 118–121 |
| [templates/sheets/investigation/mystery-sheet.hbs](../../../../../../../../templates/sheets/investigation/mystery-sheet.hbs) | actor/system/clues/obstacles/isGM/skills и addItem | Основная форма | Контекст из _prepareContext |
| [templates/sheets/investigation/partials/clue-display.hbs](../../../../../../../../templates/sheets/investigation/partials/clue-display.hbs) | editItem/deleteItem/hideItem/rollClue; inline-edit | Строка улики | Локальный data-item-id |
| [templates/sheets/investigation/partials/obstacle-display.hbs](../../../../../../../../templates/sheets/investigation/partials/obstacle-display.hbs) | editItem/deleteItem/hideItem; inline-edit | Строка препятствия | Локальный data-item-id |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

getList возвращает документы, а не копии и не только видимые записи. actorData.system — сериализованный снимок, но основной HBS читает actor.system; списки содержат live Items. add/delete ожидают API; inline возвращает update; hide/roll не возвращают свои асинхронные продолжения. Для записи используется локальный ID внутри this.actor.items; UUID другого Actor по этому маршруту не разрешается. Права на данные обеспечивает Foundry; GM-условия HBS отвечают только за кнопки удаления/скрытия.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст/сортировка | Группы 03/11/12 | Пустые и несколько записей обработаны; isHidden остаётся в списке; формы показывают корректные выбранные навыки | База листа и DOM заменены |
| CRUD и события | Группы 13/15 | Item.create получает parent Actor; add/delete ждут управляемый Promise; edit render(true); hide не ждёт; rollClue вызывается для локального Item | Реальные документы не изменялись |
| Inline value | Группа 14 | Строки false/true/checked превращаются в bool; обычные строки и массив навыков передаются дальше | Проверен payload до очистки реальным Item.update |

## Непроверенные участки и открытые вопросы

Все 115 строк прочитаны. Не проверялись браузерный submitOnChange, повторный рендер, фактический доступ observer/owner к API и сохранение встроенных Items. Унаследованная внешняя форма и собственный <form> в PARTS отмечены как структура: сбой отправки из этого факта не выводится.

## Связанные проблемы

[issue-00005](../../../../../../../issues/potential/issue-00005.md), [issue-00148](../../../../../../../issues/potential/issue-00148.md), [issue-00149](../../../../../../../issues/potential/issue-00149.md), [issue-00151](../../../../../../../issues/potential/issue-00151.md), [issue-00152](../../../../../../../issues/potential/issue-00152.md), [issue-00153](../../../../../../../issues/potential/issue-00153.md), [issue-00154](../../../../../../../issues/potential/issue-00154.md), [issue-00155](../../../../../../../issues/potential/issue-00155.md). 5 — доступность типа; остальные связаны с цепочкой броска, асинхронностью, inline-преобразованием и основной формой.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `538dbac9bb9432c123fe4f3c00ab788b58517afb`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003023) |
