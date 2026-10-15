# LEARN — See it. Understand it. Remember it.

**Live bilingual learning library:** https://ovladon.github.io/learn/

A permanent, free, open-access collection of visual explanations about computing, algorithms, data structures, artificial intelligence and agentic systems, designed for learners starting from zero.

## Contents

- **26 topics, 52 individual A4 infographic PDFs** (English and Romanian), all containing QR codes to their permanent topic links.
- Computing Foundations: `materials/foundations/` (26 files).
- AI & Agentic AI: `materials/ai/` (26 files).
- Full collection booklets, four standalone Big-O sheets and classroom QR poster: `collections/`.
- The website itself: `index.html`, `style.css`, `app.js`, `catalog.js`.
- Thumbnails: `previews/`.

## Big-O printable cheat sheets

| Format | English | Romanian |
|---|---|---|
| From zero | [PDF](https://ovladon.github.io/learn/collections/big-o-from-zero-en.pdf) | [PDF](https://ovladon.github.io/learn/collections/big-o-from-zero-ro.pdf) |
| Quick reference | [PDF](https://ovladon.github.io/learn/collections/big-o-quick-reference-en.pdf) | [PDF](https://ovladon.github.io/learn/collections/big-o-quick-reference-ro.pdf) |

## Updating LEARN

This is a **normal static site**. All student files are directly browsable in this repository. Changes committed to `main` automatically publish through [GitHub Actions](https://github.com/ovladon/learn/actions/workflows/pages.yml). The workflow checks that all catalog-referenced files exist and that all 52 initial infographic PDFs and four standalone Big-O sheets are present.

For a new lesson:
1. Upload English and Romanian PDFs to the relevant folder below `materials/`, or create a new subject folder.
2. Add catalog records to `catalog.js`. Generate QR codes pointing at the permanent lesson URL `https://ovladon.github.io/learn/#YOUR-LESSON-ID`.
3. Upload a preview image under `previews/` and commit the changes.
4. Check [the deployment workflow](https://github.com/ovladon/learn/actions/workflows/pages.yml) for success.

**Keep existing lesson IDs and the site address unchanged**: printed classroom QR codes rely on them.

## Security and privacy

The website and all repository contents are **public**. Never upload student data, grades, attendance, passwords, secrets, confidential research, instructor-only notes, or files not approved for public distribution. No student login, form, external analytics, or third-party JavaScript is used. Hosting provider GitHub may process technical access information.

[Site](https://ovladon.github.io/learn/) · [Workflow](https://github.com/ovladon/learn/actions/workflows/pages.yml)
