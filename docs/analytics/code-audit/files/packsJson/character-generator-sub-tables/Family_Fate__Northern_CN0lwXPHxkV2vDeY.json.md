# packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json](../../../../../../packsJson/character-generator-sub-tables/Family_Fate__Northern_CN0lwXPHxkV2vDeY.json) |
| Тип файла | JSON: экспорт RollTable, 19 TableResult (10 text, 9 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 63e9a79fefa7743fcf709b2fa19ddbe144f353a0 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.054](../../../../../tasks/task-0003.054.md); 35 файлов / 8319 строк; этот файл — 476 строк |
| Запись перекрёстной сверки | [TASK-0003.054](../../../review-log.md#task-0003054) |
| SHA-256 файла | e4d7855b7a9ef0d6216a9f2a3c29529e371e99fa947a1dfaeac8dc8932b0a4b3 |

## Назначение файла

Выбирает судьбу северной семьи; исходы 1–9 дополнительно раскрывают семейное положение и знакомого. Имя документа — `Family Fate: Northern`. Это экспорт таблицы для получения текста и раскрытия ссылок; собственных изменений параметров Actor, создания вещей или сущностей биографии в данных нет.

## Условия использования

[system.json](../../../../../../system.json):35,64–69 объявляет RollTable-пакет Character-gen_Sub-tables и packs/character-generator-sub-tables.db. [utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 читает этот каталог через compilePack с recursive:true; фактическое разрешение имени пути описано в [карточке утилиты](../../utils/packs.mjs.md). JSON не подключён как браузерный ES-модуль.

Адрес по манифесту и ID — `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.CN0lwXPHxkV2vDeY`. Штатный лист/каталог Foundry вызывает draw; другой генератор может получить таблицу через documentUuid. При стандартном recursive:true выбираются конечные текстовые результаты, при false документные записи остаются ссылками. Наличие экспорта не доказывает состояние установленной БД или доступ пользователя.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Family Fate: Northern`; `CN0lwXPHxkV2vDeY`; `!tables!CN0lwXPHxkV2vDeY` | Имя, идентификатор и ключ корневого RollTable |
| results | 19 вложенных документов, полный перечень ниже | Локальные ID уникальны внутри родителя; порядок определяет порядок выбранных результатов |
| formula, replacement, displayRoll | 1d10, true, false | Бросок выбора, сохранение доступности результатов и показ основного броска в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание отдельно ниже | Корневая иконка и дополнительный текст таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Сохранённые пространства флагов; настроек автоматизации внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.zqS5It6nVWTHqhqo`; systemId/systemVersion/duplicateSource/exportSource=null | История экспорта; источник происхождения не используется рекурсивным roll |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые настройки доступа и расположения |
| Result type, name, description, documentUuid | text: пустое name и заполненный description; document: имя цели, пустой description и UUID | Текст для вывода либо ссылка, которую roll может раскрыть |
| Result _id, _key | ID ниже; `!tables.results!CN0lwXPHxkV2vDeY.<resultId>` | Уникальные ключи вложенных документов; _key не входит в toObject модели |
| Result range, weight, drawn | Интервалы ниже; все weight=1, drawn=false | Выбираются все подходящие диапазоны; normalize использует веса |
| Result img, flags, _stats | Обычно text=d20-black, document=d20-grey; flags={}; coreVersion=13.341, пять остальных полей null | Иконка и служебные данные каждого результата |

Root description: Пустая строка.

Иконки результатов: Все text используют icons/svg/d20-black.svg; все document используют icons/svg/d20-grey.svg. Все указанные иконки найдены в public/icons установленного ядра. В этой группе четыре таблицы количества братьев/сестёр используют корневые изображения знамён; правила выбора иконки проверены отдельно от HTTP-доступа.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `WLL4GH2QBfngXygQ` | [1,1] | text | `Family Fate: Your family was scattered to the winds by the wars and you have no idea where most of them are.` | 10–32 |
| 2 | `k0AliUujlhUKLN0G` | [1,1] | document | `Family Status: Northern` | 33–56 |
| 3 | `4h4Sw8Y1i17AihjX` | [2,2] | text | `Family Fate: Your family was imprisoned for crimes or on trumped-up charges. You were the only one to escape. You may want to free them...or maybe not.` | 57–79 |
| 4 | `B0JK9mSkUpWrjcOB` | [2,2] | document | `Family Status: Northern` | 80–103 |
| 5 | `5VXUJzVqGqVahzfy` | [3,3] | text | `Family Fate: Your family house was cursed and now either crops won’t grow or specters roam the halls. It became too dangerous for you to stay in this home.` | 104–126 |
| 6 | `hMZ7vrUqgV5iYDPW` | [3,3] | document | `Family Status: Northern` | 127–150 |
| 7 | `oQQUBuaPK1pTABqq` | [4,4] | text | `Family Fate: With so many wars your family’s livelihood was destroyed. Your family turned to crime to survive.` | 151–173 |
| 8 | `9kRFTeQ6eDlOgwZb` | [4,4] | document | `Family Status: Northern` | 174–197 |
| 9 | `SdTrfAZtLN9cLgew` | [5,5] | text | `Family Fate: Your family accumulated a huge debt through gambling or favors from others. You need money desperately.` | 198–220 |
| 10 | `Q8sLmAt8bKK8BWRp` | [5,5] | document | `Family Status: Northern` | 221–244 |
| 11 | `7yYGp4SSAi9ymCGL` | [6,6] | text | `Family Fate: Your family has fallen into a feud with another family. You may not even remember why this feud started in the first place.` | 245–267 |
| 12 | `trQNJUPaqmlb4D1o` | [6,6] | document | `Family Status: Northern` | 268–291 |
| 13 | `ts84cRjou8LMlLD4` | [7,7] | text | `Family Fate: Due to some action or inaction your family has become hated in your home town and now no one there wants to have anything to do with them.` | 292–314 |
| 14 | `tg5VZvn8eAUQnoSe` | [7,7] | document | `Family Status: Northern` | 315–338 |
| 15 | `LEz6AVGxGmTiJS5K` | [8,8] | text | `Family Fate: One day everything you had was ripped away by a bandit mob. Your family was massacred, leaving you entirely alone.` | 339–361 |
| 16 | `zElZkUwk38v4bhFL` | [8,8] | document | `Family Status: Northern` | 362–385 |
| 17 | `X4C3zlEyKnAX96jL` | [9,9] | text | `Family Fate: Your family has a deep, dark secret that if discovered would ruin you all completely. You can decide what this secret is, or the Game Master can decide.` | 386–408 |
| 18 | `pRe4GfbvORQ8CTW5` | [9,9] | document | `Family Status: Northern` | 409–432 |
| 19 | `XEB17msQM6PA4Wl4` | [10,10] | text | `Family Fate: Your family has come to despise each other. No one you grew up with will talk with each other any more and you’re lucky to get a passing hello from your siblings.` | 433–455 |

На 1–9 одновременно выбираются описание и ссылка на Family Status: Northern; после раскрытия получаются судьба, статус и знакомый. На 10 возвращается только описание, ссылки на статус нет. Это отличие ветвей воспроизведено и сохранено как особенность данных; намеренность и соответствие правилам не установлены.

## Основные функции и методы

Собственных функций у JSON нет; методы ниже определены в Foundry 14.367.0.

| Метод | Вход, действия и результат | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Находит все записи с drawn=false и диапазоном, включающим value | Порядок соответствует JSON; при 0 и 11 массив пуст |
| RollTable.roll({recursive}) | Исполняет 1d10; при recursive:true разрешает documentUuid на RollTable и раскрывает вложенный roll | Стандартно recursive=true; без подготовки чата; заданная formula не требует нормализации |
| RollTable.draw({displayChat}) | Вызывает roll, затем toMessage при displayChat=true | Все replacement=true: результаты остаются доступными; сообщение — отдельное действие |
| RollTable.normalize({save:false}) | По 19 единичным весам создаёт клон с 1d19 и одиночными диапазонами | Меняет формулу/диапазоны; для составных выдач разделяет совместно выбранные записи; save=true записал бы изменения |
| TableResult.getHTML / documentToAnchor | Готовит описание и ссылку на документ | enrichHTML может обрабатывать разметку; inline-выражений и текстовых UUID здесь нет |
| RollTable.toMessage | Сочетает собственный description, выбранные результаты и HTML броска при displayRoll=false | Настройка displayRoll вложенного документа не управляет сообщением родителя; ChatMessage.create пишет чат в полном клиенте |

При прямом запуске с _depth=0 число конечных text по структуре связей составляет 1–3; максимальная внутренняя глубина — 2 переходов. Это границы, рассчитанные по всем ветвям экспортного графа, а не перебор всех сочетаний случайных чисел во время исполнения. В ядре глубина более 5 вызывает исключение: дополнительный внешний генератор учитывается в том же счётчике.

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
| `k0AliUujlhUKLN0G`, строка 53 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `B0JK9mSkUpWrjcOB`, строка 100 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `hMZ7vrUqgV5iYDPW`, строка 147 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `9kRFTeQ6eDlOgwZb`, строка 194 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `Q8sLmAt8bKK8BWRp`, строка 241 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `trQNJUPaqmlb4D1o`, строка 288 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `tg5VZvn8eAUQnoSe`, строка 335 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `zElZkUwk38v4bhFL`, строка 382 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `pRe4GfbvORQ8CTW5`, строка 429 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/character-generator-sub-tables/Family_and_Parents__Northern_xAVQucslVR12q2kc.json](../../../../../../packsJson/character-generator-sub-tables/Family_and_Parents__Northern_xAVQucslVR12q2kc.json) | `rx40q7d9iV7PIvy0`; строка 100; range=[2,2] | При recursive:true вызывает эту RollTable |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение при сборке каталога |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Стандартные действия пользователя вызывают draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Совпадение Item.name с `Family Fate: Northern` | Условный поиск при экспорте добычи; метод ожидает Item, а данный граф выдаёт text |

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

Отдельного нового дефекта этого файла не зарегистрировано. [issue-00039](../../../../../issues/potential/issue-00039.md) описывает предположения общего потребителя добычи о results[0]; таблица не обещает Item. [issue-00313](../../../../../issues/potential/issue-00313.md) относится к предварительной очистке корневых JSON перед извлечением. Исходники и статусы прежних issues не изменены.

## История актуализации

- 2026-09-12 — полный технический разбор в TASK-0003.054: структура, все результаты, индивидуальные отличия, зависимости и перекрёстная сверка; JSON сохранён.
