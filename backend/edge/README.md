# LEARN Quest protected edge — prepared, NOT deployed

Worker code is ready for deployment to a Cloudflare account with a domain under the user's control. Do not enable student data collection without this gate and end-to-end verification.

1. Install Wrangler 4.36 or newer in the `backend/edge` directory, authenticate interactively to the owner's Cloudflare account, and attach a **Custom Domain** to the Worker (not a Neon registered custom domain); keep workers.dev and Preview URLs disabled.
2. Provision two Wrangler *secrets*, not vars: `NEON_FUNCTION_URL` (Neon's native `learnfeedback` invocation URL) and `ORIGIN_SECRET` (the **same** secret already configured server-side on Neon). Never write their values to the repository or GitHub Pages.
3. Verify the Worker binding `QUEST_LIMIT` and Cloudflare WAF/DDoS rules on the custom domain. The built-in limiter is **approximate and per Cloudflare location**, not a hard worldwide budget cap. Neon also enforces accepted-event caps and project quotas.
4. Test CORS preflight, successful opted-in write, 401 when native Neon origin is hit without secret, non-site Origin -> 403, invalid payload -> 400, oversized body -> 413, rate excess -> 429, and verify exactly three question tallies per accepted game. Never test by inserting unlabelled fake responses into the production statistics. Prefer a separate test branch.
5. After tests, set `window.LEARN_TELEMETRY_ENDPOINT = 'https://YOUR_CUSTOM_DOMAIN/ingest'` in `quest-config.js` and publish GitHub Pages. No credentials belong in this file. Only then does the opt-in control appear in Quest.

At this point no Cloudflare account/zone/Worker is connected through the available tools, so deployment is blocked pending that access. LEARN remains free and fully playable without analytics.
