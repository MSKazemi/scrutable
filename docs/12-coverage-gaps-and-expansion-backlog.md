# Coverage gaps and expansion backlog

**Audit snapshot:** 2026-08-12, Product Questionbook 0.7 on `main`  
**Status:** evidence-based backlog and promotion ledger; published modules remain partial until representative evidence exists  
**Scope:** important omissions in reusable software-product coverage and in the
repository's ability to execute and validate that coverage

## Direct finding

Product Questionbook has broad human-readable coverage: 21 aspects, core and detailed
question banks, human-agent-robot-world integration, financial continuity,
bottlenecks, naming, attraction and distribution, adversarial review, and governed
self-improvement. It does not—and should not claim to—contain every question required
for every product, jurisdiction, industry, or risk class.

The first structural inventory is explicit. The
[prose-to-catalog manifest](../coverage/prose-to-catalog.yaml) accounts for all 396
numbered questions in the seven main human-readable banks: 388 are conservatively
mapped through 43 section-level many-to-many compression groups and eight
naming-brainstorm prompts are guidance-only. It claims zero exact mappings until
independent semantic review. Backlog candidates and unnumbered gates remain outside
that manifest's seven-bank source scope.

The second largest omission remains operational: the repository defines deterministic
validation and assurance behavior but does not contain a callable conformance and
semantic validator or an automated assurance workflow. A CLI, API, database, or
service is optional and is not required for normal framework use.

**Update, 2026-08-13 (v0.8.0):** the *conformance* validator now exists
(`tools/validate.py`) and runs as a required CI check
([ADR-0005](../decisions/ADR-0005-deterministic-conformance-validator.md)). The
*semantic* validator — state transitions, applicability, evidence sufficiency, blocker
policy, and gate correctness — and the automated assurance workflow remain open. The
largest omission is now empirical rather than operational: the framework has never been
run against an external subject.

This promotion adds eight conditional structured modules containing 52 questions for
international operations, enterprise implementation, marketplace and network
governance, intellectual property, financial crime, hardware manufacturing and
recall, crisis communication, and liability and insurance. It closes the stable-record
gap for those candidates. It does not supply project evidence, qualified legal or
professional opinions, or empirical calibration.

## Meaning of coverage

Use these labels consistently:

| Label | Meaning |
|---|---|
| Covered | Explicit questions, applicability, evidence, outputs, ownership, review rules, representative runs, and calibration exist in the human and structured layers |
| Partially covered | A generic, prose, or structured method exists, but evidence, depth, qualified interpretation, representative runs, or decision calibration remains incomplete |
| Missing | No dedicated question or reusable method exists |
| Domain pack required | The universal framework can detect the concern, but qualified domain-specific rules are necessary |
| Capability gap | The method is documented but cannot yet run or verify itself automatically |

A word appearing in a document is not proof that a concern is supported. A question
is not structurally supported by the machine-readable framework until it has a stable
ID, applicability, lifecycle stages, criticality, dependencies and activations,
evidence requirements, expected outputs, accountable roles, revisit triggers, and
validation. Structural support is still not proof of real-world correctness.

## Priority register

