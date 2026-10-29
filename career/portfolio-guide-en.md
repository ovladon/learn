# From zero to your own professional portfolio

**A complete free guide for students — even if you have never created a website.**

**You will finish with:** a working public site at `https://USERNAME.github.io/`, a QR code that opens it, a first project people can inspect, and a repeatable way to publish coursework throughout university.

> **An important promise:** the basic route uses free GitHub features and a QR generator that does not require an account or subscription. You do not buy a domain, hosting, or a template. No provider can guarantee that a free service will exist forever, so keep local backups. GitHub Pages is intended for static presentation websites, not payments or server applications.

## 00. What are we building, exactly?

Imagine an employer asks, "What can you actually do?" You hand them a QR code. They scan it, see who you are, and can inspect your best projects, the source code, an explanation and — when appropriate — a working demonstration.

**The five pieces:**
- **Portfolio:** a carefully selected collection of your actual work, with context and evidence; not merely a list of grades.
- **Website:** pages displayed by a browser, such as Firefox, Chrome or Safari.
- **URL (Uniform Resource Locator):** the exact web address of a page, such as `https://example.github.io/`.
- **QR (Quick Response) code:** a square image that encodes your URL for a phone camera to read.
- **Hosting:** a service that makes your website's files available on the internet.
- **GitHub:** a service where you can store projects and track their versions.
- **GitHub Pages:** a free option for publishing static website files from GitHub.
- **Persistent:** the address remains usable while the account, repository and service continue to exist under their rules. It is not a lifetime guarantee.

**Our route:** GitHub account → website repository → `index.html` → GitHub Pages → first coursework project → project link on the homepage → QR code → semester updates.

**You need:** a working email address, browser, internet access and preferably a laptop/desktop. You do **not** need a bank card, paid site builder, domain name, installed development tools, terminal commands or prior knowledge of HTML.

**Checkpoint:** you can explain this sentence: "The QR points to the portfolio; the portfolio points to evidence of work."

## 01. Choose a safe public identity

1. Decide what name appears publicly: a professional full name, a shortened version, or an alias. You do not have to publish every legal detail.
2. Choose two or three interests: programming, data structures, web applications, data analysis, cyber security, or other genuine interests.
3. Write a truthful introduction: "I am a first-year computer science student. I am learning by building small programs and documenting them."
4. Choose a readable GitHub username. A fictional example is `ana-builds`. Avoid usernames you might regret after distributing a printed QR.
5. Do **not** publish identity numbers, your home address, passwords, other students' grades or photographs, or confidential university material.

**Why this matters:** everything on a public portfolio can be viewed by strangers. A QR is just an address, **not** access control.

**Checkpoint:** you have a public name and two sentences describing your real interests.

## 02. Create your free GitHub account

