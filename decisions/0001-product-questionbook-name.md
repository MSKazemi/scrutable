# Decision: Use Product Questionbook as the framework name

> **Superseded on 2026-08-15 by [ADR-0007](ADR-0007-rename-to-scrutable.md).** The framework
> is now named **Scrutable** and the repository is `MSKazemi/scrutable`. This record is kept
> unaltered: it states what was decided on 2026-08-11 and what evidence supported it at that
> time. Do not read it as current.

**Status:** Superseded by ADR-0007 (was: accepted as a working name)
**Date:** 2026-08-11
**Owner:** Repository owner
**Review trigger:** Public launch, commercial use, a material collision, or failed legal/search validation

## Context

The repository needed a name for a reusable system of questions covering the whole software-product lifecycle. The name must describe the framework honestly without promising that a checklist guarantees a perfect product.

The repository slug remains `mohsen`; this decision names the framework inside the repository.

## Decision criteria

1. Immediate clarity about the contents and purpose.
2. Memorability and reasonable pronunciation and spelling.
3. Distinction from generic surveys and checklists.
4. Room to expand into domain packs, templates, software, or a book.
5. Acceptable preliminary search and repository collision risk.

## Options considered

| Candidate | Assessment |
| --- | --- |
| Product Questionbook | Directly describes a reusable collection and system of product questions |
| Product Atlas | Attractive metaphor, but related active use was found |
| Product Prism | Suggests multiple perspectives, but `Prism` is heavily used in software |
| ProductQ | Short, but related active use was found and meaning is less immediate |
| Mohsen | Appropriate as a repository placeholder but does not explain the framework to a new reader |

## Decision

Use **Product Questionbook** with the tagline:

> Questions for the whole software lifecycle.

## Rationale

The name explains the artifact on first contact, distinguishes it from a one-time questionnaire, and allows future expansion. The wording makes a modest promise: systematic questions, not guaranteed perfection.

## Evidence and limitations

A preliminary exact-name web and GitHub check reported no obvious exact collision on 2026-08-11. Related uses were found for alternatives such as [Product Atlas](https://productatlas.app/), [ProductQ](https://www.productq.co/services/), and [Prism](https://github.com/mo0rti/prism).

This was a preliminary screen, not trademark clearance. Search results, registrations, domains, repositories, packages, and accounts change. Before public or commercial adoption, complete the [naming brief](../templates/naming-brief.md), run the full [search visibility and collision audit](../docs/07-naming-and-identity.md#search-visibility-and-collision-audit), and obtain proportionate legal review.

## Consequences

- Documentation uses Product Questionbook as the framework name.
- The current repository URL may continue to use `mohsen` until the owner renames it.
- The name must be reconsidered if audience testing shows poor comprehension or if search, reputation, technical, or legal checks identify a blocker.
