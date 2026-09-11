# module/item/sheets/configurations/WitcherSpellConfigurationSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/configurations/WitcherSpellConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherSpellConfigurationSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../../review-log.md#task-0003021) |

## Назначение файла

Адаптер конфигурации spell: заменяет общую вкладку свойств на таблицы статусов и настройки атаки, сохраняя остальные части WitcherPropertiesConfigurationSheet.

## Условия использования

Создаётся только как поле configuration экземпляра WitcherSpellSheet. Отдельной регистрации этого класса в registerSheets нет. configureItem в общем листе вызывает render(true) экземпляра.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherSpellConfigurationSheet | default class; 3–11 | Наследник WitcherPropertiesConfigurationSheet | Импорт из WitcherSpellSheet | UI конфигурации |
| static PARTS | 4–10 | ...super.PARTS и новая general | ApplicationV2 PARTS | Сохраняет header/tabs/activeEffects/damageProperties/defenseProperties/regionProperties |
| PARTS.general | 6–9 | spellGeneral.hbs, scrollable:[''] | Часть окна | Подмена общей формы |

## Основные функции и методы

Собственных методов нет. _prepareContext, _prepareTabs, _configureRenderParts, _onChangeForm и addEffect/removeEffect наследуются от WitcherPropertiesConfigurationSheet; ActiveEffect CRUD — через WitcherConfigurationSheet. Не следует приписывать этому 11-строчному файлу определения унаследованных обработчиков.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherPropertiesConfigurationSheet | [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Импорт/наследование | PARTS, TABS, условия вкладок, keyed CRUD статусов | Полный родитель прочитан; собственный PARTS меняет лишь general |
| WitcherConfigurationSheet | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Косвенное наследование | item/config/systemFields и настоящие Item.effects | Отдельный ActiveEffect lifecycle |
| spellGeneral.hbs | [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | PARTS.general | Два словаря и поля атаки | Путь сверён |
| SpellData | [module/data/item/spellData.js](../../../../../../../../module/data/item/spellData.js) | Контракт документа | Поле system/schema | Все обычные поля формы определены |
| HandlebarsApplicationMixin/ItemSheetV2 | Foundry14.367.0 | Косвенное наследование UI | Рендер, actions, form | Изолированная проверка с façade ItemSheetV2 |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherSpellSheet.js](../../../../../../../../module/item/sheets/WitcherSpellSheet.js) | WitcherSpellConfigurationSheet | Создание configuration | 6 |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | Контекст и inherited actions | Вывод/редактирование | Полный разбор |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Не меняет модель при объявлении класса; задаёт конфигурацию UI. CRUD словарей использует произвольный ID и system.<field>.<id>, а ActiveEffect CRUD работает с embedded документами. Две системы данных разделены. Ошибка удаления PART regionProperties по старому system.createTemplate унаследована без исправления.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Наследование/условия | Группа 10 | Специализированная general сохранена; вкладка regionProperties остаётся в навигации, но part удаляется даже при актуальном createTemplate=true | Базовый механизм построения UI — фасад |
| Статусы | Группы 13–14 | Оба typed словаря выведены с ID; add→{percentage: 0}; edit→statusEffect; remove→-=ID | DB/update заменены сборщиком вызовов |

## Непроверенные участки и открытые вопросы

Все 11 строк прочитаны. Полный браузерный рендер частей, сохранение и работы ActiveEffect не проверены заново.

## Связанные проблемы

[issue-00060](../../../../../../../issues/potential/issue-00060.md), [issue-00062](../../../../../../../issues/potential/issue-00062.md), [issue-00074](../../../../../../../issues/potential/issue-00074.md), [issue-00075](../../../../../../../issues/potential/issue-00075.md). 60/74/75 относятся к родителю и связанным формам. issue-00062 в этом классе не воспроизводится: general заменена на spellGeneral, которая включает корректный attackOptionsPart.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003021) |
