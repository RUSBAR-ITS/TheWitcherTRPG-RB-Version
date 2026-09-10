# Журнал перекрёстных сверок

## TASK-0002 — итоговая перекрёстная сверка

Дата: 2026-09-10. Ветка rusbar-main; HEAD проверки `3252300787c348e11f95098c345a6af7704b690c`. Все исследуемые исходники совпали со срезом TASK-0001 `15da5b225535e34af4e132c701b5353ef4eb667f`. Установленное ядро — 14.367.0; это отдельно прочитанная версия, не вывод из compatibility манифеста.

| Проверка | Результат и пределы |
| --- | --- |
| Git и независимый обход дерева с согласованными исключениями | 621 одинаковый путь; исключённые файлы не получили строк реестра |
| Реестр и карточки | Ровно 11 файлов TASK-0002 имеют существующие карточки и статус «Проверено»; остальные 610 — «Не начат» |
| Полнота карточек | Все 11 исходников прочитаны полностью; обязательные разделы, версии и условия проверки присутствуют |
| Связи | Проверены импорты/определения/вызовы и реестры, примеси Actor/Item, helper sum, отправители query/socket, потребители настроек |
| Согласованность порций | Итог проверки четырёх дополнительных типов перенесён в манифест; языковые поля и namespace-импорты уточнены в точке входа; номера строк сверены |
| Конфигурация и шаблоны | Описаны 36 разделов, 21 ключ statMap, 52 навыка, 24 записи Crit, 26 статусов; сверены 59 путей шаблонов и 17 helpers |
| Проблемы | Девять новых карточек issue-00002–issue-00010; вместе с существовавшей issue-00001 — десять уникальных ID, все potential |
| Markdown | Проверены локальные пути ссылок, число столбцов таблиц, обязательные разделы и концевые пробелы; код не трактуется как навигация |
| Неизменность системы | Все 621 исходник совпали с Git blob обеих указанных версий; изменены и созданы только файлы docs |
| Метаданные доступа | Для 726 существовавших на старте путей проверены mode, uid, gid и inode: различий и пропавших путей нет; после завершающих правок проверка повторена |
| Пределы | Статическое чтение и изолированное выполнение с подменами не подтверждают запуск мира, браузер, межклиентскую доставку и игровую корректность всех механик |

Контрольные суммы состава и содержимого равны TASK-0001: `f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8` и `ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f`. Их вычисление приведено ниже.

TASK-0002 завершена; README, реестр, задача и CHANGELOG согласованы с результатом. TASK-0003–TASK-0005 остаются заготовками. Регистрация potential issues не является подтверждением пользователя, исправлением или постановкой задачи.

### Повторная проверка результата TASK-0002

Запуск из корня системы. Команда проверяет именно указанный HEAD и результат этапа. После нового коммита сначала сопоставить исследуемые исходники, прежде чем менять ожидаемую версию. Метаданные доступа проверялись отдельно относительно снимка начала работы; этот снимок не добавлялся в репозиторий.

