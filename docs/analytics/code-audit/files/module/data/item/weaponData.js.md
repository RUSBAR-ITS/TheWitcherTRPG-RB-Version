# module/data/item/weaponData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `8cca18e14b75ec53028ee6bc49a837597de4d9af` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.013](../../../../../../tasks/task-0003.013.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.013](../../../../review-log.md#task-0003013) |

## Назначение файла

Типизированные данные предмета weapon: свойства оружия, ссылки на улучшения и рецепт, подготовка данных, собственная защита и восстановление надёжности. Наследует общие поля Item и включает уже описанные вложенные боевые схемы.

## Условия использования

Default export WeaponData extends CommonItemData. Зарегистрирован как CONFIG.Item.dataModels.weapon. Foundry создаёт модель system предмета; prepareDerivedData вызывается при подготовке Item, static migrateData — при очистке входных данных. Документ Item, эта модель и её вложенные DamageProperties/DefenseProperties — разные объекты.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| WeaponData | Класс,12–115 | Модель system оружия | Default export; регистрация weapon | Инициализация, миграция, подготовка и вызовы методов |
| fields | Константа,10 | Псевдоним foundry.data.fields | Локальная | Захватывается при импорте |
| Общие поля CommonItemData | Spread17 | description, quantity, weight, cost, sourcebook, isHidden/isStored/isCarried | Восемь inherited полей | quantity — строка; см. карточку CommonItemData |
| type | SchemaField,18 | Текст и четыре флага weaponType | Вложенная схема | Не Item.type:'weapon' |
| isAmmo, equipped, usingAmmo, rollOnlyDmg | BooleanField,19/24/33/34 | Боеприпас, экипировка, расход боеприпасов, только урон | initial:false | Расчёт и отображение у потребителей |
| conceal, avail, damage, range | StringField,21–22/29–30 | Скрытность, доступность, формула, дистанция | initial:'' | Нет enum или валидации формулы в этих полях |
| hands | StringField,23 | Обозначение хвата | initial:'none' | choices задаются UI, не схемой |
| reliable, maxReliability, accuracy, enhancements | NumberField,26–27/31/36 | Надёжность, максимум, точность, ёмкость улучшений | initial:0 | Нет min/max/integer |
| rateOfFire | NumberField,32 | Скорострельность | initial:1 | Без числовых ограничений |
| enhancementItemIds | ArrayField(StringField),37 | ID улучшений в Actor.items | Элементы initial:'' | Порядок и дубликаты сохраняются |
| attackOptions/defenseOptions; damageProperties/defenseProperties | Spread39/41, EmbeddedDataField40/42 | Общие боевые данные | 11 полей:8+1+1+1 | Определения в TASK-0003.012 |
| associatedDiagramUuid | Spread44 | Ссылка на рецепт | StringField initial:'' | Без DocumentUUIDField-валидации |
| enhancementItems; associatedDiagram | Подготовленные свойства,74–91 | Разрешённые ссылки для потребителей | Не объявлены в schema | Первое создаёт метод; второе unwrapAssociatedDiagram |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| defineSchema() | super.defineSchema и импортированные фабрики | 36 полей верхнего уровня | Собирает собственные/общие/вложенные определения | Синхронно, без записи |
| isApplicableDefense(attack) | Строковый ключ атаки | boolean | Делегирует defenseProperties.isApplicableDefense | Без фильтра equipped/состояния оружия |
| createDefenseOption(attack) | Поля навыков и defenseProperties | {modifier,skills:[skill],itemTypes:[]} | Берёт минимальный вариант; выбирает первый non-nullish melee→ranged→spell→itemUse | Не проверяет существование ключа в skillMap или включённость варианта; пустая строка останавливает fallback |
| get canBeRepaired() | associatedDiagramUuid, reliable, maxReliability | Пустая строка либо boolean | UUID truthy и reliable<maxReliability | Не разрешает рецепт и не проверяет доступ |
| repair() | this.parent.update | Promise<void> | Посылает system.reliable=maxReliability | async без await/return update: завершение не подтверждает запись |
| prepareDerivedData() | parent.actor.items при непустых ID; fromUuidSync для рецепта | undefined | super; пересоздаёт enhancementItems при непустом массиве; пропускает ненайденные ID; добавляет name/img/system/id; unwrapAssociatedDiagram | system улучшения остаётся ссылкой; нет дедупликации/проверки типа/applied. При parent.actor=null возникает TypeError; UUID может не разрешиться |
| isEnoughThrowable() | isThrowable и строковый quantity | boolean | Для throwable возвращает quantity>0, иначе false | Преобразование строки сравнением; ничего не расходует |
| migrateData(source) | Сырой объект | super.migrateData(source) | Если enhancementItems присутствует, дописывает _id непустых объектов в существующий/новый массив; this.effects?.forEach(parseInt); migrateDamageProperties | Не удаляет прежний список и не устраняет повторы. this в static — класс, поэтому this.effects не является source.effects |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Import/наследование/super | База схемы/методов | Определение и настоящая модель |
| migrateDamageProperties | [module/data/migrations/damagePropertiesMigration.js](../../../../../../../module/data/migrations/damagePropertiesMigration.js) | Import/вызов 111 | Перенос прежних свойств урона | Полная карточка TASK-0003.012 |
| weaponType | [module/data/item/templates/weaponTypeData.js](../../../../../../../module/data/item/templates/weaponTypeData.js) | Import/SchemaField18 | Поля system.type | Карточка/реальная схема |
| associatedDiagramUuid; unwrapAssociatedDiagram | [module/data/item/templates/associatedDiagramData.js](../../../../../../../module/data/item/templates/associatedDiagramData.js) | Import/calls44,91 | Поле UUID и fromUuidSync→associatedDiagram | Обе функции прочитаны |
| attackOptions; defenseOptions | [module/data/item/templates/combat/attackOptionsData.js](../../../../../../../module/data/item/templates/combat/attackOptionsData.js); [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../../module/data/item/templates/combat/defenseOptionsData.js) | Import/spread | Настройки вариантов | Определения и 36 ключей модели |
| DamageProperties; DefenseProperties | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js); [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) | Import/EmbeddedDataField | Свойства урона и методы защиты | TASK-0003.012 и текущие caller |
| DataModel lifecycle, fields, Item.actor/update, Actor.items | Foundry 14.367.0; common/data/fields.mjs, common/abstract/data.mjs, client/documents/item.mjs | Внешний API | Типы, parent и prepared данные | Настоящие модели; Actor/Item.update в сценариях — фасады |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | WeaponData | CONFIG.Item.dataModels.weapon | Импорт и регистрация |
| [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../module/item/sheets/WitcherWeaponSheet.js); [module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js](../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js); [templates/sheets/item/weapon-sheet.hbs](../../../../../../../templates/sheets/item/weapon-sheet.hbs) | system-поля и schema | Лист оружия, конфигурация, форма | Контекст/36 ключей/пути сверены |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js); [module/item/mixins/defenseOptionMixin.js](../../../../../../../module/item/mixins/defenseOptionMixin.js) | attackOptions, навыки, createDefenseOption | Общие операции Item | Текущие определения |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | damage/range/accuracy/usingAmmo/isEnoughThrowable/enhancementItems | Атака и присоединение effects; quantity списывает внешний метод | 14–55,155–176 |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | isApplicableDefense и reliable | Отбор дополнительных защит; повреждение надёжности при блокировании | 19–20,424–428 |
| [module/item/systems/repair.js](../../../../../../../module/item/systems/repair.js) | associatedDiagramUuid, repair, enhancementItemIds | Рецепт ремонта, восстановление, расчёт enchantsCount/DC | 20,202,290,306–329 |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | enhancementItemIds | Добавление выбранного улучшения | 217–219 |

