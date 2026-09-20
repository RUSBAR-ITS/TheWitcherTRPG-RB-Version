# module/data/item/skillItemData.js

## Актуальное изменение TASK-0012 — 14.3.1.00139

2026-09-20, dev. Добавлено StringField skillId с начальным пустым значением и локализованной подписью. Назначение при создании выполняет WitcherItem через assignedSkillIds; само приготовление модели не генерирует ID.

Связанные потребители/границы: skillIdentity, WitcherSkillItemSheet. Статические проверки выполнены; браузер и БД не запускались. [Исходник](../../../../../../../module/data/item/skillItemData.js) · [TASK-0012](../../../../../../tasks/task-0012-temporary-hp.md) · [Проверки](../../../../../task-0012-checks.md).

Ниже сохранены предыдущие срезы анализа с их датами; изменённый контракт определяется разделом выше.

## Текущее состояние

**14.3.1.00066, TASK-0010.008.** Объявлен сохраняемый массив modifiers{id,name,value:Number}; modifiedValue=min(baseCap,value+activeEffectModifiers). Подписи/потребитель используют Item.name и system. Отрицательное значение не обрезается до0; произвольные Item AE не превращаются автоматически в Actor-строки нового вычислителя.

[Исходник](../../../../../../../module/data/item/skillItemData.js); [проверка и пределы](../../../../../task-0010-008-checks.md).

## Текущее состояние — 14.3.1.00061

2026-09-18, TASK-0010.003. **Назначение:** Модель дополнительного навыка Item.

**Сущности, действия и зависимости:** Добавлен NumberField baseCap initial10, остальные поля/наследование сохранены. Адресная интеграция Item-навыков и UI остаются в .008.

[Исходник](../../../../../../../module/data/item/skillItemData.js), [проверки и границы](../../../../../task-0010-003-checks.md). Статическая проверка; игровая приёмка не проводилась. Численный контракт следующих стадий ещё не внедрён.

## Предыдущие датированные проверки

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Схема собственного навыка как Item типа skill. Хранит выбранную характеристику, значение, подпись, состояние раскрытия и три признака происхождения навыка. Отличается от встроенного Skill внутри Actor.system.skills.

## Условия использования

