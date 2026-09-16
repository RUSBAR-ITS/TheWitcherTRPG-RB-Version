# module/item/sheets/WitcherCriticalWoundSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.020](../../../../../../tasks/task-0003.020.md), 10 файлов, 428 логических строк |
| Запись перекрёстной сверки | [TASK-0003.020](../../../../review-log.md#task-0003020) |

Актуализация [issue-00001](../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Специализированный лист criticalWound: размеры окна, основная форма и назначение followUp переносом Item.

## Условия использования

Default export extends WitcherItemSheet; registerSheets регистрирует как основной лист criticalWound. Собственного конструктора, конфигурации, вкладок и контекста нет: используются базовый _prepareContext и WitcherConfigurationSheet. Общий Drop проверяет isEditable, разрешает документ, затем вызывает этот _onDropItem.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherCriticalWoundSheet | Класс, 3–22 | Лист Item | Default export | Наследует общие действия и конфигурацию |
| DEFAULT_OPTIONS.position | Статика, 4–9 | Размер 600×620 | Опции приложения | Не задаёт разрешений документа |
| PARTS.main | Статика, 10–15 | criticalWound-sheet.hbs; scrollable=[''] | Единственная своя часть | Рендер формы по общему контексту |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _onDropItem(event,item):17–21 | Разрешённый базовым Drop Item; event не используется | Promise<void> | Запрос document.update({'system.followUp':item.uuid}) | Не проверяет подтип, self-reference или результат разрешения при дальнейшем лечении; update не await/return |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Прямой import/extends | 1–3; контекст, форма, Drop и actions | Методы базового класса прочитаны до определения |
| WitcherConfigurationSheet | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Наследуемый экземпляр configuration | Шестерёнка открывает общую конфигурацию и Item.effects | Вкладка general условно пуста для этой схемы; ActiveEffect остаются доступны |
| PARTS.main | [templates/sheets/item/criticalWound-sheet.hbs](../../../../../../../templates/sheets/item/criticalWound-sheet.hbs) | Путь шаблона | 12 | Форма сопоставлена с CriticalWoundData |
| followUp | [module/data/item/criticalWoundData.js](../../../../../../../module/data/item/criticalWoundData.js) | Запись поля | 19 | DocumentUUIDField type Item, не ограниченный конкретной разновидностью |
| document.update; Application options | Foundry 14.367.0 ItemSheetV2 / Document API | Внешние API | Наследуемая форма и запись UUID | Исполнялся только исходный дочерний класс поверх минимального фасада базы |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherCriticalWoundSheet | Import и Items.registerSheet types=['criticalWound'] | Регистрация найдена 28, 52–55 |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | _onDropItem override | _onDropDocument при documentName='Item' | Динамическая диспетчеризация |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Drop сохраняет UUID, а не копирует Item. Исходная ссылка может указывать на weapon или саму травму: специальных ограничений здесь нет. Создание последующего документа происходит позже в CriticalWoundData.treat. name/img/effects — данные документа Foundry, а не отдельные поля этого класса. Собственная форма не включает item-image; это факт состава, необходимость отдельного редактора изображения не оценивалась.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Drop и асинхронность | Настоящий класс; документ и superclass — фасады | weapon UUID передан в system.followUp; метод завершился до update | Не браузерный drag/drop и не сохранение БД |
| Настройка/форма | PARTS и базовый configuration/_prepareContext сверены | 600×620, один main, showConfig=true при общей configuration | Наследуемые V2 методы не запускались повторно |

## Непроверенные участки и открытые вопросы

Текущая сверка охватила исходник, описанные поля и конкретных потребителей; прежние результаты выше сохраняют даты своих опытов. Схема, fromUuid и запросы create/delete сопоставлены. Остаются существование мирового UUID, права/ошибки сервера, порядок сохранения, повторная подготовка Actor/AE и отдельно скопированные эффекты. Следующий критерий: отличать загруженный шаблон, запрос записи и подтверждённое состояние. Запуск мира или изменение доступа здесь не согласованы. Границы: [U012-01](../../../../cross-check-0002.md#u012-01) и [U012-08](../../../../cross-check-0002.md#u012-08).

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md), [issue-00127](../../../../../../issues/potential/issue-00127.md). Переход по сохранённой ссылке требует проверки получателя; Drop не возвращает завершение update. Это не объявлено ошибкой формата UUID.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b09f992960a76d1c75946f402e42d93fa0785008`; полный файл | Первая карточка; [сверка порции и второй серии](../../../../review-log.md#task-0003020) |

## Уточнение TASK-0003.058

2026-09-12; rusbar-main, 5283da15a49422fc339c44add4e7d7d02c174ce4; исходник не изменён.

Для 24 Simple Item сверены system-поля и followUp с редактором. Его _onDropItem сохраняет UUID без собственного преобразования состояния; переход выполняет CriticalWoundData.treat. Редактор браузера и drop-событие здесь не запускались.

[Карточки Simple](../../../packsJson/criticalWounds/Simple_kHSYUTn6UUJsIu4l/_Folder.json.md), [протокол, методы и ограничения](../../../../review-log.md#task-0003058). Реальные записи в мир не выполнялись; состояния issues не менялись.

## Сквозная сверка TASK-0004.012

2026-09-14; rusbar-main, a853fc2ff721e5d33b2716081c657bd92d62d86b. Исходник совпадает со срезом TASK-0001; изменено только описание.

Форма редактирует поля модели и followUp; Drop сохраняет UUID любого Item, не строит новую травму из состояния текущей. Унаследованный Drop проверяет isEditable, но внутренний update не ожидается. Обычные ActiveEffect доступны через конфигурацию Item; canHaveTemporaryItemImprovement=false относится к временному улучшению. стерилизация отдельным полем этой формы не выведена.

Сопоставленные определения и потребители: [module/item/sheets/WitcherItemSheet.js](WitcherItemSheet.js.md), [module/data/item/criticalWoundData.js](../../data/item/criticalWoundData.js.md), [templates/sheets/item/criticalWound-sheet.hbs](../../../templates/sheets/item/criticalWound-sheet.hbs.md).

[Протокол и границы](../../../../review-log.md#task-0004012) — TASK-0004.012; процессы [R012-02](../../../../cross-check-0002.md#r012-02). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
