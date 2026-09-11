# templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../../../review-log.md#task-0003019) |

## Назначение файла

Редактор механик одного навыка пути: атака, защита, применение, временные HP, предметные воздействия и пороги.

## Условия использования

Вызывается skillPathPart трижды на вкладку. skillFields — SchemaField навыка, skill — подготовленные данные, config наследуется от part-context.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| profession-card/h3 | 1–4 | Имя навыка | skill.skillName | Отображение, не поле редактирования имени |
| Атака | 5–65 | isAttack и условные свойства | usesWeapon/formula/options/defenseOptions/DamageProperties | При false скрывает настройки, не очищает их |
| Строки effects | 28–62 | ID→name/statusEffect/percentage | data-id, data-target=skillName, data-field | Без name; запись по change/action |
| Защита | 67–72 | isDefense;defendsAgainst;modifier | formGroup | parrying этой формой не редактируется |
| Применение/HP | 74–88 | hasCustomEffect/applySelf/applyOnTarget/temporaryHealth | Условные formGroup | DC multiplier/stat/maxRollOver;HP value/duration |
| Пороги | 91–119 | hasThresholds и ID→name/value | 6 действий всего вместе с effects | name/value без name; data-target=skillName |

## Основные функции и методы

Функций/классов нет. if выбирает видимость свойств и таблиц; each обходит effects/thresholds с ID в строке. formGroup получает соответствующий DataField/value; selectOptions statusEffects выводит список по id/name. Смена ручных полей маршрутизируется через _onChangeForm.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| skillPathPart | [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) | Включение/контекст | Три навыка | skillFields и skill |
| WitcherProfessionConfigurationSheet | [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) | Actions/change-handler | CRUD таблиц | Имена/аргументы сверены |
| professionSkill/SkillUsage/TemporaryHealth/Threshold | [module/data/item/templates/professionSkillData.js](../../../../../../../../../../module/data/item/templates/professionSkillData.js); [module/data/item/templates/profession/skillUsageData.js](../../../../../../../../../../module/data/item/templates/profession/skillUsageData.js); [module/data/item/templates/profession/temporaryHealthData.js](../../../../../../../../../../module/data/item/templates/profession/temporaryHealthData.js); [module/data/item/templates/profession/thresholdData.js](../../../../../../../../../../module/data/item/templates/profession/thresholdData.js) | Поля | Ветки атаки/защиты/HP/порогов | Все пути найдены в настоящей схеме |
| SkillAttack/SkillDefense/DamageProperties | [module/data/item/templates/combat/skillAttackData.js](../../../../../../../../../../module/data/item/templates/combat/skillAttackData.js); [module/data/item/templates/combat/skillDefenseData.js](../../../../../../../../../../module/data/item/templates/combat/skillDefenseData.js); [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | Вложенные поля | 5–71 | Схемы из .012 |
| profAttackOptionsPart | [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) | Partial | 9 | Дополнительные formGroup по attackOptions |
| config.attackOptions/statOptions/statusEffects | [module/setup/config.js](../../../../../../../../../../module/setup/config.js) | Варианты | Защита/HP/статус | statOptions формирует основной лист; has в соседнем partial |
| Подписи | [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | localize/labels | Add/RemoveEffect,Effect,Percentage,Name,thresholds и поля | В ru отсутствуют 3 thresholds; прочие пробелы skillMap отделены |
| Handlebars/formGroup/selectOptions | Foundry 14.367.0, /opt/foundryvtt/client/applications/handlebars.mjs; Handlebars 4.7.9 | Рендер | Условия/контекст | DataField metadata настоящие, конечные formGroup DOM — фасады |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) | Редактор skillN | Partial трижды | 2–4 |
| [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Путь шаблона | loadHandlebarTemplates | 58 |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

В полностью включённом навыке с melee+ranged и defenseMultiplierCap выводится 35 formGroup; у выключенного —4 главных флага. Табличные input/select идут сверх formGroup и сохраняются по data-action. Передаётся skillName, поэтому повтор имён может направить запись в другой слот.

Набор полей DamageProperties здесь включает armorPiercing,improvedArmorPiercing,ablating,crushingForce,damageIsAblation,damageToAllLocations,bypassesWornArmor,bypassesNaturalArmor,variableDamage,silverDamage,isMeteorite,isNonLethal,defenseDifferenceMultiplier и условный defenseMultiplierCap. oilEffect/silverTrait/varEffect не редактируются этим фрагментом. Строка effects — предметное воздействие; создание ActiveEffect в отдельных настройках не выполняется.

removeEffectDamageProperties не зарегистрировано под этим именем; editEffectDamageProperties с текстом on заменяет его на checked. Пороги допускают включение пустого списка. applySelf и applyOnTarget отображаются отдельно, но Actor использует только второй для выбора получателя.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все флаги/ветки | Рендер двух заполненных и одного пустого навыка | 74 formGroup;корректные path/id/target;6 data-action | DOM/запись не исполнялись |
| Действия | Сопоставление HBS/actions и core dispatch | removeEffectDamageProperties без handler;on→false в edit | Подтверждены конкретные маршруты |
| HP/пороги | Настоящие Actor-потребители | DC/формулы/получатель и пустой порог прослежены | Roll,ActiveEffect,query,Dialog — фасады |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью. Системные классы листов настоящие, ItemSheetV2/HandlebarsApplicationMixin работают поверх DocumentSheet-фасада. Рендер проверяет контекст/поля и маршруты; реальный браузер, права, сохранение Item и работа нескольких клиентов не проверены.

## Связанные проблемы

[issue-00060](../../../../../../../../../issues/potential/issue-00060.md), [issue-00071](../../../../../../../../../issues/potential/issue-00071.md), [issue-00110](../../../../../../../../../issues/potential/issue-00110.md), [issue-00111](../../../../../../../../../issues/potential/issue-00111.md), [issue-00112](../../../../../../../../../issues/potential/issue-00112.md), [issue-00113](../../../../../../../../../issues/potential/issue-00113.md), [issue-00114](../../../../../../../../../issues/potential/issue-00114.md), [issue-00115](../../../../../../../../../issues/potential/issue-00115.md), [issue-00117](../../../../../../../../../issues/potential/issue-00117.md), [issue-00119](../../../../../../../../../issues/potential/issue-00119.md), [issue-00120](../../../../../../../../../issues/potential/issue-00120.md). Описание полей не подтверждает корректность правил или всего игрового процесса.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
