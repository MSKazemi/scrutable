# Trust, quality, and operations questions

## Security

1. What assets, actors, entry points, trust boundaries, and threats exist?
2. What is the likely impact and likelihood of each credible threat?
3. Is every request authenticated and authorized at the resource and action level?
4. Are privileges minimal, time-bounded where possible, reviewed, and quickly revocable?
5. How are credentials, tokens, keys, certificates, and secrets created, stored, rotated, and revoked?
6. How are inputs validated and outputs safely encoded for their destination?
7. How are dependencies, artifacts, builds, and deployment provenance protected?
8. What prevents cross-tenant access, injection, forgery, replay, enumeration, and unsafe file handling?
9. Which actions require tamper-evident audit history or separation of duties?
10. How will vulnerabilities be discovered, prioritized, patched, disclosed, and verified?
11. What is logged for investigation without recording secrets or excessive personal data?
12. Has the threat model been tested by people independent of the implementation?

## Privacy, safety, and abuse

13. What personal or sensitive data is collected, inferred, shared, or exposed?
14. What is the purpose and lawful basis for each use, and could less data achieve it?
15. Are notice, consent, choice, access, correction, deletion, and portability meaningful and usable?
16. Can users control visibility, sharing, discovery, notifications, and personalization?
17. What harms could arise from normal use, error, misuse, coercion, or unexpected combination with other data?
18. What abuse is profitable, scalable, difficult to detect, or targeted at vulnerable people?
19. How will suspicious behavior be prevented, rate-limited, challenged, reviewed, appealed, and reported?
20. Could safety controls themselves create discrimination, surveillance, or denial of legitimate use?
21. What requires age assurance, guardian involvement, content controls, or crisis escalation?
22. How will incidents be contained, users protected, authorities notified where required, and lessons tracked?

## Reliability and resilience

23. Which user journeys require service-level indicators and objectives?
24. What availability, durability, freshness, and recovery targets are justified by user impact?
25. What are the single points of failure and correlated failure modes?
26. What happens when a database, region, network, queue, cache, identity provider, or vendor fails?
27. Are timeouts, retries, circuit breakers, queues, and fallbacks bounded to avoid cascading failure?
28. Can the product provide a safe degraded mode?
29. Are backups encrypted, isolated, retained appropriately, and restored in realistic drills?
30. Can recovery meet the recovery-time and recovery-point objectives?
31. How will data be reconciled after partial or prolonged failure?
32. Are resilience assumptions tested through game days or failure injection?

## Quality and testing

33. What could fail silently, irreversibly, or with high user impact?
34. Which behavior belongs in unit, integration, contract, end-to-end, exploratory, accessibility, performance, and security tests?
35. Does the test portfolio cover boundaries, permissions, concurrency, time, locales, failure, migration, and rollback?
36. Are test environments and data representative without exposing production information?
37. Are tests deterministic, fast enough, diagnostically useful, and owned?
38. Which quality checks block a release, and who may approve an exception?
39. How are escaped defects classified, learned from, and converted into prevention?
40. What must be validated manually because automation would provide false confidence?

## Delivery and change safety

41. Is every artifact reproducible, signed or traceable, and tied to reviewed source?
42. Are environments promoted consistently with controlled configuration differences?
43. How are database, API, event, client, and configuration changes made backward-compatible?
44. Can a release be canaried, progressively exposed, paused, and rolled back quickly?
45. What happens to in-flight work and mixed-version clients during deployment?
46. Are feature flags owned, observable, access-controlled, and removed after use?
47. What evidence and approvals are required before production?
48. How will emergency changes be controlled and reviewed afterward?

## Observability, incidents, and support

49. Can operators determine whether users are succeeding, not merely whether servers are running?
50. Do logs, metrics, traces, events, and audit records share useful correlation identifiers?
51. Are alerts tied to user impact, actionable, deduplicated, and routed to a capable owner?
52. Are dashboards, runbooks, ownership, escalation, and communication channels current?
53. Who is on call, what authority do they have, and is the load sustainable?
54. How are incidents declared, coordinated, contained, communicated, and reviewed?
55. Can support safely diagnose issues while respecting access control and privacy?
56. How are support themes connected to product priorities and documentation?
57. What maintenance windows, status communication, and customer commitments apply?
58. Are operational readiness and recovery exercised before launch?