| Priority | Gap | Current status | Why it matters |
|---|---|---|---|
| P0 | Prose-to-catalog parity | Partial — manifested, exact review pending | All numbered questions are accounted, but compressed section mappings are not independently reviewed as exact and drift checks are manual |
| P0 | Deterministic conformance validator | **Closed 2026-08-13** | `tools/validate.py` enforces schemas, stable IDs, relationship resolution, acyclicity, coverage fidelity, and links as a required CI check |
| P0 | Semantic validator (state, applicability, evidence, blocker, gate) | Capability gap | Documented guarantees cannot be tested automatically and agent behavior remains dependent on manual discipline |
| P0 | Empirical evidence from a real external run | Capability gap | The framework has never been applied to a project other than itself, so detection rate, false-blocker rate, and calibration are unmeasured |
| P0 | Regulated and safety-critical domain packs | Domain pack required — governance ready | The interface and eight governance nodes are published, but generic questions remain insufficient and no qualified specialized pack exists |
| P1 | Organizational adoption and change management | Partial — structured module published | Eight stable questions cover the change system; representative run and calibration evidence remain absent |
| P1 | Workforce and knowledge continuity | Partial — structured module published | Eight stable questions cover workforce continuity; representative absence, departure, and understaffing evidence remain absent |
| P1 | External sensing and horizon monitoring | Partial — structured method published | Eight stable questions and a source-to-decision method cover sensing; representative monitoring and missed-signal evidence remain absent |
| P1 | Information integrity and content governance | Partial — structured method published | Eight stable questions, a contextual operating method, and a register cover integrity decisions; representative multilingual, manipulation, appeal, reviewer-safety, and propagation evidence remain absent |
| P1 | Geopolitical and regional continuity | Partial — structured method published | Eight stable questions, a people-first operating method, and a register cover exposure and fallback decisions; live qualified legal review and disruption exercises remain absent |
| P1 | Internationalization and localization operations | Partial — structured method published | Eight stable questions, an operating method, and a register now cover locale scope, RTL mechanics, translation governance, local commercial operation, multilingual support, validation, parity, and market exit; qualified local review and representative runs remain absent |
| P1 | Enterprise implementation and customer success | Partial — structured method published | Eight stable questions, an operating method, and a register now cover migration, ownership, time to value, blockers, customer-success roles, value realization, renewal risk, and recovery; representative implementation and renewal evidence remain absent |
| P2 | Ecosystem, marketplace, and network governance | Partial — conditional structured module published | Six stable questions now cover sides, liquidity, cold start, governance, abuse, network effects, and portability; representative marketplace evidence remains absent |
| P2 | Intellectual-property ownership and defensibility | Partial — conditional structured module published | Six stable questions now cover ownership, rights chain, freedom to operate, protection strategy, trade secrets, and defensibility; qualified IP review and observed evidence remain absent |
| P2 | Fraud, payments, and financial crime | Partial — conditional structured module published | Six stable questions now cover abuse, obligations, controls, friction, assurance, and loss allocation; regulated interpretation and representative control evidence remain absent |
| P2 | Hardware manufacturing, field service, and recall | Partial — conditional structured module published | Six stable questions now cover dependencies, quality, production release, field service, recall traceability, and authority; manufacturing and recall exercises remain absent |
| P2 | Crisis, reputation, and public communication | Partial — conditional structured module published | Six stable questions now cover audience scope, authority, channels, changing facts, information integrity, and recovery; representative crisis exercises remain absent |
| P2 | Liability allocation and insurance | Partial — conditional structured module published | Six stable questions now cover liability mapping, contract alignment, insurance scope, correlated loss, claim evidence, and residual liability; actual policy and claim review remain absent |

P2 does not mean unimportant. It means highly consequential when applicable but not
universal. A payment platform, marketplace, medical device, manufactured product, or
public-facing safety system should promote the relevant concerns to P0 for that run.

## Quantified status excluding the validator capability gap

This snapshot excludes item 2, the deterministic validator. It measures the other
backlog items against the expansion branch rather than treating a prose mention as
structured support.

| Metric | Current value |
|---|---:|
| Gap areas excluding item 2 | 15 |
| Candidate questions in those areas | 108 |
| Candidate questions promoted as dedicated published catalog records | 100 |
| Partially covered gap areas | 14 |
| Missing or domain-pack-required gap areas | 1 |
| P0 areas / candidate questions | 2 / 16 |
| P1 areas / candidate questions | 7 / 56 |
| P2 areas / candidate questions | 6 / 36 |
| Reusable catalog after promotion | 199 questions / 794 `depends_on` and `activates` references |
| All declared relationship references after promotion | 1,009 |
| Expert-reviewed regulated or safety-critical packs | 0 |
| Prose-to-catalog coverage manifest | present: 396 numbered questions, 43 groups, 388 compressed, 8 guidance-only, 0 exact |

One hundred of the 108 candidates now have dedicated stable records: domain-pack
governance, organizational change, workforce continuity, external sensing,
information integrity, geopolitical continuity, internationalization and
localization, enterprise implementation, and all six conditional P2 modules. The
domain-pack governance records do not constitute a qualified pack, and every
operational module still needs representative run and calibration evidence. The eight
prose-to-catalog parity candidates remain unpromoted as dedicated question records
because their purpose is manifest and validator governance rather than another
compressed catalog layer.

