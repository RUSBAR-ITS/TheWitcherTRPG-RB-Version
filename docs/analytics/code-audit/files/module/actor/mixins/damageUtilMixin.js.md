# module/actor/mixins/damageUtilMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/mixins/damageUtilMixin.js](../../../../../../../module/actor/mixins/damageUtilMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 965132d5d7972a0edd73aaa62484a1b6ba15991f |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.044](../../../../../../tasks/task-0003.044.md), 9 файлов / 603 логических строк; данный файл — 17 |
| Запись перекрёстной сверки | [TASK-0003.044](../../../../review-log.md#task-0003044) |

## Назначение файла

Чтение плоского и множительного модификаторов входящего урона Actor по общему типу атаки.

## Условия использования

Именованный export damageUtilMixin присоединяется к WitcherActor.prototype через Object.assign. Не совпадает с Item-примесью того же имени. Импортов и регистрации событий нет; два метода вызываются расчётом урона/сопротивлений.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| damageUtilMixin | Export object:1–17 | Два getter-подобных метода | Actor.prototype | Только чтение |
| damageMod | Локальная переменная:8 | Запись damageTypeModification[damageObject.type] | getMultiDamageMod | Не изменяется и не создаётся при отсутствии |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| getFlatDamageMod(damage):3–5 | this.system.damageTypeModification; damage.type | flat либо 0 | Индексирует общий type и читает ?.flat??0 | Синхронно; нет проверки существования самого словаря |
| getMultiDamageMod(damageObject):7–16 | Тот же словарь; damageObject.type | multiplication либо 1; при applyAP и AP также 1 | Читает applyAP, затем damageObject.damageProperties.armorPiercing/improvedArmorPiercing | Штатный контейнер называется properties, поэтому applyAP=true способен бросить TypeError |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| damageTypeModification | [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](../../../../../../../module/data/actor/templates/character/general/damage/damageTypeModificationData.js) | this.system | Общий словарь типов | Factory ключей |
| flat/multiplication/applyAP | [module/data/actor/templates/character/general/damage/damageModificationData.js](../../../../../../../module/data/actor/templates/character/general/damage/damageModificationData.js) | Поля записи | Обе функции | Нет min для flat, multiplication initial1 |
| Мастер модификаторов | [module/activeEffect/mixins/baseMixin.js](../../../../../../../module/activeEffect/mixins/baseMixin.js) | Producer путей | getDamageModifcators формирует ключи эффектов | Не вызывается этим файлом |
| damage.properties | [module/item/mixins/damageUtilMixin.js](../../../../../../../module/item/mixins/damageUtilMixin.js); [module/data/chatMessage/templates/damageData.js](../../../../../../../module/data/chatMessage/templates/damageData.js) | Контракт входа | Источник ошибочного несовпадения имени | createBaseDamageObject и SchemaField сообщения |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | damageUtilMixin | import/Object.assign | Методы Actor |
| [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | getFlatDamageMod | После SP/раннего выхода | Добавляет только положительный flat отдельным экземпляром |
| [module/actor/mixins/armorMixin.js](../../../../../../../module/actor/mixins/armorMixin.js) | getMultiDamageMod | calculateArmorResistances, после early return AP | Множитель используется только внутри сопротивления носимой/Natural брони |

Поиск module/ и templates/. Не устанавливает самостоятельный модификатор каждого экземпляра: используется общий damage.type, даже если instance.type отличается.

## Данные и изменения состояния

Только чтение. Знак flat и положение его применения определяет caller. AP/improvedAP в armorMixin возвращают instance раньше этого helper, поэтому замена имени поля сама по себе не определит требуемую механику applyAP. Nullish fallback сохраняет нулевой коэффициент.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Положительный/отрицательный flat | Группа 23, реальные методы/модель properties |10 + flat−3/0/+3→[10]/[10]/[10,3] | Условие знака находится в caller |
| multiply/AP | Группа 24 и сверка .043 | Коэффициент 3 без брони не применяется; applyAP=true выбрасывает ошибку пути; AP обходит helper | Игровая семантика коэффициента не утверждается |

## Непроверенные участки и открытые вопросы

Полностью прочитан файл; прямой UI-мастер и создание нового эффекта здесь не запускались. Соответствие правилу отрицательных бонусов/бронебойности требует отдельного решения.

## Связанные проблемы

[00025](../../../../../../issues/potential/issue-00025.md) путь свойств; [00026](../../../../../../issues/potential/issue-00026.md) кратность множителя; [00027](../../../../../../issues/potential/issue-00027.md) отрицательный flat; [00286](../../../../../../issues/potential/issue-00286.md) положительный flat не получает тип у caller.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 965132d5d7972a0edd73aaa62484a1b6ba15991f; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003044) |
