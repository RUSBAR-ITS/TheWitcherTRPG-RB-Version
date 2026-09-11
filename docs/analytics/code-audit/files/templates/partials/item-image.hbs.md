# templates/partials/item-image.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/item-image.hbs](../../../../../../templates/partials/item-image.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.011](../../../../../tasks/task-0003.011.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.011](../../../review-log.md#task-0003011) |

## Назначение файла

Фрагмент картинки предмета в списке с условной кнопкой увеличения .item-show. В исследованном дереве его единственный прямой шаблон-потребитель — прежний список брони монстра.

## Условия использования

Предзагружается [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js). Включается из [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../templates/partials/monster/monster-inventory-tab.hbs) с item=armor; этот список подключён в прежнем [templates/sheets/actor/monster-sheet.hbs](../../../../../../templates/sheets/actor/monster-sheet.hbs). У текущего зарегистрированного MonsterSheet PARTS.inventory указывает на новый tab-inventory, который использует другие списки. Предзагрузка сама по себе не доказывает отображение partial в текущем листе.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| item-img-wrapper / a.item-show | 1–5 | Обёртка с увеличением картинки | Только разрешённый CSV-тип и item.system.clickableImage | Клик обрабатывает itemMixin листа Actor |
| img.item-img.dragable | 4/7 | Картинка для строки инвентаря | Есть в обеих ветвях; draggable=true, data-id=item._id | Имя класса в файле — dragable, с одной g; не тождественно .draggable |
| item.img / item._id / item.type / system.clickableImage | 1–7 | Контекст partial | Передаётся потребителем | Сам шаблон не меняет данные |

## Основные функции и методы

JavaScript-функций нет. Шаблон вычисляет условия Handlebars и создаёт разметку; обработчики и запись документов принадлежат указанным ниже файлам.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| getSetting/includes | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Helpers | 1; проверка CSV-типа | Исходные helpers исполнены |
| clickableImageItemTypes | [module/setup/settings.js](../../../../../../module/setup/settings.js) | World setting | 1; default valuable | Точный CSV, не поиск подстроки |
| item=armor | [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../templates/partials/monster/monster-inventory-tab.hbs) | Контекст | 83; передаёт Item в строке tbody.item[data-item-id] | Точечное чтение 75–96 |
| clickableImage | [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js); [templates/partials/item-header.hbs](../../../../../../templates/partials/item-header.hbs) | Поле из формы | 1; определяет показ ссылки | В проверенных моделях отсутствует; вручную заданные данные матрицы не означают сохранённое поле |
| itemListener / _onItemShow | [module/actor/sheets/mixins/itemMixin.js](../../../../../../module/actor/sheets/mixins/itemMixin.js) | CSS selector → click | 319→156–174; берёт itemId из внешнего .item, открывает Dialog с img | Исходный _onItemShow исполнен с подменой Dialog; картинки не загружались |
| Подключение itemListener | [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | Вызов из activateListeners | V2:235, V1:214; одинаковая примесь | Прочитаны точки подключения; нет вывода о текущей доступности старого шаблона |
| .item-img-wrapper/.item-show | [styles/tab-inventory.css](../../../../../../styles/tab-inventory.css) | CSS | 199–219; наложение и hover кнопки | Селекторы найдены; визуальный рендер не проверен |
| Текущая PARTS.inventory | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | Контроль достижимости | 44–46 → новые общие списки | В них вызова item-image не найдено |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Путь шаблона | Предзагрузка:52 | Наличие ресурса, не его рендер |
| [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../templates/partials/monster/monster-inventory-tab.hbs) | item-image с item=armor | Прямое включение:83 | Единственное найденное включение в templates |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../module/actor/sheets/mixins/itemMixin.js) | .item-show | Подписка click на доступной разметке | Исходный listener существует; в новых списках ссылки нет |

## Данные и изменения состояния

Ветви всегда выводят img src=item.img с data-id=item._id; увеличение добавляет обёртку и ссылку. Ключ для поиска предмета обработчик берёт с внешней строки data-item-id, а не с data-id картинки. Сам partial не объявляет dragstart handler и не редактирует img. _onItemShow формирует Dialog со статическим HTML картинки, без записи Item; по исходнику event.preventDefault упомянут без вызова, но навигационное последствие для этой ссылки без href не установлено.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Условия | 4 Handlebars-рендера: разрешённый тип×флаг | item-show только при true/true; картинка присутствует всегда | Контролируемые флаги; не сохранённый Item |
| Просмотр | Исходный _onItemShow с внешней строкой item1 | Создан Dialog title=Armor и img a.png; вызван stopPropagation | Dialog/Actor collection подменены; браузер не запускался |
| Достижимость | rg по module/templates + текущие регистрации/PARTS | Один прямой потребитель, связанный с прежним monster-sheet; текущий инвентарь другой | Пользовательские/модульные листы не обследовались |

## Непроверенные участки и открытые вопросы

Все 8 строк прочитаны. Не установлена достижимость прежнего monster-sheet.hbs через внешние модули или пользовательский лист. Не проверялся реальный dragstart этой разметки; атрибут draggable сам по себе не определяет передаваемый документ. Для текущего инвентаря найден разрыв маршрута, а не отсутствие самой функции просмотра.

## Связанные проблемы

[issue-00063](../../../../../issues/potential/issue-00063.md) — флаг не объявлен в модели, единственный потребитель partial не относится к текущим PARTS инвентаря.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.011 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Полностью разобран единственный найденный inventory-потребитель — прежний monster-inventory-tab.hbs. Современные восемь таблиц используют свои img/кнопки раскрытия; .item-show и clickableImage отсутствуют. Старый partial отрендерен с CSV-настройкой; запись модели и реальное увеличение картинки не запускались.

Связанные шаблоны: [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../templates/partials/monster/monster-inventory-tab.hbs). [Проверки и ограничения](../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.
