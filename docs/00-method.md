# Working method

This framework is a decision aid, not a ceremony. Ask only the questions that can change a decision, reveal a risk, or define how success will be verified.

## Step 1: establish context

Write down:

- product name and one-sentence description;
- product stage: idea, prototype, launch, growth, mature, or retirement;
- target users and other affected people;
- business model or organizational purpose;
- domain, countries, platforms, and regulatory constraints;
- team, budget, deadline, and existing systems;
- decision that this review must enable.

## Step 2: select applicable aspects

Use [the aspects map](01-aspects.md). Mark each aspect:

- `Critical`: failure could invalidate or seriously harm the product;
- `Important`: it materially affects value, cost, or risk;
- `Relevant`: it deserves a deliberate answer;
- `Not applicable`: explain why it does not apply.

## Step 3: answer with evidence

Use this format for questions whose answer affects the product:

```md
### Question

**Answer:**
**Evidence:**
**Assumptions:**
**Unknowns:**
**Decision:**
**Owner:**
**Verify by:**
**Review date:**
```

Prefer user research, production data, experiments, prototypes, and authoritative constraints over opinions. Label estimates and hypotheses honestly.

## Step 4: turn answers into action

Every important answer should produce at least one of these:

- a requirement or acceptance criterion;
- a design or architecture decision;
- an experiment or research task;
- a risk with an owner and mitigation;
- a metric, alert, test, or operational procedure;
- an explicit decision to defer or exclude something.

## Step 5: review at gates

Use the [scorecard](../templates/review-scorecard.md) at these gates:

1. problem approval;
2. scope approval;
3. architecture and security review;
4. release readiness;
5. post-launch review;
6. major change or retirement.

Do not average away a fatal weakness. A critical security, safety, legal, or reliability gap is a release blocker even if other scores are high.

## Ground rules

- Separate facts, assumptions, decisions, and preferences.
- Ask “for whom?” and “under what conditions?” when language is broad.
- Define measurable terms instead of using words such as fast, simple, scalable, secure, or intuitive without thresholds.
- Capture disagreement and rejected alternatives in a [decision record](../templates/decision-record.md).
- Revisit answers when users, scale, regulation, dependencies, or strategy change.
