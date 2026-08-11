# Output, brainstorming, convergence, and implementation contract

**Status:** Normative design for the future engine; executable implementation is not yet present  
**Applies to:** every question and every subject type, not only technology-selection questions

## Direct answer: what is the output?

The system's canonical result is a **versioned decision and assurance package backed by a traceable knowledge graph**.

It is not only a question list, answer list, specification, or set of architecture decision records (ADRs). Each of those is one layer or projection of the same graph.

| Item | Role | Is it the final output? |
| --- | --- | --- |
| Reusable question bank | Framework input: what the engine knows how to ask | No |
| Applicable question graph | Run-specific scope and dependency model | Part of the canonical state |
| Answer ledger | Current beliefs, evidence, assumptions, unknowns, confidence, and status | Intermediate and auditable output |
| Brainstorm results | Candidate questions, hypotheses, options, risks, and experiments | Intermediate; never accepted automatically |
| Product or system specification | Build-facing requirements and acceptance criteria derived from accepted answers | Required projection |
| ADRs or decision records | Durable choices, alternatives, rationale, consequences, and reversal triggers | Required for material decisions |
| Risk, experiment, and action registers | Work needed to reduce uncertainty or control harm | Required when applicable |
| Verification plan and evidence index | How claims and requirements will be checked | Required projection |
| Gate and assurance report | Whether the evidence satisfies the declared policy and what remains unresolved | Final decision-facing projection |
| Audit and change-impact trace | Why every conclusion exists and what must reopen after a change | Required canonical output |

The graph is the normalized source of run state. Markdown artifacts are human-readable projections. JSON and database views may be generated, but they must preserve the same stable IDs, versions, and relationships.

## Why a bundle is the best output

A single artifact loses necessary information:

- A question list exposes possible blind spots but says nothing about the subject.
- An answer list can contain unsupported opinions and does not tell builders what to implement.
- A specification says what to build but often hides evidence, alternatives, risks, and reversal conditions.
- ADRs explain selected decisions but do not prove complete product, business, safety, operational, or lifecycle coverage.
- A score can conceal a fatal gap if strong areas average against a critical failure.
- A graph preserves relationships but is inconvenient for human review and approval.

The package keeps all of these views linked. A requirement can be traced to the answer and evidence that created it; an ADR can be traced to alternatives and constraints; a release gate can be traced to tests, risks, and approvals. This makes the result reviewable, correctable, and regenerable when an upstream fact changes.

## Success claim and guarantee boundary

No finite questionnaire or algorithm can guarantee commercial or real-world product success. Users, competitors, regulations, evidence, execution quality, funding, and external systems can change, and important unknowns may be unobservable before release.

The engine may make only this bounded claim:

> At framework revision F, evidence snapshot E, and policy P, all required checks were executed; the recorded conclusions satisfy P, except for the explicitly listed conditions, unknowns, and accepted risks.

It can guarantee process properties that it controls:

- schema-valid records;
- stable identity and versioning;
- execution of declared applicability, dependency, validation, and gate rules;
- traceability from conclusions to questions, evidence, decisions, approvals, and tests;
- detection and explicit reporting of known missing fields, stale dependencies, and registered contradictions;
- refusal to average away a critical blocker;
- a bounded return result of `proceed`, `proceed_with_conditions`, `pause`, or `stop`.

It cannot guarantee that evidence is truthful, all relevant facts were supplied, people will execute decisions well, the environment will remain unchanged, or the product will achieve an outcome that has not yet occurred. The purpose is to raise the probability of success, reduce avoidable failure, and make residual uncertainty visible—not to manufacture certainty.

## Brainstorming is a first-class stage

Brainstorming expands the graph before evidence-based convergence. It is triggered when the initial idea is unclear, coverage is weak, alternatives are missing, a contradiction appears, a high-impact answer has low confidence, or the graph contains an unexplained dependency.

### Diverge

Generate candidates across applicable aspects:

- new questions and subquestions;
- hypotheses or candidate answers;
- solution and non-solution options;
- assumptions and counter-assumptions;
- risks, failure modes, abuse cases, and edge cases;
- experiments, research tasks, prototypes, and evidence requests;
- possible requirements, metrics, constraints, and review triggers;
- new relationships among existing nodes.

### Challenge

Search for duplicates, missing stakeholders, incompatible assumptions, disconfirming evidence, unconsidered alternatives, premature implementation choices, and consequences outside the originating aspect.

### Converge

