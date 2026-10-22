#!/usr/bin/env python3
"""Generate LEARN's bilingual Chapter 07 from one checked-in curriculum source.

Builds *into* _site, never into the owner's original PDF collection.
Requires reportlab + pypdf (already installed for Fast Start in Pages CI).
All material remains authored/reviewed; telemetry cannot auto-publish content.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

def read_var(path: Path, name: str):
    source = path.read_text(encoding="utf-8")
    match = re.search(r"window\." + re.escape(name) + r"\s*=\s*([\[{].*?[\]}])\s*;", source, flags=re.S)
    if not match:
        raise RuntimeError(f"Missing {name} in {path}")
    return json.loads(match.group(1))

def save_var(path: Path, name: str, value):
    path.write_text(f"/* Generated Chapter 07 extension; canonical content: curriculum/data-chapter.json */\nwindow.{name} = " +
                    json.dumps(value, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")

def source_svg(index: int, title: str, steps: list[str]):
    def esc(s): return xml_escape(s, {'"': '&quot;'})
    rectangles = "".join(f'<rect x="{40+i*240}" y="173" width="215" height="76" rx="13" fill="{c}"/><text x="{55+i*240}" y="205" font-size="19" font-weight="700" fill="#ffffff">{i+1:02d}</text><text x="{55+i*240}" y="229" font-size="12" fill="#ffffff">{esc(step[:25])}</text>'
                         for i, (c, step) in enumerate(zip(("#007c78","#125a88","#482d92"),steps)))
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400" viewBox="0 0 800 400"><rect width="800" height="400" fill="#edf7f5"/><rect width="800" height="74" fill="#08283e"/><text x="34" y="46" font-family="DejaVu Sans,sans-serif" font-size="25" fill="#ffffff">LEARN · DATA / {index+1:02d}</text><text x="34" y="125" font-family="DejaVu Sans,sans-serif" font-size="23" font-weight="700" fill="#122d42">{esc(title[:53])}</text>{rectangles}<text x="40" y="332" font-size="17" font-family="DejaVu Sans,sans-serif" fill="#29475a">Observe → represent → reason</text></svg>'

def make_sheet(path: Path, lesson: dict, lang: str):
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.colors import HexColor
    from reportlab.lib.utils import simpleSplit
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.graphics.barcode.qr import QrCodeWidget
    from reportlab.graphics.shapes import Drawing
    from reportlab.graphics import renderPDF
    base = Path("/usr/share/fonts/truetype/dejavu")
    for n, f in (("DataRegular","DejaVuSans.ttf"), ("DataBold","DejaVuSans-Bold.ttf")):
        if n not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(n,str(base/f)))
    w,h=A4
    c=Canvas(str(path), pagesize=A4, pageCompression=1)
    title=lesson[lang]["title"]; obj=lesson[lang]
    c.setTitle(title+" | LEARN DATA"); c.setAuthor("Vlad Belciug")
    c.setFillColor(HexColor("#092e43"));c.rect(0,h-104,w,104,fill=1,stroke=0)
    c.setFont("DataBold",10);c.setFillColor(HexColor("#86dec9"))
    c.drawString(38,h-37,"LEARN  /  DATA CHAPTER 07  /  "+lesson["id"].split("-")[1])
    def block(t,x,y,font,size,color,width,leading,max_lines=99):
        lines=simpleSplit(t,font,size,width)
        if len(lines)>max_lines: raise ValueError("Content does not fit: "+lesson["id"]+" "+lang)
        c.setFont(font,size);c.setFillColor(HexColor(color))
        for line in lines:
            c.drawString(x,y,line);y-=leading
        return y
    y=block(title,38,h-68,"DataBold",15.6,"#ffffff",w-76,20,2)-10
    y=block(obj["plain"],38,y,"DataRegular",10.5,"#102d40",w-76,16,5)-18
    c.setFillColor(HexColor("#e9f8f3"));c.roundRect(30,y-78,w-60,86,12,fill=1,stroke=0)
    c.setFont("DataBold",10);c.setFillColor(HexColor("#085e57"))
    c.drawString(42,y-9,"EXAMPLE" if lang=="en" else "EXEMPLU")
    block(obj["example"],42,y-29,"DataRegular",9.25,"#26495a",w-84,14,4)
    y-=116
    c.setFont("DataBold",11);c.setFillColor(HexColor("#1c536b"))
    c.drawString(38,y,"THREE STEPS" if lang=="en" else "TREI PAȘI")
    y-=28
    colors=["#106960","#185886","#524282"]
    for i,step in enumerate(obj["steps"]):
        c.setFillColor(HexColor(colors[i]));c.roundRect(40,y-35,w-80,40,7,fill=1,stroke=0)
        c.setFont("DataBold",10);c.setFillColor(HexColor("#ffffff"))
        c.drawString(51,y-20,f"{i+1}.  "+step)
        y-=53
    y-=8
    c.setFont("DataBold",11);c.setFillColor(HexColor("#1c536b"))
    c.drawString(38,y,"WORDS TO UNDERSTAND" if lang=="en" else "CUVINTE EXPLICATE")
    y-=26
    for term,definition in obj["terms"]:
        c.setFillColor(HexColor("#19455b"));c.setFont("DataBold",9);c.drawString(39,y,term+":")
        y-=15
        y=block(definition,46,y,"DataRegular",8.6,"#344f5d",w-104,12,2)-7
    y-=5
    c.setFillColor(HexColor("#fff2e7"));c.roundRect(30,y-69,w-60,78,10,fill=1,stroke=0)
    c.setFont("DataBold",10);c.setFillColor(HexColor("#804218"))
    c.drawString(40,y-8,"COMMON MISCONCEPTION" if lang=="en" else "CONFUZIE FRECVENTĂ")
    block(obj["myth"],40,y-27,"DataRegular",8.8,"#4a3a37",w-80,13,4)
    if y-80<80: raise ValueError("Sheet overflow "+lesson["id"]+" "+lang)
    link="https://ovladon.github.io/learn/topics/"+lesson["id"]+"-"+lang+".html"
    qr=QrCodeWidget(link)
    q=Drawing(52,52,transform=[52/qr.getBounds()[2],0,0,52/qr.getBounds()[3],0,0]);q.add(qr)
    renderPDF.draw(q,c,w-88,25)
    c.setStrokeColor(HexColor("#d4e3e3"));c.line(35,90,w-35,90)
    c.setFillColor(HexColor("#496476"));c.setFont("DataRegular",8)
    c.drawString(37,69,"LEARN · "+("Scan for explanation + Quest" if lang=="en" else "Scanează pentru explicații + Quest"))
    c.drawString(37,52,"© 2026 Vlad Belciug · Free personal study · English / Română")
    c.showPage();c.save()

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--site",required=True);parser.add_argument("--curriculum",default="curriculum/data-chapter.json")
    a=parser.parse_args();site=Path(a.site);chap=json.loads(Path(a.curriculum).read_text(encoding="utf-8"))
    lessons=chap["lessons"];assert len(lessons)==14
    assert [l["id"] for l in lessons]==[f"data-{i:02d}" for i in range(14)]
    tracks=read_var(site/"catalog.js","LEARN_TRACKS")
    catalog=read_var(site/"catalog.js","LEARN_CATALOG")
    primers=read_var(site/"learner-notes.js","LEARN_PRIMERS")
    bank=read_var(site/"quest-bank.js","LEARN_QUEST_BANK")
    assert len(catalog)==len(bank)==78 and len(tracks)==6,"Chapter 07 expects original unextended site"
    tracks.append({"id":"data","title_en":"Data, types and structures — from zero","title_ro":"Date, tipuri și structuri — de la zero","label_en":"LEARNING TRACK / 07","label_ro":"TRASEU DE ÎNVĂȚARE / 07","number":"07","booklet_en":"collections/data-en.pdf","booklet_ro":"collections/data-ro.pdf"})
    outputdir=site/"materials/data";outputdir.mkdir(parents=True,exist_ok=True)
    previews=site/"previews";previews.mkdir(exist_ok=True)
    for ix,lesson in enumerate(lessons):
        lid=lesson["id"]
        assert len({lesson[x]["title"] for x in ("en","ro")})==2
        assert all(len(lesson[lang]["terms"])==3 and len(lesson[lang]["steps"])==3 for lang in ("en","ro"))
        obj={"id":lid,"category":"data","title_en":lesson["en"]["title"],"title_ro":lesson["ro"]["title"],
             "desc_en":lesson["en"]["plain"],"desc_ro":lesson["ro"]["plain"],
             "pdf_en":f"materials/data/{lid}-en.pdf","pdf_ro":f"materials/data/{lid}-ro.pdf",
             "preview":f"previews/{lid}.svg"}
        obj["keywords"]=" ".join([lid]+[lesson[lang]["title"]+" "+lesson[lang]["plain"]+" "+" ".join(x[0] for x in lesson[lang]["terms"]) for lang in ("en","ro")])
        catalog.append(obj)
        primers[lid]={}
        bank[lid]={}
        (previews/f"{lid}.svg").write_text(source_svg(ix,lesson["en"]["title"],lesson["en"]["steps"]),encoding="utf-8")
        for lang in ("en","ro"):
            ls=lesson[lang];other=lessons[(ix+4)%len(lessons)][lang];other2=lessons[(ix+8)%len(lessons)][lang]
            primers[lid][lang]={"plain":ls["plain"],"example":ls["example"],"terms":ls["terms"]}
            stages=[
              {"kind":"scenario","q":"Which step best explains this example?" if lang=="en" else "Care pas explică cel mai bine exemplul?",
               "context":ls["example"],"answers":[ls["steps"][1],other["steps"][1],other2["steps"][1]],"correct":0,"because":ls["plain"]},
              {"kind":"term","q":("What does this term mean: " if lang=="en" else "Ce înseamnă termenul: ")+ls["terms"][0][0]+"?",
               "context":"Choose the accurate definition." if lang=="en" else "Alege definiția corectă.",
               "answers":[other["terms"][0][1],ls["terms"][0][1],other2["terms"][0][1]],"correct":1,"because":ls["terms"][0][1]},
              {"kind":"trap","q":"Myth or fact?" if lang=="en" else "Mit sau adevăr?",
               "context":ls["myth"].split("?")[0]+"?" if "?" in ls["myth"] else ls["myth"],
               "answers":["Fact · this is accurate","Myth · something is wrong"] if lang=="en" else ["Adevăr · afirmația e corectă","Mit · ceva este greșit"],
               "correct":1,"because":ls["myth"]}
            ]
            assert all(len(set(s["answers"]))==len(s["answers"]) for s in stages)
            bank[lid][lang]={"title":ls["title"],"plain":ls["plain"],"example":ls["example"],"stages":stages}
            make_sheet(outputdir/f"{lid}-{lang}.pdf",lesson,lang)
    from pypdf import PdfWriter, PdfReader
    for lang in ("en","ro"):
        w=PdfWriter()
        for l in lessons:
            path=outputdir/f'{l["id"]}-{lang}.pdf'
            assert len(PdfReader(str(path)).pages)==1
            w.append(str(path))
        path=site/f"collections/data-{lang}.pdf";path.parent.mkdir(parents=True,exist_ok=True)
        with path.open("wb") as f:w.write(f)
    save_var(site/"catalog.js","LEARN_CATALOG",catalog)
    # LEARN_TRACKS must precede LEARN_CATALOG in the same catalog.js.
    tracksrc="window.LEARN_TRACKS = "+json.dumps(tracks,ensure_ascii=False,separators=(",",":"))+";\n"
    (site/"catalog.js").write_text("/* LEARN: 6 existing tracks plus generated Chapter 07 */\n"+tracksrc+(site/"catalog.js").read_text(encoding="utf-8"),encoding="utf-8")
    save_var(site/"learner-notes.js","LEARN_PRIMERS",primers)
    save_var(site/"quest-bank.js","LEARN_QUEST_BANK",bank)
    htmlpath=site/"index.html"
    source=htmlpath.read_text(encoding="utf-8")
    source=source.replace('<strong id="count">78</strong>','<strong id="count">92</strong>')
    source=source.replace('<a href="#lang-01" data-en="Languages"', '<a href="#data-00" data-en="Data &amp; structures" data-ro="Date și structuri">Data &amp; structures</a><a href="#lang-01" data-en="Languages"')
    source=source.replace('<div class="hero-actions">','<div class="hero-actions"><a class="btn primary" href="#data-00"><span data-en="NEW: Data, types &amp; structures" data-ro="NOU: Date, tipuri și structuri">NEW: Data, types &amp; structures</span> ↗</a>',1)
    source=source.replace('No student accounts, registration forms or tracking scripts are used by this website.', 'No student accounts, registration forms or tracking scripts are used. Optional anonymous Quest answers can be shared explicitly.')
    source=source.replace('Site-ul nu folosește conturi de student, formulare sau scripturi de urmărire.', 'Site-ul nu folosește conturi de student, formulare sau scripturi de urmărire. Răspunsurile anonime din Quest se trimit doar cu acord explicit.')
    htmlpath.write_text(source,encoding="utf-8")
    print("DATA CHAPTER READY: 14 topics / 28 A4 PDFs / 2 booklets / 28 Quest games / 14 previews; catalog 92.")

if __name__=="__main__": main()
