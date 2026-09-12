# templates/dialog/combat/weapon-attack.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/dialog/combat/weapon-attack.hbs](../../../../../../../templates/dialog/combat/weapon-attack.hbs) |
| Тип файла | Handlebars / HTML |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3 |
| Изменения относительно коммита | Нет; исходник совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.041](../../../../../../tasks/task-0003.041.md), четыре файла / 687 логических строк; данный файл — 270 |
| Запись перекрёстной сверки | [TASK-0003.041](../../../../review-log.md#task-0003041) |

## Назначение файла

Полная форма выбора параметров оружейной атаки: тип повреждения, дальность, локация, удар, позиционные модификаторы, ручные добавки и боеприпас.
## Условия использования

Единственный найденный renderTemplate — weaponAttack в [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js), путь systems/TheWitcherTRPG/templates/dialog/combat/weapon-attack.hbs. HTML передаётся в DialogV2.prompt; внешний Dialog предоставляет form, кнопку подтверждения и закрытие. Сам шаблон не объявляет form, submit, script, обработчики или partial.

## Введённые сущности и действия с ними

| Узел/область | Строки | Назначение и состояние |
| --- | --- | --- |
| div.weapon_roll_sheet, h1 | 1–2 | Корень оформления и локализованный alias навыка |
| div.flex.attack-sheet и две таблицы | 3–84 | extra, damageType, условная range; location и strike |
| details с таблицами модификаторов | 87–198 | Сворачиваемые позиционные флаги и customAim; чекбоксы изначально не отмечены |
| h2.flex, img.item-img | 199–203 | Изображение, имя и displayDmgFormula; обычное HTML-экранирование Handlebars |
| Нижние таблицы | 204–268 | customAtt/customDmg, условные meleeBonus/ammo/throwable |
| option в ammunition | 250 | Тройная вставка ammunitionOption; строка генерируется JS без экранирования имени |

Вводимых JS-функций, моделей и обработчиков нет. Сущности файла — именованные поля и условные области разметки.

## Основные способы использования и поля

| name | HTML-тип / варианты | Условие, default | Использование callback |
| --- | --- | --- | --- |
| isExtraAttack | checkbox | Всегда; false | STA−3 и атака−3 |
| damageType | select | slashing/piercing/bludgeoning/elemental по item.system.type; дополнительный unavailable | damage.type |
| range | select | Только truthy item.system.range; none, pointBlank, close, medium, long, extreme | Модификатор дальности; если секции нет, callback даёт null |
| location | select | randomHuman, randomMonster, head, torso, leftArm, rightArm, leftLeg, rightLeg, tailWing | По умолчанию первый option; расчёт location и originalLocation |
| strike | select | selectOptions config.weapon.attacks, localize=true | normal, fast, strong, joint, half; число ударов/штраф/тип урона |
| outsideLOS / isAmbush / isPinned / isSilhouetted | checkbox | false | +3 / +5 / +4 / +2 |
| targetOutsideLOS / isActivelyDodging / isMoving | checkbox | false | −3 / −2 / −3 |
| isProne / isBlinded / isRicochet / isFastDraw | checkbox | false | −2 / −3 / −5 / −3 |
| customAim | number | 0 | Положительное значение прибавляется; отрицательное игнорируется |
| customAtt | number | 0 | Строка добавки к атаке, кроме '0' |
| customDmg | text | 0; inline width:auto; max-width:50% | Текст формулы добавки к урону |
| ammunition | select | usingAmmo && noAmmo !== 1; первый option | ID → Actor.items.get, quantity−1, effects |

Всего 20 уникальных name при наличии обеих условных секций; без range/ammunition — 18. Шаблон не задаёт min/max/required или взаимоисключение флагов; number не означает, что callback получает Number: .value остаётся строкой.

### Условия отображения

Четыре нормальных damageType независимы. Выражение unavailable на строке 31 вызывает eq с одним аргументом для elemental/bludgeoning и повторяет elemental; единственное двухаргументное сравнение — eq false item.system.type.piercing. В системном eq второй параметр при одноаргументном вызове становится служебным объектом Handlebars, поэтому эти сравнения false. Проверка всех 16 наборов bool дала unavailable ровно при piercing=false, в том числе вместе со slashing/bludgeoning/elemental. Его default-выбор при других нормальных типах не установлен: они стоят раньше.

meleeBonus выводится по truthy контекста; 0 скрыт, отрицательные видимы. usingAmmo с noAmmo=1 выводит error-display; иначе select с сырым HTML. isThrowable показывает NoThrowable либо Throwable в зависимости от noThrowable. Эти надписи сами не блокируют подтверждение.

location/strike не фильтруются по типу цели, hasTailWing, режиму оружия или навыку. Это описание доступности UI, не утверждение о допустимости каждого сочетания по правилам.

## Используемые сущности и зависимости

| Сущность | Файл/API | Вид и цель | Доказательство |
| --- | --- | --- | --- |
| Девять ключей контекста | [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | data → renderTemplate | item, attackSkill, displayDmgFormula, noAmmo, noThrowable, ammunitionOption, ammunitions, meleeBonus, config; ammunitions как массив напрямую не используется |
| Item.system.type | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js), [module/data/item/templates/weaponTypeData.js](../../../../../../../module/data/item/templates/weaponTypeData.js) | Bool slashing/piercing/bludgeoning/elemental | Условия option, 19–33 |
| range/usingAmmo/isThrowable | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js) | Условные секции | Входы подготовленного Item; noThrowable вычислен через isEnoughThrowable |
| config.weapon.attacks | [module/setup/config.js](../../../../../../../module/setup/config.js) | selectOptions | Таблица label, attackNumber, attackPenality, dmgMulti |
| eq / or | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные helpers | eq строгое равенство; or отбрасывает последний служебный аргумент |
| if / localize / selectOptions | Handlebars / Foundry 14.367.0 | Ветви и подписи | Нативный if, исходные eq/or исполнены. localize/selectOptions в опытах — явные фасады |
| WITCHER.Dialog.*, DamageType.*, Context.unavailable | [lang/en.json](../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../lang/ru.json), Foundry Localization | Подписи полей | В тесте возвращались ключи; настоящая локализация/expandObject/fallback не прогонялись, отсутствие перевода не заявляется |
| weapon_roll_sheet | [styles/weapon-roll.css](../../../../../../../styles/weapon-roll.css) | 4 scoped CSS-правила | Поля, td, select, label |
| attack-sheet; h2 img | [styles/attack-sheet.css](../../../../../../../styles/attack-sheet.css) | 4 CSS-правила | Таблицы, td, select и глобальные отступы изображения |
| flex / item-img / error-display | [styles/system-styles.css](../../../../../../../styles/system-styles.css) | Общие классы | display:flex; размер изображения 40px; красный текст; подключены через witcher-styles.css |
| DialogV2.prompt callback | [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) | Обратная связь по form.elements | 104–130: 12 .checked и 8 .value/условных значений |

