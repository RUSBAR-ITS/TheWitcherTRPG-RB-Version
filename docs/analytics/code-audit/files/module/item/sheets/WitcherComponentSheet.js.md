# module/item/sheets/WitcherComponentSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/WitcherComponentSheet.js](../../../../../../../module/item/sheets/WitcherComponentSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../review-log.md#task-0003016) |

## Назначение файла

Минимальный специализированный лист компонента: задаёт ширину 600 и единственную основную часть формы.

## Условия использования

registerSheets регистрирует WitcherComponentSheet с makeDefault:true/types:['component']. Наследование WitcherItemSheet даёт контекст, configuration, действия, сохранение и drag/drop; собственных методов нет.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherComponentSheet | default class extends WitcherItemSheet | Лист component | Items.registerSheet | Рендер |
| DEFAULT_OPTIONS.position.width | static object | 600 | Application options | Настройка ширины |
| PARTS.main | static object | template systems/TheWitcherTRPG/templates/sheets/item/component-sheet.hbs; scrollable=[''] | HandlebarsApplicationMixin | Основная часть |

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

Не исполнялись полный ApplicationV2, окно браузера и submit. Дополнительный пользовательский лист или модуль может предоставлять другой шаблон/helper; это не проверено.

## Связанные проблемы

[issue-00094](../../../../../../issues/potential/issue-00094.md). Ошибка вызвана подключаемым HBS на штатном наборе helpers Foundry 14.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
