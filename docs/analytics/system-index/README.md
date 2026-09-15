# Справочник-граф системы

[TASK-0006.006](../../tasks/task-0006.006.md) дополняет прошедший [приёмку пилот](pilot-acceptance.md) регистрациями документов, листов, настроек и входами системы. [Границы расширения](coverage-006.md). Формат JSONL и Python 3 согласованы в [DEC-0001](../../documentation/decisions.md#dec-0001--формат-и-локальный-поиск-справочника).

**Текущий охват:** 615 исходников в каталоге; 27 основных и 81 смежный файл имеют частичные определения, 507 пока только в каталоге определений. В графе 636 сущностей, 1601 связь и 23 процесса (145 шагов, 200 переходов). [Расширение .006](coverage-006.md), [исторический пилот](pilot-coverage.md), [очередь](expansion-plan.md#первые-порции-расширения). Следующая — [TASK-0006.007](../../tasks/task-0006.007.md), редактор ActiveEffect и мастер изменений; полный индекс остаётся незавершённым.

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

Первый запрос различает Skill.activeEffectModifiers (ent-000012) и SkillItemData.activeEffectModifiers (ent-000188). У первого читатели — getter Skill.modifiedValue и actor.modifierMixin.addActiveEffects. Два skillMixin имеют разные файлы и ID: actor — ent-000299, sheet — ent-000305. processes ent-000012 показывает шаги getter и сборки модификаторов; processes src-000047 — proc-000004/000005.

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
| [Расширение](expansion-plan.md) / [полный перечень](expansion-inventory.json) | 615 файлов: исторические роли пилота и отдельное текущее покрытие; .006 выполнена, .007–.011 planned |
| [Расширение .006](coverage-006.md) / [сущности](data/entities/expansion-006.jsonl) / [отношения](data/relations/expansion-006.jsonl) / [процессы](data/processes/expansion-006.jsonl) | Регистрации, настройки, init/ready/updateCombat и смежные определения |
| [16 случаев .006](examples/expansion-006-queries.json) / [тесты](tests/test_expansion_006.py) / [протокол](review-log.md#task-0006006) | Проверка новой порции и её границ |
| [Тесты приёмки](tests/test_acceptance.py) / [протокол .005](review-log.md#task-0006005) | Проверка запросов, взаимности связей и устаревания без изменения источников |

Подробные объяснения остаются в [аудите](../code-audit/README.md); назначение справочника задано [требованиями](../system-index-requirements.md).

## Проверки

```bash
python3 -B -m unittest discover -s docs/analytics/system-index/tests -v
```

Пройдены 38 тестовых методов, включая 16 новых CLI-случаев .006; проверены все 1601 отношение в обоих направлениях. Проверка актуальности: 615 исходников, реестр, 634 документа и package Foundry — current. [Протокол и сохранность](review-log.md#task-0006006). Размеры старого пилота проверяются на исходных частях; его запросы продолжают проверяться на текущем графе. Игровое поведение этим не исполняется.

## Практический маршрут по пилоту

Начать с find по точному имени/alias, затем выбрать владельца через show. Для вызовов использовать neighbors с --relation calls и нужным направлением; для полей — field. Processes → process раскрывают участие и соседние шаги, details — карточку и конкретные доказательства. Например, details ent-000319 ведёт к позднему уточнению issue-00043 и R005-03.

При partial/none_in_scope проверить объявленный остаток и соответствующий исходник. При stale сначала проверить применимость исторических адресов; инструмент не обновляет индекс автоматически. Общий schema-field требует чтения payload конкретного обращения. Детали использования и измеренный объём ответов — в [приёмке](pilot-acceptance.md#объём-ответа-и-ручное-чтение).