| Item | Gap | Priority | Candidate questions | Current status | Published structured coverage | What is still absent |
|---:|---|---|---:|---|---|---|
| 1 | Prose-to-catalog parity | P0 | 8 | Partial — manifested | The coverage manifest accounts for 396 numbered questions and preserves source wording against referenced stable IDs | Exact question-level semantic review, unnumbered gate coverage, deterministic drift validation, and callable enforcement remain |
| 3 | Regulated and safety-critical domain packs | P0 | 8 | Domain pack required — governance ready | `core.domain-pack.001` through `.008` define activation, authority, expert review, domain deltas, provenance, blockers, scenario assurance, and affected-run reopening | No qualified healthcare, fintech, children, government, aviation, automotive, industrial-control, or comparable pack has completed this contract |
| 4 | Organizational adoption and change management | P1 | 8 | Partial — structured module published | `team.change-impact.001` through `team.change-ownership.001`, activated by `business.adoption.001` | Representative adoption, rollback, missed-concern, false-blocker, evidence-cost, and outcome-calibration cases remain absent |
| 5 | Workforce and knowledge continuity | P1 | 8 | Partial — structured module published | `team.continuity-dependencies.001` through `team.continuity-signals.001`, activated by `team.capability.001` | Absence, departure, understaffing, supplier-exit, false-blocker, and recovery exercises remain unobserved |
| 6 | External sensing and horizon monitoring | P1 | 8 | Partial — structured method published | `operations.sensing-change.001` through `operations.sensing-blind-spots.001`, activated by `core.assumptions.001` | Representative monitoring, access-failure, false-alert, missed-signal, latency, and outcome evidence remain absent |
| 7 | Information integrity and content governance | P1 | 8 | Partial — structured method published | `ethics.integrity-content.001` through `ethics.integrity-propagation.001`, activated by `ethics.harms.001` | Representative multilingual policy, deepfake and coordination, privacy-proportionality, appeal, reviewer-safety, transparency, and downstream correction cases remain unobserved |
| 8 | Geopolitical and regional continuity | P1 | 8 | Partial — structured method published | `operations.regional-exposure.001` through `operations.regional-fallback-risks.001`, activated by `business.continuity.001` | Current qualified legal interpretations, people-protection exercises, correlated disruption, relocation, false-alert, and fallback-impact evidence remain absent |
| 9 | Internationalization and localization operations | P1 | 8 | Partial — structured method published | `operations.localization-scope.001` through `operations.market-exit.001`, activated by `core.boundary.001`, plus the international operations method and register | Representative RTL, locale mechanics, translation release, local commercial, multilingual support, incident, parity, and exit cases plus qualified local review remain absent |
| 10 | Enterprise implementation and customer success | P1 | 8 | Partial — structured method published | `business.implementation-dependencies.001` through `business.implementation-recovery.001`, activated by `business.organizational-buying.001`, plus the enterprise method and register | Successful and failed migration, rollout, time-to-value, adoption, recovery, renewal, false-signal, and outcome-calibration evidence remain absent |
| 11 | Ecosystem, marketplace, and network governance | P2 | 6 | Partial — conditional structured module published | `business.marketplace-sides.001` through `business.marketplace-portability.001`, activated by `business.channels.001` | Representative liquidity, cold-start, governance, appeal, collusion, exclusion, concentration, and portability cases remain absent |
| 12 | Intellectual-property ownership and defensibility | P2 | 6 | Partial — conditional structured module published | `legal.ip-ownership.001` through `legal.ip-defensibility.001`, activated by `legal.obligations.001` | Qualified chain-of-title, freedom-to-operate, strategy, trade-secret, enforcement-cost, and observed-defensibility evidence remain absent |
| 13 | Fraud, payments, and financial crime | P2 | 6 | Partial — conditional structured module published | `security.financial-abuse.001` through `security.financial-loss-allocation.001`, activated by `security.threats.001` and relevant market or marketplace findings | Qualified regulated interpretation, adversarial controls, investigation, appeals, reviewer safety, loss, reserves, and processor evidence remain absent |
| 14 | Hardware manufacturing, field service, and recall | P2 | 6 | Partial — conditional structured module published | `operations.manufacturing-dependencies.001` through `operations.recall-authority.001`, activated by `architecture.context.001` | Production, supplier, yield, certification, field-service, traceability, mock-recall, stop-authority, and remediation evidence remain absent |
| 15 | Crisis, reputation, and public communication | P2 | 6 | Partial — conditional structured module published | `operations.crisis-scope.001` through `operations.crisis-recovery.001`, activated by `operations.incident.001` and relevant locale or recall findings | Time-pressured authority, fallback channel, changing-fact, misinformation, correction, multilingual, and trust-recovery exercises remain absent |
| 16 | Liability allocation and insurance | P2 | 6 | Partial — conditional structured module published | `legal.liability-map.001` through `legal.residual-liability.001`, activated by `legal.obligations.001` and relevant commercial, IP, financial, or recall findings | Qualified contract and policy interpretation, correlated-loss stress, claim evidence, insurer response, reserve, and survivability evidence remain absent |

