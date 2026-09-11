# module/item/sheets/WitcherHexSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherHexSheet.js](../../../../../../../module/item/sheets/WitcherHexSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

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

Все 28 строк прочитаны. Поведение применения порчи и реальный FilePicker остаются за границей.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00136](../../../../../../issues/potential/issue-00136.md), [issue-00137](../../../../../../issues/potential/issue-00137.md). 136 относится к изображению в подключённом HBS; 137 — к трём danger-ключам.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |
