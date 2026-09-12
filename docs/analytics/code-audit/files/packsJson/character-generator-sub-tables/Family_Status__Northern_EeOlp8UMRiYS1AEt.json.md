# packsJson/character-generator-sub-tables/Family_Status__Northern_EeOlp8UMRiYS1AEt.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator-sub-tables/Family_Status__Northern_EeOlp8UMRiYS1AEt.json](../../../../../../packsJson/character-generator-sub-tables/Family_Status__Northern_EeOlp8UMRiYS1AEt.json) |
| Тип файла | JSON: экспорт RollTable, 14 TableResult (7 text, 7 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 63e9a79fefa7743fcf709b2fa19ddbe144f353a0 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.054](../../../../../tasks/task-0003.054.md); 35 файлов / 8319 строк; этот файл — 359 строк |
| Запись перекрёстной сверки | [TASK-0003.054](../../../review-log.md#task-0003054) |
| SHA-256 файла | 40d382f1783354f7d95ee2ce7aca65f25b2e704d155bd1e1a34bd461eb14bfee |

## Назначение файла

Выбирает семейное положение на Севере и влиятельного знакомого этого региона. Имя документа — `Family Status: Northern`. Это экспорт таблицы для получения текста и раскрытия ссылок; собственных изменений параметров Actor, создания вещей или сущностей биографии в данных нет.

## Условия использования

[system.json](../../../../../../system.json):35,64–69 объявляет RollTable-пакет Character-gen_Sub-tables и packs/character-generator-sub-tables.db. [utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 читает этот каталог через compilePack с recursive:true; фактическое разрешение имени пути описано в [карточке утилиты](../../utils/packs.mjs.md). JSON не подключён как браузерный ES-модуль.

Адрес по манифесту и ID — `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt`. Штатный лист/каталог Foundry вызывает draw; другой генератор может получить таблицу через documentUuid. При стандартном recursive:true выбираются конечные текстовые результаты, при false документные записи остаются ссылками. Наличие экспорта не доказывает состояние установленной БД или доступ пользователя.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Family Status: Northern`; `EeOlp8UMRiYS1AEt`; `!tables!EeOlp8UMRiYS1AEt` | Имя, идентификатор и ключ корневого RollTable |
| results | 14 вложенных документов, полный перечень ниже | Локальные ID уникальны внутри родителя; порядок определяет порядок выбранных результатов |
| formula, replacement, displayRoll | 1d10, true, false | Бросок выбора, сохранение доступности результатов и показ основного броска в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание отдельно ниже | Корневая иконка и дополнительный текст таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Сохранённые пространства флагов; настроек автоматизации внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.K0GQBcaCqzLKVuuu`; systemId/systemVersion/duplicateSource/exportSource=null | История экспорта; источник происхождения не используется рекурсивным roll |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые настройки доступа и расположения |
| Result type, name, description, documentUuid | text: пустое name и заполненный description; document: имя цели, пустой description и UUID | Текст для вывода либо ссылка, которую roll может раскрыть |
| Result _id, _key | ID ниже; `!tables.results!EeOlp8UMRiYS1AEt.<resultId>` | Уникальные ключи вложенных документов; _key не входит в toObject модели |
| Result range, weight, drawn | Интервалы ниже; все weight=1, drawn=false | Выбираются все подходящие диапазоны; normalize использует веса |
| Result img, flags, _stats | Обычно text=d20-black, document=d20-grey; flags={}; coreVersion=13.341, пять остальных полей null | Иконка и служебные данные каждого результата |

Root description: `<p>Everyone grows up differently. One man may come of age in a palace, as the son of a king, while another toils as a slave in the vineyard of a wealthy man. Your family status can tell a lot about how you grew up and what kind of person you turn out to be.</p>`.

Иконки результатов: Все text используют icons/svg/d20-black.svg; все document используют icons/svg/d20-grey.svg. Все указанные иконки найдены в public/icons установленного ядра. В этой группе четыре таблицы количества братьев/сестёр используют корневые изображения знамён; правила выбора иконки проверены отдельно от HTTP-доступа.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `5nnfEB4exhLKU2mN` | [1,1] | text | `Family Status: Aristocracy - You grew up in a noble manor with servants to wait on you, but you were always expected to behave and impress. Starting Gear: Paper of Nobility (+2 Reputation)` | 10–32 |
| 2 | `vox7NUbtHmyKyBxI` | [1,1] | document | `Most Influential Friend: Northern` | 33–56 |
| 3 | `VlrPIguiOBBjm4bm` | [2,2] | text | `Family Status: Adopted by a Mage - You were given to a mage at a young age. You lived in comfort but barely saw your caretaker, who was always busy. Starting Gear: A Chronicle (+1 Education)` | 57–79 |
| 4 | `KN1jkgllBFtZX23D` | [2,2] | document | `Most Influential Friend: Northern` | 80–103 |
| 5 | `IsRY79j4twFs8apC` | [3,3] | text | `Family Status: Knights - You grew up in a manor where you learned to be a proper lady or lord. Your fate was set from birth. Starting Gear: Personal Heraldry (+1 Reputation)` | 104–126 |
| 6 | `NQNctkYs5dmyGEkh` | [3,3] | document | `Most Influential Friend: Northern` | 127–150 |
| 7 | `d6KS3R5eEDFIeMmw` | [4,4] | text | `Family Status: Merchant Family - You grew up among merchants and you were always surrounded by yelling, haggling, and money. Starting Gear: 2 Acquaintances` | 151–173 |
| 8 | `LojwHWtEWxxqb6PZ` | [4,4] | document | `Most Influential Friend: Northern` | 174–197 |
| 9 | `BPTQOqaS1Ccdyifj` | [5,5] | text | `Family Status: Artisan Family - You grew up in an artisan’s workshop. Your days were filled with the incessant sounds of creation, and often long. Starting Gear: 3 Common Diagrams/Formulae` | 198–220 |
| 10 | `0bRV83bCJSU0qETV` | [5,5] | document | `Most Influential Friend: Northern` | 221–244 |
| 11 | `HMOPPekiY08124lE` | [6,7] | text | `Family Status: Entertainer Family - You grew up with a band of performers. You may have traveled or you may have performed at a theater. Starting Gear: 1 Instrument &amp; 1 Friend` | 245–267 |
| 12 | `mvqP5Ic7KBewbj2x` | [6,7] | document | `Most Influential Friend: Northern` | 268–291 |
| 13 | `AvyV1RxSjBFrzpUx` | [8,10] | text | `Family Status: Peasant Family - You grew up on a farm in the countryside. You didn’t have much to your name and your life was simple, but dangerous. Starting Gear: A Lucky Token (+1 Luck)` | 292–314 |
| 14 | `YEQ2wdEvKm0Eamde` | [8,10] | document | `Most Influential Friend: Northern` | 315–338 |

Семь групп диапазонов: 1,2,3,4,5,6–7,8–10. В каждой одновременно выбираются описание и Most Influential Friend: Northern; после рекурсии всегда два текста. Вероятности групп: пять раз по 10%, затем 20% и 30%. Начальные вещи и бонусы описаны текстом. normalize по 14 весам превращает пары в раздельные результаты на 1d14.

## Основные функции и методы

Собственных функций у JSON нет; методы ниже определены в Foundry 14.367.0.

| Метод | Вход, действия и результат | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Находит все записи с drawn=false и диапазоном, включающим value | Порядок соответствует JSON; при 0 и 11 массив пуст |
| RollTable.roll({recursive}) | Исполняет 1d10; при recursive:true разрешает documentUuid на RollTable и раскрывает вложенный roll | Стандартно recursive=true; без подготовки чата; заданная formula не требует нормализации |
| RollTable.draw({displayChat}) | Вызывает roll, затем toMessage при displayChat=true | Все replacement=true: результаты остаются доступными; сообщение — отдельное действие |
| RollTable.normalize({save:false}) | По 14 единичным весам создаёт клон с 1d14 и одиночными диапазонами | Меняет формулу/диапазоны; для составных выдач разделяет совместно выбранные записи; save=true записал бы изменения |
| TableResult.getHTML / documentToAnchor | Готовит описание и ссылку на документ | enrichHTML может обрабатывать разметку; inline-выражений и текстовых UUID здесь нет |
| RollTable.toMessage | Сочетает собственный description, выбранные результаты и HTML броска при displayRoll=false | Настройка displayRoll вложенного документа не управляет сообщением родителя; ChatMessage.create пишет чат в полном клиенте |

При прямом запуске с _depth=0 число конечных text по структуре связей составляет 2; максимальная внутренняя глубина — 1 переходов. Это границы, рассчитанные по всем ветвям экспортного графа, а не перебор всех сочетаний случайных чисел во время исполнения. В ядре глубина более 5 вызывает исключение: дополнительный внешний генератор учитывается в том же счётчике.

## Используемые сущности и зависимости

| Сущность | Файл-источник / API | Вид связи и доказательство |
| --- | --- | --- |
| packs, packFolders | [system.json](../../../../../../system.json) | Регистрация имени, RollTable-типа и пути пакета |
| compilePack / extractPack | [utils/packs.mjs](../../../../../../utils/packs.mjs); [utils/extract.mjs](../../../../../../utils/extract.mjs); [package.json](../../../../../../package.json) | Утилиты подготовки/извлечения экспортов; в этой порции не запускались |
| BaseRollTable / BaseTableResult.defineSchema, EmbeddedCollection | Foundry common/documents/roll-table.mjs:43–62; table-result.mjs:48–68; common/abstract/embedded-collection.mjs | Реальные строгие модели приняли все документы |
| Roll, Die, RollParser, grammar | Foundry client/dice/roll.mjs; terms/die.mjs; parser.mjs; grammar.pegjs | Реальный парсер, границы и броски; случайные значения задавались контролируемо |
| roll/draw/getResultsForRoll; parseUuid/fromUuid | Foundry client/documents/roll-table.mjs:98–143,264–342; common/utils/helpers.mjs | Выбор, вложенные переходы и ограничение глубины; адреса разрешались в памяти |
| getHTML / documentToAnchor; HBS | Foundry client/documents/table-result.mjs:45–78; templates/sheets/roll-table/result-details.hbs; templates/dice/table-result.hbs | Настоящие методы и шаблоны; enrichHTML/anchor документа и persistence подменены |
| TextEditor.enrichHTML | Foundry client/applications/ux/text-editor.mjs:123–177 | Штатная граница обработки описаний; полный DOM-обход в этой порции не исполнялся |

Пути Foundry указаны относительно /opt/foundryvtt; ядро не входит в файловый реестр системы.

Исходящие ссылки, по одной строке на каждый document-результат. Повтор одного UUID в разных диапазонах сохраняется как несколько рёбер выбора.

| Результат / строка documentUuid | Целевая карточка | Полный адрес |
| --- | --- | --- |
| `vox7NUbtHmyKyBxI`, строка 53 | [Most Influential Friend: Northern](Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.Xc9k6o8pE8Aaj1Kb` |
| `KN1jkgllBFtZX23D`, строка 100 | [Most Influential Friend: Northern](Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.Xc9k6o8pE8Aaj1Kb` |
| `NQNctkYs5dmyGEkh`, строка 147 | [Most Influential Friend: Northern](Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.Xc9k6o8pE8Aaj1Kb` |
| `LojwHWtEWxxqb6PZ`, строка 194 | [Most Influential Friend: Northern](Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.Xc9k6o8pE8Aaj1Kb` |
| `0bRV83bCJSU0qETV`, строка 241 | [Most Influential Friend: Northern](Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.Xc9k6o8pE8Aaj1Kb` |
| `mvqP5Ic7KBewbj2x`, строка 288 | [Most Influential Friend: Northern](Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.Xc9k6o8pE8Aaj1Kb` |
| `YEQ2wdEvKm0Eamde`, строка 335 | [Most Influential Friend: Northern](Most_Influential_Friend__Northern_Xc9k6o8pE8Aaj1Kb.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.Xc9k6o8pE8Aaj1Kb` |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | `k0AliUujlhUKLN0G`; строка 53; range=[1,1] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | `B0JK9mSkUpWrjcOB`; строка 100; range=[2,2] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | `hMZ7vrUqgV5iYDPW`; строка 147; range=[3,3] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | `9kRFTeQ6eDlOgwZb`; строка 194; range=[4,4] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | `Q8sLmAt8bKK8BWRp`; строка 241; range=[5,5] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | `trQNJUPaqmlb4D1o`; строка 288; range=[6,6] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | `tg5VZvn8eAUQnoSe`; строка 335; range=[7,7] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | `zElZkUwk38v4bhFL`; строка 382; range=[8,8] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) | `pRe4GfbvORQ8CTW5`; строка 429; range=[9,9] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `k0AliUujlhUKLN0G`; строка 77; range=[1,1] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `4rdoDwGz0wBAjMd4`; строка 124; range=[2,2] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `FzlIPuYLQUIFylD2`; строка 171; range=[3,3] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `NOryJpUPsim4TBIl`; строка 218; range=[4,4] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `wGk7wO8LIMj1MIDi`; строка 265; range=[5,5] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `myUH8N8CACHDNfix`; строка 312; range=[6,6] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `Wj1hOzK6VPbOXzD3`; строка 359; range=[7,7] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `H0tuujpiZTAPQIh7`; строка 406; range=[8,8] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `1I77bAtmso3hsZz4`; строка 453; range=[9,9] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) | `hm5UwJX1IhhUTLzr`; строка 500; range=[10,10] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parents__Northern_SGuXziIZzzst1LVJ.json](../../../../../../packsJson/character-generator-sub-tables/Parents__Northern_SGuXziIZzzst1LVJ.json) | `MWl2EoIWD33CT3oV`; строка 53; range=[1,1] | При recursive:true вызывает эту RollTable |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение при сборке каталога |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Стандартные действия пользователя вызывают draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Совпадение Item.name с `Family Status: Northern` | Условный поиск при экспорте добычи; метод ожидает Item, а данный граф выдаёт text |

Поиск пакета, ID, UUID и имён выполнен по module/templates/utils, system.json и всем 226 packsJson. Статических вызовов этих таблиц из программного кода системы и связей со style/lifepath не найдено. Общий поиск по имени в WitcherItem остаётся возможным; его поведение с этим набором определено чтением метода и формой реально полученных результатов, без повторного исполнения самого метода.

[module/data/actor/templates/character/general/backgroundData.js](../../../../../../module/data/actor/templates/character/general/backgroundData.js) хранит биографию как HTMLField; [module/data/actor/templates/character/general/homelandData.js](../../../../../../module/data/actor/templates/character/general/homelandData.js) — строковые value/otherValue. [module/data/item/homelandData.js](../../../../../../module/data/item/homelandData.js) и [module/data/item/professionData.js](../../../../../../module/data/item/professionData.js) задают самостоятельные Item-модели. [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js):154–156 выбирает принадлежащие Actor предметы, а [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs):7–25,51–53 показывает родину и редактор биографии. Присваивания результата этой таблицы перечисленным полям/предметам не найдено; тематическое соответствие не является вызовом или импортом.

## Данные и изменения состояния

JSON хранит RollTable и вложенные TableResult. После прямого roll/draw в проверенных сценариях исходные модели и drawn не изменились; displayChat=false не создавал сообщение. В полном клиенте обычный draw сохраняет ChatMessage, но текст награды, родственника, профессии или бонуса сам по себе не создаёт соответствующий документ.

Шанс каждой отдельной записи определяется шириной её range относительно 10 равновероятных граней. При перекрытии выбираются все записи; сумма их отдельных вероятностей не обязана равняться 100%. Одинаковые тексты с разными ID остаются отдельными результатами. Системные флаги этой таблицы не задают отдельной обработки описанных правил.

## Проверки и доказательства

В общей порции выполнена структурная сверка всех 35 JSON / 313 результатов, каждого значения в таблицах карточек, 79 внутренних и 27 прямых входящих внешних ссылок. Дубликатов JSON-ключей, локальных ID внутри родителя и полных ключей хранения не найдено; все существующие documentUuid указывают на согласованные ID, имена и тип RollTable.

Изолированный сценарий через node --input-type=module и stdin: 3263 утверждения, 281 исход основных формул, 562 повторных draw без чата, 70 draw моделей без pack и 305 перехваченных сообщений. Прямо достигнуты все 313 записей; normalize(save:false), drawn и сохранность моделей проверены для каждого файла. Для рекурсии выполнены все исходы каждой вызываемой напрямую таблицы и отдельные длинные цепочки; все сочетания вложенных бросков не перебирались.

Отдельный сценарий из 18 утверждений проверил предел внешней цепочки RandomCharacter: три воспроизведённых исключения на глубине 6 и четыре успешных контроля на глубине 5. [Методика, конкретные пути и результаты](../../../review-log.md#task-0003054).

## Непроверенные участки и открытые вопросы

Не запускались мир, полный браузер, HTTP, compile/extract, установка пакетов или запись БД. Настоящие модели/методы/формулы и HBS исполнены с фасадами ClientDocumentMixin, UUID-хранилища, enrichHTML, document anchor, Roll.render и ChatMessage.create. Результат фасада не доказывает внешний вид интерфейса, установленное содержимое pack и права игроков.

Соответствие текстов/чисел рулбукам, переводы и литературная редактура исключены. Пять прямых внешних генераторов и RandomCharacter точечно проверены как потребители; полные карточки этих файлов остаются TASK-0003.056. Внешние модули и макросы могут добавлять обработку.

## Связанные проблемы

[issue-00320](../../../../../issues/potential/issue-00320.md): семейная цепочка через RandomCharacter достигает глубины 6 и обрывается у Most Influential Friend. Прямой вызов этой таблицы и более короткие маршруты не равнозначны ошибочному пути. [issue-00039](../../../../../issues/potential/issue-00039.md) описывает предположения общего потребителя добычи о results[0]; таблица не обещает Item. [issue-00313](../../../../../issues/potential/issue-00313.md) относится к предварительной очистке корневых JSON перед извлечением. Исходники и статусы прежних issues не изменены.

## История актуализации

- 2026-09-12 — полный технический разбор в TASK-0003.054: структура, все результаты, индивидуальные отличия, зависимости и перекрёстная сверка; JSON сохранён.
