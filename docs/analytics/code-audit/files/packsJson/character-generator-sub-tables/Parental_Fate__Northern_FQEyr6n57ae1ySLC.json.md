# packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json](../../../../../../packsJson/character-generator-sub-tables/Parental_Fate__Northern_FQEyr6n57ae1ySLC.json) |
| Тип файла | JSON: экспорт RollTable, 21 TableResult (10 text, 11 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 63e9a79fefa7743fcf709b2fa19ddbe144f353a0 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.054](../../../../../tasks/task-0003.054.md); 35 файлов / 8319 строк; этот файл — 524 строк |
| Запись перекрёстной сверки | [TASK-0003.054](../../../review-log.md#task-0003054) |
| SHA-256 файла | 668a83433571ceba4db7e4bdfdfb0f57709bf4fdb4b6a46367290eb1c9488248 |

## Назначение файла

Выбирает судьбу северных родителей, затронутого родителя, семейное положение и знакомого. Имя документа — `Parental Fate: Northern`. Это экспорт таблицы для получения текста и раскрытия ссылок; собственных изменений параметров Actor, создания вещей или сущностей биографии в данных нет.

## Условия использования

[system.json](../../../../../../system.json):35,64–69 объявляет RollTable-пакет Character-gen_Sub-tables и packs/character-generator-sub-tables.db. [utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 читает этот каталог через compilePack с recursive:true; фактическое разрешение имени пути описано в [карточке утилиты](../../utils/packs.mjs.md). JSON не подключён как браузерный ES-модуль.

Адрес по манифесту и ID — `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.FQEyr6n57ae1ySLC`. Штатный лист/каталог Foundry вызывает draw; другой генератор может получить таблицу через documentUuid. При стандартном recursive:true выбираются конечные текстовые результаты, при false документные записи остаются ссылками. Наличие экспорта не доказывает состояние установленной БД или доступ пользователя.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Parental Fate: Northern`; `FQEyr6n57ae1ySLC`; `!tables!FQEyr6n57ae1ySLC` | Имя, идентификатор и ключ корневого RollTable |
| results | 21 вложенных документов, полный перечень ниже | Локальные ID уникальны внутри родителя; порядок определяет порядок выбранных результатов |
| formula, replacement, displayRoll | 1d10, true, true | Бросок выбора, сохранение доступности результатов и показ основного броска в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание отдельно ниже | Корневая иконка и дополнительный текст таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Сохранённые пространства флагов; настроек автоматизации внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.hB2TyQLaQWwvXRhL`; systemId/systemVersion/duplicateSource/exportSource=null | История экспорта; источник происхождения не используется рекурсивным roll |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые настройки доступа и расположения |
| Result type, name, description, documentUuid | text: пустое name и заполненный description; document: имя цели, пустой description и UUID | Текст для вывода либо ссылка, которую roll может раскрыть |
| Result _id, _key | ID ниже; `!tables.results!FQEyr6n57ae1ySLC.<resultId>` | Уникальные ключи вложенных документов; _key не входит в toObject модели |
| Result range, weight, drawn | Интервалы ниже; все weight=1, drawn=false | Выбираются все подходящие диапазоны; normalize использует веса |
| Result img, flags, _stats | Обычно text=d20-black, document=d20-grey; flags={}; coreVersion=13.341, пять остальных полей null | Иконка и служебные данные каждого результата |

Root description: Пустая строка.

Иконки результатов: Все text используют icons/svg/d20-black.svg; все document используют icons/svg/d20-grey.svg. Все указанные иконки найдены в public/icons установленного ядра. В этой группе четыре таблицы количества братьев/сестёр используют корневые изображения знамён; правила выбора иконки проверены отдельно от HTTP-доступа.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `WLL4GH2QBfngXygQ` | [1,1] | text | `Parental Fate: One or more of your parents were killed in the Northern Wars. Most likely your father, but it is also possible that your mother fought or was a casualty.` | 10–32 |
| 2 | `uxEsX6eym5hKf3yX` | [1,10] | document | `Which Parent` | 33–56 |
| 3 | `k0AliUujlhUKLN0G` | [1,1] | document | `Family Status: Northern` | 57–80 |
| 4 | `4h4Sw8Y1i17AihjX` | [2,2] | text | `Parental Fate: One or more of your parents left you in the wilderness to fend for yourself. Maybe they couldn’t afford to keep you; maybe you were an accident.` | 81–103 |
| 5 | `4rdoDwGz0wBAjMd4` | [2,2] | document | `Family Status: Northern` | 104–127 |
| 6 | `5VXUJzVqGqVahzfy` | [3,3] | text | `Parental Fate: One or more of your parents were cursed by a mage or due to the intense hatred of someone they encountered. The curse took their life.` | 128–150 |
| 7 | `FzlIPuYLQUIFylD2` | [3,3] | document | `Family Status: Northern` | 151–174 |
| 8 | `oQQUBuaPK1pTABqq` | [4,4] | text | `Parental Fate: One or more of your parents sold you for coin, or perhaps traded you for some goods or service. Your parents needed the money more than you.` | 175–197 |
| 9 | `NOryJpUPsim4TBIl` | [4,4] | document | `Family Status: Northern` | 198–221 |
| 10 | `SdTrfAZtLN9cLgew` | [5,5] | text | `Parental Fate: One or more of your parents joined a gang. You saw this gang often and were sometimes forced to work with them.` | 222–244 |
| 11 | `wGk7wO8LIMj1MIDi` | [5,5] | document | `Family Status: Northern` | 245–268 |
| 12 | `7yYGp4SSAi9ymCGL` | [6,6] | text | `Parental Fate: One or more of your parents were killed by monsters. It is your decision as to what they may have fallen prey to.` | 269–291 |
| 13 | `myUH8N8CACHDNfix` | [6,6] | document | `Family Status: Northern` | 292–315 |
| 14 | `ts84cRjou8LMlLD4` | [7,7] | text | `Parental Fate: One or more of your parents were falsely executed. They may have been a scapegoat for something or just in the wrong place.` | 316–338 |
| 15 | `Wj1hOzK6VPbOXzD3` | [7,7] | document | `Family Status: Northern` | 339–362 |
| 16 | `LEz6AVGxGmTiJS5K` | [8,8] | text | `Parental Fate: One or more of your parents died of a plague. There was nothing that could be done but try to ease their passing.` | 363–385 |
| 17 | `H0tuujpiZTAPQIh7` | [8,8] | document | `Family Status: Northern` | 386–409 |
| 18 | `X4C3zlEyKnAX96jL` | [9,9] | text | `Parental Fate: One or more of your parents defected to Nilfgaard. They may have been given a deal for information or they may just have jumped the border.` | 410–432 |
| 19 | `1I77bAtmso3hsZz4` | [9,9] | document | `Family Status: Northern` | 433–456 |
| 20 | `XEB17msQM6PA4Wl4` | [10,10] | text | `Parental Fate: One or more of your parents were kidnapped by nobles. Likely it was your mother, who attracted the attention of a local lord or his son.` | 457–479 |
| 21 | `hm5UwJX1IhhUTLzr` | [10,10] | document | `Family Status: Northern` | 480–503 |

На любой грани выбираются три исходные записи: судьба, Which Parent [1,10] и Family Status: Northern; статус дополнительно выбирает знакомого, всего четыре текста. На исходе 1 порядок: судьба, Which Parent, статус, знакомый; на 2–10: Which Parent, судьба, статус, знакомый. Совпадение текста или перестановка не проверялись на соответствие рулбуку.

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
| `uxEsX6eym5hKf3yX`, строка 53 | [Which Parent](Which_Parent_7fAXpaJLFwlWxkWX.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.7fAXpaJLFwlWxkWX` |
| `k0AliUujlhUKLN0G`, строка 77 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `4rdoDwGz0wBAjMd4`, строка 124 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `FzlIPuYLQUIFylD2`, строка 171 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `NOryJpUPsim4TBIl`, строка 218 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `wGk7wO8LIMj1MIDi`, строка 265 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `myUH8N8CACHDNfix`, строка 312 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `Wj1hOzK6VPbOXzD3`, строка 359 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `H0tuujpiZTAPQIh7`, строка 406 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `1I77bAtmso3hsZz4`, строка 453 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |
| `hm5UwJX1IhhUTLzr`, строка 500 | [Family Status: Northern](Family_Status__Northern_EeOlp8UMRiYS1AEt.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.EeOlp8UMRiYS1AEt` |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/character-generator-sub-tables/Parents__Northern_SGuXziIZzzst1LVJ.json](../../../../../../packsJson/character-generator-sub-tables/Parents__Northern_SGuXziIZzzst1LVJ.json) | `a6YCIDdtwpoL5ytY`; строка 100; range=[2,2] | При recursive:true вызывает эту RollTable |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение при сборке каталога |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Стандартные действия пользователя вызывают draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Совпадение Item.name с `Parental Fate: Northern` | Условный поиск при экспорте добычи; метод ожидает Item, а данный граф выдаёт text |

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
