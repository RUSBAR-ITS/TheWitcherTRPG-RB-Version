# packsJson/combat/Monster_Damage_Location_KYyK6F8JHhA3hOu7.json

## Текущий срез — 14.3.1.00016

| Поле | Значение |
| --- | --- |
| Источник | [packsJson/combat/Monster_Damage_Location_KYyK6F8JHhA3hOu7.json](../../../../../../packsJson/combat/Monster_Damage_Location_KYyK6F8JHhA3hOu7.json) |
| Проверено | 2026-09-16; `dev`; база `095395276b97f0ffe916495e26be3938cf8fdcf8` + исправление [issue-00331 / К01](../../../../../issues/open/issue-00331.md) |
| Тип / назначение | Экспорт RollTable для выдачи текстов и переходов к дочерним таблицам |
| Имя / ID | Monster Damage Location / `KYyK6F8JHhA3hOu7` |
| Строк / SHA-256 | 151 / `e7b47b997bdaf92df7ed5165c913dff450b5a1b87ae4f33c0f9b8ea2b110740a` |

### Выполненные исправления

B05: три диапазона попаданий по монстру. Остальные поля сохранены. Текущие значения и связи перечислены ниже; архив в конце описывает прежние срезы.

`formula=1d10`, `replacement=true`, `displayRoll=true`. 5 TableResult: 5 text и 0 document. Совпадающие диапазоны выбираются совместно; дочерняя таблица бросается отдельно.

| ID / строка _id | range | Тип | Текст результата / цель |
| --- | --- | --- | --- |
| `RHNQnlcfgi5i1isk` / 15 | [1,1] | text | Hit location - Head: Penalty to ATK (if aimed) = -6 &#124; DMG = x3 |
| `nGvEbuComhjRZAPP` / 38 | [2,4] | text | Hit location - Torso: Penalty to ATK (if aimed) = -1 &#124; DMG = x1 |
| `bmm5fg7mdHPOmQ3G` / 61 | [5,7] | text | Hit location - R. Limb: Penalty to ATK (if aimed) = -3 &#124; DMG = x1/2 |
| `3K1jam0ISPD3EKNg` / 84 | [8,9] | text | Hit location - L. Limb: Penalty to ATK (if aimed) = -3 &#124; DMG = x1/2 |
| `BBam5islqax05Zea` / 107 | [10,10] | text | Hit location - Tail or Wing: Penalty to ATK (if aimed) = -2 &#124; DMG = x1/2 |

### Действия и зависимости

[system.json](../../../../../../system.json) объявляет библиотеку; [utils/packs.mjs](../../../../../../utils/packs.mjs) и [utils/extract.mjs](../../../../../../utils/extract.mjs) передают данные compilePack/extractPack. В .00016 сборка выполнена во временном каталоге отдельным проверочным запуском CLI; действующая БД не заменялась.

Собственных функций у JSON нет. Foundry `RollTable.getResultsForRoll` читает range/drawn, `roll` раскрывает перечисленные documentUuid через fromUuid, `draw/toMessage` передаёт результаты в чат; `TableResult.getHTML` обогащает текст и inline-формулы. `normalize` может изменить распределение по weight; нормализация в это исправление не входит. Выданный текст не создаёт Actor/Item и не начисляет бонусы автоматически.

### Проверка и границы

Источник входит в 48 изменённых JSON [issue-00331 / К01](../../../../../issues/open/issue-00331.md). Все 226 JSON разобраны; 316 documentUuid/followUp разрешимы. Временная сборка шести пакетов и обратное извлечение совпали с исходниками, включая неизменённые документы. Полный клиент Foundry и действующие packs не проверялись; копии уже импортированных документов мира не обновлялись.

Проверки настоящих Roll/методов RollTable и потребителей травм, фасады окружения и нерешённые ограничения 00320/00328/00036 перечислены в issue-00331. Значения Actor и жизненный цикл эффектов этой порцией повторно не проверялись.

## Архив анализа до 14.3.1.00016

**Ниже сохранены датированные доказательства прежнего состояния. Старые числа результатов/эффектов, тексты, ссылки, номера строк и заявления об отсутствии исправлений не описывают текущий JSON. Актуальный срез находится выше.**

