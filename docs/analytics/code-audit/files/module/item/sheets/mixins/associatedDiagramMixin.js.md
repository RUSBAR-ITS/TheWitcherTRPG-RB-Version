# module/item/sheets/mixins/associatedDiagramMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../../review-log.md#task-0003016) |

## Назначение файла

Примесь листов оружия и брони: удаление ссылки на рецепт и принятие сброшенного рецепта допустимой категории.

## Условия использования

WitcherWeaponSheet/WitcherArmorSheet импортируют named associatedDiagramMixin и копируют методы в prototype через Object.assign. Их activateListeners вызывает _addAssociatedDiagramListeners, _onDropItem делегирует _onDropDiagram с двумя допустимыми категориями.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| associatedDiagramMixin | export let, объект | Три метода листа | Object.assign в двух листах | События/проверка/запись ссылки |
| jquery | Локальная переменная | $(html) | _addAssociatedDiagramListeners | jQuery поиск/привязка click |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _addAssociatedDiagramListeners(html) | DOM листа | undefined | $(html).find('.remove-associated-diagram').on('click', bound remove) | Только удаление; add-associated-diagram listener нет |
| async _onRemoveAssociatedDiagram(event) | Событие, this.item | Promise<void> | preventDefault; update {'system.associatedDiagramUuid':''} | update не await/return; связанный рецепт не удаляется |
| async _onDropDiagram(event,item,...diagramTypes) | Область offsetParent.dataset.type=associatedDiagram; допустимые типы | Promise<void> | Falsy item пропускает; чужая область пропускает; Item.type!=diagrams либо неподходящая system.type→warn; иначе update uuid | null offsetParent даёт TypeError; warn локализован; запись не await/return |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| associatedDiagramUuid | [module/data/item/templates/associatedDiagramData.js](../../../../../../../../module/data/item/templates/associatedDiagramData.js) | Контракт схемы | Целевой путь update | Определение и обращение сверены |
| associated-diagram.hbs | [templates/partials/associated-diagram.hbs](../../../../../../../../templates/partials/associated-diagram.hbs) | DOM-контракт | data-type и remove-класс | Определение и обращение сверены |
| $ / jQuery.on | jQuery, глобальный API клиента | Внешний API | Привязка listener | Определение и обращение сверены |
| Item.update / ui.notifications.warn / game.i18n.localize | Foundry API | Внешний API | Сохранение и сообщение | Определение и обращение сверены |
| WITCHER.Repair.alerts.invalidDiagram | [lang/ru.json](../../../../../../../../lang/ru.json) | Локализация | Предупреждение неподходящего рецепта | Определение и обращение сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../../module/item/sheets/WitcherWeaponSheet.js) | Все три метода | Object.assign; _onDropDiagram(event,item,'weapon','elderfolk-weapon') | Прямой импорт и вызовы |
| [module/item/sheets/WitcherArmorSheet.js](../../../../../../../../module/item/sheets/WitcherArmorSheet.js) | Все три метода | Object.assign; _onDropDiagram(event,item,'armor','elderfolk-armor') | Прямой импорт и вызовы |
| [templates/partials/associated-diagram.hbs](../../../../../../../../templates/partials/associated-diagram.hbs) | Удаление / область drop | Класс и data-type | Разметка |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Меняется только строка UUID в оружии/броне; рецепт не копируется в инвентарь, associatedItemUuid самого рецепта не меняется. Проверка типа находится в этой примеси, в unwrapAssociatedDiagram её нет. Область выбирается по offsetParent (контексту позиционирования), не closest('[data-type]'); поведение зависит от геометрии DOM. Вызывающие _onDropItem также не await/return вложенный Promise.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Матрица drop | Настоящий _onDropDiagram; item=null, component, неверная/верная категория, чужая область, offsetParent=null | Пропуски, два warn, запись допустимого UUID и TypeError на null | DOM/Item.update фасады |
| Удаление/слушатель | Исходный remove, существующие вызовы weapon/armor | Пустая строка update; .remove-associated-diagram click | Запись/браузер не запускались |
| Категории | Ранее сверенные weapon/armor callers, перечни перечитаны | По два разрешённых типа; новый разбор охватывает всю примесь | Предыдущие runtime-проверки не объявлены новыми |

## Непроверенные участки и открытые вопросы

В TASK-0004.007 текущие определения и потребители сопоставлены; прежние опыты TASK-0003.015/.016/.017 (2026-09-10) и .034 (2026-09-11) сохраняют собственные входы и фасады. Браузер, мир, сеть и запись в БД не запускались. Точные оставшиеся вопросы и ответственные блоки: [U007-01](../../../../../cross-check-0002.md#u007-01), [U007-03](../../../../../cross-check-0002.md#u007-03). Для этого файла установлены процессы R007-12, R007-11, а не полный клиентский lifecycle.

## Связанные проблемы

[issue-00080](../../../../../../../issues/potential/issue-00080.md), [issue-00099](../../../../../../../issues/closed/issue-00099.md). 80 — общий offsetParent/Promise; 99 — противоположные подсказки в используемом partial.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Сквозная сверка TASK-0004.007

2026-09-14; rusbar-main, 6a26042f7881d9990c304483c7219e0698f6617e. Исходник совпадает со срезом TASK-0001; изменено только описание.

AssociatedDiagramMixin принимает diagrams нужной weapon/armor или elderfolk категории и записывает UUID. Область определяет через offsetParent.dataset без проверки null. Remove обнуляет ссылку, плюс не имеет собственного picker; wrapper Weapon/Armor не ждёт вложенный async. Связанный результат рецепт получает независимо.

Сопоставленные определения и потребители: [module/data/item/templates/associatedDiagramData.js](../../../data/item/templates/associatedDiagramData.js.md), [templates/partials/associated-diagram.hbs](../../../../templates/partials/associated-diagram.hbs.md), [lang/ru.json](../../../../lang/ru.json.md), [module/item/sheets/WitcherWeaponSheet.js](../WitcherWeaponSheet.js.md), [module/item/sheets/WitcherArmorSheet.js](../WitcherArmorSheet.js.md).

[Протокол и границы](../../../../../review-log.md#task-0004007) — TASK-0004.007; процессы [R007-12](../../../../../cross-check-0002.md#r007-12), [R007-11](../../../../../cross-check-0002.md#r007-11). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Единственный новый запуск N007-01 проверяет producer/HBS alchemyComponentsList на заданном контексте; его границы не распространяются на остальные процессы.