```bash
python3 - <<'PY'
from pathlib import Path
from urllib.parse import unquote
import collections, hashlib, json, os, re, subprocess

BASE = "15da5b225535e34af4e132c701b5353ef4eb667f"
HEAD = "3252300787c348e11f95098c345a6af7704b690c"
audit = Path("docs/analytics/code-audit")
expected_cards = {
    "system.json", "module/TheWitcherTRPG.js",
    *("module/setup/" + name + ".js" for name in (
        "config", "registerDataModels", "registerSheets", "settings", "hooks",
        "handlebars", "queries", "socketHook", "deprecations"
    ))
}
excluded_files = {
    "README.md", "AGENTS.md", "LICENSE", ".gitignore", ".prettierrc",
    ".prettierignore", "jsconfig.json.default", "package-lock.json",
    "styles/fonts/thewitcher2.ttf"
}
def excluded(p):
    return (p.split("/")[0] in {"docs", "assets", ".github", ".git"}
            or p in excluded_files
            or (p.startswith("packs/") and Path(p).name == "LOCK"))
def git(*args):
    return subprocess.check_output(["git", *args])
assert git("rev-parse", "HEAD").decode().strip() == HEAD
tracked = git("ls-files", "-z").decode().split("\0")[:-1]
included = sorted(p for p in tracked if not excluded(p))
assert len(included) == 621
actual = []
for directory, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not excluded(str((Path(directory)/d).as_posix()))]
    actual.extend(str((Path(directory)/f).as_posix()) for f in files
                  if not excluded(str((Path(directory)/f).as_posix())))
assert sorted(actual) == included
rows = {}
for line in (audit/"registry.md").read_text().splitlines():
    m = re.match(r"\| \[([^]]+)\]\([^)]*\) \| (.*?) \| (.*?) \| (.*?) \|$", line)
    if m:
        path, purpose, desc, status = m.groups()
        assert path not in rows
        rows[path] = (purpose, desc, status)
assert sorted(rows) == included
assert {p for p, r in rows.items() if r[2] == "Проверено"} == expected_cards
assert all(r[2] == "Не начат" for p, r in rows.items() if p not in expected_cards)
cards = {str(p.relative_to(audit/"files"))[:-3]: p
         for p in (audit/"files").rglob("*.md") if p.name != "README.md"}
assert set(cards) == expected_cards
headings = [
    "Назначение файла", "Условия использования", "Введённые сущности и действия с ними",
    "Основные функции и методы", "Используемые сущности и зависимости",
    "Известные потребители", "Данные и изменения состояния", "Проверки и доказательства",
    "Непроверенные участки и открытые вопросы", "Связанные проблемы", "История актуализации"
]
for source, path in cards.items():
    text = path.read_text()
    assert all("\n## " + h + "\n" in text for h in headings)
    assert HEAD in text and BASE in text and "| Статус анализа | Проверено |" in text
    assert rows[source][1] == "[Карточка](files/" + source + ".md)"
for commit in (BASE, HEAD):
    blobs = {}
    for entry in git("ls-tree", "-rz", commit).split(b"\0")[:-1]:
        info, path = entry.split(b"\t", 1)
        blobs[path.decode()] = info.decode().split()[2]
    for path in included:
        data = Path(path).read_bytes()
        assert hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == blobs[path]
path_hash = hashlib.sha256(("\n".join(included)+"\n").encode()).hexdigest()
data_hash = hashlib.sha256(b"".join(
    p.encode()+b"\0"+hashlib.sha256(Path(p).read_bytes()).digest()+b"\n"
    for p in included)).hexdigest()
assert path_hash == "f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8"
assert data_hash == "ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f"
issues = list(Path("docs/issues").glob("*/issue-*.md"))
assert len(issues) == 10
assert {p.stem for p in issues} == {"issue-" + str(n).zfill(5) for n in range(1, 11)}
assert all(p.parent.name == "potential" for p in issues)
issue_registry = Path("docs/issues/README.md").read_text()
assert all("[{0}](potential/{0}.md)".format(p.stem) in issue_registry for p in issues)
links = 0
for p in Path("docs").rglob("*.md"):
    text = p.read_text()
    assert all(line == line.rstrip() for line in text.splitlines()), str(p)
    clean = re.sub(r"^\x60\x60\x60[^\n]*\n.*?^\x60\x60\x60\s*$", "", text, flags=re.M|re.S)
    no_code = re.sub(r"\x60[^\x60\n]*\x60", "", clean)
    for url in re.findall(r"\[[^]\n]+\]\(([^\s)]+)\)", no_code):
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url):
            continue
        target = unquote(url.split("#", 1)[0])
        assert (p.parent/target if target else p).exists(), (str(p), url)
        links += 1
    width = None
    for line in clean.splitlines():
        if line.startswith("|"):
            columns = len(re.split(r"(?<!\\)\|", line))-2
            if width is None: width = columns
            assert width == columns, (str(p), line)
        else: width = None
git("diff", "--check")
changes = git("diff", "--name-only").decode().splitlines()
untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
assert all(p.startswith("docs/") for p in changes + untracked)
print(json.dumps({
    "included": len(included), "cards": len(cards), "notStarted": 610,
    "issuesPotential": len(issues), "localLinks": links,
    "pathHash": path_hash, "dataHash": data_hash,
    "sourceMatches": [BASE, HEAD], "onlyDocsChanged": True
}, ensure_ascii=False))
PY
```

