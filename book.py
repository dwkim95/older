# -*- coding: utf-8 -*-
import requests
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime 

url = 'https://www.hello-senior.or.kr/bbs/board.php?bo_table=0502'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select(
    'td.td_subject > div.subj-content > a'
    )

data = {}

for title in titles:
    data[title.text] = title.get('href')
    print(title.text)
    print(title['href'])
    
    

    #주소
url = 'https://notify-api.line.me/api/notify'

token = {'Authorization' : 'Bearer gsobfOu4LyjDTCeDrAyYHqDOvBXoSw62MjYWcaCVbzH'}

message = []
i = 1
for title in titles:
    if i == 6:
        break
    inner=[]
    inner.append('\n\n'+title.text.strip()) 
    inner.append('\n'+title['href']) #[title,link]
    message.append(inner)
    i += 1
    # print(title['title'])
parameter = {"message": message}
#응답
response = requests.post(
    url, headers= token, data = parameter)

print(response.text)
