# TASK-0006.022 — Лечение, отдых, регенерация и спасброски смерти

2026-09-15; rusbar-main, исходный HEAD `924d6a149fd668a184b7bcffc625c3ad443e9b7f`; начало — чистое рабочее дерево. [Задача](../../tasks/task-0006.022.md).

## Область и остаток

Девять основных источников и выбранные соседи. Индекс текущего кода, формат v1 и CLI сохранены. Исполнение игры и соответствие рулбуку не проверяются; общее покрытие partial.

| Источник | Включено и границы |
| --- | --- |
| [module/actor/mixins/healMixin.js](../../../module/actor/mixins/healMixin.js) (src-000017) | Оба метода целиком; formula/parseInt/max и report. Core Roll/ChatMessage/sохранение остаются внешними. |
| [module/actor/sheets/mixins/healMixin.js](../../../module/actor/sheets/mixins/healMixin.js) (src-000042) | Все методы и callbacks лечения; DOM flags, сумма, ресурсы и handoff травм. Live окна/сохранение не исполнялись. |
| [module/actor/sheets/mixins/deathSaveMixin.js](../../../module/actor/sheets/mixins/deathSaveMixin.js) (src-000041) | Весь mixin: счётчик, threshold, roll и bindings. Последствия общего extendedRoll переиспользуются; автоматическая смерть не добавлена. |
| [module/scripts/chat.js](../../../module/scripts/chat.js) (src-000193) | Полный onHeal и прежняя регистрация; onRender других действий сохранён в .020. |
| [module/scripts/combat/generalCombatHook.js](../../../module/scripts/combat/generalCombatHook.js) (src-000196) | Регенерация целиком и heal-ветвь; прежние general/periodic/damage процессы сохранены, сохранение/конкурентность внешние. |
| [templates/chat/combat/heal.hbs](../../../templates/chat/combat/heal.hbs) (src-000485) | Весь HBS отчёта; кнопки лечения нет. |
| [templates/chat/combat/regeneration.hbs](../../../templates/chat/combat/regeneration.hbs) (src-000486) | Весь HBS: имя, старый HP, configured regeneration. Не delta после max. |
| [templates/chat/heal/resting-status.hbs](../../../templates/chat/heal/resting-status.hbs) (src-000494) | Весь отчёт отдыха; actualWoundList без producer, totalRec не delta, vigor не отображён. |
| [templates/dialog/heal/heal-rest.hbs](../../../templates/dialog/heal/heal-rest.hbs) (src-000513) | Весь dialog HBS; фиксированные global IDs, четыре checkbox, подсказки. Живой DOM не проверен. |

## Пути восстановления

| Путь | Источник и цель | Расчёт и предел | Запись и ожидание |
| --- | --- | --- | --- |
| Actor.calculateHealValue | Переданный value; HP текущего Actor | lowercase d → Roll; parseInt только в сравнении/max−value; иначе вернуть heal | Сам не пишет |
| Consumable.consume (.013) | Владелец Item | await calculateHealValue, затем parseInt результата | HP update без await; собственный createConsumeMessage, не createHealMessage |
| onHeal чата | data-actor — источник; target → controlled → user.character — цель | parseInt(data-heal), верхний HP.max, нет lower/NaN guard | HP update и ChatMessage.create без await; source.name читается после update |
| recoverActor | Actor листа | HP=min(old+totalRec,max); STA=max,Vigor=max при любом resting | await Actor.update; forEach травм без await; ждёт render отчёта, не ChatMessage.create |
| Регенерация | Текущий Combat Actor: monster, regeneration!==0, !dead | HP=min(old+regeneration,max); negative проходит | await render до update; create и HP update без await |
| Периодическое лечение | Тот же Actor, status.heal.amount | amount>0 → await calculateHealValue → healedFor>0; modifier не читается | await HP update и createHealMessage wrapper; внутренняя запись сообщения не ожидается |

## Контракты и маршруты

