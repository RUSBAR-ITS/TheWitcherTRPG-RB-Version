"""Локальный справочник системы: только чтение JSONL и доступных источников."""

import argparse
from collections import Counter, defaultdict, deque
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MANIFEST = Path(__file__).resolve().with_name("manifest.json")
KINDS = set("class function method getter field handler event setting template document boundary".split())
RELATIONS = set("defines imports extends mixes registers calls constructs reads writes computes passes emits handles renders refers embeds".split())
STATES = {"not_indexed", "partial", "complete"}
PREFIXES = {"sources": "src", "entities": "ent", "relations": "rel", "processes": "proc"}
NEXT_KEYS = {"sources": "source", "entities": "entity", "relations": "relation", "processes": "process"}
ID_PATTERN = re.compile(r"(src|ent|rel|proc)-[0-9]{6,}")
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")


class IndexErrorDetail(Exception):
    def __init__(self, code, message, record=None, status=1):
        super().__init__(message)
        self.detail = {"code": code, "message": message}
        if record is not None:
            self.detail["record"] = record
        self.status = status


def require(ok, code, message, record=None):
    if not ok:
        raise IndexErrorDetail(code, message, record)


def fields(value, schema, label):
    require(isinstance(value, dict), "invalid_shape", "Ожидается объект", label)
    for key, typ in schema.items():
        require(key in value and type(value[key]) is typ, "invalid_field",
                f"Поле {key}: ожидается {typ.__name__}", label)


def strings(value, label):
    require(isinstance(value, list) and all(isinstance(x, str) and x for x in value),
            "invalid_list", "Ожидается список непустых строк", label)
    require(len(value) == len(set(value)), "duplicate_value", "Повтор в списке", label)


def identifier(value, prefix=None):
    return (isinstance(value, str) and ID_PATTERN.fullmatch(value) is not None
            and int(value.split("-")[1]) > 0
            and (prefix is None or value.startswith(prefix + "-")))


def local_path(base, value):
    require(isinstance(value, str) and value and not Path(value).is_absolute(),
            "invalid_path", "Ожидается относительный путь", value)
    try:
        path = (base / value).resolve()
    except (OSError, ValueError, RuntimeError) as exc:
        raise IndexErrorDetail("invalid_path", str(exc), value) from exc
    require(path.is_relative_to(base.resolve()), "path_escape", "Путь выходит за разрешённый корень", value)
    return path


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate_key", f"Повтор ключа JSON: {key}")
        result[key] = value
    return result


def parse_json(text, label):
    try:
        return json.loads(text, object_pairs_hook=unique_object,
                          parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
    except IndexErrorDetail as exc:
        exc.detail.setdefault("record", label)
        raise
    except (ValueError, RecursionError) as exc:
        raise IndexErrorDetail("invalid_json", str(exc), label) from exc


def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError, ValueError) as exc:
        raise IndexErrorDetail("load_error", str(exc), str(path)) from exc


def aggregate(states):
    values = set(states)
    return next(iter(values)) if len(values) == 1 else "partial"


