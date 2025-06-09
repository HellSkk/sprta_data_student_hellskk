# 반복적으로 사용하는 코드들에 이름을 붙여놓은 것

def hello():
    print("안녕!")
    print("또 만나요!")
    
hello()
hello()

def bus_rate(age):
    if age > 65:
        print("무료로 이용하세요")
    elif age > 20:
        print("성인입니다.")
    else:
        print("청소년입니다.")
        
bus_rate(27)
bus_rate(10)
bus_rate(72)

# 결과값을 돌려주도록 함수를 만들 수도 있다!
def bus_fee(age):
    if age > 65:
        return 0
    elif age > 20:
        return 1200
    else:
        return 0
    
money = bus_fee(28)
print(money)

# Q. 주민등록번호를 입력받아 성별을 출력하는 함수 만들기

def check_gender(pin):
    gender_pin_num = pin.split('-')[1][0]
    if int(gender_pin_num) % 2 == 0:
        print("여성")
    else:
        print("남성")

my_pin = '200101-3012345'
check_gender(my_pin)