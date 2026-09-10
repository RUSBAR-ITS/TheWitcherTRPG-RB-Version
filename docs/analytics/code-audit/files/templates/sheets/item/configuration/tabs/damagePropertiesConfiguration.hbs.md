# templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `8cca18e14b75ec53028ee6bc49a837597de4d9af` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.013](../../../../../../../../tasks/task-0003.013.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.013](../../../../../../review-log.md#task-0003013) |

## Назначение файла

Вкладка редактора свойств урона и предметных воздействий. Показывает базовые поля DamageProperties, изменяемые собственные effects и отдельный недоступный для редактирования список effects улучшений.

## Условия использования

PARTS.damageProperties WitcherPropertiesConfigurationSheet; наследуется конфигурациями Spell/Armor, но удаляется из parts при отсутствии соответствующих свойств. Требует tabs.damageProperties, item.system, systemFields, config.statusEffects и settings.silverTrait. Корень имеет data-tab='damageProperties', data-group='primary'.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Корень вкладки | 1–2 | Содержимое damageProperties | CSS из tabs | Рендер по PARTS, а не только наличию кнопки вкладки |
| Поля свойств | 3–23 | 16 formGroup в исходнике; две взаимоисключающие серебряные ветви и условный cap | systemFields.damageProperties.fields.* | Обычные inputs модели |
| Собственные effects | 26–62 | Таблица записей | each ...effects as effect id | addEffect/removeEffect/editEffect с data-target/id/field |
| Эффекты улучшений | 63–91 | Таблица enhancementsEffects | Getter DamageProperties | Все controls disabled; нет add/remove/edit actions |
| varEffect | 53–60,82–89 | Дополнительная строка вероятности от stamina | Условие ../item.system.staminaIsVar | Собственная editable либо disabled у улучшения |

## Основные функции и методы

Функций JS нет. Использованы formGroup, if/else, each с двумя block-params, selectOptions и localize. Поля: armorPiercing, improvedArmorPiercing, ablating, crushingForce, damageIsAblation, stun, damageToAllLocations, bypassesWornArmor, bypassesNaturalArmor, variableDamage; silverTrait либо silverDamage; isMeteorite, isNonLethal, defenseDifferenceMultiplier; defenseMultiplierCap при включённом множителе. oilEffect этой вкладкой не редактируется.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DamageProperties schema/effects/enhancementsEffects | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | Чтение схемы/данных/getter | Все свойства и два each | 18 полей модели сопоставлены; oilEffect отсутствует в formGroup |
| itemEffect | [module/data/item/templates/itemEffectData.js](../../../../../../../../../module/data/item/templates/itemEffectData.js) | Схема записи | name/statusEffect/percentage/varEffect | Типы и defaults |
| WitcherPropertiesConfigurationSheet | [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Рендер/context/actions | silverTrait setting; target.id.field updates | Методы 87–114 и смена поля 80–85 |
| CONFIG.WITCHER.statusEffects | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Справочник | Select statusEffect, nameAttr=id/valueAttr=id/labelAttr=name | Путь конфигурации |
| silverTrait setting | [module/setup/settings.js](../../../../../../../../../module/setup/settings.js) | Через context.settings | 13–17 | Две ветви проверены |
| staminaIsVar | [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | Поле родителя | 53,82; видимость varEffect | BooleanField в SpellData, отсутствует в WeaponData |
| formGroup/selectOptions/localize, Handlebars prototype access | Foundry 14.367.0, client/applications/handlebars.mjs | Внешний API | Генерация полей и вызов enhancementsEffects getter | Foundry renderTemplate разрешает prototype methods/properties |
| WITCHER.Weapon/Item/Spell/Percentage/table.* | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | Подписи schema и таблицы | Ключи/условия прочитаны |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Шаблон | PARTS.damageProperties | 14–18 |
| [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js); [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) | Inherited PART | Используют общий фильтр родителя | Для Armor фактически исключён |

## Данные и изменения состояния

Новые записи создаются target.ID={percentage:0}; начальные name/statusEffect/varEffect дополняет модель. Собственная строка задаёт data-target='system.damageProperties.effects' и data-id; inputs не имеют name, изменения слушает _onChangeForm. Удаление идёт по -={id}. Percentage — text input с data-dtype=Number, но ручной обработчик передаёт element.value строкой; NumberField очищает её позднее.

Disabled строки улучшений имеют тот же data-target, но не имеют editEffect actions и не должны отправляться как собственные эффекты. Getter разрешён обычными настройками renderTemplate Foundry; предупреждение чистого Handlebars о prototype access без этих настроек не является ошибкой системы.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Матрица из 8 сочетаний | silverTrait/staminaIsVar/defenseDifferenceMultiplier на настоящем SpellData | 14 либо 15 formGroup; корректная серебряная ветвь;3 либо 4 disabled controls улучшения; editable varEffect только при staminaIsVar | formGroup оригинальный; toFormGroup/selectOptions подменены |
| Действия строки | Сопоставление attrs с реальными методами конфигурации | add/remove/edit достигают ожидаемого пути; on превращается в false; удаление прошло на WeaponData | Запись Item перехвачена |
| Прототипный getter | Рендер с runtime-options из Foundry.renderTemplate | enhancementsEffects показал переданное улучшение | Набор улучшений задан в prepared-модель вручную |

## Непроверенные участки и открытые вопросы

Не запускались создание Actor/улучшений, вероятность эффектов, применение статусов и боевой цикл. Три поля прямо обозначены переводами как неработающие; наличие controls не подтверждает их расчёт. Область поиска — module/ и templates/.

## Связанные проблемы

[issue-00060](../../../../../../../../issues/potential/issue-00060.md) — имя on; [issue-00070](../../../../../../../../issues/potential/issue-00070.md) — prepared свойства Item могут измениться при сборке атаки, что важно отличать от ручных записей этой формы. Новых проблем разметки списка не зарегистрировано.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.013 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
