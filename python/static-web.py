import requests
from bs4 import BeautifulSoup
import pandas as pd


login = 'YOUR-URL'
session = requests.Session()
login_data = {
    'username': '*****',
    'password': '******'
}


session.post(login_url, data=login_data)
url = 'YOUR-URL'
req = session.get(target_url)

soup = BeautifulSoup(response.content, 'html.parser')

syntax = soup.find_all('tr')
data = []

for row in syntax:
    a = row.find_all('td')
    if len(a) >= 6:
        data.append({
            'ลำดับ': a[0].text.strip(),
            'AC': a[1].text.strip(),
            'ชื่อ': a[2].text.strip(),
            'วันที่': a[3].text.strip(),
            'ประเภทบัญชี': a[4].text.strip(),
            'ตัวแทน': a[5].text.strip()
        })

# สร้าง DataFrame จาก list ของข้อมูล
df = pd.DataFrame(data)
df.to_csv('รายชื่อลูกค้า1.csv', index = False , encoding='utf-8-sig')



# แสดงข้อมูลที่เรียงแล้ว
print(df)