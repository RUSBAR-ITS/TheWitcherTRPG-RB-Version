# module/data/item/ritualData.js

## Актуальное поведение — issue-00333 / 14.3.1.00035

Дата: 2026-09-17. Ветка dev. [Реализация и границы проверки](../../../../../../issues/open/issue-00333.md#implementation-00035). Ниже описан текущий код; браузерная приёмка ожидает перезапуска пользователем.

**Назначение:** Модель ритуала и два представления компонентов.

**Основные методы, сущности и действия:** prepareDerivedData сохраняет uuid исходной строки на внешнем объекте каждой prepared-записи обоих списков. Поле item может отсутствовать; это не уничтожает идентичность сохраняемой ссылки.

**Зависимости и потребители:** Foundry fromUuidSync остаётся границей получения документа; WitcherRitualSheet и ritual-sheet.hbs используют внешний uuid. Никакой асинхронной загрузки внутрь prepareDerivedData не добавлено.

## Предыдущий срез анализа

Датированные сведения ниже относятся к прежнему коду. При расхождении приоритет имеет актуальный раздел выше.

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

Исходник и указанные связи сопоставлены в TASK-0004.009. Региональные методы и полный cast уже разобраны в .022/.039. Не исследованы живой UUID-кеш, запись массива и игровые нормы расхода/DC. Остаток: [U009-01](../../../../cross-check-0002.md#u009-01), [U009-02](../../../../cross-check-0002.md#u009-02), [U009-03](../../../../cross-check-0002.md#u009-03), [U009-07](../../../../cross-check-0002.md#u009-07). Новых поведенческих запусков нет; прежние протоколы сохраняют даты и фасады.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00076](../../../../../../issues/potential/issue-00076.md), [issue-00128](../../../../../../issues/potential/issue-00128.md), [issue-00129](../../../../../../issues/potential/issue-00129.md), [issue-00130](../../../../../../issues/potential/issue-00130.md), [issue-00131](../../../../../../issues/potential/issue-00131.md), [issue-00132](../../../../../../issues/potential/issue-00132.md), [issue-00135](../../../../../../issues/potential/issue-00135.md), [issue-00136](../../../../../../issues/potential/issue-00136.md), [issue-00137](../../../../../../issues/closed/issue-00137.md). 128 — миграция области; 129 — старые пути формы; 130–132 — список компонентов; 135 — альтернативный список в чате; 136/137 — форма и подписи. Остальные — уже известные зависимости.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |

## Уточнение TASK-0003.022

2026-09-11, `ef8117ba6e5a184989e65761d47a068381056e4a`; исходник не изменён.

Применяется та же региональная примесь и обе EmbeddedDataField, что у SpellData. Вложенная миграция tokenMoveWithin подтверждена на обеих реальных моделях. Ошибка прежних путей основной формы ритуала (issue129) остаётся отдельной от отказов создания/удаления примеси. Компонентные массивы моделью региона не читаются.

Связанные карточки: [module/data/item/templates/regions/templatePropertiesData.js](templates/regions/templatePropertiesData.js.md), [module/data/item/templates/regions/regionBehavioursData.js](templates/regions/regionBehavioursData.js.md), [module/data/item/templates/regions/regionPropertiesData.js](templates/regions/regionPropertiesData.js.md), [module/data/item/mixin/spellRegionMixin.js](mixin/spellRegionMixin.js.md).

[Результаты и пределы сверки](../../../../review-log.md#task-0003022).

## Дополнительная сверка TASK-0003.039

2026-09-11, `c598d74e34f4be51535de78b38f0601c286c5407`; исходники не менялись.

castSpell выбирает ritcraft, показывает difficultyCheck и компоненты, но не назначает RollConfig.threshold (группа 25). Нет onCastEffects, поэтому при цели отсоединённый TypeError (issue-00248). Главные ritualComponents в чате отображаются quantity×name; alternate массив строкифицируется в object Object. В списке Actor имя альтернативы выводится, quantity не выводится.

[module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) — [карточка](../../actor/mixins/castSpellMixin.js.md); [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../../../../../templates/sheets/actor/partials/character/spell-type-list.hbs) — [карточка](../../../templates/sheets/actor/partials/character/spell-type-list.hbs.md); [templates/partials/monster/monster-spell-tab.hbs](../../../../../../../templates/partials/monster/monster-spell-tab.hbs) — [карточка](../../../templates/partials/monster/monster-spell-tab.hbs.md); [templates/dialog/combat/spell-attack.hbs](../../../../../../../templates/dialog/combat/spell-attack.hbs) — [карточка](../../../templates/dialog/combat/spell-attack.hbs.md); [templates/chat/combat/spellItem.hbs](../../../../../../../templates/chat/combat/spellItem.hbs) — [карточка](../../../templates/chat/combat/spellItem.hbs.md).

[Сценарии, методика и пределы проверки](../../../../review-log.md#task-0003039). Соседние определения проверены в пределах связи; это не расширяет состав шести полностью разобранных файлов.

## Сквозная сверка TASK-0004.009

2026-09-14; rusbar-main, 7adc2362937779de0c03957aacf73ff2cf13e211. Исходник совпадает со срезом TASK-0001; изменено только описание.

RitualData сопоставлена с регистрацией, RitualSheet/HBS, cast и регионами. Исходные UUID/quantity отделены от prepared-массивов; fallback сохраняет имя UUID, но не component.item.uuid. Настройки области вложенные, форма использует старые пути. difficultyCheck показывается в чате без порога RollConfig; onCastEffects отсутствует. Расход компонентов не обнаружен в этом пути cast.

Сопоставленные определения и потребители: [module/data/item/commonItemData.js](commonItemData.js.md), [module/data/item/templates/combat/defenseOptionsData.js](templates/combat/defenseOptionsData.js.md), [module/data/item/templates/componentData.js](templates/componentData.js.md), [module/data/item/templates/regions/regionPropertiesData.js](templates/regions/regionPropertiesData.js.md), [module/data/item/templates/regions/templatePropertiesData.js](templates/regions/templatePropertiesData.js.md), [module/data/item/mixin/spellRegionMixin.js](mixin/spellRegionMixin.js.md), [module/setup/config.js](../../setup/config.js.md), [module/setup/registerDataModels.js](../../setup/registerDataModels.js.md), [module/item/witcherItem.js](../../item/witcherItem.js.md), [module/item/sheets/WitcherRitualSheet.js](../../item/sheets/WitcherRitualSheet.js.md), [templates/sheets/item/ritual-sheet.hbs](../../../templates/sheets/item/ritual-sheet.hbs.md), [module/actor/mixins/castSpellMixin.js](../../actor/mixins/castSpellMixin.js.md), [templates/chat/combat/spellItem.hbs](../../../templates/chat/combat/spellItem.hbs.md), [templates/sheets/actor/partials/character/spell-type-list.hbs](../../../templates/sheets/actor/partials/character/spell-type-list.hbs.md).

[Протокол и границы](../../../../review-log.md#task-0004009) — TASK-0004.009; процессы [R009-01](../../../../cross-check-0002.md#r009-01), [R009-02](../../../../cross-check-0002.md#r009-02), [R009-04](../../../../cross-check-0002.md#r009-04), [R009-08](../../../../cross-check-0002.md#r009-08), [R009-13](../../../../cross-check-0002.md#r009-13), [R009-14](../../../../cross-check-0002.md#r009-14), [R009-15](../../../../cross-check-0002.md#r009-15). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
