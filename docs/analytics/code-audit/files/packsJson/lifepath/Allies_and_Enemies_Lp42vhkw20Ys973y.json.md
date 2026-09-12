# packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json](../../../../../../packsJson/lifepath/Allies_and_Enemies_Lp42vhkw20Ys973y.json) |
| Тип файла | JSON: экспорт RollTable, 2 TableResult (0 text, 2 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 93beea0953821c9d8f080f815e686dc4da0c6f9e |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.053](../../../../../tasks/task-0003.053.md); 21 файл / 3845 строк, этот файл — 78 строк |
| Запись перекрёстной сверки | [TASK-0003.053](../../../review-log.md#task-0003053) |
| SHA-256 файла | 1ad565286ce92f99ebbdca368169092d0228fdffac421d9e0379ed26d2e6ada1 |

## Назначение файла

Выбирает генератор врага при 1 или генератор союзника при 2, затем раскрывает выбранный составной результат. Имя RollTable — `Allies and Enemies`. Последствия в описаниях служат информацией для пользователя; исполнительных changes, эффектов и обработчиков Actor в JSON нет.

## Условия использования

[system.json](../../../../../../system.json):37,76–81 регистрирует RollTable-пакет Life_Event_Sub-tables с путём packs/lifepath.db. [utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 передаёт packsJson/lifepath в compilePack с recursive:true; браузер читает документы пакета, а не импортирует этот JSON. Нормализация суффикса .db и контракт CLI установлены в [карточке утилиты](../../utils/packs.mjs.md). Компиляция и извлечение здесь не запускались.

Адрес по манифесту и ID: `Compendium.TheWitcherTRPG.Life_Event_Sub-tables.RollTable.Lp42vhkw20Ys973y`. Штатный draw доступен через лист/каталог таблиц; внешние потребители могут разрешить UUID или найти документ по имени. Экспорт не подтверждает совпадение с действующей БД и права конкретного игрока.

## Введённые сущности и действия с ними

| Сущность / поля | Значение и место | Действия |
| --- | --- | --- |
| name, _id, _key | `Allies and Enemies`; `Lp42vhkw20Ys973y`; `!tables!Lp42vhkw20Ys973y` | Имя документа, идентификатор и ключ хранилища |
| results | 2 вложенных TableResult; полный список ниже | Собственные ID уникальны внутри родителя; порядок сохраняется при выборе |
| formula, replacement, displayRoll | `1d2`, true, false | Формула выбора; повторное получение разрешено; настройка HTML основного броска в собственном сообщении |
| img, description | icons/svg/d20-grey.svg; пустая строка | Иконка и дополнительное описание корневой таблицы |
| type, name, description | text: name пуст, description заполнен; document: name цели, description пуст | Текст проходит enrichHTML; документная ссылка может быть раскрыта рекурсией |
| documentUuid | 2 ссылок, перечислены ниже | Адрес цели есть только у document-результатов |
| range, weight, drawn | Диапазоны ниже; все weight=1, drawn=false | Выбор по range; веса используются normalize; экспортные записи доступны |
| Result img, flags, _stats | text: d20-black; document: d20-grey; flags={}; coreVersion=13.341, остальные пять полей null | Метаданные вложенного документа |
| Result _key | `!tables.results!Lp42vhkw20Ys973y.<resultId>` | Отдельный ключ каждого результата; входит в экспорт, отбрасывается toObject модели |
| flags | better-rolltables={}, core={} | Пустые пространства флагов, настроек автоматизации не содержат |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.eOacMynNDvHOojIe`; systemId/systemVersion/duplicateSource/exportSource=null | История экспорта; compendiumSource не используется для вложенного броска |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые настройки доступа и расположения |

Число ключей: 14 у корня, 11 у text и 12 у document. Встроенные результаты не являются отдельными файлами. В нескольких таблицах локальные ID совпадают; полные UUID включают родителя и различаются.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `JQmqgYHhLo9rqERr` | [1,1] | document | `Enemies: Generator` | 10–33 |
| 2 | `cUNRbBflCqmrkzp7` | [2,2] | document | `Allies: Generator` | 34–57 |

Два диапазона [1,1] и [2,2] выбираются с вероятностью 1/2. Вложенность достигает двух переходов: этот селектор → генератор → листовая таблица. Итоговый массив содержит семь текстов при 1 и пять при 2. В экспортном наборе входящих documentUuid на сам селектор не найдено; доступен прямой вызов/лист.

## Основные функции и методы

Собственных функций у JSON нет. Потребляющие методы принадлежат Foundry 14.367.0:

| Метод | Вход и результат для этого файла | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Выбирает все доступные записи, диапазон которых содержит value | drawn=true исключается; weight не является дополнительным множителем |
| RollTable.roll({recursive}) | Исполняет 1d2; text возвращается, document на RollTable при recursive:true заменяется результатами вложенного roll | По умолчанию recursive=true; заданная formula не запускает normalize; сам roll не готовит чат и inline-броски |
| RollTable.draw({displayChat}) | При необходимости вызывает roll и затем toMessage | replacement=true сохраняет доступность; displayChat=false отключает сообщение |
| RollTable.normalize({save:false}) | Строит 1d2 и последовательные диапазоны по 2 единичным весам | Возвращает клон без записи; save=true обновил бы документ |
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
| `JQmqgYHhLo9rqERr`: `Enemies: Generator` | [Enemies__Generator_7AXmeCSRkK3ktJ9Y.json](Enemies__Generator_7AXmeCSRkK3ktJ9Y.json.md) | `Compendium.TheWitcherTRPG.Life_Event_Sub-tables.RollTable.7AXmeCSRkK3ktJ9Y`; recursive:true раскрывает RollTable, false сохраняет ссылку |
| `cUNRbBflCqmrkzp7`: `Allies: Generator` | [Allies__Generator_Va7NF10ETcMvndFo.json](Allies__Generator_Va7NF10ETcMvndFo.json.md) | `Compendium.TheWitcherTRPG.Life_Event_Sub-tables.RollTable.Va7NF10ETcMvndFo`; recursive:true раскрывает RollTable, false сохраняет ссылку |

Пути ядра указаны относительно /opt/foundryvtt; эти внешние файлы не получают карточек системы. Имена, типы и ID всех перечисленных целей совпали; исходящие связи этого файла остаются внутри Life_Event_Sub-tables. Общая глубина графа и входящие связи проверены в [протоколе](../../../review-log.md#task-0003053).

## Известные потребители

| Файл / компонент | Используемые данные | Условия |
| --- | --- | --- |
| Прямые ссылки из других packsJson | Не найдены | Проверены все 226 экспортов; это не исключает ручного использования |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON / _key | Чтение при компиляции каталога lifepath |
| Foundry roll-table-sheet.mjs:428–438; roll-table-directory.mjs:28–33 | Документ RollTable | Штатные действия roll/draw; пути относительно client/applications/sheets и sidebar/tabs |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Совпадение Item.name с `Allies and Enemies` | Условный поиск checkIfItemHasRollTable при экспорте добычи; берёт results[0], а этот набор после рекурсии возвращает текст и не создаёт Item |

Поиск имён, ID и UUID проведён по module/, templates/, utils/, system.json и packsJson. Прямого вызова lifepath-таблиц из программного кода системы и связи с packsJson/style не обнаружено. Общий поиск по имени в WitcherItem остаётся возможным; внешние макросы, модули и данные миров не исследованы.

[module/data/actor/templates/character/general/lifeEventData.js](../../../../../../module/data/actor/templates/character/general/lifeEventData.js) задаёт поля value/details/isOpened; [module/data/actor/templates/character/general/lifeEventsData.js](../../../../../../module/data/actor/templates/character/general/lifeEventsData.js) создаёт двадцать записей. [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs):57–95 редактирует их через форму. Автоматическое присваивание результата RollTable этим полям не найдено. [module/data/actor/templates/common/lifepathData.js](../../../../../../module/data/actor/templates/common/lifepathData.js) задаёт отдельные числовые lifepathModifiers; совпадение тематики с таблицами не образует программную связь.

## Данные и изменения состояния

Исходный JSON хранит таблицу, вложенные результаты и метаданные. При roll/draw в выполненных сценариях сохранились все исходные данные и drawn=false. Получение результата не создаёт союзника/врага, предмет, травму, бонус к навыку или запись биографии. Существующий текст описывает возможные действия пользователя.

Для 1d2 проверены все 2 целых исходов и повторные выборки. getResultsForRoll(0) и (3) возвращает пусто; собственная формула этих значений не даёт. Встроенных бросков в описаниях этого файла нет.

## Проверки и доказательства

В порции выполнены структурная проверка 21 JSON / 139 результатов, сверка каждой записи с этой карточкой, графа 18 внутренних и четырёх внешних ссылок. Дубликатов ключей JSON, локальных ID внутри родителя и полных ключей хранения нет.

Изолированный запуск через node --input-type=module и stdin на настоящих моделях/методах Foundry 14.367.0: 1917 проверок для всей порции, 168 исходов формул, 336 повторных draw без чата, 42 draw моделей без pack, 179 перехваченных сообщений. Все 139 результатов достижимы; записи документов отсутствовали. Для каждой таблицы проверены normalize(save:false), учёт drawn и неизменность исходной модели.

Методика, отдельная проверка формул 1d10x100 / 1d10*100 и индивидуальные результаты — в [журнале](../../../review-log.md#task-0003053). Полный текст всех записей этого файла приведён выше.

## Непроверенные участки и открытые вопросы

Не запускались мир, полный клиент, сборка/извлечение и запись БД. Полный enrichHTML с настоящим DOM и интерфейс inline-roll не исполнялись: выполнены реальные методы inline-обработки/бросков поверх фасадов строк и DOM-элементов. Перехват ChatMessage не подтверждает сохранённое сообщение или права игроков. Совпадение экспортов с установленными packs не проверялось.

Соответствие текстов/чисел рулбукам, переводы и литературная редактура исключены. Полные карточки внешних генераторов относятся к .055/.056; проверенные здесь входящие связи не увеличивают покрытие этих файлов.

## Связанные проблемы

Отдельной новой проблемы этого файла не зарегистрировано. [issue-00039](../../../../../issues/potential/issue-00039.md) касается предположений общего потребителя добычи о results[0]; эта таблица не обещает Item-результаты. [issue-00313](../../../../../issues/potential/issue-00313.md) относится к удалению корневых JSON до успешного извлечения; исходник здесь не изменялся.

## История актуализации

- 2026-09-12 — полный технический разбор в TASK-0003.053; исходник сохранён, выполнена перекрёстная сверка с моделью, потребителями и экспортами соседних пакетов.
