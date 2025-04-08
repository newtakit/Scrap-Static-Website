## Scrap-Static-Website

## Scrape ข้อมูลลูกค้าจากหน้าเว็บ
เราจะเขียน Python Script เพื่อดึงข้อมูลจากหน้าเว็บบริษัท(CAF) และนำข้อมูลไปเก็บใส่ Google Sheets เพื่อใช้เป็น Data Source ในการทำ Dashboard
![1](1.jpg)
## flowchart

## Tools

1. Python (ในตัวอย่างจะใช้ Version 3.13.1 / ระบบปฏิบัติการ windows 11)
2. Library ที่ต้องลงเพิ่ม
    1. requests
    2. Pandas
    3. BeautifulSoup4
3. Visual Studio Code

## Process

1. ใช้ requests เพื่อ login หน้าเว็บ สำหรับพนักงานของ(CAF)
2. ใช้ BeautifulSoup4 อ่าน HTML จากหน้าเว็บ (CAF)
3. ใช้ Pandas สร้างตาราง จาก HTML
4. นำข้อมูลใส่ CSV
