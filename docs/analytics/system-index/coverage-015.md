# TASK-0006.015 — Оружейная атака: вход, формула и результат

2026-09-15, rusbar-main; исходный HEAD baec9c69c47aca602facaddf566008c45bfc8073. Рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.015.md).

## Область и остаток

Восемь основных исходников и выбранные смежные области. Схема v1 и CLI сохранены, все новые области partial. Полный бой, применение урона, магия и ядро/мир не объявлены раскрытыми.

| Основной источник | Область/остаток |
| --- | --- |
| [module/actor/mixins/weaponAttackMixin.js](../../../module/actor/mixins/weaponAttackMixin.js) (src-000025) | Пять собственных методов, форма/ресурсы/формулы/выходы раскрыты; runtime мира, все внешние callers, полные защита/урон и доставка сообщений остаются .016–.020. |
| [module/item/witcherItem.js](../../../module/item/witcherItem.js) (src-000192) | getItemAttack 28–70 и процесс .014 переиспользованы; новые связи ведут от weaponAttack к тому же методу. Остальной Item lifecycle раскрыт только в ранее выбранных областях. |
| [module/actor/witcherActor.js](../../../module/actor/witcherActor.js) (src-000047) | Добавлены calculateAttackStats и адрес одиночного getLocationObject; все прочие Actor-процессы и полный random/location downstream не развёрнуты. |
| [module/data/actor/templates/character/attackData.js](../../../module/data/actor/templates/character/attackData.js) (src-000058) | Две строки attack(label) для punch/kick; все потребители и UI этих формул не установлены. |
| [module/data/actor/templates/character/attackStatsData.js](../../../module/data/actor/templates/character/attackStatsData.js) (src-000059) | Пять полей и schema включения раскрыты; остальной combat/runtime partial. |
| [module/data/chatMessage/attackMessageData.js](../../../module/data/chatMessage/attackMessageData.js) (src-000094) | Схема/getter/включения и selected consumers раскрыты; ядро ChatMessage lifecycle, hooks и права внешние. |
| [module/data/chatMessage/templates/attackData.js](../../../module/data/chatMessage/templates/attackData.js) (src-000098) | Фабрика attackData() и четыре поля attackOption/skill/alias/itemUuid, включение в AttackMessageData и выбранные consumers; полная доставка сообщения остаётся .020. |
| [templates/dialog/combat/weapon-attack.hbs](../../../templates/dialog/combat/weapon-attack.hbs) (src-000510) | Контекст, 20 controls/callback, конкретные CSS и известные барьеры раскрыты; DOM validation/sanitization/computedStyle не проверялись. |

## Существенные различия