## TASK-0002 — порция 1: манифест и точка входа

Дата: 2026-09-10. Коммит проверки: `3252300787c348e11f95098c345a6af7704b690c`; исходники совпадают со срезом `15da5b225535e34af4e132c701b5353ef4eb667f`. Между срезом и HEAD изменена только документация. Рабочее дерево на старте чистое. Установленное ядро — 14.367.0 по `/opt/foundryvtt/package.json`.

Полностью прочитаны system.json (195 строк) и module/TheWitcherTRPG.js (172 строки). Проверены 21 импорт и экспорты источников, соответствие ES-модуля манифесту, существование CSS и восьми локализаций, имена packFolders. Семь буквальных путей packs отсутствуют в checkout; сборка и обработка путей ядром не проверялись, поэтому это не объявлено ошибкой релиза.

Сверены вызовы регистрации и определения обработчиков чата, классов документов, API наград/эффектов, метод WitcherActor.useItem и потребители game.api в rewardsMixin. Проверка зависимого определения не считается полным разбором его файла. Типы данных и листов дополнительно сверяются в порции 3.

Изолированно выполнен исходный ready callback в Node vm с подменой импортов и Foundry API: без pack — TypeError и отсутствие дальнейших шагов; контрольный pack дал getIndex, hotbarDrop, socket, deprecations. Зарегистрирована [issue-00002](../../issues/potential/issue-00002.md). Браузерные сценарии и исполнение макроса не проверялись.

Результат: две карточки, две строки «Проверено». Исходники не изменялись. Итоговая проверка ссылок и покрытия выполняется также после всех порций.

## TASK-0002 — порция 2: конфигурация

Дата: 2026-09-10; HEAD `3252300787c348e11f95098c345a6af7704b690c`, исходник равен срезу TASK-0001. Полностью прочитаны 2431 строка config.js последовательными частями. Сверены все 36 свойств WITCHER, в том числе 52 навыка, 24 записи Crit, 26 статусов. Модуль без импортов выполнен из строки в Node: подсчитаны ключи и разобраны все JSON-строки в changes статусов.

Буквальные обращения CONFIG.WITCHER и шаблонного config сопоставлены с определениями; динамические группы проверены в modifierMixin/baseMixin. Сверены поля Stat, Skill, combatEffects и intData. Прямой буквальный потребитель Crit не найден; damageMixin.applyCritWound читает компедиум. Недостижимость Crit через динамический доступ не утверждается.

Изолированные вызовы настоящего кода с подменой Foundry API: handleStatusCounterIntegration при активном statuscounter и duration=2 даёт TypeError; chooseSkill для общего языка возвращает путь с commonspeech вместо существующего commonsp. Зарегистрированы [issue-00003](../../issues/potential/issue-00003.md) и [issue-00004](../../issues/potential/issue-00004.md). Реальный statuscounter, сохранение эффекта и бросок в мире не запускались.

В ядре 14.367.0 дополнительно проверен setter CONFIG.statusEffects (/opt/foundryvtt/client/client.mjs:30–38), копирующий переданный массив в реестр ядра: присваивание в init само по себе не объявлено ошибкой. Строковые типы changes сверены с миграцией формата в /opt/foundryvtt/common/documents/active-effect.mjs.

