# LEARN — See it. Understand it. Remember it.

**Free teaching materials created and taught by Vlad Belciug (@ovladon).**  
**Website:** https://ovladon.github.io/learn/  
**Languages:** English and Romanian  
**Maintenance:** Personal, author-managed repository. No outside submissions or uploads.

LEARN is my permanent, free-to-read visual teaching library. I write, select and publish these materials to help students understand contemporary computing, data structures, artificial intelligence and real-world infrastructure. Anyone can view or download the published files for individual study; this repository is **not** a collaborative project or student assignment upload portal.

## Teaching chapters

| Chapter | Individual topics | A4 PDFs |
|---|---:|---:|
| 01 Computing foundations (including both Big-O lessons) | 13 | 26 |
| 02 AI and agentic systems | 13 | 26 |
| 03 Data centers and AI infrastructure | 13 | 26 |
| **04 Modern computing & AI — from zero to the frontier** | **12** | **24** |
| 05 The Invisible Systems | 12 | 24 |
| **06 Programming Languages: how they think** | **15** | **30** |
| **Total** | **78** | **156** |

Chapter 04 has 12 visual lessons, two complete 12-page PDF booklets, bilingual previews and a permanent QR link on each stand-alone PDF. Students can optionally explore each idea alone; classroom participation is not required. Every standalone lesson defines AI as Artificial Intelligence (English) or Inteligență Artificială (Romanian), and does not assume earlier lessons have been read.

**[Begin chapter 04](https://ovladon.github.io/learn/#front-01)** · [English booklet](https://ovladon.github.io/learn/collections/frontier-en.pdf) · [Broșură în română](https://ovladon.github.io/learn/collections/frontier-ro.pdf)

Topics: inside a language model; attention versus memory; training versus inference; scaling services to many users; request flow from phone to model; multiple agents; tool use and permissions; concurrency; costs; evaluation; prompt injection; the programmer of 2030.

## Learning materials and permanent links

- Browse all subject tracks on the [LEARN website](https://ovladon.github.io/learn/). The website contains search, subject filtering, bilingual labels, PDFs and a back-to-top button.
- The individual files are kept in `materials/<chapter>/`, previews in `previews/`, collected booklets in `collections/` and the searchable index in `catalog.js`.
- Students can scan the QR in the top-right corner of each A4 PDF. Please preserve all `#fund-XX`, `#ai-XX`, `#dc-XX`, and `#front-XX` links permanently, including when replacing posters.
- A static GitHub Pages action publishes checked-in files after updates. It has `contents: read` and a publisher guard for GitHub owner `@ovladon`.

## Ownership and usage

I am the sole editor, publisher and maintainer. **Outside material, pull requests, translations and uploads are not accepted.** The site has no student registration or file-upload mechanism. Viewing and downloading are free; permission to republish, sell or adapt the authored materials is **not** automatically granted. See [USAGE.md](USAGE.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [SECURITY.md](SECURITY.md).

© 2026 Vlad Belciug. Rights retained except as stated in USAGE.md.

## Further reading and accuracy

This chapter teaches durable computing mechanisms, not predictions of a particular future product. Recommended background references: [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/), [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview), [Google Cloud reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide/traffic-load), and [NIST AI Agent Standards Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative). Schematics are conceptual; actual implementations vary.

## Chapter 05 — The Invisible Systems (new)

**[Explore chapter 05](https://ovladon.github.io/learn/#invis-01)** · [English 12-page booklet](https://ovladon.github.io/learn/collections/invisible-en.pdf) · [Broșură în română](https://ovladon.github.io/learn/collections/invisible-ro.pdf)

12 bilingual visual lessons (24 stand-alone A4 PDFs): distributed systems, recovering from failures, data replication, race conditions, database transactions, request balancing, containers, Kubernetes, distributed caching, latency and bandwidth, observability, and engineering trade-offs. Each page has a QR to its permanent lesson, a misconception correction and an optional solo exploration without a teacher.

## The Big Picture of Modern Computing

**[Interactive bilingual system map](https://ovladon.github.io/learn/system-map.html)** · [Printable A3 EN](https://ovladon.github.io/learn/collections/big-picture-a3-en.pdf) · [Poster A3 RO](https://ovladon.github.io/learn/collections/big-picture-a3-ro.pdf)

The conceptual nine-stage map connects user intent, devices, internet routing, applications, data centers, AI models, agents, tools and real-world outcomes. The interactive edition can distinguish a typical non-AI web path from an AI-agent path. Each station opens an existing LEARN lesson; the diagrams do not claim every request follows all nine stages.

**Updated total: 5 subject chapters, 63 topics, 126 individual A4 infographics, plus four printable A3/A4 system-map posters.** Older QR URLs remain unchanged.

Editorial policy: one concept per sheet; acronyms explained; accurate limits, risks and uses; optional individual exercise; English/Romanian; QR links; no external uploads or collaborations. The materials are freely available for individual study, rights retained by Vlad Belciug. See USAGE.md.

## Interactive LEARN — individual browser simulations

**[Open the Interactive Lab](https://ovladon.github.io/learn/interactive-lab.html)** · [View the source](interactive-lab.html)

A self-contained, free, bilingual (EN/RO) companion to the infographics, authored and maintained by Vlad Belciug. Four simulations run **entirely in the student's own browser**:

1. **Processing queues:** FIFO versus priority, capacity of workers, completion and waiting times.
2. **Concurrent programs:** an illustrated lost update without a lock, versus serialized access.
3. **Caching:** a three-slot least-recently-used cache, hits, misses, cost and stale results.
4. **CPU/RAM/GPU allocation:** jobs compete for limited tokens; compare strict FIFO and a policy that can skip a large waiting job.

No account, server calls, telemetry, uploaded data, cookies or third-party assets are required to use these simulations. The numeric units are **pedagogical**, not real infrastructure benchmarks or cost estimates. Students can use them alone; no classroom group experiment is assumed. The existing five teaching chapters (63 topics, 126 individual PDF lessons) and all permanent QR links remain unchanged.

Implementation: `interactive-lab.html`, `interactive-lab.css`, `interactive-lab.js`. The GitHub Pages deployment validates their presence and publishes them alongside the booklets and [system map](system-map.html). Contributions remain owner-only; visiting students have no ability to publish or upload materials.

## Chapter 06 — Programming Languages

Fifteen languages, one visual sheet per language in English and Romanian: **Python, JavaScript, TypeScript, C, C++, Java, C#, Go, Rust, SQL (Structured Query Language), Bash (Bourne Again Shell), Kotlin, Swift, PHP (PHP: Hypertext Preprocessor), R**. Each self-contained infographic explains a mental model, short authentic code with line-by-line clues, distinguishing behavior and trade-offs, use cases, pitfalls, and an optional safe solo exploration. Students do not need to install software.

SQL is declarative query language; Bash is a shell scripting language. HTML (HyperText Markup Language) describes document structure and CSS (Cascading Style Sheets) describes styling. These roles are shown on the map, not conflated with general-purpose programming.

[Programming Languages](https://ovladon.github.io/learn/#lang-01) · [English booklet](https://ovladon.github.io/learn/collections/languages-en.pdf) · [Broșură română](https://ovladon.github.io/learn/collections/languages-ro.pdf) · [English A3 map](https://ovladon.github.io/learn/collections/language-map-a3-en.pdf) · [Harta A3 română](https://ovladon.github.io/learn/collections/language-map-a3-ro.pdf).

The author alone publishes this free teaching library. Visitors can read and download; there are no external uploads. See [USAGE.md](USAGE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