### Interpretation

- **Highest structural assurance priority:** item 2. The manifest and new modules
  expose more inventory, but schema, semantic, link, and drift rules are not
  continuously enforced by a deterministic validator.
- **Highest safety priority:** item 3. Generic questions should activate a qualified
  pack or block a domain-qualified claim; the universal framework must not impersonate
  clinical, legal, financial, aviation, automotive, manufacturing, insurance, or
  industrial-control expertise.
- **Highest new operational validation priorities:** items 9 and 10. Their P1 methods
  now exist, but international market readiness and enterprise value claims still
  require representative end-to-end evidence.
- **Conditional promotion rule:** items 11 through 16 are now structurally published,
  but should load only when applicable. A global P2 label never delays a P0 concern in
  a specific run.
- **Unresolved side effect:** 40 of the 52 promoted records are `critical`, so 196 of
  199 catalog questions are now high or critical. This does not relieve the
  criticality-inflation finding recorded as QA-05 in the
  [quality assurance audit](13-quality-assurance-audit-and-roadmap.md). The
  `applies_when` boundary limits how often the new records load, but severity still
  needs calibration against observed decision impact.

The backlog status changes only after the promotion checklist in this document passes.
Adding another paragraph, prompt, or question does not change a gap from partial to
covered.

## P0 questions

### 1. Prose-to-catalog parity

1. Which numbered Markdown questions have a stable catalog ID, and which are
   intentionally guidance-only?
2. Where does one stable question represent several prose questions, and is that
   compression documented without losing failure modes?
3. Which of the 21 human-readable aspects have weak or absent representation in the
   16 structured domains?
4. Are the integration `I1-I20`, funding `F1-F13`, bottleneck `B1-B10`, naming,
   and release-blocker questions mapped to stable nodes?
5. Does every critical prose concern define applicability, evidence, outputs, roles,
   dependencies, activations, and revisit triggers?
6. Does validation fail when a published prose question is unmapped, an ID is
   duplicated, or a relationship target is missing?
7. Can a coverage report distinguish “not applicable,” “not yet modeled,”
   “unanswered,” “unsupported by evidence,” and “accepted risk”?
8. Which source is authoritative when prose and catalog meaning diverge?

### 2. Deterministic conformance and semantic validator

1. What callable validator accepts a repository or run snapshot pinned to a
   Questionbook revision, whether invoked by CI, an agent, a library, or an optional
   thin command wrapper?
2. Does it parse and validate every catalog, instance, answer, relationship, and run
   record against its schema?
3. Does it deterministically evaluate applicability, dependencies, activations,
   contradictions, stale evidence, reverse-dependency invalidation, and strongly
   connected components?
4. Can the same frozen input produce the same graph, gate result, and output package?
5. Are blocker and approval rules enforced outside the language model?
6. Which scenario, property, migration, security, and regression tests prove the
   state machine and convergence rules?
7. Can permission-aware adapters retrieve evidence and write only authorized paths
   while preserving provenance and an auditable diff?
8. What evaluation measures missed concerns, false blockers, calibration,
   decision-change rate, and time to justified decision?

### 3. Domain-pack governance

