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


## Human-readable question coverage

The catalog is deliberately smaller than the detailed Markdown question banks. The
[`../coverage/prose-to-catalog.yaml`](../coverage/prose-to-catalog.yaml) manifest
accounts for every numbered source question and marks its relationship as exact,
compressed, unmodeled, or guidance-only. A compressed mapping preserves the prose
detail; it does not authorize an agent to treat the stable node as semantically
identical. See the
[coverage contract](../docs/16-prose-to-catalog-coverage.md).

## Domain-pack governance

The eight questions in [`core/domain-pack-governance-questions.yaml`](core/domain-pack-governance-questions.yaml) activate and govern qualified specialized packs. A pack bundles questions that still use one of the 16 universal concern domains; it does not bypass this schema or invent an unreviewed assurance vocabulary. Pack manifests conform to [`../schemas/domain-pack.schema.json`](../schemas/domain-pack.schema.json), and the lifecycle and blocker rules are defined in the [domain-pack governance contract](../docs/17-domain-pack-governance.md).

The repository currently has zero expert-reviewed published packs. Generic catalog coverage must not be presented as healthcare, financial, children's, government, automotive, aviation, industrial-control, or other professional certification.

## Organizational change module

When `business.adoption.001` identifies a material workflow or organizational transition, load [`team/organizational-change-questions.yaml`](team/organizational-change-questions.yaml). Its eight records distinguish change impact, stakeholder power, enablement, transition, workforce obligations, adoption evidence, pause or restoration safeguards, and post-launch ownership. Technical release alone cannot satisfy these questions.
