# LEARN — private Neon feedback Function

**Deployment status 2026-10-22:** deployed on project `learn-feedback`, Frankfurt, slug `learnfeedback`. Neon reports deployment `completed`. **Not connected to the public game**: direct anonymous traffic is not safe without a protected edge.

## Structure

- `index.mjs`: server-only Neon Function; no credentials are committed.
- `sql/schema.sql`: reproducible database tables, atomic daily counters, and two diagnostic views.
- Source is publicly readable in this repository, but GitHub Pages only deploys the educational website; API source is not shipped as part of the website.
- The Function deploy archive contains this `index.mjs` and `postgres.js` v3.4.7 sources pinned to Git tag `v3.4.7` (no install-time network fetching).

## Routes

- Public `GET /health`: status only, no personal or database data.
- Server-authenticated `POST /ingest`: **X-Secret required**, accepts exactly `{schema:1,topic_id,language,correct:[boolean,boolean,boolean],confusion,variant:'original'}`. No raw answers, names, device IDs, time tracking, free-text, sessions, IP-derived identities.
- Server-authenticated `GET /diagnostics`: only aggregate rows with >=30 answers per item. Do not embed secret in client JS.
- Native Neon Function address remains publicly reachable even though its protected routes return 401. **Do not remove the secret requirement.**

## Mandatory gate before enabling student telemetry

1. Deploy an edge Worker/proxy with an appropriate **global rate limit / abuse protection** on a domain you control, and keep the `ORIGIN_SECRET` only in proxy and Function server environments. Never set this secret as a client-side variable. Cloudflare or an equivalent protected edge is suitable; not configured in the connected accounts yet.
2. Verify GET health, OPTIONS/CORS to the allowed GitHub Pages origin, POST valid/invalid, missing secret -> 401, replay/abuse bounds, database aggregation, and 429 quotas. Do not assume a completed deployment means these tests passed.
3. Add a simple *explicit opt-in* share-statistics control to LEARN Quest. Send only the payload above and never auto-submit after a completed game. Retain local-only play as default, and keep the game fully usable when API is down.
4. Check the project budget/quota and alerts. Database caps presently: <=5,000 accepted submissions/day globally, <=300 accepted/topic/day; Neon project quotas are also set. These limits don't guarantee zero billing from unsolicited Function invocations.
5. Verify real traffic metrics and privacy notice before claiming autonomous collection works. Currently **0 real submitted answers**.

## Quality rules

`learn_quest_diagnostics`: rolling 28 days, >=30 answers per question for evaluation. >=50% error -> CRITICAL, >=30% -> REVIEW, else OK. Below 30 -> INSUFFICIENT.
`learn_revision_candidates` generates a deterministic revision suggestion and requires human correctness review before publication. A bad quiz question can make a good lesson look bad; the diagnosis is a hypothesis, not proof.

Do not activate auto-publication of AI rewrites. Use versioned candidate changes, independent review, and eventual controlled A/B tests once legitimate sample sizes exist.
