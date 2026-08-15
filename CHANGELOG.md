# Changelog

Material framework changes are recorded here. Dates use `YYYY-MM-DD`.

## Unreleased

_Nothing yet._

## 0.9.0 — 2026-08-15

Renames the framework. The only behavioural change is to the artifact contract identifiers;
the catalog, graph, schemas, and gate vocabulary are untouched.

### Changed — BREAKING

- **Renamed the framework from Product Questionbook to Scrutable**, and the repository from
  `MSKazemi/mohsen` to `MSKazemi/scrutable`. Rationale, candidate evidence, and limitations in
  [ADR-0007](decisions/ADR-0007-rename-to-scrutable.md), which supersedes
  [the 2026-08-11 naming decision](decisions/0001-product-questionbook-name.md).

  The previous name was legally and technically clear but could not win branded search: the
  engine rewrites `questionbook` to `question book`, and — tested on 2026-08-15 — even the
  category-qualified compound `questionbook framework github` returned 10/10 question-bank and
  QA-system repositories. That is a *competing* result space, not an inert one. `Scrutable`
  survives quoted search unrewritten and has no commercial owner.

  Old repository URLs redirect and repository identity is preserved, so existing clones keep
  working; update the remote with
  `git remote set-url origin git@github.com:MSKazemi/scrutable.git`.

- **Artifact contract identifiers renamed.** Consumers of run packages must update:

  | Before | After |
  | --- | --- |
  | `questionbook_ref` | `scrutable_ref` |
  | `.questionbook/` (run-package directory) | `.scrutable/` |
  | `schema_version: questionbook-run/v0.1` | `schema_version: scrutable-run/v0.1` |

  Taken now deliberately: the framework had been public for two days, so the switching cost is
  at its lifetime minimum (`docs/07` Q59).

- The historical naming decision and the CHANGELOG entries recording the previous name are
  left unaltered as evidence. The dated audit snapshots in `docs/13`, `docs/15`, and `docs/19`
  carry a note recording that the rename happened after their audit date.

## 0.8.0 — 2026-08-13

Closes the conformance half of the controlling bottleneck identified in
`docs/13-quality-assurance-audit-and-roadmap.md`, and adds the licensing and governance
files that public reuse requires. Triggered by the framework's first self-assessment
run, which returned `pause` on three blockers.

### Added

- **`LICENSE` (Apache-2.0)** and `NOTICE`. The repository previously had no license, so
  publishing it would have granted no reuse rights at all — a fatal gap for a framework
  whose purpose is reuse. Rationale and alternatives in
  [ADR-0004](decisions/ADR-0004-apache-2-0-licensing.md).
- **`tools/validate.py`** — a deterministic, offline conformance validator, plus
  `tools/requirements.txt` and a `Makefile` (`make validate`, `make report`,
  `make check`). It checks catalog parsing and stable-ID uniqueness, JSON Schema
  well-formedness, question-schema conformance, relationship-target resolution,
  `depends_on` acyclicity, status hygiene, prose-to-catalog coverage fidelity, worked-
  example validity, Markdown link and anchor resolution, gate-vocabulary consistency,
  and a criticality-calibration report. Verified red-green: four injected defects
  produced six failures; reverting them returned zero.
- **`.github/workflows/validate.yml`** — required CI on push, pull request, and manual
  dispatch, publishing a machine-readable conformance report artifact. This is the
  "required CI report for the pinned commit" that assurance level **A1** demands, so an
  A1 claim is now supportable for any revision with a green run.
  [ADR-0005](decisions/ADR-0005-deterministic-conformance-validator.md).
- **`SECURITY.md`** with a private reporting path, an explicit in-scope/out-of-scope
  boundary, honest single-maintainer response targets, and a rule against writing secret
  material into a run package.
- **`CODE_OF_CONDUCT.md`** and **`CITATION.cff`**.
- A **scope-boundary statement in `README.md`**: no qualified domain pack is published,
  so a run whose subject involves healthcare, financial services, children, government,
  automotive, aviation, or industrial control will correctly block at
  `core.domain-pack.001`. The behaviour already existed; it was undeclared.
- A `README.md` section covering how to run the validator and what its green result does
  and does not claim.

