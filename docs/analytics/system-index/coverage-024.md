# TASK-0006.024 — Ручные ресурсы Actor и общая форма

2026-09-15; rusbar-main, исходный HEAD `b4dc32e5fb85529abba08a5ac96cd89cfb3a3087`; рабочее дерево в начале чистое. [Задача](../../tasks/task-0006.024.md), [запросы](examples/expansion-024-queries.json), [проверки](tests/test_expansion_024.py).

## Результат и границы

Добавлены 55 сущностей, 267 отношений и 10 процессов. Накоплено 4634 сущности, 12075 отношений и 363 процесса; 344 границы. Основных источников 151, смежных 103, без определений 361; определения в 254/615 файлах. Два словаря en/ru сохраняют complete по строкам, остальные определения partial. Участие файла или поле общей фабрики не означает полного покрытия всех его потребителей.

Сопоставлены все 22 именованных input двух sidebar, их схема, prepared значение, внешний writer и прежние расчёты/программные writers. Vigor — отображение max, временный HP — отдельная сумма. Раскрыты callbacks REC/full recovery V2/V1. Формат v1, CLI и постоянные ID сохранены.

| Основной файл | Включено и остаток |
| --- | --- |
| [module/actor/sheets/WitcherActorSheet.js](../../../module/actor/sheets/WitcherActorSheet.js) (src-000027) | Раскрыты DEFAULT_OPTIONS.form, _onRender/activateListeners в ресурсной части и весь _onRecoverSta с обоими callback. Прежние предметы/эффекты/навыки сохранены; жизнь/магия/прочие действия и все читатели контекста не исчерпаны. |
| [module/actor/sheets/WitcherActorSheetV1.js](../../../module/actor/sheets/WitcherActorSheetV1.js) (src-000028) | Отдельно раскрыт _onRecoverSta и recovery bind V1; собственный шаблон и текущая регистрация отсутствуют. Полный V1 form lifecycle и прочие методы/контексты вне выбранных путей. |
| [module/actor/sheets/WitcherCharacterSheet.js](../../../module/actor/sheets/WitcherCharacterSheet.js) (src-000029) | PARTS.sidebar/header и наследование V2 связаны с ресурсными controls и подготовкой; остальные вкладки/крафт/IP/профессии остаются последующим порциям. |
| [module/actor/sheets/WitcherMonsterSheet.js](../../../module/actor/sheets/WitcherMonsterSheet.js) (src-000031) | PARTS.sidebar/header, наследование и общий контекст ресурсов; отдельной кнопки recover-sta в header нет. Loot/export и прочие действия/читатели ещё не полностью индексированы. |
| [module/data/actor/commonActorData.js](../../../module/data/actor/commonActorData.js) (src-000055) | Ресурсные вложения/healthState и prepareBaseData переиспользованы; manual ignored адресованы конкретно. Прочие общие поля/потребители остаются частичными. |
| [module/data/actor/monsterData.js](../../../module/data/actor/monsterData.js) (src-000057) | Поля естественной брони связаны с четырьмя input, customStat сохранён как режим расчёта максимумов. Полное редактирование/потребители остальной схемы не входят. |
| [module/data/actor/templates/common/stats/derivedStatsData.js](../../../module/data/actor/templates/common/stats/derivedStatsData.js) (src-000089) | 12 контейнеров stat() и прежние расчёты/миграции; sidebar values/max/HP base сопоставлены без дублирования value. Все сторонние writers/readers и новые предметные области ещё не исчерпаны. |
| [module/data/actor/templates/common/stats/statData.js](../../../module/data/actor/templates/common/stats/statData.js) (src-000090) | Общая stat() схема и существующие поля переиспользованы; конкретные пути resources идут через контейнер/контекст связи. Полный список вызовов фабрики и сторонних readers/writers не заявлен. |
| [templates/sheets/actor/partials/character/sidebar.hbs](../../../templates/sheets/actor/partials/character/sidebar.hbs) (src-000560) | Все 10 именованных input (resolve/adrenaline условны), 5 progress, HP heart/temp sum/vigor и 4 кнопки luck/adrenaline адресованы. Изображение, все локализационные/CSS/helper связи и живая форма не покрыты полностью. |
| [templates/sheets/actor/partials/monster/sidebar.hbs](../../../templates/sheets/actor/partials/monster/sidebar.hbs) (src-000565) | Все 12 именованных input (resolve условен), 5 progress, HP heart/temp sum/vigor и четыре поля брони адресованы. Изображение/category, все локализационные/CSS/helper связи и живая форма не покрыты полностью. |

