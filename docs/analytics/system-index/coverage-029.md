# TASK-0006.029 — Профессиональные броски, способности и временное здоровье

2026-09-16; rusbar-main, исходный HEAD `ea39a61d3c4e222659abde172ef63982a2f42c66`, дерево в начале чистое. [Задача](../../tasks/task-0006.029.md), [запросы](examples/expansion-029-queries.json), [тесты](tests/test_expansion_029.py).

## Результат и пределы

Добавлены 51 сущность, 253 отношения и 8 процессов. Всего 4936 сущностей, 13603 отношения, 416 процессов (1360 шагов, 2529 переходов), 373 границы. Определения в 284/615 файлах: два словаря en/ru complete, 282 файла partial. Роли: 197 основных/87 смежных/331 без определений. Отношения в 288 файлах, локальные шаги процессов в 139.

Все прежние ID, владельцы и 408 процессов сохранены. Уточнены пять прежних сущностей. Исправлена обнаруженная адресация .028: ent-004885 и rel-013327/013328/013329 относятся к **src-000045, module/actor/sheets/mixins/skillMixin.js:31**, а не src-000046/statMixin.js. В coverage-028 и обосновании E028-12 исправлен тот же путь; команды/ожидания прежних примеров неизменны. Остальные 13347 прежних отношений полностью сохранены. Границы остаются partial; наличие всех собственных методов в графе не доказывает полное исполнение в Foundry.

| Файл | Включённая область и остаток |
| --- | --- |
| [module/actor/mixins/professionMixin.js](../../../module/actor/mixins/professionMixin.js) (src-000020) | Все собственные методы адресованы: lookup/total .028, dispatch/4 ветви/usage payload .029. Внешние Dialog/Actor/Item/AE/сеть/сохранение и полный игровой сценарий не исполнены. |
| [templates/dialog/combat/profession-attack.hbs](../../../templates/dialog/combat/profession-attack.hbs) (src-000507) | Все 14 controls, context/formula/bonus readers и callback; не все locale/styles/render-framework связи исчерпаны. |
| [module/data/item/professionData.js](../../../module/data/item/professionData.js) (src-000121) | Schema/enriched/defense .016/.028 и новые consumers связаны; полный внешний lifecycle/readers partial. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) (src-000029) | Выбор/обогащение/totalProfSkills .028 переиспользованы, прочие методы вне этой порции. |
| [templates/partials/character/tab-profession.hbs](../../../templates/partials/character/tab-profession.hbs) (src-000526) | Профессия/раса и click/inline .027/.028 сохранены; конкретные ветви исполнителя раскрыты .029. |
| [templates/sheets/actor/partials/monster/tabs/tab-profession.hbs](../../../templates/sheets/actor/partials/monster/tabs/tab-profession.hbs) (src-000572) | Только definingSkill/notes и click/inline; полный browser lifecycle partial. |
| [module/data/item/templates/profession/skillUsageData.js](../../../module/data/item/templates/profession/skillUsageData.js) (src-000144) | Все флаги schema и реальные readers; applySelf не используется professionMixin. Применение эффекта через внешние документы. |
| [module/data/item/templates/profession/temporaryHealthData.js](../../../module/data/item/templates/profession/temporaryHealthData.js) (src-000145) | DC/amount/duration readers и payload раскрыты, строки формул не объявлены общим parser. |
| [module/data/item/templates/profession/thresholdData.js](../../../module/data/item/templates/profession/thresholdData.js) (src-000146) | Словарь/CRUD .028 и выбор до броска .029; нет сортировки/автовыбора после результата. |
| [module/actor/sheets/mixins/skillMixin.js](../../../module/actor/sheets/mixins/skillMixin.js) (src-000045) | Исправлен источник прежнего click ID .028: skillMixin.js:31, не statMixin. Общий listener/другие действия остаются прежним частичным покрытием. |
| [module/actor/sheets/mixins/statMixin.js](../../../module/actor/sheets/mixins/statMixin.js) (src-000046) | Прежняя ошибочная привязка profession-roll перенесена в src-000045; собственный statMixin покрыт только ранее включёнными участками. |
| [module/actor/mixins/weaponAttackMixin.js](../../../module/actor/mixins/weaponAttackMixin.js) (src-000025) | Новые field readers skillReplacement и options handoff; все прежние .015 процессы сохранены, полный runtime partial. |
| [module/actor/mixins/modifierMixin.js](../../../module/actor/mixins/modifierMixin.js) (src-000019) | Реальный вызов addActiveEffects(undefined) прямой атаки; исходный guard и прочие модификаторы прежние. |
| [module/scripts/rolls/extendedRoll.js](../../../module/scripts/rolls/extendedRoll.js) (src-000202) | Прежний extendedRoll процесс/поля, новые profession callers; полное исполнение core Roll не тестировалось. |
| [module/scripts/temporaryEffects/applyActiveEffect.js](../../../module/scripts/temporaryEffects/applyActiveEffect.js) (src-000206) | Существующая доставка AE переиспользована с новым конкретным producer; network/create/expiry не исполнены. |
| [module/scripts/combat/combat.js](../../../module/scripts/combat/combat.js) (src-000195) | Прежний listener/onDamage и ошибочный UUID handoff профессии; полный чат lifecycle partial. |

