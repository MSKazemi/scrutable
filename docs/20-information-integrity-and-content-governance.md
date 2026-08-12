# Information integrity and content governance

## Purpose and boundary

This method governs content and claims that a product creates, transforms, imports,
ranks, recommends, stores, or distributes. It covers misinformation, impersonation,
defamation, manipulation, synthetic media, moderation, reviewer safety, correction,
appeal, transparency, and propagation to downstream systems and agents.

It does not authorize a universal truth classifier, guarantee the truth of content, or
make the framework an arbiter of lawful expression. Provenance can show where content
came from and how it changed; it cannot by itself prove that the content is true.
Authentic content can mislead, anonymous content can be accurate, and a policy-compliant
statement can still become harmful when removed from its context.

## Integrity loop

Use the eight questions in
[catalog/ethics/information-integrity-questions.yaml](../catalog/ethics/information-integrity-questions.yaml)
as one loop:

1. classify consequential content, actors, contexts, and possible harms;
2. define provenance, authenticity, citation, labeling, and custody requirements;
3. state contextual policies and enforcement thresholds;
4. test manipulation, coordination, impersonation, deepfakes, spam, and evasion using
   proportionate data;
5. provide review, notice, escalation, appeal, correction, and restoration;
6. measure errors, consistency, bias, reviewer workload and safety, and correction
   time;
7. provide safe and appropriate transparency and qualified access;
8. propagate corrections, disputes, expiry, removals, and restoration downstream.

Record the result in the
[content integrity register](../templates/content-integrity-register.md). Keep the raw
content and observation, provenance, interpretation, policy decision, action, appeal,
and propagation result as separate records.

## Content and context classification

Begin with content function and consequence rather than controversial keywords. The
classification records:

- user, employee, partner, imported, generated, transformed, or synthetic origin;
- claim, instruction, identity representation, media, ranking signal, review,
  advertisement, public record, or other function;
- intended and plausible unintended audiences;
- language, culture, jurisdiction, public or private space, and distribution scale;
- whether the content affects safety, health, finance, employment, civic participation,
  reputation, rights, access, or another material outcome;
- reversibility, velocity, virality, and vulnerability of affected parties.

The same content can require different handling in different contexts. A classification
change reopens the relevant policy, assurance, and propagation questions.

## Provenance and authenticity

Choose controls in proportion to consequence. Available controls include source
citation, author or publisher identity at an appropriate assurance level, signed
metadata, edit history, generation and transformation disclosure, content credentials,
watermarks, hashes, custody logs, and linked primary evidence.

Every provenance claim states what it proves and what it does not. A label must be
tested for human and machine comprehension, accessibility, persistence through
transformation, resistance to removal or forgery, and behavior when metadata is
missing. Missing provenance becomes unknown; it is not automatically proof of
deception.

## Contextual policy

Each policy version defines:

- covered content, actors, product surfaces, languages, jurisdictions, and contexts;
- prohibited, restricted, labeled, down-ranked, age-gated, quarantined, disputed, and
  allowed states;
- thresholds, exceptions, public-interest considerations, and urgent-harm rules;
- automation and human-review boundaries;
- the evidence preserved for decisions and appeals;
- notice, explanation, appeal, correction, restoration, and expiry behavior;
- decision and residual-risk authority.

Private communications, public distribution, professional advice, satire, documentary
evidence, political speech, and content involving children or vulnerable people can
require different rules. Qualified legal and domain review is required when rights,
regulation, or safety make generic policy insufficient.

## Manipulation and proportionate detection

Test coordinated behavior and content together. Manipulation can involve identity
fraud, coordinated accounts, copied narratives, synthetic media, engagement gaming,
brigading, evasion, or abuse of recommendation and reporting systems.

Detection must record necessity, proportionality, data minimization, retention,
access, likely bias, and abuse potential. Do not collect broad relationship, identity,
or behavioral data merely because it could improve detection. When a less intrusive
control provides adequate protection, use it.

An automated score may prioritize review or limit exposure under a published rule; it
does not become accepted evidence merely because the model is confident. Critical
actions require the review and authority specified by policy.

## Adjudication, appeal, and correction

For each action, preserve:

1. content and version reference;
2. observation and evidence available at the time;
3. applicable policy version and rule;
4. automated and human decision steps;
5. action, scope, duration, and decision authority;
6. notice and explanation;
7. appeal route and independence;
8. correction, restoration, or compensation when wrong;
9. downstream propagation and acknowledgement.

Urgent harm may justify a temporary, bounded action before full review when policy
defines the evidence threshold, time limit, reviewer, notice, and restoration path.
Temporary action must not silently become permanent.

## Reviewer safety and assurance

Measure at least:

- false positives and false negatives using representative samples;
- error and outcome differences across relevant languages, groups, and contexts;
- agreement and explainable disagreement among reviewers;
- appeal rate, overturn rate, correction time, restoration completeness, and repeat
  failure;
- reviewer exposure, workload, queue age, fatigue, trauma risk, access to support, and
  unsafe productivity pressure;
- evasion success, manipulation detection delay, and adversarial regression results;
- residual stale copies and downstream acknowledgement.

Sampling limitations and unknown ground truth remain visible. A low overall error rate
cannot average away a severe failure for a vulnerable group or a high-consequence
content class.

## Transparency and qualified access

Transparency can include policy versions, aggregate enforcement and appeal measures,
known limitations, correction performance, provenance coverage, risk assessments,
and independent audit findings. Researcher or regulator access must be scoped,
purpose-bound, logged, and protected against privacy breaches, security compromise,
reviewer identification, and release of abuse-enabling details.

The framework does not assume that maximum disclosure is always safe. It requires an
explicit balance among accountability, privacy, security, legal duties, trade secrets,
reviewer safety, and public interest.

## Downstream systems and agents

Content integrity decisions must reach every material consumer: caches, search
indexes, feeds, embeddings, retrieval stores, trained or adapted models, AI agents,
partners, exports, archives, analytics, and human decisions.

A propagation protocol records the original and corrected version, reason and policy
authority, affected recipients, tombstone or replacement mechanism, acknowledgement,
remaining stale copies, possible learned model influence, and next verification.
Deleting a source record does not prove that derived systems stopped using it.

Agents generating or transforming content must preserve citations and provenance,
identify transformations, disclose relevant uncertainty, distinguish observation from
inference, and obey correction or dispute status. They must not fabricate provenance,
watermarks, source agreement, human review, or downstream acknowledgement.

## Gate conditions

A positive gate is blocked when an applicable high-consequence content class has:

- no accountable policy owner or versioned contextual rule;
- unknown provenance treated as authenticated or true;
- no urgent-harm, notice, appeal, correction, or restoration path;
- detection that lacks necessity, proportionality, privacy, or abuse review;
- unmeasured material false-positive, false-negative, bias, or reviewer-safety risk;
- no tested downstream correction path;
- an unresolved legal, rights, safety, or qualified domain-pack requirement.

Completion means that applicable risks have an owned and tested control or an
explicitly authorized residual risk with scope and review date. It does not mean that
all harmful content will be found or that every content decision is objectively true.
