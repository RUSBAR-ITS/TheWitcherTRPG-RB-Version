# module/data/actor/templates/common/skills/skillData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../../../../module/data/actor/templates/common/skills/skillData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.002](../../../../../../../../../tasks/task-0003.002.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.002](../../../../../../../review-log.md#task-0003002) |

## Назначение файла

Определяет вложенную модель одного базового навыка Actor: семь сохраняемых полей и вычисляемое значение modifiedValue. Это DataModel, а не самостоятельный документ Item или ActiveEffect.

## Условия использования

Модуль читает глобальный foundry при импорте. Семь групп создают EmbeddedDataField(Skill, {label}), по одному для каждого из 52 навыков. Общая модель Actor подключает группы через skills(). Прямой регистрации Skill в CONFIG.Item.dataModels нет: тип Item.skill использует отдельный [SkillItemData](../../../../../../../../../../module/data/item/skillItemData.js).

## Введённые сущности и действия с ними

Экспорт по умолчанию — класс Skill, наследующий foundry.abstract.DataModel. Локальный fields — ссылка на foundry.data.fields.

| Поле / свойство | Тип и начало | Действие / смысл |
| --- | --- | --- |
| value | NumberField, initial=0 | Базовое значение навыка; в файле нет min/max/integer. |
| label | StringField, initial=label | Ключ подписи; параметр defineSchema(label) по фактическому пути вложения не передан. |
| isVisible | BooleanField, initial=false, label=label | Флаг отображения; подпись метаданных также зависит от непереданного параметра. |
| activeEffectModifiers | NumberField, initial=0 | Числовой модификатор; вычисление эффектов находится вне этой модели. |
| isProfession | BooleanField, initial=false | Признак профессионального навыка. |
| isPickup | BooleanField, initial=false | Признак дополнительного навыка. |
| isLearned | BooleanField, initial=false | Признак изученного навыка. |
| modifiedValue | getter, не поле схемы | value + activeEffectModifiers; не сериализуется в toObject(). |

## Основные функции и методы

- static defineSchema(label):4–14 возвращает объект семи полей; не изменяет экземпляр. Внешний DataModelSchemaField вызывает model.defineSchema() без аргументов.
- get modifiedValue():16–18 возвращает сумму при чтении, без записи и ограничений. При value=1, activeEffectModifiers=-4 результат -3; 12 и 3 дают 15; 2.5 и 0.5 дают 3.
- Собственных migrateData, prepareDerivedData и update нет. Наследуемые механизмы очистки и сериализации принадлежат Foundry.

## Используемые сущности и зависимости

| Сущность | Определение | Связь и доказательство |
| --- | --- | --- |
| DataModel | Внешний API: /opt/foundryvtt/common/abstract/data.mjs, Foundry 14.367.0 | Наследование :3; жизненный цикл схемы и экземпляра. |
| NumberField, StringField, BooleanField | Внешний API: /opt/foundryvtt/common/data/fields.mjs | Создание полей :6–12; DataField.toFormGroup:662–667 выбирает label либо fieldPath. |
| EmbeddedDataField → DataModelSchemaField | То же fields.mjs:2717–2730 | Внешний вызывающий код использует model.defineSchema() без аргумента; options.label остаётся на поле группы. |
| Intelligence | [module/data/actor/templates/common/skills/intData.js](../../../../../../../../../../module/data/actor/templates/common/skills/intData.js) | Импорт Skill:1, вложение для 13 навыков; [карточка](intData.js.md). |
| Reflex | [module/data/actor/templates/common/skills/refData.js](../../../../../../../../../../module/data/actor/templates/common/skills/refData.js) | Импорт Skill:1, вложение для 8 навыков; [карточка](refData.js.md). |
| Dexterity | [module/data/actor/templates/common/skills/dexData.js](../../../../../../../../../../module/data/actor/templates/common/skills/dexData.js) | Импорт Skill:1, вложение для 5 навыков; [карточка](dexData.js.md). |
| Body | [module/data/actor/templates/common/skills/bodyData.js](../../../../../../../../../../module/data/actor/templates/common/skills/bodyData.js) | Импорт Skill:1, вложение для 2 навыков; [карточка](bodyData.js.md). |
| Empathy | [module/data/actor/templates/common/skills/empData.js](../../../../../../../../../../module/data/actor/templates/common/skills/empData.js) | Импорт Skill:1, вложение для 10 навыков; [карточка](empData.js.md). |
| Craft | [module/data/actor/templates/common/skills/craData.js](../../../../../../../../../../module/data/actor/templates/common/skills/craData.js) | Импорт Skill:1, вложение для 7 навыков; [карточка](craData.js.md). |
| Will | [module/data/actor/templates/common/skills/willData.js](../../../../../../../../../../module/data/actor/templates/common/skills/willData.js) | Импорт Skill:1, вложение для 7 навыков; [карточка](willData.js.md). |

