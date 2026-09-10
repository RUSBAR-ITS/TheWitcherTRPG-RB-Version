# module/data/item/templates/armor/spData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/armor/spData.js](../../../../../../../../../module/data/item/templates/armor/spData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.012](../../../../../../../../tasks/task-0003.012.md), одна порция из десяти файлов |
| Запись перекрёстной сверки | [TASK-0003.012](../../../../../../review-log.md#task-0003012) |

## Назначение файла

Модель SP одной локации брони. Хранит исходные текущее/максимальное значения и рассчитывает их варианты с улучшениями. Название конкретной локации задаёт поле в ArmorData, сам SpData его не содержит.

## Условия использования

Default export SpData extends foundry.abstract.DataModel. ArmorData включает шесть EmbeddedDataField: head, torso, leftArm, rightArm, leftLeg, rightLeg. Затем явно вызывает обе фазы каждого экземпляра; parent — ArmorData.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, строка 1 | Псевдоним foundry.data.fields | Не экспортируется | Инициализируется при импорте |
| SpData | Класс, 3–41 | SP одной локации | Default export | Создание/очистка Foundry |
| stoppingPower | NumberField, 6–9 | Текущий базовый SP | initial:0; label WITCHER.Armor.StoppingPower | Сохраняемое поле |
| modifiedStoppingPower | NumberField, 10–13 | Текущий SP с улучшениями | initial:0, persisted:false, без label | Задаётся обеими фазами |
| maxStoppingPower | NumberField, 14–17 | Максимальный базовый SP | initial:0; label WITCHER.Armor.MaxStoppingPower | Сохраняемое поле |
| modifiedMaxStoppingPower | NumberField, 18–22 | Максимум с улучшениями | initial:0, persisted:false; тот же label максимума | Задаётся обеими фазами |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| defineSchema() | fields.NumberField | Четыре числовых поля | Описывает persisted/initial/label | Нет min/max/integer и проверки current≤max |
| prepareBaseData() | stoppingPower, maxStoppingPower | undefined | Копирует в modifiedStoppingPower/modifiedMaxStoppingPower | В памяти; обязательна перед новым добавлением бонусов |
| prepareDerivedData() | parent.enhancementItems; enhancement.system.stopping | undefined | Если maxStoppingPower == 0, выход; иначе прибавляет stopping каждого улучшения к обоим modified | Нет ограничения снизу/сверху, округления, типового фильтра или проверки applied; повтор без base накапливает |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DataModel/NumberField; persisted:false | Foundry 14.367.0, common/abstract/data.mjs и common/data/fields.mjs | Наследование/сериализация | Методы и два производных поля | Реальные toObject()/toObject(false) |
| parent.enhancementItems | [module/data/item/armorData.js](../../../../../../../../../module/data/item/armorData.js) | Данные родителя | Подготовленные связанные предметы | ArmorData.prepareDerivedData до шести вызовов SP |
| enhancement.system.stopping | [module/data/item/enhancementData.js](../../../../../../../../../module/data/item/enhancementData.js) | Чтение поля | Добавление SP, initial:0 в модели улучшения | Определение и реальный EnhancementData |
| WITCHER.Armor.StoppingPower/MaxStoppingPower | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | Подписи трёх полей | Сопоставление schema/языков |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/armorData.js](../../../../../../../../../module/data/item/armorData.js) | SpData / обе фазы / stoppingPower/maxStoppingPower | Шесть локаций; applySpDamage пишет базовое текущее, repair копирует максимум | Схема37–44, applySpDamage75–81, repair95–106, prepare108–154 |
| [module/actor/mixins/armorMixin.js](../../../../../../../../../module/actor/mixins/armorMixin.js) | modifiedMaxStoppingPower / modifiedStoppingPower | Отбор покрытия по max>0, затем подсчёт защиты | 15–20,125–129 |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Оба modified | armorPartsInfo строит current/max/percentage для локаций | 191–195 |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../../../../templates/sheets/item/armor-sheet.hbs) | stoppingPower/maxStoppingPower | Редактирование исходных чисел локаций | Поля system.head/torso/leftArm/rightArm/leftLeg/rightLeg |

## Данные и изменения состояния

Исходные 7/10 и улучшение +2 дают подготовленные 9/12. maxStoppingPower=0 блокирует бонус даже при ненулевом текущем SP. Проверка именно ==0, а не ≤0. При повторном derived без base текущий SP становится 11; base→derived возвращает 9. Это характеристика протокола фаз, не доказательство двойного начисления в штатном lifecycle.

После расчёта toObject() сохраняет только stoppingPower/maxStoppingPower, а toObject(false) включает modified. Ни один метод SpData не вызывает update. Урон/ремонт записываются внешней ArmorData. Отдельного tailWing поля здесь нет: armorMixin использует естественную броню монстра; название shield относится к другим данным.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Две фазы | Настоящий ArmorData.head и EnhancementData(stopping:2) | 7/10→9/12; повторный derived→11, base+derived→9 | Набор улучшений передан в память |
| Непокрытая локация | torso stoppingPower:2,maxStoppingPower:0 | Осталось 2/0 | Не проверка игрового правила |
| Сериализация | toObject и toObject(false) | Производные поля отсутствуют в сохранённом представлении | Не DB-сохранение |
| Числовые ограничения | Реальная модель с -2/-1 | Значения приняты и скопированы как -2/-1 | Отсутствие min не объявлено нарушением правил |
| Локации | ArmorData/armorMixin/armorPartsInfo | Все шесть путей совпали, helper использует подготовленные значения | Шаблоны/бой целиком не запускались |

## Непроверенные участки и открытые вопросы

Броня, улучшения и их редакторы будут полностью разобраны в TASK-0003.014; ремонт — TASK-0003.017. Не проверялись ActiveEffect по persisted:false путям, сетевое сохранение и повреждение нескольких слоёв. Поиск — module/ и templates/.

## Связанные проблемы

[issue-00007](../../../../../../../../issues/potential/issue-00007.md) касается подписей левых/правых ног в helper, а не ключей SP. Новых самостоятельных проблем SpData не зарегистрировано.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.012 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
