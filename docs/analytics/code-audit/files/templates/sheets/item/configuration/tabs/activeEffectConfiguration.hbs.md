# templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `07237960627bf7debc2b4283aa55d1a8c5d1bb8b` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.011](../../../../../../../../tasks/task-0003.011.md), одна порция из семи файлов |
| Запись перекрёстной сверки | [TASK-0003.011](../../../../../../review-log.md#task-0003011) |

## Назначение файла

Оборачивает общий список эффектов в часть activeEffects окна конфигурации Item. Собственного управления документами не содержит.

## Условия использования

PARTS.activeEffects [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js); CSS-класс активной вкладки берётся из tabs.activeEffects.cssClass. Partial effect-part получает текущий контекст целиком, без явного переопределения параметров.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| div.effects.tab.scrollable.standard-form | 1–4 | Контейнер вкладки | data-group=primary, data-tab=activeEffects | Вкладка связана с TABS.primary |
| Partial effect-part.hbs | 3 | Список, категории и действия | Контекст effects/document/item | Все строки и controls создаются вложенным partial |

## Основные функции и методы

JavaScript-функций нет. Шаблон вычисляет условия Handlebars и создаёт разметку; обработчики и запись документов принадлежат указанным ниже файлам.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| tabs.activeEffects.cssClass / effects / document | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js); Foundry ApplicationV2 | Контекст | 1–3; TABS и _prepareContext | Четыре категории сверены с actual handler |
| effect-part.hbs | [templates/partials/effect-part.hbs](../../../../../../../../../templates/partials/effect-part.hbs) | Включение partial | 3; вывод категорий и строк | Полная карточка TASK-0003.010 уточнена |
| Предзагрузка effect-part | [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Регистрация шаблона | Shared partial должен быть доступен рендеру | Путь в загрузчике сверён |
| create/edit/delete/toggle | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Действия вложенного partial | onManageActiveEffect:116–142 | Ищет effectId в текущем Item; здесь нет собственного handler |
| isSuppressed/canHaveTemporaryItemImprovement | [module/activeEffect/witcherActiveEffect.js](../../../../../../../../../module/activeEffect/witcherActiveEffect.js); [module/data/item/commonItemData.js](../../../../../../../../../module/data/item/commonItemData.js) | Условные данные partial | Условия suppressed-строки и кнопки улучшения | При Item-контексте @root.actor не задан; suppressed-строка не скрывается этим условием |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Путь PARTS.activeEffects | 40; наследуется конфигурациями | Один прямой путь в module; остальные через super.PARTS |

## Данные и изменения состояния

Файл не содержит формовых полей, собственных локализаций или document.update. Список effects формируется перед рендером, actions вложенного partial отправляются конфигурации. Для Item-контекста категория temporaryItemImprovement условно скрывает кнопку создания при canHaveTemporaryItemImprovement=false; это не удаляет уже имеющиеся документы. Описание эффекта выводится скрытым в partial, а раскрывающего listener у этой конфигурации не найдено.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | 4 строки и прямые ссылки | Один контейнер и один partial; таб совпадает с TABS | Шаблон прочитан полностью |
| Рендер | Реальный Handlebars, оригинальный effect-part, категории исходного класса | Видны create/edit/toggle/delete, description остаётся invisible | Не реальный click; запись документов подменена в отдельном тесте |
| Обратная связь | onManageActiveEffect и data-effect-id/type | Категория create и идентификатор остальных actions соответствуют handler | Динамические listeners внешних модулей не проверены |

## Непроверенные участки и открытые вопросы

Непрочитанных строк нет. Не выполнялись браузерный выбор вкладки, реальный drag эффекта из конфигурации, внешние слушатели и server update. Возможность drag здесь наследуется от CoreItemSheetV2 и отличается от основной ItemSheet с _canDragStart=false.

## Связанные проблемы

[issue-00056](../../../../../../../../issues/potential/issue-00056.md) — ссылка раскрытия описания не имеет найденного Item-обработчика.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.011 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
