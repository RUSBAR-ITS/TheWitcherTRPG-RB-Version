# TASK-0006.016 — Защита, критический результат и выбор локации

2026-09-15; rusbar-main, исходный HEAD 574af24e57d57ded1dfa5d39a6090e9b1d7dad81; рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.016.md).

## Область и остаток

Десять основных исходников и выбранные смежные области. Схема v1 и CLI сохранены; полный индекс остаётся partial. Все новые определения основаны на чтении текущего кода, без нового исполнения боя в Foundry.

| Основной источник | Область / остаток |
| --- | --- |
| [module/actor/mixins/defenseMixin.js](../../../module/actor/mixins/defenseMixin.js) (src-000016) | Все 11 методов и два callback раскрыты в .016; дальнейшие HP/травмы, удалённые query и runtime мира вне порции. |
| [module/item/mixins/defenseOptionMixin.js](../../../module/item/mixins/defenseOptionMixin.js) (src-000160) | Полный wrapper и Weapon/Profession контракты; все внешние Item типы и UI не объявлены покрытыми. |
| [module/actor/mixins/locationMixin.js](../../../module/actor/mixins/locationMixin.js) (src-000018) | Оба wrapper и static назначения; прочие callers/lifecycle и RNG-распределение не проверены. |
| [module/actor/witcherActor.js](../../../module/actor/witcherActor.js) (src-000047) | Оба location static раскрыты вместе с прежними областями Actor; полный Actor lifecycle/урон не объявлены покрытыми. |
| [module/data/chatMessage/defenseMessageData.js](../../../module/data/chatMessage/defenseMessageData.js) (src-000097) | Схема и getter, producer/выбранные consumers; полная доставка/история/права сообщений вне порции. |
| [module/data/chatMessage/templates/critData.js](../../../module/data/chatMessage/templates/critData.js) (src-000099) | Существующая фабрика damage.crit .015 переиспользована, чтения модификаторов защитой раскрыты; не schema DefenseMessageData. |
| [module/data/chatMessage/templates/locationData.js](../../../module/data/chatMessage/templates/locationData.js) (src-000101) | Существующая фабрика damage.location .015 переиспользована; static producer и отличие defense crit.location адресованы. |
| [templates/chat/combat/defense/defense.hbs](../../../templates/chat/combat/defense/defense.hbs) (src-000482) | Обе строки: defenseName и displayFormula из skillDefense; дальнейшие события чата вне шаблона. |
| [templates/chat/combat/defense/defenseCrit.hbs](../../../templates/chat/combat/defense/defenseCrit.hbs) (src-000483) | Условие crit, подпись тяжести, .crit-taken и button.crit-stun; dataset отсутствует, действие использует message.system.crit. |
| [templates/chat/combat/defense/defenseStun.hbs](../../../templates/chat/combat/defense/defenseStun.hbs) (src-000484) | Условие stun, подпись modifier и button.stun; callback читает attackWeaponProperties.stun из сообщения. |

## Существенные различия