Classify and promote candidates:

| Candidate type | Promotion rule |
| --- | --- |
| New question | Add only if its answer could change a decision, expose material risk, or define verification |
| Candidate answer or hypothesis | Keep as `proposed` until evidence and validation rules pass |
| Option | Compare against explicit decision criteria; record rejection rationale |
| Risk | Assess impact, likelihood, detectability, owner, mitigation, and fallback |
| Experiment | Require a falsifiable claim, method, threshold, owner, cost, and stop rule |
| Requirement | Derive from an accepted answer and give it testable acceptance criteria |
| Decision | Record scope, rationale, consequences, owner, approval, and reversal trigger |

Brainstorming therefore produces both new questions and candidate answers, but it produces **no accepted answer by itself**. Its durable output is a candidate ledger plus the graph changes that survived triage.

## Universal dependency and correction graph

Every important record is a typed node. The mechanism is independent of question topic.

Recommended node types are `Question`, `Answer`, `Evidence`, `Assumption`, `Option`, `Decision`, `Requirement`, `Risk`, `Experiment`, `Action`, `Metric`, `Test`, `Approval`, `Gate`, and `Artifact`.

Recommended directed edge types are:

| Edge | Meaning when `A -> B` |
| --- | --- |
| `depends_on` | A cannot be accepted without B |
| `constrains` | A narrows valid values or choices for B |
| `supports` | A provides evidence for B |
| `contradicts` | A and B cannot both remain accepted without resolution |
| `derives` | A produces or changes B |
| `verifies` | A tests a claim made by B |
| `blocks` | A prevents B or its gate from passing |
| `supersedes` | A replaces an earlier version of B |
| `reopens_on_change` | A changing makes B stale and queues it for review |

For example, a programming-language decision may depend on deployment targets, team capability, latency, library maturity, integration constraints, security policy, and operating cost. Changing any of those upstream nodes marks the language decision and its derived ADR, requirements, implementation plan, and tests stale.

## Answer validation contract

An answer record must separate what is known from what is proposed.

~~~yaml
schema_version: answer/v0.1
id: ANSWER-ARCH-001-v3
question_id: ARCH-001
status: proposed
value: Use Python for the reference engine.
claim_type: decision
evidence_ids: [EVID-TEAM-002, EVID-PROTOTYPE-004]
assumption_ids: [ASSUME-DEPLOY-001]
confidence: medium
owner: architecture-owner
verification_ids: [TEST-PARSER-001, TEST-GRAPH-003]
depends_on: [DEPLOY-001, TEAM-001, PERF-001]
contradicts: []
review_triggers: [deployment_target_changed, latency_budget_changed]
updated_at: 2026-08-11T20:00:00Z
~~~

The engine evaluates an answer against a policy-specific acceptance predicate:

~~~text
acceptable(answer, policy) =
  schema_valid
  AND required_dependencies_acceptable
  AND evidence_meets_policy_threshold
  AND no_unresolved_material_contradiction
  AND verification_defined_or_completed_as_required
  AND owner_present
  AND approval_present_when_required
  AND evidence_not_stale
~~~

Thresholds vary by impact and lifecycle stage. An early, reversible prototype choice needs less evidence than an irreversible safety, privacy, legal, or release decision.

## Iterative convergence algorithm

The engine processes a dirty-node queue so one answer can correct any affected answer or artifact.

~~~text
start a versioned run epoch from a frozen input snapshot
validate context and load policy
build the applicable typed graph
brainstorm and triage missing candidate nodes
queue all required unresolved or stale nodes

while queue is not empty and run budget remains:
    select the highest-priority node
    collect or revise its answer and evidence
    validate schema, dependencies, evidence, contradictions, and approvals
    propagate derived requirements, decisions, risks, tests, metrics, and artifacts
    mark reverse dependants stale when the accepted meaning changed
    enqueue every affected node
    evaluate blockers and gates

if acceptance and convergence conditions pass:
    return proceed or proceed_with_conditions
else:
    return pause or stop with unresolved nodes and reasons
~~~

A starting priority rule is:

~~~text
priority =
  gate_urgency
  * potential_harm
  * uncertainty
  * irreversibility
  * dependency_centrality
  * expected_information_gain
  / estimated_resolution_cost
~~~

The exact scales belong to a versioned policy. Critical policy rules always override numerical ranking.

## Cycles, fixed points, and termination

Some questions are mutually dependent. The engine must not pretend that a simple topological ordering exists.

