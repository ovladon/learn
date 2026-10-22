// LEARN anonymous statistics ingestion — private origin only.
// Do not connect GitHub Pages directly to the native Function URL.
import { timingSafeEqual } from 'node:crypto';
import postgres from './vendor/src/index.js';

const allowedOrigin = 'https://ovladon.github.io';
const secret = process.env.ORIGIN_SECRET;
if (!secret || Buffer.byteLength(secret, 'utf8') < 32) throw new Error('ORIGIN_SECRET missing/short');
if (!process.env.DATABASE_URL) throw new Error('DATABASE_URL unavailable');
const database = postgres(process.env.DATABASE_URL, {
  max: 2, idle_timeout: 10, max_lifetime: 300, connect_timeout: 5,
  prepare: false, no_subscribe: true, ssl: 'require',
});

function authorized(request) {
  const supplied = request.headers.get('x-origin-secret');
  if (!supplied) return false;
  const a = Buffer.from(supplied), b = Buffer.from(secret);
  return a.length === b.length && timingSafeEqual(a, b);
}
function json(object, status = 200) {
  return new Response(JSON.stringify(object), {
    status, headers: { 'content-type': 'application/json; charset=utf-8',
      'cache-control': 'no-store', 'x-content-type-options': 'nosniff' },
  });
}
function validPayload(obj) {
  if (!obj || typeof obj !== 'object' || Array.isArray(obj)) return false;
  const fields = Object.keys(obj).sort().join(',');
  if (fields !== 'confusion,correct,language,schema,topic_id,variant') return false;
  if (obj.schema !== 1 || typeof obj.topic_id !== 'string' ||
      !/^(fund|ai|dc|front|invis|lang)-\d{2}$/.test(obj.topic_id)) return false;
  if (!['ro','en'].includes(obj.language) || obj.variant !== 'original') return false;
  if (!Array.isArray(obj.correct) || obj.correct.length !== 3 ||
      !obj.correct.every(x => typeof x === 'boolean')) return false;
  if (!['term','example','diagram','too_fast','other','none','not_selected'].includes(obj.confusion)) return false;
  return true;
}
async function requestJSON(request) {
  const type = request.headers.get('content-type') || '';
  const size = Number(request.headers.get('content-length') || 0);
  if (!type.toLowerCase().startsWith('application/json') || size > 512) return null;
  const reader = request.body?.getReader(); if (!reader) return null;
  let parts=[], total=0;
  try {
    while (true) {
      const { done, value } = await reader.read(); if (done) break;
      total += value.byteLength; if (total > 512) { await reader.cancel(); return null; }
      parts.push(value);
    }
    return JSON.parse(new TextDecoder().decode(Buffer.concat(parts)));
  } catch { return null; }
}
export default {
  async fetch(request) {
    const url = new URL(request.url);
    if (request.method === 'GET' && url.pathname === '/health') {
      return json({ ok: true, name: 'learn-feedback', intake: 'private-proxy-only', schema: 1 });
    }
    if (request.method === 'OPTIONS') return new Response('Not allowed', { status: 403 });
    // An origin header and CORS do not authenticate a browser; require a server-only secret.
    if (!authorized(request)) return json({ ok: false }, 401);
    if (request.method === 'GET' && url.pathname === '/diagnostics') {
      try {
        const rows = await database`
          SELECT topic_id, language, question_slot, attempts, correct, failure_rate,
                 priority, term_flags, example_flags, diagram_flags, pacing_flags
          FROM learn_quest_diagnostics
          WHERE attempts >= 30 ORDER BY (attempts-correct) DESC LIMIT 100`;
        return json({ ok:true, data:rows });
      } catch (e) { console.error('diagnostics failure', e?.message); return json({ok:false},503); }
    }
    if (request.method !== 'POST' || url.pathname !== '/ingest') return json({ ok:false },404);
    // No raw answers, free text, names, IP or identifiers are accepted.
    const payload=await requestJSON(request);
    if (!validPayload(payload)) return json({ok:false,error:'invalid_schema'},400);
    try {
      const result = await database`
        SELECT learn_record_quest(${payload.topic_id}, ${payload.language},
        ${payload.correct[0]}, ${payload.correct[1]}, ${payload.correct[2]},
        ${payload.confusion}, ${payload.variant}) AS status`;
      if (result[0]?.status !== 'accepted') return json({ok:false,error:'unavailable'},429);
      return json({ok:true});
    } catch (e) { console.error('ingest failure',e?.message); return json({ok:false},503); }
  },
};