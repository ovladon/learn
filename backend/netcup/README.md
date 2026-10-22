# LEARN Quest gateway on existing Netcup VPS (LIVE — 2026-10-22)

**Purpose:** reuse the server already hosting Wisdom Extractor; avoid Cloudflare and Vercel. This folder is public **source code only**. Never commit filled `.env`, secret values or VPS backups. Deploy as a separate Docker service on the existing Caddy Docker network. Site remains on GitHub Pages and data remains in separate Neon `learn-feedback`.

## Gateway security and availability
- Require the Origin of the LEARN GitHub Pages site. **Origin/CORS is not authentication.** A public caller can spoof Origin; the upstream API additionally requires a server-only secret, and the app enforces global limits.
- Validate strict payload schema and max 512 bytes; no IP/device/user IDs are stored. No free-text comments. Disable request/access logging, including at Caddy, for this route.
- Limit attempts to 60/minute, successful writes to 5000/day, 4 concurrent Neon requests. Database additionally caps accepted writes to 5000/day globally and 300/day/topic. Node's in-memory limits reset on restart; DB limits are authoritative. These limits do not eliminate DDoS traffic received by the VPS.
- Constrain Docker CPU to 0.25 vCPU and memory to 96 MB, no published ports, run unprivileged, read-only filesystem. Check actual VPS free CPU/RAM/storage **before deployment**. This is not a substitute for edge DDoS protection; if public traffic becomes large, add a dedicated rate-limited edge without moving the educational site.
- Keep `ORIGIN_SECRET` identical to that in the already-deployed Neon Function. **The Neon Function expects `X-Origin-Secret`; the unused Cloudflare example incorrectly uses `X-Secret`.**
- When the gateway is down, LEARN lessons and games remain usable, but anonymous results are not submitted.

## First-time bootstrap (already completed in production)
1. Review the existing VPS Caddy container and `Caddyfile`; do not reset the server's local production file with the repository's example, which uses placeholder hostnames.
2. Check resources with `ssh root@annotate.wisdomextractor.com 'free -h; df -h /; docker stats --no-stream'` and identify the Caddy network:
   `docker inspect -f '{{range $name,$v := .NetworkSettings.Networks}}{{println $name}}{{end}}' $(cd /root/wisdom-extractor/deploy && docker compose ps -q caddy)`.
3. Clone/pull `ovladon/learn` on the VPS outside the existing app (`/root/learn` or `/opt/learn`) or copy `backend/netcup` there.
4. In `backend/netcup`, copy `.env.example` to `.env`, edit `CADDY_NETWORK` and set **the SAME** secret as the deployed Neon Function. Because the value is not retrievable from public GitHub, recover it from your private secrets or rotate it in Neon and configure the gateway together. `chmod 600 .env`.
5. `docker compose config` and `docker compose up -d --build` from the gateway directory.
6. Add this route *inside the existing* `annotate.wisdomextractor.com` site block in the **production** Caddyfile, leaving all existing routes intact:

```caddyfile
handle_path /learn-quest/* {
    reverse_proxy learn_quest:8080
}
# Keep an existing catch-all handler for the mobile app, e.g.:
handle {
    reverse_proxy mobile:8600
}
```

   If you already have a plain `reverse_proxy mobile:8600`, replace it with the catch-all `handle` block to prevent precedence surprises. Verify with `docker compose exec caddy caddy validate --config /etc/caddy/Caddyfile` and reload with `docker compose exec caddy caddy reload --config /etc/caddy/Caddyfile` from `/root/wisdom-extractor/deploy`. **Back up the Caddyfile first**.
7. Verify `GET https://annotate.wisdomextractor.com/learn-quest/health` (200); preflight to `/learn-quest/ingest` from allowed and disallowed origins; invalid payload 400; valid opted-in test result 200; repeat/limit 429, and Neon aggregation increments exactly once per accepted game. Use a disposable database branch for test data if possible; otherwise clearly mark and remove test counts before computing learning metrics.
8. **Completed:** the public URL only was enabled in `quest-config.js`, validated using a real opted-in Quest submission and published to GitHub Pages. Never put a secret in the browser.

## Developer test
`node --test backend/netcup/server.test.mjs` from repo root. No third-party Node modules required.

## Operational caution
Existing Wisdom Extractor production may have custom, uncommitted Caddy config. Do not run `git reset --hard` there or deploy the example Caddyfile. If the Netcup server is resource-constrained or receives high attack traffic, use an isolated paid managed edge instead of risking the main app. This is a no-new-subscription proposal, not a promise of unlimited free capacity.

## Routine operation (no new subscription)

GitHub Actions workflow `Netcup LEARN Gateway` now runs tests and automatically deploys *only this gateway container* for owner-authored changes to its server/compose/Docker/CI files on `main`. It uses a restricted root forced-command SSH key installed in the original Netcup setup; it does **not** modify Wisdom Extractor containers or Caddy. `LEARN Feedback Smoke` checks public reachability and access control daily. `LEARN Quality Watch` checks meaningful GitHub/Neon anomalies, respecting a >=30-response floor for pedagogical inferences. The original Caddy production file is backed up on Netcup.

**Backend version:** Neon function `learnfeedback` #3 and Netcup gateway both accept `data-00` to `data-13` topic IDs as well as the six pre-existing prefixes. Cost is included in existing Netcup infrastructure and the Neon free-tier quota under present load; accepted-event caps do not protect from all infrastructure costs.
