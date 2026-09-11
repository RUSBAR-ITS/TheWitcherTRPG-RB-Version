# module/data/item/templates/weaponTypeData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/item/templates/weaponTypeData.js](../../../../../../../../module/data/item/templates/weaponTypeData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `d20d821e3a8a0a989ec503b0e97413a5a1431ad9` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.012](../../../../../../../tasks/task-0003.012.md), одна порция из десяти файлов |
| Запись перекрёстной сверки | [TASK-0003.012](../../../../../review-log.md#task-0003012) |

## Назначение файла

Фабрика описания типа оружия: свободный текст и четыре независимых флага видов урона. Не вычисляет урон и не определяет способ атаки или навык.

## Условия использования

При импорте используется foundry.data.fields. Единственный прямой импорт — WeaponData; weaponType() включается в SchemaField поля system.type. Класс Item имеет также документный type:'weapon': это другой уровень данных.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| fields | Локальная константа, строка 1 | Псевдоним foundry.data.fields | Не экспортируется | Инициализируется при импорте |
| weaponType() | export default function, 3–11 | Создание схемы типа оружия | Импорт WeaponData | Возвращает пять полей |
| text | StringField, 5 | Свободное текстовое обозначение | initial:'' | Не является enum |
| slashing, piercing, bludgeoning, elemental | BooleanField, 6–9 | Наличие четырёх видов урона | initial:false у каждого | Независимые флаги; можно включить несколько |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| weaponType() | foundry.data.fields | Object из пяти DataField | Создаёт StringField и четыре BooleanField | Синхронно; нет label/hint/choices, записи и бизнес-валидации комбинаций |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| fields.StringField/BooleanField | Foundry 14.367.0, common/data/fields.mjs | Глобальный API | Все поля | Настоящий WeaponData |
| WITCHER.damageTypes | [module/setup/config.js](../../../../../../../../module/setup/config.js) | Смысловое соответствие ключей | Четыре имени есть в восьми настроенных damageTypes | 733–770; фабрика CONFIG не читает |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/data/item/weaponData.js](../../../../../../../../module/data/item/weaponData.js) | weaponType() | SchemaField system.type | Строки3,17 |
| [templates/sheets/item/weapon-sheet.hbs](../../../../../../../../templates/sheets/item/weapon-sheet.hbs) | Четыре флага | Checkbox .damage-type | Чтение/редактирование system.type |
| [templates/dialog/combat/weapon-attack.hbs](../../../../../../../../templates/dialog/combat/weapon-attack.hbs) | Четыре флага | Формирование select damageType | 19–31; конкретный выбранный тип передаёт weaponAttack |
| [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs); [templates/chat/item/partials/item-description/tags.hbs](../../../../../../../../templates/chat/item/partials/item-description/tags.hbs) | type.text | Отображение описания типа | Соответственно46 и292–294 |

## Данные и изменения состояния

[WitcherWeaponSheet._onDamageTypeEdit](../../../../../../../../module/item/sheets/WitcherWeaponSheet.js) копирует system.type, меняет boolean по id checkbox, составляет text из локализованных включённых типов через join и вызывает item.update({system.type:...}). Поэтому в схеме text допускает свободную строку, но его обработчик предусматривает формирование из флагов; отдельного текстового input в нём нет. Метод прочитан полностью как связь, не как полный разбор листа. На момент TASK-0003.012 подключение слушателя оставалось открытым вопросом; TASK-0003.013 проследила его через базовый _onRender и проверила изолированным вызовом, см. уточнение ниже.

Не содержит silver/electricity/fire/ice из общего damageTypes; серебро и метеорит описываются в DamageProperties. Четыре флага задают доступные варианты, а конкретный damage.type появляется из формы атаки. Фабрика не выбирает один активный вид и не запрещает все false.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Схема и сочетания | new WeaponData({type:{slashing:true,elemental:true}}) | text='', slashing/elemental true, остальные false | Без отправки диалога |
| Связи | Прямой импорт и обращения system.type в module/templates | Роль поля отделена от Item.type и attackOptions | Нестандартные обращения сторонних модулей не проверены |

## Непроверенные участки и открытые вопросы

Полная логика select и fallback в weapon-attack.hbs здесь не воспроизводилась. Лист оружия — TASK-0003.013. Отсутствие типов из общего справочника само по себе не объявляется ошибкой или нарушением правил.

## Связанные проблемы

Новых самостоятельных проблем фабрики не зарегистрировано.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.012 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.

## Уточнение TASK-0003.013

2026-09-10, `8cca18e14b75ec53028ee6bc49a837597de4d9af`; исходник неизменен. [Перекрёстная сверка](../../../../../review-log.md#task-0003013).

Полный разбор [module/item/sheets/WitcherWeaponSheet.js](../../../../../../../../module/item/sheets/WitcherWeaponSheet.js) и [templates/sheets/item/weapon-sheet.hbs](../../../../../../../../templates/sheets/item/weapon-sheet.hbs) установил цепочку WitcherItemSheet._onRender → this.activateListeners → .damage-type/change → _onDamageTypeEdit. Четыре checkbox имеют id, но не name; метод инвертирует текущий флаг по id, затем собирает text из локализованных включённых типов в фиксированном порядке. При начальном slashing=true и событии для piercing получен payload с text «Режущий, Колющий». Изолированный вызов настоящего _onRender подтвердил регистрацию слушателя; интерфейс мира не запускался.

## Уточнение TASK-0003.027

2026-09-11, `rusbar-main`, `ce0c7eb7069b215b641d725913b3aae21502e811`. Современный weapon partial читает именно weapon.system.type.text, а не преобразует type в строку; реальный WeaponData с text=Sword вывел Sword. Флаги slashing/piercing/bludgeoning/elemental этого поля непосредственно в таблице не читаются.

Связанные шаблоны: [templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs](../../../../../../../../templates/sheets/actor/partials/character/inventory/tab-inventory-weapons.hbs). [Проверки и ограничения](../../../../../review-log.md#task-0003027). Полный разбор соседей вне этой порции не засчитывается.