<details>
<summary>Предыдущие пофайловые исследования и проверки</summary>

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/combat/Monster_Damage_Location_KYyK6F8JHhA3hOu7.json](../../../../../../packsJson/combat/Monster_Damage_Location_KYyK6F8JHhA3hOu7.json) |
| Тип файла | JSON: экспорт RollTable; 5 TableResult (5 text, 0 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 8573642b0136f80b8ae3456de51e1b7f637ec7f3 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.057](../../../../../tasks/task-0003.057.md); 11 файлов / 1915 строк; этот файл — 151 строк |
| Запись перекрёстной сверки | [TASK-0003.057](../../../review-log.md#task-0003057) |
| SHA-256 файла | effe7fc2618c0e7989baba91ff6161b3d1f460d6ee9f02a41367019259675588 |

## Назначение файла

Ручной выбор локации попадания по монстру; два результата при сумме 9. Имя документа — `Monster Damage Location`. Собственных функций, классов JS или обработчиков Actor в JSON нет.

## Условия использования

[system.json](../../../../../../system.json):24–29,45–50 регистрирует Combat как RollTable, путь packs/combat.db, папка Witcher TRPG System. UUID — `Compendium.TheWitcherTRPG.Combat.RollTable.KYyK6F8JHhA3hOu7`. Соседний criticalWounds — отдельный пакет типа Item.

[utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт каталог packsJson/combat в compilePack с recursive:true; [utils/extract.mjs](../../../../../../utils/extract.mjs):18–30 выполняет обратное извлечение. [package.json](../../../../../../package.json):7–8 задаёт команды; [подробный контракт CLI](../../utils/packs.mjs.md). Сборка и извлечение не запускались; экспорт не доказывает совпадения с установленной БД.

Ручной вызов — лист RollTable либо действие каталога Foundry. Обычная content-link открывает лист; бросок запускает отдельное действие. Поведение модулей better-rolltables/scene-packer, права реального пользователя и сетевой доступ не проверены.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия |
| --- | --- | --- |
| name / _id / _key | `Monster Damage Location` / `KYyK6F8JHhA3hOu7` / `!tables!KYyK6F8JHhA3hOu7` | Название, ID и служебный ключ таблицы |
| results | 5 записей ниже | Вложенные TableResult, локальные ID уникальны у родителя |
| formula / replacement / displayRoll | `1d10` / true / true | Выбор всех подходящих диапазонов, повторение, показ основного броска |
| description | Пустая строка | Дополнительного корневого описания нет |
| img | `https://assets.forge-vtt.com/bazaar/core/icons/creatures/abilities/wing-batlike-purple-blue.webp` | Иконка таблицы |
| flags | `{"better-rolltables":{},"core":{},"scene-packer":{"sourceId":"Compendium.wtrpg-compendium.combat.RollTable.zegIE2vBQYvPOcET","hash":"955608d6069ba75501b427b6d1588ac9e7f9d337"}}` | Данные сторонних пространств; sourceId/hash не являются целью рекурсивного roll |
| ownership | `{"default":0,"c4glZubSgyUNSkxe":3,"JEflPFTBB5wpYRms":3,"dxC9PYhanWf4xPZG":3}` | Экспортированные уровни доступа, не доказательство состава пользователей мира |
| folder / sort | null / 0 | Размещение документа |
| _stats | `{"systemId":"TheWitcherTRPG","systemVersion":"0.107","coreVersion":"13.351","compendiumSource":null,"duplicateSource":null,"exportSource":null}` | Происхождение данных; версия экспорта отличается от проверенного ядра |
| Result type / name / description / documentUuid | text; name пустое, description заполнено, documentUuid отсутствует | Текст либо ссылка на документ |
| Result _id / _key | ID ниже; `!tables.results!KYyK6F8JHhA3hOu7.<id>` | ID имеет смысл вместе с родителем; повтор между таблицами допустим |
| Result range / weight / drawn | Диапазоны ниже; 1 / false | Выбираются все совпадения, веса не заменяют диапазоны при обычном roll |
| Result img / flags | `https://assets.forge-vtt.com/bazaar/core/icons/svg/d20-black.svg` / {} | Все результаты этого файла имеют одинаковую иконку и пустые flags |
| Result _stats | `{"coreVersion":"13.351","systemId":null,"systemVersion":null,"compendiumSource":null,"duplicateSource":null,"exportSource":null}` | Служебные поля всех результатов одинаковы |

Корневая иконка — внешний URL assets.forge-vtt.com. Все 5 иконок результатов — внешние URL Forge. HTTP не выполнялся, их доступность не установлена. Абсолютный URL black.svg не равен стандартному CONFIG.RollTable.resultIcon=icons/svg/d20-black.svg, поэтому обычная подстановка иконки корня при выводе не срабатывает.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `RHNQnlcfgi5i1isk` | [1,1] | text | `Hit location - Head: Penalty to ATK (if aimed) = -6 \| DMG = x3` | 14–36 |
| 2 | `nGvEbuComhjRZAPP` | [2,5] | text | `Hit location - Torso: Penalty to ATK (if aimed) = -1 \| DMG = x1` | 37–59 |
| 3 | `bmm5fg7mdHPOmQ3G` | [6,7] | text | `Hit location - R. Limb: Penalty to ATK (if aimed) = -3 \| DMG = x1/2` | 60–82 |
| 4 | `3K1jam0ISPD3EKNg` | [8,9] | text | `Hit location - L. Limb: Penalty to ATK (if aimed) = -3 \| DMG = x1/2` | 83–105 |
| 5 | `BBam5islqax05Zea` | [9,10] | text | `Hit location - Tail or Wing: Penalty to ATK (if aimed) = -2 \| DMG = x1/2` | 106–128 |

При 9 одновременно подходят 3K1jam0ISPD3EKNg [8,9] (L. Limb) и BBam5islqax05Zea [9,10] (Tail or Wing). Настоящие getResultsForRoll/roll/draw возвращают обе записи, чат показывает обе. Встроенный getLocationObject('randomMonster') при 9 выдаёт один leftLeg, при 10 — tailWing; этот switch не читает JSON. Наблюдение issue-00322 относится к одновременному выбору справочных локаций, а не к исправлению правил распределения.

При обычном независимом броске число подходящих исходов каждой записи следующее. Для 2d6 перечислены все 36 упорядоченных пар, а не равновероятные суммы; для 1dN — все N граней.

| № | resultId | Число исходов / всего |
| --- | --- | --- |
| 1 | `RHNQnlcfgi5i1isk` | 1/10 |
| 2 | `nGvEbuComhjRZAPP` | 4/10 |
| 3 | `bmm5fg7mdHPOmQ3G` | 2/10 |
| 4 | `3K1jam0ISPD3EKNg` | 2/10 |
| 5 | `BBam5islqax05Zea` | 2/10 |

Сумма частот равна 11/10: это не распределение взаимоисключающих событий, поскольку при 9 выбираются две записи. При normalize({save:false}) ядро строит копию с formula=1d5 и последовательными единичными диапазонами. Обычный roll не нормализует этот экспорт, поскольку formula уже задана. Нормализация меняет распределение и не выполнялась с сохранением.

Inline-вставок [[…]] нет; текстовые указания бросить кубик не вычисляются.

## Основные функции и методы

Собственных методов нет. Ниже указаны реальные внешние обработчики, которым принадлежат действия.

| Метод / владелец | Действие и проверенное место |
| --- | --- |
| BaseRollTable / BaseTableResult, common/documents/roll-table.mjs и table-result.mjs | Схема и строгая загрузка 11 таблиц / 66 результатов; _key не входит в подготовленную модель |
| RollTable.roll / getResultsForRoll, client/documents/roll-table.mjs:264–341 | Проверка доступного диапазона, настоящий Roll, все inclusive-совпадения, рекурсивный fromUuid |
| RollTable.draw, тот же файл:98–143 | При пустом результате ранний возврат без чата; иначе правила drawn и вызов toMessage |
| RollTable.toMessage, тот же файл:49–82 | getHTML всех результатов через allSettled, шаблон, основной бросок и ChatMessage |
| RollTable.normalize, тот же файл:213–230 | Перестройка диапазонов по весам; save:false возвращает отдельный документ |
| TableResult.getHTML / documentToAnchor, client/documents/table-result.mjs:45–78 | Описание и документная ссылка; наличие anchor не подтверждает существование цели |
| TextEditor._enrichInlineRolls / _createInlineRoll, client/applications/ux/text-editor.mjs:247–251,718–775 | [[…]] без команды вычисляется при показе; условия естественного языка не выполняются |
| Roll / Die, client/dice/roll.mjs и terms/die.mjs:136–170 | Формула, арифметика и explode; Roll.toAnchor:1021–1034 сериализует вычисленный total |
| RollTableSheet.#onDrawResult, client/applications/sheets/roll-table-sheet.mjs:428–440 | Кнопка вызывает roll, затем draw; полный браузер в этой порции не запускался |

Пути ядра относительно /opt/foundryvtt; фактически проверена Foundry 14.367.0, Node.js 24.16.0. Отдельные редакторы и стандартный клик описаны с выполненной ранее проверкой [TASK-0003.056](../../../review-log.md#task-0003056); текущий прогон относится к моделям, броскам и HTML.

## Используемые сущности и зависимости

documentUuid и текстовых @UUID/@Compendium-ссылок в этом файле нет.

| Источник определения | Используемая сущность | Вид связи и доказательство |
| --- | --- | --- |
| [system.json](../../system.json.md) | packs / packFolders, Combat | Регистрация типа, пути и пространства UUID; прямой runtime-импорт отсутствует |
| [utils/packs.mjs](../../utils/packs.mjs.md), [utils/extract.mjs](../../utils/extract.mjs.md) | compilePack / extractPack | Инструменты экспорта и сборки, чтение контрактов без выполнения записи |
| Ядро Foundry, файлы из таблицы методов | RollTable, TableResult, Roll, Die, TextEditor, ChatMessage | Фактические загрузчик/исполнители; не определения JSON |
| Foundry templates/sheets/roll-table/result-details.hbs и templates/dice/table-result.hbs | name, description, documentLink, rollHTML, results | Реальные HBS исполнены с фасадами клиента |
| Forge URL из img | SVG/WebP | Внешняя зависимость показа иконок; сеть не проверена |

[module/actor/witcherActor.js](../../module/actor/witcherActor.js.md):302–435 и [module/actor/mixins/locationMixin.js](../../module/actor/mixins/locationMixin.js.md):4–9 определяют независимый маршрут случайной локации.

## Известные потребители

| Файл-потребитель | Сущность этого файла | Способ и условия | Доказательство |
| --- | --- | --- | --- |
| utils/packs.mjs | Весь экспорт | Обход packsJson и recursive compilePack | Статическое чтение:6–10 |
| Ядро Foundry RollTableSheet / RollTableDirectory | RollTable-документ | Ручной бросок либо открытие листа | roll-table-sheet.mjs:428–440; sidebar/tabs/roll-table-directory.mjs:28–33; обычный клик text-editor.mjs:792–795 |
| [module/item/witcherItem.js](../../module/item/witcherItem.js.md) | Точное name таблицы | checkIfItemHasRollTable ищет по Item.name среди всех RollTable-пакетов | :257–315; отдельный вызов с этим именем и реальным roll/TableResult получил exportLootInvalidItemError, поскольку результат текстовый |

Среди всех 128 RollTable-экспортов нет разрешимых входящих documentUuid на этот документ; среди 98 файлов criticalWounds и module/templates не найдено точных ссылок на его ID, имя или UUID. Поиск по точным значениям не исключает произвольный макрос, динамический запрос по имени или сторонний модуль. Не устанавливалось наличие совпадающего Item в действующем мире.

## Данные и изменения состояния

roll вычисляет результат в памяти и не применяет текст к характеристикам, HP, состояниям, предметам, позиции или токену. Вставки [[…]] вычисляются только при обогащении описания. draw при replacement=true сохраняет доступность результатов; это проверено как для документа pack, так и для изолированной мировой копии. Реальный непустой draw создаёт ChatMessage; в проверке создание перехвачено в памяти. Пустой draw до toMessage не доходит.

Результаты источника и prepared-документы после проверки не изменились. Нормализация вызвана только с save:false. Настоящий Item-потребитель травм отдельно вызывает addItem и ChatMessage, но не получает эти данные из Combat.

## Проверки и доказательства

| Проверка | Сценарий / источник | Результат | Предел |
| --- | --- | --- | --- |
| Полный файл и структура | Все 151 строки, 5 результатов, flags/stats/keys/иконки | Строгие модели Foundry приняли файл, поля и IDs описаны | Не чтение БД |
| Выбор по формуле | 10 управляемых исходов настоящего Roll; для 2d6 все пары | Частоты выше; границы и все записи учтены | RNG управляемый, статистика генератора не измерялась |
| roll / draw / повтор | Рекурсивный и прямой вызов; два draw без чата для каждого исхода; два draw мировой копии | Массивы проверены; replacement сохраняет drawn=false; записи БД нет | UUID/index и persistence представлены фасадами |
| HTML / inline | Каждый result.getHTML, toMessage на каждой естественной сумме, реальные HBS | Формулы и text/link перечислены; общий прогон всех шести пакетов: 995 HTML, 51 вставка | Минимальный DOM/обход текстовых узлов, Roll.render — фасад |
| Прямые и обратные связи | Все 128 таблиц и индексные поля criticalWounds; module/templates, манифест и инструменты | Всего 254 documentUuid: 252 разрешимых и 2 отсутствующих у Mounted Control Loss | Сторонние модули и мир не исследованы |
| Игровой маршрут | Исходные getLocationObject, handleCritLocation, applyCritWound и checkIfItemHasRollTable | Независимость Combat от выборки Item и ограничения генератора добычи подтверждены | Модели Item/Actor и запись заменены индексом из экспорта и фасадами |

Полный протокол объединяет 5223 утверждения в сценарии моделей/бросков/HTML и 74 утверждения в сценарии системных потребителей. Результаты предыдущих порций не считаются выполненными повторно, кроме явно перечисленной общей сверки всех RollTable.

## Непроверенные участки и открытые вопросы

Сверка TASK-0004.017 завершила граф всех 128 RollTable, связи основных генераторов и границу с уже разобранными Item-травмами (.012). Прежние .052–.057/.061 сохраняют даты и фасады. На total=9 выбраны два результата (00322); Actor.randomMonster использует свой switch и возвращает leftLeg. Остаток: [U017-01](../../../cross-check-0002.md#u017-01), [U017-02](../../../cross-check-0002.md#u017-02), [U017-08](../../../cross-check-0002.md#u017-08); конкретные ответы и границы сведены в [итоге TASK-0004.018](../../../cross-check-0002.md#адресация-126-вопросов-предметных-блоков). Действующие packs/мир, HTTP, полный DOM, пользовательские права и внешние модули/макросы не проверялись. Соответствие контента рулбукам исключено.

## Связанные проблемы

[issue-00039](../../../../../issues/potential/issue-00039.md): условный поиск таблицы по имени Item; формат результатов Combat не является генератором Item.

[issue-00322](../../../../../issues/potential/issue-00322.md): пересечение диапазонов при 9.

Общие риски extract/compile описаны в [issue-00313](../../../../../issues/potential/issue-00313.md), [issue-00314](../../../../../issues/potential/issue-00314.md), [issue-00315](../../../../../issues/potential/issue-00315.md); повторно не воспроизводились, конкретный JSON ими не объявлен повреждённым. Регистрация наблюдений не означает подтверждения или разрешения исправления.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-12 | 8573642b0136f80b8ae3456de51e1b7f637ec7f3; весь исходник, все результаты, определения и потребители | Первая полная карточка; [TASK-0003.057](../../../review-log.md#task-0003057) |

## Сквозная сверка TASK-0004.017

2026-09-14; rusbar-main, cdb7bcb08835c62eb84efdfe7356c4eec90aa2e8. Исходник совпадает со срезом TASK-0001; изменено только описание.

Monster Damage Location: 1d10, возможные totals 1…10; 5 результатов (5 text / 0 document), replacement=true, displayRoll=true. Листовая выдача текста без documentUuid. По разрешимому графу от этого прямого входа 1–2 конечных текстов, максимальная глубина 0; входящих файлов 0. Inline-выражений в результатах нет.  На total=9 выбраны два результата (00322); Actor.randomMonster использует свой switch и возвращает leftLeg.

Сопоставленные определения и потребители: [system.json](../../system.json.md), [utils/packs.mjs](../../utils/packs.mjs.md), [utils/extract.mjs](../../utils/extract.mjs.md), [module/item/witcherItem.js](../../module/item/witcherItem.js.md), [module/actor/witcherActor.js](../../module/actor/witcherActor.js.md), [module/actor/mixins/locationMixin.js](../../module/actor/mixins/locationMixin.js.md).

[Протокол и границы](../../../review-log.md#task-0004017) — TASK-0004.017; процессы [R017-01](../../../cross-check-0002.md#r017-01), [R017-02](../../../cross-check-0002.md#r017-02), [R017-03](../../../cross-check-0002.md#r017-03), [R017-04](../../../cross-check-0002.md#r017-04), [R017-21](../../../cross-check-0002.md#r017-21). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.

</details>
