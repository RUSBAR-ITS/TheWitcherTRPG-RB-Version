# module/data/item/diagramData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/diagramData.js](../../../../../../../module/data/item/diagramData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../review-log.md#task-0003016) |

## Назначение файла

Модель Item типа diagrams: рецепт или формула, требования материалов/субстанций, сложности, результат и подготовка связанных документов.

## Условия использования

CONFIG.Item.dataModels.diagrams регистрируется registerDataModels. CommonItemData задаёт общие поля. Подготовка модели разрешает UUID синхронно; миграция выполняется при создании модели Foundry и не ограничена отдельной версией старых данных.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| DiagramData | default class | Схема и подготовка рецепта | Тип Item diagrams | Миграция/очистка/derived |
| fields; commonData | Локальные значения | DataFields и родительские поля | Внутри defineSchema | Сборка схемы |
| type; level; craftingTime; associatedItemUuid | StringField, initial='' | Категория, уровень, время и UUID результата | system | Хранение |
| isFormulae; learned | BooleanField, initial=false | Режим формы и отметка изученности | system | Редактор / инвентарь |
| craftingDC; alchemyDC; investment | NumberField, initial=0 | Две сложности и инвестиции | system | Чтение потребителями |
| craftingComponents | ArrayField(SchemaField(craftingComponent())) | Материалы рецепта | system | Редактирование массива и обогащение |
| alchemyComponents | SchemaField девяти NumberField initial=0 | vitriol, rebis, aether, quebrith, hydragenum, vermilion, sol, caelum, fulgur | system | Требования субстанций |
| resultQuantity | NumberField initial=1 | Количество результата | system | Выдача через Actor.addItem |
| associatedItem; обогащённые записи | Вычисляемые значения вне собственной схемы | Разрешённый результат, img/type и актуальное имя материала | prepareDerivedData | Подготовленная модель, не запись Item |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Вызов Foundry | 20 верхних полей | 8 общих + 12 собственных; две вложенные структуры | Числам не заданы min/max/integer |
| prepareDerivedData() | Подготовленная модель | undefined | super; associatedItem=fromUuidSync при непустом UUID; присваивает enrichDiagramComponents | Не update; пустой UUID не очищает уже выставленное свойство в ручном повторе |
| enrichDiagramComponents(craftingComponents) | Массив записей либо falsy | Новый массив или undefined | Без uuid/документа сохраняет запись; иначе spread + name/img/type из документа; quantity ?? 1 | fromUuidSync может вернуть индекс/документ/null или бросить; собственного catch нет |
| static migrateData(source) | Исходный объект | super.migrateData(source) | associatedItem._id→Compendium.TheWitcherTRPG.gear.Item.ID; alchemyDC>0→craftingDC | Меняет source; без проверки заполненного нового поля; старые ключи сам не удаляет |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Прямой импорт / наследование | Общие данные и lifecycle | Определение и потребитель сверены |
| craftingComponent() | [module/data/item/templates/craftingComponentData.js](../../../../../../../module/data/item/templates/craftingComponentData.js) | Прямой импорт / схема | id/name/quantity/uuid каждой записи | Определение и потребитель сверены |
| foundry.data.fields / TypeDataModel lifecycle | Foundry API | Внешний API | Схема, очистка, миграция | Определение и потребитель сверены |
| fromUuidSync | Foundry 14.367: /opt/foundryvtt/client/utils/helpers.mjs:188 | Глобальная функция | Разрешение результата и материалов; возможна запись индекса | Определение и потребитель сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | DiagramData | Импорт и тип diagrams | Реестр |
| [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../module/item/sheets/WitcherDiagramSheet.js) | craftingComponents / schema | Подготовка контекста и CRUD | Лист рецепта |
| [templates/sheets/item/diagrams-sheet.hbs](../../../../../../../templates/sheets/item/diagrams-sheet.hbs) | Собственные поля | Условия и редактор | system.* |
| [templates/partials/associated-item.hbs](../../../../../../../templates/partials/associated-item.hbs) | associatedItem/resultQuantity | Представление результата | Включение из основного HBS |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | associatedItem/UUID/resultQuantity; DC/components | isAlchemicalCraft, alchemyCraftComponentsList, realCraft | Выбор требований/выдача |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | craftingComponents/craftingDC/alchemyDC | Предварительная проверка и порог броска | _craftingCraft/_alchemyCraft |
| [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | craftingComponents/craftingDC | Поиск материалов и DC ремонта | prepareData / RepairData |
| [module/item/mixins/dismantlingMixin.js](../../../../../../../module/item/mixins/dismantlingMixin.js) | craftingComponents | Возврат материалов при разборке | dismantle |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs) | learned/isFormulae/компоненты | Описание и отметка изученности | HBS |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Общие поля CommonItemData: description:String='', quantity:String='1', weight:Number=0, cost:Number=0, sourcebook:String='', isHidden=false, isStored=false, isCarried=true. calcWeight и getters canHaveTemporaryItemImprovement=false/canBeRepaired=false наследуются. Из 12 собственных полей craftingComponents — массив записей, alchemyComponents — объект девяти чисел. Источник UUID и количество результата задаются независимо: обратный associatedDiagramUuid оружия/брони автоматически не записывается.

Для доступного UUID модель заменяет имя материала в prepared-массиве и добавляет img/type; исходный toObject() сохранил старое имя. Сериализация toObject(false) идёт по схеме и не включает добавленные img/type. Для недоступного UUID модель сохраняет имя, но лист затем теряет его в отдельном map. Исходный quantity=0 не заменяется на 1; null/undefined для разрешённой записи заменяется через ??.

