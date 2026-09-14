# module/data/chatMessage/templates/attackData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/chatMessage/templates/attackData.js](../../../../../../../../module/data/chatMessage/templates/attackData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.040](../../../../../../../tasks/task-0003.040.md), 10 файлов, 237 логических строк |
| Запись перекрёстной сверки | [TASK-0003.040](../../../../../review-log.md#task-0003040) |

## Назначение файла

Фабрика четырёх вложенных полей атаки сообщения: выбор режима, навык, подпись и ссылка на применённый предмет.

## Условия использования

Вызывается из AttackMessageData.defineSchema как attack:SchemaField(attackData()). Это обычная функция, не отдельный DataModel или зарегистрированный тип. Передача factory не вычисляет бросок.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| attackData | default function | Фабрика полей attackOption, skill, alias, itemUuid | Прямые импорты | Каждый вызов возвращает новые экземпляры полей; документов не создаёт. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| attackData() | Глобальный foundry.data.fields; аргументов нет | Новый объект четырёх полей | StringField для attackOption/skill/alias; DocumentUUIDField для itemUuid | Синхронно; defaults строк не заданы, UUID default null. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| fields / DataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/data.mjs; /opt/foundryvtt/common/data/fields.mjs | внешний API | defineSchema, очистка, валидация и подготовка | Настоящие fields/DataModel и BaseChatMessage в Node; не браузер. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/chatMessage/attackMessageData.js](../../../../../../../../module/data/chatMessage/attackMessageData.js) | attackData() | Прямой импорт; определяет вложенный attack | defineSchema:22. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | attack.itemUuid / skill / attackOption / alias | Заполняет параметры для атаки оружием | Форма и построение ChatMessageData. |
| [module/actor/mixins/professionMixin.js](../../../../../../../../module/actor/mixins/professionMixin.js) | attack.skill / alias | Отправляет данные способности в сообщение атаки | getItemAttack / applyProfession; прямой маршрут не заполняет itemUuid. |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../module/actor/mixins/castSpellMixin.js) | attack | Подготовка магической атаки | castSpell. |
| [module/scripts/combat/combat.js](../../../../../../../../module/scripts/combat/combat.js) | message.system.attack | Передаёт в защиту; onDamage читает itemUuid | Динамические потребители модели, не прямые импорты фабрики. |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Три текстовых поля не имеют choices, required или initial в этом файле. itemUuid использует defaults ядра: null допустим; синтаксически корректный UUID Actor также проходит, хотя onDamage ожидает Item с rollDamage. Отсутствие документа по UUID не проверяется фабрикой.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Возвращаемые поля | Полный файл, группы 04–05 | Новые поля на каждый вызов; отсутствующий UUID null, некорректный синтаксис отклонён | Проверено внутри настоящего AttackMessageData. |
| Дальнейшая передача | Группа 12 и чтение onDamage | Контекст защиты получает тот же prepared attack | Защита и rollDamage в этой группе не исполняются. |

## Непроверенные участки и открытые вопросы

Схема и оба downstream потребителя установлены. .017/.018 сохраняют доступность UUID и восстановление данных старого чата ([U011-01](../../../../../cross-check-0002.md#u011-01)); .016/.018 — реальный HTMLElement/выбор Actor, [U011-03](../../../../../cross-check-0002.md#u011-03). Никакая новая валидация исходника не внесена.

## Связанные проблемы

[issue-00239](../../../../../../../issues/potential/issue-00239.md). Типизированный UUID не устраняет отсутствующую ссылку предмета в прямом применении профессии. Новых проблем самой фабрики не зарегистрировано.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `74322e91edac106c82668f4a47eef53ce1889dc1`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003040) |

## Сквозная сверка TASK-0004.011

2026-09-14; rusbar-main, 55e56567f42ed2da8850d913f28d727113ebdbd3. Исходник совпадает со срезом TASK-0001; изменено только описание.

Фабрика attackData создаёт четыре поля attackOption/skill/alias/itemUuid, встроенные AttackMessageData. Combat.executeDefense использует их и отдельные defenseOptions/damage/attackRoll; onDamage разрешает itemUuid и передаёт damage в Item. UUIDField не заменяет guard отсутствующего Item.

Сопоставленные определения и потребители: [module/data/chatMessage/attackMessageData.js](../attackMessageData.js.md), [module/scripts/combat/combat.js](../../../scripts/combat/combat.js.md), [module/actor/mixins/weaponAttackMixin.js](../../../actor/mixins/weaponAttackMixin.js.md).

[Протокол и границы](../../../../../review-log.md#task-0004011) — TASK-0004.011; процессы [R011-02](../../../../../cross-check-0002.md#r011-02). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
