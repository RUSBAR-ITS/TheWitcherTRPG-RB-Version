# TASK-0006.019 — Применение урона, щит и изменение ресурсов

2026-09-15; rusbar-main, исходный HEAD 66ce051d648088488966465cbea06dd8c4744c5e; рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.019.md).

## Область и остаток

Девять основных исходников и выбранные смежные участки. Схема v1 и CLI сохраняются; весь справочник partial. Это индекс текущего кода, без исполнения игрового сценария и без изменения механик.

| Основной источник | Включено / границы |
| --- | --- |
| [module/actor/mixins/damageMixin.js](../../../module/actor/mixins/damageMixin.js) (src-000014) | Полные applyDamage/handleShield/одна и все зоны/updateDerivedStat/расчёт/два отчёта. Crit damage/bonus представлены точными вызовами; полные травмы/calculateHealingTime остаются .021, фактическая запись мира не проверена. |
| [module/actor/mixins/damageUtilMixin.js](../../../module/actor/mixins/damageUtilMixin.js) (src-000015) | Оба getter и стыки их применения; getMultiDamageMod/proc-000268 переиспользованы. Все возможные значения произвольного damage.type и внешние callers не перечислены. |
| [module/data/actor/templates/character/general/damage/damageModificationData.js](../../../module/data/actor/templates/character/general/damage/damageModificationData.js) (src-000062) | Вся фабрика flat/multiplication/applyAP и выбранные consumers; полная работа произвольных эффектов/мира остаётся внешней областью. |
| [module/data/actor/templates/character/general/damage/damageTypeModificationData.js](../../../module/data/actor/templates/character/general/damage/damageTypeModificationData.js) (src-000063) | Все семь SchemaField и фабричные связи, CommonActorData и выбранные getters; CONFIG не является источником ключей. |
| [module/scripts/combat/applyDamage.js](../../../module/scripts/combat/applyDamage.js) (src-000194) | Все функции, два menu callback, диалог/его callback, message/status/HP/STA маршруты. Регистрация меню .006/.017 переиспользована; полный чат/ход/доставка остаются .020. |
| [templates/chat/damage/damageToAllLocations.hbs](../../../templates/chat/damage/damageToAllLocations.hbs) (src-000490) | Весь короткий HBS: totalAppliedDamage, raw results, alias и partial; живой рендер/стили/санитизация не проверены. |
| [templates/chat/damage/damageToLocation.hbs](../../../templates/chat/damage/damageToLocation.hbs) (src-000491) | Все поля, условные флаги и localize основной подробности; прочитаны оба различных producer. Браузер/чат не исполнены. |
| [templates/chat/damage/shieldAbsorbs.hbs](../../../templates/chat/damage/shieldAbsorbs.hbs) (src-000492) | Все поля и localize отдельного shield отчёта; prepared shield в контексте отделён от запрошенной записи. |
| [templates/chat/damage/spAbsorbs.hbs](../../../templates/chat/damage/spAbsorbs.hbs) (src-000493) | Все поля и localize отдельного blocked-SP отчёта; внешний applyDamage продолжает эффекты. |

## Контракты и существенные различия

