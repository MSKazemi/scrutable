# ADR-0004: License the framework under Apache-2.0

**Status:** Accepted  
**Date:** 2026-08-13  
**Owner:** Repository maintainer  
**Review trigger:** A decision to commercialize, a request for a different license from a
material adopter, a contribution that arrives under an incompatible license, or a patent
concern raised by a contributor or adopter

## Context

The repository had **no license file**. Under default copyright, publishing it would
grant no one the right to use, copy, modify, or redistribute the material. For an
artifact whose entire purpose is reuse by other teams, that made public release
meaningless: an adopter could read the questions but could not lawfully build on them.

This was recorded as the first blocker (BLOCK-01) of the framework's self-assessment run
at revision `a80c9653`.

The repository is mixed-content. It contains prose (30 normative documents), structured
data (199 catalog questions, 8 JSON Schemas), templates intended to be copied verbatim
into other projects, and now a Python validator. A license had to work for all four.

## Decision

License the entire repository under **Apache License 2.0**, with `LICENSE` holding the
verbatim license text and `NOTICE` naming the copyright holder.

## Options considered

| Option | Assessment |
|---|---|
| **Apache-2.0** | Permissive, so it maximizes adoption for a framework whose value depends on reuse. Includes an explicit patent grant and a contribution clause, which the MIT license lacks. Widely pre-approved in corporate legal review — the population most likely to adopt an assurance framework. Applies cleanly to code, schemas, and prose. |
| MIT | Simpler and equally permissive, but has no patent grant and no explicit contribution term. For a framework describing assurance processes, the patent clause is cheap insurance. |
| CC-BY-4.0 | The natural fit for prose, and a poor fit for the JSON Schemas, templates, and validator. Creative Commons itself recommends against using CC licenses for software. Would have required dual-licensing. |
| Dual CC-BY-4.0 (docs) + Apache-2.0 (code) | Most technically precise, and it puts a licensing decision in front of every adopter and every contributor. The boundary between "docs" and "code" here is genuinely unclear — a catalog YAML file is both. Complexity not justified at this size. |
| Copyleft (GPL / MPL) | Would discourage exactly the internal corporate adoption this framework is aimed at, and offers little protection for prose that is meant to be copied into project run packages. |

## Rationale

The framework's value is proportional to how many teams reuse it, and templates are
*designed* to be copied into other repositories. Any license creating obligations on
those copies would work against the purpose. Apache-2.0 keeps that path frictionless
while providing the patent and attribution terms that make institutional adoption
straightforward.

Choosing one license for the whole repository, rather than splitting by file type, is a
deliberate simplification: the split would be ambiguous in practice and would force every
adopter to reason about it.

## Consequences

- Anyone may use, modify, and redistribute the framework, including commercially, while
  retaining the license and attribution notices.
- Copies of `templates/` inside another project inherit Apache-2.0. This is intended.
- Contributions are licensed under the same terms by the Apache-2.0 contribution clause;
  no separate CLA is required.
- Relicensing later would require the agreement of every contributor. While the project
  has a single author this is trivially reversible; it stops being trivial after the
  first external contribution. **Revisit before merging the first outside contribution.**
- This ADR does not address trademark. The name is a separate decision, recorded in
  [`0001-product-questionbook-name.md`](0001-product-questionbook-name.md), and Apache-2.0
  grants no trademark rights.
