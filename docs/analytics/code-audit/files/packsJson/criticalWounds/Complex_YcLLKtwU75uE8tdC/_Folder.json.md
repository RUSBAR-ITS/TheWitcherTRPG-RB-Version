# packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/_Folder.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/_Folder.json](../../../../../../../packsJson/criticalWounds/Complex_YcLLKtwU75uE8tdC/_Folder.json) |
| Тип файла | JSON: Folder типа Item |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-13 |
| Ветка и коммит | rusbar-main, d26e3381a7290807b8e76f9817d0f7a603c0e61a |
| Изменения относительно коммита | Нет; 20 строк; SHA-256 fc5c28500f1e19e8b813ed788fa0d7aaf9e1f5ae52985a87181922df146b9020 |
| Задача и порция | [TASK-0003.059](../../../../../../tasks/task-0003.059.md) |
| Запись перекрёстной сверки | [Протокол .059](../../../../review-log.md#task-0003059) |

## Назначение файла

Экспорт папки Complex, объединяющей 24 Item сложных травм в восемь цепочек. Папка не задаёт воздействий Actor.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Complex | Корневой Folder; name:4, _id:7 | ID `YcLLKtwU75uE8tdC`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Folder.YcLLKtwU75uE8tdC` | Группировка и отображение |
| _key / folder / sort | Корневые поля | `"!folders!YcLLKtwU75uE8tdC"` / `null` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
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
| 24 соседних Item | folder=YcLLKtwU75uE8tdC | Все прямые дети перечислены ниже; проверены файлы и модель Folder |

Текстовая [Complex Critical](../../../../../../../packsJson/combat/Complex_Critical_p3EAPCnu8RDawpWR.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Восемь цепочек none → stabilized → treated, 16 существующих followUp, восемь null-окончаний; циклов и выходов из папки нет. Изменения Actor задают Item, а не папка.

| Дочерний Item | ID / состояние / локация |
| --- | --- |
| [Broken Ribs](Broken_Ribs_VfgJzcV75cGqsjuF.json.md) | `VfgJzcV75cGqsjuF` / none / torso |
| [Broken Ribs (Stabilized)](Broken_Ribs__Stabilized__4LmC6nGwRM0PpNl7.json.md) | `4LmC6nGwRM0PpNl7` / stabilized / torso |
| [Broken Ribs (Treated)](Broken_Ribs__Treated__77evBMjaJOlKTaRv.json.md) | `77evBMjaJOlKTaRv` / treated / torso |
| [Fractured Arm (Left)](Fractured_Arm__Left__Z2L7diKDSE9L7E9d.json.md) | `Z2L7diKDSE9L7E9d` / none / leftArm |
| [Fractured Arm (Left - Stabilized)](Fractured_Arm__Left___Stabilized__eCiJjDqfUyaXCW2z.json.md) | `eCiJjDqfUyaXCW2z` / stabilized / leftArm |
| [Fractured Arm (Left - Treated)](Fractured_Arm__Left___Treated__kPIkW1AXuybKZPEh.json.md) | `kPIkW1AXuybKZPEh` / treated / leftArm |
| [Fractured Arm (Right)](Fractured_Arm__Right__ZOyO6WlnMTDjzBj9.json.md) | `ZOyO6WlnMTDjzBj9` / none / rightArm |
| [Fractured Arm (Right - Stabilized)](Fractured_Arm__Right___Stabilized__t9bcLB3zDGUX9Uuq.json.md) | `t9bcLB3zDGUX9Uuq` / stabilized / rightArm |
| [Fractured Arm (Right - Treated)](Fractured_Arm__Right___Treated__djnBTcYyGVsykdoy.json.md) | `djnBTcYyGVsykdoy` / treated / rightArm |
| [Fractured Leg (Left - Stabilized)](Fractured_Leg__Left___Stabilized__LF0C1HVgY4hNZOFE.json.md) | `LF0C1HVgY4hNZOFE` / stabilized / leftLeg |
| [Fractured Leg (Left - Treated)](Fractured_Leg__Left___Treated__nM9wqZXmrkFRRGTW.json.md) | `nM9wqZXmrkFRRGTW` / treated / leftLeg |
| [Fractured Leg (Left)](Fractured_Leg__Left__r34NuXwHfPGZCpTu.json.md) | `r34NuXwHfPGZCpTu` / none / leftLeg |
| [Fractured Leg (Right - Stabilized)](Fractured_Leg__Right___Stabilized__WNjcD3F3Hs5IdAaa.json.md) | `WNjcD3F3Hs5IdAaa` / stabilized / rightLeg |
| [Fractured Leg (Right - Treated)](Fractured_Leg__Right___Treated__Aa8wCz1OGM4gflmc.json.md) | `Aa8wCz1OGM4gflmc` / treated / rightLeg |
| [Fractured Leg (Right)](Fractured_Leg__Right__yI6kHQM8voHrBF2h.json.md) | `yI6kHQM8voHrBF2h` / none / rightLeg |
| [Lost Teeth](Lost_Teeth_IMLpjhiZ0yg6hjKI.json.md) | `IMLpjhiZ0yg6hjKI` / none / head |
| [Lost Teeth (Stabilized)](Lost_Teeth__Stabilized__wccN560fe7WQgT0N.json.md) | `wccN560fe7WQgT0N` / stabilized / head |
| [Lost Teeth (Treated)](Lost_Teeth__Treated__yHU7iYTocbAok2wH.json.md) | `yHU7iYTocbAok2wH` / treated / head |
| [Minor Head Wound (Stabilized)](Minor_Head_Wound__Stabilized__EnwgL7ApZTdHgMbD.json.md) | `EnwgL7ApZTdHgMbD` / stabilized / torso |
| [Minor Head Wound (Treated)](Minor_Head_Wound__Treated__KsYEWWO5KlPHSdCy.json.md) | `KsYEWWO5KlPHSdCy` / treated / torso |
| [Minor Head Wound](Minor_Head_Wound_wPRuwd7RdLWnWmnb.json.md) | `wPRuwd7RdLWnWmnb` / none / torso |
| [Ruptured Spleen (Stabilized)](Ruptured_Spleen__Stabilized__d8uhnIErEmsGtf94.json.md) | `d8uhnIErEmsGtf94` / stabilized / torso |
| [Ruptured Spleen (Treated)](Ruptured_Spleen__Treated__kFcie7Io28kKittg.json.md) | `kFcie7Io28kKittg` / treated / torso |
| [Ruptured Spleen](Ruptured_Spleen_rHrrGeB9A8bNCiC2.json.md) | `rHrrGeB9A8bNCiC2` / none / torso |
## Проверки и доказательства

[Протокол .059](../../../../review-log.md#task-0003059): все 25 JSON / 2058 строк прочитаны, корневые ID/_key сверены среди 98 criticalWounds, вложенные _key/ID — в своей области. Все 16 followUp проверены до конечного состояния, без циклов и переходов вне Complex. Настоящие модели и методы в изолированном Node 24.16.0 прошли 772 утверждения: 24 Item, Folder, 16 effects/61 changes, числовые поля/производные, 24 treat, семь heal, девять выборов, повторный addItem, исключение эффекта и три подписи правой ноги. Число относится к порции, индивидуальные значения указаны выше.

## Непроверенные участки и открытые вопросы

Сценарий использует реальные BaseItem/BaseActor и системные модели, настоящий WitcherActiveEffect с фасадом ClientDocumentMixin/registry. Подготовка и фазы вызваны явно; полный клиентский lifecycle, updateDuration, _preCreate/_preUpdate, calculateAttackStats, браузер и сеть не запускались. fromUuid и индекс представлены Map/массивом настоящих документов; записи и чат перехватывались, броня и вес заданы нулём. Для подписи формулы список appliedEffects задан из реальных активных эффектов; полный бросок/чат не воспроизводился. Внешние модули, действующие packs/ и игровые правила не проверены. Прохождение локальных сценариев не доказывает сохранение в мире или HTTP-доступ службы.

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. [issue-00324](../../../../../../issues/potential/issue-00324.md) — состав кандидатов complex/head/torso. [issue-00326](../../../../../../issues/potential/issue-00326.md) — подпись эффекта правой ноги. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-13 — полная карточка в TASK-0003.059 на указанном коммите; исходник не изменён. [Протокол .059](../../../../review-log.md#task-0003059) содержит общие условия и индивидуальные проверки.

## Уточнение TASK-0003.060

2026-09-13; rusbar-main, aef03ca01b0db5887653d2b1301a4fe814372a3e; исходник не изменён.

Соседняя Difficult проверена:25 JSON/25effects/201changes/16followUp. В отличие от 61 числового add Complex содержит 12 multiply и девять объектов; ADD объектов в Foundry14 не создаёт turnStartEffects. Срок Difficult=max(15−BODY.max,1), Complex=max(12−BODY.max,1). Прежние сценарии Complex повторно не исполнялись.

[Карточки Difficult](../Difficult_ox3lLmV3zp0K67Ht/_Folder.json.md), [протокол и ограничения](../../../../review-log.md#task-0003060). Мир и БД не менялись.
