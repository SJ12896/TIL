# 가장 최근에 메시지를 보낸 사용자에게
# 안녕하세요 라고 보내기

# 1.요청에 필요한 라이브러리 import
import requests, pprint

# 2.요청 url과 token 확인
token = ''
api_url = f'https://api.telegram.org/bot{token}'

# 3.메시지 보낸 사용자의 id값 찾기
chat_id_url = f'{api_url}/getUpdates'
response = requests.get(chat_id_url).json()

print(chat_id)

# 4.chat id에게 메세지 보내기
text = input('메세지를 입력하세요: ')
message_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)