# De la zero la propriul portofoliu profesional

**Ghid complet, gratuit, pentru studenți — inclusiv pentru cei care nu au creat niciodată un site.**

**Ce vei obține:** un site real la adresa `https://UTILIZATOR.github.io/`, accesibil pe telefon și calculator, un cod QR care deschide acel site, o metodă clară de a publica temele și un istoric al progresului tău până la absolvire.

> **Promisiunea corectă:** toate instrumentele necesare pentru traseul de bază au un plan gratuit, fără să cumperi un domeniu, hosting, șablon sau cod QR. Nu există o garanție că un furnizor va păstra gratuit serviciul pentru totdeauna; de aceea vei păstra și copii ale fișierelor. GitHub Pages este pentru site-uri statice de prezentare, nu pentru procesarea plăților sau pentru aplicații cu server.

## 00. Imaginea de ansamblu: ce construim?

**Problema:** la angajare, propoziția „știu Python” valorează mai puțin decât un proiect pe care îl poate vedea și înțelege cineva.

**Soluția:** o singură adresă publică în care aduni cele mai bune dovezi ale muncii tale. Angajatorul scanează un cod QR, intră pe portofoliu, alege un proiect și poate vedea codul, explicația, demonstrația și ce ai învățat.

**Cuvinte explicate imediat:**
- **Portofoliu:** colecția ta selectată de lucrări, cu context și dovezi. Nu este doar o listă de note.
- **Site web:** pagini pe care browserul (Firefox, Chrome, Safari) le afișează din internet.
- **Link / URL (Uniform Resource Locator):** adresa exactă a unei pagini, de exemplu `https://exemplu.github.io/`.
- **QR (Quick Response) code:** un desen pătrat care codifică adresa; telefonul îl transformă în link.
- **Hosting / găzduire:** serviciul care pune fișierele site-ului la dispoziție pe internet.
- **GitHub:** un serviciu de stocare și versionare a proiectelor; începem doar cu interfața din browser.
- **GitHub Pages:** partea din GitHub care publică gratuit fișierele unui site static.
- **Gratuit și persistent:** nu plătești periodic în condițiile planului gratuit, iar site-ul rămâne disponibil cât timp contul, proiectul și serviciul există și regulile sunt respectate.

**Traseul nostru:** cont GitHub → dosarul site-ului → pagina `index.html` → publicare GitHub Pages → primul proiect → link din portofoliu → cod QR → actualizări în fiecare semestru.

**Ai nevoie de:** un calculator (recomandat; telefonul singur poate fi dificil), internet, un e-mail accesibil, un browser și disponibilitatea de a învăța. **Nu îți trebuie:** card bancar, domeniu, program de editare instalat, terminal Linux sau cunoștințe de HTML.

**Verificare:** știi să explici cuiva, în propoziția „QR-ul duce la site, iar site-ul duce la dovezile proiectelor”, ce construim.

## 01. Decide cum vrei să apari public

1. Scrie pe o hârtie numele profesional sau pseudonimul pe care vrei să îl folosești. Poți folosi „Ana Ionescu”, „Ana I.” sau un alias consecvent; nu este obligatoriu să îți publici toate datele personale.
2. Alege 2–3 domenii în care vrei să arăți progres: programare, structuri de date, pagini web, analiza datelor, securitate etc.
3. Pregătește o scurtă prezentare adevărată: „Sunt student în anul I. Încep să construiesc proiecte de programare și documentez ce am învățat.”
4. Alege un **nume de utilizator** GitHub profesional, ușor de citit și de dictat. Exemplu fictiv: `ana-construieste`. Nu alege un nume jenant sau unul pe care vrei să îl schimbi după ce tipărești codul QR.
5. Nu publica CNP, adresa locuinței, numărul matricol, parole, date ale colegilor, fotografii fără acord sau materiale instituționale confidențiale.

**De ce contează:** un portofoliu e public pentru oricine are adresa; QR-ul nu este o parolă și nu oferă control de acces.

**Verificare:** ai un nume public și o descriere scurtă, fără informații sensibile.

## 02. Creează contul GitHub, pas cu pas

