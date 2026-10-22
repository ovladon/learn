(function(){
'use strict';
const catalog = window.LEARN_CATALOG || [];
const tracks = window.LEARN_TRACKS || [];
const primers = window.LEARN_PRIMERS || {};
const enBtn = document.getElementById('choose-en');
const roBtn = document.getElementById('choose-ro');
const search = document.getElementById('search');
const backToTop = document.getElementById('back-to-top');
let language = 'en';
let filter = 'all';
function esc(s){return String(s).replace(/[&<>"']/g,x=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));}
function label(en,ro){return language==='en'?en:ro;}
function cardHtml(d){
  const title=label(d.title_en,d.title_ro), other=label(d.title_ro,d.title_en), desc=label(d.desc_en,d.desc_ro);
  const primer=(primers[d.id]||{})[language];
  const quick=primer?primer.plain:desc;
  const online=`topics/${encodeURIComponent(d.id)}-${language}.html`;
  return `<article class="card ${esc(d.category)}" id="${esc(d.id)}">
    <a class="thumb" href="${online}" aria-label="${esc(label('Read online: ','Citește online: ')+title)}"><img loading="lazy" src="${esc(d.preview)}" alt="${esc(title)} infographic preview"></a>
    <div class="card-body"><div class="card-id">${esc(d.category.toUpperCase())} / ${esc(d.id.split('-').pop())}</div>
    <h4>${esc(title)}</h4><div class="romanian-title" lang="${language==='en'?'ro':'en'}">${esc(other)}</div>
    <p class="short-desc">${esc(desc)}</p><p class="card-quick-answer">${esc(quick)}</p>
    <div class="quest-row"><a class="quest-entry" href="quest.html?id=${esc(d.id)}&lang=${language}">${esc(label('Play 3 clues · 1 minute →','Joacă 3 indicii · 1 minut →'))}</a></div>
    <div class="online-row"><a class="read-online" href="${online}">${esc(label('Understand it now →','Înțelege acum →'))}</a><button class="share-lesson" type="button" data-id="${esc(d.id)}" aria-label="${esc(label('Copy lesson link','Copiază linkul lecției'))}">${esc(label('Share ↗','Distribuie ↗'))}</button></div>
    <div class="dlrow"><a href="beginner/${esc(d.id)}-en.pdf" download>EN · ${esc(label('Explained PDF','PDF explicat'))} ↓</a><a href="beginner/${esc(d.id)}-ro.pdf" download>RO · ${esc(label('Explained PDF','PDF explicat'))} ↓</a></div></div>
  </article>`;
}
function filterHtml(){
  const buttons=[{id:'all',title_en:'All topics',title_ro:'Toate temele'},...tracks];
  document.getElementById('filters').innerHTML=buttons.map(t=>`<button type="button" class="filter ${filter===t.id?'active':''}" data-filter="${esc(t.id)}">${esc(label(t.title_en,t.title_ro))}</button>`).join('');
  document.querySelectorAll('.filter').forEach(b=>b.addEventListener('click',()=>{filter=b.dataset.filter;render();}));
}
function render(){
  filterHtml(); const query=search.value.trim().toLocaleLowerCase(); let count=0;let out='';
  for(const t of tracks){
    if(filter!=='all'&&t.id!==filter)continue;
    const visible=catalog.filter(d=>d.category===t.id && (!query||[d.title_en,d.title_ro,d.desc_en,d.desc_ro,d.keywords,...['en','ro'].flatMap(lang=>{const p=(primers[d.id]||{})[lang];return p?[p.plain,p.example,...p.terms.map(t=>t.join(' '))]:[]})].join(' ').toLocaleLowerCase().includes(query)));
    if(!visible.length)continue; count+=visible.length;
    const books=['en','ro'].filter(lang=>t['booklet_'+lang]).map(lang=>`<a class="booklink" href="${esc(t['booklet_'+lang])}">${esc(language==='en'?'Full booklet':'Broșură completă')} ${lang.toUpperCase()} ↗</a>`).join('');
    out+=`<section class="topic-group"><div class="group-heading"><span class="group-icon ${t.id==='ai'?'violet':t.id==='front'?'front':t.id==='invis'?'invis':''}">${esc(t.number||'•')}</span><div><div class="kicker">${esc(label(t.label_en||'LEARNING TRACK',t.label_ro||'TRASEU DE ÎNVĂȚARE'))}</div><h3>${esc(label(t.title_en,t.title_ro))}</h3></div>${books}</div><div class="cards">${visible.map(cardHtml).join('')}</div></section>`;
  }
  document.getElementById('tracks').innerHTML=out;
  document.getElementById('count').textContent=String(count);
  document.getElementById('nothing').hidden=count>0;
}
function setLang(lang){
  language=lang;document.documentElement.lang=lang;
  enBtn.classList.toggle('active',lang==='en');roBtn.classList.toggle('active',lang==='ro');
  enBtn.setAttribute('aria-pressed',lang==='en');roBtn.setAttribute('aria-pressed',lang==='ro');
  document.querySelectorAll('[data-en][data-ro]').forEach(el=>{el.innerHTML=el.dataset[lang];});
  document.getElementById('map-preview').src='previews/big-picture-'+lang+'.webp';
  document.getElementById('map-poster').href='collections/big-picture-a3-'+lang+'.pdf';
  backToTop.setAttribute('aria-label',lang==='en'?'Back to top':'Înapoi sus');
  backToTop.title=lang==='en'?'Back to top':'Înapoi sus';
  search.placeholder=lang==='en'?'What do you want to understand?':'Ce vrei să înțelegi?';render();
}
function followLink(){
  const id=decodeURIComponent(location.hash.slice(1));
  if(!catalog.some(d=>d.id===id))return;
  search.value='';filter='all';render();
  requestAnimationFrame(()=>document.getElementById(id)?.scrollIntoView({block:'center'}));
}
function updateBackToTop(){
  backToTop.hidden = window.scrollY < 420;
}
backToTop.addEventListener('click',()=>{
  window.scrollTo({top:0,behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});
});
window.addEventListener('scroll',updateBackToTop,{passive:true});
window.addEventListener('resize',updateBackToTop);
enBtn.addEventListener('click',()=>setLang('en'));
roBtn.addEventListener('click',()=>setLang('ro'));
search.addEventListener('input',render);
document.getElementById('tracks').addEventListener('click',async ev=>{
  const btn=ev.target.closest('.share-lesson');
  if(!btn)return;
  const url=new URL('topics/'+encodeURIComponent(btn.dataset.id)+'-'+language+'.html',location.href).href;
  try{await navigator.clipboard.writeText(url);btn.textContent=language==='ro'?'Link copiat ✓':'Copied ✓';}
  catch(e){btn.textContent=language==='ro'?'Copiază linkul din browser':'Copy address from browser';}
});
window.addEventListener('hashchange',followLink);
setLang((navigator.language||'').toLowerCase().startsWith('ro')?'ro':'en');
setTimeout(()=>{followLink();updateBackToTop();},100);
})();