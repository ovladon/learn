# LEARN — Security, privacy and publishing controls

LEARN is **my public, personal teaching library**. Visitors may read and download lessons. It has **no account registration, file-upload form, backend upload endpoint, external JavaScript SDKs or student-submission feature**.

## Who can publish?

- The source is hosted in the **personal** GitHub repository `ovladon/learn`.
- **Only the owner publishes** course materials; I do not accept outside contributions.
- GitHub itself enforces the repository's write permissions. A public visitor can read, download, fork or propose a pull request, but cannot directly push to `main` without write authorization.
- The `main` branch deployment workflow has `contents: read` and uses the GitHub Pages publishing permission only; it is also gated on `github.actor == 'ovladon'`. This prevents routine automated publication initiated by another actor but **does not itself prevent a write-authorized collaborator or app from changing source code**.
- `.github/CODEOWNERS` identifies `@ovladon` as code owner; it is a reviewer/ownership signal, **not a substitute for branch protection**.
- Do not add collaborators, write-capable deploy keys, or GitHub Apps with write access unless explicitly needed. Audit **Settings → Collaborators and teams / Access**, **Settings → Deploy keys**, and the account's installed GitHub Apps.
- Enable a passkey or multi-factor authentication for the GitHub owner account.
- Recommended for a pure personal educational archive: switch **Issues** and **Wiki** off in **Settings → General → Features** if available. They do not upload to the LEARN site, but can permit unrelated content within the GitHub project.
- Optional branch protection can prevent branch deletion and force pushes. GitHub's branch restrictions depend on repository ownership and plan; don't assume a personal repository can limit pushes by actor in the same way as an organization.

## What may be published?

Only teaching material that I intend to make **public**: reviewed PDFs, images and self-contained website assets. Never commit student names or grades, attendance, private messages, teaching administration files, personal information, university-restricted licensed content, confidential professional documents, secrets, tokens, unpublished research or private instructor notes.

Review PDF metadata and file history before publication. Deleted files may remain accessible in prior Git commits.

## Visitor privacy

No forms, cookies, third-party analytics scripts or external web fonts are operated by this site. **GitHub**, the hosting provider, may nevertheless process IP addresses and other technical request information. No promise of complete anonymity is made.

All QR codes point to public `https://ovladon.github.io/learn/#...` lessons. The public website cannot guarantee that already downloaded files will never be copied or redistributed.

See [USAGE.md](USAGE.md) for copyright and free-download permissions.
