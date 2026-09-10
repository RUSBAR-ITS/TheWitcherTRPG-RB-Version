# module/data/actor/templates/common/combatEffectsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../../../module/data/actor/templates/common/combatEffectsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c34b790379fd98cd7e33ccbeeca085e49297a40f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.003](../../../../../../../../tasks/task-0003.003.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.003](../../../../../../review-log.md#task-0003003) |

## Назначение файла

Фабрика трёх словарей боевых воздействий и вложенной модели временных HP: модификаторы атаки/защиты, воздействия начала хода, temporaryEffects.

## Условия использования

Файл импортирует TemporaryEffects:1 и читает fields:3. Default export combatEffects() вызывается [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js):48 внутри SchemaField combatEffects. Фабрика не регистрирует Hooks и не выполняет боевых действий.

## Введённые сущности и действия с ними

| Поле | Тип / начало | Состав и назначение |
| --- | --- | --- |
| combatEffects() | Функция :5–41 | Возвращает четыре поля. |
| attackModifier | TypedObjectField(SchemaField), {} | Запись <ключ>: name StringField без initial, value NumberField initial=0. |
| defenseModifier | TypedObjectField(SchemaField), {} | Такая же запись name/value. |
| turnStartEffects | TypedObjectField(SchemaField), {} | Запись <ключ>: name, img, damage, heal. |
| turnStartEffects.<ключ>.name / img | StringField без initial | Метка и изображение сообщения; при отсутствии undefined. |
| damage.amount / modifier / spDamage | NumberField, initial=0 | Базовое количество урона, его добавка, повреждение брони. |
| damage.allLocations / ignoreArmor / bypassesShield / nonLethal | BooleanField, initial=false | Урон по всем зонам, обход брони, обход щита, выбор STA вместо HP. |
| damage.type | StringField без initial | Тип урона, например fire/acid; в схеме нет choices. |
| heal.amount / modifier | NumberField, initial=0 | Количество лечения и отдельная добавка. |
| temporaryEffects | EmbeddedDataField(TemporaryEffects) | temporaryHp; [отдельная карточка](temporaryEffectsData.js.md). |

У NumberField этой фабрики не заданы min/max/integer. У словарей нет ограничения ключей; damage/heal — схемные объекты, не массивы. Отсутствующие записи не создаются заранее под каждым статусом. При создании пустой записи turnStartEffects.<ключ> damage/heal получают числовые/булевы defaults, name/img/type остаются undefined.

## Основные функции и методы

combatEffects():5–41 создаёт описания полей без аргументов. Вложенные SchemaField описывают записи; собственных методов расчёта, добавления/удаления записей и исполнения начала хода нет. TemporaryEffects.defineSchema задаёт отдельный словарь временных HP.

## Используемые сущности и зависимости

| Сущность | Определение / API | Связь и доказательство |
| --- | --- | --- |
| TemporaryEffects | [module/data/actor/templates/common/temporaryEffectsData.js](../../../../../../../../../module/data/actor/templates/common/temporaryEffectsData.js) | Импорт :1, EmbeddedDataField :39. |
| TypedObjectField, SchemaField, StringField, NumberField, BooleanField, EmbeddedDataField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | fields:3; создаются :7–39. |
| Справочник statusEffects | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Внешний источник строковых путей и JSON значений; не импортируется фабрикой. |

## Известные потребители

| Файл | Место / операция |
| --- | --- |
| [module/setup/config.js](../../../../../../../../../module/setup/config.js) | statusEffects:2064–2340 содержит 11 изменений под combatEffects: 5 turnStartEffects и 6 attack/defenseModifier. Healing/fire/poison/bleed/suffocation; prone/staggered/blinded — по два модификатора. |
| [module/actor/mixins/modifierMixin.js](../../../../../../../../../module/actor/mixins/modifierMixin.js) | addAttackModifiers:38–43 и addDefenseModifiers:46–51 перебирают записи, пропускают value===0, добавляют value[localize(name)] в формулу. |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../module/actor/mixins/defenseMixin.js) | Содержит собственный addDefenseModifiers:249–255 с тем же чтением. WitcherActor назначает этот mixin после modifierMixin, поэтому метод переопределяется. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../module/actor/mixins/weaponAttackMixin.js); [module/actor/mixins/castSpellMixin.js](../../../../../../../../../module/actor/mixins/castSpellMixin.js) | Атаки оружием и магией вызывают addAttackModifiers; эти файлы не создают схему словаря. |
| [module/setup/hooks.js](../../../../../../../../../module/setup/hooks.js) | registerHooks:4–8 регистрирует updateCombat, combatHooks:10–13 вызывает applyGeneralCombatHooks без проверки changed-полей. |
| [module/scripts/combat/generalCombatHook.js](../../../../../../../../../module/scripts/combat/generalCombatHook.js) | applyGeneralCombatHooks:3–9 проверяет isActiveGM, получает текущего Actor; applyCombatEffects:40–44 перебирает turnStartEffects; applyCombatEffect:46–87 исполняет damage/heal. |
| [module/scripts/combat/applyDamage.js](../../../../../../../../../module/scripts/combat/applyDamage.js); [module/scripts/damageInstance.js](../../../../../../../../../module/scripts/damageInstance.js) | applyDamageFromStatus:99–101 создаёт DamageInstance(totalDamage).setType(damageObject.type), затем вызывает actor.applyDamage. |
| [module/actor/mixins/healMixin.js](../../../../../../../../../module/actor/mixins/healMixin.js) | calculateHealValue:2–10 ограничивает лечение максимумом HP; createHealMessage выводит сообщение. generalCombatHook передаёт только heal.amount. |
| [templates/chat/combat/statusEffect.hbs](../../../../../../../../../templates/chat/combat/statusEffect.hbs) | Читает name/img записи для сообщения начала хода. |
| [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../../../../../module/actor/sheets/mixins/activeEffectMixin.js); [module/activeEffect/witcherActiveEffect.js](../../../../../../../../../module/activeEffect/witcherActiveEffect.js) | Управление документами-источниками: delete/toggle; isSuppressed учитывает свойства родительского предмета и apply*-флаги. |
| [TemporaryEffects и потребители временных HP](temporaryEffectsData.js.md) | Создание через профессию, суммирование листом, расход урона и документный жизненный цикл описаны отдельно. |

