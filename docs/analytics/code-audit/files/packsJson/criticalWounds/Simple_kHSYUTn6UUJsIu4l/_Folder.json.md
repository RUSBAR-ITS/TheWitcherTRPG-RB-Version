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

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. 98 JSON и62 followUp проверены; состав установленного packs/ и серверный getIndex не читались. .017 сводит манифест/экспорты/таблицы, включая выбор кандидатов и пустые tailWing. Критерий: источник нужного Item и индексные поля подтверждены отдельно от текста RollTable и предположений по рулбуку. Границы: [U012-02](../../../../cross-check-0002.md#u012-02) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00325](../../../../../../issues/closed/issue-00325.md) — поле локации одного дочернего Item; [issue-00121](../../../../../../issues/potential/issue-00121.md), [issue-00127](../../../../../../issues/potential/issue-00127.md) и [issue-00288](../../../../../../issues/potential/issue-00288.md) — общие потребители. Наличие этих проблем не означает дефекта самой папки.

## История актуализации

2026-09-12 — полное описание в TASK-0003.058 на указанном коммите; исходник не изменён. [Протокол TASK-0003.058](../../../../review-log.md#task-0003058) фиксирует доказательства и пределы проверки.

## Уточнение TASK-0003.059

2026-09-13; rusbar-main, d26e3381a7290807b8e76f9817d0f7a603c0e61a; исходник не изменён.

Соседняя группа Complex проверена полностью: 25 JSON, 24 Item, 16 effects/61 changes, 16 переходов. Общая структурная сверка 50 файлов Simple/Complex сохранила границы папок. В 14 карточках Simple уточнены номера строк корневого _id; сами ID/UUID и исходники не менялись.

[Карточки Complex](../Complex_YcLLKtwU75uE8tdC/_Folder.json.md), [протокол и ограничения](../../../../review-log.md#task-0003059). Мир и БД не изменялись.

## Уточнение TASK-0003.060

2026-09-13; rusbar-main, aef03ca01b0db5887653d2b1301a4fe814372a3e; исходник не изменён.

Завершено чтение соседней Difficult: 25 JSON / 25 effects / 201 changes, в отличие от числовых add Simple/Complex есть multiply и объекты turnStartEffects. Общая область ID/_key criticalWounds проверена, цепочки Difficult не выходят из папки. Прежние сценарии Simple повторно не исполнялись.

[Карточки Difficult](../Difficult_ox3lLmV3zp0K67Ht/_Folder.json.md), [протокол и ограничения](../../../../review-log.md#task-0003060). Мир и БД не менялись.

## Дополнительная сверка TASK-0003.061

2026-09-14; rusbar-main, 1cae095ac2f0f009fb1358a888a7afcf5ea5ec2e. Исходник не изменён.

После [Deadly](../Deadly_uofXQEP6HBtekOAO/_Folder.json.md) завершено чтение всех 98 JSON criticalWounds. Повтор строгих моделей/потребителей охватил 94 Item/4 Folder/79 эффектов/360 changes, 62 перехода и 48 выборов. Статическая сверка подтверждает 31 цепочку из трёх Item плюс конечную Decapitation, без циклов/отсутствующих UUID. Пять смен location относятся к прежним [issue-00325](../../../../../../issues/closed/issue-00325.md)/[issue-00327](../../../../../../issues/closed/issue-00327.md); Complex first-find — [issue-00324](../../../../../../issues/closed/issue-00324.md); единственный disabled относится к Deadly [issue-00329](../../../../../../issues/closed/issue-00329.md). Исторические итоги данной порции сохранены.

[Протокол и ограничения](../../../../review-log.md#task-0003061). Настоящие модели/методы исполнены с явными фасадами окружения и перехватом записи; полный клиентский lifecycle, мир, БД и серверный запуск не проверены.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Folder `kHSYUTn6UUJsIu4l` («Simple») содержит 24 Item, `sorting=m`, `sort=-100000`; собственных effects/changes нет. 98 JSON — 94 Item и 4 Folder, а не таблицы бросков; четыре папки группируют 24/24/24/22 Item. Всего 79 эффектов/360 изменений;31 цепочка из 3 Item плюс конечный none,62 существующих followUp без циклов. Сырые changes мигрируют в system.changes: 32 multiply/328 add; null priority получает 10/20, четыре явных 0 сохраняются. Все transfer=true, единственный disabled в Deadly. Исторический origin не выбирает Actor-получателя; runtime читает документы пакета, не эти JSON напрямую.

Сопоставленные определения и потребители: [system.json](../../../system.json.md), [utils/packs.mjs](../../../utils/packs.mjs.md), [utils/extract.mjs](../../../utils/extract.mjs.md), [module/setup/settings.js](../../../module/setup/settings.js.md), [module/data/item/criticalWoundData.js](../../../module/data/item/criticalWoundData.js.md), [packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/Cracked_Jaw_UnWBI9Sgu4AJv1z1.json](Cracked_Jaw_UnWBI9Sgu4AJv1z1.json.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-09](../../../../cross-check-0002.md#r012-09). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
