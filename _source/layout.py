from core import *
from data import *
NAV=[('products','ผลิตภัณฑ์','/products/'),('solutions','โซลูชันตามอุตสาหกรรม','/applications/'),('services','บริการเทคนิค','/technical-services/'),('sustainability','ความยั่งยืน','/sustainability/'),('articles','บทความ','/article/'),('about','เกี่ยวกับเรา','/about/our-story/')]
SUB={'solutions':[(i['th'],i['url'],i['d']) for i in IND],
 'services':[('ร่วมพัฒนาสูตร','/technical-services/co-development/','ออกสูตรเฉพาะให้สินค้าของคุณ'),('ปรึกษาด้านเทคนิค','/technical-services/technical-consulting/','วิศวกรช่วยแก้ปัญหาหน้างาน'),('ห้องแล็บและการทดสอบ','/technical-services/lab-testing/','วิธีและเครื่องมือทดสอบ')],
 'sustainability':[('ความยั่งยืน','/sustainability/','แนวทางเพื่อโลกและผู้คน'),('คู่มือพลาสติกชีวภาพ','/sustainability/bioplastics-guide/','เข้าใจก่อนเลือกใช้'),('การรับรองมาตรฐาน','/sustainability/certifications/','เอกสารรับรองและดาวน์โหลด')],
 'articles':[('บทความทั้งหมด','/article/',''),('คู่มือเทคนิค','/article/guides/',''),('ข่าวสาร','/article/news/',''),('กิจกรรม','/article/events/','')],
 'about':[('เรื่องราวของเรา','/about/our-story/',''),('คุณภาพและมาตรฐาน','/about/quality/',''),('ค่านิยม Harmony','/about/harmony/',''),('คำถามที่พบบ่อย','/faq/',''),('ร่วมงานกับเรา','/careers/',''),('ติดต่อเรา','/contact/','')]}
def mega():
    poly=''.join(f'<a href="{p["url"]}">{p["th"]}<small>{p["en"]}</small></a>' for p in PRODUCTS if p['g']=='polyolefins')
    bio=''.join(f'<a href="{p["url"]}">{p["th"]}<small>{p["en"]}</small></a>' for p in PRODUCTS if p['g']=='bioplastics')
    return f'<div class="dd mega"><div><p class="gl">พอลิโอเลฟินส์ (Polyolefins)</p><div class="two">{poly}</div></div><div><p class="gl">พลาสติกชีวภาพ (Bioplastics)</p>{bio}</div><div class="feat"><b>ไม่แน่ใจว่าต้องใช้ตัวไหน</b><p>เล่าปัญหาหน้างานให้วิศวกรเราฟัง แล้วเราจะแนะนำสูตรที่เหมาะให้</p><a class="btn btn-p" href="/contact/">นัดปรึกษาวิศวกร</a><a href="/products/" style="color:#fff;font-weight:600">ดูผลิตภัณฑ์ทั้งหมด</a></div></div>'
