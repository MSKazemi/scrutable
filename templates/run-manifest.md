---
schema_version: questionbook-run/v0.1
run_id: RUN-YYYY-NNNN
subject_id: SUBJECT-NNN
subject_type: application
stage: discover
status: in_review
owner: owner-id
decision_to_enable: ""
target_repository: ""
target_revision: git-commit-sha
questionbook_repository: MSKazemi/mohsen
questionbook_ref: git-commit-sha
policy_ref: policy-id-or-path
gate_result: null
blockers: []
coverage:
  applicable: 0
  verified: 0
  accepted_risk: 0
  blocked: 0
  stale: 0
  unanswered: 0
created_at: YYYY-MM-DDTHH:MM:SSZ
updated_at: YYYY-MM-DDTHH:MM:SSZ
---

# Run manifest

## Purpose and boundary

- Decision this run must enable:
- Included subject boundary:
- Explicitly excluded boundary:
- Time, cost, and evidence budget:

## Required inputs

- Subject profile:
- Outcomes and guardrails:
- Constraints:
- Policies and approval authorities:
- Evidence snapshot:
- Prior-state revision:

## Output index

| Artifact | Status | Trace or path |
|---|---|---|
| Context and success | missing | `01-context-and-success.md` |
| Applicability and coverage | missing | `02-applicability-and-coverage.md` |
| Question/answer/evidence ledger | missing | `03-question-answer-ledger.md` |
| Gate and assurance report | missing | `09-gate-and-assurance-report.md` |
| Audit and change impact | missing | `10-audit-and-change-impact.md` |

## Integrity checks

- [ ] Target and Questionbook revisions are immutable and resolvable.
- [ ] Unknowns, contradictions, stale records, and accepted risks are visible.
- [ ] Critical blockers are not averaged away.
- [ ] Every accepted consequential decision has evidence, owner, approval where
      required, verification, and a review trigger.
- [ ] Generated artifacts resolve to canonical graph node IDs.

