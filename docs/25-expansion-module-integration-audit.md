# Expansion module integration audit

## Scope

This audit covers the promotion of 52 backlog candidates into eight conditional
catalog modules for international operations, enterprise implementation, marketplace
and network governance, intellectual property, financial crime, hardware
manufacturing and recall, crisis communication, and liability and insurance.

The audit evaluates structural integration only. It does not claim that a real
market, customer implementation, payment program, marketplace, IP position,
manufacturing system, crisis, claim, or insurance program has been validated.

## Change inventory

| Area | Published questions | Catalog path | Operating method or register |
|---|---:|---|---|
| Internationalization and localization operations | 8 | `catalog/operations/internationalization-localization-questions.yaml` | `docs/22-internationalization-and-localization-operations.md`; `templates/localization-readiness-register.md` |
| Enterprise implementation and customer success | 8 | `catalog/business/enterprise-implementation-questions.yaml` | `docs/23-enterprise-implementation-and-customer-success.md`; `templates/enterprise-implementation-register.md` |
| Marketplace and network governance | 6 | `catalog/business/marketplace-network-questions.yaml` | `docs/24-conditional-marketplace-ip-financial-hardware-crisis-liability.md`; `templates/conditional-risk-register.md` |
| Intellectual-property ownership and defensibility | 6 | `catalog/legal/intellectual-property-questions.yaml` | same conditional method and register |
| Fraud, payments, and financial crime | 6 | `catalog/security/financial-crime-questions.yaml` | same conditional method and register |
| Hardware manufacturing, field service, and recall | 6 | `catalog/operations/hardware-manufacturing-recall-questions.yaml` | same conditional method and register |
| Crisis, reputation, and public communication | 6 | `catalog/operations/crisis-communication-questions.yaml` | same conditional method and register |
| Liability allocation and insurance | 6 | `catalog/legal/liability-insurance-questions.yaml` | same conditional method and register |
| **Total** | **52** | **8 modules** | **3 methods/audit and 3 registers** |

## Activation integration

The new modules are reachable from existing high-level questions without making every
question universal:

- `core.boundary.001` activates `operations.localization-scope.001`;
- `business.organizational-buying.001` activates
  `business.implementation-dependencies.001`;
- `business.channels.001` activates `business.marketplace-sides.001`;
- `legal.obligations.001` activates `legal.ip-ownership.001` and
  `legal.liability-map.001`;
- `security.threats.001` activates `security.financial-abuse.001`;
- `architecture.context.001` activates
  `operations.manufacturing-dependencies.001`; and
- `operations.incident.001` activates `operations.crisis-scope.001`.

Cross-module activations connect local commercial operation and marketplace abuse to
financial crime; local commercial operation, freedom to operate, financial loss, and
hardware recall to liability; and multilingual support and hardware recall to crisis
communication. Each target retains an explicit `applies_when` condition.

## Backlog requirement mapping

Every requested backlog sentence is preserved as the decision focus of one stable
question. The promotion adds, for each question, a permanent ID, applicability,
lifecycle stages, criticality, dependencies or activations, evidence requirements,
expected outputs, accountable roles, revisit triggers, and tags.

The new methods add blocker conditions, authority limits, current-source and qualified
review boundaries, positive operating loops, exit or recovery paths, and agent
permission boundaries. The registers provide a run-level place to record evidence,
state, owner, decision, residual risk, and review trigger.

## Structural counts

Before this promotion, the catalog contained 147 published questions and 628
relationship references: 323 `depends_on`, 205 `activates`, 98 `related_to`, and two
`refines` references.

The eight new modules add 52 questions, 173 `depends_on`, 85 internal or cross-module
`activates`, and 115 `related_to` references. Eight existing anchor activations are
also added. The resulting expected catalog is:

- 199 published questions;
- 496 `depends_on` references;
- 298 `activates` references;
- 213 `related_to` references;
- two `refines` references; and
- 1,009 relationship references in total.

## Validation performed

The change is acceptable only when the repository validation records show all of the
following:

- all eight YAML modules parse;
- all 52 question objects conform to `schemas/question.schema.json`;
- all IDs are unique and follow the permanent ID pattern;
- every relationship target exists in the combined catalog;
- the `depends_on` graph remains acyclic;
- every new Markdown link resolves;
- the eight requested backlog areas and all 52 candidate questions map to stable
  records;
- navigation, agent context, contributor guidance, backlog status, and changelog are
  consistent; and
- no status is upgraded from partial to covered without run evidence.

Validation output and exact graph counts should be generated from the final branch,
not inferred from this document.

## Prose-to-catalog manifest decision

`coverage/prose-to-catalog.yaml` inventories the 396 numbered questions in the seven
main human-readable question banks. This change does not alter those source questions
or their mappings. The promoted records originate in the expansion backlog and remain
outside that seven-bank manifest scope, consistent with its documented exclusions.
Changing the manifest only to increase a count would therefore overstate its scope.

A future validator should separately check that backlog candidates marked as promoted
resolve to the published IDs named in the backlog and that status does not drift.

## Remaining evidence and limitations

All eight areas remain **partial — structured module or method published** until
representative runs demonstrate useful activation, decision change, missed-concern
coverage, evidence cost, false blockers, calibration, and recovery behavior.
Additional requirements include:

- qualified local legal, tax, payments, linguistic, cultural, and accessibility review
  for international markets;
- successful and failed enterprise implementation, value, recovery, and renewal
  evidence;
- marketplace liquidity, governance, abuse, appeal, concentration, and portability
  cases;
- qualified ownership, chain-of-title, freedom-to-operate, protection, secrecy, and
  enforcement review;
- regulated financial-crime interpretation, control, appeal, loss, and reviewer
  evidence;
- manufacturing, field-service, mock-recall, safety, and remediation exercises;
- crisis authority, fallback channel, changing-fact, misinformation, correction, and
  trust-recovery exercises; and
- actual policy, correlated-loss, evidence-preservation, claim, coverage, and
  survivability review.

The deterministic conformance and semantic validator remained a separate P0 capability
gap at the time of this audit. This promotion supplied structured inputs for that
validator but did not create it.

**Update, 2026-08-13:** the *conformance* half of that gap is now closed —
`tools/validate.py` runs in CI and enforces the structural claims this audit made by
hand ([ADR-0005](../decisions/ADR-0005-deterministic-conformance-validator.md)). The
*semantic* half — state transitions, applicability, evidence sufficiency, blocker
policy, and gate correctness — remains open, and A2 must not be claimed.
