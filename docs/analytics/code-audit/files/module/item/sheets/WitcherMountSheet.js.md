# module/item/sheets/WitcherMountSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherMountSheet.js](../../../../../../../module/item/sheets/WitcherMountSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `1d29f681ffed1c46b9c05b0eff09935300c3bf7d` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.035](../../../../../../tasks/task-0003.035.md), 6 файлов, 384 логические строки |
| Запись перекрёстной сверки | [TASK-0003.035](../../../../review-log.md#task-0003035) |

## Назначение файла

Специализация WitcherItemSheet для mount: ширина600 и основная часть mount-sheet.hbs. Собственных действий или механики верхового боя нет.

## Условия использования

registerSheets import25, регистрация Item mount88–91 makeDefault:true. DEFAULT_OPTIONS сливаются Foundry с базовыми настройками: формы/классы/actions/configuration остаются наследуемыми; PARTS.main делает этот тип отображаемым.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherMountSheet | default class:3–15 | Лист Item mount | registerSheets | Создание экземпляра |
| DEFAULT_OPTIONS.position.width | static:4–8 | 600 | Foundry merging | Остальные настройки наследуются |
| PARTS.main | static:9–14 | mount-sheet.hbs; scrollable:[''] | HandlebarsApplicationMixin | Рендер одной секции |

## Основные функции и методы

Собственных функций, методов или callback нет. _prepareContext/_onRender/_onChangeForm/_onDrop/activateListeners, actions addEffect/removeEffect/configureItem и configuration происходят из WitcherItemSheet; стандартное редактирование изображения — из DocumentSheetV2. Наследуемые действия перечислены как связи, не как определения этого файла.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | прямой импорт и наследование | 1,3 | Контекст item/systemFields/enrichedText/data/config/showConfig; форма и конфигурация |
| PARTS.main | [templates/sheets/item/mount-sheet.hbs](../../../../../../../templates/sheets/item/mount-sheet.hbs) | literal template | 11 | Рендер mount с общим header |
| DEFAULT_OPTIONS merge / ItemSheetV2 | Foundry ApplicationV2/DocumentSheetV2/ItemSheetV2 | наследуемый контракт | Класс и DEFAULT_OPTIONS | Core application.mjs:417–425 inheritanceChain и438–451 _initializeApplicationOptions собирают DEFAULT_OPTIONS предков; контекст выполнен на фасаде, полный клиент не инстанцировался. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherMountSheet | import25, register mount88–91 | makeDefault:true |
| [templates/sheets/item/mount-sheet.hbs](../../../../../../../templates/sheets/item/mount-sheet.hbs) | item/data/config/showConfig/systemFields | Контекст наследуемого ItemSheet | PARTS.main; header использует configureItem |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Сам файл не пишет документы. Ширина отличается от базовой520, height480 и form options наследуются. inherited configuration создаёт WitcherConfigurationSheet; кнопка в header доступна через showConfig. Собственного Actor либо запаса валюты нет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Импорт и контекст | 19–20 | Настоящий класс extends ItemSheet; main верный, width600, context.item тот же документ | Базовый Foundry Application — фасад |
| Регистрация/шаблон | rg registerSheets и PARTS | Ровно один прямой импорт потребителя | Пользовательская смена листа не проверялась |

## Непроверенные участки и открытые вопросы

Исполнены настоящие методы системы и модели Foundry 14.367.0 в изолированном Node 24.16.0. Коллекции документов, окна, запись и базовый Application — фасады; HBS — настоящий Handlebars 4.7.9, разбор HTML — parse5. Полный клиент, DOM-события, сервер, права реальной БД, сетевые гонки и сохранение мира не проверялись. Пути systems/TheWitcherTRPG сохранены как в исходниках; доступ по HTTP здесь не проверялся.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md). Для mount есть PARTS.main, поэтому отсутствие шаблона общего WitcherItemSheet (issue57) не переносится сюда. Checkbox clickableImage наследует прежнее наблюдение.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `1d29f681ffed1c46b9c05b0eff09935300c3bf7d`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003035) |
