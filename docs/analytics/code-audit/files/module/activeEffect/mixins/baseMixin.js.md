# module/activeEffect/mixins/baseMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/activeEffect/mixins/baseMixin.js](../../../../../../../module/activeEffect/mixins/baseMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `247d3d86e344238a1445377c686eb6455146693c` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.010](../../../../../../tasks/task-0003.010.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.010](../../../../review-log.md#task-0003010) |

## Назначение файла

Формирует каталог готовых путей для мастера обычного ActiveEffect: характеристики, навыки и группы навыков, модификаторы биографии, атаки и изменения получаемого урона.

## Условия использования

Подключён к WitcherActiveEffectConfig.prototype через Object.assign. Сборщик используется для type=base. Нужны CONFIG.WITCHER, game.i18n и this.document.parent для группы урона. Схемы не определяются здесь; возвращаются только label/value/group, а операция и величина задаются позднее в строке изменения.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| baseMixin | export let; 1–172 | Объект восьми методов | Прототип WitcherActiveEffectConfig | Синхронная генерация новых подсказок |
| Записи подсказок | label/value/group | value — строка или массив путей | selectOptions мастера | Ключи объекта — label, специальные имена либо индексы массива урона |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| getActiveEffectsBasePaths; 2–12 | Все семь групп ниже | Объединённый объект | Spread групп в порядке stat/tox/skillGroup/skill/lifepath/other/damage | 88 записей без damageTypeModification; 109 с семью типами урона |
| getStatSuggestions; 14–30 | CONFIG.WITCHER.statMap | 20 записей | Пропускает записи без origin; value=system.<origin>.<key>.totalModifiers; label либо labelShort | 9 stats + 11 derivedStats; reputation пропущена, shield не входит в statMap |
| getToxSuggestions; 32–40 | Локализация | 1 запись | system.stats.toxicity.totalModifiers | Toxicity добавляется отдельно |
| getSkillGroupSuggestions; 42–69 | skillGroups, соответствующие массивы CONFIG.WITCHER, skillMap | 6 записей с массивами value | Для каждого имени навыка строит путь; allSkills добавляет результаты getSkillSuggestions | Размеры all/melee/ranged/magic/verbal/empathetic: 52/5/3/3/7/6; нет проверки отсутствующего skill |
| getSkillSuggestions; 71–86 | CONFIG.WITCHER.skillMap | 52 записи | system.skills.<skill.attribute.name>.<ключ карты>.activeEffectModifiers | Ключ карты используется вместо skill.name; commonspeech расходится со схемой commonsp |
| getLifepathSuggestions; 87–123 | Фиксированные path/label prefixes | 6 записей | attacks.strong, attacks.joint, shieldParryBonus, shieldParryThrownBonus, ignoredArmorEncumbrance, ignoredEvWhenCasting | Первые два указывают на объект записи, без .value |
| getOtherSuggestions; 125–143 | Локализация | 3 записи | system.attackStats.meleeBonus/critLocationModifier/critEffectModifier | Численные величины не задаются |
| getDamageModifcators; 145–171 | damageTypeModification у parent.system либо parent.parent.system | Массив из 3 записей на тип урона | Для каждого ключа flat/multiplication/applyAP; группа resistances | Имя Modifcators сохранено как в коде; у источника Item вне Actor группа обычно пуста; parent=null не защищён |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| statMap, skillMap, skillGroups, массивы групп | [module/setup/config.js](../../../../../../../module/setup/config.js) | CONFIG.WITCHER | Ключи, подписи, attribute.name, origin | Все группы и пути перечислены/исполнены |
| totalModifiers | [module/data/actor/templates/common/stats/statData.js](../../../../../../../module/data/actor/templates/common/stats/statData.js); [module/data/actor/templates/common/stats/statsData.js](../../../../../../../module/data/actor/templates/common/stats/statsData.js); [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js) | Пути схемы | NumberField характеристик и производных | 20 путей + отдельная toxicity разрешились |
| activeEffectModifiers | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../module/data/actor/templates/common/skills/skillData.js) | Пути вложенной схемы | Модификатор навыка | Сопоставление с реальной CharacterData; commonsp уточняется в issue-00004 |
| lifepathModifiers | [module/data/actor/templates/common/lifepathData.js](../../../../../../../module/data/actor/templates/common/lifepathData.js) | Схема | Четыре NumberField и TypedObjectField attacks с SchemaField({value}) | Два пути attacks разрешаются в SchemaField, не NumberField |
| attackStats | [module/data/actor/templates/character/attackStatsData.js](../../../../../../../module/data/actor/templates/character/attackStatsData.js) | Схема | meleeBonus/critLocationModifier/critEffectModifier | Соответствие путей реальной модели |
| damageTypeModification | [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](../../../../../../../module/data/actor/templates/character/general/damage/damageTypeModificationData.js); [module/data/actor/templates/character/general/damage/damageModificationData.js](../../../../../../../module/data/actor/templates/character/general/damage/damageModificationData.js) | Схема и данные владельца | 7 типов × flat/multiplication/applyAP | flat/multiplication численные, applyAP логическое поле |
| game.i18n.localize, WITCHER.Stats/skills/Effect/Actor/DamageType | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json); внешнее i18n | Локализация | Группы и подписи | Ключи строятся из конфигурации и имён полей |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | baseMixin / getActiveEffectsBasePaths | Импорт, Object.assign, ветка base мастера | Не вызывается при temporaryItemImprovement |
| [templates/dialog/activeEffects/wizard.hbs](../../../../../../../templates/dialog/activeEffects/wizard.hbs) | Объект подсказок | selectOptions превращает массив value в строку с запятыми | Список путей затем делится wizardAction |

