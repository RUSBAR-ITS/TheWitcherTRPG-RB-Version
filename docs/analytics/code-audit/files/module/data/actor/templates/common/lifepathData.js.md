# module/data/actor/templates/common/lifepathData.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/data/actor/templates/common/lifepathData.js](../../../../../../../../../module/data/actor/templates/common/lifepathData.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-10 |
| Ветка и коммит | `rusbar-main`, `c34b790379fd98cd7e33ccbeeca085e49297a40f` |
| Изменения относительно коммита | Нет; содержимое также совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.003](../../../../../../../../tasks/task-0003.003.md), одна порция из восьми файлов |
| Запись перекрёстной сверки | [TASK-0003.003](../../../../../../review-log.md#task-0003003) |

## Назначение файла

Определяет числовые модификаторы, объединённые в system.lifepathModifiers. Это технические поля бонусов к защите, броне, магии и типам удара; биографические записи персонажа находятся в других файлах.

## Условия использования

Default export lifepathData импортирован [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js):8 и вызван в SchemaField lifepathModifiers:59. Наследуется CharacterData/MonsterData; файл требует foundry.data.fields при импорте.

## Введённые сущности и действия с ними

| Поле | Тип и начало | Потребляемый смысл |
| --- | --- | --- |
| shieldParryBonus | NumberField, 0 | Бонус парирования щитом: defenseMixin.handleLifepathModifier. |
| shieldParryThrownBonus | NumberField, 0 | Бонус парирования метательных атак щитом; потребитель сравнивает action с 'parrythrown'. |
| ignoredArmorEncumbrance | NumberField, 0 | Вычитается из общей encumb надетой брони; getArmorEcumbrance ограничивает результат снизу 0. |
| ignoredEvWhenCasting | NumberField, 0 | При положительной итоговой броневой нагрузке castSpell добавляет это значение к формуле, если оно >0. |
| attacks | TypedObjectField(SchemaField), {} | Словарь произвольных ключей типов удара. |
| attacks.<ключ>.value | NumberField, 0 | Число внутри записи; strong и joint не объявлены отдельными полями схемы. |

Локальный fields — ссылка на API, lifepathData() — экспортируемая фабрика. min/max/integer у чисел не заданы; допустимые ключи attacks не ограничены перечислением.

## Основные функции и методы

lifepathData():3–15 без аргументов создаёт пять полей верхнего уровня. Вложенная запись attacks содержит только value. Миграции, применение эффектов, расчёт атаки и запись Actor здесь отсутствуют.

## Используемые сущности и зависимости

| Сущность | Определение | Связь и место |
| --- | --- | --- |
| NumberField, TypedObjectField, SchemaField | Foundry 14.367.0: /opt/foundryvtt/common/data/fields.mjs | fields:1; поля:5–12. Словарь хранит объекты с числом, не числа непосредственно. |
| lifepathData | [module/data/actor/commonActorData.js](../../../../../../../../../module/data/actor/commonActorData.js) | Внешний вызов в defineSchema:59; хранение под lifepathModifiers. |
| WITCHER.weapon.attacks | [module/setup/config.js](../../../../../../../../../module/setup/config.js) | Внешние имена ударов, используемые потребителями; фабрика config не читает. |

## Известные потребители

| Файл | Обращение и условия |
| --- | --- |
| [module/activeEffect/mixins/baseMixin.js](../../../../../../../../../module/activeEffect/mixins/baseMixin.js) | getLifepathSuggestions:87–122 создаёт шесть подсказок. Четыре скалярных пути соответствуют схеме; strong/joint указывают attacks.<ключ> без .value. |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../../../module/actor/mixins/weaponAttackMixin.js) | handleStrikeType:367–381 читает attackPenality выбранного удара из config, затем напрямую вставляет attacks[strike] в формулу. |
| [module/actor/mixins/defenseMixin.js](../../../../../../../../../module/actor/mixins/defenseMixin.js) | handleLifepathModifier:272–290 читает положительные shieldParryBonus/ThrownBonus при additionalTag='armor' и указанных action. |
| [module/actor/mixins/armorMixin.js](../../../../../../../../../module/actor/mixins/armorMixin.js) | getArmorEcumbrance:2–10 начинает сумму с -ignoredArmorEncumbrance, прибавляет encumb надетой брони, возвращает Math.max(sum,0). |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../../../module/actor/mixins/castSpellMixin.js) | :35–47 отдельно читает ignoredEvWhenCasting при armorEnc>0. В этой ветке добавление не ограничивается величиной самого armorEnc. |
| [module/setup/deprecations.js](../../../../../../../../../module/setup/deprecations.js); [templates/dialog/deprecations/lifepathModifiers.hbs](../../../../../../../../../templates/dialog/deprecations/lifepathModifiers.hbs) | Текст уведомления рекомендует задавать модификаторы эффектами; это не миграция значений и не обработчик формулы. |

Поиск выполнен в module/templates и строковых путях 226 packsJson. Ссылок system.lifepathModifiers в этих JSON не найдено; отсутствие прямой строки не исключает динамическое построение пути.

## Данные и изменения состояния

Сама фабрика только задаёт типы. Мастер эффектов предлагает пути, применение принадлежит Foundry/ActiveEffect, а методы боя читают подготовленный Actor.system. Редактор отдельных биографических записей не является владельцем этой схемы.

Форма данных attacks отличается от двух потребителей: {strong:{value:2}} превращается у handleStrikeType в строку ` -3+[object Object]`. Несогласованность относится к схеме, подсказкам и чтению записи одновременно; выбор будущей формы ещё не согласован.

## Проверки и доказательства

Прочитаны все 15 строк, определение TypedObjectField и реальные потребители. Изолированно создана CommonActorData с strong.value=2 и выполнен настоящий handleStrikeType: получен указанный текст вместо числа. getLifepathSuggestions возвращает два пути без .value.

Для динамических ключей TypedObjectField при поиске поля через SchemaField.getField нужно передать source либо обращаться к element. Первоначальная проверка без source дала undefined; после чтения fields.mjs:2056–2068 проверены элемент SchemaField и его NumberField value. Эта особенность проверки не объявляется ошибкой системы.

## Непроверенные участки и открытые вопросы

Не запускались мастер, сохранение/применение ActiveEffect и полный бросок. Не определялось, какую форму attacks следует выбрать для исправления. Поведение отрицательных бонусов и допустимый объём компенсации брони описаны по ветвлениям; соответствие рулбуку не утверждается.

## Связанные проблемы

[issue-00019](../../../../../../../../issues/potential/issue-00019.md) — схема и потребители attacks используют разные формы значения.

## История актуализации

2026-09-10 — полный разбор файла и сверка определений, потребителей и внешнего API на указанной версии. Результаты приведены в записи TASK-0003.003 журнала. Проверка описания не означает проверки мира или отсутствия ошибок.
