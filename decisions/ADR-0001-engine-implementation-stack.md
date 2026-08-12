# ADR-0001: Deferred reference engine implementation stack

**Status:** Deferred and constrained by [ADR-0003](ADR-0003-text-first-agent-native-architecture.md)  
**Date:** 2026-08-11  
**Updated:** 2026-08-12  
**Owner:** Repository maintainers  
**Review trigger:** Measured need for a multi-user service, interactive application, or integration that cannot be served by the text protocol and optional validator

## Context

This ADR originally proposed a Python application containing parsing, graph algorithms,
a CLI, an HTTP API, persistence, rendering, and evaluation. That proposal treated a
full reference engine as the next milestone.

Product Questionbook is now explicitly text-first and agent-native. People and agents
can apply it directly through versioned Markdown, YAML, JSON Schema, and Git. A
database, service, API, or mandatory CLI would add deployment and maintenance cost
without currently removing the controlling bottleneck.

## Current decision

Do not implement the full stack as the next milestone.

The next justified automation is a small deterministic conformance validator that:

- reads canonical repository files without requiring a database;
- is read-only by default;
- checks only mechanically decidable rules;
- emits human-readable Markdown and machine-readable JSON reports;
- can be called by CI, an agent, a library API, or an optional thin command;
- never becomes the owner of canonical run state.

A command-line entrypoint may be added for convenience, but use of the framework must
not depend on it. FastAPI, PostgreSQL, SQLAlchemy, Alembic, a durable graph service, and
an interactive application are deferred until measured use demonstrates a need.

## Preserved implementation candidate

If the review trigger is reached, the earlier candidate remains available for a new
spike:

- Python with pinned dependencies;
- round-trip-safe Markdown and YAML handling;
- typed models and JSON Schema validation;
- explicit graph algorithms;
- scenario, invariant, state-machine, and property testing;
- an optional CLI or HTTP adapter;
- persistence selected only when concurrent durable state is required.

No package in that candidate is approved merely because it appeared in the original
proposal. The spike must compare the smallest validator design with the larger service
design.

## Acceptance evidence for expansion

A larger engine may be proposed only when at least one measured requirement cannot be
met reliably through the text protocol plus validator, such as:

1. concurrent multi-user writes requiring transactions;
2. graph size or query latency exceeding file-based processing limits;
3. a stable external API contract required by multiple consumers;
4. access-control or audit requirements requiring a managed service;
5. usability evidence showing that an interactive navigator materially reduces missed
   blockers or completion cost.

The proposal must quantify operating cost, migration, portability, lock-in, security,
and the risk that generated state diverges from canonical text.

## Consequences

Positive:

- the framework remains inspectable, portable, vendor-neutral, and easy for agents to
  load;
- users do not need to install or operate an application;
- deterministic checks can still become repeatable and required in CI;
- future interfaces remain replaceable adapters.

Trade-offs:

- agents and people continue to manage files and review diffs directly;
- a validator cannot replace human judgment about evidence quality, ethics, strategy,
  usefulness, or risk acceptance;
- richer multi-user workflows are postponed until demand is demonstrated.

ADR-0003 is authoritative for the architecture boundary.
