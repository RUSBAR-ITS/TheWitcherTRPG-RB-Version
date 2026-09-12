# module/item/mixins/defenseOptionMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/item/mixins/defenseOptionMixin.js](../../../../../../../module/item/mixins/defenseOptionMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 16695cbfc7fec3e0de56660c7cab21bc0304e94b |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.042](../../../../../../tasks/task-0003.042.md), 5 файлов / 477 логических строк; данный файл — 9 |
| Запись перекрёстной сверки | [TASK-0003.042](../../../../review-log.md#task-0003042) |

## Назначение файла

Обёртка Item: создаёт вариант защиты с именем предмета и дополнениями от модели system.

## Условия использования

[module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) импортирует defenseOptionMixin и присоединяет через Object.assign к прототипу. При импорте создаётся только объект. Вызывает [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js):20 после отбора system.isApplicableDefense?.(attack.attackOption).

## Введённые сущности и действия с ними

| Сущность | Место/доступность | Действия |
| --- | --- | --- |
| defenseOptionMixin | export let, 1–9 | Один метод передаётся прототипу Item |
| createDefenseOption | 2–8 | Новый plain object: label=this.name, value=this.name, затем spread результата system.createDefenseOption?.(attack.attackOption) |

## Основные функции и методы

createDefenseOption(attack) — синхронный. attack ожидается объектом с attackOption; читает Item.name/system, не пишет документы. Модельный результат имеет приоритет над label/value. Если метода модели нет либо он возвращает undefined, spread ничего не добавляет и остаются два поля имени. Отсутствующий attack проверкой не защищён.

Wrapper не создаёт уникальный action, не задаёт itemId и не проверяет isApplicableDefense. Условия отбора находятся у Actor. WeaponData возвращает skills/modifier/itemTypes, ProfessionData дополнительно заменяет имя на skillName и добавляет skillOverride. ArmorData метода не имеет: прямой wrapper вернул бы только имя, но обычный отбор её не включает.

## Используемые сущности и зависимости

| Сущность | Источник | Вид / доказательство |
| --- | --- | --- |
| Item.name/system | Foundry Item / [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Контекст метода; доступность через prototype |
| createDefenseOption(attackOption) | [module/data/item/weaponData.js](../../../../../../../module/data/item/weaponData.js) | skills по цепочке навыков и свойства защиты |
| createDefenseOption(attackOption) | [module/data/item/professionData.js](../../../../../../../module/data/item/professionData.js) | Первый подходящий навык пути; label/value/skillOverride |
| DefenseProperties.createDefenseOption | [module/data/item/templates/combat/defensePropertiesData.js](../../../../../../../module/data/item/templates/combat/defensePropertiesData.js) | Косвенный helper: modifier и пустые skills/itemTypes |
| attack.attackOption | [module/data/chatMessage/templates/attackData.js](../../../../../../../module/data/chatMessage/templates/attackData.js), [module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) | Модель/производитель атаки; извлечение свойства на входе |

Прямых import в файле нет; обращения к другим файлам динамические через модель Item.

## Известные потребители

[module/item/witcherItem.js](../../../../../../../module/item/witcherItem.js) подключает примесь; [module/actor/mixins/defenseMixin.js](../../../../../../../module/actor/mixins/defenseMixin.js) создаёт дополнительные способы, а затем использует option.value как Dialog action. Поиск по module не нашёл иных прямых вызовов этого wrapper; одноимённые методы моделей — определения другой ступени.

## Данные и изменения состояния

Возвращается новый внешний объект; вложенные поля результата модели не клонируются. Собственного состояния, расходов, асинхронных действий и Hooks нет. Одинаковые имена Item могут дать одинаковые value, что важно для свёртки кнопок DialogV2.

## Проверки и доказательства

Прочитаны 9 строк. [Группы 04–07/11](../../../../review-log.md#task-0003042) вызвали настоящий wrapper на фасадах Item с настоящими WeaponData/ProfessionData/ArmorData. У модели профессии label/value изменились на Guard, отключённый isDefense не помешал отбору; ArmorData отсеяна раньше wrapper. Два оружия Same дали один Dialog action с последним modifier=4. Отсутствующий метод и порядок spread установлены чтением тела, не отдельным динамическим тестом прямого Armor wrapper.

## Непроверенные участки и открытые вопросы

Файл прочитан полностью. Настоящий Item lifecycle/внешние пользовательские модели/мир не запускались. Полный разбор моделей выполнен прежде; здесь повторно проверены только связи.

## Связанные проблемы

[docs/issues/potential/issue-00268.md](../../../../../../issues/potential/issue-00268.md) — одинаковые value; [docs/issues/potential/issue-00071.md](../../../../../../issues/potential/issue-00071.md)/[docs/issues/potential/issue-00072.md](../../../../../../issues/potential/issue-00072.md) — отбор профессии; [docs/issues/potential/issue-00079.md](../../../../../../issues/potential/issue-00079.md) — пустой skill; [docs/issues/potential/issue-00085.md](../../../../../../issues/potential/issue-00085.md) — отсутствие контрактов ArmorData.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 16695cbfc7fec3e0de56660c7cab21bc0304e94b; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003042) |
