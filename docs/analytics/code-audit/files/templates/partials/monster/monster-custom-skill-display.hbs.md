# templates/partials/monster/monster-custom-skill-display.hbs

| Поле | Значение |
| --- | --- |
| Исходный файл | [templates/partials/monster/monster-custom-skill-display.hbs](../../../../../../../templates/partials/monster/monster-custom-skill-display.hbs) |
| Тип файла | Handlebars |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `273a6d7db0b7c866399db3ecd4f7191817ae6f10` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.029](../../../../../../tasks/task-0003.029.md), 14 файлов, 763 логических строк |
| Запись перекрёстной сверки | [TASK-0003.029](../../../../review-log.md#task-0003029) |

## Назначение файла

Старая строка embedded Item-навыка монстра с правильным Item ID, броском, редактированием value, раскрытием и удалением.

## Условия использования

Получает Item напрямую от monster-skill-tab. Основные поля находятся в system, имя/id — в документе. Старый родитель не выбран текущим V2 листом; работа HBS и обработчиков проверена отдельно от его актуальной доступности.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| tbody.skill.item | Строка 1 | Контейнер embedded Item | data-item-id={{id}} | Источник ID для трёх custom-действий и inline-edit |
| td#custom-rollable | Строки 3–15 | Цель собственного броска | profession/pickup → без класса; иначе learned → learned-skilled; иначе not-skilled | Ровно одна ветвь создаёт td |
| inline-edit / раскрытие / удаление | Строки 16–29 | Изменение Item.value, toggle isOpened и delete | data-field=system.value, custom-skill-modifier-display, remove-custom-skill | Все операции выполняют листовые примеси |
| activeEffectModifiers | Строки 31–43 | Только просмотр бонуса | Два disabled input при isOpened и ненулевом значении | Нет CRUD массива modifiers |

## Основные функции и методы

Собственных JS-функций нет. if/or/unless выбирают класс броска, name показывается как имя Item. Значение редактируется через inline-edit value, а не имя поля Actor. isOpened меняет направление шеврона; true и truthy activeEffectModifiers показывают строку с WITCHER.activeEffect.tab и числом. Ноль скрыт, отрицательное число показывается.

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| SkillItemData | [module/data/item/skillItemData.js](../../../../../../../module/data/item/skillItemData.js) | Модель Item | value/isOpened/activeEffectModifiers/isProfession/isPickup/isLearned | Все чтения system |
| Item-контекст | [templates/partials/monster/monster-skill-tab.hbs](../../../../../../../templates/partials/monster/monster-skill-tab.hbs) | Буквальный partial producer | customSkills.<stat> перебирает Items | Семь вызовов без hash |
| customSkillMixin | [module/actor/sheets/mixins/customSkillMixin.js](../../../../../../../module/actor/sheets/mixins/customSkillMixin.js) | DOM-события | customSkillListener связывает бросок, removeCustomSkill и customSkillModifierDisplay | Селекторы совпадают; add/edit/delete массива отсутствуют |
| rollCustomSkillCheck | [module/actor/mixins/skillMixin.js](../../../../../../../module/actor/mixins/skillMixin.js) | Метод Actor | Событие #custom-rollable и closest('.item') | Находит embedded Item по ID |
| _onItemInlineEdit | [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | DOM-событие | data-field=system.value → Item.update с element.value | inline-edit обработчик; числовое преобразование делает модель |
| or / localize / preload | [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Системные/core helper и регистрация | Классы и подпись эффекта | Определения helper и буквальный preload |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [templates/partials/monster/monster-skill-tab.hbs](../../../../../../../templates/partials/monster/monster-skill-tab.hbs) | Весь HBS | Семь вызовов для customSkills групп | Буквальные ссылки |
| [module/setup/handlebars.js](../../../../../../../module/setup/handlebars.js) | Весь HBS | Предзагрузка | Буквальная ссылка |
| [module/actor/sheets/mixins/customSkillMixin.js](../../../../../../../module/actor/sheets/mixins/customSkillMixin.js) | ID и классы событий | Привязка трёх действий | customSkillListener |
| [module/actor/sheets/mixins/itemMixin.js](../../../../../../../module/actor/sheets/mixins/itemMixin.js) | inline-edit.value | Привязка числового редактирования Item | itemListener |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Изменения идут в embedded Item, не system.skills Actor. Обработчик inline-edit передаёт строковое input.value, NumberField модели приводит допустимую строку к числу. activeEffectModifiers выводится read-only; сам собственный бросок это поле не использует. Полей списка modifiers и ID его строк здесь нет.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Весь HBS и обработчики | 44 строки; schema; customSkillListener; _onItemInlineEdit | Контракт Item ID согласован; три custom-действия и один inline-edit | Старый маршрут |
| Настоящий Handlebars | Комбинации трёх флагов, isOpened, 0/отрицательного activeEffectModifiers | Корректные класс, ID, имя/значение; 0 скрыт; отрицательный бонус показан | Не подключался браузер |
| Числовой ввод | Настоящий _onItemInlineEdit и настоящая SkillItemData | Payload system.value='-2.5'; модель принимает −2.5 | Запись Item подменена; границы value схема не задаёт |

## Непроверенные участки и открытые вопросы

Повторяющийся id custom-rollable описан как буквальный контракт; поведение селектора jQuery с несколькими подключёнными к документу строками не проверено. CRUD старого массива проверен отдельно как вызываемый код без текущих кнопок.

## Связанные проблемы

[issue-00189](../../../../../../issues/potential/issue-00189.md), [issue-00190](../../../../../../issues/potential/issue-00190.md). Рассогласование списка модификаторов и игнорирование отображаемого бонуса относятся к соответствующим potential issues.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `273a6d7db0b7c866399db3ecd4f7191817ae6f10`; полный файл | Первая карточка; [сверка порции](../../../../review-log.md#task-0003029) |
