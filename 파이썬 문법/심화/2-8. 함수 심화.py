# 함수에 인수를 넣을 때, 어떤 매개변수에 어떤 값을 넣을지 정해줄 수 있다. 순서 상관 없음!
def cal(a, b):
    return a + 2 * b

print(cal(3, 5))
print(cal(5, 3))
print(cal(a=3, b=5))
print(cal(b=5, a=3))


# 특정 매개변수에 디폴트 값을 지정해줄 수 있다.
def cal2(a, b=3):
    return a + 2 * b

print(cal2(4))
print(cal2(4, 2))
print(cal2(a=6))
print(cal2(a=1, b=7))

# 입력값의 개수를 지정하지 않고 모두 받는 방법!

def call_names(*args):
    for name in args:
        print(f"{name}야 밥 먹어라~")
        
call_names("철수", "영희", "희재")

def get_kwargs(**kwargs):
    print(kwargs)

get_kwargs(name='bob')
get_kwargs(name='john', age='27')