### Строковые ссылки компедиумов

В 226 JSON найдено 17 ссылок этой порции, все под turnStartEffects. Каждая проверена по настоящей схеме с source для динамического ключа. Значения 16 целых записей разобраны как JSON и прошли создание CommonActorData; одна ссылка ведёт к damage.modifier.

| Файл-источник | Путь внутри combatEffects |
| --- | --- |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json](../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left__KQZRzczsSx1XY63m.json](../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Left__KQZRzczsSx1XY63m.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right__ZxvWPJPDD9fm34Pc.json](../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Arm__Right__ZxvWPJPDD9fm34Pc.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json](../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json](../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json](../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json](../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json) | `turnStartEffects.bleed.damage.modifier` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json](../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json) | `turnStartEffects.poison` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json](../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left__saPd4IMUCv5qZE60.json](../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left__saPd4IMUCv5qZE60.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Treated__ujz1IMKCXoJF9w91.json](../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right___Treated__ujz1IMKCXoJF9w91.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right__c3H8Xx7WYCcM37k6.json](../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Right__c3H8Xx7WYCcM37k6.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json](../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json](../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture_UImIh794nOy21jg2.json](../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture_UImIh794nOy21jg2.json) | `turnStartEffects.bleed` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound_tiVrEesPSzZ64HpZ.json](../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound_tiVrEesPSzZ64HpZ.json) | `turnStartEffects.suffocation` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json](../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json) | `turnStartEffects.acid` |

Ссылки к остальным семи структурам порции в этом поиске строковых значений не найдены. Это не полный разбор JSON-файлов и не проверка их импорта.

## Данные и изменения состояния

1. Схема задаёт контейнеры и типы. Значения могут быть сохранены в Actor.system либо внесены при подготовке изменениями ActiveEffect.
2. В Foundry 14.367.0 Actor.applyActiveEffects перебирает allApplicableEffects, пропускает !effect.active и применяет system.changes. Порядок фаз относится к ядру: initial при подготовке embedded-документов, final после super.prepareData. Прочитан /opt/foundryvtt/client/documents/actor.mjs:238–274,428–473.
3. Удаление/выключение источника выполняет интерфейс документов ActiveEffect; фабрика не удаляет ни источник, ни сохранённые ключи. Проверка истечения длительности находится вне этой порции.
4. При начале хода обработчик пропускает запись, если обе amount ложны. Урон выполняется только при damage.amount>0: к нему прибавляется damage.modifier, флаги переводятся в свойства повреждения, nonLethal выбирает sta/hp.
5. Лечение выполняется при heal.amount>0, проходит calculateHealValue и update HP. heal.modifier не читается; damage.type не переносится в объект повреждения. Это зарегистрированные наблюдения, не реализованные исправления.

applyGeneralCombatHooks вызывает асинхронные регенерацию и applyCombatEffects без await. Внутри applyCombatEffects записи обходятся с await, однако applyDamageFromStatus также не ожидает actor.applyDamage; полный порядок завершения записей этим не гарантируется. Источник момента запуска — существующая issue-00006.

## Проверки и доказательства

Прочитаны 41 строка и места применения/добавления/управления источниками. Реальная CommonActorData дала пустые словари; записи name/value со значениями -2/-3 сформировали строки ` -2[a]` и ` -3[d]`.

Изолированно выполнена цепочка applyCombatEffect → applyDamageFromStatus → настоящий DamageInstance; перехвачен Actor.applyDamage. У fire amount=5/modifier=2 получен урон 7, но type=undefined; флаги обхода/зон и spDamage перенесены. nonLethal выбрал sta. Для лечения 3+modifier2 при HP5/20 аргумент update равен 8. Это проверка переданных данных, не всего расчёта сопротивлений.

Сверены 11 changes config.js и 17 путей JSON со схемой; строковые true/числа преобразуются полями при создании проверенных записей. Журнал содержит сценарий и ограничения.

## Непроверенные участки и открытые вопросы

Не проверены реальная передача изменений от эффекта в Actor, обработка нескольких клиентов, длительности, сопротивления/броня и итоговый боевой цикл. Возможные гонки асинхронных записей требуют отдельного воспроизведения; здесь они не объявляются доказанным результатом. Прочтение методов вне фабрики не меняет статус их файлов.

## Связанные проблемы

[issue-00006](../../../../../../../../issues/potential/issue-00006.md) — момент запуска; [issue-00021](../../../../../../../../issues/potential/issue-00021.md) — потеря damage.type; [issue-00022](../../../../../../../../issues/potential/issue-00022.md) — heal.modifier не учитывается; [issue-00023](../../../../../../../../issues/potential/issue-00023.md) — расход смешанного эффекта временных HP.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.003 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Общая модель включает combatEffects:48; транзитивное включение TemporaryEffects через EmbeddedDataField сверено. Собственный CommonActorData.prepareBaseData не запускает эффекты начала хода и не изменяет запас временных HP.

Карточки сборки: [commonActorData](../../commonActorData.js.md). [Сверка TASK-0003.006](../../../../../../review-log.md#task-0003006).
