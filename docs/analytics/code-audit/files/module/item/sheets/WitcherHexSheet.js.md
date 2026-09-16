# module/item/sheets/WitcherHexSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherHexSheet.js](../../../../../../../module/item/sheets/WitcherHexSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Актуализация issue-00330 — 2026-09-16

Версия 14.3.1.00007, dev, база 031fbb8691ad32ab01fad43253c8736071bb2f8b. [Реализация и проверки](../../../../../../issues/open/issue-00330.md#реализация-и-проверки--143100007). Ниже сохранён исторический разбор: его сообщения об исправленных подписях/пропусках относятся к прежнему коду. Механики, технические значения и компедиумы этой правкой не изменены.

Изменённые строки текущего файла:

- `22`: `Low: 'WITCHER.Spell.dangerLow',`
- `23`: `Medium: 'WITCHER.Spell.dangerMedium',`
- `24`: `High: 'WITCHER.Spell.dangerHigh'`


## Назначение файла

Редактор Item hex: основной шаблон порчи и список её опасности.

## Условия использования

registerSheets делает лист основным для hex. Вся конфигурация Item и сохранение наследуются от WitcherItemSheet; собственной конфигурации боевых/региональных свойств нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherHexSheet | default class; 3–28 | Наследник WitcherItemSheet | Items.registerSheet, hex | Подготовка контекста/форма |
| static PARTS.main | 4–9 | hex-sheet.hbs, scrollable:[''] | ApplicationV2 PARTS | Загрузка |
| selects.danger | 20–25 | Low/Medium/High → WITCHER.Spell.DangerLow/DangerMedium/DangerHigh | context.selects | Эти ключи подписей отсутствуют в en/ru |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options) | Базовый контекст | Promise контекста | await super; добавляет selects | Без update |
| createSelects() | Нет | {danger:{Low, Medium, High}} | Статический словарь | Не задаёт default danger |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Импорт/наследование | Базовый контекст, submitOnChange, configureItem, DragDrop и _onRender | Родитель прочитан; собственный createSelects дополняет контекст |
| CONFIG.WITCHER; ключи WITCHER.* | [module/setup/config.js](../../../../../../../module/setup/config.js) | Контекст через родителя | config для полей/вариантов | _prepareContext в базовом листе |
| localize/selectOptions | Foundry14.367.0 /opt/foundryvtt/client/applications/handlebars.mjs; Handlebars4.7.9 | Внешний UI | Варианты передаются HBS | Настоящий HBS; фасады helpers/ItemSheetV2, полный браузер не запускался |
| Ключи подписей | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | Значения createSelects | JSON en/ru проверены с раскрытием dotted ключей |
| hex-sheet.hbs | [templates/sheets/item/hex-sheet.hbs](../../../../../../../templates/sheets/item/hex-sheet.hbs) | PARTS.main | Основная форма | Путь сверён |
| HexData | [module/data/item/hexData.js](../../../../../../../module/data/item/hexData.js) | Косвенный контракт | Поля формы | danger хранится String без choices |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherHexSheet | Импорт/регистрация | 21, 80–82 |
| [templates/sheets/item/hex-sheet.hbs](../../../../../../../templates/sheets/item/hex-sheet.hbs) | selects.danger/base context | Вывод формы | Полный разбор |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Добавляется только context.selects. Редактор не применяет порчу, не снимает её и не исполняет эффекты. Кнопка configureItem открывает обычный WitcherConfigurationSheet родителя.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст/форма | Группы 10, 12, 15 | Medium выбран по value; danger-подписи не переведены; собственный HBS не задаёт editImage action | Системные классы/HBS настоящие; ядро листа — фасад |

## Непроверенные участки и открытые вопросы

Исходник и указанные связи сопоставлены в TASK-0004.009. Полный cast уже рассмотрен; остаются браузерный submit/FilePicker и игровой процесс снятия/доставки порчи. Остаток: [U009-01](../../../../cross-check-0002.md#u009-01), [U009-03](../../../../cross-check-0002.md#u009-03), [U009-07](../../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00136](../../../../../../issues/potential/issue-00136.md), [issue-00137](../../../../../../issues/closed/issue-00137.md). 136 относится к изображению в подключённом HBS; 137 — к трём danger-ключам.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

HexSheet расширяет общий ItemSheet контекстом danger и HBS. Uppercase DangerLow/Medium/High не совпадают с ключами en/ru; собственный img формы не имеет action editImage. Применение Hex через Actor связано с настоящей HexData и cast, а не с отдельным методом этого листа.

Сопоставленные определения и потребители: [module/item/sheets/WitcherItemSheet.js](WitcherItemSheet.js.md), [module/setup/config.js](../../setup/config.js.md), [lang/en.json](../../../lang/en.json.md), [lang/ru.json](../../../lang/ru.json.md), [templates/sheets/item/hex-sheet.hbs](../../../templates/sheets/item/hex-sheet.hbs.md), [module/data/item/hexData.js](../../data/item/hexData.js.md), [module/setup/registerSheets.js](../../setup/registerSheets.js.md).

[Протокол и границы](../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-01](../../../../cross-check-0002.md#r009-01), [R009-03](../../../../cross-check-0002.md#r009-03). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
