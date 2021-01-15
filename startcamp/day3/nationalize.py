import requests

name = input()
url = f'https://api.nationalize.io?name={name}'

response = requests.get(url).json()

name = response['name']
country = response['country'][0]['country_id']
percent = response['country'][0]['probability'] * 100

print(f'{name}의 국적은 {percent}%의 확률로 {country}입니다.')