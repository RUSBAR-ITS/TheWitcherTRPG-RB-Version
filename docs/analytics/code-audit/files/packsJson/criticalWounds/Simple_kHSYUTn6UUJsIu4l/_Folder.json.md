# packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json](../../../../../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json) |
| Тип файла | JSON: Folder типа Item |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 5283da15a49422fc339c44add4e7d7d02c174ce4 |
| Изменения относительно коммита | Нет; 20 строк; SHA-256 ec79c51780224e357c4390e18c908237eacbb7d5a2e9ca78fbe39a6a9dca8523 |
| Задача и порция | [TASK-0003.058](../../../../../../tasks/task-0003.058.md) |
| Запись перекрёстной сверки | [Протокол TASK-0003.058](../../../../review-log.md#task-0003058) |

## Назначение файла

Экспорт папки Simple: группирует 24 травмы в восьми цепочках состояний. Это Folder, не травма и не RollTable; принадлежность папке сама по себе не применяет эффекты.

## Условия использования

[system.json](../../../../../../../system.json) регистрирует Item-пакет `TheWitcherTRPG.criticalWounds` по пути `packs/criticalWounds.db`. [compilePack в packs.mjs](../../../../../../../utils/packs.mjs) рекурсивно читает экспортный каталог; [extractPack в extract.mjs](../../../../../../../utils/extract.mjs) записывает JSON с папками и исключением изменяемых временных меток. Команды определены в [package.json](../../../../../../../package.json); они не запускались. Экспортный каталог не загружается движком напрямую и не доказывает содержимое действующего пакета.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| Simple | Корневой Folder, name: 4, _id: 7 | Группа травм | `kHSYUTn6UUJsIu4l`; UUID `Compendium.TheWitcherTRPG.criticalWounds.Folder.kHSYUTn6UUJsIu4l` | Чтение и отображение папки; нет автоматических воздействий |
| _key / folder / sort | Корневые поля | Идентификация экспортного документа и порядок | `"!folders!kHSYUTn6UUJsIu4l"` / `null` / `-100000` | Потребление ядром и инструментами экспорта; sort не задаёт приоритет изменений |
| type / sorting / color | Корневые поля | Тип документов и ручная сортировка | `Item` / `m` / `null` | Folder-модель; не поля CriticalWoundData |
| description / flags / _stats | Корневые поля | Метаданные папки | `""` / `{}` / `{"compendiumSource":null,"duplicateSource":null,"exportSource":null,"coreVersion":"13.351","systemId":"TheWitcherTRPG","systemVersion":"AUTOMATICALLY REPLACED BY GITHUB WORKFLOW ACTION"}` | Загрузка и отображение; программных действий здесь нет |

## Основные функции и методы

Собственных функций, классов и обработчиков JSON не вводит. Ядро создаёт Folder, инструменты компедиумов читают и записывают его описание.

## Используемые сущности и зависимости

| Сущность | Файл-источник или API | Вид связи | Место и цель | Доказательство |
| --- | --- | --- | --- | --- |
| criticalWounds | [system.json](../../../../../../../system.json) | Регистрация пакета | name/type/path и packFolders | Манифест, строки 28 и 52–56 |
| compilePack / extractPack | [utils/packs.mjs](../../../../../../../utils/packs.mjs), [utils/extract.mjs](../../../../../../../utils/extract.mjs) | Экспорт/сборка | Рекурсивный каталог и Folder | Статический разбор; без записи |
| BaseFolder | Foundry 14.367.0; /opt/foundryvtt/common/documents/folder.mjs | Внешнее ядро | Тип и структура Folder | Настоящие классы; строгая валидация |

## Известные потребители

| Файл-потребитель | Что использует | Способ и условия | Основание |
| --- | --- | --- | --- |
| 24 соседних JSON | _id Folder | Их folder=kHSYUTn6UUJsIu4l | Все перечислены ниже, структура проверена |

Поиск и проверенные маршруты не исключают внешние макросы, модули и динамические обращения. Текстовая таблица [Simple Critical](../../../../../../../packsJson/combat/Simple_Critical_SkHR3GrB2e3Tz1v4.json) не является источником этих Item для applyCritWound.

## Данные и изменения состояния

Папка не содержит effects, system, followUp или quantity. Изменений Actor не инициирует. Все 24 дочерних Item учтены:

| Item | ID / состояние |
| --- | --- |
| [Cracked Jaw](Cracked_Jaw_UnWBI9Sgu4AJv1z1.json.md) | `UnWBI9Sgu4AJv1z1` / none |
| [Cracked Jaw (Stabilized)](Cracked_Jaw__Stabilized__h15wRehQQoIkxcf0.json.md) | `h15wRehQQoIkxcf0` / stabilized |
| [Cracked Jaw (Treated)](Cracked_Jaw__Treated__AODuTRNu2RtJJhLD.json.md) | `AODuTRNu2RtJJhLD` / treated |
| [Cracked Ribs](Cracked_Ribs_7TzGQ2y4yZnG01im.json.md) | `7TzGQ2y4yZnG01im` / none |
| [Cracked Ribs (Stabilized)](Cracked_Ribs__Stabilized__2c4PbGjd0segbvmr.json.md) | `2c4PbGjd0segbvmr` / stabilized |
| [Cracked Ribs (Treated)](Cracked_Ribs__Treated__oe4y6zxH2WUR9gSj.json.md) | `oe4y6zxH2WUR9gSj` / treated |
| [Disfiguring Scar](Disfiguring_Scar_8tqapNHVCmSwijJw.json.md) | `8tqapNHVCmSwijJw` / none |
| [Disfiguring Scar (Stabilized)](Disfiguring_Scar__Stabilized__AJeuZeFF29nEI5fc.json.md) | `AJeuZeFF29nEI5fc` / stabilized |
| [Disfiguring Scar (Treated)](Disfiguring_Scar__Treated__kbeASc2PnnkYc5SR.json.md) | `kbeASc2PnnkYc5SR` / treated |
| [Foreign Object (Stabilized)](Foreign_Object__Stabilized__fnYssldrMLVqbF22.json.md) | `fnYssldrMLVqbF22` / stabilized |
| [Foreign Object (Treated)](Foreign_Object__Treated__rgRGVfLBlHMwUvGy.json.md) | `rgRGVfLBlHMwUvGy` / treated |
| [Foreign Object](Foreign_Object_mylVzp10NMor44XR.json.md) | `mylVzp10NMor44XR` / none |
| [Sprained Arm (Left - Stabilized)](Sprained_Arm__Left___Stabilized__01Seyu22NaDnctCi.json.md) | `01Seyu22NaDnctCi` / stabilized |
| [Sprained Arm (Left - Treated)](Sprained_Arm__Left___Treated__q5vr9VLD2tEkL1ux.json.md) | `q5vr9VLD2tEkL1ux` / treated |
| [Sprained Arm (Left)](Sprained_Arm__Left__quAixM7zp2bD9lXz.json.md) | `quAixM7zp2bD9lXz` / none |
| [Sprained Arm (Right - Stabilized)](Sprained_Arm__Right___Stabilized__yGy3oWvmpX6WMm56.json.md) | `yGy3oWvmpX6WMm56` / stabilized |
| [Sprained Arm (Right - Treated)](Sprained_Arm__Right___Treated__YiusbDXfFDhqwtQT.json.md) | `YiusbDXfFDhqwtQT` / treated |
| [Sprained Arm (Right)](Sprained_Arm__Right__umPVfrJeNU65S48O.json.md) | `umPVfrJeNU65S48O` / none |
| [Sprained Leg (Left)](Sprained_Leg__Left__XPoH413WkKQUgrnw.json.md) | `XPoH413WkKQUgrnw` / none |
| [Sprained Leg (Left - Stabilized)](Sprained_Leg__Left___Stabilized__eblucqnyOS7lb5E5.json.md) | `eblucqnyOS7lb5E5` / stabilized |
| [Sprained Leg (Left - Treated)](Sprained_Leg__Left___Treated__f7NaW1AMnrSLGkd3.json.md) | `f7NaW1AMnrSLGkd3` / treated |
| [Sprained Leg (Right)](Sprained_Leg__Right__VhwzsUlv5csYSJTM.json.md) | `VhwzsUlv5csYSJTM` / none |
| [Sprained Leg (Right - Stabilized)](Sprained_Leg__Right___Stabilized__fNiSVOJzpaxVvZTE.json.md) | `fNiSVOJzpaxVvZTE` / stabilized |
| [Sprained Leg (Right - Treated)](Sprained_Leg__Right___Treated__8qatuNeEROueRDcZ.json.md) | `8qatuNeEROueRDcZ` / treated |

Восемь исходных Item → восемь stabilized → восемь treated; проверены 16 существующих UUID-переходов, нет циклов или переходов из Simple. У treated followUp=null. 17 эффектов и 55 changes принадлежат Item, не папке.
## Проверки и доказательства

[Протокол TASK-0003.058](../../../../review-log.md#task-0003058): структурно проверены 25 JSON / 2068 строк, уникальность корневых ID и _key среди 98 criticalWounds, принадлежность Folder, все 16 переходов и все 17 эффектов / 55 изменений. Изолированный Node 24.16.0 исполнил 672 утверждения: настоящие модели Foundry 14.367.0 и системы, применение числовых изменений, 24 вызова treat, шесть вариантов heal, восемь выборов исходных травм, сложение двух ног, disabled/transfer/suppression и повторный addItem. Для данного файла проверены его собственные значения; общая цифра относится ко всей порции.

## Непроверенные участки и открытые вопросы

Полный клиент, браузер, серверный индекс, БД packs/, фактические записи/ошибки записи, все разновидности Actor и модули не проверены. В сценарии использован BaseItem с настоящей CriticalWoundData, не полный WitcherItem; его миграция сопоставлена статически. Реальный WitcherActiveEffect загружен с фасадом ClientDocumentMixin и registry; prepareBaseData и изменения выполнены, автоматический цикл подготовки/истечения клиента не запускался целиком. fromUuid, индекс, чат, create/update/delete и броня/вес представлены явно заданными фасадами. Игровые числа и формулировки не сверялись с книгами. Успешное локальное чтение не доказывает HTTP-доступ службы.

## Связанные проблемы

[issue-00325](../../../../../../issues/potential/issue-00325.md) — поле локации одного дочернего Item; [issue-00121](../../../../../../issues/potential/issue-00121.md), [issue-00127](../../../../../../issues/potential/issue-00127.md) и [issue-00288](../../../../../../issues/potential/issue-00288.md) — общие потребители. Наличие этих проблем не означает дефекта самой папки.

## История актуализации

2026-09-12 — полное описание в TASK-0003.058 на указанном коммите; исходник не изменён. [Протокол TASK-0003.058](../../../../review-log.md#task-0003058) фиксирует доказательства и пределы проверки.
