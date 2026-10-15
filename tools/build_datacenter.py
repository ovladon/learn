from pathlib import Path
import io, math, textwrap, re, json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from xml.sax.saxutils import escape
import qrcode
from PIL import Image
import fitz

FONT='/usr/share/fonts/truetype/lato/'
for name,f in [('Lato','Lato-Regular.ttf'),('LatoBold','Lato-Bold.ttf'),('LatoHeavy','Lato-Heavy.ttf')]:
 pdfmetrics.registerFont(TTFont(name,FONT+f))
W,H=A4; O=Path('/mnt/data/_learn_work/site');O.mkdir(exist_ok=True,parents=True)
N='#10243B'; CYAN='#26ACAB'; PAPER='#F4F7FB'; MUTED='#50657A'; WHITE='#FFFFFF'
URL='https://ovladon.github.io/learn/'

# EN and RO versions are written for learners who are new to computing.
D=[
('INSIDE A DATA CENTER','ÎN INTERIORUL UNUI CENTRU DE DATE',
 'A building that coordinates power, computers, storage, networking and people.',
 'O clădire care coordonează electricitatea, calculatoarele, stocarea, rețeaua și oamenii.',
 ['POWER','COMPUTERS','NETWORK','SERVICE'],['ENERGIE','CALCULATOARE','REȚEA','SERVICIU'],
 [('RACKS ARE SHELVES','A rack holds multiple servers and network switches. A server is a computer that serves other computers.'),('ALWAYS-ON SUPPORT','Electric power, cooling, fire controls and physical security help the machines operate reliably.'),('SOFTWARE COORDINATES','Programs distribute requests and move work between servers. A user normally sees only the application.'),('NOT A MAGIC CLOUD','The cloud is someone else’s real hardware, offered as a service over a network.')],
 [('RACKURILE SUNT RAFTURI','Un rack ține servere și comutatoare de rețea. Un server este un calculator care oferă servicii altora.'),('SUPORT NEÎNTRERUPT','Electricitatea, răcirea, protecția la incendiu și accesul fizic controlat mențin funcționarea.'),('SOFTWARE-UL COORDONEAZĂ','Programele distribuie cererile și sarcinile între servere. Utilizatorul vede de obicei doar aplicația.'),('CLOUD NU ÎNSEAMNĂ MAGIE','Cloud înseamnă echipamente reale ale altcuiva, oferite ca serviciu prin rețea.')],
 'Like a school: rooms, electricity, corridors and schedules support the actual lessons.',
 'Ca o școală: sălile, curentul, holurile și orarul susțin lecțiile.',
 'Which parts still matter if nobody is visiting the website right now?',
 'Ce părți contează chiar și când nimeni nu vizitează site-ul?'),
('ONE CLICK, MANY MACHINES','UN CLIC, MAI MULTE CALCULATOARE',
 'Follow a request from phone to data center and back.',
 'Urmărește o cerere de la telefon la centrul de date și înapoi.',
 ['PHONE','GATEWAY','SERVER','RESPONSE'],['TELEFON','PUNCT DE INTRARE','SERVER','RĂSPUNS'],
 [('REQUEST','Your browser asks for a page or an application result. A request is a structured message.'),('ENTRY POINT','A gateway receives the message. A load balancer may choose a healthy server with available capacity.'),('WORK','The selected service may read a cache, call another service or retrieve records from a database.'),('REPLY','The server sends data back. Your device renders the result and may save a temporary copy.')],
 [('CERERE','Browserul solicită o pagină sau un rezultat. Cererea este un mesaj cu o structură precisă.'),('INTRARE','Un punct de acces primește mesajul. Un distribuitor de trafic poate alege un server funcțional.'),('EXECUȚIE','Serviciul poate citi un cache, apela alt serviciu sau căuta date într-o bază de date.'),('RĂSPUNS','Serverul trimite date înapoi. Dispozitivul afișează rezultatul și poate păstra o copie temporară.')],
 'The click is local; the computation may travel across many computers.',
 'Clicul este local; calculul poate trece prin mai multe calculatoare.',
 'If one service is slow, can the whole request become slow?',
 'Dacă un serviciu e lent, poate deveni lent întregul răspuns?'),
('CPUs, GPUs & BATCHES','PROCESOARE, GPU-URI ȘI GRUPURI DE CERERI',
 'Different workers, different tasks. Faster hardware is not enough on its own.',
 'Lucrători diferiți, sarcini diferite. Hardware-ul rapid nu este suficient.',
 ['REQUEST','CPU TASK','GPU TASK','RESULT'],['CERERE','SARCINĂ CPU','SARCINĂ GPU','REZULTAT'],
 [('CPU (CENTRAL PROCESSING UNIT)','The general-purpose processor: runs operating-system code, coordinates services and handles many kinds of logic.'),('GPU (GRAPHICS PROCESSING UNIT)','A processor designed for many parallel calculations; especially useful for many matrix operations in AI.'),('BATCHING','Several compatible jobs may be grouped to improve throughput. Waiting for a batch can add latency.'),('LATENCY VS THROUGHPUT','Latency: how long one request waits. Throughput: how many requests finish in a period of time.')],
 [('CPU (CENTRAL PROCESSING UNIT)','Procesor general: execută codul sistemului de operare, coordonează servicii și multe tipuri de logică.'),('GPU (GRAPHICS PROCESSING UNIT)','Procesor adaptat multor calcule paralele; util mai ales la operații pe matrici în inteligența artificială.'),('PROCESARE ÎN GRUP','Mai multe sarcini compatibile pot fi grupate pentru capacitate mai mare. Așteptarea adaugă uneori latență.'),('LATENȚĂ VS DEBIT','Latența: cât așteaptă o cerere. Debitul: câte cereri se termină într-o perioadă.')],
 'A GPU is not simply a “faster CPU”: it is designed for different patterns of work.',
 'Un GPU nu este doar un CPU mai rapid: este proiectat pentru alt tip de muncă.',
 'Could a full batch improve efficiency but delay one urgent request?',
 'Un grup plin de cereri poate crește eficiența, dar întârzia o cerere urgentă?'),
('MEMORY IS NOT STORAGE','MEMORIA DE LUCRU NU ESTE STOCARE',
 'Where are active calculations, saved files and backups?',
 'Unde sunt calculele active, fișierele salvate și copiile de siguranță?',
 ['ACTIVE MEMORY','LOCAL DISK','SHARED STORAGE','BACKUP'],['MEMORIE ACTIVĂ','DISC LOCAL','STOCARE PARTAJATĂ','COPIE'],
 [('RAM (RANDOM ACCESS MEMORY)','Temporary working area for running programs. Its usual contents disappear when power is lost.'),('SSD (SOLID-STATE DRIVE)','Persistent storage that keeps saved information after a normal shutdown.'),('SHARED OR OBJECT STORAGE','Multiple servers can use shared systems. Object storage manages named objects with data and metadata.'),('BACKUP IS DIFFERENT','A replicated copy is not always a backup. A separate, recoverable history protects against deletion and corruption.')],
 [('RAM (RANDOM ACCESS MEMORY)','Spațiu temporar pentru programe active. Conținutul obișnuit dispare la întreruperea alimentării.'),('SSD (SOLID-STATE DRIVE)','Unitate de stocare persistentă care păstrează informația salvată și după oprire.'),('STOCARE COMUNĂ SAU DE OBIECTE','Mai multe servere folosesc sisteme partajate. Stocarea de obiecte păstrează date cu nume și metadate.'),('COPIA DE SIGURANȚĂ ESTE ALTCEVA','Replicarea nu este automat backup. Un istoric recuperabil protejează contra ștergerilor și coruperii.')],
 'RAM is the worktable. Storage is the cabinet. Backup is the spare copy elsewhere.',
 'RAM este masa de lucru. Stocarea este dulapul. Backup este copia păstrată separat.',
 'If a file is deleted and the deletion replicates, is it still backed up?',
 'Dacă ștergerea unui fișier se propagă, există încă o copie de siguranță?'),
('NETWORKS: THE HALLWAYS','REȚELE: CORIDOARELE DIGITALE',
 'Data centers are as much about movement as they are about computing.',
 'Centrele de date înseamnă și deplasarea informației, nu doar calcul.',
 ['CLIENT','ROUTER','SWITCH','SERVER'],['CLIENT','RUTER','COMUTATOR','SERVER'],
 [('ROUTER','Moves network packets between networks, based on network addresses.'),('SWITCH','Connects devices inside a local network and forwards frames to the correct destination.'),('BOTTLENECK','A fast processor may wait for data on a slow network. Delay and congestion matter.'),('AI CLUSTER','AI servers often exchange large amounts of data. Specialized fast links connect accelerator nodes.')],
 [('RUTER','Mută pachetele între rețele, pe baza adreselor de rețea.'),('COMUTATOR (SWITCH)','Leagă dispozitive dintr-o rețea locală și trimite cadrele către destinație.'),('ÎNGUSTARE','Un procesor rapid poate aștepta date dintr-o rețea lentă. Congestia și întârzierea contează.'),('CLUSTER AI','Serverele de inteligență artificială schimbă multă informație și folosesc legături rapide dedicate.')],
 'Many fast computers still feel slow when the network becomes a traffic jam.',
 'Chiar și calculatoarele rapide par lente când rețeaua este blocată.',
 'Would adding more servers solve a network bottleneck?',
 'Ar rezolva serverele suplimentare un blocaj de rețea?'),
('POWER & COOLING','ENERGIE ȘI RĂCIRE',
 'Every computation becomes heat. Reliability begins before the code runs.',
 'Fiecare calcul produce căldură. Fiabilitatea începe înainte de cod.',
 ['GRID','POWER SUPPLY','CHIPS','COOLING'],['REȚEA ELECTRICĂ','ALIMENTARE','CIPURI','RĂCIRE'],
 [('ELECTRICAL PATH','Power reaches the facility, passes through electrical distribution and supplies computers.'),('UPS (UNINTERRUPTIBLE POWER SUPPLY)','A short-term power system that can bridge interruptions while other protection acts.'),('HEAT HAS TO MOVE','Fans or liquid cooling carry heat away. More computation generally requires more heat removal.'),('EFFICIENCY IS END TO END','Useful work per unit of energy depends on hardware, cooling, utilization and software decisions.')],
 [('DRUMUL CURENTULUI','Energia intră în clădire, trece prin distribuția electrică și alimentează calculatoarele.'),('UPS (UNINTERRUPTIBLE POWER SUPPLY)','Sistem de alimentare neîntreruptibilă ce acoperă temporar întreruperile de curent.'),('CĂLDURA TREBUIE EVACUATĂ','Ventilatoarele sau lichidul de răcire scot căldura. Mai mult calcul necesită de obicei mai multă răcire.'),('EFICIENȚA E A ÎNTREGULUI SISTEM','Munca utilă per unitate de energie depinde de hardware, răcire, utilizare și software.')],
 'A server room is a machine whose purpose is to keep other machines usable.',
 'Camera serverelor este o mașină care menține funcționale alte mașini.',
 'What happens to a busy AI cluster if cooling stops?',
 'Ce se întâmplă cu un cluster AI ocupat dacă răcirea se oprește?'),
('WHO GETS A SERVER?','CINE PRIMEȘTE UN SERVER?',
 'The scheduler coordinates requests for finite resources.',
 'Planificatorul distribuie cererile între resurse limitate.',
 ['WAITING JOBS','SCHEDULER','MACHINE','RETRY'],['CERERI ÎN AȘTEPTARE','PLANIFICATOR','MAȘINĂ','REÎNCERCARE'],
 [('JOB','A job is a piece of work, such as processing a video or running an AI model.'),('SCHEDULER','A program chooses where and when work should run, using rules about capacity and constraints.'),('CAPACITY IS FINITE','Machines have limited processor time, memory and network capacity. Some jobs must wait.'),('FAILURE & RETRY','If a job cannot run, the system may wait and try again. Retries require care to avoid repeated effects.')],
 [('SARCINĂ (JOB)','O unitate de lucru: de exemplu, prelucrarea unui videoclip sau rularea unui model AI.'),('PLANIFICATOR','Program care alege unde și când rulează sarcinile, ținând cont de limite și reguli.'),('RESURSELE SUNT LIMITATE','Mașinile au timp de procesor, memorie și rețea finite. Unele sarcini așteaptă.'),('EȘEC ȘI REÎNCERCARE','Dacă o sarcină nu poate rula, sistemul poate reîncerca. Atenție la efecte repetate.')],
 'Scheduling is like assigning students to a few available lab computers.',
 'Planificarea seamănă cu distribuirea elevilor la puține calculatoare.',
 'Should a tiny urgent job always wait behind a very large job?',
 'O sarcină mică și urgentă trebuie să aștepte mereu după una uriașă?'),
('SECURITY & FAILURES','SECURITATE ȘI DEFECȚIUNI',
 'Keeping a service working is different from keeping its information safe.',
 'A menține serviciul activ nu este același lucru cu a proteja datele.',
 ['IDENTITY','PERMISSION','MONITOR','RECOVER'],['IDENTITATE','PERMISIUNI','MONITORIZARE','RECUPERARE'],
 [('AUTHENTICATION','Proves who or what is requesting access. Machines and people may have separate identities.'),('AUTHORIZATION','Decides which action that identity may perform. A reader should not automatically be a writer.'),('ISOLATION','Separate workloads, network zones and credentials limit what an incident can affect.'),('RESILIENCE','Monitoring, multiple copies and tested recovery reduce disruption, but none can prevent every failure.')],
 [('AUTENTIFICARE','Verifică cine cere accesul. Oamenii și mașinile pot avea identități separate.'),('AUTORIZARE','Decide ce acțiuni sunt permise. Cine poate citi nu trebuie să poată și modifica.'),('IZOLARE','Separarea sarcinilor, rețelelor și credențialelor limitează pagubele.'),('REZILIENȚĂ','Monitorizarea, copiile și recuperarea testată reduc întreruperile, dar nu elimină toate riscurile.')],
 'Safe infrastructure asks two questions: Who are you? What are you allowed to do?',
 'Infrastructura sigură întreabă: Cine ești? Ce ai voie să faci?',
 'Can a service be online and still leak private records?',
 'Poate un serviciu să funcționeze și totuși să expună date private?'),
('HOW AI CLUSTERS WORK','CUM FUNCȚIONEAZĂ CLUSTERELE AI',
 'Training changes model parameters; inference uses a trained model to answer.',
 'Antrenarea schimbă parametrii modelului; inferența produce răspunsuri.',
 ['DATA','TRAINING','MODEL','INFERENCE'],['DATE','ANTRENARE','MODEL','INFERENȚĂ'],
 [('TRAINING','Repeatedly process examples and adjust a model’s internal parameters. May use many graphics processors together.'),('CHECKPOINT','Saved training state allows work to resume after interruption. It takes time and storage to save.'),('INFERENCE','Use an existing model to process new input. The serving system manages incoming requests and resources.'),('KV CACHE (KEY-VALUE CACHE)','During some transformer-model inference, stored intermediate attention data helps avoid recomputing earlier tokens.')],
 [('ANTRENARE','Prelucrează repetat exemple și modifică parametrii modelului. Poate folosi multe procesoare grafice.'),('CHECKPOINT (PUNCT DE SALVARE)','Stare de antrenare salvată pentru reluare după întreruperi; ocupă timp și spațiu.'),('INFERENȚĂ','Modelul deja antrenat prelucrează cereri noi. Serviciul gestionează cereri și resurse.'),('KV CACHE (KEY-VALUE CACHE)','În inferența unor modele transformer, date de atenție intermediare memorate evită recalcularea tokenurilor vechi.')],
 'Training builds the recipe. Inference uses it. Both need data centers.',
 'Antrenarea construiește rețeta. Inferența o folosește. Ambele au nevoie de centre de date.',
 'If the model is already trained, why might a response still be slow?',
 'Dacă modelul este antrenat, de ce poate răspunde totuși lent?'),
('QUEUES & PRIORITY HEAPS','COZI ȘI HEAP-URI DE PRIORITĂȚI',
 'A structure for waiting can determine who receives expensive hardware next.',
 'Structura de așteptare poate decide cine primește hardware-ul scump.',
 ['NEW JOBS','WAITING LINE','PRIORITY','GPU AVAILABLE'],['SARCINI NOI','COADĂ','PRIORITATE','GPU LIBER'],
 [('FIFO (FIRST IN, FIRST OUT)','A queue normally removes the oldest item first. This is fair by arrival order, but not always by urgency.'),('PRIORITY QUEUE','Returns the highest-priority item first. The queue can be implemented with a heap (a special tree shape).'),('HEAP (TREE FOR PRIORITY)','A heap lets software find a highest- or lowest-priority item quickly; it does not keep all items fully sorted.'),('THE TRADE-OFF','Strict priority can starve low-priority jobs. Real schedulers may add fairness, quotas or aging rules.')],
 [('FIFO (FIRST IN, FIRST OUT)','O coadă simplă scoate de obicei prima sarcină sosită. E corect după sosire, dar nu întotdeauna după urgență.'),('COADĂ DE PRIORITĂȚI','Extrage mai întâi elementul cu prioritate mai mare. Poate folosi un heap (tip special de arbore).'),('HEAP (ARBORE PENTRU PRIORITĂȚI)','Permite găsirea rapidă a unui element cu prioritate maximă sau minimă, fără a sorta integral lista.'),('COMPROMISUL','Prioritățile rigide pot bloca sarcini obișnuite. Planificatorul poate aplica cote sau echitate.')],
 'The scheduler is not “thinking”: it is following ordering and capacity rules.',
 'Planificatorul nu „gândește”: aplică reguli de ordine și capacitate.',
 'Which structure chooses the oldest job, and which picks the most urgent?',
 'Ce structură alege cea mai veche sarcină și care o alege pe cea urgentă?'),
('HASH MAPS, CACHES & SETS','DICȚIONARE, CACHE ȘI MULȚIMI',
 'Avoid searching every computer or recalculating the same answer.',
 'Nu căuta fiecare calculator și nu recalcula mereu același rezultat.',
 ['KEY','LOOKUP','VALUE','REUSE'],['CHEIE','CĂUTARE','VALOARE','REUTILIZARE'],
 [('HASH MAP (KEY → VALUE)','Store an association such as job ID → assigned server. A hash function helps locate the key efficiently.'),('CACHE (FAST COPY)','Keep a recent or popular value near where it is needed. The cache may become outdated.'),('SET (UNIQUE MEMBERS)','Keep unique identifiers: servers already visited or active connections. It prevents duplicate entries.'),('CACHE INVALIDATION','A cached answer is useful only while it is valid for its context. Changes, time and permissions matter.')],
 [('HASH MAP (CHEIE → VALOARE)','Asociază, de exemplu, identificator sarcină → server atribuit. O funcție hash ajută la localizare.'),('CACHE (COPIE RAPIDĂ)','Păstrează aproape valori recente sau populare. Copia poate deveni învechită.'),('SET (MULȚIME CU ELEMENTE UNICE)','Păstrează identificatori fără dubluri: servere vizitate sau conexiuni active.'),('INVALIDAREA CACHE-ULUI','Copia e utilă numai cât timp este valabilă în contextul ei. Contează schimbările, timpul și permisiunile.')],
 'A dictionary answers “Where is job 42?”; a cache asks “Can I reuse it safely?”',
 'Dicționarul răspunde „Unde e sarcina 42?”; cache-ul „Pot refolosi în siguranță?”',
 'Why might yesterday’s cached inventory give the wrong answer today?',
 'De ce inventarul memorat ieri poate da un rezultat greșit azi?'),
('TREES, INDEXES & EVENT LOGS','ARBORI, INDEXURI ȘI JURNALE',
 'Finding saved data and remembering changes are different operations.',
 'Căutarea datelor și păstrarea istoricului sunt operații diferite.',
 ['RECORDS','B-TREE INDEX','READ','EVENT LOG'],['ÎNREGISTRĂRI','INDEX B-TREE','CITIRE','JURNAL'],
 [('B-TREE (BALANCED SEARCH TREE)','A tree-based database index helps find exact or ranged values without examining every record.'),('INDEX IS NOT THE DATA','Like a book index: it points toward records. Indexes improve some reads but add work during writes.'),('APPEND-ONLY LOG','A sequence of events added at the end. Good for following what changed and replaying processing.'),('REPLICATION & ORDER','Several machines may copy logs. Order and delivery guarantees must be defined; “stored” is not always “fully committed”.')],
 [('B-TREE (ARBORE DE CĂUTARE ECHILIBRAT)','Index de baze de date ce permite căutarea unei valori sau a unui interval fără scanarea tuturor datelor.'),('INDEXUL NU ESTE DATELE','Ca indexul unei cărți: indică poziția înregistrărilor. Ajută la citire, dar costă la scriere.'),('JURNAL CU ADĂUGARE LA FINAL','Secvență de evenimente noi. Permite urmărirea schimbărilor și reluarea procesării.'),('REPLICARE ȘI ORDINE','Mai multe mașini pot copia jurnalul. Ordinea și garanțiile de livrare trebuie definite precis.')],
 'An index finds an item. A log remembers what happened.',
 'Indexul găsește un obiect. Jurnalul ține minte ce s-a întâmplat.',
 'Why can adding more indexes slow down database updates?',
 'De ce multe indexuri pot încetini actualizarea bazei de date?'),
('GRAPHS, VECTORS & AI SEARCH','GRAFURI, VECTORI ȘI CĂUTARE AI',
 'The data structure changes how an AI center finds relevant information.',
 'Structura de date influențează cum găsește un sistem AI informația relevantă.',
 ['QUESTION','VECTOR','NEIGHBORS','DOCUMENT'],['ÎNTREBARE','VECTOR','VECINI','DOCUMENT'],
 [('GRAPH (NODES + EDGES)','Represents links: service A calls service B; or documents are connected by similarity.'),('VECTOR (LIST OF NUMBERS)','A model can encode a text into numbers called an embedding. Similar meanings may yield nearby vectors.'),('NEAREST-NEIGHBOR INDEX','Special indexes accelerate approximate similarity search; results depend on the index and distance metric.'),('RAG (RETRIEVAL-AUGMENTED GENERATION)','A system retrieves potentially relevant text before generating an answer; retrieval does not guarantee truth.')],
 [('GRAF (NODURI ȘI LEGĂTURI)','Reprezintă relații: serviciul A îl apelează pe B; sau documentele sunt conectate prin similaritate.'),('VECTOR (LISTĂ DE NUMERE)','Un model poate transforma textul în numere, numite embedding. Sensuri apropiate pot genera vectori apropiați.'),('INDEX PENTRU VECINI APROPIAȚI','Indexuri speciale accelerează căutarea aproximativă a similarității. Depinde de măsura distanței.'),('RAG (RETRIEVAL-AUGMENTED GENERATION)','Sistemul caută fragmente potențial relevante înainte să răspundă. Căutarea nu garantează adevărul.')],
 'A graph shows relationships; a vector index suggests what is similar.',
 'Graful arată relații; indexul vectorial sugerează ce este similar.',
 'Can two documents be numerically similar but have different factual claims?',
 'Pot două documente să fie apropiate numeric, dar să afirme lucruri diferite?'),
]
assert len(D)==13

