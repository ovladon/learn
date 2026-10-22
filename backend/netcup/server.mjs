import http from 'node:http';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';

export const ORIGIN = 'https://ovladon.github.io';
const CONFUSIONS = new Set(['term','example','diagram','too_fast','other','none','not_selected']);
const LANGS = new Set(['en','ro']);
function valid(x) {
  return x && typeof x === 'object' && !Array.isArray(x) &&
    Object.keys(x).sort().join(',') === 'confusion,correct,language,schema,topic_id,variant' &&
    x.schema === 1 && typeof x.topic_id === 'string' &&
    /^(fund|ai|dc|front|invis|lang|data)-\d{2}$/.test(x.topic_id) &&
    LANGS.has(x.language) && x.variant === 'original' &&
    Array.isArray(x.correct) && x.correct.length === 3 &&
    x.correct.every(v => typeof v === 'boolean') &&
    CONFUSIONS.has(x.confusion);
}
function send(res, status, body, cors = false) {
  res.writeHead(status, {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'no-store',
    'X-Content-Type-Options': 'nosniff',
    'Vary': 'Origin',
    ...(cors ? { 'Access-Control-Allow-Origin': ORIGIN,
                 'Access-Control-Allow-Methods': 'POST, OPTIONS',
                 'Access-Control-Allow-Headers': 'Content-Type',
                 'Access-Control-Max-Age': '600' } : {}),
  });
  res.end(JSON.stringify(body));
}
async function bodyFrom(req) {
  let size = 0, data = '';
  for await (const b of req) {
    size += b.length;
    if (size > 512) { const e = new Error('large'); e.http = 413; throw e; }
    data += b.toString('utf8');
  }
  try { return JSON.parse(data); } catch { const e = new Error('badjson'); e.http = 400; throw e; }
}
export function createGateway({ upstream, secret, fetchImpl = fetch, minuteLimit = 60,
                                dailyLimit = 5000, maxConcurrent = 4 } = {}) {
  if (!upstream || !/^https:\/\//.test(upstream)) throw new Error('NEON_FUNCTION_URL must be HTTPS');
  if (!secret || Buffer.byteLength(secret) < 32) throw new Error('ORIGIN_SECRET missing or too short');
  const target = new URL('/ingest', upstream).toString();
  let minute = Math.floor(Date.now() / 60000), minuteCount = 0;
  let day = new Date().toISOString().slice(0,10), dayCount = 0, inFlight = 0;
  const server = http.createServer(async (req, res) => {
    const url = new URL(req.url || '/', 'http://internal');
    if (url.pathname === '/health' && req.method === 'GET') return send(res,200,{ok:true});
    if (url.pathname !== '/ingest') return send(res,404,{ok:false});
    if (req.headers.origin !== ORIGIN) return send(res,403,{ok:false});
    if (req.method === 'OPTIONS') { res.writeHead(204, {
      'Access-Control-Allow-Origin': ORIGIN,
      'Access-Control-Allow-Methods':'POST, OPTIONS',
      'Access-Control-Allow-Headers':'Content-Type',
      'Access-Control-Max-Age':'600', 'Vary':'Origin' }); return res.end(); }
    if (req.method !== 'POST') return send(res,405,{ok:false},true);
    if (!/^application\/json(?:\s*;.*)?$/i.test(req.headers['content-type'] || ''))
      return send(res,415,{ok:false},true);
    if (Number(req.headers['content-length'] || 0) > 512)
      return send(res,413,{ok:false},true);
    const thisMinute = Math.floor(Date.now() / 60000);
    if (thisMinute !== minute) { minute = thisMinute; minuteCount = 0; }
    const thisDay = new Date().toISOString().slice(0,10);
    if (thisDay !== day) { day = thisDay; dayCount = 0; }
    if (minuteCount >= minuteLimit || dayCount >= dailyLimit || inFlight >= maxConcurrent)
      return send(res,429,{ok:false,error:'busy'},true);
    minuteCount += 1;
    let payload;
    try { payload = await bodyFrom(req); }
    catch(e) { return send(res,e.http || 400,{ok:false},true); }
    if (!valid(payload)) return send(res,400,{ok:false},true);
    inFlight += 1;
    try {
      const answer = await fetchImpl(target, {
        method:'POST', redirect:'error',
        headers:{'Content-Type':'application/json','X-Origin-Secret':secret},
        body:JSON.stringify(payload), signal:AbortSignal.timeout(6500)
      });
      if (!answer.ok) return send(res,503,{ok:false},true);
      const obj = await answer.json();
      if (obj?.ok !== true) return send(res,503,{ok:false},true);
      dayCount += 1;
      return send(res,200,{ok:true},true);
    } catch { return send(res,503,{ok:false},true); }
    finally { inFlight -= 1; }
  });
  server.requestTimeout = 10000;
  server.headersTimeout = 8000;
  server.timeout = 10000;
  server.maxHeadersCount = 20;
  return server;
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const server = createGateway({
    upstream:process.env.NEON_FUNCTION_URL,
    secret:process.env.ORIGIN_SECRET,
    minuteLimit: Number(process.env.MINUTE_LIMIT || 60),
    dailyLimit: Number(process.env.DAILY_LIMIT || 5000),
    maxConcurrent: Number(process.env.MAX_CONCURRENT || 4)
  });
  server.listen(Number(process.env.PORT || 8080), '0.0.0.0');
}
