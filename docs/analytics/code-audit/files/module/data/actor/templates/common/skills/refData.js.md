# module/data/actor/templates/common/skills/refData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/skills/refData.js](../../../../../../../../../../module/data/actor/templates/common/skills/refData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.002](../../../../../../../../../tasks/task-0003.002.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.002](../../../../../../../review-log.md#task-0003002) |

## Назначение файла

Определяет Reflex — группу REF из 8 базовых навыков Actor и миграцию их ключей подписи.

## Условия использования

[skills()](../../../../../../../../../../module/data/actor/templates/common/skills/skillsData.js) создаёт EmbeddedDataField(Reflex) по ключу ref; [CommonActorData.defineSchema](../../../../../../../../../../module/data/actor/commonActorData.js) включает результат в SchemaField skills. Путь экземпляра: system.skills.ref. Для импорта требуются foundry.data.fields и foundry.abstract.DataModel.

## Введённые сущности и действия с ними

Экспорт по умолчанию — класс Reflex; локальный fields ссылается на API Foundry. Все поля таблицы — EmbeddedDataField([Skill](skillData.js.md), {label}). В колонках подписи приведены полные ключи; ключ skillMap и множитель стоимости проверены по config.js, но не задаются этой моделью.

| Ключ в system.skills.ref | label поля группы | label после миграции | Ключ skillMap / costMultiplier |
| --- | --- | --- | --- |
| `brawling` | `WITCHER.skills.brawling.label` | `WITCHER.skills.brawling.label` | `brawling` / 1 |
| `dodge` | `WITCHER.skills.dodgeEscape.label` | `WITCHER.skills.dodgeEscape.label` | `dodge` / 1 |
| `melee` | `WITCHER.skills.melee.label` | `WITCHER.skills.melee.label` | `melee` / 1 |
| `riding` | `WITCHER.skills.riding.label` | `WITCHER.skills.riding.label` | `riding` / 1 |
| `sailing` | `WITCHER.skills.sailing.label` | `WITCHER.skills.sailing.label` | `sailing` / 1 |
| `smallblades` | `WITCHER.skills.smallblades.label` | `WITCHER.skills.smallblades.label` | `smallblades` / 1 |
| `staffspear` | `WITCHER.skills.staffspear.label` | `WITCHER.skills.staffspear.label` | `staffspear` / 1 |
| `swordsmanship` | `WITCHER.skills.swordsmanship.label` | `WITCHER.skills.swordsmanship.label` | `swordsmanship` / 1 |

Каждый навык содержит value, label, isVisible, activeEffectModifiers, isProfession, isPickup, isLearned; getter modifiedValue определён только в Skill.

## Основные функции и методы

- static defineSchema():6 создаёт 8 вложенных полей. Не принимает параметров, не вычисляет бросок и не вызывает Actor.update.
- static migrateData(source):20 перебирает ключи своей defineSchema(). Для каждого truthy source[skillName] присваивает label по шаблону WITCHER.skills.<ключ>.label, выполняет имеющиеся специальные замены и возвращает super.migrateData(source).
- Изменение выполняется в переданном объекте; имеющийся пользовательский label заменяется. Отсутствующий навык метод сам не создаёт. Значения и булевы признаки этот метод не изменяет.

Миграция уточняет label dodge до WITCHER.skills.dodgeEscape.label; сам ключ остаётся dodge. В компедиумах встречаются как ref.dodge.activeEffectModifiers, так и ref.dodge.value.

## Используемые сущности и зависимости

| Сущность | Файл определения / API | Вид связи, место и цель |
| --- | --- | --- |
| Skill | [module/data/actor/templates/common/skills/skillData.js](../../../../../../../../../../module/data/actor/templates/common/skills/skillData.js) | Прямой импорт :1 и EmbeddedDataField в defineSchema; семь полей и getter — в [карточке Skill](skillData.js.md). |
| DataModel | Внешний API /opt/foundryvtt/common/abstract/data.mjs, Foundry 14.367.0 | Наследование :5 и super.migrateData(source); возвращаемый объект не записывается здесь в документ. |
| EmbeddedDataField | Внешний API /opt/foundryvtt/common/data/fields.mjs | Создание поля с моделью Skill; label — метаданные внешнего поля, не аргумент Skill.defineSchema. |
| Ключи WITCHER.skills | [lang/en.json](../../../../../../../../../../lang/en.json) и [lang/ru.json](../../../../../../../../../../lang/ru.json) | Строковые ссылки defineSchema/migrateData; проверены после разбора JSON. |
| WITCHER.skillMap | [module/setup/config.js](../../../../../../../../../../module/setup/config.js) | Сопоставленный внешний справочник для потребителей. Эта модель его не импортирует и не читает. |

## Известные потребители

Прямой импорт класса найден в [module/data/actor/templates/common/skills/skillsData.js](../../../../../../../../../../module/data/actor/templates/common/skills/skillsData.js); соответствующая [карточка](skillsData.js.md) описывает единственный вызов skills() в CommonActorData и содержит индекс конкретных JSON-потребителей по группам.

Динамические потребители всех навыков перечислены с файлами и местами обращения в [карточке Skill](skillData.js.md): листы и edit-skills читают/изменяют поля system.skills.ref.<навык>; rollSkillCheck читает value, addActiveEffects отдельно читает activeEffectModifiers; мастер и подсказки эффектов конструируют пути по skillMap; настройки монстра адресуют isVisible. Это связи по структуре данных, не импорты Reflex.

Динамическое чтение боевых навыков проверено в [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../../module/actor/mixins/weaponAttackMixin.js), constructBaseAttackFormula:315–325, и [module/actor/mixins/defenseMixin.js](../../../../../../../../../../module/actor/mixins/defenseMixin.js):135–140. Конкретный навык выбирает внешний сценарий, модель группы его не назначает.

## Данные и изменения состояния

Схема определяет вложение и метаданные; единственная собственная мутация — label при миграции существующей записи. Значения, модификаторы и флаги очищаются общим Skill/Foundry. Сумма modifiedValue наследуется экземплярами Skill, а не классом группы; диапазон, стоимость обучения и порядок применения эффектов здесь не заданы.

## Проверки и доказательства

Файл прочитан полностью. На реальных DataModel/EmbeddedDataField Foundry 14.367.0 сверены 8 полей группы, все ссылки skillMap по attribute.name/name, метаданные и подписи после повторного создания CommonActorData. migrateData проверен на всех существующих навыках с label='custom', value=3 и true-флагами, а также на пустом объекте: label заменён, значения и флаги сохранены, отсутствующие записи не добавлены.

В общей проверке 52 внешних label не передаются в Skill.defineSchema; после сериализации/повторной загрузки label заполняет миграция групп, но isVisible.label остаётся undefined. Индивидуальные различия этой группы перечислены выше. Изолированные методы, шаблоны и JSON-пути сверены в журнале TASK-0003.002.

## Непроверенные участки и открытые вопросы

Полный жизненный цикл документов, применение ActiveEffect, браузер, БД и соответствие механик рулбуку не проверялись. Указанные потребители просмотрены в пределах обращений к навыкам. Путь system.skills не следует смешивать с отдельными Item.skill или выбранными профессиональными умениями.

## Связанные проблемы

[issue-00015](../../../../../../../../../issues/potential/issue-00015.md), [issue-00018](../../../../../../../../../issues/potential/issue-00018.md) — наблюдения остаются potential.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.002 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
