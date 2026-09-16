# TASK-0006.028 — Профессии: модели, пути навыков и редактор

2026-09-16; rusbar-main, исходный HEAD `17a731d5eaca5827bbcb1375a68a21934d05b760`; дерево в начале чистое. [Задача](../../tasks/task-0006.028.md), [запросы](examples/expansion-028-queries.json), [тесты](tests/test_expansion_028.py).

## Результат и пределы

Добавлены 90 сущностей, 642 отношений и 15 процессов. Всего 4885 сущностей, 13350 отношений и 408 процессов (1314 шагов, 2426 переходов); 367 границ. Основных источников 195, смежных 88, без определений 332; определения в 283/615 файлах: 2 complete (en/ru), 281 partial. Отношения в 287 файлах, локальные шаги процессов в 139.

Все прежние 12708 отношений, 393 процесса и ID/владельцы сущностей сохранены. Уточнены две прежние записи: professionSkill() — описание/refs; tab-profession Character — добавлен профессиональный диапазон 1–261 перед прежней расой 263–337. Включены 14 основных исходников задачи и нужные смежные участки. Покрытие остаётся partial; полное исполнение способностей относится к .029.

| Файл | Включённая область и остаток |
| --- | --- |
| [module/data/item/professionData.js](../../../module/data/item/professionData.js) (src-000121) | Схема, Set базовых навыков, 11 enriched; прежние пять defense методов .016 переиспользованы. Внешние callbacks/readers не исчерпаны. |
| [module/data/item/templates/professionPathData.js](../../../module/data/item/templates/professionPathData.js) (src-000147) | pathName и три skill SchemaField, связи основной/конфигурационной формы; внешние consumers partial. |
| [module/data/item/templates/professionSkillData.js](../../../module/data/item/templates/professionSkillData.js) (src-000148) | Восемь полей и вложенные schema/EmbeddedDataField; конкретные экземпляры десяти слотов, полный runtime .029. |
| [module/data/item/templates/profession/skillUsageData.js](../../../module/data/item/templates/profession/skillUsageData.js) (src-000144) | Все schema поля и конфигурационный UI; полный skillUsage исполнитель .029. |
| [module/data/item/templates/profession/temporaryHealthData.js](../../../module/data/item/templates/profession/temporaryHealthData.js) (src-000145) | Схема чисел/строк формул, formGroup fields; вычисление temporaryHP/duration .029. |
| [module/data/item/templates/profession/thresholdData.js](../../../module/data/item/templates/profession/thresholdData.js) (src-000146) | Schema hasThresholds/TypedObject name/value, CRUD; выбор порога .029. |
| [module/item/sheets/WitcherProfessionSheet.js](../../../module/item/sheets/WitcherProfessionSheet.js) (src-000175) | Фактический класс WitcheProfessionSheet, PARTS/configuration/_prepareContext; полный inherited UI lifecycle за границей. |
| [module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js](../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) (src-000185) | Все собственные методы/PARTS/TABS и шесть CRUD, name lookup; внешний submit/DOM/commit не исполнен. |
| [templates/sheets/item/profession-sheet.hbs](../../../templates/sheets/item/profession-sheet.hbs) (src-000607) | Десять основных skill rows, notes, pathName, professionSkills; общие header поля/стили/все locale calls не исчерпаны. |
| [templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs](../../../templates/sheets/item/configuration/partials/profession/profAttackOptionsPart.hbs) (src-000586) | Set attackOptions и условные melee/ranged flags; runtime guard не отождествлён с формой. |
| [templates/sheets/item/configuration/partials/profession/skillPathPart.hbs](../../../templates/sheets/item/configuration/partials/profession/skillPathPart.hbs) (src-000587) | Три include с конкретными skillFields/skill, PART prefix; внешний rendering partial. |
| [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) (src-000588) | Условные mechanics formGroup, keyed CRUD controls и известные broken action/lookup; полный browser lifecycle не доказан. |
| [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs) (src-000526) | Профессия 1–261 и прежняя раса 263–337; inline/roll/raw editors, прочие UI зависимости не исчерпаны. |
| [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) (src-000572) | Только definingSkill/notes, inline/roll и общие Item действия; девять paths в этой форме отсутствуют. |
| [module/actor/mixins/professionMixin.js](../../../module/actor/mixins/professionMixin.js) (src-000020) | Сумма и lookup fully read, roll entry→граница .029; полные атаки/usage/пороги/броски ещё не раскрыты этой порцией. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) (src-000029) | Выбор/enriched профессии и totalProfSkills поверх .027; прочие подготовки partial. |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js) (src-000031) | Выбор первого profession, отсутствие Item enrichment, PART template; прочие методы partial. |
| [module/actor/sheets/mixins/itemMixin.js](../../../module/actor/sheets/mixins/itemMixin.js) (src-000043) | Конкретные inline skill fields и professionSkills Drop, прежние общие процессы .013; полный source/server outcome за границей. |
| [module/actor/sheets/mixins/skillMixin.js](../../../module/actor/sheets/mixins/skillMixin.js) (src-000045) | Только profession-roll listener и связь с Actor входом; другие actions покрыты прежними порциями частично. |

