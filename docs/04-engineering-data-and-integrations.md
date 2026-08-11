# Engineering, data, and integration questions

## Architecture and maintainability

1. What quality attributes matter most, and what measurable scenarios define them?
2. What is the simplest architecture that meets current evidence and constraints?
3. Where are the domain boundaries, responsibilities, and sources of truth?
4. Which decisions are expensive to reverse, and which can be deferred?
5. Where must the system tolerate independent change, deployment, or failure?
6. What consistency model is required for each workflow?
7. How are configuration, feature flags, secrets, and environment differences managed?
8. Which dependencies are critical, unmaintained, duplicated, or difficult to replace?
9. What technical debt is intentional, what is its carrying cost, and when will it be reviewed?
10. Can a new engineer understand, run, test, and safely change the system?
11. How are architecture decisions documented and checked against implementation?
12. What happens if scale remains small—are we paying unnecessary complexity costs?

## Data lifecycle and analytics

13. What data is necessary for the user outcome, and what data is merely convenient?
14. What is the authoritative source, owner, definition, sensitivity, and quality target for each important field?
15. How is data created, validated, transformed, synchronized, corrected, archived, exported, and deleted?
16. Which identifiers are stable, unique, guessable, or personally identifying?
17. What retention period applies, and how is deletion propagated to copies, caches, logs, backups, and vendors?
18. How will schema changes and backfills be deployed and verified?
19. What happens when data is missing, late, duplicated, contradictory, corrupted, or out of order?
20. Can users inspect and correct important data about themselves?
21. Are analytics events consistently named, versioned, validated, consent-aware, and linked to decisions?
22. Can reported metrics be reproduced from documented definitions and lineage?

## Search, algorithms, and AI

23. What user decision or task is the algorithm helping with?
24. Is automation necessary, and where is a deterministic rule or human process better?
25. What data and evaluations represent real users, languages, edge cases, and harms?
26. Which accuracy, relevance, latency, cost, fairness, and safety thresholds apply?
27. How are uncertainty, provenance, limitations, and generated content communicated?
28. When must a person review, override, appeal, or correct a result?
29. How will prompt injection, unsafe output, data leakage, model drift, and vendor change be handled?
30. Are model, prompt, dataset, and evaluation versions traceable to each release?
31. What is the fallback when the model or search service is unavailable or low-confidence?
32. How will live quality be sampled without violating privacy?

## APIs and integrations

33. Who owns each side of the contract, and how will changes be coordinated?
34. What authentication, authorization, scopes, and tenant boundaries apply?
35. Are schemas, units, time zones, encodings, identifiers, and error semantics unambiguous?
36. How are versioning, compatibility, deprecation, and consumer migration handled?
37. What are the timeout, retry, backoff, idempotency, ordering, pagination, and rate-limit rules?
38. How are duplicates, delayed messages, replay, partial failure, and poison events handled?
39. Can integration failures be diagnosed across system boundaries without exposing secrets?
40. What sandbox, fixtures, contract tests, documentation, and support do integrators receive?
41. Can users import and export in useful, documented, non-proprietary formats?
42. What is the exit plan if a vendor raises prices, changes terms, degrades, or shuts down?

## Performance and capacity

43. Which user-visible operations need latency targets, and at which percentiles?
44. What are expected and peak users, requests, data volume, payload size, and growth?
45. Where are CPU, memory, storage, network, connection, queue, and vendor limits?
46. How will the system behave under overload: reject, queue, degrade, prioritize, or shed work?
47. Which workloads require caching, batching, asynchronous work, or precomputation?
48. How will capacity be measured, forecast, tested, and expanded?
49. What performance budget applies to clients, APIs, pages, and background jobs?
50. Could a performance optimization damage correctness, accessibility, cost, or maintainability?