В реальной новой DiagramData alchemyDC12/craftingDC20 дали craftingDC12 даже при isFormulae=false. Старый associatedItem вместе с современным UUID заменил его жёстко собранным компедиумным адресом. isAlchemicalCraft читает положительный alchemyDC, а форма переключается по isFormulae; это отдельное рассогласование. learned изменяется потребителем инвентаря, не этой моделью.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема/обогащение | Настоящая DiagramData и BaseItem; UUID-карта | 20 полей; 3 вида записи: разрешённая, недоступная, без UUID; сохранён ID и количество | Нет загрузки настоящего pack |
| Миграция | 4 конструктора с современными/смешанными данными | Современный UUID перезаписан старым; 20→12; контроль без старых полей сохраняется | Проверка в памяти |
| Границы | undefined, пустой список, quantity0 | undefined→undefined; []→[] по map; 0 остаётся0 | Полный Item reset не запускался |
| Контракт UI/применения | Настоящие _prepareContext/isAlchemicalCraft и формы | Неразрешённая запись теряет имя в листе; isFormulae=false/DC12 всё равно алхимия | realCraft полностью заново не запускался |

## Непроверенные участки и открытые вопросы

Foundry 14.367.0, Node 24.16.0. Настоящие модели и код исполнялись изолированно; документы мира, сеть, браузерный submit и БД не запускались. fromUuidSync представлен картой с настоящим BaseItem/null; поведение core с индексом и embedded Compendium установлено по исходнику. Старый associatedItem=null/неожиданного типа и ошибка разрешения UUID не объявлены допустимым миграционным входом. Сохранение промежуточных свойств при полном reset Foundry не проверялось. Изготовление, списание и ремонт полностью остаются внешними процессами.

## Связанные проблемы

[issue-00095](../../../../../../issues/potential/issue-00095.md), [issue-00097](../../../../../../issues/potential/issue-00097.md), [issue-00101](../../../../../../issues/potential/issue-00101.md), [issue-00037](../../../../../../issues/potential/issue-00037.md), [issue-00038](../../../../../../issues/potential/issue-00038.md), [issue-00041](../../../../../../issues/potential/issue-00041.md). 95 — потеря данных листом; 97 — миграция; 101 — разные признаки режима. Остальные — ранее описанные границы изготовления.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.017

2026-09-10, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; исходники неизменны. [Сверка](../../../../review-log.md#task-0003017).

Полностью разобран потребитель [RepairSystem](../../../../../../../module/item/systems/repair.js). Он читает craftingComponents/name/uuid и craftingDC, но не quantity требования, resultQuantity, associatedItemUuid, isFormulae или alchemyComponents. Каждая строка ремонта получает required1; это фиксация алгоритма, соответствие рулбуку не утверждается. UUID отсутствующего компонента может дать null и прервать подготовку ([issue-00105](../../../../../../issues/potential/issue-00105.md)); только unknown требования скрываются в чате из-за caller guard ([issue-00107](../../../../../../issues/potential/issue-00107.md)). Реальная DiagramData сохраняет допустимые UUID; ошибочный 15-символьный ID диагностического входа был исправлен до итоговых сценариев, это не issue системы.

## Уточнение TASK-0003.026

2026-09-11, `rusbar-main`, `45a63062a2bd55939fef430609fc5dddc350b0e9`. _onItemLearned переключает существующее system.learned, не SkillItemData.isLearned. Для создания handler отдельно проверяет itemtype='diagram', которого нет в manifest; штатный itemtype='diagrams' проходит Item.create без такого preset и получает defaults. Это различие ветвей зафиксировано без признания обязательности alchemical preset для всех рецептов. Контекстное canBeDismantled читает associatedDiagramUuid у weapon/armor, сам рецепт здесь не списывается.

Определения: [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) и [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003026). Полный разбор новых соседних файлов вне порции не засчитывается.

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Нынешняя таблица рецепта показывает isFormulae-dependent DC, learned, компоненты и результаты enrichDiagramComponents. Вложенный helper получил ../../actor и дал6/3, алхимический список5/2. Нет кнопки связанного результата/associatedDiagramUuid. Кнопка формулы направлена в _craftingCraft — issue-00176; isFormulae и alchemyDC продолжают иметь отдельную проблему issue-00101.

Связанные шаблоны: [templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-diagrams.hbs). [Проверки и ограничения](../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Полный Character группирует рецепты в 13 списков по system.type, отдельно от isFormulae и isAlchemicalCraft. Обычный диалог читает craftingComponents/craftingDC; missing associatedItem допускается моделью, но обращение к .name при нехватке ресурсов падает (issue-00201). Кнопка .crafting-craft сохраняет ранее описанное несовпадение режима формулы.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../actor/sheets/WitcherCharacterSheet.js.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).

## Уточнение TASK-0003.034

2026-09-11, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`. dismantle читает craftingComponents и обрабатывает строки по одной: max(1,floor(quantity/2)); isFormulae/alchemyComponents/resultQuantity не используются. enrichDiagramComponents сохраняет строку при недоступном UUID, но последующий dismantle теряет её name/uuid в {item:null,quantity} (новая issue-00216). Это отдельный путь от прежней issue-00095 листа рецепта.

Связи: [module/item/mixins/dismantlingMixin.js](../../item/mixins/dismantlingMixin.js.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003034).