## Владельцы, слоты и значения

| Данные | Определение и роль |
| --- | --- |
| ProfessionData.definingSkill | Один SchemaField(professionSkill()), полный набор механических полей модели |
| ProfessionData.skillPath1/2/3 | Каждый professionPath() содержит pathName и skill1/2/3; всего девять навыков путей |
| professionSkill() | skillName/stat строки без choices, HTML definition, Number level(initial0) без min/max, skillAttack/skillDefense, embedded SkillUsage/Threshold |
| ProfessionData.professionSkills | Set строк базовых навыков; 52 варианта из skillMap в форме. Не набор десяти профессиональных слотов |
| SkillUsage | hasCustomEffect, applySelf, applyOnTarget (false), embedded TemporaryHealth |
| TemporaryHealth | addTemporaryHealth=false; difficultyCheck multiplier=3/stat=int/maxRollOver=5; temporaryHp value=d6/duration=2*@level — строки формул |
| Threshold | hasThresholds=false и словарь thresholds: случайный ключ строки → name/StringField, value/NumberField(initial0) |
| DamageProperties.effects | Прежний словарь itemEffect: name/statusEffect/percentage и прочие schema поля. Строка воздействия не документ ActiveEffect |

Drop профессии использует прежний proc-000140: назначает isProfession по professionSkills, а не по профессиональным уровням. Reset ожидается, update внутри forEach и actor.addItem — нет. Неизвестный ключ не проверяется, получается путь с undefined (issue116). Общий выбор getList('profession')[0] учитывает !isStored и sort. Основная форма и Actor inline правят вложенный Item, не копируют навыки в поля Actor.

<a id="forms"></a>
## Основная форма, конфигуратор и листы Actor

Класс листа в исходнике называется **WitcheProfessionSheet**. Его PARTS подключает profession-sheet.hbs; getter configuration создаёт WitcherProfessionConfigurationSheet для того же Item. После await базового _prepareContext он строит options базовых навыков и присваивает config.statOptions без none. Базовый config — ссылка на CONFIG.WITCHER; отдельного producer statOptions в конфигураторе нет. Основные stat select используют statTypes с none; temporaryHealth.stat — statOptions без none. Эти UI options не являются schema choices.

ProfessionData.enrichedText последовательно ожидает 11 createEnrichedText: definingSkill.definition, notes и девять описаний. Общий helper даёт value/enriched/systemField (прежний proc-000111). Основная Item форма правильно передаёт их formInput; имя input выводится из fieldPath. Именованные поля десяти слотов, трёх pathName, notes и Set professionSkills сохраняет общий DocumentSheetV2 handler: expand/validate/clean, затем await Item.update внутри handler. Это граница внешнего submit, а не доказательство завершения записи при DOM change.

Конфигуратор наследует general/activeEffects, добавляет только PARTS skillPath1/2/3. _prepareTabs подписывает их pathName. _preparePartContext без super возвращает для каждой части свой узкий context: config/tab/partId/skillPathFields/skillPath; прочие части получают исходный context. skillPathPart трижды передаёт конкретные skillFields/skill в skillPathSkillPart. Attack partial получает schema/value того же skillAttack. FormGroup выбирает полный fieldPath нужного слота.

Условные isAttack/isDefense/hasCustomEffect/addTemporaryHealth/hasThresholds управляют видимостью полей; скрытие не очищает source и не доказывает runtime guard. Конфигурация definingSkill отсутствует, хотя модель имеет те же поля (issue112); это отдельно от ограничения профессиональной защиты (issue72). Общие ActiveEffect callbacks переиспользованы, а не смешаны с keyed effects.

