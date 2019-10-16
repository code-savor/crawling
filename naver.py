import requests
from bs4 import BeautifulSoup
from pushbullet import Pushbullet

html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')

message = ""
pb = Pushbullet("o.xDt16QpNSjqs8WpuO4FydlVleSdwA45w")
# print(soup.prettify())

title_list = soup.select('.ah_list .ah_k')


# title_list = []
# for realtime in soup.find(class_='ah_list').find_all('li'):
#     tg2 = realtime.find(class_='ah_k')
#     title_list.append(tg2.text)

for i, t in enumerate(title_list,1):
    txt = (f'{i}위 {t.get_text()}')
    message += txt + "\n"

push = pb.push_note("[Naver 실시간 검색어]", "\n" + message)
