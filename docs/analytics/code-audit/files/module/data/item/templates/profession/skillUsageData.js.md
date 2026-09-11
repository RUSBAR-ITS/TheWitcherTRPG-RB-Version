# module/data/item/templates/profession/skillUsageData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/profession/skillUsageData.js](../../../../../../../../../module/data/item/templates/profession/skillUsageData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../../review-log.md#task-0003019) |

## Назначение файла

Вложенная модель настроек использования способности, включая выбор получателя и временное здоровье.

## Условия использования

SkillUsage extends foundry.abstract.DataModel, включён в professionSkill через EmbeddedDataField; не отдельный тип Item/ActiveEffect.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| SkillUsage/fields | Класс 5/alias3 | Схема 4 полей | Default export | defineSchema |
| hasCustomEffect | BooleanField8–11 | Выбор ветви использования | initial=false | Приоритет после isAttack, до thresholds |
| applySelf/applyOnTarget | BooleanField12–19 | Настройки получателя | initial=false | Форма показывает обе; потребитель читает только applyOnTarget |
| temporaryHealth | EmbeddedDataField20 | Настройки временных HP | TemporaryHealth | Вложенная модель |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema():6–22 | TemporaryHealth/fields | 4 поля | 3 BooleanField и EmbeddedDataField | Синхронно; без собственной apply/roll/update |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| TemporaryHealth | [module/data/item/templates/profession/temporaryHealthData.js](../../../../../../../../../module/data/item/templates/profession/temporaryHealthData.js) | Import/EmbeddedDataField | 1/20 | Полная модель |
| DataModel/BooleanField/EmbeddedDataField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs; common/abstract/data.mjs; common/abstract/type-data.mjs | Наследование/схема | 5–20 | Настоящие поля |
| Подписи | [lang/ru.json](../../../../../../../../../lang/ru.json) | Локализация | 3 label; часть ключей общая с Effect | ru/en проверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/templates/professionSkillData.js](../../../../../../../../../module/data/item/templates/professionSkillData.js) | SkillUsage | EmbeddedDataField | 3/18 |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | 4 поля | Условия и форма | 74–88 |
| [module/actor/mixins/professionMixin.js](../../../../../../../../../module/actor/mixins/professionMixin.js) | hasCustomEffect/applyOnTarget/temporaryHealth | _onProfessionRoll/doProfessionSkillUsage | applySelf поиском не найден в расчёте |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

hasCustomEffect выбирает doProfessionSkillUsage. Если temporaryHealth.addTemporaryHealth=false, эта ветвь не выполняет обычный бросок или иной эффект. applyOnTarget=true требует first target actor; иначе цель — this независимо от applySelf. Эта модель не связана с флагами одноимённого ActiveEffect и не переносит Item.effects.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все сочетания флагов | Настоящий doProfessionSkillUsage | false/false и true/false → caster; false/true и true/true → target | query/эффект/Roll-фасады |
| Отсутствующая цель | applyOnTarget=true | Уведомление noTarget и ранний возврат | Без пользовательского окна |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью. Изолированно использованы настоящие модели Foundry и системные методы; UI, TextEditor, Actor, Roll, запись и query частично заменены фасадами. Браузер, мир, БД и реальные броски не запускались. Связанные Actor-файлы прочитаны в пределах конкретных потребителей, не объявлены полностью разобранными.

## Связанные проблемы

[issue-00113](../../../../../../../../issues/potential/issue-00113.md). Флаг applySelf в этой модели не управляет получателем.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Dispatcher выбирает hasCustomEffect только после isAttack и до thresholds. Сам doProfessionSkillUsage не проверяет hasCustomEffect; если addTemporaryHealth=false, завершает без броска. Цель определяется applyOnTarget, applySelf не читается: группами 14/22 проверены другой Actor и оба self/target флага. Повторное применение/stack не проверены.

[module/actor/mixins/professionMixin.js](../../../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.
