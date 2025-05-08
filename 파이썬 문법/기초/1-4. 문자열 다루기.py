a = "aa"
b = 'aa' # 작은 따옴표 큰 따옴표 둘 다 같다
# 따옴표로 감싸지 않으면 변수명을 뜻하기 떄문에 꼭 구분해서 써야 한다

print("I'm happy :)")

# 문자열 연산
first_name = "Harry"
last_name = "Potter"

first_name + last_name # HarryPotter 
first_name + " " + last_name # Harry Potter

a = "3"
b = "5"
a + b # 35
# 문자열과 정수를 더하면 에러가 난다
# 문자열의 길이는 len() 함수를 써서 구할 수 있다.

print(len("abcde")) # 5
print(len("Hello, Sparta!")) # 14
print(len("안녕하세요.")) # 6

# 모든 알파벳을 대문자/소문자로 바꾸기
sentence = 'Python is FUN!'

sentence.upper() # PYTHON IS FUN
sentence.lower() # python is fun

# 특정 문자를 기준으로 문자열 나누기
myemail = 'test@gmail.com'

result = myemail.split('@') # ['test','gmail.com] 리스트 자료형으로 저장

print(result[0]) # test
print(result[1]) # gmail.com

result2 = result[1].split('.') # ['gmail', 'com']

print(result2[0]) # > 우리가 알고 싶었던 것 
print(result2[1]) # com

print(myemail.split('@')[1].split('.')[0])

# 특정 문자를 다른 문자로 바꾸기
txt = '서울시-마포구-망원동'
print(txt.replace('-','>')) # 서울시>마포구>망원동

# 인덱싱과 슬라이싱 0부터 n미만까지 출력
f = 'abcdefghijklmnopqrstuvwxyz'
f[1] # b

print(f[4:15])
print(f[8:])
print(f[:7])
print(f[:])
print(len(f))

# 특정 문자열로 자르고 싶을 때
myemail = 'abc@sparta.co'

domain = myemail.split('@')[1].split('.')[0]
print(domain)

# 문자열의 앞의 반만 출력하기
text = 'sparta'
print(text[:3])

# 전화번호의 지역번호 출력하기
phone = "02-123-1234"
print(phone.split('-')[0])