## Известные потребители

| Потребитель | Связь с данными и место обращения |
| --- | --- |
| [module/actor/mixins/skillMixin.js](../../../../../../../../../../module/actor/mixins/skillMixin.js) | rollSkillCheck:46–83 читает value по skillMapEntry.attribute.name/name, затем вызывает addActiveEffects; levelUpSkill:7–40 записывает value и очки развития через Actor.update. |
| [module/actor/mixins/modifierMixin.js](../../../../../../../../../../module/actor/mixins/modifierMixin.js) | addActiveEffects:2–36 читает activeEffectModifiers и skillGroupModifiers; собирает строку формулы, не меняет Skill. |
| [module/actor/sheets/mixins/skillMixin.js](../../../../../../../../../../module/actor/sheets/mixins/skillMixin.js) | calc_total_skills:2–15 суммирует value; удвоение определяет по '(2)' в локализованном label. skillListener:27–42 связывает кнопки броска и повышения с Actor. |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | _onDropItem:26–51 сбрасывает isProfession у всех навыков и выставляет по professionSkills предмета профессии. |
| [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../../../../../../module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js) | _getSkills:65–89 извлекает isVisible и значение флага через skillMap; шаблон skillConfiguration получает эти поля. |
| [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../../../../../../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs) | formGroup выводит полученный isVisible, localize=true; явной подписи навыка нет. |
| [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs) | Поля value, isProfession, isPickup, isLearned адресуются по ключам system.skills; activeEffectModifiers показан в отключённом поле. |
| [templates/partials/character/tab-skills.hbs](../../../../../../../../../../templates/partials/character/tab-skills.hbs) | Перебирает system.skills по группам; текущая вкладка и персонажа, и монстра передаёт Skill в skill-display. |
| [templates/partials/character/skill-display.hbs](../../../../../../../../../../templates/partials/character/skill-display.hbs) | Читает label, modifiedValue и три признака обучения; data-skill получает ключ модели; isVisible не читает. |
| [templates/partials/monster/monster-skill-display.hbs](../../../../../../../../../../templates/partials/monster/monster-skill-display.hbs) | Другой имеющийся шаблон скрывает навык по isVisible и выводит value. Текущий PARTS.skills листа монстра на него не указывает. |
| [module/activeEffect/mixins/baseMixin.js](../../../../../../../../../../module/activeEffect/mixins/baseMixin.js) | getSkillSuggestions:71–85 строит пути activeEffectModifiers из ключа skillMap; getSkillGroupSuggestions использует их для allSkills. |
| [module/activeEffect/witcherActiveEffect.js](../../../../../../../../../../module/activeEffect/witcherActiveEffect.js) | chooseSkill:73–107 формирует такой же путь; исполнение и сохранение ActiveEffect здесь не проверялось. |

Дополнительные потребители по назначению:

| Файл | Обращение |
| --- | --- |
| [module/TheWitcherTRPG.js](../../../../../../../../../../module/TheWitcherTRPG.js) | getUserLanguages:102–130 читает modifiedValue и признаки обучения языков int.eldersp/dwarven/commonsp; common добавляется также безусловно. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | constructBaseAttackFormula:315–325 читает value по attribute.name/name, затем вызывает addActiveEffects. |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../../module/actor/mixins/defenseMixin.js) | Формирование защиты:135–140 читает skill.value; возможен skillOverride. |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../../../module/actor/mixins/castSpellMixin.js) | Бросок:30 читает will[usedSkill.name].value. |
| [module/actor/mixins/verbalCombatMixin.js](../../../../../../../../../../module/actor/mixins/verbalCombatMixin.js) | Строка 46: value по навыку настройки вербального боя. |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | Строка 64: аналогичное чтение value защитника. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Обработчики изготовления:298–310,391–392 читают cra.alchemy/crafting.value и label. |
| [module/item/systems/repair.js](../../../../../../../../../../module/item/systems/repair.js) | Строка 209 читает cra.crafting.value исполнителя. |
| [Сборка skills и индекс JSON-потребителей](skillsData.js.md) | В 37 JSON-файлах компедиумов найдены 267 строковых путей system.skills; указатель конкретных файлов приведён в карточке сборки. |

## Данные и изменения состояния

Getter только читает. Начальное заполнение и валидацию выполняет Foundry, миграцию label — классы групп. Здесь не вычисляются цена развития, ограничения по правилам, значение характеристики, броня, групповые или социальные модификаторы. Три признака обучения независимы: модель не исключает одновременные true. Никакого Actor.update или записи в БД в Skill нет.

NumberField не задаёт ограничения диапазона и целочисленности; испытаны конечные числа, включая отрицательный итог и дроби. Это описание кода, а не утверждение о допустимости значений по рулбуку.

## Проверки и доказательства

Полностью прочитаны 19 строк. Изолированно загружены реальные поля и DataModel Foundry 14.367.0; сверены семь полей, 52 вложения, пять числовых примеров, отсутствие modifiedValue в toObject(). В new CommonActorData({}) label отсутствует у 52 навыков; после toObject() и повторного создания группы заполняют 52 label. Метаданные isVisible.label остаются undefined, а toFormGroup с подставленным input выбирает техническую подпись isVisible.

Выполнены исходные методы формирования путей, формулы навыка, повышения и два шаблона Handlebars с явными подменами внешних действий. Сценарий и результаты — в записи TASK-0003.002 журнала.

## Непроверенные участки и открытые вопросы

Создание реального Actor через клиент/сервер и повторные миграции при сохранении не воспроизводились: наблюдение свежей CommonActorData нельзя приравнивать к окончательному виду созданного документа. Не проверены применение ActiveEffect к Actor, DOM, полные процессы боя/изготовления и сторонние модули. Соседние файлы прочитаны в пределах связей и не получают статус полного разбора.

## Связанные проблемы

[issue-00004](../../../../../../../../../issues/potential/issue-00004.md), [issue-00015](../../../../../../../../../issues/potential/issue-00015.md), [issue-00016](../../../../../../../../../issues/potential/issue-00016.md), [issue-00017](../../../../../../../../../issues/potential/issue-00017.md), [issue-00018](../../../../../../../../../issues/potential/issue-00018.md). Все остаются potential; код системы не исправлялся.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.002 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.005

2026-09-10, `c9eac1ffb28fdf69935d500fff26d4d0ad1d1609`. Полностью описан [Log](../../character/logData.js.md) — потребитель levelUpSkill. Повторная проверка с настоящим Log показала два payloads для magic: 6 из журнала и 10 из levelUpSkill; дополнена [issue-00017](../../../../../../../../../issues/potential/issue-00017.md). [skillTrainingData](../../character/skillTrainingData.js.md) задаёт отдельные ручные слоты name/value, не экземпляры Skill; их кнопка списывает обычные IP и не повышает system.skills.

[Сверка TASK-0003.005](../../../../../../../review-log.md#task-0003005).

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. modifierMixin.addActiveEffects читает activeEffectModifiers напрямую и собирает имена подходящих appliedEffects, но не пересчитывает число из changes. Skill.modifiedValue не используется этим методом; неизвестный ключ skillMap даёт пустую строку до обработки групп.

Карточки: [WitcherActor](../../../../../actor/witcherActor.js.md), [modifierMixin](../../../../../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../../../../../review-log.md#task-0003007).
