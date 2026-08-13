# ADR-0006: `criticality` is an advisory label, not the ranking input

**Status:** Accepted  
**Date:** 2026-08-13  
**Owner:** Repository maintainer  
**Review trigger:** A calibrated re-grade of the catalog is performed, or evidence from
real runs shows that a static severity label would improve question selection

## Context

Every catalog question carries a `criticality` value from `low | medium | high |
critical`. Measured at revision `a80c9653`, the published distribution is:

| Value | Count |
|---|---|
| critical | 124 |
| high | 72 |
| medium | 3 |
| low | 0 |

196 of 199 questions — 98% — sit in the top two adjacent bands, and no question is
labelled `low`. A field whose values are almost constant cannot discriminate between
questions, so it cannot rank a ready frontier.

The risk is not that the field is wrong; it is that the field *looks* like a priority
input. An agent or a reader scanning the catalog would reasonably assume `criticality:
critical` means "ask this first", and would be misled 124 times.

`docs/prioritization.md` never actually used the field — it ranks by impact,
uncertainty, unlock value, urgency, and cost of answering, all scored against the
specific subject. But nothing said so, so the ambiguity survived.

## Decision

1. **`criticality` is advisory.** It is an authoring hint about how consequential a
   question usually is, and it is explicitly **not** the run-time ranking input.
2. **Say so where it is read.** Add a `description` to the field in
   `schemas/question.schema.json`, and a section to `docs/prioritization.md`.
3. **Rank by consequence to the subject.** Severity comes from what happens to *this*
   subject if *this* answer is wrong. A `critical` question may be `not_applicable` for
   an internal tool; a `medium` question may be the controlling blocker for a
   safety-critical system.
4. **Keep the skew visible.** `tools/validate.py` check `Q1` reports the distribution on
   every run and warns when the top two bands exceed 90%.
5. **Do not re-grade the catalog now.**

## Options considered

| Option | Assessment |
|---|---|
| **Demote to advisory, document, and report the skew** | Chosen. Removes the misleading signal at near-zero risk, and keeps the field's genuine value as an authoring hint. |
| Re-grade all 199 questions against a rubric with a forced distribution | The most thorough fix, and it requires the maintainer's semantic judgment on 199 items. An agent performing it would be inventing severity rankings it has no evidence for — precisely the failure mode this framework exists to prevent. Deferred as owner work. |
| Remove the field entirely | Loses real authoring signal and breaks `question.schema.json` for every existing consumer, in exchange for solving a problem that documentation solves. |
| Leave it as-is | Keeps a field that reads as priority and cannot function as one. |

## Consequences

- No catalog content changes; no stable IDs move; the schema stays backward compatible
  because a `description` is annotation only.
- Agents and readers now have an explicit statement that ranking is run-time work.
- The skew remains, and is now surfaced as a warning on every validator run rather than
  being silently carried. `make check` (`--strict`) treats it as a failure, so a future
  release gate can require it be resolved.
- A calibrated re-grade remains open work for the maintainer. It is recorded here rather
  than in the catalog so the deferral is visible.
