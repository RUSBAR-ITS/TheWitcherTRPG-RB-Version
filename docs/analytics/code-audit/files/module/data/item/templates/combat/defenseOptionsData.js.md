# module/data/item/templates/combat/defenseOptionsData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/combat/defenseOptionsData.js](../../../../../../../../../module/data/item/templates/combat/defenseOptionsData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.012](../../../../../../../../tasks/task-0003.012.md), одна порция из десяти файлов |
| Запись перекрёстной сверки | [TASK-0003.012](../../../../../../review-log.md#task-0003012) |

## Назначение файла

Фабрика разрешённых способов защиты от конкретной атаки. Возвращает одно поле defenseOptions; это список вариантов для защищающегося, а не описание собственного способа защиты предмета.

## Условия использования

При импорте запоминается foundry.data.fields; при вызове defenseOptions() создаётся новое поле, при его initial читается CONFIG.WITCHER.defenseOptions. При включении в AttackMessageData находится на корне system сообщения, в профессии — внутри skillAttack.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, строка 1 | Псевдоним foundry.data.fields | Не экспортируется | Инициализируется при импорте |
| defenseOptions() | export default function, 3–11 | Создать поле схемы | Шесть прямых импортов | Создание definitions |
| defenseOptions | SetField(StringField), 5–9 | Разрешённые защитные варианты | Поле схемы | initial: все obj.value из CONFIG; String required:true, blank:false, без choices |
| initial callback | 6 | Снять актуальный список ключей | Вызывается Foundry | Возвращает массив, который инициализируется как Set |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| defenseOptions() | foundry.data.fields | Object {defenseOptions:DataField} | Создаёт SetField с label/hint | Синхронно, без документов |
| initial() | CONFIG.WITCHER.defenseOptions — массив объектов | Массив value | map по настройке на момент инициализации | Ошибка при отсутствующей конфигурации не перехватывается |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| fields.SetField, fields.StringField | Foundry 14.367.0, /opt/foundryvtt/common/data/fields.mjs | Глобальный API | Тип множества и его элементов | Настоящие модели выполнены |
| CONFIG.WITCHER.defenseOptions | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Чтение | initial, строки226–264 конфигурации | Шесть записей сопоставлены |
| WITCHER.Item.Settings.attacks.defendWith.label/hint | [lang/ru.json](../../../../../../../../../lang/ru.json); [lang/en.json](../../../../../../../../../lang/en.json) | Локализация | label/hint | Ключи схемы и формы |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/weaponData.js](../../../../../../../../../module/data/item/weaponData.js) | defenseOptions() | Spread в defineSchema; разрешения помещаются в system.defenseOptions | Прямые импорты и определения |
| [module/data/item/spellData.js](../../../../../../../../../module/data/item/spellData.js) | defenseOptions() | Spread в defineSchema; разрешения помещаются в system.defenseOptions | Прямые импорты и определения |
| [module/data/item/hexData.js](../../../../../../../../../module/data/item/hexData.js) | defenseOptions() | Spread в defineSchema; разрешения помещаются в system.defenseOptions | Прямые импорты и определения |
| [module/data/item/ritualData.js](../../../../../../../../../module/data/item/ritualData.js) | defenseOptions() | Spread в defineSchema; разрешения помещаются в system.defenseOptions | Прямые импорты и определения |
| [module/data/item/templates/combat/skillAttackData.js](../../../../../../../../../module/data/item/templates/combat/skillAttackData.js) | defenseOptions() | Spread внутри атаки профессии | skillAttack:23 |
| [module/data/chatMessage/attackMessageData.js](../../../../../../../../../module/data/chatMessage/attackMessageData.js) | defenseOptions() | Поле сообщения об атаке | defineSchema:23 |
| [module/item/mixins/damageUtilMixin.js](../../../../../../../../../module/item/mixins/damageUtilMixin.js) | Item.system.defenseOptions | createBaseDamageObject передаёт ссылку на Set | Строка17 |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../module/actor/mixins/defenseMixin.js) | defenseOptions | prepareAndExecuteDefense сопоставляет ключи с CONFIG и добавляет особые варианты предметов | 19–33 |
| [templates/sheets/item/configuration/tabs/general.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/general.hbs); [templates/sheets/item/configuration/tabs/spellGeneral.hbs](../../../../../../../../../templates/sheets/item/configuration/tabs/spellGeneral.hbs); [templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs](../../../../../../../../../templates/sheets/item/configuration/partials/profession/skillPathSkillPart.hbs) | Поле defenseOptions | formGroup для предмета/навыка | Соответствующие обращения к schema/system |

## Данные и изменения состояния

Сама фабрика не изменяет Actor/Item. По умолчанию создаются dodge, reposition, block, parry, parryThrown, magicResist. Явный пустой массив даёт пустое множество. Список CONFIG используется в initial и UI, но не объявлен choices: неизвестная непустая строка допускается полем. Проверка смысла такого ключа в downstream не встроена в эту фабрику.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Defaults и переданные данные | Настоящий WeaponData в Node | Получены шесть ключей, [] сохранён, not-existing принят в Set | Не запускался диалог защиты |
| Направление связи | Шесть прямых импортов; getItemAttack/DefenseProperties/Actor defense | defenseOptions выбирает защиту от атаки; defendsAgainst проверяет вид атакующей стороны | Не полный разбор вызывающих файлов |

## Непроверенные участки и открытые вопросы

Область поиска: module/ и templates/. Полный список кнопок и поведение неизвестного ключа в живом клиенте не проверялись; отсутствие choices описано как свойство схемы. Внешние расширения CONFIG не исследованы.

## Связанные проблемы

Новых самостоятельных проблем этой фабрики не зарегистрировано. Расхождения собственных защит профессии относятся к DefenseProperties/ProfessionData, а не к этому списку.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.012 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
