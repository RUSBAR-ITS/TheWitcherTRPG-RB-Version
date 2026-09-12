# module/data/chatMessage/attackMessageData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/chatMessage/attackMessageData.js](../../../../../../../module/data/chatMessage/attackMessageData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.040](../../../../../../tasks/task-0003.040.md), 10 файлов, 237 логических строк |
| Запись перекрёстной сверки | [TASK-0003.040](../../../../review-log.md#task-0003040) |

## Назначение файла

Типизированные данные сообщения атаки: результат броска, ссылка на атакующего, выбранная атака, доступные защиты и параметры следующего броска урона.

## Условия использования

extends BaseMessageData; metadata.type='attack'; CONFIG.ChatMessage.dataModels.attack. Данные приходят через ChatMessageData и extendedRoll от оружия, способности профессии или магии. Подготовленные поля затем читает контекстное меню защиты и кнопка урона.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| AttackMessageData / metadata | default class, static frozen type:attack | Модель system сообщения атаки | Регистратор | Жизненный цикл DataModel. |
| attacker | DocumentUUIDField:21 | UUID атакующего | system.attacker | Default null; синтаксис UUID не доказывает существование Actor. |
| attack / defenseOptions / damage | SchemaField / SetField / SchemaField:22–24 | Атака, защиты, урон | Схемы из трёх фабрик | Вложенные поля очищаются по схемам. |
| attackRoll | getter:28–30 | Псевдоним rollTotal | Prepared-модель | Не отдельное поле source. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | BaseMessageData; attackData(); defenseOptions(); damageData() | Поля rollTotal, attacker, attack, defenseOptions, damage | Объединяет фабрики и базовую схему | Не создает Actor/Item или Roll. |
| get attackRoll() | this.rollTotal | То же число или undefined | Прямое чтение | Не повторный бросок и не сохранённое поле. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| BaseMessageData | [module/data/chatMessage/baseMessageData.js](../../../../../../../module/data/chatMessage/baseMessageData.js) | import, наследование | super.defineSchema() добавляет rollTotal | Прямой импорт и методы подкласса. |
| defenseOptions | [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../../module/data/item/templates/combat/defenseOptionsData.js) | import, фабрика полей | Шесть защит по умолчанию в Set | Импорт:1; defineSchema:23. |
| attackData | [module/data/chatMessage/templates/attackData.js](../../../../../../../module/data/chatMessage/templates/attackData.js) | import, SchemaField | attack | Импорт:3, defineSchema:22. |
| damageData | [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js) | import, SchemaField | damage | Импорт:4, defineSchema:24. |
| fields / DataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/data.mjs; /opt/foundryvtt/common/data/fields.mjs | внешний API | defineSchema, очистка, валидация и подготовка | Настоящие fields/DataModel и BaseChatMessage в Node; не браузер. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | класс и metadata.type | CONFIG.ChatMessage.dataModels[type]; документ через documentClass | registerDataModels:76–80. |
| [module/scripts/combat/combat.js](../../../../../../../module/scripts/combat/combat.js) | attack, defenseOptions, damage, attacker, attackRoll | executeDefense передаёт Actor.prepareAndExecuteDefense; onDamage разрешает attack.itemUuid | Чтение system; группа 12. |
| [module/scripts/rolls/fumble.js](../../../../../../../module/scripts/rolls/fumble.js) | AttackMessageData | Прямой import для проверки constructor | Класс влияет на доступность пункта провала. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | type:attack и payload | Подготовка сырого сообщения через ChatMessageData/extendedRoll | Отправители; схема применяется при создании документа. |
| [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js) | type:attack и payload | Подготовка сырого сообщения через ChatMessageData/extendedRoll | Отправители; схема применяется при создании документа. |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | type:attack и payload | Подготовка сырого сообщения через ChatMessageData/extendedRoll | Отправители; схема применяется при создании документа. |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

attack: attackOption, skill, alias, itemUuid. damage: itemUuid, formula, crit, strike, type, originalLocation, location, properties. properties — настоящий DamageProperties; effects — словарь, не массив отметок applied. defenseOptions по умолчанию содержит dodge/reposition/block/parry/parryThrown/magicResist; явный пустой Set сохраняется, произвольная непустая строка также допустима. UUID-поля не ограничены Actor/Item и не проверяют разрешение ссылки. damage.duration отсутствует и удаляется при подготовке документа; HTML flavor построен раньше и не является обходом этой схемы для боевых обработчиков.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Модель и getter | Группы 01–07 | Наследование, defaults, UUID, типы location, Set, DamageProperties подтверждены | Прямой вызов моделей и common-документа. |
| Очистка system | Группа 09 | duration/heal/shield/item/defenseOptions внутри damage не переживают создание attack | Это не относится к корневому defenseOptions. |
| Дальнейшая защита | Группа 12 | Реальный контекстный обработчик передал attack/damage/Set, rollTotal17 и UUID | Метод Actor защиты заменён приёмником аргументов. |

## Непроверенные участки и открытые вопросы

Локальные Foundry 14.367.0 и Node 24.16.0. Ядро полей, DataModel и общий BaseChatMessage настоящие; game/CONFIG и соседние документы представлены минимальными фасадами. Браузерный WitcherChatMessage, серверная запись, загрузка старой истории и несколько клиентов не запускались. Область итоговой сверки серии не заменяет полный разбор оставшихся боевых примесей.

## Связанные проблемы

[issue-00239](../../../../../../issues/potential/issue-00239.md), [issue-00257](../../../../../../issues/potential/issue-00257.md), [issue-00183](../../../../../../issues/potential/issue-00183.md). Профессия может отправлять атаку без itemUuid; схема оставляет null. Потеря duration оформлена отдельно. Проверка конструктора fumble не означает поддержку любого наследника.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `74322e91edac106c82668f4a47eef53ce1889dc1`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003040) |

## Дополнительная сверка TASK-0003.041

2026-09-12, rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; исходник не изменён.

[Полностью разобран производитель оружейной атаки](../../actor/mixins/weaponAttackMixin.js.md). Группа 27 передала сериализуемый снимок с валидными фиктивными UUID в настоящий AttackMessageData: attack.itemUuid/damage.itemUuid и damage.crit.critEffectModifier=2 сохранены; raw item/ammunition и вручную добавленный duration удалены. Документ ChatMessage, права, БД не запускались.

[Сверка и ограничения](../../../../review-log.md#task-0003041). Уточнение связи не увеличивает пофайловое покрытие; исправления не выполнялись.
