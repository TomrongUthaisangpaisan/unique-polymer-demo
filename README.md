# เว็บไซต์ Unique Polymer (static)

เว็บไซต์ 40 หน้า สร้างจากดีไซน์ Figma "Unique Polymer – Website Redesign"
ไม่ต้อง build ใช้ไฟล์ HTML ในโฟลเดอร์นี้ได้เลย

## Deploy ขึ้น Vercel (ผ่าน GitHub)
1. สร้าง repository ใหม่ใน github.com (Public หรือ Private ก็ได้)
2. กด "uploading an existing file" แล้วลากไฟล์และโฟลเดอร์ทั้งหมดในโฟลเดอร์นี้เข้าไป กด Commit
3. เข้า vercel.com > Add New > Project > Import repository ที่สร้าง
4. Framework Preset: **Other** ไม่ต้องใส่ Build Command ปล่อย Output Directory ว่าง แล้วกด Deploy

## Deploy ด้วย Vercel CLI (ทางเลือก)
ติดตั้ง Node.js แล้วรันในโฟลเดอร์นี้: `npx vercel` จากนั้น `npx vercel --prod`

## สิ่งที่ต้องตั้งค่าหลัง deploy
- **โดเมน**: แก้ค่า `SITE` ใน `_source/core.py` เป็นโดเมนจริง แล้วรัน `python3 _source/build.py` (แก้ path OUT ในไฟล์ก่อน) หรือค้นหาและแทนที่ `https://unique-polymer.vercel.app` ในทุกไฟล์ (ใช้ใน canonical, sitemap.xml, robots.txt, schema)
- **ฟอร์มติดต่อ**: ใส่ URL บริการรับฟอร์ม (เช่น Formspree) ในตัวแปร `FORM_ENDPOINT` ที่ `assets/site.js` ถ้ายังไม่ใส่ ฟอร์มจะแจ้งให้โทรแทน
- **ข้อความใน [ ]** เป็นข้อมูลที่ต้องเติม/ยืนยันก่อนเปิดใช้จริง

## ฟอนต์
Anuphan และ IBM Plex Sans Thai Looped (SIL Open Font License) เก็บไว้ใน `fonts/` พร้อมไฟล์ OFL
