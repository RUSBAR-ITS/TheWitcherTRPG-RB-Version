# module/data/chatMessage/templates/damageData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/chatMessage/templates/damageData.js](../../../../../../../../module/data/chatMessage/templates/damageData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.040](../../../../../../../tasks/task-0003.040.md), 10 файлов, 237 логических строк |
| Запись перекрёстной сверки | [TASK-0003.040](../../../../../review-log.md#task-0003040) |

## Назначение файла

Общая фабрика вложенных параметров damage для сообщений атаки и урона. Задаёт ссылку на Item, формулу, тип/режим удара, исходную и итоговую локации, критические поправки и свойства предмета.

## Условия использования

AttackMessageData оборачивает результат в SchemaField. DamageMessageData также использует spread, но затем заменяет properties собственным SchemaField с массивом effects. Это схема данных, не генератор исходного урона Item.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| damageData | default function | Фабрика полей itemUuid, formula, crit, strike, type, originalLocation, location, properties | Прямые импорты | Каждый вызов возвращает новые экземпляры полей; документов не создаёт. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| damageData() | DamageProperties; critData(); locationData(); fields | Восемь полей | DocumentUUIDField; три StringField formula/strike/type и StringField originalLocation; два вложенных SchemaField и EmbeddedDataField | Синхронно; каждый вызов создаёт поля заново. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| DamageProperties | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | import, EmbeddedDataField | properties | Строки 1,16. |
| critData | [module/data/chatMessage/templates/critData.js](../../../../../../../../module/data/chatMessage/templates/critData.js) | import, вложенная схема | crit | Строки 2,12. |
| locationData | [module/data/chatMessage/templates/locationData.js](../../../../../../../../module/data/chatMessage/templates/locationData.js) | import, вложенная схема | location | Строки 3,15. |
| fields / DataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/data.mjs; /opt/foundryvtt/common/data/fields.mjs | внешний API | defineSchema, очистка, валидация и подготовка | Настоящие fields/DataModel и BaseChatMessage в Node; не браузер. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/chatMessage/attackMessageData.js](../../../../../../../../module/data/chatMessage/attackMessageData.js) | damageData() | Прямой import; system.damage | Сохраняет EmbeddedDataField properties. |
| [module/data/chatMessage/damageMessageData.js](../../../../../../../../module/data/chatMessage/damageMessageData.js) | damageData() | Прямой import; spread в system.damage | Заменяет properties; урон хранит массив applied-effects. |
| [module/item/mixins/damageUtilMixin.js](../../../../../../../../module/item/mixins/damageUtilMixin.js) | поля damage | createBaseDamageObject и rollDamage формируют payload для этих моделей | Не вызывает саму фабрику. |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../module/actor/mixins/castSpellMixin.js) | damage.duration / heal / shield | Добавляет сведения к исходному объекту для сообщения и непосредственных эффектов | Схема ниже эти поля не объявляет. |
| [module/scripts/combat/applyDamage.js](../../../../../../../../module/scripts/combat/applyDamage.js) | message.system.damage | Передаёт prepared-поля в Actor.applyDamage | Не читает вспомогательный flags.damage для восстановления duration. |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

UUID не ограничен Item и не проверяет существование. formula — строка, а не результат вычисления; типы strike/type/originalLocation не ограничены перечислением. Нет duration, heal, shield, item или вложенного defenseOptions: они удаляются при построении типизированного system.damage. Текущие кнопки лечения/щита используют HTML data-*, подготовленный раньше, поэтому исчезновение этих двух полей не отключает кнопки. Напротив, обработчики onHit/onDamage читают duration из prepared damage. Прямой applyDamageFromStatus передаёт обычный объект и не проходит эту схему.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Состав/вложенные данные | Группы 04–09 | UUID defaults, location-поля, настоящий DamageProperties в attack; отсутствие пяти вспомогательных ключей | Проверены настоящие модели и common ChatMessage. |
| Дальнейшие потребители | Чтение defenseMixin.handleDefenseResults и damageMixin.applyDamage | Оба ожидают damage.duration для эффектов | Боевое событие не запускалось на сервере; потеря поля воспроизведена изолированно. |

## Непроверенные участки и открытые вопросы

Локальные Foundry 14.367.0 и Node 24.16.0. Ядро полей, DataModel и общий BaseChatMessage настоящие; game/CONFIG и соседние документы представлены минимальными фасадами. Браузерный WitcherChatMessage, серверная запись, загрузка старой истории и несколько клиентов не запускались. Область итоговой сверки серии не заменяет полный разбор оставшихся боевых примесей.

## Связанные проблемы

[issue-00257](../../../../../../../issues/potential/issue-00257.md). Не переносит ранее обсуждённую проблему clone в схему: issue-00257 описывает более раннюю потерю duration при создании сообщения, issue-00044 — другой этап.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `74322e91edac106c82668f4a47eef53ce1889dc1`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003040) |
