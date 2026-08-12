# Machine operation and output contract

**Status:** Normative text protocol and optional automation contract; automated validation is not yet implemented  
**Applies to:** software products, services, platforms, frameworks, AI systems, integrations, and robot-connected systems

## What this repository is

Product Questionbook is a text-first knowledge and decision protocol. It supplies questions, review rules, evidence expectations, schemas, and output templates that people and language-model agents can apply directly.

The canonical interface is versioned Markdown and YAML with JSON Schema and Git history. A CLI, API, database, graph service, or autonomous runtime is not required for normal use. The current absence of those components is therefore not, by itself, an implementation failure.

The logical model connects project context to questions, answers, decisions, risks, requirements, actions, metrics, and gate results. Optional deterministic automation may validate and project that model, but canonical state remains in inspectable text files. The framework reduces important omissions; it cannot guarantee that a product or system will succeed.

## System boundary

The Questionbook machine may recommend, classify, validate, and generate artifacts. It must not silently claim evidence, approve its own high-impact decisions, deploy software, send commands to hardware, spend money, or contact people unless a separate, authorized adapter and approval policy explicitly permit that action.

For robot-connected or safety-critical systems, the repository is a planning and assurance input. A separately tested control system must translate approved decisions into bounded commands. Questionbook output is never a real-time control signal.

## Inputs

Every run needs the following inputs. Missing values remain explicit unknowns.

| Input | Minimum content | Why it is needed |
| --- | --- | --- |
| Run context | run ID, owner, date, purpose, decision to enable | Makes the review traceable |
| Subject profile | name, type, lifecycle stage, users, operators, domain, countries, platforms | Selects applicable questions |
| Objectives | desired outcomes, success measures, non-goals | Prevents feature-driven drift |
| Constraints | time, budget, team, regulation, safety, architecture, dependencies | Shapes feasible decisions |
| Evidence | source, observation, date, confidence, scope | Separates knowledge from belief |
| Policies | required gates, approval roles, risk thresholds | Determines blocking behavior |
| Prior state | previous answers, decisions, incidents, metrics, and versions | Enables change-aware review |

The term **subject** is deliberately broader than application. It may be a product, application, service, platform, framework, process, AI agent, integration, or robot-connected system.

## Canonical structured definitions

Version 0.4 separates the human-readable question banks from the machine-readable
catalog. The following files are authoritative for structured operation:

- [structured graph foundation](structured-foundation.md): representations and workflow;
- [domain model](domain-model.md): entities, typed relationships, and invariants;
- [question state machine](question-state-machine.md): instance and template lifecycles;
- [prioritization](prioritization.md): ranking formula and mandatory overrides;
- [output contract](output-contract.md): machine, human, and action outputs;
- [assurance rules](assurance-rules.md): completion and readiness semantics;
- [JSON Schemas](../schemas/): validation contracts;
- [YAML catalog](../catalog/): stable reusable question templates.

The numbered Markdown question banks remain the broad human-readable source material.
A question is machine-operable after it has a stable catalog ID and validates against
the question schema. Project answers, evidence, ownership, and state are stored in
instances and answer revisions, not in the reusable template.

## Question state machine

The canonical state machine is defined in
[question-state-machine.md](question-state-machine.md). Its instance states are
`dormant`, `ready`, `asked`, `answered`, `clarification_required`, `blocked`,
`verified`, `stale`, and `not_applicable`. Template publication separately follows
`draft -> reviewed -> published -> deprecated`.

Unknown information remains explicit. `not_applicable` requires a reason, a critical
blocker prevents readiness, and verified answers can become stale after a dependency,
policy, incident, metric, assumption, or review deadline changes.

## Knowledge graph

The engine should preserve relationships rather than flattening everything into a checklist.

| Node type | Meaning |
| --- | --- |
| Question | Information or decision that must be resolved |
| Answer | Current response, including unknown or not applicable |
| Evidence | Source supporting or contradicting an answer |
| Assumption | Belief that has not yet been verified |
| Decision | Chosen option, rationale, owner, and consequences |
| Requirement | Testable behavior or constraint |
| Risk | Possible harmful outcome with likelihood, impact, and owner |
| Action | Research, build, mitigation, approval, or follow-up work |
| Metric | Observable success, guardrail, or operating signal |
| Gate | Proceed, proceed with conditions, pause, or stop decision |
| Artifact | Human- and machine-readable result document |

Recommended edge types are depends_on, applies_to, answered_by, supported_by, contradicted_by, produces, mitigates, verifies, blocks, approved_by, and supersedes.

## How a run works

1. **Validate context.** Record the subject, lifecycle stage, decision, policies, and missing inputs.
2. **Build the applicable graph.** Load question nodes, dependencies, gates, and prior answers; exclude only questions with justified non-applicability.
3. **Prioritize.** Prefer questions with high harm, uncertainty, irreversibility, dependency centrality, or near-term gate relevance.
4. **Ask the next useful question.** Ask only what can change a decision, expose a risk, or define verification.
5. **Validate the answer.** Separate facts, evidence, assumptions, preferences, and unknowns. Check required fields and contradictions.
6. **Propagate consequences.** Create or update requirements, decisions, risks, actions, metrics, tests, and approvals linked to the answer.
7. **Evaluate gates.** Apply blocker rules before score aggregation and produce a reasoned gate result.
8. **Publish artifacts.** Write Markdown outputs with structured metadata and a trace from each conclusion to its questions and evidence.
9. **Monitor and reopen.** Re-evaluate affected nodes when context, evidence, dependencies, incidents, policies, or metrics change.

A useful next-question priority model is:

