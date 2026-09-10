# module/data/item/templates/itemEffectData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/itemEffectData.js](../../../../../../../../module/data/item/templates/itemEffectData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `0fa589bd300856ff309f362afcb66d6fa43401ab` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.014](../../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../../review-log.md#task-0003014) |

## Назначение файла

Фабрика четырёх полей одной записи предметного воздействия. Определяет данные, но не применяет статус и не создаёт ActiveEffect.

## Условия использования

Default export function itemEffect() каждый раз возвращает новые определения полей. Вызывающий файл решает, будет ли запись элементом TypedObjectField или ArrayField. Сама запись не содержит ID: он может быть ключом внешнего словаря.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields; itemEffect | Константа 1; функция 3–10 | Псевдоним полей и фабрика | Локальная / default export | Создание определений |
| name | StringField 5 | Текстовое имя | initial '' | Свободная строка |
| statusEffect | StringField 6 | Ключ статуса/свойства | initial null, nullable true | Список вариантов задаёт UI; enum в схеме отсутствует |
| percentage | NumberField 7 | Процент | initial 0, min 0, max 100 | Очистка ограничивает диапазон; integer не задан |
| varEffect | BooleanField 8 | Переменная величина воздействия | initial false | Интерпретирует внешний потребитель |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| itemEffect() | Без аргументов | Объект четырёх Field | Создаёт определения name/statusEffect/percentage/varEffect | Не хранит данные, не выполняет бросок, не меняет документы |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| StringField, NumberField, BooleanField | Foundry 14.367.0, common/data/fields.mjs | Глобальный API | Строки 5–8 | Настоящие поля и очистка в моделях |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/armorData.js](../../../../../../../../module/data/item/armorData.js) | itemEffect() | TypedObjectField effects | Import 2 / поле 48 |
| [module/data/item/enhancementData.js](../../../../../../../../module/data/item/enhancementData.js) | itemEffect() | TypedObjectField effects | Import 2 / поле 21 |
| [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | itemEffect() | TypedObjectField effects; getPreprocessedEffects | 49,80–97; группирует по непустому statusEffect и складывает percentage |
| [module/data/item/templates/consumePropertiesData.js](../../../../../../../../module/data/item/templates/consumePropertiesData.js) | itemEffect() | ArrayField effects/removesEffects | Две фабрики вложенных записей |
| [module/data/item/spellData.js](../../../../../../../../module/data/item/spellData.js) | itemEffect() | TypedObjectField selfEffects/onCastEffects | 53–54 |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../../../templates/sheets/item/armor-sheet.hbs) | name/statusEffect | Форма собственных и вычисленных воздействий | percentage/varEffect здесь не редактируются |
| [templates/sheets/item/enhancement-sheet.hbs](../../../../../../../../templates/sheets/item/enhancement-sheet.hbs) | name/statusEffect/percentage | Редактор улучшения | varEffect здесь не выводится |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) | Четыре поля записи | varEffect условен по staminaIsVar | Полная карточка TASK-0003.013 |
| [module/actor/witcherActor.js](../../../../../../../../module/actor/witcherActor.js) | effects/statusEffect | Подготовка брони, applyStatus/removeStatus | Тип коллекции и формат записи критичны; изолированная сверка |
| [module/item/mixins/consumeMixin.js](../../../../../../../../module/item/mixins/consumeMixin.js) | effects/removesEffects/name/statusEffect | Применение/снятие и чат употребления | 13–14,22–27; полный маршрут позже |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Фабрика не гарантирует одинаковое представление коллекций у разных владельцев. Armor/Enhancement/DamageProperties/Spell используют словари, ConsumablePropertiesData — массивы. NumberField ограничивает отдельное сохранённое значение percentage; последующая сумма getPreprocessedEffects не является очисткой того же поля и может отличаться. name, statusEffect, percentage и varEffect не заменяют документные system.changes, duration, transfer или statuses.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Состав и вызовы | Полный файл и все пять ES-import потребителей | Четыре определения; обе формы контейнера | Соседние файлы прочитаны только в пределах связи |
| Числовая очистка | EnhancementData с −1,25,101 и строкой '25' | 0,25,100; строка стала числом | Модель в памяти |
| Диспетчеризация брони | Actor.prepareDerivedData и applyStatus | Словарь не развёрнут; объекты armorEffects имеют id, а applyStatus читает statusEffect | Действия статусов перехвачены |

## Непроверенные участки и открытые вопросы

Файл не определяет вероятность срабатывания и игровые последствия каждого ID. Полные потребители заклинаний/употребления и бросков будут разобраны отдельно; текущие выводы ограничены схемой и указанными связями.

## Связанные проблемы

[issue-00060](../../../../../../../issues/potential/issue-00060.md), [issue-00068](../../../../../../../issues/potential/issue-00068.md), [issue-00069](../../../../../../../issues/potential/issue-00069.md), [issue-00084](../../../../../../../issues/potential/issue-00084.md). Преобразование текста редактором, миграция массива и потребители, ожидающие другую форму коллекции.

Дополнительный разрыв передачи конфигурационных записей в applyStatus — [issue-00089](../../../../../../../issues/potential/issue-00089.md).

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.015

2026-09-10, `7edb814aa870da75c7ad7633536e899a8d07e205`; исходник неизменен. [Перекрёстная сверка](../../../../../review-log.md#task-0003015).

Проверен полный потребитель [module/data/item/templates/consumePropertiesData.js](../../../../../../../../module/data/item/templates/consumePropertiesData.js): effects/removesEffects — ArrayField(SchemaField(itemEffect())), а не словари, использованные бронёй/улучшением/DamageProperties. Общая запись не содержит id; очистка удаляет переданный id. [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) требует obj.id, а [templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/consumablePropertiesConfiguration.hbs) выводит пустой data-id; это [issue-00091](../../../../../../../issues/potential/issue-00091.md). percentage/varEffect входят в схему, но consume→Actor.applyStatus/removeStatus их не читает. Этот факт не задаёт игровых правил вероятности.