def qr_for(url,sz=300):
 q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q,border=2,box_size=7)
 q.add_data(url);q.make(fit=True)
 return q.make_image(fill_color='#10243B',back_color='white').convert('RGB').resize((sz,sz))

def block(c,x,top,w,h,fill,r=0,stroke=None):
 c.setFillColor(HexColor(fill))
 c.setStrokeColor(HexColor(stroke or fill))
 if r:c.roundRect(x,H-top-h,w,h,r,stroke=bool(stroke),fill=1)
 else:c.rect(x,H-top-h,w,h,stroke=bool(stroke),fill=1)

def txt(c,x,top,text,size=10,color=N,font='Lato',align='left'):
 c.setFillColor(HexColor(color));c.setFont(font,size)
 (c.drawCentredString if align=='center' else c.drawString)(x,H-top-size*.82,text)

def par(c,text,x,top,w,fontsize=9.5,leading=12,color=N,font='Lato',maxheight=None):
 style=ParagraphStyle('p',fontName=font,fontSize=fontsize,leading=leading,textColor=HexColor(color),spaceBefore=0,spaceAfter=0)
 p=Paragraph(escape(text).replace('\n','<br/>'),style)
 _,h=p.wrap(w,700)
 if maxheight is not None and h>maxheight:raise ValueError(f'text overflow {h:.1f}>{maxheight}: {text[:90]}')
 p.drawOn(c,x,H-top-h)
 return h

