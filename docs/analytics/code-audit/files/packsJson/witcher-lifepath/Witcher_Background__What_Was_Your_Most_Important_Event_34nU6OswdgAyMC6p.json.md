# packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__What_Was_Your_Most_Important_Event_34nU6OswdgAyMC6p.json) |
| Тип файла | JSON: экспорт RollTable, 20 TableResult (10 text, 10 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, cd2743d0548d5c129065c970d4aa5c43cc9632e2 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.055](../../../../../tasks/task-0003.055.md); 41 файл / 8708 строк; этот файл — 500 строк |
| Запись перекрёстной сверки | [TASK-0003.055](../../../review-log.md#task-0003055) |
| SHA-256 файла | f992a3b030a536199beceb148ffbd9abda9a112fa17bc382d2a562df8c3f0f95 |

## Назначение файла

Выбирает важное событие биографии и вслед за ним текущее положение ведьмака. Имя документа — `Witcher Background: What Was Your Most Important Event`. Это данные для выборки и вывода описаний, включая явно заданные ссылки и формулы; самостоятельной программы изменения Actor/Item в JSON нет.

## Условия использования

[system.json](../../../../../../system.json):36,71–76 регистрирует RollTable-пакет Witcher_Lifepath_and_BG_Sub-tables в папке Character Generation с путём packs/witcher-lifepath.db. Адрес документа — `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.34nU6OswdgAyMC6p`.

[utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт каталог compilePack с recursive:true; путь и контракт CLI описаны в [карточке утилиты](../../utils/packs.mjs.md). [utils/extract.mjs](../../../../../../utils/extract.mjs) выполняет обратную выгрузку. Эти команды не запускались. Экспорт не является подключаемым ES-модулем и не доказывает содержимое установленной БД.

Таблица может быть запущена штатным листом/каталогом Foundry через draw либо вложенным roll из другого документа. При recursive:true раскрываются все выбранные ссылки на RollTable. Доступы реального пользователя и установленный компедиум здесь не проверены.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Witcher Background: What Was Your Most Important Event`; `34nU6OswdgAyMC6p`; `!tables!34nU6OswdgAyMC6p` | Имя, ID и ключ хранения корневого RollTable |
| results | 20 вложенных документов | Локальные ID уникальны у этого родителя; совпадение ID в другой таблице допустимо |
| formula, replacement, displayRoll | `1d10`, true, false | Формула выбора, повторное использование результатов, скрытый основной бросок в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание ниже | Иконка и самостоятельное описание таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Пустые пространства better-rolltables/core; настроек поведения модуля внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.ub0OgKJtPKbMpWUS`; systemId/systemVersion/duplicateSource/exportSource=null | Метаданные происхождения; не ссылка для рекурсивного выбора |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые права и расположение, не проверка доступности службы |
| Result type/name/description/documentUuid | text: пустое name, текст в description; document: имя цели, пустой description, UUID | Отображаемый текст либо ссылка на вложенную таблицу |
| Result _id/_key | ID в перечне; `!tables.results!34nU6OswdgAyMC6p.<resultId>` | Ключи хранения; _key удалён строгой моделью из toObject |
| Result range/weight/drawn | Диапазоны ниже; все weight=1, drawn=false | getResultsForRoll выбирает все подходящие интервалы, normalize использует веса |
| Result img/flags/_stats | Иконки ниже; flags={}; coreVersion=13.341, systemId/systemVersion/compendiumSource/duplicateSource/exportSource=null | Служебные поля всех результатов |

Root description: Пустая строка.

Иконки результатов: `icons/svg/d20-black.svg`, `icons/svg/d20-grey.svg`. Указанные пути найдены в public/icons установленного ядра; HTTP и внешний вид не проверялись. Текст с бонусом не является изменением характеристики: в структуре нет Item, ActiveEffect, effects или changes.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `q0DM4FW7XCnFdKZu` | [1,1] | text | `What Was Your Most Important Event - Given a Child by the Law of Surprises: Along your travels you invoked the Law of Surprises and received a child. They may have been a boy, in which case they were made into a witcher, or a girl, in which case their fate was up to you.` | 10–32 |
| 2 | `sqyIMiR1RKv2AHJa` | [1,1] | document | `Witcher Background: Where Are You Now?` | 33–56 |
| 3 | `oKZeEBIq2FLMNk2e` | [2,2] | text | `What Was Your Most Important Event - Hunted by a Sentient Monster: The tables turned during one of your hunts. Sentient monsters like grave hags and katakan can be dangerous quarry, and you wound up becoming the hunted for a stressful night.` | 57–79 |
| 4 | `fCL38Rgrs0Zoi6tL` | [2,2] | document | `Witcher Background: Where Are You Now?` | 80–103 |
| 5 | `kQX7ZeIIWKy5yTPF` | [3,3] | text | `What Was Your Most Important Event - Fought Alongside a Knight: You did battle alongside a noble knight. This may have been against both of your wishes or even an accident, but fighting beside a noble changed your outlook on knights and your job as a witcher.` | 104–126 |
| 6 | `wV6AXUWCol53u7Qp` | [3,3] | document | `Witcher Background: Where Are You Now?` | 127–150 |
| 7 | `36ROPw9QWjYWmpBV` | [4,4] | text | `What Was Your Most Important Event - Captured by a Mage for Testing: Mages lust after the secrets of Witcher mutations. At some point in your life, you were captured by a mage who experimented on you in an attempt to reverse-engineer them.` | 151–173 |
| 8 | `XdFNmzMBLOFAdT0a` | [4,4] | document | `Witcher Background: Where Are You Now?` | 174–197 |
| 9 | `9kVdEtFeX4a3nAoe` | [5,5] | text | `What Was Your Most Important Event - Worked for a Nobleman: For a time you worked for a nobleman. The pay was good, but it was strange and aggravating to have to hide most of your actions to avoid shaming the family by bringing their secrets to light.` | 198–220 |
| 10 | `l4vJrb9CXI7lFvOF` | [5,5] | document | `Witcher Background: Where Are You Now?` | 221–244 |
| 11 | `cQfRuoxqB1FI58LA` | [6,6] | text | `What Was Your Most Important Event - Went Beyond the Boundaries: Once, you traveled beyond the borders of the Continent—past the Dragon Mountains, the Tir Tochair or Blue Mountains, or the Great Sea. You have seen far lands unknown to most others.` | 245–267 |
| 12 | `9ohWB7wfnoJIuyMj` | [6,6] | document | `Witcher Background: Where Are You Now?` | 268–291 |
| 13 | `th9s2aW3pwS3ZZX2` | [7,7] | text | `What Was Your Most Important Event - Meaningful Romance: Most witchers remain neutral and avoid meaningful relationships. However, this didn’t stop you. You fell in love and actually considered settling down. It still occurs to you sometimes.` | 292–314 |
| 14 | `olJrQIfiLqykKL6Y` | [7,7] | document | `Witcher Background: Where Are You Now?` | 315–338 |
| 15 | `tfUjaxwfTwqW98vG` | [8,8] | text | `What Was Your Most Important Event - Fought for your Keep: You fought at a siege of your keep. You were outnumbered and overpowered, but you stayed nonetheless. You survived the siege with serious wounds, but saw your brethren dying around you.` | 339–361 |
| 16 | `e1QeDpvSCQW3TLl0` | [8,8] | document | `Witcher Background: Where Are You Now?` | 362–385 |
| 17 | `XFy2l49tSxFMwvUu` | [9,9] | text | `What Was Your Most Important Event - Gained Infamy: After helping a city with a monster, the people became afraid and turned on you. They might have even tried to kill you. Either way, you’ve seen what kind of reward you can expect from people` | 386–408 |
| 18 | `A6SuhFPiLwWjoYCB` | [9,9] | document | `Witcher Background: Where Are You Now?` | 409–432 |
| 19 | `NlfhnGUfAnLtImRU` | [10,10] | text | `What Was Your Most Important Event - Gained Fame: You were well-received in a town after helping them with a monster. You didn’t expect free drinks or women casting you glances, but that’s what you got. You haven’t seen such kindness again, but it was heartening.` | 433–455 |
| 20 | `9rYHpxRi9jvAeqhM` | [10,10] | document | `Witcher Background: Where Are You Now?` | 456–479 |

Каждая грань 1–10 выбирает текст и ссылку на один и тот же Where Are You Now?. При recursive=true получаются два текста; указанные в рассказах ребёнок, роман, маг или слава не создают документов и новых дополнительных бросков.

Реальная formula даёт значения 1…10. Для каждого диапазона указана доля граней основного кубика; строки с одинаковым диапазоном выбираются вместе, поэтому это вероятность группы, а не деление между её записями.

| range | Одновременно выбранных записей | Доля граней | Результат |
| --- | --- | --- | --- |
| [1,1] | 2 | 1/10 | text + document |
| [2,2] | 2 | 1/10 | text + document |
| [3,3] | 2 | 1/10 | text + document |
| [4,4] | 2 | 1/10 | text + document |
| [5,5] | 2 | 1/10 | text + document |
| [6,6] | 2 | 1/10 | text + document |
| [7,7] | 2 | 1/10 | text + document |
| [8,8] | 2 | 1/10 | text + document |
| [9,9] | 2 | 1/10 | text + document |
| [10,10] | 2 | 1/10 | text + document |

## Основные функции и методы

Собственных функций и методов у JSON нет. Следующие действия определены в Foundry 14.367.0:

| Метод | Вход, действия и результат | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Все drawn=false записи, для которых value входит в range включительно | Порядок сохраняется; границы самой formula здесь не проверяются |
| RollTable.roll({roll, recursive}) | По умолчанию `1d10`; recursive=true раскрывает documentUuid через fromUuid и innerTable.roll | Родительские модификаторы и исходный roll во вложенный вызов не передаются; _depth увеличивается на 1 |
| RollTable.draw({displayChat}) | roll, затем toMessage при displayChat=true | replacement=true позволяет повторный результат; запросов записи drawn при проверке не было |
| RollTable.normalize({save:false}) | Создаёт клон с 1d20 и одиночными диапазонами по 20 единичным весам | Может изменить исходные вероятности и одновременный выбор; у этого экспорта formula задана, автоматическая нормализация в roll не требуется |
| TableResult.getHTML / documentToAnchor | Подготавливает описание и ссылку на документ, использует HBS | Вставки [[…]] исполняются на этапе enrichHTML; текстовые условия не интерпретируются |
| RollTable.toMessage | Description родителя, все конечные результаты и при displayRoll=true HTML основного броска | Здесь displayRoll=false; он не выключает inline и не переносит управление в дочернюю таблицу |

При прямом запуске с _depth=0 граф допускает 2 конечных text; максимальная внутренняя глубина — 1. Эти границы получены отдельным обходом всех диапазонов и ссылок; проверки исполнения перебирали каждый основной результат и выбранные вложенные сочетания, не все комбинации графа. Ядро отклоняет _depth>5. Witcher Background Generator даёт максимальную глубину 4, его ветка RandomCharacter — 5; эти входы проверены отдельно.

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
| `sqyIMiR1RKv2AHJa`; [1,1] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:53; имя совпало с целью; recursive:true → innerTable.roll |
| `fCL38Rgrs0Zoi6tL`; [2,2] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:100; имя совпало с целью; recursive:true → innerTable.roll |
| `wV6AXUWCol53u7Qp`; [3,3] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:147; имя совпало с целью; recursive:true → innerTable.roll |
| `XdFNmzMBLOFAdT0a`; [4,4] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:194; имя совпало с целью; recursive:true → innerTable.roll |
| `l4vJrb9CXI7lFvOF`; [5,5] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:241; имя совпало с целью; recursive:true → innerTable.roll |
| `9ohWB7wfnoJIuyMj`; [6,6] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:288; имя совпало с целью; recursive:true → innerTable.roll |
| `olJrQIfiLqykKL6Y`; [7,7] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:335; имя совпало с целью; recursive:true → innerTable.roll |
| `e1QeDpvSCQW3TLl0`; [8,8] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:382; имя совпало с целью; recursive:true → innerTable.roll |
| `A6SuhFPiLwWjoYCB`; [9,9] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:429; имя совпало с целью; recursive:true → innerTable.roll |
| `9rYHpxRi9jvAeqhM`; [10,10] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.w8GcZsTyPF85V5Rr` | [packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json); [карточка](../witcher-lifepath/Witcher_Background__Where_Are_You_Now__w8GcZsTyPF85V5Rr.json.md) | documentUuid:476; имя совпало с целью; recursive:true → innerTable.roll |

Inline-вставок [[…]] нет. Текстовые @UUID/@Compendium, внешние URL и исполняемые макросы в этом файле не найдены. Упоминания людей, предметов, монстров, правил и страниц сами по себе не являются зависимостями на документы.

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json) | `bYxTODjNqz7aUYAb`; documentUuid:53; range=[-3,1] | `Witcher Background: How Did Your Trials Go? -2`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json) | `QcVDT06FJBeWG9iX`; documentUuid:100; range=[2,3] | `Witcher Background: How Did Your Trials Go? -2`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json) | `4USYOsTytUepe5tq`; documentUuid:147; range=[4,9] | `Witcher Background: How Did Your Trials Go? -2`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_CDX4hqsxcxxovYz3.json) | `MGrLuHzN2tBHy1tD`; documentUuid:194; range=[10,14] | `Witcher Background: How Did Your Trials Go? -2`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json) | `g8M6NpFm7tM6Vxit`; documentUuid:53; range=[-3,1] | `Witcher Background: How Did Your Trials Go? +2`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json) | `PetWGxxqNcQ9CTY8`; documentUuid:100; range=[2,3] | `Witcher Background: How Did Your Trials Go? +2`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json) | `pBJUmRRDkPudGBWz`; documentUuid:147; range=[4,9] | `Witcher Background: How Did Your Trials Go? +2`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___2_zNG1R1HQoY6tpSLz.json) | `ErK1v2gFZ5OEch8Z`; documentUuid:194; range=[10,14] | `Witcher Background: How Did Your Trials Go? +2`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json) | `aMFSTIFk56aW7vyY`; documentUuid:53; range=[-3,1] | `Witcher Background: How Did Your Trials Go? +4`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json) | `7QhHNiUB0Vu3Ssqv`; documentUuid:100; range=[2,3] | `Witcher Background: How Did Your Trials Go? +4`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json) | `hkb8v9rCjQOphlyn`; documentUuid:147; range=[4,9] | `Witcher Background: How Did Your Trials Go? +4`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_GknRX1nkVVcc9rCK.json) | `VBNK7GwA0wpSZayc`; documentUuid:194; range=[10,14] | `Witcher Background: How Did Your Trials Go? +4`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json) | `zGbAd12JQAx4PVSw`; documentUuid:53; range=[-3,1] | `Witcher Background: How Did Your Trials Go? -4`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json) | `inn7wXheSB0lUHsl`; documentUuid:100; range=[2,3] | `Witcher Background: How Did Your Trials Go? -4`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json) | `kStCm5qxgqcW7pCW`; documentUuid:147; range=[4,9] | `Witcher Background: How Did Your Trials Go? -4`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go___4_sY3qw9UfVyx1l9BF.json) | `0NkBgX2JOys4dG8c`; documentUuid:194; range=[10,14] | `Witcher Background: How Did Your Trials Go? -4`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json) | `OFiLUCfJASKpW8Xy`; documentUuid:53; range=[-3,1] | `Witcher Background: How Did Your Trials Go?`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json) | `XX55UTexuEfog1TL`; documentUuid:100; range=[2,3] | `Witcher Background: How Did Your Trials Go?`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json) | `9XyHf6ekxcQQZkit`; documentUuid:147; range=[4,9] | `Witcher Background: How Did Your Trials Go?`: при выборе диапазона и recursive:true вызывает этот документ |
| [packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Your_Trials_Go__vaUFKIYBmEbJotfJ.json) | `9RwdbtijetbDyrX1`; documentUuid:194; range=[10,14] | `Witcher Background: How Did Your Trials Go?`: при выборе диапазона и recursive:true вызывает этот документ |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение экспортного каталога для сборки |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Штатное ручное действие вызывает draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Возможное совпадение Item.name с `Witcher Background: What Was Your Most Important Event` | Общий поиск таблицы при экспорте добычи ожидает Item, а этот граф возвращает text |

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
| Все поля и ключи | Python stdin, строгий JSON без повторных ключей; отдельная сверка 41 файла | 321 result, 362 уникальных ключа хранения; этот файл: 20 results | Совпадение с установленной БД не проверено |
| Диапазоны и формулы | Настоящие Roll, RollTable.roll/getResultsForRoll | Все 10 граней этой formula; ожидаемые ID независимо выбраны по raw range; минимум 1, максимум 10 | Не перебраны все комбинации вложенных случайных чисел |
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

Самостоятельная новая проблема в этом файле не зарегистрирована. Это не подтверждение всего контента или отсутствия ошибок во внешних потребителях.

Общие ограничения вывода и арифметики связанных цепочек — [issue-00319](../../../../../issues/potential/issue-00319.md), [issue-00321](../../../../../issues/potential/issue-00321.md); применимость определяется конкретными ветвями выше. Известная [issue-00320](../../../../../issues/potential/issue-00320.md) про семейные цепочки RandomCharacter не воспроизвелась для проверенного входа ведьмака. [issue-00039](../../../../../issues/potential/issue-00039.md) описывает предположения общего потребителя добычи; [issue-00313](../../../../../issues/potential/issue-00313.md), [issue-00314](../../../../../issues/potential/issue-00314.md), [issue-00315](../../../../../issues/potential/issue-00315.md) — независимые ограничения извлечения. Новые подтверждения, статусы open/closed и исправления не выполнялись.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-12 | cd2743d0548d5c129065c970d4aa5c43cc9632e2; полный файл и перечисленные связи | Первичная карточка по TASK-0003.055; [протокол](../../../review-log.md#task-0003055) |