- prepareAndExecuteDefense берёт стандартные options через CONFIG.find и дополнительные из всех Actor.items с system.isApplicableDefense. crushingForce удаляет только parry; isStored/equipped в дополнительном отборе не проверяются. getList(shield) и getList(weapon) имеют разные фильтры.
- Item wrapper задаёт label/value именем, затем модель может переопределить поля. Weapon/DefenseProperties переиспользуют .014. Profession перебирает только девять навыков путей, берёт первый; definingSkill и isDefense не участвуют. skillOverride — отдельный объект, а не стандартный skillName.
- Первый Dialog возвращает defenseAction/extra.checked/custom.value. chooser собирает skills и предметы без ammo: ноль оставляет undefined, один обходится без окна, несколько дают HTML select. data-itemId нормализуется в dataset.itemid; пункт навыка может вернуть строку undefined. Ни пустые, ни неизвестные варианты заранее не отсекаются.
- Extra defense запрашивает STA−1 до проверки skillMapEntry. Отказ при отрицательном остатке возвращает false; update не ожидается. Отмена обоих окон происходит раньше расхода. Подписи/controls сами не сохраняют документы.
- Формула: stat+skill либо override, signed action modifier, компенсация штрафа парирующим предметом, customDef, lifepath, skill AE и combat modifiers. Собственный defenseMixin.addDefenseModifiers побеждает одноимённый modifierMixin; положительное значение не получает оператор +. Shield thrown ветка ищет parrythrown, CONFIG задаёт parryThrown.
- В профессиональной ветви skillName может быть undefined, но основа работает через override. addActiveEffects получает этот же undefined, общие модификаторы добавляются. Активный stun заменяет всю строку на 10[Stun], кроме skillName=resistmagic. displayFormula показывает только названия основы, а не окончательный бросок.
- createDefenseRollConfig устанавливает defense=true, threshold=totalAttack, showResult=false; поэтому равенство считается успешной защитой. extendedRoll возвращает результат без публикации; skillDefense затем добавляет crit/stun и отдельно ждёт Roll.toMessage. Окончательный return метода — undefined.
- Разность атака−защита >=7/10/13/15 даёт simple/complex/difficult/deadly с critdamage3/5/8/10 и bonusdamage5/10/15/20. При originalLocation.includes(random) бросается 2d6+critLocationModifier; иначе используется прежний объект location по ссылке. Ни этот выбор, ни checkForCrit не вызывают RollTable.
- Raw crit.location заменяет исходный prepared attackDamageObject.location. critEffectModifier переносится в raw crit; DefenseMessageData объявляет собственные crit/location и удаляет это поле. Общие chat.critData()/chat.locationData() не включены в defense schema; modifier зоны здесь Number, в damage.location String.
- Запрос addAdrenaline отправляется атакующему через fromUuidSync/getActorOwner до окончательного сообщения и без await. Отсутствие Actor/получателя может прервать путь; сам запрос не доказывает исполнения или прироста кубов. Полный query/настройка/сохранение остаются прежними границами.
- После сообщения handleDefenseResults различает roll.total<totalAttack и остальные случаи. Попадание запускает applyOnHit с itemUuid/duration и снятие stun. Успех может дать stagger атакующему и/или износ Item: armor.reliability либо weapon.reliable минус1, crushingForce минус2. Update не ожидается, нижнего ограничения нет; brawling block не имеет Item и падает на item.type.
- checkForStun получает только location/properties: torso/head и truthy stun создают предложение независимо от успеха защиты. Его кнопка не накладывает статус. stunSave — отдельный 1d10 с showCrit=false/reversal=true/defense=false; при неотрицательном пороге успех строго меньше, равенство — неуспех. Неуспех вызывает applyStatus без await, успех не снимает прежний stun.
- defense.hbs получает имя и displayFormula. defenseCrit.hbs получает только тяжесть для подписи; полный crit передаётся через system. Ни crit, ни stun не лежат в dataset этих кнопок. .crit-taken — маркер меню, callback читает очищенный message.system.crit. stun-кнопка читает attackWeaponProperties.stun, а не выведенный текст или system.stun.modifier.
- Chat callbacks заново выбирают Actor через getInteractActor; defender UUID не определяет адресата. crit-stun передаёт default0. Критические действия вызывают applyCritDamage/applyBonusCritDamage/applyCritWound отдельно; появление crit не означает автоматического получения травмы. Адреса consumer сохранены, полные алгоритмы .021 не развёрнуты.
- getAllLocations wrapper вызывает static на классе; hasTailWing конкретного Monster не добавляет седьмую зону. getLocationObject(tailWing) и randomMonster10 отдельно поддерживают хвост. Неизвестное имя сохраняет name при torso-подобных числах; randomMonster9 даёт leftLeg независимо от справочного экспорта RollTable.
- defenseFumble раскрывает адрес, оставленный границей в .015; её ID сохранён и связан с реальной функцией. Это отдельное действие меню. <6 даёт nothing; armed <9 использует число, иначе >9; остальные навыки идут в прежний unarmed helper. Текстовый createResultMessage и его UUID/getSpeaker граница переиспользуются.

## Доказательства и границы

Прочитаны выбранные исходники, поздние карточки TASK-0004.010/.011 и R010-07–13. Сопоставлены полные issues 00032/00071/00072/00079/00085/00185 и 00268–00276; доказательства ранее прочитанных 00031/00033/00182/00257/00258 переиспользованы при неизменных файлах. Поздние .042/.043/.045/.057 уточнения сохраняют даты и ограничения своих фасадов. Новых issues и поведенческих запусков нет; статусы potential сохранены.

В этой порции дополнительно прочитано тело DialogV2 initializer: непустые buttons и reduce по action. Browser sanitization, DOM, DB, права, сетевые клиенты, распределение RNG и соответствие чисел книгам не проверялись. Прежняя граница SchemaField.clean переиспользована; установка ядра не изменялась.

| Внешний файл | Область | SHA-256 |
| --- | --- | --- |
| /opt/foundryvtt/client/applications/api/dialog.mjs | _initializeApplicationOptions:184–200; только чтение | 4e2d299eaa931d96df1839e64a2defc60b6b95ee89a3e1d32d60b99040899343 |

## Процессы

<a id="proc-000190"></a>

### proc-000190 — Защита: способ и средство

Вход из executeDefense с пятью полями сообщения атаки; при успехе возвращает Promise skillDefense.

<a id="proc-000191"></a>

### proc-000191 — Item: дополнительный вариант защиты

Actor уже проверил system.isApplicableDefense; wrapper сам не выполняет отбор.

<a id="proc-000192"></a>

### proc-000192 — Профессия: первый доступный защитный навык

Выбранный модельный контракт защиты; полный profession UI/боевые навыки вне порции.

<a id="proc-000193"></a>

### proc-000193 — Профессия: данные выбранной защиты

Уже найденные path/skill; флаг isDefense здесь не проверяется.

<a id="proc-000194"></a>

