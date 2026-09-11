# module/data/actor/templates/common/skills/skillsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/skills/skillsData.js](../../../../../../../../../../module/data/actor/templates/common/skills/skillsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `52acddd5fb7d67e993eed1ad2c89b335aef6fd1d` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.002](../../../../../../../../../tasks/task-0003.002.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.002](../../../../../../../review-log.md#task-0003002) |

## Назначение файла

Собирает семь групп базовых навыков в объект полей для схемы Actor. Функция skills() не является классом или вычислителем бросков.

## Условия использования

При импорте загружаются семь групп. [CommonActorData.defineSchema](../../../../../../../../../../module/data/actor/commonActorData.js):39 вызывает skills() и оборачивает результат в SchemaField skills; это единственный найденный прямой импорт/вызов фабрики. CharacterData и MonsterData наследуют CommonActorData. Регистрация документных моделей описана в [registerDataModels](../../../../../setup/registerDataModels.js.md).

## Введённые сущности и действия с ними

Экспорт по умолчанию — функция skills. Локальный fields ссылается на foundry.data.fields. Результат — новый обычный объект с семью EmbeddedDataField, всего 52 навыка:

| Ключ system.skills | Класс / импорт | Навыков | Карточка |
| --- | --- | --- | --- |
| int | [Intelligence](../../../../../../../../../../module/data/actor/templates/common/skills/intData.js) | 13 | [Описание](intData.js.md) |
| ref | [Reflex](../../../../../../../../../../module/data/actor/templates/common/skills/refData.js) | 8 | [Описание](refData.js.md) |
| dex | [Dexterity](../../../../../../../../../../module/data/actor/templates/common/skills/dexData.js) | 5 | [Описание](dexData.js.md) |
| body | [Body](../../../../../../../../../../module/data/actor/templates/common/skills/bodyData.js) | 2 | [Описание](bodyData.js.md) |
| emp | [Empathy](../../../../../../../../../../module/data/actor/templates/common/skills/empData.js) | 10 | [Описание](empData.js.md) |
| cra | [Craft](../../../../../../../../../../module/data/actor/templates/common/skills/craData.js) | 7 | [Описание](craData.js.md) |
| will | [Will](../../../../../../../../../../module/data/actor/templates/common/skills/willData.js) | 7 | [Описание](willData.js.md) |

SPD и LUCK в этой фабрике отсутствуют; это не утверждение об отсутствии соответствующих характеристик Actor.

## Основные функции и методы

skills():11–21 без аргументов возвращает поля групп int/ref/dex/body/emp/cra/will. Не принимает данные Actor, не вызывает update, не рассчитывает значения. Методы defineSchema/migrateData принадлежат импортированным группам; modifiedValue — вложенному Skill.

## Используемые сущности и зависимости

| Сущность | Определение | Связь и доказательство |
| --- | --- | --- |
| Intelligence | [module/data/actor/templates/common/skills/intData.js](../../../../../../../../../../module/data/actor/templates/common/skills/intData.js) | Прямой default import :1–7; EmbeddedDataField(Intelligence) :13–19 по ключу int. |
| Reflex | [module/data/actor/templates/common/skills/refData.js](../../../../../../../../../../module/data/actor/templates/common/skills/refData.js) | Прямой default import :1–7; EmbeddedDataField(Reflex) :13–19 по ключу ref. |
| Dexterity | [module/data/actor/templates/common/skills/dexData.js](../../../../../../../../../../module/data/actor/templates/common/skills/dexData.js) | Прямой default import :1–7; EmbeddedDataField(Dexterity) :13–19 по ключу dex. |
| Body | [module/data/actor/templates/common/skills/bodyData.js](../../../../../../../../../../module/data/actor/templates/common/skills/bodyData.js) | Прямой default import :1–7; EmbeddedDataField(Body) :13–19 по ключу body. |
| Empathy | [module/data/actor/templates/common/skills/empData.js](../../../../../../../../../../module/data/actor/templates/common/skills/empData.js) | Прямой default import :1–7; EmbeddedDataField(Empathy) :13–19 по ключу emp. |
| Craft | [module/data/actor/templates/common/skills/craData.js](../../../../../../../../../../module/data/actor/templates/common/skills/craData.js) | Прямой default import :1–7; EmbeddedDataField(Craft) :13–19 по ключу cra. |
| Will | [module/data/actor/templates/common/skills/willData.js](../../../../../../../../../../module/data/actor/templates/common/skills/willData.js) | Прямой default import :1–7; EmbeddedDataField(Will) :13–19 по ключу will. |
| fields.EmbeddedDataField | Внешний API /opt/foundryvtt/common/data/fields.mjs, Foundry 14.367.0 | Глобальная ссылка :9; конструирует поля с DataModel каждой группы. |