### Changed

- **`criticality` is now documented as advisory**, not the run-time ranking input. 196 of
  199 published questions are `high` or `critical` and none is `low`, so the field cannot
  order a ready frontier; `docs/prioritization.md` already ranked by run-time impact,
  uncertainty, unlock value, urgency, and cost, but nothing said so. Documented in
  `schemas/question.schema.json` and `docs/prioritization.md`, and reported by validator
  check `Q1`. No catalog content or stable ID changed.
  [ADR-0006](decisions/ADR-0006-criticality-is-advisory.md).
- `coverage/prose-to-catalog.yaml` `source_revision` refreshed to `a80c9653` and
  documented as provenance only — correctness is now enforced by re-deriving all 396
  entries from the prose at the working revision, so drift fails CI instead of hiding
  behind a stale SHA.
- `ai-context.yaml` now declares `automated_validator_available: true` with the command,
  its structure-only scope, and an explicit list of what it cannot check;
  `semantic_validator_available` remains `false`.
- `AGENTS.md`, `docs/11`, `docs/14`, and `docs/25` updated to reflect that the
  conformance validator exists. `docs/14`'s P1 validator item is marked done; the next
  controlling improvement is recorded as empirical, not structural.
- `CONTRIBUTING.md` now requires a validator run before a pull request, states the
  contribution license, and records the catalog freeze.

### Known limitations

- **The catalog is frozen at 199 questions** until the framework has been run against an
  external subject. It has never been.
- The validator checks **structure only**. A2 (semantic enforcement), A3 (empirical
  calibration), A4 (domain qualification), and A5 (outcome monitoring) remain unclaimed
  and unmet.
- `packs/` still contains no published domain pack, and qualified expert review remains
  unfunded.
- `docs/13` and `docs/19` remain pinned point-in-time audits at baseline `b2c5bd2` and
  were deliberately not amended.

## 0.7.1 — 2026-08-12

- Promoted 52 backlog candidates into eight conditional published catalog modules for internationalization and localization operations, enterprise implementation and customer success, marketplace and network governance, intellectual property, fraud and financial crime, hardware manufacturing and recall, crisis communication, and liability and insurance.
- Added three operating methods, three evidence registers, and an expansion integration audit; connected the modules to existing boundary, organizational-buying, channel, obligation, threat, architecture-context, and incident anchors while preserving conditional applicability and qualified-review boundaries.
- Expanded the universal catalog to 199 unique published questions with 496 `depends_on`, 298 `activates`, 213 `related_to`, and two `refines` references. All 1,009 declared targets are required to resolve and the dependency graph remains acyclic.
- Increased promoted expansion-backlog candidates from 48 to 100 of 108 while retaining honest partial status until representative runs, missed-concern and false-blocker review, calibration, qualified legal or professional evidence, and observed outcomes exist. The deterministic conformance validator remains a separate P0 capability gap.
- Added eight stable geopolitical and regional continuity questions covering correlated exposure, sanctions and export obligations, disruption, lawful relocation, people protection, asset access, early decision thresholds, and fallback-created legal, ethical, security, labor, environmental, and human-rights risks.
- Added the people-first regional continuity method and register, and connected `business.continuity.001` to the module; the universal catalog now contains 147 unique published questions, 323 `depends_on`, 205 `activates`, 98 `related_to`, and two `refines` references. All 628 targets resolve and the dependency graph remains acyclic.
- Reduced missing or domain-pack-required backlog areas from two to one while retaining an honest partial status until current qualified legal review and representative disruption, relocation, people-protection, asset-access, and fallback exercises provide evidence.

- Added eight stable information-integrity and content-governance questions covering contextual content harm, provenance without truth conflation, multilingual policy, coordinated manipulation and proportionality, review and appeal, reviewer safety and assurance, transparency, and downstream correction to systems and agents.
- Added the contextual content-governance method and content-integrity register, and connected `ethics.harms.001` to the module; the universal catalog now contains 139 unique published questions, 301 `depends_on`, 188 `activates`, 77 `related_to`, and two `refines` references. All 568 targets resolve and the dependency graph remains acyclic.
- Kept the gap status honestly partial until representative multilingual, deepfake and coordination, privacy-proportionality, appeal, reviewer-safety, transparency, and downstream propagation cases provide evidence.

