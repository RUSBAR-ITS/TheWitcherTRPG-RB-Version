# templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs

## Актуальное изменение — 14.3.1.00142

Заголовок использует подготовленный skillHeading (при прямом включении без него прежний skillName). formGroup поля skillId получает локализованную подсказку. Все10 путей, кнопка явного ID, помощники и CRUD сохранены.

[Исходник](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) · [Проверки и границы](../../../../../../../../task-0012-checks.md#fixes-00142). Локальная приёмка выполнена; игровой повтор впереди. Более ранние датированные описания ниже — история.

## Актуальное изменение TASK-0012 — 14.3.1.00139

2026-09-20, dev. Поле/создание skillId; режим и условная проверка, поле полной формулы количества/срока с отдельным помощником, округление и единицы; расшифровка aliases. Пути definingSkill/skillPathN.skillN сохраняются, строки локализованы.

Связанные потребители/границы: TemporaryHealth, WitcherProfessionConfigurationSheet, ru/en. Статические проверки выполнены; браузер и БД не запускались. [Исходник](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) · [TASK-0012](../../../../../../../../../tasks/task-0012-temporary-hp.md) · [Проверки](../../../../../../../../task-0012-checks.md).

Ниже сохранены предыдущие срезы анализа с их датами; изменённый контракт определяется разделом выше.

## Текущее состояние

**14.3.1.00067, issue-00111.** Шаблон не изменён в .00067. Его removeEffectDamageProperties теперь зарегистрирован в конфигурации профессии; button и вложенная иконка приводят к выбранным slot/ID. Локально проверены definingSkill и два path-слота, имена не адрес. Другие data-target/data-item-id и формы из .008 сохранены.

[Исходник](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs); [проверка и пределы](../../../../../../../../issue-00111-checks.md).

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.019](../../../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../../../review-log.md#task-0003019) |

Актуализация [issue-00001](../../../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

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

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-06, R008-07, R008-11, R008-12, R008-15, R008-16, R008-20; оставшиеся границы: [U008-01](../../../../../../../cross-check-0002.md#u008-01), [U008-02](../../../../../../../cross-check-0002.md#u008-02), [U008-03](../../../../../../../cross-check-0002.md#u008-03). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00060](../../../../../../../../../issues/potential/issue-00060.md), [issue-00071](../../../../../../../../../issues/potential/issue-00071.md), [issue-00110](../../../../../../../../../issues/closed/issue-00110.md), [issue-00111](../../../../../../../../../issues/closed/issue-00111.md), [issue-00112](../../../../../../../../../issues/potential/issue-00112.md), [issue-00113](../../../../../../../../../issues/potential/issue-00113.md), [issue-00114](../../../../../../../../../issues/closed/issue-00114.md), [issue-00115](../../../../../../../../../issues/potential/issue-00115.md), [issue-00117](../../../../../../../../../issues/closed/issue-00117.md), [issue-00119](../../../../../../../../../issues/closed/issue-00119.md), [issue-00120](../../../../../../../../../issues/potential/issue-00120.md). Описание полей не подтверждает корректность правил или всего игрового процесса.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

Вложенный partial отображает атаку/защиту/usage/пороги по флагам навыка. Формовые пути используют slot, но CRUD строк передаёт data-target имени и data-id записи; removeEffectDamageProperties не зарегистрирован под таким именем. applySelf присутствует в форме, но runtime не использует его как условие цели.

Сопоставленные определения и потребители: [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](skillPathPart.hbs.md), [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js.md), [module/data/item/templates/professionSkillData.js](../../../../../../module/data/item/templates/professionSkillData.js.md), [module/data/item/templates/profession/skillUsageData.js](../../../../../../module/data/item/templates/profession/skillUsageData.js.md), [module/data/item/templates/profession/temporaryHealthData.js](../../../../../../module/data/item/templates/profession/temporaryHealthData.js.md), [module/data/item/templates/profession/thresholdData.js](../../../../../../module/data/item/templates/profession/thresholdData.js.md), [module/data/item/templates/combat/skillAttackData.js](../../../../../../module/data/item/templates/combat/skillAttackData.js.md), [module/data/item/templates/combat/skillDefenseData.js](../../../../../../module/data/item/templates/combat/skillDefenseData.js.md), [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../module/data/item/templates/combat/damagePropertiesData.js.md), [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](profAttackOptionsPart.hbs.md), [module/setup/config.js](../../../../../../module/setup/config.js.md), [lang/en.json](../../../../../../lang/en.json.md), [lang/ru.json](../../../../../../lang/ru.json.md), [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-06](../../../../../../../cross-check-0002.md#r008-06), [R008-07](../../../../../../../cross-check-0002.md#r008-07), [R008-11](../../../../../../../cross-check-0002.md#r008-11), [R008-12](../../../../../../../cross-check-0002.md#r008-12), [R008-15](../../../../../../../cross-check-0002.md#r008-15), [R008-16](../../../../../../../cross-check-0002.md#r008-16), [R008-20](../../../../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