def diagram(c,n,flow,accent):
 # A distinctive schematic for each lesson, with exact shapes and meaningful labels.
 top=253;left=40;wd=515;gap=12;col=(wd-3*gap)/4
 if n==10: # priority queue
  txt(c,54,top+17,'FIFO' if c._lang=='en' else 'PRIMUL SOSIT',10,accent,'LatoBold')
  for j,label in enumerate(['A','B','C']):
   block(c,70+j*66,top+40,52,49,'#E7F1FB',10);txt(c,96+j*66,top+56,label,17,N,'LatoHeavy','center')
  txt(c,317,top+17,'PRIORITY' if c._lang=='en' else 'PRIORITATE',10,accent,'LatoBold')
  for j,(label,score) in enumerate([('A','1'),('B','9'),('C','3')]):
   block(c,322+j*66,top+40,53,49,'#E1F6F1',10)
   txt(c,348+j*66,top+49,label,14,N,'LatoBold','center');txt(c,348+j*66,top+70,score,10,accent,'LatoHeavy','center')
  txt(c,71,top+99,'A first' if c._lang=='en' else 'A primul',10,N,'LatoBold')
  txt(c,323,top+99,'B first (score 9)' if c._lang=='en' else 'B primul (scor 9)',10,N,'LatoBold')
 elif n==11: # hash + cache
  for j,(a,b) in enumerate([('job-42','node-3'),('file-8','cache'),('user-7','session')]):
   block(c,58,top+21+j*35,147,28,'#EAF3FC',7)
   txt(c,132,top+29+j*35,a,11,N,'LatoBold','center')
   txt(c,251,top+27+j*35,'→',22,accent,'LatoHeavy','center')
   block(c,302,top+21+j*35,175,28,'#E0F5F0',7)
   txt(c,389,top+29+j*35,b,11,N,'LatoBold','center')
 elif n==12: # B tree and log
  block(c,100,top+18,80,28,'#D7EEF0',7);txt(c,140,top+26,'40',12,N,'LatoBold','center')
  c.setStrokeColor(HexColor(accent));c.setLineWidth(1.5)
  c.line(139,H-(top+46),99,H-(top+69));c.line(141,H-(top+46),210,H-(top+69))
  for x,s in [(56,'10 | 20'),(167,'50 | 80')]:
   block(c,x,top+69,88,28,'#E8F0FA',7);txt(c,x+44,top+77,s,10,N,'LatoBold','center')
  txt(c,285,top+25,'EVENT LOG' if c._lang=='en' else 'JURNAL',11,accent,'LatoHeavy')
  for j,t in enumerate(['01 WRITE','02 COMMIT','03 REPLAY'] if c._lang=='en' else ['01 SCRIE','02 CONFIRMĂ','03 REIA']):
   block(c,286,top+50+j*27,206,23,'#E0F5F0',6);txt(c,298,top+55+j*27,t,10,N,'LatoBold')
 elif n==13: # vector proximity & graph
  pts=[(102,top+50),(166,top+78),(225,top+36),(252,top+111),(142,top+120)]
  links=[(0,1),(1,2),(1,4),(2,3),(3,4)]
  c.setStrokeColor(HexColor('#78A0BB'));c.setLineWidth(2)
  for a,b in links:c.line(pts[a][0],H-pts[a][1],pts[b][0],H-pts[b][1])
  for j,(x,y) in enumerate(pts):
   block(c,x-13,y-13,26,26,accent if j==1 else '#BFE3ED',13);txt(c,x,y-5,str(j+1),10,'#0B2942','LatoBold','center')
  txt(c,311,top+25,'SIMILARITY SPACE' if c._lang=='en' else 'SPAȚIU DE SIMILARITATE',9,accent,'LatoBold')
  for x,y in [(352,top+70),(389,top+46),(412,top+85),(475,top+58)]:
   block(c,x,y,12,12,'#A0DFD1',6)
  block(c,389,top+46,12,12,'#EEA972',6)
  txt(c,341,top+111,'near ≠ true' if c._lang=='en' else 'aproape ≠ adevărat',10,N,'LatoBold')
 else:
  for j,t in enumerate(flow):
   x=left+j*(col+gap)
   block(c,x,top+35,col,70,'#E8F2FA' if j%2==0 else '#E4F5F0',12)
   block(c,x+10,top+45,25,23,accent,7)
   txt(c,x+22.5,top+51,f'{j+1:02d}',9,WHITE,'LatoHeavy','center')
   # Flow steps up to 22 chars: wrap to two centered lines
   words=t.split(' ');lines=[];line=''
   for word in words:
    if len(line+' '+word)>14: lines.append(line);line=word
    else:line=(line+' '+word).strip()
   lines.append(line)
   for k,ln in enumerate(lines[:2]): txt(c,x+col/2,top+77+14*k,ln,9,N,'LatoBold','center')
   if j<3:txt(c,x+col+gap/2,top+63,'›',22,accent,'LatoHeavy','center')

