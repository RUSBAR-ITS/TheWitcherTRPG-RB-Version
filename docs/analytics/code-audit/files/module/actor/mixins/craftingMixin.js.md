# module/actor/mixins/craftingMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/craftingMixin.js](../../../../../../../module/actor/mixins/craftingMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.034](../../../../../../tasks/task-0003.034.md), 5 файлов, 251 логическая строка |
| Запись перекрёстной сверки | [TASK-0003.034](../../../../review-log.md#task-0003034) |

## Назначение файла

Примесь Actor с тремя способами найти компоненты: по ключу вещества, имени и UUID происхождения из компедиума.

## Условия использования

Именованный экспорт craftingMixin подключён к WitcherActor через import и Object.assign. getSubstance используют лист и алхимическое изготовление; findNeededComponent — ремесло, ремонт и helper количества. В module/templates не найден вызов findComponentByUuid вне определения: этот метод доступен через Actor, но действующий внутренний потребитель не установлен.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| craftingMixin | Экспорт объекта; 1–45 | Три метода поиска | WitcherActor.prototype | Импорт не ищет предметы и не меняет документы |
| getSubstance / findNeededComponent / findComponentByUuid | Методы; 2–6,15–40,42–44 | Поиск по разным критериям | Смешаны в Actor | Возвращают реальные ссылки на Item; не копируют и не сохраняют данные |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| getSubstance(name) | Ключ из девяти веществ; this.getList | Массив Item | getList('component'), затем system.type=='substances', substanceType==name, !isStored | Порядок sort задаёт getList; нулевые количества не исключаются. Не локализует name; неизвестный ключ даёт [] |
| findNeededComponent(componentName) | Имя или локализованное имя вещества; this.items, game.i18n | Массив Item | Тип component; item.name==componentName либо совпадение перевода с нужным substanceType | Нет фильтра isStored/quantity и сортировки; сохранён порядок коллекции. Сравнение имён учитывает регистр/пробелы, применяется JS == |
| findComponentByUuid(uuid) | UUID происхождения; getList('component') | Первый Item либо undefined | find(c => c?._stats.compendiumSource === uuid) | Порядок sort, stored исключён; quantity не проверяется. Не вызывает fromUuid и не сравнивает Item.uuid. Предполагает штатный _stats у Item. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherActor.getList; items | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | вызов/коллекция | 3,16,43; getList:250–257 | getList фильтрует тип/!isStored и сортирует sort |
| ComponentData.type/substanceType | [module/data/item/componentData.js](../../../../../../../module/data/item/componentData.js) | чтение модели | 4,18–38 | StringField без choices; отличать Item.type='component' и system.type='substances' |
| CommonItemData.quantity/isStored | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | данные | getList и поиск имени | quantity:StringField не задаёт положительный минимум |
| game.i18n.localize | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | локализация | 21–38: Inventory.Vitriol/Rebis/Aether/Quebrith/Hydragenum/Vermilion/Sol/Caelum/Fulgur | Девять переводов проверены для en/ru; это текущая локаль, не произвольный перевод |
| _stats.compendiumSource | Foundry 14.367.0, common/data/fields.mjs:4039, DocumentStatsField | метаданные Item | 43 | DocumentUUIDField источника компедиума; тестовые значения _stats заданы фасадом, миграция/импорт ядра не выполнялись |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | craftingMixin | import:16, Object.assign:451 | Совпадение трёх методов прототипа проверено |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | getSubstance; findNeededComponent | _prepareSubstances:220–237; _alchemyCraft:276; _craftingCraft:368 | Полный контекст и обычный callback изготовителя исполнены |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | getSubstance; findNeededComponent | realCraft:199–202 | Выбор по isAlchemicalCraft, без применения findComponentByUuid |
| [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | findNeededComponent | prepareData:35 берёт [0] | Если не найдено имя, отдельно разрешает UUID отсутствующего материала |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | findNeededComponent | getOwnedComponentCount:90–91 + sum('quantity') | Helper исполнен на двух одноимённых стопках |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Методы не пишут документы. Возвращаемые Items могут затем списываться потребителем. getSubstance('vitriol') и findNeededComponent(локализованный Vitriol) не эквивалентны: второй может вернуть stored и совпавший по имени компонент другого подтипа. Ни один не отбрасывает quantity=0. UUID-поиск не является резервной ветвью поиска имени и сам по себе не участвует в изготовлении.

Девять соответствий: Vitriol→vitriol, Rebis→rebis, Aether→aether, Quebrith→quebrith, Hydragenum→hydragenum, Vermilion→vermilion, Sol→sol, Caelum→caelum, Fulgur→fulgur. В findNeededComponent левая часть — результат game.i18n.localize('WITCHER.Inventory.<название>'), а не буквальное английское имя. Совпадение собственного имени предмета проверяется отдельно и может сработать независимо от языка.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Разные критерии | Группы 01–04 | getSubstance исключает stored и сортирует; имя включает stored/quantity0 и порядок коллекции; UUID находит первый по compendiumSource | _stats и инвентарь — контролируемые данные, не импорт реального pack |
| Локали | Группа 03 | Все девять веществ найдены по переводам en и ru | Другие языки не исследованы |
| Потребители | Группы 02,08–09 | Helper считает 3; ремесло списывает 2+3 из двух стопок, включая stored; алхимия использует только вещество вне хранения | Записи перехвачены, изготовление не выполнено в мире |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-03](../../../../cross-check-0002.md#u007-03), [U007-06](../../../../cross-check-0002.md#u007-06), [U007-02](../../../../cross-check-0002.md#u007-02). Для этого файла установлены процессы R007-07, R007-13, R007-16, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00037](../../../../../../issues/closed/issue-00037.md), [issue-00038](../../../../../../issues/potential/issue-00038.md), [issue-00041](../../../../../../issues/potential/issue-00041.md), [issue-00101](../../../../../../issues/potential/issue-00101.md), [issue-00104](../../../../../../issues/potential/issue-00104.md), [issue-00176](../../../../../../issues/potential/issue-00176.md). Различие критериев описано как поведение; единый способ поиска не выбирался. Новых issues самого поиска не создано. Смежные проблемы режимов/доступа алхимии и ремонта сохраняют свои локализации.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003034) |

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Три поиска имеют разные контракты: getSubstance исключает stored через getList; findNeededComponent читает все component по имени/локализованному веществу; findComponentByUuid сравнивает compendiumSource, а не UUID экземпляра. Нулевые стопки поиск не исключает. Обычное изготовление перебирает найденные стопки, ремонт берёт первую и требует1.

Сопоставленные определения и потребители: [module/actor/witcherActor.js](../witcherActor.js.md), [module/data/item/componentData.js](../../data/item/componentData.js.md), [module/data/item/commonItemData.js](../../data/item/commonItemData.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md), [module/actor/sheets/WitcherCharacterSheet.js](../sheets/WitcherCharacterSheet.js.md), [module/item/witcherItem.js](../../item/witcherItem.js.md), [module/item/systems/repair.js](../../item/systems/repair.js.md), [module/setup/handlebars.js](../../setup/handlebars.js.md).

[Протокол и границы](../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-07](../../../../cross-check-0002.md#r007-07), [R007-13](../../../../cross-check-0002.md#r007-13), [R007-16](../../../../cross-check-0002.md#r007-16). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
