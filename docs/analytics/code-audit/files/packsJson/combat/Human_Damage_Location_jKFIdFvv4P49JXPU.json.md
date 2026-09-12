# packsJson/combat/Human_Damage_Location_jKFIdFvv4P49JXPU.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/combat/Human_Damage_Location_jKFIdFvv4P49JXPU.json](../../../../../../packsJson/combat/Human_Damage_Location_jKFIdFvv4P49JXPU.json) |
| Тип файла | JSON: экспорт RollTable; 6 TableResult (6 text, 0 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 8573642b0136f80b8ae3456de51e1b7f637ec7f3 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.057](../../../../../tasks/task-0003.057.md); 11 файлов / 1915 строк; этот файл — 174 строк |
| Запись перекрёстной сверки | [TASK-0003.057](../../../review-log.md#task-0003057) |
| SHA-256 файла | 02a2ac73ab37bdfe70e8f7c1374a0eb7590cb4f5773dcdbf637e73c5b6dc9300 |

## Назначение файла

Ручной выбор локации попадания по человеку и показ справочных множителей. Имя документа — `Human Damage Location`. Собственных функций, классов JS или обработчиков Actor в JSON нет.

## Условия использования

[system.json](../../../../../../system.json):24–29,45–50 регистрирует Combat как RollTable, путь packs/combat.db, папка Witcher TRPG System. UUID — `Compendium.TheWitcherTRPG.Combat.RollTable.jKFIdFvv4P49JXPU`. Соседний criticalWounds — отдельный пакет типа Item.

[utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт каталог packsJson/combat в compilePack с recursive:true; [utils/extract.mjs](../../../../../../utils/extract.mjs):18–30 выполняет обратное извлечение. [package.json](../../../../../../package.json):7–8 задаёт команды; [подробный контракт CLI](../../utils/packs.mjs.md). Сборка и извлечение не запускались; экспорт не доказывает совпадения с установленной БД.

Ручной вызов — лист RollTable либо действие каталога Foundry. Обычная content-link открывает лист; бросок запускает отдельное действие. Поведение модулей better-rolltables/scene-packer, права реального пользователя и сетевой доступ не проверены.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия |
| --- | --- | --- |
| name / _id / _key | `Human Damage Location` / `jKFIdFvv4P49JXPU` / `!tables!jKFIdFvv4P49JXPU` | Название, ID и служебный ключ таблицы |
| results | 6 записей ниже | Вложенные TableResult, локальные ID уникальны у родителя |
| formula / replacement / displayRoll | `1d10` / true / true | Выбор всех подходящих диапазонов, повторение, показ основного броска |
| description | Пустая строка | Дополнительного корневого описания нет |
| img | `https://assets.forge-vtt.com/bazaar/core/icons/environment/people/commoner.webp` | Иконка таблицы |
| flags | `{"better-rolltables":{},"core":{},"scene-packer":{"sourceId":"Compendium.wtrpg-compendium.combat.RollTable.r88I3ET0y4hkZPTT","hash":"f99f2f2e59b8b388cbf22f1e6cd799f1b23e3d16"}}` | Данные сторонних пространств; sourceId/hash не являются целью рекурсивного roll |
| ownership | `{"default":0,"c4glZubSgyUNSkxe":3,"JEflPFTBB5wpYRms":3,"dxC9PYhanWf4xPZG":3}` | Экспортированные уровни доступа, не доказательство состава пользователей мира |
| folder / sort | null / 0 | Размещение документа |
| _stats | `{"systemId":"TheWitcherTRPG","systemVersion":"0.107","coreVersion":"13.351","compendiumSource":null,"duplicateSource":null,"exportSource":null}` | Происхождение данных; версия экспорта отличается от проверенного ядра |
| Result type / name / description / documentUuid | text; name пустое, description заполнено, documentUuid отсутствует | Текст либо ссылка на документ |
| Result _id / _key | ID ниже; `!tables.results!jKFIdFvv4P49JXPU.<id>` | ID имеет смысл вместе с родителем; повтор между таблицами допустим |
| Result range / weight / drawn | Диапазоны ниже; 1 / false | Выбираются все совпадения, веса не заменяют диапазоны при обычном roll |
| Result img / flags | `https://assets.forge-vtt.com/bazaar/core/icons/svg/d20-black.svg` / {} | Все результаты этого файла имеют одинаковую иконку и пустые flags |
| Result _stats | `{"coreVersion":"13.351","systemId":null,"systemVersion":null,"compendiumSource":null,"duplicateSource":null,"exportSource":null}` | Служебные поля всех результатов одинаковы |

Корневая иконка — внешний URL assets.forge-vtt.com. Все 6 иконок результатов — внешние URL Forge. HTTP не выполнялся, их доступность не установлена. Абсолютный URL black.svg не равен стандартному CONFIG.RollTable.resultIcon=icons/svg/d20-black.svg, поэтому обычная подстановка иконки корня при выводе не срабатывает.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `RHNQnlcfgi5i1isk` | [1,1] | text | `Hit location - Head: Penalty to ATK (if aimed) = -6 \| DMG = x3` | 14–36 |
| 2 | `nGvEbuComhjRZAPP` | [2,4] | text | `Hit location - Torso: Penalty to ATK (if aimed) = -1 \| DMG = x1` | 37–59 |
| 3 | `bmm5fg7mdHPOmQ3G` | [5,5] | text | `Hit location - R. Arm: Penalty to ATK (if aimed) = -3 \| DMG = x1/2` | 60–82 |
| 4 | `3K1jam0ISPD3EKNg` | [6,6] | text | `Hit location - L. Arm: Penalty to ATK (if aimed) = -3 \| DMG = x1/2` | 83–105 |
| 5 | `BMvFuST8XAzAv26J` | [7,8] | text | `Hit location - R. Leg: Penalty to ATK (if aimed) = -2 \| DMG = x1/2` | 106–128 |
| 6 | `BBam5islqax05Zea` | [9,10] | text | `Hit location - L. Leg: Penalty to ATK (if aimed) = -2 \| DMG = x1/2` | 129–151 |

При 1 возвращается Head, при 2–4 Torso, при 5 R. Arm, при 6 L. Arm, при 7–8 R. Leg, при 9–10 L. Leg. Значения Penalty to ATK и DMG — текст. WitcherActor.getLocationObject('randomHuman') использует свой switch и getRandomInt(10); все 10 ветвей проверены отдельно. Сходство распределения не создаёт вызов RollTable и не передаёт её текст в damage.location.

При обычном независимом броске число подходящих исходов каждой записи следующее. Для 2d6 перечислены все 36 упорядоченных пар, а не равновероятные суммы; для 1dN — все N граней.

| № | resultId | Число исходов / всего |
| --- | --- | --- |
| 1 | `RHNQnlcfgi5i1isk` | 1/10 |
| 2 | `nGvEbuComhjRZAPP` | 3/10 |
| 3 | `bmm5fg7mdHPOmQ3G` | 1/10 |
| 4 | `3K1jam0ISPD3EKNg` | 1/10 |
| 5 | `BMvFuST8XAzAv26J` | 2/10 |
| 6 | `BBam5islqax05Zea` | 2/10 |

Все естественные исходы покрыты; при каждой сумме выбирается одна запись. При normalize({save:false}) ядро строит копию с formula=1d6 и последовательными единичными диапазонами. Обычный roll не нормализует этот экспорт, поскольку formula уже задана. Нормализация меняет распределение и не выполнялась с сохранением.

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
| Полный файл и структура | Все 174 строки, 6 результатов, flags/stats/keys/иконки | Строгие модели Foundry приняли файл, поля и IDs описаны | Не чтение БД |
| Выбор по формуле | 10 управляемых исходов настоящего Roll; для 2d6 все пары | Частоты выше; границы и все записи учтены | RNG управляемый, статистика генератора не измерялась |
| roll / draw / повтор | Рекурсивный и прямой вызов; два draw без чата для каждого исхода; два draw мировой копии | Массивы проверены; replacement сохраняет drawn=false; записи БД нет | UUID/index и persistence представлены фасадами |
| HTML / inline | Каждый result.getHTML, toMessage на каждой естественной сумме, реальные HBS | Формулы и text/link перечислены; общий прогон всех шести пакетов: 995 HTML, 51 вставка | Минимальный DOM/обход текстовых узлов, Roll.render — фасад |
| Прямые и обратные связи | Все 128 таблиц и индексные поля criticalWounds; module/templates, манифест и инструменты | Всего 254 documentUuid: 252 разрешимых и 2 отсутствующих у Mounted Control Loss | Сторонние модули и мир не исследованы |
| Игровой маршрут | Исходные getLocationObject, handleCritLocation, applyCritWound и checkIfItemHasRollTable | Независимость Combat от выборки Item и ограничения генератора добычи подтверждены | Модели Item/Actor и запись заменены индексом из экспорта и фасадами |

Полный протокол объединяет 5223 утверждения в сценарии моделей/бросков/HTML и 74 утверждения в сценарии системных потребителей. Результаты предыдущих порций не считаются выполненными повторно, кроме явно перечисленной общей сверки всех RollTable.

## Непроверенные участки и открытые вопросы

Содержимое установленного packs/, миграции и запись мира, HTTP, визуальное отображение и реальные клики, действие внешних модулей не проверены. Имена и штрафы не сверялись с рулбуками. Сохраняемые flags scene-packer не исполнялись. Проверены все строки исходного файла; отсутствие специального потребителя утверждается только для прочитанного дерева и поиска точных ссылок.

Четыре будущие порции .058–.061 должны проверить 94 Item criticalWound и четыре Folder целиком. Здесь их поля использованы точечно для проверки границы с движком; это не завершённый аудит этих 98 файлов.

## Связанные проблемы

[issue-00039](../../../../../issues/potential/issue-00039.md): условный поиск таблицы по имени Item; формат результатов Combat не является генератором Item.

Общие риски extract/compile описаны в [issue-00313](../../../../../issues/potential/issue-00313.md), [issue-00314](../../../../../issues/potential/issue-00314.md), [issue-00315](../../../../../issues/potential/issue-00315.md); повторно не воспроизводились, конкретный JSON ими не объявлен повреждённым. Регистрация наблюдений не означает подтверждения или разрешения исправления.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-12 | 8573642b0136f80b8ae3456de51e1b7f637ec7f3; весь исходник, все результаты, определения и потребители | Первая полная карточка; [TASK-0003.057](../../../review-log.md#task-0003057) |
