---
artifact: improvement-cycle
schema_version: 1
run_id: "<run-id>"
project_id: "<project-id>"
cycle_id: "<cycle-id>"
level: "<application/idea/project_graph/repository>"
subject_id: "<subject-id>"
questionbook_ref: "<git-commit-sha>"
baseline_revision: 0
graph_revision: 0
owner: "<accountable owner>"
created_at: "<ISO-8601 timestamp>"
generated_at: "<ISO-8601 timestamp>"
---

# Improvement cycle: <decision and subject>

## Objective and boundary

- **Decision required:** <decision>
- **Desired outcome:** <measurable outcome>
- **Time horizon:** <window>
- **Decision deadline:** <date/time>
- **Budget/time bound:** <limit>
- **Guardrails and unacceptable losses:** <constraints>
- **Trigger:** <observation, incident, review, stale evidence, or scheduled check>

## Observations

| ID | Observation | Source type | Evidence | Confidence | Observed at |
|---|---|---|---|---|---|
| <ID> | <attributable statement> | <experiment/telemetry/research/etc.> | <evidence IDs> | <low/medium/high> | <timestamp> |

Separate direct observations from inferences and predictions.

## Independent adversarial critiques

| Critique | Target claim | Failure mechanism | Evidence for/against | Falsifier | Cheapest test | Decision impact |
|---|---|---|---|---|---|---|
| <ID> | <claim> | <causal path> | <IDs/IDs> | <observation> | <test> | <continue/pivot/stop implication> |

Preserve critical minority objections. Agent agreement is not evidence.

## Controlling bottleneck

**Statement:** <uncertainty or constraint limiting the largest downstream outcome>

| Impact | Centrality | Uncertainty | Evidence weakness | Irreversibility | Urgency | Validation cost | Score |
|---:|---:|---:|---:|---:|---:|---:|---:|
| <1-5> | <1-5> | <1-5> | <1-5> | <1-5> | <1-5> | <1-5> | <computed> |

**Dependent nodes:** <IDs>

## Candidate paths

| Candidate | Action | Preserved invariants | Changed assumptions | Predicted outcomes | Transition cost/risk |
|---|---|---|---|---|---|
| <ID> | <continue/change/pivot/split/pause/stop> | <IDs> | <assumptions> | <measures and windows> | <cost/risk> |

Include the current path, at least one materially different alternative, and stop or
pause for a consequential commitment.

## Discriminating experiments

| Experiment | Competing claims | Method | Success threshold | Failure threshold | Status | Evidence/result |
|---|---|---|---|---|---|---|
| <ID> | <A vs B> | <method> | <threshold> | <threshold> | <planned/running/completed> | <IDs/result> |

## Decision

- **Action:** <continue/implementation change/solution pivot/customer pivot/problem pivot/domain pivot/split/pause/stop>
- **Selected candidate:** <ID>
- **Rationale:** <why it beats realistic alternatives>
- **Confidence:** <low/medium/high>
- **Approval:** <proposed/accepted/rejected>
- **Decision owner:** <owner>
- **Affected graph nodes to reopen:** <IDs>
- **Kill/pivot criteria:** <thresholds and deadlines>
- **Next outcome review:** <event/date>

## Repository-learning proposal

Complete only when run evidence suggests a reusable framework change.

| Proposal | Change type | Stable IDs | Multi-run/incident evidence | Compatibility/migration | Reversal trigger |
|---|---|---|---|---|---|
| <ID> | <add/revise/deprecate/relationship/policy> | <IDs> | <evidence> | <impact> | <trigger> |

## Outcome review

| Predicted outcome | Observed outcome | Error/side effect | Evidence | Affected nodes |
|---|---|---|---|---|
| <prediction> | <observation> | <difference> | <IDs> | <IDs> |

- **Did the bottleneck move?** <answer>
- **Next trigger:** <event/date>
