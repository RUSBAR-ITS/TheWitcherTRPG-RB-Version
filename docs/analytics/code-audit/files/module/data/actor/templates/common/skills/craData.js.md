# module/data/actor/templates/common/skills/craData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/skills/craData.js](../../../../../../../../../../module/data/actor/templates/common/skills/craData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.002](../../../../../../../../../tasks/task-0003.002.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.002](../../../../../../../review-log.md#task-0003002) |

## Назначение файла

Определяет Craft — группу CRA из 7 базовых навыков Actor и миграцию их ключей подписи.

## Условия использования

[skills()](../../../../../../../../../../module/data/actor/templates/common/skills/skillsData.js) создаёт EmbeddedDataField(Craft) по ключу cra; [CommonActorData.defineSchema](../../../../../../../../../../module/data/actor/commonActorData.js) включает результат в SchemaField skills. Путь экземпляра: system.skills.cra. Для импорта требуются foundry.data.fields и foundry.abstract.DataModel.

## Введённые сущности и действия с ними

Экспорт по умолчанию — класс Craft; локальный fields ссылается на API Foundry. Все поля таблицы — EmbeddedDataField([Skill](skillData.js.md), {label}). В колонках подписи приведены полные ключи; ключ skillMap и множитель стоимости проверены по config.js, но не задаются этой моделью.

| Ключ в system.skills.cra | label поля группы | label после миграции | Ключ skillMap / costMultiplier |
| --- | --- | --- | --- |
| `alchemy` | `WITCHER.skills.alchemy.label` | `WITCHER.skills.alchemy.label` | `alchemy` / 2 |
| `crafting` | `WITCHER.skills.crafting.label` | `WITCHER.skills.crafting.label` | `crafting` / 2 |
| `disguise` | `WITCHER.skills.disguise.label` | `WITCHER.skills.disguise.label` | `disguise` / 1 |
| `firstaid` | `WITCHER.skills.firstAid.label` | `WITCHER.skills.firstaid.label` | `firstaid` / 1 |
| `forgery` | `WITCHER.skills.forgery.label` | `WITCHER.skills.forgery.label` | `forgery` / 1 |
| `picklock` | `WITCHER.skills.pickLock.label` | `WITCHER.skills.picklock.label` | `picklock` / 1 |
| `trapcraft` | `WITCHER.skills.trapCrafting.label` | `WITCHER.skills.trapcraft.label` | `trapcraft` / 2 |

Каждый навык содержит value, label, isVisible, activeEffectModifiers, isProfession, isPickup, isLearned; getter modifiedValue определён только в Skill.

## Основные функции и методы

- static defineSchema():6 создаёт 7 вложенных полей. Не принимает параметров, не вычисляет бросок и не вызывает Actor.update.
- static migrateData(source):19 перебирает ключи своей defineSchema(). Для каждого truthy source[skillName] присваивает label по шаблону WITCHER.skills.<ключ>.label, выполняет имеющиеся специальные замены и возвращает super.migrateData(source).
- Изменение выполняется в переданном объекте; имеющийся пользовательский label заменяется. Отсутствующий навык метод сам не создаёт. Значения и булевы признаки этот метод не изменяет.

У firstaid, picklock, trapcraft подписи EmbeddedDataField имеют camelCase, а migrateData создаёт нижнерегистровые ключи, существующие в en/ru. Первые три ключа отсутствуют во всех восьми языках. В skillMap неверны label picklock и label/rollLabel trapcraft; firstaid.label там корректен.

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

Динамические потребители всех навыков перечислены с файлами и местами обращения в [карточке Skill](skillData.js.md): листы и edit-skills читают/изменяют поля system.skills.cra.<навык>; rollSkillCheck читает value, addActiveEffects отдельно читает activeEffectModifiers; мастер и подсказки эффектов конструируют пути по skillMap; настройки монстра адресуют isVisible. Это связи по структуре данных, не импорты Craft.

Особые потребители — [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js):298–310,391–392 (alchemy/crafting.value и label), [module/item/systems/repair.js](../../../../../../../../../../module/item/systems/repair.js):209 (crafting.value). Полные процессы изготовления и ремонта не запускались.

## Данные и изменения состояния

Схема определяет вложение и метаданные; единственная собственная мутация — label при миграции существующей записи. Значения, модификаторы и флаги очищаются общим Skill/Foundry. Сумма modifiedValue наследуется экземплярами Skill, а не классом группы; диапазон, стоимость обучения и порядок применения эффектов здесь не заданы.

## Проверки и доказательства

Файл прочитан полностью. На реальных DataModel/EmbeddedDataField Foundry 14.367.0 сверены 7 полей группы, все ссылки skillMap по attribute.name/name, метаданные и подписи после повторного создания CommonActorData. migrateData проверен на всех существующих навыках с label='custom', value=3 и true-флагами, а также на пустом объекте: label заменён, значения и флаги сохранены, отсутствующие записи не добавлены.

В общей проверке 52 внешних label не передаются в Skill.defineSchema; после сериализации/повторной загрузки label заполняет миграция групп, но isVisible.label остаётся undefined. Индивидуальные различия этой группы перечислены выше. Изолированные методы, шаблоны и JSON-пути сверены в журнале TASK-0003.002.

## Непроверенные участки и открытые вопросы

Полный жизненный цикл документов, применение ActiveEffect, браузер, БД и соответствие механик рулбуку не проверялись. Указанные потребители просмотрены в пределах обращений к навыкам. Путь system.skills не следует смешивать с отдельными Item.skill или выбранными профессиональными умениями.

## Связанные проблемы

[issue-00015](../../../../../../../../../issues/potential/issue-00015.md), [issue-00018](../../../../../../../../../issues/potential/issue-00018.md), [issue-00016](../../../../../../../../../issues/potential/issue-00016.md) — наблюдения остаются potential.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.002 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Полный разбор UI показал, где проявляются прежние несовпадающие label: текущая/старая строка и редактор вызывают localize skill.label; исправлений словарей нет. calc_total_skills использует '(2)' из перевода, а levelUpSkill — отдельный costMultiplier карты; эти источники коэффициента не объединены.

Сверенные связи: [templates/partials/character/skill-display.hbs](../../../../../../../../../../templates/partials/character/skill-display.hbs); [templates/partials/monster/monster-skill-display.hbs](../../../../../../../../../../templates/partials/monster/monster-skill-display.hbs); [templates/sheets/actor/configuration/app/edit-skills.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/edit-skills.hbs); [module/actor/sheets/mixins/skillMixin.js](../../../../../../../../../../module/actor/sheets/mixins/skillMixin.js); [module/actor/mixins/skillMixin.js](../../../../../../../../../../module/actor/mixins/skillMixin.js). Полные карточки новых файлов — в [указателе порции](../../../../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.
