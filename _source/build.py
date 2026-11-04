import shutil,os,sys
sys.path.insert(0,'/home/claude/build')
OUTD='/home/claude/site'
for d in os.listdir(OUTD):
    p=os.path.join(OUTD,d)
    if d in ('fonts','images'): continue
    shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
os.makedirs(OUTD+'/assets',exist_ok=True)
from core import CSS,SITE,URLS
open(OUTD+'/assets/site.css','w').write(CSS)
import pages3
# 404 at root
shutil.move(OUTD+'/404/index.html',OUTD+'/404.html'); os.rmdir(OUTD+'/404'); URLS.remove('/404/')
JS=r'''(function(){
var FORM_ENDPOINT=''; // ใส่ URL ของ Formspree หรือบริการรับฟอร์ม เช่น https://formspree.io/f/xxxx
document.querySelectorAll('[data-menu]').forEach(function(b){b.addEventListener('click',function(){var o=document.body.classList.toggle('menu-open');document.querySelectorAll('[data-menu]').forEach(function(x){x.setAttribute('aria-expanded',o)});});});
document.addEventListener('keydown',function(e){if(e.key==='Escape')document.body.classList.remove('menu-open');});
var f=document.querySelector('[data-filter]');
if(f){var group='all',tag=null;var gb=f.querySelectorAll('[data-group]'),tb=f.querySelectorAll('[data-tag]'),cards=f.querySelectorAll('.card[data-g]'),cnt=f.querySelector('[data-count]');
 var init=f.querySelector('[data-group][aria-pressed=true]');if(init)group=init.dataset.group;
 function apply(){var n=0;cards.forEach(function(c){var ok=tag?(' '+c.dataset.tags+' ').indexOf(' '+tag+' ')>-1:(group==='all'||c.dataset.g===group);c.hidden=!ok;if(ok)n++;});gb.forEach(function(b){b.setAttribute('aria-pressed',!tag&&b.dataset.group===group)});tb.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.tag===tag)});if(cnt)cnt.textContent='แสดง '+n+' รายการ';}
 gb.forEach(function(b){b.addEventListener('click',function(){group=b.dataset.group;tag=null;apply();});});
 tb.forEach(function(b){b.addEventListener('click',function(){tag=(tag===b.dataset.tag)?null:b.dataset.tag;apply();});});}
document.querySelectorAll('[data-form]').forEach(function(form){form.addEventListener('submit',function(e){e.preventDefault();var m=form.querySelector('.fmsg');
 if(!FORM_ENDPOINT){m.textContent='ระบบส่งข้อความออนไลน์ยังไม่เปิดใช้งาน กรุณาโทร 02-116-3138 ต่อ 272';return;}
 var btn=form.querySelector('[type=submit]');btn.disabled=true;m.textContent='กำลังส่งข้อความ...';
 fetch(FORM_ENDPOINT,{method:'POST',body:new FormData(form),headers:{'Accept':'application/json'}}).then(function(r){if(!r.ok)throw 0;form.reset();m.textContent='ส่งข้อความแล้ว ทีมงานจะติดต่อกลับโดยเร็ว';}).catch(function(){m.textContent='ส่งข้อความไม่สำเร็จ กรุณาลองอีกครั้ง หรือโทร 02-116-3138 ต่อ 272';}).finally(function(){btn.disabled=false;});});});
})();'''
open(OUTD+'/assets/site.js','w').write(JS)
import re
logo=open(OUTD+'/images/logo-color.svg').read()
paths=''.join(re.findall(r'<path[^>]*/>',logo))
open(OUTD+'/images/favicon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 -6 290 290">{paths}</svg>')
today='2026-11-04'
open(OUTD+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>\n' for u in URLS)+'</urlset>\n')
open(OUTD+'/robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
import json
open(OUTD+'/vercel.json','w').write(json.dumps({"cleanUrls":True,"trailingSlash":True,"redirects":[{"source":"/about","destination":"/about/our-story/","permanent":True}],"headers":[{"source":"/(fonts|images)/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]},{"source":"/(.*)","headers":[{"key":"X-Content-Type-Options","value":"nosniff"},{"key":"Referrer-Policy","value":"strict-origin-when-cross-origin"}]}]},indent=2,ensure_ascii=False))
print(len(URLS),'pages')