## Известные потребители

[module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js) — единственный найденный прямой путь загрузки. [styles/weapon-roll.css](../../../../../../../styles/weapon-roll.css) и [styles/attack-sheet.css](../../../../../../../styles/attack-sheet.css) используют классы/элементы этой разметки. Профессиональный диалог — отдельный шаблон, хотя делит attack-sheet. Поиск по module/templates/styles выполнен; внешние макросы/модули вне этой области.

## Данные и изменения состояния

Сам шаблон формирует HTML, не пишет Item/Actor. Все изменения данных происходят после callback. Обычные {{item.name}}, img/title и displayDmgFormula экранируются; {{{ammunitionOption}}} сохраняет структуру строки. Имя ammo 'Arrow</option><option value="FAKE">Inserted' после настоящего Handlebars + parse5 добавило второй option FAKE. Исполнение script/XSS и прохождение sanitization Foundry этим не доказаны.

## Проверки и доказательства

Прочитаны все 270 строк. В группах 23–25 [docs/analytics/code-audit/review-log.md](../../../../review-log.md#task-0003041) выполнены 16 комбинаций типов, оба пути ammo, условная range, контроль 20 имён, 9/5/6 вариантов location/strike/range, raw option. В группах 1–22 именно callback исходного weaponAttack читал элементы, восстановленные из HTML parse5; DOM/form — фасад. В группе 28 сверены классы и inline.

## Непроверенные участки и открытые вопросы

Непрочитанной разметки нет. Браузерная вёрстка, штатный selectOptions (v14 создаёт select через createSelectInput), локализованные тексты, form validation, очистка HTML ядром и сохранение выборов не запускались. Фасад selectOptions сохранял ключи/порядок config, но не доказывает все детали штатного helper.

## Связанные проблемы

[docs/issues/potential/issue-00265.md](../../../../../../issues/potential/issue-00265.md) — unavailable; [docs/issues/potential/issue-00266.md](../../../../../../issues/potential/issue-00266.md) — сырые имена ammo; [docs/issues/potential/issue-00260.md](../../../../../../issues/potential/issue-00260.md) — отсутствие остановки при noAmmo; [docs/issues/potential/issue-00244.md](../../../../../../issues/potential/issue-00244.md) — ложный preview meleeBonus; [docs/issues/potential/issue-00259.md](../../../../../../issues/potential/issue-00259.md) — потребитель customDmg; [docs/issues/potential/issue-00267.md](../../../../../../issues/potential/issue-00267.md) — декларация оформления таблиц.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | d5c7a4b871dce3aa55f4b8b589e62c3c9450f2d3; полный файл | Первичная карточка, определения и потребители сверены; [журнал](../../../../review-log.md#task-0003041) |
