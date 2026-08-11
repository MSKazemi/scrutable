# Product Questionbook

> Questions for the whole software lifecycle.

Product Questionbook is a reusable question system for designing, reviewing, and improving software products.

The goal is not to create a product with the most features. The goal is to make important decisions explicit, expose unknowns early, and build a product that is useful, usable, secure, reliable, operable, and sustainable.

## What this repository is

- **Project:** this repository and all work used to develop Product Questionbook.
- **Framework:** the question banks, methods, evidence rules, structured catalog, schemas, and templates in this repository.
- **Application:** a future interactive implementation that can navigate the question graph, track answer state, and generate project artifacts.

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
6. Read [the output, brainstorming, convergence, and implementation contract](docs/09-output-convergence-and-implementation.md) for the canonical result, cross-question correction algorithm, convergence rules, and initial stack. The stack choice is recorded in [ADR-0001](decisions/ADR-0001-engine-implementation-stack.md).
7. Use the [structured graph foundation](docs/structured-foundation.md) for stable IDs, typed relationships, state history, schemas, and reusable domain packs.
8. Use the [governed self-improvement and adversarial review method](docs/10-self-improvement-and-adversarial-governance.md) when challenging an idea, finding the controlling bottleneck, evaluating a pivot, or improving the framework. Its governance decision is recorded in [ADR-0002](decisions/ADR-0002-governed-adversarial-self-improvement.md).
9. Follow the [usage, project placement, visibility, and agent-integration protocol](docs/11-usage-deployment-and-agent-integration.md) to apply the framework to another repository or run it with Codex, ChatGPT, Claude Code, or another agent system.
10. Record results using the [run manifest](templates/run-manifest.md), [agent run request](templates/agent-run-request.md), [product brief](templates/product-brief.md), [decision record](templates/decision-record.md), [naming brief](templates/naming-brief.md), [bottleneck register](templates/bottleneck-register.md), [risk register](templates/risk-register.md), [review scorecard](templates/review-scorecard.md), [improvement cycle](templates/improvement-cycle.md), and [adversarial review](templates/adversarial-review.md).
11. Review the [coverage gaps and expansion backlog](docs/12-coverage-gaps-and-expansion-backlog.md) before claiming comprehensive support or promoting new question domains.

The accepted framework name and its limitations are recorded in [the naming decision](decisions/0001-product-questionbook-name.md).

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

See the [machine contract](docs/08-machine-operation-and-outputs.md) for the state machine, knowledge graph, structured Markdown format, output directory, integration boundaries, and completion rules. See the [output and convergence contract](docs/09-output-convergence-and-implementation.md) for brainstorming, answer correction, cyclic dependencies, fixed-point rules, termination, and the proposed implementation stack.

## Structured graph foundation

The graph layer converts the documentation-first framework into machine-validatable
question templates and project-specific instances without replacing the existing
human-readable question banks.

The initial foundation includes:

- [framework vision and boundaries](docs/vision.md), [terminology](docs/terminology.md), and [domain model](docs/domain-model.md);
- an explicit [question state machine](docs/question-state-machine.md), [priority model](docs/prioritization.md), and [coverage matrix](docs/coverage-model.md);
- [output](docs/output-contract.md) and [assurance](docs/assurance-rules.md) contracts;
- JSON Schemas for questions, instances, answers, relationships, project profiles, and governed improvement cycles in [`schemas/`](schemas/);
- 99 starter templates with 322 typed dependencies and activations across 16 domains in [`catalog/`](catalog/);
- reusable assurance and improvement templates plus a worked project-specific example.

The graph is the machine-readable source of truth. Matrices, backlogs, reports, and
documents are projections of it.

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

Today this repository is a documentation-first decision framework with a validated
structured catalog. It does not yet contain an executable parser, API, database,
graph engine, or autonomous runtime.

The target machine will select applicable questions, maintain question state, link evidence and decisions in a graph, generate artifacts, evaluate gates, and reopen affected nodes when context changes. Its governed improvement loop will attack unsupported claims, find the controlling bottleneck, compare pivots with stopping, measure prediction error, and propose—but not autonomously publish—framework changes. It reduces blind spots and makes uncertainty auditable; it cannot guarantee real-world success.

## Status

This is version `0.7`: the graph-ready documentation includes governed adversarial
self-improvement, pivot lineage, attraction and distribution questions, reconciled
human/agent/robot integration and financial-continuity controls, stable question IDs,
machine-validatable schemas, reusable domain packs, assurance and improvement
templates, a vendor-neutral coding-agent protocol, explicit news and organizational
buying questions, and a worked example. The reference stack is proposed but not yet
validated by an executable architecture spike. See the [changelog](CHANGELOG.md).
