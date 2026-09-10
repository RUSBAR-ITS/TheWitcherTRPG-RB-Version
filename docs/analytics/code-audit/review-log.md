# Журнал перекрёстных сверок

Журнал фиксирует выполненные проверки и их пределы. [Реестр файлов](registry.md), [методика](README.md), [задачи](../../tasks/README.md).

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
