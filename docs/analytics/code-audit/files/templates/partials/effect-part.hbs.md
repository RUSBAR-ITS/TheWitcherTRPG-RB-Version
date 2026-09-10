# templates/partials/effect-part.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/effect-part.hbs](../../../../../../templates/partials/effect-part.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `247d3d86e344238a1445377c686eb6455146693c` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.010](../../../../../tasks/task-0003.010.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.010](../../../review-log.md#task-0003010) |

## Назначение файла

Общий список эффектов с категориями, источником, длительностью, кнопками управления и скрываемым описанием; используется листами Actor и конфигурацией Item.

## Условия использования

Контекст effects — объект категорий type/label/effects. document нужен для canHaveTemporaryItemImprovement; наличие @root.actor включает фильтрацию suppressed. Partial предзагружается registerHandlebarsTemplates. Один шаблон не означает одинаковые обработчики у Actor и Item.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| ol.items-list.effects-list и headers | 1–14 | Категории и кнопка create | data-effect-type=section.type | Создание улучшений скрыто, если document.system.canHaveTemporaryItemImprovement ложно |
| li.item.effect-row.flexrow.draggable | 16–50 | Строка эффекта | data-effect-id; data-parent-id и data-parent-uuid содержат effect.parent.uuid | При Actor-контексте suppressed-строка скрыта |
| a.effect-control | 9, 31–41 | create/toggle/edit/delete | data-action | Принимающий обработчик определяется использующим листом |
| a.effect-display и div.effect-description.invisible | 22–29, 44–46 | Имя/img/sourceName/duration.label и HTML description | Раскрытие отдельным listener | description выводится тройной интерполяцией |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| Рендер Handlebars; 1–53 | Категории и документы эффектов | HTML списка | Два each, localize, if/unless/and/eq/not | Собственных JS-функций, пересчёта и записи нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| Категории Actor | [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../../module/actor/sheets/mixins/activeEffectMixin.js); [module/actor/sheets/WitcherActorSheet.js](../../../../../../module/actor/sheets/WitcherActorSheet.js); [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | Подготовка контекста и listeners | Четыре группы и действия; раскрытие описания | V2/V1 явно подключают activeEffectListener |
| Категории и действия Item | [module/item/sheets/configurations/WitcherConfigurationSheet.js](../../../../../../module/item/sheets/configurations/WitcherConfigurationSheet.js) | Контекст и actions | Собственные prepareActiveEffectCategories и static onManageActiveEffect | В actions есть create/toggle/edit/delete, нет effect-display |
| canHaveTemporaryItemImprovement | [module/data/item/commonItemData.js](../../../../../../module/data/item/commonItemData.js); [module/data/item/alchemicalData.js](../../../../../../module/data/item/alchemicalData.js); [module/data/item/valuableData.js](../../../../../../module/data/item/valuableData.js); [module/data/item/spellData.js](../../../../../../module/data/item/spellData.js) | Геттер модели Item | Доступность create в категории источников улучшений | Base=false, три модели переопределяют true |
| Effect getters/fields | [module/activeEffect/witcherActiveEffect.js](../../../../../../module/activeEffect/witcherActiveEffect.js); внешний ActiveEffect | Данные строки | isSuppressed, disabled, img, name, parent.uuid, sourceName, duration.label, description | Документ системный и наследуемые поля различены |
| and/eq и регистрация partial | [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Системные Handlebars helpers | Логические условия; preload | each/if/unless — встроенные; not/localize — Foundry |
| CSS | [styles/activeEffect.css](../../../../../../styles/activeEffect.css); [styles/system-styles.css](../../../../../../styles/system-styles.css) | Классы разметки | Список/строки/description; invisible скрывает display | Связанные selectors прочитаны |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) | Partial | Вкладка эффектов Character/Monster V2 | Явное включение |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../templates/sheets/actor/monster-sheet.hbs) | Partial | Монстр V1 | Явное включение; управление через ActorSheetV1 |
| [templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs](../../../../../../templates/sheets/item/configuration/tabs/activeEffectConfiguration.hbs) | Partial | Настройка Item | Явное включение; собственные actions конфигурации |
| [module/setup/handlebars.js](../../../../../../module/setup/handlebars.js) | Путь partial | Предзагрузка | Не отдельный renderer |

## Данные и изменения состояния

В заголовке нет effectId; create получает тип категории из ближайшего li. В строках parentUuid позволяет Actor-листу открыть эффект предмета и запретить его удаление из чужого родителя. Иконка toggle выбирается по disabled, не isDisabled/isSuppressed. Шаблон не удаляет скрытые эффекты и не меняет их значения.

description выводится как HTML без дополнительного вызова TextEditor здесь; полное исследование подготовки/очистки такого текста не выполнено. На Actor раскрытие подключено; на Item конфигурация не регистрирует соответствующий listener.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Контекст/обработчики | 53 строки; три места включения и preload, Actor/Item обработчики | Все selectors/data-* имеют описанных потребителей; для Item effect-display потребитель не найден | Поиск module/item/sheets; внешние модули не проверены |
| Рендер | Настоящий Handlebars, реальные shape категорий, подмены helpers | Сохраняется parent UUID; description invisible; suppressed эффект скрыт только при actor | Не браузер |
| Раскрытие | Исходный Actor-метод с jQuery-double | Непустое описание меняет invisible | Не доказывает работу того же действия на Item |

## Непроверенные участки и открытые вопросы

Drag/drop, фактическая очистка description, разрешения UI и влияние сторонних модулей требуют полного разбора использующих листов/ядра. HTML списка не означает наличия обработчика любого клика во всех потребителях.

## Связанные проблемы

[issue-00056](../../../../../issues/potential/issue-00056.md) — раскрытие описания в Item-конфигурации.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.010 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
