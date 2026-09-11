# module/data/item/templates/combat/skillAttackData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/combat/skillAttackData.js](../../../../../../../../../module/data/item/templates/combat/skillAttackData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.012](../../../../../../../../tasks/task-0003.012.md), одна порция из десяти файлов |
| Запись перекрёстной сверки | [TASK-0003.012](../../../../../../review-log.md#task-0003012) |

## Назначение файла

Фабрика схемы атаки профессиональным навыком. Объединяет признаки доступности/использования оружия, формулу и общие боевые модели; действие броска реализует professionMixin.

## Условия использования

Default export skillAttack() вызывается внутри professionSkill(). Каждая схема навыка содержит SchemaField(skillAttack()), а вложенные свойства урона являются настоящим экземпляром DamageProperties. Конфигурация поля не является запуском способности.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, строка 5 | Псевдоним foundry.data.fields | Не экспортируется | Инициализируется при импорте |
| skillAttack() | Функция, 7–25 | Собирает 13 полей | Default export | Создаёт новую схему |
| isAttack, usesWeapon | BooleanField, 9–16 | Доступность атаки и использование оружия | initial:false; label задан | Читаются professionMixin |
| damageFormulaOverride | StringField, 17–20 | Формула собственного урона навыка | initial:''; label задан | Строка; не валидируется как Roll |
| Поля attackOptions() и defenseOptions() | Spread, 21,23 | Варианты атаки/защиты и бонусы | Имена перечислены в карточках фабрик | Получают defaults общей схемы |
| damageProperties | EmbeddedDataField(DamageProperties), 22 | Вложенные свойства урона | Экземпляр модели | В профессии parent указывает на ProfessionData, не на plain-object skillAttack |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| skillAttack() | Импортированные фабрики/класс и foundry.data.fields | Object из 13 DataField | Добавляет три собственных поля, восемь attackOptions, damageProperties и defenseOptions | Синхронно; методов броска, Hooks и записи нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| attackOptions | [module/data/item/templates/combat/attackOptionsData.js](../../../../../../../../../module/data/item/templates/combat/attackOptionsData.js) | ES import и вызов | Строки1,21; восемь полей | Определение и реальный состав вложенной модели |
| DamageProperties | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | ES import; EmbeddedDataField | Строки2,22 | Схема, методы и parent проверены |
| defenseOptions | [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../../../../module/data/item/templates/combat/defenseOptionsData.js) | ES import и вызов | Строки3,23 | Определение и Set defaults |
| fields.BooleanField/StringField/EmbeddedDataField | Foundry 14.367.0, common/data/fields.mjs | Глобальный API | Создание полей | Реальный ProfessionData |
| WITCHER.profession.skillPath.skill.skillAttack.* | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | Собственные label; ключ damageFormulaOverrides во множественном числе | Схема/ключи языка |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/templates/professionSkillData.js](../../../../../../../../../module/data/item/templates/professionSkillData.js) | skillAttack() | SchemaField для каждой способности | Импорт2, поле15 |
| [module/data/item/professionData.js](../../../../../../../../../module/data/item/professionData.js); [module/data/item/templates/professionPathData.js](../../../../../../../../../module/data/item/templates/professionPathData.js) | professionSkill().skillAttack | Один definingSkill и три ветки по три навыка | Определения schema; parent на реальной модели |
| [module/actor/mixins/professionMixin.js](../../../../../../../../../module/actor/mixins/professionMixin.js) | isAttack, usesWeapon, damageFormulaOverride, attackOptions, damageProperties, defenseOptions | _onProfessionRoll выбирает ветку; собственная атака строит damage; с оружием передаёт дополнительные properties | 34–75,143–149,231–259 |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | additionalDamageProperties | mergeDamageProperties получает DamageProperties навыка | 136–138,328–356 |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs); [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) | skillAttack.* | isAttack открывает элементы схемы и таблицу эффектов | Пути formGroup/partial сверены |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | skillAttack.damageProperties.effects | Добавление/редактирование/удаление ключей effects по path | 110–141 |

## Данные и изменения состояния

Фабрика не меняет данные. Собственная атака professionMixin берёт характеристику, имя и уровень из самого professionSkill, а не из meleeAttackSkill и прочих общих полей навыков. Для usesWeapon передаются skillReplacement и additionalDamageProperties. Общий mergeDamageProperties обрабатывает boolean/number/string/array, но effects после миграции является object и в слияние не попадает. Создание отдельной структуры свойств урона следует отличать от изменения предмета через ссылку.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Состав и вложенность | Настоящий ProfessionData в Node | 13 ключей skillAttack; damageProperties.parent===ProfessionData | Без Item-документа и мира |
| Слияние свойств | Настоящие DamageProperties и исходный mergeDamageProperties | Добавленный armorPiercing применён; effects.two отсутствует, собственный effects.one остаётся; cap 5+5→10 | Число cap описано как текущее поведение, не утверждение игрового правила |
| Маршрут атаки | professionMixin и weaponAttackMixin, фрагменты вызовов | Собственная атака и usesWeapon передают разные контексты | Полные диалоги/броски не исполнялись |

## Непроверенные участки и открытые вопросы

Полная профессия и её редактор — TASK-0003.019; бой — следующие порции. Поведение всех inherited полей не выводится из одного факта включения в схему. Три настройки урона, помеченные переводами как not functional, описаны в DamageProperties. Поиск потребителей: module/ и templates/.

## Связанные проблемы

[issue-00069](../../../../../../../../issues/potential/issue-00069.md) — effects навыка не присоединяются к атаке оружием; [issue-00066](../../../../../../../../issues/potential/issue-00066.md) — applyRangedMeleeBonus не имеет расчётного потребителя. Defaults общих полей описаны в attackOptions.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.012 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. [professionSkill](../../../../../../../../../module/data/item/templates/professionSkillData.js) включает skillAttack для definingSkill и 9 навыков путей. [Редактор](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) показывает вложенные свойства при isAttack, а professionMixin выбирает attack раньше custom usage и thresholds. usesWeapon делегирует weaponAttack с additionalDamageProperties, иначе используется собственный stat/level и damageFormulaOverride; первый attackOptions выбирает вариант. Чтение цепочки не означает полного аудита боя.

[Перекрёстная сверка](../../../../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Direct attack использует damageFormulaOverride, applyMeleeBonus, damageProperties и первый attackOptions; usesWeapon передаёт лишь skillReplacement и additionalDamageProperties в другой метод. Настройки damage override/defenseOptions способности автоматически не подменяют оружейные. Наличие extra поля не сопровождается direct расходом STA(238).

[module/actor/mixins/professionMixin.js](../../../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.
