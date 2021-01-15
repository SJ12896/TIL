#공공 데이터 API 활용 실습 (대기오염정보)

#1.필요한 라이브러리 import 하기
import requests

#2.API URL 및 KEY값 확인
key = 'zYaelgQeew4XgNetZuLoGTloPw8XviyEZAxuHkuBefyY07iEvturRS9gNNJE5Bl7pwIfUFAgDBI6%2FKGfj%2BGMaw%3D%3D'
name, dong = input().split()
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={name}&ver=1.0'

#3.요청 및 응답값 확인
response = requests.get(url).json()

for i in range(len(response['response']['body']['items'])):
    if response['response']['body']['items'][i]['stationName'] == dong:
        pmValue = response['response']['body']['items'][i]['pm10Value']

#4.최종 출력 문자열
print(f'{name} {dong}의 미세먼지 농도는 {pmValue}입니다.')
