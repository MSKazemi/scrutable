# External sensing and attention

## What this mechanism can and cannot guarantee

Scrutable can require a visible, owned, evidence-backed process for
collecting external signals and for acting when they change a decision. It cannot
guarantee that every person, company, agent, website, news outlet, regulator, or
community will reveal a change, see a product, pay attention, or respond.

Two different systems must not be confused:

| Direction | Goal | Canonical questions |
|---|---|---|
| Outside to project | Detect changes that can invalidate decisions | operations.sensing-change.001 through operations.sensing-blind-spots.001 |
| Project to audience | Earn qualified discovery, evaluation, adoption, and trust | business.attention-audience.001 through the attraction and distribution module |

High reach is not reliable sensing. Large attention is not qualified adoption. A news
mention is evidence only for what it directly establishes, not for product value or
future success.

## The sensing loop

Use the eight records in
[catalog/operations/external-sensing-questions.yaml](../catalog/operations/external-sensing-questions.yaml)
in this order:

1. define decision-changing external changes;
2. map each change to multiple appropriate sources;
3. assign owners, cadence or event triggers, reliability checks, and access-failure
   handling;
4. predefine thresholds and the graph nodes, decisions, limits, or contingencies they
   affect;
5. assess provenance, independence, corroboration, manipulation, and dissent;
6. budget time from change to detection, interpretation, decision, and action;
7. reconstruct missed and late signals against the time-stamped record;
8. preserve blind spots as explicit unknowns, exposure reductions, contingencies, or
   accepted risks.

The output is not a feed. It is a change-to-decision control loop: changes lead to an
owned source portfolio; observations are assessed and correlated; thresholds and
latency budgets trigger node reopening and action; outcomes and misses correct the
next cycle.

## Source portfolio

Select sources for the concern, not because they are easy to search. The portfolio can
include:

- primary laws, regulators, standards bodies, courts, and official notices;
- supplier, platform, marketplace, registry, security, and dependency advisories;
- customer and operator research, support evidence, communities, and field reports;
- company filings, contractual notices, procurement changes, and partner evidence;
- instrumented market, product, service, financial, and operational telemetry;
- qualified researchers, analysts, journalists, public-interest groups, and news;
- search engines, web monitoring, AI agents, and specialized databases as discovery
  intermediaries.

An intermediary must link back to inspectable underlying evidence where the claim is
consequential. Model memory, search snippets, unattributed posts, duplicated stories,
and vendor marketing do not become independent corroboration merely because many
channels repeat them.

For each source, record the concern and graph nodes it covers, owner, access method,
cadence or event trigger, provenance, likely bias, independence, timeliness, expected
failure mode, last successful check, and fallback source. Use the
[external signal register](../templates/external-signal-register.md).

## Signal assessment

Keep the raw observation separate from interpretation and action. Assess these
dimensions explicitly:

| Dimension | Question |
|---|---|
| Directness | Did the source observe the event or repeat another source? |
| Authority | Is it authoritative for this exact claim, jurisdiction, or dependency? |
| Provenance | Can the original record, time, author, and transformations be inspected? |
| Independence | Do apparently separate reports depend on the same origin? |
| Recency | Is it current enough for the decision and its detection-delay budget? |
| Corroboration | Do independent sources support or conflict with it? |
| Manipulation risk | Who benefits if the project believes or amplifies the signal? |
| Scope fit | Does it apply to this subject, use, population, market, and revision? |

Record each dimension as high, medium, low, or unknown with a reason. Do not collapse
a critical provenance, authority, or scope failure into an average score. Weak signals
may create an investigation or limited precaution without being accepted as fact.

## Threshold and propagation algorithm

For every material signal class, define before collection:

1. the minimum observation or corroboration that creates an alert;
2. which accepted answers and downstream decisions become dirty;
3. whether exposure is monitored, limited, paused, or stopped while evidence is
   uncertain;
4. who may interpret, decide, waive, or accept residual risk;
5. the maximum delay for detection, interpretation, decision, and action;
6. the contingency if sources are unavailable or disagree.

When the threshold is met, preserve the old answer and evidence, add the new signal
with its observation time and collection time, reopen affected nodes, propagate
through reverse dependencies, and issue a new gate result. Do not silently rewrite
history.

If the threshold is not met but the possible consequence is critical, keep the signal
in a disputed or weak-signal queue with a next check, owner, and bounded precaution.
Absence of evidence is not evidence that the external state is unchanged.

## Missed-signal review

After a surprise, incident, late response, or invalidated decision, reconstruct:

- when the external change occurred and when it became observable;
- which sources contained a usable signal and when;
- whether collection, access, classification, correlation, escalation, decision, or
  action failed;
- which graph nodes should have reopened;
- whether the latency budget was realistic;
- which source, ownership, threshold, contingency, or catalog change is justified.

Retain negative findings, including cases where more monitoring would not have helped.
The learning loop must not optimize for alert volume or hindsight.

## Agent and web use

Codex, ChatGPT, Claude Code, or another agent can execute the text protocol when it has
authorized access to the selected sources. The agent must report source boundaries,
query and time window, retrieval time, failures, transformations, citations, and
uncertainty. It must distinguish no result from proof of no event and must not claim
continuous monitoring unless a separately authorized recurring process actually
exists.

External writes, outreach, subscriptions, spending, or contacting people require
separate authorization. Reading public or connected sources for an authorized run does
not authorize the agent to publish, notify, or act on behalf of the user.

## Completion condition

External sensing is justified only when every material change has either:

- an owned, accessible, sufficiently timely source and tested threshold-to-action
  path; or
- an explicit blind spot with exposure reduction, contingency, residual-risk owner,
  and review trigger.

This is guaranteed visibility of the **process and its blind spots**, not guaranteed
visibility of the world and not guaranteed attention from an audience.
