# module/data/item/templates/profession/temporaryHealthData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/profession/temporaryHealthData.js](../../../../../../../../../module/data/item/templates/profession/temporaryHealthData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.019](../../../../../../../../tasks/task-0003.019.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.019](../../../../../../review-log.md#task-0003019) |

## Назначение файла

Схема выдачи временного здоровья профессиональной способностью: условие проверки, формула количества и длительности.

## Условия использования

TemporaryHealth extends DataModel; используется только как EmbeddedDataField внутри SkillUsage. Расчёт реализован в professionMixin, не в классе.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| TemporaryHealth/fields | Класс 3/alias1 | Схема 3 верхних полей | Default export | defineSchema |
| addTemporaryHealth | BooleanField6–9 | Включение временных HP | initial=false | Форма/ветка использования |
| difficultyCheck | SchemaField10–24 | Порог и ограничение превышения | multiplier Number3; stat String int blank=false; maxRollOver Number5 | Собственных min/max/choices нет |
| temporaryHp | SchemaField25–34 | Строки расчёта | value='d6'; duration='2*@level' | Формулы не проверяются этой моделью |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema():4–36 | fields | Boolean +2 SchemaField с 5 вложенными полями | Задаёт defaults/labels и blank=false у stat | Не вычисляет длительность/HP, не создаёт ActiveEffect |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DataModel/BooleanField/SchemaField/NumberField/StringField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs; common/abstract/data.mjs; common/abstract/type-data.mjs | Наследование/поля | 3–34 | Реальные классы |
| Labels temporaryHealth | [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | Локализация | 6 leaf labels | Найдены в обоих языках |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/templates/profession/skillUsageData.js](../../../../../../../../../module/data/item/templates/profession/skillUsageData.js) | TemporaryHealth | EmbeddedDataField | Импорт 1/20 |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | difficultyCheck/temporaryHp | Условные поля | 79–87 |
| [module/actor/mixins/professionMixin.js](../../../../../../../../../module/actor/mixins/professionMixin.js) | Все настройки | doProfessionSkillUsage:274–320 | DC, rollOver, Roll, ActiveEffect и query |
| [module/data/actor/templates/common/temporaryEffectsData.js](../../../../../../../../../module/data/actor/templates/common/temporaryEffectsData.js) | Форма результата name/value | Косвенный получатель созданного change | Не импорт этой модели; путь temporaryHp |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Потребитель берёт target.stats[stat].max×multiplier, вызывает профессиональный бросок с showResult=false, затем отдельно toMessage. При rollOver>0 формирует значение как строку min(rollOver,maxRollOver)+temporaryHp.value; при наличии d вызывает Roll. По умолчанию превышение 3 даёт 3d6, выше потолка 5 — 5d6. Это значение — формула с префиксом, не прямое прибавление HP.

Длительность: replace первого @level → извлечение первой подстроки /\d+\*?\d+/g → eval. Затем создаётся ActiveEffect с одним ADD-change system.combatEffects.temporaryEffects.temporaryHp.<skillName>, JSON name/value, origin=caster.uuid и duration.rounds. getActorOwner(target).query вызывает applyActiveEffectToActor; завершения сообщения/query этот код не ждёт. Формирование payload не означает применения эффекта в мире. Actor TemporaryEffects — другая модель словаря уже выданных HP.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Defaults/blank | Настоящая схема | false;3/int/5;d6/2*@level; пустой stat не проходит validate | Без серверной формы |
| Успех/порог | Реальный метод на фасадах | DC24/12 по целям;rollOver0 не создаёт эффект;3→3d6;9→5d6; level2→4 раунда | Roll.total принудительно 7, случайность не проверяется |
| Длительность | Четыре строки,level3 | 2*@level→6;10→10;2 и 2+@level→TypeError | Описание нынешнего парсинга, не правила |
| JSON/приёмник | Реальная ветвь + TemporaryEffects | Aid→{name:Aid,value:7}; кавычка в имени делает JSON некорректным | ActiveEffect/query перехвачены, полный pipeline не запускался |

## Непроверенные участки и открытые вопросы

Исходник прочитан полностью. Изолированно использованы настоящие модели Foundry и системные методы; UI, TextEditor, Actor, Roll, запись и query частично заменены фасадами. Браузер, мир, БД и реальные броски не запускались. Связанные Actor-файлы прочитаны в пределах конкретных потребителей, не объявлены полностью разобранными.

## Связанные проблемы

[issue-00023](../../../../../../../../issues/potential/issue-00023.md), [issue-00113](../../../../../../../../issues/potential/issue-00113.md), [issue-00114](../../../../../../../../issues/potential/issue-00114.md), [issue-00117](../../../../../../../../issues/potential/issue-00117.md). issue-00023 — отдельная прежняя проблема расхода нескольких changes; здесь производитель создаёт один change.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.019 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Полный путь использует target.stats[stat].max×multiplier, а бросает владелец навыка. Строгий rollOver>0; cap ограничивает количество d6 по min. Группы 14–17 проверили цель/равенство/проигрыш/cap, default duration2*@level, длительность 2→TypeError(114), quote-name→JSON ошибка(117), новое "+2" без d→5+2 в JSON(240). Это payload перед конструктором эффекта, не запись HP в БД.

[module/actor/mixins/professionMixin.js](../../../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.
