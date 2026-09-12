# module/scripts/combat/generalCombatHook.js

| Поле | Значение |
| --- | --- |
| Исходный файл | [module/scripts/combat/generalCombatHook.js](../../../../../../../module/scripts/combat/generalCombatHook.js) |
| Тип файла | JavaScript, ES module |
| Статус анализа | Проверено |
| Дата проверки | 2026-09-12 |
| Ветка и коммит | rusbar-main, 20ce99a1218a82bf46c84570e55587253d0cfbc3 |
| Изменения относительно коммита | Нет; совпадает со срезом TASK-0001 15da5b225535e34af4e132c701b5353ef4eb667f |
| Задача и порция | [TASK-0003.045](../../../../../../tasks/task-0003.045.md), 5 файлов / 336 логических строк; данный файл — 87 |
| Запись перекрёстной сверки | [TASK-0003.045](../../../../review-log.md#task-0003045) |

## Назначение файла

Запускает регенерацию монстра и урон/лечение из turnStartEffects для текущего участника Combat на активном GM.

## Условия использования

[module/setup/hooks.js](../../../../../../../module/setup/hooks.js) импортирует applyGeneralCombatHooks и вызывает его без await при каждом updateCombat. [module/TheWitcherTRPG.js](../../../../../../../module/TheWitcherTRPG.js) регистрирует общий Hook до init. Здесь нет собственной подписки, фильтра changed-полей, проверки started или отслеживания уже обработанного хода. Единственная входная проверка — game.user.isActiveGM.

## Введённые сущности и действия с ними

| Сущность | Вид и место | Доступность | Действия |
| --- | --- | --- | --- |
| applyGeneralCombatHooks | async function:3–9 | export | Получить текущего Actor; запустить регенерацию и статусы |
| applyMonsterRegeneration | async function:11–38 | local | Отфильтровать Actor; сообщение GM и update HP |
| applyCombatEffects | async function:40–44 | local | Перебор Object.values(turnStartEffects) |
| applyCombatEffect | async function:46–87 | local | Сообщение о статусе; урон HP/STA; лечение HP |
| chatData / damage | Объекты:23–28,52–56,62–73 | local payload | Данные чата; свойства/локация урона, type отсутствует |

## Основные функции и методы

| Функция | Входы и guards | Результат / действия | Ожидания и ошибки |
| --- | --- | --- | --- |
| applyGeneralCombatHooks(combat) | !game.user.isActiveGM → return | Получает combat.combatants.get(combat.current.combatantId).actor; вызывает два локальных async метода | Не ждёт оба; нет guard combatant/Actor/game.user; Promise root не означает окончания записи |
| applyMonsterRegeneration(actor) | Выходит для type!='monster', regeneration===0, statuses.has('dead') | Ждёт regeneration.hbs({actor}); создаёт сообщение whisper:[game.user.id]; update HP=Math.min(HP+regeneration,HP.max) | ChatMessage.create и update не ожидаются; нет нижнего ограничения/проверки знака, при полном HP всё равно сообщение/update |
| applyCombatEffects(actor) | Нужен system.combatEffects.turnStartEffects | for-of Object.values: await applyCombatEffect для каждой записи | Цикл ждёт лишь возвращённые Promise; передача урона из следующего метода не включает окончание Actor.applyDamage |
| applyCombatEffect(actor,status) | Если оба amount falsy → return; damage/heal исполняются только при своём amount>0 | Сначала render statusEffect.hbs(status), ChatMessage.applyMode/create; потом damage; потом heal | create не ожидается; await applyDamageFromStatus не ждёт реальную запись; calculateHealValue/update/createHealMessage ожидаются по их возвращённым Promise |

### Поля воздействия

У damage передаётся amount+(modifier??0). nonLethal выбирает sta, иначе hp. В properties передаются spDamage, damageToAllLocations=allLocations, effects=[], bypassesNaturalArmor/bypassesWornArmor=ignoreArmor, bypassesShield. Локация — actor.getLocationObject('torso'). damage.type не копируется, хотя объявлен схемой. amount=0 при modifier>0 пропускается; amount<0 может создать сообщение, но не запрос урона; amount>0 и отрицательный modifier могут дать отрицательный итог без ограничения.

Лечение вызывает calculateHealValue только с heal.amount. При результате>0 записывает HP+healedFor и создаёт сообщение лечения. heal.modifier не читается. В исходном healMixin количество ограничивается HP.max; отдельная регенерация эту функцию не использует.

Dead останавливает только регенерацию. Ветвь turnStartEffects не проверяет dead. Порядок damage перед heal в тексте не гарантирует завершения урона до расчёта лечения. Регенерация и обработка статусов вообще запускаются параллельно.

## Используемые сущности и зависимости

| Сущность | Источник | Вид / место | Основание |
| --- | --- | --- | --- |
| applyDamageFromStatus | [module/scripts/combat/applyDamage.js](../../../../../../../module/scripts/combat/applyDamage.js) | import:1; вызовы:74/76 | Создаёт DamageInstance и не ожидает Actor.applyDamage |
| applyDamage / updateDerivedStat / calculateDamageWithLocation | [module/actor/mixins/damageMixin.js](../../../../../../../module/actor/mixins/damageMixin.js) | Косвенный consumer damage | Щит, броня, запись HP/STA; очередь статусов не сериализует эти Promise |
| damageTypeModification / getters | [module/actor/mixins/damageUtilMixin.js](../../../../../../../module/actor/mixins/damageUtilMixin.js); [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](../../../../../../../module/data/actor/templates/character/general/damage/damageTypeModificationData.js) | Косвенное чтение типа урона | Потеря fire выбирает fallback вместо fire.flat |
| turnStartEffects | [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js); [module/setup/config.js](../../../../../../../module/setup/config.js) | Схема / источники статусов | amount/modifier/type, flags и поля heal; CommonActorData встраивает схему |
| regeneration / resistant fields / type | [module/data/actor/monsterData.js](../../../../../../../module/data/actor/monsterData.js) | Данные monster | regeneration NumberField initial0 без min/max |
| derivedStats.hp / sta | [module/data/actor/templates/common/stats/derivedStatsData.js](../../../../../../../module/data/actor/templates/common/stats/derivedStatsData.js) | Ресурсы | Значение/максимум HP; STA передаётся строковым именем |
| getLocationObject | [module/actor/mixins/locationMixin.js](../../../../../../../module/actor/mixins/locationMixin.js); [module/actor/witcherActor.js](../../../../../../../module/actor/witcherActor.js) | Динамический Actor-метод | Локация torso для статуса |
| calculateHealValue / createHealMessage | [module/actor/mixins/healMixin.js](../../../../../../../module/actor/mixins/healMixin.js); [templates/chat/combat/heal.hbs](../../../../../../../templates/chat/combat/heal.hbs) | Dynamic calls:81,85 | Предел HP.max и сообщение фактического лечения |
| regeneration.hbs | [templates/chat/combat/regeneration.hbs](../../../../../../../templates/chat/combat/regeneration.hbs) | renderTemplate:16–21 | Контекст {actor} до update |
| statusEffect.hbs | [templates/chat/combat/statusEffect.hbs](../../../../../../../templates/chat/combat/statusEffect.hbs) | renderTemplate:48–51 | Контекст — сама запись статуса, не Actor |
| ChatMessage.getSpeaker/create/applyMode, Combat, User, renderTemplate, CONST | Foundry 14.367.0 | Внешние API | Рендер настоящий Handlebars; документы/запись и настройки — фасады |
| core.messageMode | Foundry core setting | Статусное chatData | Регенерация вместо applyMode явно использует whisper |

## Известные потребители

[module/setup/hooks.js](../../../../../../../module/setup/hooks.js) — единственный прямой импорт/вызов export в module. Внешние макросы не проверены. Три остальные функции вызываются только внутри файла. [module/data/actor/templates/common/combatEffectsData.js](../../../../../../../module/data/actor/templates/common/combatEffectsData.js) и [module/setup/config.js](../../../../../../../module/setup/config.js) производят читаемые пути данных, а не вызывают обработчик сами.

## Данные и изменения состояния

Запросы ChatMessage.create и Actor.update; косвенно damage/SP/shield/status effects через Actor.applyDamage. Каждый статус получает отдельное информационное сообщение ещё до расчёта. Сообщение не подтверждает, что HP уже изменён. Модель регенерации не показывает фактически восстановленное количество: шаблон получает прежний HP и настроенное regeneration.

## Проверки и доказательства

| Проверка | Фактический результат | Пределы |
| --- | --- | --- |
| 13–17 | flags/start/turn доходят до общего handler; не-GM выходит; пустой combatant даёт ошибку; character/zero/dead пропускают regen; dead-статус исполняется; HP19+2→20, при 20 повторяется update; regeneration−3 приHP1→−2 | Фасады Combat/Actor, настоящие MonsterData/HBS; переход реального боя не выполнялся |
| 18–20 | Настоящая схема сохраняет fire/modifier, consumer передаёт damage7 с type undefined и heal3 без+2; modifier-only пропущен; nonLethal STA; отрицательный итог−3; heal ограничен max и ждёт update | Документы и prompt заменены |
| 21–22 | Два статуса запускают pending-записи из прежнего HP; regen/heal подготавливают 12/13 из 10 вместо суммарного 15 | Контролируемое ожидание, не измерение сетевой вероятности |
| 29–31 | Настоящий Actor.damageMixin: fire.flat4 не применился к потерянному типу — урон 5 против 9; из 100 две pending-записи 97/96 дают 96; отрицательный итог повышает shield5→8 | Реальные арифметика/броня/локации, фасады update; никакой записи в БД |

## Непроверенные участки и открытые вопросы

Все 87 строк разобраны. Реальные Hooks нескольких клиентов, очередь документов Foundry, повторное получение/снятие ActiveEffect, восстановление prepared-данных после update, серверная запись и её отказ не запускались. Наблюдения о dead/отрицательной регенерации/нулевом amount — описание существующих guards, а не автоматическое решение об изменении правил. Вероятность потери записей в конкретном мире не измерялась.

## Связанные проблемы

[6](../../../../../../issues/potential/issue-00006.md) — неверная граница запуска; [21](../../../../../../issues/potential/issue-00021.md) — потерянный type; [22](../../../../../../issues/potential/issue-00022.md) — heal.modifier; [145](../../../../../../issues/potential/issue-00145.md) — пустой Combat-контекст, теперь сверенный и в этой ветви; [299](../../../../../../issues/potential/issue-00299.md) — раннее завершение/конкурирующие записи; [291](../../../../../../issues/potential/issue-00291.md) — отрицательный урон щиту. Эти причины разделены: правильный момент запуска сам по себе не обеспечит последовательную запись нескольких эффектов.

## История актуализации

| Дата | Версия и область | Результат |
| --- | --- | --- |
| 2026-09-12 | 20ce99a1218a82bf46c84570e55587253d0cfbc3; полный файл | Первичная карточка; [перекрёстная сверка](../../../../review-log.md#task-0003045) |
