# Question catalog

Each domain file contains reusable question templates. Project-specific answers,
states, owners, and evidence belong in question-instance and answer records, never in
these files.

## Catalog file shape

```yaml
schema_version: 1
domain: security
questions:
  - id: security.identity.001
    version: 1
    status: published
    question: How will each actor prove its identity?
    purpose: Define trust boundaries before choosing authentication mechanisms.
    domain: security
    lifecycle_stages: [design, build, verify, operate]
    applies_when: [the subject has authenticated actors]
    answer_type: structured
    criticality: critical
    depends_on: [users.actors.001]
    activates: [security.authorization.001]
    evidence_required: [threat model, authentication test]
    expected_outputs: [security requirements, threat model]
```

Question objects conform to [`../schemas/question.schema.json`](../schemas/question.schema.json).
The natural-language `applies_when` rules are intentionally readable in this first
version. A future executable rule language must version its syntax and preserve the
human explanation.

## ID policy

Use `domain.topic.NNN`. Published IDs are permanent. Correct wording with a version
increment; deprecate and link a successor when the meaning changes.

