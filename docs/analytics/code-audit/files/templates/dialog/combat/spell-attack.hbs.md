# templates/dialog/combat/spell-attack.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/dialog/combat/spell-attack.hbs](../../../../../../../templates/dialog/combat/spell-attack.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `c598d74e34f4be51535de78b38f0601c286c5407` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.039](../../../../../../tasks/task-0003.039.md), 6 файлов, 870 логических строк |
| Запись перекрёстной сверки | [TASK-0003.039](../../../../review-log.md#task-0003039) |

## Назначение файла

Тело модального окна сотворения магии: необязательная локация, признак дополнительной атаки, переменная STA, основной/второй фокус и пользовательский модификатор.

## Условия использования

Только castSpellMixin.castSpell вызывает renderTemplate этого пути, затем DialogV2.prompt с rejectClose:true. Контекст causeDamage (единственное число), staminaIsVar, useFocus, focusOptions собирается из Item/Actor. Заголовок/OK принадлежат DialogV2, HBS задаёт только содержание.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| location | select:5–15 при causeDamage | Девять вариантов попадания | name=location | randomHuman/randomMonster/head/torso/leftArm/rightArm/leftLeg/rightLeg/tailWing |
| isExtraAttack | checkbox:19 всегда | Дополнительная атака | name=isExtraAttack | callback читает checked |
| staCost | input:21 при staminaIsVar | Исходная переменная стоимость | name=staCost, value=1 | type/min/max/step/required отсутствуют |
| focus / secondFocus | select:25,30 при useFocus | Значения фокусов | selectOptions focusOptions; у secondFocus blank='' | Основной выбирает первый вариант, второй пустой |
| customMod | input:35 всегда | Пользовательская поправка | name=customMod, value=0 | Тип text по умолчанию; callback возвращает строку |

## Основные функции и методы

JavaScript отсутствует. if включает условные поля, localize выводит подписи, core selectOptions превращает словарь {focus1:{value,label},…} в option. Встроенный value объекта сохраняет числовое значение фокуса; ключ focus1 не становится отправляемой ценой.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| castSpellMixin.castSpell | [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | Источник контекста / callback | data:81–86, чтение формы:99–107 | staCost?.value fallback на stamina; focus/secondFocus отсутствуют→0; location?.value; customMod.value и extra.checked |
| focus schema / common Actor | [module/data/actor/templates/common/focusData.js](../../../../../../../module/data/actor/templates/common/focusData.js); [module/data/actor/commonActorData.js](../../../../../../../module/data/actor/commonActorData.js) | Источник значений | Четыре положительных focus.value | Имена и значения в label |
| SpellData/RitualData | [module/data/item/spellData.js](../../../../../../../module/data/item/spellData.js); [module/data/item/ritualData.js](../../../../../../../module/data/item/ritualData.js) | Флаги / стоимость | staminaIsVar; causeDamages только spell | Hex не имеет этих флагов |
| Handlebars selectOptions / DialogV2 | Foundry 14.367: client/applications/handlebars.mjs:460–499; DialogV2 | Внешние API | Получение option и prompt | Настоящий helper; createSelectInput/DOM фасад, окна не запускались |
| Локализация | [lang/en.json](../../../../../../../lang/en.json); [lang/ru.json](../../../../../../../lang/ru.json) | localize | WITCHER.Dialog.*, WITCHER.Spell.*, WITCHER.Actor.DerStat.Focus | Единственный literal ru-пропуск в порции: customModifier → английский fallback |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | Диалог spell-attack | renderTemplate:88–91 | Шесть ожидаемых имён формы |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

От двух до шести именованных полей: location, isExtraAttack, staCost, focus, secondFocus, customMod. Основной focus не имеет пустого выбора; оба селекта предлагают одинаковый словарь, поэтому не исключают повтор одного значения. Включение второго фокуса не связано с отдельной способностью в этом коде; допустимость по книге не утверждалась.

После OK castSpell вычисляет стоимость и бросок. HBS не проверяет конечность/положительность STA, доступный запас, корректность формулы customMod или бюджет vigor. Отмена с rejectClose:true прерывает до update. Фокус уменьшает оплату, исходный staCost остаётся множителем; extra прибавляет 3 STA и вычитает 3 из броска.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Поля по флагам | Группа 06 | Минимум extra/customMod; максимум 6; реальные option value=2, второй пустой | parse5 и фасад HTMLForm.elements |
| Отмена/стоимость | Группы 07–12 | Недостаток отменяет расход; минимум 1; NaN не отвергнут; дробная сила обрезается parseInt | Записи Actor заменены |

## Непроверенные участки и открытые вопросы

Файлы порции прочитаны целиком. Проверка: Foundry 14.367.0, Node 24.16.0, реальные модели/методы, Roll/extendedRoll, Handlebars 4.7.9, expandObject и core Localization с fallback. Диалог, Application/DOM, вывод Roll.toAnchor, запись Actor/Item/ChatMessage, UUID resolver, создание/clone ActiveEffect, canvas и query заменены фасадами. Реальные браузер, HTTP, БД, компедиумы, сетевые клиенты и жизненный цикл эффекта не запускались. Текстовые формулы проверены как поведение кода, без выбора правил книг.

## Связанные проблемы

[issue-00186](../../../../../../issues/potential/issue-00186.md), [issue-00245](../../../../../../issues/potential/issue-00245.md), [issue-00246](../../../../../../issues/potential/issue-00246.md). Проверяется контракт формы с существующим castSpell, изменения значений по игровым правилам не выбирались.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `c598d74e34f4be51535de78b38f0601c286c5407`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003039) |
