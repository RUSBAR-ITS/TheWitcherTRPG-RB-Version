# module/data/actor/templates/common/stats/statsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/stats/statsData.js](../../../../../../../../../../module/data/actor/templates/common/stats/statsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7b7788bc614e5b7a57f8c596fb64ca75ecabd8b7` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.001](../../../../../../../../../tasks/task-0003.001.md), одна порция из пяти файлов |
| Запись перекрёстной сверки | [TASK-0003.001](../../../../../../../review-log.md#task-0003001) |

## Назначение файла

Вложенная модель десяти основных показателей Actor: восьми характеристик, удачи и токсичности. Объявляет схему, метод копирования исходных значений в max и миграцию полей. Расчёт итоговых value выполняет WitcherActor.

## Условия использования

Импортирует фабрику `stat`, сохраняет ссылку `fields`, экспортирует класс `Stats extends foundry.abstract.DataModel` по умолчанию. [module/data/actor/commonActorData.js](../../../../../../../../../../module/data/actor/commonActorData.js) включает его через `EmbeddedDataField(Stats)` в `system.stats` (строки 12, 33). Через CommonActorData данные получают модели персонажа и монстра; Stats не зарегистрирован отдельным типом Actor.

`prepareBaseData` определён, но прямого вызова `stats.prepareBaseData()` в `module/` не найдено. В проверенном коде ядра 14.367 `ClientDocument.prepareData` вызывает `system.prepareBaseData()` для TypeDataModel, без рекурсивного вызова одноимённых методов вложенных DataModel. Копирование полей Stats в реальном пути подготовки выполняет `CommonActorData.prepareBaseData` (64–74). Изолированный вызов метода Stats в проверке не выдаётся за доказательство его автоматического вызова Foundry.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 3 | Классы полей Foundry | Локальная ссылка | Создание схемы. |
| Stats | class, 5–70 | Вложенная модель характеристик | Default export | defineSchema; подготовка; миграция. |
| int, ref, dex, body, spd, emp, cra, will, luck, toxicity | SchemaField, 8–17 | Десять показателей | system.stats через CommonActorData | Каждый содержит пять полей фабрики stat. |

| Ключ | Ключ подписи | Начальное unmodifiedMax | Сопоставление со statMap |
| --- | --- | --- | --- |
| int | WITCHER.Actor.Stat.Int | 0 | stats / int |
| ref | WITCHER.Actor.Stat.Ref | 0 | stats / ref |
| dex | WITCHER.Actor.Stat.Dex | 0 | stats / dex |
| body | WITCHER.Actor.Stat.Body | 0 | stats / body |
| spd | WITCHER.Actor.Stat.Spd | 0 | stats / spd |
| emp | WITCHER.Actor.Stat.Emp | 0 | stats / emp |
| cra | WITCHER.Actor.Stat.Cra | 0 | stats / cra |
| will | WITCHER.Actor.Stat.Will | 0 | stats / will |
| luck | WITCHER.Actor.Stat.Luck | 0 | stats / luck |
| toxicity | WITCHER.Actor.Stat.Toxicity | 100 | В statMap нет; отдельный getToxSuggestions. |

Остальные начальные значения и ограничения описаны в [карточке statData.js](statData.js.md). Начальная токсичность 100 относится к `unmodifiedMax`, а `max` в схеме всё ещё начинается с 0.

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| Stats.defineSchema() | Доступная фабрика stat и SchemaField | Объект десяти полей | Создаёт 10 вложенных наборов; toxicity получает 100 | Синхронно; определение структуры. |
| Stats#prepareBaseData() | Инициализированные десять записей this | undefined | Копирует unmodifiedMax → max для всех десяти | Меняет подготовленные поля экземпляра; не меняет value/totalModifiers и не сохраняет документ. |
| Stats.migrateData(source) | Объект входных данных; отдельные записи могут отсутствовать | Результат super.migrateData(source) | Для каждой из 10 записей: если unmodifiedMax == 0, скопировать max в unmodifiedMax | Изменяет переданный source на месте; синхронно; catch отсутствует. |

Миграция использует нестрогое сравнение `== 0`. Отсутствующая запись пропускается благодаря `?.`; отсутствующее поле `unmodifiedMax` также не проходит условие, потому что `undefined == 0` ложно. `0` и строка `'0'` проходят. Существующее ненулевое исходное значение сохраняется. Если max отсутствует при нулевой базе, будет присвоен undefined; дальнейшую очистку выполняет Foundry. Здесь нет проверки формата старой версии и нет собственного вызова записи в БД.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| stat | [module/data/actor/templates/common/stats/statData.js](../../../../../../../../../../module/data/actor/templates/common/stats/statData.js) | ES import; вызов фабрики | 1, 8–17: общие поля | Определение и все десять вызовов сверены. |
| DataModel, SchemaField | Foundry 14.367.0, common/abstract/data.mjs и common/data/fields.mjs под /opt/foundryvtt | Наследование и конструктор | 5–17, 68 | Реальные классы использованы для создания Stats и миграции. |
| DataModel.migrateData | /opt/foundryvtt/common/abstract/data.mjs:908–910 | Вызов родительского метода | 68: вернуть мигрированный source | Базовая реализация возвращает source. |
| Ключи подписей | [lang/en.json](../../../../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../../../../lang/ru.json) | Данные схемы для локализации | 8–17 | Все десять ключей найдены. |
| WITCHER.statMap | [module/setup/config.js](../../../../../../../../../../module/setup/config.js) | Соответствие путей, без прямого импорта | 9 записей origin=stats сопоставлены с моделью | Реальные getField по .totalModifiers вернули поля. |
| Жизненный цикл вложения | [module/data/actor/commonActorData.js](../../../../../../../../../../module/data/actor/commonActorData.js); /opt/foundryvtt/client/documents/abstract/client-document.mjs:313–319 | Внешний владелец и вызов TypeDataModel | Инициализация и базовая подготовка | Модель Stats сама не регистрирует обработчик Foundry. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/commonActorData.js](../../../../../../../../../../module/data/actor/commonActorData.js) | Stats; system.stats.* | Включает модель; копирует базовые max; читает основы производных; сбрасывает 9 totalModifiers в migrateCalculatedStats | 12, 33, 64–88, 120–128; toxicity в этом сбросе не перечислена. |
| [module/data/actor/characterData.js](../../../../../../../../../../module/data/actor/characterData.js) | Унаследованная system.stats | Расширяет CommonActorData | 2, 9–14. |
| [module/data/actor/monsterData.js](../../../../../../../../../../module/data/actor/monsterData.js) | Унаследованная system.stats | Расширяет CommonActorData | 1, 6–11. |
| [module/actor/witcherActor.js](../../../../../../../../../../module/actor/witcherActor.js) | unmodifiedMax/max/value/totalModifiers | calculateStats/calculateStat; основы производных и атак | 55–194; два вызова calculateStats в 49, 51. |
| [module/activeEffect/mixins/baseMixin.js](../../../../../../../../../../module/activeEffect/mixins/baseMixin.js) | Пути .totalModifiers | Подсказки статов и отдельная токсичность | 14–38. |
| [module/setup/config.js](../../../../../../../../../../module/setup/config.js) | statMap и строки changes статусов | Метаданные 9 характеристик; воздействия на spd/ref/dex/int | 17–70, 2198–2242; [карточка конфигурации](../../../../../setup/config.js.md). |
| [module/actor/mixins/skillMixin.js](../../../../../../../../../../module/actor/mixins/skillMixin.js) | stats[attribute.name].value | Роли характеристики в броске навыка | 49, 139. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | stats[...].value | Атака и подмена навыка | 184–185, 319–320. |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../../module/actor/mixins/defenseMixin.js) | stats[skillMapEntry.attribute.name].value | Защита | 138. |
| [module/actor/mixins/professionMixin.js](../../../../../../../../../../module/actor/mixins/professionMixin.js) | stats[skill.stat], stats[stat], difficultyCheck.stat | Броски профессии и временного здоровья | 155–156, 276, 360. |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../../../module/actor/mixins/castSpellMixin.js) | stats.will.value | Бросок заклинания | 24–25. |
| [module/actor/mixins/verbalCombatMixin.js](../../../../../../../../../../module/actor/mixins/verbalCombatMixin.js) | stats[...].value | База вербального боя и урона | 42, 50. |
| [module/scripts/verbalCombat/verbalCombatDefense.js](../../../../../../../../../../module/scripts/verbalCombat/verbalCombatDefense.js) | actor.system.stats[...].value | Ответ в вербальном бою | 60, 68. |
| [module/actor/mixins/damageMixin.js](../../../../../../../../../../module/actor/mixins/damageMixin.js) | stats.body.max | Длительность лечения | 349–353. |
| [module/data/item/criticalWoundData.js](../../../../../../../../../../module/data/item/criticalWoundData.js) | actor.system.stats.body.max | calculateHealingTime | 50, 53, 56. |
| [module/item/systems/repair.js](../../../../../../../../../../module/item/systems/repair.js) | stats.cra.value | Характеристика исполнителя ремонта | 206. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | stats.cra.value/label | Ручной сценарий изготовления | 296–309, 389–390. |
| [module/actor/sheets/mixins/statMixin.js](../../../../../../../../../../module/actor/sheets/mixins/statMixin.js) | stats[stat].value; luck.max/value | Спасбросок, сумма статов, расход/сброс удачи | 10, 92–107; update luck.value. |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) | stats.body.value | Порог спасброска смерти | 20. |
| [module/actor/sheets/configurations/WitcherModifiersConfiguration.js](../../../../../../../../../../module/actor/sheets/configurations/WitcherModifiersConfiguration.js) | system и type | Контекст редактирования stats | 34–35, 64–66. |
| [templates/sheets/actor/configuration/app/edit-stats.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/edit-stats.hbs) | system.stats | Передаёт данные в stats-block | 2–4. |
| [templates/sheets/actor/configuration/app/partials/stats-block.hbs](../../../../../../../../../../templates/sheets/actor/configuration/app/partials/stats-block.hbs) | max/label/unmodifiedMax | Показывает max; редактируемый путь указывает unmodifiedMax | 1–8; min/max HTML не заданы. |
| [templates/partials/character/tab-stats.hbs](../../../../../../../../../../templates/partials/character/tab-stats.hbs) | system.stats.* | Вывод value/max/label и разницы; toxicity исключена | 8–34; выбран в PARTS листов персонажа и монстра. |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/sidebar.hbs) | luck, toxicity | Вывод и поля текущих значений | 43–50, 138–139. |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/sidebar.hbs) | luck | Вывод и поля текущего значения | 44–51. |

