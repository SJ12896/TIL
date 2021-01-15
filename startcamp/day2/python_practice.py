# ctrl shift p : 명령어 알려줌
#1.기초 자료형
number = 3
print(type(number))

string = '문자열'
print(type(string))

boolean = True
print(type(boolean))

string_number = '3'
print(int(string_number) + 3)

#2. f-string
name = '김창규'
print(f'제 이름은 {name} 입니다.')

#3.list
my_list = ['python', 'html', 'markdown']
print(my_list[2])
my_list[2] = 'java'
print(my_list[2])

#4.dictionary
#딕셔너리 선언
age_dict = {
    '박소현' : 25,
    '김지용' : 83,
}
#끝나기 전에 trailing comma 찍어주기. 에러 안 발생함. 
#딕셔너리 요소 접근
print(age_dict['김지용'])
print(age_dict.get('김지용'))
age_dict['김지용'] = 103
