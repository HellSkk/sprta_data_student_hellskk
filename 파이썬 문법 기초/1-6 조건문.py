# if 문은 조건을 만족했을 때만 특정 코드를 실행하도록 하는 문법
# 파이썬에서는 어디까지 구문에 포함되는지 들여쓰기로 구분해서 아주 중요!
money = 5000
if money > 3800: # 조건에는 불 자료형이 들어간다.
    print("택시 타자!")
    

money = 2000
if money > 3800:
    print("택시 타자!")
else:
    print("걸어가자...")
    
# 다양한 조건 판단 시 elif 사용하기
age = 27
if age < 20:
    print("청소년입니다.")
elif age < 65:
    print("성인입니다.")
else:
    print("무료로 이용하세요!")
    
