# templates/sheets/actor/partials/loot/loot-item-display.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/loot/loot-item-display.hbs](../../../../../../../../../templates/sheets/actor/partials/loot/loot-item-display.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `1d29f681ffed1c46b9c05b0eff09935300c3bf7d` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.035](../../../../../../../../tasks/task-0003.035.md), 6 файлов, 384 логические строки |
| Запись перекрёстной сверки | [TASK-0003.035](../../../../../../review-log.md#task-0003035) |

## Назначение файла

Одна строка Item в любой из шести таблиц loot: редактирование, изображение, количество/имя/вес/цена, покупка, удаление и GM-кнопка скрытия.

## Условия использования

Шесть each в loot-sheet.hbs передают item и isGM; файл предварительно загружается setup/handlebars. if isHidden выбирает hidden-view для GM и hidden-from-view для остальных, но всегда создаёт содержимое строки.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| tr.item / data-item-id | 1–9 | ID embedded Item и представление hidden | Контекст item._id | CSS class; не удаление документа и не сокрытие данных |
| img.item-img.dragable / draggable / data-id | 11 | Картинка и заявленный drag | HTML | Селектор ядра .draggable не совпадает; ядро ждёт dataset.itemId |
| input.inline-edit / data-field | 12–17 | system.quantity, name, system.weight, system.cost | itemMixin | Все type=text; quantity/cost data-dtype=Number, но listener передаёт строку |
| a.item-edit / item-delete / buyItem / hideItem | 10,19–22 | Открыть/удалить/купить/скрыть | Listeners либо data-action | hideItem только при isGM; остальные anchors без проверки роли |

## Основные функции и методы

JS определений нет. if/else/each-context задают строку. quantity/name/weight/cost поля не имеют name и сохраняются через _onItemInlineEdit по data-field; helper не валидирует диапазон. _onItemBuy/_onItemHide получают element.closest('.item').dataset.itemId. CSS скрывает nonGM-строку целиком.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| item, isGM | [module/actor/sheets/WitcherLootSheet.js](../../../../../../../../../module/actor/sheets/WitcherLootSheet.js) | контекст и actions | 1–25 | _prepareContext, _onItemBuy, _onItemHide |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../../../module/data/item/commonItemData.js) | поля | isHidden/quantity/weight/cost | quantity:String; остальное Number/Boolean |
| _onItemEdit/_onItemDelete/_onItemInlineEdit/itemListener | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | jQuery listeners | item-edit/item-delete/inline-edit | 128–145,147+,312+; Number dtype в этом handler не преобразует значение |
| .hidden-view / .hidden-from-view | [styles/loot-sheet.css](../../../../../../../../../styles/loot-sheet.css) | CSS | 3,5 | silver / display:none; hidden item.name остаётся в HTML |
| ActorSheetV2._dragDrop / _onDragStart | Foundry /opt/foundryvtt/client/applications/sheets/actor-sheet.mjs | селектор/drag payload | img11 и row data-item-id | 81–95 .draggable,225–237 dataset.itemId/effectId; контролируемый вызов с data-id не создаёт payload |
| Handlebars if и escaping | Handlebars 4.7.9 | рендер | item.name,img,quantity и условия | Обычные {{}} экранируют, локализации в файле нет |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/actor/loot-sheet.hbs](../../../../../../../../../templates/sheets/actor/loot-sheet.hbs) | loot-item-display | Шесть each, item/isGM | 89–125 |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | loot-item-display | preload48 | Файл входит в список шаблонов |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Только разметка. isHidden=true не исключает запись из context или DOM: меняется класс. Inline edit изменяет Item независимо от формы Actor. qty='0.5' сохранился строкой в настоящей модели с перехватом update. Сравнивать dragable и draggable буквально: native draggable=true само по себе не формирует Foundry UUID-пакет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| GM/nonGM | 04,15,23 | Одна скрытая строка, 1buy, GM1hide/nonGM0hide; flag меняется после разрешения записи | CSS проверен статически; права БД отдельно |
| Drag | 18 | 0 элементов .draggable; img data-id без itemId. Core _onDragStart не вызвал setData; контроль с itemId вызвал | Настоящее тело core с фасадом event; реальное перетаскивание не выполнялось |
| Изменение | 21 | quantity0.5 передано/сохранено строкой | Сервер не запускался |

## Непроверенные участки и открытые вопросы

Исполнены настоящие методы системы и модели Foundry 14.367.0 в изолированном Node 24.16.0. Коллекции документов, окна, запись и базовый Application — фасады; HBS — настоящий Handlebars 4.7.9, разбор HTML — parse5. Полный клиент, DOM-события, сервер, права реальной БД, сетевые гонки и сохранение мира не проверялись. Пути systems/TheWitcherTRPG сохранены как в исходниках; доступ по HTTP здесь не проверялся.

## Связанные проблемы

[issue-00168](../../../../../../../../issues/potential/issue-00168.md), [issue-00220](../../../../../../../../issues/potential/issue-00220.md), [issue-00221](../../../../../../../../issues/potential/issue-00221.md), [issue-00223](../../../../../../../../issues/potential/issue-00223.md). Контекстное меню issue168 подключено листом; обычный buyItem action использует правильный порядок (event,element) и не блокируется той ошибкой. Скрытие завершает Promise до записи; отдельной транзакции покупки это не обеспечивает.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; полный файл | Первая карточка; [сверка порции](../../../../../../review-log.md#task-0003035) |

## Дополнительная сверка TASK-0003.048

2026-09-12, rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670; исходники не изменены.

Полный [styles/loot-sheet.css](../../../../../../../../../styles/loot-sheet.css) подтвердил silver для table tr.hidden-view и display:none для hidden-from-view. Группа 13 повторила реальные Loot/clue/obstacle partial: скрытый Item остаётся в HTML; isGM меняет CSS-класс. Это представление, не проверка прав доступа. Размеры боковой области Loot и крайних ячеек mystery описаны в CSS-карточке; данные/методы покупки не переисполнялись.

[Сценарии, результаты и ограничения](../../../../../../review-log.md#task-0003048). Связанные файлы повторно не засчитываются в покрытие.