Character выбирает Item и готовит enrichedText.profession, затем totalProfSkills суммирует Number(level) десяти слотов (без профессии 0). HBS всё равно передаёт editor raw profession.system.<slot>.definition/notes с editable=false. Monster выбирает Item без вызова его enrichedText и показывает только definingSkill/notes; девять путей в этом HBS отсутствуют. Сохранена ссылка на issue109; нового browser опыта нет. Inline name/stat/level адресуются через data-field и ближайший .item data-item-id; общий itemListener → _onItemInlineEdit возвращает Item.update. Editor target с префиксом profession.system не объявлен таким же writer.

<a id="crud"></a>
## CRUD: имя навыка, путь и ID строки

Конфигуратор findSkillWithName перебирает path1/2/3, внутри skill1/2/3. Берётся первое точное совпадение; helper при совпадении вызывается повторно. definingSkill не рассматривается; незнакомое имя возвращает undefined. Пустые/одинаковые имена допускаются схемой. Actor.findSkillWithName имеет другого владельца: сначала definingSkill, потом те же девять слотов; guard отсутствия профессии нет. Модельный findDefenseSkillData — отдельный прежний метод, не поиск имени.

| Действие | Вход и путь source Item |
| --- | --- |
| add effect | actions.addEffectDamageProperties → _onAddEffectDamageProperties; data-target=skillName → lookup; randomID → system.<path>.skillAttack.damageProperties.effects.<id>={percentage:0} |
| edit effect | change data-action=editEffectDamageProperties → _onChangeForm → _onEditEffectDamageProperties; ближайший .list-item даёт row id/skillName, data-field даёт name/statusEffect/percentage; value=='on' заменяется checked |
| remove effect | HBS вызывает removeEffectDamageProperties, registry содержит removeEffect: штатная кнопка не достигает handler. Прямой _oRemoveEffectDamageProperties берёт event.currentTarget вместо переданного target; предполагаемый payload effects.-=<id>=null (issue111) |
| add threshold | actions.addThreshold → _onAddThreshold; lookup по имени и randomID; system.<path>.thresholds.thresholds.<id>={value:0} |
| edit threshold | change editThreshold → _onEditThreshold; keyed name/value, значение element.value, без преобразования on→checked |
| remove threshold | actions.removeThreshold → _oRemoveThreshold; второй аргумент element, lookup по имени; thresholds.thresholds.-=<id>=null |

Все шесть async методов запускают this.item.update без await/return. _onChangeForm также не ждёт super или edit handlers. Action dispatcher установленного ядра вызывает handler.call(this,event,target) без await. Локальное завершение не означает commit; pending/rejection записи не превращены в синхронный результат (issue120). Отсутствие совпадения даёт ошибку при обращении к skillObject.path до update. ID строки не устраняет неоднозначность имени навыка (issue110); generic edit не вводит whitelist допустимых data-field.

<a id="execution"></a>
## Стыки с прежними процессами и .029

Click .profession-roll читает имя ближайшего .profession-display, а не data-field/ID строки. Actor._onProfessionRoll после lookup выбирает isAttack → hasCustomEffect → hasThresholds → обычный roll. Здесь это адресная граница .029; существующий doProfessionSkillUsage сохраняет ID/владельца. Новых алгоритмов исполнения атаки/способности/порогового броска эта порция не объявляет.

Прежние пять defense методов ProfessionData (.016) переиспользованы. findDefenseSkillData читает имя/stat/level найденного path skill; definingSkill не перебирается. isApplicableDefenseInPath вызывает defenseProperties.isApplicable, без проверки isDefense в этом теле. UI flag не подменяет это поведение. Поля и связи общих skillAttack/skillDefense/DamageProperties/DefenseProperties остаются каноническими.

## Внешние контракты и доказательства

Прочитаны указанные участки установленного Foundry14.367.0; SHA256 фиксирует исходники, не запуск UI/БД.

| Файл | Строки | Контракт | SHA256 |
| --- | --- | --- | --- |
| `/opt/foundryvtt/client/applications/api/application.mjs` | 1931–1965 | Action dispatch: target.dataset.action, missing → _onClickAction; handler.call(this,event,target) без await. | `b5aef80d3e042a4a856be9dd875c72a5224988d62046ba770f25376f4291faa0` |
| `/opt/foundryvtt/client/applications/handlebars.mjs` | 509–548 | formInput→field.toInput; formGroup→field.toFormGroup. | `0c5959e0ebdf5847277fba3284d76ee535084e022d087659fd0791e5ccd3545c` |
| `/opt/foundryvtt/common/data/fields.mjs` | 179–180,632–636,664–666 | DataField.fieldPath становится name создаваемого элемента. | `efa8e3ccdf553ca826580e60bfbfc97db57bdeadaa954a50f6a55e0ab52c3e01` |
| `/opt/foundryvtt/client/applications/api/document-sheet.mjs` | 431–434,465–469,486–509,525–531 | Submit: expand, clean/validate, await update существующего документа; внешний контракт, не игровой опыт. | `7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01` |

