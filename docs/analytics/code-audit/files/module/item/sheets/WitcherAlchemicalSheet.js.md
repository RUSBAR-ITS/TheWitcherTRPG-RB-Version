# module/item/sheets/WitcherAlchemicalSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherAlchemicalSheet.js](../../../../../../../module/item/sheets/WitcherAlchemicalSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.015](../../../../../../tasks/task-0003.015.md), одна порция из пятнадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.015](../../../../review-log.md#task-0003015) |

Актуализация [issue-00001](../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Специализированный лист Item alchemical: основной шаблон и варианты категории, отдельная configuration расходования.

## Условия использования

registerSheets импортирует класс и назначает листом по умолчанию соответствующего типа. При создании экземпляра наследуется WitcherItemSheet; HBM использует PARTS.main. Собственных действий, drop-обработчиков и слушателей нет. Поле configuration создаёт WitcherConsumableConfigurationSheet для того же this.document.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherAlchemicalSheet | default class extends WitcherItemSheet | Лист alchemical | Регистрация registerSheets | Рендер и подготовка контекста |
| PARTS.main | static object | template systems/TheWitcherTRPG-RB-Version/templates/sheets/item/alchemical-sheet.hbs; scrollable=[''] | HandlebarsApplicationMixin | Рендер основной части |
| configuration | Поле экземпляра | WitcherConsumableConfigurationSheet({document:this.document}) | Действие configureItem из родителя | Отдельное окно того же Item |
| config.type | Результат getTypes | Словарь категорий | Контекст HBS | Изменяется общий CONFIG.WITCHER через ссылку context.config |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| async _prepareContext(options) | Опции рендера; контекст родителя | Дополненный context | await super._prepareContext; config.Availability.WITCHER='WITCHER.Item.AvailabilityWitcher'; config.type=this.getTypes() | Мутирует общий config, не сохраняет Item |
| getTypes() | Аргументов нет | Новый словарь категорий | alchemical→WITCHER.Alchemy.Alchemical, potion→WITCHER.Alchemy.Potion, decoction→WITCHER.Alchemy.Decoction, oil→WITCHER.Alchemy.Oil | Синхронно; модель StringField не ограничена этим набором |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Прямой импорт / наследование | Контекст, configureItem, формы/эффекты/действия | Определение и место использования сверены |
| WitcherConsumableConfigurationSheet | [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js) | Прямой импорт / создание | configuration | Определение и место использования сверены |
| Основной HBS | [templates/sheets/item/alchemical-sheet.hbs](../../../../../../../templates/sheets/item/alchemical-sheet.hbs) | PARTS.main.template | Представление | Определение и место использования сверены |
| CONFIG.WITCHER | [module/setup/config.js](../../../../../../../module/setup/config.js) | Данные через родителя | Availability и изменяемый config.type | Определение и место использования сверены |
| Ключи категорий | [lang/ru.json](../../../../../../../lang/ru.json) | Локализация | getTypes/createSelects; AvailabilityWitcher | Определение и место использования сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherAlchemicalSheet | Импорт и регистрация типа alchemical | registerSheet makeDefault |
| [templates/sheets/item/alchemical-sheet.hbs](../../../../../../../templates/sheets/item/alchemical-sheet.hbs) | config.type; item/system | Основная форма | PARTS |
| [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | configuration / item / config | Общая шапка; кнопка configureItem | Включение основным шаблоном |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Контекст родителя содержит item, data, systemFields, config, showConfig. config не клонируется: Availability.WITCHER и type попадают в общий CONFIG.WITCHER; _prepareContext не обновляет документ. Configuration содержит general/consumableProperties/activeEffects, всего пять частей с header/tabs; поля расходования скрыты до isConsumable=true. Обычные именованные поля сохраняются унаследованным механизмом формы, не этим файлом.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст и регистрация | Полный класс + registerSheets + реальный _prepareContext | Выбран ожидаемый класс; 4 категории в config.type | Полный браузерный выбор листа не проверялся |
| HBS/вкладки | Настоящие HBS и core _prepareTabs/_getTabsConfig | 4 варианта, 9/10/10/9 полей; 3 вкладки | DocumentSheet/DOM фасады, selectOptions ограниченный генератор |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-01](../../../../cross-check-0002.md#u007-01), [U007-04](../../../../cross-check-0002.md#u007-04), [U007-08](../../../../cross-check-0002.md#u007-08). Для этого файла установлены процессы R007-02, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00091](../../../../../../issues/potential/issue-00091.md), [issue-00092](../../../../../../issues/potential/issue-00092.md). Проблемы находятся в подключаемой configuration; не исправлялись.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.015 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

Основной лист alchemical выбирает четыре типа и availability в общем CONFIG, а configureItem открывает WitcherConsumableConfigurationSheet. HBS выбирает time/toxicity по типу; эффекты расходования находятся в отдельной вкладке и проходят общие Item/Actor методы.

Сопоставленные определения и потребители: [module/item/sheets/WitcherItemSheet.js](WitcherItemSheet.js.md), [module/item/sheets/configurations/WitcherConsumableConfigurationSheet.js](configurations/WitcherConsumableConfigurationSheet.js.md), [templates/sheets/item/alchemical-sheet.hbs](../../../templates/sheets/item/alchemical-sheet.hbs.md), [module/setup/config.js](../../setup/config.js.md), [lang/ru.json](../../../lang/ru.json.md), [module/setup/registerSheets.js](../../setup/registerSheets.js.md), [templates/partials/item-header.hbs](../../../templates/partials/item-header.hbs.md).

[Протокол и границы](../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-02](../../../../cross-check-0002.md#r007-02). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
