# module/data/item/templates/combat/defensePropertiesData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.012](../../../../../../../../tasks/task-0003.012.md), одна порция из десяти файлов |
| Запись перекрёстной сверки | [TASK-0003.012](../../../../../../review-log.md#task-0003012) |

## Назначение файла

Вложенная модель собственного защитного свойства предмета или навыка: применимость к виду атаки, числовой модификатор и признак парирующего оружия. Её методы дают минимальный контракт для сборки варианта защиты внешними моделями.

## Условия использования

Класс наследует foundry.abstract.DataModel, default export. Отдельно как тип документа не регистрируется; создаётся EmbeddedDataField в WeaponData, SpellData, ArmorData и skillDefense. Для работы методов parent не нужен.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, строка 1 | Псевдоним foundry.data.fields | Не экспортируется | Инициализируется при импорте |
| DefenseProperties | Класс, 3–26 | Вложенная модель защиты | Default export | Создание/валидация Foundry |
| parrying | BooleanField, 6 | Признак парирующего свойства | Поле, initial:false | Читается отдельной веткой Actor.skillDefense |
| defendsAgainst | SetField(StringField), 7–10 | Виды атак, против которых доступно свойство | Поле, фактический default пустой Set | Строки required:true/blank:false, choices не заданы |
| modifier | NumberField, 11 | Число для формулы защиты | Поле, initial:0 | Без min/max/integer |
| isApplicableDefense / createDefenseOption | Методы, 15–25 | Проверка и минимальная структура результата | Prototype | Не меняют модель |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| defineSchema() | foundry.data.fields | Три поля | Создаёт boolean, set, number с label; defendsAgainst с hint | Статический, без записи |
| isApplicableDefense(attack) | Ожидается строковый ключ вида атаки | boolean | this.defendsAgainst.has(attack) | Без преобразования объекта атаки в строку; undefined→false на нормальном Set |
| createDefenseOption() | Читает this.modifier | Новый {modifier,skills:[],itemTypes:[]} | Возвращает пустые списки для заполнения внешней моделью | Нет label/value/skillOverride/parrying; аргумент, который передают некоторые callers, не используется |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DataModel; BooleanField/SetField/StringField/NumberField | Foundry 14.367.0, /opt/foundryvtt/common/abstract/data.mjs и common/data/fields.mjs | Наследование и schema API | Класс и defineSchema | Настоящий класс выполнен |
| WITCHER.Item.DefenseProperties.* | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | label/hint | Ключи из 6–11 |
| CONFIG.WITCHER.attackOptions | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Связь через UI | Значения defendsAgainst выбираются из видов атаки | defensePropertiesConfiguration передаёт options, сама модель CONFIG не читает |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/weaponData.js](../../../../../../../../../module/data/item/weaponData.js) | DefenseProperties | EmbeddedDataField; Weapon/Spell делегируют методы, Armor только содержит поле | Схемы и наличие методов проверены |
| [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | DefenseProperties | EmbeddedDataField; Weapon/Spell делегируют методы, Armor только содержит поле | Схемы и наличие методов проверены |
| [module/data/item/armorData.js](../../../../../../../../../module/data/item/armorData.js) | DefenseProperties | EmbeddedDataField; Weapon/Spell делегируют методы, Armor только содержит поле | Схемы и наличие методов проверены |
| [module/data/item/templates/combat/skillDefenseData.js](../../../../../../../../../module/data/item/templates/combat/skillDefenseData.js) | DefenseProperties | EmbeddedDataField в skillDefense | Строки1,11 |
| [module/data/item/professionData.js](../../../../../../../../../module/data/item/professionData.js) | isApplicableDefense/createDefenseOption | Проверяет девять skillPath-слотов и добавляет skillOverride | 49–114 |
| [module/item/mixins/defenseOptionMixin.js](../../../../../../../../../module/item/mixins/defenseOptionMixin.js) | system.createDefenseOption | Добавляет name как label/value и делегирует system | 1–10; принимает объект attack, вниз передаёт attack.attackOption |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../module/actor/mixins/defenseMixin.js) | isApplicableDefense; parrying; созданный option | Отбор предметов, выбор навыков/itemTypes, формула; parrying снимает отрицательный modifier стандартных parry/parryThrown при выбранном weapon | 19–25,52–66,148–161 |
| [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs) | Три поля | Форма Item | Все три formGroup и options=config.attackOptions |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | defendsAgainst/modifier | Форма навыка под isDefense | 67–71 |

