# LEARN — Anonymous Learning Quality Loop

**Production checkpoint: 2026-10-22, verified.** GitHub Pages serves 92 topics. LEARN Quest uses explicit learner opt-in; the existing Netcup VPS acts as public restricted gateway at `/learn-quest/ingest`, with HTTPS handled by existing Caddy. Neon `learn-feedback` Frankfurt persists aggregate counters. The first legitimate consented Quest event was verified in Neon: **1 game / 3 question attempts** at the time of first validation (not a claim about current totals). Neon Function `learnfeedback` deployment #3 and Netcup gateway auto-deploy passed. Cloudflare and Vercel are not used for LEARN.

**Monitoring:** [LEARN Feedback Smoke](.github/workflows/learn-feedback-smoke.yml) runs daily and on relevant source changes; it tests public health, allowed/disallowed CORS preflight, invalid payload rejection and protected Neon native URL without inserting synthetic responses. [Netcup LEARN Gateway](.github/workflows/netcup-learn-gateway.yml) tests and auto-deploys **only gateway code** when the owner changes the gateway/CI files on `main`, using a forced-command SSH key; it does not touch Wisdom Extractor. A separately scheduled **LEARN Quality Watch** checks GitHub publishing and Neon learning-quality indicators daily, alerting only on new verified regressions or mature pedagogical bottlenecks. Site content remains owner-published.

## Accepted statistics and limits

- A learner must deliberately opt in after completing all three questions. No implicit telemetry from reading or playing.
- Only `{schema:1,topic_id,language,correct:[bool,bool,bool],confusion:<fixed category>,variant:'original'}` is accepted. No free text, cookies, account, device IDs, source URL, IP-derived identifier or individual responses.
- Netcup checks schema and size (512 bytes), rate-limits 60 attempts/minute, caps successful requests to 5000/day in memory, and limits concurrent Neon requests to four. The database caps accepted games to 5000/day overall and 300/day/topic. These are accepted-event caps, **not guaranteed spending caps**, and limits reset appropriately across processes.
- Neon function endpoints `POST /ingest` and `GET /diagnostics` require the secret `X-Origin-Secret`. This key remains on Netcup and Neon only.
- Supported topic IDs include `fund`, `ai`, `dc`, `front`, `invis`, `lang`, `data` followed by a two-digit numeric suffix.
- A student can refuse consent, revisit a lesson, or play offline/local-only without losing the learning experience.

## Learning-quality assessment

The Neon view `learn_quest_diagnostics` uses a rolling 28-day window for each (topic, language, question slot).

| Condition | State | Automated response |
|---|---|---|
| <30 attempted answers | INSUFFICIENT | No educational inference |
| >=30 and errors >=50% | CRITICAL | Notify for review |
| >=30 and errors >=30% | REVIEW | Notify for review |
| >=30 and errors <30% | OK | Monitor |

A question may be confusing, mistranslated, excessively difficult, or unrelated to the explanation. Diagnosis is a **hypothesis**, not proof the lesson is bad. Repeated attempts are not unique learners. A deterministic view `learn_revision_candidates` prepares first hypotheses. Any actual rewrite must pass conceptual, language and accessibility review before publication; do not generate or publish autonomous AI edits directly.

## Reliability and cost boundaries

- GitHub Pages builds static material only; reportlab/pypdf are CI build dependencies.
- Existing paid Netcup VPS holds the isolated `learn_quest_gateway` container (0.25 vCPU/96 MB); existing Wisdom and Mobile containers are separate.
- Free-tier Neon `learn-feedback` is isolated from SeenRelay and Wisdom Extractor. Monitor real quota usage; no new subscription is required under current utilisation, but this is not a contractual zero-cost guarantee.
- Caddy production file on the VPS is owner-maintained and has a server-side backup. Never overwrite it from the public repository's sample or reset the Wisdom checkout.
- Neon provider API keys used for initial configuration were revoked; only the server-to-server `ORIGIN_SECRET` remains.
- Do not add new public endpoints exposing private aggregate diagnostics. Do not expose `ORIGIN_SECRET` or `DATABASE_URL` in GitHub or client JS.

## Maintenance and expansion

- Source for the new bilingual 14-topic data chapter: [curriculum/data-chapter.json](curriculum/data-chapter.json).
- Build-time generation of 28 printable PDFs, 2 full booklets, Quests, primers, previews and pages: [tools/build_data_chapter.py](tools/build_data_chapter.py).
- Classroom reading and corrections remain controlled by the owner. Publishing runs require owner identity; feedback never writes to site files.
- Follow up on sustained actual learner evidence before applying any proposed educational change.
