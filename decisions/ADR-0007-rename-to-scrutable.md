# ADR-0007: Rename the framework and repository to Scrutable

**Status:** Accepted
**Date:** 2026-08-15
**Owner:** Repository maintainer
**Supersedes:** [`0001-product-questionbook-name.md`](0001-product-questionbook-name.md)
**Review trigger:** A material collision, a failed legal or search validation, evidence that
the name is not understood by new readers, or commercial adoption requiring clearance

## Context

`0001-product-questionbook-name.md` (2026-08-11) adopted **Product Questionbook** as a
working name. It recorded honestly that it was "a preliminary screen, not trademark
clearance", and it deferred the naming brief, the full search-visibility audit, and
candidate generation.

RUN-2026-0002 (2026-08-13) executed the audit half of `docs/07` against the existing name
and returned `proceed_with_conditions`. It found the name legally and technically clear —
every identifier free, no brand collision, 14 same-name repositories with at most 6 stars —
but found that a quoted `"Questionbook"` search returned 10/10 book results, because the
engine rewrites the token to `question book`. That run's recommendation (A-04) was to keep
the name and instead own the *compound* (`questionbook framework`, `questionbook agent`).
It explicitly excluded generating alternatives (`00-manifest.md:77`).

This decision executes the deferred half — action A-06 — and revises A-04's recommendation
on new evidence.

## Decision

Rename the framework to **Scrutable** and the repository to `MSKazemi/scrutable`.

- **Canonical spelling:** Scrutable (capitalized in prose, `scrutable` as an identifier)
- **Pronunciation:** SKROO-tuh-buhl
- **Short descriptor:** an evidence-bound decision and assurance framework for software products
- **Tagline:** Questions for the whole software lifecycle. *(unchanged)*
- **Meaning:** "capable of being understood by careful examination" — the property the
  framework confers on a product's readiness

## Evidence

31 candidates were generated across five naming territories (the gate, the test of purity,
structured questioning, graph traversal, and coined marks) and screened mechanically against
GitHub, PyPI, npm, and RDAP for `.com`, `.org`, and `.io`. The `.dev` column was **discarded**
as non-evidence: the Google RDAP endpoint failed its positive control (`web.dev` returned 404),
the same endpoint failure RUN-2026-0002 recorded. All other endpoints passed controls in both
directions.

Searches were run on Google on 2026-08-15, IT locale.

| Candidate | Rewrite test (Q68) | Result-space owner (Q65) | Outcome |
| --- | --- | --- | --- |
| `askwright` | **fail** — the quoted search was overridden: "These are results for *arkwright*" | Arkwright Consulting, Richard Arkwright, a board game, a VC fund | Rejected despite being the only candidate with perfect availability |
| `gatewright` | pass | `gatewright.com` is a live San Francisco R&D and IT firm; also a novel series and an FPGA tool | Rejected — same-sector confusion (Q54) |
| `questionbook` | **fail** — `"product questionbook"` was rewritten to *product question book* | Book and exam-prep commerce | Incumbent defect reconfirmed |
| `questionbook framework github` | **fail** — 10/10 question-bank and QA-system repositories, annotated "Missing: framework" | Quiz software | A-04's premise falsified |
| `scrutable` | pass — the token survives quoted search | Dictionaries, plus an established term of art in explainable-AI research | **Selected** |
| `scrutable framework github` | pass | Small academic repositories at ≤2 stars; no commercial owner | Q67 satisfied |

## Rationale

The decisive distinction is between an **inert** and a **competing** result space. Dictionary
entries for a rare adjective do not contend for a searcher's intent. Question-bank software
does: a reader looking for this framework and finding quiz-generation repositories has been
actively misdirected, and `docs/07` line 101 rules against exactly that.

`Scrutable` also carries meaning the previous name did not. It is already a term of art in
explainable-AI and recommender-systems research — arXiv and ACM use "scrutable" for a system
whose reasoning a user can inspect and challenge — which is precisely what an evidence-bound
assurance framework does to a product. That is adjacent-field credibility, and it makes the
category legible without a descriptor doing all the work.

A-04's recommendation was not wrong when it was written; it was untested. When tested, the
compound failed the same way the bare word did.

## Consequences

- Availability at 2026-08-15T15:17Z: PyPI, npm, and `scrutable.io` are free;
  **`scrutable.org` is registered**; the GitHub handle `scrutable` is taken but dormant
  (created 2017, zero public repositories). `MSKazemi/scrutable` was free and is now claimed.
- Repository collisions are weak and in unrelated domains: `moonymachine/scrutable-objects`
  (103 stars, Unity game development), and two repositories named `scrutable` at 1 and 0 stars.
  This is a larger collision surface than `questionbook` had, and it is accepted.
- The name is **not self-explanatory** on first contact. Every surface must pair it with the
  short descriptor. This is the cost the previous name did not carry.
- The artifact contract changes: `questionbook_ref` becomes `scrutable_ref`, the run-package
  directory `.questionbook/` becomes `.scrutable/`, and `schema_version: questionbook-run/v0.1`
  becomes `scrutable-run/v0.1`. This is a breaking change to the output contract, taken now
  because the framework has been public for two days and the switching cost is at its lifetime
  minimum (`docs/07` Q59).
- `0001-product-questionbook-name.md` and the CHANGELOG entries recording the previous name are
  left **unaltered** as historical records. The dated audit snapshots in `docs/13`, `docs/15`,
  and `docs/19` carry a note that the framework was renamed after the audit date.
- Old repository URLs redirect; GitHub preserves repository identity across a rename.

## Limitations

This is not trademark clearance and no legal review was performed. Trademark status is
`unknown`. Search results vary by date, country, language, personalization, and engine.
Per `docs/07` Q75, re-run the recorded queries before any commercial adoption.
