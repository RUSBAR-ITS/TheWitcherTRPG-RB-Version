# packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/_Folder.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/_Folder.json](../../../../../../../packsJson/criticalWounds/Deadly_uofXQEP6HBtekOAO/_Folder.json) |
| Тип файла | JSON: Folder типа Item |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-14 |
| Ветка и коммит | rusbar-main, 1cae095ac2f0f009fb1358a888a7afcf5ea5ec2e |
| Изменения относительно коммита | Нет; 20 строк; SHA-256 3883a371d0568dc36bd78da363d2abc6faafdaf4f7bcd8bb8d26a0407333b5d6 |
| Задача и порция | [TASK-0003.061](../../../../../../tasks/task-0003.061.md) |
| Запись перекрёстной сверки | [Протокол .061](../../../../review-log.md#task-0003061) |

## Назначение файла

Экспорт папки Deadly: 22 Item смертельных травм; семь цепочек из трёх состояний и конечная Separated Spine/Decapitated. Папка не задаёт воздействий Actor.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует пакет Item `TheWitcherTRPG.criticalWounds` по пути packs/criticalWounds.db. [compilePack](../../../../../../../utils/packs.mjs) рекурсивно собирает экспорт, [extractPack](../../../../../../../utils/extract.mjs) извлекает его с папками; команды из [package.json](../../../../../../../package.json) не запускались. JSON не читается непосредственно в игровом applyCritWound; содержимое установленной БД не проверялось.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Назначение и доступность | Действия |
| --- | --- | --- | --- |
| Deadly | Корневой Folder; name:4, _id:7 | ID `uofXQEP6HBtekOAO`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Folder.uofXQEP6HBtekOAO` | Группировка и отображение |
| _key / folder / sort | Корневые поля | `"!folders!uofXQEP6HBtekOAO"` / `null` / `0` | Ключ экспорта, родительская папка и сортировка; sort не приоритет эффекта |
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
| 22 соседних Item | folder=uofXQEP6HBtekOAO | Все прямые дети перечислены ниже; проверены файлы и модель Folder |

Текстовая [Deadly Critical](../../../../../../../packsJson/combat/Deadly_Critical_GoXapMH54rEUWaZn.json) не читается applyCritWound как источник Item. Найденные маршруты не исключают внешние макросы или динамических потребителей.

## Данные и изменения состояния

Семь цепочек none → stabilized → treated, 14 существующих followUp, семь treated null-окончаний и отдельная Separated Spine/Decapitated с treatment=none/followUp=null. Циклов, смен локации и выходов из папки нет. Изменения Actor задают Item, а не папка.

| Дочерний Item | ID / состояние / локация |
| --- | --- |
| [Damaged Eye (Stabilized)](Damaged_Eye__Stabilized__LNy3P3HUw2Ja9DNu.json.md) | `LNy3P3HUw2Ja9DNu` / stabilized / head |
| [Damaged Eye (Treated)](Damaged_Eye__Treated__XQeXSAhvjrQZNpAE.json.md) | `XQeXSAhvjrQZNpAE` / treated / head |
| [Damaged Eye](Damaged_Eye_zHK1XmZ77V8c26Xv.json.md) | `zHK1XmZ77V8c26Xv` / none / head |
| [Dismembered Arm (Left)](Dismembered_Arm__Left__KQZRzczsSx1XY63m.json.md) | `KQZRzczsSx1XY63m` / none / leftArm |
| [Dismembered Arm (Left - Stabilized)](Dismembered_Arm__Left___Stabilized__vmRDG8kxeCu3sYQC.json.md) | `vmRDG8kxeCu3sYQC` / stabilized / leftArm |
| [Dismembered Arm (Left - Treated)](Dismembered_Arm__Left___Treated__8Z1iHJLXrFm2i3Fb.json.md) | `8Z1iHJLXrFm2i3Fb` / treated / leftArm |
| [Dismembered Arm (Right)](Dismembered_Arm__Right__ZxvWPJPDD9fm34Pc.json.md) | `ZxvWPJPDD9fm34Pc` / none / rightArm |
| [Dismembered Arm (Right - Stabilized)](Dismembered_Arm__Right___Stabilized__hKgvgj4lJ74wPt8N.json.md) | `hKgvgj4lJ74wPt8N` / stabilized / rightArm |
| [Dismembered Arm (Right - Treated)](Dismembered_Arm__Right___Treated__gPeOdwZ0OTVF9E3w.json.md) | `gPeOdwZ0OTVF9E3w` / treated / rightArm |
| [Dismembered Leg (Left)](Dismembered_Leg__Left__Us9OmoKhRydSqA8z.json.md) | `Us9OmoKhRydSqA8z` / none / leftLeg |
| [Dismembered Leg (Left - Stabilized)](Dismembered_Leg__Left___Stabilized__lck0EEySmuLZXMrA.json.md) | `lck0EEySmuLZXMrA` / stabilized / leftLeg |
| [Dismembered Leg (Left - Treated)](Dismembered_Leg__Left___Treated__eYEp1CPif98mDm2U.json.md) | `eYEp1CPif98mDm2U` / treated / leftLeg |
| [Dismembered Leg (Right)](Dismembered_Leg__Right__Ssi9d4GQsAyYnt86.json.md) | `Ssi9d4GQsAyYnt86` / none / rightLeg |
| [Dismembered Leg (Right - Stabilized)](Dismembered_Leg__Right___Stabilized__vYza9bpK13G36YRV.json.md) | `vYza9bpK13G36YRV` / stabilized / rightLeg |
| [Dismembered Leg (Right - Treated)](Dismembered_Leg__Right___Treated__KFbDbrS3OCs0C1h4.json.md) | `KFbDbrS3OCs0C1h4` / treated / rightLeg |
| [Heart Damage](Heart_Damage_PVraD16y2VWkOH6J.json.md) | `PVraD16y2VWkOH6J` / none / torso |
| [Heart Damage (Stabilized)](Heart_Damage__Stabilized__O8EM4quPU4A5VOHH.json.md) | `O8EM4quPU4A5VOHH` / stabilized / torso |
| [Heart Damage (Treated)](Heart_Damage__Treated__Me9fgalLrB0i9Z2O.json.md) | `Me9fgalLrB0i9Z2O` / treated / torso |
| [Separated Spine/Decapitated](Separated_Spine_Decapitated_MvrwnSrEqsTRdaeY.json.md) | `MvrwnSrEqsTRdaeY` / none / head |
| [Spetic Shock (Stabilized)](Spetic_Shock__Stabilized__LM6Kkh0ib6ux4WQp.json.md) | `LM6Kkh0ib6ux4WQp` / stabilized / torso |
| [Spetic Shock (Treated)](Spetic_Shock__Treated__vkr5MXhnalPp8yJJ.json.md) | `vkr5MXhnalPp8yJJ` / treated / torso |
| [Spetic Shock](Spetic_Shock_tF3hsi4yZOMJ6xuW.json.md) | `tF3hsi4yZOMJ6xuW` / none / torso |
## Проверки и доказательства

[Протокол .061](../../../../review-log.md#task-0003061): все 23 JSON / 2131 строка прочитаны; 22 Item, Folder, 21 эффект (20 активных), 43 changes и 14 followUp проверены индивидуально. Основной сценарий — 758 утверждений: строгие модели, поля/производные, все treat, восемь heal, восемь вариантов выбора, повтор addItem, подписи Awareness и контроли включённости/переноса. Периодический сценарий — 40 утверждений: семь ADD объектов и отдельный числовой modifier, два override-контроля, положительная проверка модификатора существующей bleed. Всего по Deadly 798. Итоговый повтор всего пакета — ещё 3182 утверждения на 94 Item/4 Folder/79 effects/360 changes/62 переходах и 48 выборах; повтор шести пакетов RollTable — 5223. Всего в .061: 9203 утверждения. Числа относятся к общим сценариям, значения данного документа указаны выше.

## Непроверенные участки и открытые вопросы

Сценарий использует реальные BaseItem/BaseActor и системные модели, настоящий WitcherActiveEffect с фасадом ClientDocumentMixin/registry. Подготовка и фазы вызваны явно; полный клиентский lifecycle, updateDuration, _preCreate/_preUpdate, calculateAttackStats, браузер и сеть не запускались. fromUuid и индекс представлены Map/массивом настоящих документов; записи и чат перехватывались, броня и вес заданы нулём. Для подписи формулы список appliedEffects задан из реальных активных эффектов; полный бросок/чат не воспроизводился. У периодического обработчика настоящий DamageInstance, но Actor.applyDamage, получение torso и HTML/чат — фасады: конечные HP/броня не вычислялись. Внешние модули, действующие packs/ и игровые правила не проверены. Прохождение локальных сценариев не доказывает сохранение в мире или HTTP-доступ службы.

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md) — ожидание замены, [issue-00127](../../../../../../issues/potential/issue-00127.md) — граница завершения лечения, [issue-00288](../../../../../../issues/potential/issue-00288.md) — повтор name/type. [issue-00328](../../../../../../issues/potential/issue-00328.md) — ADD объекта периодического урона; [issue-00021](../../../../../../issues/potential/issue-00021.md) — потеря типа в отдельном положительном контроле. [issue-00036](../../../../../../issues/potential/issue-00036.md) — max/value и перезапись производного максимума. [issue-00329](../../../../../../issues/potential/issue-00329.md) — выключенный эффект исходной правой ноги. Статусы potential сохранены, подтверждения/исправления не выполнялись. Наличие этих общих проблем не объявляет дефектом каждое поле или папку.

## История актуализации

2026-09-14 — полная карточка в TASK-0003.061 на указанном коммите; исходник не изменён. [Протокол .061](../../../../review-log.md#task-0003061) содержит общие условия и индивидуальные проверки.
