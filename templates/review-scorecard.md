---
artifact: review-scorecard
run_id: "<run-id>"
project_id: "<project-id>"
subject_id: "<subject-id>"
review_id: "<review-id>"
scrutable_ref: "<git-commit-sha>"
graph_revision: 0
generated_at: "<ISO-8601 timestamp>"
---

# Product review scorecard: [Product name]

**Review gate:** Problem / Scope / Architecture / Release / Post-launch / Retirement
**Reviewer(s):** [Names]
**Date:** [YYYY-MM-DD]

## Rating scale

| Rating | Meaning |
| --- | --- |
| 0 | Not considered; no owner or evidence |
| 1 | Major gaps; unacceptable risk |
| 2 | Partly defined; important evidence or controls missing |
| 3 | Adequate for the current stage; known gaps are owned |
| 4 | Strong evidence, verification, ownership, and review loop |
| N/A | Not applicable, with a documented reason |

## Assessment

| Aspect | Importance | Rating | Evidence | Most important gap | Owner and due date |
| --- | --- | --- | --- | --- | --- |
| Vision and outcomes | | | | | |
| Users and stakeholders | | | | | |
| Problem and context | | | | | |
| Market and positioning | | | | | |
| Scope and prioritization | | | | | |
| User experience and content | | | | | |
| Accessibility and inclusion | | | | | |
| Functional behavior | | | | | |
| Data and intelligence | | | | | |
| Architecture and maintainability | | | | | |
| Integrations and interoperability | | | | | |
| Security, privacy, safety, and abuse | | | | | |
| Performance, scalability, and reliability | | | | | |
| Quality and delivery | | | | | |
| Operations and support | | | | | |
| Business and economics | | | | | |
| Legal, compliance, and governance | | | | | |
| Ethics and sustainability | | | | | |
| Measurement and learning | | | | | |
| Evolution and retirement | | | | | |
| Naming and identity | | | | | |

## Blockers

A blocker is a critical gap that cannot be neutralized by a high score elsewhere.

- [ ] No unresolved critical user-value assumption
- [ ] No unresolved critical accessibility gap
- [ ] No unresolved critical security, privacy, safety, or abuse risk
- [ ] No unresolved legal or contractual prohibition
- [ ] No unresolved data-loss or recovery risk
- [ ] No unresolved public-name collision, reputation, or search-visibility blocker
- [ ] No unresolved unsafe human-agent-robot-system authority, handoff, physical-action, or safe-stop behavior
- [ ] No unresolved funding, staffing, adoption, vendor, or critical-path gap; committed resources cover the next decision milestone and downside triggers and a continuity plan are documented
- [ ] Release, rollback, monitoring, incident response, and support are ready

## Decision

**Result:** Proceed / Proceed with conditions / Pause / Stop

**Conditions and rationale:**

[Decision, remaining gaps, owners, and deadlines.]

**Next review trigger or date:** [Trigger or YYYY-MM-DD]
