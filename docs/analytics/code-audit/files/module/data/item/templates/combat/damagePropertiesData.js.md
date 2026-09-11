# module/data/item/templates/combat/damagePropertiesData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.012](../../../../../../../../tasks/task-0003.012.md), одна порция из десяти файлов |
| Запись перекрёстной сверки | [TASK-0003.012](../../../../../../review-log.md#task-0003012) |

## Назначение файла

Общая модель свойств урона и предметных воздействий. Используется оружием, заклинаниями, атаками профессий и боевыми сообщениями. Хранит настройки, объединяет/подготавливает effects и мигрирует их прежний массив; большинство боевых правил исполняются внешними обработчиками.

## Условия использования

Default export DamageProperties extends foundry.abstract.DataModel, импортирует фабрику itemEffect. Обычно создаётся через EmbeddedDataField. У Weapon/Spell parent — модель system предмета, у вложенной атаки профессии — ProfessionData, а у сообщения — его модель. Это существенно для enhancementsEffects, который ожидает parent.enhancementItems.

DamageMessageData использует только defineSchema(), затем заменяет effects своей ArrayField: в итоговом сообщении properties — plain SchemaField, не экземпляр DamageProperties. Нельзя приписывать ему методы класса лишь из-за совпадения полей.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, строка 3 | Псевдоним foundry.data.fields | Не экспортируется | Инициализируется при импорте |
| DamageProperties | Класс, 5–116 | Вложенные свойства урона | Default export | Инициализация/миграция Foundry; подготовленные значения |
| armorPiercing, improvedArmorPiercing | BooleanField, 8–12 | Бронебойные свойства | initial:false; label задан | Читаются armorMixin/damageMixin |
| ablating, crushingForce | BooleanField, 13–14 | Настройки повреждения брони/защиты | initial:false; label задан | Читаются armorMixin/defenseMixin |
| damageIsAblation | BooleanField, 15–18 | Зарезервированная настройка | initial:false; label задан | en/ru прямо отмечают not functional/не функционирует |
| stun | NumberField, 19 | Числовой модификатор оглушения | Без явного initial/min/max; label задан | В проверенной модели undefined, пока не задан |
| damageToAllLocations | BooleanField, 21–24 | Разделение применения урона по локациям | initial:false; label задан | damageMixin.applyDamage |
| bypassesWornArmor, bypassesNaturalArmor | BooleanField, 26–33 | Обход двух видов брони | initial:false; labels | Читаются расчётом SP и сопротивлений |
| defenseDifferenceMultiplier, defenseMultiplierCap | BooleanField/NumberField, 35–42 | Зарезервированное умножение/его предел | initial:false и5; labels; cap без min/max | Оба label отмечены как не функционирующие |
| variableDamage | BooleanField, 44–47 | Ввод переменного урона | initial:false; label | Ветка rollDamage |
| effects | TypedObjectField(SchemaField(itemEffect())), 49 | Воздействия по ключам | Default {}; name/statusEffect/percentage/varEffect | Не коллекция документов ActiveEffect |
| oilEffect | StringField, 51 | Сопоставление категории масла | initial:''; label не задан | damageMixin сравнивает с Actor.system.category |
| silverTrait, silverDamage | BooleanField/StringField, 52–56 | Две формы серебряного свойства | initial:false / ''; labels | Ветка определяется настройкой silverTrait |
| isMeteorite, isNonLethal | BooleanField, 57–61 | Метеоритное свойство и нелетальный урон | initial:false; labels | damageMixin и ApplyNormalDamage |
| addEffects; enhancementsEffects; getPreprocessedEffects | Два метода и getter, 65–98 | Объединение/представление воздействий | Prototype | Поведение подробно ниже |
| migrateData; migrateEffectsToTypedField | Статические методы, 101–115 | Преобразование старого массива effects | Вызываются lifecycle модели | Изменение входного source |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| defineSchema() | fields; itemEffect() | 18 полей | 13 BooleanField, два NumberField, два StringField и TypedObjectField | Синхронно; диапазон percentage задаёт импорт itemEffect |
| addEffects(effects) | Объект записей; this.effects | undefined | this.effects={...this.effects,...effects} | Меняет подготовленное this.effects, при одинаковом ID побеждает новое; значения не клонируются; нет updateSource/update |
| get enhancementsEffects() | this.parent; необязательный parent.enhancementItems | Новый объект effects | Игнорирует пустые объекты элементов; поверхностно объединяет enhancement.system?.effects по порядку | Не добавляет в this.effects; при коллизии ID побеждает последний; parent безусловно нужен |
| getPreprocessedEffects() | this.effects — объект itemEffect | Array записей | Перебор ключей; один результат для truthy одинакового statusEffect, конкатенация различных имён и сумма percentage; записи без статуса не объединяет | Копирует записи верхнего уровня, исходные effects не меняет; varEffect сохраняет от первой; cap внутри метода отсутствует |
| migrateData(source) | Сырой объект | super.migrateData(source) | Сначала migrateEffectsToTypedField(source), потом базовая миграция | Меняет input; не DB-сохранение |
| migrateEffectsToTypedField(source) | source.effects | undefined | Только непустой Array превращает в Object.fromEntries с randomID для каждого элемента | Пустой Array/готовый object не меняет; старый ключ не удаляет, заменяет его значение |

Число BooleanField в схеме — 13: armorPiercing, improvedArmorPiercing, ablating, crushingForce, damageIsAblation, damageToAllLocations, bypassesWornArmor, bypassesNaturalArmor, defenseDifferenceMultiplier, variableDamage, silverTrait, isMeteorite, isNonLethal. Общая схема сама не выполняет их боевую семантику.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| itemEffect | [module/data/item/templates/itemEffectData.js](../../../../../../../../../module/data/item/templates/itemEffectData.js) | ES import и вызов | Строки1,49; состав отдельного воздействия | Четыре поля: name '', statusEffect null, percentage0 с min0/max100, varEffect false |
| DataModel; fields.*; randomID | Foundry14.367.0, common/abstract/data.mjs; common/data/fields.mjs; common/utils/helpers.mjs | Наследование, схема и генерация ID | defineSchema/migrateData/миграция массива | Настоящие модели/поля/утилиты в Node |
| parent.enhancementItems | [module/data/item/weaponData.js](../../../../../../../../../module/data/item/weaponData.js) | Чтение внешнего контекста | getter enhancementsEffects ожидает записи {system,...}, подготовленные WeaponData | prepareDerivedData и реальный parent сверены |
| enhancement.system.effects | [module/data/item/enhancementData.js](../../../../../../../../../module/data/item/enhancementData.js) | Чтение схемы другого предмета | getter и внешний вызов addEffects | Тип TypedObjectField совпал |
| WITCHER.Weapon.*; WITCHER.Item.DamageProperties.* | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | Labels полей | Три неработающие настройки обозначены прямо в обоих переводах |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/weaponData.js](../../../../../../../../../module/data/item/weaponData.js); [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | DamageProperties | EmbeddedDataField system.damageProperties | Прямые импорты и схемы |
| [module/data/item/templates/combat/skillAttackData.js](../../../../../../../../../module/data/item/templates/combat/skillAttackData.js) | DamageProperties | EmbeddedDataField skillAttack.damageProperties | Импорт2/поле22 |
| [module/data/chatMessage/templates/damageData.js](../../../../../../../../../module/data/chatMessage/templates/damageData.js) | DamageProperties | EmbeddedDataField damage.properties в сообщении атаки | Прямой импорт/поле |
| [module/data/chatMessage/defenseMessageData.js](../../../../../../../../../module/data/chatMessage/defenseMessageData.js) | DamageProperties | EmbeddedDataField attackWeaponProperties | Прямой импорт/поле |
| [module/data/chatMessage/damageMessageData.js](../../../../../../../../../module/data/chatMessage/damageMessageData.js) | DamageProperties.defineSchema() | Spread полей в SchemaField; effects заменён ArrayField с applied | Сверка defineSchema и реальная инициализация |
| [module/data/migrations/damagePropertiesMigration.js](../../../../../../../../../module/data/migrations/damagePropertiesMigration.js) | source.damageProperties | Перенос верхних прежних полей перед вложенной миграцией | Два caller и порядок миграции |
| [module/item/mixins/damageUtilMixin.js](../../../../../../../../../module/item/mixins/damageUtilMixin.js) | system.damageProperties; getPreprocessedEffects | createBaseDamageObject берёт ссылку; rollDamage готовит массив effects и отправляет в сообщение/flag | 8–18,47–88 |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | addEffects/toObject(false) | Присоединяет боеприпас/улучшения; сериализует properties; mergeDamageProperties добавляет свойства профессии | 136–176,328–356 |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../../module/actor/mixins/castSpellMixin.js); [module/actor/mixins/professionMixin.js](../../../../../../../../../module/actor/mixins/professionMixin.js) | damageProperties и effects | Магия масштабирует varEffect; профессия передаёт свойства своей атаки или additionalDamageProperties | castSpell185–188; profession143–149,258 |
| [module/actor/mixins/armorMixin.js](../../../../../../../../../module/actor/mixins/armorMixin.js) | AP/ablating/crushingForce/bypasses* | SP и сопротивления | calculateArmorResistances/applySpDamage |
| [module/actor/mixins/damageMixin.js](../../../../../../../../../module/actor/mixins/damageMixin.js) | damageToAllLocations/oilEffect/improvedArmorPiercing/silver*/isMeteorite | Разветвление и расчёт полученного урона | applyDamage/calculateDamageWithLocation |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../module/actor/mixins/defenseMixin.js) | crushingForce/stun | Варианты защиты, повреждение при защите и оглушение | 27,303–306,414 |
| [module/scripts/combat/applyDamage.js](../../../../../../../../../module/scripts/combat/applyDamage.js) | isNonLethal | ApplyNormalDamage выбирает sta вместо hp | 39 |
| [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs); [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | Поля схемы, effects и enhancementsEffects | Редакторы и отображение; inherited Item actions управляют TypedObjectField | Пути schema/system и таблицы effects |

## Данные и изменения состояния

Три разных формы: Item.system.damageProperties — экземпляр; объект атаки имеет ссылку properties на него; итоговое DamageMessageData.damage.properties — объект схемы с массивом подготовленных эффектов и дополнительным applied. Тип damage.type расположен снаружи модели, поля damageType здесь нет.

addEffects изменяет модель в памяти: toObject() остаётся на исходных effects, toObject(false) видит дополненные. Из-за прямой ссылки createBaseDamageObject это изменяет подготовленный Item до переинициализации. Getter улучшений отдельно возвращает коллекцию и ничего не присоединяет.

Две записи одного статуса по 60 дают результат 120 в getPreprocessedEffects. Настоящая модель DamageMessageData при очистке ограничивает percentage до 100; ошибки валидации на этом сценарии нет. Возврат с суммой120 и сохранённое значение100 — разные этапы. Условие объединения имён сравнивает полную уже собранную строку; дедупликации отдельных имён нет.

Миграция [] сама ничего не делает; инициализация TypedObjectField затем даёт {}. Миграция непустого массива сохраняет значения под новыми случайными ID. Исторические данные документов не записывались.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все методы класса | Node stdin: реальные DataModel/поля/DamageProperties | Defaults18 ключей, addEffects, getter, preprocessing и два метода миграции выполнены | Источник parent улучшений задан вручную |
| Коллизии ID | addEffects с тем же ключом; getter двух улучшений | Победило последнее значение, ссылки на записи сохранены; собственные effects getter не изменил | Не запускалась привязка улучшений в UI |
| Группировка | Два bleeding с именами A/B и 60/60, безстатусная C10 | A,B→120, varEffect первой записи; C отдельно; source без изменений | Случайный бросок вероятности не выполнялся |
| Схема сообщения | Реальный DamageMessageData с копией подготовленного массива | 120 очищено до 100; applied default:false; invalid:false | Сохранение ChatMessage не выполнялось |
| Миграция | Пустой/непустой Array, отсутствующее поле, готовый object | ID создаются только для непустого Array; модель []→{} | Без БД |
| Ссылочная передача | Настоящий createBaseDamageObject, WeaponData и addEffects | Следующая структура атаки с тем же prepared Item видит ammo; исходное представление — только base | Не установлено, когда клиент переинициализирует Item между атаками |
| Серебряный флаг | Исходный calculateDamageWithLocation и DamageInstance | При silverTrait=true поле type осталось slashing; setType стало строкой silver | Сопряжённые SP-методы заменены, проверен ранний выход blockedBySp; без урона Actor |

## Непроверенные участки и открытые вопросы

Полные листы/боевые сообщения/вычислители не включены в десять карточек порции. Их импорты, поля и отдельные вызовы проверены до определения сущности. Не запускались бой, диалоги, случайные броски вероятности, обновление документов, мир и внешние модули. Область поиска: module/, templates/, локализации en/ru.

Расчётных обращений к damageIsAblation, defenseDifferenceMultiplier и defenseMultiplierCap в текущем module/ не найдено, кроме общих операций над полями. Оба перевода прямо маркируют их неработающими; это документированная незавершённая возможность, а не открытие работоспособной механики. Формулы для этих флагов не домысливались.

## Связанные проблемы

[issue-00025](../../../../../../../../issues/potential/issue-00025.md), [issue-00067](../../../../../../../../issues/potential/issue-00067.md), [issue-00069](../../../../../../../../issues/potential/issue-00069.md), [issue-00070](../../../../../../../../issues/potential/issue-00070.md), [issue-00073](../../../../../../../../issues/potential/issue-00073.md) — путь applyAP, приоритет прежних полей, потеря effects в слиянии, изменение подготовленного Item и silverTrait. Отдельная миграция effects брони описана в [issue-00068](../../../../../../../../issues/potential/issue-00068.md).

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.012 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.013

2026-09-10, `8cca18e14b75ec53028ee6bc49a837597de4d9af`; исходник неизменен. [Перекрёстная сверка](../../../../../../review-log.md#task-0003013).

Полностью разобраны [templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/damagePropertiesConfiguration.hbs) и его [обработчик](../../../../../../../../../module/item/sheets/configurations/WitcherPropertiesConfigurationSheet.js). Проверены все 16 записей formGroup в исходнике и восемь сочетаний silverTrait/staminaIsVar/defenseDifferenceMultiplier. Собственные effects редактируются через target/id/field; enhancementEffects выводятся disabled. В настоящем renderTemplate Foundry разрешает доступ Handlebars к свойствам прототипа, поэтому getter enhancementEffects доступен при штатных опциях. В изолированном сценарии старый deletion-синтаксис удаляет запись после преобразования ядром; комментарий о v14 не доказывает поломку удаления. Строка имени on по-прежнему превращается в false: дополнена issue-00060.

## Уточнение TASK-0003.014

2026-09-10, `0fa589bd300856ff309f362afcb66d6fa43401ab`; исходник неизменен. [Перекрёстная сверка](../../../../../../review-log.md#task-0003014).

Полностью описана фабрика [module/data/item/templates/itemEffectData.js](../../../../../../../../../module/data/item/templates/itemEffectData.js): четыре поля, ID во внешнем словаре, процент ограничивается 0–100 при очистке записи. [module/data/item/enhancementData.js](../../../../../../../../../module/data/item/enhancementData.js) поставляет словарь effects; getPreprocessedEffects группирует его записи и может складывать проценты уже после очистки. Текущая [module/data/item/armorData.js](../../../../../../../../../module/data/item/armorData.js) имеет отдельные effectsWithEnhancements/enhancementsEffects; это не методы DamageProperties и не документы ActiveEffect.

## Уточнение TASK-0003.019

2026-09-10, `rusbar-main`, `c26eb64dd54cc434087f54c3c6b678b6092b15a2`. [Форма профессионального навыка](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) редактирует 14 скалярных свойств (cap условно) и записи effects.name/statusEffect/percentage. [Конфигурация](../../../../../../../../../module/item/sheets/configurations/WitcherProfessionConfigurationSheet.js) использует полный путь system.skillPathN.skillM.skillAttack.damageProperties.effects.<id>; это TypedObjectField, не ActiveEffect. Кнопка удаления имеет issue-00111; редактирование on относится к issue-00060. Слияние с оружием остаётся прежней issue-00069, в этой порции оно прочитано по цепочке и не воспроизводилось заново.

[Перекрёстная сверка](../../../../../../review-log.md#task-0003019). Исходники не изменены; уточнение касается проверенных связей, не повторного полного разбора файла.

## Уточнение TASK-0003.021

Проверено 2026-09-11 на `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; исходник не менялся.

SpellData включает эту модель в damageProperties. Словарь damageProperties.effects отдельно от selfEffects/onCastEffects и встроенных Item.effects; первые две таблицы spellGeneral используют фабрику itemEffect напрямую, без getPreprocessedEffects DamageProperties.

Сверенные карточки: [module/data/item/spellData.js](../../spellData.js.md).

[Результаты и пределы сверки](../../../../../../review-log.md#task-0003021).