- calculateHealValue не гарантирует число/положительность: else возвращает исходное heal (включая строку); выше max может вернуть отрицательную разницу. null может упасть на value.includes. onHeal не использует этот helper: parseInt строки формулы не бросает кубики. На одинаковом HP эти пути могут вести себя по-разному.
- _onHeal создаёт dialogData с половиной REC.max (floor), actor, четырьмя false flags и daysHealed=1. После await render регистрируются change listeners на global document. Это не ожидание решения пользователя. В шаблоне фиксированные ID без checked-привязки: resting, sterilized, healing-hand, healing-tent.
- updateHealAmount каждый раз начинает с floor(REC.max/2). Resting заменяет на полный REC.max; sterilized +2, hand +3, tent +2. isResting/isSterilized выставляются только true и остаются такими после снятия checkbox. Hand/tent flags не записываются. Меняются totalRec, extra-info.textContent и sterilized-info.className. Каждый callback использует общий изменяемый dialogData.
- Heal callback заново читает resting/sterilized из DOM. recoverActor использует dialogData.totalRec для HP и полные STA/Vigor независимо от resting. После await Actor.update вызывает прежний proc-000331: forEach crit.system.heal({sterilized:isSterilized}) без ожидания. Proc-000322 сохраняет treated/стерилизацию/порог, deadly запрещает только автоматический treat; proc-000323 описывает followUp/create/delete. Дублирования модели заживления нет.
- resting-status показывает sticky dialogData.isResting, расчётный totalRec и fullStamina. При ограничении HP.max это не фактическая delta. actualWoundList не установлен producer, поэтому блок daysHealed не появляется обычным путём; Vigor в отчёте не указан. Notification использует свежий аргумент isResting и может расходиться с отчётом.
- Actor.createHealMessage передаёт getSpeaker({actor:this.actor}); this здесь Actor. Отдых передаёт game.actors.getName(this.actor.name), что не тождественно Actor листа. Chat onHeal использует UUID источника; regeneration — текущий actor. Источник/speaker/вылеченная цель — отдельные роли.
- Реальный button.heal находится в spellItem.hbs: doesHeal, data-heal=damage.heal и data-actor=templateInfo.actor.uuid. Частичный magic producer castSpell:208–212 задаёт heal, а227–235 передаёт damage/templateInfo. Полный magic flow не расширялся. Fumble не является условием наличия этой кнопки. combat/heal.hbs содержит лишь heal, без button/dataset; нельзя приписывать ему запуск onHeal.
- onHeal сначала разрешает источник UUID, затем выбирает первую цель/controlled/character; без цели return. Отсутствующий source не проверяется: actor.name обращается уже после запуска update цели. Корректность UUID, записей и доступа к документам не доказана статическим графом.
- GeneralCombatHooks (.020) запускает regeneration и periodic effects без await. В regeneration до записи выводятся старый HP и configured regeneration; нет skip fullHP. Periodic heal проходит после прежней damage-ветви/её пропуска, читает только amount и дважды проверяет положительность. Общего dead guard у periodic нет. Реальная очередность конкурирующих сохранений не утверждается. Каталог turnStartEffects и status ID не являются одним хранилищем; прежняя ADD/prepared граница сохранена.
- death-minus сбрасывает deathSaves=0, death-plus пишет old+1: обе операции preventDefault и update без await. CommonActorData.deathSaves NumberField0 не задаёт min/integer. _onDeathSaveRoll не вызывает ни один из этих writers.
- Порог спасброска: при HP>0 stun.value; иначе floor((BODY.max+WILL.max)/2). Сначала min(base,10), затем минус deathSaves, без нижнего cap. Создаются ChatMessageData и RollConfig: reversal=true,showSuccess=true,showCrit=false,threshold=stunBase. await extendedRoll(1d10) с showResult defaulttrue. При threshold>=0 общий код использует строгое rollTotal<threshold; при отрицательном threshold compare пропускается. showSuccess не читается extendedRoll. Нет вызова записи dead или счётчика; deathState.ignored sidebar — отдельное поле.
- Character header выводит heal/death buttons, Monster header — только death buttons. Общий Actor sheet подключает оба listener; наследование не создаёт отсутствующую кнопку. Общий _onRecoverSta — отдельный ранее ограниченный путь, не recoverActor: REC.value добавляется без max clamp, full-кнопка задаёт STA.max. Он не получает новый подробный процесс этой порции. Ручные HP/STA поля sidebar и damage writers .019 остаются отдельными путями.

