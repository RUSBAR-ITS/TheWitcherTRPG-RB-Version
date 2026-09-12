# packsJson/character-generator-sub-tables/Parental_Fate__Elderland_jZVPaCIoQxFZiyRu.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator-sub-tables/Parental_Fate__Elderland_jZVPaCIoQxFZiyRu.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Elderland_jZVPaCIoQxFZiyRu.json) |
| Тип файла | JSON: экспорт RollTable, 21 TableResult (10 text, 11 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 63e9a79fefa7743fcf709b2fa19ddbe144f353a0 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.054](../../../../../tasks/task-0003.054.md); 35 файлов / 8319 строк; этот файл — 524 строк |
| Запись перекрёстной сверки | [TASK-0003.054](../../../review-log.md#task-0003054) |
| SHA-256 файла | 3da13d11508b247d37c7d5eae22b22a3ecd9ebd385c14005bc9628c1e91caa24 |

## Назначение файла

Выбирает судьбу родителей старших рас, затронутого родителя, семейное положение и знакомого. Имя документа — `Parental Fate: Elderland`. Это экспорт таблицы для получения текста и раскрытия ссылок; собственных изменений параметров Actor, создания вещей или сущностей биографии в данных нет.

## Условия использования

[system.json](../../../../../../system.json):35,64–69 объявляет RollTable-пакет Character-gen_Sub-tables и packs/character-generator-sub-tables.db. [utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 читает этот каталог через compilePack с recursive:true; фактическое разрешение имени пути описано в [карточке утилиты](../../utils/packs.mjs.md). JSON не подключён как браузерный ES-модуль.

Адрес по манифесту и ID — `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.jZVPaCIoQxFZiyRu`. Штатный лист/каталог Foundry вызывает draw; другой генератор может получить таблицу через documentUuid. При стандартном recursive:true выбираются конечные текстовые результаты, при false документные записи остаются ссылками. Наличие экспорта не доказывает состояние установленной БД или доступ пользователя.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Parental Fate: Elderland`; `jZVPaCIoQxFZiyRu`; `!tables!jZVPaCIoQxFZiyRu` | Имя, идентификатор и ключ корневого RollTable |
| results | 21 вложенных документов, полный перечень ниже | Локальные ID уникальны внутри родителя; порядок определяет порядок выбранных результатов |
| formula, replacement, displayRoll | 1d10, true, true | Бросок выбора, сохранение доступности результатов и показ основного броска в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание отдельно ниже | Корневая иконка и дополнительный текст таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Сохранённые пространства флагов; настроек автоматизации внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.wgUfc4KauY2AF8cH`; systemId/systemVersion/duplicateSource/exportSource=null | История экспорта; источник происхождения не используется рекурсивным roll |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые настройки доступа и расположения |
| Result type, name, description, documentUuid | text: пустое name и заполненный description; document: имя цели, пустой description и UUID | Текст для вывода либо ссылка, которую roll может раскрыть |
| Result _id, _key | ID ниже; `!tables.results!jZVPaCIoQxFZiyRu.<resultId>` | Уникальные ключи вложенных документов; _key не входит в toObject модели |
| Result range, weight, drawn | Интервалы ниже; все weight=1, drawn=false | Выбираются все подходящие диапазоны; normalize использует веса |
| Result img, flags, _stats | Обычно text=d20-black, document=d20-grey; flags={}; coreVersion=13.341, пять остальных полей null | Иконка и служебные данные каждого результата |

Root description: Пустая строка.

Иконки результатов: Все text используют icons/svg/d20-black.svg; все document используют icons/svg/d20-grey.svg. Все указанные иконки найдены в public/icons установленного ядра. В этой группе четыре таблицы количества братьев/сестёр используют корневые изображения знамён; правила выбора иконки проверены отдельно от HTTP-доступа.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `WLL4GH2QBfngXygQ` | [1,1] | text | `Parental Fate: One or more of your parents died in one of the Northern Wars. He may have already been in the military or he may have been conscripted into service during that war.` | 10–32 |
| 2 | `k0AliUujlhUKLN0G` | [1,1] | document | `Family Status: Elderland` | 33–56 |
| 3 | `uxEsX6eym5hKf3yX` | [1,10] | document | `Which Parent` | 57–80 |
| 4 | `4h4Sw8Y1i17AihjX` | [2,2] | text | `Parental Fate: One or more of your parents were poisoned. This may have been the work of a professional rival, or it may have been to get your parents out of the way.` | 81–103 |
| 5 | `ITgHqKEQCar6G6Et` | [2,2] | document | `Family Status: Elderland` | 104–127 |
| 6 | `5VXUJzVqGqVahzfy` | [3,3] | text | `Parental Fate: The secret police took your parent or parents for ‘questioning.’ The next week their bodies were found hung in the streets of the city` | 128–150 |
| 7 | `ONmmUjbSaveNjrSy` | [3,3] | document | `Family Status: Elderland` | 151–174 |
| 8 | `oQQUBuaPK1pTABqq` | [4,4] | text | `Parental Fate: One or more of your parents were killed by a rogue mage. Most likely they tried to turn the mage in question in to the Empire and paid the price.` | 175–197 |
| 9 | `R36SexxMtQ1y3Mct` | [4,4] | document | `Family Status: Elderland` | 198–221 |
| 10 | `SdTrfAZtLN9cLgew` | [5,5] | text | `Parental Fate: One or more of your parents were imprisoned for unlawful magic. Maybe they actually commited the crime or maybe it was a setup.` | 222–244 |
| 11 | `fbee84iwrEvwp5A7` | [5,5] | document | `Family Status: Elderland` | 245–268 |
| 12 | `7yYGp4SSAi9ymCGL` | [6,6] | text | `Parental Fate: One or more of your parents were exiled to the Korath Desert. Likely they committed a major crime but killing them would cause trouble.` | 269–291 |
| 13 | `AErFz1jut68I9mna` | [6,6] | document | `Family Status: Elderland` | 292–315 |
| 14 | `ts84cRjou8LMlLD4` | [7,7] | text | `Parental Fate: One or more of your parents were cursed by a mage. The mage likely had a vendetta against them.` | 316–338 |
| 15 | `fb47S0gLn0cLA2eD` | [7,7] | document | `Family Status: Elderland` | 339–362 |
| 16 | `LEz6AVGxGmTiJS5K` | [8,8] | text | `Parental Fate: Your parents simply left you one day. You may not even know why they did it. One day your parents just disappeared.` | 363–385 |
| 17 | `98Ry4FUdzahLh10P` | [8,8] | document | `Family Status: Elderland` | 386–409 |
| 18 | `X4C3zlEyKnAX96jL` | [9,9] | text | `Parental Fate: One or more of your parents were enslaved. They either commited a crime against the Empire or were set up by a rival.` | 410–432 |
| 19 | `P2j9J9NLbtkzp04u` | [9,9] | document | `Family Status: Elderland` | 433–456 |
| 20 | `XEB17msQM6PA4Wl4` | [10,10] | text | `Parental Fate: One or more of your parents were sent to the North as double agents. You likely don’t even know where they are now, but they’re serving the Emperor.` | 457–479 |
| 21 | `uW7X6oeT6MO1gf6G` | [10,10] | document | `Family Status: Elderland` | 480–503 |

На любой грани выбираются три исходные записи: судьба, Which Parent [1,10] и Family Status: Elderland; статус дополнительно выбирает знакомого, всего четыре текста. Все десять текстов судьбы совпадают с Nilfgaard; здесь статус присутствует также на исходе 10. На исходе 1 порядок: судьба, статус, знакомый, Which Parent; на 2–10: Which Parent, судьба, статус, знакомый. Совпадение текста или перестановка не проверялись на соответствие рулбуку.

## Основные функции и методы

Собственных функций у JSON нет; методы ниже определены в Foundry 14.367.0.

| Метод | Вход, действия и результат | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Находит все записи с drawn=false и диапазоном, включающим value | Порядок соответствует JSON; при 0 и 11 массив пуст |
| RollTable.roll({recursive}) | Исполняет 1d10; при recursive:true разрешает documentUuid на RollTable и раскрывает вложенный roll | Стандартно recursive=true; без подготовки чата; заданная formula не требует нормализации |
| RollTable.draw({displayChat}) | Вызывает roll, затем toMessage при displayChat=true | Все replacement=true: результаты остаются доступными; сообщение — отдельное действие |
| RollTable.normalize({save:false}) | По 21 единичным весам создаёт клон с 1d21 и одиночными диапазонами | Меняет формулу/диапазоны; для составных выдач разделяет совместно выбранные записи; save=true записал бы изменения |
| TableResult.getHTML / documentToAnchor | Готовит описание и ссылку на документ | enrichHTML может обрабатывать разметку; inline-выражений и текстовых UUID здесь нет |
| RollTable.toMessage | Сочетает собственный description, выбранные результаты и HTML броска при displayRoll=true | Настройка displayRoll вложенного документа не управляет сообщением родителя; ChatMessage.create пишет чат в полном клиенте |

При прямом запуске с _depth=0 число конечных text по структуре связей составляет 4; максимальная внутренняя глубина — 2 переходов. Это границы, рассчитанные по всем ветвям экспортного графа, а не перебор всех сочетаний случайных чисел во время исполнения. В ядре глубина более 5 вызывает исключение: дополнительный внешний генератор учитывается в том же счётчике.

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
| `k0AliUujlhUKLN0G`, строка 53 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |
| `uxEsX6eym5hKf3yX`, строка 77 | [Which Parent](Which_Parent_7fAXpaJLFwlWxkWX.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.7fAXpaJLFwlWxkWX` |
| `ITgHqKEQCar6G6Et`, строка 124 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |
| `ONmmUjbSaveNjrSy`, строка 171 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |
| `R36SexxMtQ1y3Mct`, строка 218 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |
| `fbee84iwrEvwp5A7`, строка 265 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |
| `AErFz1jut68I9mna`, строка 312 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |
| `fb47S0gLn0cLA2eD`, строка 359 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |
| `98Ry4FUdzahLh10P`, строка 406 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |
| `P2j9J9NLbtkzp04u`, строка 453 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |
| `uW7X6oeT6MO1gf6G`, строка 500 | [Family Status: Elderland](Family_Status__Elderland_GOp8mGE4MiGaqjk2.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.GOp8mGE4MiGaqjk2` |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/character-generator-sub-tables/Parents__Elderland_zSTMrICDELIRaNyL.json](../../../../../../packsJson/character-generator-sub-tables/Parents__Elderland_zSTMrICDELIRaNyL.json) | `a6YCIDdtwpoL5ytY`; строка 100; range=[2,2] | При recursive:true вызывает эту RollTable |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение при сборке каталога |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Стандартные действия пользователя вызывают draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Совпадение Item.name с `Parental Fate: Elderland` | Условный поиск при экспорте добычи; метод ожидает Item, а данный граф выдаёт text |

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
