#!/usr/bin/env bash
# Execute on your own Linux laptop. No passwords or private SSH keys enter the chat or git repository.
set -Eeuo pipefail
HOST='annotate.wisdomextractor.com'
REPO='ovladon/learn'
KEY="${HOME}/.ssh/learn_netcup_ci_ed25519"
for bin in ssh ssh-keygen gh git; do
  command -v "$bin" >/dev/null || { echo "Missing required program: $bin" >&2; exit 1; }
done
if [[ -e "$KEY" || -e "$KEY.pub" ]]; then
  echo "Existing LEARN CI key at $KEY; refusing to overwrite. Rotate manually if necessary." >&2
  exit 1
fi
gh auth status >/dev/null
KNOWN="$(ssh-keygen -F "$HOST" | sed '/^#/d')"
if [[ -z "$KNOWN" ]]; then
  echo "Host key not pinned locally. First connect manually with 'ssh root@$HOST', verify the server host key, then rerun." >&2
  exit 1
fi
install -d -m 700 "${HOME}/.ssh"
ssh-keygen -q -t ed25519 -a 64 -N '' -f "$KEY" -C 'learn-github-actions-forced-command'
chmod 600 "$KEY"
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ssh -o StrictHostKeyChecking=yes "root@$HOST" \
 'umask 077; cat > /usr/local/sbin/learn-ci-gate; chmod 700 /usr/local/sbin/learn-ci-gate; chown root:root /usr/local/sbin/learn-ci-gate' \
 < "$BASE_DIR/learn-ci-gate"
PUBLIC="$(cat "$KEY.pub")"
printf '%s\n' "restrict,command=\"/usr/local/sbin/learn-ci-gate\" $PUBLIC" | \
 ssh -o StrictHostKeyChecking=yes "root@$HOST" \
 'umask 077; install -d -m 700 /root/.ssh; touch /root/.ssh/authorized_keys; chmod 600 /root/.ssh/authorized_keys; IFS= read -r line; grep -Fqx "$line" /root/.ssh/authorized_keys || printf "%s\n" "$line" >> /root/.ssh/authorized_keys'
gh secret set LEARN_NETCUP_SSH_KEY -R "$REPO" < "$KEY"
printf '%s\n' "$KNOWN" | gh secret set LEARN_NETCUP_KNOWN_HOSTS -R "$REPO"
ssh -T -o StrictHostKeyChecking=yes -o IdentitiesOnly=yes -i "$KEY" "root@$HOST" inspect
printf '\nAccess ready. Use GitHub Actions -> Netcup LEARN Gateway -> Run workflow -> inspect.\n'
printf 'The local private key is at %s; never send it in chat.\n' "$KEY"
