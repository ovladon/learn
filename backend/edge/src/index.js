// LEARN Quest: privacy-first, rate-limited ingress. No database secrets in browser code.
const SITE_ORIGIN='https://ovladon.github.io';
function cors(request){return {'Access-Control-Allow-Origin':SITE_ORIGIN,'Access-Control-Allow-Methods':'POST, OPTIONS','Access-Control-Allow-Headers':'Content-Type','Access-Control-Max-Age':'3600','Vary':'Origin','Cache-Control':'no-store','X-Content-Type-Options':'nosniff'};}
function reply(obj,status=200,req){return new Response(JSON.stringify(obj),{status,headers:{...cors(req),'Content-Type':'application/json; charset=utf-8'}});}
function valid(x){return x&&typeof x==='object'&&!Array.isArray(x)&&Object.keys(x).sort().join(',')==='confusion,correct,language,schema,topic_id,variant'&&x.schema===1&&typeof x.topic_id==='string'&&/^(fund|ai|dc|front|invis|lang)-\d{2}$/.test(x.topic_id)&&['en','ro'].includes(x.language)&&x.variant==='original'&&Array.isArray(x.correct)&&x.correct.length===3&&x.correct.every(v=>typeof v==='boolean')&&['term','example','diagram','too_fast','other','none','not_selected'].includes(x.confusion);}
async function smallBody(req){const r=req.body?.getReader();if(!r)return null;let pieces=[],count=0;try{while(true){let {done,value}=await r.read();if(done)break;count+=value.length;if(count>512){await r.cancel();return null;}pieces.push(value);}const bytes=new Uint8Array(count);let n=0;for(let p of pieces){bytes.set(p,n);n+=p.length;}return JSON.parse(new TextDecoder().decode(bytes));}catch{return null;}}
export default {async fetch(req,env){
 const url=new URL(req.url),origin=req.headers.get('origin');
 if(url.pathname==='/health'&&req.method==='GET')return reply({ok:true,service:'learn-quest-edge'},200,req);
 if(url.pathname!=='/ingest')return reply({ok:false},404,req);
 if(origin!==SITE_ORIGIN)return new Response('Forbidden',{status:403});
 if(req.method==='OPTIONS')return new Response(null,{status:204,headers:cors(req)});
 if(req.method!=='POST')return reply({ok:false},405,req);
 if(!env.QUEST_LIMIT||!env.NEON_FUNCTION_URL||!env.ORIGIN_SECRET)return reply({ok:false,error:'service_unavailable'},503,req);
 if(!String(req.headers.get('content-type')||'').startsWith('application/json'))return reply({ok:false},415,req);
 if(Number(req.headers.get('content-length')||0)>512)return reply({ok:false},413,req);
 const limit=await env.QUEST_LIMIT.limit({key:'quest-ingest'});
 if(!limit.success)return reply({ok:false,error:'rate_limited'},429,req);
 const body=await smallBody(req);
 if(!valid(body))return reply({ok:false,error:'invalid'},400,req);
 try{
   const target=new URL('/ingest',env.NEON_FUNCTION_URL);
   const upstream=await fetch(target.toString(),{method:'POST',headers:{'Content-Type':'application/json','X-Secret':env.ORIGIN_SECRET},body:JSON.stringify(body),redirect:'manual',signal:AbortSignal.timeout(6500)});
   if(upstream.status!==200)return reply({ok:false,error:'unavailable'},503,req);
   const x=await upstream.json();
   return reply({ok:x.ok===true},x.ok===true?200:503,req);
 }catch{return reply({ok:false,error:'unavailable'},503,req);}
}};