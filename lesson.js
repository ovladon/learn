(function(){
'use strict';
const all=window.LEARN_CATALOG||[];
const tracks=window.LEARN_TRACKS||[];
const primers=window.LEARN_PRIMERS||{};
const args=new URLSearchParams(location.search);
const id=args.get('id')||'';
const item=all.find(x=>x.id===id);
const el=x=>document.getElementById(x);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
if(!item || !primers[id]){el('reader-error').hidden=false;el('reader-error').textContent='Lesson not found / Lecția nu a fost găsită. Return to the library.';return;}
const pos=all.indexOf(item);
const language=(args.get('lang')==='ro'||args.get('lang')==='en')?args.get('lang'):(navigator.language||'').toLowerCase().startsWith('ro')?'ro':'en';
function pageHref(target,lang){return 'lesson.html?id='+encodeURIComponent(target)+'&lang='+encodeURIComponent(lang);}
function setLang(lang){
 document.documentElement.lang=lang;
 const ro=lang==='ro',p=primers[id][lang],title=item['title_'+lang],pdf=item['pdf_'+lang],track=tracks.find(t=>t.id===item.category);
 if(!p||!pdf){return;}
 document.title=title+' · '+(ro?'Citește online':'Read online')+' · LEARN';
 el('reader-content').hidden=false;
 el('reader-title').textContent=title;
 el('reader-desc').textContent=item['desc_'+lang];
 el('reader-track').textContent=(track&&track['title_'+lang])||'LEARN';
 el('start-eyebrow').textContent=ro?'ÎNCEPE DE LA ZERO':'START FROM ZERO';
 el('start-heading').textContent=ro?'Ce înseamnă, pe înțelesul tuturor?':'What does this mean, in everyday words?';
 el('plain-meaning').textContent=p.plain;
 el('example-label').textContent=ro?'Exemplu din viața obișnuită:':'Everyday example:';
 el('example-text').textContent=p.example;
 el('vocab-heading').textContent=ro?'Termenii explicați înainte să ai nevoie de ei':'Words explained before you need them';
 el('vocabulary').innerHTML=p.terms.map(t=>'<div><dt>'+esc(t[0])+'</dt><dd>'+esc(t[1])+'</dd></div>').join('');
 el('reader-instruction').textContent=ro?'Citește explicațiile de mai sus, apoi urmărește diagrama. Nimic de instalat. Dacă ai mai întâlnit un termen necunoscut, caută sensul în explicația din jur, nu încerca să îl memorezi separat.':'Read the explanations above, then follow the diagram. Nothing to install. If another word is unfamiliar, use the surrounding explanation instead of memorizing it in isolation.';
 el('sheet-heading').textContent=ro?'Infograma originală':'The original infographic';
 el('sheet-note').textContent=ro?'PDF-ul este afișat în pagină. Poți mări textul folosind controalele documentului; descărcarea este opțională.':'The PDF is embedded below. Use the document controls to zoom; downloading is optional.';
 el('fallback-label').textContent=ro?'Nu vezi documentul? Arată previzualizarea ca imagine':'Cannot see the PDF? View an image preview';
 el('fallback-text').textContent=ro?'Pentru claritate maximă, deschide PDF-ul într-o filă de browser.':'For full resolution, open the PDF in a browser tab.';
 el('reader-preview').src=item.preview;
 el('reader-preview').alt=(ro?'Previzualizare a infogramei: ':'Infographic preview: ')+title;
 el('reader-pdf').title=(ro?'Infogramă PDF: ':'PDF infographic: ')+title;
 el('reader-pdf').src=pdf+'#view=FitH&navpanes=0';
 el('library-back').href='./#'+encodeURIComponent(id);el('library-back').textContent=ro?'← Toate lecțiile':'← All lessons';
 el('direct-pdf').href=pdf;el('direct-pdf').textContent=ro?'Deschide PDF ↗':'Open PDF ↗';
 el('download-pdf').href=pdf;el('download-pdf').textContent=ro?'Descarcă PDF ↓':'Download PDF ↓';
 el('permalink').href=pageHref(id,lang);el('permalink').textContent=ro?'Link spre lecție ↗':'Lesson link ↗';
 for(const k of ['en','ro']){el('choose-'+k).classList.toggle('active',k===lang);el('choose-'+k).setAttribute('aria-pressed',String(k===lang));}
 for(const [node,index,t,label] of [['previous-lesson',pos-1,'prev',''],['next-lesson',pos+1,'next','']]){
 const a=el(node);const item2=all[index];a.hidden=!item2;if(item2){a.href=pageHref(item2.id,lang);a.textContent=t==='prev'?(ro?'← Lecția anterioară':'← Previous lesson'):(ro?'Lecția următoare →':'Next lesson →');}}
}
el('choose-en').addEventListener('click',()=>{history.replaceState(null,'',pageHref(id,'en'));setLang('en')});
el('choose-ro').addEventListener('click',()=>{history.replaceState(null,'',pageHref(id,'ro'));setLang('ro')});
setLang(language);
})();
