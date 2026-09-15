# Справочник-граф системы

[TASK-0006.011](../../tasks/task-0006.011.md) дополняет справочник всеми строковыми ключами en/ru и проверенными потребителями. [Покрытие и накопленная сверка](coverage-011.md). Формат JSONL v1 и CLI Python 3 сохранены; [согласованное решение](../../documentation/decisions.md#dec-0001--формат-и-локальный-поиск-справочника).

**Текущий охват:** 615 исходников; определения есть в 154 файлах (2 complete по строковым ключам, 152 partial), роли 60 основных/94 смежных, 461 без определений. В графе 3323 сущности, 7395 связей и 97 процессов (400 шагов, 608 переходов). [Расширение .011](coverage-011.md), [исторический пилот](pilot-coverage.md), [остаток](expansion-plan.md). Очередь .006–.011 выполнена; [следующая .012–.023](expansion-plan.md#second-wave) поставлена, первая — [TASK-0006.012](../../tasks/task-0006.012.md). Новые задачи ещё не выполнялись; фактическое покрытие не изменилось, полный индекс остаётся незавершённым.

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

Первый запрос различает Skill.activeEffectModifiers (ent-000012) и SkillItemData.activeEffectModifiers (ent-000188). У первого читатели — getter Skill.modifiedValue, actor.modifierMixin.addActiveEffects и форма edit-skills с disabled AE. Два skillMixin имеют разные файлы и ID: actor — ent-000299, sheet — ent-000305. processes ent-000012 показывает шаги getter, сборки модификаторов и отображения AE в форме; processes src-000047 — proc-000004/000005/000049.

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
| [Расширение](expansion-plan.md) / [полный перечень](expansion-inventory.json) | 615 файлов: исторические роли пилота и отдельное текущее покрытие; .006–.011 выполнены; остаток требует дальнейшей постановки |
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
| [24 случая .010](examples/expansion-010-queries.json) / [тесты](tests/test_expansion_010.py) / [протокол](review-log.md#task-0006010) | Поля ввода/disabled, prepared/source, ID/строка и ожидание записи |
| [Тесты приёмки](tests/test_acceptance.py) / [протокол .005](review-log.md#task-0006005) | Проверка запросов, взаимности связей и устаревания без изменения источников |

Подробные объяснения остаются в [аудите](../code-audit/README.md); назначение справочника задано [требованиями](../system-index-requirements.md).

## Проверки

```bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
```

Пройдены 87 тестовых методов и 197 CLI-случаев, включая 24 новых .011; проверены все 7395 отношений в обоих направлениях. Актуальность: 615 исходников, реестр, 668 документов и package Foundry — current. [Протокол и сохранность](review-log.md#task-0006011). Исторические случаи A01/A13/A23/A25/P08/P13/SUI-11 сохранены на соответствующих частях; текущие читатели и размеры проверяются отдельно. Игровое поведение не исполняется.

## Практический маршрут по пилоту

Начать с find по точному имени/alias, затем выбрать владельца через show. Для вызовов использовать neighbors с --relation calls и нужным направлением; для полей — field. Processes → process раскрывают участие и соседние шаги, details — карточку и конкретные доказательства. Например, details ent-000319 ведёт к позднему уточнению issue-00043 и R005-03.

При partial/none_in_scope проверить объявленный остаток и соответствующий исходник. При stale сначала проверить применимость исторических адресов; инструмент не обновляет индекс автоматически. Общий schema-field требует чтения payload конкретного обращения. Детали использования и измеренный объём ответов — в [приёмке](pilot-acceptance.md#объём-ответа-и-ручное-чтение).
