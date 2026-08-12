# Conditional marketplace, intellectual-property, financial-crime, hardware, crisis, and liability modules

## Purpose and boundary

This method governs six concerns that are not universal but become critical when they
apply:

- ecosystem, marketplace, and network governance;
- intellectual-property ownership and defensibility;
- fraud, payments, and financial crime;
- hardware manufacturing, field service, and recall;
- crisis, reputation, and public communication; and
- liability allocation and insurance.

Their backlog priority is conditional, not a statement of low consequence. A payment
product, marketplace, manufactured device, public-facing high-impact service, or
materially insured exposure should promote the relevant module to P0 for that run.
Generic catalog questions do not replace qualified legal, financial-crime,
manufacturing, safety, insurance, regulatory, or domain expertise.

Record activation and decisions in the
[conditional risk register](../templates/conditional-risk-register.md).

## Activation map

| Module | Primary anchor | Activate when |
|---|---|---|
| [Marketplace and network](../catalog/business/marketplace-network-questions.yaml) | `business.channels.001` | Two or more participant groups depend on matching, liquidity, ranking, transactions, reputation, or network effects |
| [Intellectual property](../catalog/legal/intellectual-property-questions.yaml) | `legal.obligations.001` | Material inventions, code, data, content, models, prompts, designs, generated assets, proprietary knowledge, or third-party rights exist |
| [Financial crime](../catalog/security/financial-crime-questions.yaml) | `security.threats.001` | Money, credit, refunds, promotions, financial identity, marketplace value, safeguarding, or financially valuable access can be abused |
| [Hardware manufacturing and recall](../catalog/operations/hardware-manufacturing-recall-questions.yaml) | `architecture.context.001` | Physical units are manufactured, assembled, shipped, installed, maintained, repaired, or recalled |
| [Crisis communication](../catalog/operations/crisis-communication-questions.yaml) | `operations.incident.001` | An incident can require stakeholder, regulatory, media, or public communication |
| [Liability and insurance](../catalog/legal/liability-insurance-questions.yaml) | `legal.obligations.001` | Foreseeable material loss, third-party claims, indemnity, insurance, or organizational survivability is at stake |

Cross-module activation is intentional. Local payments and marketplace abuse can
activate financial-crime questions. Hardware recall can activate crisis communication
and liability. Freedom-to-operate can activate liability. These relationships do not
prove applicability by themselves; record the project-specific reason, owner, and
evidence.

## Marketplace and network governance

Use the six marketplace questions as one loop:

1. identify participant sides and the minimum liquidity or matching quality required
   for beneficial use;
2. test cold start without fake demand, fake supply, misleading listings, or hidden
   subsidy;
3. define ranking, access, fees, quality, disputes, suspension, notice, and appeal;
4. control fraud, collusion, adverse selection, disintermediation, and power
   asymmetry;
5. test whether network effects create durable value, concentration, exclusion, or
   coercive lock-in; and
6. provide participant portability for reputation, history, assets, and relationships.

A marketplace gate is blocked when a critical participant side, liquidity threshold,
rule, appeal path, abuse scenario, concentration harm, or exit right is unknown. Do
not count aggregate signups as liquidity or use fabricated participants as evidence.

## Intellectual-property ownership and defensibility

Use the six intellectual-property questions as one loop:

1. map ownership of inventions, code, data, content, models, prompts, designs, and
   improvements from every contributor and agent;
2. verify assignments, contributor terms, open-source obligations, provenance, and
   third-party rights;
3. obtain scoped qualified freedom-to-operate analysis for material uses and
   jurisdictions;
4. choose what to patent, publish defensively, keep secret, license, or share;
5. demonstrate that confidentiality and trade-secret controls survive collaboration,
   support, telemetry, vendors, model use, and departure; and
6. challenge claimed defensibility using design-around, imitation, expiry,
   enforcement-cost, and competitor evidence.

An IP gate is blocked when material ownership or authority is missing, rights are
incompatible, a significant freedom-to-operate risk lacks qualified disposition, or
a secrecy claim is unsupported by practical controls. The framework is not an IP
opinion and cannot grant clearance.

## Fraud, payments, and financial crime

Use the six financial-crime questions as one loop:

1. map every valuable flow, abuse path, affected party, and maximum credible loss;
2. identify current KYC, AML, sanctions, reporting, tax, licensing, safeguarding, and
   recordkeeping duties with qualified owners;
3. design and test prevention, detection, investigation, evidence, recovery, and
   learning for account takeover, synthetic identity, stolen instruments,
   chargebacks, refund abuse, collusion, and laundering;
4. set proportionate limits, holds, reserves, step-up checks, and manual reviews;
5. measure false positives, appeals, bias, customer harm, correction time, and
   reviewer workload; and
