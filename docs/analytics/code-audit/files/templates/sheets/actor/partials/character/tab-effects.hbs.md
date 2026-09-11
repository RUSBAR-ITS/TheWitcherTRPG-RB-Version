# templates/sheets/actor/partials/character/tab-effects.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/tab-effects.hbs](../../../../../../../../../templates/sheets/actor/partials/character/tab-effects.hbs) |
| Тип файла | Handlebars, HTML-шаблон |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `247d3d86e344238a1445377c686eb6455146693c` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.010](../../../../../../../../tasks/task-0003.010.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.010](../../../../../../review-log.md#task-0003010) |

## Назначение файла

Вкладка критических травм и ActiveEffect для современных листов персонажа и монстра: создание/лечение травмы, дни заживления и общий список эффектов.

## Условия использования

PARTS.effects в WitcherCharacterSheet и WitcherMonsterSheet использует этот путь; базовый WitcherActorSheet готовит контекст и listeners. Файл содержит 60 логических строк с CRLF; исходник не перезаписывался.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| section.tab | 1,60 | Вкладка effects | data-group=primary, data-tab=effects, tabs.effects.cssClass | Навигация листа |
| a.add-crit | 6 | Добавление травмы | data-action=addCrit и class add-crit | Реальный listener подключён по классу |
| Partial crit-wounds-table.hbs | 8 | Первый список травм | Текущий document/items/config | Выводит тот же тип Item, что и цикл ниже |
| each document.items.documentsByType.criticalWound | 11–52 | Второй список с описанием и лечением | li data-item-id, data-type=critWound | Имя, criticalLevel/treatment/location, дни и healingTime |
| days-healed.inline-edit / treatCriticalWound | 38–50 | Изменение daysHealed и лечение | data-field=system.daysHealed; data-action=treatCriticalWound/data-id=UUID | healingTime disabled; description через criticalWounds[uuid].enriched |
| Partial effect-part.hbs | 58 | Общий список ActiveEffect | effects/document/actor | Собственных новых обработчиков нет |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| Рендер Handlebars; 1–60 | document.items, config, criticalWounds, effects, tabs | HTML вкладки | each, lookup, localize, два partial; enriched выводится как HTML | JS-функций и изменения состояния в HBS нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| PARTS.effects | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Регистрация части | Путь шаблона и tabs.effects | Оба V2-листа используют один файл |
| Контекст и подключения | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | _prepareContext/_prepareItems/_onRender | config=WITCHER; criticalWounds по UUID после enrichedText; effects и listeners | Item-описания готовятся асинхронно до рендера |
| Критические травмы | [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js); [module/data/item/criticalWoundData.js](../../../../../../../../../module/data/item/criticalWoundData.js) | DOM → действие модели | add-crit создаёт Item criticalWound; treat resolve UUID → system.treat() | Полный процесс лечения модели остаётся отдельным разбором |
| Редактирование Item | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | inline-edit/change | _onItemInlineEdit читает ближайший itemId и вызывает item.update({[field]:value}) | Число приходит из input.value строкой; очистка данных — ядро |
| Partial травм | [templates/partials/crit-wounds-table.hbs](../../../../../../../../../templates/partials/crit-wounds-table.hbs) | Включение | Повторяет цикл того же criticalWound-массива | Полностью прочитан для проверки дублирования, отдельная карточка не создавалась |
| Partial эффектов | [templates/partials/effect-part.hbs](../../../../../../../../../templates/partials/effect-part.hbs); [module/actor/sheets/mixins/activeEffectMixin.js](../../../../../../../../../module/actor/sheets/mixins/activeEffectMixin.js) | Включение и listeners | Список/управление эффектами | Полный разбор в этой порции |
| Карты подписей и helpers | [module/setup/config.js](../../../../../../../../../module/setup/config.js); [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js); [lang/en.json](../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../lang/ru.json) | config.critLevel/critTreatment/location, preload, localize | Ключи травмы преобразуются в локализованные подписи | lookup/each встроены в Handlebars |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Полный шаблон | Часть effects двух листов | Прямые пути PARTS |
| [module/setup/handlebars.js](../../../../../../../../../module/setup/handlebars.js) | Путь шаблона | Предзагрузка | Не самостоятельный лист |

## Данные и изменения состояния

Шаблон одновременно включает старую таблицу травм и сам повторно выводит те же документы. Для одной травмы получаются две строки и две кнопки лечения. Это дублирование интерфейса, а не создание второй травмы или доказательство двойного выполнения лечения от одного клика.

Новый цикл использует details/summary и enriched-описание; старый partial такого описания не выводит. healingTime read-only, daysHealed сохраняется через общий Item-listener. Добавление и лечение не осуществляются самим атрибутом data-action: соответствующие listeners регистрирует criticalWoundMixin.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полнота | 60 строк; оба PARTS, подготовка контекста, partial и listeners | Отслежены все поля и действия | Смежные файлы целиком не считаются разобранными |
| Рендер и дублирование | Настоящий Handlebars с обоими исходными partial; parse5 разбирает полученный HTML | Одна фикстура wound → 2 data-item-id строки, 2 treat-кнопки; enriched появился в новом цикле | Без браузера, лечения и БД |
| Сохранение дней | Прочитан _onItemInlineEdit и регистрация .inline-edit | field=system.daysHealed, itemId из строки, update получает input.value | Очистка/сохранение настоящего документа не запускались |

## Непроверенные участки и открытые вопросы

Полное лечение/заживление, таблицы критических травм, drag/drop и работа листа в браузере остаются будущим порциям. Наличие кнопки не подтверждает корректность процесса лечения.

## Связанные проблемы

[issue-00054](../../../../../../../../issues/potential/issue-00054.md) — двойное представление травм.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.010 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.020

2026-09-11, `rusbar-main`, `b09f992960a76d1c75946f402e42d93fa0785008`; проверены связи с критическими травмами, лечением и отдыхом. Полный первоначальный разбор и его ограничения сохранены.

| Связь | Файл | Результат проверки |
| --- | --- | --- |
| crit-wounds-table.hbs | [templates/partials/crit-wounds-table.hbs](../../../../../../../../../templates/partials/crit-wounds-table.hbs) | Исходный HBS повторно отрендерен: одна травма дала 2 строки data-item-id и 2 treat-кнопки. Это повторный вывод, не создание документов (issue-00054). |
| criticalWoundMixin | [module/actor/sheets/mixins/criticalWoundMixin.js](../../../../../../../../../module/actor/sheets/mixins/criticalWoundMixin.js) | add-crit создаёт Item, treat вызывает system.treat по UUID; не устанавливает treatment=treated. |
| Inline daysHealed | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | Передаётся строка; NumberField модели очищает её числом. В текущем _onTreat нет чтения inline-счётчика напрямую. |

[Сверка порции и итоговая сверка 96 файлов второй серии](../../../../../../review-log.md#task-0003020); браузер, мир и записи в БД не запускались.

## Уточнение TASK-0003.025

2026-09-11, `rusbar-main`, `a2670a0a10c62b28d836b1a57577c4836f14cf20`. Прослежен producer criticalWounds: общий V2 собирает объект description={value,enriched,systemField} по critWound.uuid и ждёт все enrich. lookup (...,'enriched') соответствует producer. V1 такого контекста не создаёт и текущий шаблон не использует. Перебор actual Item по document.items.documentsByType остаётся отдельным от словаря; это не устраняет двойной список issue-00054. Категории effects также могут повторить один документ (issue-00165).

Общие определения: [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) и [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js). [Методика и перекрёстная сверка](../../../../../../review-log.md#task-0003025). Это точечное уточнение связей; полный разбор новых соседних файлов не засчитывается.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. PARTS.effects специализированного Character напрямую указывает на этот шаблон. effects-контекст готовится базовым Actor-листом, вкладки — Character._prepareTabs('primary'); весь lifecycle эффектов повторно не запускался.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../../../../module/actor/sheets/WitcherCharacterSheet.js.md). [Методика и ограничения сверки](../../../../../../review-log.md#task-0003031).

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Полный MonsterSheet.PARTS.effects выбирает эту общую часть; контекст categories готовит базовый ActorSheet. Старый полный monster-sheet использует иной effect-part; оба маршрута явно разделены.

Связи: [module/actor/sheets/WitcherMonsterSheet.js](../../../../../module/actor/sheets/WitcherMonsterSheet.js.md); [templates/sheets/actor/monster-sheet.hbs](../../monster-sheet.hbs.md). [Результаты и пределы проверки](../../../../../../review-log.md#task-0003032).