1. Find strongly connected components in the directed dependency graph.
2. Condense the graph into an acyclic component graph.
3. Process components in dependency order.
4. Within a cyclic component, iterate candidate assignments and validations until no accepted value or status changes.
5. Stop the component at its policy limit for iterations, elapsed time, evidence cost, or human-review budget.
6. If it does not stabilize, return `pause` with the unresolved cycle, competing assignments, missing evidence, and required escalation.

An epoch converges only when:

- all required applicable questions meet their acceptance predicates;
- no unresolved critical blocker or material contradiction remains;
- no accepted node is dirty or stale;
- all required derived artifacts are regenerated and link-valid;
- mandatory tests and approvals pass;
- coverage and evidence freshness meet the gate policy;
- no new in-scope graph mutation is pending.

New external evidence or a changed requirement starts a new epoch and may reopen the result. A maximum run budget guarantees that the engine returns a truthful gate result; it does not guarantee that every problem has a satisfactory solution.

## Output package layout

~~~text
runs/<run-id>/
  00-manifest.md
  01-context-and-success.md
  02-applicability-and-coverage.md
  03-question-answer-ledger.md
  04-brainstorm-candidates.md
  05-system-brief.md
  06-specification.md
  decisions/
  07-risks-experiments-and-actions.md
  08-verification-and-evidence.md
  09-gate-and-assurance-report.md
  10-audit-and-change-impact.md
  graph.json
~~~

Markdown is canonical for human review. YAML front matter carries schema and identity fields. `graph.json` is a deterministic projection for machines; it must be regenerable from canonical records or checked against them by CI.

## Proposed implementation stack

The reference implementation should begin as a modular Python application because the dominant work is typed document validation, graph algorithms, policy evaluation, testing, API integration, and optional language-model orchestration—not hard real-time control.

| Layer | Initial choice | Purpose |
| --- | --- | --- |
| Language | Python 3.13+ | One typed implementation for parser, graph, CLI, API, and evaluations |
| Environment and packaging | `uv`, `pyproject.toml` | Reproducible dependency and project management |
| Markdown/YAML | `markdown-it-py`, `ruamel.yaml` | Parse Markdown and preserve structured YAML during round trips |
| Models and schemas | Pydantic 2, generated JSON Schema | Typed validation and shared API/artifact contracts |
| Graph reference engine | NetworkX `MultiDiGraph` | Typed directed relationships, traversal, centrality, SCCs, and impact analysis |
| CLI | Typer | Local commands such as `validate`, `run`, `next`, `gate`, and `export` |
| API | FastAPI | Versioned HTTP contract and OpenAPI documentation |
| Persistence | SQLite locally; PostgreSQL for a service | Transactions, versioned records, audit events, and relational graph tables |
| Database access | SQLAlchemy 2 and Alembic | Persistence mapping and controlled schema migrations |
| Templates | Jinja2 | Deterministic Markdown projections |
| Tests | pytest, Hypothesis | Scenario, invariant, state-machine, and property-based tests |
| Quality | Ruff and mypy | Formatting, linting, and static type checks |

Do not require a graph database in the first implementation. Begin with an explicit node table and edge table plus NetworkX for in-memory algorithms. Revisit a dedicated graph store only when measured query volume, traversal depth, multi-user concurrency, or operational evidence justifies it.

Language-model support must be an optional adapter. Deterministic schema validation, state transitions, dependency propagation, blocker rules, and gate evaluation must work without an LLM. Robots and devices require a separate safety-certified or otherwise appropriately assured control boundary; this engine never emits direct real-time actuation.

Package choices and minimum versions must be locked only when implementation begins, then reviewed by compatibility, security, maintenance, license, and reproducibility checks. See the implementation ADR for the rationale and reversal triggers.

## First executable milestone

The first implementation is complete only when it can:

1. parse stable question and answer records;
2. validate them against versioned schemas;
3. build the typed dependency graph;
4. detect broken links, contradictions, cycles, and stale reverse dependencies;
5. calculate the next-question frontier deterministically;
6. propagate a changed answer and list every affected node and artifact;
7. evaluate a gate without averaging away blockers;
8. export the complete package and reproduce it from the same inputs;
9. pass fixture-based scenarios and property tests for termination, idempotency, traceability, and change propagation.

Only after that milestone should autonomous brainstorming or LLM-assisted candidate generation be allowed to modify a run—and even then, candidates require the same validation and approval path as human proposals.

