# packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json) |
| Тип файла | JSON: экспорт RollTable, 8 TableResult (4 text, 4 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, cd2743d0548d5c129065c970d4aa5c43cc9632e2 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.055](../../../../../tasks/task-0003.055.md); 41 файл / 8708 строк; этот файл — 218 строк |
| Запись перекрёстной сверки | [TASK-0003.055](../../../review-log.md#task-0003055) |
| SHA-256 файла | bf93b6e37871b13063100f1ed688bb5eb3f273f90f5f7fc849834944a19d7e1a |

## Назначение файла

Испытания ведьмака с формулой 1d10+4; выводит результат мутаций и продолжает важным событием. Имя документа — `Witcher Background: How Did Your Trials Go? +4`. Это данные для выборки и вывода описаний, включая явно заданные ссылки и формулы; самостоятельной программы изменения Actor/Item в JSON нет.

## Условия использования

[system.json](../../../../../../system.json):36,71–76 регистрирует RollTable-пакет Witcher_Lifepath_and_BG_Sub-tables в папке Character Generation с путём packs/witcher-lifepath.db. Адрес документа — `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.GknRX1nkVVcc9rCK`.

[utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт каталог compilePack с recursive:true; путь и контракт CLI описаны в [карточке утилиты](../../utils/packs.mjs.md). [utils/extract.mjs](../../../../../../utils/extract.mjs) выполняет обратную выгрузку. Эти команды не запускались. Экспорт не является подключаемым ES-модулем и не доказывает содержимое установленной БД.

Таблица может быть запущена штатным листом/каталогом Foundry через draw либо вложенным roll из другого документа. При recursive:true раскрываются все выбранные ссылки на RollTable. Доступы реального пользователя и установленный компедиум здесь не проверены.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Witcher Background: How Did Your Trials Go? +4`; `GknRX1nkVVcc9rCK`; `!tables!GknRX1nkVVcc9rCK` | Имя, ID и ключ хранения корневого RollTable |
| results | 8 вложенных документов | Локальные ID уникальны у этого родителя; совпадение ID в другой таблице допустимо |
| formula, replacement, displayRoll | `1d10+4`, true, false | Формула выбора, повторное использование результатов, скрытый основной бросок в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание ниже | Иконка и самостоятельное описание таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Пустые пространства better-rolltables/core; настроек поведения модуля внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.ub0OgKJtPKbMpWUS`; systemId/systemVersion/duplicateSource/exportSource=null | Метаданные происхождения; не ссылка для рекурсивного выбора |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые права и расположение, не проверка доступности службы |
| Result type/name/description/documentUuid | text: пустое name, текст в description; document: имя цели, пустой description, UUID | Отображаемый текст либо ссылка на вложенную таблицу |
| Result _id/_key | ID в перечне; `!tables.results!GknRX1nkVVcc9rCK.<resultId>` | Ключи хранения; _key удалён строгой моделью из toObject |
| Result range/weight/drawn | Диапазоны ниже; все weight=1, drawn=false | getResultsForRoll выбирает все подходящие интервалы, normalize использует веса |
| Result img/flags/_stats | Иконки ниже; flags={}; coreVersion=13.341, systemId/systemVersion/compendiumSource/duplicateSource/exportSource=null | Служебные поля всех результатов |

Root description: Пустая строка.

Иконки результатов: `icons/svg/d20-black.svg`, `icons/svg/d20-grey.svg`. Указанные пути найдены в public/icons установленного ядра; HTTP и внешний вид не проверялись. Текст с бонусом не является изменением характеристики: в структуре нет Item, ActiveEffect, effects или changes.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `q0DM4FW7XCnFdKZu` | [-3,1] | text | `How Did Your Trials Go? - Nearly Fatal (Additional -1 EMP &amp; -1 BODY) The Trial of the Grasses nearly destroyed your body. Though you survived the process, your body and mind were damaged permanently.` | 10–32 |
| 2 | `aMFSTIFk56aW7vyY` | [-3,1] | document | `Witcher Background: What Was Your Most Important Event` | 33–56 |
| 3 | `oKZeEBIq2FLMNk2e` | [2,3] | text | `How Did Your Trials Go? - Poorly Accepted (Additional-1 EMP) The Trial of the Grasses went poorly and the witchers in charge of mutation weren’t entirely sure you would make it. You survived, but not without mental scars.` | 57–79 |
| 4 | `7QhHNiUB0Vu3Ssqv` | [2,3] | document | `Witcher Background: What Was Your Most Important Event` | 80–103 |
| 5 | `kQX7ZeIIWKy5yTPF` | [4,9] | text | `How Did Your Trials Go? - Passable Mutations (No Modifiers) The Trial of the Grasses went well. You passed into the ranks of witchers with nothing more than memories of horrible pain.` | 104–126 |
| 6 | `hkb8v9rCjQOphlyn` | [4,9] | document | `Witcher Background: What Was Your Most Important Event` | 127–150 |
| 7 | `36ROPw9QWjYWmpBV` | [10,14] | text | `How Did Your Trials Go? - Extra Mutations (Additional +1 EMP &amp; +1 DEX) Your body was very receptive to the Trial of the Grasses and you had extra mutations applied to you. Your body handled it well, and all of the pain paid off in the end.` | 151–173 |
| 8 | `VBNK7GwA0wpSZayc` | [10,14] | document | `Witcher Background: What Was Your Most Important Event` | 174–197 |

Во всех пяти вариантах сохранены одинаковые четыре текстовых исхода и четыре перехода к Important Event; различаются formula, корневые ID и часть ID ссылок. Интервалы −3…1, 2…3, 4…9, 10…14 покрывают общий диапазон всех вариантов. Недостижимость отдельного интервала при данной formula ожидается из её границ и сама по себе не объявляется ошибкой. Реальный getResultsForRoll принимает отрицательные числа и 0; он не ограничивает вход диапазоном собственного кубика. Внешний roll может выбрать иначе недостижимую строку: проверено испытание −4 с roll=1d1+13, итог 14 и пара Extra Mutations + Important Event.

Реальная formula даёт значения 5…14. Для каждого диапазона указана доля граней основного кубика; строки с одинаковым диапазоном выбираются вместе, поэтому это вероятность группы, а не деление между её записями.

| range | Одновременно выбранных записей | Доля граней | Результат |
| --- | --- | --- | --- |
| [-3,1] | 2 | 0/10 | Не выбирается штатной formula |
| [2,3] | 2 | 0/10 | Не выбирается штатной formula |
| [4,9] | 2 | 5/10 | text + document |
| [10,14] | 2 | 5/10 | text + document |

## Основные функции и методы

Собственных функций и методов у JSON нет. Следующие действия определены в Foundry 14.367.0:

| Метод | Вход, действия и результат | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Все drawn=false записи, для которых value входит в range включительно | Порядок сохраняется; границы самой formula здесь не проверяются |
| RollTable.roll({roll, recursive}) | По умолчанию `1d10+4`; recursive=true раскрывает documentUuid через fromUuid и innerTable.roll | Родительские модификаторы и исходный roll во вложенный вызов не передаются; _depth увеличивается на 1 |
| RollTable.draw({displayChat}) | roll, затем toMessage при displayChat=true | replacement=true позволяет повторный результат; запросов записи drawn при проверке не было |
| RollTable.normalize({save:false}) | Создаёт клон с 1d8 и одиночными диапазонами по 8 единичным весам | Может изменить исходные вероятности и одновременный выбор; у этого экспорта formula задана, автоматическая нормализация в roll не требуется |
| TableResult.getHTML / documentToAnchor | Подготавливает описание и ссылку на документ, использует HBS | Вставки [[…]] исполняются на этапе enrichHTML; текстовые условия не интерпретируются |
| RollTable.toMessage | Description родителя, все конечные результаты и при displayRoll=true HTML основного броска | Здесь displayRoll=false; он не выключает inline и не переносит управление в дочернюю таблицу |

При прямом запуске с _depth=0 граф допускает 3 конечных text; максимальная внутренняя глубина — 2. Эти границы получены отдельным обходом всех диапазонов и ссылок; проверки исполнения перебирали каждый основной результат и выбранные вложенные сочетания, не все комбинации графа. Ядро отклоняет _depth>5. Witcher Background Generator даёт максимальную глубину 4, его ветка RandomCharacter — 5; эти входы проверены отдельно.

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
| `aMFSTIFk56aW7vyY`; [-3,1] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.34nU6OswdgAyMC6p` | [packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json); [карточка](../witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json.md) | documentUuid:53; имя совпало с целью; recursive:true → innerTable.roll |
| `7QhHNiUB0Vu3Ssqv`; [2,3] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.34nU6OswdgAyMC6p` | [packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json); [карточка](../witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json.md) | documentUuid:100; имя совпало с целью; recursive:true → innerTable.roll |
| `hkb8v9rCjQOphlyn`; [4,9] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.34nU6OswdgAyMC6p` | [packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json); [карточка](../witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json.md) | documentUuid:147; имя совпало с целью; recursive:true → innerTable.roll |
| `VBNK7GwA0wpSZayc`; [10,14] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.34nU6OswdgAyMC6p` | [packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json); [карточка](../witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json.md) | documentUuid:194; имя совпало с целью; recursive:true → innerTable.roll |

Inline-вставок [[…]] нет. Текстовые @UUID/@Compendium, внешние URL и исполняемые макросы в этом файле не найдены. Упоминания людей, предметов, монстров, правил и страниц сами по себе не являются зависимостями на документы.

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_A7jt3mfuFTEQiXRv.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_A7jt3mfuFTEQiXRv.json) | `EjpUyBW2tKuwSB3E`; documentUuid:194; range=[4,4] | `Witcher Background: How Did Early Training Go? +2`: при выборе диапазона и recursive:true вызывает этот документ |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение экспортного каталога для сборки |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Штатное ручное действие вызывает draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Возможное совпадение Item.name с `Witcher Background: How Did Your Trials Go? +4` | Общий поиск таблицы при экспорте добычи ожидает Item, а этот граф возвращает text |

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
| Все поля и ключи | Python stdin, строгий JSON без повторных ключей; отдельная сверка 41 файла | 321 result, 362 уникальных ключа хранения; этот файл: 8 results | Совпадение с установленной БД не проверено |
| Диапазоны и формулы | Настоящие Roll, RollTable.roll/getResultsForRoll | Все 10 граней этой formula; ожидаемые ID независимо выбраны по raw range; минимум 5, максимум 14 | Не перебраны все комбинации вложенных случайных чисел |
| Вложенные вызовы и повторы | Настоящие roll/draw с фасадом fromUuid | Вся порция: 563 основных значений, 1126 повторных draw без чата, 82 draw моделей без pack | Нет сервера, прав игроков или записи DB |
| Каждый result / вывод | Настоящие TableResult.getHTML, HBS, draw/toMessage | Все 95 document и 226 text, 14 inline; 563 прямых сообщений плюс 8 сообщений внешних Decade-сценариев | enrichHTML использует фасад обхода текста; полный браузерный DOM не проверен |
| Варианты и границы | 30 сценариев возраст × обучение; 15 дополнительных сценариев; ещё 23 проверки внешних roll | Основной запуск: 6683 assertions; отдельный запуск: 23; writes=0 | Числа/тексты рулбуков не сверялись |
| Граф и потребители | Все 226 JSON, system.json, module/templates/utils, en/ru | 94 внутренних ссылки, одна исходящая в lifepath, 18 входящих из пяти Character-gen; все цели найдены | Не исключает внешние макросы, модули и динамические вызовы |
| Сохранность и документы | SHA-256, Git, ссылки, таблицы Markdown; журнал порции | Итог зафиксирован в [сверке](../../../review-log.md#task-0003055) | Метаданные доступа не изменялись |

Первый запуск общего сценария остановился на декодировании URI в проверочном коде чтения Roll.toAnchor.dataset.roll; после исправления фасада сравнения весь сценарий выполнен заново. Это не дефект исходной таблицы и не пропущенная проверка её поведения.

## Непроверенные участки и открытые вопросы

Установленные packs/LevelDB, сборка/извлечение, HTTP, визуальная отрисовка, клики, права реальных игроков, полный DOM enrichHTML, сторонние модули и запись мира не проверялись. Наличие schemaVersion=13.341 в истории экспорта не заменяет проверенную совместимость методов ядра 14.367.0. Нет утверждения о соответствии вероятностей, текстов, названий и бонусов рулбукам.

Связанные ещё не разобранные Character-gen-файлы прочитаны и вызваны лишь для перечисленных переходов; полный аудит остаётся в [TASK-0003.056](../../../../../tasks/task-0003.056.md). Точки выбора пользователем не заменялись предполагаемой автоматизацией.

## Связанные проблемы

Связь вариантов обучения с испытаниями описана в [issue-00321](../../../../../issues/potential/issue-00321.md): 16 переходов в вариантах +2/−2 теряют исходный модификатор. Это не ошибка отрицательных range и не изменение ядра.

Общие ограничения вывода и арифметики связанных цепочек — [issue-00319](../../../../../issues/potential/issue-00319.md), [issue-00321](../../../../../issues/potential/issue-00321.md); применимость определяется конкретными ветвями выше. Известная [issue-00320](../../../../../issues/potential/issue-00320.md) про семейные цепочки RandomCharacter не воспроизвелась для проверенного входа ведьмака. [issue-00039](../../../../../issues/potential/issue-00039.md) описывает предположения общего потребителя добычи; [issue-00313](../../../../../issues/potential/issue-00313.md), [issue-00314](../../../../../issues/potential/issue-00314.md), [issue-00315](../../../../../issues/potential/issue-00315.md) — независимые ограничения извлечения. Новые подтверждения, статусы open/closed и исправления не выполнялись.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-12 | cd2743d0548d5c129065c970d4aa5c43cc9632e2; полный файл и перечисленные связи | Первичная карточка по TASK-0003.055; [протокол](../../../review-log.md#task-0003055) |
