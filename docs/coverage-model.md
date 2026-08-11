# Coverage matrix

The coverage matrix is generated from question instances. Lifecycle stages are rows;
concern domains are columns. A question can contribute to multiple cells.

## Lifecycle stages

| Stage | Central concern |
|---|---|
| `discover` | Is there a worthwhile, understood problem and affected population? |
| `define` | Are outcomes, scope, requirements, constraints, and ownership explicit? |
| `design` | Is the proposed experience and system approach coherent and testable? |
| `build` | Can the approach be implemented safely and consistently? |
| `verify` | Does accepted evidence show the system meets its declared criteria? |
| `release` | Are exposure, migration, support, and rollback controlled? |
| `operate` | Can the service be observed, supported, secured, and recovered? |
| `evolve` | Can changes be made without losing intent, compatibility, or assurance? |
| `retire` | Can users, data, obligations, and dependencies be exited responsibly? |

## Concern domains

The starter matrix uses: core purpose, users, product and naming, UX and
accessibility, architecture, data, security and privacy, reliability, performance,
quality, operations, business, legal and compliance, team and governance, ethics and
societal impact, and retirement.

## Cell summary

Each cell contains:

- total applicable questions;
- counts by state;
- verified critical questions;
- unresolved critical questions;
- accepted risks;
- missing or expired evidence;
- next recommended question.

The detailed list must remain accessible from every aggregate count. A green cell
without traceability to its questions, evidence, and risk decisions is not meaningful.