def draw_one(n,lang,item):
 en=lang=='en'; title=item[0] if en else item[1]; sub=item[2] if en else item[3];flow=item[4] if en else item[5];cards=item[6] if en else item[7];anchor=item[8] if en else item[9];question=item[10] if en else item[11]
 accent=('#0F8E8D' if n%3==1 else ('#4773AC' if n%3==2 else '#8661AC'))
 path=O/'materials/datacenters'/f'dc-{n:02d}-{lang}.pdf';path.parent.mkdir(exist_ok=True,parents=True)
 c=canvas.Canvas(str(path),pagesize=A4,pageCompression=1);c._lang=lang;c.setTitle('LEARN | '+title);c.setAuthor('Vlad Belciug');c.setSubject('Bilingual data center learning series')
 block(c,0,0,W,H,PAPER)
 block(c,0,0,W,175,N)
 block(c,0,0,8,175,accent)
 txt(c,35,24,'LEARN  /  DATA CENTERS  /  BEGINNER EDITION' if en else 'LEARN  /  CENTRE DE DATE  /  PENTRU ÎNCEPĂTORI',9,'#92D7D6','LatoHeavy')
 first_terms={12:('B-tree (balanced search tree index)','B-tree (index de căutare echilibrat)'),3:('CPU (Central Processing Unit)  ·  GPU (Graphics Processing Unit)','CPU (Central Processing Unit)  ·  GPU (Graphics Processing Unit)'),5:('AI (Artificial Intelligence)','AI (Artificial Intelligence - inteligență artificială)'),7:('AI (Artificial Intelligence)','AI (Artificial Intelligence - inteligență artificială)'),9:('AI (Artificial Intelligence)  ·  KV (Key-Value)','AI (Artificial Intelligence - inteligență artificială)  ·  KV (Key-Value)'),10:('FIFO (First In, First Out)  ·  GPU (Graphics Processing Unit)','FIFO (First In, First Out)  ·  GPU (Graphics Processing Unit)'),13:('AI (Artificial Intelligence)  ·  RAG (Retrieval-Augmented Generation)','AI (Artificial Intelligence - inteligență artificială)')}
 if n in first_terms:
  txt(c,35,40,first_terms[n][0 if en else 1],7.6,'#D6EEE6','LatoBold')
 # wrap title depending length
 lines=[];current=''; limit=30 if en else 27
 for w in title.split():
  if len((current+' '+w).strip())>limit:lines.append(current);current=w
  else:current=(current+' '+w).strip()
 lines.append(current)
 if len(lines)>2:raise ValueError(f'long title {title}')
 for j,t in enumerate(lines):txt(c,35,55+j*38,t,26 if len(t)>27 else 29,WHITE,'LatoHeavy')
 top=55+len(lines)*38+9
 par(c,sub,35,top,430,10.3,13,'#D0E7ED',maxheight=30)
 img=qr_for(URL+f'#dc-{n:02d}')
 ib=io.BytesIO();img.save(ib,'PNG');ib.seek(0)
 from reportlab.lib.utils import ImageReader
 c.drawImage(ImageReader(ib),486,H-111,84,84)
 txt(c,528,116,'SCAN  /  LEARN',7,'#CCDEE9','LatoBold','center')
 c.linkURL(URL+f'#dc-{n:02d}',(486,H-111,570,H-27),relative=0,thickness=0)
 txt(c,38,196,'THE SYSTEM AT A GLANCE' if en else 'SISTEMUL DINTR-O PRIVIRE',10,accent,'LatoHeavy')
 block(c,35,220,525,159,WHITE,14,stroke='#D8E3ED')
 diagram(c,n,flow,accent)
 txt(c,38,393,'FOUR IDEAS THAT MATTER' if en else 'PATRU IDEI IMPORTANTE',10,accent,'LatoHeavy')
 for j,(heading,description) in enumerate(cards):
  x=36+(j%2)*267;y=417+(j//2)*137
  block(c,x,y,257,127,WHITE,12,stroke='#DCE6EF');block(c,x,y,5,127,accent,2)
  block(c,x+12,y+11,22,22,'#E1F1F3',7);txt(c,x+23,y+17,str(j+1),10,accent,'LatoHeavy','center')
  hs=8.7 if len(heading)>29 else 10.1
  # multi-line short heading
  ph=par(c,heading,x+43,y+15,205,hs,11.3,N,'LatoBold',maxheight=25)
  hy=y+(42 if ph<=12 else 50)
  fs=8.8
  par(c,description,x+14,hy,228,fs,11.5,MUTED,maxheight=(y+120-hy))
 block(c,35,696,525,65,'#DBF3EA',12)
 txt(c,49,709,'MEMORY HOOK' if en else 'DE ȚINUT MINTE',9,'#12746D','LatoHeavy')
 par(c,anchor,49,728,490,9.7,12,N,'LatoBold',maxheight=29)
 block(c,35,772,525,43,N,10)
 txt(c,49,782,'DISCUSS WITHOUT COMPUTERS' if en else 'DISCUTAȚI FĂRĂ CALCULATOARE',8,'#ADEAD1','LatoBold')
 par(c,question,49,797,490,8.7,10.5,WHITE,maxheight=18)
 txt(c,36,823,'© 2026 VLAD BELCIUG  •  FREE FOR PERSONAL STUDY',7,MUTED,'LatoBold')
 txt(c,560,823,f'{n:02d} / 13',8,accent,'LatoBold','right') if False else None
 c.save()
 # preview from English only later
 return path

def run():
 from PIL import Image
 for n,item in enumerate(D,1):
  for lang in ('en','ro'):
   draw_one(n,lang,item)
  doc=fitz.open(O/'materials/datacenters'/f'dc-{n:02d}-en.pdf')
  pix=doc[0].get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
  out=O/'previews'/f'dc-{n:02d}.webp';out.parent.mkdir(exist_ok=True,parents=True)
  im.save(out,'WEBP',quality=83,method=6)
 for lang in ('en','ro'):
  whole=fitz.open()
  for n in range(1,14):
   d=fitz.open(O/'materials/datacenters'/f'dc-{n:02d}-{lang}.pdf');whole.insert_pdf(d,links=False)
  target=O/'collections'/f'datacenters-{lang}.pdf';target.parent.mkdir(exist_ok=True,parents=True)
  whole.save(target,garbage=3,deflate=True)
 print('Generated data center collection: 26 A4 PDFs, 2 booklets, 13 previews')

if __name__=='__main__':run()