<a id="resource-fields"></a>
## Ручные поля и отображение

| Путь Actor | Character | Monster | Схема / представление |
| --- | --- | --- | --- |
| `system.derivedStats.hp.value`, `.sta.value` | Два number input | Два number input | stat().value initial0 без min/max/integer; HTML max99, progress/подпись читают текущий max |
| `system.stats.toxicity.value` | number | number | Stats.toxicity → stat(); HTML max из подготовленного toxicity.max |
| `system.derivedStats.focus.value` | number | number | HTML max из focus.max |
| `system.derivedStats.resolve.value` | При useVerbalCombat | При useVerbalCombat | HTML max из resolve.max; скрытого control нет |
| `system.derivedStats.shield.value` | number | number | Без HTML min/max; самостоятельный value, не временные HP |
| `system.healthState.woundThreshold.ignored`, `.deathState.ignored` | Два checkbox | Два checkbox | BooleanField; applied вычисляет Actor; это system.healthState, не flags |
| `system.stats.luck.value` | number + отдельные minus/reset | Нет | stat().value; кнопки .010 имеют собственные callbacks и ожидания |
| `system.adrenaline.value` | number + minus/plus при useAdrenaline | Нет | adrenaline().value без min/max; кнопки не эквивалентны submit формы |
| `system.armorHead`, `.armorUpper`, `.armorLower`, `.armorTailWing` | Нет | Четыре number | MonsterData NumberField initial0; hasTailWing не скрывает input |
| `system.derivedStats.vigor.max` | Только display | Только display | Truthiness: 0 скрыт, отрицательное значение показано. Нет input vigor.value/max |
| `temporaryHpSum` | Отдельное `+ сумма` при >=1 | То же | Вычисляется общим context; не прибавляется к input или progress HP |

Character: максимум 10 input, без resolve/adrenaline — 8. Monster: максимум 12, без resolve — 11. У всех numeric полей data-dtype Number; у двух healthState checkbox нет value attribute. Перечень относится к sidebar, а унаследованный submit собирает всю Actor-form, включая остальные вкладки. Полный набор полей этих вкладок здесь не заявлен.

Иконка сердца использует hp.unmodifiedMax и woundTreshold.value; полоса и числовой максимум — hp.max. Изображение, alt, category и оформление не превращены в новые ресурсные механики. Прежние issue-00203/00205 использованы с поздними уточнениями; повторного поведенческого опыта нет.

В графе input имеет собственный владелец-template, но не создаёт копию stat().value. `passes` связывает input с унаследованным сохранением; `writes` от `WitcherActorSheet/resource-form-submit` локализован на соответствующем control и содержит точный path/условия. Это связь внешнего проверенного writer с локальной формой, а не вызов update из HBS. Такой способ позволяет найти ручной writer по конкретному контейнеру и источнику формы.

<a id="core-form"></a>
## Внешний контракт общей формы

Установленное ядро Foundry 14.367.0. Слияние DEFAULT_OPTIONS сохраняет DocumentSheetV2.tag=form и handler; WitcherActorSheet меняет submitOnChange=true/closeOnSubmit=false. Character/Monster наследуют текущий V2; V1 не зарегистрирован и не задаёт своего template. Контракт V2 не перенесён на V1 как доказанный маршрут.

