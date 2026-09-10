# module/data/actor/templates/character/general/damage/damageTypeModificationData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](../../../../../../../../../../../module/data/actor/templates/character/general/damage/damageTypeModificationData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `17eeb6ae9efccf7474b9ca1845b9ab6370671a26` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.004](../../../../../../../../../../tasks/task-0003.004.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.004](../../../../../../../../review-log.md#task-0003004) |

## Назначение файла

Создаёт фиксированный набор изменений урона для семи типов, общий для персонажей и монстров через CommonActorData. Структура находится на system.damageTypeModification, вне general.

## Условия использования

При импорте локальная const fields получает foundry.data.fields. Файл экспортирует фабрику определения схемы; значениями экземпляра и валидацией занимается Foundry, а не сама фабрика. CommonActorData импортирует damageTypeModification из физического каталога character/general/damage. Расположение файла не ограничивает его использованием только персонажем.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | const, 3 | Классы полей | Локальная | Читается фабрикой |
| damageTypeModification | function, 5–15 | Сборка семи наборов | Default export | Создаёт семь независимых SchemaField |
| slashing | SchemaField, 7 | Поля flat/multiplication/applyAP | system.damageTypeModification.slashing | damageModification() → defaults 0/1/false |
| piercing | SchemaField, 8 | Поля flat/multiplication/applyAP | system.damageTypeModification.piercing | damageModification() → defaults 0/1/false |
| bludgeoning | SchemaField, 9 | Поля flat/multiplication/applyAP | system.damageTypeModification.bludgeoning | damageModification() → defaults 0/1/false |
| elemental | SchemaField, 10 | Поля flat/multiplication/applyAP | system.damageTypeModification.elemental | damageModification() → defaults 0/1/false |
| electricity | SchemaField, 11 | Поля flat/multiplication/applyAP | system.damageTypeModification.electricity | damageModification() → defaults 0/1/false |
| fire | SchemaField, 12 | Поля flat/multiplication/applyAP | system.damageTypeModification.fire | damageModification() → defaults 0/1/false |
| ice | SchemaField, 13 | Поля flat/multiplication/applyAP | system.damageTypeModification.ice | damageModification() → defaults 0/1/false |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| damageTypeModification(); 5–15 | Доступен foundry.data.fields | Объект семи SchemaField | Создаёт новые определения полей при каждом вызове | Синхронно; без записи документов, обработчиков событий и собственного catch |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| damageModification (default) | [module/data/actor/templates/character/general/damage/damageModificationData.js](../../../../../../../../../../../module/data/actor/templates/character/general/damage/damageModificationData.js) | Импорт и вызов | 1,7–13: схема одного типа | Полный разбор обеих фабрик |
| SchemaField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Глобальный API | 3,7–13 | Реальные CommonActorData, CharacterData, MonsterData |
| WITCHER.damageTypes | [module/setup/config.js](../../../../../../../../../../../module/setup/config.js) | Сверка ключей с интерфейсным словарём; прямого импорта нет | 733–768: восемь типов в конфигурации | Схема содержит семь; silver отсутствует. Назначение этого различия не установлено |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/actor/commonActorData.js](../../../../../../../../../../../module/data/actor/commonActorData.js) | damageTypeModification() | SchemaField на system.damageTypeModification | Импорт 9; вызов 49 |
| [module/data/actor/characterData.js](../../../../../../../../../../../module/data/actor/characterData.js); [module/data/actor/monsterData.js](../../../../../../../../../../../module/data/actor/monsterData.js) | Общий блок семи типов | Наследование CommonActorData, spread super.defineSchema() | Обе defineSchema:10–14 / 8–11 |
| [module/activeEffect/mixins/baseMixin.js](../../../../../../../../../../../module/activeEffect/mixins/baseMixin.js) | Ключи типов и flat/multiplication/applyAP | getDamageModifcators строит три пути на ключ; getActiveEffectsBasePaths включает их | 10,145–171 |
| [module/activeEffect/WitcherActiveEffectSheet.js](../../../../../../../../../../../module/activeEffect/WitcherActiveEffectSheet.js) | Пути мастера | wizardAction вызывает getActiveEffectsBasePaths для base; добавляет key в changes | 59–96; приложение mixin:140 |
| [module/actor/mixins/damageUtilMixin.js](../../../../../../../../../../../module/actor/mixins/damageUtilMixin.js) | flat/multiplication/applyAP | getFlatDamageMod и getMultiDamageMod читают выбранный damage.type | 3–16 |
| [module/actor/mixins/damageMixin.js](../../../../../../../../../../../module/actor/mixins/damageMixin.js) | flat и коэффициент через calculateArmorResistances | calculateDamageWithLocation вызывает getter flat и обработку сопротивлений | 200–214 |
| [module/actor/mixins/armorMixin.js](../../../../../../../../../../../module/actor/mixins/armorMixin.js) | multiplication/applyAP через getMultiDamageMod | calculateArmorResistances вызывает getter; множитель применяется внутри двух веток брони | 206–227 |
| [module/actor/witcherActor.js](../../../../../../../../../../../module/actor/witcherActor.js) | Методы mixin на Actor | Object.assign связывает damageMixin/damageUtilMixin/armorMixin | 440–441,449 |

Поиск выполнен по именам файлов/экспортов, полным и относительным путям данных в module/, templates/ и packsJson/. В 226 JSON-компедиумах строковых путей, начинающихся с system.general или system.damageTypeModification, не найдено. Содержимое действующих БД packs и внешние макросы не проверялись.