## Доказательства и пределы

Девять основных файлов прочитаны целиком; для chat/generalCombatHook индекс дополнен только выбранными телами и переиспользованными входами. Прочитаны поздние разделы девяти карточек и полные группы R003-11, R011-07/21/22, R012-24…29. Ранние исторические описания не выдаются за новый запуск.
Полностью прочитаны issues 00006,00022,00123,00124,00125,00126,00127,00164,00196,00197,00202,00249,00253,00255,00256,00299,00328. Их статусы и файлы сохранены. Другие refs прежних процессов переиспользуются без заявления нового полного чтения.
Соседи: consumeMixin1–43; RollConfig1–20; extendedRoll1–107; ChatMessageData1–21; CriticalWoundData67–106; spellItem44–59; castSpell193–235/246–270; ActorSheet212–244/249–322 и V1 выбранные listeners/recoverSTA214–291; CharacterSheet1–60/106–122; MonsterSheet1–65/93–130; character header40–69 и monster header1–42; два sidebar выбранные HP/STA/deathState поля; CommonActorData17–37, MonsterData17–36, DerivedStats/stat целиком, Stats1–32, combatEffects28–41. Остальная прежняя регистрация/подготовка/урон/эффекты переиспользуются.
Внешняя проверка getSpeaker: /opt/foundryvtt/client/documents/chat-message.mjs:231–273, SHA256 `446c041c59b3f097e5c3358a528181e368e072be9cfe55fa928fa92932e55c5b`. При отсутствии Actor ядро может выбрать controlled token, затем user.character, затем user. Это отдельное внешнее чтение, не исходник системы. JS сценарии, browser/DOM, мир, права, документы и многоклиентность не исполнялись.

Внешний контракт окна дополнительно прочитан: /opt/foundryvtt/client/applications/api/application.mjs:496–535, SHA256 `b5aef80d3e042a4a856be9dd875c72a5224988d62046ba770f25376f4291faa0`; /opt/foundryvtt/client/applications/api/dialog.mjs:260–285, SHA256 `4e2d299eaa931d96df1839e64a2defc60b6b95ee89a3e1d32d60b99040899343`. ApplicationV2.render возвращает Promise отрисовки. DialogV2._onSubmit отдельно ожидает callback кнопки; это не Promise из render.

## Процессы

<a id="proc-000335"></a>

### proc-000335 — Лечение Actor: формула и верхний предел

calculateHealValue(value); общий вычислитель расходника и periodic heal, не onHeal чата.

<a id="proc-000336"></a>

### proc-000336 — Лечение Actor: сообщение

createHealMessage(heal); отчёт combat/heal без кнопки применения.

<a id="proc-000337"></a>

### proc-000337 — Лист: открыть окно лечения

click .heal-button; callback heal выполняется после render и регистрации DOM.

<a id="proc-000338"></a>

### proc-000338 — Окно лечения: применить

DialogV2 action heal; реальные два checkbox читаются при callback.

<a id="proc-000339"></a>

### proc-000339 — Окно лечения: пересчитать сумму и подпись

Change любого из четырёх checkbox; async без await.

<a id="proc-000340"></a>

### proc-000340 — Отдых: ресурсы, травмы и отчёт

recoverActor(isResting,isSterilized,dialogData); эффект ресурсов не зависит от resting.

<a id="proc-000341"></a>

### proc-000341 — Лист: регистрация кнопки лечения