## Данные и изменения состояния

prepareDerivedData только меняет подготовленную модель. Если enhancementItemIds пуст, существующее enhancementItems сам метод не очищает; то же относится к associatedDiagram при опустошении UUID. Поведение этих свойств при штатном reset и повторной подготовке Item не проверялось; ручной повтор вызова не доказывает остаточные данные в клиенте.

repair посылает update родительскому документу, но сама модель остаётся reliable:2 до выполнения/подготовки записи. Счётчик ёмкости enhancements не ограничивает здесь число ID. Повторы ID дают повторные prepared записи и учитываются repair.enchantsCount; одинаковые ID эффектов при поверхностном объединении могут перекрываться, поэтому двойной урон не утверждается.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема | Настоящий WeaponData и все фабрики | 36 полей верхнего уровня; перечислены определения/defaults | Без сохранения Item |
| Улучшения | ID[e,missing,e], Actor.items содержит e | Две prepared записи e с общей system-ссылкой; missing пропущен | Коллекция Actor представлена Map |
| Нет владельца | parent.actor=null, ID[e] | TypeError чтения items | Не запускалось окно компедиума |
| Миграция | ID[e] + старый enhancementItems[{_id:e}] | Один вызов→[e,e], второй raw вызов→[e,e,e]; модель дала[e,e] | Реальные старые документы не сканировались |
| Защита | Пустой melee и ranged archery; контроль без melee | Первый результат skills:['']; контроль skills:['archery'] | Не диалог защиты |
| Ремонт/количество | pending update; пять комбинаций quantity/throwable | repair Promise завершился до update;1/true→true,0/-1/abc/false→false | БД и расход ресурсов не запускались |

