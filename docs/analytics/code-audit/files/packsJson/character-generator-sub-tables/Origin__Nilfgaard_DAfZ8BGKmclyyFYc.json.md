# packsJson/character-generator-sub-tables/Origin__Nilfgaard_DAfZ8BGKmclyyFYc.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator-sub-tables/Origin__Nilfgaard_DAfZ8BGKmclyyFYc.json](../../../../../../packsJson/character-generator-sub-tables/Origin__Nilfgaard_DAfZ8BGKmclyyFYc.json) |
| Тип файла | JSON: экспорт RollTable, 3 TableResult (2 text, 1 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.054](../../../../../tasks/task-0003.054.md); 35 файлов / 8319 строк; этот файл — 100 строк |
| Запись перекрёстной сверки | [TASK-0003.054](../../../review-log.md#task-0003054) |
| SHA-256 файла | b3ec843b5603ca2341ca270bd9ec4ab0428f81aa9cc7e7fc3869040e918a64fd |

Актуализация [issue-00001](../../../../../issues/open/issue-00001.md), 2026-09-16: Внутренние UUID направлены на TheWitcherTRPG-RB-Version. ID документов, диапазоны, эффекты и _stats сохранены. Датированные результаты и прежние значения UUID ниже являются историей.

## Назначение файла

Выбирает сердце Нильфгаарда либо заголовок и вассальное государство из подтаблицы. Имя документа — `Origin: Nilfgaard`. Это экспорт таблицы для получения текста и раскрытия ссылок; собственных изменений параметров Actor, создания вещей или сущностей биографии в данных нет.

## Условия использования

[system.json](../../../../../../system.json):35,64–69 объявляет RollTable-пакет Character-gen_Sub-tables и packs/character-generator-sub-tables.db. [utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 читает этот каталог через compilePack с recursive:true; фактическое разрешение имени пути описано в [карточке утилиты](../../utils/packs.mjs.md). JSON не подключён как браузерный ES-модуль.

Адрес по манифесту и ID — `Compendium.TheWitcherTRPG-RB-Version.Character-gen_Sub-tables.RollTable.DAfZ8BGKmclyyFYc`. Штатный лист/каталог Foundry вызывает draw; другой генератор может получить таблицу через documentUuid. При стандартном recursive:true выбираются конечные текстовые результаты, при false документные записи остаются ссылками. Наличие экспорта не доказывает состояние установленной БД или доступ пользователя.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Origin: Nilfgaard`; `DAfZ8BGKmclyyFYc`; `!tables!DAfZ8BGKmclyyFYc` | Имя, идентификатор и ключ корневого RollTable |
| results | 3 вложенных документов, полный перечень ниже | Локальные ID уникальны внутри родителя; порядок определяет порядок выбранных результатов |
| formula, replacement, displayRoll | 1d10, true, true | Бросок выбора, сохранение доступности результатов и показ основного броска в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание отдельно ниже | Корневая иконка и дополнительный текст таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Сохранённые пространства флагов; настроек автоматизации внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.WylxcMCSIE6tcNz6`; systemId/systemVersion/duplicateSource/exportSource=null | История экспорта; источник происхождения не используется рекурсивным roll |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые настройки доступа и расположения |
| Result type, name, description, documentUuid | text: пустое name и заполненный description; document: имя цели, пустой description и UUID | Текст для вывода либо ссылка, которую roll может раскрыть |
| Result _id, _key | ID ниже; `!tables.results!DAfZ8BGKmclyyFYc.<resultId>` | Уникальные ключи вложенных документов; _key не входит в toObject модели |
| Result range, weight, drawn | Интервалы ниже; все weight=1, drawn=false | Выбираются все подходящие диапазоны; normalize использует веса |
| Result img, flags, _stats | Обычно text=d20-black, document=d20-grey; flags={}; coreVersion=13.341, пять остальных полей null | Иконка и служебные данные каждого результата |

Root description: Пустая строка.

Иконки результатов: `yWqJljl7QFD5RvAg`: `icons/svg/d20-grey.svg`; все document используют icons/svg/d20-grey.svg. Все указанные иконки найдены в public/icons установленного ядра. В этой группе четыре таблицы количества братьев/сестёр используют корневые изображения знамён; правила выбора иконки проверены отдельно от HTTP-доступа.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `nX4mbx8F2ITxvBNF` | [1,3] | text | `Origin: The Heart of Nilfgaard (+1 Deceit)` | 10–32 |
| 2 | `yWqJljl7QFD5RvAg` | [4,10] | text | `Nilfgaard Vassal Origin:` | 33–55 |
| 3 | `cFrOuK1g41ekdakj` | [4,10] | document | `Nilfgaard Vassal Origin` | 56–79 |

1–3: сердце Нильфгаарда (30%); 4–10: заголовок Nilfgaard Vassal Origin и ссылка на одноимённую подтаблицу (70%). Во втором случае два text в итоге. У заголовка явно задан d20-grey, хотя тип text; схема это допускает.

## Основные функции и методы

Собственных функций у JSON нет; методы ниже определены в Foundry 14.367.0.

| Метод | Вход, действия и результат | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Находит все записи с drawn=false и диапазоном, включающим value | Порядок соответствует JSON; при 0 и 11 массив пуст |
| RollTable.roll({recursive}) | Исполняет 1d10; при recursive:true разрешает documentUuid на RollTable и раскрывает вложенный roll | Стандартно recursive=true; без подготовки чата; заданная formula не требует нормализации |
| RollTable.draw({displayChat}) | Вызывает roll, затем toMessage при displayChat=true | Все replacement=true: результаты остаются доступными; сообщение — отдельное действие |
| RollTable.normalize({save:false}) | По 3 единичным весам создаёт клон с 1d3 и одиночными диапазонами | Меняет формулу/диапазоны; для составных выдач разделяет совместно выбранные записи; save=true записал бы изменения |
| TableResult.getHTML / documentToAnchor | Готовит описание и ссылку на документ | enrichHTML может обрабатывать разметку; inline-выражений и текстовых UUID здесь нет |
| RollTable.toMessage | Сочетает собственный description, выбранные результаты и HTML броска при displayRoll=true | Настройка displayRoll вложенного документа не управляет сообщением родителя; ChatMessage.create пишет чат в полном клиенте |

При прямом запуске с _depth=0 число конечных text по структуре связей составляет 1–2; максимальная внутренняя глубина — 1 переходов. Это границы, рассчитанные по всем ветвям экспортного графа, а не перебор всех сочетаний случайных чисел во время исполнения. В ядре глубина более 5 вызывает исключение: дополнительный внешний генератор учитывается в том же счётчике.

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
| `cFrOuK1g41ekdakj`, строка 76 | [Nilfgaard Vassal Origin](Nilfgaard_Vassal_Origin_IEPMPHNGahrfyCWI.json.md) | `Compendium.TheWitcherTRPG-RB-Version.Character-gen_Sub-tables.RollTable.IEPMPHNGahrfyCWI` |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json](../../../../../../packsJson/character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json) | `NQvQKUljwbGcZKIk`; строка 175; range=[2,2] | При recursive:true вызывает эту RollTable |
| [packsJson/character-generator-sub-tables/Origin__Human_Lands_de64KicDG5R7FFO9.json](../../../../../../packsJson/character-generator-sub-tables/Origin__Human_Lands_de64KicDG5R7FFO9.json) | `yWqJljl7QFD5RvAg`; строка 54; range=[2,2] | При recursive:true вызывает эту RollTable |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение при сборке каталога |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Стандартные действия пользователя вызывают draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Совпадение Item.name с `Origin: Nilfgaard` | Условный поиск при экспорте добычи; метод ожидает Item, а данный граф выдаёт text |

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

Сверка TASK-0004.017 завершила граф всех 128 RollTable, связи основных генераторов и границу с уже разобранными Item-травмами (.012). Прежние .052–.057/.061 сохраняют даты и фасады.  Остаток: [U017-01](../../../cross-check-0002.md#u017-01), [U017-02](../../../cross-check-0002.md#u017-02), [U017-07](../../../cross-check-0002.md#u017-07); конкретные ответы и границы сведены в [итоге TASK-0004.018](../../../cross-check-0002.md#адресация-126-вопросов-предметных-блоков). Действующие packs/мир, HTTP, полный DOM, пользовательские права и внешние модули/макросы не проверялись. Соответствие контента рулбукам исключено.

## Связанные проблемы

Отдельного нового дефекта этого файла не зарегистрировано. [issue-00039](../../../../../issues/potential/issue-00039.md) описывает предположения общего потребителя добычи о results[0]; таблица не обещает Item. [issue-00313](../../../../../issues/potential/issue-00313.md) относится к предварительной очистке корневых JSON перед извлечением. Исходники и статусы прежних issues не изменены.

## История актуализации

- 2026-09-12 — полный технический разбор в TASK-0003.054: структура, все результаты, индивидуальные отличия, зависимости и перекрёстная сверка; JSON сохранён.

## Уточнение TASK-0003.056

2026-09-12, rusbar-main be1c48770219a6d2871259f12c30d93636aac646; исходник сохранён. Завершён полный разбор основных генераторов. Ранее описанные входящие ссылки сопоставлены с новыми карточками и реальным рекурсивным выбором:

| Генератор | ID его результата | Строка documentUuid / range |
| --- | --- | --- |
| [Background Generator: Human](../character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json.md) | `NQvQKUljwbGcZKIk` | 175; [2,2] |

В общей сверке пяти пакетов проверены 117 JSON / 929 результатов, 252 ссылки и getHTML всех результатов. Все поля/тексты/UUID данной карточки сопоставлены с источником. Отдельные случайные комбинации не перебирались полностью; реальные пакеты, мир и права игроков не проверялись. [Протокол .056](../../../review-log.md#task-0003056).

## Сквозная сверка TASK-0004.017

2026-09-14; rusbar-main, cdb7bcb08835c62eb84efdfe7356c4eec90aa2e8. Исходник совпадает со срезом TASK-0001; изменено только описание.

Origin: Nilfgaard: 1d10, возможные totals 1…10; 3 результатов (2 text / 1 document), replacement=true, displayRoll=true. Рекурсивные переходы: Nilfgaard Vassal Origin. По разрешимому графу от этого прямого входа 1–2 конечных текстов, максимальная глубина 1; входящих файлов 2. Inline-выражений в результатах нет.

Сопоставленные определения и потребители: [system.json](../../system.json.md), [utils/packs.mjs](../../utils/packs.mjs.md), [utils/extract.mjs](../../utils/extract.mjs.md), [module/item/witcherItem.js](../../module/item/witcherItem.js.md), [packsJson/character-generator-sub-tables/Origin__Human_Lands_de64KicDG5R7FFO9.json](Origin__Human_Lands_de64KicDG5R7FFO9.json.md), [packsJson/character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json](../character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json.md), [packsJson/character-generator-sub-tables/Nilfgaard_Vassal_Origin_IEPMPHNGahrfyCWI.json](Nilfgaard_Vassal_Origin_IEPMPHNGahrfyCWI.json.md), [module/data/item/homelandData.js](../../module/data/item/homelandData.js.md), [module/data/item/professionData.js](../../module/data/item/professionData.js.md), [module/actor/sheets/WitcherCharacterSheet.js](../../module/actor/sheets/WitcherCharacterSheet.js.md).

[Протокол и границы](../../../review-log.md#task-0004017) — TASK-0004.017; процессы [R017-01](../../../cross-check-0002.md#r017-01), [R017-02](../../../cross-check-0002.md#r017-02), [R017-03](../../../cross-check-0002.md#r017-03), [R017-04](../../../cross-check-0002.md#r017-04), [R017-11](../../../cross-check-0002.md#r017-11). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
