# module/data/actor/templates/common/temporaryEffectsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/temporaryEffectsData.js](../../../../../../../../../module/data/actor/templates/common/temporaryEffectsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c34b790379fd98cd7e33ccbeeca085e49297a40f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.003](../../../../../../../../tasks/task-0003.003.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.003](../../../../../../review-log.md#task-0003003) |

## Назначение файла

Определяет вложенный словарь временных HP Actor. Несмотря на общее имя TemporaryEffects, собственная схема содержит только temporaryHp.

## Условия использования

Default export TemporaryEffects extends foundry.abstract.DataModel. Прямой импорт — [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../../../module/data/actor/templates/common/combatEffectsData.js):1; фабрика включает EmbeddedDataField(TemporaryEffects):39. В общей модели путь — system.combatEffects.temporaryEffects.

## Введённые сущности и действия с ними

| Поле / сущность | Тип и начало | Назначение |
| --- | --- | --- |
| TemporaryEffects | Класс :3 | Вложенная модель, не документ ActiveEffect. |
| temporaryHp | TypedObjectField(SchemaField), :6–11; {} | Словарь записей с произвольными ключами. |
| temporaryHp.<ключ>.name | StringField без явно заданного initial | Имя источника; при отсутствии остаётся undefined, обязательность здесь не задана. |
| temporaryHp.<ключ>.value | NumberField, initial=0; min/max/integer не заданы | Количество временных HP. |

temporaryHpSum не объявлен полем и не является getter этой модели. Длительность, disabled, origin и правила истечения здесь не хранятся.

## Основные функции и методы

static defineSchema():4–13 возвращает одно поле temporaryHp с двухполевой записью. Собственных методов суммирования, расхода, удаления, миграции или подготовки нет.

## Используемые сущности и зависимости

| Сущность | Определение | Связь |
| --- | --- | --- |
| DataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/data.mjs | Наследование :3. |
| TypedObjectField, SchemaField, StringField, NumberField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | Построение словаря и его записи :6–11. |
| combatEffects() | [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../../../module/data/actor/templates/common/combatEffectsData.js); [карточка](combatEffectsData.js.md) | Единственное найденное прямое вложение TemporaryEffects:39. |

## Известные потребители

| Файл | Место и условия |
| --- | --- |
| [module/actor/mixins/professionMixin.js](../../../../../../../../../module/actor/mixins/professionMixin.js) | Ветка temporaryHealth:274–326 после успешной проверки навыка создаёт ActiveEffect с changes к temporaryHp.<skill.skillName>, JSON name/value и duration.rounds. |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../../../../../../../module/scripts/temporaryEffects/applyActiveEffect.js) | applyActiveEffectToActor:31–69 переносит/клонирует эффекты на Actor через createEmbeddedDocuments; это обработчик документов, а не вызов TemporaryEffects. |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | V2:74–76, V1:39–41 присваивают temporaryHpSum как сумму Object.values(...temporaryHp).value в контексте, ссылающемся на живую модель. |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs); [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs); [templates/sheets/actor/monster-sheet.hbs](../../../../../../../../../templates/sheets/actor/monster-sheet.hbs) | Показывают добавку temporaryHpSum, если сумма >=1; последний шаблон отдельно от текущего sidebar. |
| [module/actor/mixins/damageMixin.js](../../../../../../../../../module/actor/mixins/damageMixin.js) | updateDerivedStat:121–147 при derivedStat='hp' выбирает temporaryEffects с изменением, содержащим temporaryHp; уменьшает JSON value изменений эффектов, затем записывает остаточный урон Actor. |
| [module/actor/witcherActor.js](../../../../../../../../../module/actor/witcherActor.js) | getter temporaryEffects:26–32 объединяет super.temporaryEffects и применённые временные улучшения Item. Это коллекция документов, не поле этой DataModel. |
| [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../../../../../module/actor/sheets/mixins/activeEffectMixin.js) | onManageActiveEffect:49–80 создаёт, удаляет или выключает документ-источник. Сама temporaryHp-запись не имеет отдельного переключателя/таймера. |

## Данные и изменения состояния

Заготовки name/value попадают в подготовленные данные через изменения ActiveEffect. Профессия формирует документ-источник, лист добавляет вычисленную сумму в память, расход HP изменяет changes этого документа. Нулевые записи updateDerivedStat не удаляет и эффект не удаляет: value устанавливается в 0. Исключение выключенного/удалённого источника из расчёта относится к жизненному циклу Foundry.

Восемь моделей этой порции не реализуют истечение длительности. Обычный Actor.system может также содержать сохранённые записи: отсутствие активного источника не доказывает, что любой одноимённый ключ должен исчезнуть.

## Проверки и доказательства

Прочитаны 14 строк, определение TemporaryEffects и прямое вложение. Реальные экземпляры дали пустой словарь по умолчанию и сумму 7 для двух записей 3/4. temporaryHpSum отсутствует до подготовки листом; чтение места присваивания подтверждено.

Исходный updateDerivedStat выполнен с временными HP=3 и дополнительным attackModifier=5 в одном эффекте. Урон 6 изменил второй бонус до 2 и оставил HP=10. Перехвачены аргументы update эффекта и Actor; запись в БД не выполнялась.

## Непроверенные участки и открытые вопросы

Не запускались профессия/её бросок, перенос через сеть, создание настоящего ActiveEffect, миграция формы changes и его истечение. Таймеры и применение фаз эффектов требуют полного разбора соответствующих файлов. Словарь не следует смешивать с Item типа temporaryItemImprovement или Actor.temporaryEffects.

## Связанные проблемы

[issue-00023](../../../../../../../../issues/potential/issue-00023.md) — расход временных HP обрабатывает также посторонние changes того же эффекта.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.003 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. Потребитель [TemporaryHealth профессии](../../../../../../../../../module/data/item/templates/profession/temporaryHealthData.js) в doProfessionSkillUsage создаёт один ADD-change temporaryHp.<skillName> с JSON name/value и duration.rounds. Контроль {Aid:{name:'Aid',value:7}} принят этой моделью. Выбор получателя/длительность/кавычки исследованы отдельно; модель результата не вычисляет эти значения. issue-00023 остаётся границей расхода нескольких changes; такой эффект не создаётся производителем в данном сценарии.

[Перекрёстная сверка](../../../../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Дополнительная сверка TASK-0003.038

2026-09-11, `rusbar-main`, `b47ba02cdaebc6a66ad14a5638213b6eb24460b4`; исходники не менялись.

Производитель HP создаёт key system.combatEffects.temporaryEffects.temporaryHp.<skillName> и строку name/value. Корректный d6-путь вычислил 9 HP в группе 14; выражение +2 без кубов дало невалидный JSON (240), кавычка в имени остаётся проблемой 117. Эти наблюдения сделаны до применения effects, прямой derivedStats.hp update отсутствует.

[module/actor/mixins/professionMixin.js](../../../../actor/mixins/professionMixin.js.md), [templates/partials/character/tab-profession.hbs](../../../../../templates/partials/character/tab-profession.hbs.md), [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs.md), [templates/dialog/combat/profession-attack.hbs](../../../../../templates/dialog/combat/profession-attack.hbs.md).

[Сверка и ограничения](../../../../../../review-log.md#task-0003038). Связанные файлы повторно в покрытии не учитывались; код и статусы issues не изменены.
