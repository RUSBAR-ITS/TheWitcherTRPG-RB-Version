# module/actor/mixins/modifierMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.007](../../../../../../tasks/task-0003.007.md), одна порция из двух файлов |
| Запись перекрёстной сверки | [TASK-0003.007](../../../../review-log.md#task-0003007) |

## Назначение файла

Три метода построения фрагментов строк бросков из уже подготовленных модификаторов навыков, групп навыков, атак и защиты. Файл не применяет ActiveEffect к данным Actor: он читает результаты подготовки и добавляет значения/подписи в формулу.

## Условия использования

Именованный изменяемый export let modifierMixin — объект с тремя методами, без импортов. [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js):3,439 копирует его в прототип Actor. this методов должен содержать общую модель навыков/combatEffects и appliedEffects. Глобальные game/CONFIG должны быть доступны.

Позднейший Object.assign с defenseMixin:443 заменяет Actor.addDefenseModifiers. Тела двух определений сейчас побайтно совпадают после Function.toString; фактически метод защиты экземпляра происходит из [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js):249–255. Это описано отдельно от определения здесь; остальные два метода не заменяются последующими примесями.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| modifierMixin | export let объект:1–53 | Набор методов строковых модификаторов | Named export; копирование в Actor.prototype | Содержит addActiveEffects/addAttackModifiers/addDefenseModifiers; своей регистрации нет |
| formula / modifiers | Локальные строки:6,39,47 | Накопление фрагментов формулы | Внутри методов | Конкатенация и return, без сохранения данных |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| addActiveEffects(skillName):2–36 | Ключ CONFIG.WITCHER.skillMap, this.system.skills, appliedEffects, необязательные skillGroupModifiers | Строка, начинающаяся с пробела при наличии слагаемых, либо '' | Считывает displayRollsDetails; находит skill; добавляет готовый activeEffectModifiers с именами эффектов, затем групповые записи | Синхронно, без записи/catch. При неизвестном ключе сразу '', даже если есть allSkills. Отсутствующий путь навыка, changes или неизвестный group могут вызвать ошибку. |
| addAttackModifiers:38–44 | this.system.combatEffects.attackModifier — словарь {name,value} | Конкатенация ненулевых значений с локализованными подписями | Object.values, пропуск mod.value===0, строка ' '+value+'['+localize(name)+']' | Синхронно, без нормализации знака и без displayRollsDetails. |
| addDefenseModifiers:46–52 | this.system.combatEffects.defenseModifier — аналогичный словарь | Аналогичная строка | Та же операция над defenseModifier | Синхронно; это определение заменяется defenseMixin при сборке Actor. |

Для навыка сначала определяется skill.attribute.name и skill.name. При activeEffectModifiers!=0 число читается из system.skills[attribute][name].activeEffectModifiers. Имена берутся из this.appliedEffects, у которых хотя бы одна system.changes[] имеет key, точно равный этому пути; затем effect.name соединяются через ' & '. Число не пересчитывается из changes, не суммируются значения отдельных эффектов.

Имена ищутся даже при выключенной детализации; флаг меняет только полученную строку. Ни phase, ни конкретная операция change не проверяются при поиске подписей; коллекция appliedEffects уже отфильтрована ядром по active. Метод не отключает/переносит эффекты и не применяет их приоритеты.

Группы перебираются в порядке Object.values. modifier.group=='allSkills' подходит без чтения массива CONFIG; остальные сравниваются через CONFIG.WITCHER[group].some(name===skill.name). Подпись групповой записи локализуется и добавляется независимо от displayRollsDetails; нулевой групповой value не отбрасывается. Неизвестный group не пропускается безопасно: возможен TypeError на .some. Схема StringField(group) не содержит choices, а UI мастера даёт свои известные варианты.

### Точные примеры результата

| Вход | Выход |
| --- | --- |
| Известный swordsmanship, modifier=0, групп нет | '' |
| Неизвестный custom_unknown, даже с allSkills | '' |
| Навык +2, эффекты A/B; группа disease=-2/allSkills; details=false | ` +2 +-2[L:disease]` |
| Те же данные; details=true | ` +2[A & B] +-2[L:disease]` |
| attack/defense value=-2, имя bonus | ` -2[L:bonus]` |
| attack/defense value=0 | '' |
| attack/defense value=+2 | ` 2[L:bonus]` — '+' отсутствует |

L: — метка подменённой локализации в изолированной проверке. Строка '+-2' у навыкового/группового модификатора следует из буквального '+' перед отрицательным числом; атакующий/защитный метод этого '+' не ставит вообще. Реальная грамматика Foundry принимает '8+0 -2[L:bonus]' и '8+0', но отвергает '8+0 2[L:bonus]' с SyntaxError. Это issue-00033, а не пересмотр правил сложения.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| game.settings.get('TheWitcherTRPG','displayRollsDetails') | [module/setup/settings.js](../../../../../../../module/setup/settings.js); [карточка](../../setup/settings.js.md) | Глобальный API настройки | addActiveEffects:3,19–21 | Настройка зарегистрирована системой; прочитанное значение влияет только на подпись модификатора конкретного навыка. |
| CONFIG.WITCHER.skillMap; массивы групп | [module/setup/config.js](../../../../../../../module/setup/config.js); [карточка](../../setup/config.js.md) | Глобальная конфигурация | skillMap:4; CONFIG.WITCHER[group]:28 | Структуры skill.attribute.name/skill.name определены в config. skillGroups:265–290 перечисляет allSkills, meleeSkills, rangedSkills, magicSkills, verbalCombatSkills, empatheticVerbalCombatSkills. |
| system.skills.*.*.activeEffectModifiers | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js); [карточка](../../data/actor/templates/common/skills/skillData.js.md) | Чтение модели | 10,20–21 | NumberField=0; включение через группы/skills/CommonActorData. |
| system.skillGroupModifiers | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js); [карточка](../../data/actor/commonActorData.js.md) | Чтение словаря | 24–32 | TypedObjectField записей name/group/value:40–46; число и строки определены там. |
| system.combatEffects.attackModifier/defenseModifier | [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js); [карточка](../../data/actor/templates/common/combatEffectsData.js.md) | Чтение словарей | 40,48 | Записи name:StringField/value:NumberField=0; схему включает CommonActorData:48. |
| Actor.appliedEffects; effect.system.changes; effect.name | Foundry14.367.0: /opt/foundryvtt/client/documents/actor.mjs:149–156; /opt/foundryvtt/common/data/active-effect.mjs:16–24 | Унаследованная коллекция и данные эффектов | 11–18, подписи | appliedEffects выбирает active; phase/type/priority каждого изменения здесь не фильтруются. |
| WitcherActiveEffect.isSuppressed | [module/activeEffect/witcherActiveEffect.js](../../../../../../../module/activeEffect/witcherActiveEffect.js) | Транзитивное условие коллекции | Определяет active ядра | Не вызов этого файла; подавление/transfer описаны в карточке Actor. |
| game.i18n.localize; Object.values; Array.filter/some/map/join; шаблонные строки | Foundry Localization API; ECMAScript | Внешний API | Названия групп/атаки/защиты и конкатенация | Имя из записей динамическое, фиксированного списка ключей локализации файл не вводит. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | modifierMixin | Object.assign:439; позже addDefenseModifiers заменяется defenseMixin:443 | Проверена тождественность методов прототипа после всех подключений. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | addActiveEffects, addAttackModifiers | constructBaseAttackFormula:315–325 дописывает к характеристике+навыку | 322–323; полученные строки проверены грамматикой. |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | addActiveEffects, addAttackModifiers | castSpell добавляет к 1d10+WILL+навыку | 32–33. |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | addActiveEffects; итоговый addDefenseModifiers | skillDefense формирует формулу перед extendedRoll | 180–181; метод защиты берётся из этого же defenseMixin. |
| [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | addActiveEffects | rollSkillCheck по skillMapEntry.name; rollCustomSkillCheck по customSkill.name | 65,157; неизвестное имя вернёт ''. Это предел поддержки, не создание записи skillMap. |
| [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | addActiveEffects | doProfessionAttackRoll передаёт attack.name | 158; базовый attackModifier этим вызовом не добавляется. |
| [module/actor/mixins/verbalCombatMixin.js](../../../../../../../module/actor/mixins/verbalCombatMixin.js); [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | addActiveEffects | Формулы вербального боя | 64;79 соответственно. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | addActiveEffects | Алхимия/крафт/ремонт | CharacterSheet:324,412; repair:221; явные имена alchemy/crafting. |
| [module/scripts/rolls/extendedRoll.js](../../../../../../../module/scripts/rolls/extendedRoll.js) | Собранная строка броска | new Roll(rollFormula), затем evaluate | 10–11; это последующий потребитель через боевые методы, не прямой импорт modifierMixin. |

Поиск всех трёх имён выполнен в module/; также проверены templates/ и packsJson/ на прямые ссылки. Статические вызовы перечислены выше; действия внешних модулей/макросов не исследованы. Точки применения групповых записей и schema не приравниваются к универсальному обработчику модификаторов всей системы.

## Данные и изменения состояния

Все три метода читают модель/коллекцию/настройку и возвращают строку. Они не записывают Actor, не изменяют значение навыка, не расходуют ресурс и не бросают кубы. Исполнение, критические результаты и отправка сообщений принадлежат Roll/extendedRoll и вызывающим методам. Значение already-prepared activeEffectModifiers берётся целиком; подписи эффектов служат отображению и могут не объяснять точную последовательность их арифметики.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | 53 строки, без импортов, три метода | Контракты, условия и конкатенации разобраны полностью | Не все формы создания модификаторов. |
| Известный/неизвестный навык и флаг | Оригинальный mixin с настоящей CharacterData и skillMap; подмены game.settings/i18n, appliedEffects | Получены точные строки таблицы; custom_unknown→''; unknown group→TypeError | appliedEffects в данном опыте — заданный массив, не реальный клиент. |
| Коллизия методов | Оригинальные 17 объектов примесей и Object.assign класса | Actor.addDefenseModifiers===defenseMixin.addDefenseModifiers; исходные тела совпали | Совпадение сейчас не гарантирует будущие изменения. |
| Положительный знак | Оригинальные методы и constructBaseAttackFormula; Peggy из установленного Foundry, оригинальная grammar.pegjs и RollParser | -2/0 парсятся; +2→SyntaxError отсутствующего оператора | Без Roll.evaluate/ChatMessage; issue-00033. |
| Фильтрация эффектов | Отдельный сценарий исходного core applyActiveEffects с системным isSuppressed | Disabled/непереносимый/подавленный исключены из вычислений согласно этапам Actor | Сам modifierMixin числа эффектов не вычисляет. |

## Непроверенные участки и открытые вопросы

Файл полностью прочитан. Внешние источники некорректных group/skillName, имена с квадратными скобками и все нечисловые записи не перебирались. Полный клиент, сериализация эффектов, редактор мастера, бросок кубов и отправка чата не запускались. Параметры поля допускают конфигурирование; их отсутствие проверки в строковом методе описано как граница входов, а не как согласованное новое ограничение.

## Связанные проблемы

[issue-00033](../../../../../../issues/potential/issue-00033.md) — положительный модификатор атаки или защиты добавляется без '+' и делает строку невалидной. [issue-00004](../../../../../../issues/potential/issue-00004.md) — несовпадение commonspeech/commonsp в конфигурации/модели может нарушить доступ к полю навыка. Дублирование тела addDefenseModifiers само по себе отдельной ошибкой не зарегистрировано.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.007 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.017

2026-09-10, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; исходники неизменны. [Сверка](../../../../review-log.md#task-0003017).

Уточнён caller [RepairSystem.prepareRollFormula](../../../../../../../module/item/systems/repair.js): он добавляет фрагмент addActiveEffects('crafting') к 1d10+CRA+crafting. Настоящий метод дал +2[bonus] для allSkills и не добавил закрывающую скобку. Ошибка устаревшей настройки/незакрытой скобки принадлежит caller ([issue-00103](../../../../../../issues/potential/issue-00103.md)). Настоящие RollParser/grammar.pegjs приняли варианты с false и отклонили варианты с true; броски кубов не выполнялись.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Уточнён потребитель addActiveEffects: rollSkillCheck передаёт skillMapEntry.name, а rollCustomSkillCheck — Item.name. Неизвестный Item.name выходит до обработки allSkills; совпадающее встроенное имя адресует его Skill. Item.system.activeEffectModifiers данным helper не читается. Общий язык дополнительно попадает в commonsp/commonspeech рассогласование.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js); [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js). Полные карточки новых файлов — в [указателе порции](../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Настоящий addActiveEffects участвует в обоих ремесленных callbacks; подробный режим с подходящим именованным эффектом работает. При ненулевом activeEffectModifiers и пустом списке подходящих имён формируется +1[], которое отвергает парсер Foundry14 (issue-00204). Возникновение такого несогласованного Actor в мире не установлено.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../sheets/WitcherCharacterSheet.js.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Full profession direct attack передаёт addActiveEffects(attack.name), но объект attack имеет skill/alias без name. Group09 записала undefined, modifier вернул пустую строку при навыке awareness с AE+4. addAttackModifiers в этой ветке отсутствует; skillReplacement оружия обходит constructBaseAttackFormula. Новая 237 фиксирует пропуск, а 33 остаётся отдельной проблемой синтаксиса добавляемого общего модификатора.

[module/actor/mixins/professionMixin.js](professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.

## Дополнительная сверка TASK-0003.039

2026-09-11, `c598d74e34f4be51535de78b38f0601c286c5407`; исходники не менялись.

Полный castSpell добавляет addActiveEffects(usedSkill.name) и addAttackModifiers для всех типов магии, даже без causeDamages. Группы 09–10 проверили actual activeEffectModifiers/группу/боевой штраф и режим подписей. Это отличается от профессиональных атак .038, обходящих эти добавки.

[module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) — [карточка](castSpellMixin.js.md).

[Сценарии, методика и пределы проверки](../../../../review-log.md#task-0003039). Соседние определения проверены в пределах связи; это не расширяет состав шести полностью разобранных файлов.

## Дополнительная сверка TASK-0003.041

2026-09-12, rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; исходник не изменён.

[constructBaseAttackFormula](weaponAttackMixin.js.md) действительно вызывает addActiveEffects и addAttackModifiers: REF5, skill3, AE+2, attack−2 дают '1d10+5+3 +2 -2[Penalty]-1'. Ветка skillReplacement REF5/level4 даёт '1d10+5+4-1', не вызывая helpers. Положительный attackModifier снова не разбирается настоящим Roll (issue-00033).

[Сверка и ограничения](../../../../review-log.md#task-0003041). Уточнение связи не увеличивает пофайловое покрытие; исправления не выполнялись.
