(function(){
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
})();