1. Which subject attributes activate a regulated or safety-critical pack?
2. Which authoritative laws, standards, clinical or engineering practices, and
   jurisdictional interpretations does the pack depend on?
3. Who is qualified and accountable to approve the pack and accept residual risk?
4. Which domain hazards and required evidence are not represented by the universal
   catalog?
5. How are sources, effective dates, jurisdictions, versions, conflicts, and expiry
   recorded?
6. Which pack questions are mandatory blockers, and which allow documented
   equivalence or risk acceptance?
7. How is the pack tested against real incidents, audits, recalls, enforcement
   actions, and expert review?
8. How are existing runs reopened when a pack or its authority changes?

**Current status:** the [governance contract](17-domain-pack-governance.md), manifest
schema, draft template, and `core.domain-pack.001` through `.008` implement these
eight universal governance questions. Expert-reviewed published packs remain at zero;
any run needing one must pause or stop until a qualified pack exists.

## P1 questions

### 4. Organizational adoption and change management

**Current status:** `team.change-impact.001` through `team.change-ownership.001`
implement these eight questions and `business.adoption.001` activates the module. It
remains partial until representative runs test rollback, missed concerns, evidence
cost, false blockers, and outcome calibration.

1. Whose workflow, authority, incentives, workload, status, or professional identity
   must change for the product to succeed?
2. Who benefits from the change, who bears its cost, and who can quietly resist or
   block it?
3. Which training, practice, certification, job aids, champions, and manager support
   are required before responsibility transfers?
4. What migration, parallel-run, cutover, fallback, and productivity-trough plan
   protects users and operations?
5. Which labor, works-council, union, consultation, or employee-monitoring obligations
   apply?
6. How will readiness, real adoption, workaround use, proficiency, and change fatigue
   be measured?
7. What threshold pauses rollout or restores the former workflow?
8. Who owns adoption after launch rather than only software delivery?

### 5. Workforce and knowledge continuity

**Current status:** `team.continuity-dependencies.001` through
`team.continuity-signals.001` implement these eight questions and
`team.capability.001` activates the module. It remains partial until exercises
demonstrate transfer, secure departure, minimum operation, separation of duties,
supplier exit, and useful leading indicators.

1. Which outcomes, systems, approvals, and relationships depend on one person or a
   fragile group?
2. What succession, cross-training, documentation, shadowing, and access-transfer plan
   reduces key-person risk?
3. How do hiring lead time, turnover, contractor dependence, leave, burnout, and
   on-call load affect the critical path and minimum viable operation?
4. Are incentives and performance measures encouraging hidden risk, metric gaming,
   silence, or unsafe speed?
5. Can departures revoke access promptly without losing essential knowledge or
   operational authority?
6. Is separation of duties preserved during understaffing and emergencies?
7. Which skills must remain internal, and which may safely depend on suppliers?
8. What leading indicators show team capacity or knowledge continuity is failing?

### 6. External sensing and horizon monitoring

**Current status:** `operations.sensing-change.001` through
`operations.sensing-blind-spots.001` implement these eight questions,
`core.assumptions.001` activates the module, and
[the sensing contract](18-external-sensing-and-attention.md) defines the operating
loop. It remains partial until representative runs exercise source loss,
corroboration, thresholds, latency, missed signals, and blind spots.

1. Which external changes could invalidate value, legality, safety, security,
   economics, distribution, or technical feasibility?
2. Which authoritative sources, telemetry, suppliers, communities, customers,
   regulators, standards bodies, and news signals reveal each change?
3. Who monitors each signal, at what cadence, and how is source reliability assessed?
4. Which threshold creates an alert, reopens graph nodes, triggers a decision, or
   invokes a contingency?
5. How are weak signals distinguished from noise and correlated evidence?
6. What is the maximum tolerable delay from external change to internal action?
7. Can a missed or late signal be reconstructed and learned from?
8. Which dependencies have no observable early-warning signal?

### 7. Information integrity and content governance

**Current status:** `ethics.integrity-content.001` through
`ethics.integrity-propagation.001` implement these eight questions,
`ethics.harms.001` activates the module, and the
[content-governance method](20-information-integrity-and-content-governance.md) plus
integrity register define the operating loop. It remains partial until representative
runs exercise multilingual and contextual rules, manipulation and evasion,
proportionality, appeal and correction, reviewer safety, transparency, and downstream
agents.

