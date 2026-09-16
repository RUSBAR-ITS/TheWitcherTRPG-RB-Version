# module/data/chatMessage/templates/locationData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/chatMessage/templates/locationData.js](../../../../../../../../module/data/chatMessage/templates/locationData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `74322e91edac106c82668f4a47eef53ce1889dc1` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.040](../../../../../../../tasks/task-0003.040.md), 10 файлов, 237 логических строк |
| Запись перекрёстной сверки | [TASK-0003.040](../../../../../review-log.md#task-0003040) |

## Назначение файла

Фабрика локации попадания внутри damage: имя, отображаемая подпись, множитель урона и текстовый модификатор.

## Условия использования

damageData вызывает locationData при создании SchemaField. DefenseMessageData самостоятельно описывает crit.location с другими типами/defaults и не импортирует эту фабрику.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| locationData | default function | Фабрика полей name, alias, formula, modifier | Прямые импорты | Каждый вызов возвращает новые экземпляры полей; документов не создаёт. |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| locationData() | foundry.data.fields | Четыре новых поля | name/alias/modifier:StringField initial ''; formula:NumberField initial1 | Не выбирает локацию и не вычисляет урон. |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| fields / DataModel | Foundry 14.367.0: /opt/foundryvtt/common/abstract/data.mjs; /opt/foundryvtt/common/data/fields.mjs | внешний API | defineSchema, очистка, валидация и подготовка | Настоящие fields/DataModel и BaseChatMessage в Node; не браузер. |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/chatMessage/templates/damageData.js](../../../../../../../../module/data/chatMessage/templates/damageData.js) | locationData() | Прямой import; damage.location | Строки 3,15. |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../module/actor/mixins/defenseMixin.js) | damage.location | Определяет критическую локацию и переносит в crit.location результата | handleCritLocation / подготовка сообщения. |
| [module/scripts/combat/applyDamage.js](../../../../../../../../module/scripts/combat/applyDamage.js) | location | Подменяет/уточняет место перед Actor.applyDamage | Динамическое чтение prepared damage. |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../module/actor/mixins/castSpellMixin.js) | location | Подготовка выбранной локации магической атаки | castSpell. |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Пустая локация нормализуется в {name:'',alias:'',formula:1,modifier:''}. Число modifier −3 становится строкой '-3'; formula '0.5' становится числом0.5. min/max/choices не заданы. В crit.location защиты modifier:NumberField, formula без initial1, есть critEffect:NumberField; передача текста вроде '-3[label]' туда не является допустимым числом.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Оба контракта локации | Группа 05 | Подтверждены initial1 против undefined и StringField против NumberField; нечисловой modifier защиты отвергнут | Не доказательство наличия такого текста в действующих данных. |
| Свежие экземпляры | Группа 05 | Повторный вызов фабрики возвращает новый объект полей | Жизненный цикл документов не исполнялся. |

## Непроверенные участки и открытые вопросы

Обе схемы и локационные consumers установлены. .017 проверяет таблицы/индекс tailWing ([U011-05](../../../../../cross-check-0002.md#u011-05)), .018 — жизнь prepared объекта при повторе/после update ([U011-01](../../../../../cross-check-0002.md#u011-01)/[U011-02](../../../../../cross-check-0002.md#u011-02)). Случайное распределение попаданий не проверялось.

## Связанные проблемы

Различие схем зафиксировано как контракт, а не самостоятельная неисправность: фактический маршрут с несовместимым текстовым modifier не установлен.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `74322e91edac106c82668f4a47eef53ce1889dc1`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003040) |

## Сквозная сверка TASK-0004.011

2026-09-14; rusbar-main, 55e56567f42ed2da8850d913f28d727113ebdbd3. Исходник совпадает со срезом TASK-0001; изменено только описание.

damage location содержит name/alias/formula/modifier, где modifier — строка. Defense.crit.location отдельно использует числовой modifier и critEffect. Actor.getLocationObject при нанесении может заменить prepared location целиком; Empty оставляет ранее выбранное значение. В allLocations внешний damage.location меняется по очереди, но общие порции остаются общими.

Сопоставленные определения и потребители: [module/data/chatMessage/templates/damageData.js](damageData.js.md), [module/data/chatMessage/defenseMessageData.js](../defenseMessageData.js.md), [module/scripts/combat/applyDamage.js](../../../scripts/combat/applyDamage.js.md), [module/actor/mixins/damageMixin.js](../../../actor/mixins/damageMixin.js.md), [module/actor/mixins/locationMixin.js](../../../actor/mixins/locationMixin.js.md).

[Протокол и границы](../../../../../review-log.md#task-0004011) — TASK-0004.011; процессы [R011-02](../../../../../cross-check-0002.md#r011-02). В этой порции выполнена статическая сверка; прежние опыты сохраняют свои даты и фасады. Новых поведенческих запусков нет; браузер, мир, сеть и запись в БД не запускались.
