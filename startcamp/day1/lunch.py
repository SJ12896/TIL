menu = ['예향정',  '장가계', '첨단공원국밥']
# print(menu)
# print(menu[0], menu[-1])
phone_book = {'예향정' : '123-123', '첨단공원국밥' : '456-456', '장가계' : '789-789'}
# print(phone_book)
# print(phone_book['첨단공원국밥'])

import random
print(f'{phone_book[random.choice(menu)]} 의 전화번호는 {123}')