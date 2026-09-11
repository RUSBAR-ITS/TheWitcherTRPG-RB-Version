# module/data/item/componentData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/componentData.js](../../../../../../../module/data/item/componentData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `53f74994011383cb544cabac96285430f00cb38a` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.016](../../../../../../tasks/task-0003.016.md), одна порция из двенадцати файлов |
| Запись перекрёстной сверки | [TASK-0003.016](../../../../review-log.md#task-0003016) |

## Назначение файла

Модель Item типа component: материал, часть животного, алхимический компонент, минерал или субстанция; хранит описательные сведения и категорию.

## Условия использования

registerDataModels присваивает ComponentData в CONFIG.Item.dataModels.component. Foundry создаёт system-модель Item; класс напрямую расширяет CommonItemData. При импорте создаётся только alias fields и объявляется класс.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| ComponentData | default class extends CommonItemData | Данные component | CONFIG.Item.dataModels.component | Создание/очистка через Foundry |
| fields; commonData | Локальный alias и переменная defineSchema | Конструкторы полей / родительская схема | Внутри файла/метода | Сборка схемы |
| type | StringField, initial='' | Категория или описательное значение | system.type | Хранение и редактирование основным листом |
| rarity | StringField, initial='' | Категория или описательное значение | system.rarity | Хранение и редактирование основным листом |
| location | StringField, initial='' | Категория или описательное значение | system.location | Хранение и редактирование основным листом |
| quantityObtainable | StringField, initial='' | Категория или описательное значение | system.quantityObtainable | Хранение и редактирование основным листом |
| forage | StringField, initial='' | Категория или описательное значение | system.forage | Хранение и редактирование основным листом |
| substanceType | StringField, initial='' | Категория или описательное значение | system.substanceType | Хранение и редактирование основным листом |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Вызов Foundry | 14 полей: 8 общих + 6 собственных | super.defineSchema; создание строковых полей | Никаких writes/миграций/расчёта добычи |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Прямой импорт / наследование | Схема, calcWeight и getters | Определение и потребитель сверены |
| foundry.data.fields | Foundry DataField API | Внешний API | StringField | Определение и потребитель сверены |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | ComponentData | Импорт и регистрация component | Реестр |
| [module/item/sheets/WitcherComponentSheet.js](../../../../../../../module/item/sheets/WitcherComponentSheet.js) | system/schema | Контекст из базового ItemSheet | Специализированный лист |
| [templates/sheets/item/component-sheet.hbs](../../../../../../../templates/sheets/item/component-sheet.hbs) | Шесть полей модели | Категория/субстанция/доступность и текстовые поля | name=system.* |
| [module/actor/mixins/craftingMixin.js](../../../../../../../module/actor/mixins/craftingMixin.js) | type/substanceType/isStored; name | getSubstance/findNeededComponent/findComponentByUuid | Поиск инвентаря |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | type/substanceType | Данные создания компонента из инвентаря | _onItemAdd |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs) | quantityObtainable и прочие поля | Отображение компонента в инвентаре | Прямое чтение |
| [templates/chat/item/partials/item-description/tags.hbs](../../../../../../../templates/chat/item/partials/item-description/tags.hbs) | quantityObtainable/forage | Предметное описание | Прямое чтение |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Общие поля CommonItemData: description:String='', quantity:String='1', weight:Number=0, cost:Number=0, sourcebook:String='', isHidden=false, isStored=false, isCarried=true. calcWeight и getters canHaveTemporaryItemImprovement=false/canBeRepaired=false наследуются. Собственные строки не имеют choices; пять категорий задаёт HBS, девять типов субстанций — config.substanceTypes. quantityObtainable и forage не являются автоматическими бросками добычи в этой модели. Схема не хранит UUID рецепта. Другая сущность craftingComponent представляет требование рецепта, а не этот Item.

getSubstance исключает isStored; findNeededComponent ищет Item.name либо локализованное имя субстанции и не исключает isStored. findComponentByUuid сравнивает _stats.compendiumSource; realCraft использует поиск по имени. Подготовка рецепта может брать актуальное имя из связанного документа; это не сравнение UUID инвентарного Item.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема | Полное чтение; настоящая ComponentData | 14 верхних полей; реальные BaseItem используют эту system-модель | Не Foundry-клиент |
| Поиск | Настоящий craftingMixin с двумя компонентами | Leather найден по имени даже isStored=true; Current Leather не найден; UUID-метод нашёл compendiumSource; vitriol найден отдельно | Инвентарь/Actor — фасад |
| Форма | Исходный HBS / список core helpers V14 | Missing helper: select; условные поля отдельно изучены с явно временным helper | Не исправление формы |

## Непроверенные участки и открытые вопросы

Foundry 14.367.0, Node 24.16.0. Настоящие модели и код исполнялись изолированно; документы мира, сеть, браузерный submit и БД не запускались. Нормы добычи, допустимые числовые/текстовые записи и правила именования материалов не переопределялись. Существование поля не означает его использование всеми потребителями.

## Связанные проблемы

[issue-00094](../../../../../../issues/potential/issue-00094.md). Неподключённый helper относится к форме, не к defineSchema.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.016 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.026

2026-09-11, `rusbar-main`, `45a63062a2bd55939fef430609fc5dddc350b0e9`. _onItemAdd имеет три формы начальных данных: alchemical, substances+substanceType и обычный component. Реальный HBS списка веществ не передаёт subtype в data-subtype кнопки, и попытка создания из vitriol передала обычный component (issue-00173). Прямой ввод subtype=vitriol даёт правильную форму данных. StringField quantity не превращает строковый inline ввод в число на уровне handler.

Определения: [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) и [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003026). Полный разбор новых соседних файлов вне порции не засчитывается.

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. В реальном компоненте строковые rarity/forage='0' truthy, числовой weight=0 скрывается; quantity='0' остаётся в input. subtype передаётся через substances→components→summary, но не превращается в data-subtype кнопки. findNeededComponent считает по имени, UUID используется другим этапом подготовки.

Связанные шаблоны: [templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-components.hbs). [Проверки и ограничения](../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. _prepareCrafting/_prepareAlchemy и девять списков _prepareSubstances сверены с system.type/substanceType/quantity. Настоящие getSubstance и Array.sum дали 2+3=5; isStored-компонент qty99 исключён поиском Actor. Неизвестный числовой ввод отдельно проверен на raw fixture, не приписан успешной валидации модели.

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../../actor/sheets/WitcherCharacterSheet.js.md). [Методика и ограничения сверки](../../../../review-log.md#task-0003031).
