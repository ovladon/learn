# LEARN — isolated Neon Function for anonymous learning feedback

**Production (2026-10-22):** `learn-feedback` in Frankfurt, slug `learnfeedback`, active deployment **#3 (completed)**, connected to the live Quest through the existing Netcup reverse proxy. One real opt-in game was independently checked to create three aggregate question attempts at initial validation; later traffic must be read from Neon rather than assumed.

## Security and API

- Public `GET /health`: coarse service status.
- Private `POST /ingest`: accepts exact schema `{schema:1,topic_id,language,correct:[boolean,boolean,boolean],confusion,variant:'original'}`. **Requires `X-Origin-Secret`**, supplied by the server-side Netcup gateway only.
- Private `GET /diagnostics`: returns only aggregated metrics based on at least 30 answers per question. Requires the same `X-Origin-Secret`.
- Not allowed: raw student answers, free text, names, login, individual histories, IP-derived identity, credentials in browser or Git.
- Accepted topic prefixes are `fund|ai|dc|front|invis|lang|data`. Update both the Neon Function and `learn_record_quest()` whenever supporting new prefixes.
- The deployment archive bundles this server-side `index.mjs` with pinned `postgres.js` source **v3.4.7**. GitHub Pages does not package backend sources.

## Limits and interpretation

The database stores aggregated totals by date, topic, language, question and content variant; overall limit 5000 accepted games/day and 300 per topic/day. Rate limits and concurrent requests are also bounded on Netcup. These are not hard protection against every public denial-of-service or cost scenario.

`learn_quest_diagnostics`: rolling 28 days; below 30 attempts -> INSUFFICIENT; at least 30 with >=50% errors -> CRITICAL; >=30 with >=30% -> REVIEW; else OK. `learn_revision_candidates`: deterministic review suggestions. Human educational review remains mandatory before publication.

The API secret should be rotated by updating **both** server-side environments. A Neon API key is **not** the origin secret and must not remain installed after setup.

Canonical roadmap: [LEARNING_QUALITY_LOOP.md](../../../LEARNING_QUALITY_LOOP.md).
