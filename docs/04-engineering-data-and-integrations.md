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

## Human, agent, robot, platform, and world integration

I1. Which humans, teams, organizations, AI agents, robots, devices, platforms, and physical environments participate in each end-to-end outcome?
I2. What information, command, material, money, identity, or responsibility crosses each boundary?
I3. Which work should be performed by a person, deterministic software, an AI agent, or a physical machine, and why?
I4. Where must a person consent, confirm, supervise, override, appeal, or take control?
I5. How are state, intent, uncertainty, progress, failure, and required action communicated across human and machine participants?
I6. How is every human, service, agent, robot, and device discovered, addressed, identified, authenticated, authorized, scoped, suspended, and revoked?
I7. What goals, instructions, tools, credentials, data, time, budget, cost, rate, delegation chain, and autonomy limits constrain an AI agent?
I8. How are agent actions, memory, provenance, delegated authority, and resulting changes audited and corrected?
I9. How do multiple agents coordinate ownership, prevent duplicate work, detect stale plans or fabricated capabilities, resolve conflict, and stop loops or deadlocks?
I10. How are prompt injection, untrusted agent messages, tool abuse, data leakage, and compromised external agents contained?
I11. What assumptions about location, localization, lighting, weather, people, terrain, connectivity, calibration, payload, energy, sensors, and actuators constrain a robot or device?
I12. What physical hazards exist, and which safe operating envelope, interlock, fail-safe state, emergency stop, safety boundary, and manual recovery or override are required?
I13. What happens during lost power or connectivity, stale or delayed commands, noisy or degraded sensors, clock drift, uncertain world state, actuator failure, or unsafe environmental change?
I14. How are calibration, maintenance, inspection, firmware, inventory, fleet rollout, and hardware end-of-life controlled?
I15. Which workflows require real-time latency, clock synchronization, geospatial accuracy, or deterministic ordering?
I16. Which platform certification, policy, quota, permission, commercial term, release cycle, interface limitation, or lock-in can block the product, and can the product move to a viable alternative?
I17. How do organizational processes, contracts, support teams, and accountability boundaries align with the technical integration?
I18. Are automated and physical interactions usable and accessible to people with different abilities, languages, expertise, and levels of connectivity?
I19. Which simulations, sandboxes, digital twins, contract tests, supervised pilots, or field trials validate behavior before full exposure?
I20. Can the complete interaction be observed, safely degraded, handed to a person, disconnected, replaced, and reconstructed after failure?

## Performance and capacity

43. Which user-visible operations need latency targets, and at which percentiles?
44. What are expected and peak users, requests, data volume, payload size, and growth?
45. Where are CPU, memory, storage, network, connection, queue, and vendor limits?
46. How will the system behave under overload: reject, queue, degrade, prioritize, or shed work?
47. Which workloads require caching, batching, asynchronous work, or precomputation?
48. How will capacity be measured, forecast, tested, and expanded?
49. What performance budget applies to clients, APIs, pages, and background jobs?
50. Could a performance optimization damage correctness, accessibility, cost, or maintainability?
