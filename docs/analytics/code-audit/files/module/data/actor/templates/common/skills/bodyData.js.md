# module/data/actor/templates/common/skills/bodyData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/skills/bodyData.js](../../../../../../../../../../module/data/actor/templates/common/skills/bodyData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.002](../../../../../../../../../tasks/task-0003.002.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.002](../../../../../../../review-log.md#task-0003002) |

## Назначение файла

Определяет Body — группу BODY из 2 базовых навыков Actor и миграцию их ключей подписи.

## Условия использования

[skills()](../../../../../../../../../../module/data/actor/templates/common/skills/skillsData.js) создаёт EmbeddedDataField(Body) по ключу body; [CommonActorData.defineSchema](../../../../../../../../../../module/data/actor/commonActorData.js) включает результат в SchemaField skills. Путь экземпляра: system.skills.body. Для импорта требуются foundry.data.fields и foundry.abstract.DataModel.

## Введённые сущности и действия с ними

Экспорт по умолчанию — класс Body; локальный fields ссылается на API Foundry. Все поля таблицы — EmbeddedDataField([Skill](skillData.js.md), {label}). В колонках подписи приведены полные ключи; ключ skillMap и множитель стоимости проверены по config.js, но не задаются этой моделью.

| Ключ в system.skills.body | label поля группы | label после миграции | Ключ skillMap / costMultiplier |
| --- | --- | --- | --- |
| `physique` | `WITCHER.skills.physique.label` | `WITCHER.skills.physique.label` | `physique` / 1 |
| `endurance` | `WITCHER.skills.endurance.label` | `WITCHER.skills.endurance.label` | `endurance` / 1 |

Каждый навык содержит value, label, isVisible, activeEffectModifiers, isProfession, isPickup, isLearned; getter modifiedValue определён только в Skill.

## Основные функции и методы

- static defineSchema():6 создаёт 2 вложенных полей. Не принимает параметров, не вычисляет бросок и не вызывает Actor.update.
- static migrateData(source):14 перебирает ключи своей defineSchema(). Для каждого truthy source[skillName] присваивает label по шаблону WITCHER.skills.<ключ>.label, выполняет имеющиеся специальные замены и возвращает super.migrateData(source).
- Изменение выполняется в переданном объекте; имеющийся пользовательский label заменяется. Отсутствующий навык метод сам не создаёт. Значения и булевы признаки этот метод не изменяет.

Группа не содержит собственных расчётов выносливости или телосложения. Конфигурация и общий обработчик броска отдельно добавляют характеристику BODY.

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

Динамические потребители всех навыков перечислены с файлами и местами обращения в [карточке Skill](skillData.js.md): листы и edit-skills читают/изменяют поля system.skills.body.<навык>; rollSkillCheck читает value, addActiveEffects отдельно читает activeEffectModifiers; мастер и подсказки эффектов конструируют пути по skillMap; настройки монстра адресуют isVisible. Это связи по структуре данных, не импорты Body.

Точные строки путей обоих навыков найдены в JSON-компедиумах; карточка сборки содержит их индекс. Отдельной логики броска или изменения BODY в этом файле нет.

## Данные и изменения состояния

Схема определяет вложение и метаданные; единственная собственная мутация — label при миграции существующей записи. Значения, модификаторы и флаги очищаются общим Skill/Foundry. Сумма modifiedValue наследуется экземплярами Skill, а не классом группы; диапазон, стоимость обучения и порядок применения эффектов здесь не заданы.

## Проверки и доказательства

Файл прочитан полностью. На реальных DataModel/EmbeddedDataField Foundry 14.367.0 сверены 2 полей группы, все ссылки skillMap по attribute.name/name, метаданные и подписи после повторного создания CommonActorData. migrateData проверен на всех существующих навыках с label='custom', value=3 и true-флагами, а также на пустом объекте: label заменён, значения и флаги сохранены, отсутствующие записи не добавлены.

В общей проверке 52 внешних label не передаются в Skill.defineSchema; после сериализации/повторной загрузки label заполняет миграция групп, но isVisible.label остаётся undefined. Индивидуальные различия этой группы перечислены выше. Изолированные методы, шаблоны и JSON-пути сверены в журнале TASK-0003.002.

## Непроверенные участки и открытые вопросы

В .003 сверены схема, миграции и потребители; прежние этапы TASK-0003 завершены. N01 проверяет модели в памяти и сброс к source, не Actor.create в клиенте. Полный lifecycle и фазы — [U003-01](../../../../../../../cross-check-0002.md#u003-01)/02; отображение и сохранение формы — [U003-04](../../../../../../../cross-check-0002.md#u003-04). Игровые пределы не выбирались.

## Связанные проблемы

[issue-00015](../../../../../../../../../issues/closed/issue-00015.md), [issue-00018](../../../../../../../../../issues/potential/issue-00018.md) — наблюдения остаются potential.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.002 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.003

2026-09-14; rusbar-main, b4aeecb967caf97700cc565a670d6347b933619f. Исходник совпадает со срезом TASK-0001; изменено только описание.

Body задаёт 2 EmbeddedDataField(Skill) под группой body; миграция меняет label только существующих записей, не уровень навыка. Сверены адреса подписей: physique/endurance без переименования. Опция label внешнего поля не становится аргументом Skill.defineSchema; fresh/reconstructed различие проверено N01 для всех52 навыков. Поля и getter принадлежат вложенным Skill, формулы броска — внешним потребителям.

Сопоставленные определения и потребители: [module/data/actor/templates/common/skills/skillData.js](skillData.js.md), [module/data/actor/templates/common/skills/skillsData.js](skillsData.js.md), [module/setup/config.js](../../../../../setup/config.js.md), [module/actor/mixins/skillMixin.js](../../../../../actor/mixins/skillMixin.js.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004003) — TASK-0004.003; процессы [R003-04](../../../../../../../cross-check-0002.md#r003-04). Новое исполнение N01 протокола ограничено моделями и собственными расчётами Actor; остальные перечисленные опыты относятся к прежним порциям.