1. Which user, generated, imported, or synthetic content can mislead, impersonate,
   defame, manipulate, or cause material harm?
2. What provenance, authenticity, labeling, watermarking, source citation, or chain of
   custody is required?
3. What content rules apply across languages, cultures, contexts, private spaces, and
   public distribution?
4. How will coordinated manipulation, spam, deepfakes, brigading, and evasion be
   detected without creating disproportionate surveillance?
5. What human review, escalation, appeal, correction, notice, and restoration process
   applies?
6. How are false positives, false negatives, reviewer safety, consistency, and bias
   measured?
7. What transparency and researcher or regulator access is appropriate?
8. How will removed, corrected, disputed, or time-sensitive information propagate to
   downstream systems and agents?

### 8. Geopolitical and regional continuity

**Current status:** `operations.regional-exposure.001` through
`operations.regional-fallback-risks.001` implement these eight questions,
`business.continuity.001` activates the module, and the
[regional continuity method](21-geopolitical-and-regional-continuity.md) plus register
define the operating loop. It remains partial until current qualified legal reviews
and representative conflict, shutdown, banking, currency, people-protection,
asset-access, relocation, false-alert, and fallback-risk cases provide evidence.

1. Which countries, regions, currencies, networks, cloud regions, suppliers, staff,
   and customers create concentrated exposure?
2. Which sanctions, export controls, import rules, ownership restrictions, data
   localization, or government-access obligations apply?
3. What happens during conflict, civil disruption, internet shutdown, border closure,
   banking restriction, currency control, or abrupt regulatory action?
4. Can essential operations move legally and safely to another region, supplier,
   payment path, or operating entity?
5. How will affected staff, users, contractors, and partners be protected and
   communicated with?
6. Which contracts, data, licenses, hardware, or funds could become inaccessible?
7. What early signals and decision thresholds trigger diversification, suspension,
   evacuation, or exit?
8. Which fallback creates new legal, ethical, security, or human-rights risks?

### 9. Internationalization and localization operations

**Current status:** `operations.localization-scope.001` through
`operations.market-exit.001` implement these eight questions,
`core.boundary.001` activates the module, and the
[international operations method](22-internationalization-and-localization-operations.md)
plus localization readiness register define the operating loop. It remains partial
until representative locale, market, translation, commercial, support, incident,
parity, and exit evidence plus current qualified local review are available.

1. Which markets require translation, localization, transcreation, or a redesigned
   workflow rather than translated strings?
2. Do right-to-left scripts, input methods, fonts, sorting, search, names, addresses,
   calendars, units, and text expansion work end to end?
3. Who owns terminology, translation memory, review, release synchronization, and
   correction quality?
4. Which local laws, prices, taxes, payment methods, identity methods, and contractual
   terms change the product?
5. Can support, incident response, safety communication, and escalation operate in
   the required language and time zone?
6. Have local users tested comprehension, trust, accessibility, and cultural fit in
   realistic conditions?
7. How are locale-specific defects and missing parity measured and prioritized?
8. Can a market be paused or exited without abandoning users or obligations?

### 10. Enterprise implementation and customer success

**Current status:** `business.implementation-dependencies.001` through
`business.implementation-recovery.001` implement these eight questions,
`business.organizational-buying.001` activates the module, and the
[enterprise implementation method](23-enterprise-implementation-and-customer-success.md)
plus implementation register define the operating loop. It remains partial until
representative successful and failed implementations, recoveries, value outcomes,
false signals, and renewals calibrate the method.

1. What must the customer configure, migrate, integrate, clean, approve, and change
   before first value?
2. Who owns each implementation dependency on the provider and customer sides?
3. What time-to-first-value target, implementation milestones, acceptance evidence,
   and escalation rules apply?
4. Which identity, provisioning, audit, security-review, data-processing,
   accessibility, and procurement requirements repeatedly block rollout?
5. Are an operational champion, executive sponsor, administrator, support path, and
   renewal owner present?
6. How will actual workflow adoption and value realization be distinguished from
   license activation?
7. Which signals predict stalled implementation, shelfware, churn, downsell, or failed
   renewal?
