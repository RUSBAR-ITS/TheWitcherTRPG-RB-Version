# packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Are_They_Alive__2l9nl4ndvdgtn2SJ.json

## Текущий срез — 14.3.1.00016

| Поле | Значение |
| --- | --- |
| Источник | [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Are_They_Alive__2l9nl4ndvdgtn2SJ.json](../../../../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Are_They_Alive__2l9nl4ndvdgtn2SJ.json) |
| Проверено | 2026-09-16; `dev`; база `095395276b97f0ffe916495e26be3938cf8fdcf8` + исправление [issue-00331 / К01](../../../../../issues/closed/issue-00331.md) |
| Тип / назначение | Экспорт RollTable для выдачи текстов и переходов к дочерним таблицам |
| Имя / ID | Witcher Lifepath: Allies - Are They Alive? / `2l9nl4ndvdgtn2SJ` |
| Строк / SHA-256 | 100 / `c1ee4dab8ec6767b553bf0a02b211be4774a84247f763a952167b0f4ba08e795` |

### Выполненные исправления

B10: один inline-бросок срока смерти в мёртвой ветви. Остальные поля сохранены. Текущие значения и связи перечислены ниже; архив в конце описывает прежние срезы.

`formula=1d100`, `replacement=true`, `displayRoll=false`. 3 TableResult: 2 text и 1 document. Совпадающие диапазоны выбираются совместно; дочерняя таблица бросается отдельно.

| ID / строка _id | range | Тип | Текст результата / цель |
| --- | --- | --- | --- |
| `ciSfEh9nn9LIoeuR` / 11 | [1,30] | text | The ally that you made in this decade is dead. They died [[1d10]] decades after you met. |
| `WeN79l7ug6yDM7Qf` / 34 | [1,30] | document | [Witcher Lifepath: Allies - How Did They Die](../../../../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json) — `Compendium.TheWitcherTRPG-RB-Version.Witcher_Lifepath_and_BG_Sub-tables.RollTable.AMYeAxAXD3DMX6St` |
| `Gl1XVUlHbuQVyANO` / 58 | [31,100] | text | The ally that you made in this decade is still alive (Any living friend you’ve known for more than eight decades is either an elderfolk or a mage). |

### Действия и зависимости

[system.json](../../../../../../system.json) объявляет библиотеку; [utils/packs.mjs](../../../../../../utils/packs.mjs) и [utils/extract.mjs](../../../../../../utils/extract.mjs) передают данные compilePack/extractPack. В .00016 сборка выполнена во временном каталоге отдельным проверочным запуском CLI; действующая БД не заменялась.

Собственных функций у JSON нет. Foundry `RollTable.getResultsForRoll` читает range/drawn, `roll` раскрывает перечисленные documentUuid через fromUuid, `draw/toMessage` передаёт результаты в чат; `TableResult.getHTML` обогащает текст и inline-формулы. `normalize` может изменить распределение по weight; нормализация в это исправление не входит. Выданный текст не создаёт Actor/Item и не начисляет бонусы автоматически.

### Проверка и границы

Источник входит в 48 изменённых JSON [issue-00331 / К01](../../../../../issues/closed/issue-00331.md). Все 226 JSON разобраны; 316 documentUuid/followUp разрешимы. Временная сборка шести пакетов и обратное извлечение совпали с исходниками, включая неизменённые документы. Полный клиент Foundry и действующие packs не проверялись; копии уже импортированных документов мира не обновлялись.

Проверки настоящих Roll/методов RollTable и потребителей травм, фасады окружения и нерешённые ограничения 00320/00328/00036 перечислены в issue-00331. Значения Actor и жизненный цикл эффектов этой порцией повторно не проверялись.

## Архив анализа до 14.3.1.00016

**Ниже сохранены датированные доказательства прежнего состояния. Старые числа результатов/эффектов, тексты, ссылки, номера строк и заявления об отсутствии исправлений не описывают текущий JSON. Актуальный срез находится выше.**

