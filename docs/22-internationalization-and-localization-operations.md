# Internationalization and localization operations

## Purpose and boundary

This method covers the operational system required to serve people and organizations
across languages, scripts, locales, cultures, time zones, payment environments, tax
regimes, identity methods, contracts, and market-specific support obligations. It
connects translation governance, right-to-left and locale mechanics, local commercial
requirements, multilingual support and incident communication, local validation,
parity measurement, and market exit to explicit evidence and decisions.

It is not a substitute for qualified legal, tax, accounting, payments, accessibility,
linguistic, cultural, or local-market review. A translated string, a locale library,
or a machine-generated translation is not evidence that a journey, contract, safety
message, payment, or support process works in a market.

## Conditional operating loop

Use the eight questions in
[`catalog/operations/internationalization-localization-questions.yaml`](../catalog/operations/internationalization-localization-questions.yaml)
as one conditional loop:

1. define the markets, languages, scripts, locales, workflows, and obligations in
   scope;
2. verify right-to-left, bidirectional, input, font, search, sort, name, address,
   calendar, unit, formatting, expansion, export, and accessibility behavior end to
   end;
3. assign terminology, translation-memory, source, review, release, and correction
   ownership;
4. identify market-specific laws, taxes, prices, payments, identity methods,
   contracts, notices, and records;
5. demonstrate support, escalation, incident, and safety communication in the
   required language and time zone;
6. obtain evidence from representative local users and qualified reviewers;
7. measure feature, quality, content, support, and incident-response parity by
   locale; and
8. prepare a lawful, supported, and humane market pause or exit.

Record the result in the
[localization readiness register](../templates/localization-readiness-register.md).

## Scope and applicability

Start with markets and real user journeys, not a language list. A single language can
have multiple legal, currency, tax, payment, identity, address, calendar, support,
and cultural contexts. A single market can require several languages, scripts, and
accessibility paths. Record at least:

- supported and affected user groups, including non-users and operators;
- languages, scripts, writing direction, locale variants, time zones, and fallback
  behavior;
- critical journeys and high-consequence content classes;
- commercial, contractual, tax, payment, identity, privacy, support, and incident
  obligations;
- channels, vendors, reviewers, owners, release cadence, and exit dependencies;
- evidence source, date, confidence, jurisdiction, and review trigger.

A market or locale that is advertised, contractually promised, safety relevant, or
used by a material population remains in scope even when feature coverage is
incomplete.

## Locale mechanics and right-to-left behavior

Test complete journeys with realistic mixed-language and mixed-direction content.
The test model should include, where applicable:

- right-to-left layout, mirroring, focus order, navigation, icons, charts, maps, and
  bidirectional text isolation;
- keyboard and input-method composition, cursor movement, selection, validation,
  copy and paste, speech, scanning, and assistive technology;
- font availability, shaping, ligatures, fallback, glyph coverage, line breaking,
  truncation, text expansion, and zoom;
- Unicode normalization, identifiers, names, addresses, phone numbers, postal codes,
  currencies, decimals, dates, calendars, time zones, units, and plural rules;
- locale-aware sort, search, tokenization, collation, transliteration, matching, and
  error recovery;
- generated documents, email, notifications, logs, exports, imports, receipts,
  invoices, audit records, support tools, and incident channels;
- accessibility behavior with local language, script, reading order, labels, error
  text, and user preferences.

A screenshot of one translated screen is not end-to-end evidence. Preserve test data,
expected results, environments, devices, browsers, assistive technologies, and known
unsupported combinations.

## Translation and content governance

Define one authoritative source and a controlled content lifecycle. For each content
class, record:

- source owner, terminology owner, glossary, style guide, translation memory, and
  approved locale variants;
- translator and reviewer qualifications, independence, local context, and conflict
  escalation;
- whether machine translation, generated content, or vendor automation is permitted,
  prohibited, or requires human review;
- risk tier for contractual, privacy, safety, security, financial, medical,
  accessibility, support, and incident content;
- version, effective date, release synchronization, fallback language, stale-content
  threshold, and correction propagation;
- vendor access, confidentiality, data handling, continuity, quality measurement, and
  exit plan.

