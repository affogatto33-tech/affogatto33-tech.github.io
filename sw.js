const CACHE="princess-castle-v32";
const ASSETS=["./","index.html","manifest.json","icon-192.png","icon-512.png","apple-touch-icon.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting()));});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener("fetch",e=>{
  if(e.request.method!=="GET")return;
  const req=e.request;
  const isDoc = req.mode==="navigate" || req.destination==="document";
  if(isDoc){
    // 항상 최신 HTML을 네트워크에서 먼저 가져옴(업데이트 즉시 반영), 오프라인이면 캐시
    e.respondWith(
      fetch(req).then(res=>{try{const cp=res.clone();caches.open(CACHE).then(c=>c.put(req,cp));}catch(_){ } return res;})
      .catch(()=>caches.match(req).then(r=>r||caches.match("index.html")))
    );
    return;
  }
  // 정적 자산은 캐시 우선(빠름)
  e.respondWith(caches.match(req).then(r=>r||fetch(req).then(res=>{
    try{const cp=res.clone();caches.open(CACHE).then(c=>c.put(req,cp));}catch(_){ }
    return res;
  }).catch(()=>caches.match("index.html"))));
});