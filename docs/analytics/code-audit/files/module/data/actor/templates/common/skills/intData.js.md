# module/data/actor/templates/common/skills/intData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/skills/intData.js](../../../../../../../../../../module/data/actor/templates/common/skills/intData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.002](../../../../../../../../../tasks/task-0003.002.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.002](../../../../../../../review-log.md#task-0003002) |

## Назначение файла

Определяет Intelligence — группу INT из 13 базовых навыков Actor и миграцию их ключей подписи.

## Условия использования

[skills()](../../../../../../../../../../module/data/actor/templates/common/skills/skillsData.js) создаёт EmbeddedDataField(Intelligence) по ключу int; [CommonActorData.defineSchema](../../../../../../../../../../module/data/actor/commonActorData.js) включает результат в SchemaField skills. Путь экземпляра: system.skills.int. Для импорта требуются foundry.data.fields и foundry.abstract.DataModel.

## Введённые сущности и действия с ними

Экспорт по умолчанию — класс Intelligence; локальный fields ссылается на API Foundry. Все поля таблицы — EmbeddedDataField([Skill](skillData.js.md), {label}). В колонках подписи приведены полные ключи; ключ skillMap и множитель стоимости проверены по config.js, но не задаются этой моделью.

| Ключ в system.skills.int | label поля группы | label после миграции | Ключ skillMap / costMultiplier |
| --- | --- | --- | --- |
| `awareness` | `WITCHER.skills.awareness.label` | `WITCHER.skills.awareness.label` | `awareness` / 1 |
| `business` | `WITCHER.skills.business.label` | `WITCHER.skills.business.label` | `business` / 1 |
| `deduction` | `WITCHER.skills.deduction.label` | `WITCHER.skills.deduction.label` | `deduction` / 1 |
| `education` | `WITCHER.skills.education.label` | `WITCHER.skills.education.label` | `education` / 1 |
| `commonsp` | `WITCHER.skills.commonSpeech.label` | `WITCHER.skills.commonSpeech.label` | `commonspeech` / 2 |
| `eldersp` | `WITCHER.skills.elderSpeech.label` | `WITCHER.skills.elderSpeech.label` | `eldersp` / 2 |
| `dwarven` | `WITCHER.skills.dwarvenSpeech.label` | `WITCHER.skills.dwarvenSpeech.label` | `dwarven` / 2 |
| `monster` | `WITCHER.skills.monsterLore.label` | `WITCHER.skills.monsterLore.label` | `monster` / 2 |
| `socialetq` | `WITCHER.skills.socialEtiquette.label` | `WITCHER.skills.socialEtiquette.label` | `socialetq` / 1 |
| `streetwise` | `WITCHER.skills.streetwise.label` | `WITCHER.skills.streetwise.label` | `streetwise` / 1 |
| `tactics` | `WITCHER.skills.tactics.label` | `WITCHER.skills.tactics.label` | `tactics` / 2 |
| `teaching` | `WITCHER.skills.teaching.label` | `WITCHER.skills.teaching.label` | `teaching` / 1 |
| `wilderness` | `WITCHER.skills.wildernessSurvival.label` | `WITCHER.skills.wildernessSurvival.label` | `wilderness` / 1 |

Каждый навык содержит value, label, isVisible, activeEffectModifiers, isProfession, isPickup, isLearned; getter modifiedValue определён только в Skill.

## Основные функции и методы

- static defineSchema():6 создаёт 13 вложенных полей. Не принимает параметров, не вычисляет бросок и не вызывает Actor.update.
- static migrateData(source):25 перебирает ключи своей defineSchema(). Для каждого truthy source[skillName] присваивает label по шаблону WITCHER.skills.<ключ>.label, выполняет имеющиеся специальные замены и возвращает super.migrateData(source).
- Изменение выполняется в переданном объекте; имеющийся пользовательский label заменяется. Отсутствующий навык метод сам не создаёт. Значения и булевы признаки этот метод не изменяет.

