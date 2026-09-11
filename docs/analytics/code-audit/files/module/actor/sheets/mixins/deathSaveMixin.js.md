# module/actor/sheets/mixins/deathSaveMixin.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/actor/sheets/mixins/deathSaveMixin.js](../../../../../../../../module/actor/sheets/mixins/deathSaveMixin.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-11 |
| Ветка и коммит | `rusbar-main`, `aa6af106e86a9c75fe050d599f961c8fadb74f1b` |
| Изменения относительно коммита | Нет; содержимое совпадает со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. |
| Задача и порция | [TASK-0003.030](../../../../../../../tasks/task-0003.030.md), 9 файлов, 424 логических строк |
| Запись перекрёстной сверки | [TASK-0003.030](../../../../../review-log.md#task-0003030) |

## Назначение файла

Примесь листа для ручного счётчика спасбросков смерти и броска с порогом из STUN либо базовых BODY/WILL.

## Условия использования

Export называется deathsaveMixin (строчная s), файл — deathSaveMixin.js. Импортирован/присоединён к V2/V1 базовым ActorSheet; текущие Character и Monster header предоставляют три цели клика.

## Введённые сущности и действия с ними

| Сущность | Вид и место определения | Назначение | Доступность или регистрация | Действия и жизненный цикл |
| --- | --- | --- | --- | --- |
| deathsaveMixin | export let,5–51 | Четыре метода | Object.assign базовых листов | Счётчик и бросок |
| stunBase | 16–24 | Локальный порог | Не сохраняется в Actor | Выбор источника → Math.min(...,10) → вычитание deathSaves |

## Основные функции и методы

| Функция или метод | Входы и предусловия | Результат | Основные действия | Ошибки, асинхронность и изменения состояния |
| --- | --- | --- | --- | --- |
| _removeDeathSaves(event) | Actor.deathSaves | Promise<void> | preventDefault; update system.deathSaves=0 | Это сброс, не −1; update не ожидается/не возвращается |
| _addDeathSaves(event) | Actor.deathSaves | Promise<void> | preventDefault; update deathSaves+1 | Нет целочисленности/пределов; update не ожидается |
| _onDeathSaveRoll(event) | hp.value, stun.value, body.max/will.max, deathSaves | Promise<void> после extendedRoll | HP>0 → stun.value; иначе floor((BODY.max+WILL.max)/2); верхний clamp10, затем −deathSaves; 1d10 reversal=true/showCrit=false/showSuccess=true | Нижней границы нет; отрицательный threshold не сравнивается extendedRoll. Счётчик автоматически не увеличивается; event не используется |
| deathSaveListener(html) | DOM/$ | Три click-подписки | death-roll → бросок; death-minus → сброс; death-plus → +1 | Обёртка html локальна, this привязан к листу |

## Используемые сущности и зависимости

| Используемая сущность | Файл-источник или внешний API | Вид связи | Где и зачем используется | Основание |
| --- | --- | --- | --- | --- |
| ChatMessageData | [module/chatMessage/chatMessageData.js](../../../../../../../../module/chatMessage/chatMessageData.js) | Прямой default import | Actor и HTML подпись WITCHER.DeathSave | 1,26–35 |
| RollConfig | [module/scripts/rollConfig.js](../../../../../../../../module/scripts/rollConfig.js) | Прямой named import | reversal/showSuccess/showCrit/threshold | 2,37–41 |
| extendedRoll | [module/scripts/rolls/extendedRoll.js](../../../../../../../../module/scripts/rolls/extendedRoll.js) | Прямой named import | Настоящий 1d10 и строгий roll<threshold | 3,43; сравнение включается только при threshold>=0 |
| CommonActorData.deathSaves / Stats / DerivedStats | [module/data/actor/commonActorData.js](../../../../../../../../module/data/actor/commonActorData.js); [module/data/actor/templates/common/stats/statsData.js](../../../../../../../../module/data/actor/templates/common/stats/statsData.js); [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js) | Поля схем | deathSaves NumberField0 без min/integer; HP/STUN.value и BODY/WILL.max | 7–24 |
| calculateFixedDerivedStats | [module/actor/witcherActor.js](../../../../../../../../module/actor/witcherActor.js) | Подготовка STUN | Источники stun.value/max и ограничения до этого броска | Локальный Math.min в примеси не является общим clamp всех характеристик |
| Actor.update / $, game.i18n | Foundry 14.367 и браузер; lang/en.json/lang/ru.json | Внешние API | Документные записи, события, подписи | Прямые обращения |

## Известные потребители

| Файл-потребитель | Используемая сущность этого файла | Способ и условия использования | Основание |
| --- | --- | --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../../../../../../module/actor/sheets/WitcherActorSheet.js) | deathsaveMixin | Импорт, Object.assign, deathSaveListener | 1,activateListeners,317 |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../../../../../../module/actor/sheets/WitcherActorSheetV1.js) | deathsaveMixin | Старый базовый лист: аналогичное подключение | 1,activateListeners,297 |
| [templates/partials/character-header.hbs](../../../../../../../../templates/partials/character-header.hbs) | Три DOM-события | Текущий Character header | 49,61,66 |
| [templates/sheets/actor/partials/monster/header.hbs](../../../../../../../../templates/sheets/actor/partials/monster/header.hbs) | Три DOM-события | Текущий Monster header | 25,34,39 |
| [templates/sheets/actor/monster-sheet.hbs](../../../../../../../../templates/sheets/actor/monster-sheet.hbs) | Три DOM-события | Старый родитель, текущая V2 регистрация не найдена | 177,224,270 |

