# module/data/item/templates/professionSkillData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/professionSkillData.js](../../../../../../../../module/data/item/templates/professionSkillData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../review-log.md#task-0003019) |

## Назначение файла

Общая схема профессионального навыка: имя, характеристика, описание, уровень, атака, защита, использование и пороги.

## Условия использования

Default function professionSkill создаёт поля для definingSkill и девяти навыков путей. Не наследуется от базовой модели обычного навыка Actor и не содержит isProfession.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields / professionSkill | Alias6/функция 8–21 | 8 полей схемы | Default export | Каждый вызов создаёт новые DataField |
| skillName/stat | StringField10–11 | Название/код характеристики | initial='' | Без choices/ограничения уникальности |
| definition | HTMLField12 | Описание | initial='' | Обогащение выполняет ProfessionData |
| level | NumberField13 | Уровень | initial=0 | Нет собственного min/max/integer |
| skillAttack/skillDefense | SchemaField15–16 | Данные атак/защит | Две импортированные фабрики | Не отдельные документы |
| skillUsage/thresholds | EmbeddedDataField18–19 | Вложенные модели | SkillUsage/Threshold | Типизированные экземпляры DataModel |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| professionSkill() | 4 импорта и foundry.data.fields | 8 новых DataField | Собирает общие и вложенные данные | Синхронно; без записи, проверки правил роста и вызова броска |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| skillDefense() | [module/data/item/templates/combat/skillDefenseData.js](../../../../../../../../module/data/item/templates/combat/skillDefenseData.js) | Import/call | 1/16 | isDefense+DefenseProperties |
| skillAttack() | [module/data/item/templates/combat/skillAttackData.js](../../../../../../../../module/data/item/templates/combat/skillAttackData.js) | Import/call | 2/15 | isAttack/usesWeapon/formula/общие опции и свойства урона |
| SkillUsage | [module/data/item/templates/profession/skillUsageData.js](../../../../../../../../module/data/item/templates/profession/skillUsageData.js) | Import/EmbeddedDataField | 3/18 | 4 поля |
| Threshold | [module/data/item/templates/profession/thresholdData.js](../../../../../../../../module/data/item/templates/profession/thresholdData.js) | Import/EmbeddedDataField | 4/19 | Boolean и словарь порогов |
| fields | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs; common/abstract/data.mjs; common/abstract/type-data.mjs | Внешняя схема | 10–19 | String/HTML/Number/Schema/Embedded |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/professionData.js](../../../../../../../../module/data/item/professionData.js) | professionSkill() | definingSkill | Импорт 3/15 |
| [module/data/item/templates/professionPathData.js](../../../../../../../../module/data/item/templates/professionPathData.js) | professionSkill() | skill1–3 | Импорт 1/8–10 |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | skillAttack/skillDefense/skillUsage/thresholds | Включение настроек | Полный шаблон |
| [templates/sheets/item/profession-sheet.hbs](../../../../../../../../templates/sheets/item/profession-sheet.hbs) | skillName/stat/level/definition | 10 основных наборов полей | 47 именованных элементов всей формы |
| [module/actor/mixins/professionMixin.js](../../../../../../../../module/actor/mixins/professionMixin.js) | Все четыре ветви навыка | Выбор и выполнение | Приоритет isAttack→usage→threshold→roll |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Идентичность слота задаётся путём в профессии, но некоторые потребители вместо него используют skillName. Уровень -2 и произвольный stat приняты моделью; это отсутствие ограничений схемы, не согласованное правило. Пустой stat отличается от UI-значения none: Actor скрывает кнопку только для none. Бросок читает actor.stats[stat].value и level. Настройки основного навыка поддерживаются Actor-потребителем, но редактор путей его не включает.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Состав/значения | Настоящая модель | 8 полей; пустые строки/level0; отрицательный уровень и madeup stat приняты | Не правило допустимого уровня |
| Пустой навык | Исходный Actor-HBS и doProfessionSkillRoll | 10 видимых кнопок; stat='' дал TypeError до броска | DOM/Actor-фасады |
| Маршрутизация | Настоящий _onProfessionRoll | Четыре сочетания дали attack,usage,threshold,roll по приоритету | Операции после выбора заменены регистраторами |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью. Изолированно использованы настоящие модели Foundry и системные методы; UI, TextEditor, Actor, Roll, запись и query частично заменены фасадами. Браузер, мир, БД и реальные броски не запускались. Связанные Actor-файлы прочитаны в пределах конкретных потребителей, не объявлены полностью разобранными.

## Связанные проблемы

[issue-00110](../../../../../../../issues/potential/issue-00110.md), [issue-00112](../../../../../../../issues/potential/issue-00112.md), [issue-00118](../../../../../../../issues/potential/issue-00118.md). Речь об адресации, доступности конфигурации и предусловии броска.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
