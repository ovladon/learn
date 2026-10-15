# LEARN — See it. Understand it. Remember it.

**Student library:** https://ovladon.github.io/learn/

Permanent, publicly accessible bilingual (English and Romanian) learning materials for Computer Science, Data Structures, AI and more.

- 26 learning topics, 52 separate A4 QR-coded PDF sheets.
- **Both Big-O formats (from zero and quick reference), in English and Romanian**, included and directly linked.
- Four full curriculum booklets and a classroom QR poster.
- One stable QR link per topic, to `#fund-00`–`#fund-12` and `#ai-01`–`#ai-13`.
- Read-only students, no signup, no trackers or external scripts.

## How it is deployed

The public website is safely bundled in nine binary parts under `.site_payload/`. The GitHub Actions workflow in `.github/workflows/pages.yml` recombines and verifies the archive and publishes it to **GitHub Pages** after a push to `main`.

If the first deployment says "Pages is not enabled", open **Settings → Pages → Build and deployment → Source: GitHub Actions**, then rerun the deployment using **Actions → Deploy LEARN to GitHub Pages → Run workflow**.

**Never put teacher-only files or personal information into this repository.** All files are public. For updates, rebuild the site archive and split into the nine parts using the publishing script in the offline laptop backup. Preserve the domain and lesson IDs so printed QR codes continue to work.

## Big-O cheat sheets

| Version | English | Romanian |
|---|---|---|
| **From zero** | [Open PDF](https://ovladon.github.io/learn/collections/big-o-from-zero-en.pdf) | [Deschide PDF](https://ovladon.github.io/learn/collections/big-o-from-zero-ro.pdf) |
| **Quick reference** | [Open PDF](https://ovladon.github.io/learn/collections/big-o-quick-reference-en.pdf) | [Deschide PDF](https://ovladon.github.io/learn/collections/big-o-quick-reference-ro.pdf) |

The site is statically generated and does not require student accounts. GitHub, as a hosting platform, may maintain technical access logs.

## Publication diagnostics

The repository stores the student site as a verified release archive under `.site_payload/`; individual PDFs appear at `https://ovladon.github.io/learn/...` **only after** the Pages deployment succeeds. The `.site_payload/` directory is not itself a browsable educational library. If students encounter HTTP 404 responses, first check [Actions → Deploy LEARN to GitHub Pages](https://github.com/ovladon/learn/actions/workflows/pages.yml) for a completed successful run and ensure [Settings → Pages](https://github.com/ovladon/learn/settings/pages) is set to **Source: GitHub Actions**.