Результат: карточка и её связи сверены; пределы поиска и динамические связи явно отмечены. Проверка зависимых определений не выдана за полный разбор их файлов.

## TASK-0002 — порция 3: модели, листы и настройки

Дата: 2026-09-10; тот же HEAD и базовый срез. Полностью прочитаны registerDataModels.js (81 строка), registerSheets.js (145), settings.js (96). Проверены определения 33 импортов моделей/документа чата и 26 импортов листов. Оба регистратора сопоставлены между собой, с манифестом и вызовами из init.

В Node vm выполнены исходные функции с подменой классов и регистрационных API: 4 модели Actor, 22 Item с base, 2 ActiveEffect, 4 ChatMessage; отдельный класс WitcherChatMessage. Листы: 21 Item, 4 Actor, unregister/register ActiveEffect. Настройки: 9 ключей; callback choices на фиктивных Item/Actor pack вернул только Item.

Actor.mystery и Item.clue/obstacle/skill отсутствуют в documentTypes — [issue-00005](../../issues/potential/issue-00005.md). По ядру проверено: Document.TYPES читает game.model; DocumentTypeField проверяет этот список; DocumentSheetConfig допускает отдельную запись sheetClasses[type]. Падение регистрации листов не утверждается. Создание документов в действующем мире не проверено.

Буквальные чтения девяти настроек сверены с module/templates, включая helper getSetting. Наличие чтений в V1-файле не выдано за используемый интерфейс. Карточки разделяют регистрацию, создание модели и рендер. Результат: три карточки и их связи сверены; реальные Foundry-классы и UI не запускались.

## TASK-0002 — порция 4: события, шаблоны, запросы и сокет

Дата: 2026-09-10; тот же HEAD `3252300787c348e11f95098c345a6af7704b690c` и срез TASK-0001. Полностью прочитаны hooks.js (13 строк), handlebars.js (217), queries.js (51), socketHook.js (24), deprecations.js (7). Разделены импорт, регистрация и вызов обработчика. Проверены источники импортов, динамические методы Actor/Item, их подключение примесями, отправители запросов и сокета.

В handlebars сверены 59 существующих шаблонов и 17 helpers; буквальные потребители собраны по templates/**/*.hbs и сопоставлены с регистрацией. Неявная зависимость getOwnedComponentCount → findNeededComponent → Array.prototype.sum подтверждена определениями craftingMixin/ActorSheet и подключением к Actor. Это не утверждение полного разбора зависимых файлов.

Изолированные проверки исходных функций в Node vm с подменой API:

- hooks + два настоящих зависимых обработчика: update флагов без round/turn записал HP 5→7 и duration региона 3→2 — [issue-00006](../../issues/potential/issue-00006.md).
- Helpers: получены 59 путей и 17 регистраций; проверены сравнение, CSV, разность, and/or, capitalize, eachLimit за числом ключей и перепутанные подписи ног — [issue-00007](../../issues/potential/issue-00007.md). eachLimit описан без утверждения достижимости ошибочного входа из UI.
- Query: true до разрешения Promise цели и при отсутствии метода; unknown=false, constructor=true — [issue-00008](../../issues/potential/issue-00008.md). Цели подменены управляемыми заглушками; реальные операции не выполнялись.
- Query регионов: вложенный метод не вызван при true, deleteSpellVisualEffect=false. Настоящий deleteSpellVisualEffect при isGM=false даёт ReferenceError: item is not defined — [issue-00009](../../issues/potential/issue-00009.md).
- Сокет: addItem передал аргументы нужному UUID и удалил его из message.data; unknown на активном GM дал TypeError, другой пользователь проигнорирован — [issue-00010](../../issues/potential/issue-00010.md).

