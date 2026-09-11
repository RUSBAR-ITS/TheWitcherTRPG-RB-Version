# module/data/item/armorData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `0fa589bd300856ff309f362afcb66d6fa43401ab` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.014](../../../../../../tasks/task-0003.014.md), одна порция из девяти файлов |
| Запись перекрёстной сверки | [TASK-0003.014](../../../../review-log.md#task-0003014) |

## Назначение файла

Модель system брони и щитов: исходный и вычисленный SP шести частей тела, сопротивления, ссылки на улучшения, предметные воздействия, ремонт и миграция.

## Условия использования

Default export ArmorData extends CommonItemData; зарегистрирован в CONFIG.Item.dataModels.armor. Shield — строковое значение system.location, а не отдельный тип документа. Подготовка base/derived вызывается документом Item; вложенные SpData и ResistanceData готовятся здесь явно.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| ArmorData; fields | Класс 11–267; локальная константа 9 | Модель Item.system и псевдоним foundry.data.fields | Default export / Item.armor | Схема, подготовка, методы и миграция |
| Поля CommonItemData | Spread 16 | description, quantity, weight, cost, sourcebook, isHidden, isStored, isCarried | Восемь полей | quantity строковый, прочее по базовой модели |
| type | StringField 17–20 | Light, Medium, Heavy, Natural | initial Light, choices ограничены схемой | Тип брони, не тип Item |
| location | Определения 21–26 и 34 | Место ношения / Shield | Реально StringField initial '' без choices | Поздний ключ заменяет ArrayField целиком; проверено на настоящей схеме |
| avail; equipped | StringField/BooleanField 28–29 | Доступность и экипировка | initial '' / false | Читают листы и Actor |
| reliability, reliabilityMax, encumb, enhancements | NumberField 31–33,45 | Надёжность щита, штраф и число ячеек | initial 0, без min/max/integer | Числа допускают значения, непригодные для длины массива |
| resistance | EmbeddedDataField 36 | Три физических сопротивления | ResistanceData | Расчёт OR с улучшениями |
| head, torso, leftArm, rightArm, leftLeg, rightLeg | EmbeddedDataField 38–43 | SP каждой части | Шесть SpData | Исходные и modified значения |
| enhancementItemIds; effects | ArrayField(StringField) 46; TypedObjectField 48 | ID улучшений; словарь itemEffect | Порядок/дубли ID; четыре поля в записи эффекта | Разрешение ID и объединение записей |
| associatedDiagramUuid; defenseProperties | Spread 50; EmbeddedDataField 51 | Рецепт и вложенная защита | Строка UUID; DefenseProperties | Сама ArmorData не делегирует методы выбора защиты |
| enhancementItems; freeEnhancements; associatedDiagram | Prepared свойства 124–154 | Разрешённые Items, пустые ячейки, рецепт | Вне schema | system улучшения сохраняется по ссылке; fill({}) повторяет один объект |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | super и шесть импортов | 27 полей верхнего уровня | Собирает общую/собственную/вложенную схему | Дублирующий location заменён последним определением |
| get effectsWithEnhancements() | effects и enhancementItems | Новый верхний объект записей | Начинает с собственных effects; поздние улучшения перекрывают равные ID | Вложенные записи общие по ссылке; прямой потребитель getter не найден |
| get enhancementsEffects() | enhancementItems | Объект только улучшений | Фильтрует пустые объекты, объединяет system?.effects по ключам | Не проверяет applied/type; используется HBS |
| async applySpDamage(location,spDamage) | location.name соответствует одной модели SP | Promise<void> | Если modifiedStoppingPower−урон≥0, записывает stoppingPower−урон | При превышении modified SP update пропускается; при бонусе базовый SP может стать отрицательным. Update не ожидается |
| get canBeRepaired() | UUID, надёжность, шесть исходных SP/максимумов | Пустая строка либо boolean | Любое повреждение при truthy UUID | Не ограничивается текущим location; не разрешает рецепт |
| async repair() | parent.update | Promise<void> | Записывает reliabilityMax и шесть исходных maxStoppingPower | Семь полей; update без await/return, эффект завершения не передан |
| prepareBaseData() | Вложенные модели созданы | undefined | super; resistance base; base всех шести SpData | SpData копируют исходные значения в modified |
| prepareDerivedData() | parent.actor.items при непустых ID | undefined | super; разрешает непустые ID; freeEnhancements; resistance derived; шесть SP derived; unwrapAssociatedDiagram | Пропускает отсутствующий Item, сохраняет дубли. Нет Actor → TypeError; отрицательная/дробная длина freeEnhancements → RangeError до дальнейшей подготовки |
| static migrateData(source) | Сырой объект | super.migrateData(source) | Добавляет прежние enhancementItems._id; this.effects?.forEach; три migrate*; super | this — класс, не source; выражение source; ничего не меняет. Старые ID не удаляются |
| static migrateEffectsToTypedField(source) | Старый непустой массив effects | undefined | randomID → Object.fromEntries → delete source.effects | Результат конверсии удалён; пустой массив и актуальный объект не входят в ветвь |
| static migrateSpFields(source) | Шесть пар *Stopping/*MaxStopping | undefined | При truthy старом максимуме создаёт вложенный объект, записывает SP/max и удаляет пару старых полей | Ноль пропускается; существующие новые SP перезаписываются старыми |
| static migrateResitances(source) | Три старых boolean, вложенный resistance | undefined | Создаёт resistance при отсутствии; переносит truthy bludgeoning/slashing/piercing с удалением ключа | Имя метода именно Resitances. Старые true перезаписывают новые false; старые false не удаляются |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Import/наследование | Схема и base/derived/super.migrateData | Определения ранее проверены |
| itemEffect() | [module/data/item/templates/itemEffectData.js](../../../../../../../module/data/item/templates/itemEffectData.js) | Import/SchemaField | effects,48 | Четыре поля полностью разобраны |
| associatedDiagramUuid; unwrapAssociatedDiagram | [module/data/item/templates/associatedDiagramData.js](../../../../../../../module/data/item/templates/associatedDiagramData.js) | Import/вызов | 50,154; поле и разрешение рецепта | Обе функции прочитаны; fromUuidSync подменён |
| SpData; ResistanceData | [module/data/item/templates/armor/spData.js](../../../../../../../module/data/item/templates/armor/spData.js); [module/data/item/templates/armor/resistanceData.js](../../../../../../../module/data/item/templates/armor/resistanceData.js) | Import/EmbeddedDataField/методы | Подготовка физических свойств | Настоящие вложенные модели и шесть частей проверены |
| DefenseProperties | [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) | Import/EmbeddedDataField | 51; настройки защиты | Методы вложенной модели есть, делегирования в Armor нет |
| DataModel/TypeDataModel, поля, randomID, Item.update/actor | Foundry 14.367.0, common/abstract/data.mjs, common/abstract/type-data.mjs, common/data/fields.mjs, client/documents/item.mjs | Внешний API | Миграция, подготовка и запись | Настоящие модели; родитель Item и update представлены фасадами |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | ArmorData | Регистрация типа armor | Импорт 18, регистрация 49 |
| [module/item/sheets/WitcherArmorSheet.js](../../../../../../../module/item/sheets/WitcherArmorSheet.js) | system/schema | Контекст листа и конфигурация | Полный разбор |
| [templates/sheets/item/armor-sheet.hbs](../../../../../../../templates/sheets/item/armor-sheet.hbs) | Поля и enhancementsEffects | Редактирование и вывод воздействий | Все пути сопоставлены |
| [templates/sheets/item/configuration/tabs/armorGeneral.hbs](../../../../../../../templates/sheets/item/configuration/tabs/armorGeneral.hbs) | Шесть исходных SP/max | Настройка независимо от location | 12 formGroup |
| [module/actor/mixins/armorMixin.js](../../../../../../../module/actor/mixins/armorMixin.js) | equipped/type/encumb, modified SP, resistance, applySpDamage | Отбор, суммарная защита, сопротивления и повреждение | Связи методов прочитаны; полный бой не исполнялся |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | location Shield; effects | getList('shield'); подготовка воздействий экипированной брони | Не использует effectsWithEnhancements; формат effects не согласован |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | reliability; system.isApplicableDefense | Повреждение щита; отбор дополнительных защит | Метод на ArmorData отсутствует |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | enhancementItemIds | Добавление выбранного улучшения | Callback _chooseEnhancement |
| [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js) | enhancementItemIds | Удаление ID связанного улучшения | removeEnhancement |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs) | enhancementItems/freeEnhancements, SP | Показ установленных улучшений, свободных ячеек и состояния | Строки 90–127, helper armorPartsInfo |
| [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | canBeRepaired, repair, associatedDiagramUuid, enhancementItemIds | Допуск/выполнение ремонта и подсчёт улучшений | Точечная сверка RepairData |

Область поиска: текущие module/ и templates/; регистрации сверены отдельно. Динамические обращения внешних модулей не исследовались.

## Данные и изменения состояния

Подготовка меняет модель в памяти; update выполняют только applySpDamage и repair. В разрешённых улучшениях system — исходная модель Item улучшения. Для исходного SP 4/10 и улучшений +2/+1 получено 7/13; часть с исходным максимумом 0 пропускает бонус и остаётся 4/0. Сопротивления объединяются логическим OR. Равные ID воздействий перекрываются последним улучшением, собственный source.effects не изменяется.

В freeEnhancements учитывается длина исходного списка ID, включая пустые и ненайденные, а не количество успешно разрешённых Items. При пустом списке ID метод не очищает ранее существовавшее enhancementItems; последствия штатного reset отдельно не проверялись. Исходный отрицательный SP при положительном modified SP описан как факт, без самостоятельного вывода о нарушении правил.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема и подготовка | Настоящие ArmorData/EnhancementData | 27 полей; location StringField; два разрешённых ID из четырёх, 0 свободных; SP и сопротивления сверены | Родитель и Actor.items — фасады |
| Границы ячеек/владельца | 0 ячеек/1 ID; −1; 1.5; 2/0; actor=null | Три RangeError, контроль 2 ячейки, отдельный TypeError без Actor | Не загрузка реального Item |
| Повреждение | SP5: урон 2/5/6; SP1+бонус 2: урон 2/4 | Записи 3/0/нет; −1/нет | Без БД и правила округления урона извне |
| Ремонт | Каждая из шести частей и надёжность повреждены поочерёдно | canBeRepaired true; ремонт послал семь полей, Promise завершился до update | Полный RepairSystem не запускался |
| Миграции | Шесть старых SP-пар, конфликты, нулевой максимум, три сопротивления, effects | Пары переносятся; новые значения перезаписываются; armor effects удалены | Исходные миры не сканировались |
| Потребители | Настоящая подготовка Actor с перехватом действий; формы | Объект effects не развёрнут; методы дополнительных защит отсутствуют; prepared resistance отмечено в форме | Подробности и контролируемые подмены в журнале |

## Непроверенные участки и открытые вопросы

Не выполнялись полная атака, реальные ремонты/копирование документов, браузерное снятие улучшения и миграция БД. Регистрация, поля, все собственные методы и три миграционных функции прочитаны целиком. Механика временных ActiveEffect-улучшений остаётся отдельным ранее разобранным маршрутом.

## Связанные проблемы

[issue-00068](../../../../../../issues/potential/issue-00068.md), [issue-00077](../../../../../../issues/potential/issue-00077.md), [issue-00078](../../../../../../issues/potential/issue-00078.md), [issue-00081](../../../../../../issues/potential/issue-00081.md), [issue-00082](../../../../../../issues/potential/issue-00082.md), [issue-00083](../../../../../../issues/potential/issue-00083.md), [issue-00084](../../../../../../issues/potential/issue-00084.md), [issue-00085](../../../../../../issues/potential/issue-00085.md), [issue-00086](../../../../../../issues/potential/issue-00086.md), [issue-00087](../../../../../../issues/potential/issue-00087.md), [issue-00088](../../../../../../issues/potential/issue-00088.md). Миграция воздействий, владелец, повтор ID и завершение записи уточняют существующие наблюдения; остальные относятся к ячейкам, SP, применению воздействий/защиты, переносу старых полей и форме сопротивлений.

Дополнительный разрыв передачи конфигурационных записей в applyStatus — [issue-00089](../../../../../../issues/potential/issue-00089.md).

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.014 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.016

2026-09-10, `53f74994011383cb544cabac96285430f00cb38a`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003016).

Полностью проверены [module/data/item/templates/associatedDiagramData.js](../../../../../../../module/data/item/templates/associatedDiagramData.js), [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js) и [templates/partials/associated-diagram.hbs](../../../../../../../templates/partials/associated-diagram.hbs). Броня использует ту же строковую ссылку и resolver, что оружие; её caller передаёт armor/elderfolk-armor. Ссылка раскрывается после обработки улучшений. Partial обращается к description вне system, поэтому текст связанного рецепта не появляется даже с полным BaseItem (issue-00096); подсказки add/remove перепутаны (issue-00099). Нового поведения расчёта SP эта порция не вводит.

## Уточнение TASK-0003.017

2026-09-10, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; исходники неизменны. [Сверка](../../../../review-log.md#task-0003017).

Уточнён [RepairSystem](../../../../../../../module/item/systems/repair.js) как потребитель system.repair. Прямой вызов настоящей модели через restoreReliability дал payload reliability8 и stoppingPower шести зон: head6,torso7,остальные 0; ожидание update не передаётся наружу. _doRepair при праве update ссылается на отсутствующий собственный getRestoreReliabilityData, а не на ArmorData.repair. Структура текущей модели не создаёт data.damagedLocations автоматически ([issue-00102](../../../../../../issues/potential/issue-00102.md)). Числа — входы диагностического сценария, не изменения правил.

## Уточнение TASK-0003.025

2026-09-11, `rusbar-main`, `a2670a0a10c62b28d836b1a57577c4836f14cf20`. В V2 _prepareArmor только фильтрует armor и unapplied enhancement(type=armor). Свободные слоты приходят из ArmorData.freeEnhancements. V1 дополнительно переписывает enhancementItems по enhancements; его код не зарегистрирован. Обоим листам передаются живые Item, даже когда V1 копирует actor.system. _prepareArmor листов не исправляет разрыв словаря effects в Actor.prepareDerivedData (issue-00084).

Общие определения: [module/actor/sheets/WitcherActorSheet.js](../../../../../../../module/actor/sheets/WitcherActorSheet.js) и [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../module/actor/sheets/WitcherActorSheetV1.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003025). Это точечное уточнение связей; полный разбор новых соседних файлов не засчитывается.

## Уточнение TASK-0003.026

2026-09-11, `rusbar-main`, `45a63062a2bd55939fef430609fc5dddc350b0e9`. Выбор улучшения зависит от dataset.type ближайшей .item, а не названия CSS-класса enhancement-weapon-slot. У современной брони data-type отсутствует: undefined выбирает else для glyph/armor (уточнено в TASK-0003.027). В .026 выбор проверялся с явно заданным armor на DOM-фасаде; это не доказательство наличия атрибута в HBS. Запись enhancementItemIds и applied происходит двумя независимыми вызовами (issue-00171); снятие через меню раньше падает на порядке callback (issue-00168).

Определения: [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) и [module/actor/sheets/interactions/itemContextMenu.js](../../../../../../../module/actor/sheets/interactions/itemContextMenu.js). [Методика и перекрёстная сверка](../../../../review-log.md#task-0003026). Полный разбор новых соседних файлов вне порции не засчитывается.

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Современный armor partial читает вложенный SP через armorPartsInfo и вложенные resistance, а прежний monster partial — отсутствующие плоские поля; issue-00180 ограничена старым шаблоном. Исправлено прежнее утверждение об атрибуте: современная .item брони не содержит data-type; выбор glyph/armor получается через else обработчика. На рендере quantity не зависит от hasQuantity заголовка, ремонтная кнопка у Monster не имеет найденного listener.

Связанные шаблоны: [templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs](../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-armors.hbs); [templates/partials/monster/monster-inventory-tab.hbs](../../../../../../../templates/partials/monster/monster-inventory-tab.hbs). [Проверки и ограничения](../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.
