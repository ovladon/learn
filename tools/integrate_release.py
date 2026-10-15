from pathlib import Path
import importlib.util,re,json,fitz,zipfile,shutil,io
ROOT=Path('/mnt/data/_learn_work');W=ROOT/'site';PREV=Path('/mnt/data/LEARN_OWNER_LIBRARY_BACKUP_2026-10-15')
sp=importlib.util.spec_from_file_location('dc',ROOT/'build_datacenter.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
catpath=W/'catalog.js'; raw=catpath.read_text(encoding='utf-8')
tracks=json.loads(raw.split('window.LEARN_TRACKS = ')[1].split(';\nwindow.LEARN_CATALOG = ')[0]);cat=json.loads(raw.split('window.LEARN_CATALOG = ')[1].split(';\n')[0])
assert len(tracks)==2 and len(cat)==26
tracks.append({'id':'dc','title_en':'Data centers & AI infrastructure','title_ro':'Centre de date și infrastructură AI','label_en':'LEARNING TRACK / 03','label_ro':'TRASEU DE ÎNVĂȚARE / 03','number':'03','booklet_en':'collections/datacenters-en.pdf','booklet_ro':'collections/datacenters-ro.pdf'})
for idx,item in enumerate(m.D,1):
 title_en,title_ro,desc_en,desc_ro=item[:4]
 cat.append({'id':f'dc-{idx:02d}','category':'dc','title_en':title_en.title().replace('Ai','AI').replace('Cpu','CPU').replace('Gpu','GPU'),
 'title_ro':title_ro.title().replace('Ai','AI').replace('Gpu','GPU').replace('Cpu','CPU'),
 'desc_en':desc_en,'desc_ro':desc_ro,'pdf_en':f'materials/datacenters/dc-{idx:02d}-en.pdf','pdf_ro':f'materials/datacenters/dc-{idx:02d}-ro.pdf','preview':f'previews/dc-{idx:02d}.webp',
 'keywords':' '.join([title_en,title_ro,desc_en,desc_ro,'data center AI infrastructure distributed systems queue heap hash map cache index B-tree log graph vector GPU']).lower()})
catpath.write_text('/* LEARN teaching library: author-published content only. */\nwindow.LEARN_TRACKS = '+json.dumps(tracks,indent=2,ensure_ascii=False)+';\nwindow.LEARN_CATALOG = '+json.dumps(cat,indent=2,ensure_ascii=False)+';\n',encoding='utf-8')
index=W/'index.html';s=index.read_text(encoding='utf-8');s=s.replace('<strong id="count">26</strong>','<strong id="count">39</strong>');s=s.replace('A visual learning library','A free visual learning library');s=s.replace('visual learning library: computing foundations, data structures, artificial intelligence and AI agents.', 'visual learning library: computing, data structures, artificial intelligence, AI agents and data centers.');index.write_text(s,encoding='utf-8')
readme=W/'README.md';s=readme.read_text(encoding='utf-8');s=s.replace('**26 topics, 52 individual A4 infographic PDFs**','**39 topics, 78 individual A4 infographic PDFs**').replace('**26 topics, 52 individual A4','**39 topics, 78 individual A4').replace('26 visual','39 visual').replace('26 individual','39 individual');s=s.replace('Computing Foundations, including Data Structures and both Big-O sheets | 13 | 26 |','Computing Foundations, including Data Structures and both Big-O sheets | 13 | 26 |');s=s.replace('| **Total** | **26** | **52** |','| Data centers, AI infrastructure and real-world data structures | 13 | 26 |\n| **Total** | **39** | **78** |');s=s.replace('26 files).\n- Full', '26 files).\n- Data centers and AI infrastructure: `materials/datacenters/` (26 files).\n- Full')
s+='\n## Data centers & AI infrastructure\n\nThe third teaching track explains data-center hardware, request flow, power, cooling, networks, workload scheduling, security, AI training/inference, and real-life uses of queues, priority heaps, hash maps, caches, sets, tree indexes, append-only logs, graphs, and vector retrieval. Every sheet stands alone in English and Romanian and has a permanent scannable QR code.\n\nThe Computing Foundations series was audited for first-use acronyms and corrected while retaining the original lesson IDs and QR destinations.\n';readme.write_text(s,encoding='utf-8')
for name in ['RELEASE_INFO.json','SITE_MANIFEST.json']:
 p=W/name
 j=json.loads(p.read_text())
 j.update({'topics':39,'individual_student_pdfs':78,'subjects':['Computing Foundations','AI and agentic systems','Data centers and AI infrastructure'],'site_url':'https://ovladon.github.io/learn/','current_release':'2026-10-15 foundations acronym fix and data center collection','publisher':'Vlad Belciug (@ovladon)'})
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Big-O historical standalone mirrors updated QR-coded foundations, preserve same file URL.
for lg in ('en','ro'):
 shutil.copy2(W/f'materials/foundations/fund-11-{lg}.pdf',W/f'collections/big-o-from-zero-{lg}.pdf')
 shutil.copy2(W/f'materials/foundations/fund-12-{lg}.pdf',W/f'collections/big-o-quick-reference-{lg}.pdf')
# Update read-only owner-only deployment checks in the release workspace.
yml=W/'.github/workflows/pages.yml';yml.parent.mkdir(parents=True,exist_ok=True)
base=(PREV/'website/.github/workflows/pages.yml').read_text()
assert "if: github.repository == 'ovladon/learn' && github.actor == 'ovladon'" in base
base=base.replace("==52,'Expected 52 student PDFs'","==78,'Expected 78 student PDFs'")
base=base.replace("assert len(list((root/'collections').glob('big-o-*.pdf')))==4,'Expected four Big-O PDFs'","assert len(list((root/'collections').glob('big-o-*.pdf')))==4,'Expected four Big-O PDFs'\n          assert len(list((root/'materials/datacenters').glob('dc-*.pdf')))==26,'Expected 26 data center PDFs'")
base=base.replace('52 sheets, four standalone Big-O sheets','78 sheets, four standalone Big-O sheets')
base=base.replace(")==52", ")==78")
assert "==78" in base, "Workflow must validate 78 PDFs"
yml.write_text(base)
# Source repository can stay in owner's offline backup only; included teaching source under teacher-only dir.
teach=ROOT/'teacher_only';teach.mkdir(exist_ok=True)
shutil.copy2(ROOT/'build_datacenter.py',teach/'datacenter_poster_generator.py')
shutil.copy2(ROOT/'fix_foundations.py',teach/'foundations_first_use_acronyms.py')
# Developer details+design factual-source URLs; not shipped publicly until approved by owner.
refs={
 'Kubernetes scheduler':'https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/',
 'Redis data structures':'https://redis.io/docs/latest/develop/data-types/',
 'Redis choosing data types':'https://redis.io/docs/latest/develop/data-types/compare-data-types/',
 'PostgreSQL index types':'https://www.postgresql.org/docs/current/indexes-types.html',
 'NVIDIA AI networking architecture':'https://docs.nvidia.com/ncx/ncp-software-reference-guide/latest/data-center-architecture.html'
}
for lg in ('en','ro'):
 lines=['LEARN: 13 DATA CENTER LESSONS' if lg=='en' else 'LEARN: 13 LECȚII DESPRE CENTRE DE DATE','',
 'Each lesson is an A4 stand-alone handout. Project the QR or hand out printed pages.' if lg=='en' else 'Fiecare lecție este o fișă A4 independentă; proiectați codurile QR sau distribuiți foi.',
 'No laptops required: ask students to become requests, servers, queues and cache entries.' if lg=='en' else 'Fără laptop: studenții devin cereri, servere, cozi și intrări de cache.','',
 'SUGGESTED ACTIVITIES / ACTIVITĂȚI:','1. Student roles: browser, load balancer, worker, database, response.',
 '2. Build a FIFO queue, then rank students by numeric priority and discuss fairness.',
 '3. Use name->server cards as a hash map; add a stale cache card to trigger revalidation.',
 '4. Arrange folders as a tree and arrows between services as a directed graph.',
 '5. Sort cards by similarity and explain why close scores do not prove truth.','',
 'TECHNICAL REFERENCES / SURSE (verified 2026):']
 for k,v in refs.items():lines.extend([k,v])
 (teach/f'Data_Center_Instructor_Notes_{lg.upper()}.txt').write_text('\n'.join(lines),encoding='utf-8')
# check site paths
files={f.relative_to(W).as_posix() for f in W.rglob('*') if f.is_file()}
for d in cat:
 for k in ('pdf_en','pdf_ro','preview'):
  assert d[k] in files,(d['id'],k,d[k])
for t in tracks:
 for k in ('booklet_en','booklet_ro'): assert t[k] in files
assert len(list((W/'materials').rglob('*.pdf')))==78
print('Integrated:',len(tracks),'tracks;',len(cat),'topics; 78 files; all references exist.')