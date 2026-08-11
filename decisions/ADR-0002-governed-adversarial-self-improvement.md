# ADR-0002: Governed adversarial self-improvement

- **Status:** Accepted
- **Date:** 2026-08-11
- **Decision owners:** Repository maintainers
- **Scope:** Product Questionbook framework and future engine

## Context

The framework must challenge weak application ideas, find controlling bottlenecks,
support evidence-based pivots, cover attraction and distribution, and learn from prior
runs. LLMs can be sycophantic, can produce confident but unsupported criticism, and
can amplify a shared prompt bias through apparent multi-agent consensus.

Unrestricted self-modification would allow the engine to change its own questions,
blocker rules, schemas, or approval policy in response to one run. That would destroy
traceability and permit local optimization, data poisoning, or convenient removal of
difficult questions.

## Decision

Adopt the governed adversarial improvement loop defined in
[`../docs/10-self-improvement-and-adversarial-governance.md`](../docs/10-self-improvement-and-adversarial-governance.md).

The loop will:

1. separate application, idea, project-graph, and repository improvement;
2. require attributable observations, falsifiable challenge packets, alternative
   candidates, discriminating tests, a decision, and an outcome review;
3. use independent critic roles followed by cross-examination and evidence audit;
4. rank the controlling bottleneck by consequence, graph centrality, uncertainty,
   evidence weakness, irreversibility, urgency, and validation cost;
5. preserve idea lineage and create a new subject for a domain pivot instead of
   silently rewriting history;
6. treat attraction as a qualified funnel from discovery through retained value and
   sustainable economics, not as raw impressions;
7. allow the engine to propose repository changes but prohibit autonomous publication
   of catalog, schema, blocker-policy, security-control, or approval-rule changes;
8. require accountable human or organizational authority for material commitment and
   risk acceptance.

"Brutal" is defined as unflinching evidentiary and causal scrutiny. Abusive tone,
performative negativity, and unsupported certainty are not accepted review methods.

## Consequences

### Positive

- Praise and criticism become inspectable inputs rather than persuasion.
- Pivots can be radical while retaining provenance and comparability.
- The framework can learn which questions predict failures or change decisions.
- Distribution, advertising, retention, and machine discoverability become explicit
  success concerns where applicable.
- Protected governance assets cannot be rewritten by the system they govern.

### Costs and limitations

- Independent review, experiments, and outcome measurement require time and money.
- Human authority remains a bottleneck for high-impact decisions.
- Historical outcome data can be biased and must be segmented by project type.
- The loop improves decision quality but cannot guarantee market or operational
  success.

## Validation

Before implementing an autonomous runner, validate:

- the improvement-cycle schema against complete and minimal examples;
- challenge-packet usefulness on at least three different project types;
- inter-rater consistency for bottleneck ranking;
- whether critics find seeded failure mechanisms without inventing evidence;
- whether candidate generation includes stop/pause and preserves idea lineage;
- whether attraction questions distinguish reach, activation, retention, and
  sustainable economics;
- that protected framework assets can only change through the repository review path.

## Reversal triggers

Revisit this decision if the process produces large false-blocker costs, suppresses
safe exploration, fails to discover known seeded risks, or if a stronger auditable
governance mechanism becomes available.

