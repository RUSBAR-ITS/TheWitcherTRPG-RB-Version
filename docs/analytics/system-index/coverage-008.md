# Покрытие TASK-0006.008 — категории, перенос и статусы эффектов

2026-09-15; rusbar-main, исходный HEAD fa18840b7dfd3a9ecc341b0ba9cc323fdce6e9a1. [Задача](../../tasks/task-0006.008.md), [манифест](manifest.json), [протокол](review-log.md#task-0006008).

Добавлены **111 сущностей, 306 отношений и 17 процессов**. Накоплено **615 источников, 879 сущностей, 2211 отношений и 49 процессов**; 270 шагов и 417 переходов. Частичные определения имеют 134 файла: 41 основной и 93 смежных; 481 пока без определений. Старые ID сохранены; существующие определения ViaId, chatMessageListeners, getter Actor.temporaryEffects и listener листа уточнены на прежнем месте. Формат и CLI не менялись.

## Включённые области

| Источник | Индексированная область |
| --- | --- |
| [activeEffectMixin.js](../../../module/actor/sheets/mixins/activeEffectMixin.js) — src-000036 | Четыре метода: категории, управление документом, раскрытие описания, установка listeners. |
| [temporaryEffectMixin.js](../../../module/actor/mixins/temporaryEffectMixin.js) — src-000023 | Actor-метод применения улучшений, callback выбора оружия, состав копии и сообщение. |
| [applyStatusEffect.js](../../../module/scripts/statusEffects/applyStatusEffect.js) — src-000205 | Шесть функций, bulk/click listeners, targets, UUID/owner, counter и callback иммунитета. |
| [applyActiveEffect.js](../../../module/scripts/temporaryEffects/applyActiveEffect.js) — src-000206 | Targets, ViaId, обычные эффекты Actor и отдельный передатчик улучшений. |
| [temporaryEffectsData.js](../../../module/data/actor/templates/common/temporaryEffectsData.js) — src-000092 | Модель TemporaryEffects, defineSchema и temporaryHp с name/value. |
| [witcherItem.js](../../../module/item/witcherItem.js) — src-000192 | Только prepareEmbeddedDocuments, allApplicableEffects, applyActiveEffects и changes.map. |
| [effect-part.hbs](../../../templates/partials/effect-part.hbs) — src-000531 | Категории, create gate, suppression, owner/ID/action, controls и описание. |
| [tab-effects.hbs](../../../templates/sheets/actor/partials/character/tab-effects.hbs) — src-000562 | Включение списка на строке 58; отдельная граница повторного представления травм. |

Смежные области: getters и _preCreate ActiveEffect, обе модели эффектов, Actor.temporaryEffects, фрагменты контекста Actor V2 и старого V1, собственные категории/actions Item-конфигурации и её HBS-wrapper, сообщение улучшения, getCurrentCharacter/getActorOwner, два query-получателя и их регистрация. CommonItemData выбран только ради getter возможности улучшения; MonsterData — ради массива иммунитетов; combatEffects — ради контейнера пула временных HP.

У consume/castSpell/applyDamage/handleDefenseResults внесены ближайшие вызовы эффектов, у profession/updateDerivedStat — producer и потребитель пути temporaryHp. Полные процессы боя, магии, профессий, лечения и списания Items этим не покрыты. Два фактических producer a.apply-status представлены отдельно; statusEffect.hbs остаётся уведомлением.

## Категория, видимость и участие в расчёте

| Условие | Что делает |
| --- | --- |
| Actor-категоризатор — ent-000771 | isDisabled → inactive; затем неприменённое temporaryItemImprovement → отдельная группа; затем isTemporary → temporary; иначе passive. |
| Item-категоризатор — ent-000827 | Тот же порядок групп, но первая проверка — e.disabled. Это собственная копия метода. |
| isDisabled — ent-000314 | disabled либо отрицание parent.system.equipped с fallback true. Это не полная проверка suppression. |
| isSuppressed — ent-000313 | Локальный getter проверяет isActive/equipped родителя и четыре apply-флага. Не делегирует проверку длительности core getter. |
| Core active — ent-000795 | !disabled && !isSuppressed. Исполнение внешнего getter учитывает локальное переопределение suppression. |
| effect-part, строка 18 | Скрывает строку только при effect.isSuppressed && root.actor. Состояние документа не меняется. |
| Core isTemporary — ent-000796 | duration.expiry либо конечное duration.value. Не равно типу temporaryItemImprovement. |

Core transfer — ent-000797 — участвует во внешнем Actor.allApplicableEffects; system.isTransferred — прежний ent-000181 — читается локальным isAppliedTemporaryItemImprovement. Getter последнего сам не проверяет type. Item.allApplicableEffects сначала выбирает этот флаг, а Item.applyActiveEffects затем проверяет active.

Actor V2 собирает core allApplicableEffects и добавляет улучшения из context.items, где раньше исключены isStored. Getter Actor.temporaryEffects добавляет улучшения из всех Items к super.temporaryEffects. В добавочных списках нет собственного active/isTemporary-фильтра или dedup. Эти два коллектора не объединены.

Основание: [R005-04](../code-audit/cross-check-0002.md#r005-04), [R005-11](../code-audit/cross-check-0002.md#r005-11). Внешний scheduler не следует из присутствия эффекта в категории.

## Управление списком

Actor-handler читает parentUuid и effectId из li и разрешает embedded effect через fromUuidSync(parentUuid).effects.get(id). Оба атрибута parent-id/parent-uuid в HBS содержат UUID; callback читает parentUuid. Create получает категорию заголовка и создаёт эффект на caller; type и transfer явно не задаются. Edit открывает лист, toggle отправляет disabled=!effect.disabled. Только delete сравнивает parentUuid с caller.uuid; при несовпадении показывает ошибку.

Item-конфигурация берёт effect из this.document.effects и регистрирует четыре actions. Её create явно выбирает type=temporaryItemImprovement/base. Раскрытие описания подключает Actor-примесь; в Item actions его нет. Общий HBS скрывает create временного улучшения при неподходящем canHaveTemporaryItemImprovement, но это UI-условие, не проверка в backend-методе выбора оружия.

Отсутствующие li/owner/effect не везде защищены. Запросы create/update/delete и косвенные _preCreate/_preUpdate проходят через ядро. Возвращаемый Promise события не означает ожидания со стороны DOM dispatch. Браузер, права и запись в БД здесь не исполнялись. См. [issue-00055](../../issues/closed/issue-00055.md), [issue-00056](../../issues/closed/issue-00056.md).

## Два маршрута копирования

| Этап | Обычный эффект на Actor | Временное улучшение на оружие |
| --- | --- | --- |
| Отбор | Non-temp; ViaId дополнительно читает system[applyWhen]. | Только type=temporaryItemImprovement; active/disabled/transfer не фильтруются. |
| Получатель | Actor по UUID; не найден — return. | Все weapon Items Actor; prompt не проверяет equipped/isStored/canHaveTemporaryItemImprovement. |
| Подготовка | Входной effect.duration.rounds мутируется до owner-проверки; clone читает source. | toObject?.() либо raw spread; имя оружия + имя эффекта, origin=Actor.uuid. |
| system | Четыре apply-флага false в clone payload. | Объект заменяется целиком: isTransferred=true, applySelf=false, applyOnTarget=false. Современный system.changes этим payload не переносится. |
| Длительность | duration.combat в clone; отдельный duration отсутствует в non-owner query. | Spread temp.duration и legacy combat; нового start в payload нет. |
| Завершение | Прямой owned helper ждёт createEmbeddedDocuments даже для []. | Prompt и render ожидаются, weapon.createEmbeddedDocuments и ChatMessage.create — нет. |

Обычный helper до owner-проверки отдельно запускает передатчик временных улучшений. При non-owner тот отправляет специализированный query со всем списком; обычная ветка посылает другой query с non-temp списком. Не-await вызовы независимы по завершению. Undefined вход, отсутствующий duration или getter-only legacy поле могут остановить обычный маршрут ещё до копирования. Пустой список оружия не закрывает путь к prompt; неизвестный выбранный id приводит к обращению к отсутствующему weapon при построении копии.

Сообщение об улучшениях получает payload temps, не результат создания. getSpeaker вызывается с this.actor, хотя метод примешан Actor; успешное создание/истечение не следует из наличия сообщения.

[Распределение и копирование R005-07](../code-audit/cross-check-0002.md#r005-07), [улучшения R005-08](../code-audit/cross-check-0002.md#r005-08), [длительность R005-09](../code-audit/cross-check-0002.md#r005-09), [позднее уточнение issue-00042](../../issues/closed/issue-00042.md#уточнение-task-0003009), [issue-00044](../../issues/closed/issue-00044.md), [issue-00045](../../issues/potential/issue-00045.md), [issue-00046](../../issues/potential/issue-00046.md), [issue-00050](../../issues/closed/issue-00050.md).

## Статусы, запросы и временные HP

Статус-click выбирает первый controlled token.actor либо user.character через getCurrentCharacter, а не targets/автора сообщения; отсутствие target не защищает чтение uuid. Bulk-export сочетает querySelector с .each; его внутренний вызов не найден. Рабочий отдельный chatMessageListeners привязывает a.apply-status. Его producers: damageUtilMixin, строка 58, без duration; spellItem.hbs, строки 63–68, с duration.

applyStatusEffectToActor сначала разрешает Actor/owner, затем проверяет ID в appliedEffects. Core toggleStatusEffect ищет существующие эффекты в effects, включая disabled: без active:true он может удалить такой документ. После await toggle идёт синхронный counter, затем проверка иммунитета. Если модуль активен и duration ненулевой, штатный WITCHER.statusEffects — массив — не предоставляет querySelector. Ошибка на этом месте препятствует постановке таймера. API стороннего EffectCounter не проверен. Callback иммунитета через 1000 ms выполняет ещё один toggle без active:false; это отдельный вход, не установленная длительность документа. См. [R005-10](../code-audit/cross-check-0002.md#r005-10), [issue-00003](../../issues/potential/issue-00003.md), [issue-00047](../../issues/potential/issue-00047.md), [issue-00048](../../issues/potential/issue-00048.md), [issue-00049](../../issues/potential/issue-00049.md).

getActorOwner выбирает активного игрока с OWNER либо activeGM. Отсутствующий получатель может остановить код до query. Общий query и специализированный query возвращают true после запуска, без ожидания результата метода; generic entity-ветка допускает два вызова — на entity и system. Оператор in в callableFunctions видит также наследуемые свойства обычного объекта, для них оставлена отдельная динамическая граница ent-000879. Полный сетевой маршрут не развёрнут. См. [issue-00008](../../issues/potential/issue-00008.md), [issue-00185](../../issues/potential/issue-00185.md).

TemporaryEffects — модель пула temporaryHp с произвольными ключами и элементом {name,value}, а не коллекция ActiveEffect. Контекст листа вычисляет temporaryHpSum; этого поля в схеме пула нет. Profession формирует legacy ADD по динамическому пути и посылает query; damage.updateDerivedStat ищет подстроку temporaryHp среди changes. Эти ближайшие связи не доказывают числовое применение ADD объекта и не покрывают весь процесс урона.

## Процессы и границы

| Процесс | Локальная область |
| --- | --- |
| <a id="proc-000033"></a>proc-000033 | Категории Actor: четыре группы эффектов. Приоритет predicates списка; suppression и core active не заменяются категорией. |
| <a id="proc-000034"></a>proc-000034 | Actor-список: create/edit/toggle/delete. Возвращает API-результат; listener не ждёт. Li/owner/effect не валидируются. Нет автоматического type=temporaryItemImprovement у create. |
| <a id="proc-000035"></a>proc-000035 | Actor-список: раскрытие описания. Только DOM/jQuery; Item-конфигурация не подключает этот listener. |
| <a id="proc-000036"></a>proc-000036 | Временное улучшение: выбор оружия, копия и чат. Обработка современных system.changes и начала времени различены; create/ChatMessage без await. Прочие типы Item/состояния equipped/isStored не проверяются. |
| <a id="proc-000037"></a>proc-000037 | Обычный эффект: Actor UUID, копирование и создание. Prepared duration mutation до clone не равна source update. Временная ветка запускается отдельно без ожидания; non-owner duration отдельным аргументом не отправляется. |
| <a id="proc-000038"></a>proc-000038 | Эффект по Item UUID: фильтр триггера или запрос GM. Нет ограничения повторного перенаправления, guard activeGM или проверки типизированного Item. Удалённое исполнение не предполагается. |
| <a id="proc-000039"></a>proc-000039 | Передатчик временных улучшений: владелец или query. Отправляет весь activeEffects; фильтрация по типу выполняется Actor-методом. Ни query, ни локальный Actor-вызов не ожидаются. |
| <a id="proc-000040"></a>proc-000040 | Статус: получатель, toggle, counter и иммунитет. Не путать с WitcherActor.applyStatus. Существующий disabled эффект core toggle может удалить; counter ошибка препятствует постановке таймера. |
| <a id="proc-000041"></a>proc-000041 | Статус: отложенное переключение иммунитета. 1000ms задаёт задержку вызова, не длительность ActiveEffect; повторный toggle без active:false и без ожидания. |
| <a id="proc-000042"></a>proc-000042 | Интеграция statuscounter: guards и поиск счётчика. API стороннего модуля не исполнен/не проверен. Текущий Array WITCHER.statusEffects не имеет querySelector; штатная ветка останавливается на ней. |
| <a id="proc-000043"></a>proc-000043 | Команда чата: текущий Actor и применение статуса. Читает status/duration из dataset; controlled Actor либо user.character. Выбор targets/автора сообщения не выполняется. |
| <a id="proc-000044"></a>proc-000044 | Item: применение transferred эффектов. Генератор передаёт эффекты с isTransferred; затем core active. Нет shouldApplyChange/phase. Legacy apply делегирует applyChange; неопределённый priority/mode допускает NaN, type не подставляется в fallback. |
| <a id="proc-000045"></a>proc-000045 | Общий query: whitelist и запуск обработчика. Объявленные whitelist выбранного участка; in также видит наследуемые свойства обычного объекта. Для них цель оставлена за границей. Вызов не ожидается. Entity/system пути generic оставлены динамическими, timeout здесь не используется. |
| <a id="proc-000046"></a>proc-000046 | Специализированный query: передача улучшения Actor. Нет guard UUID и ожидания Actor-метода; return true не означает завершённый выбор оружия/запись. |
| <a id="proc-000047"></a>proc-000047 | Общий список HBS: категории и видимость строки. Скрытие строки не меняет эффект. Предикаты категоризатора, create gate и suppression различаются. Действия запускает внешний event dispatch/listener. |
| <a id="proc-000048"></a>proc-000048 | Actor V2: сборка категорий context.effects. Только строки85–92; context.items заранее исключил isStored. AllApplicableEffects приходит из ядра. Не выводить полноту _prepareContext из этого процесса. |
| <a id="proc-000049"></a>proc-000049 | Actor: getter temporaryEffects и Item-улучшения. Super фильтрует active/isTemporary; добавочный список не делает этих проверок, не фильтрует stored и не устраняет дубли. Scheduler не является частью getter. |

Все процессы partial. Пустые inputs/targets, чужой owner, тип/флаги, отмена prompt, выбор неверного документа, ошибки counter и ранние query-ответы разделены. Вложенные callback не считаются исполненными при регистрации. Все локальные шаги имеют адрес исходника; core API, сеть, registry истечения, произвольные ошибки DOM/ядра и сохранение — внешние границы. Временной scheduler не строился. Proc-000006/000007 и прежний @skill-процесс не дублируются.

Категории/actions Item-конфигурации и targets-обёртки имеют определения и связи, но не отдельные полные процессы. Фрагменты соседних контекстов и вызовов не означают покрытия всех их ветвей. Дублирование травм в tab — представление, не два документа или два выполнения лечения: [issue-00054](../../issues/closed/issue-00054.md#дополнительная-сверка-task-0003047).

## Проверенные внешние контракты

Установленная Foundry 14.367.0. Прочитанные участки ниже остаются внешними границами, не добавлены в каталог 615 исходников. SHA256 относится к целому файлу; стандартная freshness проверяет package, отдельный тест .008 — эти контракты.

| Внешний файл | Прочитанная область | SHA256 |
| --- | --- | --- |
| /opt/foundryvtt/client/documents/active-effect.mjs | 199–234, 500–502, 980–992, 1069–1073: target/active/temporary/trackable, phase, start и legacy apply | 7eacad67767aaa9840a6249dcd55098d62279fad5cc2bf3fa6d28da4455236b8 |
| /opt/foundryvtt/client/documents/actor.mjs | 149–170, 238–273, 305–314, 547–582: applied/temporary, изменения, transfer, toggle | e82580bf9cef39d934c972dee859a3b9ba7ab5f3ebdc7502319dfed1bc214bb3 |
| /opt/foundryvtt/common/abstract/document.mjs | 472–484: clone читает source через toObject, merge и новый документ | 303e6bc84fbaa7d564dab144b1f59fd0a1f6584a14e872b293e74358ed9b49dc |
| /opt/foundryvtt/client/documents/user.mjs | 289–321: имя, QUERY_USER, адресат, userQuery/ответ | 43e0837d478838959c8676a319ce4af44196bc1e7fc0ae98e8c4f2976aab9682 |
| /opt/foundryvtt/client/applications/api/dialog.mjs | 264–275, 369–377, 405–424: callback, prompt, rejectClose | 4e2d299eaa931d96df1839e64a2defc60b6b95ee89a3e1d32d60b99040899343 |

Современные поля changes и перенос legacy changes в system.changes проверены в [предыдущем расширении](coverage-007.md#проверенные-внешние-контракты). Core _preCreate задаёт start Actor-owned эффекту; локальный _preCreate корректирует combatant/длительность только при соответствующем parent/isTransferred и start.combat.started. Внешняя отслеживаемость требует persisted, вне compendium, embedded, active, start и isTemporary. Наличие legacy combat в payload не доказывает регистрацию отсчёта у эффекта оружия.

## Проверки и дальнейший остаток

[24 примера](examples/expansion-008-queries.json) проверяют определения, прямые/обратные обращения, поля, процессы и ссылки на доказательства. [Тесты](tests/test_expansion_008.py) дополнительно сверяют буквальные строки исходников, predicates, разные payload, порядок await, приоритеты/phase, шаблоны, достижимость шагов, границы и версии ядра. Ожидаемые адреса заданы по прочитанному коду, не скопированы из результатов CLI.

Прежние фиксированные размеры .007 перенесены на её исторические части; её поисковые и предметные проверки сохранены на текущем наборе. Случаи A23/P13 с прежним объёмом value/Actor-процессов сохранены на пилотном срезе, новая порция отдельно проверяет расширенную выдачу. Общая приёмка сверяет оба направления всех отношений. Фактические результаты и сохранность — в [протоколе](review-log.md#task-0006008).

Игровой код, ядро, браузер, сеть и БД не исполнялись. Аудит, issues и их статусы сохранены; ссылки на прежние наблюдения не являются новым подтверждением/исправлением. Следующая согласованная порция — [TASK-0006.009](../../tasks/task-0006.009.md).
