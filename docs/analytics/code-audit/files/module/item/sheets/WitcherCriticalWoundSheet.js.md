# module/item/sheets/WitcherCriticalWoundSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherCriticalWoundSheet.js](../../../../../../../module/item/sheets/WitcherCriticalWoundSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.020](../../../../../../tasks/task-0003.020.md), 10 файлов, 428 логических строк |
| Запись перекрёстной сверки | [TASK-0003.020](../../../../review-log.md#task-0003020) |

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

Все 22 строки прочитаны. Полное открытие окна в Foundry, форма DocumentUUIDField и применение прав не исполнялись. Общие ограничения Drop из issue-00058/00059 остаются в базовом классе; здесь Item-обработчик определён.

## Связанные проблемы

[issue-00121](../../../../../../issues/potential/issue-00121.md), [issue-00127](../../../../../../issues/potential/issue-00127.md). Переход по сохранённой ссылке требует проверки получателя; Drop не возвращает завершение update. Это не объявлено ошибкой формата UUID.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `b09f992960a76d1c75946f402e42d93fa0785008`; полный файл | Первая карточка; [сверка порции и второй серии](../../../../review-log.md#task-0003020) |
