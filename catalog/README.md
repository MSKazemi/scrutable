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

The similarly named `catalog/core/project-profile.yaml` is a catalog module containing
the ten starting question templates. It is not a run-specific project profile and is
not validated as one object by `schemas/project-profile.schema.json`; each item in its
`questions` array validates against `schemas/question.schema.json`.

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

The expansion-backlog candidates promoted in the modules below are outside the
seven-bank numbered-source scope of that manifest. Their stable IDs and status are
tracked in the [expansion backlog](../docs/12-coverage-gaps-and-expansion-backlog.md)
and [integration audit](../docs/25-expansion-module-integration-audit.md).

## Domain-pack governance

The eight questions in
[`core/domain-pack-governance-questions.yaml`](core/domain-pack-governance-questions.yaml)
activate and govern qualified specialized packs. A pack bundles questions that still
use one of the 16 universal concern domains; it does not bypass this schema or invent
an unreviewed assurance vocabulary. Pack manifests conform to
[`../schemas/domain-pack.schema.json`](../schemas/domain-pack.schema.json), and the
lifecycle and blocker rules are defined in the
[domain-pack governance contract](../docs/17-domain-pack-governance.md).

The repository currently has zero expert-reviewed published packs. Generic catalog
coverage must not be presented as healthcare, financial, children's, government,
automotive, aviation, industrial-control, or other professional certification.

## Organizational change module

When `business.adoption.001` identifies a material workflow or organizational
transition, load
[`team/organizational-change-questions.yaml`](team/organizational-change-questions.yaml).
Its eight records distinguish change impact, stakeholder power, enablement,
transition, workforce obligations, adoption evidence, pause or restoration
safeguards, and post-launch ownership. Technical release alone cannot satisfy these
questions.

## Workforce continuity module

When `team.capability.001` reveals material human dependencies, load
[`team/workforce-continuity-questions.yaml`](team/workforce-continuity-questions.yaml).
Its eight records separate key-person concentration, transfer and rehearsal,
sustainable capacity, unsafe incentives, secure departure, emergency separation of
duties, supplier dependence, and leading indicators. A named backup or a document
alone is not continuity evidence; transfer and recovery must be demonstrated.

## External sensing module

When `core.assumptions.001` depends on changing outside conditions, load
[`operations/external-sensing-questions.yaml`](operations/external-sensing-questions.yaml)
and the
[external sensing method](../docs/18-external-sensing-and-attention.md). The eight
records connect change classes, source portfolios, monitoring ownership, correlation,
thresholds, response latency, missed-signal learning, and blind spots. They guarantee
visible process accounting, not complete world knowledge or audience attention.

## Information-integrity module

When `ethics.harms.001` identifies harm from created, imported, transformed, ranked,
recommended, stored, or distributed content, load
[`ethics/information-integrity-questions.yaml`](ethics/information-integrity-questions.yaml)
and the
[content-governance method](../docs/20-information-integrity-and-content-governance.md).
Its eight records separate content and context risk, provenance, policy, coordinated
manipulation, review and appeal, assurance and reviewer safety, transparency, and
downstream correction. Provenance is never treated as proof of truth.

## Geopolitical continuity module

When `business.continuity.001` identifies regional, cross-border, currency, network,
supplier, staff, customer, asset, or legal-entity concentration, load
[`operations/geopolitical-continuity-questions.yaml`](operations/geopolitical-continuity-questions.yaml)
and the
[regional continuity method](../docs/21-geopolitical-and-regional-continuity.md). The
eight records separate exposure, changing obligations, disruption, lawful relocation,
people protection, asset access, early triggers, and fallback-created harm. Generic
records do not replace qualified sanctions, trade, privacy, labor, safety, or local
legal review.

## Internationalization and localization operations module

When `core.boundary.001` reveals more than one language, script, locale, culture,
time zone, or market, load
[`operations/internationalization-localization-questions.yaml`](operations/internationalization-localization-questions.yaml)
and the
[international operations method](../docs/22-internationalization-and-localization-operations.md).
Its eight records cover market scope, right-to-left and locale mechanics, translation
governance, local prices, taxes, payments, identity and contracts, multilingual
support and incident communication, local validation, parity, and market exit.

## Enterprise implementation and customer-success module

When `business.organizational-buying.001` leads to customer-side configuration,
migration, integration, approval, or organizational change, load
[`business/enterprise-implementation-questions.yaml`](business/enterprise-implementation-questions.yaml)
and the
[enterprise implementation method](../docs/23-enterprise-implementation-and-customer-success.md).
Its eight records cover cross-party dependencies and ownership, time to value,
recurring rollout blockers, customer-success roles, value realization, renewal risk,
and recovery or exit.

## Marketplace and network module

When `business.channels.001` includes a multi-sided marketplace, network, matching,
ranking, reputation, or transaction system, load
[`business/marketplace-network-questions.yaml`](business/marketplace-network-questions.yaml).
Its six records cover participant sides and liquidity, ethical cold start, rules and
appeals, strategic abuse, network concentration and exclusion, and participant
portability.

## Intellectual-property module

When `legal.obligations.001` identifies material inventions, code, data, content,
models, prompts, designs, proprietary knowledge, or third-party rights, load
[`legal/intellectual-property-questions.yaml`](legal/intellectual-property-questions.yaml).
Its six records cover ownership, rights chain, freedom to operate, protection and
disclosure strategy, trade-secret controls, and evidence-backed defensibility.

## Financial-crime module

When `security.threats.001` identifies money, credit, refunds, promotions, financial
identity, marketplace value, safeguarding, or valuable access, load
[`security/financial-crime-questions.yaml`](security/financial-crime-questions.yaml).
Its six records cover abuse and maximum loss, qualified obligations, prevention and
investigation, proportionate friction, false positives and appeals, and loss
allocation and reserves.

## Hardware manufacturing and recall module

When `architecture.context.001` includes manufactured, assembled, shipped, installed,
maintained, or recalled hardware, load
[`operations/hardware-manufacturing-recall-questions.yaml`](operations/hardware-manufacturing-recall-questions.yaml).
Its six records cover production dependencies, quality and traceability, release
evidence, field service, affected-unit discovery, and stop, quarantine, recall, and
remediation authority.

## Crisis-communication module

When `operations.incident.001` can require stakeholder, regulatory, media, or public
communication, load
[`operations/crisis-communication-questions.yaml`](operations/crisis-communication-questions.yaml).
Its six records cover audiences and thresholds, spokesperson and correction
authority, resilient channels, actionable uncertainty, misinformation and
impersonation, and evidence of trust and relationship recovery.

## Liability and insurance module

When `legal.obligations.001` identifies material loss, third-party claims, indemnity,
insurance, or survivability exposure, load
[`legal/liability-insurance-questions.yaml`](legal/liability-insurance-questions.yaml).
Its six records cover liability mapping, contract alignment, policy scope and
conditions, correlated coverage failure, claim evidence, and residual loss acceptance.

The six conditional modules above share the
[conditional operating method](../docs/24-conditional-marketplace-ip-financial-hardware-crisis-liability.md)
and [conditional risk register](../templates/conditional-risk-register.md). Their
priority is determined by applicability and consequence in each run, not by the global
backlog label.
