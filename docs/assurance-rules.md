# Assurance rules

Scrutable distinguishes catalog coverage, answered questions, verified claims, and
accepted risk. A high answer count alone is not assurance.

## Question-complete criteria

A subject is question-complete for a declared scope and graph revision only when:

1. Every applicable critical question is `verified` or covered by a formally accepted risk.
2. Every high-impact answer has the evidence required by its template or a documented exception.
3. No unresolved contradiction affects a critical decision or release criterion.
4. Important decisions have an accountable owner and link to supporting answers.
5. Success measures, failure conditions, and their tests are defined.
6. No critical answer is stale.
7. `not_applicable` decisions have recorded reasons.
8. Accepted critical risks have an owner, rationale, authority, and future review date.

## Readiness levels

| Level | Meaning |
|---|---|
| `unknown` | Applicability has not been evaluated |
| `exploring` | Critical unknowns or unowned blockers remain |
| `defined` | Scope, stakeholders, outcomes, and critical risks are identified |
| `evidenced` | Applicable critical claims are verified or formally accepted as risks |
| `ready` | The declared gate's criteria are satisfied for this graph revision |
| `degraded` | A material change or stale critical answer invalidated prior readiness |

Readiness is always qualified: for example, “ready for a limited beta in Italy at
graph revision 17,” not simply “ready.”

## Coverage measures

Report counts and weighted percentages by domain and lifecycle stage:

- applicable questions;
- verified questions;
- unresolved critical questions;
- blocked and stale questions;
- answers missing required evidence;
- formally accepted risks;
- unowned decisions and actions.

Do not combine `not_applicable` with `verified`, and do not count an accepted risk as
verified. Both may satisfy a completion gate, but they communicate different exposure.

## Honest guarantee

Passing these rules shows that the catalog's applicable critical concerns received an
explicit, traceable treatment. It does not guarantee adoption, profitability,
delivery quality, safety, compliance, or the absence of unknown unknowns.

