---
artifact: adversarial-review
run_id: "<run-id>"
project_id: "<project-id>"
review_id: "<review-id>"
subject_id: "<subject-id>"
decision_id: "<decision-id>"
questionbook_ref: "<git-commit-sha>"
graph_revision: 0
generated_at: "<ISO-8601 timestamp>"
---

# Adversarial review: <claim or proposal>

## Decision under attack

- **Claim/proposal:** <precise statement>
- **Owner:** <accountable owner>
- **Commitment and deadline:** <what becomes difficult to reverse, and when>
- **Desired outcome:** <measurable outcome>
- **Guardrails:** <unacceptable losses>

## Steelman

State the strongest evidence-based case for the proposal before attacking it. Do not
use enthusiasm, novelty, status, or agent agreement as evidence.

## Challenge packets

### <critique ID>: <short failure mode>

- **Reviewer role:** <market/technical/security/distribution/finance/evidence/etc.>
- **Target claim:** <claim>
- **Strongest counterclaim:** <counterclaim>
- **Causal failure mechanism:** <step-by-step mechanism>
- **Exposed people/assets/obligations:** <scope and blast radius>
- **Evidence for the critique:** <IDs or missing>
- **Evidence against the critique:** <IDs or missing>
- **Likelihood / impact / confidence:** <1-5> / <1-5> / <low-medium-high>
- **Falsifier:** <what observation would show this critique is wrong>
- **Cheapest safe test:** <test>
- **Continue/pivot/stop threshold:** <threshold and window>
- **Decision impact:** <affected decision and nodes>

Repeat for each material critique. Reject criticism that has no plausible mechanism or
cannot change a decision.

## Controlling bottleneck

<Identify the attack that blocks the largest amount of downstream value and explain
why it outranks more visible concerns.>

## Cross-examination

| Issue | Champion response | Critic rebuttal | Evidence-auditor finding | Unresolved? |
|---|---|---|---|---|
| <issue> | <response> | <rebuttal> | <provenance/strength> | <yes/no> |

## Required alternatives

| Candidate | What remains invariant | What changes | Best case | Pessimistic case | Test | Kill threshold |
|---|---|---|---|---|---|---|
| Current path | <invariants> | <none> | <outcome> | <outcome> | <test> | <threshold> |
| Alternative | <invariants> | <change> | <outcome> | <outcome> | <test> | <threshold> |
| Stop/pause | <protected value> | <commitment avoided> | <outcome> | <outcome> | <trigger> | <threshold> |

## Distribution and attraction check

- **Intended qualified audience:** <segment and size>
- **Discovery path:** <how they encounter it>
- **Positioning/message test:** <evidence>
- **Reach -> activation -> retention evidence:** <metrics, denominators, cohorts, windows>
- **Paid advertising incrementality and CAC:** <evidence or not applicable>
- **Channel concentration/platform risk:** <risk>
- **Machine/search/marketplace discoverability:** <evidence>
- **Vanity-metric or harmful-attention risk:** <guardrail>

## Verdict

- **Recommendation:** <continue/change/pivot/split/pause/stop>
- **Confidence and scope:** <qualified confidence>
- **Blocking critiques:** <IDs>
- **Accepted risks and authority:** <IDs/owner>
- **Required experiment or evidence:** <IDs>
- **Review trigger:** <event/date>
