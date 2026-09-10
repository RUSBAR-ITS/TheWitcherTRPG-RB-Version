# module/data/item/templates/consumePropertiesData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/consumePropertiesData.js](../../../../../../../../module/data/item/templates/consumePropertiesData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../../review-log.md#task-0003015) |

## Назначение файла

Схема настроек расходования: лечение и два массива добавляемых/снимаемых статусов.

## Условия использования

Создаётся как EmbeddedDataField из consumable(). Это DataModel, не Item и не коллекция embedded ActiveEffect. Все три включающие модели получают одну форму данных.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| ConsumablePropertiesData | default class extends foundry.abstract.DataModel | Вложенные данные применения | Импорт consumableData | Создание и очистка Foundry |
| fields | Локальный alias | foundry.data.fields | Внутри модуля | Конструирование схемы |
| doesHeal | BooleanField | initial=false; label WITCHER.Item.ConsumeProperties.doesHeal | consumeProperties.doesHeal | Условие лечения/поля heal |
| heal | StringField | initial=''; label WITCHER.Item.ConsumeProperties.heal | consumeProperties.heal | Текст для calculateHealValue |
| effects; removesEffects | Два ArrayField(SchemaField(itemEffect())) | Списки добавления и снятия статусов | consumeProperties | Чтение и целиковое обновление массива |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Вызов DataModel | Четыре поля | Дважды вызывает itemEffect() для массивов | Не создаёт id; собственных миграций/методов применения нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| itemEffect() | [module/data/item/templates/itemEffectData.js](../../../../../../../../module/data/item/templates/itemEffectData.js) | Прямой импорт / фабрика | Схема каждой записи обоих массивов | Определение и место вызова сверены |
| DataModel; BooleanField/StringField/ArrayField/SchemaField | Foundry model API | Внешний API | Наследование и схема | Определение и место вызова сверены |
| WITCHER.Item.ConsumeProperties.* | [lang/ru.json](../../../../../../../../lang/ru.json) | Локализация | Labels doesHeal/heal | Определение и место вызова сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/templates/consumableData.js](../../../../../../../../module/data/item/templates/consumableData.js) | ConsumablePropertiesData | EmbeddedDataField | Прямой импорт |
| [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) | effects/removesEffects | Ручное добавление, поиск по obj.id, удаление | Методы редактора |
| [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) | Четыре поля, попытка addsTempHp | Форма и таблицы | systemFields / item.system |
| [module/item/mixins/consumeMixin.js](../../../../../../../../module/item/mixins/consumeMixin.js) | doesHeal/heal/effects/removesEffects | Применение и сообщение | consume/createConsumeMessage |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

itemEffect задаёт name:String='', statusEffect:String=null (nullable), percentage:Number=0 с min=0/max=100 и varEffect:Boolean=false. Это массивы, в отличие от словаря TypedObjectField у брони/улучшений/урона. В записи нет id. В этой модели нет addsTempHp. Переданный id и addsTempHp отсутствуют в подготовленных данных после очистки настоящей моделью. doesHeal не валидирует текст heal как выражение Roll. Текущая UI-форма не предлагает percentage/varEffect; Actor.applyStatus/removeStatus их не читают.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Форма коллекции | Реальные модели трёх типов с входными id/addsTempHp | Лишние поля отброшены; элементы — массивы из четырёх полей | В памяти |
| Связь с редактором | Настоящий _onEditEffect/_oRemoveEffect и HBS | Пустой data-id; edit даёт TypeError, remove сохраняет список | DOM событий/запись подменены |
| Связь с formGroup | Реальный core helper | Включённая configuration пишет ошибку для addsTempHp; остальные группы остаются | Вместо DOM widgets — toFormGroup facade |

## Непроверенные участки и открытые вопросы

Настоящие модели/методы Foundry 14.367.0 и системы в изолированном Node 24.16.0; DOM, родительские документы и запись представлены фасадами. Мир и браузер не запускались. Семантика вероятности/вариативности для расходования отдельно не согласована; отсутствие ветви не заменяет текст игровых правил. Пустые/невалидные выражения лечения и полноценная серверная валидация HP требуют отдельного разбора healMixin.

## Связанные проблемы

[issue-00091](../../../../../../../issues/potential/issue-00091.md), [issue-00092](../../../../../../../issues/potential/issue-00092.md). Два разных несоответствия схемы и редактора; исправление не выполнялось.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
