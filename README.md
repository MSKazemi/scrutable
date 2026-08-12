# Product Questionbook

> Questions for the whole software lifecycle.

Product Questionbook is a reusable question system for designing, reviewing, and improving software products.

The goal is not to create a product with the most features. The goal is to make important decisions explicit, expose unknowns early, and build a product that is useful, usable, secure, reliable, operable, and sustainable.

## Choose your path

| Goal | Start here |
| --- | --- |
| Apply it to an idea or project | [`QUICKSTART.md`](QUICKSTART.md) |
| Use it with an AI agent | [`ai-context.yaml`](ai-context.yaml), then [`AGENTS.md`](AGENTS.md) |
| See a worked structure | [`examples/sample-application/`](examples/sample-application/) |
| Understand the complete framework | [Full documentation path](#start-here) |
| Change the framework | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Trace prose questions to the graph | [`docs/16-prose-to-catalog-coverage.md`](docs/16-prose-to-catalog-coverage.md) |
| Govern a specialized domain pack | [`docs/17-domain-pack-governance.md`](docs/17-domain-pack-governance.md) |
| Monitor external change, web, and news | [`docs/18-external-sensing-and-attention.md`](docs/18-external-sensing-and-attention.md) |
| Verify coverage and current limits | [`docs/15-request-coverage-and-operational-readiness-audit.md`](docs/15-request-coverage-and-operational-readiness-audit.md) |

## What this repository is

- **Project:** this repository and all work used to develop Product Questionbook.
- **Framework:** the question banks, methods, evidence rules, structured catalog, schemas, and templates in this repository.
- **Optional application:** a future convenience interface that may navigate the question graph, track answer state, and generate project artifacts. It is not required to use the framework; the canonical interface remains versioned Markdown, YAML, JSON Schema, and Git.

The framework can improve decision quality and expose failure risks; it cannot guarantee a perfect or successful product.

## Start here

1. Read [the working method](docs/00-method.md).
2. Scan [the product aspects](docs/01-aspects.md) to decide what matters for this product.
3. Answer [the core questions](docs/02-core-questions.md) before major implementation begins.
4. Continue with the detailed question banks:
   - [Discovery and experience](docs/03-discovery-and-experience.md)
   - [Engineering, data, and integrations](docs/04-engineering-data-and-integrations.md)
   - [Trust, quality, and operations](docs/05-trust-quality-and-operations.md)
   - [Business, governance, and evolution](docs/06-business-governance-and-evolution.md)
   - [Naming and identity](docs/07-naming-and-identity.md)
5. Read the [machine operation and output contract](docs/08-machine-operation-and-outputs.md) when building automation or an interactive navigator.
6. Read [the output, brainstorming, convergence, and implementation contract](docs/09-output-convergence-and-implementation.md) for the canonical result, cross-question correction algorithm, convergence rules, and automation boundary. The text-first decision is recorded in [ADR-0003](decisions/ADR-0003-text-first-agent-native-architecture.md); the earlier full-engine stack proposal is deferred in [ADR-0001](decisions/ADR-0001-engine-implementation-stack.md).
7. Use the [structured graph foundation](docs/structured-foundation.md) for stable IDs, typed relationships, state history, schemas, and the governed domain-pack interface.
8. Use the [governed self-improvement and adversarial review method](docs/10-self-improvement-and-adversarial-governance.md) when challenging an idea, finding the controlling bottleneck, evaluating a pivot, or improving the framework. Its governance decision is recorded in [ADR-0002](decisions/ADR-0002-governed-adversarial-self-improvement.md).
9. Follow the [usage, project placement, visibility, and agent-integration protocol](docs/11-usage-deployment-and-agent-integration.md) to apply the framework to another repository or run it with Codex, ChatGPT, Claude Code, or another agent system.
10. Record results using the [run manifest](templates/run-manifest.md), [agent run request](templates/agent-run-request.md), [project charter](templates/project-charter.md), [product brief](templates/product-brief.md), [decision record](templates/decision-record.md), [assurance decision record](templates/assurance-decision-record.md), [naming brief](templates/naming-brief.md), [bottleneck register](templates/bottleneck-register.md), [risk register](templates/risk-register.md), [review scorecard](templates/review-scorecard.md), [readiness report](templates/readiness-report.md), [improvement cycle](templates/improvement-cycle.md), [adversarial review](templates/adversarial-review.md), and [external signal register](templates/external-signal-register.md).
11. Inspect the [prose-to-catalog coverage contract](docs/16-prose-to-catalog-coverage.md) to see how every numbered human-readable question is preserved and connected to the stable graph without claiming false one-to-one equivalence.
12. Use the [domain-pack governance contract](docs/17-domain-pack-governance.md) when regulation, safety criticality, or material sector-specific harm may require qualified coverage.
13. Use the [external sensing and attention contract](docs/18-external-sensing-and-attention.md) to collect decision-changing signals from authorities, people, companies, agents, the web, and news while keeping blind spots explicit.
14. Review the [coverage gaps and expansion backlog](docs/12-coverage-gaps-and-expansion-backlog.md) before claiming comprehensive support or promoting new question domains.
15. Read the [framework quality assurance audit](docs/13-quality-assurance-audit-and-roadmap.md) for the controlling bottleneck, measurable assurance levels, release gates, and validation roadmap.
16. Read the [human and AI usability contract](docs/14-human-and-ai-usability.md) for progressive disclosure, task-based entrypoints, context loading, failure behavior, and the prioritized usability roadmap.
17. Read the [request coverage and operational-readiness audit](docs/15-request-coverage-and-operational-readiness-audit.md) for a direct status of branch integration, self-improvement, usage, inputs, outputs, visibility, algorithms, agent compatibility, and remaining implementation gaps.
18. Read the [whole-repository integration audit](docs/19-whole-repository-integration-audit.md) for the pinned file-by-file review, deterministic cross-file checks, corrections, and remaining integration risks.

The accepted framework name and its limitations are recorded in [the naming decision](decisions/0001-product-questionbook-name.md). The primary-interface boundary is recorded in [ADR-0003: text-first, agent-native architecture](decisions/ADR-0003-text-first-agent-native-architecture.md).

## How it works

1. Establish the subject, lifecycle stage, desired outcome, constraints, and decision that the review must enable.
2. Classify each aspect as critical, important, relevant, or not applicable.
3. Ask only questions that can change a decision, expose a risk, or define verification.
4. Record answers with evidence, assumptions, unknowns, decisions, owners, and review triggers.
5. Propagate each important answer into requirements, decisions, risks, experiments, metrics, tests, approvals, or operational procedures.
6. Evaluate lifecycle gates. Critical safety, security, privacy, legal, reliability, or data-loss gaps block progress even when other areas score well.
7. Run independent evidence-based attacks against consequential claims, preserve dissent, and test the controlling bottleneck before commitment.
8. Reopen affected questions when evidence, dependencies, users, scale, regulation, incidents, or strategy change.
9. Compare predicted and observed outcomes; use the error to improve the application, idea, project graph, or reusable framework through governed change.

## Outputs

The canonical result is a **versioned decision and assurance package backed by a
traceable knowledge graph**. The reusable question bank is framework input; answers
are validated run state; specifications, ADRs, tests, and gate reports are linked
projections. A completed review therefore produces a bundle rather than a single score:

- a product or system brief;
- a question and evidence ledger;
- decision records;
- requirements and acceptance criteria;
- risks, blockers, mitigations, and owners;
- experiments, research, and follow-up actions;
- adversarial challenge packets, controlling-bottleneck analysis, and improvement-cycle records;
- integration and verification plans;
- success metrics, guardrails, operational controls, and support ownership;
- a gate result: proceed, proceed with conditions, pause, or stop;
- an audit trace and change-impact report.

See the [machine contract](docs/08-machine-operation-and-outputs.md) for the state machine, knowledge graph, structured Markdown format, output directory, integration boundaries, and completion rules. See the [output and convergence contract](docs/09-output-convergence-and-implementation.md) for brainstorming, answer correction, cyclic dependencies, fixed-point rules, termination, and the optional automation boundary.

## Structured graph foundation

The graph layer converts the documentation-first framework into machine-validatable
question templates and project-specific instances without replacing the existing
human-readable question banks.

The initial foundation includes:

- [framework vision and boundaries](docs/vision.md), [terminology](docs/terminology.md), and [domain model](docs/domain-model.md);
- an explicit [question state machine](docs/question-state-machine.md), [priority model](docs/prioritization.md), and [coverage matrix](docs/coverage-model.md);
- [output](docs/output-contract.md) and [assurance](docs/assurance-rules.md) contracts;
- JSON Schemas for questions, instances, answers, relationships, project profiles,
  governed improvement cycles, prose coverage, and domain-pack manifests in
  [`schemas/`](schemas/);
- a [prose-to-catalog coverage manifest](coverage/prose-to-catalog.yaml) with 396 stable source identities and a [coverage schema](schemas/prose-coverage.schema.json);
- 131 starter templates with 450 declared dependencies and activations across 16
  universal concern domains in [`catalog/`](catalog/);
- a [domain-pack governance contract](docs/17-domain-pack-governance.md), schema,
  draft manifest, and eight stable governance questions; no expert-reviewed pack is
  yet published;
- an eight-question
  [organizational adoption and change module](catalog/team/organizational-change-questions.yaml)
  covering impact, resistance, enablement, transition, workforce obligations,
  measurement, safeguards, and post-launch ownership;
- an eight-question
  [workforce and knowledge continuity module](catalog/team/workforce-continuity-questions.yaml)
  covering key-person dependencies, succession, capacity, incentives, secure
  departure, separation of duties, sourcing, and leading indicators;
- an eight-question
  [external sensing module](catalog/operations/external-sensing-questions.yaml), a
  source-to-decision
  [operating method](docs/18-external-sensing-and-attention.md), and a reusable signal
  register;
- reusable assurance and improvement templates plus a worked project-specific example.

The versioned Markdown and YAML records are the source of truth. The graph is their
logical relationship model and may be materialized as a reproducible JSON projection;
it is not required to live in a database or separate application.

## What a good answer contains

A useful answer is specific and testable. It should include:

- the decision or current belief;
- evidence and its source;
- assumptions and unknowns;
- trade-offs and rejected alternatives;
- an owner and review date;
- a way to verify the result.

`Unknown` is an acceptable answer. A vague statement presented as certainty is not.

## Repository is the source of truth

Important conclusions from conversations, research, reviews, and experiments must be distilled into the appropriate repository file. A material result is not considered incorporated until its decision, evidence, owner, and implications are recorded here. See [the working method](docs/00-method.md#repository-propagation-rule).

## Suggested lifecycle

| Stage | Main outcome |
| --- | --- |
| Discover | A validated problem, audience, and desired outcome |
| Define | Scope, requirements, risks, and success measures |
| Design | Usable flows and sound technical decisions |
| Build | Tested, observable, secure, maintainable software |
| Release | Safe rollout, support readiness, and rollback capability |
| Operate | Reliable service, learning loops, and controlled change |
| Retire | Data export, migration, communication, and decommissioning |

## Machine status

Today this repository is a text-first, agent-native decision framework with a
structured catalog. People and capable agents can use it directly by reading and
writing versioned Markdown and YAML; the absence of a CLI, API, database, or service
does not prevent normal use.

Automation should begin with a small, deterministic conformance validator for checks
that language models should not judge by themselves: schemas, stable IDs, references,
links, legal state transitions, blocker policy, and reproducible reports. A CLI may
wrap that validator for convenience, but it is not the product or a required
interface. APIs, databases, interactive navigators, and a larger graph engine remain
optional and require evidence of a real need. This boundary is defined in
[ADR-0003](decisions/ADR-0003-text-first-agent-native-architecture.md).

## Status

This is version `0.7`: the graph-ready documentation includes governed adversarial
self-improvement, pivot lineage, attraction and distribution questions, reconciled
human/agent/robot integration and financial-continuity controls, stable question IDs,
machine-validatable schemas, a governed domain-pack interface, assurance and improvement
templates, a vendor-neutral coding-agent protocol, explicit news and organizational
buying questions, and a worked example. The full reference-engine stack is deferred;
the next justified automation is an optional conformance validator that preserves the
text files as canonical state. See the [changelog](CHANGELOG.md).
