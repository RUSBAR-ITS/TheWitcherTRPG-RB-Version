# module/actor/mixins/locationMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/locationMixin.js](../../../../../../../module/actor/mixins/locationMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 929ac4c6d90509ce06ef0795be380925e8b59e69 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.043](../../../../../../tasks/task-0003.043.md), 3 файла / 320 логических строк; данный файл — 11 |
| Запись перекрёстной сверки | [TASK-0003.043](../../../../review-log.md#task-0003043) |

## Назначение файла

Два метода экземпляра Actor, делегирующие перечисление и описание локаций статическим методам WitcherActor.

## Условия использования

Прямой import WitcherActor из [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js). Обратный import и Object.assign:447 присоединяют locationMixin к прототипу Actor. Возникает цикл модулей, но обращение к статическим методам находится внутри вызываемых функций; сам import не запускает перечисление локаций.

## Введённые сущности и действия с ними

| Сущность | Место | Назначение и доступность |
| --- | --- | --- |
| WitcherActor | import, 1 | Ссылка на класс; локальная зависимость |
| locationMixin | export let, 3–11 | Объект двух методов для прототипа |
| getAllLocations | 4–6 | Перечисление через класс |
| getLocationObject | 8–10 | Объект одной локации через класс |

## Основные функции и методы

| Метод | Входы | Действие / результат | Состояние и ошибки |
| --- | --- | --- | --- |
| getAllLocations() | Аргументов нет | return WitcherActor.getAllLocations() | this экземпляра не передаётся; новый массив выдаёт static |
| getLocationObject(location) | Строка имени или randomHuman/randomMonster | return WitcherActor.getLocationObject(location) | Аргумент проходит неизменным; объект/случайность создаёт static |

Собственных таблиц, CONFIG, валидации, асинхронности, Hooks и записи здесь нет. Внешние аргументы getAllLocations также не передаются.

## Используемые сущности и зависимости

| Сущность | Источник | Вид и назначение | Доказательство |
| --- | --- | --- | --- |
| WitcherActor.getAllLocations | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js):292–300 | Прямой вызов | static читает this.type и this.system.hasTailWing |
| WitcherActor.getLocationObject | [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js):302–435 | Прямой вызов с location | Таблица коэффициентов, модификаторов и random находится в Actor |
| hasTailWing | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js):62 | Косвенный вход перечисления | В обёртке контекст теряется; реальная модель использована в 24/26 |
| getRandomInt / i18n | [module/scripts/helper.js](../../../../../../../module/scripts/helper.js), Foundry | Косвенные зависимости static | В опытах фиксированы результат RNG=10 и localize=k |
| Ключи WITCHER.Armor/Location/Dialog.attackTail | [lang/en.json](../../../../../../../lang/en.json), [lang/ru.json](../../../../../../../lang/ru.json) | Косвенные подписи объектов | Штатный перевод и fallback в этой порции не запускались |

CONFIG не является источником таблиц этих двух static: они прописаны в WitcherActor. Не следует приписывать их определение примеси.

## Известные потребители

| Файл | Метод / действие |
| --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Подключение примеси |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | applyDamageToAllLocations вызывает оба; критический урон использует torso |
| [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) | handleCritLocation получает объекты частей |
| [module/actor/mixins/weaponAttackMixin.js](../../../../../../../module/actor/mixins/weaponAttackMixin.js), [module/actor/mixins/professionMixin.js](../../../../../../../module/actor/mixins/professionMixin.js), [module/actor/mixins/castSpellMixin.js](../../../../../../../module/actor/mixins/castSpellMixin.js) | Обработка выбранной локации атаки/заклинания |
| [module/scripts/combat/applyDamage.js](../../../../../../../module/scripts/combat/applyDamage.js) | Выбор новой локации урона |
| [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) | Урон состояния по torso |
| [module/item/mixins/damageUtilMixin.js](../../../../../../../module/item/mixins/damageUtilMixin.js) | Соседний путь: прямой static WitcherActor.getLocationObject, минуя эту обёртку |

Поиск выполнен по module/templates; внешние макросы не проверены. Таблица различает вызовы примеси и одноимённый прямой static.

## Данные и изменения состояния

getAllLocations возвращает head, torso, rightArm, leftArm, rightLeg, leftLeg. Static добавил бы tailWing при this=monster с hasTailWing, но штатный wrapper вызывает его с this=класс. Группа 24: wrapper 6, явный static.call(actor) 7, флаг false даёт 6. Отдельный getLocationObject('tailWing') работает и от флага не зависит.

| Локация | formula | modifier |
| --- | --- | --- |
| head | 3 | '-6' |
| torso | 1 | '-1' |
| rightArm / leftArm | 0.5 | '-3' |
| rightLeg / leftLeg | 0.5 | '-2' |
| tailWing | 0.5 | '+0' |

Это данные static. randomHuman/randomMonster используют d10-таблицы в Actor; при фиксированном 10 возвращают leftLeg/tailWing. Неизвестная строка сохраняется в name, хотя formula/alias получают значения торса. Последующий getLocationArmor('unknown') поэтому не находит ветку и падает; валидность всех внешних вводов не установлена.

Группа 26 исполнила настоящий applyDamageToAllLocations с подменённым расчётом каждой зоны: в расчёт вошли только шесть имён, сумма была 6. Это подтверждает достижение consumer, но не расчёт реального урона/HP по всем локациям.

## Проверки и доказательства

Прочитаны 11 строк. [Группы 24–26](../../../../review-log.md#task-0003043) исполнили исходную примесь в vm с заменой импортированного класса классом, содержащим неизменённые два static. Использованы настоящая MonsterData, фиксированный RNG и фасады записи/шаблона. Семь прицельных объектов проверены полностью; обе random-ветки проверены на исходе 10.

## Непроверенные участки и открытые вопросы

Файл прочитан целиком. Полный WitcherActor и его регистрация в Foundry не исполнялись; циклический import проверен чтением, не загрузкой всего приложения. Браузер, распределение случайных результатов, полный урон, HP и запись не проверены. Неизвестная локация описана как граница входного контракта.

## Связанные проблемы

[issue-00032](../../../../../../issues/potential/issue-00032.md) уточнена проверкой consumer. Отдельные корректные объекты tailWing не отменяют ошибку перечисления. Новых самостоятельных issues для этого файла не зарегистрировано.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 929ac4c6d90509ce06ef0795be380925e8b59e69; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003043) |
