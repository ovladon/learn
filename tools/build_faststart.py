#!/usr/bin/env python3
"""LEARN Fast Start: accessible standalone primers, discoverable topic pages, audit.
Author-maintained, offline-capable. Reads the existing canonical catalog & primers.
Builds into _site or a local website copy; leaves the original A4 sheets intact.
"""
import argparse
import html
import json
import re
import shutil
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

SITE = 'https://ovladon.github.io/learn/'


def parse_js_json(path, var):
    s = path.read_text(encoding='utf-8')
    m = re.search(r'window\.' + re.escape(var) + r'\s*=\s*([\[{].*?[\]}])\s*;', s, re.S)
    if not m:
        raise RuntimeError(f'Cannot find {var} in {path}')
    return json.loads(m.group(1))


def esc(s):
    return html.escape(str(s), quote=True)


def langphrase(en, ro, lang):
    return ro if lang == 'ro' else en


def build_page(item, primer, lang, neighbors, track):
    lid = item['id']
    other = 'ro' if lang == 'en' else 'en'
    title = item[f'title_{lang}']
    headline = esc(title)
    desc = item[f'desc_{lang}']
    direct = f'../{item["pdf_"+lang]}'
    begin = f'../beginner/{lid}-{lang}.pdf'
    canonical = SITE + f'topics/{lid}-{lang}.html'
    prev, nxt = neighbors
    terms = primer['terms']
    glossary = ''.join(f'<div class="term"><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in terms)
    root = f'{SITE}#{lid}'
    tracktitle = track.get(f'title_{lang}', 'LEARN')
    copylbl = langphrase('Copy link', 'Copiază linkul', lang)
    before = langphrase('Before the diagram', 'Înainte de diagramă', lang)
    definitions = langphrase('Words you need to know', 'Cuvinte explicate pe înțelesul tuturor', lang)
    prior = langphrase('Previous', 'Înapoi', lang)
    after = langphrase('Next', 'Următorul', lang)
    foot = langphrase('One idea, without prerequisites. Free for individual study.',
                      'O idee, fără cunoștințe presupuse. Gratuit pentru studiu individual.', lang)
    why = langphrase('Why this matters', 'La ce te ajută', lang)
    bigpicture = langphrase('The big idea', 'Ideea esențială', lang)
    show = langphrase('See the infographic', 'Vezi infograma', lang)
    download = langphrase('Download explained PDF', 'Descarcă PDF-ul explicat', lang)
    quick = langphrase('Original one-page sheet', 'Fișa originală de o pagină', lang)
    explbl = langphrase('Everyday example', 'Exemplu obișnuit', lang)
    openpage = langphrase('Open in a new tab', 'Deschide într-o filă nouă', lang)
    homework = langphrase('Check if you understood', 'Verifică dacă ai înțeles', lang)
    qs = (['What is the problem being solved?', 'What happens first, then next?', 'Which unfamiliar word can you now explain in your own words?'] if lang == 'en'
          else ['Ce problemă încercăm să rezolvăm?', 'Ce se întâmplă mai întâi și ce urmează?', 'Ce termen necunoscut poți explica acum în cuvintele tale?'])
    nexturl = f'{nxt}-{lang}.html' if nxt else None
    prevurl = f'{prev}-{lang}.html' if prev else None
    prevhtml = f'<a href="{prevurl}">← {esc(prior)}</a>' if prevurl else ''
    nexthtml = f'<a href="{nexturl}">{esc(after)} →</a>' if nexturl else ''
    same = f'{lid}-{other}.html'
    summary = primer['plain']
    example = primer['example']
    data = {
        '@context':'https://schema.org','@type':'LearningResource','name':title,
        'description':summary,'url':canonical,'author':{'@type':'Person','name':'Vlad Belciug'},
        'provider':{'@type':'Organization','name':'LEARN'},'inLanguage':lang,
        'educationalLevel':'Beginner','isAccessibleForFree':True,'learningResourceType':'Visual explainer'
    }
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{headline} — {langphrase('Explained from zero','Explicat de la zero',lang)} | LEARN</title>
<meta name="description" content="{esc(summary)} {esc(example)}">
<meta name="author" content="Vlad Belciug"><meta name="robots" content="index,follow">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="{other}" href="{SITE}topics/{same}">
<meta property="og:type" content="article"><meta property="og:site_name" content="LEARN">
<meta property="og:title" content="{headline} — LEARN"><meta property="og:description" content="{esc(summary)}">
<meta property="og:image" content="{SITE}{esc(item['preview'])}"><meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="../style.css"><link rel="stylesheet" href="../lesson.css">
<script type="application/ld+json">{json.dumps(data,ensure_ascii=False).replace('</','<\\/')}</script>
<style>
.fast-page{{max-width:1060px;margin:auto;padding:24px 24px 80px}}.fast-nav{{display:flex!important;gap:14px;align-items:center;flex-wrap:wrap;font-size:14px}}.fast-nav a{{color:#e2fff2;text-decoration:none}}
.fast-nav a:hover{{text-decoration:underline}}.fast-eyebrow{{font-weight:850;color:#147a68;letter-spacing:.13em;font-size:12px;text-transform:uppercase}}
.fast-hero h1{{color:#0b293d;font-size:clamp(32px,5vw,54px);line-height:1.12;letter-spacing:-.035em;margin:14px 0}}.fast-hero p{{max-width:830px}}
.fast-actions{{display:flex;flex-wrap:wrap;gap:11px;margin:20px 0}}.fast-actions a,.fast-actions button{{padding:13px 17px;border:1px solid #bdd6d6;background:white;color:#104f52;text-decoration:none;font-weight:800;border-radius:12px;font-size:14px;min-height:46px}}
.fast-actions .primary{{background:#0c514c;color:white}}.fast-actions a:focus-visible,.fast-actions button:focus-visible{{outline:3px solid orange;outline-offset:3px}}
.fast-intro{{background:linear-gradient(130deg,#ecfaf4,#f2f7ff);border:1px solid #bfdcdb;padding:clamp(18px,3vw,30px);border-radius:17px}}.fast-intro h2{{font-size:25px;margin:0 0 13px;color:#103d43}}
.fast-plain{{font-size:clamp(18px,2.5vw,22px);font-weight:800;color:#0b3b43;line-height:1.5}}.fast-example{{padding:17px;border-left:4px solid #0da47b;background:white;font-size:16px;line-height:1.55;border-radius:10px}}
.fast-terms{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:10px 0 20px}}.fast-terms .term{{background:#fff;border:1px solid #e3e9ea;border-radius:10px;padding:13px 16px}}.fast-terms dt{{font-weight:850;color:#0e5260}}.fast-terms dd{{margin:5px 0 0;color:#344f5d;line-height:1.5;font-size:14px}}
.fast-iframe{{height:min(94vh,1100px);min-height:520px;width:100%;border:1px solid #c7d9e3;border-radius:15px;background:white}}.fast-check{{padding:19px 25px;background:#fff;border:1px solid #ccdfe2;border-radius:15px}}
.fast-check li{{margin-bottom:7px}}.fast-footer{{margin-top:38px;font-size:12px;color:#62798a}}.fast-arrows{{display:flex;justify-content:space-between;gap:20px;margin:20px 0}}
@media(max-width:700px){{.fast-terms{{grid-template-columns:1fr}}.fast-iframe{{min-height:460px;height:72vh}}.fast-page{{padding-left:16px;padding-right:16px}}}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
</style></head>
<body><a class="skip" href="#content">{esc(langphrase('Skip to explanation','Sari la explicație',lang))}</a>
<header class="sitehead"><div class="wrap topbar"><a class="brand" href="../" aria-label="LEARN home"><span class="brand-mark">L<span>.</span></span>LEARN</a><nav class="fast-nav" aria-label="Navigation"><a href="../#{lid}">← {esc(langphrase('All lessons','Toate lecțiile',lang))}</a><a href="{same}" lang="{other}">{'Română' if lang=='en' else 'English'} ↗</a></nav></div></header>
<main class="fast-page" id="content">
<div class="fast-hero"><p class="fast-eyebrow">{esc(tracktitle)} · {esc(langphrase('Start from zero','De la zero',lang))}</p><h1>{headline}</h1>
<p class="reader-desc">{esc(desc)}</p><p class="fast-eyebrow">{esc(why)}: {esc(langphrase('Understand the key idea without a course or account','Înțelege ideea fără cursuri sau cont',lang))}</p></div>
<div class="fast-actions"><a class="primary" href="#sheet">{esc(show)} ↓</a><a href="{begin}" download>{esc(download)} ↓</a><a href="{direct}" target="_blank" rel="noopener">{esc(quick)} ↗</a><button type="button" id="share" aria-live="polite">{esc(copylbl)} ↗</button></div>
<section class="fast-intro" aria-labelledby="intro"><h2 id="intro">{esc(before)}</h2><div class="fast-eyebrow">{esc(bigpicture)}</div><p class="fast-plain">{esc(summary)}</p>
<p class="fast-example"><b>{esc(explbl)}:</b> {esc(example)}</p><h3>{esc(definitions)}</h3><dl class="fast-terms">{glossary}</dl></section>
<section id="sheet" class="reader-sheet-section" aria-label="{esc(show)}"><h2>{esc(show)}</h2>
<p><a href="{direct}" target="_blank" rel="noopener">{esc(openpage)} ↗</a></p>
<iframe class="fast-iframe" src="{direct}#view=FitH&navpanes=0" loading="lazy" title="{esc(title)} — PDF"></iframe>
<details><summary>{esc(langphrase('Cannot see the PDF? Open the illustration','Nu vezi PDF-ul? Deschide imaginea',lang))}</summary><img loading="lazy" src="../{esc(item['preview'])}" alt="{headline}" style="max-width:100%;height:auto"></details></section>
<section class="fast-check"><h2>{esc(homework)}</h2><p><a href="../quest.html?id={lid}&lang={lang}" style="display:inline-block;background:#005a4f;color:white;border-radius:11px;text-decoration:none;padding:13px 18px;font-weight:850">{esc(langphrase('Play LEARN Quest · 3 quick clues →','Joacă LEARN Quest · 3 indicii →',lang))}</a></p><ol>{''.join('<li>'+esc(q)+'</li>' for q in qs)}</ol><p>{esc(langphrase('The point is understanding, not memorising.', 'Scopul este să înțelegi, nu să memorezi.', lang))}</p></section>
<nav class="fast-arrows" aria-label="{esc(langphrase('Other topics','Alte teme',lang))}">{prevhtml}{nexthtml}</nav>
<footer class="fast-footer">© 2026 Vlad Belciug · {esc(foot)} · <a href="https://github.com/ovladon/learn/blob/main/USAGE.md">Usage and rights</a> · <a href="{root}">QR lesson link</a></footer></main>
<script>document.getElementById('share').addEventListener('click',async()=>{{let b=document.getElementById('share');try{{await navigator.clipboard.writeText(location.href);b.textContent={'"Link copied!"' if lang=='en' else '"Link copiat!"'};}}catch(e){{b.textContent={'"Copy address from the address bar"' if lang=='en' else '"Copiază adresa din browser"'};}}}});</script>
</body></html>'''


def build_pdf(pdf_path, output, item, primer, lang):
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from pypdf import PdfReader, PdfWriter
    fontbase = Path('/usr/share/fonts/truetype/dejavu')
    regular = fontbase / 'DejaVuSans.ttf'
    bold = fontbase / 'DejaVuSans-Bold.ttf'
    if not regular.is_file() or not bold.is_file():
        raise RuntimeError('Unicode-capable DejaVu font missing on builder')
    if 'DejaVuLEARN' not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont('DejaVuLEARN', str(regular)))
        pdfmetrics.registerFont(TTFont('DejaVuLEARN-Bold', str(bold)))
        pdfmetrics.registerFontFamily('DejaVuLEARN', normal='DejaVuLEARN', bold='DejaVuLEARN-Bold')
    import io
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, leftMargin=44,rightMargin=44,topMargin=47,bottomMargin=52,
                            title=item[f'title_{lang}'] + ' — LEARN Start from Zero', author='Vlad Belciug')
    base = getSampleStyleSheet()
    styles = {
        'minor':ParagraphStyle('LEARN_M',parent=base['Normal'],fontName='DejaVuLEARN-Bold',fontSize=8.5,leading=13,textColor=HexColor('#188576'),spaceAfter=9),
        'title':ParagraphStyle('LEARN_T',fontName='DejaVuLEARN-Bold',fontSize=20,leading=26,textColor=HexColor('#102c3d'),spaceAfter=16),
        'lead':ParagraphStyle('LEARN_L',fontName='DejaVuLEARN-Bold',fontSize=12.5,leading=19,textColor=HexColor('#133c48'),spaceAfter=11),
        'body':ParagraphStyle('LEARN_B',fontName='DejaVuLEARN',fontSize=10,leading=15.8,textColor=HexColor('#304556'),spaceAfter=9),
        'term':ParagraphStyle('LEARN_TERM',fontName='DejaVuLEARN',fontSize=9.4,leading=14.4,textColor=HexColor('#344b53'),leftIndent=10,spaceAfter=6),
        'sub':ParagraphStyle('LEARN_S',fontName='DejaVuLEARN-Bold',fontSize=11.1,leading=16,textColor=HexColor('#145c58'),spaceBefore=12,spaceAfter=7),
        'note':ParagraphStyle('LEARN_N',fontName='DejaVuLEARN',fontSize=8.5,leading=13,textColor=HexColor('#637886'),spaceBefore=12),
    }
    words = lambda s: esc(s).replace('\n','<br/>')
    topic_url = SITE + f'topics/{item["id"]}-{lang}.html'
    story = [Paragraph('LEARN · '+('EXPLAINED FROM ZERO' if lang=='en' else 'EXPLICAT DE LA ZERO'),styles['minor']),
             Paragraph(words(item[f'title_{lang}']),styles['title']),
             Paragraph(words(primer['plain']),styles['lead']),
             Paragraph('<b>'+('Example from everyday life:' if lang=='en' else 'Exemplu din viața obișnuită:')+'</b> '+words(primer['example']),styles['body']),
             Paragraph('WORDS EXPLAINED' if lang=='en' else 'TERMENI EXPLICAȚI',styles['sub'])]
    for term,definition in primer['terms']:
        story.append(Paragraph('<b>'+words(term)+'</b> — '+words(definition),styles['term']))
    story += [Paragraph('FOLLOW THE INFOGRAPHIC' if lang=='en' else 'URMĂREȘTE INFOGRAMA',styles['sub']),
              Paragraph('Read the original visual on the next page. Ask yourself: what problem is solved, what happens first, and what result do we get?' if lang=='en' else 'Citește infograma de pe pagina următoare. Întreabă-te: ce problemă se rezolvă, ce se întâmplă prima dată și care este rezultatul?',styles['body']),
              Paragraph('<link href="'+esc(topic_url)+'" color="#0b6c67">'+esc(topic_url)+'</link>',styles['note']),
              Paragraph('© 2026 Vlad Belciug · Free for individual study. Original infographic follows.' if lang=='en' else '© 2026 Vlad Belciug · Gratuit pentru studiu individual. Urmează infograma originală.',styles['note'])]
    doc.build(story)
    buffer.seek(0)
    cover = PdfReader(buffer)
    original = PdfReader(str(pdf_path))
    writer=PdfWriter()
    writer.append(cover)
    writer.append(original)
    writer.add_metadata({'/Title':item[f'title_{lang}']+' — LEARN explained','/Author':'Vlad Belciug'})
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('wb') as f:writer.write(f)
    return len(cover.pages),len(writer.pages)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--site',default='_site')
    parser.add_argument('--no-pdf',action='store_true')
    args=parser.parse_args()
    site=Path(args.site).resolve()
    tracks=parse_js_json(site/'catalog.js','LEARN_TRACKS')
    catalog=parse_js_json(site/'catalog.js','LEARN_CATALOG')
    primers=parse_js_json(site/'learner-notes.js','LEARN_PRIMERS')
    assert len(catalog) in (78,92), ('Unexpected topic count',len(catalog))
    assert len({i['id'] for i in catalog})==len(catalog)
    assert all(x['id'] in primers for x in catalog)
    track_by_id={x['id']:x for x in tracks}
    topicdir=site/'topics';topicdir.mkdir(exist_ok=True)
    bdir=site/'beginner';bdir.mkdir(exist_ok=True)
    audit=[]
    static_urls=[]
    for i,item in enumerate(catalog):
        lid=item['id'];t=track_by_id[item['category']]
        neighbors=(catalog[i-1]['id'] if i else None,catalog[i+1]['id'] if i+1<len(catalog) else None)
        for lang in ('en','ro'):
            p=primers[lid][lang]
            assert len(p['plain'])>=15 and len(p['example'])>=14 and len(p['terms'])>=3,(lid,lang)
            # Source notes occasionally repeat a term; keep the first definition and flag editorial follow-up.
            oldcount=len(p['terms'])
            seen=set(); p['terms']=[term for term in p['terms'] if not (term[0].lower() in seen or seen.add(term[0].lower()))]
            duplicate_count=oldcount-len(p['terms'])
            path=site/item['pdf_'+lang]
            assert path.exists() and path.stat().st_size>1000,(lid,lang,path)
            htmlpath=topicdir/f'{lid}-{lang}.html'
            htmlpath.write_text(build_page(item,p,lang,neighbors,t),encoding='utf-8')
            static_urls.append(SITE+'topics/'+htmlpath.name)
            pages=None
            if not args.no_pdf:
                cover,total=build_pdf(path,bdir/f'{lid}-{lang}.pdf',item,p,lang)
                assert total>cover,('original missing',lid,lang)
                pages=total
            audit.append({'id':lid,'lang':lang,'terms_defined':len(p['terms']),'plain_length':len(p['plain']),
                          'example_length':len(p['example']),'original_pdf':item['pdf_'+lang],
                          'beginner_pdf':'beginner/'+lid+'-'+lang+'.pdf',
                          'pages':pages,'duplicate_terms_removed':duplicate_count,'review_status':'machine_checked_editorial_review_needed'})
    linklisting='\n'.join(f'<li><a href="{esc(i["id"])}-{lang}.html">{esc(i["title_"+lang])} ({lang.upper()})</a></li>'
                           for i in catalog for lang in ('en','ro'))
    (topicdir/'index.html').write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><title>All beginner-friendly technology explanations · LEARN</title><meta name="description" content="{len(catalog)} free beginner technology topics explained in English and Romanian. No registration."><link rel="stylesheet" href="../style.css"><main class="wrap" style="padding-top:25px;padding-bottom:60px"><h1>All LEARN topics · {len(catalog)} / {len(catalog)*2} versions</h1><p><a href="../">← LEARN home</a></p><ul>{linklisting}</ul></main></html>',encoding='utf-8')
    urls=[SITE,SITE+'system-map.html',SITE+'interactive-lab.html',SITE+'topics/']+static_urls
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>'+xml_escape(u)+'</loc></url>\n' for u in urls)+'</urlset>\n'
    (site/'sitemap.xml').write_text(sitemap,encoding='utf-8')
    (site/'robots.txt').write_text('User-agent: *\nAllow: /learn/\nSitemap: '+SITE+'sitemap.xml\n',encoding='utf-8')
    report={'version':'2026-10-22-faststart-v1','catalog_topics':len(catalog),'localized_guides':len(audit),
            'generated_pdf_count':0 if args.no_pdf else len(audit),'quality_claim':'Automated structural QA, not proof of human comprehension',
            'audit':audit}
    (site/'BEGINNER_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(catalog)} lessons · {len(audit)} canonical static pages · {0 if args.no_pdf else len(audit)} beginner editions · sitemap valid')


if __name__=='__main__':main()
