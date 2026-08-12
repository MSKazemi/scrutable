# Prose-to-catalog coverage

## Purpose

The human-readable question banks are intentionally richer than the reusable graph.
That is useful only when the relationship is explicit. The
[coverage manifest](../coverage/prose-to-catalog.yaml) accounts for every numbered
question in the seven main question-bank documents and connects it to published
catalog records or marks it as guidance.

The manifest solves the previous accounting gap. It does not claim that 115 reusable
templates are semantically identical to hundreds of detailed questions.

## Current snapshot

| Measure | Value |
|---|---:|
| Source question-bank files | 7 |
| Numbered questions accounted for | 396 |
| Section mapping groups | 43 |
| Exact mappings claimed | 0 |
| Compressed mappings | 388 |
| Unmodeled questions inside the declared source scope | 0 |
| Guidance-only prompts | 8 |
| Published catalog questions referenced | 95 distinct IDs out of 115 available |

The conservative `exact: 0` result is deliberate. This first manifest records
section-level many-to-many compression and preserves the full source wording. An
independent semantic review may later promote individual mappings to `exact`; an agent
must not infer exact equivalence merely because two questions share keywords.

`unmodeled: 0` applies only to the existing numbered question banks. It does not mean
that every possible concern is modeled. Candidate questions and missing domains remain
in the [coverage backlog](12-coverage-gaps-and-expansion-backlog.md).

## Coverage states

| State | Meaning |
|---|---|
| `exact` | The source question and catalog record have the same decision and failure semantics |
| `compressed` | Detailed source wording is preserved while a smaller stable set drives graph selection and propagation |
| `unmodeled` | No adequate published catalog record exists |
| `guidance_only` | The prompt helps facilitation or brainstorming but cannot independently satisfy an assurance gate |

Compression is not deletion. A run that activates a compressed group must retain the
applicable detailed source questions as review guidance. The stable catalog records
provide reusable identity and relationships; they do not authorize an agent to ignore
failure modes present only in the prose.

## Stable source identity

Each question receives a source identity:

```text
<path>::<section-anchor>::<visible-label>
```

For example:

```text
docs/04-engineering-data-and-integrations.md::human-agent-robot-platform-and-world-integration::i12
```

The manifest also preserves the complete source text. A future validator must fail
when a source question is added, removed, relabeled, moved between sections, or changed
without a corresponding manifest revision.

## Required integrity checks

Whether performed by a human or a future agent adapter, a coverage review must verify:

1. every in-scope question appears exactly once;
2. every manifest source path and section exists;
3. every stored source text matches the pinned source revision;
4. every `catalog_id` resolves to a published or explicitly deprecated record;
5. summary counts equal the expanded group contents;
6. `exact` or `compressed` groups have at least one catalog ID;
7. guidance-only items are never counted as verified assurance coverage;
8. unmodeled and compressed concerns remain visible in gate and backlog reports;
9. a changed mapping records its reviewer, rationale, compatibility effect, and
   evidence.

The manifest conforms to
[`../schemas/prose-coverage.schema.json`](../schemas/prose-coverage.schema.json).
Schema validation checks structure; semantic comparison with the Markdown sources and
catalog still requires deterministic validation or a documented manual review.

## Promotion path

Do not respond to compressed mappings by automatically creating one catalog record per
sentence. Promote a dedicated stable question only when its answer can change a
decision, expose a distinct material failure, activate different work, require
different evidence or ownership, or repeatedly gets lost during runs.

Promotion proceeds as:

1. identify a compressed or unmodeled source question;
2. compare it with the existing catalog and run evidence;
3. propose a reusable neutral question with applicability, evidence, outputs, owner
   roles, dependencies, activations, and revisit triggers;
4. review overlap, criticality, compatibility, and migration;
5. publish or reject the proposal;
6. update the manifest, relevant prose, changelog, and any affected run guidance.

This preserves a compact graph without allowing important prose detail to disappear.
