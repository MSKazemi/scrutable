# ADR-0005: Deterministic conformance validator in required CI

**Status:** Accepted  
**Date:** 2026-08-13  
**Owner:** Repository maintainer  
**Review trigger:** A check produces a false failure that blocks legitimate work, the
validator becomes a bottleneck for contributors, or semantic (A2) validation is
implemented and supersedes part of this scope

## Context

[`docs/13-quality-assurance-audit-and-roadmap.md`](../docs/13-quality-assurance-audit-and-roadmap.md)
identified the controlling bottleneck as the **specification-to-evidence gap**: the
repository could describe what a quality process should do, but could not continuously
demonstrate that its own structural claims held. It named a small deterministic
conformance validator as the first investment, ahead of any further question content,
and warned that adding questions first "increases maintenance cost and the appearance of
completeness without proportionally increasing assurance."

That warning was not followed. Between `c0cd702` and `a80c9653` the catalog grew from 99
to 199 questions in a single day, while the validator, CI, release tags, published packs,
and field trials all remained at zero. Each added question was well-formed, which is
precisely why the drift was invisible in the artifact and visible only in its trajectory.

Meanwhile the assurance ladder in `docs/13` defines level **A1 — Structurally valid** as
requiring a "Required CI report for the pinned commit." Without CI, A1 was unreachable by
the project's own definition, and every structural claim in `CHANGELOG.md` rested on
manual observation that decayed on the next commit.

## Decision

1. **Add `tools/validate.py`**, a dependency-light, offline, deterministic validator.
2. **Run it in CI** on every push to `main`, every pull request, and on demand
   (`.github/workflows/validate.yml`), publishing a machine-readable report artifact.
3. **Scope it to structure only.** It checks eleven things: catalog parsing and stable-ID
   uniqueness; JSON Schemas being well-formed; question objects validating against
   `question.schema.json`; every declared relationship target resolving; the `depends_on`
   graph being acyclic; status hygiene; the prose-to-catalog coverage manifest still
   matching the prose it cites; the worked example validating; relative Markdown links
   and anchors resolving; gate-vocabulary consistency across contract files; and a
   criticality-calibration report.
4. **Failures block; the calibration report only warns.** `--strict` promotes warnings to
   failures for use in a release gate.
5. **The validator never owns canonical state.** It reads the files and reports. It does
   not rewrite, generate, or normalize them, consistent with
   [ADR-0003](ADR-0003-text-first-agent-native-architecture.md) and
   `ai-context.yaml: validator_must_not_own_canonical_state`.
6. **Freeze the catalog at 199 questions** until CI is green on `main`. New question
   content resumes only after the evidence mechanism exists.

## Rationale

The checks were not speculative: all eleven were first executed by hand during the
self-assessment run, and each one had already been claimed as true somewhere in the
repository. Promoting them from prose assertions to executable checks converts roughly
sixty lines of throwaway analysis into permanent, reproducible evidence.

Structure-only scope is a deliberate limit. Whether an answer is true, whether evidence
is sufficient, and whether a gate result is correct are A2–A5 concerns that a script
cannot judge, and pretending otherwise would recreate the exact overclaiming the
framework exists to prevent.

The coverage-manifest check is designed so it cannot rot: rather than comparing a stored
`source_revision` SHA against HEAD — which would go stale on every commit — it re-derives
every one of the 396 entries from the prose files at the working revision. Drift fails CI
instead of hiding behind a stale provenance field.

## Verification

The validator was verified red-green before adoption. With four defects deliberately
injected — an unresolved `activates` target, an out-of-enum `criticality` value, a
broken Markdown link plus a broken anchor, and a coverage entry whose `source_text` no
longer appears in the prose — it reported six failures and exited non-zero. With the
defects reverted it reported zero failures across 199 questions, 1,009 edges, 396
coverage entries, and 252 Markdown links.

## Consequences

- The repository can make an **A1 claim for any revision with a green CI run**, and must
  still not claim A2 (no semantic validation), A3 (no independent review or calibration),
  A4 (no published packs), or A5 (no outcome loops).
- Contributors need `PyYAML` and `jsonschema` to validate locally. Reading and using the
  framework still requires no installation, preserving ADR-0003.
- Every future catalog change must keep 1,009+ edges resolvable and the coverage manifest
  true, or CI fails. This raises the cost of adding questions — which is the intended
  effect, given the trajectory described above.
- `docs/13` remains a pinned point-in-time audit at baseline `b2c5bd2` and is **not**
  amended by this ADR. Its roadmap item is satisfied; its snapshot stays historical.
