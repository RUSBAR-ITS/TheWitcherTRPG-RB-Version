# module/data/item/valuableData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/valuableData.js](../../../../../../../module/data/item/valuableData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

## Назначение файла

Определяет данные Item типа valuable и включает общую схему расходования. effect и quality хранятся моделью, но собственная основная форма их не редактирует; одно это не устанавливает дефект.

## Условия использования

Регистрация через registerDataModels присваивает класс CONFIG.Item.dataModels.valuable. Foundry создаёт модель для system соответствующего Item; импорт объявляет класс и локальный fields. Собственных hooks или обращений к миру нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| ValuableData | default class | Схема конкретного типа Item | CONFIG.Item.dataModels.valuable | Создание/очистка/подготовка через Foundry |
| fields; commonData | Локальный alias; переменная defineSchema | foundry.data.fields и результат super.defineSchema() | Внутри модуля/метода | Создание описаний полей |
| type | Поле defineSchema | StringField, initial='' | system.type | Хранение; редактирование листом там, где поле выведено |
| avail | Поле defineSchema | StringField, initial='' | system.avail | Хранение; редактирование листом там, где поле выведено |
| effect | Поле defineSchema | StringField, initial='' | system.effect | Хранение; редактирование листом там, где поле выведено |
| conceal | Поле defineSchema | StringField, initial='' | system.conceal | Хранение; редактирование листом там, где поле выведено |
| quality | Поле defineSchema | StringField, initial='' | system.quality | Хранение; редактирование листом там, где поле выведено |
| isConsumable; consumeProperties | Spread consumable() | Boolean false и EmbeddedDataField | system | Общий признак и вложенные настройки |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Вызов Foundry, схема родителя | 15 верхних полей | 8 общих + 5 собственных + 2 из consumable() | Не пишет Item/Actor; собственных миграций нет |
| get canHaveTemporaryItemImprovement() | Чтение свойства модели | true | Разрешает интерфейсу показывать временные улучшения | Не применяет улучшение; отличается от унаследованного false |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Прямой импорт / наследование | defineSchema; общие getters и calcWeight | Определение и место вызова сверены |
| consumable() | [module/data/item/templates/consumableData.js](../../../../../../../module/data/item/templates/consumableData.js) | Прямой импорт / фабрика схемы | Включение isConsumable и consumeProperties | Определение и место вызова сверены |
| foundry.data.fields | Foundry DataField API | Внешний API | StringField в defineSchema | Определение и место вызова сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | ValuableData | Импорт и регистрация типа valuable | CONFIG.Item.dataModels |
| [module/item/sheets/WitcherValuableSheet.js](../../../../../../../module/item/sheets/WitcherValuableSheet.js) | system; schema.fields | Контекст и специализированная форма | Наследуемый _prepareContext |
| [templates/sheets/item/valuable-sheet.hbs](../../../../../../../templates/sheets/item/valuable-sheet.hbs) | Собственные поля | Отображение и редактирование | Имена system.* |
| [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js) | consumeProperties | Лечение, статусы, сообщение | Методы WitcherItem из consumeMixin |
| [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | quantity/weight/sourcebook; type или cost | Общие поля | Включение основным HBS |
| [templates/partials/effect-part.hbs](../../../../../../../templates/partials/effect-part.hbs) | canHaveTemporaryItemImprovement | Условие отображения временных улучшений | Проверка свойства в partial |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Общие поля: description:String='', quantity:String='1', weight:Number=0, cost:Number=0, sourcebook:String='', isHidden=false, isStored=false, isCarried=true. Общая модель не ограничивает категории дочерними перечислениями. effect и quality хранятся моделью, но собственная основная форма их не редактирует; одно это не устанавливает дефект. isConsumable по умолчанию false; consumeProperties содержит doesHeal/heal/effects/removesEffects. Массивы воздействий имеют схему itemEffect без id; схема удаляет посторонний id. Собственный класс не задаёт расход количества, применение эффектов или лечение. Собственный getter возвращает true.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема | Полное чтение и реальный конструктор ValuableData | 15 полей; четыре вложенных поля consumeProperties; лишние id/addsTempHp отсутствуют после очистки | Не сериализация DB |
| Форма | Контекст WitcherValuableSheet и настоящий HBS | 7 категорий, по 10 полей; configuration расходования | formGroup widgets подменены |
| Внешний процесс | consume / useItem / context menu | isConsumable проверяют входные маршруты; сам consume не проверяет признак и не списывает quantity | Actor/Item — фасады |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-01](../../../../cross-check-0002.md#u007-01), [U007-02](../../../../cross-check-0002.md#u007-02), [U007-08](../../../../cross-check-0002.md#u007-08). Для этого файла установлены процессы R007-01, R007-02, R007-05, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00091](../../../../../../issues/potential/issue-00091.md), [issue-00092](../../../../../../issues/potential/issue-00092.md). Связанные проблемы общей configuration, не отдельные дефекты defineSchema.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Таблица valuables использует isCarried/avail/conceal/quantity/weight/cost/description и также принимает loots разных типов у Monster. Подготовка Character задаёт семь группы ценностей, mount — отдельный partial. Отсутствующие на чужой модели avail/conceal не становятся ошибкой рендера. issue-00178 касается подписи доступности, а не существующих словарей.

Связанные шаблоны: [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs); [templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-valuables.hbs). [Проверки и ограничения](../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

ValuableData имеет 15 верхних полей и расходование. Категория valuable type выбирается из словаря листа; effect/quality в модели не означают автоматического эффекта основной формы. Конфигурация содержит consumable вкладку, а применение и quantity принадлежат общим Item/Actor входам.

Сопоставленные определения и потребители: [module/data/item/commonItemData.js](commonItemData.js.md), [module/data/item/templates/consumableData.js](templates/consumableData.js.md), [module/setup/registerDataModels.js](../../setup/registerDataModels.js.md), [module/item/sheets/WitcherValuableSheet.js](../../item/sheets/WitcherValuableSheet.js.md), [templates/sheets/item/valuable-sheet.hbs](../../../templates/sheets/item/valuable-sheet.hbs.md), [module/item/mixins/consumeMixin.js](../../item/mixins/consumeMixin.js.md), [templates/partials/item-header.hbs](../../../templates/partials/item-header.hbs.md), [templates/partials/effect-part.hbs](../../../templates/partials/effect-part.hbs.md).

[Протокол и границы](../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-01](../../../../cross-check-0002.md#r007-01), [R007-02](../../../../cross-check-0002.md#r007-02), [R007-05](../../../../cross-check-0002.md#r007-05). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