~~~text
priority = gate_urgency × potential_harm × uncertainty × irreversibility × dependency_centrality
~~~

This is a ranking aid, not a substitute for policy or human judgment.

## Output catalog

A run produces a bundle, not one answer.

| Output | Purpose | Typical source |
| --- | --- | --- |
| Run manifest | Identity, version, owner, policy, subject, and timestamps | Context input |
| Applicability and coverage map | Selected, excluded, unanswered, and completed questions | Question graph |
| Question ledger | State, answer, evidence, owner, verification, and review trigger per question | Answer workflow |
| Product or system brief | Consolidated purpose, scope, people, constraints, architecture, and lifecycle | Product brief template |
| Decision records | Options, decision, rationale, trade-offs, and reversal condition | Decision template |
| Requirements and acceptance criteria | Testable consequences of answers | Answer propagation |
| Risk and blocker register | Severity, mitigation, detection, owner, and status | Risk analysis |
| Experiment and research backlog | Unknowns with methods, owners, and deadlines | Evidence gaps |
| Integration contracts | APIs, events, identity, failure behavior, compatibility, and ownership | Integration questions |
| Verification plan | Tests, evaluations, reviews, drills, and acceptance thresholds | Evidence expectations |
| Metrics and operational controls | Outcomes, guardrails, SLOs, alerts, runbooks, and support ownership | Measurement and operations |
| Gate report | Proceed, proceed with conditions, pause, or stop, with reasons | Scorecard and blocker policy |
| Audit trace | Links from conclusions to questions, evidence, decisions, approvals, and versions | Entire graph |
| Change impact report | Nodes and artifacts that must be reopened after a change | Dependency graph |

## Output format

Canonical outputs should be Markdown files with machine-readable YAML front matter. JSON projections may be generated for validation or graph queries, but they must be reproducible from the text records and carry the same schema version and trace IDs. A database is optional and never silently becomes the source of truth.

A minimal run artifact begins like this:

~~~yaml
---
schema_version: questionbook-run/v0.1
run_id: RUN-2026-0001
subject_id: SUBJECT-001
subject_type: application
stage: architecture
status: in_review
owner: owner-id
questionbook_ref: git-commit-sha
gate_result: pause
blockers:
  - RISK-004
coverage:
  applicable: 84
  accepted: 51
  needs_evidence: 12
  blocked: 1
  deferred: 7
  unanswered: 13
updated_at: 2026-08-11T20:00:00Z
---
~~~

Recommended run directory:

~~~text
runs/<run-id>/
  00-context.md
  01-coverage.md
  02-question-ledger.md
  03-system-brief.md
  decisions/
  04-requirements.md
  05-risks-and-blockers.md
  06-actions-and-experiments.md
  07-verification-and-operations.md
  08-gate-report.md
  09-audit-trace.md
~~~

Every generated artifact should record the Questionbook Git commit used, schema version, run ID, subject ID, timestamps, owner, and linked source node IDs.

## Integration surfaces

| Consumer | Reads | Writes or receives | Required guardrail |
| --- | --- | --- | --- |
| Human workshop | Questions and current artifacts | Answers, evidence, decisions, approvals | Facilitator records disagreement and unknowns |
| Language-model agent | Question graph, context, policies, prior state | Proposed answers, follow-up questions, draft artifacts | Never invent evidence; label inference and confidence |
| Workflow system | Actions, owners, deadlines, blockers | Issues, tasks, status updates | Idempotency and explicit authorization |
| CI or policy gate | Required questions, evidence rules, gate policy | Pass, conditional pass, or fail report | Critical blockers cannot be averaged away |
| Optional API client | Versioned schemas and explicitly justified endpoints | Structured events and artifact links | Authentication, authorization, validation, audit, and no hidden canonical state |
| Robot or device adapter | Approved bounded requirement or action | Command proposal or configuration | Separate safety controller and human approval where consequential |

If measured multi-user or integration requirements justify it, a future service could expose operations such as create run, submit answer, attach evidence, get next question, evaluate gate, export artifacts, and reopen affected nodes. Such a service is an optional adapter, not the framework's required interface.

## Completion and success semantics

A run is structurally complete when:

- every required applicable question is in a terminal state;
- no critical blocker remains unresolved;
- every accepted high-impact decision has the required evidence, owner, verification, and approval;
- required artifacts have passed schema and link validation;
- the gate result and remaining conditions are explicit.

Structural completion does **not** guarantee commercial, technical, ethical, or operational success. The machine can guarantee only properties it can verify, such as schema validity, traceability, stated coverage, rule execution, and explicit unresolved uncertainty. Real success still depends on the quality of evidence, decisions, execution, changing conditions, and human accountability.

## Implementation roadmap

| Phase | Capability | Completion evidence |
| --- | --- | --- |
| 0 — complete | Human-readable question banks and templates | Existing Markdown documents |
| 1 — current | Stable question IDs, schemas, structured metadata, and examples | Starter catalog and examples validate |
| 2 | Read-only conformance validator for schemas, IDs, references, and links | Repeatable tests and reports in CI |
| 3 | Optional semantic validation for state transitions, blockers, policies, and reproducible projections | Deterministic scenario tests |
| 4 | Evidence-justified adapters; CLI/API only when a consumer needs them | Versioned contract and usability tests |
| 5 | Domain packs, evaluations, telemetry, and change-impact analysis | Quality and safety benchmarks |

Phases 2–3 strengthen assurance but do not replace the text interface. Consumers may
use the framework manually or with an agent today; they must not describe it as an
automatically enforced assurance system until the relevant validators exist.

