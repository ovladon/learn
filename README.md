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
| **07 Data, types and structures — from zero** | **14** | **28** |\n| **Total** | **92** | **184** |

Chapter 04 has 12 visual lessons, two complete 12-page PDF booklets, bilingual previews and a permanent QR link on each stand-alone PDF. Students can optionally explore each idea alone; classroom participation is not required. Every standalone lesson defines AI as Artificial Intelligence (English) or Inteligență Artificială (Romanian), and does not assume earlier lessons have been read.

**[Begin chapter 04](https://ovladon.github.io/learn/#front-01)** · [English booklet](https://ovladon.github.io/learn/collections/frontier-en.pdf) · [Broșură în română](https://ovladon.github.io/learn/collections/frontier-ro.pdf)

Topics: inside a language model; attention versus memory; training versus inference; scaling services to many users; request flow from phone to model; multiple agents; tool use and permissions; concurrency; costs; evaluation; prompt injection; the programmer of 2030.

## Chapter 07 — Data, types and structures

**[Begin chapter 07](https://ovladon.github.io/learn/#data-00)** · [English A4 booklet](https://ovladon.github.io/learn/collections/data-en.pdf) · [Broșură A4 în română](https://ovladon.github.io/learn/collections/data-ro.pdf).

Fourteen concepts in beginner order: data and information; binary representation and UTF-8; types and missing values; CSV/JSON; arrays and linked lists; stacks/queues; sets/maps/hash tables; trees/heaps; graphs; search/sort/Big-O; SQL and transactions; quality/provenance/privacy; batches/streams/cache; AI datasets/embeddings/retrieval. Each topic has an A4 bilingual sheet with a QR link, a standalone plain-language online explanation, three Quest challenges and a beginner-edition PDF.

The canonical Chapter 07 curriculum is in `curriculum/data-chapter.json`. GitHub Pages builds its 28 PDF sheets, two booklets, 14 previews, pages, primers and topic-specific Quests deterministically using `tools/build_data_chapter.py`. This is **build-time generation**, so the generated binaries are hosted in the published site artifact rather than checked into `materials/data` in Git. Existing chapters remain unchanged.

## LEARN Quest — privacy-first learning-quality feedback

Quest results remain local by default. After answering, a student may explicitly choose to share only the topic identifier, language, three correctness flags and a predefined confusion category. The payload is schema-validated and immediately aggregated via existing Netcup + isolated Neon infrastructure; no account, free-text response or individual history is stored. Telemetry can be refused without affecting lessons. `LEARN Feedback Smoke` checks the public gateway daily, and LEARN Quality Watch checks for verified problems and mature anonymous bottlenecks (>=30 answers per question). Automated suggestions require educational review; the system never silently rewrites published lessons. Technical details: [LEARNING_QUALITY_LOOP.md](LEARNING_QUALITY_LOOP.md).

## Learning materials and permanent links

- Browse all subject tracks on the [LEARN website](https://ovladon.github.io/learn/). The website contains search, subject filtering, bilingual labels, PDFs and a back-to-top button.
- The individual files are kept in `materials/<chapter>/`, previews in `previews/`, collected booklets in `collections/` and the searchable index in `catalog.js`.
- Students can scan the QR in the top-right corner of each A4 PDF. Please preserve the permanent topic links across all seven tracks (including `#data-XX`), including when replacing posters.
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

**Updated total: 7 subject chapters, 92 topics, 184 individual A4 sheets, 184 explained PDF editions and four printable system-map posters.** Existing QR URLs remain unchanged.

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

## Read every infographic online — and begin from zero

The [LEARN website](https://ovladon.github.io/learn/) now has a dedicated **Read online / Citește online** link on all 92 lesson cards. The original PDF is embedded in a responsive reading page (no download required in browsers supporting inline PDF viewing); a browser-image preview and an **Open PDF** alternative are also available. **Download PDF** remains optional. The student can switch English/Romanian on the reading page. No logins or file uploads; optional anonymous aggregate Quest feedback is sent only by explicit opt-in.

Each reading page begins with a bespoke everyday-language explanation of the topic, a simple concrete example, and a vocabulary guide defining the main ideas and prerequisites. The original 78 bilingual notes are versioned in `learner-notes.js`; Chapter 07 additions are generated at build time from `curriculum/data-chapter.json`. This is an **accessibility and learning layer**, not a claim that every underlying one-page PDF is now fully self-contained: the standalone infographics still require individual educational review and, where needed, rewriting to fit the same strict editorial standard. See [BEGINNER_STANDARD.md](BEGINNER_STANDARD.md).

The learner's online reading page is `lesson.html?id=LANGUAGE-INDEPENDENT-LESSON-ID&lang=en` (or `lang=ro`). Previously printed QR codes pointing to `#lesson-id` still reach the corresponding lesson card on the original site.

## LEARN Fast Start — read and understand before the jargon

Every one of the **92 topics** has a bilingual, directly shareable HTML explanation at `topics/<lesson-id>-en.html` and `topics/<lesson-id>-ro.html`. Each page has a plain-language explanation, an everyday example, topic-specific vocabulary, the original one-page infographic in an online PDF viewer, a simple comprehension check, and links to the original and the new explained PDF edition. There are **184 printable explained editions** in the published `beginner/` folder, with an introduction followed by the original infographic; original one-page URLs remain unchanged.

The page cards lead to the shareable lessons, show a one-sentence answer, and make the beginner edition the default PDF download. The generated `sitemap.xml` lists the accessible HTML lessons; no signup, analytics, uploads or outside scripts are used. The generator source is `tools/build_faststart.py` and runs in the existing owner-only GitHub Pages workflow.

**Accuracy boundary:** the automated audit confirms the presence of both languages, definitions, examples, PDF documents and links. It cannot establish true conceptual self-sufficiency or technical correctness. The original sheets and guides still require human beginner testing and editorial review, per [BEGINNER_STANDARD.md](BEGINNER_STANDARD.md); never label them as independently pedagogically certified. The [BEGINNER_AUDIT.json](https://ovladon.github.io/learn/BEGINNER_AUDIT.json) build report lists every guide and its status.

For discoverability, students may link directly to pages and download the material free for individual study. This does not change copyright ownership or allow visitors to publish.

## LEARN Quest — 3 clues per topic (October 2026)

Every one of the 92 lessons has a voluntary bilingual three-step Quest at `quest.html?id=TOPIC-ID&lang=ro` (or `en`): a concrete scenario, a vocabulary check and a misconception check. The website does not grade students or record identities. Results remain local unless the student explicitly opts in at the end; in that case only the topic, language, three correctness flags and a fixed confusion category are sent to Netcup and aggregated by Neon. There is no student account or raw response history. The quiz questions are educational checks, not validated psychometric measures.

The lesson page generator in `tools/build_faststart.py` adds the game link to every one of the 184 language-specific lesson pages. Previously printed QR IDs remain stable and lead to topic cards with a game CTA.

## LEARN Quest privacy-first feedback rollout (2026-10-22)
The private backend exists on Neon, but students **do not submit statistics automatically** and anonymous collection remains disabled until a protected, rate-limited HTTPS proxy is deployed and tested. Quest now hides its feedback submission controls when disabled, removing the old manual copy/email workflow. The configured endpoint is currently empty in `quest-config.js`. Do not put a database password or the Neon Function server secret in any browser-facing file. See `backend/neon/learnfeedback/README.md`.
