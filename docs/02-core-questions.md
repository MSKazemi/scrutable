# Core questions for every software product

These are the minimum questions to answer before committing substantial time or money. Detailed question banks expand each area.

## Purpose and value

1. What change should this product create, for whom, and why does it matter now?
2. What painful or valuable job is the user trying to complete?
3. How do people solve it today, including doing nothing?
4. What evidence shows that the problem is real, frequent, and important?
5. What unique value will make users choose and continue using this product?
6. Which outcome would justify the product's cost and risk?

## Naming and identity

N1. What should the name help the intended audience understand, feel, remember, and expect?
N2. Can intended users pronounce, spell, recall, search for, and distinguish the name?
N3. What linguistic, cultural, legal, trademark, domain, package, app-store, and account-name risks must be cleared?

Continue with the detailed [naming and identity questions](07-naming-and-identity.md).

## People and context

7. Who are the primary users, buyers, administrators, operators, and affected non-users?
8. In what physical, social, technical, and emotional context will they use it?
9. Which abilities, languages, devices, bandwidth levels, and levels of expertise must be supported?
10. What incentives or conflicts exist among stakeholders?
11. Who could be excluded, manipulated, or harmed?

## Scope and behavior

12. What is the smallest complete outcome the first release must enable?
13. What is explicitly out of scope, and why?
14. What are the critical user journeys from entry to successful completion?
15. What business and domain rules determine correct behavior?
16. What permissions, states, transitions, limits, and edge cases exist?
17. How can users prevent, understand, and recover from mistakes?

## Evidence and success

18. What observable user and business outcomes define success?
19. What guardrail metrics show harm, poor quality, or unhealthy behavior?
20. What baseline and target will be used, over what period?
21. What would make us change direction, pause, or stop?
22. How will qualitative feedback and quantitative data reach decision-makers?

## Technology and data

23. What system qualities are critical: security, privacy, safety, availability, latency, scale, accessibility, or maintainability?
24. What data is required, who owns it, where does it come from, and how long should it exist?
25. What architecture is the simplest one that satisfies known constraints?
26. Which external systems and vendors can fail, change, become expensive, or disappear?
27. How will the product be tested, observed, deployed, rolled back, recovered, and supported?

## Trust and responsibility

28. What can attackers, insiders, careless users, or automated abuse do?
29. What personal, confidential, regulated, or safety-critical information is involved?
30. What laws, contracts, standards, licenses, and organizational policies apply?
31. Which decisions require human judgment, appeal, explanation, or audit history?
32. What is the worst credible failure, and how will we prevent, detect, contain, and learn from it?

## Sustainability and lifecycle

33. Who owns the product after launch, and what capacity do they have?
34. What are the build, infrastructure, support, compliance, and change costs?
35. How will the product evolve without breaking users or integrations?
36. How can users export their data and leave?
37. How will data, dependencies, and communication be handled if the product is retired?

## Release gate

Before launch, can the team demonstrate—not merely claim—that:

- the main user can complete the critical journey;
- important accessibility paths work;
- access control and data handling are correct;
- critical risks have owners and mitigations;
- service objectives and capacity are adequate;
- monitoring, support, incident response, backup, recovery, and rollback are ready;
- legal and operational approvals are complete;
- success and guardrail metrics can be measured?