6. allocate losses contractually and economically with reserves and survivability.

A financial gate is blocked when material value flows or losses are unknown, required
qualified interpretation is missing, controls cannot be investigated or tested,
legitimate users lack appeal and correction, or the organization cannot fund the
credible residual loss. Regulated financial activity requires an approved qualified
domain pack where the universal catalog is insufficient.

## Hardware manufacturing, field service, and recall

Use the six hardware questions as one loop:

1. map the bill of materials, sub-tier suppliers, factories, tooling, firmware
   signers, logistics, and correlated single points of failure;
2. define yield, tolerance, incoming quality, calibration, counterfeit, lot, serial,
   and configuration traceability;
3. require certification, environmental, pre-production, design-transfer, process,
   and production-release evidence;
4. provide safe installation, inspection, maintenance, repairability, spares, tools,
   qualified field service, and records;
5. demonstrate time-bounded identification of affected units, firmware, customers,
   channels, and locations; and
6. pre-authorize production stop, quarantine, correction, recall, communication, and
   remediation funding.

A hardware gate is blocked when a critical component or process is untraceable,
production evidence is incomplete, field service cannot maintain safe operation, an
affected-unit population cannot be found, or protective authority and funding are
missing. Safety-critical hardware requires qualified engineering and regulatory packs.

## Crisis, reputation, and public communication

Use the six crisis questions as one loop:

1. map incident classes to users, staff, customers, partners, regulators, media, and
   public communication thresholds;
2. assign spokesperson, fact approval, correction, deputy, investigation-integrity,
   and urgent-protective authority;
3. test authenticated, accessible, multilingual primary and fallback channels;
4. communicate uncertainty, changing facts, affected scope, user action, and the next
   update time;
5. handle misinformation, impersonation, leaks, and distrust without disproportionate
   surveillance or retaliation; and
6. measure fulfilled duties, remediation, affected-party outcomes, relationship
   repair, and sustained trust recovery.

A crisis gate is blocked when audiences or duties are unknown, approval prevents
urgent protection, channels or authentication are untested, messages omit actionable
uncertainty, corrections cannot propagate, or recovery is asserted without evidence.
A generated statement is a draft, not authorization to publish.

## Liability allocation and insurance

Use the six liability and insurance questions as one loop:

1. map foreseeable losses, claimants, control, duty, jurisdiction, liability, and
   recourse across all parties including affected non-users;
2. compare actual system behavior with warranties, service commitments, limitations,
   indemnities, and bargaining power;
3. map policy scope, limits, exclusions, deductibles, territories, notification,
   security, safety, and cooperation conditions;
4. stress correlated claims, aggregation, exhaustion, common-cause exclusions, and
   insurer or coverage failure;
5. preserve notices, chronology, causation, control, loss, remediation, custody,
   privilege, and cooperation evidence; and
6. quantify residual uncovered loss, identify authorized acceptance, and test
   organizational survivability.

A liability gate is blocked when a material claimant or loss is omitted, contractual
obligations contradict system behavior, relied-on coverage is unverified, a correlated
loss can exceed coverage without contingency, claim evidence will not survive, or
residual loss lacks authorized and survivable disposition.

## Domain-pack escalation

Activate the domain-pack governance process when a question depends on specialized
laws, standards, engineering practices, regulated controls, mandatory scenarios, or
qualified interpretation that the universal catalog cannot supply. Examples include
licensed financial services, medical or safety devices, automotive or aviation
systems, industrial controls, children, government, or other regulated high-impact
uses.

A generic answer must not be upgraded to a domain-qualified claim. Missing qualified
pack content is a blocker, not permission for an agent or maintainer to improvise it.

## Agent use and permissions

An agent can identify likely activation, maintain registers, compare evidence,
construct scenarios, calculate graph impact, prepare tests, and draft decisions. It
must record scope, source, jurisdiction, version, retrieval time, uncertainty,
qualification boundary, and missing evidence.

Separate explicit authorization is required before changing marketplace rules,
blocking participants or transactions, filing or disclosing intellectual property,
making legal or compliance determinations, moving or holding funds, contacting law
enforcement or regulators, stopping production, issuing a recall, publishing crisis
communications, notifying an insurer, accepting liability, or accepting residual
risk.

## Completion and remaining evidence

Publishing these conditional modules closes a structured coverage gap: applicable
projects can now select stable questions with explicit evidence, outputs, ownership,
relationships, and revisit triggers. It does not make the concerns empirically
validated or legally resolved. Representative positive and negative runs, incident or
claim evidence, false-blocker review, calibration, and qualified domain approvals are
still required.