Конфигурация и локализации не импортируются фабрикой. Их используют группы/потребители по описанным связям. Общая структура каждой записи — [Skill](skillData.js.md).

## Известные потребители

[module/data/actor/commonActorData.js](../../../../../../../../../../module/data/actor/commonActorData.js):3,39 — прямой импорт и вызов. Наследующие [module/data/actor/characterData.js](../../../../../../../../../../module/data/actor/characterData.js) и [module/data/actor/monsterData.js](../../../../../../../../../../module/data/actor/monsterData.js) получают дерево system.skills. [module/data/actor/lootData.js](../../../../../../../../../../module/data/actor/lootData.js) и [module/data/investigation/mysteryActorData.js](../../../../../../../../../../module/data/investigation/mysteryActorData.js) не наследуют CommonActorData.

Динамические читатели и источники изменений полей перечислены по именам методов и файлам в [карточке Skill](skillData.js.md); особые потребители отдельных групп — в семи карточках выше. [config.js](../../../../../setup/config.js.md) содержит 52 записи skillMap: все attribute.name/name разрешаются в реальные навыки; в одной записи ключ commonspeech отличается от name=commonsp.

### Строковые пути из JSON-компедиумов

Рекурсивно просмотрены строковые значения 226 JSON, найдено 267 ссылок system.skills в 37 файлах ниже; 54 различных пути. Проверена адресация, а не исполнение и миграция этих эффектов в Foundry. 264 ссылки соответствуют полям модели, три адресуют int.commonspeech.activeEffectModifiers вместо commonsp. Ни одна карточка JSON этим просмотром не считается завершённой.

| Файл-источник | Группы / число ссылок | Несовпадение |
| --- | --- | --- |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Stabilized__LF0C1HVgY4hNZOFE.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Stabilized__LF0C1HVgY4hNZOFE.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Treated__nM9wqZXmrkFRRGTW.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left___Treated__nM9wqZXmrkFRRGTW.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left__r34NuXwHfPGZCpTu.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Left__r34NuXwHfPGZCpTu.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right__yI6kHQM8voHrBF2h.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Fractured_Leg__Right__yI6kHQM8voHrBF2h.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth_IMLpjhiZ0yg6hjKI.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth_IMLpjhiZ0yg6hjKI.json) | emp, int, will / 10 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Stabilized__wccN560fe7WQgT0N.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Stabilized__wccN560fe7WQgT0N.json) | emp, int, will / 10 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Treated__yHU7iYTocbAok2wH.json](../../../../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/Lost_Teeth__Treated__yHU7iYTocbAok2wH.json) | emp, int, will / 10 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Stabilized__LNy3P3HUw2Ja9DNu.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Stabilized__LNy3P3HUw2Ja9DNu.json) | int / 1 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Treated__XQeXSAhvjrQZNpAE.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye__Treated__XQeXSAhvjrQZNpAE.json) | int / 1 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Damaged_Eye_zHK1XmZ77V8c26Xv.json) | int / 1 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Stabilized__lck0EEySmuLZXMrA.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Left___Stabilized__lck0EEySmuLZXMrA.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Stabilized__vYza9bpK13G36YRV.json](../../../../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/Dismembered_Leg__Right___Stabilized__vYza9bpK13G36YRV.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Stabilized__NiGtzaHs4dUj8Pmd.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Stabilized__NiGtzaHs4dUj8Pmd.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Treated__kfyfxEVsMRUDDk1A.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left___Treated__kfyfxEVsMRUDDk1A.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach_5gnx9xNF52ap9PYi.json) | body, cra, dex, emp, int, ref, will / 52 | effects[0].changes[4].key → commonspeech; [issue-00004](../../../../../../../../../issues/potential/issue-00004.md) |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Stabilized__EpF0FD1nFXJTJ5Tj.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Stabilized__EpF0FD1nFXJTJ5Tj.json) | body, cra, dex, emp, int, ref, will / 52 | effects[0].changes[4].key → commonspeech; [issue-00004](../../../../../../../../../issues/potential/issue-00004.md) |
| [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Treated__Mg1jn99OitVPdvje.json](../../../../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Torn_Stomach__Treated__Mg1jn99OitVPdvje.json) | body, cra, dex, emp, int, ref, will / 52 | effects[0].changes[4].key → commonspeech; [issue-00004](../../../../../../../../../issues/potential/issue-00004.md) |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw_UnWBI9Sgu4AJv1z1.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw_UnWBI9Sgu4AJv1z1.json) | emp, int, will / 10 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Stabilized__h15wRehQQoIkxcf0.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Stabilized__h15wRehQQoIkxcf0.json) | emp, int, will / 10 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Treated__AODuTRNu2RtJJhLD.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw__Treated__AODuTRNu2RtJJhLD.json) | will / 3 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar_8tqapNHVCmSwijJw.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar_8tqapNHVCmSwijJw.json) | emp, int / 6 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Stabilized__AJeuZeFF29nEI5fc.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Stabilized__AJeuZeFF29nEI5fc.json) | emp, int / 6 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Treated__kbeASc2PnnkYc5SR.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Disfiguring_Scar__Treated__kbeASc2PnnkYc5SR.json) | emp / 1 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left___Treated__q5vr9VLD2tEkL1ux.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Left___Treated__q5vr9VLD2tEkL1ux.json) | body / 1 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right___Treated__YiusbDXfFDhqwtQT.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Arm__Right___Treated__YiusbDXfFDhqwtQT.json) | body / 1 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left__XPoH413WkKQUgrnw.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left__XPoH413WkKQUgrnw.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right__VhwzsUlv5csYSJTM.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right__VhwzsUlv5csYSJTM.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |
| [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Stabilized__fNiSVOJzpaxVvZTE.json](../../../../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Sprained_Leg__Right___Stabilized__fNiSVOJzpaxVvZTE.json) | dex, ref / 2 | Не найдено по проверенным строковым путям |

