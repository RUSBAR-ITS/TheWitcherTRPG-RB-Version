# module/data/item/ritualData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

## Назначение файла

Модель system ритуала и подготовка двух списков ссылок на компоненты для интерфейса. Хранит геометрию/поведение области и получает региональные методы примесью.

## Условия использования

registerDataModels регистрирует ritual; WitcherItem.migrateSpells распознаёт прежний class='Rituals'. Foundry вызывает prepareDerivedData, лист и чат читают подготовленные массивы. Импорт присоединяет spellRegionMixin через Object.assign.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| RitualData | default class; 10–89 | Расширение CommonItemData | CONFIG.Item.dataModels.ritual | Схема/подготовка/миграция |
| level; stamina; staminaIsVar | String''; Number0; Booleanfalse; 16–19 | Уровень и стоимость | system.* | Ввод, чтение castSpell |
| effect, range, duration, defence | String''; 21–24 | Описание и параметры применения | system.* | range/defence не выведены в собственном редакторе |
| components, preparationTime, difficultyCheck | String''; 26, 29–30 | Свободное описание состава, время подготовки, DC | system.* | Отдельны от структурированных списков |
| ritualComponentUuids; alternateRitualComponentUuids | ArrayField(SchemaField(component())); 27–28 | Сохранённые uuid/quantity записи | system.* | Нет собственного ID строки; одинаковый UUID допустим |
| templateProperties; regionProperties; defenseOptions() | Два EmbeddedDataField и фабрика; 32–35 | Геометрия, регион и защита цели | system.* | Собственных defenseProperties/attackOptions нет |
| ritualComponents; alternateRitualComponents | Вычисляемые массивы; 50–66 | {item, quantity, img} для отображения | Свойства экземпляра вне schema | На каждом prepareDerivedData очищаются и строятся заново |
| fields; commonData; component callback | Локальные ссылки/параметры; 8, 12, 52–65 | Построение схемы/представления | Не экспортируются | component callback не путать с импортированной фабрикой |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Общая схема/фабрики | Объект полей | Дополняет общую модель | Без записи |
| getUsedSkill() | parent.type | Объект навыка | skillMap → magic[parent.type]?.skill → magic[class].skill | Тип ritual даёт ritcraft; class/spellAttackSkill в схеме отсутствуют |
| prepareDerivedData() | Оба сохранённых массива; fromUuidSync | undefined | super; сброс массивов; разрешает UUID либо создаёт {name: uuid}; копирует quantity и component.img | img не объявлен фабрикой и обычно undefined; fallback не содержит uuid; исключения resolver не перехватываются |
| static migrateData(source) | Исходные данные | super.migrateData(source) | migrateTemplate перед родителем | Меняет source |
| static migrateTemplate(source) | Truthy старое templateSize | undefined | Перезаписывает templateProperties четырьмя прежними значениями и удаляет старые ключи | Не делает parseInt, в отличие от SpellData; числовой 0 не переносится |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Импорт/наследование | defineSchema/prepareDerivedData через TypeDataModel | Схема и inherited capabilities |
| defenseOptions | [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../../module/data/item/templates/combat/defenseOptionsData.js) | Импорт/фабрика | Список ответов цели | Начальные 6 вариантов |
| component | [module/data/item/templates/componentData.js](../../../../../../../module/data/item/templates/componentData.js) | Импорт/фабрика | Оба ArrayField | DocumentUUIDField и NumberField0 |
| RegionProperties; TemplateProperties | [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../../module/data/item/templates/regions/regionPropertiesData.js); [module/data/item/templates/regions/templatePropertiesData.js](../../../../../../../module/data/item/templates/regions/templatePropertiesData.js) | Импорт/вложение | Схема и региональная примесь | Определения прочитаны; полный разбор .022 |
| spellRegionMixin | [module/data/item/mixin/spellRegionMixin.js](../../../../../../../module/data/item/mixin/spellRegionMixin.js) | Импорт/Object.assign | createSpellRegion/fromItem, drawPreview/deleteSpellVisualEffect | Проверен контракт templateProperties |
| CONFIG.WITCHER.skillMap/magic | [module/setup/config.js](../../../../../../../module/setup/config.js) | Глобальный реестр | getUsedSkill | magic.ritual.skill=ritcraft |
| foundry.data.fields; fromUuidSync | Foundry14.367.0, common/data/fields.mjs; client/utils/uuid.mjs | Поля/глобальное разрешение | Валидация UUID и prepareDerivedData | Поля настоящие, resolver заменён картой; недоступный UUID возвращает null |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | RitualData | Регистрация ritual | 25, 63 |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Тип ritual | Преобразование прежнего class Rituals | migrateSpells |
| [module/item/sheets/WitcherRitualSheet.js](../../../../../../../module/item/sheets/WitcherRitualSheet.js) | Два uuid-массива | Drop/edit/remove | Полный разбор |
| [templates/sheets/item/ritual-sheet.hbs](../../../../../../../templates/sheets/item/ritual-sheet.hbs) | system.* и оба подготовленных массива | Редактор | Строки имеют dataset от component.item.uuid |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | getUsedSkill/стоимость/duration/createSpellRegion | Применение магии | Проверены входные обращения, не весь процесс |
| [templates/chat/combat/spellItem.hbs](../../../../../../../templates/chat/combat/spellItem.hbs) | ritualComponents/alternateRitualComponents | Сообщение магии | Основной список перебирается, альтернативный выводится напрямую |
| [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) | components/alternateRitualComponents | Описание ритуала в списке Actor | 103–120; чтение связано с этой моделью |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Сохранённые UUID-массивы и свободный текст components независимы. prepareDerivedData не списывает материалы, не сохраняет Item и не загружает документы асинхронно: он строит представление через fromUuidSync. quantity наследуется из записи; изображение документа доступно через item.img. Оба рассчитанных массива отсутствуют в toObject(), хотя читаются UI. Миграция source сама не пишет в БД.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Оба списка | Группа 06, реальные ArrayField/DocumentUUIDField | Известный UUID возвращает документ; неизвестный — объект с именем; повторная подготовка не дублирует строки; img неизвестен | Действующий pack-кеш не проверен |
| Форма/изменение | Группы 07–09, 12 | Недоступный UUID становится пустым dataset; дубликаты не различаются; старые параметры области отсутствуют в schema | Подменены update и DOM-события |
| Миграция/чат | Группы 04, 17 | Смешанные поля теряют актуальный шаблон; ритуал сохраняет 2.75; чат альтернативы содержит [object Object] | Не исполнялось создание регионов |

