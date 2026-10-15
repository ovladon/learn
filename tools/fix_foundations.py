from pathlib import Path
from PIL import Image
import fitz,re
ROOT=Path('/mnt/data/_learn_work/site'); SRC=Path('/mnt/data/LEARN_OWNER_LIBRARY_BACKUP_2026-10-15/website/materials/foundations')
SITE='https://ovladon.github.io/learn/'
GLOSS_FONT=fitz.Font(fontfile='/usr/share/fonts/truetype/lato/Lato-Regular.ttf')
# First appearances are addressed in a READ FIRST bar placed BEFORE the original poster content.
ACROS={
0: {
'en':[('CPU','Central Processing Unit'),('RAM','Random Access Memory'),('SSD','Solid-State Drive'),('GUI','Graphical User Interface')],
'ro':[('CPU','Central Processing Unit - procesor central'),('RAM','Random Access Memory - memorie temporară'),('SSD','Solid-State Drive - stocare persistentă'),('GUI','Graphical User Interface - interfață grafică')]},
1:{'en':[('CPU','Central Processing Unit'),('OS','Operating System')], 'ro':[('CPU','Central Processing Unit - procesor central'),('OS','Operating System - sistem de operare'),('PC','Personal Computer - calculator personal')]},
2:{'en':[('URL','Uniform Resource Locator'),('DNS','Domain Name System'),('HTML','HyperText Markup Language'),('CSS','Cascading Style Sheets'),('Wi-Fi','wireless-network technology; not an acronym')],
'ro':[('URL','Uniform Resource Locator - adresă web'),('DNS','Domain Name System - sistemul numelor de domenii'),('HTML','HyperText Markup Language - limbaj de marcare'),('CSS','Cascading Style Sheets - foi de stil'),('Wi-Fi','tehnologie de rețea fără fir; nu este acronim')]},
3:{'en':[('GUI','Graphical User Interface'),('OS','Operating System'),('ADB','Android Debug Bridge'),('PC','Personal Computer')],
'ro':[('GUI','Graphical User Interface - interfață grafică'),('OS','Operating System - sistem de operare'),('ADB','Android Debug Bridge - instrument Android'),('PC','Personal Computer - calculator personal')]},
4:{'en':[('GUI','Graphical User Interface'),('HTML','HyperText Markup Language'),('HTTP','Hypertext Transfer Protocol')],
'ro':[('HTML','HyperText Markup Language - limbaj de marcare'),('HTTP','Hypertext Transfer Protocol - protocol web')]},
5:{'en':[], 'ro':[]},
6:{'en':[], 'ro':[]},
7:{'en':[('LIFO','Last In, First Out'),('FIFO','First In, First Out')],
'ro':[('LIFO','Last In, First Out - ultimul intrat, primul ieșit'),('FIFO','First In, First Out - primul intrat, primul ieșit')]},
8:{'en':[],'ro':[]},
9:{'en':[('RAM','Random Access Memory'),('SSD','Solid-State Drive')],
'ro':[('RAM','Random Access Memory - memorie temporară'),('SSD','Solid-State Drive - stocare persistentă'),('PC','Personal Computer - calculator personal')]},
10:{'en':[('AI','Artificial Intelligence'),('HTTPS','Hypertext Transfer Protocol Secure'),('MFA','Multi-Factor Authentication'),('QR','Quick Response')],
'ro':[('AI','Artificial Intelligence - inteligență artificială'),('HTTPS','Hypertext Transfer Protocol Secure - protocol web securizat'),('MFA','Multi-Factor Authentication - autentificare multifactor'),('QR','Quick Response - cod de răspuns rapid')]}
}
# Preserve QR within original content. Each result remains one A4 page.
def glossary_fix(idx,lang):
 f=SRC/f'fund-{idx:02d}-{lang}.pdf';raw=fitz.open(f);p=raw[0];out=fitz.open();op=out.new_page(width=p.rect.width,height=p.rect.height)
 W,H=op.rect.width,op.rect.height
 entries=ACROS.get(idx,{}).get(lang,[]); ifneeded=bool(entries)
 if not ifneeded: out.close();raw.close();return None
 # area at very top; original sheet scaled 0.874, deliberately leaving original intact.
 op.draw_rect(fitz.Rect(0,0,W,H),color=None,fill=(.953,.969,.989),overlay=True)
 band=fitz.Rect(0,0,W,97)
 op.draw_rect(band,color=None,fill=(.070,.142,.238),overlay=True)
 op.draw_rect(fitz.Rect(0,0,7,97),color=None,fill=(.13,.70,.70),overlay=True)
 heading=('READ FIRST · UNPACK THE ABBREVIATIONS' if lang=='en' else 'CITEȘTE MAI ÎNTÂI · EXPLICĂM ABREVIERILE')
 op.insert_font(fontname='LatoGloss',fontfile='/usr/share/fonts/truetype/lato/Lato-Regular.ttf')
 op.insert_text((31,19),heading,fontname='LatoGloss',fontsize=11.7,color=(.69,.95,.84),overlay=True)
 # Column ordering reads top-to-bottom in each column. Acronyms always precede sheet text.
 rows=3 if len(entries)>4 else 2
 for i,(k,exp) in enumerate(entries):
  col=i//rows;row=i%rows
  x=31+col*281;y=35+row*18.9
  sz=8.9 if len(exp)<33 else 7.6
  content=f'{k} ({exp})'
  if GLOSS_FONT.text_length(content,fontsize=sz)>258:
   sz=7.1
  if GLOSS_FONT.text_length(content,fontsize=sz)>258:
   sz=6.5
  if GLOSS_FONT.text_length(content,fontsize=sz)>258:
   raise ValueError('Glossary entry too long: '+content)
  op.insert_text((x,y),content,fontname='LatoGloss',fontsize=sz,color=(1,1,1),overlay=True)
 factor=.87; ww=W*factor;hh=H*factor
 dest=fitz.Rect((W-ww)/2,98,(W+ww)/2,98+hh)
 op.show_pdf_page(dest,raw,0,overlay=True)
 # transformed top-right QR rectangle from poster original (unchanged link destination)
 qr=fitz.Rect(487,24,572,113)
 target=fitz.Rect(dest.x0+qr.x0*factor,dest.y0+qr.y0*factor,dest.x0+qr.x1*factor,dest.y0+qr.y1*factor)
 op.insert_link(dict(kind=fitz.LINK_URI,from_=target,uri=SITE+f'#fund-{idx:02d}')) if False else op.insert_link({'kind':fitz.LINK_URI,'from':target,'uri':SITE+f'#fund-{idx:02d}'})
 folder=ROOT/'materials/foundations';folder.mkdir(exist_ok=True,parents=True)
 outfile=folder/f'fund-{idx:02d}-{lang}.pdf'
 out.set_metadata({'title':f'LEARN Foundations {idx:02d} - expanded abbreviations','author':'Vlad Belciug','subject':'Standalone beginner teaching sheet, acronym definitions before original content'})
 out.subset_fonts()
 out.save(outfile,garbage=4,deflate=True)
 out.close();raw.close();return outfile

def run():
 import shutil
 for i in range(13):
  for lang in ('en','ro'):
   if glossary_fix(i,lang) is None:
    # original 05,06,08 and Big O sheets do not have unexplained technical acronyms.
    pass
 for i in range(13):
  path=ROOT/'materials/foundations'/f'fund-{i:02d}-en.pdf'
  if not path.exists():shutil.copy2(SRC/f'fund-{i:02d}-en.pdf',path)
  doc=fitz.open(path)
  pix=doc[0].get_pixmap(matrix=fitz.Matrix(1.24,1.24),alpha=False)
  Image.frombytes('RGB',[pix.width,pix.height],pix.samples).save(ROOT/'previews'/f'fund-{i:02d}.webp','WEBP',quality=84,method=6)
 for lang in ('en','ro'):
  full=fitz.open()
  for i in range(13):
   doc=fitz.open(ROOT/'materials/foundations'/f'fund-{i:02d}-{lang}.pdf');full.insert_pdf(doc,links=False)
  full.subset_fonts()
  full.save(ROOT/'collections'/f'foundations-{lang}.pdf',garbage=4,deflate=True)
 print('Corrected 16? glossary pages per language; assembled Foundations booklets.')

if __name__=='__main__':run()