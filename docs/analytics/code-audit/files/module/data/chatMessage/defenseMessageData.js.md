# module/data/chatMessage/defenseMessageData.js

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

Локальные Foundry 14.367.0 и Node 24.16.0. Ядро полей, DataModel и общий BaseChatMessage настоящие; game/CONFIG и соседние документы представлены минимальными фасадами. Браузерный WitcherChatMessage, серверная запись, загрузка старой истории и несколько клиентов не запускались. Область итоговой сверки серии не заменяет полный разбор оставшихся боевых примесей.

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
