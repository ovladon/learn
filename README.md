# LEARN — See it. Understand it. Remember it.

**Free teaching materials created and taught by Vlad Belciug.**

**Student website:** https://ovladon.github.io/learn/  
**Publisher and sole maintainer:** [Vlad Belciug (@ovladon)](https://github.com/ovladon)  
**Languages:** English and Romanian

LEARN is my **personal, author-maintained teaching library**: a growing collection of visual explanations, printable infographics and course resources that I create and use in my teaching. It is not a community-upload site, collaborative textbook or student-submission system. I decide what is added, revised and published.

Anyone can **view and download** the published materials for personal study, free of charge. No registration is required.

## Start learning

Open the [LEARN website](https://ovladon.github.io/learn/), choose a subject, then read or download the lesson PDF in English or Romanian. A QR code on each A4 infographic links to its permanent lesson card; students can scan it from a classroom screen.

Currently available:

| Teaching collection | Topics | Individual PDFs |
| --- | ---: | ---: |
| Computing Foundations, including Data Structures and both Big-O sheets | 13 | 26 |
| Artificial Intelligence and Agentic Systems | 13 | 26 |
| **Total** | **26** | **52** |

The [collections folder](collections/) also has complete booklets, four standalone Big-O PDF links retained for compatibility, and the classroom QR poster. The Big-O lessons are **ordinary Computing Foundations lessons**, not a separate subject. New subjects can be added over time without changing existing QR destinations.

## Read/download only — no external contributions

- **Only I publish or change the teaching materials.** Visitors have no upload form or write access through the website.
- The repository is public for reading and downloading, **not for public contributions**. I do **not** accept externally submitted files, pull requests, or other user-generated teaching content.
- GitHub may still let people **fork** a public repository or propose a pull request. That does **not** grant permission to modify this repository or publish on the LEARN website.
- Adding collaborators, deploy keys or write-capable GitHub Apps could grant others write access. These must remain tightly controlled by the repository owner.
- GitHub Actions deploys the static site from `main`; its `contents` permission is **read-only**, and deployment is restricted to runs initiated by `@ovladon`. These deployment checks supplement—not replace—GitHub repository access controls.

See [CONTRIBUTING.md](CONTRIBUTING.md) (no outside contributions) and [SECURITY.md](SECURITY.md) (account and hosting safeguards).

## Free access does not mean public-domain content

The repository has **no open-source or open-content license**. My educational materials are free to view, download and print for **personal study**. The original author retains copyright and other rights. Free access does not automatically permit republishing, resale, modifying and distributing adaptations, or using these materials as someone else's work.

See [USAGE.md](USAGE.md) for a concise permission statement. If you want rights beyond individual study, please obtain permission from the author.

## How I update the library

This is a straightforward static HTML/CSS/JavaScript site. The lesson PDFs live in `materials/`, previews in `previews/`, and the website's searchable lesson index in `catalog.js`.

As the owner, I may add more subjects and teaching materials to `main`. The [Pages workflow](.github/workflows/pages.yml) validates existing PDF references and publishes the website automatically. Permanent lesson IDs and PDF URLs should remain stable so printed QR codes keep working.

Instructor-only notes, student information, grades, passwords, unpublished research and any other confidential material are **never** part of this public repository.

© 2026 Vlad Belciug. All rights reserved, except for the limited individual-study permissions described in [USAGE.md](USAGE.md).