1. Open **[github.com](https://github.com/)** in your browser. Check the spelling of the domain; do not follow an untrusted lookalike.
2. Click **Sign up**. Already have an account? Click **Sign in** and move to step 03.
3. Enter an email address you can access. Follow the email verification steps if GitHub requests them.
4. Create a strong, unique password. A reputable password manager can create and remember one.
5. Enter the username you chose in step 01; if unavailable, try a simple variation. **Write down the exact final username.**
6. Complete GitHub's requested verification steps. Choose the **Free** option if offered a plan selection. The core tutorial requires no paid subscription.
7. Open your public profile. It should look like `https://github.com/YOUR-USERNAME`.

**What the terms mean:** an **account** is your sign-in identity; a **username** is its public short name; a **profile** is a page that displays information and projects about that account.

**If stuck:** look for a confirmation email, including Spam, or choose another username. Do not borrow another student's account.

**Checkpoint:** you can sign in and open your own public GitHub profile.

## 03. Secure your account before publishing

1. Open your profile menu and choose **Settings**.
2. Under **Password and authentication**, set up a second factor (**2FA = Two-Factor Authentication**). This adds a second proof of identity alongside a password.
3. Save any recovery codes privately, somewhere outside GitHub. **Never put them in the portfolio.**
4. Under **Emails**, look for the privacy setting that keeps your email address out of commits. GitHub offers a `noreply` address. A **commit** means a saved version with a short change description.
5. Check which details your public profile displays. You can leave phone number, physical location and personal email blank.
6. If using a shared computer, sign out when you finish.

**Checkpoint:** you know how you would recover your account and which profile information is public.

## 04. Download your ready-made website

1. Open **[Download the starter ZIP from LEARN](downloads/student-portfolio-starter.zip)**.
2. Find it in **Downloads**. A file ending in `.zip` is an archive that contains other files.
3. Right-click → **Extract here** or **Extract all**. On some systems double-clicking the archive opens an extraction window.
4. Open the extracted folder and find **`index.html`** and an explanatory readme. **Do not upload the ZIP archive itself** as your website.
5. Double-click `index.html` to open it locally in your browser. You should see a well-designed sample with `[YOUR NAME]` and three example project cards.
6. Keep the file as it is for your first public test. Personalise the content later so you can clearly identify each step.

**HTML (HyperText Markup Language)** specifies the structure of a webpage — headings, paragraphs, links. **CSS (Cascading Style Sheets)** controls presentation — colours, spacing, layout. This starter includes its CSS inside `index.html`, so there is **only one file to upload**.

**Checkpoint:** the extracted `index.html` opens successfully on your computer.

## 05. Create the repository with the precise name

A **repository** or **repo** is the GitHub project folder that holds files and their history.

1. Sign in to GitHub. Select **+ → New repository**, or the **New** button in your repositories list.
2. Under **Owner**, choose your account.
3. In **Repository name**, type **your exact GitHub username followed by `.github.io`**. If your username is `ana-builds`, enter `ana-builds.github.io`. Do not call it simply `portfolio`.
4. Set visibility to **Public**. On GitHub Free, a published personal Pages website uses a public repository.
5. You may enable **Add a README file**. A README is a document that explains a repository. It is helpful but optional.
6. Click **Create repository**.
7. Confirm that you are now looking at `https://github.com/YOUR-USERNAME/YOUR-USERNAME.github.io`.

**If the repository already exists:** do not delete or overwrite it blindly. Inspect it first. It may already be a website.

**Checkpoint:** the repository name is spelled exactly like the GitHub username plus `.github.io`.

## 06. Upload the HTML file using only your browser

1. In your new repository, open the **Code** tab.
2. Click **Add file → Upload files**. Depending on the interface, this option may be beside the file list or inside a menu.
3. Pick **only the extracted `index.html`** from step 04. You can also drag it into the upload area.
4. Check the filename before saving: `index.html`, not `index.html.txt`, `Index.HTML`, or `index(1).html`.
5. Use **Commit changes** to save. A suggested message is `Add my starter portfolio`.
6. Save to the default **main** branch. A **branch** is a line of saved versions of your work; `main` is commonly the primary one.
7. Return to the repository file list. The `index.html` must be at the **root**, meaning directly in the main directory, not inside an extra downloaded folder.

**Common error:** uploading the ZIP does not automatically extract it into a website. Extract first, upload `index.html`.

**Checkpoint:** clicking `index.html` on GitHub shows the code of your webpage.

## 07. Publish it for free with GitHub Pages

1. From your own repository, open **Settings**. If hidden in a narrow layout, look under the repository's overflow menu.
2. Find **Pages** in the left sidebar, typically in the "Code and automation" group.
3. Under **Build and deployment → Source**, select **Deploy from a branch**. **Deployment** means making a version publicly available.
4. Under **Branch**, choose `main`; under folder, choose **/(root)**.
5. Click **Save**.
6. Open the Pages settings again to see the status and published address. The site might take several minutes to appear; don't assume an immediate 404 means failure.
7. In a separate browser tab, visit **`https://YOUR-USERNAME.github.io/`** — replacing `YOUR-USERNAME` with the real value.
8. If the page is not there yet, use the troubleshooting table in step 21. You do not need to buy a domain.

**Know the difference:** `github.com/username/username.github.io` shows the **project files**; `https://username.github.io/` shows the **website visitors will see**.

**Checkpoint:** the sample portfolio homepage opens at the public URL.

## 08. Inspect the site like an employer

1. Copy the full public URL. It begins with **`https://`**. **HTTPS** means an encrypted connection between browser and website.
2. Open a **Private/Incognito** window. This does not share the login session of your usual window.
3. Paste the URL. If the site opens without signing in, an employer can see it too.
4. Click **About**, **Projects**, **Skills** and **Contact**. Each menu link should jump to the matching part of the page.
5. Open the site on your phone; the layout should fit the screen. A **responsive** design adjusts to different screen sizes.
6. Save the public URL. You will need precisely this address to generate your QR.

**Checkpoint:** an unauthenticated visitor can open your portfolio from a different device.

## 09. Replace the sample name and introduction

1. Go to your **GitHub repository**, not the published website, and click `index.html`.
2. Use the pencil icon (**Edit this file**) to edit it. If absent, check you are signed in to the correct account.
3. In the editor, use browser search (`Ctrl+F`, or `Cmd+F` on Mac) for `[YOUR NAME]`.
4. Replace every occurrence with your chosen professional name. Do not accidentally remove the surrounding HTML characters `<`, `>`, quotes or brackets outside the placeholder text.
5. Replace `[YOUR FIELD]`, `[TOPIC 1]`, `[TOPIC 2]`, `[TOPIC 3]` with actual studies and interests.
6. In **About me**, replace the example paragraph with three or four truthful sentences. In your first year, "I am beginning to learn" is completely acceptable.
7. Click **Commit changes**, with message `Personalise my introduction`.
8. Once publication finishes, refresh your public site. If it still looks old, try `Ctrl+Shift+R` or another private window.

**Three HTML tags explained:** `<h1>Heading</h1>` marks a major heading; `<p>Text</p>` is a paragraph; `<a href="URL">Visit</a>` is a link. Usually you change the **text between tags**, not the tags.

**Checkpoint:** the live page shows your own name and interests, with no remaining `[YOUR NAME]` placeholder.

## 10. Understand what employers expect from a project

A useful project page is not simply named "homework 3". Explain:
1. **Problem:** what needed solving? For example, process requests in arrival order.
2. **Solution:** what did you build? A queue-based processing program.
3. **Tools:** which languages, libraries or approaches did you use?
4. **Evidence:** where is the code, output, screenshot, tests or live demo?
5. **Decisions:** why a queue rather than a stack?
6. **Testing:** what inputs and edge cases did you try? What if the queue is empty?
7. **Limitations:** what doesn't the program do yet?
8. **Your contribution:** what did you personally do? Be transparent about AI assistance.

**A modest, correctly explained program is more convincing than impressive code you cannot explain.**

## 11. Publish your first homework as a separate project

The portfolio is your front door; a **separate repo for each worthwhile project** is the simplest long-term record.

1. On GitHub, click **+ → New repository**.
2. Give the work a descriptive name, such as `lab-01-queue-simulator`, not `final-homework-final2`.
3. Choose **Public** only if you own the work and are permitted to publish it. Otherwise use a private repository and share only a permitted description or public demonstration.
4. Select **Add a README file**. GitHub shows `README.md` at the top of the repo.
5. Open `README.md`, click the pencil and replace the sample text with the project guide in step 12.
6. Commit the README change.
7. Use **Add file → Upload files** to upload your actual source files (`main.py`, `app.js`, `index.html`, etc.), plus only non-sensitive examples.
8. Test the uploaded work; explain the prerequisites and exact run instructions in README so another person can reproduce it.

**Academic ethics:** do not publish confidential problem statements, teacher answer keys, assessment answers for ongoing assignments, classmates' information or code you are not permitted to distribute.

**Checkpoint:** you have a public project repo containing original work and a readable explanation.

## 12. Copy and adapt this README example

Edit `README.md` and replace every example with your own true details:

```md
# Request queue simulator

## Problem
I needed to process requests in the order they arrived.

## What I built
A Python program that adds requests to a queue and
processes them one at a time.

## How it works
1. Enter a request.
2. The request is added at the end.
3. The oldest waiting request is processed first.

## How I tested it
I used three requests: A, B and C.
The output was A, then B, then C.
I also tested an empty queue.

## What I learned
A queue follows FIFO (First In, First Out):
the earliest inserted item is processed first.

## Limitations
The program does not save data after closing.

## My work and AI assistance
I wrote [describe what you actually implemented].
I used [name any AI tool, if relevant] for
[understanding errors / documentation / suggestions].
I verified results by [list your actual tests].
```

**Markdown** is a simple way to format text. `#` starts a heading, `##` a smaller heading, and `- ` a list. GitHub displays formatted Markdown automatically.

**Not using Python?** Replace the language and steps with the ones that match your own project. Do not invent outcomes or tests.

**Checkpoint:** someone unfamiliar with the assignment can understand the project and how to try it.

## 13. Link that project to your portfolio

1. In your project repository, copy the full URL from the browser address bar, for example `https://github.com/ANA/lab-01-queue-simulator`.
2. Return to your personal website repo `ANA.github.io`; open `index.html`; click the pencil.
3. Search for `Project 01 · A data structure in action` and replace the example title.
4. Edit the three short paragraphs beneath it: **Problem**, **What I built**, and **What I learned**.
5. Find its link, starting with `<a href="https://github.com/" ...>`. Replace **only the URL inside the `href` quotes** with the full address of your project. **`href`** means the destination of a link.
6. Replace the `EXAMPLE — REPLACE ME` label with an honest label like `PROJECT 01`.
7. Commit with message `Add my first real project`.
8. In a private browser window, open your published homepage, click the project card link and confirm it opens your actual project, with code and README.

**Minimal example:** `<a href="https://github.com/ANA/lab-01-queue-simulator">View my code</a>`.

**Checkpoint:** from the portfolio homepage, an employer can reach one real project in two clicks.

## 14. Add every future assignment without rebuilding everything

For each worthwhile homework:
1. Finish a working version and test it.
2. Check publication rights and remove credentials, personal information, classmates' details and **API keys**. **API (Application Programming Interface)** means a way for computer programs to communicate.
3. Create a separate public GitHub repo when you have permission to make it public.
4. Add code, clear README, and representative test inputs and outputs.
5. If the work deserves a card on the portfolio homepage, replace the next example project card. To add more than three cards, carefully copy a complete `<article class="card"> ... </article>` block and place it among the existing cards; don't remove the surrounding `</div>` tag.
6. Commit and click every new link.

**How do ALL assignments remain accessible without editing the homepage every week?** The starter includes an **All my coursework · full archive** section. In `index.html`, find `[REPLACE THIS LINK WITH MY PUBLIC GITHUB REPOSITORIES]` and replace that link's `https://github.com/` destination with `https://github.com/YOUR-USERNAME?tab=repositories`. You do this **once**. Each new public homework repository then becomes discoverable through your GitHub repository archive; private repositories remain invisible to visitors. Keep only your strongest 3–6 projects featured on the homepage.

**Checkpoint:** every featured project has its own genuine code and explanation.

## 15. When possible, let an employer try the project live

A GitHub repository displays code; it does not automatically execute every program. For a small website made with HTML, CSS and JavaScript:

1. Put its `index.html` and related files in the project's own repo.
2. In that project repository's **Settings → Pages**, select **Deploy from a branch → main → /(root)**.
3. For a repo named `lab-01-queue-simulator`, the demo might be at `https://ANA.github.io/lab-01-queue-simulator/`.
4. Add both **Source code** and **Live demo** links to README and, if appropriate, to your portfolio.
5. Test the demo on mobile and from a private browser window.

**Important limit:** GitHub Pages publishes static files; it does not run your Python, Java or Node server application. For Python, share the source, reproducible steps and possibly a safe screenshot or video; never claim a `.py` file runs in the browser by itself.

**Checkpoint:** readers can distinguish code they can inspect from a demo they can actually use.

## 16. Adjust the visual style carefully

1. In `index.html`, look for `<style>`, which contains the page's CSS.
2. Find a colour such as `#0d2035`. This is a **hex colour** code, often written `#RRGGBB`. You can change one colour and check the result.
3. Keep text easy to read against its background. Do not shrink important text just to fit more on one screen.
4. Keep `<meta name="viewport" ...>`: it helps layout work on small screens.
5. If adding photos, use images you own or are licensed to use. Important images should include meaningful **alt text** through `alt="description"` for users with screen readers.
6. A portrait photo is optional. Clear explanations and real code are sufficient.

**Change one thing at a time.** Commits preserve earlier versions so it is easier to identify what broke.

## 17. Generate a permanent-link QR, with no paid QR service

1. Make sure the full portfolio address, `https://YOUR-USERNAME.github.io/`, already opens publicly.
2. Open **[LEARN's private, browser-based QR maker](portfolio-qr.html)**.
3. Paste the exact **https://** portfolio address into the input field.
4. Select **Generate QR**. The code is produced inside your browser; LEARN does not send the address to an external QR service.
5. Choose **Download SVG** for high-quality printing or **Download PNG** for a presentation or résumé. **SVG (Scalable Vector Graphics)** is a crisp scalable image. **PNG (Portable Network Graphics)** is a pixel-based image.
6. Put the QR alongside the written portfolio address on your résumé, project poster or networking card. Keep high contrast and enough white space around it.
7. **Scan the printed QR using a different phone.** It must open the correct public portfolio without a login or an advertisement page.

**Avoid an apparently free "dynamic QR" subscription or redirect service.** Such codes can later become paywalled. Your LEARN QR encodes the destination URL directly, but it will no longer point to the same website if you change your GitHub username or remove the website.

**Checkpoint:** another person can scan the QR and view your work.

## 18. Make the portfolio useful to an employer

1. Within the first two lines, say who you are and what you are building. Don't call yourself an expert in skills you have only just started studying.
2. Feature your strongest 3–6 pieces of work, each with a problem, your role, evidence and limitations.
3. Include a clear link to your GitHub profile. Add a professional public email address only if you are comfortable publishing it; there is no need for a contact form.
4. Write in a language you actually know. English may help international employers, but accurate explanations matter more.
5. Test external links without logging into GitHub.
6. Show learning and improvement: a project that documents a bug and a tested fix can be more persuasive than a flashy unverified demo.

**An accurate opening:** "Second-year computer science student interested in data structures and web applications. Here are three public projects, each with reproducible tests."

**Checkpoint:** a new reader can understand your strengths and verify an example within a minute.

## 19. Privacy, copyright and AI honesty

Before each upload, ask:
- Is this **my own work**, and do I have permission to publish it? Avoid distributing instructor solution keys, exam materials or copyrighted code without permission.
- Does anything contain classmates' names, participant data, legal/medical files, passwords, tokens, database credentials, screenshots of accounts, or other protected content? **Do not upload it.**
- Are images, code or libraries from others correctly licensed and attributed? A **licence** explains permitted uses.
- Did I use an artificial intelligence tool? Can I accurately describe where it helped and what I personally tested or verified?
- Can I explain the implementation in an interview? If not, revisit the program before advertising that skill.

**Critical:** deleting a secret from a file does **not** automatically remove it from Git history. If you accidentally publish a credential, revoke or rotate it immediately, then follow the official security and history-cleanup guidance.

**Checkpoint:** the project can be shared publicly without exposing private data or misrepresenting ownership.

## 20. The semester-by-semester routine

After every assignment worth showing:
1. Implement and test a working version.
2. Write the README: problem → approach → test → what I learned → limitations.
3. Publish only permitted materials.
4. Link it from the portfolio when it is one of your strongest examples; keep the rest discoverable on GitHub.
5. Update your **Skills** section only when a project supports the claim.
6. Every semester, open your site as a stranger: fix links, remove sample placeholders, keep the strongest projects in front.
7. At least once each academic year, keep a backup of important repositories and your portfolio files outside your GitHub account.

**Example progression:** year one — basic programming and data structures; year two — databases, small applications and testing; year three — integrated projects, reliable documentation and your final-year project where publication is allowed.

**A long commit history is not the objective. Verifiable progress is.**

## 21. Troubleshooting: read the symptom, then the solution

| Symptom | Likely cause | Precise action |
|---|---|---|
| `404` at `username.github.io` | Repository name wrong or Pages disabled | Check the exact `USERNAME.github.io` repo name; Settings → Pages → main → /(root). |
| `404` shortly after Save | Publishing still underway | Check the Pages status and Actions; retry after publishing finishes. |
| GitHub shows README but not your website | `index.html` missing or in another folder | Upload `index.html` to the repository root. |
| HTML downloads instead of displaying as a website | Wrong link or archive | Open `https://USERNAME.github.io/` rather than the raw file URL. |
| The page still says `[YOUR NAME]` | Changes not committed or browser cache | Commit edits and try `Ctrl+Shift+R`. |
| No pencil icon | Not signed in or wrong repository | Check your account avatar and edit your own repo. |
| Filename is `index.html.txt` | Incorrect extension | Rename/create the real `index.html` file. |
| Project link opens GitHub's homepage | You didn't replace the sample `href` | Insert the full URL of the actual project repo. |
| QR points somewhere unexpected | Wrong address encoded | Open the public URL first and regenerate the QR. |
| Printed QR does not scan | Too small or poor contrast | Use SVG with a plain white background and a clear border. |
| Python file won't run inside Pages | Pages is static hosting | Publish source and run instructions; use HTML/JS for a live browser demo. |
| Desktop works but phone is missing resources | Relative link errors or missing files | Verify filenames and letter case, then upload all resources. |
| My edit seems to have vanished | Wrong repository/version or uncommitted edit | Open repository history and inspect commits. |
| Private repo won't publish on Free | Free Pages sources must be public | Publish only non-sensitive material in a public site repo. |
| Link works for me only | Destination project is private | Publish a permitted public excerpt or a neutral description. |

**Troubleshooting principle:** check the repository name, file location, Pages publishing setting, URL and cache before changing anything. Do not delete your entire project to fix a broken link.

## 22. Final acceptance checklist: do I really have a portfolio?

- [ ] `https://USERNAME.github.io/` opens in a private browser window.
- [ ] I replaced the sample name and introduction with honest information.
- [ ] At least one **real** project has code, a readable README and a test.
- [ ] The project link on the homepage opens the correct repo.
- [ ] I published no secrets, classmates' information or restricted materials.
- [ ] The website is readable and usable on a phone.
- [ ] I generated and downloaded a QR and scanned it using another phone.
- [ ] I can explain a repo, a commit, `index.html`, Pages and links in plain language.
- [ ] I know how to add the next assignment: **repo → README → code → link → test**.
- [ ] I have a backup outside GitHub.

**Result:** a genuinely functional portfolio that can grow for years. It does not need to be impressive on day one. It does need to be real, public, correct and easy to update.

## Glossary: every unfamiliar word explained

| Word | Meaning for a beginner |
|---|---|
| Browser | Software that displays web pages, e.g. Firefox or Chrome. |
| Website | One or more linked public pages. |
| URL | The exact address of an online resource. |
| Domain | The identifiable name part of an address, e.g. `github.io`. |
| HTTPS | Encrypted communication between browser and website. |
| Hosting | The computer/service that makes website files available. |
| GitHub | A platform for code, projects and version history. |
| Repository | A project folder with its files and history. |
| Root | The top level of a folder, not a nested subfolder. |
| Branch | A line of project versions, commonly `main`. |
| Commit | A saved project change with an explanatory message. |
| README.md | A formatted document explaining a GitHub project. |
| Markdown | Simple text formatting rules, such as `# Heading`. |
| HTML | The language that structures a web page. |
| CSS | Rules that control visual appearance. |
| JavaScript | Programming language used for browser interactions. |
| `index.html` | The entry-point file for a static website. |
| GitHub Pages | GitHub's service for publishing static sites. |
| Deploy | Make a saved website version publicly available. |
| Static site | Website delivered as files, without a custom server program. |
| Responsive | Design that fits mobile, tablet and desktop screens. |
| Link / `href` | A clickable connection / its target address. |
| QR | A visual code that can encode a website address. |
| SVG | Sharp vector image format, useful for printing. |
| PNG | Common pixel-based image format. |
| ZIP | A compressed package of files to extract. |
| Cache | Temporary stored copy; it may show an older version. |
| 404 | Error code meaning "requested page not found". |
| 2FA | Two-factor authentication, not just a password. |
| Licence | Rules under which another person's creation may be reused. |
| AI | Artificial Intelligence: software that performs certain intelligent tasks. |
| API | Application Programming Interface: a way for software to communicate. |
| Open source | Code published under a licence allowing specified reuse. |
| Personal data | Information that can identify a person. |
| Backup | A separate copy used for recovery. |

## Official references for current GitHub screens

- [GitHub Pages beginner quickstart](https://docs.github.com/en/pages/quickstart)
- [How to select a publishing branch and folder](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Create new files directly in GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files)
- [GitHub Pages limits and free-tier restrictions](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)

*LEARN beginner guide based on GitHub's public documentation, October 2026. Interface labels may move over time; look for the English button names listed here. No software installation is needed for the basic route.*
