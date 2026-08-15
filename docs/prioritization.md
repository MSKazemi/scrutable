# Adaptive interview and prioritization

Scrutable does not ask every question in catalog order. It first builds a subject
profile, evaluates applicability and dependencies, then ranks ready questions.

## Selection sequence

1. Instantiate the core project-profile questions.
2. Evaluate `applies_when` rules against known facts and answers.
3. Mark false applicability as `not_applicable` with a reason.
4. Keep questions with unmet dependencies `dormant`.
5. Detect contradictions, stale answers, and missing evidence.
6. Rank ready questions.
7. Ask the highest-value question appropriate for the available owner.
8. Re-evaluate the graph after every answer or material event.

## Baseline score

For a ready question:

\[
\text{priority} =
\frac{\text{impact} \times \text{uncertainty} \times \text{unlock value} \times \text{urgency}}
{\max(\text{cost of answering}, 1)}
\]

Use normalized values from 1 to 5:

- **impact**: consequence of an incorrect or missing answer;
- **uncertainty**: weakness of current knowledge or evidence;
- **unlock value**: number and importance of downstream questions or actions enabled;
- **urgency**: time sensitivity, reversibility, and proximity to a commitment;
- **cost of answering**: time, money, access, and coordination needed.

## The catalog `criticality` field is advisory, not the ranking input

Every catalog question carries a `criticality` value. It is an authoring hint about how
consequential the question *usually* is. **It is not used to rank the ready frontier**,
and it must not be substituted for the score above.

The reason is measurable. In the published catalog, 196 of 199 questions are labelled
`high` or `critical` and none is labelled `low`. A field whose values are 98% one of two
adjacent levels cannot order anything. `tools/validate.py` reports this distribution on
every run (check `Q1`) so that the skew stays visible instead of being mistaken for
priority information.

Severity always comes from what happens to **this** subject if **this** answer is wrong.
A question marked `critical` may be `not_applicable` for an internal tool; a question
marked `medium` may be the controlling blocker for a safety-critical system.

## Mandatory overrides

Scoring never suppresses a critical gate. A question moves ahead of the numeric queue
when it:

- blocks a release, legal obligation, safety control, or irreversible decision;
- reveals a contradiction in a critical answer;
- is stale after a material change;
- lacks an owner despite high impact;
- is required to assess whether other questions apply.

## Tie-breaking

When scores are equal, prefer the question that is cheaper to answer, unlocks more of
the graph, reduces risk sooner, and can be answered by a currently available owner.
The score and its inputs should remain visible so a human can override the ranking.