def header(active):
    items=''
    for k,l,h in NAV:
        dd=mega() if k=='products' else '<div class="dd">'+''.join(f'<a href="{u}">{t}{"<small>"+d+"</small>" if d else ""}</a>' for t,u,d in SUB[k])+'</div>'
        items+=f'<div class="ni"><a href="{h}" class="{"on" if k==active else ""}"{" aria-current=page" if k==active else ""}>{l}{CHEV}</a>{dd}</div>'
    drawer=''
    for k,l,h in NAV:
        subs=[('ผลิตภัณฑ์ทั้งหมด','/products/','')]+[(p['th'],p['url'],'') for p in PRODUCTS] if k=='products' else SUB[k]
        drawer+=f'<details{" open" if k==active else ""}><summary>{l}</summary><div class="sub">'+''.join(f'<a href="{u}">{t}</a>' for t,u,d in subs)+'</div></details>'
    return f'''<a class="skip" href="#main">ข้ามไปเนื้อหาหลัก</a><div class="topbar"><div class="wrap"><div><span>282 หมู่ 2 ต.แพรกษาใหม่ อ.เมืองสมุทรปราการ</span><span>โทร <a href="tel:+6621163138" style="color:#C9D0F5">02-116-3138 ต่อ 272</a></span></div><div><b style="color:#fff">TH</b> | EN</div></div></div>
<header class="hdr"><div class="wrap"><a class="logo" href="/" aria-label="Unique Polymer หน้าแรก"><img src="/images/logo-color.svg" alt="Unique Polymer" width="159" height="40"></a><nav class="nav" aria-label="เมนูหลัก">{items}</nav><a class="btn btn-p" href="/contact/">นัดปรึกษาวิศวกร</a>
<button class="burger" aria-label="เปิดเมนู" aria-expanded="false" data-menu><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#231F20" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button></div></header>
<div class="drawer" role="dialog" aria-label="เมนู"><div class="top"><img src="/images/logo-color.svg" alt="Unique Polymer"><button class="burger" style="display:block" aria-label="ปิดเมนู" data-menu><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#231F20" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>{drawer}<a class="m" href="/faq/">คำถามที่พบบ่อย</a><a class="m" href="/contact/">ติดต่อเรา</a><div class="foot"><a class="btn btn-p" href="/contact/">นัดปรึกษาวิศวกร</a><a href="tel:+6621163138" style="font-weight:600;color:var(--primary)">โทร 02-116-3138 ต่อ 272</a></div></div>'''
FOOT='''<footer class="ft"><div class="wrap"><div class="cols"><div><img src="/images/logo-white.svg" alt="Unique Polymer" width="159" height="40"><p>บริษัท ยูนิค โพลีเมอร์ จำกัด<br>282 หมู่ 2 ต.แพรกษาใหม่ อ.เมืองสมุทรปราการ จ.สมุทรปราการ 10280<br>โทร 02-116-3138 ต่อ 272</p></div>
<div><b>ผลิตภัณฑ์</b><a href="/products/polyolefins/">พอลิโอเลฟินส์</a><a href="/products/bioplastics/">พลาสติกชีวภาพ BIONEX</a><a href="/applications/">โซลูชันตามอุตสาหกรรม</a></div>
<div><b>บริการเทคนิค</b><a href="/technical-services/co-development/">ร่วมพัฒนาสูตร</a><a href="/technical-services/technical-consulting/">ปรึกษาด้านเทคนิค</a><a href="/technical-services/lab-testing/">ห้องแล็บและการทดสอบ</a></div>
<div><b>บริษัท</b><a href="/about/our-story/">เกี่ยวกับเรา</a><a href="/article/">บทความและข่าวสาร</a><a href="/faq/">คำถามที่พบบ่อย</a><a href="/careers/">ร่วมงานกับเรา</a><a href="/contact/">ติดต่อเรา</a></div></div>
<div class="bottom"><span>© 2026 Unique Polymer Co., Ltd.</span><span>Commit for the Planet, the People and Future Generations | <a href="/privacy-policy/">นโยบายความเป็นส่วนตัว</a></span></div></div></footer>'''
def page(url,title,desc,active,body,crumbs=None,schema=None,img='/images/commit-hands.jpg'):
    URLS.append(url)
    ld=[ORG]
    if crumbs:
        items=[{"@type":"ListItem","position":1,"name":"หน้าแรก","item":SITE+"/"}]+[{"@type":"ListItem","position":i+2,"name":n,"item":SITE+(u or url)} for i,(n,u) in enumerate(crumbs)]
        ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items})
    if schema: ld+=schema if isinstance(schema,list) else [schema]
    full=title if url=='/' else f'{title} | Unique Polymer'
    lds=''.join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in ld)
    doc=f'''<!doctype html><html lang="th"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(full)}</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{SITE}{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(full)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{SITE}{url}"><meta property="og:image" content="{SITE}{img}"><meta property="og:locale" content="th_TH"><meta name="theme-color" content="#070D5C">
<link rel="icon" href="/images/favicon.svg" type="image/svg+xml"><link rel="preload" href="/fonts/anuphan-var.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/plex-looped-400.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/site.css">{lds}</head>
<body>{header(active)}<main id="main">{body}</main>{FOOT}<script src="/assets/site.js" defer></script></body></html>'''
    d=OUT+url; os.makedirs(d,exist_ok=True); open(d+'index.html','w').write(doc)
def crumb(items):
    return '<ol class="crumb" aria-label="breadcrumb"><li><a href="/">หน้าแรก</a></li>'+''.join(f'<li><a href="{u}">{n}</a></li>' if u else f'<li aria-current="page">{n}</li>' for n,u in items)+'</ol>'
