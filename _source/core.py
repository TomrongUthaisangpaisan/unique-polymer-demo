import os, json, html
OUT='/home/claude/site'
SITE='https://unique-polymer.vercel.app'   # เปลี่ยนเป็นโดเมนจริงเมื่อมี
CSS_FONTS='''@font-face{font-family:'Anuphan';src:url(/fonts/anuphan-var.woff2) format('woff2');font-weight:100 700;font-display:swap}
@font-face{font-family:'IBM Plex Sans Thai Looped';src:url(/fonts/plex-looped-400.woff2) format('woff2');font-weight:400;font-display:swap}
@font-face{font-family:'IBM Plex Sans Thai Looped';src:url(/fonts/plex-looped-500.woff2) format('woff2');font-weight:500;font-display:swap}
@font-face{font-family:'IBM Plex Sans Thai Looped';src:url(/fonts/plex-looped-600.woff2) format('woff2');font-weight:600;font-display:swap}
'''
CSS=CSS_FONTS+'''
:root{--primary:#0A149A;--deep:#070D5C;--accent:#2F45D8;--hl:#3D5AFE;--page:#F6F7FB;--surface:#fff;--soft:#EEF1FF;--tint:#E6EAFB;--text:#231F20;--muted:#5B5E6E;--ondark:#F4F6FF;--ondarkm:#B7C0EE;--border:#DEE2EF}
[hidden]{display:none!important}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}
body{margin:0;font-family:'IBM Plex Sans Thai Looped','Leelawadee UI',Tahoma,sans-serif;color:var(--text);background:var(--page);font-size:16px;line-height:1.75;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:'Anuphan','IBM Plex Sans Thai Looped',sans-serif;margin:0;color:var(--deep);text-wrap:balance}
h1{font-size:48px;line-height:1.2;font-weight:700}h2{font-size:34px;line-height:1.3;font-weight:700}h3{font-size:21px;line-height:1.4;font-weight:600;color:var(--text)}
p{margin:0}a{color:var(--accent)}a:hover{color:var(--primary)}img{max-width:100%}
:focus-visible{outline:3px solid var(--hl);outline-offset:2px;border-radius:4px}
.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;z-index:100;background:#fff;padding:8px 14px}
.wrap{max-width:1200px;margin:0 auto}
.topbar{background:var(--deep);color:#C9D0F5;font-size:13px;padding:8px 24px}.topbar .wrap{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap}.topbar span+span{margin-left:28px}
.hdr{background:#fff;border-bottom:1px solid var(--border);padding:0 24px;position:sticky;top:0;z-index:50}.hdr>.wrap{display:flex;align-items:center;justify-content:space-between;gap:24px;min-height:72px}
.hdr .logo img{height:40px;display:block}
.nav{display:flex;gap:22px;align-items:stretch;height:72px}.ni{position:relative;display:flex;align-items:center}
.ni>a{display:inline-flex;align-items:center;gap:4px;height:100%;font-size:15px;font-weight:600;color:var(--text);text-decoration:none;border-bottom:3px solid transparent;padding-top:3px}
.ni>a svg{transition:transform .2s}.ni:hover>a,.ni:focus-within>a{color:var(--accent);border-bottom-color:var(--hl)}.ni:hover>a svg,.ni:focus-within>a svg{transform:rotate(180deg)}.ni>a.on{color:var(--primary);border-bottom-color:var(--hl)}
.dd{display:none;position:absolute;top:100%;left:-16px;background:#fff;border:1px solid var(--border);border-radius:0 0 16px 16px;box-shadow:0 20px 48px rgba(7,13,92,.16);padding:10px;min-width:300px;z-index:60}
.ni:hover .dd,.ni:focus-within .dd{display:block}
.dd a{display:flex;flex-direction:column;padding:10px 14px;border-radius:10px;text-decoration:none;color:var(--text);font-weight:600;font-size:15px;line-height:1.5}.dd a small{font-weight:400;color:var(--muted);font-size:13px}.dd a:hover{background:var(--tint);color:var(--accent)}
.dd.mega{display:none;left:-200px;width:980px;padding:28px;grid-template-columns:2fr 1fr 1fr;gap:28px}.ni:hover .dd.mega,.ni:focus-within .dd.mega{display:grid}
.dd.mega .gl{font-size:13px;color:var(--muted);margin:0 0 8px 14px}.dd.mega .two{display:grid;grid-template-columns:1fr 1fr;gap:2px}
.feat{background:linear-gradient(135deg,var(--deep),var(--primary));border-radius:16px;padding:24px;color:#fff;display:flex;flex-direction:column;gap:12px}.feat b{font-family:'Anuphan';font-size:20px}.feat p{color:var(--ondarkm);font-size:14px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:0 24px;border-radius:999px;font-weight:600;font-size:16px;text-decoration:none;border:1.5px solid transparent;font-family:inherit;cursor:pointer;line-height:1.3;text-align:center}
.btn-p{background:var(--hl);color:#fff}.btn-p:hover{background:#2B47EF;color:#fff}.btn-n{background:var(--primary);color:#fff}.btn-n:hover{background:var(--deep);color:#fff}.btn-o{border-color:var(--primary);color:var(--primary);background:transparent}.btn-g{border-color:#8C97E0;color:#fff;background:transparent}.btn-g:hover{border-color:#fff;color:#fff}
.burger{display:none;background:none;border:0;padding:8px;cursor:pointer}
.drawer{display:none}
.crumb{display:flex;gap:8px;flex-wrap:wrap;font-size:14px;color:var(--muted);margin:0 0 24px;padding:0;list-style:none}.crumb li+li:before{content:'/';margin-right:8px}.crumb a{color:var(--muted);text-decoration:none}.crumb li:last-child{color:var(--text)}
.hero{background:#fff;border-bottom:1px solid var(--border);padding:40px 24px 64px}.hero .row{display:flex;gap:48px;align-items:center}.hero .txt{flex:1 1 0;display:flex;flex-direction:column;gap:18px;min-width:0}
.kicker{font-size:15px;font-weight:600;color:var(--accent)}.lead{font-size:18px;color:var(--muted);max-width:640px}.ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:6px}
.hero .media{flex:0 0 520px}.hero .media img{width:100%;height:400px;object-fit:cover;border-radius:20px;display:block}
.sec{padding:80px 24px}.sec.white{background:#fff}.sec.tint{background:var(--tint)}.sec.soft{background:var(--soft)}.sec.navy{background:var(--deep)}.sec.navy h2,.sec.navy h3{color:#fff}.sec.navy p{color:var(--ondarkm)}
.shead{display:flex;flex-direction:column;gap:12px;margin-bottom:36px;max-width:760px}.shead p{font-size:18px;color:var(--muted)}.shead.row{max-width:none;flex-direction:row;justify-content:space-between;align-items:flex-end;gap:24px}
.grid{display:grid;gap:24px}.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}.g4{grid-template-columns:repeat(4,minmax(0,1fr))}.g5{grid-template-columns:repeat(5,minmax(0,1fr))}
.card{background:#fff;border:1px solid var(--border);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;text-decoration:none;color:var(--text)}a.card:hover{border-color:var(--accent)}a.card:hover h3{color:var(--accent)}
.card img{width:100%;height:190px;object-fit:cover;display:block}.card .in{padding:24px;display:flex;flex-direction:column;gap:8px;flex-grow:1}.card .lab{font-size:13px;font-weight:600;color:var(--accent)}.card .en{font-size:14px;color:var(--muted)}.card p{font-size:15px;color:var(--muted)}.card .more{font-weight:600;color:var(--accent);margin-top:auto;padding-top:8px;font-size:15px}
.soon{display:inline-flex;align-self:flex-start;font-size:12px;font-weight:600;color:var(--muted);background:var(--page);border:1px solid var(--border);border-radius:999px;padding:2px 10px}
.ico{width:56px;height:56px;border-radius:50%;background:var(--tint);display:flex;align-items:center;justify-content:center;flex:none}
.steps{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:24px;list-style:none;margin:0;padding:0;counter-reset:s}.steps.s4{grid-template-columns:repeat(4,minmax(0,1fr))}
.steps li{counter-increment:s;display:flex;flex-direction:column;gap:12px}.steps li:before{content:counter(s);width:52px;height:52px;border-radius:50%;background:var(--primary);color:#fff;font-family:'Anuphan';font-weight:700;font-size:20px;display:flex;align-items:center;justify-content:center;flex:none}
.steps p{font-size:15px;color:var(--muted);margin-top:4px}.steps small{display:inline-block;margin-top:8px;font-size:13px;font-weight:600;color:var(--accent)}
.faq{max-width:860px}.faq details{border-top:1px solid var(--border);padding:18px 0}.faq details:last-child{border-bottom:1px solid var(--border)}.faq summary{font-weight:600;font-size:17px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:16px}.faq summary::-webkit-details-marker{display:none}.faq summary:after{content:'+';font-size:24px;line-height:1;color:var(--accent)}.faq details[open] summary:after{content:'−'}.faq details p{margin-top:10px;color:var(--muted)}
.cta{background:var(--deep);border-radius:24px;padding:48px;display:flex;gap:32px;align-items:center;justify-content:space-between}.cta h2{color:#fff;font-size:32px}.cta p{color:var(--ondarkm);margin-top:10px;font-size:17px}.cta .ctas{flex:none;margin:0}
.band{background:var(--hl);padding:56px 24px}.band .wrap{display:flex;justify-content:space-between;align-items:center;gap:24px}.band h2,.band p{color:#fff}
.box{background:#fff;border:1px solid var(--border);border-radius:16px;padding:28px}.box.tint{background:var(--tint);border:0}
.answer{background:var(--tint);border-radius:16px;padding:24px 26px;display:flex;flex-direction:column;gap:8px}.answer b{font-family:'Anuphan';font-size:19px;color:var(--deep)}
.tbl{overflow-x:auto;background:#fff;border:1px solid var(--border);border-radius:16px}table{width:100%;border-collapse:collapse;min-width:560px;font-size:15px}caption{text-align:left;padding:18px 20px 4px;font-family:'Anuphan';font-weight:600;font-size:19px;color:var(--deep)}th,td{text-align:left;padding:14px 20px;border-bottom:1px solid #EEF0F6;vertical-align:top}thead th{color:var(--muted);background:var(--page);font-weight:600}tbody tr:last-child th,tbody tr:last-child td{border-bottom:0}tbody th{font-weight:600}td.v{color:var(--primary)}
.note{font-size:13px;color:var(--muted);margin-top:10px}
.prose{max-width:760px;display:flex;flex-direction:column;gap:22px;font-size:18px;line-height:1.85;min-width:0}.prose h2{font-size:30px;margin-top:14px}.prose ul,.prose ol{margin:0;padding-left:24px;display:flex;flex-direction:column;gap:8px}
.split{display:flex;gap:56px;align-items:flex-start}.split>*{min-width:0}.toc{flex:0 0 280px;position:sticky;top:96px;background:var(--page);border-radius:16px;padding:22px;display:flex;flex-direction:column;gap:8px}.toc b{color:var(--deep)}.toc a{text-decoration:none;font-size:15px}
.ph{background:var(--tint);color:var(--primary);border-radius:14px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:14px;padding:12px;min-height:96px}
.banner{position:relative;min-height:520px;display:flex;align-items:center;justify-content:center;text-align:center;padding:40px 24px;background-size:cover;background-position:center}.banner:before{content:'';position:absolute;inset:0;background:rgba(7,13,92,.45)}.banner div{position:relative;color:#fff}.banner b{display:block;font-family:'Anuphan';font-size:44px;line-height:1.2}.banner span{font-size:30px}
.chip{display:inline-flex;padding:6px 14px;border-radius:999px;background:var(--tint);color:var(--primary);font-size:14px;font-weight:600}.chips{display:flex;gap:8px;flex-wrap:wrap}
.fbtn{min-height:44px;padding:0 20px;border-radius:999px;border:1.5px solid var(--border);background:#fff;color:var(--text);font:inherit;font-size:15px;font-weight:600;cursor:pointer}.fbtn[aria-pressed=true]{background:var(--primary);border-color:var(--primary);color:#fff}
.pbtn{min-height:36px;padding:0 14px;border-radius:8px;border:1px solid var(--border);background:#fff;color:var(--muted);font:inherit;font-size:14px;cursor:pointer}.pbtn[aria-pressed=true]{background:var(--tint);border-color:var(--accent);color:var(--primary)}
form.f{display:flex;flex-direction:column;gap:14px}form.f label{display:flex;flex-direction:column;gap:6px;font-size:14px;font-weight:500}form.f input,form.f select,form.f textarea{min-height:46px;border:1px solid #C9CEDF;border-radius:10px;padding:0 12px;font:inherit;font-weight:400;background:#fff}form.f textarea{padding:10px 12px;min-height:110px}
form.f .check{flex-direction:row;align-items:flex-start;gap:10px;font-weight:400;color:var(--muted)}form.f .check input{min-height:auto;width:18px;height:18px;margin-top:5px;flex:none}.fmsg{font-size:14px;color:var(--primary)}
.big{font-family:'Anuphan';font-size:96px;font-weight:700;color:var(--hl);line-height:1}
.stats{display:flex;gap:56px;flex-wrap:wrap}.stat b{display:block;font-family:'Anuphan';font-size:40px;color:var(--accent);line-height:1.2}.stat span{font-size:14px;color:var(--muted)}
.tl{list-style:none;margin:0;padding:0;border-left:3px solid var(--border);display:flex;flex-direction:column;gap:28px}.tl li{padding-left:28px;position:relative}.tl li:before{content:'';position:absolute;left:-10px;top:8px;width:17px;height:17px;border-radius:50%;background:var(--hl);border:3px solid #fff}.tl b{font-family:'Anuphan';font-size:20px;color:var(--deep);display:block}
.job{display:flex;justify-content:space-between;align-items:center;gap:20px;padding:22px 24px}.job+.job{border-top:1px solid var(--border)}.meta{font-size:14px;color:var(--muted)}
.checks{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px}.checks li{display:flex;gap:12px}.checks li:before{content:'';flex:none;width:22px;height:22px;margin-top:3px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%232F45D8' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12l5 5L20 7'/%3E%3C/svg%3E") no-repeat}
footer.ft{background:var(--deep);color:#C9D0F5;padding:64px 24px 28px;font-size:14px}.ft .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:32px}.ft b{color:#fff;font-size:15px;display:block;margin-bottom:10px}.ft a{display:block;color:#C9D0F5;text-decoration:none;margin-bottom:8px}.ft a:hover{color:#fff}.ft img{height:40px;margin-bottom:14px}.ft .bottom{border-top:1px solid #2A3180;margin-top:40px;padding-top:20px;display:flex;justify-content:space-between;gap:12px;font-size:13px}.ft .bottom a{display:inline;margin:0}
/* home */
.hhero{background:linear-gradient(90deg,var(--deep),var(--primary));padding:96px 24px}.hhero .row{display:flex;gap:56px;align-items:center}.hhero h1{color:#fff;font-size:60px;line-height:1.2}.hhero .lead{color:var(--ondarkm)}.hhero .kicker{color:#8FA6FF}.hhero .media{flex:0 0 520px}.hhero img{width:100%;height:440px;object-fit:cover;border-radius:20px;display:block}
.facts{display:flex;gap:10px 28px;flex-wrap:wrap;list-style:none;padding:0;margin:24px 0 0;color:var(--ondarkm);font-size:15px}.facts li{display:flex;gap:8px;align-items:center}.facts li:before{content:'';width:8px;height:8px;border-radius:50%;background:var(--hl)}
.tile{display:flex;flex-direction:column;gap:12px;text-decoration:none;color:#fff}.tile img{width:100%;height:160px;object-fit:cover;border-radius:16px;display:block}.tile span{font-family:'Anuphan';font-weight:600;font-size:20px}.tile:hover span{text-decoration:underline}
.harmony .wrap{display:flex;flex-direction:column;gap:14px}.harmony h2{color:var(--deep);font-size:34px;max-width:900px}
@media (max-width:1100px){.nav,.hdr .btn-p{display:none}.burger{display:block}.dd,.dd.mega{display:none!important}
 .drawer{position:fixed;inset:0;background:#fff;z-index:90;overflow-y:auto;padding:0 20px 32px}body.menu-open .drawer{display:block}body.menu-open{overflow:hidden}
 .drawer .top{display:flex;justify-content:space-between;align-items:center;min-height:64px;border-bottom:1px solid var(--border);margin:0 -20px 16px;padding:0 20px}.drawer .top img{height:32px}
 .drawer details,.drawer>a.m{display:block;border-radius:12px}.drawer summary,.drawer>a.m{list-style:none;display:flex;justify-content:space-between;align-items:center;min-height:56px;padding:0 12px 0 16px;font-family:'Anuphan';font-weight:600;font-size:18px;color:var(--text);text-decoration:none;cursor:pointer}
 .drawer summary::-webkit-details-marker{display:none}.drawer summary:after{content:'';width:10px;height:10px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg);margin-top:-4px;transition:transform .2s}.drawer details[open] summary{color:var(--primary)}.drawer details[open] summary:after{transform:rotate(-135deg);margin-top:4px}
 .drawer summary:active,.drawer>a.m:active{background:var(--tint);box-shadow:inset 4px 0 0 var(--hl)}
 .drawer .sub{background:var(--page);border-radius:12px;padding:8px;margin:0 0 8px 12px;display:flex;flex-direction:column}.drawer .sub a{padding:10px 14px;border-radius:10px;text-decoration:none;color:var(--text);font-weight:600}.drawer .sub a:active{background:var(--tint);color:var(--accent)}
 .drawer .foot{background:var(--page);margin:16px -20px 0;padding:20px;display:flex;flex-direction:column;gap:14px}}
@media (max-width:900px){.hero .row,.hhero .row,.split,.cta,.band .wrap,.shead.row{flex-direction:column;align-items:stretch;gap:28px}.hero .media,.hhero .media{flex:none;order:-1}.g3,.g4,.g5{grid-template-columns:repeat(2,minmax(0,1fr))}.steps,.steps.s4{grid-template-columns:1fr 1fr}.toc{position:static;flex:none}.ft .cols{grid-template-columns:1fr 1fr}}
@media (max-width:640px){body{font-size:15px}h1,.hhero h1{font-size:34px}h2,.harmony h2{font-size:26px}h3{font-size:19px}.lead,.shead p{font-size:16px}
 .topbar{display:none}.hdr{padding:0 20px}.hdr>.wrap{min-height:60px}.hdr .logo img{height:32px}
 .hero{padding:24px 20px 48px}.hhero{padding:32px 20px 56px}.hero .media img{height:220px}.hhero img{height:240px}
 .sec{padding:56px 20px}.band{padding:44px 20px}.g2,.g3,.g4,.g5,.steps,.steps.s4{grid-template-columns:1fr}.steps li{flex-direction:row;gap:16px}.steps li:before{width:44px;height:44px;font-size:18px}
 .cta{padding:28px}.cta h2{font-size:24px}.prose{font-size:16px}.prose h2{font-size:24px}.big{font-size:56px}.banner{min-height:260px}.banner b{font-size:24px}.banner span{font-size:17px}
 .ctas .btn,.cta .btn{width:100%}.job{flex-direction:column;align-items:flex-start}.stats{gap:24px}.stat b{font-size:28px}
 footer.ft{padding:40px 20px 24px}.ft .cols{grid-template-columns:1fr}.ft .cols>div+div{display:none}.ft .bottom{flex-direction:column}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
'''
CHEV='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
def ico(p): return f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#0A149A" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
I={'lab':ico('<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.7 3h10.6a2 2 0 0 0 1.7-3l-5-9V3M7 15h10"/>'),'people':ico('<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.2A5 5 0 0 1 21 19"/>'),
'chat':ico('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>'),'leaf':ico('<path d="M5 19c0-8 5-14 15-15-1 10-7 15-15 15z"/><path d="M5 19l8-8"/>'),
'shield':ico('<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>'),'heart':ico('<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>'),
'globe':ico('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>'),'doc':ico('<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 13h6M9 17h6"/>')}
ORG={"@context":"https://schema.org","@type":"Organization","name":"Unique Polymer Co., Ltd.","alternateName":"บริษัท ยูนิค โพลีเมอร์ จำกัด","url":SITE,"logo":SITE+"/images/logo-color.svg","foundingDate":"2016-08-05","telephone":"+66-2-116-3138","address":{"@type":"PostalAddress","streetAddress":"282 หมู่ 2 ต.แพรกษาใหม่","addressLocality":"เมืองสมุทรปราการ","addressRegion":"สมุทรปราการ","postalCode":"10280","addressCountry":"TH"},"knowsAbout":["Masterbatch","Plastic compound","Bioplastics","Compostable compounds","Biomass compounds"]}
URLS=[]
def esc(s): return html.escape(s,quote=True)
