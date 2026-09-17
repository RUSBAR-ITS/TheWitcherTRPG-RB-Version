# module/data/chatMessage/defenseMessageData.js

## Актуализация 2026-09-17 — 14.3.1.00026

М04; [реализация и пределы проверок](../../../../../../issues/open/issue-00332.md).

В crit добавлено числовое поле critEffectModifier с initial=0. Оно сохраняет поправку выбора меньшего/большего эффекта в typed ChatMessage; это не critLocationModifier и не изменение criticalLevel.

Непосредственные зависимости и потребители: [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js), [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js).

Основание: чтение текущего diff относительно `cd6fe2678105977ac220ab59e5fc87e6b3c6a343`; только статические проверки. Датированный разбор ниже сохраняет исходные доказательства и прежние адреса строк; изменённые контракты заменены описанием выше. Игровое исполнение этой версии пока не проверено.

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/chatMessage/defenseMessageData.js](../../../../../../../module/data/chatMessage/defenseMessageData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.040](../../../../../../tasks/task-0003.040.md), 10 файлов, 237 логических строк |
| Запись перекрёстной сверки | [TASK-0003.040](../../../../review-log.md#task-0003040) |

## Назначение файла

Данные результата защиты: бросок, защищающийся Actor, подпись защиты, свойства атакующего оружия и подготовленные последствия критического попадания/оглушения.

## Условия использования

extends BaseMessageData, frozen metadata.type='defense', регистрация CONFIG.ChatMessage.dataModels.defense. defenseMixin создаёт сырой payload, дополняет его через ChatMessageData.append и передаёт в Roll.toMessage.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| DefenseMessageData / metadata | default class, static frozen type:defense | Модель сообщения защиты | Регистратор | Наследует DataModel. |
| attackWeaponProperties / defender / defense | EmbeddedDataField / DocumentUUIDField / StringField:18–20 | Свойства атакующего, UUID защитника и выбранный навык | system | properties — экземпляр DamageProperties; defender default null. |
| crit | SchemaField:21–32 | criticalLevel, critdamage, bonusdamage, location | system.crit | location содержит name, alias, formula, critEffect, modifier; critEffectModifier отсутствует. |
| stun | SchemaField:33–35 | modifier NumberField | system.stun | Не автоматический спасбросок. |
| attackRoll | getter:39–41 | Псевдоним результата защиты rollTotal | Prepared | Название getter не превращает результат защиты в результат атакующего. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | super.defineSchema; DamageProperties | Схема system | Добавляет properties, UUID, String и две вложенные схемы | Нет выполнения последствий критического попадания. |
| get attackRoll() | this.rollTotal | Итог этого сообщения | Чтение | Не входит в toObject как schema-поле. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| BaseMessageData | [module/data/chatMessage/baseMessageData.js](../../../../../../../module/data/chatMessage/baseMessageData.js) | import, наследование | super.defineSchema() добавляет rollTotal | Прямой импорт и методы подкласса. |
| DamageProperties | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | import, EmbeddedDataField | attackWeaponProperties | Прямой импорт:1, схема:18. |
| fields / DataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/data.mjs; /opt/foundryvtt/common/data/fields.mjs | внешний API | defineSchema, очистка, валидация и подготовка | Настоящие fields/DataModel и BaseChatMessage в Node; не браузер. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | класс и metadata.type | CONFIG.ChatMessage.dataModels[type]; документ через documentClass | registerDataModels:76–80. |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | type:defense; crit/stun | Создаёт результат защиты, добавляет последствия до toMessage | prepareAndExecuteDefense / checkForCrit / handleCritLocation. |
| [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) | crit, attackWeaponProperties | Передаёт crit в applyCritDamage/applyBonusCritDamage/applyCritWound; stun кнопка читает properties.stun | Критический stun вызывает stunSave без аргумента. |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | crit | applyCritWound выбирает травму по location/criticalLevel/critEffectModifier | Потребитель через combat.js. |
| [module/scripts/rolls/fumble.js](../../../../../../../module/scripts/rolls/fumble.js) | DefenseMessageData | Прямой import; проверка constructor | Условие отображения пункта провала. |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

rollTotal — результат защиты. criticalLevel/critdamage/bonusdamage относятся к последствиям атаки. В отличие от locationData, crit.location.modifier числовой, formula без initial1, добавлено critEffect. При пустом payload crit.location={} и stun={}, не нули. Сырой crit.critEffectModifier, присвоенный defenseMixin, отсутствует в этой схеме: модель его очищает. При отсутствии явного location.critEffect дальнейшее сложение случайного числа с undefined даёт NaN, что влияет на выбор lesserEffect.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Типы и сериализация | Группы 01–05,10 | Числовой modifier '-3'→−3; formula default undefined; critEffectModifier удалён и из prepared, и из source | Проверен настоящий common BaseChatMessage. |
| Выбор травмы | Группа 11, настоящий damageMixin.applyCritWound | Сырой modifier+6 выбрал greater; тот же crit после модели — lesser | Каталог двух травм, fromUuid, addItem/ChatMessage — фасады; не DB/книги правил. |

## Непроверенные участки и открытые вопросы

Границы crit/stun и текущий consumer сопоставлены. .012/.017 продолжают состояние Item/UUID/индекс ([U011-05](../../../../cross-check-0002.md#u011-05)), .018 — существование документов после загрузки истории ([U011-01](../../../../cross-check-0002.md#u011-01)). Реальное контекстное меню и helper выбора Actor — [U011-03](../../../../cross-check-0002.md#u011-03).

## Связанные проблемы

[issue-00258](../../../../../../issues/potential/issue-00258.md), [issue-00183](../../../../../../issues/potential/issue-00183.md). Потеря критического модификатора подтверждена на границе данных и потребителя; пока potential. Работа всех формул защиты и полное применение критического урона не охвачены.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `74322e91edac106c82668f4a47eef53ce1889dc1`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003040) |

## Дополнительная сверка TASK-0003.041

2026-09-12, rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; исходник не изменён.

[weaponAttack](../../actor/mixins/weaponAttackMixin.js.md) получает critEffectModifier от Item.createBaseDamageObject и передаёт его в AttackMessageData: значение 2 сохраняется. Отдельное создание настоящей DefenseMessageData снова очистило critEffectModifier (258). Полная prepareAndExecuteDefense не запускалась; её разбор — TASK-0003.042.

[Сверка и ограничения](../../../../review-log.md#task-0003041). Уточнение связи не увеличивает пофайловое покрытие; исправления не выполнялись.

## Дополнительная сверка TASK-0003.042

2026-09-12, rusbar-main, 16695cbfc7fec3e0de56660c7cab21bc0304e94b; исходники не изменены.

[Полный producer](../../actor/mixins/defenseMixin.js.md) в группе 22 передал critEffectModifier=6; настоящая модель удаляет его (258). Группа 32 на выходе этого producer: native applyCritWound выбрал greater для raw и lesser для cleaned при фиксированном d6=1. В профессиональной ветке defense undefined, основа/заголовок работают через skillOverride; влияние на предметные fumble отдельно не тестировалось.

[Сверка и ограничения](../../../../review-log.md#task-0003042). Уточнение связей не увеличивает покрытие. Код и статусы issues не исправлялись; подтверждение пользователя не получено.

## Дополнительная сверка TASK-0003.045

2026-09-12, rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3; исходники не изменены.

Группа 23 выполнила [критический пункт меню](../../../../../../../module/scripts/combat/combat.js) с настоящей DefenseMessageData. Consumer передал actor.applyCritWound тот же model.crit, в котором critEffectModifier уже отсутствует. Это подтверждает последнюю границу issue258, без повторного создания травмы/выбора компедиума. Группы 03/05 отдельно подтвердили чтение attackWeaponProperties.stun и пять аргументов executeDefense; DOM/выбор Actor — фасады.

[Проверки, результаты и ограничения](../../../../review-log.md#task-0003045). Связанные файлы не засчитываются повторно в покрытии.

## Сквозная сверка TASK-0004.011

2026-09-14; rusbar-main, 55e56567f42ed2da8850d913f28d727113ebdbd3. Исходник совпадает со срезом TASK-0001; изменено только описание.

Defense определяет собственную crit.location со stun и Embedded attackWeaponProperties; это другая схема, чем damage.crit/location. critEffectModifier не объявлен и удаляется, criticalLevel/critdamage/bonusdamage/critEffect остаются. attackRoll — getter rollTotal. Combat callbacks выбирают текущего Actor, затем передают crit; defenderUUID не гарантирует этого адресата.

Сопоставленные определения и потребители: [module/data/chatMessage/baseMessageData.js](baseMessageData.js.md), [module/data/chatMessage/templates/critData.js](templates/critData.js.md), [module/data/chatMessage/templates/locationData.js](templates/locationData.js.md), [module/scripts/combat/combat.js](../../scripts/combat/combat.js.md), [module/actor/mixins/damageMixin.js](../../actor/mixins/damageMixin.js.md), [module/data/item/templates/combat/damagePropertiesData.js](../item/templates/combat/damagePropertiesData.js.md), [module/setup/registerDataModels.js](../../setup/registerDataModels.js.md).

[Протокол и границы](../../../../review-log.md#task-0004011) — TASK-0004.011; процессы [R011-01](../../../../cross-check-0002.md#r011-01), [R011-02](../../../../cross-check-0002.md#r011-02), [R011-09](../../../../cross-check-0002.md#r011-09). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