### Пути воздействий в данных компедиума

Из JSON рекурсивно извлечены поля `key` с префиксом `system.stats.`; они обозначают адрес изменения. Полные документы компедиума не разбирались. Это подтверждает ссылку на поле, но не перенос, активность или результат эффекта в мире.

| Файл данных | Пути в changes |
| --- | --- |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs_VfgJzcV75cGqsjuF.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs_VfgJzcV75cGqsjuF.json) | `system.stats.body.totalModifiers`, `system.stats.dex.totalModifiers`, `system.stats.ref.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Stabilized__4LmC6nGwRM0PpNl7.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Stabilized__4LmC6nGwRM0PpNl7.json) | `system.stats.body.totalModifiers`, `system.stats.ref.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Treated__77evBMjaJOlKTaRv.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Broken_Ribs__Treated__77evBMjaJOlKTaRv.json) | `system.stats.body.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Stabilized__LF0C1HVgY4hNZOFE.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Stabilized__LF0C1HVgY4hNZOFE.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Treated__nM9wqZXmrkFRRGTW.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Treated__nM9wqZXmrkFRRGTW.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left__r34NuXwHfPGZCpTu.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left__r34NuXwHfPGZCpTu.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right__yI6kHQM8voHrBF2h.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right__yI6kHQM8voHrBF2h.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json) | `system.stats.int.totalModifiers`, `system.stats.will.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Treated__KsYEWWO5KlPHSdCy.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound__Treated__KsYEWWO5KlPHSdCy.json) | `system.stats.will.totalModifiers` |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Minor_Head_Wound_wPRuwd7RdLWnWmnb.json) | `system.stats.int.totalModifiers`, `system.stats.will.totalModifiers` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Stabilized__LNy3P3HUw2Ja9DNu.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Stabilized__LNy3P3HUw2Ja9DNu.json) | `system.stats.dex.totalModifiers` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Treated__XQeXSAhvjrQZNpAE.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Treated__XQeXSAhvjrQZNpAE.json) | `system.stats.dex.totalModifiers` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json) | `system.stats.dex.totalModifiers` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json) | `system.stats.spd.max` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Stabilized__lck0EEySmuLZXMrA.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Stabilized__lck0EEySmuLZXMrA.json) | `system.stats.spd.max` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json) | `system.stats.spd.max` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Stabilized__vYza9bpK13G36YRV.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Stabilized__vYza9bpK13G36YRV.json) | `system.stats.spd.max` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage_PVraD16y2VWkOH6J.json) | `system.stats.body.max`, `system.stats.spd.max` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json) | `system.stats.body.max`, `system.stats.spd.max` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Stabilized__LM6Kkh0ib6ux4WQp.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock__Stabilized__LM6Kkh0ib6ux4WQp.json) | `system.stats.dex.totalModifiers`, `system.stats.int.totalModifiers`, `system.stats.ref.totalModifiers`, `system.stats.will.totalModifiers` |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Spetic_Shock_tF3hsi4yZOMJ6xuW.json) | `system.stats.dex.totalModifiers`, `system.stats.int.totalModifiers`, `system.stats.ref.totalModifiers`, `system.stats.will.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Stabilized__NiGtzaHs4dUj8Pmd.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Stabilized__NiGtzaHs4dUj8Pmd.json) | `system.stats.spd.max` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Treated__kfyfxEVsMRUDDk1A.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Treated__kfyfxEVsMRUDDk1A.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json) | `system.stats.spd.max` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json) | `system.stats.spd.max` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json) | `system.stats.spd.max` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion_IK7pM8p3NcM4thcz.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion_IK7pM8p3NcM4thcz.json) | `system.stats.dex.totalModifiers`, `system.stats.int.totalModifiers`, `system.stats.ref.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Stabilized__AFkm8KjxkwYxOCQo.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Stabilized__AFkm8KjxkwYxOCQo.json) | `system.stats.dex.totalModifiers`, `system.stats.int.totalModifiers`, `system.stats.ref.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Treated__ItXAMwWil2A7IqRv.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Concussion__Treated__ItXAMwWil2A7IqRv.json) | `system.stats.dex.totalModifiers`, `system.stats.int.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture_UImIh794nOy21jg2.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture_UImIh794nOy21jg2.json) | `system.stats.dex.totalModifiers`, `system.stats.int.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture__Stabilized__ikv3qioEgGJG6Olw.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Skull_Fracture__Stabilized__ikv3qioEgGJG6Olw.json) | `system.stats.dex.totalModifiers`, `system.stats.int.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Stabilized__cfQ2OHPNVVKMDsDo.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Stabilized__cfQ2OHPNVVKMDsDo.json) | `system.stats.body.totalModifiers`, `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Treated__wFul3Zr7mMaKjA5I.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound__Treated__wFul3Zr7mMaKjA5I.json) | `system.stats.body.totalModifiers`, `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound_tiVrEesPSzZ64HpZ.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Sucking_Chest_Wound_tiVrEesPSzZ64HpZ.json) | `system.stats.body.totalModifiers`, `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs_7TzGQ2y4yZnG01im.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs_7TzGQ2y4yZnG01im.json) | `system.stats.body.totalModifiers` |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Stabilized__2c4PbGjd0segbvmr.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Ribs__Stabilized__2c4PbGjd0segbvmr.json) | `system.stats.body.totalModifiers` |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left__XPoH413WkKQUgrnw.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left__XPoH413WkKQUgrnw.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right__VhwzsUlv5csYSJTM.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right__VhwzsUlv5csYSJTM.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Stabilized__fNiSVOJzpaxVvZTE.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Stabilized__fNiSVOJzpaxVvZTE.json) | `system.stats.spd.totalModifiers` |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Treated__8qatuNeEROueRDcZ.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Treated__8qatuNeEROueRDcZ.json) | `system.stats.spd.totalModifiers` |

Область поиска: `module/`, `templates/`, `packsJson/`; дополнительно проверены динамические пути через `statMap` и `system[type]`. В старых [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) и [templates/sheets/actor/monster-sheet.hbs](../../../../../../../../../../templates/sheets/actor/monster-sheet.hbs) также есть обращения к статам; их текущая достижимость здесь не установлена. Все перечисленные соседи сохраняют прежний статус анализа.

## Данные и изменения состояния

`prepareBaseData` копирует данные без прибавления бонусов, деления или ограничения диапазона. Два последовательных вызова с одинаковыми исходными значениями дают одинаковый max. Для восьми характеристик `value` рассчитывает WitcherActor.calculateStat из `unmodifiedMax`, модификаторов и делителя состояния здоровья; у luck и toxicity текущий `value` служит ресурсом и не рассчитывается этим методом.

В `calculateStat` результат округляется вниз; собственного ограничения 1–10 в этой функции нет. Отдельные ограничения, изменение max эффектами и поздние этапы всего Actor должны разбираться в TASK-0003.007/009. Подмена смысла всех полей одним термином «характеристика с потолком» была бы неверной.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема и копирование | Реальные Stats/DataModel/NumberField Foundry 14.367 | 10 записей; toxicity initial 100; копирование идемпотентно и не меняет value/totalModifiers | Прямой вызов, не полный Actor. |
| Миграция | Три входа int: {max:7}, {max:7,unmodifiedMax:0}, {max:7,unmodifiedMax:4} | После подготовки max соответственно 0, 7, 4 | Мир и реальные старые документы не проверялись. |
| Охват migrateData | По одному прямому вызову для каждой из 10 записей с max=7/base=0 | Все десять баз стали 7; переданный source возвращён | Проверка условий текущего кода. |
| statMap | Реальный getField для 9 origin=stats | Все пути существуют; toxicity обслуживается отдельно | Отсутствие поля в справочнике не объявлено ошибкой. |
| Повторный проход Actor | Исходные prepareDerivedData/calculateStats с подменёнными соседними методами | Luck: 10 + модификатор 2 → 14; toxicity: 100 + 5 → 110 | Проверена именно повторная прибавка; не полноценный расчёт Actor. |

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Не установлено наличие проблемных старых данных в мирах; не проверены браузерные формы и полный цикл ActiveEffect. Внешние вызовы Stats.prepareBaseData вне репозитория не исключены. Полный Actor, его mixin-файлы и runtime компедиумов будут разобраны последующими порциями.

## Связанные проблемы

- [issue-00011](../../../../../../../../../issues/potential/issue-00011.md) — отсутствующее unmodifiedMax не восстанавливается из max при миграции.
- [issue-00012](../../../../../../../../../issues/potential/issue-00012.md) — два прохода calculateStats повторно прибавляют модификаторы luck/toxicity.max; проблема в потребителе.


## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.001 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