## Непроверенные участки и открытые вопросы

Полный бой и ремонт относятся к отдельным порциям. Не проверялись все комбинации экипировки/улучшений, запись/копирование Item мира и цепочка сетевого ремонта. Поиск зависимостей выполнен в текущих module/ и templates/; динамические сторонние изменения не учитывались.

## Связанные проблемы

[issue-00064](../../../../../../issues/potential/issue-00064.md), [issue-00065](../../../../../../issues/potential/issue-00065.md), [issue-00067](../../../../../../issues/potential/issue-00067.md), [issue-00077](../../../../../../issues/potential/issue-00077.md), [issue-00078](../../../../../../issues/potential/issue-00078.md), [issue-00079](../../../../../../issues/potential/issue-00079.md), [issue-00081](../../../../../../issues/potential/issue-00081.md) — defaults/прежние поля, отсутствие Actor, повторные ID, выбор навыка защиты и завершение repair.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.013 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.014

2026-09-10, `0fa589bd300856ff309f362afcb66d6fa43401ab`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003014).

Полный разбор [module/data/item/armorData.js](../../../../../../../module/data/item/armorData.js) подтвердил общие с оружием отсутствие проверки владельца при непустых enhancementItemIds, добавление прежних ID без устранения повторов и раннее завершение repair. Дополнены issue-00077/00078/00081. Отличие брони: фильтр пустых ID и расчёт freeEnhancements, который может выбросить RangeError; оружие такого массива не создаёт. Миграция effects брони удаляет результат, а [module/data/item/enhancementData.js](../../../../../../../module/data/item/enhancementData.js) сохраняет конверсию. Это сравнение текущих типов, не перенос поведения брони на оружие.

## Уточнение TASK-0003.016

2026-09-10, `53f74994011383cb544cabac96285430f00cb38a`; исходник неизменен. [Перекрёстная сверка](../../../../review-log.md#task-0003016).

Полностью разобраны импортируемые [module/data/item/templates/associatedDiagramData.js](../../../../../../../module/data/item/templates/associatedDiagramData.js) и [module/item/sheets/mixins/associatedDiagramMixin.js](../../../../../../../module/item/sheets/mixins/associatedDiagramMixin.js). associatedDiagramUuid — строка; unwrapAssociatedDiagram синхронно задаёт prepared объект/индекс/null и не проверяет тип. Допустимые категории weapon/elderfolk-weapon проверяет drop-примесь листа. Ремонт/разборка заново разрешают UUID асинхронно. Обратный associatedItemUuid рецепта автоматически не устанавливается; его отдельный редактор описан в [module/item/sheets/WitcherDiagramSheet.js](../../../../../../../module/item/sheets/WitcherDiagramSheet.js).

## Уточнение TASK-0003.017

2026-09-10, `c7cd9d71dcb1714cdccb175aee351a3f1df95c5b`; исходники неизменны. [Сверка](../../../../review-log.md#task-0003017).

Полностью разобран [ремонт](../../../../../../../module/item/systems/repair.js). RepairData.enchantsCount считает все truthy enhancementItemIds, включая повтор одного ID: [a,'',a] дал 2 и добавил 4 к DC. Рецепт DC20 дал итог 19. Прямые gmRepair/restoreReliability вызывают WeaponData.repair→parent.update({'system.reliable':10}); update в опыте оставался pending. Обычный путь не использует этот метод в ветке update: там отсутствуют damagedLocations/getRestoreReliabilityData ([issue-00102](../../../../../../issues/potential/issue-00102.md)). Прежняя [issue-00081](../../../../../../issues/potential/issue-00081.md) дополнена всеми уровнями ожидания.
