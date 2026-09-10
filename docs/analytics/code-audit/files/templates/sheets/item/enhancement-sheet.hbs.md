# templates/sheets/item/enhancement-sheet.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/item/enhancement-sheet.hbs](../../../../../../../templates/sheets/item/enhancement-sheet.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `0fa589bd300856ff309f362afcb66d6fa43401ab` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.014](../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../review-log.md#task-0003014) |

## Назначение файла

Форма категории улучшения, его бронирования/сопротивлений и редактируемых предметных воздействий.

## Условия использования

PARTS.main WitcherEnhancementSheet; section.scrollable, item-header partial. Контекст item/config/selects; данные берутся из EnhancementData. Не содержит формы документа ActiveEffect.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| item-header | 2 | Общие поля предмета | Partial | Название, количество, вес, цена, книга-источник |
| system.type | 5–8 | Категория | selectOptions selects.enhancementTypes | weapon/rune/armor/glyph |
| system.avail | 11–37,22–24 | Доступность | Только type armor | config.Availability |
| system.stopping | 26 | Бонус SP | Только armor; text input data-dtype Number | Модель NumberField |
| system.bludgeoning/slashing/piercing | 28–30 | Физические сопротивления | Только armor; checkbox | Checked из полей модели |
| system.effects | 39–71 | Редактор словаря | each effect,id; data-target system.effects | Добавление/удаление, имя, statusEffect и percentage |
| Выбор statusEffect | 55–60 | Статус оружия или свойство брони | weapon/rune → config.statusEffects; остальные → config.armorEffects | valueAttr id, labelAttr name, blank='', localize=true |
| percentage | 64–67 | Процент записи | Для всех категорий | text/data-dtype Number, без name, ручной editEffect |

## Основные функции и методы

Функций нет. if/eq включает физические бонусы только для точной строки armor; glyph не входит в эту ветвь. Внутри each условия or/eq выбирают список статусов. addEffect/removeEffect/editEffect обслуживаются базовым WitcherItemSheet, обычные именованные поля — общей формой.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WitcherEnhancementSheet | [module/item/sheets/WitcherEnhancementSheet.js](../../../../../../../module/item/sheets/WitcherEnhancementSheet.js) | PARTS/context | selects.enhancementTypes | Список полностью проверен |
| EnhancementData; itemEffect | [module/data/item/enhancementData.js](../../../../../../../module/data/item/enhancementData.js); [module/data/item/templates/itemEffectData.js](../../../../../../../module/data/item/templates/itemEffectData.js) | Поля модели | Тип, бонусы, словарь | 16 верхних полей и четыре поля записи |
| WitcherItemSheet | [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | Actions/change/submit | Добавление percentage=0, edit target.id.field, удаление -=id | Методы вызваны отдельно |
| CONFIG.statusEffects/armorEffects/Availability | [module/setup/config.js](../../../../../../../module/setup/config.js) | Варианты UI | Три selectOptions | Различие списка по категории сверено |
| item-header.hbs | [templates/partials/item-header.hbs](../../../../../../../templates/partials/item-header.hbs) | Partial | 2 | Унаследованные общие поля |
| Ключи локализации | [lang/ru.json](../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../lang/en.json) | localize | Type/Diagram/Enhancement/Item/Percentage | Все буквальные ключи проверены |
| Handlebars/форма | Foundry 14.367.0 и клиентская библиотека Handlebars | Внешний API | Рендер и submit | Handlebars/parse5 настоящие, selectOptions — ограниченный генератор |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherEnhancementSheet.js](../../../../../../../module/item/sheets/WitcherEnhancementSheet.js) | Шаблон | PARTS.main | 6 |
| [module/item/sheets/WitcherItemSheet.js](../../../../../../../module/item/sheets/WitcherItemSheet.js) | data-action/data-field | Унаследованный редактор effects | DEFAULT_OPTIONS/_onChangeForm/_onEditEffect |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Форма не показывает applied, varEffect и собственный редактор description; описание остаётся полем модели. Переключение категории скрывает блок физической брони, но не сбрасывает stopping/сопротивления или выбранный statusEffect. Это факт разметки, не автоматически ошибка: последствия и допустимые категории определяются внешним процессом установки.

Строки воздействий без name сохраняются отдельным update по ID. data-dtype Number на percentage не заменяет логику ручного обработчика: тот передаёт строку до очистки моделью. Верхние числовые ограничения задаёт itemEffect.percentage, а не HTML.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Пять вариантов | Пустой type, weapon,rune,armor,glyph | С header 6/6/6/11/6 именованных полей; всегда три editable-поля эффекта | Мир не запускался |
| Списки статусов | Render с текущими CONFIG-массивами | weapon/rune используют statusEffects, остальные armorEffects | selectOptions воспроизводит нужные valueAttr/labelAttr, не весь внешний helper |
| Редактор | Исходный базовый _onEditEffect с value on | Запись name=false; NumberField отдельно очистил percentage | Известная issue-00060, без исправления |

## Непроверенные участки и открытые вопросы

Не выполнено полноценное редактирование и переоткрытие Item в клиенте. Границы категории glyph и применения процентных сопротивлений не подменены предположениями о правилах.

## Связанные проблемы

[issue-00060](../../../../../../issues/potential/issue-00060.md), [issue-00084](../../../../../../issues/potential/issue-00084.md). Обработчик имени и внешний маршрут применения воздействий брони; форма не исправляет несовместимость потребителя.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
