import test from 'node:test';
import assert from 'node:assert/strict';
import { createGateway, ORIGIN } from './server.mjs';
const secret = 'a'.repeat(48);
const sample={schema:1,topic_id:'data-01',language:'ro',correct:[true,false,true],confusion:'diagram',variant:'original'};
async function withGateway(fake, fn, opts={}) {
  let calls=[];
  let server=createGateway({upstream:'https://neon.example.test/',secret,fetchImpl:async(u, args)=>{
    calls.push({u, args});return fake?.(u,args) ?? Response.json({ok:true}); },...opts});
  await new Promise(ok=>server.listen(0,'127.0.0.1',ok));
  try{await fn(`http://127.0.0.1:${server.address().port}`,calls)}finally{await new Promise(ok=>server.close(ok))}
}
const post=(base,body,headers={})=>fetch(base+'/ingest',{method:'POST',headers:{Origin:ORIGIN,'Content-Type':'application/json',...headers},body:JSON.stringify(body)});
test('accepts only correct opted-in aggregate data; forwards correct origin secret',async()=>{
  await withGateway(null,async(base,calls)=>{
    let res=await post(base,sample);assert.equal(res.status,200);assert.deepEqual(await res.json(),{ok:true});
    assert.equal(calls.length,1); assert.equal(calls[0].u,'https://neon.example.test/ingest');
    assert.equal(calls[0].args.headers['X-Origin-Secret'],secret);
    assert.deepEqual(JSON.parse(calls[0].args.body),sample);
  });
});
test('forbids forged/missing origin and rejects invalid schema before forwarding',async()=>{
  await withGateway(null,async(base,calls)=>{
    assert.equal((await post(base,sample,{Origin:'https://wrong.test'})).status,403);
    assert.equal((await post(base,{...sample, extra:'sensitive'})).status,400);
    assert.equal((await post(base,{...sample, correct:['yes',true,true]})).status,400);
    assert.equal(calls.length,0);
  });
});
test('CORS preflight only for LEARN; health responds without secrets',async()=>{
  await withGateway(null,async(base)=>{
    let r=await fetch(base+'/ingest',{method:'OPTIONS',headers:{Origin:ORIGIN}});
    assert.equal(r.status,204);assert.equal(r.headers.get('access-control-allow-origin'),ORIGIN);
    assert.equal((await fetch(base+'/health')).status,200);
  });
});
test('limits requests and fails closed if upstream unavailable',async()=>{
  await withGateway(null,async(base,calls)=>{
    assert.equal((await post(base,sample)).status,200);
    assert.equal((await post(base,sample)).status,429);
    assert.equal(calls.length,1);
  },{minuteLimit:1});
  await withGateway(()=>new Response('error',{status:500}),async(base)=>{
    assert.equal((await post(base,sample)).status,503);
  });
});