- Actor attack(label) описывает label/value punch/kick. Chat attackData() описывает attackOption/skill/alias/itemUuid. Похожие имена файлов не объединяют владельцев. attackStats — фабрика схемы; расчёт BODY выполняет Actor.
- B=ceil((BODY.value−6)/2)×2 добавляется к prepared meleeBonus, а punch/kick.value строятся из локального B. CommonActorData.migrateCalculatedStats обнуляет truthy исходный meleeBonus. Повторное начисление в мире не утверждается; прежний reset опыт сохраняет свою дату.
- getItemAttack и процесс .014 переиспользованы: порядок Set, ctrl/alt/shift, пустой набор и служебные options. Профессиональная замена меняет skill/alias, не режим; stat/level идут в формулу без addActiveEffects/addAttackModifiers. Неизвестный непустой skill отклоняется позже пустого.
- Диалог получает девять полей context и читает 20 controls: 12 checked и 8 value, из которых range/ammunition условны. Numeric input.value остаётся строкой. noAmmo/noThrowable — предупреждения, не запрет подтверждения. AmmunitionOption — сырая HTML строка; подтверждённый прежний эффект ограничен структурой разметки.
- Предпросмотр damageFormula учитывает applyMeleeBonus и character/addMeleeBonus; отдельная ячейка meleeBonus — только флаг предмета. customDmg и выбранный удар ещё не входят в preview. unavailable в форме обусловлен piercing=false по текущим helpers.
- Ресурсы запрашиваются до цикла: extraSTA−3, выбранный ammo−1, ranged throwable−1. Updates без await; ammo quantity>0 не проверяется. Throwable либо поздняя ошибка skill/strike могут остановить путь после первых запросов. Откат/транзакция не реализованы этим методом; соответствие кратности расхода правилам не устанавливается.
- Каждый удар заново строит attFormula. Accuracy сохраняет знак; positional/range поправки отражены дословно; customAim применяется лишь >0, customAtt добавляется через + даже для отрицательной строки. Обычная основа читает подготовленные stat/skill и прежние helpers. Положительный combat modifier без оператора и lifepath объект вместо .value остаются известными границами.
- Общая damageFormula находится вне цикла: fast с customDmg=2 даёт второму удару дополнительное +2. Это ранее установленное поведение, не новый поведенческий запуск. merge AP/IAP и TypedObject effects переиспользуют .014; ammo/enhancement addEffects мутируют prepared модель.
- handleAttackLocation сохраняет resolved location и originalLocation; одиночный tailWing и getAllLocations различны. Карта удара — config.weapon.attacks, modifier в поле attackPenality; dmgMulti используется позднее rollDamage, не множителем броска атаки.
- После properties.toObject(false) обычный путь ждёт extendedRoll. ChatMessageData является контейнером, AttackMessageData — типизированной моделью, которая восстанавливает Embedded DamageProperties. attackRoll getter возвращает rollTotal; UUIDField не подтверждает существование Item. damage.crit сохраняет оба модификатора, а defense.crit имеет другой контракт.
- rollOnlyDmg вызывает Item.rollDamage без await с тем же общим damage/plain properties. На consumer159:47 у переданного объекта отсутствует getPreprocessedEffects; variableDamage может сначала открыть окно. Прежний pending-фасад .041 подтверждал ожидание/ссылки, но успешность прямого пути уточнена .044/issue297.
- extendedRoll уже проиндексирован: default RollConfig включает showCrit/showResult, threshold−1 и defense=false; flags[]. Он оценивает Roll, при crit/fumble формирует дополнительный результат, пишет rollTotal и ждёт toMessage. Его процесс не дублируется.
- Fumble consequences — отдельный click меню. Видимость смотрит options.fumble, dispatcher сравнивает точные constructor. attackFumble читает skill/attackOption; unarmed9 оставляет undefined, ranged7/9 попадают в следующие интервалы. Создаётся текст по en/ru WITCHER.fumbleResults, RollTable не вызывается и последствия автоматически не применяются. UUID в getSpeaker отличается от Actor, передаваемого оружейным producer.

## Доказательства и границы

Сопоставлены текущие исходники, поздние карточки TASK-0004.003/.004/.010/.011 и R003-05, R010-01–06. Прочитаны полные связанные issues 00019/00033/00181/00182/00183/00237/00244/00257/00258/00259/00260/00261/00262/00263/00265/00266/00267/00297; для уже раскрытых связей .014 переиспользованы 00064/00065/00069/00070/00264. Даты опытов, фасады и potential статусы сохранены. Новый игровой запуск, исправления и регистрация issues не выполнялись.

Смежные: CommonActorData, stat/Skill, modifier helpers, ChatMessageData, RollConfig/extendedRoll, typed damage/crit/location, CSS двух файлов по конкретным selectors, Item damageUtil entry, combat onDamage/executeDefense и fumble ветви. Полные защита/урон/чат остаются .016–.020; не исследуется соответствие контента книгам. В задаче уточнено: сосед fumble использует локализации, а не внешний RollTable.

## Процессы

<a id="proc-000177"></a>

### proc-000177 — Actor: подготовка бонуса BODY и безоружных формул

calculateAttackStats после calculateDerivedStats; reset/миграция остаются прежними процессами.

<a id="proc-000178"></a>

### proc-000178 — Оружие: обычная основа формулы атаки

Вход skill=CONFIG.skillMap[attack.skill]; неизвестный skill не защищён guard.

<a id="proc-000179"></a>

### proc-000179 — Оружие: подтверждение параметров диалога

DialogV2.prompt OK callback (event,button,dialog); отмена принадлежит внешнему rejectClose, сюда не входит.

<a id="proc-000180"></a>

### proc-000180 — Оружейная атака: от Item до результата

