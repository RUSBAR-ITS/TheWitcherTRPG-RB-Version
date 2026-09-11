# module/data/item/templates/associatedDiagramData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/associatedDiagramData.js](../../../../../../../../module/data/item/templates/associatedDiagramData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../../review-log.md#task-0003016) |

## Назначение файла

Общая фабрика поля обратной ссылки оружия/брони на рецепт и функция синхронного раскрытия этой ссылки.

## Условия использования

WeaponData и ArmorData напрямую импортируют две named-функции. associatedDiagramUuid вызывается в defineSchema, unwrapAssociatedDiagram — в prepareDerivedData после обработки улучшений.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальный alias | foundry.data.fields | Внутри модуля | StringField |
| associatedDiagramUuid | named function | Одно поле StringField initial='' | Схемы Weapon/Armor | Хранение UUID |
| unwrapAssociatedDiagram | named function | Связанный объект associatedDiagram | Derived моделей | Синхронное разрешение |
| parent.associatedDiagram | Подготовленное свойство | Документ/индекс/null | Вне возвращаемой схемы | Присваивается при truthy UUID |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| associatedDiagramUuid() | Без аргументов | Объект {associatedDiagramUuid: StringField} | Возвращает описание поля | Не разрешает и не записывает документ |
| unwrapAssociatedDiagram(parent) | Объект с associatedDiagramUuid | undefined | Если diagramId truthy: parent.associatedDiagram=fromUuidSync(diagramId) | Пустой UUID пропускается; тип рецепта не проверяется; catch/async нет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| foundry.data.fields | Foundry DataField API | Внешний API | StringField | Определение и потребитель сверены |
| fromUuidSync | Foundry 14.367: /opt/foundryvtt/client/utils/helpers.mjs:188 | Внешний API | Документ/индекс/null; strict для embedded Compendium | Определение и потребитель сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/weaponData.js](../../../../../../../../module/data/item/weaponData.js) | Обе функции | defineSchema/prepareDerivedData | Прямой импорт |
| [module/data/item/armorData.js](../../../../../../../../module/data/item/armorData.js) | Обе функции | defineSchema/prepareDerivedData | Прямой импорт |
| [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js) | associatedDiagramUuid | Drop/очистка строки UUID | Item.update |
| [templates/partials/associated-diagram.hbs](../../../../../../../../templates/partials/associated-diagram.hbs) | associatedDiagram | Представление связанного рецепта | Динамическое чтение |
| [module/item/systems/repair.js](../../../../../../../../module/item/systems/repair.js) | associatedDiagramUuid | Самостоятельный await fromUuid для ремонта | prepareData |
| [module/item/mixins/dismantlingMixin.js](../../../../../../../../module/item/mixins/dismantlingMixin.js) | associatedDiagramUuid | Доступность и await fromUuid | canBeDismantled/dismantle |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Строка схемы не DocumentUUIDField; класс рецепта и категория проверяются в UI-примеси, не здесь. Прямой UUID компонента тоже раскрывается. Пустая строка в ручном повторе оставила старое associatedDiagram; неразрешённая непустая строка присвоила null. Это наблюдение функции без утверждения о полном reset Item. Ссылка на рецепт не записывает встречный associatedItemUuid. Ремонт/разборка сами получают документ асинхронно и не полагаются только на prepared associatedDiagram.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Потребители | Полные Weapon/Armor карточки и места вызова | Два импорта; вызов после улучшений | Предыдущие проверки моделей не повторялись |
| Границы раскрытия | Настоящая функция; UUID '', доступный, отсутствующий | Старое значение / объект / null; нет writes | UUID API заменён картой |

## Непроверенные участки и открытые вопросы

Foundry 14.367.0, Node 24.16.0. Настоящие модели и код исполнялись изолированно; документы мира, сеть, браузерный submit и БД не запускались. Не исследованы загрузка pack, восстановление документа после reset и сообщения при неразрешимом embedded UUID. issue-00077 касается более раннего этапа модели и не ошибки этой фабрики.

## Связанные проблемы

[issue-00077](../../../../../../../issues/potential/issue-00077.md), [issue-00080](../../../../../../../issues/potential/issue-00080.md), [issue-00096](../../../../../../../issues/potential/issue-00096.md). Границы до раскрытия, UI-drop и неверный путь описания в partial.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.034

2026-09-11, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`. dismantle разрешает associatedDiagramUuid через fromUuid заново; prepared associatedDiagram не использует. canBeDismantled возвращает truthy строку для weapon/armor, не проверяя разрешение. Отсутствующий рецепт/неподходящая структура дали TypeError до выдачи/списания (issue-00215).

Связи: [module/item/mixins/dismantlingMixin.js](../../../item/mixins/dismantlingMixin.js.md). [Результаты и пределы проверки](../../../../../review-log.md#task-0003034).