## Данные и изменения состояния

Оба метода синхронны и не пишут документы. Множество хранит виды атак melee/ranged/spell/itemUse. modifier — число, не отдельный ActiveEffect. createDefenseOption не выбирает навык и не проверяет isDefense: этот флаг находится во внешнем skillDefense. ArmorData в текущем коде не предоставляет делегирующие isApplicableDefense/createDefenseOption; полное пользовательское поведение брони подлежит проверке TASK-0003.014.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Методы | Реальная модель {defendsAgainst:[melee],modifier:-2,parrying:true} | melee→true, ranged/undefined/объект→false; result {modifier:-2,skills:[],itemTypes:[]} | Диалог/бросок не запускались |
| Контракт consumers | WeaponData/SpellData/ProfessionData/Item.mixin/Actor.mixin | Первые добавляют skills либо skillOverride; Item обеспечивает название; Actor использует результат | Прикладные методы проверены в пределах связи |
| Профессия | Реальный ProfessionData, два отдельных входа | isDefense:false в ветке всё равно applicable:true; definingSkill с true не найден | Новые potential issues; не подтверждение пользователя |

## Непроверенные участки и открытые вопросы

Не исполнялся полный выбор предмета, штрафы парирования и применение результата защиты. Отсутствие метода у ArmorData фиксируется как граница контракта; её специализированный UI и сценарий полного цикла остаются TASK-0003.014. Поиск зависимостей — module/ и templates/.

## Связанные проблемы

[issue-00071](../../../../../../../../issues/potential/issue-00071.md) — отключение защитного навыка не учитывается ProfessionData; [issue-00072](../../../../../../../../issues/potential/issue-00072.md) — definingSkill отсутствует в её переборе.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.012 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.013

2026-09-10, `8cca18e14b75ec53028ee6bc49a837597de4d9af`; исходник неизменен. [Перекрёстная сверка](../../../../../../review-log.md#task-0003013).

В [module/data/item/weaponData.js](../../../../../../../../../module/data/item/weaponData.js) isApplicableDefense делегирует проверку вложенной модели, а createDefenseOption дополняет её результат одним навыком через цепочку ??. Настоящие модели подтвердили сохранение modifier и defendsAgainst, но skills может содержать пустую строку ([issue-00079](../../../../../../../../issues/potential/issue-00079.md)). [templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/defensePropertiesConfiguration.hbs) выводит ровно три поля parrying/defendsAgainst/modifier; собственных actions не содержит.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. [ProfessionData](../../../../../../../../../module/data/item/professionData.js) проверяет Set.has через isApplicableDefense и расширяет createDefenseOption полями skillOverride/label/value. Реальный метод возвращает первый применимый навык; он передаёт строку attack корректно. При нескольких навыках выбран первый по порядку; при отсутствии — undefined. createDefenseOption Item затем сохраняет label/value навыка, перекрывая имя профессии.

[Перекрёстная сверка](../../../../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Уточнение TASK-0003.021

Проверено 2026-09-11 на `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; исходник не менялся.

SpellData.isApplicableDefense делегирует проверку множества, createDefenseOption добавляет skills:[getUsedSkill().name]. Контроль defendsAgainst=[ranged], modifier2 вернул ожидаемый объект для spellcast; HexData/RitualData этой вложенной модели не имеют.

Сверенные карточки: [module/data/item/spellData.js](../../spellData.js.md).

[Результаты и пределы сверки](../../../../../../review-log.md#task-0003021).
