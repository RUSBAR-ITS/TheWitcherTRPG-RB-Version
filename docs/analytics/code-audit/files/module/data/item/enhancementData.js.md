# module/data/item/enhancementData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/enhancementData.js](../../../../../../../module/data/item/enhancementData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `0fa589bd300856ff309f362afcb66d6fa43401ab` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.014](../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../review-log.md#task-0003014) |

## Назначение файла

Модель отдельного Item улучшения: категория, состояние установки, бонус SP, физические сопротивления и словарь предметных воздействий.

## Условия использования

EnhancementData extends CommonItemData, default export, CONFIG.Item.dataModels.enhancement. Это предмет, на который оружие/броня ссылаются через enhancementItemIds. Он не является документом ActiveEffect типа temporaryItemImprovement.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| EnhancementData; fields | Класс 6–42; константа 4 | Модель и псевдоним полей | Default export / Item.enhancement | Инициализация и миграция |
| Поля CommonItemData | Spread 11 | description, quantity, weight, cost, sourcebook, isHidden, isStored, isCarried | Восемь inherited полей | Общие данные предмета |
| type, avail | StringField 12–13 | Категория и доступность | initial '', choices отсутствуют | weapon/rune/armor/glyph задаёт редактор |
| applied | BooleanField 14 | Отметка установки | initial false | Потребитель исключает уже установленные из выбора |
| stopping | NumberField 16 | Добавка SP | initial 0, без min/max/integer | SpData применяет к текущему и максимальному SP |
| bludgeoning, slashing, piercing | BooleanField 17–19 | Физические сопротивления | initial false | Объединение OR в ResistanceData |
| effects | TypedObjectField(SchemaField) 21 | Словарь четырёх полей itemEffect | Ключи записей вне самой схемы записи | Объединение по ID и показ в формах |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | super и itemEffect() | 16 полей | Общие 8 плюс собственные 8 | Без вычислений и обновлений документов |
| static migrateData(source) | Сырой объект | super.migrateData(source) | this.effects?.forEach(parseInt); migrateEffectsToTypedField; super | this в static — класс, не source; числовую очистку выполняет NumberField |
| static migrateEffectsToTypedField(source) | Непустой массив source.effects | undefined | Каждая запись получает randomID; массив заменён Object.fromEntries | В отличие от ArmorData результат не удаляет; пустой массив/объект не входят в ветвь |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Import/наследование | Схема и super.migrateData | Предыдущая карточка и текущая модель |
| itemEffect() | [module/data/item/templates/itemEffectData.js](../../../../../../../module/data/item/templates/itemEffectData.js) | Import/SchemaField | effects:21 | Полное определение |
| Поля, randomID, очистка данных | Foundry 14.367.0, common/data/fields.mjs и common/abstract/data.mjs | Внешний API | Типы и миграция | Настоящий new EnhancementData; percentage очищается и ограничивается |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | EnhancementData | Регистрация enhancement | Импорт 7, регистрация 54 |
| [module/item/sheets/WitcherEnhancementSheet.js](../../../../../../../module/item/sheets/WitcherEnhancementSheet.js) | system/schema | Контекст редактора | Полный разбор |
| [templates/sheets/item/enhancement-sheet.hbs](../../../../../../../templates/sheets/item/enhancement-sheet.hbs) | type/avail/stopping/сопротивления/effects | Редактирование | Все поля/действия сверены |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | type/applied/quantity | Отбор и установка улучшения | _chooseEnhancement: выбирает категорию, имя +(Applied), applied=true, quantity=1 |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | applied/name | Снятие отметки и ID у владельца | removeEnhancement; UI-вызов не проверялся |
| [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js) | system улучшения | Разрешение ID, объединение effects | Ссылки сохраняются по порядку |
| [module/data/item/templates/armor/spData.js](../../../../../../../module/data/item/templates/armor/spData.js) | stopping | При maxStoppingPower != 0 добавляет к modified SP/max | Настоящая модель |
| [module/data/item/templates/armor/resistanceData.js](../../../../../../../module/data/item/templates/armor/resistanceData.js) | Три сопротивления | OR с базовыми | Настоящая модель |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | effects | Добавляет воздействия установленного улучшения в свойства атаки | 173; полный бой вне порции |
| [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | effects | Getter enhancementsEffects для UI | 69–76 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | effects/name/percentage | Показ установленных улучшений | Точечная сверка разметки |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Модель сама не устанавливает applied и не расходует quantity. Эти изменения делает внешний обработчик инвентаря. Она также не создаёт ActiveEffect. При старом массиве effects получает новые ключи и сохраняет записи; при современном объекте ключи сохраняются. NumberField percentage преобразовал '25' в 25 и ограничил −1/101 до 0/100.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема | Настоящая EnhancementData | 16 верхних полей; четыре поля каждой записи | Без Item мира |
| Миграция | Старый массив с percentage='25', varEffect=true; пустой массив | Запись сохранена с новым ID, 25/true; пустой дал {} после очистки | Случайный ID проверен по структуре, не конкретному значению |
| Улучшение брони | Две настоящие модели со stopping2/1 и сопротивлениями | Бонусы SP +3, OR сопротивлений, поздний ID эффекта перекрывает ранний | Внешний Item-контекст подменён |
| Отличие от временного эффекта | Структура модели и вызовы инвентаря | Item.effects и Item.system.effects — разные хранилища | Прежний тест temporaryItemImprovement не повторялся |

## Непроверенные участки и открытые вопросы

Не выполнялись реальная установка/снятие через контекстное меню, разделение стека quantity, запись в БД и полная атака. Поля, обе миграции и входящие/исходящие связи прочитаны полностью.

## Связанные проблемы

[issue-00042](../../../../../../issues/potential/issue-00042.md), [issue-00060](../../../../../../issues/potential/issue-00060.md), [issue-00068](../../../../../../issues/potential/issue-00068.md), [issue-00078](../../../../../../issues/potential/issue-00078.md), [issue-00088](../../../../../../issues/potential/issue-00088.md). issue-00042 относится к отдельному временному ActiveEffect, не к этой модели. Корректная миграция здесь служит контролем для issue-00068; остальные связи относятся к редактору и использованию улучшений.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