- Completed a line-by-line semantic and deterministic integration audit of all 92
  files in baseline commit `b2c5bd2`; recorded the method, per-file disposition,
  corrections, validation results, branch state, and residual risks in
  `docs/19-whole-repository-integration-audit.md`.
- Reconciled the canonical run layout, answer example, lifecycle and coverage
  vocabularies, scoring-policy names, accepted-risk semantics, subject types,
  generated-artifact metadata, domain-pack approval semantics, schema counts, link
  counts, and merged-branch history.
- Preserved the text-first boundary: the next automation is a callable read-only
  conformance and semantic validator; a CLI, API, database, or service remains
  optional.

- Added eight stable external-sensing questions and a source-to-decision operating
  method covering change classes, sources from people, companies, authorities, agents,
  web and news, monitoring ownership, corroboration, thresholds, detection latency,
  missed-signal review, and blind spots.
- Added a reusable external signal register and connected `core.assumptions.001` to
  the sensing module; the universal catalog now contains 131 unique published
  questions, 278 `depends_on`, 172 `activates`, 58 `related_to`, and two `refines`
  references.
- Defined the honest guarantee: the framework can make the sensing process and its
  blind spots visible, but cannot guarantee complete knowledge, continuous
  monitoring, audience visibility, attention, or response.

- Added eight stable workforce-continuity questions covering concentrated human
  dependencies, succession and demonstrated transfer, sustainable capacity, unsafe
  incentives, secure departure, separation of duties under shortage, capability
  sourcing, and leading indicators.
- Connected `team.capability.001` to the new module and expanded the universal catalog
  to 123 unique published questions, 262 `depends_on`, 159 `activates`, 41
  `related_to`, and two `refines` references; all targets resolve and dependencies
  remain acyclic.
- Changed the workforce-continuity gap to “structured module published” while
  retaining an honest `partial` status until absence, departure, understaffing,
  supplier-exit, and recovery exercises produce evidence.

- Added eight stable organizational-change questions covering affected workflows and
  authority, uneven benefit and resistance, training and proficiency, migration and
  fallback, workforce obligations, adoption and fatigue measurement, pause or
  restoration thresholds, and post-launch ownership.
- Connected `business.adoption.001` to the new module and expanded the universal
  catalog to 115 unique published questions, 242 `depends_on`, 145 `activates`, 27
  `related_to`, and two `refines` references; all targets resolve and dependencies
  remain acyclic.
- Changed the adoption gap to “structured module published” while retaining an honest
  `partial` status until representative runs test rollback, missed concerns, evidence
  cost, and false blockers.

- Added the domain-pack governance contract, JSON Schema, draft manifest, directory
  boundary, and eight stable `core.domain-pack.001`–`.008` questions covering
  activation, authorities, qualified approval, domain deltas, provenance, blockers
  and waivers, scenario assurance, and affected-run reopening.
- Made required-but-unavailable, unpublished, expired, suspended, and out-of-scope
  packs explicit blockers; no expert-reviewed specialized pack is claimed, and the
  published-pack count remains zero pending qualified review.
- Expanded the universal catalog to 107 unique published questions, 224
  `depends_on`, 132 `activates`, 13 `related_to`, and two `refines` references, with
  all targets required to resolve.

- Added a machine-readable prose-to-catalog coverage manifest and schema accounting for all 396 numbered questions in the seven main human-readable banks: 388 conservatively compressed through 43 section mappings, eight guidance-only naming prompts, zero exact mappings claimed, and complete preserved source wording.
- Updated catalog, AI context, backlog, quality audit, and navigation so compressed coverage cannot be mistaken for exact semantic parity; unnumbered gates, backlog candidates, independent semantic review, and automated drift enforcement remain explicit work.

- Accepted a text-first, agent-native architecture: versioned Markdown and YAML remain the normal human and agent interface, while a deterministic validator is optional support rather than the product.
- Deferred the proposed full CLI/API/database engine stack until measured multi-user or integration needs justify it; a CLI may remain a thin convenience wrapper over validation logic.
- Aligned the machine, convergence, usage, usability, quality, readiness, quick-start, and agent contracts with the text-first boundary.

