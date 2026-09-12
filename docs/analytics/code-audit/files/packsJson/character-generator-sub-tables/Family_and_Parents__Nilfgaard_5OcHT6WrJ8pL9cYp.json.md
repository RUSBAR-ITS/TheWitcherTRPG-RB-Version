# packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json

| Поле | Значение |
| --- | --- |
| Исходный файл | [packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json](../../../../../../packsJson/character-generator-sub-tables/Family_and_Parents__Nilfgaard_5OcHT6WrJ8pL9cYp.json) |
| Тип файла | JSON: экспорт RollTable, 5 TableResult (2 text, 3 document) |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 63e9a79fefa7743fcf709b2fa19ddbe144f353a0 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.054](../../../../../tasks/task-0003.054.md); 35 файлов / 8319 строк; этот файл — 148 строк |
| Запись перекрёстной сверки | [TASK-0003.054](../../../review-log.md#task-0003054) |
| SHA-256 файла | 33e10b9ddeca874e5771516eb549994b456b37dda4bd41b3b2cbc8224b93e858 |

## Назначение файла

Составляет сведения о семье и родителях в Нильфгаарде через связанные подтаблицы. Имя документа — `Family and Parents: Nilfgaard`. Это экспорт таблицы для получения текста и раскрытия ссылок; собственных изменений параметров Actor, создания вещей или сущностей биографии в данных нет.

## Условия использования

[system.json](../../../../../../system.json):35,64–69 объявляет RollTable-пакет Character-gen_Sub-tables и packs/character-generator-sub-tables.db. [utils/packs.mjs](../../../../../../utils/packs.mjs):6–10 читает этот каталог через compilePack с recursive:true; фактическое разрешение имени пути описано в [карточке утилиты](../../utils/packs.mjs.md). JSON не подключён как браузерный ES-модуль.

Адрес по манифесту и ID — `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.5OcHT6WrJ8pL9cYp`. Штатный лист/каталог Foundry вызывает draw; другой генератор может получить таблицу через documentUuid. При стандартном recursive:true выбираются конечные текстовые результаты, при false документные записи остаются ссылками. Наличие экспорта не доказывает состояние установленной БД или доступ пользователя.

## Введённые сущности и действия с ними

| Сущность / поля | Значение | Действия и смысл |
| --- | --- | --- |
| name, _id, _key | `Family and Parents: Nilfgaard`; `5OcHT6WrJ8pL9cYp`; `!tables!5OcHT6WrJ8pL9cYp` | Имя, идентификатор и ключ корневого RollTable |
| results | 5 вложенных документов, полный перечень ниже | Локальные ID уникальны внутри родителя; порядок определяет порядок выбранных результатов |
| formula, replacement, displayRoll | 1d2, true, false | Бросок выбора, сохранение доступности результатов и показ основного броска в собственном сообщении |
| img, description | `icons/svg/d20-grey.svg`; описание отдельно ниже | Корневая иконка и дополнительный текст таблицы |
| flags | `{"better-rolltables":{},"core":{}}` | Сохранённые пространства флагов; настроек автоматизации внутри нет |
| _stats | coreVersion=13.341; compendiumSource=`RollTable.l7wOQAP4owJziCHk`; systemId/systemVersion/duplicateSource/exportSource=null | История экспорта; источник происхождения не используется рекурсивным roll |
| ownership, folder, sort | default=0; 2w1nWBDVMXqVbciv=3; null; 0 | Сохранённые настройки доступа и расположения |
| Result type, name, description, documentUuid | text: пустое name и заполненный description; document: имя цели, пустой description и UUID | Текст для вывода либо ссылка, которую roll может раскрыть |
| Result _id, _key | ID ниже; `!tables.results!5OcHT6WrJ8pL9cYp.<resultId>` | Уникальные ключи вложенных документов; _key не входит в toObject модели |
| Result range, weight, drawn | Интервалы ниже; все weight=1, drawn=false | Выбираются все подходящие диапазоны; normalize использует веса |
| Result img, flags, _stats | Обычно text=d20-black, document=d20-grey; flags={}; coreVersion=13.341, пять остальных полей null | Иконка и служебные данные каждого результата |

Root description: Пустая строка.

Иконки результатов: Все text используют icons/svg/d20-black.svg; все document используют icons/svg/d20-grey.svg. Все указанные иконки найдены в public/icons установленного ядра. В этой группе четыре таблицы количества братьев/сестёр используют корневые изображения знамён; правила выбора иконки проверены отдельно от HTTP-доступа.

| № | ID результата | range | type | Точное description для text / name для document | Строки записи |
| --- | --- | --- | --- | --- | --- |
| 1 | `FyjZwFRJUzcqDrwW` | [1,1] | text | `At Least Some of Your Family Is Alive` | 10–32 |
| 2 | `VySuFOPm5I8jY8r9` | [1,1] | document | `Parents: Nilfgaard` | 33–56 |
| 3 | `g4JnOCAOpDRIw8tQ` | [2,2] | text | `Something Happened to Your Family` | 57–79 |
| 4 | `rx40q7d9iV7PIvy0` | [2,2] | document | `Family Fate: Nilfgaard` | 80–103 |
| 5 | `JQeprlU3cojjnCY0` | [2,2] | document | `Family Status: Nilfgaard` | 104–127 |

При 1 выбираются текст о живой семье и Parents: Nilfgaard; при 2 — текст о событии, Family Fate и Family Status. Fate не ссылается на статус самостоятельно. Первый путь может вернуть от четырёх до шести текстов в зависимости от состояния и судьбы родителей.

## Основные функции и методы

Собственных функций у JSON нет; методы ниже определены в Foundry 14.367.0.

| Метод | Вход, действия и результат | Состояние и ограничения |
| --- | --- | --- |
| RollTable.getResultsForRoll(value) | Находит все записи с drawn=false и диапазоном, включающим value | Порядок соответствует JSON; при 0 и 3 массив пуст |
| RollTable.roll({recursive}) | Исполняет 1d2; при recursive:true разрешает documentUuid на RollTable и раскрывает вложенный roll | Стандартно recursive=true; без подготовки чата; заданная formula не требует нормализации |
| RollTable.draw({displayChat}) | Вызывает roll, затем toMessage при displayChat=true | Все replacement=true: результаты остаются доступными; сообщение — отдельное действие |
| RollTable.normalize({save:false}) | По 5 единичным весам создаёт клон с 1d5 и одиночными диапазонами | Меняет формулу/диапазоны; для составных выдач разделяет совместно выбранные записи; save=true записал бы изменения |
| TableResult.getHTML / documentToAnchor | Готовит описание и ссылку на документ | enrichHTML может обрабатывать разметку; inline-выражений и текстовых UUID здесь нет |
| RollTable.toMessage | Сочетает собственный description, выбранные результаты и HTML броска при displayRoll=false | Настройка displayRoll вложенного документа не управляет сообщением родителя; ChatMessage.create пишет чат в полном клиенте |

При прямом запуске с _depth=0 число конечных text по структуре связей составляет 4–6; максимальная внутренняя глубина — 4 переходов. Это границы, рассчитанные по всем ветвям экспортного графа, а не перебор всех сочетаний случайных чисел во время исполнения. В ядре глубина более 5 вызывает исключение: дополнительный внешний генератор учитывается в том же счётчике.

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
| `VySuFOPm5I8jY8r9`, строка 53 | [Parents: Nilfgaard](Parents__Nilfgaard_Nnf1BMSJOnc5Mx3m.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.Nnf1BMSJOnc5Mx3m` |
| `rx40q7d9iV7PIvy0`, строка 100 | [Family Fate: Nilfgaard](Family_Fate__Nilfgaard_VstrJuRw43OKcuGr.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.VstrJuRw43OKcuGr` |
| `JQeprlU3cojjnCY0`, строка 124 | [Family Status: Nilfgaard](Family_Status__Nilfgaard_6WXA7KAOHjeqCCRn.json.md) | `Compendium.TheWitcherTRPG.Character-gen_Sub-tables.RollTable.6WXA7KAOHjeqCCRn` |

## Известные потребители

| Файл / компонент | Запись / используемые данные | Условия |
| --- | --- | --- |
| [packsJson/character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json](../../../../../../packsJson/character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json) | `L1KBkf196CGL9GXv`; строка 199; range=[2,2] | При recursive:true вызывает эту RollTable |
| [utils/packs.mjs](../../../../../../utils/packs.mjs) | Полный JSON | Чтение при сборке каталога |
| Foundry client/applications/sheets/roll-table-sheet.mjs:428–438; sidebar/tabs/roll-table-directory.mjs:28–33 | RollTable | Стандартные действия пользователя вызывают draw |
| [module/item/witcherItem.js](../../../../../../module/item/witcherItem.js):257–315 | Совпадение Item.name с `Family and Parents: Nilfgaard` | Условный поиск при экспорте добычи; метод ожидает Item, а данный граф выдаёт text |

Поиск пакета, ID, UUID и имён выполнен по module/templates/utils, system.json и всем 226 packsJson. Статических вызовов этих таблиц из программного кода системы и связей со style/lifepath не найдено. Общий поиск по имени в WitcherItem остаётся возможным; его поведение с этим набором определено чтением метода и формой реально полученных результатов, без повторного исполнения самого метода.

[module/data/actor/templates/character/general/backgroundData.js](../../../../../../module/data/actor/templates/character/general/backgroundData.js) хранит биографию как HTMLField; [module/data/actor/templates/character/general/homelandData.js](../../../../../../module/data/actor/templates/character/general/homelandData.js) — строковые value/otherValue. [module/data/item/homelandData.js](../../../../../../module/data/item/homelandData.js) и [module/data/item/professionData.js](../../../../../../module/data/item/professionData.js) задают самостоятельные Item-модели. [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../module/actor/sheets/WitcherCharacterSheet.js):154–156 выбирает принадлежащие Actor предметы, а [templates/partials/character/tab-background.hbs](../../../../../../templates/partials/character/tab-background.hbs):7–25,51–53 показывает родину и редактор биографии. Присваивания результата этой таблицы перечисленным полям/предметам не найдено; тематическое соответствие не является вызовом или импортом.

## Данные и изменения состояния

JSON хранит RollTable и вложенные TableResult. После прямого roll/draw в проверенных сценариях исходные модели и drawn не изменились; displayChat=false не создавал сообщение. В полном клиенте обычный draw сохраняет ChatMessage, но текст награды, родственника, профессии или бонуса сам по себе не создаёт соответствующий документ.

Шанс каждой отдельной записи определяется шириной её range относительно 2 равновероятных граней. При перекрытии выбираются все записи; сумма их отдельных вероятностей не обязана равняться 100%. Одинаковые тексты с разными ID остаются отдельными результатами. Системные флаги этой таблицы не задают отдельной обработки описанных правил.

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

## Уточнение TASK-0003.056

2026-09-12, rusbar-main be1c48770219a6d2871259f12c30d93636aac646; исходник сохранён. Завершён полный разбор основных генераторов. Ранее описанные входящие ссылки сопоставлены с новыми карточками и реальным рекурсивным выбором:

| Генератор | ID его результата | Строка documentUuid / range |
| --- | --- | --- |
| [Background Generator: Human](../character-generator/Background_Generator__Human_g9I3DpPOi5CfOFBz.json.md) | `L1KBkf196CGL9GXv` | 199; [2,2] |

В общей сверке пяти пакетов проверены 117 JSON / 929 результатов, 252 ссылки и getHTML всех результатов. Все поля/тексты/UUID данной карточки сопоставлены с источником. Отдельные случайные комбинации не перебирались полностью; реальные пакеты, мир и права игроков не проверялись. [Протокол .056](../../../review-log.md#task-0003056).