8. What recovery or exit plan applies when implementation cannot meet the promised
   outcome?

## P2 conditional questions

The six sections below share the
[conditional operating method](24-conditional-marketplace-ip-financial-hardware-crisis-liability.md)
and [conditional risk register](../templates/conditional-risk-register.md). Their
catalog publication does not make them universal; record applicability and promote
them to the run's required criticality.

### 11. Ecosystem, marketplace, and network governance

**Current status:** `business.marketplace-sides.001` through
`business.marketplace-portability.001` implement these six questions and
`business.channels.001` activates the module. It remains partial until representative
liquidity, cold-start, rule, appeal, abuse, concentration, exclusion, and portability
cases provide evidence.

1. Which sides must participate, and what minimum liquidity or matching quality makes
   the system useful?
2. How will the cold-start problem be tested without fabricating demand or supply?
3. Which rules govern ranking, access, fees, quality, disputes, suspension, and appeal?
4. How are fraud, collusion, adverse selection, disintermediation, and power imbalance
   controlled?
5. Do network effects create durable value, lock-in, concentration, or unacceptable
   exclusion?
6. Can participants export reputation, history, assets, and relationships when they
   leave?

### 12. Intellectual-property ownership and defensibility

**Current status:** `legal.ip-ownership.001` through
`legal.ip-defensibility.001` implement these six questions and
`legal.obligations.001` activates the module. It remains partial until qualified
ownership, rights-chain, freedom-to-operate, strategy, trade-secret, and observed
defensibility evidence exists.

1. Who owns inventions, code, data, content, models, prompts, designs, and improvements
   created by employees, contractors, partners, users, and agents?
2. Are assignments, contributor terms, open-source obligations, and third-party rights
   complete and compatible?
3. Does freedom-to-operate evidence identify material patent, copyright, database,
   trade-secret, or publicity-right risk?
4. Which knowledge should be patented, published defensively, kept secret, or shared?
5. Can confidentiality and trade-secret controls survive collaboration, support,
   telemetry, and model use?
6. Is claimed defensibility supported by evidence rather than merely by complexity or
   first-mover language?

### 13. Fraud, payments, and financial crime

**Current status:** `security.financial-abuse.001` through
`security.financial-loss-allocation.001` implement these six questions and
`security.threats.001`, local commercial findings, or marketplace abuse can activate
the module. It remains partial until qualified regulated interpretation and
representative prevention, investigation, appeal, workload, loss, and reserve evidence
exists.

1. Which money, credit, refund, promotion, identity, account, or marketplace flows can
   be abused, and what is the maximum credible loss?
2. Which KYC, AML, sanctions-screening, reporting, tax, licensing, safeguarding, and
   recordkeeping duties apply?
3. How will account takeover, synthetic identity, stolen instruments, chargebacks,
   refund abuse, collusion, and laundering be prevented and investigated?
4. What transaction limits, holds, reserves, step-up checks, and manual reviews are
   proportionate?
5. How are false positives, appeals, bias, customer harm, and reviewer workload
   measured?
6. Who bears each loss contractually and economically, and is capital reserved for it?

### 14. Hardware manufacturing, field service, and recall

**Current status:** `operations.manufacturing-dependencies.001` through
`operations.recall-authority.001` implement these six questions and
`architecture.context.001` activates the module. It remains partial until qualified
production, certification, field-service, mock-recall, stop-authority, and remediation
exercises provide evidence.

1. Which bill-of-materials items, factories, tools, firmware signers, logistics
   providers, and sub-tier suppliers are single points of failure?
2. What yield, tolerance, traceability, counterfeit, calibration, and incoming-quality
   thresholds apply?
3. Which certifications, environmental tests, pre-production validations, and
   production-release evidence are required?
4. How are installation, inspection, maintenance, repairability, spare parts, and
   field-service competence managed?
5. Can affected serial numbers, firmware versions, customers, and locations be found
   quickly during a safety action or recall?
6. Who can stop production, quarantine inventory, issue a recall, and fund remediation?

### 15. Crisis, reputation, and public communication