Пустой deprecationWarnings проверен чтением; запуск функции без тела не выдаётся за отдельный тест. Для внешнего поведения дополнительно прочитаны локальные User.query и loadTemplates ядра 14.367.0. Мир, сеть между клиентами, настоящий statuscounter, Handlebars-рендер и canvas не запускались.

Результат: пять карточек сверены с первичными исходниками, регистрациями/вызовами в точке входа и установленными потребителями. Найденные проблемы зарегистрированы только как potential; исходники и данные не исправлялись.

## 2026-09-10 — TASK-0001: состав исследуемого среза

| Поле | Значение |
| --- | --- |
| Задача | [TASK-0001](../../tasks/task-0001-code-inventory.md) |
| Ветка | `rusbar-main` |
| Коммит | `15da5b225535e34af4e132c701b5353ef4eb667f` |
| Начальная проверка состава | `2026-09-10 07:12:58 UTC` |
| Рабочее дерево до записи материалов | Чистое |
| Область проверки | Полный перечень файлов после согласованных исключений; существование и версия исходников |

### Выполненная сверка источников перечня

| Проверка | Способ | Полученный результат |
| --- | --- | --- |
| Исходная версия | `git rev-parse HEAD`, `git branch --show-current`, `git status --porcelain=v1` | Коммит и ветка выше; вывод статуса на старте пустой |
| HEAD и индекс Git | `git ls-tree -rz --name-only HEAD` и `git ls-files -z` | По 706 путей; разность множеств пуста |
| Применение исключений | Сопоставление путей с согласованными 14 правилами | 85 отслеживаемых файлов исключены, 621 включён |
| Фактическое дерево без правил Git ignore | `rg --files --hidden --no-ignore --null` с исключением служебных каталогов, затем согласованных файлов | 621 включённый путь |
| Независимый обход каталогов | `os.walk` с теми же явными исключениями | 621 путь; разности с Git и `rg` пусты |
| Игнорируемые файлы | `git ls-files --others --ignored --exclude-standard -z` | На старте не найдено |
| Неотслеживаемые файлы | `git ls-files --others --exclude-standard -z` | На старте не найдено |
| Чтение и тип включённых файлов | `lstat` и чтение байтов каждого файла | Ошибок чтения и обхода нет; все 621 файла обычные, без символических ссылок |
| Содержимое относительно коммита | Сопоставление Git blob SHA-1 прочитанных байтов с объектами `git ls-tree -rz HEAD` | Все 621 файла совпали с коммитом |

### Учёт исключений

Количество относится к отслеживаемым файлам зафиксированного коммита. Содержимое `.git/` не перечислялось и в Git-перечень не входит.

| Правило | Исключено отслеживаемых файлов |
| --- | --- |
| `docs/` | 28 |
| `assets/` | 39 |
| `.github/` | 4 |
| `.git/` | 0 |
| `README.md` | 1 |
| `AGENTS.md` | 1 |
| `LICENSE` | 1 |
| `.gitignore` | 1 |
| `.prettierrc` | 1 |
| `.prettierignore` | 1 |
| `jsconfig.json.default` | 1 |
| `package-lock.json` | 1 |
| `styles/fonts/thewitcher2.ttf` | 1 |
| `packs/**/LOCK` | 5 |
| **Всего** | **85** |

Рост относительно оценки 701 / 80 обусловлен пятью добавленными файлами задач в `docs/`. Анализируемый состав остался прежним: 621 файл.

### Контрольные суммы

| Проверяемый набор | SHA-256 |
| --- | --- |
| Отсортированный перечень 621 пути | `f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8` |
| Пути и содержимое 621 файла | `ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f` |

Для первой суммы пути сортируются лексикографически, соединяются переводами строки с завершающим переводом строки и кодируются UTF-8. Для второй в том же порядке объединяются UTF-8 путь, нулевой байт, 32 байта SHA-256 содержимого и перевод строки; затем считается SHA-256 объединения.

### Повторная проверка реестра

