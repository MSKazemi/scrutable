#!/usr/bin/env python3
"""Deterministic conformance validator for Product Questionbook.

This is the P0 capability named in `docs/13-quality-assurance-audit-and-roadmap.md`:
it turns the structural claims in `CHANGELOG.md` and the audit documents from
manually observed assertions into a check that CI reproduces at a pinned commit.

It validates structure only. It cannot judge whether an answer is true, whether
evidence is sufficient, or whether a gate result is correct -- those are the A2+
levels on the assurance ladder and remain out of scope. Passing this validator
supports an A1 claim for the checked revision and nothing beyond it.

Usage:
    python3 tools/validate.py              # human-readable report
    python3 tools/validate.py --json       # machine-readable report
    python3 tools/validate.py --strict     # treat warnings as failures

Exit codes: 0 = all required checks pass, 1 = at least one failure.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install -r tools/requirements.txt")

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    sys.exit("jsonschema is required: pip install -r tools/requirements.txt")

ROOT = pathlib.Path(__file__).resolve().parent.parent

RELATIONSHIP_FIELDS = (
    "depends_on",
    "activates",
    "related_to",
    "refines",
    "deprecated_by",
)

# Container key -> schema file, for the worked example records.
EXAMPLE_RECORDS = (
    ("examples/sample-application/project-profile.yaml", None, "schemas/project-profile.schema.json"),
    ("examples/sample-application/answers.yaml", "answers", "schemas/answer.schema.json"),
    ("examples/sample-application/question-instances.yaml", "instances", "schemas/question-instance.schema.json"),
)


class Report:
    """Collects check results. A failure fails the build; a warning does not."""

    def __init__(self) -> None:
        self.checks: list[dict] = []

    def add(self, check_id: str, name: str, failures: list[str],
            warnings: list[str] | None = None, detail: dict | None = None) -> None:
        self.checks.append({
            "id": check_id,
            "name": name,
            "status": "fail" if failures else "pass",
            "failures": failures,
            "warnings": warnings or [],
            "detail": detail or {},
        })

    @property
    def failures(self) -> list[str]:
        return [f"[{c['id']}] {f}" for c in self.checks for f in c["failures"]]

    @property
    def warnings(self) -> list[str]:
        return [f"[{c['id']}] {w}" for c in self.checks for w in c["warnings"]]


def load_yaml(path: pathlib.Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def catalog_files() -> list[pathlib.Path]:
    return sorted((ROOT / "catalog").rglob("*.yaml"))


def load_catalog() -> tuple[dict[str, dict], list[str]]:
    """Return (questions by id, failures). Duplicate ids are reported, not merged."""
    questions: dict[str, dict] = {}
    failures: list[str] = []
    for path in catalog_files():
        rel = path.relative_to(ROOT)
        try:
            data = load_yaml(path)
        except yaml.YAMLError as exc:
            failures.append(f"{rel}: YAML parse error: {exc}")
            continue
        if not isinstance(data, dict) or "questions" not in data:
            failures.append(f"{rel}: missing top-level 'questions' key")
            continue
        for question in data["questions"] or []:
            qid = question.get("id")
            if not qid:
                failures.append(f"{rel}: a question object has no 'id'")
                continue
            if qid in questions:
                failures.append(f"{rel}: duplicate stable id '{qid}'")
                continue
            question["__source__"] = str(rel)
            questions[qid] = question
    return questions, failures


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def check_schemas_wellformed(report: Report) -> None:
    """Every JSON Schema in schemas/ must itself be a valid Draft 2020-12 schema."""
    failures = []
    paths = sorted((ROOT / "schemas").glob("*.json"))
    for path in paths:
        rel = path.relative_to(ROOT)
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"{rel}: invalid JSON: {exc}")
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:  # noqa: BLE001 - surface any schema defect
            failures.append(f"{rel}: not a valid Draft 2020-12 schema: {exc}")
    report.add("S1", "JSON Schemas are well-formed", failures,
               detail={"schemas_checked": len(paths)})


def check_catalog_schema(report: Report, questions: dict[str, dict]) -> None:
    """Every published question object validates against question.schema.json."""
    schema = json.loads((ROOT / "schemas" / "question.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    failures = []
    for qid, question in sorted(questions.items()):
        payload = {k: v for k, v in question.items() if not k.startswith("__")}
        for error in validator.iter_errors(payload):
            location = "/".join(str(p) for p in error.path) or "(root)"
            failures.append(f"{question['__source__']}: {qid}: {location}: {error.message}")
    report.add("C1", "Catalog questions validate against question.schema.json",
               failures, detail={"questions": len(questions)})


def check_relationships_resolve(report: Report, questions: dict[str, dict]) -> None:
    """Every declared relationship target resolves to a published stable id."""
    failures = []
    counts: Counter[str] = Counter()
    for qid, question in sorted(questions.items()):
        for field in RELATIONSHIP_FIELDS:
            for target in question.get(field) or []:
                counts[field] += 1
                if target not in questions:
                    failures.append(
                        f"{question['__source__']}: {qid}.{field} -> unresolved id '{target}'")
    report.add("C2", "Declared relationship targets resolve", failures,
               detail={"edges_by_type": dict(counts), "edges_total": sum(counts.values())})


def check_dependency_acyclic(report: Report, questions: dict[str, dict]) -> None:
    """`depends_on` must form a DAG; a cycle makes the ready-frontier undefined."""
    graph = {qid: [t for t in (q.get("depends_on") or []) if t in questions]
             for qid, q in questions.items()}
    WHITE, GREY, BLACK = 0, 1, 2
    color = dict.fromkeys(graph, WHITE)
    cycles: list[list[str]] = []

    def visit(node: str, stack: list[str]) -> None:
        color[node] = GREY
        stack.append(node)
        for neighbour in graph.get(node, []):
            if color.get(neighbour) == GREY:
                cycles.append(stack[stack.index(neighbour):] + [neighbour])
            elif color.get(neighbour) == WHITE:
                visit(neighbour, stack)
        stack.pop()
        color[node] = BLACK

    sys.setrecursionlimit(10000)
    for node in graph:
        if color[node] == WHITE:
            visit(node, [])

    failures = [f"dependency cycle: {' -> '.join(cycle)}" for cycle in cycles]
    report.add("C3", "depends_on graph is acyclic", failures,
               detail={"nodes": len(graph)})


def check_status_values(report: Report, questions: dict[str, dict]) -> None:
    """Deprecated questions must name a successor; drafts must not ship silently."""
    failures, warnings = [], []
    status_counts = Counter(q.get("status") for q in questions.values())
    for qid, question in sorted(questions.items()):
        if question.get("status") == "deprecated" and not question.get("deprecated_by"):
            failures.append(f"{qid}: status 'deprecated' without 'deprecated_by'")
        if question.get("status") == "draft":
            warnings.append(f"{qid}: status 'draft' present in the published catalog")
    report.add("C4", "Question status hygiene", failures, warnings,
               detail={"status_counts": dict(status_counts)})


def check_coverage_manifest(report: Report, questions: dict[str, dict]) -> None:
    """The prose->catalog manifest must stay true to the prose it claims to cover.

    This is the drift check. `source_revision` records when the manifest was last
    reconciled; correctness is enforced by re-deriving every entry from the prose
    files at the current revision, so the check cannot silently rot.
    """
    path = ROOT / "coverage" / "prose-to-catalog.yaml"
    failures: list[str] = []
    warnings: list[str] = []
    detail: dict = {}

    manifest = load_yaml(path)
    schema_path = ROOT / "schemas" / "prose-coverage.schema.json"
    if schema_path.exists():
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        for error in Draft202012Validator(schema).iter_errors(manifest):
            location = "/".join(str(p) for p in error.path) or "(root)"
            failures.append(f"coverage/prose-to-catalog.yaml: {location}: {error.message}")

    bodies: dict[str, str] = {}
    seen_ids: Counter[str] = Counter()
    entry_count = 0
    referenced: set[str] = set()

    for group in manifest.get("groups") or []:
        source_path = group.get("source_path", "")
        prose = ROOT / source_path
        if source_path not in bodies:
            if not prose.exists():
                failures.append(f"coverage manifest references missing file '{source_path}'")
                bodies[source_path] = ""
            else:
                bodies[source_path] = re.sub(r"\s+", " ", prose.read_text(encoding="utf-8"))
        body = bodies[source_path]

        for cid in group.get("catalog_ids") or []:
            referenced.add(cid)
            if cid not in questions:
                failures.append(
                    f"coverage manifest group '{group.get('section')}' -> unknown catalog id '{cid}'")

        for entry in group.get("questions") or []:
            entry_count += 1
            sid = entry.get("source_id", "")
            seen_ids[sid] += 1
            text = re.sub(r"\s+", " ", entry.get("source_text", "")).strip()
            if body and text and text not in body:
                failures.append(
                    f"coverage manifest entry '{sid}' no longer matches prose in {source_path} "
                    f"(prose changed, or the entry was mistyped)")

    for sid, count in seen_ids.items():
        if count > 1:
            failures.append(f"coverage manifest duplicate source_id '{sid}' ({count}x)")

    summary = manifest.get("summary") or {}
    declared_total = summary.get("total_numbered_questions")
    if declared_total is not None and declared_total != entry_count:
        failures.append(
            f"coverage manifest summary.total_numbered_questions={declared_total} "
            f"but {entry_count} entries are present")

    detail = {
        "entries": entry_count,
        "catalog_ids_referenced": len(referenced),
        "catalog_ids_total": len(questions),
        "catalog_without_prose_ancestor": len(set(questions) - referenced),
        "source_revision": manifest.get("source_revision"),
    }
    report.add("V1", "Prose-to-catalog coverage manifest is true to the prose",
               failures, warnings, detail)


def check_examples(report: Report) -> None:
    """The worked example must validate, or it teaches the wrong shape."""
    failures = []
    counted = 0
    for doc_rel, container, schema_rel in EXAMPLE_RECORDS:
        doc_path, schema_path = ROOT / doc_rel, ROOT / schema_rel
        if not doc_path.exists() or not schema_path.exists():
            failures.append(f"{doc_rel} or {schema_rel} is missing")
            continue
        data = load_yaml(doc_path)
        items = data.get(container) if container else [data]
        if items is None:
            failures.append(f"{doc_rel}: expected container key '{container}'")
            continue
        validator = Draft202012Validator(json.loads(schema_path.read_text(encoding="utf-8")))
        for item in items:
            counted += 1
            for error in validator.iter_errors(item):
                location = "/".join(str(p) for p in error.path) or "(root)"
                failures.append(f"{doc_rel}: {item.get('id', '?')}: {location}: {error.message}")
    report.add("E1", "Worked example records validate against their schemas",
               failures, detail={"records": counted})


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.MULTILINE)


def slugify(heading: str) -> str:
    text = re.sub(r"`|\*|_", "", heading).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text)


def check_markdown_links(report: Report) -> None:
    """Every relative Markdown link resolves, including its anchor.

    Gate 1 in docs/13 requires that 'every Markdown link ... validates in CI'.
    External http(s) links are not fetched: CI must stay deterministic and offline.
    """
    failures = []
    anchors: dict[pathlib.Path, set[str]] = {}
    md_files = [p for p in ROOT.rglob("*.md")
                if ".git" not in p.parts and ".questionbook" not in p.parts
                and ".claude" not in p.parts]

    def anchors_for(path: pathlib.Path) -> set[str]:
        if path not in anchors:
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                anchors[path] = set()
            else:
                found = Counter()
                result = set()
                for heading in HEADING_RE.findall(text):
                    slug = slugify(heading)
                    found[slug] += 1
                    result.add(slug if found[slug] == 1 else f"{slug}-{found[slug] - 1}")
                anchors[path] = result
        return anchors[path]

    checked = 0
    for md in sorted(md_files):
        rel = md.relative_to(ROOT)
        for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            file_part, _, anchor = target.partition("#")
            if not file_part:
                if anchor and anchor not in anchors_for(md):
                    failures.append(f"{rel}: anchor '#{anchor}' not found in this file")
                continue
            resolved = (md.parent / file_part).resolve()
            if not resolved.exists():
                failures.append(f"{rel}: link target '{target}' does not exist")
                continue
            if anchor and resolved.suffix == ".md":
                if anchor not in anchors_for(resolved):
                    failures.append(f"{rel}: anchor '{target}' not found in the target file")
    report.add("L1", "Relative Markdown links and anchors resolve", failures,
               detail={"files": len(md_files), "links_checked": checked})


def check_calibration(report: Report, questions: dict[str, dict]) -> None:
    """Informational: report criticality spread so skew stays visible.

    `criticality` is advisory (see docs/prioritization.md). This never fails the
    build -- it exists so that a field which cannot rank a frontier cannot quietly
    be mistaken for one that can.
    """
    counts = Counter(q.get("criticality") for q in questions.values())
    total = sum(counts.values()) or 1
    top = counts.get("critical", 0) + counts.get("high", 0)
    share = top / total
    warnings = []
    if share > 0.90:
        warnings.append(
            f"{top}/{total} ({share:.0%}) of questions are 'critical' or 'high'; "
            "criticality is advisory only and cannot rank the ready frontier "
            "(see docs/prioritization.md)")
    report.add("Q1", "Criticality calibration report", [], warnings,
               detail={"criticality_counts": dict(counts), "top_two_share": round(share, 4)})


def check_run_contract(report: Report) -> None:
    """The declared gate vocabulary must stay identical across the contract files."""
    failures = []
    expected = {"proceed", "proceed_with_conditions", "pause", "stop"}
    ai_context = load_yaml(ROOT / "ai-context.yaml")
    declared = set((ai_context.get("run_contract") or {}).get("allowed_gate_results") or [])
    if declared != expected:
        failures.append(
            f"ai-context.yaml allowed_gate_results {sorted(declared)} != {sorted(expected)}")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for token in sorted(expected):
        if token not in agents:
            failures.append(f"AGENTS.md does not mention gate value '{token}'")
    report.add("R1", "Run contract and gate vocabulary are consistent", failures,
               detail={"allowed_gate_results": sorted(expected)})


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

def run_all() -> Report:
    report = Report()
    questions, load_failures = load_catalog()
    report.add("C0", "Catalog files parse and stable ids are unique", load_failures,
               detail={"files": len(catalog_files()), "questions": len(questions)})

    check_schemas_wellformed(report)
    check_catalog_schema(report, questions)
    check_relationships_resolve(report, questions)
    check_dependency_acyclic(report, questions)
    check_status_values(report, questions)
    check_coverage_manifest(report, questions)
    check_examples(report)
    check_markdown_links(report)
    check_run_contract(report)
    check_calibration(report, questions)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--json", action="store_true", help="emit a machine-readable report")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = parser.parse_args()

    report = run_all()
    failed = bool(report.failures) or (args.strict and bool(report.warnings))

    if args.json:
        print(json.dumps({
            "result": "fail" if failed else "pass",
            "assurance_level_supported": "A0" if failed else "A1",
            "checks": report.checks,
            "failure_count": len(report.failures),
            "warning_count": len(report.warnings),
        }, indent=2))
        return 1 if failed else 0

    print("Product Questionbook conformance validator\n")
    for check in report.checks:
        mark = "FAIL" if check["status"] == "fail" else "ok  "
        detail = ", ".join(f"{k}={v}" for k, v in check["detail"].items())
        print(f"  {mark} {check['id']:<3} {check['name']}")
        if detail:
            print(f"          {detail}")
        for failure in check["failures"]:
            print(f"          FAIL: {failure}")
        for warning in check["warnings"]:
            print(f"          warn: {warning}")

    print()
    if failed:
        print(f"FAILED: {len(report.failures)} failure(s), {len(report.warnings)} warning(s).")
        print("This revision does not support an A1 structural claim.")
    else:
        print(f"PASSED: 0 failures, {len(report.warnings)} warning(s).")
        print("Structural checks pass for this revision (assurance level A1).")
        print("A1 covers structure only -- not answer truth, evidence sufficiency, or gate correctness.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
