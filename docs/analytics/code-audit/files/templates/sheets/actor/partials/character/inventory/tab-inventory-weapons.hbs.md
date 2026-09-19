# templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs

## Актуализация 2026-09-19 — 14.3.1.00115

Ввод system.quantity сделан числовым: type=number,min=0,step=1,required; значение берётся из CommonItemData.quantity. Обработчик sheet.itemMixin._onItemInlineEdit проверяет целое неотрицательное значение до Item.update, отклоняя пустой/дробный ввод. Расположение остальных колонок и действия предметов сохранены.

[Результаты107 статических проверок и границы](../../../../../../../../task-0011-static-checks.md#quantity-installed-00115). Ниже сохранён исходный пофайловый аудит на его дату; при расхождении текущий контракт описан выше.

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-16: актуализация технических обращений по issue-00001 |
| Ветка и коммит | `dev`, база `d8e0e1ad1159cb71a8769b0353f812de6f1ed4d8` + незакоммиченное исправление issue-00001 |
| Изменения относительно коммита | issue-00001; текущие технические обращения актуализированы. Прежние опыты ниже относятся к своим датам. |
| Задача и порция | [TASK-0003.027](../../../../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../../../../review-log.md#task-0003027) |

Актуализация [issue-00001](../../../../../../../../../issues/closed/issue-00001.md), 2026-09-16: Обращения к ресурсам и/или техническим namespaces переведены на TheWitcherTRPG-RB-Version. Формулы и порядок действий сохранены. Датированные проверки ниже выполнены до смены ID.

## Назначение файла

Таблица оружия и свободных улучшений типа weapon: бросок/использование, урон, надёжность, количество, экипировка/ремонт, признаки и ячейки улучшений.

## Условия использования

Character и Monster получают weapons от _prepareWeapons общего V2. Строка .item.list-item.draggable имеет data-type=weapon даже если элемент — EnhancementData.type=weapon; ветка unless проверяет текущий Item.type, а не data-type DOM.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| summary/rows:1–42 | Блок HBS | Параметры и действия | Рендер через потребителей | hasDamage/hasReliability явно, hasQuantity наследуется; damage, reliable/maxReliability, quantity, roll/chat/equip/repair |
| tags/description:43–83 | Блок HBS | Сведения оружия | Рендер через потребителей | type.text, range; accuracy>0 с плюсом; isAmmo либо hands lookup; conceal, weight, экранированное description |
| enhancements:84–126 | Блок HBS | Ячейки | Рендер через потребителей | unless Item.type enhancement; each enhancementItems: img→вложенный Item/effects, иначе свободная ячейка |

## Основные функции и методы

Собственных JS-функций, экспортов и схем нет. В файле используются each, eq, gt, if, localize, lookup, unless и включения partial. Ветви и поля описаны по блокам выше.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .inline-edit | [itemMixin._onItemInlineEdit](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → data-field/value → Item.update; Number/String очищаются моделью |
| .item-weapon-display | [itemMixin._onItemDisplayInfo](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | Тот же обработчик описания оружия |
| .item-chat | [itemMixin._onItemMessage](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .list-item → item-description → ChatMessage |
| .item-roll | [itemMixin._onItemRoll](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → Actor.useItem с alt/ctrl/shift |
| .item-equip | [itemMixin._onItemEquip](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → toggle system.equipped |
| .enhancement-label | [itemMixin._onEnhancementInfo](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .weapon-enhancement → .enhancement-info |
| .enhancement-weapon-slot | [itemMixin._chooseEnhancement](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → dataset.type; weapon → weapon/rune, иначе armor/glyph |
| .item-repair | [WitcherCharacterSheet._repairItem](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | closest .item → Item.repair; подключено только Character |

Поля name/data-field, буквально присутствующие в файле: `system.quantity`, `system.reliable`.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WeaponData/weaponTypeData | [module/data/item/weaponData.js](../../../../../../../../../../module/data/item/weaponData.js); [module/data/item/templates/weaponTypeData.js](../../../../../../../../../../module/data/item/templates/weaponTypeData.js) | Поля/getters | type.text, reliable/maxReliability, damage, accuracy, equipped, canBeRepaired | type — SchemaField, text существует; отрицательная accuracy не попадает в ветку gt0 по явному условию |
| EnhancementData/itemEffect | [module/data/item/enhancementData.js](../../../../../../../../../../module/data/item/enhancementData.js); [module/data/item/templates/itemEffectData.js](../../../../../../../../../../module/data/item/templates/itemEffectData.js) | Вложенные Item | effects/statusEffect/percentage/name | Для свободного weapon-enhancement часть полей WeaponData отсутствует; HBS не конвертирует схему |
| Подготовка ячеек | [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | Producer | _prepareWeapons дополняет enhancementItems пустыми объектами | Проблема обрезки прежней подготовки — issue-00166; здесь только разметка |
| item-repair | [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | Listener | _repairItem→Item.repair | У Monster такой listener не найден |
| useItem | [module/actor/witcherActor.js](../../../../../../../../../../module/actor/witcherActor.js) | Действие Item | item-roll→itemMixin._onItemRoll→actor.useItem | Weapon вызывает weaponAttack; Enhancement сам не становится Weapon от data-type DOM |
| eq, gt | [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | Системные helpers | Точные вызовы в этом HBS | registerHandelbarHelpers исполнен из исходника; расчёты отделены от UI-записи |
| each, if, localize, lookup, unless | Handlebars 4.7.9 / Foundry VTT 14.367.0 | Внешний шаблонный API | Вызовы в этом HBS; core localize/concat: /opt/foundryvtt/client/applications/handlebars.mjs | Рендер настоящий; game.i18n/окружение представлены фасадом, core helper localize/concat дополнительно исполнены |
| Словари и подписи | [module/setup/config.js](../../../../../../../../../../module/setup/config.js); [lang/en.json](../../../../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../../../../lang/ru.json) | Контекст и локализация | lookup CONFIG.WITCHER и точные строковые ключи в HBS | 114 статических ключей порции сверены с en/ru; отсутствующие и динамические ключи отражены в issue-00178 |
| Общие поля Item и доступ Document | [module/data/item/commonItemData.js](../../../../../../../../../../module/data/item/commonItemData.js) | Чтение данных | name/id/_id/img у Foundry Document; system.description/quantity/weight/cost/isCarried/isStored/isHidden у модели | quantity StringField; weight/cost NumberField; чтение не означает сохранение |
| Обработчики DOM | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../../../../module/actor/sheets/mixins/itemMixin.js); [module/actor/sheets/WitcherCharacterSheet.js](../../../../../../../../../../module/actor/sheets/WitcherCharacterSheet.js) | DOM→JS | Сопоставление ниже в таблице действий | Селекторы и ближайшие контейнеры проверены по реальному шаблону и определениям |
| Контекстное меню Item | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Внешний listener | Ближайшая .item и data-item-id → меню шести действий | Отдельных menu entries HBS не создаёт; неисправные callbacks issue-00168 не переисполнялись |
| partial inventory-items-summary.hbs | [templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs](../../../../../../../../../../templates/sheets/actor/partials/character/inventory/inventory-items-summary.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| Классы списка, details, progress, изображения | [styles/tab-inventory.css](../../../../../../../../../../styles/tab-inventory.css) | CSS/HTML | grid заголовков/строк, stored-item и carry-bar до привязки селекторов | Полный CSS и вид браузера не проверялись; img без src не получает fallback в HBS, assets вне границ анализа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и кеширование пути; не доказательство активного листа | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/tabs/tab-inventory.hbs) | partial tab-inventory-weapons.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs](../../../../../../../../../../templates/sheets/actor/partials/monster/tabs/tab-inventory.hbs) | partial tab-inventory-weapons.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Надёжность редактируется числовой моделью, quantity — строковой. Основные ячейки урона/надёжности/количества безусловны: has* влияют на summary, не на строки. Подтип оружия берётся из type.text. Изображение без img не получает fallback в шаблоне; для улучшения отсутствие img используется как признак пустой ячейки. Отрицательная/нулевая accuracy не выводится.

Буквальные пути чтения в этом файле: `enhancement.id`, `enhancement.img`, `enhancement.name`, `enhancement.system.effects`, `system.quantity`, `system.reliable`, `weapon.hands`, `weapon.id`, `weapon.img`, `weapon.name`, `weapon.system.accuracy`, `weapon.system.canBeRepaired`, `weapon.system.conceal`, `weapon.system.damage`, `weapon.system.description`, `weapon.system.enhancementItems`, `weapon.system.enhancementItems.length`, `weapon.system.equipped`, `weapon.system.hands`, `weapon.system.isAmmo`, `weapon.system.maxReliability`, `weapon.system.quantity`, `weapon.system.range`, `weapon.system.reliable`, `weapon.system.type.text`, `weapon.system.weight`.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 131 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 01–04,12,17,19; реальный Handlebars/модели и обработчики | Проверены accuracy -2/0/+2, isAmmo, equipped, canBeRepaired, строки количества и inherited hasQuantity. Для реального WeaponData type.text отображается. Вложенный эффект и пустая ячейка отрендерены; Item.type=enhancement исключил секцию улучшений. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Исходник и текущие связи сопоставлены в TASK-0004.006. Прежние ссылки на будущий пофайловый разбор TASK-0003 больше не являются очередью: он завершён. Остались конкретные границы сквозной проверки: [U006-01](../../../../../../../cross-check-0002.md#u006-01); [U006-03](../../../../../../../cross-check-0002.md#u006-03). Ремонтная кнопка не подтверждает listener Monster.

## Связанные проблемы

[issue-00063](../../../../../../../../../issues/potential/issue-00063.md), [issue-00166](../../../../../../../../../issues/potential/issue-00166.md), [issue-00168](../../../../../../../../../issues/potential/issue-00168.md), [issue-00171](../../../../../../../../../issues/potential/issue-00171.md), [issue-00172](../../../../../../../../../issues/closed/issue-00172.md), [issue-00175](../../../../../../../../../issues/potential/issue-00175.md), [issue-00177](../../../../../../../../../issues/potential/issue-00177.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../../../../review-log.md#task-0003027) |

## Уточнение TASK-0003.034

2026-09-11, `7dbb31bdbd094f58c77c9e58dd5a684df6bb942c`. quantity остаётся текстовым inline-полем, без min. Новая issue-00217 касается прямого dismantle при сохранённом quantity='0'/'-1': материалы выдаются до удаления источника. Само редактирование и хранение quantity не исправлялись; блокирующая ошибка menu callback issue-00168 сохранена.

Связи: [module/item/mixins/dismantlingMixin.js](../../../../../../module/item/mixins/dismantlingMixin.js.md). [Результаты и пределы проверки](../../../../../../../review-log.md#task-0003034).

## Дополнительная сверка TASK-0003.048

2026-09-12, rusbar-main, ee24c2605f4db98fad1ff6db024d2b0c26883670; исходники не изменены.

У [templates/chat/item/partials/item-description/tags.hbs](../../../../../../../../../../templates/chat/item/partials/item-description/tags.hbs) такое же условие accuracy>0, как в этой строке инвентаря. Группа 07 дала 0/0/1 тег при -2/0/+2; weaponAttack:190–198 включает отрицательную точность в формулу. Зарегистрирована [docs/issues/potential/issue-00307.md](../../../../../../../../../issues/potential/issue-00307.md). Прежнее слово «намеренно» не доказывало решения автора; заменено нейтральным описанием условия. Общая .item-tag использует ошибочное background-color в tab-inventory.css — [docs/issues/potential/issue-00310.md](../../../../../../../../../issues/potential/issue-00310.md); полный CSS остаётся в .049.

[Сценарии, результаты и ограничения](../../../../../../../review-log.md#task-0003048). Связанные файлы повторно не засчитываются в покрытие.

## Сквозная сверка TASK-0004.006

2026-09-14; rusbar-main, a176c4f18879f2e5a63b93bc15345fc26d9f535a. Исходник совпадает со срезом TASK-0001; изменено только описание.

Оружейная строка имеет data-type=weapon, вводит reliable/quantity и вызывает roll/equip/chat; enhancement Item исключает собственный блок слотов через настоящий type. Список enhancementItems заранее дополнен листом пустыми объектами. Положительная accuracy видна, неположительная скрыта условием. Ремонтная кнопка не подтверждает listener Monster.

Сопоставленные определения и потребители: [module/data/item/templates/weaponTypeData.js](../../../../../../module/data/item/templates/weaponTypeData.js.md), [module/data/item/weaponData.js](../../../../../../module/data/item/weaponData.js.md), [module/item/sheets/WitcherWeaponSheet.js](../../../../../../module/item/sheets/WitcherWeaponSheet.js.md), [templates/sheets/item/weapon-sheet.hbs](../../../../item/weapon-sheet.hbs.md).

[Протокол и границы](../../../../../../../review-log.md#task-0004006) — TASK-0004.006; процессы [R006-08](../../../../../../../cross-check-0002.md#r006-08), [R006-11](../../../../../../../cross-check-0002.md#r006-11), [R006-17](../../../../../../../cross-check-0002.md#r006-17). В этой порции выполнена статическая сверка; поведенческие опыты принадлежат датированным прежним протоколам, а не новому прогону.
