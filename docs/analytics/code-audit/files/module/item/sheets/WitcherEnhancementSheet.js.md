# module/item/sheets/WitcherEnhancementSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherEnhancementSheet.js](../../../../../../../module/item/sheets/WitcherEnhancementSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `0fa589bd300856ff309f362afcb66d6fa43401ab` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.014](../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../review-log.md#task-0003014) |

## Назначение файла

Лист улучшения: подключает форму и добавляет список четырёх категорий улучшений.

## Условия использования

Default export WitcherEnhancementSheet extends WitcherItemSheet; тип Item.enhancement. Собственное configuration не объявлено: остаётся базовое окно WitcherConfigurationSheet. Нет собственных методов применения или установки улучшения.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherEnhancementSheet | Класс 3–29 | Редактор enhancement | Default export / Items.registerSheet | Наследование базовой формы |
| PARTS.main | 4–9 | enhancement-sheet.hbs | Static, scrollable:[''] | Рендер |
| context.selects.enhancementTypes | 14,20–27 | Список категорий | Отдельный объект context.selects | weapon/rune/armor/glyph |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _prepareContext(options) | super context | Promise<context> | Добавляет selects=this.createSelects() | Собственной записи CONFIG или Item нет |
| createSelects() | Нет аргументов | {enhancementTypes:{...}} | weapon→WITCHER.Diagram.Weapon, rune→WITCHER.Enhancement.Rune, armor→...Armor, glyph→...Glyph | Новый объект при каждом вызове |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Import/наследование | Контекст, DEFAULT_OPTIONS, действия effects, базовая конфигурация | Ранее полностью описан; обработчики сверены |
| enhancement-sheet.hbs | [templates/sheets/item/enhancement-sheet.hbs](../../../../../../../templates/sheets/item/enhancement-sheet.hbs) | PARTS | 6 | Все варианты type проверены |
| Ключи названий категорий | [lang/ru.json](../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../lang/en.json) | Локализация через HBS | 22–25 | Значения найдены |
| ItemSheetV2/HBM | Foundry 14.367.0 | Наследуемый API | Подготовка/рендер | Метод исполнялся с фасадом окружения |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherEnhancementSheet | Регистрация Item.enhancement | Импорт 20, регистрация 60 |
| [templates/sheets/item/enhancement-sheet.hbs](../../../../../../../templates/sheets/item/enhancement-sheet.hbs) | selects.enhancementTypes | selectOptions для system.type | 7 |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Этот класс не ограничивает type схемой: варианты существуют в UI, EnhancementData.type остаётся свободной строкой. Изменения system.effects выполняют унаследованные addEffect/removeEffect/_onEditEffect. Поля applied/quantity при установке меняет внешний инвентарь, а не лист.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст | Настоящие лист и EnhancementData | Четыре значения selects; базовая configuration | Никакая установка улучшения не выполнялась |
| Рендер | Пустой type и четыре категории | 6 именованных полей с header, у armor 11; три поля редактирования эффекта | Handlebars настоящий, selectOptions/toFormGroup ограничены фасадами |

## Непроверенные участки и открытые вопросы

Нет своих обработчиков drop или применения эффекта. Полный цикл формы/сохранения/установки в мире не запускался; методы, регистрация и все используемые значения проверены.

## Связанные проблемы

[issue-00060](../../../../../../issues/potential/issue-00060.md). Унаследованный обработчик преобразует имя on в false; собственного исправления в этом классе нет.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