Default class SkillItemData extends foundry.abstract.TypeDataModel. registerDataModels назначает её CONFIG.Item.dataModels.skill. Не наследует CommonItemData; при создании Item действуют стандартные _id/name/type документа, а этот класс определяет только system.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| SkillItemData / defineSchema | Класс и статический метод, 3–16 | Восемь полей system | Default export | Инициализация, валидация и сериализация через Foundry. |
| attribute / label | StringField, 6/8 | Ключ характеристики и дополнительная подпись | Начальные значения '' | attribute не имеет choices; label не равен Item.name автоматически. |
| value / activeEffectModifiers | NumberField, 7/10 | Уровень и поле модификатора | Начальные значения 0 | Нет min/max/integer; поддерживаются отрицательные/дробные значения и числовые строки при очистке. |
| isOpened / isProfession / isPickup / isLearned | BooleanField, 9/11–13 | Раскрытие и флаги происхождения | false по умолчанию | Признаки не исключают друг друга. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Глобальные foundry.data.fields | Объект восьми DataField | Создаёт String/Number/Boolean поля | Собственных методов броска, вычисления modifiedValue, миграции и CRUD модификаторов нет. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| TypeDataModel / StringField / NumberField / BooleanField | Foundry 14.367.0, common/abstract/type-data.mjs и common/data/fields.mjs | Наследование/конструирование | Вся схема | Настоящие классы выполнены в Node; неизвестные поля отбрасываются. |
| Встроенный Skill — сравнение контрактов | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js) | Смежная модель, без импорта | Отличие Item.system от Actor.system.skills | Skill имеет isVisible и getter modifiedValue; SkillItemData их не объявляет. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | SkillItemData | Импорт и регистрация типа skill | 23, 70 |
| [module/item/sheets/WitcherSkillItemSheet.js](../../../../../../../module/item/sheets/WitcherSkillItemSheet.js) | attribute/value и прочие system | Контекст ItemSheet; редактирует только attribute вместе с Item.name | _prepareContext; шаблон отдельной формы |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | attribute | _prepareCustomSkills группирует Item типа skill | 103–115 |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | attribute | Аналогичная группировка | 78–90 |
| [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | attribute/value и ожидаемый modifiers | rollCustomSkillCheck; собственный activeEffectModifiers прямо не читается | 134–172 |
| [module/actor/sheets/mixins/customSkillMixin.js](../../../../../../../module/actor/sheets/mixins/customSkillMixin.js) | isOpened и ожидаемый modifiers | Раскрытие и CRUD; modifiers отсутствует в схеме | 19–60 |
| [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../../../templates/partials/monster/monster-custom-skill-display.hbs) | value/isOpened/activeEffectModifiers/flags | Старый табличный вывод Item-навыка | Весь partial |
| [templates/partials/character/custom-skill-display.hbs](../../../../../../../templates/partials/character/custom-skill-display.hbs) | Несовпадающий контекст skill.* | Текущая строка обращается не к system Item | Весь partial |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Схема не хранит массив modifiers, ID строки модификатора, isVisible, modifiedValue, описание, quantity или isStored. Группа навыка определяется строкой attribute, а имя документа хранится в Item.name. В изолированном new SkillItemData({modifiers:[...]}) и updateSource({modifiers:[...]}) массив не попадает в system/сериализацию. Наличие обработчиков с обращением к этому полю не расширяет схему автоматически.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема/числа/неизвестные поля | Группа 01 | Восемь полей; '-1.5' → -1.5; произвольный attribute принят; нечисловой value отвергнут; modifiers отброшен при создании и updateSource | Реальная модель; Item.create/update в БД не выполнялись. |
| Форма и потребители | Группы 02, 07, 15–17, 22 | 9 вариантов характеристики; собственный effect-бонус не входит в обычный custom roll; CRUD пишет неизвестный массив; NumberField преобразует inline-строку | Классы документов и UI представлены фасадами. |

## Непроверенные участки и открытые вопросы

Форма и схема установлены; live Item.create/update, стороннее расширение и достижимость старого массива — [U004-03](../../../../cross-check-0002.md#u004-03). Настройка допустимых spd/luck и политика группового бонуса не согласовывались.

## Связанные проблемы

[issue-00187](../../../../../../issues/closed/issue-00187.md), [issue-00188](../../../../../../issues/potential/issue-00188.md), [issue-00189](../../../../../../issues/potential/issue-00189.md), [issue-00190](../../../../../../issues/closed/issue-00190.md). Контекст текущей строки, отсутствующие группы SPD/LUCK, схема/CRUD modifiers и применение собственных эффектов описаны раздельно.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |

## Сквозная сверка TASK-0004.004

2026-09-14; rusbar-main, f31a2541770dddb23c01b5284c16f31989c5d1e5. Исходник совпадает со срезом TASK-0001; изменено только описание.

Восемь полей Item skill сопоставлены с формой имени/атрибута, группировкой Actor и старым CRUD. В отличие от встроенного Skill отсутствуют isVisible/modifiedValue/modifiers; поле activeEffectModifiers существует, но прямой custom-бросок его не читает. .029 проверила числовое приведение, произвольный attribute и отбрасывание массива настоящей DataModel; это не доказательство успешного Item.update в мире.

Сопоставленные определения и потребители: [module/actor/mixins/skillMixin.js](../../actor/mixins/skillMixin.js.md), [module/actor/sheets/mixins/customSkillMixin.js](../../actor/sheets/mixins/customSkillMixin.js.md), [module/item/sheets/WitcherSkillItemSheet.js](../../item/sheets/WitcherSkillItemSheet.js.md), [templates/sheets/item/skill-item-sheet.hbs](../../../templates/sheets/item/skill-item-sheet.hbs.md), [module/data/actor/templates/common/skills/skillData.js](../actor/templates/common/skills/skillData.js.md), [module/setup/registerDataModels.js](../../setup/registerDataModels.js.md).

[Протокол и границы](../../../../review-log.md#task-0004004) — TASK-0004.004; процессы [R004-06](../../../../cross-check-0002.md#r004-06), [R004-08](../../../../cross-check-0002.md#r004-08). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