Сверены R008-04/05/06/07/08/20 и R013-09 позднего аудита. Полные issue72/110/111/112/116/119/120 прочитаны в этой порции; полный issue109 прочитан в .027 и переиспользован при неизменном тексте/исходниках. Ссылки сохраняют прежние даты/статусы/ограничения. В частности, issue119 о ключах Threshold в ru не означает нового исполнения локализации. Мир, БД, браузер и несколько клиентов не запускались. Аудит/issues используются для чтения.

## Новые процессы

<a id="proc-000394"></a>
### proc-000394 — Профессия Item: варианты базовых навыков и характеристик

Подготовка основной формы; this.item сохраняет исходный документ.

Шаги: base → skills → stats. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000395"></a>
### proc-000395 — Профессия: 11 обогащённых описаний

Отдельный результат с value/enriched/systemField; последовательно awaits.

Шаги: defining → notes → path1 → path2 → path3. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000396"></a>
### proc-000396 — Профессия: основная именованная форма

Десять основных слотов, notes, pathName и Set базовых навыков.

Шаги: fields → submit. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000397"></a>
### proc-000397 — Профессия: контекст вкладки пути

PartId из трёх PARTS; definingSkill отсутствует.

Шаги: part → path → skill. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000398"></a>
### proc-000398 — Профессиональный навык: schema поля конфигурации

Обычный formGroup, отдельно от keyed effects/thresholds CRUD.

Шаги: fields → submit. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000399"></a>
### proc-000399 — Конфигурация профессии: маршрутизация change

Унаследованная форма и отдельный data-action обработчик.

Шаги: super → route → effect → threshold. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000400"></a>
### proc-000400 — Профессия: effect add

Прямой обработчик _onAddEffectDamageProperties; вход из action registry/change.

Шаги: target → lookup → write. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000401"></a>
### proc-000401 — Профессия: effect edit

Прямой обработчик _onEditEffectDamageProperties; вход из action registry/change.

Шаги: target → lookup → write. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000402"></a>
### proc-000402 — Профессия: effect remove

Прямой обработчик _oRemoveEffectDamageProperties; штатная кнопка не достигает его по issue111.

Шаги: target → lookup → write. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000403"></a>
### proc-000403 — Профессия: threshold add

Прямой обработчик _onAddThreshold; вход из action registry/change.

Шаги: target → lookup → write. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000404"></a>
### proc-000404 — Профессия: threshold edit

Прямой обработчик _onEditThreshold; вход из action registry/change.

Шаги: target → lookup → write. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000405"></a>
### proc-000405 — Профессия: threshold remove

Прямой обработчик _oRemoveThreshold; вход из action registry/change.

Шаги: target → lookup → write. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000406"></a>
### proc-000406 — Конфигурация: поиск навыка среди девяти слотов

Точное имя, порядок path1/2/3 и skill1/2/3; definingSkill не входит.

Шаги: paths → slots. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000407"></a>
### proc-000407 — Actor: поиск профессионального навыка с definingSkill

Исполнитель .029 использует этот же адрес; здесь только lookup.

Шаги: profession → defining → paths. Ветви, циклы, await/scheduled и выходы — в JSONL.

<a id="proc-000408"></a>
### proc-000408 — Персонаж: сумма уровней профессиональных навыков

calc_total_skills_profession вызывается Character preparation, не уровень/награда .030.

Шаги: select → sum. Ветви, циклы, await/scheduled и выходы — в JSONL.

## Проверки

Проверены все 236 тестовых методов в 27 модулях и 698 CLI-примеров, включая 33 новых по IQ-01–IQ-08; ошибок в итоговых результатах нет. Исторические проверки выполняются на предусмотренных прежними тестами срезах. Это проверки справочника по исходникам, без запуска игрового сценария. Перекрёстно сверены source/owner, оба конца отношений, readers/writers, lookup/CRUD, ветви/выходы, refs и facets/роли. [Протокол](review-log.md#task-0006028). Следующая — [TASK-0006.029](../../tasks/task-0006.029.md); родитель in-progress.
Уточнение адреса при TASK-0006.029: profession-roll listener находится в skillMixin.js:31 (src-000045). Исправлены источник прежнего event и трёх связей; их ID и назначение сохранены. Исторические показатели этой порции не пересчитаны.
