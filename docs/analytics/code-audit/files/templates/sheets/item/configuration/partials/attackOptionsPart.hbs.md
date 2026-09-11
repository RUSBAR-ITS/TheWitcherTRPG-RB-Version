# templates/sheets/item/configuration/partials/attackOptionsPart.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/partials/attackOptionsPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/attackOptionsPart.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `8cca18e14b75ec53028ee6bc49a837597de4d9af` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.013](../../../../../../../../tasks/task-0003.013.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.013](../../../../../../review-log.md#task-0003013) |

## Назначение файла

Общий фрагмент выбора вариантов атаки и связанных навыков/бонусов. В отличие от general.hbs использует правильную подпись раздела заклинания; поле навыка itemUse также не выводит.

## Условия использования

Partial предзагружается setup/handlebars и вызывается spellGeneral.hbs. Требует item.system, systemFields и config. Оружие использует похожую разметку непосредственно в general.hbs: этот partial не является его прямым потребителем.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Выбор attackOptions | formGroup2 | Включённые варианты атаки | SetField | options=config.attackOptions |
| Ветка melee | 4–13 | Навык и бонус | has melee | meleeAttackSkill/applyMeleeBonus |
| Ветка ranged | 14–24 | Навык, отдельный бонус и throwable | has ranged | rangedAttackSkill/applyRangedMeleeBonus/isThrowable |
| Ветка spell | 25–33 | Магический навык | has spell | spellAttackSkill; заголовок WITCHER.Attack.attackOptions.spell |

## Основные функции и методы

JS-функций нет. Семь formGroup, три условия if с helper has и три localize заголовка. Нет ветви itemUse и нет своих action/listener: поля сохраняются общей формой конфигурации.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| systemFields и item.system.* | [module/data/item/templates/combat/attackOptionsData.js](../../../../../../../../../module/data/item/templates/combat/attackOptionsData.js) | Schema/value | Все семь formGroup | Настоящий SpellData; пути system.* совпали |
| Контекст | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js); [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Передача item/systemFields/config | Готовится родителем general | Реальный _prepareContext |
| attackOptions/meleeAttackOptions/rangedAttackOptions/spellAttackOptions | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Чтение справочников | options= в четырёх группах | Определения списков |
| has | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Helper | Set.has в трёх условиях | Настоящий helper выполнен |
| formGroup/localize | Foundry 14.367.0, client/applications/handlebars.mjs | Helpers | Поля/тексты | formGroup исходный, field.toFormGroup заменён учётом путей |
| WITCHER.Attack.attackOptions.* | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | Три заголовка | Результаты рендера |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Partial | Предзагрузка,57 | Имя шаблона |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | Весь фрагмент | Включение 46 | Единственный прямой вызов в templates/ |

## Данные и изменения состояния

Значения выбираются из schema, вводы генерирует formGroup; необязательные ветви скрывают поля без удаления их данных. Набор CONFIG содержит itemUse, но здесь не создаётся itemUseAttackSkill. Существование отдельного applyRangedMeleeBonus в UI не подтверждает его применение к формуле.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все четыре варианта | SpellData.attackOptions=[melee,ranged,spell,itemUse] | Рендер семи полей, itemUseAttackSkill отсутствует | Генерация HTML controls подменена фасадом |
| Подписи | Настоящий Handlebars, ru.json | Ближний бой / Дальний бой / Заклинание | Остальные языки кроме en/ru не сверялись |
| Потребитель | rg в module/templates | Предзагрузка плюс spellGeneral | Не полный разбор spellGeneral |

## Непроверенные участки и открытые вопросы

Настройка заклинания и реальное сохранение выбранных навыков не запускались. Изолированный рендер не создаёт новый тип Item или новое правило атаки.

## Связанные проблемы

[issue-00061](../../../../../../../../issues/potential/issue-00061.md) дополнена вторым отсутствующим itemUse-редактором; [issue-00066](../../../../../../../../issues/potential/issue-00066.md) — неиспользуемый бонус; [issue-00064](../../../../../../../../issues/potential/issue-00064.md) — default spellcasting. Подпись spell в этом partial корректна, issue-00062 относится к general.hbs.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.013 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.021

Проверено 2026-09-11 на `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; исходник не менялся.

Подтверждён новый полностью разобранный потребитель spellGeneral.hbs. При варианте spell partial использует WITCHER.Attack.attackOptions.spell; issue62 изобщей general к этой ветви не относится. Все formGroup-поля partial найдены в SpellData через attackOptions. Поле itemUseAttackSkill здесь по-прежнему не отображается.

Сверенные карточки: [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../tabs/spellGeneral.hbs.md).

[Результаты и пределы сверки](../../../../../../review-log.md#task-0003021).