- Входы сообщения и статуса различаются. Два menu callback ждут getInteractActor, затем берут первый parseInt(.dice-total.innerText) и li.dataset.messageId. Marker .damage-message сам не доказывает наличие числа/Actor. Normal выбирает hp/sta по prepared isNonLethal; NonLethal всегда sta. Их вложенные Promise не возвращаются вызывающей стороне.
- Диалог содержит Empty и семь локаций; это не динамический getAllLocations. Только monster получает defaults resistantNonSilver/Meteorite. Vulnerable/oil изначально не отмечены. Callback возвращает пять полей; недоступные monster checkbox дают undefined. rejectClose отклоняет prompt; внешняя обёртка этого завершения не ждёт.
- applyDamageFromMessage держит ссылку на message.system.damage. Не-Empty заменяет prepared location; addOilDmg записывает category. Empty/false не отменяют прошлые изменения. Message.update отсутствует; время жизни prepared объекта после реальной переподготовки не исследовано. Каждый вызов создаёт новый DamageInstance, но payload сообщения может быть прежним.
- applyDamageFromStatus пропускает сообщение и диалог, передаёт null и заданный ресурс. applyCombatEffect создаёт properties/location без damage.type, поэтому setType получает undefined. Его сумма amount+(modifier??0) может быть отрицательной при положительном amount. Полный ход/регенерация/транспорт остаются .020.
- handleShield вызывается всегда и раньше bypassesShield. Флаг лишь отменяет последующий early return при отсутствии положительного урона. Щит общий для массива; отрицательный instance может увеличить локальный бюджет. Actor.update щита не ожидается. Отчёт создаётся при локальном остатке>0 и читает текущий prepared shield, который может быть прежним.
- Oil +5 добавляется после щита при truthy категории и точном совпадении properties.oilEffect. Затем одна/все локации ожидаются. Полный blocked-SP return одиночной обёртки не останавливает внешний applyDamage: applied statusEffect и Item applyOnDamage запускаются без await. Полное поглощение щитом может остановить весь внешний путь раньше.
- calculateDamageWithLocation захватывает properties/location до await, затем выполняет SP/IAP → режим серебра → поглощение SP по порциям → прямой износ → blocked return либо положительный flat → коэффициент локации → сопротивления/уязвимость → обычный износ → result. Настройка silverTrait присваивает setType строке; альтернативный strong суффикс *2 не заключает составной silverDamage в скобки.
- Flat читается по общему damage.type и применяется только при >0 после проверки SP. Новый flat имеет type=null, oil — type=oil; обоих нет в CONFIG.damageTypes. Условное чтение likeSilver/likeMeteorite может прерваться на undefined. Множитель остаётся только в ветвях armor resistance; AP/IAP и различия общего/порционного типа переиспользуют .018.
- Все локации получают один damage и один массив DamageInstance. Запись damage.location меняется в цикле; локально захваченная location не изолирует экземпляры. Promise.all ждёт результаты, но они продолжают ссылаться на общие экземпляры. Суммирование берёт поздние значения каждого result; blocked результаты тоже участвуют. Чат allLocations ожидается перед ресурсом, одиночные сообщения запускаются без await.
- updateDerivedStat округляет damage вниз. Только hp отбирает Actor.temporaryEffects по наличию любого key с temporaryHp; затем расходует все changes выбранного эффекта. JSON.parse без проверки типа/формы, JSON.stringify и await update каждого эффекта; при damage0 цикл не прерывается, пустой эффект не удаляется. JSON внутри change.value и схема prepared TemporaryEffects — разные контейнеры.
- Корневой update({changes: tempHp.system.changes}) не включает applyAfterCalculations. Миграция ядра14 и системный _preUpdate — внешняя цепочка с ранее проверенными границами .007/.008 и issues00043/00294. Ошибка объекта value после миграции, неправильная строка producer и расход чужих changes — разные условия; новых запусков ядра/БД здесь нет.
- Конечный Actor.update ожидается и пишет абсолютное текущее derivedStats[derivedStat].value минус остаток. Сам метод не вводит min/max и не валидирует динамический ключ; штатные выбранные callers дают hp/sta. Внешние status/message/crit wrappers не передают ожидание этого результата. Износ SP, запись shield, запись ActiveEffect и HP/STA имеют самостоятельные границы завершения.
- Обычный result содержит properties, но одиночный message producer читает damageResult.damageProperties. AllLocations передаёт raw result в тот же partial без пяти готовых строк стадий. Ошибка представления отделена от совместного использования порций. Shield/SP отчёты имеют собственные корректно адресованные поля; их создание не означает применение ресурса.
- Семь типов damageTypeModification заданы фиксированными SchemaField в CommonActorData, каждый с flat0/multiplication1/applyAPfalse. Это не список CONFIG, он не получает автоматически silver/oil/acid. Переиспользованы прежние владельцы и getter множителя; два ранних определения applyDamage/updateDerivedStat уточнены до методов damageMixin с сохранением ID и двух defines-ID.

## Доказательства и ограничения

