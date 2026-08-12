---
artifact: decision-record
run_id: "<run-id>"
decision_id: "<decision-id>"
project_id: "<project-id>"
subject_id: "<subject-id>"
questionbook_ref: "<git-commit-sha>"
status: proposed
graph_revision: 0
generated_at: "<ISO-8601 timestamp>"
---

# Assurance decision: <short title>

## Context

<The situation, boundary, and commitment requiring a decision.>

## Decision owner and authority

- **Accountable owner:** <name or role>
- **Required reviewers:** <names or roles>
- **Decision deadline:** <date or event>
- **Reversibility:** <easy, costly, or effectively irreversible>

## Questions and evidence

| Question instance | Accepted answer revision | Evidence | Confidence | Unresolved concern |
|---|---|---|---|---|
| <ID> | <answer ID> | <evidence IDs> | <low/medium/high> | <concern or none> |

## Options considered

| Option | Benefits | Costs and risks | Constraint fit | Evidence |
|---|---|---|---|---|
| <option> | <benefits> | <costs/risks> | <fit> | <evidence IDs> |

## Decision

<Chosen option and the reasoning that distinguishes it from alternatives.>

## Consequences

- **Expected benefits:** <outcomes>
- **Accepted tradeoffs:** <tradeoffs>
- **New risks:** <risk IDs>
- **Required actions:** <action IDs>
- **Affected artifacts and tests:** <IDs>

## Revisit conditions

- <event, measurement threshold, expiry, or assumption change>

## History

| Date | Status | Actor | Reason | Supersedes |
|---|---|---|---|---|
| <date> | <proposed/accepted/superseded> | <actor> | <reason> | <decision ID or none> |
