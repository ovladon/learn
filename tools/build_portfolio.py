#!/usr/bin/env python3
"""Build beginner portfolio workshop into the already-public LEARN site.

Uses authored, accessible Markdown source and a self-contained starter.
No secrets, backend, account creation, telemetry or external QR requests.
"""
from __future__ import annotations
import argparse
import html
import re
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from markdown import Markdown

SITE="https://ovladon.github.io/learn/"
SRC=Path("career")
STARTER=Path("portfolio-starter/index.html")
STYLE="""*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f2f6f9;color:#163149;font:16px/1.8 system-ui,-apple-system,Segoe UI,sans-serif}a{color:#056c65}a:hover{text-decoration-thickness:2px}a:focus-visible,button:focus-visible{outline:3px solid #f5a52f;outline-offset:3px}
.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;background:#fff;padding:12px;z-index:20}
.top{background:#0b2135;color:#fff}.top .bar{max-width:1250px;margin:auto;padding:14px 24px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px}.top a{color:#d5ffed;font-weight:800;text-decoration:none}.top .bar nav{display:flex;gap:15px;flex-wrap:wrap;font-size:14px}
.hero{background:radial-gradient(circle at 88% 15%,#1a6470,#0b2135 66%);color:#fff;padding:45px 22px 65px}.hero .inner{max-width:1140px;margin:auto}.hero h1{max-width:850px;line-height:1.14;font-size:clamp(34px,5.2vw,58px);margin:12px 0 22px;letter-spacing:-.035em}.hero p{max-width:850px;color:#d2e9ed;font-size:18px}.caps{font-size:13px;font-weight:850;color:#a0e6d2;letter-spacing:.14em;text-transform:uppercase}
.actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}.actions a,.actions button{padding:11px 18px;border-radius:11px;background:#adf1d9;color:#082d33;text-decoration:none;font-weight:800;border:0;cursor:pointer}.actions .secondary{background:transparent;color:white;border:1px solid #8bb3ba}
.layout{display:grid;grid-template-columns:minmax(0,270px) minmax(0,1fr);gap:28px;max-width:1250px;margin:33px auto 90px;padding:0 25px;align-items:start}
.sidebar{position:sticky;top:16px;max-height:calc(100vh - 32px);overflow:auto;background:white;border:1px solid #d7e4e8;border-radius:16px;padding:20px;font-size:13px}
.sidebar h2{font-size:16px;line-height:1.3;margin:0 0 15px}.sidebar ul{padding-left:16px;margin:0}.sidebar li{margin-bottom:8px;line-height:1.45}.sidebar a{text-decoration:none}.sidebar a:hover{text-decoration:underline}
.guide{min-width:0;background:white;border:1px solid #d7e4e8;border-radius:18px;padding:clamp(21px,3.5vw,54px);box-shadow:0 15px 48px #1034480b}
.guide h2{font-size:clamp(23px,3vw,32px);line-height:1.25;margin:48px 0 20px;padding-top:22px;border-top:2px solid #d6e9e7;color:#0a4f56;scroll-margin-top:20px}
.guide h2:first-of-type{margin-top:16px}.guide h3{font-size:21px}.guide p{max-width:83ch}.guide ol,.guide ul{padding-left:25px}.guide li{margin-bottom:10px}.guide blockquote{margin:22px 0;padding:14px 20px;background:#ecf9f2;border-left:5px solid #158a6b;border-radius:0 12px 12px 0}.guide blockquote p{margin:0}.guide code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;background:#eff5f7;padding:2px 5px;border-radius:5px;font-size:.91em;overflow-wrap:anywhere}.guide pre{overflow-x:auto;background:#10293b;color:#e2f9f5;padding:22px;border-radius:14px;font-size:13px;line-height:1.55;white-space:pre}.guide pre code{background:transparent;padding:0;color:inherit;overflow-wrap:normal}.guide table{border-collapse:collapse;display:block;overflow-x:auto;width:100%;font-size:14px;margin:22px 0}.guide th,.guide td{border:1px solid #d1e1e3;padding:10px 12px;text-align:left;min-width:130px}.guide th{background:#e4f5f0;color:#123e49}.guide hr{border:0;border-top:1px solid #d7e4e8}
.mark-done{border:1px solid #a5cbc0;border-radius:9px;color:#0b5754;background:#eaf9f2;padding:7px 11px;cursor:pointer;margin:-8px 0 8px;font-size:13px;font-weight:800}.mark-done[aria-pressed=true]{background:#0c6e61;color:white}.completion{background:#e8f6f1;padding:10px 14px;border-radius:10px;font-size:14px}
@media(max-width:930px){.layout{grid-template-columns:1fr}.sidebar{position:static;max-height:320px}.guide{padding:22px}}@media print{.top,.sidebar,.actions,.mark-done,.completion{display:none!important}body{background:white}.hero{background:white;color:#0c293f;padding:0}.hero p,.caps{color:#214050}.layout{display:block;margin:0;padding:0}.guide{box-shadow:none;border:0;padding:0}.guide h2{break-after:avoid}.guide li{break-inside:avoid}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""
def make_page(text, lang):
    parsed=Markdown(extensions=["fenced_code","tables","toc","sane_lists"],extension_configs={"toc":{"permalink":False}})
    content=parsed.convert(text)
    toc=parsed.toc
    title="Portofoliul tău, de la zero" if lang=="ro" else "Your portfolio, from absolute zero"
    desc=("Tutorial pas cu pas, în limba română, pentru construirea gratuită a unui portofoliu GitHub Pages cu QR și proiecte verificabile." if lang=="ro" else
          "A complete zero-experience guide to a free GitHub Pages student portfolio, QR code and verifiable coursework projects.")
    count=len(re.findall(r'<h2\b',content))
    assert count>=24,(lang,count)
    # Each numbered section has a browser-only local progress button.
    def addbutton(m):
        header,number=m.group(0),m.group(1)
        if not re.match(r"\d\d",number):return header
        label=("Marchează pasul ca terminat" if lang=="ro" else "Mark this step complete")
        return header+f'<button class="mark-done" data-step="{html.escape(number)}" type="button" aria-pressed="false">{label}</button>'
    content=re.sub(r'<h2 id="[^"]+">\s*(\d\d).*?</h2>',addbutton,content)
    printtext="Tipărește / Salvează ca PDF" if lang=="ro" else "Print / Save as PDF"
    other="en" if lang=="ro" else "ro"
    linklabel="English" if lang=="ro" else "Română"
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{html.escape(desc,quote=True)}"><title>{html.escape(title)} — LEARN</title>
<link rel="canonical" href="{SITE}portfolio-guide-{lang}.html"><link rel="alternate" hreflang="{other}" href="{SITE}portfolio-guide-{other}.html"><link rel="icon" href="favicon.svg" type="image/svg+xml">
<style>{STYLE}</style></head>
<body><a class="skip" href="#tutorial">Skip to tutorial / Sari la tutorial</a>
<header class="top"><div class="bar"><a href="./">L· LEARN</a><nav><a href="./">LEARN Library</a><a href="portfolio-guide-{other}.html" lang="{other}">{linklabel}</a><a href="portfolio-qr.html">QR Maker</a></nav></div></header>
<section class="hero"><div class="inner"><div class="caps">LEARN / CAREER TOOLBOX / FREE WORKSHOP</div><h1>{html.escape(title)}</h1><p>{html.escape(desc)}</p>
<div class="actions"><a href="downloads/student-portfolio-starter.zip">{"Descarcă șablonul ZIP ↓" if lang=="ro" else "Download starter ZIP ↓"}</a><a href="portfolio-qr.html">{"Generator QR gratuit ↗" if lang=="ro" else "Free QR maker ↗"}</a><button type="button" class="secondary" onclick="window.print()">{printtext}</button></div></div></section>
<div class="layout"><aside class="sidebar" aria-label="Contents / Cuprins"><h2>{"Cuprins — mergi la orice pas" if lang=="ro" else "Contents — jump to any step"}</h2>{toc}<p class="completion" role="status"><span id="done">0</span> / 23 {"pași marcați" if lang=="ro" else "steps completed"}<br>{"Salvat doar pe acest dispozitiv." if lang=="ro" else "Saved only on this device."}</p></aside>
<main id="tutorial" class="guide">{content}</main></div><script>
(function(){{const lang={json_str(lang)};const all=document.querySelectorAll('.mark-done'),key='learn-portfolio-progress-'+lang;let saved={{}};
try{{saved=JSON.parse(localStorage.getItem(key)||'{{}}')}}catch(e){{}}
const refresh=()=>{{document.getElementById('done').textContent=String(Object.values(saved).filter(Boolean).length);all.forEach(b=>{{const yes=!!saved[b.dataset.step];b.setAttribute('aria-pressed',yes?'true':'false');b.textContent=yes?({json_str("✓ Finalizat" if lang=="ro" else "✓ Completed")}):({json_str("Marchează pasul ca terminat" if lang=="ro" else "Mark this step complete")})}})}};all.forEach(b=>b.addEventListener('click',()=>{{saved[b.dataset.step]=!saved[b.dataset.step];try{{localStorage.setItem(key,JSON.stringify(saved))}}catch(e){{}}refresh()}}));refresh();
}})();</script></body></html>'''

def json_str(value: str)->str:
    import json
    return json.dumps(value,ensure_ascii=False)

def main():
    p=argparse.ArgumentParser();p.add_argument("--site",required=True)
    args=p.parse_args();site=Path(args.site)
    for lang in ("ro","en"):
        source=(SRC/f"portfolio-guide-{lang}.md").read_text(encoding="utf-8")
        assert len(source)>18000
        page=make_page(source,lang)
        (site/f"portfolio-guide-{lang}.html").write_text(page,encoding="utf-8")
    target=site/"downloads/student-portfolio-starter.zip";target.parent.mkdir(exist_ok=True,parents=True)
    start=STARTER.read_bytes()
    assert b"<title>[YOUR NAME]" in start and b"EXAMPLE" in start
    readme="""LEARN — Student Portfolio Starter (free, no subscription)
 1. Extract the ZIP.
 2. Create a PUBLIC GitHub repository called YOUR-USERNAME.github.io.
 3. In the GitHub web interface select Add file -> Upload files.
 4. Upload the extracted index.html (not this ZIP).
 5. Settings -> Pages -> Deploy from a branch -> main -> /(root) -> Save.
 6. Open https://YOUR-USERNAME.github.io/ and test it in a private window.
 7. Edit index.html on GitHub to replace every [PLACEHOLDER] and sample project.
 8. Create one repository per substantial homework; add code and README.
 9. Link each real project from this portfolio and test every link.
 10. Visit LEARN's QR Maker; paste your own public HTTPS URL and download SVG.
 No backend, secrets, student tracking, paid QR service or domain is needed.
 Full EN tutorial: https://ovladon.github.io/learn/portfolio-guide-en.html
 Tutorial RO: https://ovladon.github.io/learn/portfolio-guide-ro.html
 IMPORTANT: Share only material you are allowed to publish. No passwords or private data.
"""
    with ZipFile(target,"w",compression=ZIP_DEFLATED,compresslevel=9) as z:
        z.writestr("index.html",start)
        z.writestr("READ_ME_FIRST.txt",readme)
    assert target.stat().st_size>2000
    print("CAREER READY: bilingual long-form guides + zero-install one-file website starter ZIP.")

if __name__=="__main__":main()
