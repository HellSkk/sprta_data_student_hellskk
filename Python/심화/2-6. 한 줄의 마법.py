num = 3

if num % 2 == 0:
    result = "짝수"
else:
    result = "홀수"

print(f"{num}은 {result}입니다.")

# 삼항 연산자 조건식

num = 3
result = "짝수" if num % 2 == 0 else "홀수"
print(f"{num}은 {result}입니다.")

# 참일때 값 if 조건 else 거짓일 때 값

a_list  = [1, 3, 2, 5, 1, 2]

# a_list의 각 요소에 2를 곱한 새로운 리스트를 만들고 싶다면?

b_list = []
for a in a_list:
    b_list.append(a*2)

print(b_list)

# 한 번에 쓰는 방법

b_list = [a*2 for a in a_list]