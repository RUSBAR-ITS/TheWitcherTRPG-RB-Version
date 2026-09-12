# module/data/chatMessage/damageMessageData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/chatMessage/damageMessageData.js](../../../../../../../module/data/chatMessage/damageMessageData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.040](../../../../../../tasks/task-0003.040.md), 10 файлов, 237 логических строк |
| Запись перекрёстной сверки | [TASK-0003.040](../../../../review-log.md#task-0003040) |

## Назначение файла

Схема сообщения уже брошенного урона. Сохраняет параметры damage и массив предварительно обработанных воздействий с результатом проверки вероятности applied.

## Условия использования

extends BaseMessageData; frozen metadata.type='damage'; регистрация CONFIG.ChatMessage.dataModels.damage. Item.rollDamage получает DamageProperties из сырого damage/сообщения атаки, вызывает getPreprocessedEffects и передаёт массив в эту модель.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| DamageMessageData / metadata | default class, static frozen type:damage | Модель system урона | Регистрация damage | DataModel. |
| damage / properties | SchemaField:19–34 / SchemaField:21 | Общая damage-схема с заменой properties | system.damage.properties | Обычный подготовленный объект, не экземпляр DamageProperties. |
| effects | ArrayField(SchemaField):23–32 | name, statusEffect, percentage, varEffect, applied | properties.effects | name initial ''; statusEffect null; percentage0 с min0/max100; два Boolean initialfalse. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| static defineSchema() | super.defineSchema(), damageData(), DamageProperties.defineSchema() | Схема rollTotal + damage | После spread заменяет properties, затем effects внутри него | Не вызывает getPreprocessedEffects и не бросает процент сам. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| BaseMessageData | [module/data/chatMessage/baseMessageData.js](../../../../../../../module/data/chatMessage/baseMessageData.js) | import, наследование | super.defineSchema() добавляет rollTotal | Прямой импорт и методы подкласса. |
| damageData | [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js) | import, spread | Базовые поля damage | Строки 3,20. |
| DamageProperties | [module/data/item/templates/combat/damagePropertiesData.js](../../../../../../../module/data/item/templates/combat/damagePropertiesData.js) | import, копирование defineSchema | Поля properties кроме effects | Строки 1,22; EmbeddedDataField из фабрики заменён. |
| fields / DataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/data.mjs; /opt/foundryvtt/common/data/fields.mjs | внешний API | defineSchema, очистка, валидация и подготовка | Настоящие fields/DataModel и BaseChatMessage в Node; не браузер. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/setup/registerDataModels.js](../../../../../../../module/setup/registerDataModels.js) | класс и metadata.type | CONFIG.ChatMessage.dataModels[type]; документ через documentClass | registerDataModels:76–80. |
| [module/item/mixins/damageUtilMixin.js](../../../../../../../module/item/mixins/damageUtilMixin.js) | type:damage; effects/applied | rollDamage отправляет обработанный массив через Roll.toMessage | Вычисляет applied до создания сообщения; отдельно пишет flags.damage. |
| [module/scripts/combat/applyDamage.js](../../../../../../../module/scripts/combat/applyDamage.js) | damage, properties.isNonLethal | Выбирает ресурс hp/sta и передаёт damage в Actor.applyDamage | Полный боевой расчёт остаётся последующим задачам. |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | properties.effects/applied и duration | Фильтрует статусные воздействия и применяет onDamage эффекты | applyDamage, вызов через applyDamage.js. |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

damage.itemUuid/formula/crit/strike/type/originalLocation/location наследуются из фабрики. properties сохраняет поля DamageProperties, но не его методы/миграцию контейнера. Входной словарь effects при обычной очистке ArrayField превращается в []; percentage101 ограничивается до100, −1 до0, '25' становится25. Запись без applied получает false. rollDamage обычно не задаёт system.rollTotal: итог лежит в message.rolls[0].total. Нестандартные damage.duration/heal/shield/item/defenseOptions не входят в схему. Дополнительный flags.TheWitcherTRPG.damage не восстанавливает duration в показанном потребителе system.damage.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Вложенные properties | Группы 07–08 | Обычный объект без getPreprocessedEffects; массив effects и default applied=false; диапазон очищается | ArrayField не выбрасывает ошибку на словарь, а очищает в пустой массив. |
| Очистка common-документа | Группы 02,09 | Незаявленные поля удаляются; registered class выбран верно | Без сохранения в мире. |
| Отправитель/потребитель | Статическое чтение damageUtilMixin, applyDamage.js и damageMixin | preprocessed effects → Roll.toMessage → system.damage → applied-фильтр | Не выполнен полный цикл броска и нанесения всех типов урона. |

## Непроверенные участки и открытые вопросы

Локальные Foundry 14.367.0 и Node 24.16.0. Ядро полей, DataModel и общий BaseChatMessage настоящие; game/CONFIG и соседние документы представлены минимальными фасадами. Браузерный WitcherChatMessage, серверная запись, загрузка старой истории и несколько клиентов не запускались. Область итоговой сверки серии не заменяет полный разбор оставшихся боевых примесей.

## Связанные проблемы

[issue-00025](../../../../../../issues/potential/issue-00025.md), [issue-00257](../../../../../../issues/potential/issue-00257.md). Неверное чтение damage.damageProperties в одном потребителе остаётся issue-00025. Потеря duration выделена; намеренность остальных отличий схем не объявлена ошибкой.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `74322e91edac106c82668f4a47eef53ce1889dc1`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003040) |

## Дополнительная сверка TASK-0003.044

2026-09-12, rusbar-main, 965132d5d7972a0edd73aaa62484a1b6ba15991f; исходники не изменены.

Выполнен полный [rollDamage](../../item/mixins/damageUtilMixin.js.md) с настоящим Roll и очисткой payload через DamageMessageData (группы 03–06): properties.effects — Array, applied50%=true/false по контролируемому входу,0%=false. raw/flag duration7 остаётся, system.damage.duration удаляется; critEffectModifier6 внутри damage.crit сохраняется. toMessage ожидается, последующий setFlag нет (уточнение 184). [Получатель](../../actor/mixins/damageMixin.js.md) рассчитывает урон и читает именно эту Array-форму, не Item TypedObject. Запись ChatMessage в БД подменена.

[Методика и пределы проверки](../../../../review-log.md#task-0003044). Уточнение связей не увеличивает покрытие; мир, браузер и БД не запускались.

## Дополнительная сверка TASK-0003.045

2026-09-12, rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3; исходники не изменены.

Полностью разобран [consumer сообщения](../../../../../../../module/scripts/combat/applyDamage.js). Он читает первый DOM .dice-total, а не message.rolls/system.rollTotal, выбирает HP/STA и передаёт prepared damage по ссылке. Группа 12 на настоящей модели повторила удаление duration и установила наследование выбранных head/oilEffect следующим применением при неизменном _source (300). Группы 29–31 проверили отдельные полные расчёты статуса до фасадной записи HP/shield; это не полный цикл обычного клика с реальным ChatMessage. [Расчёт Actor](../../../../../../../module/actor/mixins/damageMixin.js) описан в .044; прежняя оговорка о последующих задачах теперь относится к истории проверки .040.

[Проверки, результаты и ограничения](../../../../review-log.md#task-0003045). Связанные файлы не засчитываются повторно в покрытии.