def anchors(text):
    result = set(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    fence = chr(96) * 3
    text = re.sub("(?ms)^" + fence + r".*?^" + fence + r"\s*\n?", "", text)
    counts = Counter()
    for heading in re.findall(r"^#{1,6}[ \t]+(.+?)\s*#*\s*$", text, re.M):
        heading = re.sub(r"<[^>]*>", "", heading).strip().lower()
        slug = "".join(c for c in heading if c in " -_" or unicodedata.category(c)[0] in "LN"
                       or unicodedata.category(c) in ("Mn", "Mc")).replace(" ", "-")
        n = counts[slug]
        counts[slug] += 1
        result.add(slug + (f"-{n}" if n else ""))
    return result


class Dataset:
    def __init__(self, manifest=DEFAULT_MANIFEST, root=ROOT):
        self.root = Path(root).resolve()
        self.path = Path(manifest).resolve()
        self.manifest = parse_json(read_text(self.path), str(self.path))
        m = self.manifest
        fields(m, {"format_version": int, "dataset_id": str, "purpose": str, "approval": str,
                   "snapshot": dict, "scope": dict, "parts": dict, "next_ids": dict, "retired_ids": list}, "manifest")
        require(m["format_version"] == 1, "unsupported_version", "Поддерживается format_version=1")
        require(m["approval"] in {"pending", "approved"}, "invalid_approval", "Неизвестное состояние согласования")
        fields(m["snapshot"], {"date": str, "branch": str, "head": str, "source_hash": str}, "snapshot")
        require(re.fullmatch(r"[0-9a-f]{40}", m["snapshot"]["head"]), "invalid_hash", "Некорректный HEAD")
        fields(m["scope"], {"registry": str, "registry_sha256": str, "source_count": int,
                           "selected_sources": list, "semantic_scope": str, "global_coverage": str}, "scope")
        require(set(m["parts"]) == set(PREFIXES), "invalid_parts", "Нужны четыре вида частей")
        self.records = {}
        used_parts = set()
        for kind, paths in m["parts"].items():
            strings(paths, f"parts.{kind}")
            records = {}
            for value in paths:
                path = local_path(self.path.parent, value)
                require(path not in used_parts, "duplicate_part", "Часть подключена повторно", value)
                used_parts.add(path)
                rows = []
                for number, line in enumerate(read_text(path).splitlines(), 1):
                    if not line.strip():
                        continue
                    label = f"{value}:{number}"
                    row = parse_json(line, label)
                    fields(row, {"id": str}, label)
                    rid = row["id"]
                    require(identifier(rid, PREFIXES[kind]), "invalid_id", "Некорректный ID", label)
                    require(rid not in records, "duplicate_id", "ID уже определён", rid)
                    records[rid] = row
                    rows.append(rid)
                require(rows == sorted(rows), "invalid_order", "Часть не упорядочена по ID", value)
            self.records[kind] = records
        self.sources, self.entities, self.relations, self.processes = (
            self.records[k] for k in ("sources", "entities", "relations", "processes"))
        self.nodes = {**self.sources, **self.entities}
        self.all = {**self.nodes, **self.relations, **self.processes}
        self.doc_hashes = {}
        self.dependencies = m.get("dependencies", {})
        require(isinstance(self.dependencies, dict), "invalid_shape", "dependencies должен быть объектом")
        self._validate()
        self.outgoing, self.incoming = defaultdict(list), defaultdict(list)
        for rel in sorted(self.relations.values(), key=lambda x: x["id"]):
            self.outgoing[rel["from"]].append(rel)
            self.incoming[rel["to"]].append(rel)

    def _hash(self, value, label):
        require(isinstance(value, str) and SHA_PATTERN.fullmatch(value), "invalid_hash", "Некорректный SHA-256", label)

    def _document(self, path, sha):
        local_path(self.root, path)
        self._hash(sha, path)
        require(path not in self.doc_hashes or self.doc_hashes[path] == sha,
                "conflicting_hash", "Разные хеши одного документа", path)
        self.doc_hashes[path] = sha

    def _location(self, loc, label):
        fields(loc, {"source": str, "symbol": str, "line_start": int, "line_end": int}, label)
        require(loc["source"] in self.sources, "unknown_source", "Неизвестный источник", label)
        require(loc["symbol"] and 1 <= loc["line_start"] <= loc["line_end"],
                "invalid_location", "Неверный символ или диапазон строк", label)

    def _refs(self, row):
        refs = row.get("refs", [])
        require(isinstance(refs, list), "invalid_refs", "refs должен быть списком", row["id"])
        for ref in refs:
            fields(ref, {"path": str, "relation": str}, row["id"])
            local_path(self.root, ref["path"])
            require(ref["path"] in self.doc_hashes, "unversioned_ref", "У ссылки нет отпечатка", row["id"])
            if "anchor" in ref:
                require(isinstance(ref["anchor"], str) and ref["anchor"], "invalid_ref", "Пустой якорь", row["id"])

    def _basis(self, row):
        require(row["basis"] in {"source_read", "historical_execution"}, "invalid_basis", "Неизвестное основание", row["id"])
        if row["basis"] == "historical_execution":
            require(row.get("refs"), "missing_evidence", "Нужна ссылка на историческое доказательство", row["id"])
        self._refs(row)

    def _validate(self):
        m = self.manifest
        require(self.sources and len(self.sources) == m["scope"]["source_count"],
                "source_count", "Количество источников не совпадает с манифестом")
        paths = set()
        for src in self.sources.values():
            fields(src, {"path": str, "sha256": str, "card": str, "card_sha256": str, "coverage": dict}, src["id"])
            path = local_path(self.root, src["path"])
            require(path not in paths, "duplicate_source", "Повтор пути источника", src["id"])
            paths.add(path)
            self._hash(src["sha256"], src["id"])
            self._document(src["card"], src["card_sha256"])
        references = m.get("reference_hashes", {})
        require(isinstance(references, dict), "invalid_shape", "reference_hashes должен быть объектом")
        for path, sha in references.items():
            self._document(path, sha)
        local_path(self.root, m["scope"]["registry"])
        self._hash(m["scope"]["registry_sha256"], "registry")
        self._hash(m["snapshot"]["source_hash"], "source_hash")
        strings(m["scope"]["selected_sources"], "selected_sources")
        require(set(m["scope"]["selected_sources"]) <= self.sources.keys(), "unknown_source", "Неизвестный выбранный источник")
        for name, dep in self.dependencies.items():
            fields(dep, {"version": str, "package_sha256": str, "observed_package_path": str, "coverage": str}, name)
            self._hash(dep["package_sha256"], name)
            require(Path(dep["observed_package_path"]).is_absolute(), "invalid_dependency",
                    "observed_package_path должен быть абсолютным", name)
        for ent in self.entities.values():
            fields(ent, {"kind": str, "name": str, "qualified_name": str, "summary": str,
                         "aliases": list, "basis": str, "refs": list}, ent["id"])
            require(ent["kind"] in KINDS, "invalid_kind", "Неизвестный вид сущности", ent["id"])
            require("owner" in ent and "location" in ent, "missing_field", "Нужны owner и location", ent["id"])
            owner = ent["owner"]
            require(owner is None or (isinstance(owner, str) and owner in self.nodes),
                    "invalid_owner", "Неизвестный владелец", ent["id"])
            strings(ent["aliases"], ent["id"])
            if ent["kind"] == "boundary":
                boundary = ent.get("boundary")
                fields(boundary, {"kind": str, "expression": str}, ent["id"])
                require(boundary["kind"] in {"external", "dynamic"} and boundary["expression"],
                        "invalid_boundary", "Неизвестная или пустая граница", ent["id"])
                if boundary["kind"] == "external":
                    require(ent["location"] is None and isinstance(boundary.get("dependency"), str)
                            and boundary["dependency"] in self.dependencies,
                            "invalid_boundary", "У внешней границы нужны dependency и location=null", ent["id"])
                else:
                    require(owner is not None and isinstance(boundary.get("reason"), str) and boundary["reason"],
                            "invalid_boundary", "Нужна причина неразрешимости", ent["id"])
                    self._location(ent["location"], ent["id"])
            else:
                require(owner is not None and "boundary" not in ent, "invalid_owner", "Локальное определение требует владельца", ent["id"])
                self._location(ent["location"], ent["id"])
            self._basis(ent)
        # Ownership must be acyclic; call/process cycles are valid.
        for ent in self.entities.values():
            seen = {ent["id"]}
            owner = ent["owner"]
            while owner in self.entities:
                require(owner not in seen, "owner_cycle", "Цикл владения", ent["id"])
                seen.add(owner)
                owner = self.entities[owner]["owner"]
        for rel in self.relations.values():
            fields(rel, {"kind": str, "from": str, "to": str, "location": dict, "basis": str}, rel["id"])
            require(rel["kind"] in RELATIONS, "invalid_relation", "Неизвестный вид отношения", rel["id"])
            require(rel["from"] in self.nodes and rel["to"] in self.nodes,
                    "unknown_endpoint", "Неизвестный конец отношения", rel["id"])
            for key in ("condition", "context", "payload"):
                if key in rel:
                    require(isinstance(rel[key], str), "invalid_field", f"{key} должен быть строкой", rel["id"])
            self._location(rel["location"], rel["id"])
            self._basis(rel)
        for proc in self.processes.values():
            self._process(proc)
        for src in self.sources.values():
            require(set(src["coverage"]) == {"definitions", "relations", "processes"},
                    "invalid_coverage", "Нужны три аспекта покрытия", src["id"])
            for aspect, cov in src["coverage"].items():
                fields(cov, {"state": str, "included": list, "remaining": list}, src["id"])
                strings(cov["included"], src["id"])
                strings(cov["remaining"], src["id"])
                require(cov["state"] in STATES, "invalid_coverage", "Неизвестный статус покрытия", src["id"])
                if aspect == "definitions":
                    expected = {x["id"] for x in self.entities.values() if x["kind"] != "boundary"
                                and x["location"]["source"] == src["id"]}
                elif aspect == "relations":
                    expected = {x["id"] for x in self.relations.values() if x["location"]["source"] == src["id"]}
                else:
                    expected = {x["id"] for x in self.processes.values()
                                if any(y["location"]["source"] == src["id"] for y in x["steps"])}
                require(set(cov["included"]) == expected, "coverage_mismatch", f"Неверный included: {aspect}", src["id"])
                require(not (cov["state"] == "complete" and cov["remaining"]),
                        "invalid_coverage", "complete содержит остаток", src["id"])
                require(not (cov["state"] == "not_indexed" and cov["included"]),
                        "invalid_coverage", "not_indexed содержит записи", src["id"])
                require(cov["state"] == "complete" or cov["remaining"],
                        "invalid_coverage", "Нужно описание остатка", src["id"])
        states = [cov["state"] for src in self.sources.values() for cov in src["coverage"].values()]
        require(m["scope"]["global_coverage"] == aggregate(states), "coverage_mismatch", "Неверный общий охват")
        strings(m["retired_ids"], "retired_ids")
        for rid in m["retired_ids"]:
            require(identifier(rid) and rid not in self.all, "invalid_retired_id", "Некорректный или активный удалённый ID", rid)
        require(set(m["next_ids"]) == set(NEXT_KEYS.values()), "invalid_next_id", "Неверные счётчики ID")
        for kind, key in NEXT_KEYS.items():
            ids = list(self.records[kind]) + [x for x in m["retired_ids"] if x.startswith(PREFIXES[kind] + "-")]
            n = m["next_ids"][key]
            require(type(n) is int and n > max([int(x.split("-")[1]) for x in ids] or [0]),
                    "invalid_next_id", "Следующий ID уже использован", key)

    def _process(self, proc):
        fields(proc, {"name": str, "entry": dict, "scope": str, "coverage": str, "basis": str,
                      "steps": list, "exits": list, "refs": list}, proc["id"])
        fields(proc["entry"], {"entity": str, "trigger": str}, proc["id"])
        require(proc["entry"]["entity"] in self.entities, "unknown_entry", "Неизвестный вход процесса", proc["id"])
        require(proc["coverage"] in {"partial", "complete"} and proc["scope"] and proc["steps"],
                "invalid_process", "Нужны область, шаги и допустимое покрытие", proc["id"])
        keys = set()
        for row in proc["steps"] + proc["exits"]:
            fields(row, {"id": str, "summary": str}, proc["id"])
            require(re.fullmatch(r"[A-Za-z0-9_-]+", row["id"]) and row["id"] not in keys,
                    "invalid_step_id", "Некорректный или повторный локальный ID", proc["id"])
            keys.add(row["id"])
        steps = {x["id"] for x in proc["steps"]}
        exits = {x["id"] for x in proc["exits"]}
        for step in proc["steps"]:
            label = proc["id"] + "/" + step["id"]
            fields(step, {"entity": str, "location": dict, "relations": list, "next": list}, label)
            require(step["entity"] in self.entities, "unknown_entity", "Неизвестная сущность шага", label)
            self._location(step["location"], label)
            strings(step["relations"], label)
            require(set(step["relations"]) <= self.relations.keys(), "unknown_relation", "Неизвестная связь шага", label)
            require(step["next"], "missing_transition", "Нет перехода или выхода", label)
            for edge in step["next"]:
                fields(edge, {"when": str, "flow": str}, label)
                require(("step" in edge) != ("exit" in edge), "invalid_transition", "Нужна ровно одна цель", label)
                key = "step" if "step" in edge else "exit"
                require(isinstance(edge[key], str) and edge[key] in (steps if key == "step" else exits),
                        "unknown_transition", "Неизвестная цель перехода", label)
                require(edge["when"] and edge["flow"] in {"sync", "await", "scheduled", "unknown"},
                        "invalid_flow", "Неверное условие или порядок исполнения", label)
        for ex in proc["exits"]:
            fields(ex, {"kind": str}, proc["id"])
            require(ex["kind"] in {"return", "error", "scope_boundary", "external_boundary"},
                    "invalid_exit", "Неизвестный вид выхода", proc["id"])
            if "location" in ex:
                self._location(ex["location"], proc["id"])
        self._basis(proc)

    def source_ids(self, record):
        """Sources providing this record, including local ends and process steps."""
        if record["id"] in self.sources:
            return {record["id"]}
        ids = set()
        if record.get("location"):
            ids.add(record["location"]["source"])
        for key in ("from", "to"):
            node = self.nodes.get(record.get(key))
            if node:
                if node["id"] in self.sources:
                    ids.add(node["id"])
                elif node.get("location"):
                    ids.add(node["location"]["source"])
        if record["id"] in self.processes:
            ids.update(self.source_ids(self.entities[record["entry"]["entity"]]))
            for step in record["steps"]:
                ids.add(step["location"]["source"])
                ids.update(self.source_ids(self.entities[step["entity"]]))
                for rid in step["relations"]:
                    ids.update(self.source_ids(self.relations[rid]))
        return ids

    def references(self, record):
        refs = [{"path": self.sources[sid]["card"], "relation": "details"}
                for sid in sorted(self.source_ids(record))]
        refs += record.get("refs", [])
        # Relation endpoints can carry their own evidence, e.g. an external boundary.
        for key in ("from", "to"):
            refs += self.nodes.get(record.get(key), {}).get("refs", [])
        if record["id"] in self.processes:
            for rid in {r for step in record["steps"] for r in step["relations"]}:
                refs += self.relations[rid].get("refs", [])
        by_key = {(ref["path"], ref.get("anchor", ""), ref["relation"]): ref for ref in refs}
        return [dict(by_key[key], sha256=self.doc_hashes[key[0]]) for key in sorted(by_key)]

    def verify(self, records=(), all_docs=False):
        """Read current bytes, retain historical addresses, never rewrite the index."""
        differences, dependencies, cached = [], {}, {}
        checked = Counter()

        def inspect(value, sha, kind, absolute=False):
            path = Path(value) if absolute else local_path(self.root, value)
            if path in cached:
                return cached[path]
            checked[kind] += 1
            try:
                data = path.read_bytes()
                actual = hashlib.sha256(data).hexdigest()
                state = "current" if actual == sha else "stale"
            except (OSError, ValueError) as exc:
                data, actual, state = None, None, "missing"
            result = {"path": value, "state": state, "expected": sha, "actual": actual}
            cached[path] = (result, data)
            if state != "current" and not absolute:
                differences.append(result)
            return result, data

        source_bytes = {}
        total_hash = hashlib.sha256()
        all_current = True
        for src in sorted(self.sources.values(), key=lambda x: x["path"]):
            result, data = inspect(src["path"], src["sha256"], "sources")
            all_current &= result["state"] == "current"
            if result["state"] == "current":
                source_bytes[src["id"]] = data
            if data is not None:
                total_hash.update(src["path"].encode() + b"\0" + data)
        if all_current:
            require(total_hash.hexdigest() == self.manifest["snapshot"]["source_hash"],
                    "source_hash_mismatch", "Совокупный хеш не соответствует записям источников")
        scope = self.manifest["scope"]
        result, data = inspect(scope["registry"], scope["registry_sha256"], "registry")
        if result["state"] == "current":
            text = data.decode("utf-8")
            paths = re.findall(r"^\| \[[^\]]+\]\(\.\./\.\./\.\./([^)\n]+)\) \|", text, re.M)
            require(len(paths) == len(set(paths)) and set(paths) == {s["path"] for s in self.sources.values()},
                    "registry_mismatch", "Каталог не соответствует зафиксированному реестру")
        # Validate line hints only on their actual indexed version.
        for row in self.all.values():
            locations = [row["location"]] if row.get("location") else []
            if row["id"] in self.processes:
                locations += [x["location"] for x in row["steps"] + row["exits"] if x.get("location")]
            for loc in locations:
                if loc["source"] in source_bytes:
                    require(loc["line_end"] <= len(source_bytes[loc["source"]].splitlines()),
                            "invalid_location", "Строка за пределами проверенного источника", row["id"])
        wanted = {}
        for row in records:
            for ref in self.references(row):
                wanted[(ref["path"], ref.get("anchor", ""))] = ref
        if all_docs:
            for path, sha in self.doc_hashes.items():
                wanted.setdefault((path, ""), {"path": path, "sha256": sha})
            for row in self.all.values():
                for ref in row.get("refs", []):
                    wanted[(ref["path"], ref.get("anchor", ""))] = dict(ref, sha256=self.doc_hashes[ref["path"]])
        anchor_cache = {}
        for (path, anchor), ref in sorted(wanted.items()):
            result, data = inspect(path, ref["sha256"], "documents")
            if result["state"] == "current" and anchor:
                if path not in anchor_cache:
                    anchor_cache[path] = anchors(data.decode("utf-8"))
                require(anchor in anchor_cache[path], "unknown_anchor", "Нет якоря в проверенной версии документа", path + "#" + anchor)
        for name, dep in self.dependencies.items():
            result, data = inspect(dep["observed_package_path"], dep["package_sha256"], "dependencies", absolute=True)
            dependencies[name] = {**result, "version": dep["version"], "coverage": dep["coverage"]}
            if result["state"] == "current":
                package = parse_json(data.decode("utf-8"), dep["observed_package_path"])
                require(isinstance(package, dict) and package.get("version") == dep["version"],
                        "dependency_version", "Версия package не соответствует объявленной", name)
        state = "missing" if any(d["state"] == "missing" for d in differences) else ("stale" if differences else "current")
        return {"state": state, "checked": dict(checked), "differences": differences, "dependencies": dependencies}

    def node_summary(self, row):
        if row["id"] in self.sources:
            return {key: row[key] for key in ("id", "path", "sha256", "card")} | {
                "kind": "source",
                "coverage": {a: {"state": c["state"], "included_count": len(c["included"]),
                                  "remaining": c["remaining"]} for a, c in row["coverage"].items()}}
        return deepcopy(row)

    def get(self, rid, collection):
        if rid in self.manifest["retired_ids"]:
            raise IndexErrorDetail("retired_id", "ID выведен из использования", rid, 2)
        if rid not in collection:
            raise IndexErrorDetail("unknown_id", "ID отсутствует или не подходит для команды", rid, 2)
        return collection[rid]

    def query(self, args):
        op = args.operation
        scopes = set(args.scope or [])
        for sid in scopes:
            self.get(sid, self.sources)
        explicit = bool(scopes)
        aspect = "relations" if op in {"neighbors", "field"} else (
            "processes" if op in {"processes", "process"} else "definitions")
        items, referenced = [], []
        process_info = None
        traversal = None
        subject = None
        if op != "find":
            collection = self.all if op == "details" else self.processes if op == "process" else self.nodes
            subject = self.get(args.id, collection)
            referenced.append(subject)
        if op == "find":
            term = args.term
            normalized = unicodedata.normalize("NFC", term).casefold()
            for row in sorted(self.nodes.values(), key=lambda x: x["id"]):
                kind = "source" if row["id"] in self.sources else row["kind"]
                if args.kind and args.kind != kind:
                    continue
                if scopes and not self.source_ids(row) & scopes:
                    continue
                exact_fields = [row.get(key, "") for key in ("id", "path", "name", "qualified_name")]
                aliases = [unicodedata.normalize("NFC", a).casefold() for a in row.get("aliases", [])]
                match = (term in exact_fields or normalized in aliases) if args.match == "exact" else (
                    any(term in x for x in exact_fields) or any(normalized in a for a in aliases))
                if match:
                    items.append(self.node_summary(row))
        elif op == "show":
            if not scopes or self.source_ids(subject) & scopes:
                items = [self.node_summary(subject)]
            if not explicit:
                scopes = self.source_ids(subject)
        elif op in {"neighbors", "field"}:
            if op == "field":
                require_kind = subject.get("kind") in {"field", "getter"} or subject.get("boundary", {}).get("kind") == "dynamic"
                if not require_kind:
                    raise IndexErrorDetail("invalid_target", "Нужно поле, getter или динамическое поле", args.id, 2)
                direction, depth = "in", 1
                kinds = {"reads", "writes", "computes"} if args.access == "all" else {args.access}
            else:
                direction, depth, kinds = args.direction, args.depth, set(args.relation or [])
            adjacency = self.incoming if direction == "in" else self.outgoing
            other = "from" if direction == "in" else "to"
            queue = deque([(args.id, [])])
            seen_nodes, seen_edges = {args.id}, set()
            frontier = set()
            while queue:
                node, chain = queue.popleft()
                eligible = [r for r in adjacency[node] if (not kinds or r["kind"] in kinds)
                            and (not scopes or r["location"]["source"] in scopes)]
                if len(chain) >= depth:
                    if any(r["id"] not in seen_edges for r in eligible):
                        frontier.add(node)
                    continue
                for rel in eligible:
                    if rel["id"] not in seen_edges:
                        seen_edges.add(rel["id"])
                        items.append(deepcopy(rel) | {"path": chain + [rel["id"]]})
                    target = rel[other]
                    if target not in seen_nodes:
                        seen_nodes.add(target)
                        queue.append((target, chain + [rel["id"]]))
            items.sort(key=lambda x: x["id"])
            traversal = {"direction": direction, "depth": depth, "depth_limited": bool(frontier), "frontier_count": len(frontier)}
        elif op == "processes":
            if args.id in self.sources and not explicit:
                scopes = {args.id}
            for proc in sorted(self.processes.values(), key=lambda x: x["id"]):
                steps = [x for x in proc["steps"] if (
                    x["entity"] == args.id if args.id in self.entities else x["location"]["source"] == args.id)]
                entry_node = self.entities[proc["entry"]["entity"]]
                entry_matches = (entry_node["id"] == args.id if args.id in self.entities else args.id in self.source_ids(entry_node))
                if scopes:
                    steps = [x for x in steps if x["location"]["source"] in scopes]
                    entry_matches = entry_matches and bool(self.source_ids(entry_node) & scopes)
                if steps or entry_matches:
                    items.append({"id": proc["id"], "name": proc["name"], "coverage": proc["coverage"],
                                  "step_ids": [proc["id"] + "/" + x["id"] for x in steps], "entry_matches": entry_matches})
        elif op == "process":
            process_info = {key: deepcopy(subject[key]) for key in ("id", "name", "entry", "scope", "coverage", "exits", "refs")}
            items = [deepcopy(x) | {"address": subject["id"] + "/" + x["id"]} for x in subject["steps"]
                     if not scopes or x["location"]["source"] in scopes]
            if not explicit:
                scopes = self.source_ids(subject)
        elif op == "details":
            items = self.references(subject) if not scopes or self.source_ids(subject) & scopes else []
            items.sort(key=lambda x: (x["path"], x.get("anchor", ""), x["relation"]))
            if not explicit:
                scopes = self.source_ids(subject)
        total = len(items)
        page = items[args.offset:args.offset + args.limit]
        if process_info:
            visible = {step["id"] for step in page}
            for step in page:
                for edge in step["next"]:
                    if "step" in edge:
                        edge["outside_page"] = edge["step"] not in visible
        for item in page:
            if item.get("id") in self.all:
                referenced.append(self.all[item["id"]])
            for rid in item.get("path", []) if isinstance(item.get("path"), list) else []:
                referenced.append(self.relations[rid])
        if process_info:
            referenced.append(subject)
        scope_ids = scopes or set(self.sources)
        counts = Counter(self.sources[sid]["coverage"][aspect]["state"] for sid in scope_ids)
        state = aggregate(counts)
        coverage = {"state": state, "aspect": aspect, "scope": sorted(scopes),
                    "scope_kind": "sources" if scopes else "catalog", "source_count": len(scope_ids),
                    "states": dict(sorted(counts.items()))}
        freshness = {"state": "unchecked"} if args.no_verify else self.verify(referenced)
        gaps = set()
        participants = {}
        for row in referenced:
            participants[row["id"]] = row
            for key in ("from", "to"):
                if row.get(key) in self.nodes:
                    participants[row[key]] = self.nodes[row[key]]
        for row in participants.values():
            boundary = row.get("boundary", {}).get("kind")
            if boundary:
                gaps.add("unresolved_target" if boundary == "dynamic" else "external_boundary")
        if any(dep["state"] != "current" for dep in freshness.get("dependencies", {}).values()):
            gaps.add("external_dependency_unverified")
        # An exhausted page is different from an empty search.
        empty = ("not_indexed" if state == "not_indexed" else "none_in_scope") if total == 0 else None
        result = {
            "query": {k: v for k, v in vars(args).items() if k not in {"dataset", "format"}},
            "dataset": {"id": self.manifest["dataset_id"], "snapshot": self.manifest["snapshot"],
                        "registry": self.manifest["scope"]["registry"]},
            "items": page, "coverage": coverage, "freshness": freshness,
            "sources": [self.node_summary(self.sources[sid]) for sid in sorted(
                {sid for row in referenced for sid in self.source_ids(row)})],
            "gaps": sorted(gaps), "empty_reason": empty,
            "page": {"total": total, "limit": args.limit, "offset": args.offset,
                     "truncated": args.offset + len(page) < total,
                     "next_offset": args.offset + len(page) if args.offset + len(page) < total else None}
        }
        if process_info:
            result["process"] = process_info
        if traversal:
            result["traversal"] = traversal
        return result


def positive(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("Ожидается положительное целое")
    return number


def nonnegative(value):
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("Ожидается неотрицательное целое")
    return number


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--dataset", type=Path, default=DEFAULT_MANIFEST, help="Манифест набора")
    sub = cli.add_subparsers(dest="operation", required=True)
    for op in ("find", "show", "neighbors", "field", "processes", "process", "details", "check"):
        command = sub.add_parser(op)
        command.add_argument("--format", choices=("text", "json"), default="text")
        if op == "check":
            command.add_argument("--freshness", action="store_true")
            continue
        command.add_argument("--scope", action="append", metavar="SRC_ID")
        command.add_argument("--no-verify", action="store_true")
        command.add_argument("--limit", type=positive, default=20)
        command.add_argument("--offset", type=nonnegative, default=0)
        command.add_argument("term" if op == "find" else "id")
        if op == "find":
            command.add_argument("--match", choices=("exact", "contains"), default="contains")
            command.add_argument("--kind", choices=sorted(KINDS | {"source"}))
        elif op == "neighbors":
            command.add_argument("--direction", choices=("in", "out"), required=True)
            command.add_argument("--relation", action="append", choices=sorted(RELATIONS))
            command.add_argument("--depth", type=positive, default=1)
        elif op == "field":
            command.add_argument("--access", choices=("reads", "writes", "computes", "all"), default="all")
    return cli


def text_result(result):
    if "valid" in result:
        yield "Проверка: " + ("успешно" if result["valid"] else "обнаружены расхождения")
        yield json.dumps(result, ensure_ascii=False)
        return
    yield (f"Охват: {result['coverage']['state']}; источников: {result['coverage']['source_count']}; "
           f"актуальность: {result['freshness']['state']}")
    source_map = {s["id"]: s for s in result["sources"]}
    if "process" in result:
        proc = result["process"]
        yield f"{proc['id']} {proc['name']} [{proc['coverage']}] — {proc['scope']}"
    for item in result["items"]:
        rid = item.get("address", item.get("id", item.get("path", "")))
        if "from" in item:
            yield f"{rid} {item['kind']}: {item['from']} -> {item['to']}; путь: {' / '.join(item['path'])}"
        else:
            name = item.get("qualified_name", item.get("name", item.get("summary", item.get("path", ""))))
            yield f"{rid} {name}" + (f"; владелец: {item['owner']}" if "owner" in item else "")
        loc = item.get("location")
        if loc:
            path = source_map.get(loc["source"], {}).get("path", loc["source"])
            yield f"  {path}:{loc['line_start']} {loc['symbol']}"
        if item.get("summary") and item.get("summary") != item.get("name"):
            yield "  " + item["summary"]
        for key in ("condition", "payload"):
            if item.get(key):
                yield f"  {key}: {item[key]}"
        if item.get("step_ids"):
            yield "  шаги: " + ", ".join(item["step_ids"])
        for edge in item.get("next", []):
            yield f"  -> {edge.get('step', edge.get('exit'))}: {edge['when']} [{edge['flow']}]" + (
                " [outside_page]" if edge.get("outside_page") else "")
        if item.get("anchor"):
            yield "  #" + item["anchor"]
    if result["empty_reason"]:
        yield "Нет результатов: " + result["empty_reason"]
    if "process" in result:
        for ex in result["process"]["exits"]:
            yield f"Выход {ex['id']} [{ex['kind']}]: {ex['summary']}"
    if result["gaps"]:
        yield "Границы: " + ", ".join(result["gaps"])
    for source in result["sources"]:
        yield f"Источник {source['id']}: {source['path']}; карточка: {source['card']}"
    if result.get("traversal"):
        yield "Обход: " + json.dumps(result["traversal"], ensure_ascii=False)
    page = result["page"]
    yield f"Показано {len(result['items'])} из {page['total']}; offset={page['offset']}"
    if page["truncated"]:
        yield f"Продолжение: --offset {page['next_offset']} --limit {page['limit']}"
    for diff in result["freshness"].get("differences", []):
        yield f"{diff['state']}: {diff['path']}"
    for name, dep in result["freshness"].get("dependencies", {}).items():
        if dep["state"] != "current":
            yield f"Внешняя зависимость {name}: {dep['state']}"


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        data = Dataset(args.dataset)
        if args.operation == "check":
            freshness = data.verify(all_docs=True) if args.freshness else {"state": "unchecked"}
            valid = freshness["state"] in {"current", "unchecked"} and all(
                x["state"] == "current" for x in freshness.get("dependencies", {}).values())
            result = {"valid": valid, "counts": {k: len(v) for k, v in data.records.items()}, "freshness": freshness}
            status = 0 if valid else 1
        else:
            result = data.query(args)
            status = 0
        print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json" else "\n".join(text_result(result)))
        return status
    except IndexErrorDetail as exc:
        print(json.dumps({"error": exc.detail}, ensure_ascii=False), file=sys.stderr)
        return exc.status


if __name__ == "__main__":
    sys.exit(main())
