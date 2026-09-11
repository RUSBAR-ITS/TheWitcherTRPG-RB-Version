# module/data/item/mutagenData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/mutagenData.js](../../../../../../../module/data/item/mutagenData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

## Назначение файла

Определяет данные Item типа mutagen и включает общую схему расходования. alchemyDC — NumberField initial=0 без min/max/integer; остальные собственные поля — строки initial=''. Редактор цвета system.type находится в общей шапке.

## Условия использования

Регистрация через registerDataModels присваивает класс CONFIG.Item.dataModels.mutagen. Foundry создаёт модель для system соответствующего Item; импорт объявляет класс и локальный fields. Собственных hooks или обращений к миру нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| MutagenData | default class | Схема конкретного типа Item | CONFIG.Item.dataModels.mutagen | Создание/очистка/подготовка через Foundry |
| fields; commonData | Локальный alias; переменная defineSchema | foundry.data.fields и результат super.defineSchema() | Внутри модуля/метода | Создание описаний полей |
| type | Поле defineSchema | StringField, initial='' | system.type | Хранение; редактирование листом там, где поле выведено |
| source | Поле defineSchema | StringField, initial='' | system.source | Хранение; редактирование листом там, где поле выведено |
| effect | Поле defineSchema | StringField, initial='' | system.effect | Хранение; редактирование листом там, где поле выведено |
| alchemyDC | Поле defineSchema | NumberField, initial=0 | system.alchemyDC | Хранение; редактирование листом там, где поле выведено |
| minorMutation | Поле defineSchema | StringField, initial='' | system.minorMutation | Хранение; редактирование листом там, где поле выведено |
| isConsumable; consumeProperties | Spread consumable() | Boolean false и EmbeddedDataField | system | Общий признак и вложенные настройки |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Вызов Foundry, схема родителя | 15 верхних полей | 8 общих + 5 собственных + 2 из consumable() | Не пишет Item/Actor; собственных миграций нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Прямой импорт / наследование | defineSchema; общие getters и calcWeight | Определение и место вызова сверены |
| consumable() | [module/data/item/templates/consumableData.js](../../../../../../../module/data/item/templates/consumableData.js) | Прямой импорт / фабрика схемы | Включение isConsumable и consumeProperties | Определение и место вызова сверены |
| foundry.data.fields | Foundry DataField API | Внешний API | StringField/NumberField в defineSchema | Определение и место вызова сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | MutagenData | Импорт и регистрация типа mutagen | CONFIG.Item.dataModels |
| [module/item/sheets/WitcherMutagenSheet.js](../../../../../../../module/item/sheets/WitcherMutagenSheet.js) | system; schema.fields | Контекст и специализированная форма | Наследуемый _prepareContext |
| [templates/sheets/item/mutagen-sheet.hbs](../../../../../../../templates/sheets/item/mutagen-sheet.hbs) | Собственные поля | Отображение и редактирование | Имена system.* |
| [module/item/mixins/consumeMixin.js](../../../../../../../module/item/mixins/consumeMixin.js) | consumeProperties | Лечение, статусы, сообщение | Методы WitcherItem из consumeMixin |
| [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | quantity/weight/sourcebook; type или cost | Общие поля; выбор red/green/blue | Включение основным HBS |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Общие поля: description:String='', quantity:String='1', weight:Number=0, cost:Number=0, sourcebook:String='', isHidden=false, isStored=false, isCarried=true. Общая модель не ограничивает категории дочерними перечислениями. alchemyDC — NumberField initial=0 без min/max/integer; остальные собственные поля — строки initial=''. Редактор цвета system.type находится в общей шапке. isConsumable по умолчанию false; consumeProperties содержит doesHeal/heal/effects/removesEffects. Массивы воздействий имеют схему itemEffect без id; схема удаляет посторонний id. Собственный класс не задаёт расход количества, применение эффектов или лечение. canHaveTemporaryItemImprovement и canBeRepaired наследуют false.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема | Полное чтение и реальный конструктор MutagenData | 15 полей; четыре вложенных поля consumeProperties; лишние id/addsTempHp отсутствуют после очистки | Не сериализация DB |
| Форма | Контекст WitcherMutagenSheet и настоящий HBS | 3 цвета, по 10 именованных полей; type есть в header; только 2 вкладки общей configuration | formGroup widgets подменены |
| Внешний процесс | consume / useItem / context menu | isConsumable проверяют входные маршруты; сам consume не проверяет признак и не списывает quantity | Actor/Item — фасады |

## Непроверенные участки и открытые вопросы

Настоящие модели/методы Foundry 14.367.0 и системы в изолированном Node 24.16.0; DOM, родительские документы и запись представлены фасадами. Мир и браузер не запускались. Не проверялись импорт компедиумов, изготовление алхимии и игровые правила мутаций. Фактическая регистрация не исключает пользовательский выбор другого листа.

## Связанные проблемы

[issue-00093](../../../../../../issues/potential/issue-00093.md). Разрыв между схемой расходования и доступной configuration; выбор цвета исправен.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Алхимическая таблица показывает effect с дополнительной подписью при ../itemType=mutagen и minorMutation отдельно. В изолированном рендере оба текста присутствовали, HTML effect экранирован. Наличие общего алхимического layout не добавляет в модель отсутствующие поля.

Связанные шаблоны: [templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-alchemical.hbs). [Проверки и ограничения](../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.