Миграция исправляет подписи commonsp, eldersp, dwarven, monster, socialetq, wilderness. Ключ модели commonsp отличается от ключа skillMap.commonspeech; поле name справочника указывает commonsp. Polyglot читает языки по действительным ключам модели.

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

Динамические потребители всех навыков перечислены с файлами и местами обращения в [карточке Skill](skillData.js.md): листы и edit-skills читают/изменяют поля system.skills.int.<навык>; rollSkillCheck читает value, addActiveEffects отдельно читает activeEffectModifiers; мастер и подсказки эффектов конструируют пути по skillMap; настройки монстра адресуют isVisible. Это связи по структуре данных, не импорты Intelligence.

Особый потребитель — [module/TheWitcherTRPG.js](../../../../../../../../../../module/TheWitcherTRPG.js), getUserLanguages:102–130 читает языковые флаги и modifiedValue; common добавляется безусловно ещё до проверок. Подтверждены неверные пути commonspeech в chooseSkill, getSkillSuggestions, _getSkills и трёх Torn Stomach JSON; см. issue-00004.

## Данные и изменения состояния

Схема определяет вложение и метаданные; единственная собственная мутация — label при миграции существующей записи. Значения, модификаторы и флаги очищаются общим Skill/Foundry. Сумма modifiedValue наследуется экземплярами Skill, а не классом группы; диапазон, стоимость обучения и порядок применения эффектов здесь не заданы.

## Проверки и доказательства

Файл прочитан полностью. На реальных DataModel/EmbeddedDataField Foundry 14.367.0 сверены 13 полей группы, все ссылки skillMap по attribute.name/name, метаданные и подписи после повторного создания CommonActorData. migrateData проверен на всех существующих навыках с label='custom', value=3 и true-флагами, а также на пустом объекте: label заменён, значения и флаги сохранены, отсутствующие записи не добавлены.

В общей проверке 52 внешних label не передаются в Skill.defineSchema; после сериализации/повторной загрузки label заполняет миграция групп, но isVisible.label остаётся undefined. Индивидуальные различия этой группы перечислены выше. Изолированные методы, шаблоны и JSON-пути сверены в журнале TASK-0003.002.

## Непроверенные участки и открытые вопросы

Полный жизненный цикл документов, применение ActiveEffect, браузер, БД и соответствие механик рулбуку не проверялись. Указанные потребители просмотрены в пределах обращений к навыкам. Путь system.skills не следует смешивать с отдельными Item.skill или выбранными профессиональными умениями.

## Связанные проблемы

[issue-00015](../../../../../../../../../issues/potential/issue-00015.md), [issue-00018](../../../../../../../../../issues/potential/issue-00018.md), [issue-00004](../../../../../../../../../issues/potential/issue-00004.md) — наблюдения остаются potential.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.002 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Уточнены три потребителя commonsp/commonspeech: rollSkill('commonspeech') находит entry.name=commonsp, но addActiveEffects(commonsp) теряет добавку; levelUpSkill ломается для обоих написаний в разных местах; _getSkills конфигурации не находит одно isVisible-поле, поэтому formGroup выводит 51 вместо 52 строк.

Сверенные связи: [module/actor/mixins/skillMixin.js](../../../../../../../../../../module/actor/mixins/skillMixin.js); [templates/sheets/actor/configuration/partials/skillConfiguration.hbs](../../../../../../../../../../templates/sheets/actor/configuration/partials/skillConfiguration.hbs); [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs). Полные карточки новых файлов — в [указателе порции](../../../../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Конфигурация монстра строит путь по ключу skillMap.commonspeech, а модель хранит commonsp: запись есть, поле isVisible отсутствует, core formGroup выводит предупреждение и ничего не рисует. В общем количестве 52 записей остаётся 51 checkbox; прежняя issue-00004 не исправлена.

Связи: [module/actor/sheets/configurations/WitcherMonsterConfigurationSheet.js](../../../../../actor/sheets/configurations/WitcherMonsterConfigurationSheet.js.md). [Результаты и пределы проверки](../../../../../../../review-log.md#task-0003032).
