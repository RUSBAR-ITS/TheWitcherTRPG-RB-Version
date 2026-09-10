# module/item/sheets/WitcherValuableSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherValuableSheet.js](../../../../../../../module/item/sheets/WitcherValuableSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `7edb814aa870da75c7ad7633536e899a8d07e205` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

## Назначение файла

Специализированный лист Item valuable: основной шаблон и варианты категории, отдельная configuration расходования.

## Условия использования

registerSheets импортирует класс и назначает листом по умолчанию соответствующего типа. При создании экземпляра наследуется WitcherItemSheet; HBM использует PARTS.main. Собственных действий, drop-обработчиков и слушателей нет. Поле configuration создаёт WitcherConsumableConfigurationSheet для того же this.document.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherValuableSheet | default class extends WitcherItemSheet | Лист valuable | Регистрация registerSheets | Рендер и подготовка контекста |
| PARTS.main | static object | template systems/TheWitcherTRPG/templates/sheets/item/valuable-sheet.hbs; scrollable=[''] | HandlebarsApplicationMixin | Рендер основной части |
| configuration | Поле экземпляра | WitcherConsumableConfigurationSheet({document:this.document}) | Действие configureItem из родителя | Отдельное окно того же Item |
| selects.type | Результат createSelects | Словарь категорий | Контекст HBS | Отдельный объект контекста |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options) | Опции рендера; контекст родителя | Дополненный context | await super._prepareContext; context.selects=this.createSelects() | Не меняет общий config.type |
| createSelects() | Аргументов нет | Объект с вложенным type | general→General, toolkit→Toolkit, food-drink→Food&Drinks, clothing→Clothings, alchemical-item→AlchemicalItem, mount-accessories→MountAccessories, quest-item→QuestItem (префикс WITCHER.Valuable) | Синхронно; модель StringField не ограничена этим набором |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Прямой импорт / наследование | Контекст, configureItem, формы/эффекты/действия | Определение и место использования сверены |
| WitcherConsumableConfigurationSheet | [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) | Прямой импорт / создание | configuration | Определение и место использования сверены |
| Основной HBS | [templates/sheets/item/valuable-sheet.hbs](../../../../../../../templates/sheets/item/valuable-sheet.hbs) | PARTS.main.template | Представление | Определение и место использования сверены |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../module/setup/config.js) | Данные через родителя | Availability/Concealment доступны форме | Определение и место использования сверены |
| Ключи категорий | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | getTypes/createSelects; AvailabilityWitcher | Определение и место использования сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherValuableSheet | Импорт и регистрация типа valuable | registerSheet makeDefault |
| [templates/sheets/item/valuable-sheet.hbs](../../../../../../../templates/sheets/item/valuable-sheet.hbs) | selects.type | Основная форма | PARTS |
| [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | configuration / item / config | Общая шапка; кнопка configureItem | Включение основным шаблоном |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Контекст родителя содержит item, data, systemFields, config, showConfig. selects отделён от config. Configuration содержит general/consumableProperties/activeEffects, всего пять частей с header/tabs; поля расходования скрыты до isConsumable=true. Обычные именованные поля сохраняются унаследованным механизмом формы, не этим файлом.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст и регистрация | Полный класс + registerSheets + реальный _prepareContext | Выбран ожидаемый класс; отдельный selects.type | Полный браузерный выбор листа не проверялся |
| HBS/вкладки | Настоящие HBS и core _prepareTabs/_getTabsConfig | 7 вариантов по 10 именованных полей; 3 вкладки | DocumentSheet/DOM фасады, selectOptions ограниченный генератор |

## Непроверенные участки и открытые вопросы

Полное сохранение формы, одновременно открытые окна и пользовательские sheet-настройки не проверялись. У мутагена добавление Availability.WITCHER не создаёт поле avail в модели. В этой порции не делаются выводы о правилах мутаций или категориях контента.

## Связанные проблемы

[issue-00091](../../../../../../issues/potential/issue-00091.md), [issue-00092](../../../../../../issues/potential/issue-00092.md). Проблемы находятся в подключаемой configuration; не исправлялись.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