Actor.useItem/прямой вызов/профессиональный caller; здесь нет проверки цели и хода. Две конечные ветви и ранние отказы.

<a id="proc-000181"></a>

### proc-000181 — Оружие: сборка формулы одного удара

Выбранный участок одной итерации; полная ресурсная цепочка в соседнем процессе weaponAttack.

<a id="proc-000182"></a>

### proc-000182 — Оружие: локация и её модификатор

Локальная обёртка выбранной локации; random resolver отдельный адрес, последующее применение урона вне порции.

<a id="proc-000183"></a>

### proc-000183 — Оружие: тип удара и биография

Конкретный strike; config entry обязателен, lifepath запись используется целиком.

<a id="proc-000184"></a>

### proc-000184 — Сообщение атаки: состав схемы и внешняя очистка

Регистрация модели не означает создание сообщения; это schema assembly и адрес внешнего восстановления properties.

<a id="proc-000185"></a>

### proc-000185 — Сообщение атаки: готовое значение броска

Чтение getter после подготовки сообщения; без повторного Roll.

<a id="proc-000186"></a>

### proc-000186 — Провал: отдельное действие контекстного меню

После click, а не автоматически из extendedRoll. Видимость ранее проверила только options.fumble.

<a id="proc-000187"></a>

### proc-000187 — Провал атаки: выбор ключа текста

fumbleAmount после extendedRoll; melee/ranged проверки отдельные, spell может заменить выбранный результат.

<a id="proc-000188"></a>

### proc-000188 — Провал: безоружный диапазон

Локальный lookup ключа; unarmed9 не получает результат.

<a id="proc-000189"></a>

### proc-000189 — Провал: текстовое сообщение последствий

Свойства Actor/Item не меняются; localize lookup не RollTable.

## Проверки

Выполнен полный прогон 118 тестовых методов (644.949 с): единственное несоответствие — устаревший список читателей displayRollsDetails в X006-10. После добавления двух подтверждённых читателей все 8 тестов .006 повторно прошли (38.717 с). Остальные 117 методов полного прогона, включая все проверки .015, прошли. Накоплен 301 CLI-пример, из них 28 новых. Это проверки справочника, без исполнения игрового сценария.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
git diff --check
~~~

Сверены определения и владельцы схем, поля контекста и все 20 controls с их callback, source/prepared/message payload, точные места resource update, границы await и два выхода атаки. Все 9427 отношений проверены в обоих направлениях; для новых процессов — адреса и участие отношений в шагах, достижимость каждого шага и выхода. Три аспекта покрытия сопоставлены с реальными записями для всех 615 sources.

Предварительные проверки уточнили путь lifepathModifiers.attacks в индексе; в тестах — реальные имена переменных, сокращённые свойства объекта context и многострочную сборку customDmg. Запрос боеприпаса проверяет чтение control, а не запись документа; процесс атаки сохраняет отдельный шаг damage-formula. Числа .014 теперь проверяются по историческому диапазону ID, прежние содержательные проверки сохранены. Поиск value учитывает новое строковое поле actor.attack(label).value. Игровое поведение этими правками не менялось.

Полный прогон проведён после предварительной проверки новой порции. Единственное несоответствие полного прогона устранено в ожидании X006-10: добавлены weaponAttack:8 и constructBaseAttackFormula:316, которые читают displayRollsDetails. Повторно проверена вся .006; другие записи после полного прогона не менялись. Более ранний неполный запуск остановлен при уточнении тестовых литералов и не засчитывается как успешная проверка. Сохранность и итоговая актуальность проверяются после обновления навигации, результат — в журнале.


## Итог и следующая порция

Добавлены 129 сущностей, 432 отношения, 13 процессов. Накоплено 4022 сущности, 9427 связей и 189 процессов (684 шага, 1169 переходов). Определения есть в 221/615 файлах: два словаря complete по строковым ключам, 219 файлов partial; роли 94 основных/127 смежных, 394 без определений.

TASK-0006.015 done; следующая — [TASK-0006.016](../../tasks/task-0006.016.md), защита, критический результат и выбор локации. Родитель остаётся in-progress. Проверки сохранности и финальная актуальность — в [журнале](review-log.md#task-0006015).
