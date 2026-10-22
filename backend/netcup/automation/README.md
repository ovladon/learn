# LEARN — GitHub Actions access to existing Netcup VPS

**Status:** the CI workflow and restrictive access setup are prepared. This does not connect the server automatically. The owner executes the one-time local setup below. **Never paste passwords, private SSH keys, or Neon secrets into ChatGPT or GitHub source code.**

## What is possible

- `inspect`: read-only `free`, `df`, Docker container names and state, Caddy Docker network, whether the LEARN route and env file exist (does not show secrets).
- `deploy <commit SHA>`: only after a separate, one-time server configuration. Builds/restarts **only the LEARN Quest gateway**, from a commit on `ovladon/learn` `main`; requires `/etc/learn-quest/learn.env` and an existing Caddy route. It does not modify, reset or reload the Wisdom Extractor app or Caddy.
- All GitHub Actions operations are manually invoked (`workflow_dispatch`), only by `ovladon` on `main`. An administrative secret key is protected by a **forced-command SSH entry**, limiting it to those two operations. No interactive shell, port or agent forwarding is allowed for that key.
- We do **not** use a self-hosted GitHub runner, expose `/var/run/docker.sock`, or add the CI key to your normal full-access keys.

## One-time setup — owner's Ubuntu laptop

1. Verify `gh` (`gh --version`) and your GitHub authorization (`gh auth status`). Install and log in to GitHub CLI on your laptop if missing (`sudo apt install gh`, then `gh auth login`).
2. You must already be able to run `ssh root@annotate.wisdomextractor.com`, and the host's real SSH fingerprint must already be stored in your laptop's `~/.ssh/known_hosts` from that verified connection. The setup script reuses it (does **not** blindly trust `ssh-keyscan`).
3. In your local clone of `ovladon/learn` (or a fresh clone), run:

   ```bash
   git clone https://github.com/ovladon/learn.git  # skip if you already have a clone
   cd learn
   bash backend/netcup/automation/setup-access.sh
   ```

   The script locally creates a dedicated Ed25519 key with no passphrase for unattended CI, installs a **root-owned** forced-command gate on the VPS, appends **only its public key** to the root account's SSH keys and uploads the **private key** as an encrypted GitHub Actions secret via `gh secret set` (without displaying it). It also uploads the already trusted SSH host key as another Actions secret. Your existing SSH keys and the running services are not changed.
4. GitHub → `ovladon/learn` → Actions → `Netcup LEARN Gateway` → `Run workflow` → `operation: inspect`. The output should report available resources, Caddy network name, and whether the LEARN route and secret file have been installed.

## First LEARN deploy (separate manual production preparation)

This access alone does not activate the student feedback collection. The private Neon secret is not retrievable from this repository. The first installation requires confirming or rotating it **privately**, configuring `/etc/learn-quest/learn.env` as root-only (mode 600) with `CADDY_NETWORK`, `NEON_FUNCTION_URL`, and `ORIGIN_SECRET` matching the deployed Neon Function, and backing up + validating the **actual** production Caddyfile before adding a `/learn-quest/` route. See `backend/netcup/README.md`. Do not copy the generic `wisdom-extractor/deploy/Caddyfile` from GitHub over the production local file.

After a verified initial installation, use the same GitHub Actions workflow with `operation: deploy` to update **only** the LEARN gateway. The job checks gateway logic, fetches a SHA already merged into `main`, starts only that service, and verifies internal `/health`.

**Browser result collection remains OFF until end-to-end checks pass**: trusted host key, remote health, network route, HTTP CORS/validation, a consented write with test isolation, matching Neon aggregate, quota behavior, and GitHub Pages game submission.

## Revocation

To revoke the CI access, delete **only** the dedicated public key line identified by the comment `learn-github-actions-forced-command` from `/root/.ssh/authorized_keys`, and delete GitHub Actions secrets `LEARN_NETCUP_SSH_KEY` and `LEARN_NETCUP_KNOWN_HOSTS` in the repository. Preserve your personal SSH key entries. You can also delete `/usr/local/sbin/learn-ci-gate` after disabling the key. This does not affect the running LEARN app or the Wisdom Extractor app.

## Security boundaries

The forced-command gate runs as root but has fixed, fully validated operations. Protect `main` and workflow modifications in GitHub: changes to the deployment workflow or this server gate must be reviewed carefully. GitHub Actions secrets are not available to pull requests from forks. The dedicated private key lives on your laptop and in GitHub Secrets, **never in source control or in this chat**. GitHub Actions logs must not print secrets. For unattended automatic production updates, first add proper branch protection and a review/approval gate rather than enabling all pushes immediately.