## Данные и изменения состояния

Нет записи документов, расчёта бонусов, изменения потолка или фильтрации по текущему Actor.type. Данные урона выбираются по уже имеющимся ключам владельца; в остальных группах используются общие карты. При spread массива damage его индексы становятся числовыми ключами результирующего объекта и перечисляются раньше строковых ключей, хотя эта группа записана последней.

Проверены 179 вхождений путей после раскрытия групп при семи типах урона. Два вхождения commonspeech не разрешаются; это один и тот же путь из одиночной подсказки и allSkills. Два attacks.strong/joint разрешаются в объектный SchemaField. Остальные разрешаются в поле CharacterData; это подтверждение схемы, не корректности всех игровых вычислений.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Состав | Полное чтение 172 строк, исходные восемь методов с картой WITCHER | 20+1+6+52+6+3+21=109 вариантов; без урона88 | Параметры владельца заданы явно |
| Пути | Настоящая CharacterData.getFieldForProperty; раскрытие массивов групп | 179 вхождений; commonspeech отсутствует дважды; strong/joint — SchemaField | Дубликаты групп намеренно не удалялись |
| Сериализация | Настоящие selectOptions/prepareSelectOptionGroups ядра, HTML-обёртка подменена | Группа навыков становится строкой путей через запятую | Браузер не запускался |

## Непроверенные участки и открытые вопросы

Не проверены все режимы changes для каждого типа поля, произвольные Actor/Item и все динамически добавленные навыки. Для полного процесса урона/атак остаются damageMixin, weaponAttackMixin, defenseMixin, armorMixin, castSpellMixin; их связанные обращения прочитаны, целиком они не разобраны.

## Связанные проблемы

[issue-00004](../../../../../../issues/potential/issue-00004.md) — commonsp/commonspeech; [issue-00019](../../../../../../issues/potential/issue-00019.md) — attacks без .value. Группа урона связана с [issue-00025](../../../../../../issues/potential/issue-00025.md), [issue-00026](../../../../../../issues/potential/issue-00026.md), [issue-00027](../../../../../../issues/potential/issue-00027.md); это ошибки потребителей, не новые проблемы этого каталога.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.010 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
