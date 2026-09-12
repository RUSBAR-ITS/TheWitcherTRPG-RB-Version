# packsJson/character-generator/Style_and_Values_CjaIcLRWSlzwI6ly.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator/Style_and_Values_CjaIcLRWSlzwI6ly.json](../../../../../../packsJson/character-generator/Style_and_Values_CjaIcLRWSlzwI6ly.json) |
| Тип файла | JSON: экспорт RollTable; 7 TableResult (0 text, 7 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, be1c48770219a6d2871259f12c30d93636aac646 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.056](../../../../../tasks/task-0003.056.md); 13 файлов / 2435 строк; этот файл — 198 строк |
| Запись перекрёстной сверки | [TASK-0003.056](../../../review-log.md#task-0003056) |
| SHA-256 файла | 9caafc6910b2f7368bc77c23e31600681b3696d02c1af9b382c75866c98156da |

## Назначение файла

Собирает семь текстовых аспектов стиля и ценностей. Имя документа — `Style and Values`. Результат работы — текстовые TableResult и сообщение; создание персонажа как Actor, его вещей или ActiveEffect этим файлом не реализовано.

## Условия использования

[system.json](../../../../../../system.json):32–38,58–63 регистрирует Character-gen как RollTable в Character Generation, путь packs/character-generator.db. UUID данного документа — `Compendium.TheWitcherTRPG.Character-gen.RollTable.CjaIcLRWSlzwI6ly`. JSON является экспортом данных, не браузерным модулем.

[utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт каталог в compilePack с recursive:true; [utils/extract.mjs](../../../../../../utils/extract.mjs) выгружает данные обратно. [Контракт путей и CLI](../../utils/packs.mjs.md), [package.json](../../../../../../package.json):7–8. Команды не запускались, наличие экспорта не доказывает состояние живой БД.

Ручной запуск доступен через лист таблицы или меню каталога Foundry; обычная content-link открывает лист, а не бросает таблицу. При рекурсивном выборе другой RollTable происходит отдельный вызов её roll. Права пользователей, реальные пакеты и сторонние модули не проверены.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name / _id / _key | `Style and Values`; `CjaIcLRWSlzwI6ly`; `!tables!CjaIcLRWSlzwI6ly` | Название, ID и ключ хранения RollTable |
| results | 7 записей, полный перечень ниже | Локальные ID уникальны у родителя; совпадение с ID другого родителя допустимо |
| formula / replacement / displayRoll | `1d1` / true / false | Выбор по диапазонам, повторение результатов и видимость основного броска в сообщении этой таблицы |
| img | `icons/sundries/survival/razor.webp` | Корневая иконка; путь найден в public установленного Foundry |
| description | Полный текст ниже | Отдельное описание таблицы, не дополнительный TableResult |
| flags | `{"better-rolltables":{},"core":{}}` | Поля сохранены моделью; параметры better-rolltables не исполняются стандартным RollTable.roll |
| ownership / folder / sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые права и расположение |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.hwod1LcFof5GLUzW`; остальные четыре поля null | История происхождения; roll следует documentUuid, не compendiumSource |
| Result type / name / description / documentUuid | text: пустое name, текст в description; document: имя цели, пустое описание и UUID | Строка для показа либо вложенный вызов |
| Result _id / _key | Перечень ID ниже; `!tables.results!CjaIcLRWSlzwI6ly.<id>` | Ключ экспорта; _key не является полем модели Foundry |
| Result range / weight / drawn | Интервалы ниже; weight=1; drawn=false | Выбираются все подходящие range, единичные веса используются нормализацией |
| Result img / flags / _stats | Изображения ниже; flags={}; coreVersion=13.341, пять остальных полей null | Представление и служебные данные |

Описание корня: пустая строка.

Иконки результатов: `icons/svg/d20-grey.svg`. Все ресурсы найдены локально; HTTP и видимость для Foundry-службы не установлены. Непустые table-type/loot-amount-key, когда они есть, относятся к пространству better-rolltables и не меняют доказанное стандартное поведение ядра; сам модуль не исполнялся.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `q0DM4FW7XCnFdKZu` | [1,1] | document | `Style: Clothing` | 10–33 |
| 2 | `6eMBIJMQZmhaVyCr` | [1,1] | document | `Style: Personality` | 34–57 |
| 3 | `Kot5qN9Crj60jbwU` | [1,1] | document | `Style: Hair Style` | 58–81 |
| 4 | `YqKoWFzgGZuSuzj0` | [1,1] | document | `Style: Affectations` | 82–105 |
| 5 | `7LFO8Ez5nQK98SWT` | [1,1] | document | `Values: Valued Person` | 106–129 |
| 6 | `O4kO4Ec9Zjr1F3Qm` | [1,1] | document | `Values: Ideals` | 130–153 |
| 7 | `HkPKK3KrmtmNyo1B` | [1,1] | document | `Values: Feelings on People` | 154–177 |

Все семь [1,1] выбираются вместе: Clothing → Personality → Hair Style → Affectations → Valued Person → Ideals → Feelings on People. Семь конечных текстов, глубина 1; порядок задан results, а не алфавитным именем. Генератор не вызывается автоматически из RandomCharacter или расовых Background. Одежда и детали внешности не создают Item и не заполняют поля Actor.

Все 1 штатных значения основного кубика покрыты. Порядок совместно выбранных ID соответствует массиву results; одинаковый диапазон не делится по весу между совпавшими записями.

| Значения основного броска | Доля граней | Совместно выбранные ID, в порядке JSON |
| --- | --- | --- |
| 1–1 | 1/1 | `q0DM4FW7XCnFdKZu`, `6eMBIJMQZmhaVyCr`, `Kot5qN9Crj60jbwU`, `YqKoWFzgGZuSuzj0`, `7LFO8Ez5nQK98SWT`, `O4kO4Ec9Zjr1F3Qm`, `HkPKK3KrmtmNyo1B` |

## Основные функции и методы

Собственных функций у JSON нет. Методы определены в Foundry 14.367.0.

| Метод / действие | Что читает и делает | Результат и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | drawn и включительные границы range | Все совпадения; при 0/2 пусто |
| RollTable.roll({recursive, roll}) | По умолчанию `1d1`; recursive=true разрешает ссылки и вызывает innerTable.roll с увеличенным _depth | Результаты раскрываются в порядке JSON; броски детей и их сообщения отдельно не возвращаются |
| RollTable.draw({displayChat}) | Вызывает roll, если готовые results не переданы; затем toMessage | replacement=true сохраняет доступность результатов; сообщение может быть отключено |
| RollTable.normalize({save:false}) | Единичные weight → клон с 1d7 и одиночными диапазонами | Может разрушить составные выдачи и исходные вероятности; при заданной formula автоматически не вызывается |
| TableResult.getHTML / documentToAnchor | Разрешает документную ссылку, обогащает description, передаёт в HBS | При recursive=false ссылки остаются ссылками; клик открывает лист |
| RollTable.toMessage | Описание корня, конечные результаты, displayRoll корневой таблицы | Вложенный displayRoll не управляет родительским сообщением; inline исполняются при обогащении текста |
| RollTableSheet.#onDrawResult | Сначала submit формы, затем roll; передаёт готовую выдачу в draw | Один корневой roll, а не два; при успешном replacement=true кнопка снова включена |
| ClientDocumentMixin._onClickDocumentLink | this.sheet.render(true) | Открывает лист; сам не запускает roll/draw |

Статический граф этого входа без ограничения ядра: 7–7 конечных text, глубина до 1. Все ветви данного прямого входа укладываются в предел _depth≤5; дополнительные внешние уровни нужно считать отдельно. Эти границы получены обходом диапазонов и ссылок, не утверждением о переборе всех случайных сочетаний во время исполнения.

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
| `q0DM4FW7XCnFdKZu`; [1,1] | `Compendium.TheWitcherTRPG.Style_and_Values_Sub-tables.RollTable.BuyEb4FcAyQL2hov` | [packsJson/style/Style__Clothing_BuyEb4FcAyQL2hov.json](../../../../../../packsJson/style/Style__Clothing_BuyEb4FcAyQL2hov.json); [карточка](../style/Style__Clothing_BuyEb4FcAyQL2hov.json.md) | documentUuid:30; имя/ID/тип сверены |
| `6eMBIJMQZmhaVyCr`; [1,1] | `Compendium.TheWitcherTRPG.Style_and_Values_Sub-tables.RollTable.TOQz3ETDronoeEDt` | [packsJson/style/Style__Personality_TOQz3ETDronoeEDt.json](../../../../../../packsJson/style/Style__Personality_TOQz3ETDronoeEDt.json); [карточка](../style/Style__Personality_TOQz3ETDronoeEDt.json.md) | documentUuid:54; имя/ID/тип сверены |
| `Kot5qN9Crj60jbwU`; [1,1] | `Compendium.TheWitcherTRPG.Style_and_Values_Sub-tables.RollTable.Ov9xIpAdWEPZCIoH` | [packsJson/style/Style__Hair_Style_Ov9xIpAdWEPZCIoH.json](../../../../../../packsJson/style/Style__Hair_Style_Ov9xIpAdWEPZCIoH.json); [карточка](../style/Style__Hair_Style_Ov9xIpAdWEPZCIoH.json.md) | documentUuid:78; имя/ID/тип сверены |
| `YqKoWFzgGZuSuzj0`; [1,1] | `Compendium.TheWitcherTRPG.Style_and_Values_Sub-tables.RollTable.4RWDMDzNdnz2kgwU` | [packsJson/style/Style__Affectations_4RWDMDzNdnz2kgwU.json](../../../../../../packsJson/style/Style__Affectations_4RWDMDzNdnz2kgwU.json); [карточка](../style/Style__Affectations_4RWDMDzNdnz2kgwU.json.md) | documentUuid:102; имя/ID/тип сверены |
| `7LFO8Ez5nQK98SWT`; [1,1] | `Compendium.TheWitcherTRPG.Style_and_Values_Sub-tables.RollTable.y1WCi6n2Kpwqb27P` | [packsJson/style/Values__Valued_Person_y1WCi6n2Kpwqb27P.json](../../../../../../packsJson/style/Values__Valued_Person_y1WCi6n2Kpwqb27P.json); [карточка](../style/Values__Valued_Person_y1WCi6n2Kpwqb27P.json.md) | documentUuid:126; имя/ID/тип сверены |
| `O4kO4Ec9Zjr1F3Qm`; [1,1] | `Compendium.TheWitcherTRPG.Style_and_Values_Sub-tables.RollTable.s5EjP50ddIVoitHT` | [packsJson/style/Values__Ideals_s5EjP50ddIVoitHT.json](../../../../../../packsJson/style/Values__Ideals_s5EjP50ddIVoitHT.json); [карточка](../style/Values__Ideals_s5EjP50ddIVoitHT.json.md) | documentUuid:150; имя/ID/тип сверены |
| `HkPKK3KrmtmNyo1B`; [1,1] | `Compendium.TheWitcherTRPG.Style_and_Values_Sub-tables.RollTable.4eCXMVEfRx4PivWH` | [packsJson/style/Values__Feelings_on_People_4eCXMVEfRx4PivWH.json](../../../../../../packsJson/style/Values__Feelings_on_People_4eCXMVEfRx4PivWH.json); [карточка](../style/Values__Feelings_on_People_4eCXMVEfRx4PivWH.json.md) | documentUuid:174; имя/ID/тип сверены |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Способ использования |
| --- | --- | --- |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Обработка экспортного каталога при сборке |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–440 | Документ таблицы | Submit → roll → draw готового результата |
| Foundry client/applications/sidebar/tabs/roll-table-directory.mjs:28–33 | Документ таблицы | Пункт меню вызывает draw(displayChat:true) |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Возможное совпадение Item.name с `Style and Values` | Общий поиск при экспорте добычи ожидает Item; этот граф выдаёт текст |

Входящих documentUuid из всех 226 экспортов не найдено; это самостоятельная точка ручного/внешнего запуска. Поиск всех 13 имён, ID и имени пакета по module/templates/utils не нашёл прямого программного вызова этих генераторов. Общее совпадение имени в WitcherItem остаётся возможным; повторного исполнения метода для этих имён не было. Отсутствие строки не исключает внешние макросы, другой мир и динамические обращения.

[module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js):133–137 готовит список событий для листа, :154–156 получает существующие profession/homeland/race Items. [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs):51–95 редактирует биографию и события. [module/data/actor/templates/character/general/backgroundData.js](../../../../../../module/data/actor/templates/character/general/backgroundData.js) и [module/data/actor/templates/character/general/lifeEventData.js](../../../../../../module/data/actor/templates/character/general/lifeEventData.js) задают их поля. Это соседний механизм ручного хранения, а не автоматические потребители текстов этого генератора.

## Данные и изменения состояния

roll возвращает Roll и TableResult[] в памяти; при recursive=true все ссылки этого графа доходят до text либо вызов отклоняется по глубине. Повторные draw при replacement=true не меняют drawn. Нормализация save:false создаёт отдельный клон; исходники и модели сохранены.

draw с показом чата вызывает ChatMessage.create и может вычислить inline во вложенном description; displayRoll относится только к основному Roll. При исключении глубины до toMessage чат не создаётся. Обработчик листа сначала сохраняет форму: в изолированном сценарии submit был фасадом без записи, поэтому отсутствие записей теста не означает отсутствия штатного сохранения формы в полном клиенте.

Обычная content-link только открывает лист. Ни текст расы, ни название профессии/школы, ни бонус/ранение не создают Actor, Item или ActiveEffect. Число братьев/сестёр и указания «за десятилетие» не становятся циклом без внешнего вызова.

## Проверки и доказательства

| Что проверено | Реальное действие / источник | Результат | Предел |
| --- | --- | --- | --- |
| Полный файл и схема | Строгий Python JSON, реальные модели ядра | 7 results, все поля и resource paths; имя/ID/UUID согласованы | Экспорт не сравнивался с DB |
| Основной выбор | Настоящий roll(recursive:false) | Все 1 значений, ID сопоставлены независимо по raw range | Не доказывает все вложенные сочетания |
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

Новая самостоятельная проблема в этом файле не зарегистрирована.

[issue-00039](../../../../../issues/potential/issue-00039.md) относится к отдельному общему потребителю добычи; [issue-00313](../../../../../issues/potential/issue-00313.md), [issue-00314](../../../../../issues/potential/issue-00314.md), [issue-00315](../../../../../issues/potential/issue-00315.md) — к утилитам извлечения. Они не доказывают дефект конкретного JSON. При выполнении TASK-0003.056 новых issues не создано; issue-00320 дополнена, статусы potential и отсутствие исправлений сохранены.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | be1c48770219a6d2871259f12c30d93636aac646; полный файл и перечисленные связи | Первичная карточка; [протокол TASK-0003.056](../../../review-log.md#task-0003056) |