Команда запускается из корня системы. Она проверяет именно результат TASK-0001 с ещё не начатым пофайловым разбором. После появления карточек ожидаемые статусы и их количество должны проверяться по результатам соответствующей порции; исходная запись этой сверки сохраняется.

```bash
python3 - <<'PY'
from pathlib import Path, PurePosixPath
from urllib.parse import unquote
import collections, hashlib, json, os, re, subprocess

SNAPSHOT = "15da5b225535e34af4e132c701b5353ef4eb667f"
audit = Path("docs/analytics/code-audit")
expected_rules = [
    "docs/", "assets/", ".github/", ".git/",
    "README.md", "AGENTS.md", "LICENSE", ".gitignore", ".prettierrc",
    ".prettierignore", "jsconfig.json.default", "package-lock.json",
    "styles/fonts/thewitcher2.ttf", "packs/**/LOCK",
]

def output(*args):
    return subprocess.check_output(args).decode()

def excluded(path):
    for rule in expected_rules:
        if rule.endswith("/") and path.startswith(rule):
            return True
        if rule == "packs/**/LOCK":
            if path.startswith("packs/") and PurePosixPath(path).name == "LOCK":
                return True
        elif path == rule:
            return True
    return False

def documented_rules(path):
    text = path.read_text()
    section = text.split("## Согласованные исключения\n", 1)[1].split("\n## ", 1)[0]
    return re.findall(r"^\| `([^`]+)` \|", section, re.M)

assert documented_rules(audit / "README.md") == expected_rules
assert documented_rules(Path("docs/tasks/task-0001-code-inventory.md")) == expected_rules
tree = [p for p in output("git", "ls-tree", "-rz", "--name-only", SNAPSHOT).split("\0") if p]
expected = sorted(p for p in tree if not excluded(p))
current_git = {p for p in output("git", "ls-files", "-z").split("\0") if p and not excluded(p)}
rg_paths = {
    p for p in output("rg", "--files", "--hidden", "--no-ignore", "--null",
                      "-g", "!.git/**", "-g", "!docs/**", "-g", "!assets/**", "-g", "!.github/**").split("\0")
    if p and not excluded(p)
}
walk_paths, walk_errors = set(), []
for directory, dirs, files in os.walk(".", followlinks=False, onerror=lambda e: walk_errors.append(str(e))):
    base = Path(directory)
    dirs[:] = [d for d in dirs if not excluded((base / d).as_posix() + "/")]
    for name in files:
        path = base / name
        if not excluded(path.as_posix()):
            assert path.is_file() and not path.is_symlink(), path
            walk_paths.add(path.as_posix())
assert not walk_errors, walk_errors
assert set(expected) == current_git == rg_paths == walk_paths
rows = re.findall(
    r"^\| \[([^\]]+)\]\(([^)]+)\) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$",
    (audit / "registry.md").read_text(), re.M
)
paths = [row[0] for row in rows]
assert len(paths) == len(set(paths)) and paths == expected
assert all(row[2:] == ("Не установлено", "Не подготовлено", "Не начат") for row in rows)
for path, target, *_ in rows:
    assert (audit / unquote(target)).resolve() == Path(path).resolve()
cards = [p for p in (audit / "files").rglob("*.md") if p != audit / "files/README.md"]
assert not cards, cards

digest = hashlib.sha256()
for path in expected:
    digest.update(path.encode() + b"\0" + hashlib.sha256(Path(path).read_bytes()).digest() + b"\n")
paths_hash = hashlib.sha256(("\n".join(expected) + "\n").encode()).hexdigest()
assert paths_hash == "f6291adae3b89183f60336e7cee8c74afe45ed8dddd3d5a19b68e2e458a4f3d8"
assert digest.hexdigest() == "ff62af9c097bf62087f4a67485e78fab808a46008067a323f7478c0d56e9e88f"

links, anchors, errors = 0, 0, []
markdown = [Path("README.md"), Path("AGENTS.md"), *sorted(Path("docs").rglob("*.md"))]
for file in markdown:
    text = file.read_text()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.rstrip() != line:
            errors.append(f"{file}:{index + 1}: trailing whitespace")
        if line.startswith("#") and index + 1 < len(lines) and lines[index + 1].strip():
            errors.append(f"{file}:{index + 1}: no blank line after heading")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.strip().strip("<>")
        if re.match(r"^[a-zA-Z][\w+.-]*:", target):
            continue
        name, sep, fragment = target.partition("#")
        destination = file.parent / unquote(name) if name else file
        if not destination.exists():
            errors.append(f"{file}: missing {target}")
        elif destination.is_file() and destination.suffix == ".md" and sep and fragment:
            headings = re.findall(r"^#+\s+(.+)$", destination.read_text(), re.M)
            slugs = {re.sub(r"[^\w\s-]", "", h.lower()).replace(" ", "-") for h in headings}
            if unquote(fragment) not in slugs:
                errors.append(f"{file}: missing heading {target}")
            anchors += 1
        links += 1
assert not errors, errors
subprocess.run(["git", "diff", "--check"], check=True)
print(json.dumps({
    "snapshot": SNAPSHOT,
    "tracked_in_snapshot": len(tree),
    "excluded_in_snapshot": len(tree) - len(expected),
    "registry_rows": len(paths),
    "git_rg_walk_equal": True,
    "file_cards": len(cards),
    "content_unchanged": True,
    "local_links": links,
    "heading_anchors": anchors,
    "markdown_files": len(markdown),
    "groups": dict(sorted(collections.Counter(p.split("/")[0] if "/" in p else "(root)" for p in paths).items())),
    "errors": []
}, ensure_ascii=False, indent=2))
PY
```

### Результат проверки готовых документов

Приведённая команда выполнена после создания материалов и повторно после оформления итогов; оба запуска завершились с кодом 0. Итоговая проверка охватила 35 Markdown-документов, 813 локальных ссылок и 5 ссылок на заголовки. Состав реестра и контрольные суммы повторно совпали с исходной проверкой.

| Проверка | Результат |
| --- | --- |
| Строки реестра против Git, `rg` и обхода каталогов | 621 уникальная строка; множества путей совпали в обе стороны; порядок соответствует сортировке |
| Исключения в задаче и README | Все 14 согласованных правил совпадают; исключённых файлов в реестре нет |
| Ссылки на исходники | Каждый путь ведёт к соответствующему существующему файлу |
| Назначения, карточки и статусы | Во всех 621 строках «Не установлено», «Не подготовлено», «Не начат»; карточек исходников нет; `files/README.md` учитывается как указатель |
| Шаблон карточки | Сверен с требованиями: назначение, определения, функции и методы, действия с данными, зависимости, потребители, доказательства, ограничения и проблемы предусмотрены |
| Контрольные суммы исходников | Перечень и содержимое совпали с начальной проверкой |
| Локальные ссылки и якоря заголовков | Ошибок не выявлено; ссылки на каталоги также проверены |
| Markdown и `git diff --check` | Пробелов в конце строк и ошибок проверяемого оформления нет |
| Метаданные доступа существующих файлов | Права, владельцы, группы и inode сохранены |

TASK-0001 завершена как инвентаризация и подготовка основы. Появление 621 строки не означает завершения пофайлового анализа. Реестр и документы результатов находятся в исключённой папке `docs/` и не увеличивают исследуемый состав.

### Пределы вывода

Совпадение путей и содержимого подтверждает состав и версию исследуемых файлов. В этом этапе не проверялись назначения отдельных файлов, функции, межфайловые связи, загрузка системы или игровые сценарии. Базы компедиумов не собирались и не извлекались.

Новых проблем системы при сверке состава не выявлено. Отсутствие новых карточек проблем на этапе инвентаризации не означает исправности кода.