1. Deschide în browser adresa **[github.com](https://github.com/)**. Verifică să fie exact domeniul, nu un link suspect primit prin mesaj.
2. Apasă **Sign up** (înregistrare). Dacă ai deja cont, apasă **Sign in** și treci la pasul 03.
3. Introdu adresa de e-mail la care ai acces. Verifică instrucțiunile primite prin e-mail și confirmă contul dacă ți se solicită.
4. Alege o **parolă** lungă, unică, pe care nu o reutilizezi la alte servicii. Un manager de parole poate crea și reține una în siguranță.
5. Introdu numele de utilizator ales la pasul 01. Dacă este ocupat, folosește o variantă simplă; **notează exact** numele final.
6. Parcurge verificările solicitate de GitHub. Dacă apare oferta unui plan plătit, alege planul **Free**; pentru acest proiect nu ai nevoie de un plan plătit.
7. După conectare, verifică în colțul paginii profilul tău. Adresa contului va arăta ca `https://github.com/NUMELE-TAU`.

**Termeni:** **Cont** = identitatea ta pe serviciu. **Username** = numele public al contului. **Profil** = pagina GitHub care arată proiectele tale.

**Dacă nu poți continua:** verifică e-mailul de confirmare, inclusiv folderul Spam; încearcă alt username. Nu folosi contul altui student.

**Verificare:** ai acces la propriul profil GitHub.

## 03. Securizează contul și adresa de e-mail

1. Deschide meniul profilului → **Settings** (setările contului).
2. Caută secțiunea **Password and authentication**. Activează autentificarea în doi pași (**2FA = Two-Factor Authentication**): pe lângă parolă se cere un al doilea factor, de exemplu o aplicație de autentificare sau o cheie de securitate.
3. Salvează codurile de recuperare într-un loc privat, în afara repository-ului. **Niciodată în portofoliu.**
4. În **Emails**, caută opțiunea care păstrează adresa de e-mail privată în commituri. Poți folosi adresa `noreply` oferită de GitHub. Un **commit** este o versiune salvată a proiectului, cu un mesaj despre schimbare.
5. Verifică datele publice din profil: poți lăsa necompletate telefonul, locația exactă și e-mailul.
6. Evită să folosești același computer conectat permanent la contul tău dacă este împărțit cu alții. Deconectează-te când pleci.

**Verificare:** poți intra în cont, ai o metodă de recuperare și știi ce informații vede un necunoscut.

## 04. Descarcă șablonul care funcționează deja

1. În LEARN, apasă **[Descarcă pachetul ZIP pentru portofoliu](downloads/student-portfolio-starter.zip)**.
2. Găsește fișierul descărcat, de regulă în **Downloads / Descărcări**. Numele lui se termină în `.zip`.
3. Un **ZIP** este un pachet care conține alte fișiere. Apasă cu butonul drept → **Extract here / Extrage aici** (denumirea poate diferi). Pe Windows poți folosi **Extract All**.
4. Deschide dosarul extras: în interior se află **`index.html`** și un fișier cu explicații. **Nu încărca fișierul ZIP direct în repository** — site-ul are nevoie de pagina din interiorul lui.
5. Dă dublu clic pe `index.html`. Dacă se deschide în browser și vezi un site cu numele `[YOUR NAME]`, șablonul funcționează deja **local**, adică pe calculatorul tău.
6. Nu încerca să schimbi încă tot conținutul: îl vei personaliza după ce îl publici. Este mai ușor să verifici câte o schimbare.

**HTML (HyperText Markup Language)** este limbajul de marcare care definește titluri, texte, butoane și linkuri într-o pagină. **CSS (Cascading Style Sheets)** stabilește aspectul vizual: culori, spațiere, așezare. În șablon, CSS este inclus în același `index.html`, deci ai **un singur fișier** de urcat.

**Verificare:** ai un fișier `index.html` și îl poți deschide fără erori în browser.

## 05. Creează repository-ul cu numele CORECT

**Repository / repo:** un dosar de proiect în GitHub care conține fișierele și istoricul lor.

1. Conectează-te la GitHub. Din colțul din dreapta sus, alege **+ → New repository** (sau butonul **New** din lista proiectelor).
2. La **Owner**, selectează propriul cont.
3. La **Repository name**, scrie **exact numele tău de utilizator urmat de `.github.io`**. Dacă username-ul este `ana-construieste`, numele repo-ului trebuie să fie `ana-construieste.github.io` — **nu** `portofoliul-meu`.
4. La **Visibility** (vizibilitate), alege **Public**. Pentru GitHub Free, un site Pages personal se publică din repository public.
5. Opțional, bifează **Add a README file** (un document de prezentare a proiectului). Această alegere este utilă, dar nu obligatorie.
6. Nu adăuga date personale sau parole în descrierea repository-ului.
7. Apasă **Create repository**. Ar trebui să vezi pagina repo-ului tău și, eventual, fișierul `README.md`.

**Important:** dacă repo-ul cu acest nume există deja, **nu crea altul** și nu șterge nimic. Deschide-l și verifică dacă este site-ul tău; folosește-l sau cere ajutor înainte să modifici o pagină existentă.

**Verificare:** adresa repo-ului este `https://github.com/NUMELE-TAU/NUMELE-TAU.github.io`.

## 06. Urcă pagina pe GitHub fără să scrii cod

1. Intră în repository-ul creat. Deschide fila **Code** (fișierele proiectului).
2. Apasă **Add file → Upload files**. Dacă meniul GitHub arată altfel, caută opțiunea „Upload files” de lângă lista fișierelor.
3. Din dosarul extras la pasul 04, alege **doar fișierul `index.html`**. Îl poți trage în zona de încărcare.
4. Așteaptă ca fișierul să apară în lista de încărcare. Verifică numele exact: `index.html`, nu `index.html.txt`, nu `Index.HTML`, nu `index(1).html`.
5. La **Commit changes** (salvează această versiune), lasă sau scrie mesajul `Add my starter portfolio`. Mesajul explică pe scurt ce ai făcut.
6. Confirmă salvarea pe ramura **main** (ramura principală). O **ramură / branch** este o linie de versiuni a proiectului.
7. Revino la lista fișierelor. Fișierul `index.html` trebuie să fie vizibil **la rădăcină (root)**, adică direct în repo, nu într-un subdosar `student-portfolio-starter` sau `Downloads`.

**Dacă ai încărcat ZIP-ul în loc de `index.html`:** nu îl redenumi în `.html`; extrage pachetul pe calculator și urcă fișierul real.

**Verificare:** când deschizi `index.html` pe GitHub, vezi textul și codul paginii.

## 07. Publică site-ul gratuit folosind GitHub Pages

1. În repository-ul tău, apasă **Settings**. Dacă fila nu este vizibilă, verifică meniul **…** al repository-ului; ai nevoie de acces la setările propriului repo.
2. În meniul lateral, găsește **Pages** (de obicei sub „Code and automation”).
3. La **Build and deployment → Source**, selectează **Deploy from a branch**. „Deploy” înseamnă să faci o versiune accesibilă pe internet.
4. La **Branch**, alege `main`; la director (folder), alege **/ (root)** sau **/(root)**.
5. Apasă **Save**.
6. Verifică secțiunea Pages: GitHub îți va afișa adresa site-ului după publicare. Poate fi nevoie să reîncarci pagina după câteva minute; publicarea nu apare întotdeauna instantaneu.
7. Într-o filă nouă, deschide **`https://NUMELE-TAU.github.io/`**, înlocuind numai `NUMELE-TAU` cu username-ul real.
8. Dacă apare încă `404`, nu cumpăra nimic: mergi la secțiunea „Depanare” de la sfârșit.

**Diferență importantă:** `github.com/username/username.github.io` este adresa **fișierelor**; `https://username.github.io/` este adresa **site-ului pe care îl vor vedea angajatorii**.

**Verificare:** se vede pagina „Hi, I'm [YOUR NAME]” la adresa publică.

## 08. Fă prima verificare ca un angajator

1. Copiază adresa site-ului din bara browserului; începe cu **`https://`**. `HTTPS` este varianta criptată a comunicării dintre browser și server.
2. Deschide o fereastră privată / **Private Window**: un mod de navigare care nu folosește sesiunea ta obișnuită de autentificare.
3. Lipește adresa. Dacă pagina este vizibilă fără autentificare, înseamnă că un evaluator extern o poate vedea.
4. Deschide linkurile **About**, **Projects**, **Skills** și **Contact**. Ele trebuie să ducă la secțiunile corecte ale aceleiași pagini.
5. Deschide și pe telefon. Dacă textele ies în afara ecranului, vei corecta designul; șablonul este însă deja adaptat pentru ecrane mici (**responsive**).
6. Păstrează adresa în notițe. Aceasta este adresa pe care o vei transforma mai târziu într-un QR.

**Verificare:** site-ul este public și funcționează fără cont de GitHub.

## 09. Schimbă numele și descrierea, direct în browser

1. Deschide repository-ul **nu** pagina publică; pe GitHub, apasă pe fișierul `index.html`.
2. Apasă pictograma creion (**Edit this file**) pentru a modifica textul. Dacă nu o vezi, verifică să fii conectat la contul corect.
3. Folosește căutarea browserului (`Ctrl+F` sau `Cmd+F`) pentru `[YOUR NAME]`.
4. Înlocuiește fiecare apariție cu numele profesional ales. **Nu șterge** caracterele `<`, `>`, ghilimelele sau parantezele din jurul codului HTML.
5. Caută `[YOUR FIELD]` și scrie domeniul tău, de exemplu „computer science”. Caută `[TOPIC 1]`, `[TOPIC 2]`, `[TOPIC 3]` și pune doar interesele reale.
6. La secțiunea **About me**, înlocuiește textul de exemplu cu 3–4 propoziții simple despre ce înveți. Nu este nevoie de un CV impresionant în anul I.
7. La final, apasă **Commit changes**, cu mesajul `Personalize introduction`.
8. Reîncarcă site-ul public după publicare. Dacă încă vezi textul vechi, încearcă `Ctrl+Shift+R` (reîncărcare fără cache) sau o fereastră privată.

**Ce este un tag HTML?** `<h1>Text</h1>` este un titlu mare. `<p>Text</p>` este un paragraf. `<a href="ADRESA">Vizitează</a>` este un link. Schimbă de regulă **textul dintre taguri**, nu structura lor.

**Verificare:** pagina publică afișează numele și descrierea ta reale, nu marcajele `[...]`.

## 10. Înțelege cum se construiește o dovadă de competență

Un proiect bun nu spune doar „tema 3”. Prezintă clar:

1. **Problema:** ce trebuia rezolvat? Exemplu: „O listă de așteptare trebuie procesată în ordinea sosirii”.
2. **Soluția:** ce ai creat? „Un program care folosește o coadă”.
3. **Instrumentele:** ce ai folosit și ce știi să explici? „Python, liste și funcții”.
4. **Dovezile:** unde poate vedea cineva codul, un rezultat de test sau o demonstrație?
5. **Deciziile:** de ce ai ales coada și nu stiva?
6. **Testele:** ce intrări ai încercat? Ce se întâmplă când lista este goală?
7. **Limitările:** ce nu poate face încă programul?
8. **Contribuția personală:** ce ai făcut tu? Dacă AI a ajutat, descrie transparent la ce.

**Regulă:** o temă modestă, dar explicată și verificabilă, este mai valoroasă decât o demonstrație spectaculoasă pe care nu o poți explica.

## 11. Publică prima temă ca proiect separat

**Recomandare pe termen lung:** un repository pentru fiecare temă relevantă (sau pentru fiecare proiect mai mare), iar portofoliul rămâne pagina de prezentare cu linkuri.

1. Pe GitHub, folosește **+ → New repository** din nou.
2. Alege un nume care descrie lucrul realizat. Exemplu: `lab-01-queue-simulator`. Evită `tema-final-final2`.
3. Alege **Public** doar dacă ai dreptul să publici materialul. Dacă tema conține date private ori cod restricționat, păstreaz-o privată și prezintă în portofoliu numai o descriere neutră și rezultatele permise.
4. Activează **Add a README**. **README.md** este pagina de explicații pe care GitHub o afișează în repo.
5. Creează repo-ul și deschide `README.md`; apasă creionul.
6. Înlocuiește conținutul cu șablonul din secțiunea următoare. Salvează folosind **Commit changes**.
7. Folosește **Add file → Upload files** pentru a urca fișierele temei tale: de exemplu `main.py`, `app.js`, `index.html`, instrucțiuni și eventual o imagine demonstrativă.
8. Testează local ce ai urcat. Dacă execuția nu este posibilă în browser, explică precis cum o poate reproduce o persoană care are limbajul instalat.

**Atenție:** nu publica enunțuri, bareme, soluții de examen sau materiale ale profesorului fără drept de publicare. Publică **munca ta**, fără note și nume de colegi.

**Verificare:** există un repository nou cu codul și un README care se înțelege fără explicații suplimentare.

## 12. Scrie README-ul fiecărui proiect: șablon gata de copiat

În editorul `README.md` scrie, adaptând **fiecare** fragment:

```md
# Simulare de coadă pentru solicitări

## Problema
Am avut de procesat cereri în ordinea sosirii.

## Ce am construit
Un program în Python care adaugă cereri într-o coadă
și le procesează pe rând.

## Cum funcționează
1. Introdu o cerere.
2. Cererea intră la sfârșitul cozii.
3. Programul procesează prima cerere intrată.

## Cum se testează
Am rulat programul cu trei cereri: A, B, C.
Rezultatul a fost A, apoi B, apoi C.
Am testat și coada goală.

## Ce am învățat
O coadă funcționează FIFO (First In, First Out):
primul element introdus este primul procesat.

## Limitări
Nu salvez cererile după închiderea programului.

## Contribuția mea și asistența AI
Am scris [descrie adevărat ce ai făcut].
Am folosit [instrumentul AI, dacă este cazul] pentru
[explicarea erorilor / documentare / sugestii].
Am verificat rezultatele prin [testele tale].
```

**Markdown** este un mod simplu de formatare a textului: `#` creează un titlu, `##` un subtitlu, iar `- ` o listă. Nu trebuie să înveți HTML pentru README.

**Dacă nu folosești Python:** înlocuiește exemplul cu limbajul și comenzile reale ale proiectului. Nu inventa teste, rezultate sau procente.

**Verificare:** un coleg poate spune ce face proiectul, unde este codul și cum îl poate testa doar din README.

## 13. Leagă prima temă de portofoliu

1. În repo-ul temei, copiază adresa exactă din browser, de exemplu `https://github.com/ANA/lab-01-queue-simulator`.
2. Revino în repository-ul `ANA.github.io`, deschide `index.html` și apasă creionul.
3. Caută textul `Project 01 · A data structure in action`. Schimbă-l în numele real al proiectului tău.
4. Imediat sub titlu, editează cele trei paragrafe: **Problem**, **What I built**, **What I learned**, astfel încât să descrie proiectul tău.
5. Caută primul link `<a href="https://github.com/" ...>`. **Înlocuiește doar adresa dintre ghilimelele lui `href`** cu linkul real al repository-ului. `href` înseamnă adresa spre care duce un link.
6. Înlocuiește eticheta `EXAMPLE — REPLACE ME` cu `PROJECT 01` sau `PROIECT REAL`.
7. Salvează cu commit `Add first real project`.
8. Deschide site-ul public într-o fereastră privată și **apasă pe proiect**: trebuie să ajungi la README-ul și codul tău, nu la pagina generică GitHub.

**Exemplu minim de link:** `<a href="https://github.com/ANA/lab-01-queue-simulator">Vezi codul meu</a>`.

**Verificare:** angajatorul poate ajunge din portofoliu la un proiect real în două clicuri.

## 14. Adaugă alte teme fără să reconstruiești site-ul

**La fiecare temă nouă:**

1. Salvează o versiune care funcționează pe calculatorul tău.
2. Verifică drepturile de publicare și elimină secretele, datele personale, parolele, numele colegilor sau cheile API (**API = Application Programming Interface**, o interfață prin care programele comunică).
3. Creează un repository public separat, dacă tema poate fi publicată.
4. Adaugă codul, README-ul, un exemplu de intrare și un exemplu de rezultat. Numele fișierelor trebuie să fie clare.
5. Revino la portofoliu: pentru început, înlocuiește următorul card de exemplu cu noul proiect. Când ai mai mult de trei, poți copia un întreg bloc `<article class="card"> ... </article>` între celelalte carduri — fără să ștergi `</div>` din final.
6. Salvează și verifică toate linkurile.

**Ce faci cu 40 de teme?** Nu pune 40 de carduri egale pe prima pagină. Arată cele mai bune 3–6; oferă un link către profilul tău GitHub pentru arhiva completă și actualizează selecția în fiecare semestru.

**Regulă de aur:** nu publica un link care duce la `404`, un repo gol sau la un exemplu neînlocuit.

## 15. Proiecte care chiar pot fi încercate de evaluator

**Codul** dintr-un repository poate fi citit, dar nu este mereu executabil direct în browser. Dacă ai o aplicație mică realizată în HTML, CSS și JavaScript:

1. În repository-ul proiectului, adaugă fișierul `index.html` și toate fișierele lui.
2. În **Settings → Pages** al **acelui repo de proiect**, activează **Deploy from a branch → main → /(root)**.
3. Pentru repo-ul `lab-01-queue-simulator`, adresa demonstrației poate fi `https://ANA.github.io/lab-01-queue-simulator/`.
4. În README, adaugă separat **Code** (link la repo) și **Live demo** (link la pagina care rulează). În portofoliu poți include ambele linkuri.
5. Testează demonstrația pe telefon și într-o fereastră privată.

**Limită:** GitHub Pages publică fișiere statice, nu execută un backend Python/Java/Node pe server. Pentru Python publică sursa, intrări/ieșiri și instrucțiuni, nu pretinde că `main.py` rulează direct pe Pages. Un „demo” poate fi și o captură de ecran sau o înregistrare care nu expune date personale.

**Verificare:** distingem clar între „cod disponibil” și „demonstrație care rulează”.

## 16. Personalizează designul fără să strici structura

1. În `index.html`, caută secțiunea `<style>`. Acolo sunt regulile CSS pentru culori și aspect.
2. Caută `--teal:#086e67` sau `background:#0d2035`. Acestea sunt **culori hexazecimale**: coduri de tipul `#RRGGBB`. Poți modifica o culoare, apoi salva și verifica.
3. Păstrează contrastul: text foarte deschis pe fundal închis sau invers. Nu folosi text minuscul pentru informațiile esențiale.
4. Nu șterge `<meta name="viewport"...>`: ajută pagina să se adapteze la mobil.
5. Dacă adaugi fotografii, folosește poze proprii sau imagini cu licență potrivită. Explică imaginile importante cu `alt="..." ` (text alternativ util inclusiv cititoarelor de ecran).
6. Pentru profil nu este obligatorie fotografia. O descriere clară și proiecte reale sunt suficiente.

**Nu schimba toate culorile, fonturile și cardurile simultan.** Schimbă un singur lucru, salvează, privește rezultatul. Istoricul commiturilor te poate ajuta să revii la o versiune anterioară.

## 17. Generează codul QR fără abonament și fără cont suplimentar

1. Verifică întâi că portofoliul tău se vede public la `https://NUMELE-TAU.github.io/`.
2. Deschide **[Generatorul QR local din LEARN](portfolio-qr.html)**.
3. În câmpul **Adresa publică a portofoliului**, lipește adresa completă, începând cu `https://`.
4. Apasă **Generează QR**. Un algoritm care rulează **în browserul tău** transformă adresa într-un desen alb-negru; nu o trimite unui serviciu QR extern.
5. Apasă **Descarcă SVG** pentru tipar sau **Descarcă PNG** pentru prezentări. **SVG (Scalable Vector Graphics)** este o imagine vectorială care rămâne clară la orice dimensiune; **PNG (Portable Network Graphics)** este o imagine obișnuită, formată din pixeli.
6. Pune codul QR pe CV, pe un poster de proiect sau într-o prezentare, lângă adresa scrisă în clar. Nu folosi un cod minuscul sau culori cu contrast scăzut.
7. **Testează-l cu camera altui telefon, de pe hârtie sau de pe ecran.** Verifică să deschidă site-ul corect, fără autentificare sau reclame.

**Evită „QR dinamic gratuit” care redirecționează prin domeniul altei firme:** poate impune taxe, expira ori modifica destinația. Codul produs de LEARN conține direct adresa ta. **Dacă schimbi username-ul GitHub, QR-ul vechi poate deveni inutil.**

**Verificare:** o altă persoană scanează codul și vede portofoliul tău.

## 18. Pregătește-l pentru recrutare și colaborări

1. Primele două rânduri trebuie să spună **cine ești și ce construiești**. Evită formule precum „expert în toate tehnologiile” dacă nu le poți demonstra.
2. Afișează 3–6 lucrări relevante, nu neapărat cele mai recente. Pentru fiecare: problemă, rolul tău, dovezi și limitări.
3. Pune la îndemână profilul GitHub. Adaugă o adresă de e-mail profesională doar dacă vrei să fie publică; te poți limita la profilul GitHub.
4. Scrie într-o limbă pe care o stăpânești. Pentru angajatori internaționali, engleza poate ajuta, dar explicațiile trebuie să rămână corecte.
5. Verifică dacă linkurile externe se deschid într-o fereastră privată, fără autentificare.
6. Include și un proiect la care ai greșit, ai testat și ai îmbunătățit soluția: angajatorii pot vedea gândirea ta, nu doar rezultatul.

**Exemplu de prezentare:** „Student informatică, anul II. Mă interesează structurile de date și aplicațiile web. Am implementat trei proiecte publice, fiecare cu instrucțiuni de reproducere și teste.”

**Verificare:** cineva care nu te cunoaște înțelege în mai puțin de un minut în ce ai lucrat și unde poate verifica.

## 19. Protecția datelor, drepturile de autor și folosirea AI

**Înainte de fiecare publicare, întreabă-te:**
- Este lucrarea **a mea** și am permisiunea să o fac publică? Nu publica soluții-model ale profesorului, cod licențiat necorespunzător sau răspunsuri la evaluări în desfășurare.
- Conține date personale ale colegilor, ale unor participanți, fișiere juridice/medicale, parole, tokenuri, chei, acces la baze de date sau capturi de ecran cu conturi reale? Dacă da, **nu le publica**.
- Folosesc imagini, cod sau biblioteci create de altcineva? Verifică licența și atribuie autorul. O **licență** spune în ce condiții poate fi folosită o lucrare.
- Am folosit un instrument de inteligență artificială? Pot descrie cinstit asistența primită și verifica fiecare linie publicată?
- Pot explica la interviu de ce codul funcționează și ce aș modifica? Dacă nu, reia proiectul și înțelege-l înainte să-l evidențiezi.

**Foarte important:** eliminarea unui secret din fișier **nu îl șterge automat din istoricul GitHub**. Dacă ai publicat accidental o cheie, **revocă/rotește cheia imediat**, apoi rezolvă expunerea din istoric conform instrucțiunilor oficiale.

**Verificare:** proiectul poate fi distribuit public fără să expună date ale altora.

## 20. Un obicei repetabil pentru fiecare semestru

După **fiecare temă care merită arătată**, urmează aceeași rutină:

1. Fă tema și testeaz-o.
2. Scrie README: problema → soluția → testul → ce am învățat → limitări.
3. Publică doar fișierele permise.
4. Leagă repo-ul de portofoliu dacă este o lucrare reprezentativă; altfel lasă-l vizibil în profilul GitHub.
5. Actualizează o propoziție din „Skills” **numai când ai dovada**.
6. O dată pe semestru, deschide portofoliul ca un străin: repară linkuri, îndepărtează exemplele, păstrează proiectele cele mai bune.
7. La sfârșitul fiecărui an, păstrează o copie a repo-urilor importante pe calculator și într-o locație privată de rezervă.

**Exemplu de evoluție:** anul I — probleme de programare și structuri de date; anul II — aplicații mici, baze de date și teste; anul III — proiecte integrate, documentație, demonstrații și lucrarea finală (doar ce este permis public).

**Nu urmărim numărul de commituri, ci progresul explicabil.**

## 21. Depanare: dacă nu merge, găsește exact problema

| Ce vezi | Cauza probabilă | Ce faci exact |
|---|---|---|
| `404` la `username.github.io` | nume repo greșit sau Pages neactivat | Verifică `USERNAME.github.io` exact; Settings → Pages → main → /(root). |
| `404` imediat după Save | publicare neîncheiată | Verifică Settings → Pages și Actions; reîncarcă după procesare. |
| Pagina arată README, nu site-ul | `index.html` lipsește sau e în subdosar | Mută/încarcă `index.html` în rădăcina repository-ului. |
| Browserul descarcă HTML în loc să afișeze | deschizi fișierul nepotrivit sau o arhivă | Intră pe adresa `https://USERNAME.github.io/`, nu pe URL-ul raw al fișierului. |
| Văd încă `[YOUR NAME]` | nu ai salvat schimbarea sau ai cache | Editează, Commit changes, apoi `Ctrl+Shift+R`. |
| Nu există butonul creion | nu ești autentificat sau nu ai drepturi | Verifică avatarul și repository-ul tău. |
| `index.html.txt` | extensie greșită | Creează sau redenumește fișierul în `index.html`. |
| Linkul proiectului duce la GitHub generic | `href` nu a fost schimbat | Copiază adresa repo-ului real și înlocuiește doar URL-ul dintre ghilimele. |
| QR-ul deschide alt site | ai copiat o adresă greșită | Testează URL-ul public; generează alt QR și testează prin scanare. |
| QR-ul nu se scanează tipărit | prea mic, neclar, lipsă contrast | Folosește SVG, alb pe fundal și negru pentru cod, cu margine albă. |
| Nu merge programul Python din browser | Pages servește fișiere statice | Publică sursa și README; pentru demo web folosește HTML/JS. |
| Site-ul funcționează pe laptop, nu pe telefon | linkuri relative sau resurse lipsă | Verifică toate fișierele urcate și literele mari/mici din nume. |
| A dispărut o modificare | nu a fost salvată sau ai editat repo-ul greșit | Deschide History/Commits, verifică ultima versiune și mesajele. |
| Repo privat: site-ul nu apare pe plan Free | Pages necesită sursă publică pe Free | Nu publica materiale sensibile; creează repo public numai pentru site. |
| Într-un link apare `404` dar pe cont merge | proiectul este privat | Nu distribui proiectul privat; publică doar o demonstrație permisă sau descriere. |

**Regula de depanare:** verifică *mai întâi* dacă problema este la repo, la fișier, la Pages, la adresă sau la cache. Nu șterge tot site-ul ca „soluție”.

## 22. Examenul final: când poți spune „am portofoliu”

Bifează doar ce ai verificat **tu**:
- [ ] Pot deschide `https://USERNAME.github.io/` într-o fereastră privată.
- [ ] Numele și descrierea sunt ale mele, nu text de exemplu.
- [ ] Am cel puțin un proiect real cu README, cod și o verificare.
- [ ] Linkul din card duce la proiectul corect.
- [ ] Nu public date sensibile, parole, datele colegilor sau cod fără drept de distribuire.
- [ ] Site-ul se citește pe un telefon.
- [ ] Am generat și descărcat QR-ul; l-am scanat de pe alt telefon.
- [ ] Pot explica în cuvintele mele ce este un repository, un commit, `index.html`, GitHub Pages și un link.
- [ ] Știu cum voi adăuga următoarea temă: **repo → README → cod → link → test**.
- [ ] Am o copie de rezervă a fișierelor importante.

**Rezultatul:** ai un portofoliu real care poate crește cu tine până la absolvire. Nu trebuie să arate spectaculos acum; trebuie să funcționeze, să fie adevărat și să fie ușor de actualizat.

## Dicționarul complet, fără presupuneri

| Cuvânt | Explicație în limbaj obișnuit |
|---|---|
| Browser | Programul care afișează pagini web: Firefox, Chrome, Safari. |
| Site | Una sau mai multe pagini accesibile printr-o adresă de internet. |
| URL | Adresa exactă a unei resurse online. |
| Domeniu | Partea identificabilă din adresă, precum `github.io`. |
| HTTPS | Conexiune criptată între browser și site. |
| Hosting | Calculatorul/serviciul care pune site-ul pe internet. |
| GitHub | Platformă pentru proiecte, fișiere și istoricul modificărilor. |
| Repository | Dosarul unui proiect, cu fișiere și istoric. |
| Root | Nivelul principal al dosarului, nu un subdosar. |
| Branch | Linie de versiuni a proiectului; de obicei `main`. |
| Commit | Salvarea unei versiuni cu un mesaj explicativ. |
| README.md | Documentul de prezentare al unui proiect GitHub. |
| Markdown | Reguli simple de formatare a textului. |
| HTML | Limbaj pentru structura conținutului unui site. |
| CSS | Reguli pentru aspectul vizual al paginii. |
| JavaScript | Limbaj de programare care poate face pagina interactivă. |
| `index.html` | Fișierul-pagină de intrare al unui site static. |
| GitHub Pages | Serviciu GitHub care publică un site static dintr-un repo. |
| Deploy | Procesul prin care versiunea site-ului devine publică. |
| Static | Fișiere trimise browserului fără un program-server personalizat. |
| Responsive | Design care se adaptează telefoanelor, tabletelor și calculatoarelor. |
| Link / `href` | Legătură clicabilă / adresa pe care o deschide. |
| QR | Cod vizual ce poate reprezenta un URL. |
| SVG | Imagine vectorială, bună pentru tipărire clară. |
| PNG | Format de imagine digitală bazat pe pixeli. |
| ZIP | Pachet comprimat cu fișiere, care se extrage. |
| Cache | Copie temporară ce poate afișa o versiune mai veche. |
| 404 | Cod de eroare: resursa cerută nu a fost găsită. |
| 2FA | Autentificare cu doi factori, nu doar cu parolă. |
| Licență | Condițiile în care poți folosi o lucrare creată de cineva. |
| AI / IA | Inteligență artificială, programe capabile de anumite sarcini asociate inteligenței. |
| API | O interfață prin care două programe comunică. |
| Open source | Cod sursă publicat sub o licență care permite drepturi de utilizare. |
| Date personale | Informații care pot identifica o persoană. |
| Backup | Copie de rezervă pentru recuperare. |

## Resursele oficiale de verificare

- [GitHub Pages: început de la zero](https://docs.github.com/en/pages/quickstart)
- [Cum alegi ramura și dosarul de publicare](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Cum creezi fișiere direct în GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files)
- [Limitele actuale ale GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)

*Ghid LEARN pentru începători: verificat pe baza documentației publice GitHub, octombrie 2026. Interfața GitHub poate evolua; dacă butoanele se mută, caută denumirile în limba engleză din acest ghid. Nu este necesară instalarea de software suplimentar pentru traseul de bază.*
