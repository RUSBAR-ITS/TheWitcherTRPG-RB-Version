# module/item/sheets/configurations/WitcherArmorConfigurationSheet.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/configurations/WitcherArmorConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherArmorConfigurationSheet.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `0fa589bd300856ff309f362afcb66d6fa43401ab` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.014](../../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../../review-log.md#task-0003014) |

## Назначение файла

Специализация общего окна свойств, заменяющая вкладку general на форму SP брони.

## Условия использования

Default export WitcherArmorConfigurationSheet extends WitcherPropertiesConfigurationSheet. Создаётся полем configuration у WitcherArmorSheet, не регистрируется самостоятельным типом документа или листом по умолчанию.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WitcherArmorConfigurationSheet | Класс 3–11 | Конфигурация брони | Default export | Наследование общего окна |
| PARTS.general | 4–10 | armorGeneral.hbs | Spread super.PARTS; заменён один descriptor | scrollable:['']; остальные части наследуются |

## Основные функции и методы

Собственных функций/методов нет. Static PARTS вычисляется при определении класса. Подготовка context/TABS/PARTS, actions и изменения формы унаследованы от WitcherPropertiesConfigurationSheet и WitcherConfigurationSheet.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherPropertiesConfigurationSheet | [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js) | Import/наследование/spread | PARTS и весь жизненный цикл | Полный разбор TASK-0003.013 |
| armorGeneral.hbs | [templates/sheets/item/configuration/tabs/armorGeneral.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) | PARTS.general | 7 | Полный разбор 12 полей |
| ArmorData/DefenseProperties | [module/data/item/armorData.js](../../../../../../../../module/data/item/armorData.js) | Условие унаследованной фильтрации | Нет damage/region, есть defenseProperties | Настоящая модель |
| HandlebarsApplicationMixin/ItemSheetV2 | Foundry 14.367.0 | Наследуемый API | Фильтрация частей и подготовка вкладок | Оригинальные методы в изолированном окружении |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherArmorSheet.js](../../../../../../../../module/item/sheets/WitcherArmorSheet.js) | Класс конфигурации | new {document:this.item} | 1,6 |
| [templates/sheets/item/configuration/tabs/armorGeneral.hbs](../../../../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) | context.document/systemFields/tabs | Форма general | Все пути сверены |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

У брони остаются general/defenseProperties/activeEffects, пять частей header/tabs/general/activeEffects/defenseProperties. Не добавляет методы защиты в ArmorData. Наличие вкладки defenseProperties не означает, что общий отбор защит умеет использовать её модель. Для Shield состав general такой же: двенадцать полей SP, без собственной ветви надёжности.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| TABS/PARTS | Настоящий ArmorConfig с FullCover и Shield | 3 вкладки, 5 частей; 12 general-полей в обоих случаях | Без браузера и записи |

## Непроверенные участки и открытые вопросы

Проверен весь файл, собственных вычислений кроме PARTS нет. Полный родительский документный submit и боевой диалог здесь не выполнялись.

## Связанные проблемы

[issue-00085](../../../../../../../issues/potential/issue-00085.md). Видимая вкладка защиты ссылается на модель, у которой нет методов делегирования в общий отбор.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

Отдельно установлено отсутствие четырёх русских подсказок в armorGeneral.hbs: [issue-00090](../../../../../../../issues/potential/issue-00090.md). Это не меняет правильную привязку полей к сторонам.
