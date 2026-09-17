# Справочник-граф системы

[План 00332](../../issues/closed/issue-00332.md#plan), .00025: по текущим сущностям/отношениям и процессам выделены девять блоков/12 issues. Нового покрытия графа на этапе плана нет; [TASK-0010](../../tasks/task-0010-parameter-limits.md) откладывает ограничения параметров. После реализации обновляются только затронутые записи, новые исходники и прямые связи.

Текущий UI-срез: [issue-00334](../../issues/closed/issue-00334.md), 14.3.1.00022. Уточнены единственный список травм, уникальность Actor-категорий, Item-action описания и повторный рендер редактора/конвертера. Новые локальные маршруты: proc-000466–000468; удалённые определения/связи находятся в retired_ids. Игровая приёмка P01–P12 выполнена 2026-09-17; пользователь подтвердил закрытие общей и шести исходных issues. Закрытие оформлено в .00023; игровой код остаётся реализацией .00022.


[К01 / .00016](../../issues/closed/issue-00331.md#implementation): актуализированы хеши 48 JSON и их пофайловые карточки после контентных исправлений. Эти источники не имеют отдельных определений/процессов в JSONL; три входящие ссылки на файлы сохранены. Объём покрытия, сущности, отношения и процессы не менялись.

Согласованный состав работ по компедиумам: [контент](../../issues/closed/issue-00331.md), [механики](../../issues/closed/issue-00332.md), [процессы](../../issues/open/issue-00333.md). Общие карточки содержат 9 / 15 / 11 исходных issues; 2026-09-17 четыре из 15 механик (00036, 00121, 00288, 00289) отложены в [TASK-0009](../../tasks/task-0009-critical-wound-behavior.md), 11 остаются в текущей работе; нового покрытия кода или изменения механизма справочника этим оформлением нет.

[issue-00330](../../issues/closed/issue-00330.md) закрыта по подтверждению пользователя в 14.3.1.00011. N01–N08 выполнены в 14.3.1.00010; все 20 исходных локализационных карточек также закрыты. Прежние ключи сохранены; отложенные ошибки пустых полей, механики и компедиумы остаются вне этого исправления.


Текущий технический срез обновлён после [issue-00001](../../issues/closed/issue-00001.md): ID пакета и зависимые обращения — TheWitcherTRPG-RB-Version. Постоянные ID и объём покрытия сохранены. HEAD в snapshot — база рабочих изменений; source_hash фиксирует фактические исходники. Датированные coverage/протоколы прежних задач описывают прежние срезы.

[TASK-0006.023](../../tasks/task-0006.023.md) завершает накопленную проверку предметов, боя, эффектов и восстановления. [Матрица 12 стыков, остаток и сверка](coverage-023.md). Формат JSONL v1 и CLI Python 3 сохранены; [согласованное решение](../../documentation/decisions.md#dec-0001--формат-и-локальный-поиск-справочника).

**Текущий охват (.00026):** 617 источников, 5430 сущностей, 15319 отношений, 468 процессов (1545 шагов / 2934 переходов). Определения в 307 файлах, отношения в 321, шаги процессов в 161. Покрытие partial; новые определения и прямые связи ограничены issue-00332, М08 не менялся и в .00027 передан в TASK-0009. Датированные итоги прежних очередей остаются историческими.

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
| [Расширение](expansion-plan.md) / [полный перечень](expansion-inventory.json) | 615 файлов: исторические роли пилота и отдельное текущее покрытие; .006–.025 выполнены; .026–.034 planned, следующая .026; полный индекс partial |
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
| [Расширение .019](coverage-019.md) / [сущности](data/entities/expansion-019.jsonl) / [отношения](data/relations/expansion-019.jsonl) / [процессы](data/processes/expansion-019.jsonl) | Message/status, щит, одна/все локации, временные HP и ресурс |
| [Расширение .020](coverage-020.md) / [сущности](data/entities/expansion-020.jsonl) / [отношения](data/relations/expansion-020.jsonl) / [процессы](data/processes/expansion-020.jsonl) | Действия чата, query/socket, activeGM и периодика |
| [Расширение .021](coverage-021.md) / [сущности](data/entities/expansion-021.jsonl) / [отношения](data/relations/expansion-021.jsonl) / [процессы](data/processes/expansion-021.jsonl) | Критические травмы: pack/Item, UI, heal/treat/followUp и срок |
| [Расширение .022](coverage-022.md) / [сущности](data/entities/expansion-022.jsonl) / [отношения](data/relations/expansion-022.jsonl) / [процессы](data/processes/expansion-022.jsonl) | Лечение, отдых, регенерация и спасброски смерти |
| [Накопленная сверка .023](coverage-023.md) / [35 примеров и 12 стыков](examples/expansion-023-queries.json) / [тесты](tests/test_expansion_023.py) | Связи предметов, боя и восстановления; остаток всех 615 sources, границы полноты |
| [24 случая .010](examples/expansion-010-queries.json) / [тесты](tests/test_expansion_010.py) / [протокол](review-log.md#task-0006010) | Поля ввода/disabled, prepared/source, ID/строка и ожидание записи |
| [Тесты приёмки](tests/test_acceptance.py) / [протокол .005](review-log.md#task-0006005) | Проверка запросов, взаимности связей и устаревания без изменения источников |

Подробные объяснения остаются в [аудите](../code-audit/README.md); назначение справочника задано [требованиями](../system-index-requirements.md).

## Проверки

```bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
```

Пройдены все 188 тестовых методов, включая 552 CLI-примера (35 новых). Полный набор unittest discovery выполнен четырьмя независимыми группами модулей за 434.92 с; все группы завершились успешно. Это проверка справочника по исходникам, без исполнения игрового сценария. Стыки проверены в обоих направлениях. Актуальность и сохранность — в [протоколе](review-log.md#task-0006023).

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

## Применение урона и ресурсы — .019

- neighbors ent-000869 --direction in --relation calls — входы сообщения, статуса и критического урона.
- process proc-000269 — щит, ранний выход, масло, локации и последующие эффекты.
- process proc-000270 — изменение экземпляров, запрос записи shield и условный отчёт.
- process proc-000274 — SP, серебро, flat, коэффициент локации, сопротивления и износ.
- process proc-000272 — общий массив, Promise.all, суммирование и ожидаемое сообщение.
- field ent-004350 --access writes — расход JSON внутри changes; это отдельное поле от prepared TemporaryEffects.
- process proc-000273 — отбор временных HP, изменения ActiveEffect и конечный Actor.update.
- process proc-000286 — изменения prepared сообщения без ChatMessage.update.
- show ent-004369 — граница отсутствующего типа в статусном producer.
- show ent-004368 — raw result и требования общего шаблона.

[32 примера IQ-01–IQ-08](examples/expansion-019-queries.json) и [сверка](coverage-019.md) различают prepared документ, runtime экземпляры, JSON changes и запросы сохранения. Полная обработка чата/начала хода остаётся .020, травмы — .021.

## Чат, доставка и начало хода — .020

- process proc-000295 — UUID Item из attack сообщения и запуск rollDamage.
- process proc-000300 — guard Actor и пять prepared аргументов защиты.
- process proc-000302 — строка/UUID из кнопки, shield update и отдельное сообщение.
- process proc-000045 — общий query: whitelist, entity/system, true/false и отсутствие await.
- process proc-000046 — отдельный запрос временных улучшений.
- process proc-000306 — guard отправки и emit без подтверждения действия.
- process proc-000308 — activeGM, data.shift, UUID и unchecked fallback.
- process proc-000309 — реальный Combat и два запуска без await.
- process proc-000311 — сообщение, periodic damage и отдельный heal handoff.
- show ent-004468 — почему вложенный метод не достигается по Item.uuid.

[32 примера IQ-01–IQ-08](examples/expansion-020-queries.json) и [границы](coverage-020.md). Полные критические травмы — .021, регенерация и лечение — .022. Справочник различает регистрацию, запуск и локальный возврат; завершённая запись/межклиентская доставка ими не подтверждается.

## Критические травмы — .021

- find CriticalWoundData.followUp --match exact → ent-004491; writers — Drop специализированного листа.
- neighbors ent-004120 --direction out --relation calls → выбор/UUID, addItem и сообщение; процесс proc-000316 раскрывает ветви.
- process proc-000317 и process proc-000320 → два владельца calculateHealingTime, возврат и prepared запись различены.
- process proc-000322 → дни, стерилизация, порог вне treated и условная запись updates.
- process proc-000323 → followUp/UUID/create/delete; только загрузка ожидается.
- process proc-000329 → ручная кнопка с UUID; proc-000331 → callback отдыха, полный процесс в .022.
- details ent-004528 → три экспортных документа как свидетельство, граница runtime pack и issue-00325.

[32 проверочных запроса](examples/expansion-021-queries.json), [покрытие и ограничения](coverage-021.md), [протокол](review-log.md#task-0006021). Срок, дни и состояние не смешаны с применением embedded ActiveEffect.

## Лечение, отдых и спасброски — .022

- find actor.healMixin.calculateHealValue --match exact → ent-003593; входящие calls различают расходник и periodic heal.
- field ent-000055 --access writes → HP writers урона и разных путей восстановления; уточняйте --scope и страницу.
- process proc-000339 → checkbox/REC/bonuses/DOM; proc-000340 → ресурсы, травмы и отчёт с разным ожиданием.
- process proc-000347 → chat source/target, parseInt/max и сообщение; combat/heal.hbs не содержит этой кнопки.
- process proc-000348 и process proc-000349 → раздельные guards/лимиты/await регенерации и periodic heal.
- process proc-000350 → minus сбрасывает счётчик; proc-000352 → порог и 1d10 без автоматической записи смерти.
- details ent-004579 → пределы threshold/результата; соседние границы описывают DOM, отчёт и сохранение.

[32 проверочных запроса](examples/expansion-022-queries.json), [покрытие и ограничения](coverage-022.md), [протокол](review-log.md#task-0006022).

## Накопленная проверка — .023

- `find броня --match exact` → ArmorData и четыре ключа ru; `find healMixin --match exact` → две разные примеси.
- `neighbors ent-003555 --direction in --relation calls` → вход useItem из строки Item; для следующих вызовов выбирать направление и глубину.
- `field ent-000055 --access writes --scope src-000196` → два пути восстановления HP в Combat; ручные поля другого источника не исключаются.
- `process proc-000180 --offset 13 --limit 1` → output с альтернативами direct/message; показ страницы не меняет ветвление.
- `show ent-004526` → граница сохранения формы травмы; `details ent-003944` → исходные доказательства ограничения rollOnlyDmg.

[Матрица H01–H12, четыре маршрута и восемь IQ](coverage-023.md), [полный остаток](sources.jsonl), [протокол](review-log.md#task-0006023). Завершена очередь; общий справочник остаётся partial.

## Текущая очередь — .024–.034

[План и десять стыков](expansion-plan.md#third-wave): ручные ресурсы, хранение/улучшения Item, расы/профессии/развитие, магические данные, сотворение и регионы. Десять порций наполнения .024–.033 и завершающая сверка [TASK-0006.034](../../tasks/task-0006.034.md) done. Существующие записи, формат/CLI и исторические показатели сохранены; новая очередь не создавалась.

## Ресурсные формы — .024

[Покрытие и внешние контракты](coverage-024.md), [29 запросов](examples/expansion-024-queries.json), [сущности](data/entities/expansion-024.jsonl), [связи](data/relations/expansion-024.jsonl), [процессы](data/processes/expansion-024.jsonl).

- `field ent-000055 --access writes --scope src-000560` — ручной writer HP текущего Character sidebar.
- `field ent-000060 --access writes --scope src-000560` — пусто в этой области: Vigor только отображается.
- `process proc-000356` — типизация всей формы, isEditable, validate и внешний запрос update.
- `process proc-000359` — REC callback: guard → уведомление или запрос STA без ожидания.

Ручная форма, REC/full recovery, отдых и урон имеют отдельные входы. Общая схема stat().value не размножена; точные пути указаны в рёбрах и controls. Мир, браузер и сохранение БД не исполнялись.

## Контейнеры и вес — .025

[Покрытие и границы](coverage-025.md), [27 запросов](examples/expansion-025-queries.json), [сущности](data/entities/expansion-025.jsonl), [связи](data/relations/expansion-025.jsonl), [процессы](data/processes/expansion-025.jsonl).

- `field ent-004639 --access writes --scope src-000166` — изменения массива UUID при помещении и извлечении.
- `field ent-003388 --access writes --scope src-000166` — независимые записи isStored на исходном Item.
- `field ent-004638 --access reads` — потребители подготовленного веса; вложенный storedWeight не суммируется моделью.
- `process proc-000364` — общий Item-drop, guard контейнера и два запроса без ожидания.
- `process proc-000372` — удаление контейнера и внешний lifecycle без локального освобождения содержимого.

Carry/input, UUID и локальный Item ID, сохранение и prepared snapshots имеют отдельные узлы. Прежние процессы addItem/меню/carried/валюты переиспользованы. Справочник остаётся partial.

## Улучшения предметов и мутагены — .026

[Покрытие и границы](coverage-026.md), [26 запросов](examples/expansion-026-queries.json), [сущности](data/entities/expansion-026.jsonl), [связи](data/relations/expansion-026.jsonl), [процессы](data/processes/expansion-026.jsonl).

- `field ent-004675 --access writes` — установка/снятие applied у улучшения; отдельные записи связанных Item.
- `process proc-000379` — поздний OK: push, parent.update, enhancement.update и условная source-копия остатка.
- `field ent-003782 --access writes --scope src-000027` — подготовка листом live enhancementItems; исходные ID остаются прежними.
- `show ent-004694` — граница описательного текста мутагена и исполняемых consumeProperties/ActiveEffect.
- `neighbors ent-004691 --direction out --relation renders` — общий item-header с реальным select типа мутагена.

Прежние Weapon/Armor, SP/resistance, consume и временные улучшения продолжаются по тем же ID. Substances.hbs остаётся секцией веществ; мутагены выводятся общим alchemical partial. Покрытие partial.

## Расы, родина и биография — .027

[Покрытие и границы](coverage-027.md), [31 запрос](examples/expansion-027-queries.json), [сущности](data/entities/expansion-027.jsonl), [связи](data/relations/expansion-027.jsonl), [процессы](data/processes/expansion-027.jsonl).

- `field ent-004738 --access reads --scope src-000022` — реальное поле Actor для навыковой поправки.
- `field ent-004729 --access writes` — региональное поле Race Item и его отдельные writers.
- `process proc-000387` — приоритет Item родины над полями Actor.
- `process proc-000392` — UI key, prepared поиск и запрос source isOpened.
- `show ent-004786` — граница сохранения описания расы через Actor editor.

Текстовые особенности, региональный выбор, lifepathModifiers и жизненные события имеют разных владельцев и потребителей. Drop, модельная подготовка и ActiveEffect переиспользуют прежние ID/процессы; профессия остаётся .028, покрытие partial.

## Профессии: модели и редактор — .028

[Покрытие и границы](coverage-028.md), [33 запроса](examples/expansion-028-queries.json), [сущности](data/entities/expansion-028.jsonl), [связи](data/relations/expansion-028.jsonl), [процессы](data/processes/expansion-028.jsonl).

- `field ent-004804 --access reads` — набор базовых навыков, отдельно от десяти профессиональных слотов.
- `field ent-004839 --access writes` — writer конкретного поля строки порога.
- `process proc-000406` — поиск по имени в девяти слотах конфигуратора.
- `process proc-000407` — Actor сначала ищет definingSkill, затем пути.
- `process proc-000403` — data-target → lookup → randomID → Item.update без await.
- `show ent-004874` — несовпадение действия HBS и registry, без вымышленного успешного callback.

Механические schema поля, видимость UI и исполнение способности разделены. Прежняя профессиональная защита .016 и общие drop/inline/AE процессы используют существующие ID. Полное исполнение профессиональных навыков — следующая .029; общий справочник partial.

## Профессиональные броски и способности — .029

[Покрытие и границы](coverage-029.md), [35 запросов](examples/expansion-029-queries.json), [сущности](data/entities/expansion-029.jsonl), [связи](data/relations/expansion-029.jsonl), [процессы](data/processes/expansion-029.jsonl).

- `process proc-000409` — имя навыка и приоритет четырёх ветвей dispatch.
- `process proc-000410` — обычный бросок, custom modifier и RollConfig.
- `process proc-000411` — выбор порога до броска, в том числе пустой словарь.
- `process proc-000412` и `process proc-000413` — прямая атака и делегирование оружию.
- `process proc-000414` и `process proc-000415` — цель/сложность/успех и payload временных HP.
- `process proc-000416` — сообщение прямой атаки и поздняя кнопка damage без Item UUID.
- `field ent-004905 --access writes` — подготовленный ActiveEffect; не source update Actor HP.

Общие процессы броска, оружия, защиты, урона, чата и доставки AE переиспользованы. Исправлен адрес прежнего profession-roll listener: skillMixin.js:31, src-000045. Покрытие partial; следующая .030 — развитие навыков, IP и журнал обучения.

## Развитие навыков, IP и журнал — .030

[Покрытие и границы](coverage-030.md), [36 запросов](examples/expansion-030-queries.json), [сущности](data/entities/expansion-030.jsonl), [связи](data/relations/expansion-030.jsonl), [процессы](data/processes/expansion-030.jsonl).

- `process proc-000417` — builtin уровень, цена и два различных magicalCost.
- `process proc-000418` — prepared push истории и абсолютный update выбранного пула.
- `process proc-000419` и `process proc-000420` — ручные IP/training поля через форму Actor.
- `process proc-000421` — DOM-строка обучения и ручное списание обычных IP.
- `process proc-000422` и `process proc-000423` — wrappers API и типизированная форма награды.
- `process proc-000424` — GM/выбор/ip guards, Log, render и ChatMessage.create.
- `process proc-000425` — только просмотр IP истории в RewardsSheet.
- `field ent-004943 --access writes` — writers журнала; уровни Item/профессии и training отдельны.

Ранее описанные редакторы, броски и внешняя Actor форма переиспользованы. Запрос сохранения без await не объявлен завершённой записью. Автоматическое обучение из training не найдено в module/templates; внешние макросы не проверены. Покрытие partial; следующая .031 — магические модели, редакторы и компоненты ритуалов.

## Магические Item и компоненты ритуалов — .031

[Покрытие и границы](coverage-031.md), [43 запроса](examples/expansion-031-queries.json), [сущности](data/entities/expansion-031.jsonl), [связи](data/relations/expansion-031.jsonl), [процессы](data/processes/expansion-031.jsonl).

- `process proc-000426` — выбор навыка Spell; .427/.428 — собственные методы Hex/Ritual.
- `process proc-000429` и `process proc-000430` — source миграции Spell/Ritual; `process proc-000440` — миграция массивов воздействий.
- `process proc-000431`–`process proc-000433` — именованные поля трёх Item через унаследованную форму.
- `process proc-000434` — подготовка двух списков компонентов; .435/.436/.437 — drop/edit/remove.
- `process proc-000438` — конфигурация self/onCast через прежние общие обработчики.
- `process proc-000439` — четыре focus Actor: форма и последующее чтение при cast.

Spell, Hex и Ritual имеют разные возможности. Два массива ссылок компонентов и свободный текст не означают автоматического расходования при cast. Прямые consumers магических полей адресованы; полное сотворение — .032, регионы — .033. Покрытие partial.

## Сотворение магии — .032

[Покрытие и границы](coverage-032.md), [43 запроса](examples/expansion-032-queries.json), [сущности](data/entities/expansion-032.jsonl), [связи](data/relations/expansion-032.jsonl), [процессы](data/processes/expansion-032.jsonl).

- `process proc-000441` — списки Actor; .442 — V2 клик→useItem→castSpell.
- `process proc-000443` — WILL/навык/EV; .444 — prompt; .445 — оплата и исходная сила STA.
- `process proc-000446` — calcStaminaMulti; .447 — duration; .448 — damage/проценты; .449 — shield/heal.
- `process proc-000450` — flavor→typed сообщение→основной бросок.
- `process proc-000451` — region до fumble и четыре канала status/AE без ожидания.
- `process proc-000452` — полное локальное исполнение castSpell.
- `process proc-000453` — поздние кнопки damage/shield/heal и разные получатели.

Raw duration/HTML и typed damage не взаимозаменяемы. Оплата STA отделена от силы; опубликованное сообщение и возвращённый Roll не подтверждают завершение независимых update/эффектов. Legacy шаблон монстра не объявлен действующим V2 листом. Полный региональный lifecycle — .033; покрытие partial.

## Регионы магии — .033

[Покрытие и границы](coverage-033.md), [42 запроса](examples/expansion-033-queries.json), [сущности](data/entities/expansion-033.jsonl), [связи](data/relations/expansion-033.jsonl), [процессы](data/processes/expansion-033.jsonl).

- `process proc-000454` — региональная форма и её guard; .455 — миграция tokenPreMove.
- `process proc-000456` — запуск createSpellRegion и раннее завершение; .457 — geometry/raw flags.
- `process proc-000458` — placement/emanation; .459 — drawPreview и отмена.
- `process proc-000460` — UUID adapter; .461 — GM update/non-GM query; .462 — executeMacro payload и внешняя граница.
- `process proc-000463` — whitelist и вложенный owner метода.
- `process proc-000464` — visual seconds и будущая canvas Scene; .465 — Combat countdown активной Scene.

Один Region от placeRegion, массив эманаций и Promise не взаимозаменяемы. Raw flags не приравнены к сохранённому документу. Вызов метода/query не подтверждает update или исполнение Macro; оба удаления не синхронизированы. Внешний runtime и общий охват partial.

## Накопленная сверка третьей очереди — .034

[Результат и остаток](coverage-034.md), [44 запроса и 74 адресных свидетеля](examples/expansion-034-queries.json), [проверки](tests/test_expansion_034.py).

Проверены все десять стыков с прежними порциями в обе стороны. Путь от ручной формы, контейнера, улучшения, профессии или магии сохраняет владельца поля и различает подготовку, payload, запрос записи и внешнее завершение. Новые части графа не потребовались; у item-header.hbs уточнены два текста remaining.

Третья очередь завершена. Общий TASK-0006 остаётся in-progress: 305 файлов имеют определения, 310 — только каталог по этой грани; внутри partial-файлов остаются методы/читатели. Полный список и внешние ограничения приведены в coverage, новая очередь автоматически не создавалась.
