import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())


title_list = []
for realtime in soup.find(class_='ah_list').find_all('li'):
    tg2 = realtime.find(class_='ah_k')
    title_list.append(tg2.text)

for i, t in enumerate(title_list,1):
    print("{}{} {}".format(i,"위",t))