activateListeners общего листа; наличие метода не добавляет кнопку Monster.

<a id="proc-000342"></a>

### proc-000342 — Окно лечения: регистрация change

Вызов после render, parameter html здесь global document.

<a id="proc-000343"></a>

### proc-000343 — Лечение: change resting

DOM change callback; передаёт общий контекст.

<a id="proc-000344"></a>

### proc-000344 — Лечение: change sterilized

DOM change callback; передаёт общий контекст.

<a id="proc-000345"></a>

### proc-000345 — Лечение: change healing-hand

DOM change callback; передаёт общий контекст.

<a id="proc-000346"></a>

### proc-000346 — Лечение: change healing-tent

DOM change callback; передаёт общий контекст.

<a id="proc-000347"></a>

### proc-000347 — Чат: применить лечение к выбранной цели

chatMessageListeners зарегистрировал первый button.heal; источник не определяет target.

<a id="proc-000348"></a>

### proc-000348 — Combat: регенерация монстра

applyGeneralCombatHooks activeGM запускает без await; любое прошедшее updateCombat.

<a id="proc-000349"></a>

### proc-000349 — Combat: периодическая ветвь лечения

Продолжение proc-000311 после damage/его пропуска; status guard и сообщение ранее.

<a id="proc-000350"></a>

### proc-000350 — Спасброски: death-reset

click death-minus/plus; не выполняет бросок.

<a id="proc-000351"></a>

### proc-000351 — Спасброски: death-plus

click death-minus/plus; не выполняет бросок.

<a id="proc-000352"></a>

### proc-000352 — Спасбросок смерти: порог и бросок

click death-roll; возвращение extendedRoll не изменяет dead/count.

<a id="proc-000353"></a>

### proc-000353 — Лист: регистрация спасброска и счётчика

Общий Actor sheet V2/V1 вызывает deathSaveListener.

## Проверки

Пройдены все 179 тестовых методов, включая 517 CLI-примеров (32 новых). Полный набор unittest discovery выполнен четырьмя независимыми группами модулей за 407.793 с; все группы завершились успешно. Это проверки справочника по исходникам, без исполнения игрового сценария.

До публикации прошли 32 новых CLI-ожидания и восемь проверок .022; затем 132 проверки расширений без CLI (60.447 с). Сверены определения, оба конца отношений и обратный поиск, достижимость шагов/выходов и три аспекта покрытия 615 sources. Все 334 прежних процесса и 11605 прежних отношений сохранены как записи. Восемь прежних сущностей уточнены с сохранением ID/owner/kind; onHeal/applyMonsterRegeneration/recoverActor раскрыты по прежним адресам.

Все 485 прежних CLI-примеров сохранены побайтно и прошли на предназначенных им срезах. Сравнение полной текущей выдачи выявило дополнительный proc-000352 у RollConfig.threshold; PR-04 относится к пилотному набору и поэтому его ожидания не менялись. Исторические численные итоги .021 закреплены диапазонами ID; две проверки .020 теперь проверяют начало существующих методов вместо длины прежней заглушки. Полные тела дополнительно проверяет .022. Код query.py и смысл CLI сохранены.

После проверки добавлены результаты, навигация и её контрольные суммы; итоговая актуальность, ссылки и сохранность приведены в протоколе.


## Итог и следующая порция

Добавлены 51 сущность, 203 отношения, 19 процессов и 10 динамических границ. Накоплено 4579 сущностей, 11808 связей и 353 процесса (1138 шагов, 2092 перехода); 339 границ. Определения есть в 252/615 файлах: два словаря complete по строковым ключам, 250 файлов partial; роли 149 основных/103 смежных, 363 без определений.

TASK-0006.022 done; следующая — [TASK-0006.023](../../tasks/task-0006.023.md), накопленная проверка связей предметов, боя и восстановления. Родитель остаётся in-progress. [Итоговая сверка](review-log.md#task-0006022).
