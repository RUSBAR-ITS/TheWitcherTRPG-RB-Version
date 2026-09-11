# module/data/actor/commonActorData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.006](../../../../../../tasks/task-0003.006.md), одна порция из четырёх файлов |
| Запись перекрёстной сверки | [TASK-0003.006](../../../../review-log.md#task-0003006) |

## Назначение файла

Общая TypeDataModel для персонажа и монстра: собирает 19 полей system, подготавливает исходные максимумы и часть производных баз, считает массу монет, переносит отдельные старые поля. Самостоятельного типа Actor для CommonActorData нет.

## Условия использования

При загрузке нужен глобальный foundry. Локальная fields ссылается на foundry.data.fields. [CharacterData](../../../../../../../module/data/actor/characterData.js) и [MonsterData](../../../../../../../module/data/actor/monsterData.js) наследуют класс; [LootData](../../../../../../../module/data/actor/lootData.js) наследует TypeDataModel самостоятельно. [registerDataModels](../../../../../../../module/setup/registerDataModels.js):35–43 регистрирует только специализированные классы, CommonActorData не имеет собственного ключа.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const:15 | Классы полей | Локальная | Чтение при defineSchema |
| CommonActorData | class:17–134 | Общая модель | Default export | Наследование; создание схемы; подготовка; миграция |

| Поле system | Строка | Тип и начальное значение | Определение и смысл |
| --- | --- | --- | --- |
| currency | 20 | SchemaField(currency()) | Семь валют → common/currencyData.js. |
| healthState | 21 | SchemaField; два вложенных SchemaField | woundThreshold и deathState; у каждого applied=false, ignored=false. Все четыре — BooleanField, определены здесь:22–29. |
| deathSaves | 31 | NumberField, initial=0 | Счётчик штрафа спасбросков; своих min/max/integer нет. |
| stats | 33 | EmbeddedDataField(Stats) | Десять показателей → common/stats/statsData.js → statData.js. |
| derivedStats | 34 | EmbeddedDataField(DerivedStats) | 12 производных показателей → common/stats/derivedStatsData.js → statData.js. |
| reputation | 36 | EmbeddedDataField(Reputation) | Числовая репутация → common/reputationData.js → statData.js. |
| adrenaline | 37 | SchemaField(adrenaline()) | value/label → common/adrenalineData.js. |
| skills | 39 | SchemaField(skills()) | Семь групп, 52 EmbeddedDataField(Skill) → common/skills/skillsData.js и файлы групп. |
| skillGroupModifiers | 40 | TypedObjectField(SchemaField) | Произвольные ID; запись name:StringField, group:StringField без explicit initial; value:NumberField=0. Определено здесь:40–46. |
| attackStats | 47 | SchemaField(attackStats()) | Бонус ближнего боя, punch/kick, два crit-модификатора → character/attackStatsData.js. |
| combatEffects | 48 | SchemaField(combatEffects()) | Модификаторы атаки/защиты, начала хода и временные HP → common/combatEffectsData.js. |
| damageTypeModification | 49 | SchemaField(damageTypeModification()) | Семь типов воздействия → character/general/damage/damageTypeModificationData.js. |
| focus1 | 51 | SchemaField(focus()) | Отдельный слот name/value → common/focusData.js; не derivedStats.focus. |
| focus2 | 52 | SchemaField(focus()) | Отдельный слот name/value → common/focusData.js; не derivedStats.focus. |
| focus3 | 53 | SchemaField(focus()) | Отдельный слот name/value → common/focusData.js; не derivedStats.focus. |
| focus4 | 54 | SchemaField(focus()) | Отдельный слот name/value → common/focusData.js; не derivedStats.focus. |
| notes | 56 | ArrayField(SchemaField(note())) | Массив title/details → common/noteData.js. |
| pannels | 57 | SchemaField(pannels()) | 22 флага false → character/pannelsData.js; написание ключа сохранено. |
| lifepathModifiers | 59 | SchemaField(lifepathData()) | Четыре числа и словарь attacks → common/lifepathData.js. |

Пути в последнем столбце отсчитываются от module/data/actor/templates; все 13 источников связаны ниже с исходниками и карточками. Значения и ограничения вложенных полей задают эти источники. Папка character у некоторых фабрик не ограничивает их применение персонажем. Свойства name/img/type/items/effects принадлежат документу Actor, а не этой схеме system.

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema:18–61 | Классы Foundry и 13 импортов | Объект 19 полей | Вызовы фабрик, включение трёх EmbeddedDataField | Синхронно; super.defineSchema не вызывается; не пишет документы. |
| prepareBaseData:63–91 | Инициализированные stats/derivedStats/reputation | undefined | Копирование максимумов и формулы ниже | Присваивания в модели в памяти; без update, catch и super.prepareBaseData. |
| calcCurrencyWeight:93–103 | currency с семью значениями | Number | Сумма Number каждого номинала ×0.001 | Не меняет состояние; не округляет вверх; нет проверки отрицательных/нечисловых значений. |
| static migrateData(source):106–115 | Объект исходных данных; вложения могут отсутствовать | super.migrateData(source) | Если vigor.unmodifiedMax == 0, перенос value; затем два метода ниже | Синхронно меняет переданный source; сам не пишет БД. В проверенном ядре super возвращает тот же объект. |
| static migrateCalculatedStats(source):117–129 | Объект, возможны отсутствующие вложения | undefined | Обнуляет truthy meleeBonus и девять totalModifiers | Optional chaining; исходный объект; нулевые/отсутствующие поля не трогает. |
| static migrateAdrenaline(source):131–133 | Объект с возможным adrenaline | undefined | При adrenaline и falsy value записывает current в value | Ноль тоже заменяется; старое current не удаляет; нет проверки наличия current. |

Обозначим B=stats.body.unmodifiedMax, W=stats.will.unmodifiedMax, I=stats.int.unmodifiedMax, S=stats.spd.unmodifiedMax, M=floor((B+W)/2). Полный список присваиваний prepareBaseData:

| Цель | Присваивание | Строки |
| --- | --- | --- |
| stats.{int,ref,dex,body,spd,emp,cra,will,toxicity,luck}.max | Соответствующее unmodifiedMax | 64–74 |
| reputation.max | reputation.unmodifiedMax | 75 |
| derivedStats.stun.unmodifiedMax | Math.clamp(M,1,10) | 79 |
| derivedStats.run.unmodifiedMax | S×3 | 81 |
| derivedStats.leap.unmodifiedMax | floor(S×3/5) | 82 |
| derivedStats.enc.unmodifiedMax | B×10 | 83 |
| derivedStats.rec.unmodifiedMax | M | 84 |
| derivedStats.woundTreshold.unmodifiedMax | M; это фактическое написание, в healthState другой ключ woundThreshold | 85 |
| derivedStats.resolve.unmodifiedMax | (W+I)×5 | 87 |
| derivedStats.focus.unmodifiedMax | (stats.will.value+stats.int.value)×3; используются текущие value, не W/I | 88 |
| derivedStats.vigor.max | derivedStats.vigor.unmodifiedMax | 90 |

Метод не рассчитывает hp/sta/shield, не присваивает всем производным max/value и не применяет общего диапазона 1–10 ко всем характеристикам. Ограничение в этом файле относится только к базовому stun. Итоговые вычисления выполняет WitcherActor; это отдельный этап.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| currency | [module/data/actor/templates/common/currencyData.js](../../../../../../../module/data/actor/templates/common/currencyData.js); [карточка](templates/common/currencyData.js.md) | Прямой импорт : 1 | currency:20 | Определение и включение схемы сверены. |
| adrenaline | [module/data/actor/templates/common/adrenalineData.js](../../../../../../../module/data/actor/templates/common/adrenalineData.js); [карточка](templates/common/adrenalineData.js.md) | Прямой импорт : 2 | adrenaline:37 | Определение и включение схемы сверены. |
| skills | [module/data/actor/templates/common/skills/skillsData.js](../../../../../../../module/data/actor/templates/common/skills/skillsData.js); [карточка](templates/common/skills/skillsData.js.md) | Прямой импорт : 3 | skills:39 | Определение и включение схемы сверены. |
| focus | [module/data/actor/templates/common/focusData.js](../../../../../../../module/data/actor/templates/common/focusData.js); [карточка](templates/common/focusData.js.md) | Прямой импорт : 4 | focus1–4:51–54 | Определение и включение схемы сверены. |
| note | [module/data/actor/templates/common/noteData.js](../../../../../../../module/data/actor/templates/common/noteData.js); [карточка](templates/common/noteData.js.md) | Прямой импорт : 5 | notes:56 | Определение и включение схемы сверены. |
| attackStats | [module/data/actor/templates/character/attackStatsData.js](../../../../../../../module/data/actor/templates/character/attackStatsData.js); [карточка](templates/character/attackStatsData.js.md) | Прямой импорт : 6 | attackStats:47 | Определение и включение схемы сверены. |
| pannels | [module/data/actor/templates/character/pannelsData.js](../../../../../../../module/data/actor/templates/character/pannelsData.js); [карточка](templates/character/pannelsData.js.md) | Прямой импорт : 7 | pannels:57 | Определение и включение схемы сверены. |
| lifepathData | [module/data/actor/templates/common/lifepathData.js](../../../../../../../module/data/actor/templates/common/lifepathData.js); [карточка](templates/common/lifepathData.js.md) | Прямой импорт : 8 | lifepathModifiers:59 | Определение и включение схемы сверены. |
| damageTypeModification | [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](../../../../../../../module/data/actor/templates/character/general/damage/damageTypeModificationData.js); [карточка](templates/character/general/damage/damageTypeModificationData.js.md) | Прямой импорт : 9 | damageTypeModification:49 | Определение и включение схемы сверены. |
| combatEffects | [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js); [карточка](templates/common/combatEffectsData.js.md) | Прямой импорт : 10 | combatEffects:48 | Определение и включение схемы сверены. |
| DerivedStats | [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js); [карточка](templates/common/stats/derivedStatsData.js.md) | Прямой импорт : 11 | derivedStats:34; prepareBaseData:79–90 | Определение и включение схемы сверены. |
| Stats | [module/data/actor/templates/common/stats/statsData.js](../../../../../../../module/data/actor/templates/common/stats/statsData.js); [карточка](templates/common/stats/statsData.js.md) | Прямой импорт : 12 | stats:33; prepareBaseData:64–88 | Определение и включение схемы сверены. |
| Reputation | [module/data/actor/templates/common/reputationData.js](../../../../../../../module/data/actor/templates/common/reputationData.js); [карточка](templates/common/reputationData.js.md) | Прямой импорт : 13 | reputation:36,75 | Определение и включение схемы сверены. |
| TypeDataModel; super.migrateData | Foundry 14.367.0: /opt/foundryvtt/common/abstract/type-data.mjs, data.mjs:908–910 | Наследование / вызов | Класс:17; миграция:114 | Родительский migrateData возвращает source. |
| SchemaField, BooleanField, NumberField, EmbeddedDataField, TypedObjectField, StringField, ArrayField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | Глобальный API | defineSchema | Настоящие поля использованы в изолированной проверке. |
| Math.floor, Number; Math.clamp | ECMAScript; расширения /opt/foundryvtt/common/primitives/_module.mjs Foundry 14.367.0 | Вызов | Подготовка:77–88; масса:95–102 | Math.clamp доступен после подключения primitives. |
| ClientDocument.prepareData; Actor.prepareData/prepareEmbeddedDocuments | Foundry 14.367.0: /opt/foundryvtt/client/documents/abstract/client-document.mjs:313–319; /opt/foundryvtt/client/documents/actor.mjs:428–473 | Внешний вызов / жизненный цикл | Вызывает system.prepareBaseData | Прочитан порядок, не запуск полного Actor. |
| TypeDataField._migrate, EmbeddedDataField._migrate | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs:4318–4326,2795–2796 | Миграция при очистке данных | migrateDataSafe модели и вложений | Не равнозначно отдельной записи изменений в БД. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/characterData.js](../../../../../../../module/data/actor/characterData.js) | CommonActorData, defineSchema, подготовка/миграции/масса | extends и super.defineSchema; остальные методы наследуются | 2,9–14 |
| [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | То же | extends и super.defineSchema | 1,6–11 |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | stats, derivedStats, reputation, healthState, attackStats; calcCurrencyWeight | calculateStats/calculateStat, производные расчёты, getTotalWeight | 35–196,245–247; loot/mystery пропускаются в prepareDerivedData |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) | system, schema.fields | Передаёт живую модель и определения в контекст | 70–71 |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | deathSaves | _removeDeathSaves/_addDeathSaves делают actor.update; _onDeathSaveRoll вычитает счётчик | 5–24; кнопки death-minus/death-plus/death-roll:48–53 |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs); [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | healthState.{woundThreshold,deathState}.ignored | Флаги формы; applied рассчитывает Actor.calculateStat | character:111–125; monster:134–148 |
| [module/actor/mixins/modifierMixin.js](../../../../../../../module/actor/mixins/modifierMixin.js) | skillGroupModifiers | addActiveEffects добавляет value к формуле при allSkills или попадании навыка в CONFIG.WITCHER[group] | 24–35; группу определяет потребитель, схема не содержит choices |
| [module/setup/config.js](../../../../../../../module/setup/config.js) | skillGroupModifiers.disease | Статус disease задаёт name, allSkills и -2 | 2135–2146; это источник данных эффекта, не импорт CommonActorData |

Для остальных вложенных полей подробные потребители перечислены в 13 связанных карточках, включая их транзитивные схемы. Поиск выполнен в module/, templates/, packsJson/; ядро прочитано отдельно. Наличие строковых ссылок не подтверждает достижимость старых шаблонов или применение всех эффектов.

## Данные и изменения состояния

В ядре сначала вызывается system.prepareBaseData(), затем базовая подготовка Actor, вложенные документы и начальная фаза эффектов, system.prepareDerivedData() и WitcherActor.prepareDerivedData(); после super.prepareData() ядро применяет финальную фазу эффектов. Четыре модели этой порции не переопределяют prepareDerivedData. Вложенные Stats/Reputation — DataModel, а не отдельные документы: их одноимённые prepareBaseData не вызываются здесь рекурсивно, нужное копирование выполнено явно.

Собственный prepareBaseData меняет подготовленную модель; в проверке model.toObject() после вызова совпадает с исходным снимком, а toObject(false) содержит вычисления. Повторный прямой вызов при тех же входах дал те же значения. Это не доказательство идемпотентности всего Actor или сохранения в мире.

Миграции меняют полученный объект: vigor без unmodifiedMax не переносится этим условием; explicit 0 переносится из value. migrateCalculatedStats обнуляет int/ref/dex/body/spd/emp/cra/will/luck.totalModifiers и attackStats.meleeBonus при truthy; toxicity.totalModifiers, reputation.totalModifiers и остальные поля этим методом не обнуляются. Такое различие зафиксировано, но само по себе не объявлено ошибкой. Adrenaline {current:3}→value3; {value:0,current:3}→3; {value:2,current:3}→2; {value:0}→свойство value=undefined до последующей очистки полей. Наличие таких старых данных в мире не проверялось.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полная сборка | 134 строки; 13 прямых импортов; настоящая CommonActorData.schema | 19 полей; одинаковый общий набор у Character/Monster | Не реальный Actor. |
| Подготовка и округление | BODY base7/value2, WILL5/3, INT9/4, SPD6/1 | stun6, run18, leap3, enc70, rec6, woundTreshold6, resolve70, focus21; vigor.max4; reputation.max3 | Проверен исходный prepareBaseData, следующие этапы не запускались. |
| Границы и память | base BODY/WILL0 и20; два повторных вызова модели | stun.base1/10; исходный снимок неизменен; повторный результат совпал | Не общий потолок характеристик. |
| Миграции | Три формы vigor, четыре adrenaline, заполненные totalModifiers | Условия и пропуски соответствуют описанию | Прямые исходные методы; без миграции мира. |
| Масса | По одной монете каждого из семи видов | 0.007 для Common/Character/Monster/Loot | Масса предметов и округление Actor проверены по коду. |

## Непроверенные участки и открытые вопросы

Схема и все шесть собственных методов прочитаны полностью. Полный Actor, эффекты, работа листов и серверное сохранение остаются последующим порциям. Не сделан вывод о правилах ограничения характеристик. Порядок ядра установлен по локальной версии 14.367.0, его расширения внешними модулями не проверялись.

## Связанные проблемы

- [issue-00011](../../../../../../issues/potential/issue-00011.md) — условия переноса отсутствующей базовой величины, включая vigor; повторно сверено без дублирования.
- [issue-00012](../../../../../../issues/potential/issue-00012.md) — два прохода calculateStats в потребителе повторно прибавляют luck/toxicity.
- [issue-00030](../../../../../../issues/potential/issue-00030.md) — общая модель не даёт монстру поля опыта/обучения CharacterData.
- [issue-00031](../../../../../../issues/potential/issue-00031.md) — потребитель statusEffectImmunities монстра ошибается при непустом списке; поле добавляет MonsterData, не CommonActorData.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.006 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. Полностью разобран потребитель WitcherActor: модель задаёт исходные максимумы, затем initial эффекты, два прохода основных характеристик и производные расчёты, затем final эффекты ядра. Восемь stats.value рассчитываются из unmodifiedMax, не max. Числовой initial-эффект по max может не достигнуть value либо быть перезаписан (issue-00036); это дополнительный результат интеграции.

Карточки: [WitcherActor](../../actor/witcherActor.js.md), [modifierMixin](../../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../../review-log.md#task-0003007).

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. calcCurrencyWeight прослежен до индикатора инвентаря через Actor.getTotalWeight. Семь валют вводятся через name=system.currency.*; 1001 монета дала 1.001 до общего округления вверх. HBS не выполняет этот расчёт; английские Carry/Max Carry отражены в issue-00179.

Связанные шаблоны: [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs). [Проверки и ограничения](../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. system.skills содержит семь групп встроенных моделей, а Item-навыки готовятся отдельно по девяти originstat. Это различие приводит к пропуску spd/luck в общем HBS. Наследование общих skills не добавляет монстру Character IP/logs/magic, необходимых levelUpSkill.

Сверенные связи: [templates/partials/character/tab-skills.hbs](../../../../../../../templates/partials/character/tab-skills.hbs); [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js); [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js). Полные карточки новых файлов — в [указателе порции](../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.

## Уточнение TASK-0003.030

2026-09-11, `aa6af106e86a9c75fe050d599f961c8fadb74f1b`. deathSaves — числовой счётчик без min/integer; текущий death-minus сбрасывает его 0. Спасбросок выбирает STUN.value либо BODY/WILL.max, clamp10 до счётчика. prepareBaseData перезаписывает часть редактируемых derived.unmodifiedMax: форма не учитывает вычисляемость полей.

Сверенные источники: [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js); [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs). [Итоговая сверка третьей серии, сценарии и ограничения](../../../../review-log.md#task-0003030). Код и статусы проблем не менялись.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Подтверждено чтение stats, skills, derivedStats и general из настоящих вложенных моделей в полном контексте Character. Fresh Skill.label и повторная модель из toObject различаются из-за миграции; это учтено отдельно от штатных ремесленных проверок.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../actor/sheets/WitcherCharacterSheet.js.md); [templates/sheets/actor/partials/character/sidebar.hbs](../../../templates/sheets/actor/partials/character/sidebar.hbs.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Сверены notes, healthState, skills и ресурсы в полном MonsterSheet. healthState объявлен прямо в CommonActorData, отдельного healthStateData файла нет. Старые Item notes и массивные notes обслуживают разные handlers. Иммунитеты к статусам принадлежат MonsterData, а общая подготовка не добавляет IP/logs/training.

Связи: [module/actor/sheets/WitcherMonsterSheet.js](../../actor/sheets/WitcherMonsterSheet.js.md); [templates/sheets/actor/partials/monster/sidebar.hbs](../../../templates/sheets/actor/partials/monster/sidebar.hbs.md); [templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-notes.hbs.md); [templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs](../../../templates/sheets/actor/partials/monster/tabs/partials/monster-status.hbs.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003032).
