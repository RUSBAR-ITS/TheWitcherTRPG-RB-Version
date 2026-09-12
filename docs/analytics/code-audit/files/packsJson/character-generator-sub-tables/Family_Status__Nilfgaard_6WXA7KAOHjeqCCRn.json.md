# packsJson/character-generator-sub-tables/Family_Status__Nilfgaard_6WXA7KAOHjeqCCRn.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator-sub-tables/Family_Status__Nilfgaard_6WXA7KAOHjeqCCRn.json](../../../../../../packsJson/character-generator-sub-tables/Family_Status__Nilfgaard_6WXA7KAOHjeqCCRn.json) |
| Тип файла | JSON: экспорт RollTable, 14 TableResult (7 text, 7 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 63e9a79fefa7743fcf709b2fa19ddbe144f353a0 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.054](../../../../../tasks/task-0003.054.md); 35 файлов / 8319 строк; этот файл — 359 строк |
| Запись перекрёстной сверки | [TASK-0003.054](../../../review-log.md#task-0003054) |
| SHA-256 файла | a3ad1211129a65a8a786f9ddd060fa1ac55a4e71223e9a44befab33900cd12bb |

## Назначение файла

Выбирает семейное положение в Нильфгаарде и влиятельного знакомого этого региона. Имя документа — `Family Status: Nilfgaard`. Это экспорт таблицы для получения текста и раскрытия ссылок; собственных изменений параметров Actor, создания вещей или сущностей биографии в данных нет.

## Условия использования

[system.json](../../../../../../system.json):35,64–69 объявляет RollTable-пакет Character-gen_Sub-tables и packs/character-generator-sub-tables.db. [utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 читает этот каталог через compilePack с recursive:true; фактическое разрешение имени пути описано в [карточке утилиты](../../utils/packs.mjs.md). JSON не подключён как браузерный ES-модуль.

Адрес по манифесту и ID — `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.6WXA7KAOHjeqCCRn`. Штатный лист/каталог Foundry вызывает draw; другой генератор может получить таблицу через documentUuid. При стандартном recursive:true выбираются конечные текстовые результаты, при false документные записи остаются ссылками. Наличие экспорта не доказывает состояние установленной БД или доступ пользователя.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Family Status: Nilfgaard`; `6WXA7KAOHjeqCCRn`; `!tables!6WXA7KAOHjeqCCRn` | Имя, идентификатор и ключ корневого RollTable |
| results | 14 вложенных документов, полный перечень ниже | Локальные ID уникальны внутри родителя; порядок определяет порядок выбранных результатов |
| formula, replacement, displayRoll | 1d10, true, false | Бросок выбора, сохранение доступности результатов и показ основного броска в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание отдельно ниже | Корневая иконка и дополнительный текст таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Сохранённые пространства флагов; настроек автоматизации внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.AZM9P0e4192Tcf5m`; systemId/systemVersion/duplicateSource/exportSource=null | История экспорта; источник происхождения не используется рекурсивным roll |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые настройки доступа и расположения |
| Result type, name, description, documentUuid | text: пустое name и заполненный description; document: имя цели, пустой description и UUID | Текст для вывода либо ссылка, которую roll может раскрыть |
| Result _id, _key | ID ниже; `!tables.results!6WXA7KAOHjeqCCRn.<resultId>` | Уникальные ключи вложенных документов; _key не входит в toObject модели |
| Result range, weight, drawn | Интервалы ниже; все weight=1, drawn=false | Выбираются все подходящие диапазоны; normalize использует веса |
| Result img, flags, _stats | Обычно text=d20-black, document=d20-grey; flags={}; coreVersion=13.341, пять остальных полей null | Иконка и служебные данные каждого результата |

Root description: `<p>Everyone grows up differently. One man may come of age in a palace, as the son of a king, while another toils as a slave in the vineyard of a wealthy man. Your family status can tell a lot about how you grew up and what kind of person you turn out to be.</p>`.

Иконки результатов: Все text используют icons/svg/d20-black.svg; все document используют icons/svg/d20-grey.svg. Все указанные иконки найдены в public/icons установленного ядра. В этой группе четыре таблицы количества братьев/сестёр используют корневые изображения знамён; правила выбора иконки проверены отдельно от HTTP-доступа.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `5nnfEB4exhLKU2mN` | [1,1] | text | `Family Status: Aristocracy - You grew up in a manor, training to be well-versed in the world of the court. The luxury was just your incentive. Starting Gear: Paper of Nobility (+2 Reputation)` | 10–32 |
| 2 | `YKSa1ZWzSmILymvX` | [1,1] | document | `Most Influential Friend: Nilfgaard` | 33–56 |
| 3 | `VlrPIguiOBBjm4bm` | [2,2] | text | `Family Status: High Clergy - You were raised among the clergy of the Great Sun. You grew up pious and always aware that the Church would guide you. Starting Gear: A Holy Symbol (+1 Courage)` | 57–79 |
| 4 | `lisAkdcM9LZzCIFB` | [2,2] | document | `Most Influential Friend: Nilfgaard` | 80–103 |
| 5 | `IsRY79j4twFs8apC` | [3,3] | text | `Family Status: Knights - You grew up knowing that your duty was to the Emperor, and that all of your luxury was a reward for your eventual service. Starting Gear: Personal Heraldry (+1 Reputation)` | 104–126 |
| 6 | `bjZwAmuqXpNKHjAg` | [3,3] | document | `Most Influential Friend: Nilfgaard` | 127–150 |
| 7 | `d6KS3R5eEDFIeMmw` | [4,4] | text | `Family Status: Artisan Family - You grew up in an artisan’s shop, learning to craft products for sale around the world. You learned the value of quality. Starting Gear: 3 Common Diagrams/Formulae` | 151–173 |
| 8 | `vZecLds1BUXGxeQg` | [4,4] | document | `Most Influential Friend: Nilfgaard` | 174–197 |
| 9 | `BPTQOqaS1Ccdyifj` | [5,5] | text | `Family Status: Merchant Family - You grew up selling products all around the Empire. You saw all kinds exotic of goods from all around the world. Starting Gear: 2 Acquaintances` | 198–220 |
| 10 | `srTNN36Ce2HHSisB` | [5,5] | document | `Most Influential Friend: Nilfgaard` | 221–244 |
| 11 | `HMOPPekiY08124lE` | [6,7] | text | `Family Status: Born into Servitude - You were born into servitude and lived in simple quarters. You owned very little and toiled often. Starting Gear: A trained bird or serpent` | 245–267 |
| 12 | `ye32sHyFgcEeHX1J` | [6,7] | document | `Most Influential Friend: Nilfgaard` | 268–291 |
| 13 | `AvyV1RxSjBFrzpUx` | [8,10] | text | `Family Status: Peasant Family - You grew up on one of the thousands of farms across the Empire. You had little to your name but life was simple. Starting Gear: A Lucky Token (+1 Luck)` | 292–314 |
| 14 | `6jOqPsAISSRQJWuL` | [8,10] | document | `Most Influential Friend: Nilfgaard` | 315–338 |

Семь групп диапазонов: 1,2,3,4,5,6–7,8–10. В каждой одновременно выбираются описание и Most Influential Friend: Nilfgaard; после рекурсии всегда два текста. Вероятности групп: пять раз по 10%, затем 20% и 30%. Начальные вещи и бонусы описаны текстом. normalize по 14 весам превращает пары в раздельные результаты на 1d14.

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
| `YKSa1ZWzSmILymvX`, строка 53 | [Most Influential Friend: Nilfgaard](Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.8R2zAqegJcbDr4xB` |
| `lisAkdcM9LZzCIFB`, строка 100 | [Most Influential Friend: Nilfgaard](Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.8R2zAqegJcbDr4xB` |
| `bjZwAmuqXpNKHjAg`, строка 147 | [Most Influential Friend: Nilfgaard](Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.8R2zAqegJcbDr4xB` |
| `vZecLds1BUXGxeQg`, строка 194 | [Most Influential Friend: Nilfgaard](Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.8R2zAqegJcbDr4xB` |
| `srTNN36Ce2HHSisB`, строка 241 | [Most Influential Friend: Nilfgaard](Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.8R2zAqegJcbDr4xB` |
| `ye32sHyFgcEeHX1J`, строка 288 | [Most Influential Friend: Nilfgaard](Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.8R2zAqegJcbDr4xB` |
| `6jOqPsAISSRQJWuL`, строка 335 | [Most Influential Friend: Nilfgaard](Most_Influential_Friend__Nilfgaard_8R2zAqegJcbDr4xB.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.8R2zAqegJcbDr4xB` |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json](../../../../../../packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json) | `JQeprlU3cojjnCY0`; строка 124; range=[2,2] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | `k0AliUujlhUKLN0G`; строка 53; range=[1,1] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | `ITgHqKEQCar6G6Et`; строка 124; range=[2,2] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | `ONmmUjbSaveNjrSy`; строка 171; range=[3,3] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | `R36SexxMtQ1y3Mct`; строка 218; range=[4,4] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | `fbee84iwrEvwp5A7`; строка 265; range=[5,5] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | `AErFz1jut68I9mna`; строка 312; range=[6,6] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | `fb47S0gLn0cLA2eD`; строка 359; range=[7,7] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | `98Ry4FUdzahLh10P`; строка 406; range=[8,8] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Nilfgaard_wFuCDleU9PzP00mf.json) | `P2j9J9NLbtkzp04u`; строка 453; range=[9,9] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Parents__Nilfgaard_Nnf1BMSJOnc5Mx3m.json](../../../../../../packsJson/character-generator-sub-tables/Parents__Nilfgaard_Nnf1BMSJOnc5Mx3m.json) | `MWl2EoIWD33CT3oV`; строка 53; range=[1,1] | При recursive:true вызывает эту RollTable |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение при сборке каталога |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Стандартные действия пользователя вызывают draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Совпадение Item.name с `Family Status: Nilfgaard` | Условный поиск при экспорте добычи; метод ожидает Item, а данный граф выдаёт text |

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
