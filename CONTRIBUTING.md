# Contributing questions

Product Questionbook is useful only when its questions are clear, reusable, traceable, and
capable of changing a decision.

## Before adding a question

Check whether an existing question can be refined, related, or given a better
activation rule. Avoid duplicates that differ only in wording.

A good question:

- exposes a consequential unknown, assumption, constraint, or risk;
- can be answered for a defined subject;
- states why the answer matters;
- identifies the evidence needed for high-impact claims;
- activates, depends on, or informs other work;
- is neutral and does not embed a preferred answer;
- is small enough to have a clear owner and state.

## Required fields

New templates must conform to [`schemas/question.schema.json`](schemas/question.schema.json)
and include a stable ID, question text, purpose, domain, lifecycle stages, answer
type, criticality, evidence expectations, and expected outputs.

Use IDs of the form `domain.topic.NNN`. IDs are permanent: deprecate a published
question instead of reusing its ID for a different meaning.

## Review checklist

- Is the question applicable to more than one project?
- Could two reasonable people interpret it the same way?
- Does it overlap with an existing question?
- Are dependencies and activations expressed as template IDs?
- Can the required evidence actually be produced or inspected?
- Does the question avoid promising that a single answer guarantees success?
- Is `criticality` proportionate to the consequence of getting the answer wrong?

Template publication follows `draft -> reviewed -> published -> deprecated`.

## Domain packs

A specialized pack must follow the [domain-pack governance contract](docs/17-domain-pack-governance.md) and conform to [`schemas/domain-pack.schema.json`](schemas/domain-pack.schema.json). Repository maintainership or agent authorship is not domain qualification. Do not mark a pack `reviewed` or `published` without current authoritative sources, qualified scoped approvals, blocker and waiver rules, positive and negative scenarios, incident or audit evidence, limitations, expiry, and affected-run behavior.

