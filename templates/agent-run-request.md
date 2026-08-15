# Scrutable agent run request

Use the pinned Scrutable revision to review the subject below. Follow
`AGENTS.md` and `docs/11-usage-deployment-and-agent-integration.md`.

## Run inputs

- Run ID:
- Subject and boundary:
- Target repository and revision:
- Decision this run must enable:
- Lifecycle stage:
- Intended beneficiaries and affected parties:
- Desired outcome and success/failure measures:
- Constraints and unacceptable losses:
- Evidence already available:
- Decision owner and approval authorities:
- Time, cost, and evidence budget:

## Required behavior

1. Create or update only `runs/<run-id>/` unless framework changes are separately
   authorized.
2. Pin `scrutable_ref` and the target revision in `00-manifest.md`.
3. Instantiate the core project-profile questions, then select conditional questions.
4. Label facts, observations, inferences, assumptions, predictions, preferences, and
   decisions separately. Never invent evidence.
5. Produce the strongest evidence-based failure mechanisms, controlling bottleneck,
   realistic alternatives, cheapest discriminating test, and kill/pivot thresholds.
6. Propagate accepted answers into linked requirements, decisions, risks, experiments,
   metrics, tests, approvals, and artifacts.
7. End with `proceed`, `proceed_with_conditions`, `pause`, or `stop`, plus unresolved
   conditions, owners, and review triggers.

## Permission boundary

Do not deploy, contact people, purchase advertising, spend money, change external
systems, or command hardware unless that action is separately and explicitly
authorized. Draft proposals and experiments instead.

