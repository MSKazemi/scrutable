# ADR-0001: Reference engine implementation stack

**Status:** Proposed  
**Date:** 2026-08-11  
**Owner:** Repository maintainers  
**Review trigger:** Phase 1 implementation start, failed architecture spike, or material deployment constraint change

## Context

The Product Questionbook needs an executable reference engine that parses Markdown and YAML, validates typed records, maintains a directed multigraph, propagates changes, evaluates policies and gates, exposes a CLI and API, and generates deterministic artifacts.

The engine is not a hard real-time controller. AI, workflow, CI, and robot/device integrations are adapters outside the deterministic decision core.

## Decision criteria

1. Correct and inspectable validation and state transitions.
2. Strong graph and testing support.
3. Low complexity for the first executable milestone.
4. Human-readable canonical artifacts and machine-readable projections.
5. Reproducible builds and dependency locking.
6. Ability to add an API and optional LLM adapters without coupling the core to them.
7. A migration path from local runs to a multi-user service.

## Decision

Use Python 3.13+ for the initial reference implementation, with this baseline:

- `uv` and `pyproject.toml` for environments, dependency locking, and packaging;
- `markdown-it-py` and `ruamel.yaml` for source parsing and round-trip-safe structured metadata;
- Pydantic 2 and JSON Schema for domain and artifact validation;
- NetworkX `MultiDiGraph` for reference graph algorithms;
- Typer for the CLI and FastAPI for the optional HTTP API;
- SQLite for local execution and PostgreSQL for service deployment;
- SQLAlchemy 2 and Alembic for persistence and migrations;
- Jinja2 for deterministic Markdown rendering;
- pytest and Hypothesis for example-based, state-machine, invariant, and property testing;
- Ruff and mypy for code quality and static type checking.

Pin exact versions in a lockfile when implementation begins. This ADR selects components and compatibility families, not immutable package versions.

## Rationale

Python keeps the schema, graph, CLI, API, and evaluation code in one typed language. Pydantic models can expose JSON Schema, FastAPI uses Python types and OpenAPI for API contracts, NetworkX represents attributed nodes and edges and supplies the algorithms needed for dependency analysis, and Typer exposes typed local commands. A relational node/edge model avoids operating a second database category before requirements justify it.

Relevant primary documentation:

- [Pydantic documentation](https://docs.pydantic.dev/latest/)
- [NetworkX graph documentation](https://networkx.org/documentation/stable/reference/classes/graph.html)
- [FastAPI features and standards](https://fastapi.tiangolo.com/features/)
- [Typer documentation](https://typer.tiangolo.com/)
- [SQLAlchemy ORM documentation](https://docs.sqlalchemy.org/en/20/orm/)
- [`uv` dependency management](https://docs.astral.sh/uv/concepts/projects/dependencies/)
- [pytest documentation](https://docs.pytest.org/en/stable/)

## Consequences

Positive:

- fast path from documents to validated graph and CLI;
- deterministic core can run without a server or LLM;
- schemas can be reused by artifacts, API clients, and tests;
- local and service modes can share domain logic.

Negative:

- NetworkX is an in-process reference engine, not the durable multi-user store;
- Python is unsuitable for a safety-critical real-time control loop;
- round-trip Markdown/YAML editing and deterministic rendering require explicit tests;
- PostgreSQL graph traversal may need careful indexing or later specialization.

## Rejected initial alternatives

- **TypeScript-first:** strong for a web UI, but the first milestone is a validation and graph engine rather than a browser application. A TypeScript client can consume generated JSON Schema or OpenAPI later.
- **Dedicated graph database first:** premature operational complexity without measured traversal or scale requirements.
- **LLM-agent framework as the core:** would make deterministic validation, reproducibility, and provider independence harder. LLMs remain optional candidate-generation adapters.
- **Direct robot/device control:** outside the system boundary and incompatible with the assurance level of a documentation and decision engine.

## Validation

Before changing this ADR to `Accepted`, build an architecture spike that:

1. parses representative question and answer documents without losing structured metadata;
2. validates schemas and emits actionable errors;
3. detects SCCs, propagates a changed node, and produces a stable impacted-node set;
4. runs the same gate twice with identical output;
5. exports Markdown and JSON with trace-equivalent IDs;
6. passes performance thresholds defined for a representative graph size;
7. completes dependency, license, and security review.

Reverse or revise the decision if the spike fails, deployment forbids Python, graph size or concurrency exceeds the measured design envelope, the team cannot operate the stack, or safety requirements place execution inside a real-time control boundary.
