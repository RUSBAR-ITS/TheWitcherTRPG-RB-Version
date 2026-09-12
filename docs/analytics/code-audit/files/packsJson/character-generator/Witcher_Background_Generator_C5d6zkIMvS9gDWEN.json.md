# packsJson/character-generator/Witcher_Background_Generator_C5d6zkIMvS9gDWEN.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator/Witcher_Background_Generator_C5d6zkIMvS9gDWEN.json](../../../../../../packsJson/character-generator/Witcher_Background_Generator_C5d6zkIMvS9gDWEN.json) |
| Тип файла | JSON: экспорт RollTable; 9 TableResult (3 text, 6 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, be1c48770219a6d2871259f12c30d93636aac646 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.056](../../../../../tasks/task-0003.056.md); 13 файлов / 2435 строк; этот файл — 243 строк |
| Запись перекрёстной сверки | [TASK-0003.056](../../../review-log.md#task-0003056) |
| SHA-256 файла | 73830c25617963955b7d417bfd072883fcda1811ee067d3cfe7f962063f85b0e |

## Назначение файла

Выбирает возраст начала обучения ведьмака, школу и цепочку обучения, испытаний и последующей биографии. Имя документа — `Witcher Background Generator`. Результат работы — текстовые TableResult и сообщение; создание персонажа как Actor, его вещей или ActiveEffect этим файлом не реализовано.

## Условия использования

[system.json](../../../../../../system.json):32–38,58–63 регистрирует Character-gen как RollTable в Character Generation, путь packs/character-generator.db. UUID данного документа — `Compendium.TheWitcherTRPG.Character-gen.RollTable.C5d6zkIMvS9gDWEN`. JSON является экспортом данных, не браузерным модулем.

[utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт каталог в compilePack с recursive:true; [utils/extract.mjs](../../../../../../utils/extract.mjs) выгружает данные обратно. [Контракт путей и CLI](../../utils/packs.mjs.md), [package.json](../../../../../../package.json):7–8. Команды не запускались, наличие экспорта не доказывает состояние живой БД.

Ручной запуск доступен через лист таблицы или меню каталога Foundry; обычная content-link открывает лист, а не бросает таблицу. При рекурсивном выборе другой RollTable происходит отдельный вызов её roll. Права пользователей, реальные пакеты и сторонние модули не проверены.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name / _id / _key | `Witcher Background Generator`; `C5d6zkIMvS9gDWEN`; `!tables!C5d6zkIMvS9gDWEN` | Название, ID и ключ хранения RollTable |
| results | 9 записей, полный перечень ниже | Локальные ID уникальны у родителя; совпадение с ID другого родителя допустимо |
| formula / replacement / displayRoll | `1d10` / true / true | Выбор по диапазонам, повторение результатов и видимость основного броска в сообщении этой таблицы |
| img | `icons/sundries/scrolls/scroll-worn-beige.webp` | Корневая иконка; путь найден в public установленного Foundry |
| description | Полный текст ниже | Отдельное описание таблицы, не дополнительный TableResult |
| flags | `{"better-rolltables":{},"core":{}}` | Поля сохранены моделью; параметры better-rolltables не исполняются стандартным RollTable.roll |
| ownership / folder / sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые права и расположение |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.ub0OgKJtPKbMpWUS`; остальные четыре поля null | История происхождения; roll следует documentUuid, не compendiumSource |
| Result type / name / description / documentUuid | text: пустое name, текст в description; document: имя цели, пустое описание и UUID | Строка для показа либо вложенный вызов |
| Result _id / _key | Перечень ID ниже; `!tables.results!C5d6zkIMvS9gDWEN.<id>` | Ключ экспорта; _key не является полем модели Foundry |
| Result range / weight / drawn | Интервалы ниже; weight=1; drawn=false | Выбираются все подходящие range, единичные веса используются нормализацией |
| Result img / flags / _stats | Изображения ниже; flags={}; coreVersion=13.341, пять остальных полей null | Представление и служебные данные |

Описание корня: пустая строка.

Иконки результатов: `icons/svg/d20-black.svg`, `icons/svg/d20-grey.svg`. Все ресурсы найдены локально; HTTP и видимость для Foundry-службы не установлены. Непустые table-type/loot-amount-key, когда они есть, относятся к пространству better-rolltables и не меняют доказанное стандартное поведение ядра; сам модуль не исполнялся.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `q0DM4FW7XCnFdKZu` | [1,2] | text | `When Did You Become A Witcher? - Infancy (-2 to the Trial of the Grasses): You were taken to become a witcher when you were a toddler, between 1 and 2 years old. You have no memories of life before becoming a witcher and had nothing to cling to when taking the Trial of the Grasses.` | 10–32 |
| 2 | `qajkRaccfhCw3FmJ` | [1,2] | document | `Witcher Background: What School Did You Train In?` | 33–56 |
| 3 | `nZaULCfUDcjTijGv` | [1,2] | document | `Witcher Background: How Did Early Training Go? -2` | 57–80 |
| 4 | `oKZeEBIq2FLMNk2e` | [3,8] | text | `When Did You Become A Witcher? - Early Childhood (No Modifiers): You were taken to become a witcher when you were young, between 4 and 6 years old. You had some normal memories to aid you when taking the Trial of the Grasses.` | 81–103 |
| 5 | `I2WgdMaqvCOO86Cd` | [3,8] | document | `Witcher Background: What School Did You Train In?` | 104–127 |
| 6 | `d9NGvIh79ha1B9mq` | [3,8] | document | `Witcher Background: How Did Early Training Go?` | 128–151 |
| 7 | `kQX7ZeIIWKy5yTPF` | [9,10] | text | `When Did You Become A Witcher? - Late Childhood (+2 to the Trial of the Grasses): You were taken to become a witcher when you were relatively old, between 8 and 11 years old. While training was somewhat harder, your many memories bolstered you when you took the Trial of the Grasses.` | 152–174 |
| 8 | `q8LCtgshNjOjac5P` | [9,10] | document | `Witcher Background: What School Did You Train In?` | 175–198 |
| 9 | `VaBMiBo9HQjCGHT1` | [9,10] | document | `Witcher Background: How Did Early Training Go? +2` | 199–222 |

На 1–2 выбран текст Infancy (−2 к испытаниям), школа и Early Training −2; на 3–8 — Early Childhood без модификатора и обычное обучение; на 9–10 — Late Childhood (+2) и Early Training +2. Школа вызывается отдельно при любом возрасте и не задаёт модификатор Trials. Цепочка обучения затем выводит Trials → Important Event → Where Are You Now?. Прямой результат — шесть текстов, глубина 4; через RandomCharacter — семь, глубина 5. Настоящая formula этого документа — 1d10, возрастные модификаторы представлены в выборе целевых таблиц. Issue-00321 локализована ниже, в 16 переходах вариантов обучения. Здесь displayRoll=true показывает основной возрастной бросок при прямом draw, а не все вложенные броски.

Все 10 штатных значения основного кубика покрыты. Порядок совместно выбранных ID соответствует массиву results; одинаковый диапазон не делится по весу между совпавшими записями.

| Значения основного броска | Доля граней | Совместно выбранные ID, в порядке JSON |
| --- | --- | --- |
| 1–2 | 2/10 | `q0DM4FW7XCnFdKZu`, `qajkRaccfhCw3FmJ`, `nZaULCfUDcjTijGv` |
| 3–8 | 6/10 | `oKZeEBIq2FLMNk2e`, `I2WgdMaqvCOO86Cd`, `d9NGvIh79ha1B9mq` |
| 9–10 | 2/10 | `kQX7ZeIIWKy5yTPF`, `q8LCtgshNjOjac5P`, `VaBMiBo9HQjCGHT1` |

## Основные функции и методы

Собственных функций у JSON нет. Методы определены в Foundry 14.367.0.

| Метод / действие | Что читает и делает | Результат и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | drawn и включительные границы range | Все совпадения; при 0/11 пусто |
| RollTable.roll({recursive, roll}) | По умолчанию `1d10`; recursive=true разрешает ссылки и вызывает innerTable.roll с увеличенным _depth | Результаты раскрываются в порядке JSON; броски детей и их сообщения отдельно не возвращаются |
| RollTable.draw({displayChat}) | Вызывает roll, если готовые results не переданы; затем toMessage | replacement=true сохраняет доступность результатов; сообщение может быть отключено |
| RollTable.normalize({save:false}) | Единичные weight → клон с 1d9 и одиночными диапазонами | Может разрушить составные выдачи и исходные вероятности; при заданной formula автоматически не вызывается |
| TableResult.getHTML / documentToAnchor | Разрешает документную ссылку, обогащает description, передаёт в HBS | При recursive=false ссылки остаются ссылками; клик открывает лист |
| RollTable.toMessage | Описание корня, конечные результаты, displayRoll корневой таблицы | Вложенный displayRoll не управляет родительским сообщением; inline исполняются при обогащении текста |
| RollTableSheet.#onDrawResult | Сначала submit формы, затем roll; передаёт готовую выдачу в draw | Один корневой roll, а не два; при успешном replacement=true кнопка снова включена |
| ClientDocumentMixin._onClickDocumentLink | this.sheet.render(true) | Открывает лист; сам не запускает roll/draw |

Статический граф этого входа без ограничения ядра: 6–6 конечных text, глубина до 4. Все ветви данного прямого входа укладываются в предел _depth≤5; дополнительные внешние уровни нужно считать отдельно. Эти границы получены обходом диапазонов и ссылок, не утверждением о переборе всех случайных сочетаний во время исполнения.

## Используемые сущности и зависимости

| Используемая сущность | Источник / API | Вид связи и доказательство |
| --- | --- | --- |
| packs / packFolders | [system.json](../../../../../../system.json) | Регистрация имени, типа и пути компедиума |
| compilePack / extractPack | [utils/packs.mjs](../../../../../../utils/packs.mjs); [utils/extract.mjs](../../../../../../utils/extract.mjs); [package.json](../../../../../../package.json) | Чтение/выгрузка экспортных данных; в этой порции не запускались |
| BaseRollTable / BaseTableResult.defineSchema / EmbeddedCollection | Foundry common/documents/roll-table.mjs:43–62; table-result.mjs:48–68; common/abstract/embedded-collection.mjs | Реальные строгие модели приняли все поля и вложенные документы |
| Roll / Die / RollParser / grammar | Foundry client/dice/roll.mjs; terms/die.mjs; parser.mjs; grammar.pegjs | Настоящий выбор кубика, границы и вычисления; RNG контролируемый |
| getResultsForRoll / roll / draw / fromUuid | Foundry client/documents/roll-table.mjs:98–143,264–342 | Выбор, рекурсия, проверка _depth>5; lookup экспортов подменён памятью |
| getHTML / HBS / toMessage | Foundry client/documents/table-result.mjs:45–78; roll-table.mjs:49–82; templates/sheets/roll-table/result-details.hbs; templates/dice/table-result.hbs | Настоящие методы и шаблоны; ChatMessage и anchor документа — фасады |
| _enrichInlineRolls / _createInlineRoll / Roll.toAnchor | Foundry client/applications/ux/text-editor.mjs:247–251,718–775; client/dice/roll.mjs:1021–1034 | Вычисления в конечных описаниях; полный DOM-обход не исполнялся |
| #onClickContentLink / _onClickDocumentLink | Foundry client/applications/ux/text-editor.mjs:792–795; client/documents/abstract/client-document.mjs:422–423 | Настоящие тела обработчиков: UUID → документ → sheet.render(true), с фасадами события/листа |

Пути Foundry относятся к /opt/foundryvtt, вне реестра системы. Ни основной description, ни text-результаты этого файла не содержат [[…]], текстовых @UUID/@Compendium, URL или макросов; исполняемые ссылки представлены documentUuid.

| ID результата / range | Полный documentUuid | Файл и карточка цели | Место обращения / проверка |
| --- | --- | --- | --- |
| `qajkRaccfhCw3FmJ`; [1,2] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.kEqyptPU1X7TvKc1` | [packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json); [карточка](../witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json.md) | documentUuid:53; имя/ID/тип сверены |
| `nZaULCfUDcjTijGv`; [1,2] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.G9iWzbiGQloX7sls` | [packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_G9iWzbiGQloX7sls.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_G9iWzbiGQloX7sls.json); [карточка](../witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_G9iWzbiGQloX7sls.json.md) | documentUuid:77; имя/ID/тип сверены |
| `I2WgdMaqvCOO86Cd`; [3,8] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.kEqyptPU1X7TvKc1` | [packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json); [карточка](../witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json.md) | documentUuid:124; имя/ID/тип сверены |
| `d9NGvIh79ha1B9mq`; [3,8] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.u2n9HR4RhSt1QV3l` | [packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go__u2n9HR4RhSt1QV3l.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go__u2n9HR4RhSt1QV3l.json); [карточка](../witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go__u2n9HR4RhSt1QV3l.json.md) | documentUuid:148; имя/ID/тип сверены |
| `q8LCtgshNjOjac5P`; [9,10] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.kEqyptPU1X7TvKc1` | [packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json); [карточка](../witcher-lifepath/Witcher_Background__What_School_Did_You_Train_In__kEqyptPU1X7TvKc1.json.md) | documentUuid:195; имя/ID/тип сверены |
| `VaBMiBo9HQjCGHT1`; [9,10] | `Compendium.TheWitcherTRPG.Witcher_Lifepath_and_BG_Sub-tables.RollTable.A7jt3mfuFTEQiXRv` | [packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_A7jt3mfuFTEQiXRv.json](../../../../../../packsJson/witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_A7jt3mfuFTEQiXRv.json); [карточка](../witcher-lifepath/Witcher_Background__How_Did_Early_Training_Go___2_A7jt3mfuFTEQiXRv.json.md) | documentUuid:219; имя/ID/тип сверены |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Способ использования |
| --- | --- | --- |
| [packsJson/character-generator/Background_Generator__RandomCharacter_CIpykDUYYuJB0zLv.json](../../../../../../packsJson/character-generator/Background_Generator__RandomCharacter_CIpykDUYYuJB0zLv.json) | `aLWilOjK1d94Rr0Y`; documentUuid:193; [11,11] | `Background Generator: RandomCharacter` при recursive=true вызывает эту таблицу |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Обработка экспортного каталога при сборке |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–440 | Документ таблицы | Submit → roll → draw готового результата |
| Foundry client/applications/sidebar/tabs/roll-table-directory.mjs:28–33 | Документ таблицы | Пункт меню вызывает draw(displayChat:true) |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Возможное совпадение Item.name с `Witcher Background Generator` | Общий поиск при экспорте добычи ожидает Item; этот граф выдаёт текст |

Входящие прямые ссылки перечислены выше. Поиск всех 13 имён, ID и имени пакета по module/templates/utils не нашёл прямого программного вызова этих генераторов. Общее совпадение имени в WitcherItem остаётся возможным; повторного исполнения метода для этих имён не было. Отсутствие строки не исключает внешние макросы, другой мир и динамические обращения.

[module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js):133–137 готовит список событий для листа, :154–156 получает существующие profession/homeland/race Items. [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs):51–95 редактирует биографию и события. [module/data/actor/templates/character/general/backgroundData.js](../../../../../../module/data/actor/templates/character/general/backgroundData.js) и [module/data/actor/templates/character/general/lifeEventData.js](../../../../../../module/data/actor/templates/character/general/lifeEventData.js) задают их поля. Это соседний механизм ручного хранения, а не автоматические потребители текстов этого генератора.

## Данные и изменения состояния

roll возвращает Roll и TableResult[] в памяти; при recursive=true все ссылки этого графа доходят до text либо вызов отклоняется по глубине. Повторные draw при replacement=true не меняют drawn. Нормализация save:false создаёт отдельный клон; исходники и модели сохранены.

draw с показом чата вызывает ChatMessage.create и может вычислить inline во вложенном description; displayRoll относится только к основному Roll. При исключении глубины до toMessage чат не создаётся. Обработчик листа сначала сохраняет форму: в изолированном сценарии submit был фасадом без записи, поэтому отсутствие записей теста не означает отсутствия штатного сохранения формы в полном клиенте.

Обычная content-link только открывает лист. Ни текст расы, ни название профессии/школы, ни бонус/ранение не создают Actor, Item или ActiveEffect. Число братьев/сестёр и указания «за десятилетие» не становятся циклом без внешнего вызова.

## Проверки и доказательства

| Что проверено | Реальное действие / источник | Результат | Предел |
| --- | --- | --- | --- |
| Полный файл и схема | Строгий Python JSON, реальные модели ядра | 9 results, все поля и resource paths; имя/ID/UUID согласованы | Экспорт не сравнивался с DB |
| Основной выбор | Настоящий roll(recursive:false) | Все 10 значений, ID сопоставлены независимо по raw range | Не доказывает все вложенные сочетания |
| Полные выдачи и повторы | Настоящие roll/draw | В порции 445 основных значений, 890 повторных draw без чата, 26 draw моделей без pack | Случайные грани управляемы; реального сервера нет |
| Общая сверка пяти пакетов | 117 моделей, 1527 основных значений, getHTML всех results | 929 results: 677 text, 252 document; 919 достижимы своими formula; 26 inline в 23 описаниях | Десять строк Trials не выбираются штатной формулой своего варианта |
| Вывод корневых генераторов | draw/toMessage, настоящие HBS | 445 рекурсивных и 13 нерекурсивных сообщений; displayRoll соответствует корню | Render Roll заменён маркером, не визуальным кубиком |
| Составные и отказавшие пути | 22 успешных целевых сценария и 4 отказа глубины | 8345 assertions основного запуска; writes=0, snapshots сохранены | Не полный перебор комбинаций и не проверка игровых правил |
| Обычный клик и кнопка броска | Настоящие обработчики с событиями/формой/листом в памяти | 68 assertions; 13 открытий без броска, 13 успешных действий; отдельный отказ RandomCharacter оставил кнопку disabled и не создал чат | Полный браузер/форма не запускались |
| Карточки и исходники | [Итоговая перекрёстная сверка](../../../review-log.md#task-0003056) | 13 новых карточек и общая проверка прежних 104 | История прежних проверок сохранена |

Первоначальные ошибки самого сценария (синтаксис вычисляемого ключа, ожидаемая глубина живых родителей и выбор Happy Love вместо Romantic Tragedy) исправлены после чтения источников; полный запуск затем пройден. Они не зарегистрированы как ошибки системы.

## Непроверенные участки и открытые вопросы

Не проверялись действующие packs/LevelDB, compile/extract, HTTP, полное DOM enrichHTML, внешний вид, права игроков, настоящее сохранение форм/мира, макросы и better-rolltables. Случайные сочетания, не входящие в перечисленные сценарии, описаны по графу с явным пределом проверки. Соответствие контента и чисел книгам исключено.

Общая сверка охватывает все 117 файлов пяти пакетов, включая 15 lifepath-таблиц вне дерева этих 13 генераторов; они доступны отдельно и не объявлены ненужными. Другие компедиумы разбираются в следующих порциях.

## Связанные проблемы

[issue-00321](../../../../../issues/potential/issue-00321.md) — потери возрастного модификатора находятся в 16 ссылках вариантов Early Training, вызываемых этим генератором.

[issue-00039](../../../../../issues/potential/issue-00039.md) относится к отдельному общему потребителю добычи; [issue-00313](../../../../../issues/potential/issue-00313.md), [issue-00314](../../../../../issues/potential/issue-00314.md), [issue-00315](../../../../../issues/potential/issue-00315.md) — к утилитам извлечения. Они не доказывают дефект конкретного JSON. При выполнении TASK-0003.056 новых issues не создано; issue-00320 дополнена, статусы potential и отсутствие исправлений сохранены.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | be1c48770219a6d2871259f12c30d93636aac646; полный файл и перечисленные связи | Первичная карточка; [протокол TASK-0003.056](../../../review-log.md#task-0003056) |