## Непроверенные участки и открытые вопросы

Все 91 строка прочитана. Региональные модели/примесь полностью относятся к .022; расход компонентов и полный процесс castSpell здесь не устанавливаются. UUID-кеш и живой клиент не запускались.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00076](../../../../../../issues/potential/issue-00076.md), [issue-00128](../../../../../../issues/potential/issue-00128.md), [issue-00129](../../../../../../issues/potential/issue-00129.md), [issue-00130](../../../../../../issues/potential/issue-00130.md), [issue-00131](../../../../../../issues/potential/issue-00131.md), [issue-00132](../../../../../../issues/potential/issue-00132.md), [issue-00135](../../../../../../issues/potential/issue-00135.md), [issue-00136](../../../../../../issues/potential/issue-00136.md), [issue-00137](../../../../../../issues/potential/issue-00137.md). 128 — миграция области; 129 — старые пути формы; 130–132 — список компонентов; 135 — альтернативный список в чате; 136/137 — форма и подписи. Остальные — уже известные зависимости.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |

## Уточнение TASK-0003.022

2026-09-11, `ef8117ba6e5a184989e65761d47a068381056e4a`; исходник не изменён.

Применяется та же региональная примесь и обе EmbeddedDataField, что у SpellData. Вложенная миграция tokenMoveWithin подтверждена на обеих реальных моделях. Ошибка прежних путей основной формы ритуала (issue129) остаётся отдельной от отказов создания/удаления примеси. Компонентные массивы моделью региона не читаются.

Связанные карточки: [module/data/item/templates/regions/templatePropertiesData.js](templates/regions/templatePropertiesData.js.md), [module/data/item/templates/regions/regionBehavioursData.js](templates/regions/regionBehavioursData.js.md), [module/data/item/templates/regions/regionPropertiesData.js](templates/regions/regionPropertiesData.js.md), [module/data/item/mixin/spellRegionMixin.js](mixin/spellRegionMixin.js.md).

[Результаты и пределы сверки](../../../../review-log.md#task-0003022).
