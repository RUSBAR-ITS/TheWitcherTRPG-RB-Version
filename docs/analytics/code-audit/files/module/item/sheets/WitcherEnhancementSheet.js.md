# module/item/sheets/WitcherEnhancementSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherEnhancementSheet.js](../../../../../../../module/item/sheets/WitcherEnhancementSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.014](../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../review-log.md#task-0003014) |

Актуализация [issue-00001](../../../../../../issues/open/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

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

Исходник и текущие связи сопоставлены в TASK-0004.006. Прежние ссылки на будущий пофайловый разбор TASK-0003 больше не являются очередью: он завершён. Остались конкретные границы сквозной проверки: [U006-01](../../../../cross-check-0002.md#u006-01); [U006-02](../../../../cross-check-0002.md#u006-02). Выбор категории формы влияет на поля сопротивлений и список statusEffect, а установка выполняется Actor itemMixin.

## Связанные проблемы

[issue-00060](../../../../../../issues/potential/issue-00060.md). Унаследованный обработчик преобразует имя on в false; собственного исправления в этом классе нет.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.006

2026-09-14; rusbar-main, a176c4f18879f2e5a63b93bc15345fc26d9f535a. Исходник совпадает со срезом TASK-0001; изменено только описание.

Лист enhancement наследует базовые actions и обычную configuration, задаёт единственный PART и четыре значения type: weapon/rune/armor/glyph. Собственного применения/Drop-handler не вводит. Выбор категории формы влияет на поля сопротивлений и список statusEffect, а установка выполняется Actor itemMixin.

Сопоставленные определения и потребители: [module/actor/sheets/mixins/itemMixin.js](../../actor/sheets/mixins/itemMixin.js.md), [module/data/item/armorData.js](../../data/item/armorData.js.md), [module/data/item/enhancementData.js](../../data/item/enhancementData.js.md), [module/data/item/weaponData.js](../../data/item/weaponData.js.md).

[Протокол и границы](../../../../review-log.md#task-0004006) — TASK-0004.006; процессы [R006-11](../../../../cross-check-0002.md#r006-11). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
