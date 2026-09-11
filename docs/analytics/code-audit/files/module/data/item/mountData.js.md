# module/data/item/mountData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/mountData.js](../../../../../../../module/data/item/mountData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `1d29f681ffed1c46b9c05b0eff09935300c3bf7d` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.035](../../../../../../tasks/task-0003.035.md), 6 файлов, 384 логические строки |
| Запись перекрёстной сверки | [TASK-0003.035](../../../../review-log.md#task-0003035) |

## Назначение файла

Схема Item mount с dex/control/speed/hp поверх восьми общих полей Item. Это запись предмета; собственной связи с Actor верхового животного или автоматических бросков здесь нет.

## Условия использования

registerDataModels импорт8 и CONFIG.Item.dataModels.mount55; system.json объявляет Item mount. Импорт только определяет класс, defineSchema вызывается при построении модели.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| MountData | default class:5–19 extends CommonItemData | Схема mount | CONFIG.Item.dataModels.mount | Конструирование/валидация |
| fields | const:3 | foundry.data.fields | Локальное имя | Фабрики полей |
| dex / control / speed | StringField:13–15, initial:'' | Три текстовых параметра | system.dex/control/speed | Число6→'6'; '2d6' и '' остаются строками |
| hp | NumberField:16 initial:0 | Одно число HP | system.hp | Нет value/max или min/max/integer; 0,−2.5 допустимы схемой |
| commonData | локальное:9 и spread12 | Восемь унаследованных полей | defineSchema | description,quantity,weight,cost,sourcebook,isHidden,isStored,isCarried |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema():7–18 | super.defineSchema() | 12 полей | Spread общих + четыре собственных | Не обновляет Actor; дополнительных prepare/migrate нет |
| Унаследованные calcWeight / canHaveTemporaryItemImprovement / canBeRepaired | CommonItemData | quantity×weight либо0; false; false | Учитывает carried/stored | HP на вес и состояние Actor здесь не влияет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | прямой импорт/наследование | 1,5,9 | Восемь полей и три inherited метода |
| StringField / NumberField | Foundry /opt/foundryvtt/common/data/fields.mjs | схема | 3,13–16 | Настоящие TypeDataModel и fields; тест01 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | MountData | import8, ключ mount55 | Регистрация схемы |
| [templates/sheets/item/mount-sheet.hbs](../../../../../../../templates/sheets/item/mount-sheet.hbs) | dex/control/speed/hp + общие поля | Форма system.* | 14–17 |
| [module/actor/sheets/WitcherLootSheet.js](../../../../../../../module/actor/sheets/WitcherLootSheet.js) | mount, quantity/cost/weight/isHidden | getList('mount'), покупка | 55,75–169; не читает специальные dex/hp |
| [module/item/sheets/WitcherMountSheet.js](../../../../../../../module/item/sheets/WitcherMountSheet.js) | Item mount | Косвенно item.system.schema и контекст базового листа | WitcherItemSheet._prepareContext |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

description/quantity/sourcebook текст, cost/weight числовые, hidden/stored/carried Boolean. hp не ограничен диапазоном и не является DerivedStatData. При hp=0 Item остаётся в loot и доступен покупателю; код модели не объявляет животное мёртвым и не синхронизирует HP с Actor. Текстовые speed/control/dex сохраняют формулы как строки, не вычисляют Roll. inherited calcWeight при qty2,weight3 даёт6.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Реальная схема | 01,20 | 12 полей, строки/числа/пустые/нулевойHP; hp='bad' отклонён; hp−2.5 допустим; форма сохраняет типы | Не правила игры |
| Consumer search | rg MountData/mount/system.dex/control/speed/hp | Регистрация, форма, getList; нет собственного actorUUID или методов связи | Макросы/модули/БД не исследовались |

## Непроверенные участки и открытые вопросы

Исполнены настоящие методы системы и модели Foundry 14.367.0 в изолированном Node 24.16.0. Коллекции документов, окна, запись и базовый Application — фасады; HBS — настоящий Handlebars 4.7.9, разбор HTML — parse5. Полный клиент, DOM-события, сервер, права реальной БД, сетевые гонки и сохранение мира не проверялись. Пути systems/TheWitcherTRPG сохранены как в исходниках; доступ по HTTP здесь не проверялся. Общие свойства относятся к контракту Item, не к правилам верхового боя. Поля dex/control/speed могут содержать текст; автоматически объявлять это ошибкой нельзя.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md). clickableImage отсутствует и в этой модели; общий header может показать checkbox при настройке типа mount. Отдельная неисправность mount HP=0 не установлена.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003035) |
