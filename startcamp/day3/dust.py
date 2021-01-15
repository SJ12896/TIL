#공공 데이터 API 활용 실습 (대기오염정보)

#1.필요한 라이브러리 import 하기
import requests

#2.API URL 및 KEY값 확인
key = 'zYaelgQeew4XgNetZuLoGTloPw8XviyEZAxuHkuBefyY07iEvturRS9gNNJE5Bl7pwIfUFAgDBI6%2FKGfj%2BGMaw%3D%3D'
name = "광주"
dong = "노대동"
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={name}&ver=1.0'

#3.요청 및 응답값 확인
response = requests.get(url).json()

for i in range(len(response['response']['body']['items'])):
    if response['response']['body']['items'][i]['stationName'] == dong:
        pmValue = response['response']['body']['items'][i]['pm10Value']

#4.최종 출력 문자열
text = f'{name} {dong}의 미세먼지 농도는 {pmValue}입니다.'

# 5.텔레그램 메시지 전송(sendMessage)
token = ''
api_url = f'https://api.telegram.org/bot{token}'

# 3.메시지 보낸 사용자의 id값 찾기
chat_id_url = f'{api_url}/getUpdates'
response = requests.get(chat_id_url).json()


# 4.chat id에게 메세지 보내기
message_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)

