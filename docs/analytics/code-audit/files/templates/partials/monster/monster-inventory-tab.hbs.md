# templates/partials/monster/monster-inventory-tab.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../../templates/partials/monster/monster-inventory-tab.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.027](../../../../../../tasks/task-0003.027.md), 12 файлов, 1375 логических строк |
| Запись перекрёстной сверки | [TASK-0003.027](../../../../review-log.md#task-0003027) |

## Назначение файла

Прежний табличный инвентарь монстра: оружие с inline-уроном/надёжностью/ROF, броня со старыми SP-полями и добыча. Сохранившийся partial, не используемый текущим зарегистрированным V2.

## Условия использования

preloadHandlebarsTemplates загружает его и старый monster-sheet.hbs, который включает этот файл. У WitcherMonsterSheet.PARTS.inventory другой путь; регистрация старого полноэкранного шаблона/класса не найдена. Загрузка partial не делает его действующим UI.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| weapon:1–57 | Блок HBS | Старая таблица | Рендер через потребителей | _id, data-id/draggable, damage/reliable/rateOfFire inline; item-weapon-display/edit/delete; damageProperties.effects.name/percentage, NoEffects |
| armor:58–205 | Блок HBS | Старые поля защиты | Рендер через потребителей | _id/data-type=armor, item-image partial, name/quantity/equipped; location Head/Torso/Leg/FullCover/Shield; flat headStopping...rightLegMaxStopping; shield reliability/reliabilityMax; disabled system.bludgeoning/slashing/Piercing |
| enhancements/info:207–293 | Блок HBS | Вложенная таблица | Рендер через потребителей | enhancementItems по img; edit и пустые enhancement-armor-slot; eq текущего Item.type armor/enhancement: encumb/weight/effects/effect/delete |
| loot:296–313 | Блок HBS | Старая добыча | Рендер через потребителей | add valuable, export-loot без data-action; quantity по system.quantity текущего each Item, name inline, delete |

## Основные функции и методы

Собственных JS-функций, экспортов и схем нет. В файле используются checked, each, eq, if, localize, unless и включения partial. Ветви и поля описаны по блокам выше.

| Селектор / вход | Обработчик и источник | Действие и поле |
| --- | --- | --- |
| .add-item | [itemMixin._onItemAdd](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | dataset.itemtype/spelltype/subtype → Item.create({parent:actor}) |
| .inline-edit | [itemMixin._onItemInlineEdit](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → data-field/value → Item.update; Number/String очищаются моделью |
| .item-display-info | [itemMixin._onItemDisplayInfo](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → .item-info.toggleClass(invisible) |
| .item-weapon-display | [itemMixin._onItemDisplayInfo](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | Тот же обработчик описания оружия |
| .item-roll | [itemMixin._onItemRoll](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → Actor.useItem с alt/ctrl/shift |
| .enhancement-armor-slot | [itemMixin._chooseEnhancement](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | Старый armor слот → тот же выбор; действия записи вне HBS |
| .item-edit | [itemMixin._onItemEdit](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → Item.sheet.render(true) |
| .item-delete | [itemMixin._onItemDelete](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | closest .item → Item.delete |
| .export-loot | [WitcherMonsterSheet.#exportLoot](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | Современный data-action=exportLoot; у прежней ссылки есть только class без action |

Поля name/data-field, буквально присутствующие в файле: `name`, `system.Piercing`, `system.bludgeoning`, `system.damage`, `system.equipped`, `system.headStopping`, `system.leftArmStopping`, `system.leftLegStopping`, `system.quantity`, `system.rateOfFire`, `system.reliability`, `system.reliable`, `system.rightArmStopping`, `system.rightLegStopping`, `system.slashing`, `system.torsoStopping`.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| WeaponData/ArmorData/EnhancementData | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js); [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js); [module/data/item/enhancementData.js](../../../../../../../module/data/item/enhancementData.js) | Схемы Item | Старые поля сравниваются с текущими вложенными SP/resistance | headStopping и плоские сопротивления отсутствуют; у Shield reliability/reliabilityMax существуют |
| item-image | [templates/partials/item-image.hbs](../../../../../../../templates/partials/item-image.hbs) | Partial | Только броня использует getSetting/includes/clickableImage | Флаг отсутствует в текущей модели; issue-00063 |
| WitcherMonsterSheet/registerSheets | [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js); [module/setup/registerSheets.js](../../../../../../../module/setup/registerSheets.js) | Проверка достижимости | Действующий V2 ведёт к другому inventory | Для export-loot здесь нет data-action; отдельного старого listener в module не найдено |
| eq | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные helpers | Точные вызовы в этом HBS | registerHandelbarHelpers исполнен из исходника; расчёты отделены от UI-записи |
| checked, each, if, localize, unless | Handlebars 4.7.9 / Foundry VTT 14.367.0 | Внешний шаблонный API | Вызовы в этом HBS; core localize/concat: /opt/foundryvtt/client/applications/handlebars.mjs | Рендер настоящий; game.i18n/окружение представлены фасадом, core helper localize/concat дополнительно исполнены |
| Словари и подписи | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | Контекст и локализация | Точные строковые ключи localize в HBS | 114 статических ключей порции сверены с en/ru; отсутствующие и динамические ключи отражены в issue-00178 |
| Общие поля Item и доступ Document | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Чтение данных | name/id/_id/img у Foundry Document; system.description/quantity/weight/cost/isCarried/isStored/isHidden у модели | quantity StringField; weight/cost NumberField; чтение не означает сохранение |
| Обработчики DOM | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js); [module/actor/sheets/WitcherMonsterSheet.js](../../../../../../../module/actor/sheets/WitcherMonsterSheet.js) | DOM→JS | Сопоставление ниже в таблице действий | Селекторы и ближайшие контейнеры проверены по реальному шаблону и определениям |
| Контекстное меню Item | [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | Внешний listener | Ближайшая .item и data-item-id → меню шести действий | Отдельных menu entries HBS не создаёт; неисправные callbacks issue-00168 не переисполнялись |
| partial item-image.hbs | [templates/partials/item-image.hbs](../../../../../../../templates/partials/item-image.hbs) | Литеральное включение | Шаблонный контекст и hash-аргументы из исследуемого файла | Путь существует, регистрация/вызов и встречное включение сверены |
| Классы списка, details, progress, изображения | [styles/tab-inventory.css](../../../../../../../styles/tab-inventory.css) | CSS/HTML | grid заголовков/строк, stored-item и carry-bar до привязки селекторов | Полный CSS и вид браузера не проверялись; img без src не получает fallback в HBS, assets вне границ анализа |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | preloadHandlebarsTemplates | Загрузка и кеширование пути; не доказательство активного листа | Поиск module/templates; конкретный путь найден в исходном потребителе |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../../templates/sheets/actor/monster-sheet.hbs) | partial monster-inventory-tab.hbs | Включение с унаследованным контекстом и hash из исходника | Поиск module/templates; конкретный путь найден в исходном потребителе |

Область поиска: module/ и templates/ текущего checkout. Типы проверены по system.json, регистрация листов — по module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Собственных записей нет; прежние input.data-field направляли бы обновления в устаревшие пути. Disabled checkbox сопротивлений не являются активным вводом. Обычное each делает system.quantity в строке добычи корректной ссылкой на Item.system, несмотря на отсутствие alias valuable. Старое dragable написание и table/tbody не заменяют текущий V2 DOM.

Буквальные пути чтения в этом файле: `armor._id`, `armor.name`, `armor.system.bludgeoning`, `armor.system.effect`, `armor.system.effects`, `armor.system.encumb`, `armor.system.enhancementItems`, `armor.system.enhancements`, `armor.system.equipped`, `armor.system.headMaxStopping`, `armor.system.headStopping`, `armor.system.leftArmMaxStopping`, `armor.system.leftArmStopping`, `armor.system.leftLegMaxStopping`, `armor.system.leftLegStopping`, `armor.system.location`, `armor.system.piercing`, `armor.system.quantity`, `armor.system.reliability`, `armor.system.reliabilityMax`, `armor.system.rightArmMaxStopping`, `armor.system.rightArmStopping`, `armor.system.rightLegMaxStopping`, `armor.system.rightLegStopping`, `armor.system.slashing`, `armor.system.torsoMaxStopping`, `armor.system.torsoStopping`, `armor.system.weight`, `enhancement.id`, `enhancement.img`, `system.Piercing`, `system.bludgeoning`, `system.damage`, `system.equipped`, `system.headStopping`, `system.leftArmStopping`, `system.leftLegStopping`, `system.quantity`, `system.rateOfFire`, `system.reliability`, `system.reliable`, `system.rightArmStopping`, `system.rightLegStopping`, `system.slashing`, `system.torsoStopping`, `valuable._id`, `valuable.img`, `valuable.name`, `weapon._id`, `weapon.img`, `weapon.name`, `weapon.system.damage`, `weapon.system.damageProperties.effects`, `weapon.system.rateOfFire`, `weapon.system.reliable`.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Полное чтение/структура | 313 логических строк; все блоки и вложенные each/if прочитаны | Назначение, входные поля, partial и actions сопоставлены | HBS не является реализацией методов Item/Actor |
| Изолированные проверки | Группы 13,19; реальный Handlebars/модели и обработчики | Отрендерены пустой список, Weapon/Armor/Loot и пять location. Current ArmorData.head.stoppingPower=5/max10 не заполняет старый headStopping; resistance.slashing=true не отмечает старый disabled checkbox. Quantity добычи '1d6' сохранилось. Эти выводы относятся к отдельно отрендеренному старому partial. | Actor/DOM/запись/диалоги представлены фасадами; без мира и браузера |
| Встречные связи | Определения producer/helper/handler и найденные потребители | Пути и имена сверены, частичный разбор соседей не добавляет охват | Мировые макросы, внешние модули и компедиумы не проверялись |

## Непроверенные участки и открытые вопросы

Весь файл прочитан. Проверены данные рендера и существенные границы, перечисленные выше. Не запускались браузер, серверная запись, DragDrop, реальные броски/производство/ремонт/экспорт или полноценные листы Actor. CSS проверен только до селекторов. Реальный Foundry Document и UI представлены ограниченными фасадами; фактическая регистрация проверена статически. Полные файлы Character/Monster/MountData, валюта/награды и производство остаются за дальнейшими порциями.

## Связанные проблемы

[issue-00063](../../../../../../issues/potential/issue-00063.md), [issue-00084](../../../../../../issues/potential/issue-00084.md), [issue-00089](../../../../../../issues/potential/issue-00089.md), [issue-00153](../../../../../../issues/potential/issue-00153.md), [issue-00180](../../../../../../issues/potential/issue-00180.md). Наблюдения остаются potential. Прежние issues сопоставлены по конкретному маршруту; отсутствие новой карточки не означает проверки исправности всей подсистемы.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `ce0c7eb7069b215b641d725913b3aae21502e811`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003027) |

## Уточнение TASK-0003.032

2026-09-11, `8b938d44a042749df027d8b58e28bb1d79638091`. Полностью описан старый внешний monster-sheet.hbs: 296 и отсутствие его регистрации. Прежняя issue-00180 об устаревших полях брони сохраняется в пределах старого маршрута; новый MonsterSheet использует другой tab-inventory.

Связи: [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js.md); [templates/sheets/actor/monster-sheet.hbs](../../sheets/actor/monster-sheet.hbs.md). [Результаты и пределы проверки](../../../../review-log.md#task-0003032).
