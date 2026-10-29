(function(){'use strict';
const $=id=>document.getElementById(id),form=$('generate'),area=$('qr'),status=$('status'),actions=$('actions');
let svgUrl, pngUrl;
function clean(){if(svgUrl)URL.revokeObjectURL(svgUrl);if(pngUrl)URL.revokeObjectURL(pngUrl);svgUrl=pngUrl=null;actions.hidden=true;}
function svgFrom(matrix){const n=matrix.getModuleCount(), size=n+8;let cells='';
for(let row=0;row<n;row++)for(let col=0;col<n;col++)if(matrix.isDark(row,col))cells+='<rect x="'+(col+4)+'" y="'+(row+4)+'" width="1" height="1"/>';
return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 '+size+' '+size+'" shape-rendering="crispEdges" role="img" aria-label="Portfolio QR code"><rect width="'+size+'" height="'+size+'" fill="#fff"/><g fill="#000">'+cells+'</g></svg>';}
form.addEventListener('submit',async e=>{e.preventDefault();clean();status.textContent='';
try{const raw=$('portfolioUrl').value.trim(),u=new URL(raw);
if(u.protocol!=='https:'||!u.hostname||u.username||u.password)throw Error('Use a complete public HTTPS URL. / Introdu o adresă HTTPS publică.');
if(u.href.length>500)throw Error('URL too long. / Adresă prea lungă.');
const code=qrcode(0,'M');code.addData(u.href,'Byte');code.make();
const svg=svgFrom(code);area.innerHTML=svg;
svgUrl=URL.createObjectURL(new Blob([svg],{type:'image/svg+xml;charset=utf-8'}));
$('saveSvg').href=svgUrl;
const cvs=document.createElement('canvas');const n=code.getModuleCount(),scale=12;const ctx=cvs.getContext('2d');
if(!ctx)throw Error('Canvas is not supported.');
cvs.width=(n+8)*scale;cvs.height=(n+8)*scale;ctx.fillStyle='#fff';ctx.fillRect(0,0,cvs.width,cvs.height);ctx.fillStyle='#000';
for(let r=0;r<n;r++)for(let c=0;c<n;c++)if(code.isDark(r,c))ctx.fillRect((c+4)*scale,(r+4)*scale,scale,scale);
await new Promise((resolve,reject)=>cvs.toBlob(blob=>{if(!blob){reject(Error('PNG failed'));return;}pngUrl=URL.createObjectURL(blob);$('savePng').href=pngUrl;resolve();},'image/png'));
$('testLink').href=u.href;actions.hidden=false;status.textContent='QR created locally. Scan it with your phone before sharing. / Codul a fost creat local. Verifică-l prin scanare.';
}catch(err){area.textContent='No QR generated / Codul nu a fost generat.';status.textContent=String(err.message||'Invalid URL');}
});
$('printQr').addEventListener('click',()=>print());
})();