<details>
<summary>Предыдущие пофайловые исследования и проверки</summary>

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Are_They_Alive__2l9nl4ndvdgtn2SJ.json](../../../../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Are_They_Alive__2l9nl4ndvdgtn2SJ.json) |
| Тип файла | JSON: экспорт RollTable, 3 TableResult (2 text, 1 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.055](../../../../../tasks/task-0003.055.md); 41 файл / 8708 строк; этот файл — 100 строк |
| Запись перекрёстной сверки | [TASK-0003.055](../../../review-log.md#task-0003055) |
| SHA-256 файла | e2538265cd090eb8623c4bc18e5800ff24bdac98941c08a7c9e4a897e4e7aa7c |

Актуализация [issue-00001](../../../../../issues/closed/issue-00001.md), 2026-09-16: Внутренние UUID направлены на TheWitcherTRPG-RB-Version. ID документов, диапазоны, эффекты и _stats сохранены. Датированные результаты и прежние значения UUID ниже являются историей.

## Назначение файла

Определяет, жив ли союзник; при смерти добавляет бросок причины смерти. Имя документа — `Witcher Lifepath: Allies - Are They Alive?`. Это данные для выборки и вывода описаний, включая явно заданные ссылки и формулы; самостоятельной программы изменения Actor/Item в JSON нет.

## Условия использования

[system.json](../../../../../../system.json):36,71–76 регистрирует RollTable-пакет Witcher_Lifepath_and_BG_Sub-tables в папке Character Generation с путём packs/witcher-lifepath.db. Адрес документа — `Compendium.TheWitcherTRPG-RB-Version.Witcher_Lifepath_and_BG_Sub-tables.RollTable.2l9nl4ndvdgtn2SJ`.

[utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт каталог compilePack с recursive:true; путь и контракт CLI описаны в [карточке утилиты](../../utils/packs.mjs.md). [utils/extract.mjs](../../../../../../utils/extract.mjs) выполняет обратную выгрузку. Эти команды не запускались. Экспорт не является подключаемым ES-модулем и не доказывает содержимое установленной БД.

Таблица может быть запущена штатным листом/каталогом Foundry через draw либо вложенным roll из другого документа. При recursive:true раскрываются все выбранные ссылки на RollTable. Доступы реального пользователя и установленный компедиум здесь не проверены.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Witcher Lifepath: Allies - Are They Alive?`; `2l9nl4ndvdgtn2SJ`; `!tables!2l9nl4ndvdgtn2SJ` | Имя, ID и ключ хранения корневого RollTable |
| results | 3 вложенных документов | Локальные ID уникальны у этого родителя; совпадение ID в другой таблице допустимо |
| formula, replacement, displayRoll | `1d100`, true, false | Формула выбора, повторное использование результатов, скрытый основной бросок в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание ниже | Иконка и самостоятельное описание таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Пустые пространства better-rolltables/core; настроек поведения модуля внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.rm8eePJo6BXuXQSk`; systemId/systemVersion/duplicateSource/exportSource=null | Метаданные происхождения; не ссылка для рекурсивного выбора |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые права и расположение, не проверка доступности службы |
| Result type/name/description/documentUuid | text: пустое name, текст в description; document: имя цели, пустой description, UUID | Отображаемый текст либо ссылка на вложенную таблицу |
| Result _id/_key | ID в перечне; `!tables.results!2l9nl4ndvdgtn2SJ.<resultId>` | Ключи хранения; _key удалён строгой моделью из toObject |
| Result range/weight/drawn | Диапазоны ниже; все weight=1, drawn=false | getResultsForRoll выбирает все подходящие интервалы, normalize использует веса |
| Result img/flags/_stats | Иконки ниже; flags={}; coreVersion=13.341, systemId/systemVersion/compendiumSource/duplicateSource/exportSource=null | Служебные поля всех результатов |

Root description: Пустая строка.

Иконки результатов: `icons/svg/d20-black.svg`, `icons/svg/d20-grey.svg`. Указанные пути найдены в public/icons установленного ядра; HTTP и внешний вид не проверялись. Текст с бонусом не является изменением характеристики: в структуре нет Item, ActiveEffect, effects или changes.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `ciSfEh9nn9LIoeuR` | [1,30] | text | `The ally that you made in this decade is dead.` | 10–32 |
| 2 | `WeN79l7ug6yDM7Qf` | [1,30] | document | `Witcher Lifepath: Allies - How Did They Die` | 33–56 |
| 3 | `Gl1XVUlHbuQVyANO` | [31,100] | text | `The ally that you made in this decade is still alive (Any living friend you’ve known for more than eight decades is either an elderfolk or a mage).` | 57–79 |

При 1–30 выбираются сообщение о смерти и вложенная причина смерти; при 31–100 — только сообщение о жизни. Получается два либо один конечный текст. Возраст персонажа и число прошедших десятилетий не читаются; замечание об elderfolk/mage после восьми десятилетий — текст.

Реальная formula даёт значения 1…100. Для каждого диапазона указана доля граней основного кубика; строки с одинаковым диапазоном выбираются вместе, поэтому это вероятность группы, а не деление между её записями.

| range | Одновременно выбранных записей | Доля граней | Результат |
| --- | --- | --- | --- |
| [1,30] | 2 | 30/100 | text + document |
| [31,100] | 1 | 70/100 | text |

## Основные функции и методы

Собственных функций и методов у JSON нет. Следующие действия определены в Foundry 14.367.0:

| Метод | Вход, действия и результат | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Все drawn=false записи, для которых value входит в range включительно | Порядок сохраняется; границы самой formula здесь не проверяются |
| RollTable.roll({roll, recursive}) | По умолчанию `1d100`; recursive=true раскрывает documentUuid через fromUuid и innerTable.roll | Родительские модификаторы и исходный roll во вложенный вызов не передаются; _depth увеличивается на 1 |
| RollTable.draw({displayChat}) | roll, затем toMessage при displayChat=true | replacement=true позволяет повторный результат; запросов записи drawn при проверке не было |
| RollTable.normalize({save:false}) | Создаёт клон с 1d3 и одиночными диапазонами по 3 единичным весам | Может изменить исходные вероятности и одновременный выбор; у этого экспорта formula задана, автоматическая нормализация в roll не требуется |
| TableResult.getHTML / documentToAnchor | Подготавливает описание и ссылку на документ, использует HBS | Вставки [[…]] исполняются на этапе enrichHTML; текстовые условия не интерпретируются |
| RollTable.toMessage | Description родителя, все конечные результаты и при displayRoll=true HTML основного броска | Здесь displayRoll=false; он не выключает inline и не переносит управление в дочернюю таблицу |

При прямом запуске с _depth=0 граф допускает 1–2 конечных text; максимальная внутренняя глубина — 1. Эти границы получены отдельным обходом всех диапазонов и ссылок; проверки исполнения перебирали каждый основной результат и выбранные вложенные сочетания, не все комбинации графа. Ядро отклоняет _depth>5. Witcher Background Generator даёт максимальную глубину 4, его ветка RandomCharacter — 5; эти входы проверены отдельно.

При отсутствии пересечения диапазонов и возможных значений внешнего roll ядро выдаёт TABLE.NoPossibleResults и пустой результат. Если отдельный бросок попал вне диапазонов, но пересечение существует, ядро перебрасывает, а не обрезает значение. Дополнительная проверка Trials с внешним 1d20 дала сначала 20, затем 10; два вызова генератора случайных чисел, выбрана строка для 10. Все штатные значения формул этой порции покрыты диапазонами.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник / API | Вид связи, место и доказательство |
| --- | --- | --- |
| packs/packFolders | [system.json](../../../../../../system.json) | Регистрация имени, RollTable-типа и пути пакета |
| compilePack / extractPack | [utils/packs.mjs](../../../../../../utils/packs.mjs); [utils/extract.mjs](../../../../../../utils/extract.mjs); [package.json](../../../../../../package.json) | Подготовка и извлечение JSON; только чтение контрактов и прежних карточек |
| BaseRollTable / BaseTableResult.defineSchema / EmbeddedCollection | Foundry common/documents/roll-table.mjs:43–62; table-result.mjs:48–68; common/abstract/embedded-collection.mjs | Реальные строгие модели приняли документ и все results, включая отрицательные range |
| Roll / RollParser / Die | Foundry client/dice/roll.mjs; parser.mjs; terms/die.mjs; grammar.pegjs | Парсер и вычисления выполнялись настоящим ядром, RNG управляемый |
| roll / draw / getResultsForRoll / parseUuid / fromUuid | Foundry client/documents/roll-table.mjs:98–143,264–342; common/utils/helpers.mjs | Разрешение ссылок, выбор по диапазону, предел вложенности; lookup документов в памяти |
| getHTML / documentToAnchor / HBS | Foundry client/documents/table-result.mjs:45–78; templates/sheets/roll-table/result-details.hbs; templates/dice/table-result.hbs | Настоящие методы и шаблоны; anchor документа и ChatMessage.create — фасады |
| TextEditor._enrichInlineRolls / _createInlineRoll / Roll.toAnchor | Foundry client/applications/ux/text-editor.mjs:247–251,718–775; client/dice/roll.mjs:1021–1034 | Настоящие inline-методы и сериализация броска; обход текстовых узлов и DOM-элементы подменены |

Пути Foundry относятся к /opt/foundryvtt и не включены в файловый реестр системы.

Исходящие ссылки — каждая запись, включая повторный адрес, показана отдельно:

| ID результата / range | Полный documentUuid | Файл цели | Обращение и проверка |
| --- | --- | --- | --- |
| `WeN79l7ug6yDM7Qf`; [1,30] | `Compendium.TheWitcherTRPG-RB-Version.Witcher_Lifepath_and_BG_Sub-tables.RollTable.AMYeAxAXD3DMX6St` | [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json](../../../../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json); [карточка](../witcher-lifepath/Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json.md) | documentUuid:53; имя совпало с целью; recursive:true → innerTable.roll |

Inline-вставок [[…]] нет. Текстовые @UUID/@Compendium, внешние URL и исполняемые макросы в этом файле не найдены. Упоминания людей, предметов, монстров, правил и страниц сами по себе не являются зависимостями на документы.

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Generator_47kWQhpq3yeAG74c.json](../../../../../../packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Generator_47kWQhpq3yeAG74c.json) | `CO3QQZcFp1D2YDGe`; documentUuid:150; range=[1,1] | `Witcher Lifepath: Allies - Generator`: при выборе диапазона и recursive:true вызывает этот документ |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение экспортного каталога для сборки |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Штатное ручное действие вызывает draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Возможное совпадение Item.name с `Witcher Lifepath: Allies - Are They Alive?` | Общий поиск таблицы при экспорте добычи ожидает Item, а этот граф возвращает text |

Прямые входящие documentUuid перечислены полностью по всем 226 экспортам. Поиск пакета, всех 41 ID и имён по module/templates/utils и en/ru не нашёл статических программных вызовов. Совпадение имени в общем поиске WitcherItem остаётся отдельным динамическим случаем; метод прочитан, но с этими 41 именем заново не запускался.

[module/data/actor/templates/character/general/backgroundData.js](../../../../../../module/data/actor/templates/character/general/backgroundData.js):3–6 хранит HTML биографии; [module/data/actor/templates/character/general/lifeEventData.js](../../../../../../module/data/actor/templates/character/general/lifeEventData.js):3–9 — decade/value/details/isOpened. [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs):51–95 редактирует биографию и события, но не вызывает таблицы. Это соседние места ручного хранения сведений, а не найденные автоматические потребители экспортного текста.

[module/data/actor/templates/common/lifepathData.js](../../../../../../module/data/actor/templates/common/lifepathData.js):3–14 задаёт числовые shieldParryBonus, shieldParryThrownBonus, ignoredArmorEncumbrance, ignoredEvWhenCasting и attacks. Эти поля включены в commonActorData.js:59 и используются кодом бросков/брони. Рассматриваемая RollTable не записывает их; само совпадение слова «бонус» в description не устанавливает связь исполнения.

## Данные и изменения состояния

Strict-модель создаётся в памяти из экспорта; _key служит экспорту, но не входит в её toObject. RollTable.roll возвращает Roll и TableResult[], раскрывая ссылки. При recursive=false ссылки остаются документными результатами; при true этот граф заканчивается текстом. Наличие нескольких совпадающих range не требует отдельного режима модуля.

Все результаты имеют drawn=false и replacement=true у родителя. Повторные draw дали доступные результаты без записи статуса; нормализация save:false вернула отдельный клон. При обычном displayChat=true создаётся ChatMessage, и в процессе подготовки HTML могут вычисляться inline-броски. В проверке сообщение перехвачено в памяти, записи мира/БД недоступны.

Actor, Item, ActiveEffect, кошелёк, лечение, возраст и общая биография не изменяются описаниями сами. Повторение «за каждое десятилетие», выбор риска, перенос текста и интерпретация словесных условий остаются внешними действиями.

## Проверки и доказательства

| Что проверено | Источник / сценарий | Фактический результат | Предел |
| --- | --- | --- | --- |
| Все поля и ключи | Python stdin, строгий JSON без повторных ключей; отдельная сверка 41 файла | 321 result, 362 уникальных ключа хранения; этот файл: 3 results | Совпадение с установленной БД не проверено |
| Диапазоны и формулы | Настоящие Roll, RollTable.roll/getResultsForRoll | Все 100 граней этой formula; ожидаемые ID независимо выбраны по raw range; минимум 1, максимум 100 | Не перебраны все комбинации вложенных случайных чисел |
| Вложенные вызовы и повторы | Настоящие roll/draw с фасадом fromUuid | Вся порция: 563 основных значений, 1126 повторных draw без чата, 82 draw моделей без pack | Нет сервера, прав игроков или записи DB |
| Каждый result / вывод | Настоящие TableResult.getHTML, HBS, draw/toMessage | Все 95 document и 226 text, 14 inline; 563 прямых сообщений плюс 8 сообщений внешних Decade-сценариев | enrichHTML использует фасад обхода текста; полный браузерный DOM не проверен |
| Варианты и границы | 30 сценариев возраст × обучение; 15 дополнительных сценариев; ещё 23 проверки внешних roll | Основной запуск: 6683 assertions; отдельный запуск: 23; writes=0 | Числа/тексты рулбуков не сверялись |
| Граф и потребители | Все 226 JSON, system.json, module/templates/utils, en/ru | 94 внутренних ссылки, одна исходящая в lifepath, 18 входящих из пяти Character-gen; все цели найдены | Не исключает внешние макросы, модули и динамические вызовы |
| Сохранность и документы | SHA-256, Git, ссылки, таблицы Markdown; журнал порции | Итог зафиксирован в [сверке](../../../review-log.md#task-0003055) | Метаданные доступа не изменялись |

Первый запуск общего сценария остановился на декодировании URI в проверочном коде чтения Roll.toAnchor.dataset.roll; после исправления фасада сравнения весь сценарий выполнен заново. Это не дефект исходной таблицы и не пропущенная проверка её поведения.

## Непроверенные участки и открытые вопросы

Сверка TASK-0004.017 завершила граф всех 128 RollTable, связи основных генераторов и границу с уже разобранными Item-травмами (.012). Прежние .052–.057/.061 сохраняют даты и фасады.  Остаток: [U017-01](../../../cross-check-0002.md#u017-01), [U017-02](../../../cross-check-0002.md#u017-02), [U017-03](../../../cross-check-0002.md#u017-03); конкретные ответы и границы сведены в [итоге TASK-0004.018](../../../cross-check-0002.md#адресация-126-вопросов-предметных-блоков). Действующие packs/мир, HTTP, полный DOM, пользовательские права и внешние модули/макросы не проверялись. Соответствие контента рулбукам исключено.

## Связанные проблемы

Самостоятельная новая проблема в этом файле не зарегистрирована. Это не подтверждение всего контента или отсутствия ошибок во внешних потребителях.

Общие ограничения вывода и арифметики связанных цепочек — [issue-00319](../../../../../issues/closed/issue-00319.md), [issue-00321](../../../../../issues/closed/issue-00321.md); применимость определяется конкретными ветвями выше. Известная [issue-00320](../../../../../issues/closed/issue-00320.md) про семейные цепочки RandomCharacter не воспроизвелась для проверенного входа ведьмака. [issue-00039](../../../../../issues/closed/issue-00039.md) описывает предположения общего потребителя добычи; [issue-00313](../../../../../issues/potential/issue-00313.md), [issue-00314](../../../../../issues/potential/issue-00314.md), [issue-00315](../../../../../issues/potential/issue-00315.md) — независимые ограничения извлечения. Новые подтверждения, статусы open/closed и исправления не выполнялись.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-12 | cd2743d0548d5c129065c970d4aa5c43cc9632e2; полный файл и перечисленные связи | Первичная карточка по TASK-0003.055; [протокол](../../../review-log.md#task-0003055) |

## Сквозная сверка TASK-0004.017

2026-09-14; rusbar-main, cdb7bcb08835c62eb84efdfe7356c4eec90aa2e8. Исходник совпадает со срезом TASK-0001; изменено только описание.

Witcher Lifepath: Allies - Are They Alive?: 1d100, возможные totals 1…100; 3 результатов (2 text / 1 document), replacement=true, displayRoll=false. Рекурсивные переходы: Witcher Lifepath: Allies - How Did They Die. По разрешимому графу от этого прямого входа 1–2 конечных текстов, максимальная глубина 1; входящих файлов 1. Inline-выражений в результатах нет.

Сопоставленные определения и потребители: [system.json](../../system.json.md), [utils/packs.mjs](../../utils/packs.mjs.md), [utils/extract.mjs](../../utils/extract.mjs.md), [module/item/witcherItem.js](../../module/item/witcherItem.js.md), [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___Generator_47kWQhpq3yeAG74c.json](Witcher_Lifepath__Allies___Generator_47kWQhpq3yeAG74c.json.md), [packsJson/witcher-lifepath/Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json](Witcher_Lifepath__Allies___How_Did_They_Die_AMYeAxAXD3DMX6St.json.md).

[Протокол и границы](../../../review-log.md#task-0004017) — TASK-0004.017; процессы [R017-01](../../../cross-check-0002.md#r017-01), [R017-02](../../../cross-check-0002.md#r017-02), [R017-03](../../../cross-check-0002.md#r017-03), [R017-04](../../../cross-check-0002.md#r017-04), [R017-17](../../../cross-check-0002.md#r017-17). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.

</details>