<a id="dispatch"></a>
## Вход и порядок ветвей

Существующий listener skillMixin.js:31 передаёт событие Actor. _onProfessionRoll берёт имя ближайшего .profession-display; Actor lookup сначала definingSkill, затем девять слотов путей, первое точное совпадение. Нет guard отсутствия профессии/совпадения. Приоритет: isAttack → hasCustomEffect → hasThresholds → обычный бросок. Все четыре вызова запускаются без await/return. Флаг isDefense не образует здесь пятую ветвь: прежняя защита .016 имеет отдельный вход.

Связи модели/редактора .028, totalProfSkills и Character/Monster переиспользованы. UI скрывает кнопку для stat=none, но schema не ограничивает строку stat. Прямой обычный метод без guard читает stats[stat].value и statMap[stat].label до открытия окна. Одинаковые имена навыков остаются неоднозначными; ID строки threshold/effect не является ID навыка.

<a id="roll"></a>
## Обычный бросок

Формула — 1d10 + подготовленный stat.value владельца + level||0, затем await getCustomModifier. Это чтение уже подготовленной характеристики, а не отдельный повторный расчёт эффектов. В этом теле нет вызова addActiveEffects/addAttackModifiers. ChatMessageData получает this.actor вместо this; у Actor такое поле обычно отсутствует, поэтому ядро выбирает speaker по controlled token/user.character/user (issue236).

Без options default threshold=0/showResult=true. Новый RollConfig получает showCrit=true, threshold/thresholdDesc/showResult; defense/reversal остаются false. return extendedRoll усваивает его Promise. Прежний extendedRoll при threshold>=0 проверяет строго total>threshold, записывает rollOver=total−threshold; при showResult=false возвращает Roll с messageData. Отмена окна отвергает ожидающий метод; dispatcher не возвращает его Promise.

<a id="threshold"></a>
## Пороговый бросок

Object.entries словаря сохраняет порядок записей, явной сортировки нет. Одна запись выбирается сразу; при нуле или нескольких открывается prompt. Inline select имеет id=threshold; доступ form.elements.threshold допустим по id, отсутствие name само по себе не объявлено ошибкой. Callback возвращает выбранный ключ, а метод без guard читает его value/name и запускает обычный бросок без await. Пустой словарь может дать undefined.value до запуска броска. Порог выбирается **до** броска; автоматического поиска лучшего достигнутого результата нет.

<a id="attack"></a>
## Прямая атака

usesWeapon возвращает Promise оружейного chooser; иначе собирается отдельная прямая атака. damageFormulaOverride — базовый урон. Фактическое добавление meleeBonus требует applyMeleeBonus && (character || addMeleeBonus); отображение bonus в dialog context проверяет только applyMeleeBonus (issue244).

Template profession-attack.hbs содержит 14 controls: десять checked (extra и ситуационные флаги), четыре value (location/damageType/customAtt/customDmg). Числовой data-dtype в HBS не преобразует возвращаемые callback строки. renderTemplate и prompt ожидаются; rejectClose=true.