- Added a quantified status snapshot for all 15 coverage gaps outside the validator
  capability item: 108 candidate questions, 13 partially covered areas, two
  missing or domain-pack-required areas, eight domain-governance promotions, and the
  nearest existing stable catalog IDs for every gap.

- Added a request-coverage and operational-readiness audit that maps branch integration, self-improvement, usage, placement, inputs, outputs, visibility, algorithms, and coding-agent compatibility to their canonical sources and honest limitations.
- Independently rechecked the live `main` baseline structure: 92 files, 131 unique
  question IDs, 510 resolved declared relationships, eight syntactically valid JSON
  files, 29 parseable YAML files, all resolving internal Markdown links, all
  required human and agent entrypoints present, three historical pull requests merged,
  and no open pull request.
- Reaffirmed that the current framework is A0 overall with manually observed parts of A1; executable semantic enforcement, required CI, end-to-end agent evaluation, and real-project efficacy evidence remain future work.

- Added a root quick start that gives humans and AI agents a minimum useful path
  from an unclear idea to a pinned decision and assurance package.
- Added `ai-context.yaml` as a compact machine-readable discovery manifest for
  canonical sources, context loading, outputs, gate values, truth rules, and
  permission boundaries.
- Added a human and AI usability contract with task-oriented entrypoints,
  progressive disclosure, predictable failure behavior, usability checks, and a
  prioritized automation roadmap.
- Updated README and agent navigation without changing question semantics or
  claiming that an executable engine or success guarantee exists.

- Added a framework quality assurance audit that distinguishes a strong specification
  from an executable and empirically validated assurance system.
- Recorded the audit snapshot: 131 unique questions, 510 resolved references, no
  dependency cycles, 128 high-or-critical labels, 120 natural-language applicability
  rules, eight partial schemas, no reported commit status checks, and one synthetic
  run.
- Defined the specification-to-evidence bottleneck, assurance levels A0-A5, semantic
  validation gaps, quality metrics, stop rules, release gates, and implementation order.

- Added a prioritized coverage-gap and expansion backlog that separates strong
  existing coverage, shallow or missing subject areas, prose-to-catalog parity, and
  executable-runtime limitations.
- Added explicit candidate questions for organizational change, workforce continuity,
  external sensing, information integrity, geopolitical continuity, localization,
  enterprise implementation, ecosystems, intellectual property, fraud and payments,
  hardware production, crisis communication, and liability and insurance.
- Defined promotion rules so a prose mention or backlog question is not presented as
  supported until stable graph records, evidence, outputs, ownership, blocker policy,
  and validation exist.

## 0.7 — 2026-08-12

- Defined the recommended deployment model: this repository owns the reusable
  framework while each target project normally owns its pinned run artifacts.
- Added a complete manual and agent-assisted quick-start, stable-versus-conditional
  output contract, input envelope, and project-placement decision rules.
- Added a vendor-neutral coding-agent architecture with deterministic validation,
  generative, evidence, approval, and repository adapters.
- Added root `AGENTS.md` and `CLAUDE.md` compatibility entrypoints without moving
  canonical behavior out of the normative documentation.
- Added run-manifest and agent-run-request templates with revision pins, integrity
  checks, evidence rules, gate semantics, and permission boundaries.
- Added an explicit qualified-attention loop covering people, companies, agents,
  search, marketplaces, communities, analysts, journalists, advertising, retention,
  referral, procurement, and distribution continuity.
- Added `business.earned-media.001` and `business.organizational-buying.001`, bringing
  the structured catalog to 99 questions and 322 dependencies/activations while
  preserving every existing stable ID.
- Reaffirmed that visibility and real-world success cannot be guaranteed; the
  framework guarantees only declared rule execution, traceability, blocker handling,
  and explicit residual uncertainty.

## 0.6 — 2026-08-11

- Reconciled the integration and financial-continuity branch with the newer graph and
  self-improvement foundation without reverting or duplicating either question model.
- Expanded context capture and release blockers for human/agent/robot authority,
  physical-world safe-stop behavior, committed funding, runway, and continuity.
