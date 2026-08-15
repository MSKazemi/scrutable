# Output contract

Scrutable produces an **assurance package**, not only a questionnaire or a set of
documents. Outputs must be reproducible from canonical run records pinned to a target
and Scrutable revision; a graph snapshot is a derived logical projection of those
records.

## Machine-readable outputs

| Output | Minimum content |
|---|---|
| Project graph | Subjects, instances, answers, evidence, decisions, risks, actions, artifacts, and typed relationships |
| Instance state | Current state plus append-only transition history |
| Answer history | Revisions, assumptions, confidence, owner, and supersession |
| Evidence index | Source, type, collection time, reviewer, validity, and expiry |
| Conflict report | Contradictions and unresolved reconciliation actions |
| Coverage report | Applicable, verified, blocked, stale, accepted-risk, and missing-evidence counts |
| Priority queue | Ranked ready questions with visible scoring factors and overrides |

## Human-readable outputs

- project charter and definition of success;
- stakeholder and user-needs summary;
- product requirements and naming brief;
- architecture and decision records;
- data model and governance plan;
- security and privacy assessment;
- UX and accessibility specification;
- test and quality strategy;
- deployment, observability, support, and operational plan;
- business case and risk register;
- launch-readiness report;
- maintenance, evolution, and retirement plan.

## Action outputs

- tasks for unresolved questions or evidence collection;
- experiments required to validate assumptions;
- decisions awaiting an accountable approver;
- risks awaiting treatment or formal acceptance;
- scheduled reviews for answers that can become stale.

## Generation rules

1. Every generated item includes project ID, subject boundary, graph revision, and generation time.
2. Claims link to the answer and evidence records that support them.
3. Unresolved, blocked, stale, and accepted-risk items remain visible.
4. Missing information is rendered as missing, never silently invented.
5. Conflicting answers are shown with their reconciliation status.
6. A generated document is a view; edits must be captured back into the canonical
   Markdown or YAML records from which the logical graph is derived.
7. Regeneration is deterministic for the same graph revision and template version.

Templates in [`templates`](../templates) define the first human-readable views.
