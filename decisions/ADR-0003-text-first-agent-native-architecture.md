# ADR-0003: Text-first, agent-native architecture

**Status:** Accepted  
**Date:** 2026-08-12  
**Owner:** Repository maintainers  
**Review trigger:** A measured usability, scale, concurrency, access-control, or integration need cannot be met by the text protocol plus optional validator

## Context

Scrutable is intended to help people and agents turn unclear ideas into
evidence-backed decisions and project documentation. Its artifacts must remain easy to
inspect, edit, review, version, migrate, and use across different agent platforms.

A full application with a mandatory CLI, API, database, and graph runtime could make
simple use harder, introduce hidden state, and couple the framework to one deployment
model. Pure prose without deterministic checks has the opposite problem: agents and
people can silently create duplicate IDs, broken references, illegal states, or gate
results that violate declared policy.

The architecture therefore needs to remain text-first without becoming text-only.

## Decision

1. **The primary interface is versioned text.** Humans and agents read and write
   Markdown and YAML directly. JSON Schema defines structural contracts, and Git
   records revisions and reviewable diffs.
2. **No application is required for normal use.** A run must remain possible without
   installing a CLI, starting a service, or operating a database.
3. **Canonical state stays in the files.** A graph is the logical relationship model.
   The graph.json file, indexes, databases, and reports are reproducible projections or
   caches, never silent alternative sources of truth.
4. **Deterministic validation is optional support and may become required governance.**
   A small validator should enforce mechanically decidable rules and may run in CI.
   It must be read-only by default and emit revision-pinned Markdown and JSON reports.
5. **A CLI is only a convenience adapter.** The same validator must be callable by an
   agent, CI, or library interface. The framework must not require users to learn CLI
   commands.
6. **Larger runtime components are evidence-gated.** APIs, databases, interactive
   navigators, multi-user services, and durable graph engines are deferred until
   measured requirements justify their security, migration, maintenance, and
   operational cost.
7. **Judgment remains accountable.** Code can check structure and declared policy; it
   cannot decide whether evidence is credible, a product is useful, a trade-off is
   ethical, or a consequential risk is acceptable. Those decisions require identified
   owners and approvals.

## Responsibility boundary

| Layer | Owns | Must not own |
| --- | --- | --- |
| Markdown/YAML protocol | Questions, run state, evidence links, decisions, risks, outputs | Hidden generated state |
| Agent | Context discovery, drafting, analysis, challenge, propagation, file updates | Fabricated evidence or self-approval |
| Deterministic validator | Schemas, IDs, references, links, legal transitions, blocker and gate rules, reproducibility checks | Product judgment or canonical state |
| Human/accountable owner | Evidence acceptance, priorities, exceptions, approvals, risk acceptance | Silent unreviewed rule changes |
| Optional adapters | Convenience invocation, external integration, presentation | A proprietary replacement contract |

## Minimum validator behavior

The first validator should:

- operate offline on a pinned repository snapshot;
- validate structured records and internal links;
- detect duplicate or dangling IDs, self-references, and forbidden cycles;
- enforce allowed state transitions and conditional required fields;
- check evidence, ownership, blocker, approval, and gate invariants that are encoded in
  versioned policy;
- produce deterministic reports without rewriting source files unless a separate,
  explicit formatting or migration action is requested;
- fail safely when a rule is unknown or cannot be evaluated.

Its implementation language and packaging are secondary to these behaviors. A shell
command may exist, but it is not the architecture.

## Consequences

Positive:

- immediate compatibility with repository-capable agents;
- portability across vendors and operating environments;
- human-readable reviews and recoverable Git history;
- low setup cost for a first run;
- deterministic protection against structural drift without hiding the reasoning.

Trade-offs:

- file coordination is less convenient for concurrent multi-user editing;
- an agent still needs disciplined context loading and evidence rules;
- some semantic checks require a versioned policy vocabulary before they can be
  automated;
- interactive navigation and rich dashboards are deferred.

## Expansion test

Before adding a mandatory runtime component, document:

1. the observed failure or unmet requirement;
2. evidence that text plus validator cannot solve it adequately;
3. the smallest adapter that would solve it;
4. how canonical text remains exportable and authoritative;
5. security, privacy, migration, operating-cost, and vendor-lock-in consequences;
6. a removal or reversal path.

This ADR constrains [ADR-0001](ADR-0001-engine-implementation-stack.md) and is
normative for future implementation work.