1. На форме зарегистрированы submit/change. DocumentSheet._onChangeForm передаёт обычные controls в ApplicationV2; секретный HTML имеет отдельную ветку вне выбранных inputs.
2. При RENDERED/CLOSING и submitOnChange _onChangeForm вызывает _onSubmitForm без await. Последний делает preventDefault и FormDataExtended(event.currentTarget), затем внутри try ожидает handler. Ошибка handler вызывает notification.error; сбор FormData находится перед try.
3. FormDataExtended обходит всю form.elements. Пропускает безымянные, уже обработанные имена, button/editor/disabled; readonly по умолчанию включены. Number/range: пустая строка → null, иначе Number(value). Checkbox без явного value возвращает checked как boolean. Произвольные повторяющиеся имена могут давать массив, но выбранные sidebar names уникальны.
4. #onSubmitDocumentForm проверяет isEditable, expandObject(formData.object), затем document.validate(changes, clean addTypes/copyfalse, fallbackfalse). Ручной updateData может дополнительно объединяться; обычный change его не передаёт.
5. _processSubmitData для document.collection.has(id) ожидает document.update(submitData,options). В ином случае ядро рассматривает canCreate и ошибку; это не штатная гарантия записи нового Actor. Сервер, права конкретного пользователя и фактические документы не исполнялись.

В прочитанных шагах form parser/change submit нет checkValidity/reportValidity и сравнения с HTML min/max. Это не утверждение об отсутствии любой браузерной валидации и не полный контракт NumberField: модель проверяется отдельно. Схема stat().value явно не задаёт общего динамического ограничения текущим max или числом 99.

<a id="core-prepare"></a>
## Подготовка после изменения

Прочитан клиентский путь после серверного результата: backend берёт найденный документ и updateSource; DataModel при непустом diff и не dryRun выполняет commit → _initialize. ClientDocument при documentsReady и готовом родителе вызывает safePrepareData, ошибки подготовки ловятся ядром. Условия пропуска/пустого diff сохранены; сеть и synthetic Actor отдельной сцены не воспроизводились.

Порядок: system.prepareBaseData → document.prepareBaseData → embedded/initial AE → system.prepareDerivedData → WitcherActor.prepareDerivedData → final AE. CommonActorData задаёт базовые максимумы и производные базы, vigor.max=unmodifiedMax. Локальный Actor дважды считает stats, fixed derived, прочие derived и attackStats. Эти существующие определения/процессы переиспользованы.

calculateDerivedStat меняет unmodifiedMax/max/totalModifiers по customStat и виду параметра; hp/sta/focus/resolve/vigor.value он не восстанавливает и не обрезает. Shield не входит в calculateDerivedStats. Ignored читается calculateStat, applied пересчитывается. HP/value может дополнительно меняться ActiveEffect соответствующей фазы — поэтому вывод об отсутствии clamp конкретного метода не является гарантией неизменного значения при любых эффектах.

<a id="core-dialog"></a>
## Восстановление STA

Character header содержит recover-sta → общий V2 activateListeners → _onRecoverSta. В Monster header кнопки нет, хотя метод наследуется. V1 имеет отдельные одноимённые тела, но его регистрация/реальный template не установлены.

Открытие: modal DialogV2 с двумя действиями, await render. Кнопка запускает callback позже; завершение render не ждёт выбора. Оба callback при исходном STA.value>=STA.max показывают info и возвращают управление. Иначе Recovery Action передаёт old STA+REC.value без итогового clamp; Full Recovery передаёт STA.max. Actor.update ни awaited, ни returned. При 9/10 и REC3 запрашиваются соответственно 12 и 10; это вывод по коду и прежний изолированный опыт issue-00164, не новое исполнение мира. Callback не создаёт ChatMessage.

