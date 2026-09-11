# module/data/item/templates/combat/attackOptionsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/combat/attackOptionsData.js](../../../../../../../../../module/data/item/templates/combat/attackOptionsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.012](../../../../../../../../tasks/task-0003.012.md), одна порция из десяти файлов |
| Запись перекрёстной сверки | [TASK-0003.012](../../../../../../review-log.md#task-0003012) |

## Назначение файла

Фабрика восьми полей выбора способа атаки, связанных навыков и бонусов. Её поля включаются в WeaponData, SpellData и вложенную атаку профессионального навыка; фабрика сама не бросает кубы и не рассчитывает урон.

## Условия использования

При импорте запоминается foundry.data.fields. Каждый вызов attackOptions() создаёт новый набор полей. CONFIG.WITCHER читается отложенными initial-функциями при определении начальных значений. Фабрика не зарегистрирована отдельным типом документа.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, строка 1 | Псевдоним foundry.data.fields | Не экспортируется | Инициализируется при импорте |
| attackOptions | export default function, 3–49 | Сборка схемы | Прямой импорт тремя потребителями | Возвращает object полей |
| attackOptions | SetField(StringField), 5–17 | Множество вариантов атаки | Включено в схему родителя | Элементы required:true, blank:false; choices не задан |
| meleeAttackSkill, rangedAttackSkill | StringField, 18–27 | Ключ навыка выбранного варианта | Поля родителя | initial: source.attackSkill |
| spellAttackSkill | StringField, 28–32 | Ключ магического навыка | Поле родителя | initial:'spellcasting' |
| itemUseAttackSkill | StringField, 33–36 | Ключ навыка применения предмета | Поле родителя | initial явно не задан; на проверенной модели undefined |
| applyMeleeBonus, applyRangedMeleeBonus | BooleanField, 38–46 | Настройки добавления бонуса урона | Поля родителя | Первая initial зависит от meleeSkills/attackSkill; вторая source.applyMeleeBonus ?? false |
| isThrowable | BooleanField, 47 | Признак метательного предмета | Поле родителя | initial:false |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| attackOptions() | Глобальный foundry.data.fields | Object с восемью DataField | Конструирует поля и initial-callbacks | Синхронно, без записи |
| initial для attackOptions | source, CONFIG.WITCHER | Array строк, затем Set при инициализации модели | Добавляет melee для meleeSkills; ranged для rangedSkills или isThrowable; spell для truthy level, в этом порядке | Не устанавливает itemUse; явно переданное [] сохраняется |
| initial для навыков и бонусов | source родительской схемы | Значения соответствующих полей | Читает прежний attackSkill и applyMeleeBonus | Это callbacks defaults, не миграция до очистки неизвестных ключей |

Все восемь полей имеют label; кроме applyMeleeBonus и isThrowable имеют также hint. Конкретные ключи перечислены в исходнике 15–47 и сверены с en/ru. Поля навыков не имеют choices, min/max; значения конфигурации передаёт UI. Строки melee/ranged/spell/itemUse обозначают варианты атаки, а dodge/parry — варианты защиты из другого файла.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DataField / SetField / StringField / BooleanField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Глобальный API; создание схемы | Все поля; SchemaField._cleanType очищает неизвестные ключи до defaults | Исходник ядра и реальные WeaponData/SpellData |
| CONFIG.WITCHER.meleeSkills, rangedSkills, attackOptions, skillMap | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Чтение конфигурации | initial-классификация и проверка ключей; строки 136–170, 426–430 | Определения массивов и spellcast сопоставлены с фабрикой |
| WITCHER.Attack.*, WITCHER.Weapon.* | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | label/hint полей | Проверка ключей и подписей в двух языках |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/weaponData.js](../../../../../../../../../module/data/item/weaponData.js) | attackOptions() | Spread на корне system | Импорт и defineSchema:38 |
| [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | attackOptions() | Spread на корне system | Импорт и defineSchema:55 |
| [module/data/item/templates/combat/skillAttackData.js](../../../../../../../../../module/data/item/templates/combat/skillAttackData.js) | attackOptions() | Spread внутри skillAttack | Импорт и строка21 |
| [module/item/witcherItem.js](../../../../../../../../../module/item/witcherItem.js) | attackOptions; <вариант>AttackSkill | getItemAttack выбирает Set-позицию по клавишам и читает ключ навыка | 28–70; настоящий метод выполнен отдельно |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | getItemAttack; applyMeleeBonus; isThrowable | Проверка наличия skill, формула урона, расход метательного оружия | weaponAttack:14–38,52–60,162–169 |
| [module/actor/mixins/professionMixin.js](../../../../../../../../../module/actor/mixins/professionMixin.js) | isAttack/attackOptions/applyMeleeBonus | Атака собственным навыком либо фильтр оружия; конкретный навык берётся из professionSkill | doProfessionAttackRoll / doProfessionWeaponAttackRoll |
| [templates/sheets/item/configuration/tabs/general.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/general.hbs); [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs) | Варианты, навыки, бонусы | formGroup; условия has | Предметные формы; issue-00061 описывает отсутствие itemUseAttackSkill |
| [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) | attackOptions и бонусы | Форма атаки профессии без отдельных навыков | Вложенный контекст system=skill.skillAttack |

## Данные и изменения состояния

Фабрика изменяет только состав возвращённой схемы. Значения создаёт/очищает Foundry. В проверенной версии `attackSkill` не входит в WeaponData: при загрузке старых данных он удаляется раньше initial. Поэтому прямой callback с swordsmanship возвращает melee, но настоящий new WeaponData({attackSkill:'swordsmanship'}) даёт пустое множество и undefined навыки. Это различие между текстом callback и реальным жизненным циклом модели.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Начальные значения | Node stdin; настоящие поля/WeaponData/SpellData; семь входов | Пустой Weapon→[]; старые swordsmanship/archery→[]; throwable→[ranged] без навыка; spell с level→[spell]; явный [] не заменён | Без загрузки документов мира |
| Магический ключ | getItemAttack + constructBaseAttackFormula; SpellData.getUsedSkill | spellcasting отсутствует в skillMap; общий построитель формулы получает undefined. Специальный getUsedSkill для class Spells успешно возвращает spellcast | Не утверждается отказ любого castSpell: у него есть fallback |
| Бонусы | Поиск всех applyRangedMeleeBonus в module/templates; сверка weaponAttack/professionMixin | Поле и UI существуют; расчёт использует applyMeleeBonus. Явный applyMeleeBonus:true даёт ranged default:true | Бой/браузер не исполнялись |

## Непроверенные участки и открытые вопросы

Полный цикл атаки и специализированные редакторы остаются последующим порциям. Не проверялись внешние изменения CONFIG, миграция реальных packs/миров и сохранение форм. Область поиска потребителей: текущие module/ и templates/, прямые импорты всей системы.

## Связанные проблемы

[issue-00064](../../../../../../../../issues/potential/issue-00064.md), [issue-00065](../../../../../../../../issues/potential/issue-00065.md), [issue-00066](../../../../../../../../issues/potential/issue-00066.md), [issue-00061](../../../../../../../../issues/potential/issue-00061.md) — неверный магический default, утрата attackSkill при инициализации, неиспользуемый бонус дальнего боя и отсутствие поля itemUse в общем UI.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.012 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.013

2026-09-10, `8cca18e14b75ec53028ee6bc49a837597de4d9af`; исходник неизменен. [Перекрёстная сверка](../../../../../../review-log.md#task-0003013).

Полностью проверен [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs): семь formGroup, три условные секции melee/ranged/spell, отсутствует редактор itemUseAttackSkill ([issue-00061](../../../../../../../../issues/potential/issue-00061.md)). Прямое включение найдено в spellGeneral.hbs; оружие использует отдельную разметку general.hbs. [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../../../module/item/sheets/WitcherWeaponSheet.js) формирует общий context.config.attackSkills из восьми навыков ближнего/дальнего боя, но читатель этого нового списка поиском не найден. Выбор skills в WeaponData.createDefenseOption использует ?? и может остановиться на пустой строке: [issue-00079](../../../../../../../../issues/potential/issue-00079.md).

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. [Профессиональный partial](../../../../../../../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) выводит attackOptions и условные applyMeleeBonus/applyRangedMeleeBonus/isThrowable. В отличие от формы оружия, он не выбирает базовый навык: professionMixin использует собственный профессиональный stat/level. Реальный has/Set проверен; applyRangedMeleeBonus по-прежнему не читается непосредственным расчётом профессии (issue-00066).

[Перекрёстная сверка](../../../../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Уточнение TASK-0003.021

Проверено 2026-09-11 на `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; исходник не менялся.

У SpellData начальный spellAttackSkill остаётся spellcasting. Четыре известных класса маскируют неверный ключ fallback на spellcast, пустой class даёт TypeError; явный ritcraft имеет приоритет. При level=novice начальный набор содержит spell, но старый attackSkill после очистки не даёт meleeAttackSkill. HexData/RitualData эту фабрику не включают.

Сверенные карточки: [module/data/item/spellData.js](../../spellData.js.md).

[Результаты и пределы сверки](../../../../../../review-log.md#task-0003021).

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Профессиональная примесь берёт только первый элемент Set attackOptions: для chooser ranged/melee группа 11 предложила только ranged. Поля meleeAttackSkill/rangedAttackSkill/spellAttackSkill/itemUseAttackSkill не участвуют в direct formula — берутся skill.stat/level. Empty set не защищён chooser(242); выбор семантики нескольких вариантов отдельно не согласован.

[module/actor/mixins/professionMixin.js](../../../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.