**Current status:** `operations.crisis-scope.001` through
`operations.crisis-recovery.001` implement these six questions and
`operations.incident.001`, multilingual support, or recall findings can activate the
module. It remains partial until time-pressured authority, fallback-channel,
changing-fact, misinformation, correction, multilingual, and recovery exercises
provide evidence.

1. Which incidents require communication to users, staff, customers, partners,
   regulators, media, or the public?
2. Who is authorized to speak, approve facts, correct errors, and protect
   investigation integrity?
3. Which channels and prepared fallbacks work when normal systems or accounts are
   unavailable?
4. How will uncertainty, changing facts, affected scope, user action, and next update
   time be communicated?
5. How will misinformation, impersonation, leaks, and stakeholder distrust during the
   crisis be handled?
6. What evidence shows that trust, obligations, and harmed relationships are actually
   recovering?

### 16. Liability allocation and insurance

**Current status:** `legal.liability-map.001` through
`legal.residual-liability.001` implement these six questions and
`legal.obligations.001` plus relevant local commercial, IP, financial-loss, or recall
findings can activate the module. It remains partial until qualified contract and
policy review, correlated-loss stress, claim evidence, insurer response, reserve, and
survivability evidence exists.

1. Which party is liable for each foreseeable loss across customers, users, suppliers,
   agents, operators, and affected non-users?
2. Do warranties, limitations, indemnities, service commitments, and insurance align
   with real system behavior and bargaining power?
3. Which policies, limits, exclusions, deductibles, territories, notification duties,
   and security or safety conditions apply?
4. Could one correlated event exceed coverage or make coverage unavailable?
5. What evidence must be preserved to defend a claim or recover under a policy?
6. What residual loss remains, who accepts it, and can the organization survive it?

## Areas that are already explicit

Do not duplicate these as “missing” without identifying a narrower failure mechanism:

- human, organization, agent, robot, device, platform, and physical-world integration;
- funding, burn, runway, financial concentration, continuity, and shutdown;
- end-to-end bottlenecks, critical paths, leading signals, owners, and fallbacks;
- naming, search collision, discoverability, reputation, and legal checks;
- qualified attention, advertising incrementality, retention, referral, earned media,
  machine discovery, procurement, and distribution concentration;
- AI uncertainty, human review, prompt injection, model drift, traceability, fallback,
  multi-agent coordination, delegated authority, and safe stopping;
- adversarial review, pivot lineage, kill criteria, prediction error, and governed
  framework self-improvement.

## Promotion rules

A backlog area becomes structurally supported only when:

1. its applicability boundary prevents irrelevant universal questioning;
2. stable YAML questions are added without repurposing published IDs;
3. dependencies, activations, lifecycle stages, evidence, outputs, roles, and revisit
   triggers are complete;
4. critical blockers and allowed risk-acceptance authorities are defined;
5. prose, catalog, templates, schemas, examples, and navigation remain consistent;
6. validation checks IDs, relationships, schemas, links, and representative positive
   and negative scenarios;
7. a maintainer reviews the change and the changelog records it.

An area becomes **covered** only after the structural promotion is also tested against
representative real cases, missed concerns, false blockers, evidence cost, decision
change, calibration, and outcomes, with qualified review where required.

## Recommended sequence

1. Implement and test the read-only conformance validator, state-policy checks, gate
   policy, relationship resolution, link checks, and backlog-promotion drift checks
   without making a CLI or service mandatory.
2. Independently review compressed prose mappings and account for unnumbered gate
   concerns.
3. Validate the organizational-change, workforce-continuity, external-sensing,
   information-integrity, geopolitical-continuity, internationalization, and
   enterprise-implementation methods on representative positive and negative runs.
4. Validate each applicable conditional marketplace, IP, financial-crime, hardware,
   crisis, and liability module against qualified real scenarios; promote it to the
   run's P0 set when consequences require it.
5. Pilot at least one high-value specialized pack through the domain-pack interface
   with qualified expert review; do not mark that gap covered until the exact pack and
   scope are published and tested.
6. Use observed prediction error, missed concerns, false blockers, evidence cost, and
   decision outcomes to revise the framework through governed change.

This sequence preserves the framework's central distinction: a useful question written
somewhere is not the same as proving that the right project was asked it, answered it
with qualified evidence, propagated the result, and blocked unsafe progress when
necessary.