Прочитаны девять основных исходников, выбранные поставщики/потребители и поздние карточки TASK-0004.003/.011; R011-10–17/19. Исходники сопоставлены с текущим индексом .018. Прежние опыты аудита сохраняют даты, подмены и ограничения; новых запусков JavaScript, браузера, мира, БД или боевого клиента нет.
Полные связанные issues прочитаны: 00021/00023/00027/00043/00073/00117/00149/00257, 00284–00287, 00290–00292, 00294, 00298–00301. Ранее прочитанные 00025/00026/00280/00282/00283 и их границы .018 переиспользованы без изменения. Полные области травм, отдыха, магии, профессий и чата не объявляются покрытыми. Статусы issues остаются potential; новые карточки и исправления не создавались.
Дополнительно прочитан внешний ChatMessage.applyMode: /opt/foundryvtt/client/documents/chat-message.mjs:144–150,165–190; SHA256 446c041c59b3f097e5c3358a528181e368e072be9cfe55fa928fa92932e55c5b. Он меняет тот же chatData через режим/whisper/blind/style либо cfg.handler и не сохраняет сообщение. Создана явная внешняя граница; выполнение custom handler и ядра не воспроизводилось. Коллекция temporaryEffects, Document.update/ActiveEffect, Actor.update, DialogV2, Roll, renderTemplate и остальные ChatMessage API — переиспользованные внешние контракты. Актуальность package подтверждает версию, а не весь lifecycle. Чтение кода и успешный поиск не подтверждают завершённую запись, межклиентский порядок или отсутствие иных динамических callers.

## Процессы

<a id="proc-000269"></a>

### proc-000269 — Урон: щит, локации и последующие эффекты

Actor.applyDamage(dialogData, instances, damageObject, derivedStat); normal/status/crit имеют разные payload.

<a id="proc-000270"></a>

### proc-000270 — Урон: поглощение щитом

Общий ресурс derivedStats.shield, не Item с location Shield.

<a id="proc-000271"></a>

### proc-000271 — Урон: применение к одной локации

Одиночный расчёт и отчёт; blocked-SP не прекращает внешний applyDamage.

<a id="proc-000272"></a>

### proc-000272 — Урон: применение ко всем локациям

Локальная location захватывается каждым расчётом, но массив и экземпляры общие; Promise.all не изолирует данные.

<a id="proc-000273"></a>

### proc-000273 — Урон: временные HP и конечный ресурс

Обрабатывает JSON всех changes выбранного временного эффекта; не читает напрямую prepared temporaryHp pool.

<a id="proc-000274"></a>

### proc-000274 — Урон: расчёт выбранной локации

Полный локальный расчёт до result; ожидаемые SP-обёртки не гарантируют завершения дочернего износа .018.

<a id="proc-000275"></a>

### proc-000275 — Отчёт: поглощение SP

Самостоятельный отчёт с двумя полями; вызывается без await из одной локации.

<a id="proc-000276"></a>

### proc-000276 — Отчёт: стадии одной локации

Строки стадий готовятся только здесь; неправильное имя поля properties сохранено в графе как граница.

<a id="proc-000277"></a>

### proc-000277 — Урон: фиксированная модификация типа

Lookup по внешнему damage.type; знак передаётся caller без изменения.

<a id="proc-000278"></a>

### proc-000278 — Модификация урона: тройка полей

Фабрика схемы, не применение игрового эффекта.

<a id="proc-000279"></a>

### proc-000279 — Модификация урона: семь типов

Фиксированные поля CommonActorData; не динамический список CONFIG.

<a id="proc-000280"></a>

### proc-000280 — Чат: обычное нанесение урона

Callback получает li от внешнего меню; прежняя регистрация proc-000230 сохранена.

<a id="proc-000281"></a>

### proc-000281 — Чат: несмертельное нанесение урона

Callback получает li от внешнего меню; прежняя регистрация proc-000230 сохранена.

<a id="proc-000282"></a>

### proc-000282 — Вход урона: ApplyNormalDamage

Promise<void> обёртки не включает диалог/Actor.applyDamage.

<a id="proc-000283"></a>

### proc-000283 — Вход урона: ApplyNonLethalDamage