## Данные и изменения состояния

Фабрика создаёт описания полей. Значения экземпляров и модификации Actor в ней отсутствуют. Миграции групп меняют label, Skill.modifiedValue только читает. Сохранение флагов/значений выполняется внешними формами и методами Actor, применение модификаторов — отдельными механизмами Foundry и системы.

## Проверки и доказательства

Прочитаны все 21 строка и определения семи импортов. Поиск импортов и вызовов подтверждает CommonActorData как непосредственного потребителя. Реальная схема CommonActorData сверена в обе стороны с 52 записями skillMap; повторное создание из toObject() дало подписи всех навыков. Поля сгруппированы 13+8+5+2+10+7+7=52. Рекурсивная сверка JSON-путей и изолированные сценарии приведены в журнале TASK-0003.002.

## Непроверенные участки и открытые вопросы

Полный разбор CommonActorData/CharacterData/MonsterData запланирован в TASK-0003.006. Здесь подтверждены наследование, вложение навыков и указанные обращения. Не выполнялись загрузка мира, миграция компедиумов, работа effects.changes в текущем клиенте или изменение данных.

## Связанные проблемы

[issue-00004](../../../../../../../../../issues/potential/issue-00004.md), [issue-00015](../../../../../../../../../issues/potential/issue-00015.md), [issue-00016](../../../../../../../../../issues/potential/issue-00016.md), [issue-00017](../../../../../../../../../issues/potential/issue-00017.md), [issue-00018](../../../../../../../../../issues/potential/issue-00018.md). Это проблемы определений/потребителей дерева навыков; фабрика не объявляется причиной всех перечисленных наблюдений.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.002 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Подтверждено общее включение skills:39 и семи групп/52 моделей Skill у персонажа и монстра. skillGroupModifiers определён отдельно в CommonActorData:40–46; modifierMixin.addActiveEffects добавляет его значения в строку броска, не записывает их в Skill.value.

Карточки сборки: [commonActorData](../../../commonActorData.js.md). [Сверка TASK-0003.006](../../../../../../../review-log.md#task-0003006).

## Уточнение TASK-0003.007

2026-09-10, `b8b89a7e3392235f993c21f3c6d277a4a2e7a55f`. Подтверждён доступ modifierMixin через skill.attribute.name/skill.name. Указанный в конфигурации путь должен существовать в общей модели; groups allSkills не обходят ранний выход для неизвестного имени. Перечень вызовов навыкового модификатора отражён в новой карточке.

Карточки: [WitcherActor](../../../../../actor/witcherActor.js.md), [modifierMixin](../../../../../actor/mixins/modifierMixin.js.md). [Сверка TASK-0003.007](../../../../../../../review-log.md#task-0003007).

## Уточнение TASK-0003.029

2026-09-11, `273a6d7db0b7c866399db3ecd4f7191817ae6f10`. Семь групп дают 52 встроенных навыка; текущий tab-skills выводит их дважды — all и соответствующая группа. Те же ключи ограничивают показ собственных Items и исключают spd/luck, хотя Item-лист и _prepareCustomSkills предлагают/готовят девять групп.

Сверенные связи: [templates/partials/character/tab-skills.hbs](../../../../../../../../../../templates/partials/character/tab-skills.hbs); [module/item/sheets/WitcherSkillItemSheet.js](../../../../../../../../../../module/item/sheets/WitcherSkillItemSheet.js). Полные карточки новых файлов — в [указателе порции](../../../../../../README.md#навыки-броски-развитие-и-пользовательские-навыки--task-0003029). [Проверки, ограничения и версия](../../../../../../../review-log.md#task-0003029). Исходники и статус проблем не менялись.
