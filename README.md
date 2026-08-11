# Product Questionbook

> Questions for the whole software lifecycle.

Product Questionbook is a reusable question system for designing, reviewing, and improving software products.

The goal is not to create a product with the most features. The goal is to make important decisions explicit, expose unknowns early, and build a product that is useful, usable, secure, reliable, operable, and sustainable.

## What this repository is

- **Project:** this repository and all work used to develop Product Questionbook.
- **Framework:** the question banks, methods, evidence rules, and templates in this repository.
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
7. Record the result using the [product brief](templates/product-brief.md), [decision record](templates/decision-record.md), [naming brief](templates/naming-brief.md), [bottleneck register](templates/bottleneck-register.md), and [review scorecard](templates/review-scorecard.md).

The accepted framework name and its limitations are recorded in [the naming decision](decisions/0001-product-questionbook-name.md).

## How it works

1. Establish the subject, lifecycle stage, desired outcome, constraints, and decision that the review must enable.
2. Classify each aspect as critical, important, relevant, or not applicable.
3. Ask only questions that can change a decision, expose a risk, or define verification.
4. Record answers with evidence, assumptions, unknowns, decisions, owners, and review triggers.
5. Propagate each important answer into requirements, decisions, risks, experiments, metrics, tests, approvals, or operational procedures.
6. Evaluate lifecycle gates. Critical safety, security, privacy, legal, reliability, or data-loss gaps block progress even when other areas score well.
7. Reopen affected questions when evidence, dependencies, users, scale, regulation, incidents, or strategy change.

## Outputs

The canonical result is a **versioned decision and assurance package backed by a traceable knowledge graph**. The reusable question bank is framework input; answers are validated run state; specifications, ADRs, tests, and gate reports are linked projections. A completed review therefore produces a bundle rather than a single score:

- a product or system brief;
- a question and evidence ledger;
- decision records;
- requirements and acceptance criteria;
- risks, blockers, mitigations, and owners;
- experiments, research, and follow-up actions;
- integration and verification plans;
- success metrics, guardrails, operational controls, and support ownership;
- a gate result: proceed, proceed with conditions, pause, or stop;
- an audit trace and change-impact report.

See the [machine contract](docs/08-machine-operation-and-outputs.md) for the state machine, knowledge graph, structured Markdown format, output directory, integration boundaries, and completion rules. See the [output and convergence contract](docs/09-output-convergence-and-implementation.md) for brainstorming, answer correction, cyclic dependencies, fixed-point rules, termination, and the proposed implementation stack.

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

Important conclusions from conversations, research, reviews, and experiments must be distilled into the appropriate Markdown file. A material result is not considered incorporated until its decision, evidence, owner, and implications are recorded here. See [the working method](docs/00-method.md#repository-propagation-rule).

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

Today this repository is a documentation-first decision framework. Humans and language-model agents can follow its Markdown, but it does not yet contain an executable parser, API, database, graph engine, or autonomous runtime.

The target machine will select applicable questions, maintain question state, link evidence and decisions in a graph, generate artifacts, evaluate gates, and reopen affected nodes when context changes. It reduces blind spots and makes uncertainty auditable; it cannot guarantee real-world success.

## Status

This is version `0.4`: a broad, graph-ready foundation with explicit output, brainstorming, convergence, correction, and implementation contracts. The reference stack is proposed but not yet validated by an executable architecture spike. See the [changelog](CHANGELOG.md).
