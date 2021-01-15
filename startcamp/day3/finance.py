

import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
#.text는 데이터를 꺼내는 느낌
#.json()은 메서드(기능)을 실행시킨다.

soup = BeautifulSoup(response, 'html.parser')

finance = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").text

print(f'현재 원/달러 환율은 {finance}입니다.')