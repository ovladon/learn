#!/usr/bin/env bash
# One-time LEARN Quest gateway bootstrap. Run ONLY via verified root SSH.
# Does not deploy LEARN container; creates private env + installs isolated Caddy route.
set -Eeuo pipefail
umask 077
CF=/root/wisdom-extractor/deploy/Caddyfile
ENVFILE=/etc/learn-quest/learn.env
EXPECTED=$'annotate.wisdomextractor.com {\n    reverse_proxy mobile:8600\n}'
NEW=$'annotate.wisdomextractor.com {\n    handle_path /learn-quest/* {\n        reverse_proxy learn_quest:8080\n    }\n    handle {\n        reverse_proxy mobile:8600\n    }\n}'
command -v docker >/dev/null
command -v openssl >/dev/null
command -v git >/dev/null
[[ -f "$CF" ]] || { echo 'STOP: production Caddyfile missing'; exit 2; }
[[ "$(/usr/bin/docker inspect -f '{{range $k,$_ := .NetworkSettings.Networks}}{{$k}}{{end}}' deploy-caddy-1)" == 'deploy_default' ]] || { echo 'STOP: unexpected Caddy network'; exit 2; }
CURRENT="$(cat "$CF")"
if [[ "$CURRENT" != "$EXPECTED" && "$CURRENT" != "$NEW" ]]; then
  echo 'STOP: Caddy production file differs from verified minimal version; no changes made.'
  exit 2
fi
[[ ! -e "$ENVFILE" || -f "$ENVFILE" ]] || { echo 'STOP: env path exists but is not a regular file'; exit 2; }
install -d -m 0700 /etc/learn-quest
if [[ ! -f "$ENVFILE" ]]; then
  SECRET="$(openssl rand -hex 32)"
  cat > "$ENVFILE" <<EOF
CADDY_NETWORK=deploy_default
NEON_FUNCTION_URL=https://br-lucky-sun-b9lhjzlx-learnfeedback.compute.c-7.eu-central-1.aws.neon.tech/
ORIGIN_SECRET=$SECRET
EOF
  chmod 600 "$ENVFILE"
  unset SECRET
  echo 'LEARN environment: created, root-only (secret NOT printed)'
else
  chmod 600 "$ENVFILE"
  grep -q '^ORIGIN_SECRET=[0-9a-f]\{64\}$' "$ENVFILE" || { echo 'STOP: existing secret invalid'; exit 2; }
  echo 'LEARN environment: kept existing secret'
fi
if [[ "$CURRENT" == "$EXPECTED" ]]; then
  BACKUP="$CF.learn-backup-$(date -u +%Y%m%dT%H%M%SZ)"
  cp -p "$CF" "$BACKUP"
  printf '%s\n' "$NEW" > "$CF"
  if ! docker exec deploy-caddy-1 caddy validate --config /etc/caddy/Caddyfile ||
     ! docker exec deploy-caddy-1 caddy reload --config /etc/caddy/Caddyfile; then
    echo 'Caddy validation/reload failed: restoring saved configuration.'
    cat "$BACKUP" > "$CF"
    docker exec deploy-caddy-1 caddy reload --config /etc/caddy/Caddyfile || true
    exit 3
  fi
  echo "Caddy route: installed; original backed up at $BACKUP"
else
  echo 'Caddy route: already configured, unchanged'
fi
echo 'READY: LEARN bootstrapped on Netcup. Wisdom Extractor routes preserved.'
echo 'NEXT: use the Neon CLI to rotate the private Neon Function ORIGIN_SECRET to the value stored here.'