| Путь | Ресурс и расчёт | Ожидание |
| --- | --- | --- |
| Ручной sidebar | Введённое число/boolean; вся форма | Внешний handler ждёт update, DOM change — нет |
| REC / full recovery | Только STA; old+REC.value или max, guard до операции | Callback не ждёт update |
| Отдых .022 | HP с верхним cap, STA=max, vigor=max; REC.max | recoverActor ждёт общий resource update; травмы отдельно |
| Урон .019 | Общий updateDerivedStat, щит и temporary HP с отдельными этапами | Порядок эффекта/ресурса сохранён в прежних процессах |
| Consume / чат / Combat | Прежние writers HP/STA/vigor/shield с собственными условиями | Не объединены в один способ восстановления |

## Источники внешних контрактов

Чтение ограничено указанными диапазонами; hashes фиксируют целые файлы для последующей сверки. Ядро не добавлено в 615 sources и не индексируется целиком. Freshness CLI проверяет прежнюю зависимость package.json; байты перечисленных core-файлов дополнительно проверяются тестом этой порции.

| Файл ядра | Прочитанные строки | Основание | SHA256 |
| --- | --- | --- | --- |
| `/opt/foundryvtt/client/applications/api/application.mjs` | 438–450, 496–535, 1890–1901, 2134–2162 | Слияние DEFAULT_OPTIONS, bind формы, сбор FormDataExtended, ожидание handler и change guard. | `b5aef80d3e042a4a856be9dd875c72a5224988d62046ba770f25376f4291faa0` |
| `/opt/foundryvtt/client/applications/api/document-sheet.mjs` | 37–70, 431–434, 465–536 | tag form, handler, isEditable, expand/validate и await update существующего документа. | `7925d81900eeea0d5e79606e12ce43539ae00714f50d8452c7305fe81394aa01` |
| `/opt/foundryvtt/client/applications/sheets/actor-sheet.mjs` | 17–20, 63–66 | ActorSheetV2 наследует DocumentSheetV2; actor возвращает document. | `060e65ed9746a1ade375e61b45330dd083b3102c73d5be8b16e6637c2a89350b` |
| `/opt/foundryvtt/client/applications/ux/form-data-extended.mjs` | 23–45, 105–126, 171–243 | Обход form.elements, исключения полей, Number/null и checkbox. | `0585d07f0ca067969b4dfdde6d187e7d8315abd1cb2dbf9dd55325c003175a01` |
| `/opt/foundryvtt/client/data/client-backend.mjs` | 310–344 | Обработка изменений после результата сервера; updateSource каждого найденного документа. | `8ffe114bca601980bf2f4582ce1f6e27c555d76586470f1a16ac23f6f021b9c5` |
| `/opt/foundryvtt/common/abstract/data.mjs` | 669–701, 784–787 | Пустой diff/dryRun без commit; commit → _initialize. | `11bb7f848c707803607accfa9f6b946c7cbfe8b17781ff562b468bdc77b934e5` |
| `/opt/foundryvtt/client/documents/abstract/client-document.mjs` | 60–67, 276–284, 313–320 | Guard готовности, safePrepareData и порядок model/document preparation. | `a007180e3cf8d465dffe43b11272f289b4cf77a9e301c7d431f48267dfad8e9e` |
| `/opt/foundryvtt/client/documents/actor.mjs` | 428–474 | Initial AE после embedded, final после super.prepareData. | `e82580bf9cef39d934c972dee859a3b9ba7ab5f3ebdc7502319dfed1bc214bb3` |
| `/opt/foundryvtt/client/applications/api/dialog.mjs` | 260–285 | Отдельный submit кнопки ожидает callback; render не его Promise. | `4e2d299eaa931d96df1839e64a2defc60b6b95ee89a3e1d32d60b99040899343` |

## Процессы

<a id="proc-000354"></a>
### proc-000354 — Ручные ресурсы: character sidebar → общий submit

Пользователь меняет одно именованное поле; отправляется вся общая форма. Охват inputs sidebar, не всех вкладок Actor.

