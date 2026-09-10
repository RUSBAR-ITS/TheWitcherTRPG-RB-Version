# module/data/item/templates/consumableData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/consumableData.js](../../../../../../../../module/data/item/templates/consumableData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../../review-log.md#task-0003015) |

## Назначение файла

Общая фабрика двух полей, включаемых в схемы алхимии, мутагенов и прочих предметов.

## Условия использования

Три модели напрямую импортируют default consumable и вызывают его внутри defineSchema. При импорте создаётся локальный alias fields; данные Actor и Item не меняются.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| consumable | default function | Создаёт описания двух полей | Прямой импорт | Новый объект схемы при вызове |
| fields | Локальный alias | foundry.data.fields | Внутри модуля | BooleanField/EmbeddedDataField |
| isConsumable | BooleanField | initial=false; label WITCHER.Item.isConsumable | system.isConsumable | Признак доступности применения |
| consumeProperties | EmbeddedDataField | Вложенная ConsumablePropertiesData | system.consumeProperties | Создание/очистка вложенной модели |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| consumable() | Аргументов нет | Объект isConsumable/consumeProperties | Создаёт BooleanField и EmbeddedDataField(ConsumablePropertiesData) | Синхронная фабрика; не добавляет методы consume или списание |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ConsumablePropertiesData | [module/data/item/templates/consumePropertiesData.js](../../../../../../../../module/data/item/templates/consumePropertiesData.js) | Прямой импорт | Тип EmbeddedDataField | Определение и место вызова сверены |
| foundry.data.fields | Foundry DataField API | Внешний API | Конструкторы полей | Определение и место вызова сверены |
| WITCHER.Item.isConsumable | [lang/ru.json](../../../../../../../../lang/ru.json) | Локализация | Label поля | Определение и место вызова сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/alchemicalData.js](../../../../../../../../module/data/item/alchemicalData.js) | consumable() | Spread внутри defineSchema | Три прямых импорта |
| [module/data/item/mutagenData.js](../../../../../../../../module/data/item/mutagenData.js) | consumable() | Spread внутри defineSchema | Три прямых импорта |
| [module/data/item/valuableData.js](../../../../../../../../module/data/item/valuableData.js) | consumable() | Spread внутри defineSchema | Три прямых импорта |
| [module/item/mixins/consumeMixin.js](../../../../../../../../module/item/mixins/consumeMixin.js) | consumeProperties | Чтение через модель Item | Косвенный потребитель полей |
| [module/item/witcherItem.js](../../../../../../../../module/item/witcherItem.js) | isConsumable | Getter возвращает system.isConsumable ?? false | Динамическое чтение |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) | isConsumable / schema | formGroup и условное раскрытие настроек | Путь поля |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Фабрика задаёт данные, а поведение добавляется отдельно через consumeMixin к WitcherItem. false по умолчанию не запрещает прямой вызов consume(), но скрывает действие в контекстном меню и останавливает Actor.useItem. Конкретная модель может содержать эти поля без специализированного редактора (mutagen).

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Определение/потребители | Полное чтение, поиск consumableData.js | Ровно три прямых caller; по два поля | Динамический сторонний импорт не искался |
| Модели/маршруты | Настоящие три модели; useItem и menu на фасадах | false по умолчанию; оба маршрута учитывают flag; прямой consume выполняется при false | Нет записи в мир |

## Непроверенные участки и открытые вопросы

Настоящие модели/методы Foundry 14.367.0 и системы в изолированном Node 24.16.0; DOM, родительские документы и запись представлены фасадами. Мир и браузер не запускались. Фабрика не определяет условия экипировки, допустимые рецепты или полномочия пользователя.

## Связанные проблемы

[issue-00093](../../../../../../../issues/potential/issue-00093.md). Поля мутагена присутствуют, но конфигурация их не выводит.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