Локальный attack содержит первый attackOption, skill и alias, но не name/UUID. Формула атаки — 1d10 + stat.value + level??0; addActiveEffects(attack.name) получает undefined и возвращает пустую добавку. Отдельно учитываются десять флагов, custom и модификатор локации. isExtraAttack даёт −3 без записи STA. Это отличается от общего weaponAttack: там дополнительная атака требует 3 STA, а source update запускается без await (прежние процессы .015, issues238/262).

<a id="chat"></a>

Локальный damage содержит cloned properties/defenseOptions, item{name}, crit, выбранный type/formula/location/originalLocation. Damage schema не содержит item и вложенное defenseOptions. ChatMessageData(this, ..., 'attack') передаёт attacker, attack, damage и верхний defenseOptions; await extendedRoll без явного config использует threshold−1. После этого поздняя кнопка damage вызывает прежний onDamage, который требует attack.itemUuid. Producer UUID не задаёт; item{name} этого не заменяет (issue239). Ни успешное создание сообщения, ни успешный бросок урона этим анализом не подтверждены.

<a id="weapon"></a>
## Атака через оружие

Chooser фильтрует raw this.items только по type=weapon и наличию **первого** attackOption навыка. Нет фильтра isStored/equipped или guard пустого списка. Callback возвращает choosen.value; items.get(id) не проверяется. weaponAttack получает {skillReplacement:skill, additionalDamageProperties:skillAttack.damageProperties} без await/return. Promise chooser завершается раньше этой атаки.

Прежние процессы weaponAttack/getItemAttack/merge сохранены. При skillReplacement берутся имя/stat/level навыка; ветвь обходит constructBaseAttackFormula с его skill/group/allAttacks modifiers (issue237). Перенос additionalDamageProperties зависит от общего merge: массивы обрабатываются, TypedObject effects не становится массивом автоматически. Сохраняются прежние ограничения пустого оружия и взаимодействия options с несколькими режимами (issues242/264).

<a id="temporary-health"></a>
## Способность и временные HP

| Этап | Фактический контракт |
| --- | --- |
| Цель | applyOnTarget → game.user.targets.first()?.actor, при отсутствии notification+return. Иначе this; applySelf этот метод не читает |
| Guard | Собственная реализованная ветвь только addTemporaryHealth; false завершает метод |
| Сложность | target.stats[difficultyCheck.stat].max * multiplier, а не value и не характеристика владельца |
| Бросок | await doProfessionSkillRoll владельца с threshold и showResult=false; затем roll.toMessage(messageData) без await |
| Успех | Только rollOver>0 строит эффект; min(rollOver,maxRollOver) ограничивает часть количества |
| Длительность | replace первого @level, первое совпадение /\d+\*?\d+/g, затем eval; это не универсальный разбор формулы. '2' не совпадает, '10' совпадает |
| Количество | Строковая конкатенация min(...) + temporaryHp.value. Только при lowercase d выполняется await new Roll(value).evaluate(); иначе строка не вычисляется |
| Payload | new ActiveEffect: name=skillName, icon=profession.img, description=definition, origin=this.uuid, changes.key с skillName, ADD mode, вручную собранный JSON name/value, duration.rounds |
| Доставка | getActorOwner(target).query('TheWitcherTRPG.query', {function:'applyActiveEffectToActor',data:[target.uuid,[newEffect]]}) без await/return |

queryData с actorUuid/itemUuid создаётся, но не отправляется; поиск первой профессии для него всё равно исполняется и может завершиться ошибкой. newEffect — подготовленный документ, не прямой update HP или запись поля TemporaryEffects. Query receiver запускает helper и возвращает true без ожидания; доставка, clone и createEmbeddedDocuments представлены прежней .008. Успех локального вызова не равен завершению сети/сохранения/истечения эффекта.

Ручной JSON не экранирует имя; dotted key также содержит имя. Legacy schema установленного ядра перемещает changes в system.changes и может разобрать value в объект; mode/rounds мигрируются, icon→img здесь не реализован. Прежний updateDerivedStat .019 расходует HP через temporary effects и JSON.parse(change.value). Некорректный JSON и уже мигрированный объект — разные ограничения (issues117/240 и 294). Формула/имя/длительность/доставка оставлены как в коде; новых правил лечения/здоровья не вводится.

## Источники доказательств

