# Справочник-граф системы

[TASK-0006.018](../../tasks/task-0006.018.md) связывает исходные и подготовленные SP/сопротивления с формами, EV, выбором слоёв и запросами износа Item/Monster. [Покрытие и сверка](coverage-018.md). Формат JSONL v1 и CLI Python 3 сохранены; [согласованное решение](../../documentation/decisions.md#dec-0001--формат-и-локальный-поиск-справочника).

**Текущий охват:** 4330 сущностей, 10834 связи и 268 процессов (923 шага, 1645 переходов). Определения есть в 235/615 файлах: два словаря complete по строковым ключам, 233 файла partial; роли 119 основных/116 смежных, 380 без определений. .001–.018 выполнены; следующая — [TASK-0006.019](../../tasks/task-0006.019.md). [Очередь и остаток](expansion-plan.md#second-wave) сохраняют непокрытые области; полный индекс остаётся незавершённым.

## Быстрый запуск

Из корня репозитория; установка пакетов не нужна:

```bash
python3 docs/analytics/system-index/query.py find activeEffectModifiers --match exact --kind field
python3 docs/analytics/system-index/query.py find skillMixin --match exact
python3 docs/analytics/system-index/query.py show ent-000012
python3 docs/analytics/system-index/query.py field ent-000012 --access reads
python3 docs/analytics/system-index/query.py neighbors ent-000302 --direction in --relation calls
python3 docs/analytics/system-index/query.py neighbors ent-000277 --direction in --relation registers
python3 docs/analytics/system-index/query.py show ent-000326
python3 docs/analytics/system-index/query.py details ent-000304
python3 docs/analytics/system-index/query.py processes ent-000012
python3 docs/analytics/system-index/query.py process proc-000012 --offset 16 --limit 1
python3 docs/analytics/system-index/query.py check --freshness
```

Первый запрос различает Skill.activeEffectModifiers (ent-000012) и SkillItemData.activeEffectModifiers (ent-000188). У первого читатели — getter Skill.modifiedValue, actor.modifierMixin.addActiveEffects и форма edit-skills с disabled AE. Два skillMixin имеют разные файлы и ID: actor — ent-000299, sheet — ent-000305. processes ent-000012 показывает шаги getter, сборки модификаторов и отображения AE в форме; processes src-000047 включает прежние proc-000004/000005/000049 и новые процессы .013; используйте пагинацию для полного ответа.

Ответы содержат ID, адреса исходников/карточек, область и актуальность. Поиск по ID/символу/пути точный и чувствителен к регистру; aliases поддерживают русские термины, например find НАВЫК --match exact. Для программного чтения добавить --format json после команды.

По умолчанию выдаётся до 20 результатов. --offset N продолжает страницу; --depth N у neighbors раскрывает косвенные связи. Циклы завершаются, условия не исполняются. Входящий поиск использует те же отношения, что исходящий. Процесс показывает выходы и переходы к шагам вне страницы.

## Как читать ограничения

- partial — описана часть области; пустая выдача не доказывает отсутствие связи в системе.
- not_indexed — нужный участок ещё не внесён.
- unresolved_target / external_boundary — сохранено динамическое выражение либо внешнее API.
- current / stale / missing — проверка содержимого; --no-verify возвращает unchecked.
- depth_limited и page.truncated различают предел обхода и страницы.

Связи различают определения, импорты, регистрацию, установку обработчика, вызовы и доступ к данным. Конкретный путь экземпляра и контекст source/prepared/update-payload указаны в соответствующих отношениях. Общий проход Foundry по changes не выдан за локальную реализацию WitcherActiveEffect.

По умолчанию проверяются исходники каталога, реестр и документы выдачи. Полная check --freshness проверяет все карточки и ссылки; внешний package проверяется отдельно. Его хеш не заменяет проверку реализации ядра: прочитанные участки перечислены в [границах пилота](pilot-coverage.md#внешние-контракты-и-динамические-цели). Исторические адреса при изменении источника остаются с отметкой stale; поиск не обновляет записи.

Инструмент работает из другого каталога при запуске по абсолютному пути. Манифест по умолчанию расположен рядом с query.py. --dataset PATH перед командой выбирает другой набор, но его исходники всё равно адресуются от корня этого репозитория.

## Поиск по расширению .006

```bash
python3 docs/analytics/system-index/query.py find CONFIG.Actor.dataModels.mystery --match exact
python3 docs/analytics/system-index/query.py find WitcherProfessionSheet --match exact
python3 docs/analytics/system-index/query.py neighbors ent-000570 --direction in --relation reads
python3 docs/analytics/system-index/query.py neighbors ent-000575 --direction in --relation reads
python3 docs/analytics/system-index/query.py process proc-000021
```

Настройки — узлы setting; readers ищутся через neighbors. `proc-000021` показывает ready, ожидание getIndex и условия достижения сокета. Полный набор [16 примеров](examples/expansion-006-queries.json) и [покрытие](coverage-006.md) отделяют декларации манифеста, CONFIG-регистрации и реальное выполнение.

## Поиск по расширению .007

- find WitcherActiveEffectConfig.wizardAction --match exact → ent-000697, фактический класс листа и действие.
- neighbors ent-000639 --direction out --relation calls → семь групп базовых подсказок.
- field ent-000715 --access reads → чтение prepared changes в OK-callback.
- neighbors ent-000699 --direction out --relation refers → прежний _preUpdate через внешнее обновление.
- process proc-000026 и process proc-000027 → открытие мастера и отдельное подтверждение.
- details ent-000726 → условия системной вкладки и различие отсутствующего поля/перевода.

Команды передаются тому же query.py; добавить --format json для машинной выдачи. [20 точных примеров](examples/expansion-007-queries.json), [покрытие](coverage-007.md), [процессы](coverage-007.md#процессы-и-границы), [внешние контракты](coverage-007.md#проверенные-внешние-контракты). Раскрытие подсказки до поля модели не означает применения бонуса.

## Поиск по расширению .008

- find sheet.activeEffectMixin.prepareActiveEffectCategories --match exact → ent-000771; Item-копия — ent-000827.
- neighbors ent-000780 --direction in --relation calls → непосредственные входы status helper.
- field ent-000857 --access writes → замена system копии улучшения.
- process proc-000037 → обычный перенос; proc-000036 → выбор оружия; proc-000040 → статус/counter/иммунитет.
- process proc-000044 → Item-проход priority/active/legacy apply; Actor-проверка phase остаётся отдельной.
- details ent-000775 → R005 и позднее уточнение потери system.changes.

[24 проверочных запроса](examples/expansion-008-queries.json), [различия состояний и payload](coverage-008.md), [пять внешних контрактов](coverage-008.md#проверенные-внешние-контракты). Query true и сообщение в чате не означают завершения записи.

## Поиск по расширению .009

- find WitcherActorSheet._prepareCustomSkills --match exact → ent-000882; V1 — ent-000886.
- field ent-000885 --access reads → два места lookup собственных навыков в общем tab.
- neighbors ent-000382 --direction out --relation reads → ключи текущей builtin-строки и Item-строки.
- process proc-000056 → два прохода семи групп; proc-000058 → текущая Item-строка без hash.
- process proc-000059 → старый Item ID/selector; proc-000060 → установка подписки; бросок остаётся proc-000013.
- process proc-000061 → поля формы Item до внешнего submit; details ent-000898 → основание девяти вариантов атрибута.

[22 проверочных запроса](examples/expansion-009-queries.json), [контексты и границы](coverage-009.md), [шесть внешних контрактов](coverage-009.md#проверенные-внешние-контракты). PARTS, предзагрузка, render, подписка и click учитываются отдельно.

## Поиск переводов после .011

Точные ключи чувствительны к регистру; подписи ищутся как нормализуемые aliases. Одинаковые тексты дают отдельные результаты с языком и raw JSON Pointer. Для ограничения словарём CLI принимает ID источника: src-000002 (en), src-000003 (ru).

~~~bash
python3 docs/analytics/system-index/query.py find WITCHER.Settings.criticalWoundsPack --match exact --kind field
python3 docs/analytics/system-index/query.py find WITCHER.Actor.Skill.Intelligence --match exact --scope src-000003
python3 docs/analytics/system-index/query.py neighbors ent-001827 --direction in --relation refers
python3 docs/analytics/system-index/query.py process proc-000093
~~~

[24 проверенных примера](examples/expansion-011-queries.json) охватывают все восемь IQ; [coverage-011](coverage-011.md) объясняет состав словарей, fallback, placeholders и границы потребителей.

## Поиск по расширению .010

- find CONFIG.WITCHER.statLabels --match exact → ent-000946; field ent-000946 --access writes → два производителя общей карты.
- neighbors ent-000981 --direction out --relation refers → поле назначения unmodifiedMax и внешний submit.
- field ent-000012 --access reads --scope src-000542 → показ AE в edit-skills; disabled input не получает writes.
- process proc-000071 → max в имени unmodifiedMax; proc-000072 → прямое редактирование навыка.
- process proc-000073 и proc-000075 → уменьшение/сброс удачи с await; proc-000076/000077 → два уровня адреналина без ожидания записи.
- process proc-000081 и proc-000082 → удаление по ID и строковое редактирование старого массива; details ent-000972 → отсутствие schema.
- neighbors ent-000990 --direction out --relation refers → настоящий PARTS skillConfiguration; proc-000083 → поля видимости.

[24 проверочных запроса](examples/expansion-010-queries.json), [формы и границы записи](coverage-010.md), [шесть внешних контрактов](coverage-010.md#проверенные-внешние-контракты). Прямой input, подготовленное значение, запрос update и последующий расчёт различаются.

## Материалы

| Материал | Содержание |
| --- | --- |
| [Формат](format.md) / [контракт поиска](query-contract.md) | Записи, ID, версии, восемь запросов и коды завершения |
| [Инструмент](query.py) | Поиск, обход, валидация и проверка свежести |
| [Манифест](manifest.json) / [источники](sources.jsonl) | Проверенный срез, части и покрытие |
| [Сущности пилота](data/entities/pilot.jsonl) / [связи пилота](data/relations/pilot.jsonl) | Дополнение .003 к начальным записям |
| [Начальные сущности](examples/entities.jsonl) / [связи](examples/relations.jsonl) / [процессы](examples/processes.jsonl) | Записи .001; ID и содержимое сохранены |
| [Покрытие пилота](pilot-coverage.md) / [процессы](process-guide.md) | Границы 23 основных/13 смежных файлов и 14 процессов |
| [12 случаев процессов](examples/process-queries.json) / [13 случаев пилота](examples/pilot-queries.json) / [16 начальных](examples/queries.json) | Ожидаемые ответы; начальные проверяются отдельно |
| [Тесты процессов](tests/test_processes.py) / [пилота](tests/test_pilot.py) / [инструмента](tests/test_query.py) | Участие поля/метода, переходы, исходники и изолированные входы |
| [Приёмка пилота](pilot-acceptance.md) / [26 приёмочных случаев](examples/acceptance-queries.json) | Независимые ориентиры IQ-01–IQ-08, выдача и границы пригодности |
| [Расширение](expansion-plan.md) / [полный перечень](expansion-inventory.json) | 615 файлов: исторические роли пилота и отдельное текущее покрытие; .006–.018 выполнены; .019–.023 стоят в согласованной очереди |
| [Расширение .006](coverage-006.md) / [сущности](data/entities/expansion-006.jsonl) / [отношения](data/relations/expansion-006.jsonl) / [процессы](data/processes/expansion-006.jsonl) | Регистрации, настройки, init/ready/updateCombat и смежные определения |
| [16 случаев .006](examples/expansion-006-queries.json) / [тесты](tests/test_expansion_006.py) / [протокол](review-log.md#task-0006006) | Проверка новой порции и её границ |
| [Расширение .007](coverage-007.md) / [сущности](data/entities/expansion-007.jsonl) / [отношения](data/relations/expansion-007.jsonl) / [процессы](data/processes/expansion-007.jsonl) | Редактор AE, подсказки, prepared/source/payload, системная вкладка и CSS |
| [20 случаев .007](examples/expansion-007-queries.json) / [тесты](tests/test_expansion_007.py) / [протокол](review-log.md#task-0006007) | Проверки расширения и внешних контрактов |
| [Расширение .008](coverage-008.md) / [сущности](data/entities/expansion-008.jsonl) / [отношения](data/relations/expansion-008.jsonl) / [процессы](data/processes/expansion-008.jsonl) | Категории, CRUD, перенос/статусы, Item-проход, query и временные HP |
| [24 случая .008](examples/expansion-008-queries.json) / [тесты](tests/test_expansion_008.py) / [протокол](review-log.md#task-0006008) | Исходные адреса, разные predicates/payload, ветви и внешние границы |
| [Расширение .009](coverage-009.md) / [сущности](data/entities/expansion-009.jsonl) / [отношения](data/relations/expansion-009.jsonl) / [процессы](data/processes/expansion-009.jsonl) | Контексты листов, строки builtin/Item, старый ID/selector и форма навыка |
| [22 случая .009](examples/expansion-009-queries.json) / [тесты](tests/test_expansion_009.py) / [протокол](review-log.md#task-0006009) | PARTS/preload, девять/семь групп, hash/dataset, имя/ID и внешняя запись |
| [Расширение .010](coverage-010.md) / [сущности](data/entities/expansion-010.jsonl) / [отношения](data/relations/expansion-010.jsonl) / [процессы](data/processes/expansion-010.jsonl) | Формы/submit, ресурсы, старый CRUD и видимость навыков |
| [Расширение .011](coverage-011.md) / [сущности](data/entities/expansion-011.jsonl) / [отношения](data/relations/expansion-011.jsonl) / [процессы](data/processes/expansion-011.jsonl) | Полные строки en/ru, выбранные потребители, шесть процессов и накопленная сверка |
| [Расширение .012](coverage-012.md) / [сущности](data/entities/expansion-012.jsonl) / [отношения](data/relations/expansion-012.jsonl) / [процессы](data/processes/expansion-012.jsonl) | Общие модели/документы, миграции, контекст, enrichment, свойства Item и Drop |
| [Расширение .013](coverage-013.md) / [сущности](data/entities/expansion-013.jsonl) / [отношения](data/relations/expansion-013.jsonl) / [процессы](data/processes/expansion-013.jsonl) | Инвентарь, quantity, расходники, редактор и передача Item |
| [Расширение .014](coverage-014.md) / [сущности](data/entities/expansion-014.jsonl) / [отношения](data/relations/expansion-014.jsonl) / [процессы](data/processes/expansion-014.jsonl) | Схемы/редакторы оружия, атаки, защиты и урона, выбранные consumers |
| [Расширение .015](coverage-015.md) / [сущности](data/entities/expansion-015.jsonl) / [отношения](data/relations/expansion-015.jsonl) / [процессы](data/processes/expansion-015.jsonl) | Оружейная атака, форма/ресурсы/формула, модель сообщения и провал |
| [Расширение .016](coverage-016.md) / [сущности](data/entities/expansion-016.jsonl) / [отношения](data/relations/expansion-016.jsonl) / [процессы](data/processes/expansion-016.jsonl) | Выбор/формула защиты, crit/stun, износ, локации и выбранные действия чата |
| [Расширение .017](coverage-017.md) / [сущности](data/entities/expansion-017.jsonl) / [отношения](data/relations/expansion-017.jsonl) / [процессы](data/processes/expansion-017.jsonl) | Формула/проценты/сообщение урона, схемы и DamageInstance |
| [Расширение .018](coverage-018.md) / [сущности](data/entities/expansion-018.jsonl) / [отношения](data/relations/expansion-018.jsonl) / [процессы](data/processes/expansion-018.jsonl) | SP/EV, формы, слои, сопротивления и запросы износа |
| [24 случая .010](examples/expansion-010-queries.json) / [тесты](tests/test_expansion_010.py) / [протокол](review-log.md#task-0006010) | Поля ввода/disabled, prepared/source, ID/строка и ожидание записи |
| [Тесты приёмки](tests/test_acceptance.py) / [протокол .005](review-log.md#task-0006005) | Проверка запросов, взаимности связей и устаревания без изменения источников |

Подробные объяснения остаются в [аудите](../code-audit/README.md); назначение справочника задано [требованиями](../system-index-requirements.md).

## Проверки

```bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
```

Пройдены все 143 тестовых метода (unittest, 980.173 с), включая 32 новых CLI-случая; накоплено 389 CLI-примеров. Это проверки справочника по исходникам, без исполнения игрового сценария. Проверены все 10834 отношения в обоих направлениях. Итоговая актуальность и сохранность — в [протоколе](review-log.md#task-0006018). Исторические случаи и численные срезы отделены от накопленных ответов.

## Практический маршрут по пилоту

Начать с find по точному имени/alias, затем выбрать владельца через show. Для вызовов использовать neighbors с --relation calls и нужным направлением; для полей — field. Processes → process раскрывают участие и соседние шаги, details — карточку и конкретные доказательства. Например, details ent-000319 ведёт к позднему уточнению issue-00043 и R005-03.

При partial/none_in_scope проверить объявленный остаток и соответствующий исходник. При stale сначала проверить применимость исторических адресов; инструмент не обновляет индекс автоматически. Общий schema-field требует чтения payload конкретного обращения. Детали использования и измеренный объём ответов — в [приёмке](pilot-acceptance.md#объём-ответа-и-ручное-чтение).

## Общие документы и контекст — .012

- find CommonItemData.quantity --match exact → ent-003383: строковое поле модели.
- field ent-003383 --access reads → вклад в вес и цена списка.
- neighbors ent-000168 --direction out --relation extends → отдельная база LootData.
- process proc-000115 → live context Actor V2; proc-000116 → копия system в V1.
- process proc-000123 → прямой optional enrichment модели Item; proc-000127 → ручная запись свойства.
- process proc-000129 → разрешение Drop; proc-000130 → четыре типа документов и границы handlers.

Команды передаются query.py. [24 примера](examples/expansion-012-queries.json), [покрытие](coverage-012.md) и [протокол](review-log.md#task-0006012) различают подготовленные данные, запрос записи и внешнее сохранение. Полные инвентарь/бой/ремесло/восстановление раскрываются следующими задачами.

## Инвентарь и расходники — .013

- field ent-003383 --access writes → изменение количества: addItem/removeItem/inline edit.
- process proc-000135 → ветви useItem; proc-000136/137 → объединение/создание и списание/удаление.
- process proc-000140 → Drop, уникальность, prepared equipped и profession flags.
- process proc-000149 → consume с HP, статусами, applySelf и сообщением; количество меняют его callers.
- process proc-000152 → передача Item с барьером legacy callback и отсутствием подтверждения доставки.
- process proc-000154 → поиск записи editor по отсутствующему id и недостижимый штатный update.

Команды передаются query.py. [26 примеров](examples/expansion-013-queries.json), [тесты](tests/test_expansion_013.py), [покрытие](coverage-013.md). Сохранение в мире и работа нескольких клиентов остаются внешними границами.

## Боевые свойства Item — .014

- find DefenseProperties --match exact --kind class — реальная модель; одноимённые поля имеют других владельцев.
- find DamageProperties.effects --match exact — словарь TypedObject; Array расходника имеет отдельного владельца.
- field ent-003755 --access writes --scope src-000186 — три ручных операции записи по ключу словаря.
- neighbors ent-003777 --direction out --relation reads — навыки цепочки ??, включая границу пустой строки.
- process proc-000158 — подготовка улучшений, цикл разрешения ID и граница recipe.
- process proc-000171 — dataset key/field, on→checked и update dot-path.
- process proc-000173 — выбор Set по клавишам, пустой набор и служебные options.
- process proc-000174 — последовательный AP/IAP и primitive/Array merge, без object effects.

[26 примеров IQ-01–IQ-08](examples/expansion-014-queries.json) и [сверка](coverage-014.md) различают общий general.hbs, включаемый spell partial и внешнее сохранение формы. Полные боевые процессы продолжаются в следующих задачах.

## Оружейная атака — .015

- find actor.attack(label) --match exact — строковые label/value схемы безоружной атаки Actor.
- find chat.attackData() --match exact — отдельная схема атаки сообщения.
- field ent-003900 --access writes --scope src-000047 — запись prepared punch/kick.value.
- neighbors ent-003895 --direction out --relation calls — общие модификаторы обычной основы; замена навыка обходит этот helper.
- process proc-000180 — форма, ранние возвраты, расходы до цикла, общий damage и два выхода.
- process proc-000181 — порядок сборки одного удара, включая накопление customDmg в общей строке.
- show ent-003944 — граница plain properties прямого rollDamage и позднее уточнение issue297.
- process proc-000186 — отдельное меню по точному типу сообщения.
- process proc-000189 — локализованный текст последствий, без RollTable и автоматического применения.

[28 примеров IQ-01–IQ-08](examples/expansion-015-queries.json) и [сверка](coverage-015.md) различают подготовленные формулы, диалог, payload и модель сообщения. Полные защита и применение урона остаются следующими задачами.

## Защита и локации — .016

- find actor.defenseMixin.prepareAndExecuteDefense --match exact — стандартные способы, Item и профессиональный override.
- neighbors ent-003890 --direction out --relation calls — модельные варианты Weapon/Profession.
- neighbors ent-004024 --direction out --relation calls --limit 100 — формула, собственный defense modifier, общий Roll и отдельная публикация.
- process proc-000190 — выбор способа и средства; отдельные ветви нуля, одного и нескольких вариантов.
- process proc-000198 — расход STA, Roll, crit/stun, сообщение и последующие запросы изменений.
- process proc-000200 — собственный 2d6 и возврат существующей локации.
- process proc-000203 — спасбросок с обратным строгим сравнением; равенство отличается от защиты.
- show ent-004092 — поле raw crit, которого нет в DefenseMessageData.
- show ent-004098 — instance wrapper и static this.
- process proc-000210 — отдельные действия над выбранным Actor; создание crit не вызывает травму автоматически.

[28 примеров IQ-01–IQ-08](examples/expansion-016-queries.json) и [сверка](coverage-016.md) различают формулу, prepared damage, очищенную модель сообщения и действия чата. Бросок урона, SP/HP и полный цикл травмы остаются последующим порциям.

## Бросок урона и данные сообщения — .017

- find DamageMessageData.damage.properties --match exact — собственный SchemaField сообщения; общая damageData объявляет Embedded модель.
- neighbors ent-003889 --direction out --relation calls --limit 100 — ввод, preprocessing, обычный Roll и отдельный setFlag.
- field ent-004133 --access computes — назначение applied в копиях; --access reads — автоматический consumer.
- field ent-004143 --access writes — дополнительная запись после toMessage.
- field ent-004182 --access reads — два callback физического меню и числовой вход из DOM.
- process proc-000219 — формула/локация/эффекты до Roll, сообщение и флаг с разными ожиданиями.
- process proc-000215 — три уровня схемы и override effects.
- process proc-000221 — исходное/текущее значения и семь null-полей обычного объекта.
- field ent-004174 --access computes — выбранный writer промежуточной стадии; afterSpText только читает её.
- show ent-004192 — присваивание строке имени метода, не вызов setter.

[28 примеров IQ-01–IQ-08](examples/expansion-017-queries.json) и [сверка](coverage-017.md) отделяют prepared Item, очищенное сообщение, сырой flag и runtime DamageInstance. Полные SP/HP, чат и травмы остаются следующим порциям.

## Броня, сопротивления и износ — .018

- find SpData --match exact --kind class — общий владелец четырёх полей; экземпляры зон принадлежат ArmorData.
- field ent-004239 --access writes --scope src-000108 --limit 100 — запись базы износом, локальным repair и миграцией.
- field ent-004240 --access computes --scope src-000127 — base-копия и derived улучшений.
- neighbors ent-000310 --direction in --relation calls — три прямых consumer EV.
- neighbors ent-004193 --direction out --relation calls --limit 100 — getList, getArmors и два вызова getArmorSp.
- process proc-000235 — Heavy→Medium→Light и отдельный Natural, два обхода.
- process proc-000237 — ранний AP, multiplier и два источника типа сопротивления.
- process proc-000247 — проверка modified SP, цель в базе и не ожидаемый update.
- field ent-004268 --access reads — consumer прямого износа plain status payload.
- show ent-004269 — граница числового SP и текстового пояснения.

[32 примера IQ-01–IQ-08](examples/expansion-018-queries.json) и [сверка](coverage-018.md) разделяют source/prepared/payload, Natural Item/Monster и размер износа/подтверждение записи. Полное применение урона и изменение HP/STA остаются .019.