### proc-000194 — Защита: стоимость дополнительной попытки

extraDefense boolean; запись STA не является частью результата Roll.

<a id="proc-000195"></a>

### proc-000195 — Защита: формула и замена при оглушении

После успешного handleExtraDefense; обе основы, обычная и skillOverride, используют выбранные входы.

<a id="proc-000196"></a>

### proc-000196 — Защита: бонусы щита из биографии

Конкретные action/additionalTag; ожидаемые из CONFIG имена не исправляются.

<a id="proc-000197"></a>

### proc-000197 — Защита: конфигурация общего броска

Общий extendedRoll остаётся прежним процессом; сравнение защиты включает равенство.

<a id="proc-000198"></a>

### proc-000198 — Защита: от формулы до последствий

skillDefense после chooser; сообщение и запрошенные изменения состояния имеют разные границы ожидания.

<a id="proc-000199"></a>

### proc-000199 — Защита: критическая тяжесть

Разность totalAttack−defenseRoll; чистые числовые сравнения, без RollTable.

<a id="proc-000200"></a>

### proc-000200 — Защита: локация критического результата

Исходная строка содержит random → собственный Roll; прочие значения возвращают существующий объект.

<a id="proc-000201"></a>

### proc-000201 — Защита: предложение оглушения

Результат Roll не является аргументом; предложение не накладывает статус.

<a id="proc-000202"></a>

### proc-000202 — Защита: реакции попадания и блока

Запускается после await сообщения; все дочерние update/query/effect/status Promise здесь не ожидаются.

<a id="proc-000203"></a>

### proc-000203 — Защита: спасбросок оглушения

Отдельный вызов с modifier=0 по умолчанию; при неотрицательном пороге strict<, равенство неуспех.

<a id="proc-000204"></a>

### proc-000204 — Локации: перечисление через static

Wrapper вызывается на Actor, но не передаёт его this статическому методу.

<a id="proc-000205"></a>

### proc-000205 — Локации: объект зоны или случайный исход

Статический resolver; это собственные ветки исходника, не RollTable из компедиума.

<a id="proc-000206"></a>

### proc-000206 — Сообщение защиты: собственная схема

Схема не включает общие critData/locationData и не объявляет critEffectModifier.

<a id="proc-000207"></a>

### proc-000207 — Сообщение защиты: псевдоним результата

Getter attackRoll возвращает итог этого сообщения защиты.

<a id="proc-000208"></a>

### proc-000208 — Чат защиты: оглушение от свойства

DOM callback связан с выбранным message; Actor определяется заново при клике.

<a id="proc-000209"></a>

### proc-000209 — Чат защиты: оглушение от критического результата

DOM callback связан с выбранным message; Actor определяется заново при клике.

<a id="proc-000210"></a>

### proc-000210 — Чат защиты: адреса критических действий

Menu visibility .crit-taken; три независимых onClick, не автоматическое получение травмы.

<a id="proc-000211"></a>

### proc-000211 — Провал защиты: выбор текста

Отдельный пункт fumble меню .015; точный constructor DefenseMessageData.

## Проверки

Пройдены все 126 тестовых методов (unittest, 731.738 с), включая 28 новых CLI-случаев; накоплено 329 CLI-примеров. Это проверки справочника по исходникам, без исполнения игрового сценария.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
git diff --check
~~~

Перед общим прогоном все 28 новых ожиданий сопоставлены с запросами к временному набору, семь отдельных проверок новой порции прошли. Проверены choice/override, формула и расход STA, пороги crit, отличие raw payload от схемы сообщения, износ и stunSave, статический контекст локаций, выбранные callbacks чата и внешний контракт DialogV2. Шаги новых процессов достижимы; все их отношения исходят от сущности шага и адресованы внутри его диапазона. Все 9766 отношений проверены в обоих направлениях, три аспекта покрытия — для 615 источников.

Накопительный X006-10 дополнен прямым читателем displayRollsDetails — skillDefense:131. Численные итоги .015 теперь проверяются по историческому диапазону ID, содержательные проверки сохранены. Исторические наборы пилота и его процессов не менялись. Эти уточнения выполнены до общего прогона; результат всех 126 методов успешен.

Итоговая актуальность, ссылки и сохранность после обновления навигации приведены в журнале. Проверки не исполняют JavaScript боя, не сохраняют документы мира и не подтверждают межклиентскую доставку.


## Итог и следующая порция

Добавлены 98 сущностей, 339 отношений и 22 процесса; шесть новых внешних/динамических границ. Накоплено 4120 сущностей, 9766 связей и 211 процессов (770 шагов, 1344 перехода); 278 границ. Определения есть в 224/615 файлах: два словаря complete по строковым ключам, 222 файла partial; роли 103 основных/121 смежный, 391 без определений.

TASK-0006.016 done; следующая — [TASK-0006.017](../../tasks/task-0006.017.md), бросок урона и контракты боевых сообщений. Родитель остаётся in-progress. Окончательная сверка — в [журнале](review-log.md#task-0006016).