- Added sharper agent-delegation, fabricated-capability, robot operating-envelope,
  sensor uncertainty, platform portability, financial concentration, cost
  reversibility, minimum-team, surviving-obligation, and finance-delay questions.
- Extended the product brief with an interaction-ecosystem map and explicit cash,
  runway, milestone, downside-trigger, and shutdown-obligation fields.
- Preserved existing human-readable question identifiers and all stable structured
  graph identifiers while consolidating development back into `main`.

## 0.5 — 2026-08-11

- Defined separate improvement loops for an application, an idea, a project-specific graph, and the reusable repository.
- Added a bounded observe, attack, bottleneck, question, experiment, decide, propagate, and outcome-review algorithm.
- Added independent adversarial roles, falsifiable challenge packets, cross-examination, evidence auditing, anti-sycophancy rules, and accountable decision ownership.
- Added a controlling-bottleneck score using impact, graph centrality, uncertainty, evidence weakness, irreversibility, urgency, and validation cost.
- Added pivot classes, preserved-invariant tests, domain-pivot lineage, and explicit comparison with continuing, splitting, pausing, and stopping.
- Added attraction, positioning, channel, funnel, advertising incrementality, acquisition economics, retention, referral, machine-discovery, attention-quality, and distribution-continuity coverage.
- Added 20 reusable questions and 73 relationships, bringing the structured catalog to 97 questions and 312 dependencies/activations.
- Added an improvement-cycle JSON Schema, improvement-cycle and adversarial-review templates, and ADR-0002.
- Protected published catalogs, schemas, blocker policies, security controls, and approval rules from autonomous self-modification.

## 0.4 — 2026-08-11

- Defined the canonical output as a versioned decision and assurance package backed by a traceable knowledge graph.
- Distinguished framework questions, run-specific answers, brainstorming candidates, specifications, ADRs, verification evidence, and gate reports.
- Added universal answer validation, reverse-dependency invalidation, dirty-node propagation, strongly connected component handling, fixed-point convergence, and bounded termination rules.
- Added explicit brainstorming divergence, challenge, promotion, and validation rules; candidate answers can never become accepted merely because they were generated.
- Documented the process guarantees the engine may claim and the real-world success guarantees it must not claim.
- Proposed a Python reference implementation stack and recorded its rationale, validation spike, consequences, and reversal triggers in ADR-0001.
- Added 77 stable, reusable question templates across 16 domains with 239 declared dependencies and activations.
- Added JSON Schemas for question templates, project-specific instances, answer revisions, typed relationships, and project profiles.
- Added explicit domain, lifecycle, state-machine, prioritization, coverage, output, and assurance contracts.
- Separated reusable templates from project answers, evidence, ownership, and state history.
- Added project charter, assurance decision, risk register, and readiness report templates.
- Added a worked sample application showing verified, asked, dormant, and not-applicable question states.
- Defined an honest assurance promise: critical concerns require accepted evidence or explicit risk acceptance with an owner and review date.

## 0.3 — 2026-08-11

- Added the repository propagation rule so important conversation, research, and review outputs become durable Markdown records.
- Added 15 explicit search-visibility and collision questions covering exact and unquoted search, older-brand dominance, search features, reputation, GitHub/GitLab/package/app-store collisions, domains, and dated evidence.
- Expanded the naming brief with a repeatable search query log and channel-specific validation checks.
- Added human, organization, AI-agent, robot, device, platform, and physical-world integration questions.
- Added funding viability, financial failure, success bottleneck, and critical-path questions.
- Added a graph-ready question record, relationship model, answer state machine, application boundaries, and implementation sequence.
- Added a bottleneck register and recorded the Product Questionbook naming decision.
- Clarified the distinction among the repository project, framework, and future application.

## 0.2 — 2026-08-11

- Adopted the Product Questionbook working name and tagline.
- Added naming and identity as the twenty-first product aspect.
- Added naming questions, candidate-generation guidance, a recommended process, anti-patterns, and a naming brief.

## 0.1 — 2026-08-11

- Added the universal software-product aspects, core and detailed question banks, working method, product brief, decision record, and review scorecard.