Promise<void> обёртки не включает диалог/Actor.applyDamage.

<a id="proc-000284"></a>

### proc-000284 — Урон: диалог цели и локации

Восемь location option и четыре checkbox; выбор не пишет документ сам.

<a id="proc-000285"></a>

### proc-000285 — Урон: чтение формы подтверждения

Отдельный callback prompt; до подтверждения не выполняется.

<a id="proc-000286"></a>

### proc-000286 — Урон: применение prepared сообщения

Ссылка на system.damage, отдельный runtime DamageInstance; без ChatMessage.update.

<a id="proc-000287"></a>

### proc-000287 — Урон: прямой статусный вход

Пропускает диалог и типизированное сообщение; тип берётся из plain damageObject.

<a id="proc-000288"></a>

### proc-000288 — Шаблон урона: damageToAllLocations

Вызов Handlebars с подготовленным контекстом; живой DOM/санитизация/чат не исполнялись.

<a id="proc-000289"></a>

### proc-000289 — Шаблон урона: damageToLocation

Вызов Handlebars с подготовленным контекстом; живой DOM/санитизация/чат не исполнялись.

<a id="proc-000290"></a>

### proc-000290 — Шаблон урона: shieldAbsorbs

Вызов Handlebars с подготовленным контекстом; живой DOM/санитизация/чат не исполнялись.

<a id="proc-000291"></a>

### proc-000291 — Шаблон урона: spAbsorbs

Вызов Handlebars с подготовленным контекстом; живой DOM/санитизация/чат не исполнялись.

## Проверки

Пройдены все 153 тестовых метода (unittest, 1103.282 с), включая 32 новых CLI-случая; накоплен 421 CLI-пример. Это проверки справочника по исходникам, без исполнения игрового сценария.

~~~bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
python3 -B docs/analytics/system-index/query.py check --freshness --format json
git diff --check
~~~

До общего прогона прошли 32 новых ожидания поиска и девять отдельных проверок .019: владельцы/схемы, меню/диалог, message/status, shield/ожидания, локация/последующие эффекты, общие экземпляры allLocations, временные HP/ресурс, контексты отчётов и накопленный граф. Проверка прямых calls уточнила маршрут через actor.locationMixin, который вызывает static WitcherActor; прежние ID обёрток сохранены.

Новые ожидания сопоставлены с исходниками. У 373 прежних накопленных примеров не изменились проверяемые списки ID/концов связей; 16 исходных примеров проверены отдельно на seed-наборе. Исторический EX-02 с полями value не переносится на накопленную выдачу автоматически: .019 добавляет отдельные JSON/container поля. Первоначальный общий прогон обнаружил два устаревших тестовых предположения и был остановлен: счётчик value в .008 и owner .012, отсутствующий в историческом срезе .009. Уточнены только исторические фикстуры; прежние ожидаемые ответы и текущие фактические владельцы сохранены. Численные итоги .018 также закреплены историческим диапазоном. Полный успешный прогон выполнен после этих правок.

Проверены прямые и обратные связи (11181 отношение), принадлежность шагов/отношений, достижимость выходов и три аспекта покрытия 615 sources. Прежние 268 процессов и 10832 отношения неизменны; у rel-002171/rel-002193 уточнён только владелец defines на damageMixin. Семнадцать прежних сущностей уточнены с сохранением ID. Ссылки, окончательная актуальность и сохранность после обновления навигации записаны в журнале. Тесты не исполняют браузер, игровой JavaScript, сохранение в мире или доставку между клиентами.


## Итог и следующая порция

Добавлены 73 сущности, 347 отношений и 23 процесса; 13 новых динамических/внешних границ. Накоплено 4403 сущности, 11181 связь и 291 процесс (989 шагов, 1778 переходов); 305 границ. Определения есть в 239/615 файлах: два словаря complete по строковым ключам, 237 файлов partial; роли 128 основных/111 смежных, 376 без определений.

TASK-0006.019 done; следующая — [TASK-0006.020](../../tasks/task-0006.020.md), действия чата, GM-доставка и начало хода. Родитель остаётся in-progress. Окончательная сверка — в [журнале](review-log.md#task-0006019).