def hero(cr,title,lead,kicker='',ctas=(),img=None,alt=''):
    c=''.join(f'<a class="btn {cls}" href="{h}">{l}</a>' for l,cls,h in ctas)
    media=f'<div class="media"><img src="/images/{img}.jpg" alt="{alt}" width="520" height="400"></div>' if img else ''
    k=f'<span class="kicker">{kicker}</span>' if kicker else ''
    return f'<section class="hero"><div class="wrap">{crumb(cr)}<div class="row"><div class="txt">{k}<h1>{title}</h1><p class="lead">{lead}</p>{"<div class=ctas>"+c+"</div>" if c else ""}</div>{media}</div></div></section>'
def sec(title,intro,inner,bg='',sid='',h='h2'):
    hd=f'<div class="shead"><{h}>{title}</{h}>{"<p>"+intro+"</p>" if intro else ""}</div>' if title else ''
    return f'<section class="sec {bg}"{" id="+sid if sid else ""}><div class="wrap">{hd}{inner}</div></section>'
def card(t,d,img=None,lab='',href=None,more='',icon=None,en='',soon=False,alt=''):
    im=f'<img src="/images/{img}.jpg" alt="{alt}" loading="lazy" width="400" height="190">' if img else ''
    ic=f'<div class="ico">{I[icon]}</div>' if icon else ''
    tag='a' if href else 'div'; hr=f' href="{href}"' if href else ''
    return f'<{tag} class="card"{hr}>{im}<div class="in">{ic}{"<span class=lab>"+lab+"</span>" if lab else ""}<h3>{t}</h3>{"<span class=en>"+en+"</span>" if en else ""}<p>{d}</p>{"<span class=soon>เร็วๆ นี้</span>" if soon else ""}{"<span class=more>"+more+"</span>" if more else ""}</div></{tag}>'
def grid(cards,n=3): return f'<div class="grid g{n}">'+''.join(cards)+'</div>'
def steps(items,cls=''): return f'<ol class="steps {cls}">'+''.join(f'<li><div><h3>{x[0]}</h3><p>{x[1]}</p>{"<small>"+x[2]+"</small>" if len(x)>2 else ""}</div></li>' for x in items)+'</ol>'
def faq(items): return '<div class="faq">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)+'</div>'
def faq_schema(items): return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items if '[' not in a]}
def cta(t,d,btns=(('นัดปรึกษาวิศวกร','btn-p','/contact/'),)):
    b=''.join(f'<a class="btn {c}" href="{h}">{l}</a>' for l,c,h in btns)
    return f'<section class="sec"><div class="wrap"><div class="cta"><div><h2>{t}</h2><p>{d}</p></div><div class="ctas">{b}</div></div></div></section>'
def table(head,rows,caption=''):
    cap=f'<caption>{caption}</caption>' if caption else ''
    return f'<div class="tbl"><table>{cap}<thead><tr>'+''.join(f'<th scope="col">{h}</th>' for h in head)+'</tr></thead><tbody>'+''.join('<tr><th scope="row">'+r[0]+'</th>'+''.join(f'<td>{c}</td>' for c in r[1:])+'</tr>' for r in rows)+'</tbody></table></div>'
def form(title,topic='ขอตัวอย่างสินค้า',note='ทีมเทคนิคจะติดต่อกลับเพื่อสอบถามรายละเอียดงาน'):
    opts=''.join(f'<option{" selected" if o==topic else ""}>{o}</option>' for o in ['ขอตัวอย่างสินค้า','ปรึกษาด้านเทคนิค','สอบถามราคา','อื่นๆ'])
    return f'''<form class="f box" data-form><h2 style="font-size:26px">{title}</h2><p class="meta">{note}</p><label>หัวข้อ<select name="topic">{opts}</select></label><label>ชื่อผู้ติดต่อ<input name="name" autocomplete="name" required></label><label>บริษัท<input name="company" autocomplete="organization"></label><label>อีเมล<input type="email" name="email" autocomplete="email" required></label><label>เบอร์โทร<input type="tel" name="phone" autocomplete="tel"></label><label>รายละเอียด (ชนิดงาน เครื่องจักร ปัญหาที่พบ)<textarea name="message"></textarea></label>
<label class="check"><input type="checkbox" name="consent" required><span>ยินยอมให้บริษัทเก็บและใช้ข้อมูลเพื่อติดต่อกลับ ตาม<a href="/privacy-policy/">นโยบายความเป็นส่วนตัว</a></span></label><button class="btn btn-n" type="submit">ส่งข้อความ</button><p class="fmsg" role="status" aria-live="polite"></p></form>'''
