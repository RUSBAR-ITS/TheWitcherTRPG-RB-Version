# templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../../../review-log.md#task-0003019) |

## Назначение файла

Частичный редактор вариантов профессиональной атаки: набор видов атаки и условные флаги ближнего/дальнего применения.

## Условия использования

Включается skillPathSkillPart только при skillAttack.isAttack=true. Получает systemFields=skillAttack.fields и system=skillAttack; config наследуется.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| attackOptions formGroup | 1–3 | Выбор множества вариантов | options=config.attackOptions | SetField из общей фабрики |
| melee секция | 4–7 | Заголовок/бонус | has('melee',system.attackOptions) | applyMeleeBonus |
| ranged секция | 8–12 | Заголовок/2 флага | has('ranged',system.attackOptions) | applyRangedMeleeBonus/isThrowable |

## Основные функции и методы

Функций/классов нет. Helper has вызывает Set.has; на пустом Set выводится только attackOptions. Для melee/ranged добавляются соответствующие поля; собственных секций spell/itemUse нет.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| skillPathSkillPart | [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | Включение/контекст | 9 | skillAttack fields и данные |
| attackOptions() | [module/data/item/templates/combat/attackOptionsData.js](../../../../../../../../../../module/data/item/templates/combat/attackOptionsData.js) | Поля схемы | attackOptions/applyMeleeBonus/applyRangedMeleeBonus/isThrowable | Фабрика общая с оружием |
| WITCHER.attackOptions | [module/setup/config.js](../../../../../../../../../../module/setup/config.js) | Варианты | formGroup3 | melee/ranged/spell/itemUse |
| has/helper предзагрузки | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Helper/partial registration | has:147–149;load:59 | Настоящий helper использует Set.has |
| Подписи | [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | localize/labels | melee/ranged и поля | Проверены |
| formGroup | Foundry 14.367.0, /opt/foundryvtt/client/applications/handlebars.mjs | Helper | Поля | Реальная metadata, DOM-регистратор |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | Варианты атаки | Partial при isAttack | 9 |
| [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Путь partial | loadHandlebarTemplates | 59 |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Редактирует флаги модели через полный DataField.fieldPath; собственных кнопок/обработчиков нет. С выбором melee+ranged выводятся 4 formGroup. При выбранном spell/itemUse дополнительных полей этот шаблон не вводит; это не общий выбор навыка оружия: professionMixin берёт собственные stat/level и первый attackOptions. usesWeapon выбирается снаружи.

doProfessionAttackRoll читает applyMeleeBonus; applyRangedMeleeBonus в его вычислениях не найден — прежняя issue-00066. isThrowable участвует в default attackOptions, но отдельного расчёта броска этим фрагментом не делает.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пустой/все варианты | Настоящие Set/has/HBS | 1 formGroup на пустом;4 для melee+ranged;spell/itemUse не добавили секций | Проверка рендера;полный бой не запускался |
| Потребитель бонуса | professionMixin:59–81 | Расчёт читает applyMeleeBonus | Дополнение прежней границы .012 |

## Непроверенные участки и открытые вопросы

В TASK-0004.008 текущий файл и его связи сопоставлены с датированными протоколами TASK-0003.018/.019 (2026-09-10) и .038 (2026-09-11), в пределах относящихся к нему сценариев. Новых поведенческих запусков нет; прежние настоящие модели/методы и фасады различены в протоколе. Браузерный submit, мир, сеть и запись в БД не проверены. Установлены процессы R008-06, R008-15, R008-16, R008-20; оставшиеся границы: [U008-01](../../../../../../../cross-check-0002.md#u008-01), [U008-03](../../../../../../../cross-check-0002.md#u008-03). Полный пофайловый разбор соседей в TASK-0003 не равен проверке клиентского lifecycle.

## Связанные проблемы

[issue-00066](../../../../../../../../../issues/potential/issue-00066.md). Не переносить автоматически issue-00061 про выбор базового itemUse-навыка оружия на эту форму: профессиональный навык выбирается иначе.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.008

2026-09-14; rusbar-main, f96434101e0e827838c2e6a3e09da8933a9801ef. Исходник совпадает со срезом TASK-0001; изменено только описание.

Partial читает skillAttack.attackOptions как Set и показывает applyMeleeBonus для melee, applyRangedMeleeBonus/isThrowable для ranged. Ветка исполнения выбирается usesWeapon; runtime прямой атаки не реализует каждую показанную опцию автоматически.

Сопоставленные определения и потребители: [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](skillPathSkillPart.hbs.md), [module/data/item/templates/combat/attackOptionsData.js](../../../../../../module/data/item/templates/combat/attackOptionsData.js.md), [module/setup/config.js](../../../../../../module/setup/config.js.md), [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js.md), [lang/en.json](../../../../../../lang/en.json.md), [lang/ru.json](../../../../../../lang/ru.json.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004008) — TASK-0004.008; процессы [R008-06](../../../../../../../cross-check-0002.md#r008-06), [R008-15](../../../../../../../cross-check-0002.md#r008-15), [R008-16](../../../../../../../cross-check-0002.md#r008-16), [R008-20](../../../../../../../cross-check-0002.md#r008-20). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
