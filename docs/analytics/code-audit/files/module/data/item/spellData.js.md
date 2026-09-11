# module/data/item/spellData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.021](../../../../../../tasks/task-0003.021.md), 13 файлов, 936 логических строк |
| Запись перекрёстной сверки | [TASK-0003.021](../../../../review-log.md#task-0003021) |

## Назначение файла

Модель system предмета spell: хранение класса магии, параметров броска, формул урона/щита/лечения, словарей статусов и параметров области. Делегирует проверку пригодности защиты вложенной модели. Самостоятельно не бросает кубики, не применяет ActiveEffect и не списывает STA.

## Условия использования

registerDataModels связывает тип spell с SpellData; при импорте Object.assign добавляет методы spellRegionMixin в прототип. Foundry создаёт и очищает модель, миграционные методы принимают исходный объект. Лист читает поля; Actor.castSpell и общий Item.getItemAttack используют разные способы выбора навыка.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| SpellData | default class; 15–135 | Расширение CommonItemData | CONFIG.Item.dataModels.spell | Схема и методы модели |
| class, level, source, domain, sideEffect | StringField; 21–25; initial='' | Класс, уровень, стихия/традиция, вид знака, побочный эффект дара | system.* | Варианты UI не являются choices-ограничениями схемы |
| stamina, staminaIsVar | NumberField0 / BooleanFieldfalse; 27–28 | Стоимость и переменный режим | system.* | Ввод и чтение при castSpell |
| effect, range, duration, defence | StringField''; 30–33 | Описание, дальность, длительность и текст защиты | system.* | Текст defence отдельно от defenseOptions/defenseProperties |
| templateProperties, regionProperties | EmbeddedDataField; 35–36 | Геометрия и поведение региона | TemplateProperties / RegionProperties | Методы региона присоединены примесью |
| causeDamages, damage, damageType, damageProperties | Booleanfalse, Stringnull nullable, String'elemental', EmbeddedDataField; 38–45 | Признак урона, формула, тип и свойства | system.* | damageType имеет label, но не choices |
| createsShield, shield, doesHeal, heal | Booleanfalse / String''; 47–51 | Признаки и формулы щита/лечения | system.* | Потребитель рассчитывает результат позже |
| selfEffects, onCastEffects | TypedObjectField(SchemaField(itemEffect())); 53–54 | Словари записей name/statusEffect/percentage/varEffect | system.* с произвольным ID строки | Это данные статусов, не документы Item.effects |
| attackOptions(), defenseOptions(), defenseProperties | Фабрики и EmbeddedDataField; 56–58 | Виды/навыки атаки, допустимые ответы противника, собственная защита | system.* | Общие определения не дублируются здесь |
| fields; commonData | Локальные ссылки; 13, 17 | API полей и схема родителя | Не экспортируются | Схема дополняется spread |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | Внешние классы/CONFIG доступны | Объект полей | Общая схема + собственные/боевые/региональные поля | Ничего не записывает в документы |
| getUsedSkill() | parent.type; spellAttackSkill; class | Объект CONFIG.WITCHER.skillMap | Приоритет явный skillMap → magic[parent.type]?.skill → magic[class].skill | Последний lookup без optional chaining: пустой/неизвестный class при неверном навыке даёт TypeError |
| isApplicableDefense(attack) | Строка вида атаки | Boolean | defenseProperties.isApplicableDefense(attack) | Не проверяет текст defence |
| createDefenseOption(attack) | Пригодный навык | {modifier, skills:[name], itemTypes:[]} | Свойства защиты + имя getUsedSkill | getUsedSkill может бросить исключение |
| get canHaveTemporaryItemImprovement | Нет | true | Разрешает категорию временных улучшений | Не применяет улучшение сам |
| static migrateData(source) | Объект прежней/актуальной схемы | super.migrateData(source) | dificultyCheck → difficultyCheck; this.effects?.forEach(parseInt); migrateDamageProperties → migrateEffectsToTypedField → migrateTemplate → super | Меняет source; this — класс, а не source, поэтому this.effects обычно undefined; difficultyCheck не объявлен в итоговой схеме |
| static migrateEffectsToTypedField(source) | selfEffects/onCastEffects | undefined | Непустой массив → Object.fromEntries с randomID; объект и пустой массив оставляет | Пустые массивы затем очищаются TypedObjectField в {}; числовые строки очищает NumberField |
| static migrateTemplate(source) | Старое truthy templateSize | undefined | Строку переводит parseInt\|\|0; полностью заменяет templateProperties четырьмя старыми полями; удаляет четыре старых ключа | Числовой 0 пропускает перенос; смешанный ввод теряет новые настройки; '2.75' становится 2 |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| CommonItemData | [module/data/item/commonItemData.js](../../../../../../../module/data/item/commonItemData.js) | Импорт/наследование | defineSchema; super.migrateData через TypeDataModel | Прочитана вся общая модель |
| migrateDamageProperties | [module/data/migrations/damagePropertiesMigration.js](../../../../../../../module/data/migrations/damagePropertiesMigration.js) | Импорт/вызов | migrateData; перенос свойств и effects | Сверены truthy-ветви; issue-00067 |
| spellRegionMixin | [module/data/item/mixin/spellRegionMixin.js](../../../../../../../module/data/item/mixin/spellRegionMixin.js) | Импорт/Object.assign | createSpellRegion, fromItem, drawPreview, deleteSpellVisualEffect | Проверены имена методов и чтение templateProperties; полный региональный процесс — .022 |
| attackOptions | [module/data/item/templates/combat/attackOptionsData.js](../../../../../../../module/data/item/templates/combat/attackOptionsData.js) | Импорт/фабрика | defineSchema | spellAttackSkill.initial='spellcasting'; level добавляет вариант spell |
| DamageProperties | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | Импорт/вложенная модель | damageProperties | Определение и карточка .012 |
| defenseOptions | [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../../module/data/item/templates/combat/defenseOptionsData.js) | Импорт/фабрика | Допустимые виды ответа противника | Начальное множество всех CONFIG.defenseOptions.value |
| DefenseProperties | [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) | Импорт/вложение/делегирование | isApplicableDefense/createDefenseOption | Реальные методы проверены на ranged/melee |
| itemEffect | [module/data/item/templates/itemEffectData.js](../../../../../../../module/data/item/templates/itemEffectData.js) | Импорт/фабрика | Два словаря статусов | Четыре поля; percentage Number0..100 |
| TemplateProperties; RegionProperties | [module/data/item/templates/regions/templatePropertiesData.js](../../../../../../../module/data/item/templates/regions/templatePropertiesData.js); [module/data/item/templates/regions/regionPropertiesData.js](../../../../../../../module/data/item/templates/regions/regionPropertiesData.js) | Импорт/вложение | defineSchema | Проверены определения, полный разбор .022 |
| CONFIG.WITCHER.skillMap/magic | [module/setup/config.js](../../../../../../../module/setup/config.js) | Глобальный реестр | getUsedSkill | 4 класса spell → spellcast; типы hex/ritual → hexweave/ritcraft |
| foundry.data.fields; foundry.utils.randomID | Foundry14.367.0; /opt/foundryvtt/common/data/fields.mjs; common/abstract/data.mjs | Внешние поля/ID/миграция | Валидация, очистка TypedObjectField, генерация ключей | Использованы настоящие поля/TypeDataModel в Node |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | SpellData | Импорт и регистрация spell | 16, 61 |
| [module/item/sheets/WitcherSpellSheet.js](../../../../../../../module/item/sheets/WitcherSpellSheet.js) | system/схема | Контекст и отдельная конфигурация | _prepareContext через родителя |
| [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | attackOptions и *AttackSkill; type migration | getItemAttack; Hexes/Rituals переводятся в другие типы до модели | 18–25, 28–70 |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | getUsedSkill, параметры, selfEffects/onCastEffects, createSpellRegion | Рассчитывает бросок и передаёт статусы/формулы | Проверены ветви на границе модели; полного аудита файла нет |
| [module/item/mixins/defenseOptionMixin.js](../../../../../../../module/item/mixins/defenseOptionMixin.js) | createDefenseOption | Оборачивает результат модели именем Item | 2–7 |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | isApplicableDefense | Фильтрует пригодные предметы защиты | 18–20 |
| [templates/sheets/item/spell-sheet.hbs](../../../../../../../templates/sheets/item/spell-sheet.hbs) | system.* | Редактор | Полный разбор этой порции |
| [templates/partials/spell-header.hbs](../../../../../../../templates/partials/spell-header.hbs) | class/level/source/sourcebook | Заголовок редактора | Полный разбор этой порции |
| [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs) | selfEffects/onCastEffects/боевые поля | Таблица статусов | Полный разбор этой порции |

Область поиска: module/ и templates/ текущего checkout; регистрация сверена с system.json. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Сохранённые значения — поля схемы; атака/защита возвращают данные без update. Миграции меняют переданный source в памяти; сохранение относится к Foundry. Вызов new SpellData в проверках очищает поля, а миграции отдельно вызывались до конструктора. Статусы словарей передаются applyStatusEffect*, документы item.effects — applyActiveEffect*. UI не показывает percentage/varEffect для self/onCast, а прямое применение статуса в castSpell не использует эти поля как шанс.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Навыки/защита | Node, группы 01–02; реальные модели | 4 известных класса разрешаются; пустой class с default вызывает TypeError; явный ritcraft перекрывает fallback; защита ranged даёт modifier2/skills[spellcast] | Родитель Item — DataModel-фасад |
| Миграции | Группы 03–05; source → migrateData → модель | Пустые массивы становятся {}; непустые получают ID; 42 строкой →42 числом; старые значения области перезаписывают новые | Действующие базы и распространённость прежних схем не проверены |
| Контракт потребителя | Группа 16; исходный castSpell с подменами UI/Roll/записи | Typed selfEffects применяются, но не попадают в templateInfo; переменное лечение даёт ReferenceError heal | Нет сохранения STA/статусов, полного боя и мира |

## Непроверенные участки и открытые вопросы

Все 137 строк прочитаны. Внешние методы регионов и полный цикл магии остаются отдельными порциями. Игровые правила по книгам не сверялись. Влияние статусов, RPC, fumble, атаки и лечения в браузере не подтверждено.

## Связанные проблемы

[issue-00064](../../../../../../issues/potential/issue-00064.md), [issue-00065](../../../../../../issues/potential/issue-00065.md), [issue-00067](../../../../../../issues/potential/issue-00067.md), [issue-00074](../../../../../../issues/potential/issue-00074.md), [issue-00075](../../../../../../issues/potential/issue-00075.md), [issue-00076](../../../../../../issues/potential/issue-00076.md), [issue-00128](../../../../../../issues/potential/issue-00128.md), [issue-00133](../../../../../../issues/potential/issue-00133.md), [issue-00134](../../../../../../issues/potential/issue-00134.md). 64 дополнена пустым/неизвестным class; 65/67 — общие миграции; 74–76 — региональная граница; 128 — перенос области; 133/134 — установленные несовпадения модели с потребителем. Исправлений нет.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `a29234e7c42ef5f9d8095c2b5470e5e3c95824cc`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003021) |

## Уточнение TASK-0003.022

2026-09-11, `ef8117ba6e5a184989e65761d47a068381056e4a`; исходник не изменён.

Полностью разобраны обе вложенные региональные модели и примесь. TemplateProperties задаёт геометрию/секундный таймер, RegionProperties — Macro UUID и адаптеры записи. Обычные формы fromItem прерываются на Promise.all от Promise; эманации имеют отдельный рабочий путь с несогласованным выбором сцен/единиц. Поля damage.duration и visualEffectDuration запускают независимые механизмы удаления. Имена четырёх присоединённых методов подтверждены; это не собственные определения SpellData.

Связанные карточки: [module/data/item/templates/regions/templatePropertiesData.js](templates/regions/templatePropertiesData.js.md), [module/data/item/templates/regions/regionBehavioursData.js](templates/regions/regionBehavioursData.js.md), [module/data/item/templates/regions/regionPropertiesData.js](templates/regions/regionPropertiesData.js.md), [module/data/item/mixin/spellRegionMixin.js](mixin/spellRegionMixin.js.md).

[Результаты и пределы сверки](../../../../review-log.md#task-0003022).
