---
artifact: risk-register
run_id: "<run-id>"
project_id: "<project-id>"
subject_id: "<subject-id>"
scrutable_ref: "<git-commit-sha>"
graph_revision: 0
generated_at: "<ISO-8601 timestamp>"
---

# Risk register: <subject name>

## Rating model

State the scales used for likelihood, impact, detectability, and exposure. Do not
present a numeric score without its assumptions and time horizon.

## Active risks

| Risk ID | Uncertain condition and consequence | Exposed groups/assets | Likelihood | Impact | Evidence | Treatment | Owner | Due or review date |
|---|---|---|---:|---:|---|---|---|---|
| <ID> | <if/then statement> | <groups/assets> | <rating> | <rating> | <evidence IDs> | <avoid/reduce/transfer/accept> | <owner> | <date> |

## Accepted risks

| Risk ID | Residual exposure | Rationale | Acceptance authority | Accepted at | Review date | Reopen trigger |
|---|---|---|---|---|---|---|
| <ID> | <exposure> | <reason> | <owner> | <date> | <date> | <trigger> |

Critical risk acceptance is incomplete without an accountable authority, rationale,
review date, and reopen trigger.

## Closed or superseded risks

| Risk ID | Resolution | Evidence | Closed by | Date | Successor |
|---|---|---|---|---|---|
| <ID> | <resolution> | <evidence IDs> | <owner> | <date> | <risk ID or none> |
