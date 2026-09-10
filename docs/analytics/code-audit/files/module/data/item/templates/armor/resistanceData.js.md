# module/data/item/templates/armor/resistanceData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/armor/resistanceData.js](../../../../../../../../../module/data/item/templates/armor/resistanceData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.012](../../../../../../../../tasks/task-0003.012.md), одна порция из десяти файлов |
| Запись перекрёстной сверки | [TASK-0003.012](../../../../../../review-log.md#task-0003012) |

## Назначение файла

Вложенная модель сопротивлений брони трём физическим видам урона. При подготовке объединяет базовые флаги с флагами прикреплённых улучшений, а само уменьшение урона выполняет armorMixin.

## Условия использования

Default export ResistanceData extends foundry.abstract.DataModel. Единственный прямой потребитель — ArmorData.resistance через EmbeddedDataField. ArmorData явно вызывает prepareBaseData/prepareDerivedData после формирования enhancementItems; импорт класса сам расчёт не запускает.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, строка 1 | Псевдоним foundry.data.fields | Не экспортируется | Инициализируется при импорте |
| ResistanceData | Класс, 3–23 | Сопротивления брони | Default export, вложенная модель | Создаётся Foundry |
| bludgeoning, slashing, piercing | BooleanField, 6–8 | Три независимых сопротивления | initial:false; labels/hints отсутствуют | Хранят базу, в подготовленной модели объединяются с улучшениями |
| prepareBaseData, prepareDerivedData | Методы, 12–22 | Фазы подготовки | Вызываются ArmorData | Первая пустая, вторая меняет this[resistance] |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| defineSchema() | fields.BooleanField | Три поля | Создаёт определения, initial:false | Статически, без записи |
| prepareBaseData() | Нет аргументов | undefined | Пустое тело | Не сбрасывает флаги самостоятельно |
| prepareDerivedData() | this.parent.enhancementItems, элементы с system | undefined | Для каждого улучшения перебирает Object.keys(this); сохраняет true либо берёт !!enhancement.system[key] | OR в памяти; optional chaining только у списка. Не читает enhancement.system.applied, не проверяет тип документа и не пишет source |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DataModel/BooleanField | Foundry 14.367.0, common/abstract/data.mjs и common/data/fields.mjs | Наследование/API | Модель и enumerable поля | Настоящий экземпляр содержит ровно три ключа |
| parent.enhancementItems | [module/data/item/armorData.js](../../../../../../../../../module/data/item/armorData.js) | Контекст родителя | prepareDerivedData создаёт записи name/img/system/id | Строки119–145; parent===ArmorData проверено |
| enhancement.system.bludgeoning/slashing/piercing | [module/data/item/enhancementData.js](../../../../../../../../../module/data/item/enhancementData.js) | Чтение данных | OR с каждым флагом | Три поля EnhancementData |
| Виды damageTypes | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Сопоставление ключей | Сопротивления имеют три из восьми ключей | Конфигурация damageTypes |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/armorData.js](../../../../../../../../../module/data/item/armorData.js) | ResistanceData и её методы | EmbeddedDataField; подготовка двух фаз | Строки36,110,145 |
| [module/actor/mixins/armorMixin.js](../../../../../../../../../module/actor/mixins/armorMixin.js) | armor.system.resistance[тип] | calculateArmorResistances читает надетые и natural armor; AP даёт ранний выход | 206–228 |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../../../../templates/sheets/item/armor-sheet.hbs) | Три resistance-поля | Checkbox исходной брони | 31–36 |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | Подготовленные сопротивления | Вывод признаков в инвентаре | 54–66 |

## Данные и изменения состояния

OR делает сопротивление true, если оно уже было true или true у любого улучшения. Типичное восстановление исходного состояния происходит при переинициализации модели Foundry; пустой prepareBaseData не отменяет OR самостоятельно. Повторный derived с тем же набором идемпотентен по этим boolean, удаление улучшения без reset не было объявлено штатным циклом. В этой модели нет elemental/silver/fire и расчёта коэффициента 0.5.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Parent и ключи | Настоящие ArmorData и EnhancementData, Node stdin | resistance.parent===ArmorData; Object.keys содержит только три resistance-поля | Без Actor/Item-документов |
| OR улучшения | База false, улучшение slashing:true | Подготовленные false/true/false; источник улучшения прочитан из system | Полный prepareDerivedData ArmorData со связанными Actor.items не запускался |
| Применение | armorMixin.calculateArmorResistances и конфигурация | Схема поставляет boolean; формула и ранний выход AP принадлежат Actor | Расчёт боя в этой порции не повторялся |

## Непроверенные участки и открытые вопросы

Отбор/удаление улучшений, системный lifecycle Item и работа нескольких слоёв брони остаются последующим порциям. Отсутствие дополнительных типов сопротивления не объявлено нарушением правил. Поиск — module/ и templates/.

## Связанные проблемы

[issue-00025](../../../../../../../../issues/potential/issue-00025.md) и [issue-00026](../../../../../../../../issues/potential/issue-00026.md) относятся к downstream расчёту типа/AP, а не к OR сопротивлений. Новых самостоятельных проблем этой модели не зарегистрировано.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.012 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