Область поиска: module/ и templates/ текущего checkout; прямые импорты и места вызова сверены отдельно от динамических обращений. Типы и листы сверены с system.json, module/setup/registerDataModels.js и module/setup/registerSheets.js. Внешние модули, макросы миров и действующие компедиумы не исследовались.

## Данные и изменения состояния

Только две счётные кнопки пишут system.deathSaves. Бросок считывает разные источники по HP; BODY/WILL.value в смертельном состоянии не используются. Ограничение 10 применяется до счётчика: отрицательный счётчик способен поднять порог выше исходного; число 0 не заменяется минимумом 1.

## Проверки и доказательства

| Что проверено | Источник, команда или сценарий | Фактический результат | Ограничения |
| --- | --- | --- | --- |
| Все определения и связи | 51 строка,3 импорта,4 метода; headers и schemas | Ручной reset/+1 отделён от самого броска | Не утверждается автоматическое продвижение счётчика |
| Настоящие броски | Группы 08–09: HP1/0/−1, STUN0/5/7/14, BODY/WILL разной чётности, deathSaves0/5/6/7/−2 | Верхний clamp подтверждён; threshold0 даёт неуспех, −1/−2 оставляют success undefined; кубики 1/10 не взрываются | Roll настоящий; сообщения и документы подменены |
| Счётчик/события | Группы 07,10 | Сброс всегда 0; +1 работает с 0/3/−1/0.5; Promise завершается при двух ожидающих update | Без серверной записи |

## Непроверенные участки и открытые вопросы

Правила автоматической смерти/штрафов и содержимое рулбука не переопределялись. Полный боевой маршрут, браузер и многоклиентские гонки не исполнялись.

## Связанные проблемы

[issue-00196](../../../../../../../issues/potential/issue-00196.md), [issue-00197](../../../../../../../issues/potential/issue-00197.md). Отрицательные пороги и преждевременное завершение ресурсных операций оформлены отдельно.

## История актуализации

| Дата | Версия и область пересмотра | Результат и запись сверки |
| --- | --- | --- |
| 2026-09-11 | `aa6af106e86a9c75fe050d599f961c8fadb74f1b`; полный файл | Первая карточка; [сверка порции](../../../../../review-log.md#task-0003030) |

## Уточнение TASK-0003.031

2026-09-11, `928ce4e537c6a3fdc34f8b6fa3fcfdb5a669f68d`. Header содержит .death-roll/.death-minus/.death-plus и .death-counter; sidebar редактирует healthState.deathState.ignored. Полный activateListeners Character вызывает базовую цепочку, где deathSaveListener привязывает действия. Незакрытая open-rewards создаёт пустые ссылки, но счётчик смертей не оказывается их дочерним узлом (issue-00202).

Связи: [module/actor/sheets/WitcherCharacterSheet.js](../WitcherCharacterSheet.js.md); [templates/partials/character-header.hbs](../../../../templates/partials/character-header.hbs.md); [templates/sheets/actor/partials/character/sidebar.hbs](../../../../templates/sheets/actor/partials/character/sidebar.hbs.md). [Методика и ограничения сверки](../../../../../review-log.md#task-0003031).
