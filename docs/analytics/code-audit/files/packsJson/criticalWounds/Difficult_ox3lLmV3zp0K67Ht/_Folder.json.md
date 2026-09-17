# packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/_Folder.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/_Folder.json](../../../../../../../packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/_Folder.json) |
| Тип файла | JSON: Folder типа Item |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-13 |
| Ветка и коммит | rusbar-main, aef03ca01b0db5887653d2b1301a4fe814372a3e |
| Изменения относительно коммита | Нет; 20 строк; SHA-256 f582bbe1f4b5af782c541756e51fa2c5b742f922c9dfe35f0601c96cc0b20313 |
| Задача и порция | [TASK-0003.060](../../../../../../tasks/task-0003.060.md) |
| Запись перекрёстной сверки | [Протокол .060](../../../../review-log.md#task-0003060) |

## Назначение файла

Экспорт папки Difficult, объединяющей 24 Item тяжёлых травм в восемь цепочек. Папка не задаёт воздействий Actor.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Difficult | Корневой Folder; name:4, _id:7 | ID `ox3lLmV3zp0K67Ht`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Folder.ox3lLmV3zp0K67Ht` | Группировка и отображение |
| _key / folder / sort | Корневые поля | `"!folders!ox3lLmV3zp0K67Ht"` / `null` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
| flags / _stats | Корневые метаданные | `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | История экспорта и пользовательские флаги; версия в _stats не подтверждает запуск этой версии сейчас |
| type / sorting / color / description | Корневые поля | `"Item"` / `"a"` / `null` / `""` | Folder-модель; system/effects/followUp отсутствуют |

## Основные функции и методы

JSON не вводит собственных функций или обработчиков. BaseFolder и инструменты компедиумов обеспечивают чтение, отображение и экспорт папки.

## Используемые сущности и зависимости

| Сущность | Источник | Вид связи | Место/цель и доказательство |
| --- | --- | --- | --- |
| criticalWounds | [system.json](../../../../../../../system.json) | Регистрация | Строки 28,52–56; Item-пакет и packFolders |
| compilePack / extractPack | [utils/packs.mjs](../../../../../../../utils/packs.mjs), [utils/extract.mjs](../../../../../../../utils/extract.mjs) | Сборка/экспорт | Рекурсивные JSON и folders:true; статически, без записи |
| BaseFolder | Foundry 14.367.0; /opt/foundryvtt/common/documents/ и common/data/fields.mjs | Внешнее ядро | Настоящие классы, строгая валидация и штатная миграция |

## Известные потребители

| Потребитель | Используемые данные | Условия и доказательство |
| --- | --- | --- |
| 24 соседних Item | folder=ox3lLmV3zp0K67Ht | Все прямые дети перечислены ниже; проверены файлы и модель Folder |

Текстовая [Difficult Critical](../../../../../../../packsJson/combat/Difficult_Critical_VIup1SZTMKCSGGbT.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Восемь цепочек none → stabilized → treated, 16 существующих followUp, восемь null-окончаний; циклов и выходов из папки нет. У двух правых stabilized Item перепутаны location (issue-00327). Изменения Actor задают Item, а не папка.

| Дочерний Item | ID / состояние / локация |
| --- | --- |
| [Compound Arm Fracture (Left - Stabilized)](Compound_Arm_Fracture__Left___Stabilized__tdcGSOZGCUhNArDc.json.md) | `tdcGSOZGCUhNArDc` / stabilized / leftArm |
| [Compound Arm Fracture (Left - Treated)](Compound_Arm_Fracture__Left___Treated__zaKPfDQFGTR8FKju.json.md) | `zaKPfDQFGTR8FKju` / treated / leftArm |
| [Compound Arm Fracture (Left)](Compound_Arm_Fracture__Left__saPd4IMUCv5qZE60.json.md) | `saPd4IMUCv5qZE60` / none / leftArm |
| [Compound Arm Fracture (Right - Stabilized)](Compound_Arm_Fracture__Right___Stabilized__NHNctAuhsapGZXiP.json.md) | `NHNctAuhsapGZXiP` / stabilized / rightLeg |
| [Compound Arm Fracture (Right - Treated)](Compound_Arm_Fracture__Right___Treated__ujz1IMKCXoJF9w91.json.md) | `ujz1IMKCXoJF9w91` / treated / rightArm |
| [Compound Arm Fracture (Right)](Compound_Arm_Fracture__Right__c3H8Xx7WYCcM37k6.json.md) | `c3H8Xx7WYCcM37k6` / none / rightArm |
| [Compound Leg Fracture (Left - Stabilized)](Compound_Leg_Fracture__Left___Stabilized__NiGtzaHs4dUj8Pmd.json.md) | `NiGtzaHs4dUj8Pmd` / stabilized / leftLeg |
| [Compound Leg Fracture (Left - Treated)](Compound_Leg_Fracture__Left___Treated__kfyfxEVsMRUDDk1A.json.md) | `kfyfxEVsMRUDDk1A` / treated / leftLeg |
| [Compound Leg Fracture (Left)](Compound_Leg_Fracture__Left__flpxY7FVPGevwfcg.json.md) | `flpxY7FVPGevwfcg` / none / leftLeg |
| [Compound Leg Fracture (Right)](Compound_Leg_Fracture__Right__Rf0m4mGjeHEl0PxP.json.md) | `Rf0m4mGjeHEl0PxP` / none / rightLeg |
| [Compound Leg Fracture (Right - Stabilized)](Compound_Leg_Fracture__Right___Stabilized__QCugb1JqpiFyBEN4.json.md) | `QCugb1JqpiFyBEN4` / stabilized / rightArm |
| [Compound Leg Fracture (Right - Treated)](Compound_Leg_Fracture__Right___Treated__3SwpPbi2ddEJkebh.json.md) | `3SwpPbi2ddEJkebh` / treated / rightLeg |
| [Concussion](Concussion_IK7pM8p3NcM4thcz.json.md) | `IK7pM8p3NcM4thcz` / none / head |
| [Concussion (Stabilized)](Concussion__Stabilized__AFkm8KjxkwYxOCQo.json.md) | `AFkm8KjxkwYxOCQo` / stabilized / head |
| [Concussion (Treated)](Concussion__Treated__ItXAMwWil2A7IqRv.json.md) | `ItXAMwWil2A7IqRv` / treated / head |
| [Skull Fracture](Skull_Fracture_UImIh794nOy21jg2.json.md) | `UImIh794nOy21jg2` / none / head |
| [Skull Fracture (Stabilized)](Skull_Fracture__Stabilized__ikv3qioEgGJG6Olw.json.md) | `ikv3qioEgGJG6Olw` / stabilized / head |
| [Skull Fracture (Treated)](Skull_Fracture__Treated__v4RVIshohh1PPuAu.json.md) | `v4RVIshohh1PPuAu` / treated / head |
| [Sucking Chest Wound (Stabilized)](Sucking_Chest_Wound__Stabilized__cfQ2OHPNVVKMDsDo.json.md) | `cfQ2OHPNVVKMDsDo` / stabilized / torso |
| [Sucking Chest Wound (Treated)](Sucking_Chest_Wound__Treated__wFul3Zr7mMaKjA5I.json.md) | `wFul3Zr7mMaKjA5I` / treated / torso |
| [Sucking Chest Wound](Sucking_Chest_Wound_tiVrEesPSzZ64HpZ.json.md) | `tiVrEesPSzZ64HpZ` / none / torso |
| [Torn Stomach](Torn_Stomach_5gnx9xNF52ap9PYi.json.md) | `5gnx9xNF52ap9PYi` / none / torso |
| [Torn Stomach (Stabilized)](Torn_Stomach__Stabilized__EpF0FD1nFXJTJ5Tj.json.md) | `EpF0FD1nFXJTJ5Tj` / stabilized / torso |
| [Torn Stomach (Treated)](Torn_Stomach__Treated__Mg1jn99OitVPdvje.json.md) | `Mg1jn99OitVPdvje` / treated / torso |

## Проверки и доказательства

[Протокол .060](../../../../review-log.md#task-0003060): все 25 JSON / 3351 строк прочитаны, корневые ID/_key сверены среди 98 criticalWounds, вложенные _key/ID — в своей области. Все 16 followUp проверены до конечного состояния, без циклов и переходов вне Difficult. Настоящие модели и методы в изолированном Node 24.16.0 прошли 1748 утверждений: 24 Item, Folder, 25 effects/201 changes, подготовленные поля/производные, 24 treat, семь heal, восемь выборов, повторный addItem, исключение эффекта и подпись правой treated ноги. Отдельный сценарий: 43 утверждения, девять исходных периодических записей и три диагностические копии с override вместо ADD. Всего 1791 утверждение. Числа относятся к порции, индивидуальные значения указаны выше.

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. 98 JSON и62 followUp проверены; состав установленного packs/ и серверный getIndex не читались. .017 сводит манифест/экспорты/таблицы, включая выбор кандидатов и пустые tailWing. Критерий: источник нужного Item и индексные поля подтверждены отдельно от текста RollTable и предположений по рулбуку. Границы: [U012-02](../../../../cross-check-0002.md#u012-02) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. [issue-00328](../../../../../../issues/potential/issue-00328.md) — ADD объекта периодического урона; [issue-00021](../../../../../../issues/potential/issue-00021.md) — потеря типа в отдельном положительном контроле. [issue-00036](../../../../../../issues/potential/issue-00036.md) — max/value характеристики. [issue-00004](../../../../../../issues/potential/issue-00004.md) — commonspeech/commonsp. [issue-00327](../../../../../../issues/closed/issue-00327.md) — локации стабилизированных правых переломов. [issue-00326](../../../../../../issues/closed/issue-00326.md) — имя левой ноги у правого Item. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-13 — полная карточка в TASK-0003.060 на указанном коммите; исходник не изменён. [Протокол .060](../../../../review-log.md#task-0003060) содержит общие условия и индивидуальные проверки.

## Дополнительная сверка TASK-0003.061

2026-09-14; rusbar-main, 1cae095ac2f0f009fb1358a888a7afcf5ea5ec2e. Исходник не изменён.

После [Deadly](../Deadly_uofXQEP6HBtekOAO/_Folder.json.md) завершено чтение всех 98 JSON criticalWounds. Повтор строгих моделей/потребителей охватил 94 Item/4 Folder/79 эффектов/360 changes, 62 перехода и 48 выборов. Статическая сверка подтверждает 31 цепочку из трёх Item плюс конечную Decapitation, без циклов/отсутствующих UUID. Пять смен location относятся к прежним [issue-00325](../../../../../../issues/closed/issue-00325.md)/[issue-00327](../../../../../../issues/closed/issue-00327.md); Complex first-find — [issue-00324](../../../../../../issues/closed/issue-00324.md); единственный disabled относится к Deadly [issue-00329](../../../../../../issues/closed/issue-00329.md). Исторические итоги данной порции сохранены.

[Протокол и ограничения](../../../../review-log.md#task-0003061). Настоящие модели/методы исполнены с явными фасадами окружения и перехватом записи; полный клиентский lifecycle, мир, БД и серверный запуск не проверены.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Folder `ox3lLmV3zp0K67Ht` («Difficult») содержит 24 Item, `sorting=a`, `sort=0`; собственных effects/changes нет. 98 JSON — 94 Item и 4 Folder, а не таблицы бросков; четыре папки группируют 24/24/24/22 Item. Всего 79 эффектов/360 изменений;31 цепочка из 3 Item плюс конечный none,62 существующих followUp без циклов. Сырые changes мигрируют в system.changes: 32 multiply/328 add; null priority получает 10/20, четыре явных 0 сохраняются. Все transfer=true, единственный disabled в Deadly. Исторический origin не выбирает Actor-получателя; runtime читает документы пакета, не эти JSON напрямую.

Сопоставленные определения и потребители: [system.json](../../../system.json.md), [utils/packs.mjs](../../../utils/packs.mjs.md), [utils/extract.mjs](../../../utils/extract.mjs.md), [module/setup/settings.js](../../../module/setup/settings.js.md), [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [packsJson/criticalWounds/Difficult_ox3lLmV3zp0K67Ht/Compound_Arm_Fracture__Left___Stabilized__tdcGSOZGCUhNArDc.json](Compound_Arm_Fracture__Left___Stabilized__tdcGSOZGCUhNArDc.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-09](../../../../cross-check-0002.md#r012-09). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
