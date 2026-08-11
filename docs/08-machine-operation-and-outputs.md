# Machine operation and output contract

**Status:** Architecture contract; engine implementation is not yet present  
**Applies to:** software products, services, platforms, frameworks, AI systems, integrations, and robot-connected systems

## What this repository is

Product Questionbook is the knowledge and decision layer for a question engine. It supplies questions, review rules, evidence expectations, and output templates.

The current repository is documentation-first. A person or language-model agent can follow it today, but the repository does not yet contain an executable parser, API, database, graph engine, or autonomous runtime. Calling the Markdown files an implemented machine would be inaccurate.

The intended machine turns incomplete project context into an evidence-linked graph of questions, answers, decisions, risks, requirements, actions, metrics, and gate results. It reduces important omissions; it cannot guarantee that a product or system will succeed.

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

## Canonical question record

A machine-ready question needs stable metadata in addition to its human-readable text. Markdown remains the source format; YAML front matter or fenced YAML may carry structured fields.

~~~yaml
schema_version: question/v0.1
id: ARCH-001
text: What is the simplest architecture that meets current evidence and constraints?
aspect: architecture-and-maintainability
importance_default: important
applies_when:
  any_subject_type: [application, service, platform, framework, ai-system]
depends_on: [CTX-001, SCOPE-001]
produces: [decision, requirement, risk, experiment]
required_at: [architecture-review]
blocker_if:
  - critical_dependency_has_no_owner
evidence_expected:
  - architecture-record
  - constraint-list
review_triggers:
  - major_scope_change
  - critical_dependency_change
~~~

Stable IDs must not be derived only from line numbers because documents are edited over time.

## Question state machine

~~~mermaid
stateDiagram-v2
    [*] --> Unseen
    Unseen --> Selected: applicable
    Unseen --> NotApplicable: reason recorded
    Selected --> Asked
    Asked --> Answered
    Answered --> NeedsEvidence: insufficient support
    NeedsEvidence --> Answered: evidence added
    Answered --> Blocked: critical gap
    Answered --> Verified: checks pass
    Verified --> Accepted: owner approves
    Blocked --> Answered: gap resolved
    Accepted --> Superseded: context changes
    NotApplicable --> Selected: applicability changes
    Superseded --> Selected: review reopened
~~~

Deferred may be used from Selected, Asked, or Answered, but it requires an owner, reason, due date or trigger, and a statement of what risk is accepted.

State rules:

- Unknown is valid; invented certainty is not.
- NotApplicable requires a recorded reason.
- NeedsEvidence is not equivalent to Accepted.
- A critical blocker prevents a Proceed result even if aggregate scores are high.
- Accepted requires an owner and verification rule; high-impact decisions also require an authorized human approver.
- A changed dependency, policy, incident, metric, or assumption can reopen an accepted answer.

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

Canonical outputs should be Markdown files with machine-readable YAML front matter. JSON or database projections may be generated for APIs and graph queries, but they should carry the same schema version and trace IDs.

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
| API client | Versioned schemas and run endpoints | Structured events and artifact links | Authentication, authorization, validation, audit |
| Robot or device adapter | Approved bounded requirement or action | Command proposal or configuration | Separate safety controller and human approval where consequential |

A future service could expose operations such as create run, submit answer, attach evidence, get next question, evaluate gate, export artifacts, and reopen affected nodes. These are target interfaces, not current repository capabilities.

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
| 0 — current | Human-readable question banks and templates | Existing Markdown documents |
| 1 | Stable question IDs and structured metadata | All question records validate |
| 2 | Parser, schema validator, and link checker | Repeatable tests in CI |
| 3 | Dependency graph, state transitions, prioritizer, and gate evaluator | Deterministic scenario tests |
| 4 | CLI/API plus human, agent, workflow, CI, and device adapters | Versioned contract tests |
| 5 | Domain packs, evaluations, telemetry, and change-impact analysis | Quality and safety benchmarks |

Until phases 1–3 exist, consumers should treat this repository as a rigorously structured decision framework, not as an executable autonomous machine.
