# packsJson/lifepath/Allies__Generator_Va7NF10ETcMvndFo.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/lifepath/Allies__Generator_Va7NF10ETcMvndFo.json](../../../../../../packsJson/lifepath/Allies__Generator_Va7NF10ETcMvndFo.json) |
| Тип файла | JSON: экспорт RollTable, 5 TableResult (0 text, 5 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.053](../../../../../tasks/task-0003.053.md); 21 файл / 3845 строк, этот файл — 150 строк |
| Запись перекрёстной сверки | [TASK-0003.053](../../../review-log.md#task-0003053) |
| SHA-256 файла | 027004168cd5457d394ee75b3e73e4a7b88737a4f476e787041666987144f89e |

Актуализация [issue-00001](../../../../../issues/open/issue-00001.md), 2026-09-16: Внутренние UUID направлены на TheWitcherTRPG-RB-Version. ID документов, диапазоны, эффекты и _stats сохранены. Датированные результаты и прежние значения UUID ниже являются историей.

## Назначение файла

Собирает описание союзника из пяти подтаблиц: гендер, положение, знакомство, близость и местонахождение. Имя RollTable — `Allies: Generator`. Последствия в описаниях служат информацией для пользователя; исполнительных changes, эффектов и обработчиков Actor в JSON нет.

## Условия использования

[system.json](../../../../../../system.json):37,76–81 регистрирует RollTable-пакет Life_Event_Sub-tables с путём packs/lifepath.db. [utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт packsJson/lifepath в compilePack с recursive:true; браузер читает документы пакета, а не импортирует этот JSON. Нормализация суффикса .db и контракт CLI установлены в [карточке утилиты](../../utils/packs.mjs.md). Компиляция и извлечение здесь не запускались.

Адрес по манифесту и ID: `Compendium.TheWitcherTRPG-RB-Version.Life_Event_Sub-tables.RollTable.Va7NF10ETcMvndFo`. Штатный draw доступен через лист/каталог таблиц; внешние потребители могут разрешить UUID или найти документ по имени. Экспорт не подтверждает совпадение с действующей БД и права конкретного игрока.

## Введённые сущности и действия с ними

| Сущность / поля | Значение и место | Действия |
| --- | --- | --- |
| name, _id, _key | `Allies: Generator`; `Va7NF10ETcMvndFo`; `!tables!Va7NF10ETcMvndFo` | Имя документа, идентификатор и ключ хранилища |
| results | 5 вложенных TableResult; полный список ниже | Собственные ID уникальны внутри родителя; порядок сохраняется при выборе |
| formula, replacement, displayRoll | `1d1`, true, false | Формула выбора; повторное получение разрешено; настройка HTML основного броска в собственном сообщении |
| img, description | icons/svg/d20-grey.svg; пустая строка | Иконка и дополнительное описание корневой таблицы |
| type, name, description | text: name пуст, description заполнен; document: name цели, description пуст | Текст проходит enrichHTML; документная ссылка может быть раскрыта рекурсией |
| documentUuid | 5 ссылок, перечислены ниже | Адрес цели есть только у document-результатов |
| range, weight, drawn | Диапазоны ниже; все weight=1, drawn=false | Выбор по range; веса используются normalize; экспортные записи доступны |
| Result img, flags, _stats | text: d20-black; document: d20-grey; flags={}; coreVersion=13.341, остальные пять полей null | Метаданные вложенного документа |
| Result _key | `!tables.results!Va7NF10ETcMvndFo.<resultId>` | Отдельный ключ каждого результата; входит в экспорт, отбрасывается toObject модели |
| flags | better-rolltables={}, core={} | Пустые пространства флагов, настроек автоматизации не содержат |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.bLSfyUmSTKxz4odd`; systemId/systemVersion/duplicateSource/exportSource=null | История экспорта; compendiumSource не используется для вложенного броска |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые настройки доступа и расположения |

Число ключей: 14 у корня, 11 у text и 12 у document. Встроенные результаты не являются отдельными файлами. В нескольких таблицах локальные ID совпадают; полные UUID включают родителя и различаются.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `q0DM4FW7XCnFdKZu` | [1,1] | document | `Allies: Gender` | 10–33 |
| 2 | `mp0F0yfLeczgHYKB` | [1,1] | document | `Allies: Position` | 34–57 |
| 3 | `a90EHPhkX2hszHH8` | [1,1] | document | `Allies: How You Met` | 58–81 |
| 4 | `KgpE0Q8gz4x0tE9A` | [1,1] | document | `Allies: Closeness` | 82–105 |
| 5 | `ph4JxbZMB7MniZZ5` | [1,1] | document | `Allies: Where Are They?` | 106–129 |

Все пять результатов имеют диапазон [1,1] и выбираются одновременно. recursive:false возвращает пять document-результатов; recursive:true раскрывает их в пять текстов в порядке записей. normalize построит 1d5 с выбором одной подтаблицы и изменит смысл генератора.

## Основные функции и методы

Собственных функций у JSON нет. Потребляющие методы принадлежат Foundry 14.367.0:

| Метод | Вход и результат для этого файла | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Выбирает все доступные записи, диапазон которых содержит value | drawn=true исключается; weight не является дополнительным множителем |
| RollTable.roll({recursive}) | Исполняет 1d1; text возвращается, document на RollTable при recursive:true заменяется результатами вложенного roll | По умолчанию recursive=true; заданная formula не запускает normalize; сам roll не готовит чат и inline-броски |
| RollTable.draw({displayChat}) | При необходимости вызывает roll и затем toMessage | replacement=true сохраняет доступность; displayChat=false отключает сообщение |
| RollTable.normalize({save:false}) | Строит 1d5 и последовательные диапазоны по 5 единичным весам | Возвращает клон без записи; save=true обновил бы документ |
| TableResult.getHTML / RollTable.toMessage | Готовят описание/ссылку и HTML результата, затем ChatMessage | displayRoll=false действует у таблицы, создающей сообщение; у вложенной таблицы свой чат не создаётся |
| TextEditor._enrichInlineRolls / _createInlineRoll | В description этого файла выражений [[…]] нет | Изменение Actor текстом не выполняется; клик по готовому inline-result раскрывает детали броска |

## Используемые сущности и зависимости

| Сущность | Файл-источник / API | Вид связи и основание |
| --- | --- | --- |
| packs, packFolders | [system.json](../../../../../../system.json) | Регистрация имени, RollTable-типа и пути пакета |
| compilePack / extractPack | [utils/packs.mjs](../../../../../../utils/packs.mjs); [utils/extract.mjs](../../../../../../utils/extract.mjs); [package.json](../../../../../../package.json) | Чтение экспортов при сборке, обратное создание JSON при извлечении; команды не запускались |
| BaseRollTable / BaseTableResult.defineSchema, EmbeddedCollection | Foundry common/documents/roll-table.mjs:43–62; table-result.mjs:48–68; common/abstract/embedded-collection.mjs | Декларативные данные реально загружены строгими моделями |
| Roll, RollParser, Die, grammar | Foundry client/dice/roll.mjs; parser.mjs; terms/die.mjs; grammar.pegjs | Исполнение формулы и модификаторов кубика |
| roll/draw/getResultsForRoll; parseUuid; fromUuid | Foundry client/documents/roll-table.mjs:98–143,264–342; common/utils/helpers.mjs | Выбор и рекурсия; UUID разрешались в памяти по реальным ID и пакетам |
| getHTML / documentToAnchor | Foundry client/documents/table-result.mjs:45–78 | Подготовка текста и ссылки; оболочка клиентского документа и anchor документа подменены |
| _enrichInlineRolls / _createInlineRoll; Roll.toAnchor | Foundry client/applications/ux/text-editor.mjs:247–251,718–775; client/dice/roll.mjs:1021–1034 | Выполнены реальные методы и парсер; обход DOM заменён последовательной обработкой строк |
| Шаблоны результата и чата | Foundry templates/sheets/roll-table/result-details.hbs; templates/dice/table-result.hbs | Настоящие HBS-шаблоны исполнены; запись ChatMessage и HTML основного кубика подменены |
| `q0DM4FW7XCnFdKZu`: `Allies: Gender` | [Allies__Gender_QFHhoiXtIBYkL8Rd.json](Allies__Gender_QFHhoiXtIBYkL8Rd.json.md) | `Compendium.TheWitcherTRPG-RB-Version.Life_Event_Sub-tables.RollTable.QFHhoiXtIBYkL8Rd`; recursive:true раскрывает RollTable, false сохраняет ссылку |
| `mp0F0yfLeczgHYKB`: `Allies: Position` | [Allies__Position_5sroduMneFqG9INx.json](Allies__Position_5sroduMneFqG9INx.json.md) | `Compendium.TheWitcherTRPG-RB-Version.Life_Event_Sub-tables.RollTable.5sroduMneFqG9INx`; recursive:true раскрывает RollTable, false сохраняет ссылку |
| `a90EHPhkX2hszHH8`: `Allies: How You Met` | [Allies__How_You_Met_BqAizN8u9r6nMSyK.json](Allies__How_You_Met_BqAizN8u9r6nMSyK.json.md) | `Compendium.TheWitcherTRPG-RB-Version.Life_Event_Sub-tables.RollTable.BqAizN8u9r6nMSyK`; recursive:true раскрывает RollTable, false сохраняет ссылку |
| `KgpE0Q8gz4x0tE9A`: `Allies: Closeness` | [Allies__Closeness_IswiqefPmaHECa5X.json](Allies__Closeness_IswiqefPmaHECa5X.json.md) | `Compendium.TheWitcherTRPG-RB-Version.Life_Event_Sub-tables.RollTable.IswiqefPmaHECa5X`; recursive:true раскрывает RollTable, false сохраняет ссылку |
| `ph4JxbZMB7MniZZ5`: `Allies: Where Are They?` | [Allies__Where_Are_They__W19e7rtl3ycrMhQU.json](Allies__Where_Are_They__W19e7rtl3ycrMhQU.json.md) | `Compendium.TheWitcherTRPG-RB-Version.Life_Event_Sub-tables.RollTable.W19e7rtl3ycrMhQU`; recursive:true раскрывает RollTable, false сохраняет ссылку |

Пути ядра указаны относительно /opt/foundryvtt; эти внешние файлы не получают карточек системы. Имена, типы и ID всех перечисленных целей совпали; исходящие связи этого файла остаются внутри Life_Event_Sub-tables. Общая глубина графа и входящие связи проверены в [протоколе](../../../review-log.md#task-0003053).

## Известные потребители

| Файл / компонент | Используемые данные | Условия |
| --- | --- | --- |
| [packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json](../../../../../../packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json) | `cUNRbBflCqmrkzp7`, documentUuid:54; диапазон [2,2] | При рекурсивном roll обращается к этой таблице |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON / _key | Чтение при компиляции каталога lifepath |
| Foundry roll-table-sheet.mjs:428–438; roll-table-directory.mjs:28–33 | Документ RollTable | Штатные действия roll/draw; пути относительно client/applications/sheets и sidebar/tabs |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Совпадение Item.name с `Allies: Generator` | Условный поиск checkIfItemHasRollTable при экспорте добычи; берёт results[0], а этот набор после рекурсии возвращает текст и не создаёт Item |

Поиск имён, ID и UUID проведён по module/, templates/, utils/, system.json и packsJson. Прямого вызова lifepath-таблиц из программного кода системы и связи с packsJson/style не обнаружено. Общий поиск по имени в WitcherItem остаётся возможным; внешние макросы, модули и данные миров не исследованы.

[module/data/actor/templates/character/general/lifeEventData.js](../../../../../../module/data/actor/templates/character/general/lifeEventData.js) задаёт поля value/details/isOpened; [module/data/actor/templates/character/general/lifeEventsData.js](../../../../../../module/data/actor/templates/character/general/lifeEventsData.js) создаёт двадцать записей. [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs):57–95 редактирует их через форму. Автоматическое присваивание результата RollTable этим полям не найдено. [module/data/actor/templates/common/lifepathData.js](../../../../../../module/data/actor/templates/common/lifepathData.js) задаёт отдельные числовые lifepathModifiers; совпадение тематики с таблицами не образует программную связь.

## Данные и изменения состояния

Исходный JSON хранит таблицу, вложенные результаты и метаданные. При roll/draw в выполненных сценариях сохранились все исходные данные и drawn=false. Получение результата не создаёт союзника/врага, предмет, травму, бонус к навыку или запись биографии. Существующий текст описывает возможные действия пользователя.

Для 1d1 проверены все 1 целых исходов и повторные выборки. getResultsForRoll(0) и (2) возвращает пусто; собственная формула этих значений не даёт. Встроенных бросков в описаниях этого файла нет.

## Проверки и доказательства

В порции выполнены структурная проверка 21 JSON / 139 результатов, сверка каждой записи с этой карточкой, графа 18 внутренних и четырёх внешних ссылок. Дубликатов ключей JSON, локальных ID внутри родителя и полных ключей хранения нет.

Изолированный запуск через node --input-type=module и stdin на настоящих моделях/методах Foundry 14.367.0: 1917 проверок для всей порции, 168 исходов формул, 336 повторных draw без чата, 42 draw моделей без pack, 179 перехваченных сообщений. Все 139 результатов достижимы; записи документов отсутствовали. Для каждой таблицы проверены normalize(save:false), учёт drawn и неизменность исходной модели.

Методика, отдельная проверка формул 1d10x100 / 1d10*100 и индивидуальные результаты — в [журнале](../../../review-log.md#task-0003053). Полный текст всех записей этого файла приведён выше.

## Непроверенные участки и открытые вопросы

Сверка TASK-0004.017 завершила граф всех 128 RollTable, связи основных генераторов и границу с уже разобранными Item-травмами (.012). Прежние .052–.057/.061 сохраняют даты и фасады.  Остаток: [U017-01](../../../cross-check-0002.md#u017-01), [U017-02](../../../cross-check-0002.md#u017-02), [U017-07](../../../cross-check-0002.md#u017-07); конкретные ответы и границы сведены в [итоге TASK-0004.018](../../../cross-check-0002.md#адресация-126-вопросов-предметных-блоков). Действующие packs/мир, HTTP, полный DOM, пользовательские права и внешние модули/макросы не проверялись. Соответствие контента рулбукам исключено.

## Связанные проблемы

Отдельной новой проблемы этого файла не зарегистрировано. [issue-00039](../../../../../issues/potential/issue-00039.md) касается предположений общего потребителя добычи о results[0]; эта таблица не обещает Item-результаты. [issue-00313](../../../../../issues/potential/issue-00313.md) относится к удалению корневых JSON до успешного извлечения; исходник здесь не изменялся.

## История актуализации

- 2026-09-12 — полный технический разбор в TASK-0003.053; исходник сохранён, выполнена перекрёстная сверка с моделью, потребителями и экспортами соседних пакетов.

## Сквозная сверка TASK-0004.017

2026-09-14; rusbar-main, cdb7bcb08835c62eb84efdfe7356c4eec90aa2e8. Исходник совпадает со срезом TASK-0001; изменено только описание.

Allies: Generator: 1d1, возможные totals 1…1; 5 результатов (0 text / 5 document), replacement=true, displayRoll=false. Рекурсивные переходы: Allies: Gender; Allies: Position; Allies: How You Met; Allies: Closeness; Allies: Where Are They?. По разрешимому графу от этого прямого входа 5–5 конечных текстов, максимальная глубина 1; входящих файлов 1. Inline-выражений в результатах нет.

Сопоставленные определения и потребители: [system.json](../../system.json.md), [utils/packs.mjs](../../utils/packs.mjs.md), [utils/extract.mjs](../../utils/extract.mjs.md), [module/item/witcherItem.js](../../module/item/witcherItem.js.md), [packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json](Allies_and_Enemies_Lp42vhkw20Ys973y.json.md), [packsJson/lifepath/Allies__Gender_QFHhoiXtIBYkL8Rd.json](Allies__Gender_QFHhoiXtIBYkL8Rd.json.md), [packsJson/lifepath/Allies__Position_5sroduMneFqG9INx.json](Allies__Position_5sroduMneFqG9INx.json.md), [packsJson/lifepath/Allies__How_You_Met_BqAizN8u9r6nMSyK.json](Allies__How_You_Met_BqAizN8u9r6nMSyK.json.md), [packsJson/lifepath/Allies__Closeness_IswiqefPmaHECa5X.json](Allies__Closeness_IswiqefPmaHECa5X.json.md), [packsJson/lifepath/Allies__Where_Are_They__W19e7rtl3ycrMhQU.json](Allies__Where_Are_They__W19e7rtl3ycrMhQU.json.md), [module/actor/sheets/WitcherCharacterSheet.js](../../module/actor/sheets/WitcherCharacterSheet.js.md).

[Протокол и границы](../../../review-log.md#task-0004017) — TASK-0004.017; процессы [R017-01](../../../cross-check-0002.md#r017-01), [R017-02](../../../cross-check-0002.md#r017-02), [R017-03](../../../cross-check-0002.md#r017-03), [R017-04](../../../cross-check-0002.md#r017-04), [R017-08](../../../cross-check-0002.md#r017-08). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