Do not silently publish the source language when a required high-consequence
translation is absent or stale. Record the explicit fallback, user impact, owner, and
release decision.

## Local commercial and legal operation

For every market, determine whether pricing, tax, invoicing, payment methods,
settlement, refunds, identity, age or eligibility checks, consumer rights, contract
formation, notices, records, accessibility, privacy, data location, support, or
termination changes product behavior.

Use current authoritative sources and qualified owners. News, search, vendors, and
models can help locate or compare evidence but do not provide legal, tax, accounting,
or regulatory clearance. When local payment or financially valuable flows are
present, activate the
[financial-crime module](../catalog/security/financial-crime-questions.yaml). When
contracts or foreseeable losses change, activate the
[liability and insurance module](../catalog/legal/liability-insurance-questions.yaml).
A regulated or safety-critical market may also require a qualified domain pack.

## Multilingual support and incident communication

Support and incident capability includes more than translated help-center pages.
Test:

- staffed language and time-zone coverage, handoff, escalation, and surge capacity;
- authenticated primary and fallback channels;
- diagnostic access, privacy, evidence preservation, and interpreter or translation
  controls;
- localized safety instructions, status updates, next-update times, corrections, and
  recovery messages;
- comprehension by affected users under realistic urgency and channel constraints;
- continuity when a vendor, network, account, region, or qualified reviewer is
  unavailable.

When an event requires public or stakeholder-specific communication, use the
[crisis-communication module](../catalog/operations/crisis-communication-questions.yaml)
as well as the ordinary incident process.

## Local validation and parity

Local validation should include representative users and qualified local reviewers,
not only internal bilingual staff. Preserve disagreement where cultural fit, trust,
meaning, or harm is contested. Test normal, error, recovery, support, payment,
contract, accessibility, privacy, incident, and exit journeys.

Parity does not require identical features in every market. It requires an explicit,
justified, observable decision about which outcomes, safeguards, quality levels,
support targets, notices, and recovery capabilities are equivalent or intentionally
different. Measure at least:

- journey and feature availability;
- translation freshness and terminology defects;
- locale-specific functional, accessibility, payment, tax, contract, support, and
  incident defects;
- severity, population, exposure duration, workaround, and correction time;
- complaints, support demand, failed transactions, abandonment, harms, and outcomes
  by locale;
- delayed releases and unsupported promises.

A critical locale defect or missing required safeguard blocks release for that market
unless an authorized, lawful, time-bounded alternative protects affected users.

## Market pause and exit

A market exit plan covers authority, triggers, notice, support, refunds, contract
termination, export, data retention and deletion, accessibility, incident handling,
partner and payment obligations, records, surviving duties, and affected users who
lack alternatives. Test primary and fallback communication in the relevant languages.
Do not use market exit to erase outstanding claims, records, safety duties, or user
rights.

## Agent use and permissions

An agent can maintain inventories, compare locale assets, identify missing tests,
prepare test cases, calculate parity metrics, retrieve authorized sources, and draft
messages or decisions. It must preserve source, locale, jurisdiction, version,
retrieval time, uncertainty, reviewer identity or qualification boundary, and failed
retrievals.

Separate explicit authorization is required before publishing translations or crisis
messages, changing prices or taxes, accepting legal conclusions, moving funds or
personal data, changing contracts, suspending a market, or contacting users,
authorities, vendors, or partners.

## Gate conditions

A positive market or release gate is blocked when:

- the locale, market, or high-consequence content scope is unknown;
- a critical journey has untested right-to-left, bidirectional, input, font, search,
  sort, format, export, or accessibility behavior;
- terminology, source, review, release, or correction ownership is missing;
- a material local legal, tax, payment, identity, contractual, privacy, or support
  obligation lacks current qualified interpretation;
- required support, incident, or safety communication cannot operate in the relevant
  language and time zone;
- representative local validation is absent for a material user or harm scenario;
- a critical locale defect or parity gap lacks an approved protective response; or
- market suspension or exit would abandon users or surviving obligations.

Structural completion means that each applicable question has an owner, current
evidence, decision, blocker or accepted residual risk, and revisit trigger. It does
not prove that every market implementation is correct; representative runs and
qualified local review remain necessary.
