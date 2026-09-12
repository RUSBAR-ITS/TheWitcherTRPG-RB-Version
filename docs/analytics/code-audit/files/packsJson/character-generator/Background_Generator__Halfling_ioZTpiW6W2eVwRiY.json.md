# packsJson/character-generator/Background_Generator__Halfling_ioZTpiW6W2eVwRiY.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator/Background_Generator__Halfling_ioZTpiW6W2eVwRiY.json](../../../../../../packsJson/character-generator/Background_Generator__Halfling_ioZTpiW6W2eVwRiY.json) |
| Тип файла | JSON: экспорт RollTable; 8 TableResult (2 text, 6 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, be1c48770219a6d2871259f12c30d93636aac646 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.056](../../../../../tasks/task-0003.056.md); 13 файлов / 2435 строк; этот файл — 223 строк |
| Запись перекрёстной сверки | [TASK-0003.056](../../../review-log.md#task-0003056) |
| SHA-256 файла | e3eb0f4bf5bd7711757fc00583fbe26f4315e05f0df87d3786b9a5cce2097b8d |

## Назначение файла

Выбирает происхождение полурослика и собирает семью, число братьев/сестёр и профессию. Имя документа — `Background Generator: Halfling`. Результат работы — текстовые TableResult и сообщение; создание персонажа как Actor, его вещей или ActiveEffect этим файлом не реализовано.

## Условия использования

[system.json](../../../../../../system.json):32–38,58–63 регистрирует Character-gen как RollTable в Character Generation, путь packs/character-generator.db. UUID данного документа — `Compendium.TheWitcherTRPG.Character-gen.RollTable.ioZTpiW6W2eVwRiY`. JSON является экспортом данных, не браузерным модулем.

[utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт каталог в compilePack с recursive:true; [utils/extract.mjs](../../../../../../utils/extract.mjs) выгружает данные обратно. [Контракт путей и CLI](../../utils/packs.mjs.md), [package.json](../../../../../../package.json):7–8. Команды не запускались, наличие экспорта не доказывает состояние живой БД.

Ручной запуск доступен через лист таблицы или меню каталога Foundry; обычная content-link открывает лист, а не бросает таблицу. При рекурсивном выборе другой RollTable происходит отдельный вызов её roll. Права пользователей, реальные пакеты и сторонние модули не проверены.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name / _id / _key | `Background Generator: Halfling`; `ioZTpiW6W2eVwRiY`; `!tables!ioZTpiW6W2eVwRiY` | Название, ID и ключ хранения RollTable |
| results | 8 записей, полный перечень ниже | Локальные ID уникальны у родителя; совпадение с ID другого родителя допустимо |
| formula / replacement / displayRoll | `1d2` / true / false | Выбор по диапазонам, повторение результатов и видимость основного броска в сообщении этой таблицы |
| img | `icons/svg/cave.svg` | Корневая иконка; путь найден в public установленного Foundry |
| description | Полный текст ниже | Отдельное описание таблицы, не дополнительный TableResult |
| flags | `{"better-rolltables":{"table-type":"none","loot-amount-key":""},"core":{}}` | Поля сохранены моделью; параметры better-rolltables не исполняются стандартным RollTable.roll |
| ownership / folder / sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые права и расположение |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.2fQwpgAKFqEzT5uq`; остальные четыре поля null | История происхождения; roll следует documentUuid, не compendiumSource |
| Result type / name / description / documentUuid | text: пустое name, текст в description; document: имя цели, пустое описание и UUID | Строка для показа либо вложенный вызов |
| Result _id / _key | Перечень ID ниже; `!tables.results!ioZTpiW6W2eVwRiY.<id>` | Ключ экспорта; _key не является полем модели Foundry |
| Result range / weight / drawn | Интервалы ниже; weight=1; drawn=false | Выбираются все подходящие range, единичные веса используются нормализацией |
| Result img / flags / _stats | Изображения ниже; flags={}; coreVersion=13.341, пять остальных полей null | Представление и служебные данные |

Описание корня: `<p>In the world of The Witcher your early life can be very important. Not only does it tell you what land you grew up in, but also what kind of environment you lived in, what the people around you were like, and even what skills you learned. This is also the point at which you decide which of the three sides of the Third Northern War you hail from. This may not reflect what side you are on now, but it will tell you what you grew up knowing about the conflict and what people will expect of you.</p>`

Иконки результатов: `icons/svg/d20-grey.svg`, `icons/sundries/flags/banner-silver-white.webp`. Все ресурсы найдены локально; HTTP и видимость для Foundry-службы не установлены. Непустые table-type/loot-amount-key, когда они есть, относятся к пространству better-rolltables и не меняют доказанное стандартное поведение ядра; сам модуль не исполнялся.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `rGAJedctF1vHUm0t` | [1,1] | text | `Origin: Human Lands` | 13–35 |
| 2 | `0dQ3NR8YsZjPzHul` | [1,1] | document | `Origin: Human Lands` | 36–59 |
| 3 | `L1KBkf196CGL9GXv` | [1,1] | document | `Family and Parents: Elderland` | 60–83 |
| 4 | `dsneFT5aK1HggTKQ` | [1,2] | document | `Siblings: Dwarves/Halflings` | 84–107 |
| 5 | `pbEqX2RnJhB453Ch` | [1,2] | document | `Dwarf / Gnome Profession` | 108–131 |
| 6 | `obUPNuwQ20fRhtom` | [2,2] | text | `Elderland Origin:` | 132–154 |
| 7 | `NQvQKUljwbGcZKIk` | [2,2] | document | `Origin: Elderland` | 155–178 |
| 8 | `Lq6SDOHwOyB0ZrZt` | [2,2] | document | `Family and Parents: Elderland` | 179–202 |

Грань 1 выбирает текст Human Lands и Origin: Human Lands; грань 2 — Elderland Origin и Origin: Elderland. В обеих ветвях выбрана Family and Parents: Elderland, общие Siblings: Dwarves/Halflings и Dwarf / Gnome Profession. Это фактическая структура, не вывод о правильности расовых/региональных правил. Порядок общего числа родственников и профессии в ветви 2 предшествует её происхождению. Прямой вызов может достигать глубины 5; обе ветви при добавлении RandomCharacter воспроизвели отказ на длинном пути к Most Influential Friend: Elderland (issue-00320).

Все 2 штатных значения основного кубика покрыты. Порядок совместно выбранных ID соответствует массиву results; одинаковый диапазон не делится по весу между совпавшими записями.

| Значения основного броска | Доля граней | Совместно выбранные ID, в порядке JSON |
| --- | --- | --- |
| 1–1 | 1/2 | `rGAJedctF1vHUm0t`, `0dQ3NR8YsZjPzHul`, `L1KBkf196CGL9GXv`, `dsneFT5aK1HggTKQ`, `pbEqX2RnJhB453Ch` |
| 2–2 | 1/2 | `dsneFT5aK1HggTKQ`, `pbEqX2RnJhB453Ch`, `obUPNuwQ20fRhtom`, `NQvQKUljwbGcZKIk`, `Lq6SDOHwOyB0ZrZt` |

## Основные функции и методы

Собственных функций у JSON нет. Методы определены в Foundry 14.367.0.

| Метод / действие | Что читает и делает | Результат и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | drawn и включительные границы range | Все совпадения; при 0/3 пусто |
| RollTable.roll({recursive, roll}) | По умолчанию `1d2`; recursive=true разрешает ссылки и вызывает innerTable.roll с увеличенным _depth | Результаты раскрываются в порядке JSON; броски детей и их сообщения отдельно не возвращаются |
| RollTable.draw({displayChat}) | Вызывает roll, если готовые results не переданы; затем toMessage | replacement=true сохраняет доступность результатов; сообщение может быть отключено |
| RollTable.normalize({save:false}) | Единичные weight → клон с 1d8 и одиночными диапазонами | Может разрушить составные выдачи и исходные вероятности; при заданной formula автоматически не вызывается |
| TableResult.getHTML / documentToAnchor | Разрешает документную ссылку, обогащает description, передаёт в HBS | При recursive=false ссылки остаются ссылками; клик открывает лист |
| RollTable.toMessage | Описание корня, конечные результаты, displayRoll корневой таблицы | Вложенный displayRoll не управляет родительским сообщением; inline исполняются при обогащении текста |
| RollTableSheet.#onDrawResult | Сначала submit формы, затем roll; передаёт готовую выдачу в draw | Один корневой roll, а не два; при успешном replacement=true кнопка снова включена |
| ClientDocumentMixin._onClickDocumentLink | this.sheet.render(true) | Открывает лист; сам не запускает roll/draw |

Статический граф этого входа без ограничения ядра: 8–11 конечных text, глубина до 5. Все ветви данного прямого входа укладываются в предел _depth≤5; дополнительные внешние уровни нужно считать отдельно. Эти границы получены обходом диапазонов и ссылок, не утверждением о переборе всех случайных сочетаний во время исполнения.

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
| `0dQ3NR8YsZjPzHul`; [1,1] | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.de64KicDG5R7FFO9` | [packsJson/character-generator-sub-tables/Origin__Human_Lands_de64KicDG5R7FFO9.json](../../../../../../packsJson/character-generator-sub-tables/Origin__Human_Lands_de64KicDG5R7FFO9.json); [карточка](../character-generator-sub-tables/Origin__Human_Lands_de64KicDG5R7FFO9.json.md) | documentUuid:56; имя/ID/тип сверены |
| `L1KBkf196CGL9GXv`; [1,1] | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.d7NLtNEdvkagBLOP` | [packsJson/character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json](../../../../../../packsJson/character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json); [карточка](../character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json.md) | documentUuid:80; имя/ID/тип сверены |
| `dsneFT5aK1HggTKQ`; [1,2] | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.Ty1Hs3G4BXkkTu67` | [packsJson/character-generator-sub-tables/Siblings__Dwarves_Halflings_Ty1Hs3G4BXkkTu67.json](../../../../../../packsJson/character-generator-sub-tables/Siblings__Dwarves_Halflings_Ty1Hs3G4BXkkTu67.json); [карточка](../character-generator-sub-tables/Siblings__Dwarves_Halflings_Ty1Hs3G4BXkkTu67.json.md) | documentUuid:104; имя/ID/тип сверены |
| `pbEqX2RnJhB453Ch`; [1,2] | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.TjKh0NMxyyYxjSDt` | [packsJson/character-generator-sub-tables/Dwarf___Gnome_Profession_TjKh0NMxyyYxjSDt.json](../../../../../../packsJson/character-generator-sub-tables/Dwarf___Gnome_Profession_TjKh0NMxyyYxjSDt.json); [карточка](../character-generator-sub-tables/Dwarf___Gnome_Profession_TjKh0NMxyyYxjSDt.json.md) | documentUuid:128; имя/ID/тип сверены |
| `NQvQKUljwbGcZKIk`; [2,2] | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.f17QrlT4P5u8m65o` | [packsJson/character-generator-sub-tables/Origin__Elderland_f17QrlT4P5u8m65o.json](../../../../../../packsJson/character-generator-sub-tables/Origin__Elderland_f17QrlT4P5u8m65o.json); [карточка](../character-generator-sub-tables/Origin__Elderland_f17QrlT4P5u8m65o.json.md) | documentUuid:175; имя/ID/тип сверены |
| `Lq6SDOHwOyB0ZrZt`; [2,2] | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.d7NLtNEdvkagBLOP` | [packsJson/character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json](../../../../../../packsJson/character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json); [карточка](../character-generator-sub-tables/Family_and_Parents__Elderland_d7NLtNEdvkagBLOP.json.md) | documentUuid:199; имя/ID/тип сверены |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Способ использования |
| --- | --- | --- |
| [packsJson/character-generator/Background_Generator__RandomCharacter_CIpykDUYYuJB0zLv.json](../../../../../../packsJson/character-generator/Background_Generator__RandomCharacter_CIpykDUYYuJB0zLv.json) | `bemPGrSsRJpsnjWT`; documentUuid:240; [12,15] | `Background Generator: RandomCharacter` при recursive=true вызывает эту таблицу |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Обработка экспортного каталога при сборке |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–440 | Документ таблицы | Submit → roll → draw готового результата |
| Foundry client/applications/sidebar/tabs/roll-table-directory.mjs:28–33 | Документ таблицы | Пункт меню вызывает draw(displayChat:true) |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Возможное совпадение Item.name с `Background Generator: Halfling` | Общий поиск при экспорте добычи ожидает Item; этот граф выдаёт текст |

Входящие прямые ссылки перечислены выше. Поиск всех 13 имён, ID и имени пакета по module/templates/utils не нашёл прямого программного вызова этих генераторов. Общее совпадение имени в WitcherItem остаётся возможным; повторного исполнения метода для этих имён не было. Отсутствие строки не исключает внешние макросы, другой мир и динамические обращения.

[module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js):133–137 готовит список событий для листа, :154–156 получает существующие profession/homeland/race Items. [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs):51–95 редактирует биографию и события. [module/data/actor/templates/character/general/backgroundData.js](../../../../../../module/data/actor/templates/character/general/backgroundData.js) и [module/data/actor/templates/character/general/lifeEventData.js](../../../../../../module/data/actor/templates/character/general/lifeEventData.js) задают их поля. Это соседний механизм ручного хранения, а не автоматические потребители текстов этого генератора.

## Данные и изменения состояния

roll возвращает Roll и TableResult[] в памяти; при recursive=true все ссылки этого графа доходят до text либо вызов отклоняется по глубине. Повторные draw при replacement=true не меняют drawn. Нормализация save:false создаёт отдельный клон; исходники и модели сохранены.

draw с показом чата вызывает ChatMessage.create и может вычислить inline во вложенном description; displayRoll относится только к основному Roll. При исключении глубины до toMessage чат не создаётся. Обработчик листа сначала сохраняет форму: в изолированном сценарии submit был фасадом без записи, поэтому отсутствие записей теста не означает отсутствия штатного сохранения формы в полном клиенте.

Обычная content-link только открывает лист. Ни текст расы, ни название профессии/школы, ни бонус/ранение не создают Actor, Item или ActiveEffect. Число братьев/сестёр и указания «за десятилетие» не становятся циклом без внешнего вызова.

## Проверки и доказательства

| Что проверено | Реальное действие / источник | Результат | Предел |
| --- | --- | --- | --- |
| Полный файл и схема | Строгий Python JSON, реальные модели ядра | 8 results, все поля и resource paths; имя/ID/UUID согласованы | Экспорт не сравнивался с DB |
| Основной выбор | Настоящий roll(recursive:false) | Все 2 значений, ID сопоставлены независимо по raw range | Не доказывает все вложенные сочетания |
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

[issue-00320](../../../../../issues/potential/issue-00320.md) — полный RandomCharacter превышает глубину 5 на длинных семейных путях. Прямые Human/Halfling проходят; ветки остальных рас проверены отдельно.

[issue-00039](../../../../../issues/potential/issue-00039.md) относится к отдельному общему потребителю добычи; [issue-00313](../../../../../issues/potential/issue-00313.md), [issue-00314](../../../../../issues/potential/issue-00314.md), [issue-00315](../../../../../issues/potential/issue-00315.md) — к утилитам извлечения. Они не доказывают дефект конкретного JSON. При выполнении TASK-0003.056 новых issues не создано; issue-00320 дополнена, статусы potential и отсутствие исправлений сохранены.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | be1c48770219a6d2871259f12c30d93636aac646; полный файл и перечисленные связи | Первичная карточка; [протокол TASK-0003.056](../../../review-log.md#task-0003056) |
