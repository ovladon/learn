## Technical implementation update — 2026-10-22

- Created a **separate** Neon feedback project in Frankfurt; no Vercel app or cost added.
- Neon Function `learnfeedback` deployment completed. Public health route; private `/ingest` and `/diagnostics` require a server-only secret, never shipped to visitors.
- Atomic, opt-in-only anonymous aggregation schema is deployed: 5,000 accepted submissions/day global, 300/topic/day and rolling 28-day diagnostic/suggested-revision views. Project consumption quotas are configured.
- **Blocked activation:** no connected protected edge/Worker and no verified live HTTPS ingestion test. GitHub Pages Quest **does not transmit results automatically**. Do not expose credentials to bypass this boundary.
- No real submissions have been collected and no educational text has been auto-rewritten.
- Implementation and release prerequisites: [backend/neon/learnfeedback/README.md](backend/neon/learnfeedback/README.md).

# LEARN — Autonomous Learning Quality Loop

## Goal
Student reads → plays a three-question lesson-specific quest → the system records **coarse anonymous aggregate counts only, after explicit opt-in** → detects recurring bottlenecks → proposes an explanation change → tests a revised version → keeps or rolls back based on evidence.

**Status 2026-10-22:** game is published; independent Neon project and aggregation schema/view have been created. The HTTPS ingestion API is **NOT deployed** (Vercel creation denied, 403); therefore **no remote quest feedback is collected automatically yet**. Do not claim otherwise.

## Privacy and measurement
- Only collect with an explicit learner action and accessible consent text. Never use quiz participation as implicit consent.
- No names, emails, IP-derived identities, user-agent fingerprints, raw answers, free-text comments, or per-person histories in the database.
- Store only date, lesson ID, language, question position, content variant, totals, correct totals, and fixed-category confusion tallies.
- Backend must validate lesson IDs, version, bounds, rate-limit without permanent IP storage, allow only approved site origins, cap payload size, and aggregate immediately. Do not expose write credentials to the browser.
- Do not collect cohorts or demographics. Suppress metrics with fewer than 30 attempts; do not publish usage counts unless actual telemetry exists.
- A count of attempts is not a count of unique students. Shared links, retries, and self-selection bias must be flagged.

## Bottleneck diagnosis
Use a rolling 28-day window at the granularity (topic, language, question slot, content variant):
- < 30 attempts: INSUFFICIENT.
- >= 30 attempts, error rate >= 50%: CRITICAL.
- >= 30 attempts, error rate >= 30%: REVIEW.
- Otherwise OK.
Sort by observed missed-answer count and question difficulty; compare RO/EN independently. Account for unusually hard questions or ambiguous distractors before editing lessons.

## Improvement loop
1. Detect repeated difficulty and its location: example, term, diagram or pacing.
2. Check question validity and technical correctness before concluding the lesson is faulty.
3. Generate **candidate** rewrite with explicit original/revised diff and hypothesis, citing the concept and first-use prerequisites.
4. Evaluate accessibility and conceptual correctness. Do **not** automatically change a published educational explanation without verification.
5. With sufficient traffic and valid consent, compare randomly assigned content versions, track the same questions or calibrated equivalents and uncertainty intervals. Avoid declaring success for tiny samples.
6. Promote only a confirmed improvement, retain rollback, and keep a history of content changes.
7. Stop/alert on sudden abnormal traffic and unexpected cost; maintain independent infrastructure from SeenRelay.

## Infrastructure separation
- LEARN database: Neon `learn-feedback` (`jolly-voice-22581556`, Frankfurt). Schema: `learn_quest_daily`, `learn_chokepoints`, view `learn_quest_diagnostics`.
- A separate HTTPS API deployment is still required. Vercel project creation was refused (403) in this session, so no URL or credentials should be placed in the frontend yet.
- Do not store database secrets in the public GitHub Pages repository. Do not allow browser-to-database writes.
- Next backend milestone: verified API, explicit opt-in submission from Quest, reporting scheduled daily, private change-proposal generation.

## Research quality
This system can detect suspicious questions and likely explanatory bottlenecks; it **cannot automatically prove comprehension**, because game answers may reflect guessing, accessibility, interpretation, or question defects. Validate with real beginner feedback and track revision effects.