## Данные и изменения состояния

Фабрики хранят параметры без собственных вычислений. Применение установлено по конкретной цепочке:

| Поле | Чтение | Фактическое применение |
| --- | --- | --- |
| flat | getFlatDamageMod(damage) по damage.type; нет типа → 0 | После вычитания SP и проверки полного блокирования calculateDamageWithLocation добавляет отдельный DamageInstance только при flat>0. Затем применяется коэффициент локации. Отрицательное значение не уменьшает урон; созданный экземпляр имеет type=null. |
| multiplication | getMultiDamageMod(damage) по damage.type; нет типа → 1 | calculateArmorResistances умножает только в успешных ветках сопротивления надетой/естественной брони: floor(0.5 × damage × multiplication). Без сопротивлений брони не применяется; при обеих ветках применяется дважды. |
| applyAP | getMultiDamageMod проверяет флаг выбранного типа | При true пытается читать damage.damageProperties.armorPiercing/improvedArmorPiercing, хотя вызывающий код передаёт damage.properties. На обычном входе без AP воспроизведён TypeError. При AP calculateArmorResistances возвращает экземпляр до вызова getter, независимо от флага. |

Getter flat вызывается для общего damage.type, а не каждого damageInstance.type. Аналогично множитель выбирается по damage.type; у сопротивлений надетой брони проверяется тип экземпляра, у естественной — тип общего damage. Это зафиксированные обращения, а не предложенная архитектура. Сами getters ничего не сохраняют; calculateArmorResistances меняет переданный instance.damage в памяти. Сохранение HP находится дальше в damageMixin и здесь не воспроизводилось.

Блок отсутствует у LootData в проверке. Семь ключей фиксированы SchemaField, не создаются из CONFIG автоматически. getDamageModifcators перебирает данные непосредственного родителя эффекта либо его родителя: Actor/принадлежащий Actor Item дают 21 путь. Самостоятельный Item не имеет этих данных, поэтому эта функция возвращает пустой список; доступность других вариантов ввода определяется остальным редактором и здесь не оценивается.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Defaults и диапазоны | Реальные Common/Character/MonsterData | У семи типов {flat:0,multiplication:1,applyAP:false}; отрицательные и дробные числа принимаются | Не проверяет игровой смысл |
| Мастер ↔ схема | Исходный getDamageModifcators с подменой i18n и родителей | 21 путь Actor и Item внутри Actor; все найдены в схеме. Для самостоятельного Item — 0 | Окно, выбор и запись ActiveEffect не выполнялись |
| applyAP ↔ реальный контракт damage | Исходные calculateArmorResistances/getMultiDamageMod | true и properties без AP → TypeError; AP-вход → возврат damage=10 | Без полного боя |
| multiplication ↔ сопротивления | Урон 10, multiplication=0.5, applyAP=false | Без брони 10; только надетая 2; только естественная 2; обе 0 | Модель брони подменена объектами; её правила отдельно не оценивались |
| flat ↔ calculateDamageWithLocation | Исходный метод, SP=0, torso×1, брони нет; запись SP подменена | flat=-3/0/+3 → массивы урона [10]/[10]/[10,3] | Нет реального урона, чата, износа, серебра и прочих веток |

## Непроверенные участки и открытые вопросы

Полностью прочитан исходник и точечно проверены определения и потребители перечисленных связей. Мир, браузер, сохранение форм и применение реального ActiveEffect не запускались. Полный анализ соседних файлов остаётся их порциям; просмотр связи не повышает их статус в реестре. Отсутствие silver в этой фиксированной схеме при наличии в CONFIG.damageTypes зафиксировано как различие. Для признания его проблемой нужно определить предусмотренную поддержку модификаторов серебра; отдельная issue на этом основании не создана.

## Связанные проблемы

[issue-00025](../../../../../../../../../../issues/potential/issue-00025.md), [issue-00026](../../../../../../../../../../issues/potential/issue-00026.md), [issue-00027](../../../../../../../../../../issues/potential/issue-00027.md) — применение вложенных параметров. [issue-00021](../../../../../../../../../../issues/potential/issue-00021.md) — ранее обнаруженная потеря damage.type при уроне начала хода: такой вход выбирает fallback 0/1 вместо набора конкретного типа.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.004 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.006

2026-09-10, `fe7ea7420cd4dfa6ee51baf7520f7b0ad8f8b13d`. Подтверждено самостоятельное верхнее поле damageTypeModification:49. Оно наследуется монстром вместе с CommonActorData; строки MonsterData.resistances/immunities и два resistantNon* флага — другие поля и другие потребители.

Карточки сборки: [commonActorData](../../../../commonActorData.js.md), [monsterData](../../../../monsterData.js.md). [Сверка TASK-0003.006](../../../../../../../../review-log.md#task-0003006).

## Уточнение TASK-0003.012

2026-09-10, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9`; исходник не изменён. Схема свойств источника разобрана в [DamageProperties](../../../../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js). Тип конкретного повреждения находится в damage.type, а свойства — в damage.properties; поле Item.system.damageProperties имеет другое положение. Наличие одного общего класса не исправляет ошибочный путь getMultiDamageMod при applyAP: уточнена [issue-00025](../../../../../../../../../../issues/potential/issue-00025.md). Флаги AP по-прежнему вызывают ранний выход calculateArmorResistances.

Результат и границы — [сверка TASK-0003.012](../../../../../../../../review-log.md#task-0003012).
