a = 3
print(a)
b = a
print(b)
a = 5
print(a, b)

# 숫자형 자료형
a = 5
b = 4.8
# 사칙연산
a = 7
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a+3*b)
print((a+3)*b)

# 변수에 저장된 값 연산 후 같은 값을 변수에 저장 가능
a = 5
a = a+3
print(a)
a += 3 # 같은 의미

a // b # 3 몫
a % b # 1 나머지
a ** b # 거듭제곱

# Bool 자료형
x = True
y = False

# 소문자로 쓰면 자료형이라고 인식하지 않고 변수명이라 생각해 에러가 난다.
# True/False는 변수명으로 쓸 수 없다.

a = 4 > 2 # True   NOT 연산자로 참을 거짓으로, 거짓을 참으로 바꿔준다.
not a     # False
a and b   # False  AND 연산자로 모두 참이어야 참을 반환한다
a or b    # True   OR 연산자로 둘 중 하나만 참이면 참이다

# 숫자들의 평균 구하기
a = 24
b = 16
c = 26
print((a+b+c)/3)
