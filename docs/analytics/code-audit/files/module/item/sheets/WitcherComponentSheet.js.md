# module/item/sheets/WitcherComponentSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherComponentSheet.js](../../../../../../../module/item/sheets/WitcherComponentSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.016](../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../review-log.md#task-0003016) |

Актуализация [issue-00001](../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Минимальный специализированный лист компонента: задаёт ширину 600 и единственную основную часть формы.

## Условия использования

registerSheets регистрирует WitcherComponentSheet с makeDefault:true/types:['component']. Наследование WitcherItemSheet даёт контекст, configuration, действия, сохранение и drag/drop; собственных методов нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherComponentSheet | default class extends WitcherItemSheet | Лист component | Items.registerSheet | Рендер |
| DEFAULT_OPTIONS.position.width | static object | 600 | Application options | Настройка ширины |
| PARTS.main | static object | template systems/TheWitcherTRPG-RB-Version/templates/sheets/item/component-sheet.hbs; scrollable=[''] | HandlebarsApplicationMixin | Основная часть |

## Основные функции и методы

Собственных функций, методов и getters нет. _prepareContext, _onRender, activateListeners, configureItem и форма унаследованы от WitcherItemSheet; configuration остаётся WitcherConfigurationSheet. Здесь не задаются варианты категории, добыча или применение компонента.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Прямой импорт / наследование | Контекст и поведение | Определение и обращение сверены |
| component-sheet.hbs | [templates/sheets/item/component-sheet.hbs](../../../../../../../templates/sheets/item/component-sheet.hbs) | PARTS.main.template | Основная форма | Определение и обращение сверены |
| ApplicationV2 option merge / HBM | Foundry 14.367 | Внешний API через родителя | Параметры и рендер частей | Определение и обращение сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | WitcherComponentSheet | Импорт/регистрация | makeDefault component |
| [templates/sheets/item/component-sheet.hbs](../../../../../../../templates/sheets/item/component-sheet.hbs) | item/config | Унаследованный контекст | PARTS |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Сам класс не пишет документы и не меняет CONFIG. Модель ComponentData имеет 14 полей; type/substanceType/rarity и остальные поля задаются в HBS. Для общей configuration нет специальных настроек компонента.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Определения | Весь файл, 15 строк | Два static-объекта; нет собственных методов | Ширина установлена кодом, браузер не проверялся |
| Контекст/шаблон | Настоящий класс и HBS | Основной рендер остановился на Missing helper: select | DocumentSheet фасад; отсутствие helper сверено с ядром/системой |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-01](../../../../cross-check-0002.md#u007-01), [U007-07](../../../../cross-check-0002.md#u007-07), [U007-08](../../../../cross-check-0002.md#u007-08). Для этого файла установлены процессы R007-02, R007-07, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00094](../../../../../../issues/potential/issue-00094.md). Ошибка вызвана подключаемым HBS на штатном наборе helpers Foundry 14.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

WitcherComponentSheet передаёт componentTypes и общую availability в главный HBS. Поля существуют в ComponentData; первый барьер рендера — старый select helper. Подстановка helper в старом опыте давала изучить остальную форму, а не подтверждала штатный submit/выбор option.

Сопоставленные определения и потребители: [module/item/sheets/WitcherItemSheet.js](WitcherItemSheet.js.md), [templates/sheets/item/component-sheet.hbs](../../../templates/sheets/item/component-sheet.hbs.md), [module/setup/registerSheets.js](../../setup/registerSheets.js.md).

[Протокол и границы](../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-02](../../../../cross-check-0002.md#r007-02), [R007-07](../../../../cross-check-0002.md#r007-07). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