Сверены R008-09–R008-19 позднего аудита. Прочитаны связанные полные issue8/110/113/114/115/117/118/120/236/237/238/239/240/241/242/243/244/262/264/294. Сохраняются их даты, статусы potential и пределы воспроизведения; новое игровое воспроизведение не заявлено. Аудит и issues не изменены.

Установленное ядро Foundry14.367.0 проверено чтением исходников. Hash фиксирует файл, не запуск клиента/БД.

| Файл | Строки | Контракт | SHA256 |
| --- | --- | --- | --- |
| `/opt/foundryvtt/client/documents/chat-message.mjs` | 231–274 | getSpeaker: Actor/Token либо controlled token/user.character/user. | `446c041c59b3f097e5c3358a528181e368e072be9cfe55fa928fa92932e55c5b` |
| `/opt/foundryvtt/client/applications/api/dialog.mjs` | 369–375,405–426 | prompt delegates wait; rejectClose=true: закрытие отвергает Promise, submit ожидает callback. | `4e2d299eaa931d96df1839e64a2defc60b6b95ee89a3e1d32d60b99040899343` |
| `/opt/foundryvtt/common/documents/active-effect.mjs` | 44–84,152–203,213–220,229–239 | Legacy changes→system.changes, mode→type, JSON value→объект; rounds→duration.value/units; icon не переносится в img. | `e8a1c26a2c84e415f814146f3e632f28fe6f3504920262e324c9ef071dfc5bf5` |

## Процессы

<a id="proc-000409"></a>
### proc-000409 — Профессия: клик и приоритет исполнения

Имя → первый совпавший навык, четыре непересекающиеся ветви.

Шаги: lookup → choose → attack → usage → threshold → regular. Guards, await/scheduled и выходы — в JSONL.

<a id="proc-000410"></a>
### proc-000410 — Профессия: обычный бросок и RollConfig

Бросок исполнителя; тот же метод вызывают threshold и HP usage.

Шаги: stat → custom → message → config → roll. Guards, await/scheduled и выходы — в JSONL.

<a id="proc-000411"></a>
### proc-000411 — Профессия: выбор порога до броска

Нет сортировки и автоматического выбора достигнутого результата.

Шаги: entries → prompt → choice → launch. Guards, await/scheduled и выходы — в JSONL.

<a id="proc-000412"></a>
### proc-000412 — Профессия: прямая атака или переход к оружию

Прямая ветвь собирает attack message; rollDamage является отдельным поздним действием.

Шаги: mode → weapon → damage-base → context → prompt → controls → payload → formula → location → message → roll. Guards, await/scheduled и выходы — в JSONL.

<a id="proc-000413"></a>
### proc-000413 — Профессия: выбор оружия и делегирование

Выбранный Item и options передаются существующему weaponAttack .015.

Шаги: filter → prompt → choice → launch. Guards, await/scheduled и выходы — в JSONL.

<a id="proc-000414"></a>
### proc-000414 — Профессия: цель и бросок временного здоровья

Флаги applyOnTarget/addTemporaryHealth определяют фактические ветви.

Шаги: target → feature → roll → publish → success → effect. Guards, await/scheduled и выходы — в JSONL.

<a id="proc-000415"></a>
### proc-000415 — Профессия: временные HP как payload ActiveEffect

Продолжение usage только при roll.options.rollOver>0; прямой update HP отсутствует.

Шаги: source → duration → amount → dice → construct → query. Guards, await/scheduled и выходы — в JSONL.

<a id="proc-000416"></a>
### proc-000416 — Профессия: сообщение прямой атаки и поздний запрос урона

Стык producer с моделью/кнопкой; не доказательство браузерной доставки.

Шаги: producer → publish → click → item. Guards, await/scheduled и выходы — в JSONL.

## Проверки

Проверены все 245 тестовых методов в 28 модулях и 733 примера CLI, включая 35 новых по IQ-01–IQ-08; ошибок в итоговых результатах нет. Исторические проверки выполняются на предусмотренных прежними тестами срезах. Это проверки справочника по исходникам, без запуска игрового сценария. Перекрёстно сверены исходные адреса/владельцы, оба конца отношений, readers/payload/source writers, ветви и выходы, refs/facets/роли. [Протокол](review-log.md#task-0006029). Следующая — [TASK-0006.030](../../tasks/task-0006.030.md); родитель in-progress.