Шаги: select → input → change → submit. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

<a id="proc-000355"></a>
### proc-000355 — Ручные ресурсы: monster sidebar → общий submit

Пользователь меняет одно именованное поле; отправляется вся общая форма. Охват inputs sidebar, не всех вкладок Actor.

Шаги: select → input → change → submit. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

<a id="proc-000356"></a>
### proc-000356 — Actor-form: типизация, validation и запрос записи

Change общей ActorSheetV2 формы; локальная точка подключения DEFAULT_OPTIONS. Внешние этапы помечены call-site, версия ядра в core-form.

Шаги: collect → editable → validate → request. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

<a id="proc-000357"></a>
### proc-000357 — Actor: подготовка после полученного изменения ресурсов

Только клиентский handoff после непустого подтверждённого diff; updateSource/dryRun/готовность документов и последующие AE различены.

Шаги: commit → base → embedded → derived → final. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

<a id="proc-000358"></a>
### proc-000358 — WitcherActorSheet: открыть восстановление STA

click recover-sta; у V1 вызов лишь гипотетический, текущей регистрации/собственного шаблона нет.

Шаги: dialog. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

<a id="proc-000359"></a>
### proc-000359 — WitcherActorSheet: восстановление по REC

Отдельное нажатие recovery в DialogV2; общая форма sidebar не участвует.

Шаги: guard → notify → write. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

<a id="proc-000360"></a>
### proc-000360 — WitcherActorSheet: полное STA

Отдельное нажатие full в DialogV2; общая форма sidebar не участвует.

Шаги: guard → notify → write. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

<a id="proc-000361"></a>
### proc-000361 — WitcherActorSheetV1: открыть восстановление STA

click recover-sta; у V1 вызов лишь гипотетический, текущей регистрации/собственного шаблона нет.

Шаги: dialog. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

<a id="proc-000362"></a>
### proc-000362 — WitcherActorSheetV1: восстановление по REC

Отдельное нажатие recovery в DialogV2; общая форма sidebar не участвует.

Шаги: guard → notify → write. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

<a id="proc-000363"></a>
### proc-000363 — WitcherActorSheetV1: полное STA

Отдельное нажатие full в DialogV2; общая форма sidebar не участвует.

Шаги: guard → notify → write. Ветви и выходы хранятся в JSONL; перечень шагов не заменяет условия переходов.

## Перекрёстная проверка

Просмотрены исходники десяти основных файлов по заявленным участкам; обе sidebar и модели CommonActorData/MonsterData/DerivedStats/stat прочитаны целиком. Проверены соответствующие карточки и поздние R003-03/10/11, R013-01/07/13 с относящимися issues. Большие Character/Monster/Actor используются по регистрации, ресурсному контексту и выбранным расчётам; прочие методы не объявлены повторно исследованными целиком.

Проверяются соответствие named input → schema-owner → внешний writer, оба конца отношений, существующие ID, раздельные фасеты sources, роли inventory, все восемь IQ и прежние примеры. Исторический пустой ответ JOIN-21 (.023) по HP writer sidebar и точный ED-10 (.010) по adrenaline writers проверяются на реконструированном охвате до .024. A15 приёмки сохраняется на прежнем пилоте: появился дополнительный процесс подготовки Actor. Все прежние ожидаемые ответы сохранены; .024 отдельно проверяет новые пути. JS/браузер/БД и правила рулбуков этими проверками не исполняются.

## Статус проверок

Проверены все 197 тестовых методов и 581 CLI-пример, включая 29 новых; после исправлений повторные проверки затронутых тестов прошли. Это проверки справочника по исходникам, без запуска игрового сценария. Ссылки, актуальность, владельцы/фасеты и сохранность проверяются при закрытии; итог — в [журнале](review-log.md#task-0006024). Следующая — [TASK-0006.025](../../tasks/task-0006.025.md). Родитель остаётся in-progress.